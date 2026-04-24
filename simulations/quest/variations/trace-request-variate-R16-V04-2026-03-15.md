## V-04 — Combined: Inertia framing + Machine-first output format

**Axis:** COMMON SKIP blocks at each boundary (V-01 axis) COMBINED WITH machine-first output (Step 8 Header emitted before Step 1, all tables before prose in each step).

**Hypothesis:** Skip labeling + machine-first output maximizes both completeness (fewer omitted failure surfaces) and structural token density (C-37/C-38 compliance) simultaneously.

---

You are executing a `trace-request` signal for the following scenario. Auto-select the appropriate platform expert role from context: Dataverse / Commerce / Automate. This trace applies two rules simultaneously:
Rule 1 — Inertia framing: Each boundary step opens with COMMON SKIP: + REQUIRED: blocks naming what developers typically omit.
Rule 2 — Machine-first: The Step 8 Header (VT-N schema + CHECKER ALGORITHM) is emitted as the VERY FIRST block of the trace, before Step 1. Every step emits its failure table BEFORE explanatory prose.

**Scenario:** POST /api/data/v9.2/accounts — Create Account with `parentaccountid` referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on `parentaccountid`.

**Platform Expert Selected:** Dataverse platform expert.

---

## STEP 8 HEADER — EMITTED FIRST (Machine-first rule)

```
VT-1: "user_impersonation"
VT-2: "prvCreateAccount"
VT-3: "prvReadAccount"
VT-4: "FLS write permission on parentaccountid"
VT-5: "internal service identity"
TOKEN-COUNT: 5

CHECKER ALGORITHM:
MATCH-RULE: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; case-sensitive; whitespace-normalized; character-for-character identity with the quoted VT-N value required.
HALT-RULE: Fire when Step 8b prose asserts coherence (confirms the three link arms are consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous presence of a prose-coherent claim and a table-level mismatch constitutes a contradiction that must halt the trace.
OUTPUT-RULE: Assign Row-Verdict = PASS if Match? = Y for that row; assign Row-Verdict = HALT if HALT-RULE fires; emit CHECK RESULT summary line immediately after last row of Step 8c table.
```

*Step 8 Header emitted before Step 1 per machine-first rule. The VT-N schema and CHECKER ALGORITHM are machine-greppable tokens available before any boundary is traced.*

---

### Step 1 — Scenario Registration

COMMON SKIP at scenario registration: Developers note the plug-in pipeline and skip registering the FLS overlay as a distinct security surface with its own boundary evaluation.
REQUIRED: Register FLS on `parentaccountid` as a named trace target — it is evaluated independently at the caller level, at the FLS pre-check in auth, and again at the PreOperation plug-in modification boundary.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-00 | Trace skips FLS as a named boundary → misses F-08 and F-17 entirely | Y | No |

**Scenario fields:**
- **Operation:** POST /api/data/v9.2/accounts
- **Payload key field:** `parentaccountid` (GUID reference to existing account)
- **Plug-in pipeline:** PreValidation → PreOperation → PostOperation (all synchronous)
- **Security overlay:** Field-level security (FLS) on `parentaccountid` — NAMED TRACE TARGET
- **Trace goal:** Hand-compile every boundary crossing, failure point, latency source, and auth gap from entry to response.

---

### Step 2 — Role Declaration

COMMON SKIP at role declaration: Developers assign a single API expert and skip separate storage and auth sub-roles, missing blast-radius ordering from the storage perspective.
REQUIRED: Declare all three sub-roles active. Storage expert contributes to each boundary.

**Role:** Dataverse platform expert (Auth, Routing, and Storage sub-roles all active).
**Rules active:** Inertia framing (COMMON SKIP + REQUIRED at each boundary) + Machine-first (failure tables emitted before prose in each step).

---

### Step 3 — Authentication Contract

COMMON SKIP at auth contract: Developers list Bearer token scope and create privilege, skip FLS as a separate auth surface, and skip internal service identity for the SQL layer.
REQUIRED: Enumerate all five distinct auth surfaces; each must appear as a VT-N entry in the Step 8 Header (already emitted above).

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-00b | Auth contract omits FLS surface → Step 8 cannot evaluate VT-4 boundary | Y | No |
| F-00c | Auth contract omits internal service identity → VT-5 row missing from Step 8c | Y | No |

**Auth contract:**

| Boundary | Required Scope / Permission | Token Type | VT-N |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | VT-1 |
| System user privilege check | `prvCreateAccount` | System user + role | VT-2 |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | FLS profile | VT-4 |
| SQL storage layer | `internal service identity` | Internal | VT-5 |
| Parent GUID relationship validation | `prvReadAccount` | System user | VT-3 |

