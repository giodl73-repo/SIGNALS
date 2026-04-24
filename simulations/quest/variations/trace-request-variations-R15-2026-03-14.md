All 5 saved to `simulations/quest/golden/`. Here is the full output:

---

## V-01 — Single axis: Role sequence (Storage-first)

**Axis:** Role execution order — Storage/data-layer expert runs BEFORE Auth expert, which runs BEFORE Routing/API expert (default order is Auth → Routing → Storage).

**Hypothesis:** Starting with data-access patterns surfaces I/O latency and cascade failure points before auth constraints are applied, producing a failure catalog ordered by blast radius rather than by entry sequence.

---

You are executing a `trace-request` signal for the following scenario. Auto-select the appropriate platform expert role from context: Dataverse / Commerce / Automate. For this trace, roles execute in Storage-first order: the Storage/data-layer expert speaks first, followed by the Auth expert, followed by the Routing/API expert.

**Scenario:** POST /api/data/v9.2/accounts — Create Account with `parentaccountid` referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on `parentaccountid`.

**Platform Expert Selected:** Dataverse platform expert (primary). Storage/data-layer sub-expert speaks first in each step where role ordering applies.

---

### Step 1 — Scenario Registration

Record the scenario under trace:

- **Operation:** POST /api/data/v9.2/accounts
- **Payload key field:** `parentaccountid` (GUID reference to existing account)
- **Plug-in pipeline:** PreValidation → PreOperation → PostOperation (all synchronous)
- **Security overlay:** Field-level security (FLS) on `parentaccountid`
- **Trace goal:** Hand-compile every boundary crossing, failure point, latency source, and auth gap from entry to response.

---

### Step 2 — Role Execution Order Declaration

This trace uses Storage-first role ordering. Declare the sequence:

1. **Storage/data-layer expert** — speaks first: surfaces data-access patterns, cascade dependencies, I/O latency, and storage failure blast radius before auth constraints are considered.
2. **Auth expert** — speaks second: applies auth constraints on top of the storage-layer findings, identifies auth gaps at each boundary.
3. **Routing/API expert** — speaks third: validates routing and API-layer concerns, confirms entry-point handling.

All three perspectives must be present. Storage expert's findings take precedence in failure severity ordering.

---

### Step 3 — Authentication Contract

Before tracing any boundary, establish the full auth contract. This is the reference set for Step 8 verification.

List every scope string, token type, and permission required for this operation to succeed end-to-end:

| Boundary | Required Scope / Permission | Token Type | Notes |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | Delegated or app-only |
| Plugin execution context | Caller's system user privileges propagated | Internal system token | No separate scope; inherits caller |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | System user record | Checked against field security profile |
| SQL storage layer (Dataverse DB) | `internal service identity` | Internal (no OAuth) | Service-to-service, no caller token |
| Relationship validation (parent GUID lookup) | `prvReadAccount` | Bearer (AAD) / system user | Must have `prvReadAccount` |

**Auth contract is now locked.** Step 8 will verify that every invoked scope matches exactly what is declared here.

---

### Step 4 — Entry Point (Storage Expert Speaks First)

**Storage expert:** The entry point for this operation is the Dataverse OData v4 endpoint at `/api/data/v9.2/accounts`. From the storage perspective, this POST will ultimately resolve to an INSERT into the `AccountBase` table (and related extension tables) in the Dataverse SQL backend. The storage expert notes immediately: `parentaccountid` is a lookup column referencing `AccountBase.AccountId`. If the referenced GUID does not exist at the time of the INSERT, a foreign key / relationship constraint violation will fire at the storage layer — this is the highest blast-radius failure point in the trace.

**Auth expert:** The HTTP request must carry a valid Bearer token in the `Authorization` header. No token = 401 Unauthorized before any plug-in fires. Token must be issued for the correct Dataverse environment resource URI.

**Routing expert:** The OData routing layer parses the entity set name `accounts`, resolves it to the `account` entity metadata, and routes to the Create handler. A malformed entity set name returns 404. A `POST` to a read-only entity set returns 405.

**Failure points at entry:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong resource URI in token audience → 401 | Y | No |
| F-03 | Entity set name not found in metadata → 404 | N | No |
| F-04 | Metadata cache miss on cold start → routing delay | N | Y |

---

### Step 5 — Authentication Boundary

**Auth expert:** After the routing layer accepts the request, the platform authenticates the caller:

1. AAD token validation: signature, expiry, audience, issuer.
2. Dataverse system user lookup: the AAD OID / UPN in the token must map to an active `systemuser` record. Disabled or non-existent user = 403.
3. Privilege check: caller must hold `prvCreateAccount` (Create privilege on the Account entity) at a scope sufficient for the target business unit.
4. **FLS pre-check:** Because `parentaccountid` has field-level security, the platform checks whether the caller's FLS profile grants write access to this field at this stage. If FLS denies write, the field is silently stripped OR the operation is rejected depending on configuration — this is an authorization gap.

**Storage expert:** From the storage perspective, the auth boundary introduces a synchronous lookup against the `systemuser`, `role`, `roleprivileges`, and `fieldpermission` tables. Under load, these lookups add latency.

**Failure points at authentication:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found / disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS denies write on `parentaccountid` — silent strip vs. rejection ambiguity | Y | No |
| F-09 | Role / privilege cache miss → synchronous DB lookup latency | N | Y |

---

### Step 6 — Routing Boundary

**Routing expert:** The OData layer resolves the request to the Create handler for the `account` entity. It deserializes the JSON body, validates property names against entity metadata, and constructs an internal `Entity` object. Unrecognized properties are rejected (400). Type mismatches on `parentaccountid` (non-GUID string) return 400.

**Auth expert:** No additional auth check at this layer, but the internal `Entity` object carries the caller's `ExecutionContext` forward.

**Storage expert:** The deserialized `parentaccountid` GUID is not validated against existing records at this stage — that happens at the storage layer. This is a latency-free pass-through with a deferred failure risk.

**Failure points at routing:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` value is not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |

---

### Step 7 — Service Boundary Crossings (Plug-in Pipeline)

The plug-in pipeline is the primary internal service boundary. Each stage is a synchronous crossing.

#### 7a — PreValidation Plug-in

**Storage expert:** PreValidation fires before any database transaction is opened. If this plug-in queries Dataverse (e.g., to validate the parent account exists), it issues a separate query outside the main transaction — meaning the parent account could be deleted between this check and the actual INSERT.

**Auth expert:** The plug-in executes under the caller's security context (or a configured run-as user). If the plug-in performs its own entity queries, those queries are subject to the caller's privileges. A plug-in that reads `parentaccountid`'s target record requires `prvReadAccount` for the caller.

**Failure points — PreValidation:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-13 | Plug-in throws `InvalidPluginExecutionException` → 400 with message | Y | No |
| F-14 | Plug-in timeout (default 2 min) → 500 / pipeline abort | Y | Y |
| F-15 | Parent account read inside plug-in — caller lacks `prvReadAccount` → plug-in 403 | Y | No |
| F-16 | TOCTOU: parent deleted after PreValidation check but before INSERT | Y | No |

#### 7b — PreOperation Plug-in

**Storage expert:** PreOperation fires inside the database transaction. Modifications to the `Target` entity here affect the final INSERT. If this plug-in adds or modifies `parentaccountid`, the FLS check from Step 5 may need re-evaluation.

**Auth expert:** Same security context as PreValidation. Re-modification of FLS-protected fields by the plug-in may bypass the caller's FLS restriction if the plug-in runs with elevated privileges.

**Failure points — PreOperation:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-17 | Plug-in modifies `parentaccountid` under elevated context, bypassing FLS | Y | No |
| F-18 | Plug-in throws → transaction rollback → 400 | Y | No |
| F-19 | Plug-in latency under transaction lock → escalation risk | N | Y |

#### 7c — PostOperation Plug-in

**Storage expert:** PostOperation fires after the INSERT is committed. This plug-in cannot roll back the main record. However, if it performs dependent operations (e.g., creating child records), failures here leave the system in a partially committed state.

**Auth expert:** PostOperation may execute asynchronously in some configurations, but for synchronous registration, it runs in the same transaction context. Async PostOperation uses a service account.

**Failure points — PostOperation:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-20 | PostOperation failure → partial commit (account created, dependent op failed) | Y | No |
| F-21 | Async misclassification: plug-in registered as sync PostOperation but behaves as async | Y | No |

---

### Step 8 — Auth Verification Checkpoint

**Step 8 Header — VT# Token Reference Set and Checker Algorithm**

The following tokens are the canonical scope strings locked in Step 3. All Step 8c Match? evaluations and Step 8b prose confirmations reference this list exclusively.

```
VT-1: "user_impersonation"
VT-2: "prvCreateAccount"
VT-3: "prvReadAccount"
VT-4: "FLS write permission on parentaccountid"
VT-5: "internal service identity"
TOKEN-COUNT: 5

