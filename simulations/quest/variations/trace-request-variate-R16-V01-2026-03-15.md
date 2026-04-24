## V-01 — Single axis: Inertia framing (Common-skip explicit labeling)

**Axis:** At every boundary section, an explicit COMMON SKIP: block names what developers typically omit at that boundary, followed by REQUIRED: forcing the trace to walk the skipped surface.

**Hypothesis:** Explicit skip labeling increases model probability of surfacing omitted failure surfaces and prevents happy-path bias where only the primary auth flow is traced.

---

You are executing a `trace-request` signal for the following scenario. Auto-select the appropriate platform expert role from context: Dataverse / Commerce / Automate. This trace applies inertia framing: every boundary section opens with a COMMON SKIP: block naming what developers typically omit, followed by a REQUIRED: block forcing the trace to walk the skipped surface.

**Scenario:** POST /api/data/v9.2/accounts — Create Account with `parentaccountid` referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on `parentaccountid`.

**Platform Expert Selected:** Dataverse platform expert.

---

### Step 1 — Scenario Registration

COMMON SKIP at scenario registration: Developers skip registering the FLS overlay as a distinct trace concern — they note the plug-ins but omit that FLS is an independent security surface evaluated separately at the caller level and again at each plug-in boundary.
REQUIRED: Record the FLS overlay as a named trace target with its own boundary entries.

- **Operation:** POST /api/data/v9.2/accounts
- **Payload key field:** `parentaccountid` (GUID reference to existing account)
- **Plug-in pipeline:** PreValidation → PreOperation → PostOperation (all synchronous)
- **Security overlay:** Field-level security (FLS) on `parentaccountid` — NAMED TRACE TARGET
- **Trace goal:** Hand-compile every boundary crossing, failure point, latency source, and auth gap from entry to response, with explicit skip surfaces surfaced at each boundary.

---

### Step 2 — Role Declaration

COMMON SKIP at role declaration: Developers select a single "API expert" role and skip the storage-layer perspective, missing cascade dependency and blast-radius ordering.
REQUIRED: Declare distinct Auth, Routing, and Storage expert perspectives. All three must contribute findings.

**Platform Expert:** Dataverse platform expert (all three sub-roles active).
**Inertia framing rule:** Each boundary step opens with COMMON SKIP: + REQUIRED: before any analysis is emitted.

---

### Step 3 — Authentication Contract

COMMON SKIP at auth contract: Developers list the Bearer token scope and the create privilege, then stop — they skip FLS as a separate auth surface and skip the internal service identity for the SQL layer entirely.
REQUIRED: Enumerate all five distinct auth surfaces including FLS profile and internal service identity.

Lock the full auth contract before tracing any boundary:

| Boundary | Required Scope / Permission | Token Type | Notes |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | Environment resource URI audience |
| System user privilege check | `prvCreateAccount` | System user + role | Create privilege on account entity |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | FLS profile | Write permission on named field — separate from privilege check |
| SQL storage layer | `internal service identity` | Internal | Service-to-service, no OAuth, no caller token |
| Parent GUID relationship validation | `prvReadAccount` | System user | Read privilege on account entity (required in plug-in context) |

**Auth contract locked.** Step 8 verifies every invoked scope against this set.

---

### Step 4 — Entry Point

COMMON SKIP at entry: Developers check for Bearer token presence, then skip the token audience validation — they assume any valid AAD token will work on any Dataverse environment.
REQUIRED: Trace token audience (resource URI) as a distinct failure surface separate from token validity.

The HTTP POST arrives at `/api/data/v9.2/accounts`. The entry point performs: HTTP method check, content-type validation (`application/json`), URL parsing to extract entity set name `accounts`, and immediate token presence check (401 before any routing if absent).

**Failure points at entry:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong token audience (incorrect environment resource URI) → 401 | Y | No |
| F-03 | Entity set name `accounts` not found in OData metadata → 404 | N | No |
| F-04 | OData metadata cache miss on cold start → routing delay | N | Y |

---

### Step 5 — Authentication Boundary

