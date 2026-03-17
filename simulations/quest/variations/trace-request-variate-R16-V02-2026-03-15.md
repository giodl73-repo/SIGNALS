## V-02 — Single axis: Phrasing register (Maximally formal/declarative)

**Axis:** All instructional content uses declarative token-format commands (DECLARE, EMIT, ASSERT, VERIFY, REQUIRE). No narrative prose in instructions.

**Hypothesis:** Declarative register forces the model to use formal pseudocode declarations for the HALT-RULE rather than paraphrasing in prose, increasing C-37/C-38 compliance.

---

SKILL DECLARATION {
  SKILL: trace-request
  PLATFORM-CONTEXT: Dataverse
  REGISTER: formal-declarative
  SCENARIO: "POST /api/data/v9.2/accounts — Create Account with parentaccountid referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on parentaccountid"
  INSTRUCTION-FORMAT: DECLARE/EMIT/VERIFY/ASSERT/REQUIRE tokens only; no narrative prose in instructional lines
}

---

### Step 1 — Scenario Registration

DECLARE SCENARIO-FIELDS {
  OPERATION: "POST /api/data/v9.2/accounts"
  PAYLOAD-KEY-FIELD: "parentaccountid" (GUID reference to existing account)
  PLUGIN-PIPELINE: "PreValidation -> PreOperation -> PostOperation (all synchronous)"
  SECURITY-OVERLAY: "Field-level security (FLS) on parentaccountid"
  TRACE-GOAL: "Hand-compile every boundary crossing, failure point, latency source, and auth gap from entry to response"
}

---

### Step 2 — Role Declaration

DECLARE PLATFORM-EXPERT: "Dataverse platform expert"
DECLARE REGISTER-RULE: "All step headers use DECLARE/EMIT/VERIFY/REQUIRE tokens; execution content (failure tables, auth contract, Step 8) is fully present in structured form"

---

### Step 3 — Authentication Contract

DECLARE AUTH-CONTRACT {
  LOCK-BEFORE: "any boundary trace"
  REFERENCE-FOR: "Step 8 verification"
}

EMIT AUTH-CONTRACT-TABLE:

| Boundary | Required Scope / Permission | Token Type | Notes |
|---|---|---|---|
| OData API entry | `user_impersonation` | Bearer (AAD) | Environment resource URI audience |
| System user privilege check | `prvCreateAccount` | System user + role | Create privilege on account entity |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | FLS profile | Write permission on named field |
| SQL storage layer | `internal service identity` | Internal | Service-to-service, no caller token |
| Parent GUID relationship validation | `prvReadAccount` | System user | Read privilege on account entity |

ASSERT AUTH-CONTRACT-STATUS: "LOCKED"

---

### Step 4 — Entry Point

DECLARE BOUNDARY: "OData API endpoint /api/data/v9.2/accounts"
DECLARE ENTRY-OPERATIONS: "HTTP method check; content-type validation (application/json); URL parsing for entity set name; immediate token presence check"

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong token audience (incorrect environment resource URI) → 401 | Y | No |
| F-03 | Entity set name not found in OData metadata → 404 | N | No |
| F-04 | OData metadata cache miss on cold start → routing delay | N | Y |

DECLARE LATENCY-SOURCE: "OData metadata cache miss on cold start or after metadata invalidation; sub-millisecond on warm instance; 500ms-2s on cold start"

---

### Step 5 — Authentication Boundary

DECLARE BOUNDARY: "Dataverse authentication layer"
DECLARE AUTH-SEQUENCE: {
  STEP-A: "AAD token signature, expiry, audience, issuer validation"
  STEP-B: "Dataverse system user resolution from AAD OID/UPN"
  STEP-C: "Privilege check: prvCreateAccount at scope covering target business unit"
  STEP-D: "FLS pre-check on parentaccountid: caller FLS profile evaluated for write access"
}

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found or disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS profile denies write on `parentaccountid` — silent strip or hard 400 depending on config | Y | No |
| F-09 | Role/privilege cache miss → synchronous DB lookup latency | N | Y |