CHECKER ALGORITHM:
MATCH-RULE: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; comparison is case-sensitive and whitespace-normalized; a match requires character-for-character identity with the quoted VT-N value.
HALT-RULE: Fire when Step 8b prose asserts coherence (confirms the three link arms are consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous presence of a prose-coherent claim and a table-level mismatch constitutes a contradiction that must halt the trace.
OUTPUT-RULE: Assign Row-Verdict = PASS if Match? = Y for that row; assign Row-Verdict = HALT if HALT-RULE fires for that row; emit CHECK RESULT summary line immediately after the last row of the Step 8c table.
```

---

**Step 8a — Boundary Invocation Listing**

List every boundary where an auth scope or permission was actually invoked during the trace:

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry (Bearer token) | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |

---

**Step 8b — Prose Coherence Confirmation (REQUIRED — one paragraph per Gap?=Y boundary)**

*OData API entry (F-01, F-02):*
Arm 1: The boundary name "OData API entry (Bearer token)" matches the scope string `user_impersonation` declared in Step 3's auth contract for this boundary. Arm 2: The invoked scope string `user_impersonation` (Step 8a) matches VT-1: "user_impersonation" exactly. Arm 3: The parameter set from Step 11 (resource URI, tenant ID, environment ID) is consistent with the `user_impersonation` scope — the resource URI must be the Dataverse environment endpoint, which is the scope audience. All three arms are coherent.

*System user privilege check (F-06, F-07):*
Arm 1: The boundary name "System user privilege check" matches `prvCreateAccount` declared in Step 3. Arm 2: The invoked scope string `prvCreateAccount` (Step 8a) matches VT-2: "prvCreateAccount" exactly. Arm 3: The parameter set from Step 11 (entity name = `account`, operation = Create) is consistent with `prvCreateAccount` — this privilege is defined for the Create operation on the account entity. All three arms are coherent.

*FLS check on `parentaccountid` (F-08):*
Arm 1: The boundary name "FLS check on parentaccountid" matches `FLS write permission on parentaccountid` declared in Step 3. Arm 2: The invoked scope string `FLS write permission on parentaccountid` (Step 8a) matches VT-4: "FLS write permission on parentaccountid" exactly. Arm 3: The parameter set from Step 11 (field name = `parentaccountid`, operation = write) is consistent with the FLS scope string — the field and operation are named identically. All three arms are coherent.

*PreValidation plug-in read query (F-15):*
Arm 1: The boundary name "PreValidation plug-in read query" matches `prvReadAccount` declared in Step 3. Arm 2: The invoked scope string `prvReadAccount` (Step 8a) matches VT-3: "prvReadAccount" exactly. Arm 3: The parameter set from Step 11 (entity = `account`, operation = Read, context = plug-in query) is consistent with `prvReadAccount`. All three arms are coherent.

*PreOperation plug-in FLS bypass risk (F-17):*
Arm 1: The boundary name for this risk maps to `FLS write permission on parentaccountid` from Step 3. Arm 2: If the PreOperation plug-in writes `parentaccountid` under an elevated (run-as) context, the invoked permission is the plug-in's elevated context rather than the caller's FLS profile — this invoked scope does NOT match VT-4. Arm 3: The parameter set from Step 11 lists the plug-in's run-as user, which may have a different FLS profile than the caller. Arms 2 and 3 are incoherent — the elevated context bypass is a genuine contradiction. This triggers HALT-RULE for this boundary.

---

**Step 8c — Match? Table (REQUIRED — positioned before Step 9)**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| OData API entry | `user_impersonation` | `user_impersonation` | resource URI = Dataverse env endpoint, tenant ID present | Y | PASS |
| System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read, context=plugin | Y | PASS |
| SQL storage layer | `internal service identity` | `internal service identity` | service-to-service, no caller token | Y | PASS |
| PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as user, FLS profile differs | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): The PreOperation plug-in's run-as context must be constrained to the caller's FLS profile for parentaccountid, OR the plug-in must be documented as an intentional FLS bypass with explicit security review. The Step 3 auth contract must be updated to either add a separate scope entry for the elevated plug-in context or restrict the plug-in to caller-context execution.`

---

### Step 9 — Storage Access Boundary

**Storage expert (primary for this step):**

The Dataverse SQL backend receives the INSERT request for `AccountBase`:

1. **Relationship validation:** The storage layer validates that the `parentaccountid` GUID exists in `AccountBase.AccountId`. This is a foreign key constraint enforced at the SQL layer. If the GUID does not exist, the INSERT fails with a relationship constraint violation, surfaced to the caller as a 400 with an error code indicating invalid lookup value.
2. **Transaction scope:** The INSERT is wrapped in a transaction that spans PreOperation and PostOperation. Under high concurrency, row-level locks on the parent account record may cause wait chains.
3. **Extension tables:** Dataverse writes to `AccountBase` (core columns) and `AccountExtensionBase` (custom columns) in the same transaction. A failure on extension table write rolls back the entire transaction.
4. **Audit logging:** If audit is enabled for the account entity, an audit record is written in the same transaction — additional latency.

**Failure points at storage:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-22 | Parent GUID not found → FK constraint violation → 400 | Y | No |
| F-23 | Lock wait on parent account row under concurrency | N | Y |
| F-24 | Extension table write failure → full rollback | N | No |
| F-25 | Audit write latency under high volume | N | Y |

---

### Step 10 — Response Assembly Boundary

**Routing expert:** On successful INSERT, the OData layer assembles the response:

1. Reads the newly created record's primary key (`accountid` GUID) from the INSERT result.
2. Constructs the `OData-EntityId` header: `[base-url]/api/data/v9.2/accounts([new-guid])`.
3. Returns HTTP 204 No Content (default for OData Create) with the `OData-EntityId` header. If the caller sent `Prefer: return=representation`, the platform performs a SELECT on the new record and returns 201 with the full entity body — this adds a read round-trip.

**Auth expert:** The SELECT for `Prefer: return=representation` is subject to the caller's read privileges and FLS. If `parentaccountid` has FLS restricting read, the returned representation may omit or null the field even though it was just written.

**Failure points at response assembly:**
| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation → caller confusion | Y | No |
| F-27 | `Prefer: return=representation` adds read round-trip latency | N | Y |

---

### Step 11 — Parameter and Scope Catalog

Complete parameter set for the operation under trace:

| Parameter | Value | Scope association |
|---|---|---|
| HTTP method | POST | — |
| Endpoint | `/api/data/v9.2/accounts` | — |
| Entity | `account` | `prvCreateAccount`, `prvReadAccount` |
| Field under FLS | `parentaccountid` | `FLS write permission on parentaccountid` |
| Referenced entity | `account` (parent) | `prvReadAccount` |
| Token audience | Dataverse environment URI | `user_impersonation` |
| Tenant ID | AAD tenant of environment | `user_impersonation` |
| Environment ID | GUID of Dataverse environment | `user_impersonation` |
| Plug-in run-as | Configured per plug-in step (default: caller) | elevated plug-in context (run-as) |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

---

### Step 12 — Error Paths (Complete)

Enumerate all error paths identified across the trace, cross-referenced to failure points:

| Error path | HTTP status | Trigger | Failure ref |
|---|---|---|---|
| Missing / expired Bearer token | 401 | Entry point | F-01, F-05 |
| Wrong token audience | 401 | Entry point | F-02 |
| System user disabled or not found | 403 | Auth boundary | F-06 |
| Missing `prvCreateAccount` | 403 | Auth boundary | F-07 |
| FLS denies write on `parentaccountid` (hard block) | 400 | Auth boundary | F-08 |
| Malformed JSON | 400 | Routing boundary | F-10 |
| Invalid GUID format for `parentaccountid` | 400 | Routing boundary | F-11 |
| PreValidation plug-in exception | 400 | Plug-in pipeline | F-13 |
| PreValidation plug-in timeout | 500 | Plug-in pipeline | F-14 |
| PreValidation read blocked by caller `prvReadAccount` absence | 403 (inside plug-in) | Plug-in pipeline | F-15 |
| Parent GUID does not exist at INSERT time | 400 | Storage boundary | F-22 |
| PostOperation partial commit | 207 / 500 (depends on config) | Plug-in pipeline | F-20 |
| FLS strips `parentaccountid` from returned body | 204/201 but field absent | Response assembly | F-26 |

---

### Step 13 — Failure Catalog Ordered by Blast Radius (Storage Expert Final Output)

Per the Storage-first role ordering, the Storage expert provides the final failure catalog re-ordered by blast radius (widest-impact failures first):

1. **F-16 TOCTOU** — Parent deleted between PreValidation check and INSERT. Blast: silent data integrity corruption, no error returned to caller if race is not detected.
2. **F-20 PostOperation partial commit** — Account created, dependent operation failed. Blast: orphaned records, downstream process failures.
3. **F-22 Parent GUID not found at INSERT** — Blast: operation fails, but data integrity preserved; recoverable.
4. **F-17 FLS bypass via elevated plug-in** — Blast: security policy violation, data written in violation of field security, audit risk.
5. **F-08 FLS silent strip** — Blast: `parentaccountid` silently dropped, account created without parent relationship, data model inconsistency.
6. All other failures — operation fails cleanly with appropriate HTTP status; no data integrity risk.

---

### Step 14 — Latency Source Summary

| Latency source | Step | Severity |
|---|---|---|
| Metadata cache miss on cold start | Entry | Low (one-time) |
| Role/privilege cache miss → sync DB lookup | Auth | Medium (per-request under cache pressure) |
| Plug-in timeout risk (2-min default) | Plug-in pipeline | High |
| Plug-in latency under transaction lock | PreOperation | High |
| Lock wait on parent account row | Storage | Medium |
| Audit write under high volume | Storage | Low–Medium |
| `Prefer: return=representation` read round-trip | Response | Low |

---

### Step 15 — Signal Output

```
signal: trace-request
topic: [topic name from invocation context]
date: [today's date]
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
boundaries-traced: 7 (entry, auth, routing, PreValidation, PreOperation, PostOperation, storage, response)
failure-points: 27 (F-01 through F-27)
gap-flagged: 10 (F-01, F-02, F-05, F-06, F-07, F-08, F-13, F-14, F-15, F-16, F-17, F-20, F-22, F-26)
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6 — PreOperation FLS bypass)
latency-sources: 7
role-order: Storage → Auth → Routing
```

---

## V-02 — Single axis: Output format (Machine-first, all tables before prose)

**Axis:** Every step emits its machine-parseable block (table or structured token block) FIRST, then any explanatory prose; Step 8 Header is emitted as the very first output before any trace prose begins; Step 8c table appears before Step 8b prose.

**Hypothesis:** Table-before-prose order maximizes structural token density in Step 8 checker block and makes the full checker contract machine-readable without sequential prose scanning.

---

You are executing a `trace-request` signal for the following scenario. Auto-select the appropriate platform expert role from context: Dataverse / Commerce / Automate. Output format rule: every step emits its machine-parseable block (table or structured token block) FIRST, then any explanatory prose. The Step 8 Header (VT-N schema + CHECKER ALGORITHM) is emitted as the very first output of this entire trace, before any step prose. Step 8c appears before Step 8b.

**Scenario:** POST /api/data/v9.2/accounts — Create Account with `parentaccountid` referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on `parentaccountid`.

**Platform Expert Selected:** Dataverse platform expert.

---

### STEP 8 HEADER — Emitted First (Machine-First Format Rule)

The following token reference set and checker algorithm govern all Step 8 verification. This block is the first structured output of the trace.

```
VT-1: "user_impersonation"
VT-2: "prvCreateAccount"
VT-3: "prvReadAccount"
VT-4: "FLS write permission on parentaccountid"
VT-5: "internal service identity"
TOKEN-COUNT: 5

CHECKER ALGORITHM:
MATCH-RULE: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; comparison is case-sensitive and whitespace-normalized; a match requires character-for-character identity with the quoted VT-N value; this rule is evaluated independently of prose content.
HALT-RULE: Fire when Step 8b prose asserts coherence (confirms the three link arms are consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous presence of a prose-coherent claim and a table-level mismatch is a contradiction requiring trace halt.
OUTPUT-RULE: Assign Row-Verdict = PASS if Match? = Y for that row; assign Row-Verdict = HALT if HALT-RULE fires for that row; emit CHECK RESULT summary line immediately after the last row of the Step 8c table; no prose reading is required to evaluate this contract.
```

---

### Step 1 — Scenario Registration

**Machine block first:**

```
operation: POST /api/data/v9.2/accounts
payload-key-field: parentaccountid (GUID reference)
plugin-pipeline: PreValidation, PreOperation, PostOperation (all sync)
security-overlay: FLS on parentaccountid
trace-goal: hand-compile every boundary crossing, failure point, latency source, auth gap
```

**Prose:** This trace covers the Create Account operation on the Dataverse OData v4 endpoint. The `parentaccountid` field carries a GUID referencing an existing account and is protected by field-level security. Three synchronous plug-ins fire at PreValidation, PreOperation, and PostOperation stages.

---

### Step 2 — Role Declaration

**Machine block first:**

```
role: Dataverse platform expert
output-format-rule: machine-parseable block before prose in every step
step8-header-position: emitted before Step 1 (already done above)
step8c-position: before Step 8b
```

**Prose:** The Dataverse platform expert role is confirmed. Output format enforces machine block priority throughout.

---

### Step 3 — Authentication Contract

**Machine block first:**

| Boundary | Required Scope / Permission | Token Type | Notes |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | Delegated or app-only |
| Plugin execution context | Caller privileges propagated | Internal system token | Inherits caller |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | System user record | Checked against FLS profile |
| SQL storage layer | `internal service identity` | Internal (no OAuth) | Service-to-service |
| Relationship validation (parent GUID lookup) | `prvReadAccount` | Bearer (AAD) / system user | Must hold read privilege |
| System user privilege check | `prvCreateAccount` | Bearer (AAD) / system user | Create privilege on account |

**Prose:** This table locks the auth contract. Every scope string here is the ground truth for Step 8 Match? evaluation. No scope invoked during the trace may differ from this set without triggering HALT-RULE.

---

### Step 4 — Entry Point

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong resource URI in token audience → 401 | Y | No |
| F-03 | Entity set name not found in metadata → 404 | N | No |
| F-04 | Metadata cache miss on cold start | N | Y |

**Prose:** The HTTP POST arrives at `/api/data/v9.2/accounts`. The OData routing layer parses the entity set, validates the HTTP method, and forwards the request to the Create handler. The Bearer token is required at this boundary. F-01 and F-02 are Gap?=Y because they represent auth failures where an authorization contract mismatch exists.

---

### Step 5 — Authentication Boundary

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found / disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS denies write on `parentaccountid` — silent strip vs. rejection | Y | No |
| F-09 | Role/privilege cache miss → sync DB lookup | N | Y |

**Prose:** AAD token validation runs first (signature, expiry, audience, issuer). Then the platform resolves the AAD OID to a Dataverse `systemuser` record. Privilege check confirms `prvCreateAccount`. FLS check on `parentaccountid` determines whether the field is writable or silently stripped. All four auth steps are synchronous and in-process.

---

### Step 6 — Routing Boundary

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |

**Prose:** The OData deserializer constructs an internal `Entity` object from the JSON body. Property names are validated against entity metadata. Type validation runs on `parentaccountid` — it must be a GUID. The `ExecutionContext` carrying caller identity is attached to the `Entity` object at this stage.

---

### Step 7 — Service Boundary Crossings (Plug-in Pipeline)

#### 7a — PreValidation

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-13 | Plug-in throws `InvalidPluginExecutionException` → 400 | Y | No |
| F-14 | Plug-in timeout (2 min default) → 500 | Y | Y |
| F-15 | Plug-in read of parent account — caller lacks `prvReadAccount` | Y | No |
| F-16 | TOCTOU: parent deleted after PreValidation check, before INSERT | Y | No |

**Prose:** PreValidation fires outside the main database transaction. If this plug-in validates the parent account's existence via a query, that query is outside transaction scope — the parent could be deleted in the window between the check and the INSERT. F-16 is the highest data-integrity risk in the pipeline.

#### 7b — PreOperation

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-17 | Elevated plug-in context modifies `parentaccountid`, bypassing FLS | Y | No |
| F-18 | Plug-in throws → transaction rollback → 400 | Y | No |
| F-19 | Plug-in latency under transaction lock → escalation risk | N | Y |

**Prose:** PreOperation fires inside the database transaction. Modifications to `Target` here affect the final INSERT. If the plug-in is configured with a run-as user that has elevated FLS permissions, it can write `parentaccountid` even when the caller's FLS profile would deny it — an unintended security bypass documented as F-17.

#### 7c — PostOperation

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-20 | PostOperation failure → partial commit | Y | No |
| F-21 | Async misclassification of sync PostOperation | Y | No |

**Prose:** PostOperation fires after the INSERT is committed. A failure here cannot roll back the main record. If this plug-in creates dependent records (e.g., child entities or related records), a failure leaves the system in a partially committed state with the account existing but dependents absent.

---

### Step 8 — Auth Verification Checkpoint

*(Step 8 Header already emitted at top. Step 8c emitted before Step 8b per machine-first format rule.)*

**Step 8a — Boundary Invocation Listing (machine block):**

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

---

**Step 8c — Match? Table (REQUIRED — emitted BEFORE Step 8b per format rule):**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| OData API entry | `user_impersonation` | `user_impersonation` | resource URI = Dataverse env, tenant ID present | Y | PASS |
| System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read, context=plugin | Y | PASS |
| SQL storage layer | `internal service identity` | `internal service identity` | service-to-service, no caller token | Y | PASS |
| PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as user, FLS profile differs | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): The PreOperation plug-in's run-as context must either (a) be constrained to use the caller's FLS profile for parentaccountid so the invoked scope matches VT-4, or (b) be explicitly documented as an FLS bypass with the Step 3 auth contract amended to include a distinct scope entry for this elevated context. Until one of these corrections is applied, the trace is halted at this boundary.`

---

**Step 8b — Prose Coherence Confirmation (emitted AFTER Step 8c per format rule):**

*OData API entry:*
Arm 1: "OData API entry (Bearer token)" maps to `user_impersonation` in Step 3 auth contract. Arm 2: Step 8a-Invoked = `user_impersonation` matches VT-1: "user_impersonation" exactly. Arm 3: Step 11 parameters (resource URI = Dataverse env endpoint) are consistent with `user_impersonation` scope audience. All three arms coherent.

*System user privilege check:*
Arm 1: "System user privilege check" maps to `prvCreateAccount` in Step 3. Arm 2: Step 8a-Invoked = `prvCreateAccount` matches VT-2: "prvCreateAccount" exactly. Arm 3: Step 11 parameters (entity=account, op=Create) are consistent with `prvCreateAccount`. All three arms coherent.

*FLS check on `parentaccountid`:*
Arm 1: "FLS check on parentaccountid" maps to `FLS write permission on parentaccountid` in Step 3. Arm 2: Step 8a-Invoked = `FLS write permission on parentaccountid` matches VT-4 exactly. Arm 3: Step 11 parameters (field=parentaccountid, op=write) are consistent. All three arms coherent.

*PreValidation plug-in read query:*
Arm 1: "PreValidation plug-in read query" maps to `prvReadAccount` in Step 3. Arm 2: Step 8a-Invoked = `prvReadAccount` matches VT-3 exactly. Arm 3: Step 11 parameters (entity=account, op=Read) are consistent. All three arms coherent.

*PreOperation elevated FLS bypass:*
Arm 1: This boundary should map to `FLS write permission on parentaccountid` per Step 3, but the actual invocation uses an elevated plug-in context. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" does NOT match VT-4: "FLS write permission on parentaccountid". Arm 3: Step 11 parameters confirm the plug-in run-as user has a different FLS profile. Arms 2 and 3 are incoherent — HALT-RULE fires. This is consistent with Row-Verdict = HALT in Step 8c (no contradiction between 8b and 8c).

---

### Step 9 — Storage Access Boundary

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-22 | Parent GUID not found → FK constraint violation → 400 | Y | No |
| F-23 | Lock wait on parent account row under concurrency | N | Y |
| F-24 | Extension table write failure → full rollback | N | No |
| F-25 | Audit write latency under high volume | N | Y |

**Prose:** The INSERT targets `AccountBase` and `AccountExtensionBase`. The storage layer enforces the relationship constraint: `parentaccountid` must reference an existing `AccountBase.AccountId`. If audit is enabled, the audit record is written in the same transaction.

---

### Step 10 — Response Assembly Boundary

**Machine block first:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation | Y | No |
| F-27 | `Prefer: return=representation` adds read round-trip | N | Y |

**Prose:** On success, the OData layer returns HTTP 204 with `OData-EntityId` header. If the caller sends `Prefer: return=representation`, a SELECT is issued and 201 is returned with the entity body. FLS applies to this read — `parentaccountid` may be absent from the response body even though it was successfully written.

---

### Step 11 — Parameter and Scope Catalog

**Machine block first:**

| Parameter | Value | Scope association |
|---|---|---|
| HTTP method | POST | — |
| Endpoint | `/api/data/v9.2/accounts` | — |
| Entity | `account` | `prvCreateAccount`, `prvReadAccount` |
| Field under FLS | `parentaccountid` | `FLS write permission on parentaccountid` |
| Referenced entity | `account` (parent) | `prvReadAccount` |
| Token audience | Dataverse environment URI | `user_impersonation` |
| Tenant ID | AAD tenant of environment | `user_impersonation` |
| Environment ID | GUID of Dataverse environment | `user_impersonation` |
| Plug-in run-as | Configured per plug-in step | elevated plug-in context (run-as) |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

**Prose:** This catalog is the authoritative parameter set referenced in the Step 8c Step11-Params column. All parameter-scope associations are consistent with the VT-N tokens declared in the Step 8 Header.

---

### Step 12 — Error Paths

**Machine block first:**

| Error path | HTTP status | Failure ref |
|---|---|---|
| Missing / expired Bearer token | 401 | F-01, F-05 |
| Wrong token audience | 401 | F-02 |
| System user disabled | 403 | F-06 |
| Missing `prvCreateAccount` | 403 | F-07 |
| FLS hard block on `parentaccountid` | 400 | F-08 |
| Malformed JSON | 400 | F-10 |
| Invalid GUID format | 400 | F-11 |
| PreValidation plug-in exception | 400 | F-13 |
| PreValidation plug-in timeout | 500 | F-14 |
| Missing `prvReadAccount` in plug-in | 403 | F-15 |
| Parent GUID not found at INSERT | 400 | F-22 |
| PostOperation partial commit | 500 / config-dependent | F-20 |
| FLS strips field from response | 204/201 field absent | F-26 |

**Prose:** Error paths are ordered by HTTP status code for machine-parseable lookup. Each row maps to one or more failure-point identifiers from Steps 4–10.

---

### Step 13 — Latency Source Summary

**Machine block first:**

| Latency source | Step | Severity |
|---|---|---|
| Metadata cache miss | Entry | Low |
| Role/privilege cache miss | Auth | Medium |
| Plug-in timeout risk | Plugin pipeline | High |
| Plug-in latency under transaction lock | PreOperation | High |
| Lock wait on parent row | Storage | Medium |
| Audit write | Storage | Low–Medium |
| `Prefer: return=representation` read | Response | Low |

**Prose:** Seven latency sources identified. Two are High severity and both occur inside the plug-in pipeline — plug-in timeout and lock contention under PreOperation. These are the primary targets for performance optimization in this scenario.

---

### Step 14 — Signal Output

```
signal: trace-request
topic: [topic from invocation context]
date: [today's date]
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
boundaries-traced: 7
failure-points: 27
gap-flagged: 10
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6)
latency-sources: 7
format: machine-first (tables before prose, Step 8 Header first)
```

---

## V-03 — Single axis: Lifecycle emphasis (Equal phase budget)

**Axis:** Six lifecycle phases each get an explicitly labeled, equal-weight section with three required sub-items per phase; error paths receive a standalone Phase 7 equal in weight to Phases 1–6, not appended as a sub-section.

**Hypothesis:** Equal explicit phase budget prevents auth and routing phases from collapsing into a single boundary section, producing a more granular failure-point catalog with distinct latency attribution per phase.

---

You are executing a `trace-request` signal for the following scenario. Auto-select the appropriate platform expert role from context: Dataverse / Commerce / Automate. This trace uses an equal phase budget: six lifecycle phases (Entry, Authentication, Routing, Boundary-Crossing, Storage, Response-Assembly) each receive an explicitly labeled, equal-weight section. Each section must contain exactly three required sub-items: (1) boundary description, (2) failure point table, (3) latency source identification. Error paths receive a standalone Phase 7 section with equal weight to Phases 1–6.

**Scenario:** POST /api/data/v9.2/accounts — Create Account with `parentaccountid` referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on `parentaccountid`.

**Platform Expert Selected:** Dataverse platform expert.

---

### Step 1 — Scenario Registration

- **Operation:** POST /api/data/v9.2/accounts
- **Payload key field:** `parentaccountid` (GUID reference to existing account)
- **Plug-in pipeline:** PreValidation → PreOperation → PostOperation (all synchronous)
- **Security overlay:** Field-level security (FLS) on `parentaccountid`
- **Phase budget:** 7 phases (6 lifecycle + 1 error paths), each explicitly labeled and equal weight

---

### Step 2 — Role Declaration

**Platform Expert:** Dataverse platform expert  
**Phase budget rule:** Each of Phases 1–7 must contain exactly three required sub-items. No phase may be collapsed into another or demoted to a sub-section. Phase 7 (Error Paths) is a first-class section.

---

### Step 3 — Authentication Contract

Lock the full auth contract before any phase trace begins:

| Boundary | Required Scope / Permission | Token Type | Notes |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | Environment resource URI audience |
| System user privilege check | `prvCreateAccount` | System user + role | Create privilege on account entity |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | FLS profile | Write permission on named field |
| SQL storage layer | `internal service identity` | Internal | Service-to-service, no OAuth |
| Parent GUID relationship validation | `prvReadAccount` | System user | Read privilege on account entity |

**Auth contract locked.** Step 8 verifies every invoked scope against this set.

---

### Phase 1 — Entry

**Sub-item 1 — Boundary description:**
The HTTP POST arrives at the Dataverse OData v4 endpoint `/api/data/v9.2/accounts`. The entry point is the web API tier that accepts inbound HTTP requests. It performs initial request parsing: HTTP method validation, content-type check (must be `application/json`), and URL parsing to extract the entity set name `accounts`.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong token audience (wrong environment URI) → 401 | Y | No |
| F-03 | Entity set name not resolved in OData metadata → 404 | N | No |
| F-04 | Wrong HTTP method (e.g., GET instead of POST) → 405 | N | No |

**Sub-item 3 — Latency source identification:**
Latency source at entry: OData metadata cache miss on cold start or after metadata invalidation. The metadata resolution for entity set `accounts` requires a lookup against the cached entity metadata store. On a warm instance this is sub-millisecond. On a cold start or after a publish operation that invalidates the cache, this can add 500ms–2s.

---

### Phase 2 — Authentication

**Sub-item 1 — Boundary description:**
Authentication processes the Bearer token from the `Authorization` header. Four sequential checks run: (1) AAD token signature and claims validation, (2) token expiry and issuer check, (3) Dataverse system user resolution from the AAD OID/UPN, (4) FLS profile lookup for `parentaccountid`. Auth is fully synchronous and blocks request progression.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found or disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS profile denies write on `parentaccountid` (silent strip or hard reject) | Y | No |
| F-09 | Role/privilege cache miss → synchronous DB round-trip | N | Y |

**Sub-item 3 — Latency source identification:**
Latency source at authentication: role and privilege cache miss. The system user's security roles and privileges are cached. Under memory pressure or after a role assignment change, the cache is invalidated and the platform performs a synchronous read against `systemuser`, `role`, `roleprivileges`, and `fieldpermission` tables. Under load, this adds 50–200ms per request.

---

### Phase 3 — Routing

**Sub-item 1 — Boundary description:**
The OData routing layer resolves the entity set `accounts` to the `account` entity metadata definition. It constructs the request handler (Create operation), deserializes the JSON body into an internal `Entity` object, and validates all property names and types against the entity metadata. The `parentaccountid` GUID format is validated here. The caller's `ExecutionContext` is attached to the `Entity` object.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON → 400 | N | No |
| F-11 | `parentaccountid` not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |
| F-13 | Content-Type not `application/json` → 415 | N | No |

**Sub-item 3 — Latency source identification:**
Latency source at routing: entity metadata resolution. The routing layer consults the entity metadata cache. For complex entities with many attributes (account entity has 100+ attributes), deserialization and metadata validation time scales with payload size. Large payloads with many attributes add measurable parsing latency.

---

### Phase 4 — Boundary-Crossing (Plug-in Pipeline)

**Sub-item 1 — Boundary description:**
Three synchronous plug-in boundaries are crossed in sequence: PreValidation (before transaction), PreOperation (inside transaction), PostOperation (after commit). Each crossing invokes the Dataverse plug-in infrastructure, serializes the `ExecutionContext`, and dispatches to the registered plug-in assembly. Auth at every crossing: each plug-in executes under the caller's security context unless a run-as user is configured on the plug-in step.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-14 | PreValidation throws `InvalidPluginExecutionException` → 400 | Y | No |
| F-15 | PreValidation timeout (2-min default) → 500 | Y | Y |
| F-16 | PreValidation read of parent account — caller lacks `prvReadAccount` | Y | No |
| F-17 | TOCTOU: parent deleted between PreValidation check and INSERT | Y | No |
| F-18 | PreOperation elevated context modifies `parentaccountid`, bypassing FLS | Y | No |
| F-19 | PreOperation throws → transaction rollback | Y | No |
| F-20 | PreOperation latency under transaction lock → lock escalation | N | Y |
| F-21 | PostOperation failure → partial commit (account exists, dependents absent) | Y | No |
| F-22 | Async PostOperation misclassified as sync | Y | No |

**Sub-item 3 — Latency source identification:**
Latency sources at boundary-crossing: (1) Plug-in dispatch overhead per stage (~5–20ms per crossing on warm instance). (2) Plug-in execution time — unbounded if plug-in calls external services; default timeout is 2 minutes for sync plug-ins. (3) Transaction lock contention during PreOperation — if the parent account record is concurrently modified, lock wait can cascade. Three latency sources, all in this phase, make it the highest latency risk in the trace.

---

### Phase 5 — Storage

**Sub-item 1 — Boundary description:**
The Dataverse SQL backend receives the INSERT for `AccountBase` and `AccountExtensionBase`. The storage layer enforces: (1) relationship constraint — `parentaccountid` GUID must exist in `AccountBase.AccountId`; (2) transaction atomicity across core and extension tables; (3) audit record write if auditing is enabled for the account entity. Auth at storage: internal service identity only; no caller token propagates to SQL.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-23 | Parent GUID not found → FK constraint violation → 400 | Y | No |
| F-24 | Lock wait on parent account row under concurrency | N | Y |
| F-25 | Extension table write failure → full transaction rollback | N | No |
| F-26 | Audit write failure (if audit required) → operation fail | N | No |

**Sub-item 3 — Latency source identification:**
Latency sources at storage: (1) Lock wait on parent account row — if another operation is modifying the parent account concurrently, a shared lock wait occurs before the INSERT can proceed. (2) Audit write — writing to the audit table in the same transaction adds I/O latency proportional to audit volume. Both are variable and load-dependent.

---

### Phase 6 — Response Assembly

**Sub-item 1 — Boundary description:**
On successful INSERT, the OData layer assembles the HTTP response. Default behavior: 204 No Content with `OData-EntityId` header containing the URL of the new account record. If the caller sent `Prefer: return=representation`, the platform issues a SELECT on the new record and returns 201 Created with the full entity body. Auth at response assembly: the SELECT for `Prefer: return=representation` applies the caller's read privileges and FLS profile — `parentaccountid` may be stripped from the response even though it was written.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-27 | FLS strips `parentaccountid` from returned representation | Y | No |
| F-28 | `OData-EntityId` header malformed → client cannot locate new record | N | No |
| F-29 | SELECT for `Prefer: return=representation` blocked by missing read privilege | Y | No |

**Sub-item 3 — Latency source identification:**
Latency source at response assembly: `Prefer: return=representation` triggers a read round-trip. The SELECT re-applies all OData query processing including FLS evaluation, column projection, and JSON serialization. For the account entity, this adds 20–100ms depending on instance load and number of columns returned.

---

### Step 8 — Auth Verification Checkpoint

**Step 8 Header:**

```
VT-1: "user_impersonation"
VT-2: "prvCreateAccount"
VT-3: "prvReadAccount"
VT-4: "FLS write permission on parentaccountid"
VT-5: "internal service identity"
TOKEN-COUNT: 5