COMMON SKIP at auth: Developers assume FLS is a single check at the API layer and skip FLS re-evaluation at the plug-in modification step. They confirm the caller has `prvCreateAccount` and stop.
REQUIRED: Trace FLS at every boundary where `parentaccountid` is accessed or written — including PreOperation modification context.

After the routing layer accepts the request, the platform authenticates the caller:

1. AAD token signature, expiry, audience, issuer validation.
2. Dataverse system user resolution from AAD OID/UPN — disabled or missing = 403.
3. Privilege check: caller must hold `prvCreateAccount` at a scope covering the target business unit.
4. **FLS pre-check on `parentaccountid`:** The platform evaluates the caller's FLS profile for write access to `parentaccountid`. FLS denial can result in silent field strip or hard 400 depending on configuration. This is an authorization gap because the behavior varies per environment configuration.

**Failure points at authentication:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found or disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS profile denies write on `parentaccountid` — silent strip vs. hard reject ambiguity | Y | No |
| F-09 | Role/privilege cache miss → synchronous DB lookup latency | N | Y |

---

### Step 6 — Routing Boundary

COMMON SKIP at routing: Developers validate JSON structure and skip validating GUID format for lookup fields — they assume the ORM layer will handle type mismatches.
REQUIRED: Trace GUID format validation on `parentaccountid` as a distinct routing failure surface.

The OData routing layer resolves `accounts` to the `account` entity metadata, constructs the Create request handler, deserializes the JSON body into an internal `Entity` object, and validates all property names and types against entity metadata. The `parentaccountid` value is validated as a GUID format here. The caller's `ExecutionContext` is attached to the `Entity` object and propagates through the plug-in pipeline.

