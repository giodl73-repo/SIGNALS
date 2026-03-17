## V-05 — Combined: Formal register + Storage-first + Equal phase budget

**Axis:** Three-axis combination: declarative formal register (V-02 axis) + Storage expert speaks first at every step + seven equal-weight phases (6 lifecycle + 1 error paths, each with exactly 3 required sub-items).

**Hypothesis:** Three-axis combination maximizes overall rubric composite by addressing formal structural compliance (formal register → C-37/C-38), failure severity ordering (storage-first → blast radius ranking), and completeness (equal phase budget → no boundary collapsed).

---

SKILL DECLARATION {
  SKILL: trace-request
  PLATFORM-CONTEXT: Dataverse
  REGISTER: formal-declarative
  ROLE-ORDER: Storage-first (Storage expert speaks first; Auth expert second; Routing expert third)
  PHASE-BUDGET: 7 phases (Entry, Authentication, Routing, Boundary-Crossing, Storage, Response-Assembly, Error-Paths) each equal weight, each with exactly 3 required sub-items: (1) boundary description, (2) failure point table, (3) latency identification
  SCENARIO: "POST /api/data/v9.2/accounts -- Create Account with parentaccountid referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on parentaccountid"
}

---

### Step 1 — Scenario Registration

DECLARE SCENARIO-FIELDS {
  OPERATION: "POST /api/data/v9.2/accounts"
  PAYLOAD-KEY-FIELD: "parentaccountid" (GUID reference to existing account)
  PLUGIN-PIPELINE: "PreValidation -> PreOperation -> PostOperation (all synchronous)"
  SECURITY-OVERLAY: "Field-level security (FLS) on parentaccountid"
  PHASE-COUNT: 7
  TRACE-GOAL: "Hand-compile every boundary crossing, failure point, latency source, and auth gap across 7 equal-weight phases"
}

---

### Step 2 — Role and Phase Declaration

DECLARE PLATFORM-EXPERT: "Dataverse platform expert"
DECLARE ROLE-ORDER {
  ROLE-1: "Storage/data-layer expert -- speaks first; surfaces data-access patterns, cascade dependencies, I/O latency, blast-radius ordering"
  ROLE-2: "Auth expert -- speaks second; surfaces auth constraints, FLS gaps, token scope mismatches"
  ROLE-3: "Routing/API expert -- speaks third; surfaces routing failures, payload validation"
}
DECLARE PHASE-BUDGET-RULE: "7 phases; each phase is explicitly labeled and equal weight; each phase contains exactly 3 required sub-items: (1) boundary description, (2) failure point table, (3) latency identification; no phase may be collapsed; Phase 7 Error-Paths is a first-class section"

---

### Step 3 — Authentication Contract

DECLARE AUTH-CONTRACT {
  LOCK-BEFORE: "any phase trace"
  REFERENCE-FOR: "Step 8 CHECKER ALGORITHM"
}