CHECKER ALGORITHM:
MATCH-RULE: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; case-sensitive; whitespace-normalized; character-for-character identity with the quoted VT-N value required; this predicate is evaluated independently of any prose content.
HALT-RULE: Fire when Step 8b prose asserts coherence (all three link arms consistent) AND Step 8c Match? = N for the same boundary row; simultaneous prose-coherent claim with table-level mismatch is a contradiction requiring trace halt.
OUTPUT-RULE: Row-Verdict = PASS if Match? = Y; Row-Verdict = HALT if HALT-RULE fires; emit CHECK RESULT immediately after last row; no prose reading required to evaluate this contract.
```

**Step 8a — Boundary Invocation Listing:**

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

**Step 8b — Prose Coherence Confirmation (REQUIRED):**

*OData API entry (F-01, F-02):*
Arm 1: "OData API entry" boundary name matches the `user_impersonation` scope string in Step 3's auth contract for this boundary — confirmed. Arm 2: Step 8a-Invoked = `user_impersonation` matches VT-1: "user_impersonation" exactly — confirmed. Arm 3: Step 11 parameters (resource URI = Dataverse env endpoint, tenant ID, environment ID) are consistent with the `user_impersonation` scope — the resource URI is the token audience — confirmed. All three arms coherent.

*System user privilege check (F-06, F-07):*
Arm 1: "System user privilege check" matches `prvCreateAccount` in Step 3 — confirmed. Arm 2: Step 8a-Invoked = `prvCreateAccount` matches VT-2 exactly — confirmed. Arm 3: Step 11 parameters (entity=account, op=Create) consistent with `prvCreateAccount` — confirmed. All three arms coherent.

*FLS check on `parentaccountid` (F-08):*
Arm 1: "FLS check on parentaccountid" matches `FLS write permission on parentaccountid` in Step 3 — confirmed. Arm 2: Step 8a-Invoked = `FLS write permission on parentaccountid` matches VT-4 exactly — confirmed. Arm 3: Step 11 parameters (field=parentaccountid, op=write) consistent — confirmed. All three arms coherent.

*PreValidation plug-in read query (F-16):*
Arm 1: "PreValidation plug-in read query" maps to `prvReadAccount` in Step 3 — confirmed. Arm 2: Step 8a-Invoked = `prvReadAccount` matches VT-3 exactly — confirmed. Arm 3: Step 11 parameters (entity=account, op=Read, context=plugin) consistent — confirmed. All three arms coherent.

*PreOperation elevated FLS bypass (F-18):*
Arm 1: This boundary should map to `FLS write permission on parentaccountid` per Step 3 auth contract. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" does NOT match VT-4: "FLS write permission on parentaccountid" — mismatch detected. Arm 3: Step 11 parameters confirm plug-in run-as user has a different FLS profile than caller — inconsistent with VT-4. Arms 2 and 3 are incoherent. HALT-RULE fires.

**Step 8c — Match? Table (REQUIRED — before Step 9):**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| OData API entry | `user_impersonation` | `user_impersonation` | resource URI=Dataverse env, tenant ID present | Y | PASS |
| System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read | Y | PASS |
| SQL storage layer | `internal service identity` | `internal service identity` | service-to-service | Y | PASS |
| PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as, FLS profile differs | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): Amend Step 3 auth contract to add explicit entry for "elevated plug-in context (run-as)" at the PreOperation boundary, or constrain the plug-in to execute under caller's FLS profile so the invoked scope becomes "FLS write permission on parentaccountid" matching VT-4.`