**Failure points at routing:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` value is not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |

---

### Step 7 — Service Boundary Crossings (Plug-in Pipeline)

COMMON SKIP at plug-in pipeline: Developers check that the plug-in fires and moves on — they skip tracing the security context propagation through each crossing, missing the elevated run-as context divergence at PreOperation.
REQUIRED: Trace the security context (caller vs. run-as) at each plug-in crossing, and trace FLS re-evaluation at any crossing where `parentaccountid` is written.

#### 7a — PreValidation Plug-in

COMMON SKIP at PreValidation: Developers skip the TOCTOU risk — they see the plug-in validates the parent account exists and assume that covers the storage layer check.
REQUIRED: Trace TOCTOU explicitly: PreValidation fires before the database transaction, so any validation of the parent GUID here is subject to a race with concurrent deletes.

**PreValidation fires before any database transaction is opened.** Security context: caller's context by default (unless run-as user configured on the step). If the plug-in queries Dataverse to validate the parent account, that query runs outside the main transaction and is subject to TOCTOU.

**Failure points — PreValidation:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-13 | Plug-in throws `InvalidPluginExecutionException` → 400 with message | Y | No |
| F-14 | Plug-in timeout (2-min default) → 500 / pipeline abort | Y | Y |
| F-15 | Plug-in read of parent account — caller lacks `prvReadAccount` → plug-in 403 | Y | No |
| F-16 | TOCTOU: parent account deleted after PreValidation check but before INSERT | Y | No |

#### 7b — PreOperation Plug-in

COMMON SKIP at PreOperation: Developers confirm the plug-in fires inside the transaction and stop — they skip the FLS bypass risk when the plug-in runs under an elevated (run-as) context that has a different FLS profile than the caller.
REQUIRED: Trace FLS re-evaluation at PreOperation explicitly: if the plug-in modifies `parentaccountid` under an elevated context, the caller's FLS restriction is bypassed — this is F-17 and the HALT boundary.

**PreOperation fires inside the database transaction.** Security context: may diverge from caller if a run-as user is configured on this step. If the plug-in adds or modifies `parentaccountid`, and the run-as user has a broader FLS profile than the caller, the caller's FLS restriction is bypassed — the write proceeds under the run-as scope, not the caller's scope.

**Failure points — PreOperation:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-17 | Plug-in modifies `parentaccountid` under elevated run-as context, bypassing caller FLS | Y | No |
| F-18 | Plug-in throws → transaction rollback → 400 | Y | No |
| F-19 | Plug-in latency under transaction lock → lock escalation risk | N | Y |

#### 7c — PostOperation Plug-in

COMMON SKIP at PostOperation: Developers mark PostOperation as "after commit" and assume failure here is recoverable — they skip partial commit risk where the account record exists but dependent operations (child record creation, async workflows) have not been initiated.
REQUIRED: Trace the partial commit surface: PostOperation failure after INSERT leaves the system in an inconsistent state.

**PostOperation fires after the INSERT is committed.** Cannot roll back the main account record. Failures here leave a partial commit: the account exists, but dependent operations triggered by this plug-in have not completed.

**Failure points — PostOperation:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-20 | PostOperation failure → partial commit (account created, dependent op failed) | Y | No |
| F-21 | Async misclassification: plug-in registered as sync PostOperation but behaves async | Y | No |

---

### Step 8 — Auth Verification Checkpoint

COMMON SKIP at Step 8: Developers list the token scopes invoked and confirm they match the declared contract. They skip the PreOperation elevated context boundary entirely — it does not appear in the invocation list because no OAuth scope was checked; it was a run-as context switch.
REQUIRED: Explicitly add the PreOperation elevated context as a distinct boundary row in the invocation list, and evaluate it against VT-4 in the Match? table.

**Step 8 Header — VT# Token Reference Set and Checker Algorithm**

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

COMMON SKIP at Step 8a: Developers list the five OAuth / privilege scopes and stop — they omit the PreOperation run-as context because it was not an OAuth token check.
REQUIRED: List all six boundaries including the PreOperation elevated context row.

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry (Bearer token) | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

---

**Step 8b — Prose Coherence Confirmation (REQUIRED — one paragraph per Gap?=Y boundary)**

COMMON SKIP at Step 8b: Developers write a single confirmation paragraph for the whole checkpoint — they skip per-boundary arm verification and miss the PreOperation boundary mismatch.
REQUIRED: Write one distinct coherence paragraph per Gap?=Y boundary, naming all three link arms explicitly.

*OData API entry (F-01, F-02):*
Arm 1: The boundary name "OData API entry (Bearer token)" maps to `user_impersonation` declared in Step 3 for this boundary — confirmed. Arm 2: Step 8a-Invoked `user_impersonation` matches VT-1: "user_impersonation" exactly — confirmed. Arm 3: Step 11 parameters (resource URI = Dataverse environment endpoint, tenant ID, environment ID) are consistent with the `user_impersonation` scope — the resource URI is the token audience — confirmed. All three arms are coherent.

*System user privilege check (F-06, F-07):*
Arm 1: "System user privilege check" boundary maps to `prvCreateAccount` in Step 3 — confirmed. Arm 2: Step 8a-Invoked `prvCreateAccount` matches VT-2: "prvCreateAccount" exactly — confirmed. Arm 3: Step 11 parameters (entity=account, op=Create) are consistent with `prvCreateAccount` — the privilege is defined for Create on the account entity — confirmed. All three arms are coherent.

*FLS check on `parentaccountid` (F-08):*
Arm 1: "FLS check on parentaccountid" maps to `FLS write permission on parentaccountid` in Step 3 — confirmed. Arm 2: Step 8a-Invoked `FLS write permission on parentaccountid` matches VT-4: "FLS write permission on parentaccountid" exactly — confirmed. Arm 3: Step 11 parameters (field=parentaccountid, op=write) are consistent with the FLS scope string — field and operation named identically — confirmed. All three arms are coherent.

*PreValidation plug-in read query (F-15):*
Arm 1: "PreValidation plug-in read query" maps to `prvReadAccount` in Step 3 — confirmed. Arm 2: Step 8a-Invoked `prvReadAccount` matches VT-3: "prvReadAccount" exactly — confirmed. Arm 3: Step 11 parameters (entity=account, op=Read, context=plugin query) are consistent with `prvReadAccount` — confirmed. All three arms are coherent.

*PreOperation elevated FLS bypass (F-17):*
Arm 1: This boundary should map to `FLS write permission on parentaccountid` per the Step 3 auth contract — the PreOperation plug-in is modifying `parentaccountid`, a field governed by VT-4. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" does NOT match VT-4: "FLS write permission on parentaccountid" — the invoked permission is the run-as user's elevated context, not the caller's FLS profile — mismatch. Arm 3: Step 11 parameters confirm the plug-in run-as user has a different FLS profile than the caller — the scope is inconsistent with VT-4. Arms 2 and 3 are incoherent with Arm 1. All three arms assert a contradiction: prose claims coherence for this boundary under the auth contract, but the invoked scope does not match VT-4. HALT-RULE fires.

---

**Step 8c — Match? Table (REQUIRED — positioned before Step 9)**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| OData API entry | `user_impersonation` | `user_impersonation` | resource URI=Dataverse env endpoint, tenant ID present | Y | PASS |
| System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read, context=plugin | Y | PASS |
| SQL storage layer | `internal service identity` | `internal service identity` | service-to-service, no caller token | Y | PASS |
| PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as user, FLS profile differs from caller | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): The PreOperation plug-in's run-as context must be constrained to the caller's FLS profile for parentaccountid, OR the plug-in must be documented as an intentional FLS bypass with an explicit security exception review. The Step 3 auth contract must be updated to either add a separate scope entry for the elevated plug-in run-as context, or restrict the plug-in step to caller-context execution (no run-as configured) so that the invoked scope at this boundary becomes "FLS write permission on parentaccountid" matching VT-4.`