**Auth contract locked. All five VT-N entries verified against Step 8 Header (emitted above).**

---

### Step 4 — Entry Point

COMMON SKIP at entry: Developers check for Bearer token presence and skip token audience validation — they assume any valid AAD token works on any Dataverse environment.
REQUIRED: Trace token audience (environment resource URI) as a distinct failure surface separate from token validity.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong token audience (incorrect environment resource URI) → 401 | Y | No |
| F-03 | Entity set name not found in OData metadata → 404 | N | No |
| F-04 | OData metadata cache miss on cold start → routing delay | N | Y |

The HTTP POST arrives at `/api/data/v9.2/accounts`. The entry point performs HTTP method check, content-type validation (`application/json`), URL parsing for entity set name `accounts`, and Bearer token presence check. F-01 and F-02 are distinct: F-01 is token validity (expired/missing); F-02 is token audience mismatch (valid token, wrong environment URI).

---

### Step 5 — Authentication Boundary

COMMON SKIP at auth: Developers confirm `prvCreateAccount` is present and stop — they skip FLS re-evaluation at the PreOperation plug-in modification step, treating FLS as a one-time check at the API layer.
REQUIRED: Trace FLS at every boundary where `parentaccountid` is accessed or written. Document that FLS is checked here at BC-2 AND again implicitly at BC-5 (PreOperation modification). The PreOperation elevated context at BC-5 is the HALT boundary.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found or disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS profile denies write on `parentaccountid` — silent strip or hard 400 | Y | No |
| F-09 | Role/privilege cache miss → synchronous DB lookup latency | N | Y |

After the routing layer accepts the request, four sequential auth checks run: (1) AAD token signature, expiry, audience, issuer; (2) system user resolution from AAD OID/UPN; (3) `prvCreateAccount` privilege check; (4) FLS pre-check for `parentaccountid` write access. FLS at this boundary evaluates the caller's FLS profile. The FLS surface will be re-evaluated at PreOperation if the plug-in modifies `parentaccountid` — that re-evaluation is the source of F-17.

---

### Step 6 — Routing Boundary

COMMON SKIP at routing: Developers verify JSON parses successfully and skip GUID format validation as a distinct failure surface.
REQUIRED: Trace GUID format validation on `parentaccountid` as a named routing failure point.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |

The OData routing layer resolves `accounts` to the `account` entity metadata, constructs the Create request handler, deserializes the JSON body into an internal `Entity` object, validates all property names and types against entity metadata, and validates `parentaccountid` as a GUID format. The caller's `ExecutionContext` is attached to the `Entity` object and propagates through the plug-in pipeline.

---

### Step 7 — Service Boundary Crossings (Plug-in Pipeline)

COMMON SKIP at plug-in pipeline: Developers confirm plug-ins fire in sequence and skip tracing the security context divergence — specifically, the elevated run-as context at PreOperation that bypasses the caller's FLS profile.
REQUIRED: Trace the security context at each crossing. Document run-as divergence at PreOperation as the HALT boundary.

#### 7a — PreValidation Plug-in

COMMON SKIP at PreValidation: Developers confirm PreValidation fires and skip the TOCTOU risk from queries running outside the main transaction.
REQUIRED: Trace TOCTOU explicitly as F-16: parent account can be deleted between PreValidation check and INSERT.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-13 | Plug-in throws `InvalidPluginExecutionException` → 400 | Y | No |
| F-14 | Plug-in timeout (2-min default) → 500 | Y | Y |
| F-15 | Plug-in read of parent account — caller lacks `prvReadAccount` | Y | No |
| F-16 | TOCTOU: parent account deleted between PreValidation check and INSERT | Y | No |

PreValidation fires before any database transaction. Security context: caller's context unless run-as configured. Plug-in queries run outside the main transaction — parent account existence verified here is not guaranteed at INSERT time.

#### 7b — PreOperation Plug-in (HALT BOUNDARY)

COMMON SKIP at PreOperation: Developers see the plug-in fires inside the transaction and stop — they skip the FLS bypass risk when the plug-in modifies a FLS-protected field under an elevated run-as context.
REQUIRED: Trace the elevated run-as context at PreOperation as a distinct security boundary. This is F-17 and the source of CONTRADICTION SIGNAL Seq# 6.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-17 | Plug-in modifies `parentaccountid` under elevated run-as context, bypassing caller FLS | Y | No |
| F-18 | Plug-in throws → transaction rollback → 400 | Y | No |
| F-19 | Plug-in latency under transaction lock → lock escalation risk | N | Y |

