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
| OData API entry | `user_impersonation` on Dataverse resource | Bearer (AAD) | Delegated or app-only |
| Plugin execution context | Caller's system user privileges propagated | Internal system token | No separate scope; inherits caller |
| FLS check on `parentaccountid` | FLS profile read/write permission for caller | System user record | Checked against field security profile |
| SQL storage layer (Dataverse DB) | Internal service identity | Internal (no OAuth) | Service-to-service, no caller token |
| Relationship validation (parent GUID lookup) | Read privilege on `account` entity for caller | Bearer (AAD) / system user | Must have `prvReadAccount` |

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

Emit the signal artifact header:

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