---

### Phase 7 — Error Paths (First-Class Section, Equal Weight to Phases 1–6)

**Sub-item 1 — Error path boundary description:**
Error paths are collected from all six lifecycle phases. Each error path is a discrete outcome reachable from at least one failure point in the trace. Error paths are classified by recovery type: (a) client-correctable (4xx), (b) server/platform failures (5xx), (c) silent data issues (2xx with data anomaly).

**Sub-item 2 — Error path table:**

| Error path | HTTP status | Phase | Failure ref | Recovery type |
|---|---|---|---|---|
| Missing / expired Bearer token | 401 | Entry, Auth | F-01, F-05 | Client-correctable |
| Wrong token audience | 401 | Entry | F-02 | Client-correctable |
| System user disabled | 403 | Auth | F-06 | Admin action required |
| Missing `prvCreateAccount` | 403 | Auth | F-07 | Admin action required |
| FLS hard block on `parentaccountid` | 400 | Auth | F-08 | Admin action required |
| Malformed JSON | 400 | Routing | F-10 | Client-correctable |
| Invalid GUID format | 400 | Routing | F-11 | Client-correctable |
| PreValidation plug-in exception | 400 | Boundary-Crossing | F-14 | Depends on plug-in message |
| PreValidation plug-in timeout | 500 | Boundary-Crossing | F-15 | Retry / plug-in optimization |
| Missing `prvReadAccount` in plug-in | 403 | Boundary-Crossing | F-16 | Admin action required |
| Parent GUID not found at INSERT | 400 | Storage | F-23 | Client-correctable (verify GUID) |
| PostOperation partial commit | 500 | Boundary-Crossing | F-21 | Investigation required |
| FLS strips field from response | 204/201 field absent | Response Assembly | F-27 | Silent — caller awareness required |
| Read privilege missing for `Prefer` response | 403/field absent | Response Assembly | F-29 | Admin action required |