DECLARE STEP-8-HEADER {
  VT-1: "user_impersonation"
  VT-2: "prvCreateAccount"
  VT-3: "prvReadAccount"
  VT-4: "FLS write permission on parentaccountid"
  VT-5: "internal service identity"
  TOKEN-COUNT: 5
  CHECKER-ALGORITHM {
    DECLARE MATCH-RULE AS: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; case-sensitive; whitespace-normalized; character-for-character identity with the quoted VT-N value required.
    DECLARE HALT-RULE AS: Fire when Step 8b prose asserts coherence (confirms the three link arms are consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous presence of a prose-coherent claim and a table-level mismatch constitutes a contradiction that must halt the trace.
    DECLARE OUTPUT-RULE AS: Assign Row-Verdict = PASS if Match? = Y for that row; assign Row-Verdict = HALT if HALT-RULE fires; emit CHECK RESULT summary line immediately after last row of Step 8c table.
  }
}

EMIT AUTH-CONTRACT-TABLE:

| Boundary | Required Scope / Permission | Token Type | VT-N |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | VT-1 |
| System user privilege check | `prvCreateAccount` | System user + role | VT-2 |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | FLS profile | VT-4 |
| SQL storage layer | `internal service identity` | Internal | VT-5 |
| Parent GUID relationship validation | `prvReadAccount` | System user | VT-3 |

ASSERT AUTH-CONTRACT-STATUS: "LOCKED"

---

## Phase 1 — Entry

**Sub-item 1 — Boundary description:**

DECLARE BOUNDARY: "OData API endpoint /api/data/v9.2/accounts"

*Storage expert (speaks first):* From the storage perspective, the entry point is the gateway before any data operation is initiated. The critical storage-layer concern at entry is that the `parentaccountid` GUID passed in the payload will eventually resolve to a FK constraint check against `AccountBase.AccountId` at the INSERT layer — failure to validate the GUID format here means a malformed value reaches the SQL layer. The entry point does not perform storage operations, but it gates all subsequent storage interactions.

*Auth expert:* The entry point performs an immediate token presence check. Missing or expired Bearer token returns 401 before any routing or storage operation occurs. The token audience must match the Dataverse environment resource URI — a valid AAD token for a different environment returns 401.

*Routing expert:* HTTP method validation (must be POST), content-type check (`application/json`), URL parsing to extract entity set name `accounts`.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong token audience (incorrect environment resource URI) → 401 | Y | No |
| F-03 | Entity set name not found in OData metadata → 404 | N | No |
| F-04 | OData metadata cache miss on cold start → routing delay | N | Y |

**Sub-item 3 — Latency identification:**

DECLARE LATENCY-SOURCE: "OData metadata cache miss on cold start or after metadata invalidation; sub-millisecond on warm instance; 500ms-2s on cold start or after publish operation"

---

## Phase 2 — Authentication

**Sub-item 1 — Boundary description:**

DECLARE BOUNDARY: "Dataverse authentication layer -- AAD token validation and caller privilege resolution"

*Storage expert (speaks first):* The authentication layer performs synchronous database lookups against `systemuser`, `role`, `roleprivileges`, and `fieldpermission` tables. From the storage perspective, these are read operations with caching — a cache miss forces a synchronous read path under high request volume. The FLS profile lookup for `parentaccountid` is a read against the `fieldpermission` table.

*Auth expert:* Four sequential checks: (1) AAD token signature, expiry, audience, issuer validation; (2) system user resolution from AAD OID/UPN — disabled or missing = 403; (3) `prvCreateAccount` privilege check at scope covering target business unit; (4) FLS pre-check on `parentaccountid` — caller's FLS profile evaluated for write access; denial = silent strip or hard 400 depending on configuration.

*Routing expert:* Authentication result gates routing; failed authentication terminates the request before the OData routing layer constructs the `Entity` object.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found or disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS profile denies write on `parentaccountid` — silent strip or hard 400 | Y | No |
| F-09 | Role/privilege cache miss → synchronous DB lookup latency | N | Y |

**Sub-item 3 — Latency identification:**

DECLARE LATENCY-SOURCE: "Role and privilege cache miss; invalidated by role assignment change or system user modification; forces synchronous read against systemuser/role/roleprivileges/fieldpermission; 50-200ms per request under load"

---

## Phase 3 — Routing

**Sub-item 1 — Boundary description:**

DECLARE BOUNDARY: "OData routing layer -- entity set resolution, payload deserialization, and ExecutionContext construction"

*Storage expert (speaks first):* The routing layer deserializes the `parentaccountid` value from the JSON payload. The storage expert notes: the routing layer validates GUID format but does NOT validate that the GUID exists in `AccountBase` — that check is deferred to the storage layer at Phase 5. This deferred check creates a latency-free pass-through with a storage-layer failure risk.

*Auth expert:* No additional auth check at routing, but the `ExecutionContext` — carrying the caller's system user identity and security roles — is attached to the `Entity` object here and propagates through the plug-in pipeline.

*Routing expert:* Entity set `accounts` resolved to `account` entity metadata; Create request handler constructed; JSON body deserialized to internal `Entity` object; all property names and types validated against entity metadata; `parentaccountid` validated as GUID format.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |

**Sub-item 3 — Latency identification:**

DECLARE LATENCY-SOURCE: "Entity metadata resolution for large payloads; account entity has 100+ attributes; parsing latency scales with payload attribute count; warm instance: negligible; large custom-attribute payloads: measurable"

---

## Phase 4 — Boundary-Crossing (Plug-in Pipeline)

**Sub-item 1 — Boundary description:**

DECLARE BOUNDARY: "Synchronous plug-in pipeline -- PreValidation, PreOperation, PostOperation crossings"

*Storage expert (speaks first):* From the storage perspective, the plug-in pipeline introduces three distinct data-access patterns: (a) PreValidation may issue read queries outside the main transaction — TOCTOU risk; (b) PreOperation executes inside the database transaction — write modifications to `Target` entity here affect the final INSERT, and plug-in latency under transaction lock escalates to lock contention; (c) PostOperation fires after INSERT is committed — failures here produce partial commits at the storage layer.

*Auth expert:* Each crossing propagates the `ExecutionContext`. If a run-as user is configured on a plug-in step, the security context diverges. At PreOperation, a run-as user with an elevated FLS profile can write `parentaccountid` even if the caller's FLS profile denies the write — this is F-17, the HALT boundary. The invoked permission at this crossing is "elevated plug-in context (run-as)" rather than VT-4: "FLS write permission on parentaccountid."

*Routing expert:* Plug-in dispatch serializes the `ExecutionContext` and invokes the registered assembly at each stage.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-13 | PreValidation throws `InvalidPluginExecutionException` → 400 | Y | No |
| F-14 | PreValidation plug-in timeout (2-min default) → 500 | Y | Y |
| F-15 | PreValidation read — caller lacks `prvReadAccount` → plug-in 403 | Y | No |
| F-16 | TOCTOU: parent account deleted between PreValidation check and INSERT | Y | No |
| F-17 | PreOperation modifies `parentaccountid` under elevated run-as context, bypassing caller FLS | Y | No |
| F-18 | PreOperation throws → transaction rollback → 400 | Y | No |
| F-19 | PreOperation latency under transaction lock → lock escalation | N | Y |
| F-20 | PostOperation failure → partial commit (account created, dependent op failed) | Y | No |
| F-21 | Async misclassification: plug-in registered sync but behaves async | Y | No |

**Sub-item 3 — Latency identification:**

DECLARE LATENCY-SOURCES {
  SOURCE-1: "Plug-in dispatch overhead per crossing: 5-20ms on warm instance; three crossings"
  SOURCE-2: "Plug-in execution time: unbounded if plug-in calls external services; default sync timeout 2 minutes"
  SOURCE-3: "Transaction lock contention at PreOperation: if parent account record concurrently modified, lock wait can cascade; unbounded under high concurrency"
}

---

## Phase 5 — Storage

**Sub-item 1 — Boundary description:**

DECLARE BOUNDARY: "Dataverse SQL backend -- INSERT AccountBase and AccountExtensionBase with FK constraint enforcement"

*Storage expert (speaks first):* The storage layer is the authoritative data integrity enforcement point. Four operations occur: (1) Relationship validation: `parentaccountid` GUID checked against `AccountBase.AccountId` via FK constraint — non-existent GUID fails here; (2) Transaction atomicity: `AccountBase` (core columns) and `AccountExtensionBase` (custom columns) written in a single transaction — extension table failure rolls back everything; (3) Audit record write if auditing is enabled for the account entity — written in the same transaction; (4) Row-level locking on the parent account record during the transaction — concurrent modifications cause lock waits.

*Auth expert:* No caller token propagates to the SQL layer. The storage layer operates under the internal service identity (VT-5). Auth concerns at this layer are limited to validating that the `parentaccountid` value was not modified by the PreOperation elevated context in violation of the caller's FLS profile — that violation was already flagged at Phase 4.

*Routing expert:* The storage layer returns an INSERT result containing the new `accountid` GUID; this feeds the response assembly phase.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-22 | Parent GUID not found at INSERT → FK constraint violation → 400 | Y | No |
| F-23 | Lock wait on parent account row under concurrency | N | Y |
| F-24 | Extension table write failure → full transaction rollback | N | No |
| F-25 | Audit write latency under high volume | N | Y |

**Sub-item 3 — Latency identification:**

DECLARE LATENCY-SOURCES {
  SOURCE-1: "Lock wait on parent account row: if another operation holds a write lock on the parent account, a shared lock wait occurs; duration unbounded under high concurrency"
  SOURCE-2: "Audit write I/O: proportional to audit record volume and table size; low-medium under normal load"
}

---

## Phase 6 — Response Assembly

**Sub-item 1 — Boundary description:**

DECLARE BOUNDARY: "OData layer response assembly -- OData-EntityId header and Prefer: return=representation path"

*Storage expert (speaks first):* On successful INSERT, the storage layer returns the new `accountid` GUID. The response assembly layer reads this value and constructs the `OData-EntityId` header. If `Prefer: return=representation` is present, a SELECT on the new record is performed — this is a separate read operation against the storage layer, adding a round-trip. The SELECT applies FLS on the `parentaccountid` field; if the caller's FLS profile denies read access, the field is stripped from the response even though the write succeeded.

*Auth expert:* The SELECT for `Prefer: return=representation` re-applies the caller's read privileges and FLS profile. FLS denial on read strips `parentaccountid` from the returned entity body — a silent data anomaly from the caller's perspective.

*Routing expert:* Default response: HTTP 204 No Content with `OData-EntityId` header. With `Prefer: return=representation`: HTTP 201 Created with full entity body from SELECT.

**Sub-item 2 — Failure point table:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation | Y | No |
| F-27 | `Prefer: return=representation` adds read round-trip latency | N | Y |

**Sub-item 3 — Latency identification:**

DECLARE LATENCY-SOURCE: "Prefer: return=representation triggers SELECT with full OData query processing, FLS evaluation, column projection, and JSON serialization; 20-100ms additional latency depending on instance load and column count"

---

### Step 8 — Auth Verification Checkpoint

DECLARE CHECKPOINT: "Step 8 -- Auth Verification"
VERIFY AUTH-CONTRACT-STATUS: "LOCKED in Step 3"

**Step 8 Header:**

```
VT-1: "user_impersonation"
VT-2: "prvCreateAccount"
VT-3: "prvReadAccount"
VT-4: "FLS write permission on parentaccountid"
VT-5: "internal service identity"
TOKEN-COUNT: 5

CHECKER ALGORITHM:
DECLARE MATCH-RULE AS: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; case-sensitive; whitespace-normalized; character-for-character identity with the quoted VT-N value required; predicate evaluated independently of any prose content.
DECLARE HALT-RULE AS: Fire when Step 8b prose asserts coherence (confirms the three link arms are consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous presence of a prose-coherent claim and a table-level mismatch constitutes a contradiction that must halt the trace.
DECLARE OUTPUT-RULE AS: Assign Row-Verdict = PASS if Match? = Y for that row; assign Row-Verdict = HALT if HALT-RULE fires; emit CHECK RESULT summary line immediately after last row of Step 8c table; no prose reading required to evaluate this contract.
```

**Step 8a — Boundary Invocation Listing:**

EMIT INVOCATION-TABLE:

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

**Step 8b — Prose Coherence Confirmation:**

REQUIRE: One coherence paragraph per Gap?=Y boundary; all three link arms named explicitly.

*OData API entry (F-01, F-02):*
Arm 1: "OData API entry" maps to `user_impersonation` in Step 3 — VERIFY: confirmed. Arm 2: Step 8a-Invoked `user_impersonation` equals VT-1: "user_impersonation" — ASSERT: match confirmed. Arm 3: Step 11 parameters (resource URI=Dataverse env endpoint, tenant ID, environment ID) consistent with `user_impersonation` audience — ASSERT: consistent. All three arms coherent.

*System user privilege check (F-06, F-07):*
Arm 1: Maps to `prvCreateAccount` — VERIFY: confirmed. Arm 2: Step 8a-Invoked `prvCreateAccount` equals VT-2 — ASSERT: match. Arm 3: entity=account, op=Create consistent — ASSERT: consistent. All three arms coherent.

*FLS check on `parentaccountid` (F-08):*
Arm 1: Maps to `FLS write permission on parentaccountid` (VT-4) — VERIFY: confirmed. Arm 2: Step 8a-Invoked `FLS write permission on parentaccountid` equals VT-4 — ASSERT: match. Arm 3: field=parentaccountid, op=write consistent — ASSERT: consistent. All three arms coherent.

*PreValidation plug-in read query (F-15):*
Arm 1: Maps to `prvReadAccount` (VT-3) — VERIFY: confirmed. Arm 2: Step 8a-Invoked `prvReadAccount` equals VT-3 — ASSERT: match. Arm 3: entity=account, op=Read, context=plugin consistent — ASSERT: consistent. All three arms coherent.

*PreOperation elevated FLS bypass (F-17):*
Arm 1: This boundary should map to `FLS write permission on parentaccountid` (VT-4) per Step 3 auth contract — PreOperation plug-in modifies `parentaccountid`, a VT-4 governed field. ASSERT: Arm 1 asserts coherence with VT-4. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" — VERIFY against VT-4: "FLS write permission on parentaccountid" — ASSERT: NOT EQUAL; mismatch. Arm 3: Step 11 parameters (plug-in run-as user, FLS profile differs from caller) — ASSERT: inconsistent with VT-4. DECLARE CONTRADICTION: Arm 1 asserts coherence; Arms 2 and 3 confirm mismatch. Dual-surface contradiction present. HALT-RULE fires.

**Step 8c — Match? Table (REQUIRED — before Phase 7):**

EMIT MATCH-TABLE:

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
`Scope String Correction (Rem#1): The PreOperation plug-in step must be constrained to caller-context execution — remove run-as user configuration so invoked scope becomes "FLS write permission on parentaccountid" matching VT-4. If elevated context is intentional, add an explicit scope entry in Step 3 auth contract for the run-as user's FLS profile and document the intentional bypass with a security exception review record.`

---

## Phase 7 — Error Paths (First-Class Section, Equal Weight to Phases 1–6)

**Sub-item 1 — Error path boundary description:**

DECLARE BOUNDARY: "Error path catalog -- all error paths collected from Phases 1 through 6"

*Storage expert (speaks first):* From the storage perspective, error paths are classified by data integrity impact. Priority: (a) silent data anomalies (2xx response but data is incorrect or partially committed) — these are the most dangerous because the caller has no indication of a problem; (b) partial commits (operation partially succeeds, system in inconsistent state); (c) clean storage constraint failures (400 with meaningful error code, data integrity preserved).

*Auth expert:* Auth error paths are clean 4xx responses. The silent security violation (F-17, 2xx but FLS policy bypassed) is classified as a storage-layer anomaly per the storage expert's priority ordering.

*Routing expert:* Routing error paths are client-correctable 4xx responses: malformed JSON, invalid GUID format, unrecognized property names.

**Sub-item 2 — Error path table:**

EMIT ERROR-PATH-TABLE:

| Error path | HTTP status | Phase | Failure ref | Category |
|---|---|---|---|---|
| Missing / expired Bearer token | 401 | Phase 1, 2 | F-01, F-05 | Client-correctable |
| Wrong token audience | 401 | Phase 1 | F-02 | Client-correctable |
| System user disabled or not found | 403 | Phase 2 | F-06 | Admin action required |
| Missing `prvCreateAccount` | 403 | Phase 2 | F-07 | Admin action required |
| FLS hard block on `parentaccountid` | 400 | Phase 2 | F-08 | Admin action required |
| Malformed JSON | 400 | Phase 3 | F-10 | Client-correctable |
| Invalid GUID format | 400 | Phase 3 | F-11 | Client-correctable |
| PreValidation plug-in exception | 400 | Phase 4 | F-13 | Depends on plug-in message |
| PreValidation plug-in timeout | 500 | Phase 4 | F-14 | Retry / plug-in optimization |
| Missing `prvReadAccount` in plug-in | 403 | Phase 4 | F-15 | Admin action required |
| TOCTOU parent deleted | 400 or silent | Phase 4 | F-16 | Integrity risk — investigation required |
| FLS bypass via elevated plug-in | 204 (silent violation) | Phase 4 | F-17 | Security violation — silent |
| PostOperation partial commit | 500 | Phase 4 | F-20 | Investigation required |
| Parent GUID not found at INSERT | 400 | Phase 5 | F-22 | Client-correctable (verify GUID) |
| FLS strips `parentaccountid` from response | 204/201 field absent | Phase 6 | F-26 | Silent anomaly — caller awareness required |
| Read privilege missing for `Prefer` response | 403/field absent | Phase 6 | F-26 variant | Admin action required |

**Sub-item 3 — Latency attribution per error path:**

DECLARE LATENCY-ATTRIBUTION {
  HIGHEST-LATENCY-FAILURE: "F-14 PreValidation timeout (up to 2 minutes) -- highest blast radius for latency; request holds resources for full timeout duration before failing with 500"
  SECOND-HIGHEST: "F-23 lock wait on parent account row -- unbounded under high concurrency; failure eventually surfaces as timeout or deadlock detection"
  NOTE: "Error paths themselves terminate the request and do not accumulate further latency; the latency is incurred by the operations that precede the failure point"
}

---

### Step 9 — Parameter and Scope Catalog

EMIT PARAMETER-TABLE:

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
| Plug-in run-as (PreOperation) | Configured run-as user on plug-in step | elevated plug-in context (run-as) |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

---

### Step 10 — Latency Source Summary (Cross-Phase)

EMIT LATENCY-TABLE:

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

EMIT SIGNAL-ARTIFACT:

```
signal: trace-request
topic: [topic name from invocation context]
date: 2026-03-15
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
variation-axis: combined -- formal-register + storage-first + equal-phase-budget
phase-count: 7 (Phases 1-6 lifecycle + Phase 7 error-paths, equal weight)
role-order: Storage -> Auth -> Routing
register: formal-declarative (DECLARE/EMIT/ASSERT/VERIFY/REQUIRE)
boundaries-traced: 8
failure-points: 27 (F-01 through F-27)
gap-flagged: 13
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6 -- PreOperation elevated FLS bypass)
latency-sources: 9 (cross-phase)
```