DECLARE LATENCY-SOURCE: "Role and privilege cache miss; invalidated by role assignment change; synchronous read against systemuser/role/roleprivileges/fieldpermission tables; 50-200ms per request under load"

---

### Step 6 — Routing Boundary

DECLARE BOUNDARY: "OData routing layer — entity set resolution and payload deserialization"
DECLARE ROUTING-OPERATIONS: {
  STEP-A: "Resolve entity set accounts to account entity metadata"
  STEP-B: "Construct Create request handler"
  STEP-C: "Deserialize JSON body to internal Entity object"
  STEP-D: "Validate all property names and types against entity metadata"
  STEP-E: "Validate parentaccountid as GUID format"
  STEP-F: "Attach caller ExecutionContext to Entity object"
}

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |

DECLARE LATENCY-SOURCE: "Entity metadata resolution for large payloads; account entity has 100+ attributes; parsing latency scales with payload attribute count"

---

### Step 7 — Service Boundary Crossings (Plug-in Pipeline)

DECLARE BOUNDARY-CLASS: "Synchronous plug-in pipeline — three sequential crossings"
DECLARE SECURITY-CONTEXT-RULE: "Each crossing executes under caller security context unless run-as user is configured on the plug-in step; run-as divergence is the HALT-BOUNDARY at PreOperation"

#### 7a — PreValidation Plug-in

DECLARE CROSSING: "PreValidation — fires before any database transaction"
DECLARE SECURITY-CONTEXT: "Caller's context (unless run-as configured)"
DECLARE TOCTOU-RISK: "PreValidation queries run outside the main transaction; parent account can be deleted between PreValidation check and INSERT"

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-13 | Plug-in throws `InvalidPluginExecutionException` → 400 | Y | No |
| F-14 | Plug-in timeout (2-min default) → 500 / pipeline abort | Y | Y |
| F-15 | Plug-in read of parent account — caller lacks `prvReadAccount` → plug-in 403 | Y | No |
| F-16 | TOCTOU: parent account deleted after PreValidation check but before INSERT | Y | No |

#### 7b — PreOperation Plug-in

DECLARE CROSSING: "PreOperation — fires inside database transaction"
DECLARE SECURITY-CONTEXT: "May diverge from caller if run-as user configured on plug-in step"
DECLARE HALT-BOUNDARY: "F-17: If plug-in modifies parentaccountid under elevated run-as context, caller FLS restriction bypassed — invoked scope = elevated plug-in context, not VT-4"

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-17 | Plug-in modifies `parentaccountid` under elevated run-as context, bypassing caller FLS | Y | No |
| F-18 | Plug-in throws → transaction rollback → 400 | Y | No |
| F-19 | Plug-in latency under transaction lock → lock escalation risk | N | Y |

#### 7c — PostOperation Plug-in

DECLARE CROSSING: "PostOperation — fires after INSERT is committed"
DECLARE PARTIAL-COMMIT-RISK: "PostOperation failure cannot roll back main account record; dependent operations left incomplete"

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-20 | PostOperation failure → partial commit (account created, dependent op failed) | Y | No |
| F-21 | Async misclassification: plug-in registered as sync PostOperation but behaves async | Y | No |

---

### Step 8 — Auth Verification Checkpoint

DECLARE CHECKPOINT: "Step 8 — Auth Verification"
DECLARE REFERENCE-SOURCE: "Step 3 locked auth contract"

**Step 8 Header — VT# Token Reference Set and Checker Algorithm**

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

---

**Step 8a — Boundary Invocation Listing**

DECLARE INVOCATION-LIST-RULE: "List every boundary where an auth scope or permission was actually invoked; include PreOperation elevated context as a named row"

EMIT INVOCATION-TABLE:

| Boundary | Step8a-Invoked Scope / Permission |
|---|---|
| OData API entry (Bearer token) | `user_impersonation` |
| System user privilege check | `prvCreateAccount` |
| FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| PreValidation plug-in read query | `prvReadAccount` |
| SQL storage layer | `internal service identity` |
| PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

---

**Step 8b — Prose Coherence Confirmation**

REQUIRE: One coherence paragraph per Gap?=Y boundary; each paragraph names all three link arms explicitly.

*OData API entry (F-01, F-02):*
Arm 1: Boundary "OData API entry (Bearer token)" maps to `user_impersonation` in Step 3 auth contract — VERIFY: confirmed. Arm 2: Step 8a-Invoked `user_impersonation` equals VT-1: "user_impersonation" — ASSERT: character-for-character match confirmed. Arm 3: Step 11 parameters (resource URI=Dataverse env endpoint, tenant ID, environment ID) are consistent with `user_impersonation` audience requirement — ASSERT: consistent. All three arms coherent.

*System user privilege check (F-06, F-07):*
Arm 1: Boundary "System user privilege check" maps to `prvCreateAccount` in Step 3 — VERIFY: confirmed. Arm 2: Step 8a-Invoked `prvCreateAccount` equals VT-2: "prvCreateAccount" — ASSERT: match confirmed. Arm 3: Step 11 parameters (entity=account, op=Create) consistent with `prvCreateAccount` — ASSERT: consistent. All three arms coherent.

*FLS check on `parentaccountid` (F-08):*
Arm 1: Boundary "FLS check on parentaccountid" maps to `FLS write permission on parentaccountid` in Step 3 — VERIFY: confirmed. Arm 2: Step 8a-Invoked `FLS write permission on parentaccountid` equals VT-4: "FLS write permission on parentaccountid" — ASSERT: match confirmed. Arm 3: Step 11 parameters (field=parentaccountid, op=write) consistent — ASSERT: consistent. All three arms coherent.

*PreValidation plug-in read query (F-15):*
Arm 1: Boundary "PreValidation plug-in read query" maps to `prvReadAccount` in Step 3 — VERIFY: confirmed. Arm 2: Step 8a-Invoked `prvReadAccount` equals VT-3: "prvReadAccount" — ASSERT: match confirmed. Arm 3: Step 11 parameters (entity=account, op=Read, context=plugin) consistent — ASSERT: consistent. All three arms coherent.

*PreOperation elevated FLS bypass (F-17):*
Arm 1: This boundary should map to `FLS write permission on parentaccountid` per Step 3 auth contract — PreOperation plug-in modifies `parentaccountid`, a field governed by VT-4. ASSERT: Arm 1 claims coherence with VT-4. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" — VERIFY against VT-4: "FLS write permission on parentaccountid" — ASSERT: NOT EQUAL; mismatch detected. Arm 3: Step 11 parameters confirm plug-in run-as user has different FLS profile than caller — ASSERT: inconsistent with VT-4. DECLARE CONTRADICTION: Arm 1 asserts coherence; Arm 2 and Arm 3 assert mismatch — dual-surface contradiction present. HALT-RULE fires.

---

**Step 8c — Match? Table (REQUIRED — before Step 9)**

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
`Scope String Correction (Rem#1): Constrain the PreOperation plug-in step to execute under the caller's security context (remove run-as user configuration), so the invoked scope at this boundary becomes "FLS write permission on parentaccountid" matching VT-4. If elevated context is intentional, add an explicit scope entry in the Step 3 auth contract for the run-as user's FLS profile and document the intentional bypass with a security exception review record.`

---

### Step 9 — Storage Access Boundary