PreOperation fires inside the database transaction. If a run-as user is configured on this plug-in step, the security context diverges from the caller. If the plug-in modifies `parentaccountid`, it does so under the run-as user's FLS profile — which may permit the write even if the caller's FLS profile denies it. This is the HALT boundary: Step 8b will assert coherence for this boundary against the auth contract, but Step 8c will record Match? = N because the invoked scope is "elevated plug-in context (run-as)" not VT-4.

#### 7c — PostOperation Plug-in

COMMON SKIP at PostOperation: Developers verify 204 is returned and skip partial commit risk from PostOperation failures after INSERT.
REQUIRED: Trace partial commit surface explicitly as F-20.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-20 | PostOperation failure → partial commit (account created, dependent op failed) | Y | No |
| F-21 | Async misclassification: plug-in registered as sync but behaves async | Y | No |

PostOperation fires after the INSERT is committed. Cannot roll back the main account record. Failure here leaves a partial commit: the account record exists in the database but dependent operations (child records, async workflows, notifications) triggered by this plug-in have not been completed.

---

### Step 8 — Auth Verification Checkpoint

COMMON SKIP at Step 8: Developers list five token scopes and stop — they omit the PreOperation elevated context row because it was a run-as context switch, not an OAuth token check.
REQUIRED: Add the PreOperation elevated context as a distinct row in the invocation list and evaluate it against VT-4 in the Match? table.

*(Step 8 Header was emitted before Step 1 per machine-first rule. The VT-N schema and CHECKER ALGORITHM are already declared above.)*

---

**Step 8a — Boundary Invocation Listing**

**Invocation table (emitted before prose — machine-first rule):**

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry (Bearer token) | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

Every boundary where an auth scope or permission was actually invoked is listed. The sixth row is the HALT boundary — included per machine-first rule requiring all invoked boundaries to be present in the table.

---

**Step 8b — Prose Coherence Confirmation (REQUIRED — one paragraph per Gap?=Y boundary)**

*OData API entry (F-01, F-02):*
Arm 1: Boundary "OData API entry" maps to `user_impersonation` in Step 3 auth contract — confirmed. Arm 2: Step 8a-Invoked `user_impersonation` matches VT-1: "user_impersonation" exactly — confirmed. Arm 3: Step 11 parameters (resource URI=Dataverse env endpoint, tenant ID, environment ID) consistent with `user_impersonation` audience — confirmed. All three arms coherent.

*System user privilege check (F-06, F-07):*
Arm 1: Boundary maps to `prvCreateAccount` in Step 3 — confirmed. Arm 2: Step 8a-Invoked `prvCreateAccount` matches VT-2: "prvCreateAccount" — confirmed. Arm 3: Step 11 parameters (entity=account, op=Create) consistent — confirmed. All three arms coherent.

*FLS check on `parentaccountid` (F-08):*
Arm 1: Boundary maps to `FLS write permission on parentaccountid` in Step 3 — confirmed. Arm 2: Step 8a-Invoked `FLS write permission on parentaccountid` matches VT-4 — confirmed. Arm 3: Step 11 parameters (field=parentaccountid, op=write) consistent — confirmed. All three arms coherent.

*PreValidation plug-in read query (F-15):*
Arm 1: Boundary maps to `prvReadAccount` in Step 3 — confirmed. Arm 2: Step 8a-Invoked `prvReadAccount` matches VT-3 — confirmed. Arm 3: Step 11 parameters (entity=account, op=Read, context=plugin) consistent — confirmed. All three arms coherent.

*PreOperation elevated FLS bypass (F-17):*
Arm 1: This boundary should map to `FLS write permission on parentaccountid` per Step 3 auth contract — the PreOperation plug-in modifies `parentaccountid`, governed by VT-4. Arm 1 asserts coherence with VT-4 as the expected scope. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" does NOT match VT-4: "FLS write permission on parentaccountid" — mismatch. Arm 3: Step 11 parameters confirm the plug-in run-as user has a different FLS profile than the caller — inconsistent with VT-4. Arms 2 and 3 are incoherent with the contract declared in Arm 1. HALT-RULE fires: Step 8b asserts coherence for this boundary AND Step 8c will record Match? = N.

---

**Step 8c — Match? Table (REQUIRED — positioned before Step 9)**