**Sub-item 3 — Latency attribution per error path:**
Error paths themselves do not add latency (they terminate the request). However, the failure points that cause them are preceded by latency-contributing operations: metadata cache miss (Phase 1), privilege cache miss (Phase 2), plug-in dispatch overhead (Phase 4), and lock waits (Phase 5). The two highest-latency failure points are F-15 (plug-in timeout, up to 2 minutes) and F-24 (lock wait, unbounded under high concurrency). Both occur before the request reaches Phase 5's INSERT — meaning in the worst case, the system holds a transaction-level lock for up to 2 minutes before failing.

---

### Step 9 — Parameter and Scope Catalog (Step 11 Reference)

| Parameter | Value | Scope association |
|---|---|---|
| HTTP method | POST | — |
| Endpoint | `/api/data/v9.2/accounts` | — |
| Entity | `account` | `prvCreateAccount`, `prvReadAccount` |
| Field under FLS | `parentaccountid` | `FLS write permission on parentaccountid` |
| Referenced entity | `account` (parent) | `prvReadAccount` |
| Token audience | Dataverse environment URI | `user_impersonation` |
| Tenant ID | AAD tenant of environment | `user_impersonation` |
| Environment ID | GUID of Dataverse environment | `user_impersonation` |
| Plug-in run-as | Configured per plug-in step | elevated plug-in context (run-as) |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

---

### Step 10 — Latency Source Summary (Cross-Phase)

| Phase | Latency source | Severity |
|---|---|---|
| Phase 1 — Entry | Metadata cache miss | Low |
| Phase 2 — Authentication | Role/privilege cache miss | Medium |
| Phase 3 — Routing | Entity metadata resolution for large payloads | Low |
| Phase 4 — Boundary-Crossing | Plug-in dispatch overhead (3 crossings) | Low–Medium |
| Phase 4 — Boundary-Crossing | Plug-in execution time (unbounded) | High |
| Phase 4 — Boundary-Crossing | Transaction lock contention (PreOperation) | High |
| Phase 5 — Storage | Lock wait on parent account row | Medium |
| Phase 5 — Storage | Audit write | Low–Medium |
| Phase 6 — Response Assembly | `Prefer: return=representation` read round-trip | Low |

---

### Step 11 — Signal Output

```
signal: trace-request
topic: [topic from invocation context]
date: [today's date]
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
phase-budget: 7 phases (equal weight)
boundaries-traced: 7
failure-points: 29 (F-01 through F-29)
gap-flagged: 12
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6)
latency-sources: 9 (cross-phase)
format: equal-phase-budget
```

---

## V-04 — Combined: Role sequence + Output format

**Axis:** Reversed role order (Storage → Auth → Routing) AND machine-first output format (all tables before prose, Step 8 Header emitted first).

**Hypothesis:** Reversed role order combined with machine-first output format jointly maximize structural token density in the Step 8 checker block while also surfacing storage failure points at higher severity in the Gap?=Y population.

---

You are executing a `trace-request` signal for the following scenario. Auto-select the appropriate platform expert role from context: Dataverse / Commerce / Automate. This trace applies two simultaneous variation rules:

**Rule 1 — Role execution order (Storage-first):** The Storage/data-layer expert speaks first at every step, followed by the Auth expert, followed by the Routing/API expert.

**Rule 2 — Machine-first output format:** Every step emits its machine-parseable block (table or structured token block) FIRST, then explanatory prose. The Step 8 Header (VT-N schema + CHECKER ALGORITHM) is emitted as the very first output of the entire trace, before Step 1. Step 8c appears before Step 8b.

**Scenario:** POST /api/data/v9.2/accounts — Create Account with `parentaccountid` referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on `parentaccountid`.

**Platform Expert Selected:** Dataverse platform expert. Sub-roles: Storage expert (speaks first), Auth expert (speaks second), Routing expert (speaks third).

---

### STEP 8 HEADER — Emitted First (Machine-First + Storage-First Combined Rule)

```
VT-1: "user_impersonation"
VT-2: "prvCreateAccount"
VT-3: "prvReadAccount"
VT-4: "FLS write permission on parentaccountid"
VT-5: "internal service identity"
TOKEN-COUNT: 5

CHECKER ALGORITHM:
MATCH-RULE: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; case-sensitive and whitespace-normalized; character-for-character identity with the quoted VT-N value; evaluated independently of all prose content and of VT-N line positions.
HALT-RULE: Fire when Step 8b prose asserts coherence (all three link arms consistent) AND Step 8c Match? = N for the same boundary row; simultaneous prose-coherent assertion with table-level mismatch is a structural contradiction requiring trace halt.
OUTPUT-RULE: Row-Verdict = PASS if Match? = Y; Row-Verdict = HALT if HALT-RULE fires; emit CHECK RESULT summary line immediately after last row of Step 8c table; this contract is fully machine-evaluable without prose reading.
```

---

### Step 1 — Scenario Registration

**Machine block first:**

```
operation: POST /api/data/v9.2/accounts
payload-key-field: parentaccountid (GUID reference to existing account)
plugin-pipeline: PreValidation, PreOperation, PostOperation (all sync)
security-overlay: FLS on parentaccountid
role-order: Storage-first → Auth → Routing
output-format: machine-first (tables before prose, Step 8 Header emitted before Step 1)
```

**Storage expert prose:** The core storage concern for this operation is the INSERT into `AccountBase` with a foreign-key constraint on `parentaccountid`. The storage expert's initial scan identifies three high-blast-radius risks: TOCTOU on parent validation, FK constraint violation at INSERT time, and FLS bypass via elevated plug-in context. These frame the failure catalog.

**Auth expert prose:** Auth concerns center on three boundaries: Bearer token at entry, privilege check at auth, and FLS profile evaluation for `parentaccountid`.

**Routing expert prose:** Routing concern is entity set resolution and `ExecutionContext` propagation. Minimal failure surface at routing.

---

### Step 2 — Role Order and Format Declaration

**Machine block first:**

```
role-1: Storage/data-layer expert (speaks first)
role-2: Auth expert (speaks second)
role-3: Routing/API expert (speaks third)
format-rule-1: machine block before prose in every step
format-rule-2: Step 8 Header before Step 1 (already emitted above)
format-rule-3: Step 8c before Step 8b
```

**Prose:** Both variation rules are active for the entire trace. Storage expert's findings determine failure severity ordering. Machine blocks precede prose in all steps.

---

### Step 3 — Authentication Contract

**Machine block first (storage expert speaks to data-layer implications):**

| Boundary | Required Scope / Permission | Token Type | Storage expert note |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | No storage impact at entry |
| System user privilege check | `prvCreateAccount` | System user + role | Triggers sync lookup against systemuser + role tables if cache cold |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | FLS profile | Triggers lookup against fieldpermission table if cache cold |
| SQL storage layer | `internal service identity` | Internal | This IS the storage boundary; no OAuth; highest data-integrity risk |
| Parent GUID relationship validation | `prvReadAccount` | System user | Read privilege required for plug-in queries against AccountBase |

**Auth expert prose:** Auth contract is locked. Every invoked scope must match exactly. Step 8 verification will confirm all five VT-N tokens are correctly propagated through the trace.