---

### Step 9 — Storage Access Boundary

COMMON SKIP at storage: Developers confirm the INSERT fires and stop — they skip the relationship constraint validation as a distinct failure surface, and skip the extension table atomicity risk.
REQUIRED: Trace foreign key constraint enforcement on `parentaccountid` and extension table write atomicity as separate storage failure surfaces.

The Dataverse SQL backend receives the INSERT request for `AccountBase`:

1. **Relationship validation:** `parentaccountid` GUID is validated against `AccountBase.AccountId` via foreign key constraint. If the GUID does not exist at INSERT time, the operation fails with a 400 indicating invalid lookup value.
2. **Transaction scope:** The INSERT spans PreOperation and PostOperation in a single transaction. Under high concurrency, row-level locks on the parent account record may cause wait chains.
3. **Extension tables:** Dataverse writes to `AccountBase` (core columns) and `AccountExtensionBase` (custom columns) atomically. Extension table write failure rolls back the entire transaction.
4. **Audit logging:** If audit is enabled for the account entity, an audit record is written in the same transaction — additional I/O latency.

**Failure points at storage:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-22 | Parent GUID not found at INSERT → FK constraint violation → 400 | Y | No |
| F-23 | Lock wait on parent account row under concurrency | N | Y |
| F-24 | Extension table write failure → full transaction rollback | N | No |
| F-25 | Audit write latency under high volume | N | Y |

---

### Step 10 — Response Assembly Boundary

COMMON SKIP at response assembly: Developers verify the 204 is returned and stop — they skip the `Prefer: return=representation` path which adds a read round-trip subject to FLS re-evaluation on the returned payload.
REQUIRED: Trace the `Prefer: return=representation` path as a distinct response assembly surface, including FLS re-evaluation on `parentaccountid` in the returned body.

On successful INSERT, the OData layer assembles the response:

1. Reads the newly created record's primary key (`accountid` GUID) from the INSERT result.
2. Constructs the `OData-EntityId` header: `[base-url]/api/data/v9.2/accounts([new-guid])`.
3. Returns HTTP 204 No Content (default). If caller sent `Prefer: return=representation`, a SELECT on the new record is performed — returning 201 with full entity body, but re-applying FLS on all fields including `parentaccountid`.

**Failure points at response assembly:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation → caller confusion | Y | No |
| F-27 | `Prefer: return=representation` adds read round-trip latency | N | Y |

---

### Step 11 — Parameter and Scope Catalog

COMMON SKIP at parameter catalog: Developers list the endpoint and entity name, then skip the plug-in run-as configuration as a parameter — it is treated as an implementation detail rather than a security-relevant parameter.
REQUIRED: Catalog the plug-in run-as configuration as a named parameter with its scope association.

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
| Plug-in run-as (PreOperation) | Configured run-as user on plug-in step | elevated plug-in context (run-as) — HALT boundary |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check at response |