**Match table (emitted before prose — machine-first rule):**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| OData API entry | `user_impersonation` | `user_impersonation` | resource URI=Dataverse env, tenant ID present | Y | PASS |
| System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read, context=plugin | Y | PASS |
| SQL storage layer | `internal service identity` | `internal service identity` | service-to-service, no caller token | Y | PASS |
| PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as user, FLS profile differs | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): The PreOperation plug-in's run-as context must be constrained to the caller's FLS profile for parentaccountid. Remediation options: (a) Remove run-as user configuration from the PreOperation plug-in step — invoked scope becomes "FLS write permission on parentaccountid" matching VT-4; (b) If elevated context is intentional, add an explicit scope entry in the Step 3 auth contract for the run-as user context and document the intentional FLS bypass with a security exception review record.`

---

### Step 9 — Storage Access Boundary

COMMON SKIP at storage: Developers assume the INSERT fires and skip the FK constraint enforcement on `parentaccountid` as a named failure surface.
REQUIRED: Trace FK constraint violation on `parentaccountid` as F-22, distinct from the PreValidation GUID format check.

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-22 | Parent GUID not found at INSERT → FK constraint violation → 400 | Y | No |
| F-23 | Lock wait on parent account row under concurrency | N | Y |
| F-24 | Extension table write failure → full transaction rollback | N | No |
| F-25 | Audit write latency under high volume | N | Y |

The Dataverse SQL backend receives the INSERT request. Relationship validation: `parentaccountid` GUID checked against `AccountBase.AccountId` via FK constraint. The INSERT spans a transaction covering PreOperation and PostOperation. `AccountBase` and `AccountExtensionBase` are written atomically — extension table failure rolls back everything. Audit records written in the same transaction if auditing is enabled.

---

### Step 10 — Response Assembly Boundary

COMMON SKIP at response assembly: Developers confirm 204 is returned and skip the `Prefer: return=representation` path — specifically, they skip FLS re-evaluation on `parentaccountid` in the SELECT that powers the 201 response.
REQUIRED: Trace FLS re-evaluation on `parentaccountid` in the `Prefer: return=representation` SELECT as a named failure surface (F-26).

**Failure table (emitted before prose — machine-first rule):**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation | Y | No |
| F-27 | `Prefer: return=representation` adds read round-trip latency | N | Y |

On successful INSERT, the OData layer returns 204 No Content with `OData-EntityId` header by default. If `Prefer: return=representation` is present, the platform performs a SELECT on the new record and returns 201 with full entity body. This SELECT re-applies the caller's FLS profile — `parentaccountid` may be stripped from the response even though it was successfully written, creating a silent data anomaly.

---

### Step 11 — Parameter and Scope Catalog

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
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

---

### Step 12 — Error Paths (Complete)

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
| FLS bypass via elevated plug-in | 204 (security violation) | Plug-in pipeline | F-17 |

---

### Step 13 — Failure Catalog (Blast Radius Order)

1. **F-16 TOCTOU** — Silent data integrity corruption in race window.
2. **F-20 PostOperation partial commit** — Orphaned records, downstream failures.
3. **F-17 FLS bypass via elevated plug-in** — Security policy violation; field written against caller FLS profile.
4. **F-22 Parent GUID not found at INSERT** — Clean 400, FK enforced, data integrity preserved.
5. **F-08 FLS silent strip** — Account created without parent relationship, silent anomaly.
6. All other failures — clean HTTP error responses.

---

### Step 14 — Latency Source Summary

| Latency source | Step | Severity |
|---|---|---|
| Metadata cache miss on cold start | Entry | Low |
| Role/privilege cache miss | Auth | Medium |
| Plug-in timeout risk (2-min default) | Plug-in pipeline | High |
| Plug-in latency under transaction lock (PreOperation) | Plug-in pipeline | High |
| Lock wait on parent account row | Storage | Medium |
| Audit write under high volume | Storage | Low–Medium |
| `Prefer: return=representation` round-trip | Response | Low |

---

### Step 15 — Signal Output

```
signal: trace-request
topic: [topic name from invocation context]
date: 2026-03-15
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
variation-axis: combined -- inertia-framing + machine-first output
boundaries-traced: 8 (entry, auth, routing, PreValidation, PreOperation, PostOperation, storage, response)
failure-points: 27 (F-01 through F-27)
gap-flagged: 13
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6 -- PreOperation elevated FLS bypass)
latency-sources: 7
common-skip-surfaces-surfaced: 9
machine-first-rule: Step 8 Header emitted before Step 1; failure tables emitted before prose at every step
```