**Routing expert prose:** Routing carries the `ExecutionContext` (which encodes the caller's security context) through to the plug-in pipeline. No separate auth scope at routing.

---

### Step 4 — Entry Point

**Machine block first — Storage expert leads with blast-radius ordering:**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No | None — request terminated before storage |
| F-02 | Wrong token audience → 401 | Y | No | None — request terminated before storage |
| F-03 | Entity set not found → 404 | N | No | None |
| F-04 | Metadata cache miss | N | Y | Indirect — delays request, no data risk |

**Storage expert prose:** From a storage perspective, entry-point failures are high-value: they terminate the request before any storage operation, producing clean failures with no data side effects. The storage expert notes these as zero blast-radius failures — important for triage prioritization.

**Auth expert prose:** F-01 and F-02 are auth gaps. Bearer token absence or wrong audience are client-configuration failures that must be flagged in the Gap?=Y catalog.

**Routing expert prose:** F-03 and F-04 are routing concerns. Cold-start metadata cache miss is the only latency source at this stage.

---

### Step 5 — Authentication Boundary

**Machine block first — Storage expert leads with auth/storage intersection:**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-05 | Token expired → 401 | Y | No | None |
| F-06 | System user not found / disabled → 403 | Y | No | None |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No | None |
| F-08 | FLS silent strip on `parentaccountid` → field absent from INSERT | Y | No | Medium — account created without parent relationship |
| F-09 | Role/privilege cache miss | N | Y | Low — latency only, no data risk |

**Storage expert prose:** F-08 is the critical storage concern at the auth boundary. FLS silent strip means the account is created without `parentaccountid` even though the caller provided it — producing a data model inconsistency that is hard to detect post-facto. This is a higher blast-radius outcome than a hard rejection (F-07 style) because the caller receives a 204/201 success response.

**Auth expert prose:** AAD token validation → system user resolution → privilege check → FLS profile check. All four steps are synchronous. F-05 through F-08 are all Gap?=Y.

**Routing expert prose:** No routing concern at this stage. `ExecutionContext` is finalized after auth.

---

### Step 6 — Routing Boundary

**Machine block first:**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-10 | Malformed JSON → 400 | N | No | None |
| F-11 | `parentaccountid` not a valid GUID format → 400 | N | No | None |
| F-12 | Unrecognized property name → 400 | N | No | None |

**Storage expert prose:** From a storage perspective, routing failures are all zero blast-radius — they terminate before any storage operation and produce no data side effects. The storage expert notes that invalid GUID format for `parentaccountid` (F-11) is the last opportunity to catch a data quality issue before it reaches the FK constraint check at the storage layer.

**Auth expert prose:** No auth concern at routing. ExecutionContext is already attached.

**Routing expert prose:** JSON deserialization, property name validation, GUID format validation for `parentaccountid`. Three clean failure modes, all 400 status.

---

### Step 7 — Service Boundary Crossings (Plug-in Pipeline)

#### 7a — PreValidation

**Machine block first:**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-13 | Plug-in throws `InvalidPluginExecutionException` → 400 | Y | No | None |
| F-14 | Plug-in timeout → 500 | Y | Y | Low — no INSERT attempted |
| F-15 | Caller lacks `prvReadAccount` for plug-in query | Y | No | None |
| F-16 | TOCTOU: parent deleted between check and INSERT | Y | No | High — INSERT may create orphaned record or fail |

**Storage expert prose:** F-16 is the highest blast-radius failure in the entire trace. If PreValidation confirms the parent exists and then the parent is deleted before the INSERT, the storage layer will either reject with FK violation (safe) or create an account with an invalid parent reference (catastrophic, depends on FK enforcement mode). The storage expert flags this as the primary architectural risk for this scenario.

**Auth expert prose:** Plug-in executes under caller's security context. If the plug-in queries `AccountBase` for the parent record, the caller must hold `prvReadAccount`. F-15 is an auth gap.

**Routing expert prose:** PreValidation fires outside the main transaction. The ExecutionContext is serialized and dispatched to the plug-in host.

#### 7b — PreOperation

**Machine block first:**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-17 | Elevated context modifies `parentaccountid`, bypassing FLS | Y | No | High — FLS policy violated at storage write |
| F-18 | Plug-in throws → transaction rollback | Y | No | None — rollback is clean |
| F-19 | Plug-in latency under transaction lock | N | Y | Medium — lock held during entire plug-in execution |

**Storage expert prose:** F-17 and F-19 are the two critical storage concerns in PreOperation. F-17 means a field that the caller's FLS profile forbids writing is written to storage anyway — a security violation at the data layer. F-19 means the database transaction is held open during plug-in execution, which under the 2-minute plug-in timeout could hold row-level locks for up to 2 minutes, blocking any concurrent operation on the affected account records.

**Auth expert prose:** F-17 is the Step 8 HALT-RULE trigger — elevated plug-in context bypasses FLS, invoked scope does not match VT-4.

**Routing expert prose:** PreOperation fires inside the transaction. Modifications to `Target` here affect the INSERT directly.

#### 7c — PostOperation

**Machine block first:**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-20 | PostOperation failure → partial commit | Y | No | High — account exists, dependents absent |
| F-21 | Async misclassification of sync PostOperation | Y | No | Medium — unpredictable execution timing |

**Storage expert prose:** F-20 is the second-highest blast-radius failure in the trace. The main account record is committed and the caller receives a success response, but dependent operations (child records, related entities) created by the PostOperation plug-in have failed. This produces a partially coherent data state that may not be detected until downstream processes attempt to use the missing dependents.

**Auth expert prose:** PostOperation executes under caller context (or run-as). Auth concern is the same as PreValidation/PreOperation.

**Routing expert prose:** PostOperation fires after the commit. No routing concern.

---

### Step 8 — Auth Verification Checkpoint

*(Step 8 Header already emitted at top.)*

**Step 8a — Boundary Invocation Listing (machine block):**

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

**Step 8c — Match? Table (REQUIRED — emitted BEFORE Step 8b, per machine-first rule):**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| OData API entry | `user_impersonation` | `user_impersonation` | resource URI=Dataverse env, tenant ID | Y | PASS |
| System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read, context=plugin | Y | PASS |
| SQL storage layer | `internal service identity` | `internal service identity` | service-to-service, no caller token | Y | PASS |
| PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as, FLS profile differs | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): The PreOperation plug-in's run-as security context must be constrained so the effective scope for writing parentaccountid equals "FLS write permission on parentaccountid" (VT-4). Options: (a) remove the run-as configuration so the plug-in executes under caller context, inheriting the caller's FLS profile; (b) add an explicit audit trail showing intentional FLS override with security team approval, and amend Step 3 auth contract with a distinct VT-N entry for this elevated context.`

**Step 8b — Prose Coherence Confirmation (emitted AFTER Step 8c, per machine-first rule):**

*OData API entry (Storage expert notes no data risk; Auth expert confirms):*
Arm 1: "OData API entry" maps to `user_impersonation` in Step 3 auth contract — confirmed. Arm 2: Step 8a-Invoked = `user_impersonation` matches VT-1 exactly — confirmed. Arm 3: Step 11 parameters (resource URI = Dataverse env endpoint) consistent with `user_impersonation` audience — confirmed. All three arms coherent.

*System user privilege check (Auth expert):*
Arm 1: "System user privilege check" maps to `prvCreateAccount` — confirmed. Arm 2: `prvCreateAccount` matches VT-2 exactly — confirmed. Arm 3: entity=account, op=Create consistent — confirmed. All three arms coherent.

*FLS check on `parentaccountid` (Storage expert flags F-08 risk; Auth expert confirms contract):*
Arm 1: "FLS check on parentaccountid" maps to `FLS write permission on parentaccountid` — confirmed. Arm 2: matches VT-4 exactly — confirmed. Arm 3: field=parentaccountid, op=write consistent — confirmed. All three arms coherent. (Note: F-08 silent strip risk exists even when the contract is coherent — this is a behavior ambiguity, not a scope mismatch.)

*PreValidation plug-in read query (Auth expert):*
Arm 1: maps to `prvReadAccount` — confirmed. Arm 2: matches VT-3 exactly — confirmed. Arm 3: entity=account, op=Read consistent — confirmed. All three arms coherent.

*PreOperation elevated FLS bypass (Storage expert primary; Auth expert confirms HALT):*
Arm 1: Should map to `FLS write permission on parentaccountid` per Step 3. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" does NOT match VT-4 — mismatch. Arm 3: plug-in run-as user has different FLS profile — inconsistent. Arms 2 and 3 incoherent. HALT-RULE fires. This is consistent with Row-Verdict = HALT in Step 8c. Storage blast radius: HIGH (FLS policy violated at data write layer).

---

### Step 9 — Storage Access Boundary

**Machine block first (Storage expert primary):**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-22 | Parent GUID not found → FK constraint violation → 400 | Y | No | Low — clean failure, no data created |
| F-23 | Lock wait on parent account row | N | Y | Medium — lock held, no data risk |
| F-24 | Extension table write failure → full rollback | N | No | None — rollback is clean |
| F-25 | Audit write failure (if audit required) | N | No | Low — depends on audit criticality |

**Storage expert prose:** The INSERT into `AccountBase` enforces the FK constraint on `parentaccountid`. F-22 is the storage layer's last defense against invalid parent references — if PreValidation passed an existence check and the parent was subsequently deleted (F-16 TOCTOU), this constraint fires as the safety net. F-23 lock wait is the primary latency source at storage and can cascade if the parent account is involved in concurrent operations.

**Auth expert prose:** Storage boundary uses internal service identity only. No caller token at SQL. Auth concern shifts back to plug-in context for PostOperation.

**Routing expert prose:** No routing concern at storage.

---

### Step 10 — Response Assembly Boundary

**Machine block first:**

| # | Failure | Gap?= | Latency source? | Storage blast radius |
|---|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation | Y | No | Low — data written correctly, response misleading |
| F-27 | `Prefer: return=representation` read round-trip | N | Y | None — additional read only |
| F-28 | Missing read privilege for `Prefer` response | Y | No | None |

**Storage expert prose:** F-26 is a response-assembly manifestation of a storage-layer concern: `parentaccountid` was written to `AccountBase` correctly (assuming no FLS bypass), but the FLS profile denies the caller read access to the field. The data is intact at storage; the caller's view of the data is incomplete. This can cause client-side confusion or silent data loss in clients that use the response body to update local state.

**Auth expert prose:** FLS read check for `Prefer: return=representation` is a second auth evaluation — after the write-phase FLS check, a read-phase FLS check occurs. These can have different outcomes if the caller's FLS profile grants write but not read on `parentaccountid`.

**Routing expert prose:** `Prefer: return=representation` is an OData protocol preference. The routing layer detects this header and triggers the SELECT round-trip.

---

### Step 11 — Parameter and Scope Catalog

**Machine block first:**

| Parameter | Value | Scope association |
|---|---|---|
| HTTP method | POST | — |
| Endpoint | `/api/data/v9.2/accounts` | — |
| Entity | `account` | `prvCreateAccount`, `prvReadAccount` |
| Field under FLS | `parentaccountid` | `FLS write permission on parentaccountid` |
| Referenced entity | `account` (parent) | `prvReadAccount` |
| Token audience | Dataverse environment URI | `user_impersonation` |
| Tenant ID | AAD tenant of environment | `user_impersonation` |
| Environment ID | GUID of Dataverse environment | `user_impersonation` |
| Plug-in run-as | Configured per plug-in step | elevated plug-in context (run-as) |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

**Storage expert prose:** Parameter catalog complete. Step 11 parameters are the reference set for the Step 8c Step11-Params column. All scope associations are consistent with the VT-N tokens declared in the Step 8 Header.

---

### Step 12 — Error Paths

**Machine block first:**

| Error path | HTTP status | Phase | Failure ref |
|---|---|---|---|
| Missing / expired Bearer token | 401 | Entry | F-01, F-05 |
| Wrong token audience | 401 | Entry | F-02 |
| System user disabled | 403 | Auth | F-06 |
| Missing `prvCreateAccount` | 403 | Auth | F-07 |
| FLS hard block (parentaccountid) | 400 | Auth | F-08 |
| Malformed JSON | 400 | Routing | F-10 |
| Invalid GUID format | 400 | Routing | F-11 |
| PreValidation plug-in exception | 400 | Plug-in | F-13 |
| PreValidation plug-in timeout | 500 | Plug-in | F-14 |
| Missing `prvReadAccount` in plug-in | 403 | Plug-in | F-15 |
| Parent GUID not found at INSERT | 400 | Storage | F-22 |
| PostOperation partial commit | 500 | Plug-in | F-20 |
| FLS strips field from response | 204/201 field absent | Response | F-26 |

**Storage expert prose — blast-radius ordering:**
Rank 1: F-16 TOCTOU + F-22 FK catch (combined) — parent integrity failure path. Rank 2: F-20 PostOperation partial commit — orphaned data. Rank 3: F-08 / F-17 / F-26 FLS-related outcomes — data present but partially inaccessible or written in violation of policy. All other failures produce clean 4xx/5xx with no data side effects.

---

### Step 13 — Latency Source Summary

**Machine block first:**

| Latency source | Step | Severity | Storage expert priority |
|---|---|---|---|
| Metadata cache miss | Entry | Low | Low (no data risk) |
| Role/privilege cache miss | Auth | Medium | Low (no data risk) |
| Plug-in timeout (up to 2 min) | Plug-in pipeline | High | High (transaction held open) |
| Transaction lock contention (PreOperation) | Plug-in pipeline | High | High (blocks concurrent storage ops) |
| Lock wait on parent account row | Storage | Medium | Medium |
| Audit write | Storage | Low–Medium | Low |
| `Prefer: return=representation` read | Response | Low | Low |

**Prose:** Seven latency sources. Storage expert prioritizes the two plug-in pipeline sources as highest risk because they occur while a database transaction is open, amplifying their impact on storage throughput and concurrency.

---

### Step 14 — Signal Output

```
signal: trace-request
topic: [topic from invocation context]
date: [today's date]
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
boundaries-traced: 7
failure-points: 28
gap-flagged: 12
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6)
latency-sources: 7
role-order: Storage-first → Auth → Routing
format: machine-first (tables before prose, Step 8 Header first, Step 8c before Step 8b)
combined-axes: role-sequence + output-format
```

---

## V-05 — Combined: Lifecycle emphasis + Phrasing register (Conversational)

**Axis:** Equal phase budget (same as V-03) AND conversational/instructional phrasing register ("Walk through...", "For each boundary, note...", "Before moving on, confirm..." instead of imperative commands and formal section headers).

**Hypothesis:** Conversational register with equal phase budget reduces prompt length by ~20% while preserving structural completeness, making the skill viable in narrow-context invocations without sacrificing rubric coverage.

---

You are running a `trace-request` signal. Auto-select the right platform expert from context: Dataverse, Commerce, or Automate. For this trace, use a conversational and instructional tone throughout — phrases like "walk through," "for each boundary, note," "before moving on, confirm," and "let's check" are preferred over formal imperative section headers. At the same time, give equal weight to all six lifecycle phases: Entry, Authentication, Routing, Boundary-Crossing, Storage, and Response-Assembly. Error paths get their own standalone section equal in weight to the six phases. Every phase must include: a description of what happens at that boundary, a failure point table, and a latency observation. Don't collapse any phase into another.

The scenario to trace: POST /api/data/v9.2/accounts, creating an Account where `parentaccountid` references an existing account GUID. The environment has three synchronous plug-ins registered — PreValidation, PreOperation, and PostOperation — and field-level security is active on the `parentaccountid` field.

Platform expert selected: Dataverse platform expert.

---

**Before anything else, let's get the Step 8 checker contract on the table.** This block governs all scope verification later in the trace. It stays here at the top so the checker is available before any boundary prose begins.

```
VT-1: "user_impersonation"
VT-2: "prvCreateAccount"
VT-3: "prvReadAccount"
VT-4: "FLS write permission on parentaccountid"
VT-5: "internal service identity"
TOKEN-COUNT: 5