---

### Step 12 — Error Paths (Complete)

COMMON SKIP at error paths: Developers list 4xx client errors and stop — they skip the silent data anomaly paths (2xx with field stripped, 2xx with partial commit state).
REQUIRED: Enumerate all error path categories including silent data anomalies that return 2xx.

| Error path | HTTP status | Trigger | Failure ref |
|---|---|---|---|
| Missing / expired Bearer token | 401 | Entry | F-01, F-05 |
| Wrong token audience | 401 | Entry | F-02 |
| System user disabled or not found | 403 | Auth | F-06 |
| Missing `prvCreateAccount` | 403 | Auth | F-07 |
| FLS hard block on `parentaccountid` | 400 | Auth | F-08 |
| Malformed JSON | 400 | Routing | F-10 |
| Invalid GUID format for `parentaccountid` | 400 | Routing | F-11 |
| PreValidation plug-in exception | 400 | Plug-in pipeline | F-13 |
| PreValidation plug-in timeout | 500 | Plug-in pipeline | F-14 |
| Missing `prvReadAccount` in plug-in context | 403 | Plug-in pipeline | F-15 |
| Parent GUID not found at INSERT | 400 | Storage | F-22 |
| PostOperation partial commit | 500 | Plug-in pipeline | F-20 |
| FLS strips `parentaccountid` from response | 204/201 field absent (silent) | Response | F-26 |
| FLS bypass via elevated plug-in (security violation) | 204 (write succeeds, policy violated) | Plug-in pipeline | F-17 |

---

### Step 13 — Blast Radius Ordered Failure Catalog

COMMON SKIP at failure summary: Developers list failures in occurrence order — they skip reordering by blast radius, missing that the FLS bypass (F-17) is a security policy violation even though the operation returns 2xx.
REQUIRED: Reorder by blast radius with data integrity and security violations ranked above clean 4xx/5xx failures.

1. **F-16 TOCTOU** — Parent deleted between PreValidation check and INSERT. Blast: silent data integrity corruption if not detected; no error surfaced to caller in race window.
2. **F-20 PostOperation partial commit** — Account created, dependent operation failed. Blast: orphaned records, downstream process failures.
3. **F-17 FLS bypass via elevated plug-in** — Security policy violation: `parentaccountid` written in violation of caller's FLS profile. Blast: audit risk, field security policy circumvented, requires security exception documentation.
4. **F-22 Parent GUID not found at INSERT** — Operation fails, FK constraint enforced, data integrity preserved. Blast: recoverable 400.
5. **F-08 FLS silent strip** — `parentaccountid` silently dropped from CREATE, account created without parent relationship. Blast: data model inconsistency, caller unaware.
6. All other failures — operation fails cleanly with appropriate HTTP status; no data integrity risk.

---

### Step 14 — Latency Source Summary

| Latency source | Step | Severity |
|---|---|---|
| Metadata cache miss on cold start | Entry | Low (one-time) |
| Role/privilege cache miss → sync DB lookup | Auth | Medium |
| Plug-in timeout risk (2-min default) | Plug-in pipeline | High |
| Plug-in latency under transaction lock (PreOperation) | Plug-in pipeline | High |
| Lock wait on parent account row | Storage | Medium |
| Audit write under high volume | Storage | Low–Medium |
| `Prefer: return=representation` read round-trip | Response | Low |

---

### Step 15 — Signal Output

```
signal: trace-request
topic: [topic name from invocation context]
date: 2026-03-15
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
variation-axis: inertia-framing (common-skip explicit labeling)
boundaries-traced: 8 (entry, auth, routing, PreValidation, PreOperation, PostOperation, storage, response)
failure-points: 27 (F-01 through F-27)
gap-flagged: 13 (F-01, F-02, F-05, F-06, F-07, F-08, F-13, F-14, F-15, F-16, F-17, F-20, F-22, F-26)
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6 -- PreOperation elevated FLS bypass)
latency-sources: 7
common-skip-surfaces-surfaced: 9
```