DECLARE BOUNDARY: "Dataverse SQL backend — INSERT AccountBase and AccountExtensionBase"
DECLARE STORAGE-OPERATIONS: {
  STEP-A: "Relationship validation: parentaccountid GUID must exist in AccountBase.AccountId (FK constraint)"
  STEP-B: "Transaction atomicity across AccountBase and AccountExtensionBase"
  STEP-C: "Audit record write if auditing enabled for account entity"
}
DECLARE AUTH-AT-STORAGE: "Internal service identity only; no caller token propagates to SQL layer"

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-22 | Parent GUID not found at INSERT → FK constraint violation → 400 | Y | No |
| F-23 | Lock wait on parent account row under concurrency | N | Y |
| F-24 | Extension table write failure → full transaction rollback | N | No |
| F-25 | Audit write latency under high volume | N | Y |

DECLARE LATENCY-SOURCES: "Lock wait on parent account row (variable, load-dependent); audit write I/O (proportional to audit volume)"

---

### Step 10 — Response Assembly Boundary

DECLARE BOUNDARY: "OData layer response assembly"
DECLARE DEFAULT-RESPONSE: "204 No Content + OData-EntityId header containing URL of new account record"
DECLARE PREFER-PATH: "If Prefer: return=representation sent, platform issues SELECT on new record → 201 Created with full entity body; SELECT applies caller read privileges and FLS — parentaccountid may be stripped"

EMIT FAILURE-TABLE:

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation | Y | No |
| F-27 | `Prefer: return=representation` adds read round-trip latency | N | Y |

DECLARE LATENCY-SOURCE: "Prefer: return=representation triggers SELECT with OData query processing, FLS evaluation, column projection, and JSON serialization; 20-100ms additional latency"

---

### Step 11 — Parameter and Scope Catalog

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

### Step 12 — Error Paths

EMIT ERROR-PATH-TABLE:

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
| FLS strips `parentaccountid` from response | 204/201 field absent | Response | F-26 |
| FLS bypass via elevated plug-in | 204 (security violation, write succeeds) | Plug-in pipeline | F-17 |

---

### Step 13 — Failure Catalog (Blast Radius Order)

DECLARE ORDERING-RULE: "Failures ordered by blast radius: data integrity violations and security policy violations rank above clean HTTP error responses"

EMIT BLAST-RADIUS-CATALOG:
1. F-16 TOCTOU — Blast: silent data integrity corruption; race window not surfaced to caller.
2. F-20 PostOperation partial commit — Blast: orphaned records, downstream process failures.
3. F-17 FLS bypass via elevated plug-in — Blast: security policy violation; field written in violation of caller FLS profile; audit risk.
4. F-22 Parent GUID not found at INSERT — Blast: clean failure, FK constraint enforced, data integrity preserved.
5. F-08 FLS silent strip — Blast: account created without parent relationship, caller unaware.
6. All other failures — clean HTTP error responses; no data integrity or security policy risk.

---

### Step 14 — Latency Source Summary

EMIT LATENCY-TABLE:

| Latency source | Step | Severity |
|---|---|---|
| Metadata cache miss on cold start | Entry | Low |
| Role/privilege cache miss | Auth | Medium |
| Plug-in timeout risk (2-min default) | Plug-in pipeline | High |
| Plug-in latency under transaction lock | PreOperation | High |
| Lock wait on parent account row | Storage | Medium |
| Audit write under high volume | Storage | Low–Medium |
| `Prefer: return=representation` round-trip | Response | Low |

---

### Step 15 — Signal Output

EMIT SIGNAL-ARTIFACT:

```
signal: trace-request
topic: [topic name from invocation context]
date: 2026-03-15
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
variation-axis: phrasing-register (formal/declarative)
boundaries-traced: 8 (entry, auth, routing, PreValidation, PreOperation, PostOperation, storage, response)
failure-points: 27 (F-01 through F-27)
gap-flagged: 13
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6 -- PreOperation elevated FLS bypass)
latency-sources: 7
register: formal-declarative (DECLARE/EMIT/ASSERT/VERIFY/REQUIRE)
```