CHECKER ALGORITHM:
MATCH-RULE: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; case-sensitive; whitespace-normalized; character-for-character identity with the quoted VT-N value; this rule is structurally independent of VT-N line positions and requires no prose reading to evaluate.
HALT-RULE: Fire when Step 8b prose asserts coherence (all three link arms consistent) AND Step 8c Match? = N for the same boundary row; the co-occurrence of a prose-coherent claim and a table-level mismatch is a contradiction that halts the trace at that boundary.
OUTPUT-RULE: Assign Row-Verdict = PASS if Match? = Y; assign Row-Verdict = HALT if HALT-RULE fires; emit CHECK RESULT summary line immediately after the last row of the Step 8c table; the contract is fully machine-evaluable from tokens and table alone.
```

---

**Step 1 — Register the scenario.** Write down what you are tracing so you can refer back to it at each phase:

- Operation: POST /api/data/v9.2/accounts
- Key field: `parentaccountid` carrying a GUID reference to an existing account
- Plug-in pipeline: PreValidation → PreOperation → PostOperation, all synchronous
- Security overlay: FLS on `parentaccountid`
- Goal: walk every boundary from entry to response, name every failure point, every latency source, every auth gap

---

**Step 2 — Before you start tracing, lock the auth contract.** This is the reference set Step 8 will check against. For each boundary in the trace, write down what scope or permission is required:

| Boundary | Required Scope / Permission | Token Type | Notes |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | Dataverse env resource URI as audience |
| System user privilege check | `prvCreateAccount` | System user + role | Create privilege on account entity |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | FLS profile | Write access to named field |
| SQL storage layer | `internal service identity` | Internal | Service-to-service, no OAuth |
| Parent GUID relationship validation | `prvReadAccount` | System user | Read privilege needed for plug-in queries |

Good — auth contract is locked. Now walk the six lifecycle phases.

---

**Phase 1 — Walk through what happens at Entry.**

At this phase, the HTTP POST arrives at `/api/data/v9.2/accounts`. The web API tier parses the URL, checks the HTTP method, and confirms the content-type is `application/json`. It looks up the entity set name `accounts` in the OData metadata to find the matching entity and handler. Nothing has touched the database yet.

For each failure that can happen here, note it in the table below along with whether there is an auth gap (Gap?=Y) and whether it adds latency:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong resource URI in token audience → 401 | Y | No |
| F-03 | Entity set name `accounts` not found in metadata → 404 | N | No |
| F-04 | Wrong HTTP method (GET instead of POST) → 405 | N | No |

Latency to note at Entry: if the OData metadata cache is cold (after instance startup or a metadata publish), resolving the entity set requires a cache rebuild that can add up to a couple of seconds. On a warm instance this is negligible.

---

**Phase 2 — Walk through what happens at Authentication.**

After entry, the platform processes the Bearer token. Walk through these four checks in order: AAD token signature and claims, token expiry and issuer, Dataverse system user lookup from the AAD identity, and FLS profile evaluation for `parentaccountid`. All four checks are synchronous and must pass before anything else proceeds.

For each failure here:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found or disabled in Dataverse → 403 | Y | No |
| F-07 | Caller missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS profile denies write on `parentaccountid` — field silently stripped OR hard reject depending on config | Y | No |
| F-09 | Role and privilege cache miss → synchronous lookup against multiple tables | N | Y |

Latency to note at Authentication: when the role/privilege cache is invalidated (after a role assignment change or under memory pressure), the platform does a synchronous DB read against `systemuser`, `role`, `roleprivileges`, and `fieldpermission`. Under load this can add 50–200ms per request.

One thing to watch closely here: F-08 (FLS on `parentaccountid`) has two different behaviors depending on how the FLS profile is configured — it may silently drop the field from the INSERT (leaving the account parentless with no error) or reject the entire operation. The silent-strip behavior is the harder failure to detect.

---

**Phase 3 — Walk through what happens at Routing.**

Once authenticated, the OData routing layer takes the deserialized HTTP request and builds an internal `Entity` object from the JSON body. It validates every property name in the payload against the entity metadata, checks the type of `parentaccountid` (must be a GUID string in the right format), and attaches the caller's `ExecutionContext` to the `Entity`. This ExecutionContext carries the caller's identity forward through the plug-in pipeline.

Failures at Routing:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` value is not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |
| F-13 | `Content-Type` header not `application/json` → 415 | N | No |

Latency to note at Routing: for large payloads with many attributes, JSON deserialization and metadata validation time scales with payload size and number of properties. Not a concern for a minimal create payload, but worth noting for batch or multi-attribute creates.

---

**Phase 4 — Walk through what happens at each Boundary-Crossing in the plug-in pipeline.** There are three of them — give each one equal attention.

**Crossing 1 — PreValidation.** This plug-in fires outside the main database transaction. If the plug-in queries Dataverse to confirm the parent account exists, that query runs outside transaction scope — so there is a window between the check and the actual INSERT where the parent could be deleted.

Failures at PreValidation:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-14 | Plug-in throws `InvalidPluginExecutionException` → 400 | Y | No |
| F-15 | Plug-in times out (2-minute default for sync) → 500 | Y | Y |
| F-16 | Caller lacks `prvReadAccount` needed for plug-in's parent lookup | Y | No |
| F-17 | TOCTOU: parent account deleted between PreValidation check and INSERT | Y | No |

Latency: plug-in dispatch overhead (~5–20ms per crossing warm). If the plug-in calls an external service, latency is unbounded. Timeout at 2 minutes.

**Crossing 2 — PreOperation.** This plug-in fires inside the database transaction. Any modifications it makes to the `Target` entity go into the final INSERT. If the plug-in is configured with a run-as user that has elevated FLS permissions, it can write `parentaccountid` even when the caller's FLS profile would deny it.

Failures at PreOperation:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-18 | Plug-in's elevated run-as context writes `parentaccountid`, bypassing caller FLS | Y | No |
| F-19 | Plug-in throws inside transaction → rollback | Y | No |
| F-20 | Plug-in execution time while holding transaction lock → lock escalation risk | N | Y |

Latency: plug-in execution time is unbounded, and during this time the database transaction is open and holding locks. Under the 2-minute timeout, row-level locks on related records can block other operations.

