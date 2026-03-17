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