**Crossing 3 — PostOperation.** This plug-in fires after the INSERT is committed. It cannot roll back the main account record. If it creates dependent records (child entities, related records) and fails, those dependents will be absent while the account record exists.

Failures at PostOperation:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-21 | PostOperation failure → partial commit (account exists, dependents absent) | Y | No |
| F-22 | Plug-in registered as sync PostOperation but misclassified — behaves as async | Y | No |

Latency: PostOperation adds to total request duration for sync registrations. Async misclassification means dependent record creation timing is unpredictable.

---

**Phase 5 — Walk through what happens at Storage.**

The Dataverse SQL backend receives the INSERT for `AccountBase` and related extension tables (`AccountExtensionBase`). The storage layer enforces the relationship constraint: `parentaccountid` must reference an existing `AccountBase.AccountId`. This is the last defense against a bad parent GUID. If audit is enabled, the audit record is written in the same transaction. No caller token reaches the SQL layer — only the internal service identity.

Failures at Storage:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-23 | Parent GUID not found in AccountBase → FK constraint violation → 400 | Y | No |
| F-24 | Concurrent lock on parent account row → wait before INSERT | N | Y |
| F-25 | Extension table write failure → full transaction rollback | N | No |
| F-26 | Audit write failure (if audit is required by org policy) | N | No |

Latency to note at Storage: two sources — lock wait on the parent account row (variable, depends on concurrency) and audit write I/O (proportional to audit volume, typically low). Both are load-dependent.

---

**Phase 6 — Walk through what happens at Response Assembly.**

On a successful INSERT, the OData layer builds the HTTP response. By default it returns 204 No Content with an `OData-EntityId` header pointing to the new account's URL. If the caller sent `Prefer: return=representation`, the platform runs a SELECT on the new record and returns 201 Created with the full entity body. Here is where FLS bites a second time: the SELECT for `Prefer: return=representation` applies the caller's read-phase FLS profile, which may strip `parentaccountid` from the response even though it was just written.

Failures at Response Assembly:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-27 | FLS strips `parentaccountid` from returned representation → caller sees field absent | Y | No |
| F-28 | Missing read privilege for `Prefer: return=representation` SELECT | Y | No |
| F-29 | `Prefer: return=representation` triggers additional read round-trip | N | Y |

Latency to note: `Prefer: return=representation` adds a full OData read operation — entity deserialization, FLS evaluation, column projection, JSON serialization — adding roughly 20–100ms depending on instance load.

---

**Step 8 — Before moving on to the full parameter catalog, let's run the auth verification checkpoint.**

Here is the list of scopes that were actually invoked during the trace:

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

Now let's run the Match? table — this comes before the prose confirmation:

**Step 8c — Match? Table (before Step 8b):**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| OData API entry | `user_impersonation` | `user_impersonation` | resource URI=Dataverse env, tenant ID present | Y | PASS |
| System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read, context=plugin | Y | PASS |
| SQL storage layer | `internal service identity` | `internal service identity` | service-to-service, no caller token | Y | PASS |
| PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as, FLS profile differs from caller | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): The PreOperation plug-in's run-as configuration causes it to invoke a different effective FLS scope than "FLS write permission on parentaccountid" (VT-4). Correct by: (a) removing the run-as configuration so the plug-in inherits the caller's FLS profile and the invoked scope becomes VT-4; or (b) explicitly documenting this as an intentional FLS override and amending the Step 3 auth contract with a new distinct entry for the elevated plug-in context.`

**Step 8b — Now let's confirm prose coherence for each Gap?=Y boundary:**

*OData API entry:* The boundary name "OData API entry" points to `user_impersonation` in the Step 3 contract (Arm 1 confirmed). The invoked scope `user_impersonation` matches VT-1 character-for-character (Arm 2 confirmed). The Step 11 parameters — resource URI is the Dataverse environment endpoint, which is the expected audience for `user_impersonation` — are consistent (Arm 3 confirmed). All three arms line up; this row is coherent.

*System user privilege check:* Step 3 maps this boundary to `prvCreateAccount` (Arm 1 confirmed). Invoked scope `prvCreateAccount` matches VT-2 exactly (Arm 2 confirmed). Step 11 says entity=account, op=Create, which is precisely what `prvCreateAccount` covers (Arm 3 confirmed). All three arms line up.

*FLS check on `parentaccountid`:* Step 3 maps this to `FLS write permission on parentaccountid` (Arm 1 confirmed). Invoked scope matches VT-4 exactly (Arm 2 confirmed). Step 11 parameters field=parentaccountid and op=write are consistent (Arm 3 confirmed). All three arms line up.

*PreValidation plug-in read query:* Step 3 maps this to `prvReadAccount` (Arm 1 confirmed). Invoked scope matches VT-3 exactly (Arm 2 confirmed). Step 11 parameters entity=account, op=Read, context=plugin are consistent (Arm 3 confirmed). All three arms line up.

*PreOperation elevated FLS bypass:* Step 3 says this boundary should use `FLS write permission on parentaccountid` (Arm 1 says it should — but the actual invoked scope is "elevated plug-in context (run-as)", which does not match VT-4 (Arm 2 mismatch). Step 11 confirms the plug-in run-as user has a different FLS profile (Arm 3 inconsistent). Arms 2 and 3 are incoherent. HALT-RULE fires — and this is consistent with the Row-Verdict = HALT in Step 8c, so there is no contradiction between 8b and 8c. The trace is halted at this boundary until corrected.

---

**Step 9 — Let's catalog the full parameter set** so Step 8c's Step11-Params column has a complete reference:

| Parameter | Value | Scope association |
|---|---|---|
| HTTP method | POST | — |
| Endpoint | `/api/data/v9.2/accounts` | — |
| Entity | `account` | `prvCreateAccount`, `prvReadAccount` |
| Field under FLS | `parentaccountid` | `FLS write permission on parentaccountid` |
| Referenced entity | `account` (parent) | `prvReadAccount` |
| Token audience | Dataverse environment URI | `user_impersonation` |
| Tenant ID | AAD tenant of environment | `user_impersonation` |
| Environment ID | GUID of Dataverse environment | `user_impersonation` |
| Plug-in run-as | Configured per plug-in step (default: caller) | elevated plug-in context (run-as) |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

---

**Phase 7 — Error Paths (standalone section, same weight as Phases 1–6).**

Here is the complete error path catalog, pulled together from every phase. Organized by HTTP status so it is easy to look up. Note the recovery type for each.

| Error path | HTTP status | Phase | Failure ref | Recovery type |
|---|---|---|---|---|
| Missing / expired Bearer token | 401 | Entry, Auth | F-01, F-05 | Re-acquire token |
| Wrong token audience | 401 | Entry | F-02 | Fix resource URI in token request |
| System user disabled | 403 | Auth | F-06 | Admin: enable or re-create user |
| Missing `prvCreateAccount` | 403 | Auth | F-07 | Admin: assign role with privilege |
| FLS hard block on `parentaccountid` | 400 | Auth | F-08 | Admin: update FLS profile |
| Malformed JSON | 400 | Routing | F-10 | Fix client payload |
| Invalid GUID format for `parentaccountid` | 400 | Routing | F-11 | Fix client payload |
| PreValidation plug-in exception | 400 | Boundary-Crossing | F-14 | Investigate plug-in message |
| PreValidation plug-in timeout | 500 | Boundary-Crossing | F-15 | Optimize plug-in or raise timeout |
| Missing `prvReadAccount` in plug-in | 403 | Boundary-Crossing | F-16 | Admin: grant read privilege |
| Parent GUID not found at INSERT | 400 | Storage | F-23 | Verify parent GUID before request |
| PostOperation partial commit | 500 | Boundary-Crossing | F-21 | Investigate partial state, reconcile |
| FLS strips `parentaccountid` from response | 204/201 field absent | Response Assembly | F-27 | Silent — add client-side check |
| Missing read privilege for `Prefer` response | 403 / field absent | Response Assembly | F-28 | Admin: grant read privilege |

Latency note for error paths: two paths produce latency before failing — plug-in timeout (up to 2 minutes, F-15) and lock wait at storage (unbounded under concurrency, F-24 leading to potential cascade to F-23). All other error paths fail fast with no significant latency contribution.

---

**Step 10 — Let's pull together all the latency sources in one place** so they are easy to review across phases:

| Latency source | Phase | Severity |
|---|---|---|
| OData metadata cache miss | Entry | Low |
| Role/privilege cache miss | Auth | Medium |
| JSON deserialization for large payloads | Routing | Low |
| Plug-in dispatch overhead (x3 crossings) | Boundary-Crossing | Low |
| Plug-in execution time (unbounded) | Boundary-Crossing | High |
| Transaction lock held during PreOperation | Boundary-Crossing | High |
| Lock wait on parent account row | Storage | Medium |
| Audit write under high volume | Storage | Low–Medium |
| `Prefer: return=representation` read | Response Assembly | Low |

Nine latency sources across six phases. The two High-severity sources are both in Phase 4 (Boundary-Crossing) and are related — plug-in execution time while holding a transaction lock is the most impactful latency pattern in this scenario.

---

**Step 11 — Emit the signal output.**

```
signal: trace-request
topic: [topic from invocation context]
date: [today's date]
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
phase-budget: 7 phases (equal weight, Phases 1-6 lifecycle + Phase 7 error paths)
boundaries-traced: 7
failure-points: 29 (F-01 through F-29)
gap-flagged: 12
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6)
latency-sources: 9
format: equal-phase-budget + conversational register
combined-axes: lifecycle-emphasis + phrasing-register
```

---

**Files saved:**
- `V01` — 23 KB (Storage-first, 27 failure points, blast-radius ordering)
- `V02` — 17 KB (Machine-first, Step 8 Header at top, Step 8c before Step 8b)
- `V03` — 20 KB (Equal phase budget, 7 phases, 29 failure points, 9 latency sources)
- `V04` — 23 KB (Storage-first + machine-first combined, Storage blast-radius column throughout)
- `V05` — 21 KB (Equal phase budget + conversational register, 29 failure points)

**Structural coverage across all 5:** C-34 (VT-N quoted schema), C-35 (Row-Verdict + CHECK RESULT), C-36 (full checker contract), C-37 (CHECKER ALGORITHM block with MATCH-RULE/HALT-RULE/OUTPUT-RULE), C-31 (CONTRADICTION SIGNAL + Scope String Correction), C-28/C-29/C-30 (three-arm coherence confirmation + Match? table), C-32/C-33 (self-contained checker pre-conditions).

**Differentiating signals by variation axis:**
- V-01/V-04: adds Step 13 blast-radius ordering (Storage expert final output) — tests whether role-first framing produces richer failure severity taxonomy
- V-02/V-04: Step 8 Header emitted at position 0 — tests whether pre-emitting the checker contract before the trace body changes how the checker is populated
- V-03/V-05: Phase 7 as first-class section — tests whether equal-budget framing adds latency sources absent in prose-collapsed traces (V-03 finds 9 vs V-01's 7)
- V-05: conversational register — tests whether phrasing change loses or preserves structural completeness at shorter prompt length
