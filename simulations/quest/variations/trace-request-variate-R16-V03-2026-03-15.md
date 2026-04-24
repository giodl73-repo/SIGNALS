## V-03 — Single axis: Output format (Pre-declared trace contract)

**Axis:** A TRACE CONTRACT block is emitted FIRST (before Step 1), declaring all boundaries to be traced, all VT scope strings, and the expected HALT-RULE trigger points. The trace then executes against the contract.

**Hypothesis:** Pre-committing to trace structure before generating evidence reduces boundary omissions because the model checks off a pre-declared list rather than discovering structure incrementally.

---

You are executing a `trace-request` signal for the following scenario. Auto-select the appropriate platform expert role from context: Dataverse / Commerce / Automate. This trace emits a TRACE CONTRACT block before Step 1, declaring all boundaries, VT scope strings, and expected HALT boundaries. Steps 1-15 execute against the declared contract and reference it at each step.

**Scenario:** POST /api/data/v9.2/accounts — Create Account with `parentaccountid` referencing an existing account GUID, in a Dataverse environment with three sync plug-ins registered (PreValidation, PreOperation, PostOperation) and field-level security on `parentaccountid`.

**Platform Expert Selected:** Dataverse platform expert.

---

## TRACE CONTRACT

```
TRACE-CONTRACT-VERSION: R16-V03
SCENARIO: "POST /api/data/v9.2/accounts -- Create Account with parentaccountid, 3 sync plugins, FLS on parentaccountid"

BOUNDARIES-TO-TRACE:
  BC-1: "OData API entry -- HTTP request receipt and token presence check"
  BC-2: "Authentication -- AAD token validation and system user privilege check"
  BC-3: "Routing -- OData entity set resolution and payload deserialization"
  BC-4: "PreValidation plug-in crossing -- pre-transaction security context"
  BC-5: "PreOperation plug-in crossing -- in-transaction, run-as divergence risk"
  BC-6: "PostOperation plug-in crossing -- post-commit, partial commit risk"
  BC-7: "Storage -- INSERT to AccountBase with FK constraint on parentaccountid"
  BC-8: "Response assembly -- OData-EntityId header and Prefer: return=representation path"

VT-SCOPE-COMMITS:
  VT-1: "user_impersonation"
  VT-2: "prvCreateAccount"
  VT-3: "prvReadAccount"
  VT-4: "FLS write permission on parentaccountid"
  VT-5: "internal service identity"
  TOKEN-COUNT: 5

EXPECTED-HALT-BOUNDARIES:
  HALT-EXPECTED-BOUNDARY: "BC-5 -- PreOperation elevated FLS bypass"
  HALT-EXPECTED-TRIGGER: "F-17 -- Plug-in modifies parentaccountid under elevated run-as context, bypassing caller FLS"
  HALT-EXPECTED-CONDITION: "Step 8b prose asserts coherence for BC-5 AND Step 8c Match? = N for BC-5 row"

CHECKER-CONTRACT:
  MATCH-RULE: Exact string equality between Step8a-Invoked scope string and the corresponding VT-N token string; case-sensitive; whitespace-normalized; character-for-character identity with the quoted VT-N value required.
  HALT-RULE: Fire when Step 8b prose asserts coherence (confirms the three link arms are consistent) AND Step 8c Match? = N for the same boundary row; the simultaneous presence of a prose-coherent claim and a table-level mismatch constitutes a contradiction that must halt the trace.
  OUTPUT-RULE: Assign Row-Verdict = PASS if Match? = Y for that row; assign Row-Verdict = HALT if HALT-RULE fires; emit CHECK RESULT summary line immediately after last row of Step 8c table.
```

---

### Step 1 — Scenario Registration

Per TRACE CONTRACT, this boundary was declared as initial scenario registration. The trace will cover boundaries BC-1 through BC-8 as declared.

- **Operation:** POST /api/data/v9.2/accounts
- **Payload key field:** `parentaccountid` (GUID reference to existing account)
- **Plug-in pipeline:** PreValidation → PreOperation → PostOperation (all synchronous)
- **Security overlay:** Field-level security (FLS) on `parentaccountid`
- **Contract reference:** TRACE CONTRACT declares 8 boundaries (BC-1 through BC-8) and 5 VT scope strings (VT-1 through VT-5)

---

### Step 2 — Role Declaration

Per TRACE CONTRACT, the declared scenario context is Dataverse. Platform expert auto-selected: Dataverse platform expert. The TRACE CONTRACT pre-declares the HALT-RULE; this step confirms the algorithm will be applied as declared.

---

### Step 3 — Authentication Contract

Per TRACE CONTRACT, VT-SCOPE-COMMITS declares five scope strings. The auth contract table maps each to its boundary:

| Boundary | Required Scope / Permission | Token Type | Notes |
|---|---|---|---|
| BC-1: OData API entry | `user_impersonation` (VT-1) | Bearer (AAD) | Environment resource URI audience |
| BC-2: System user privilege check | `prvCreateAccount` (VT-2) | System user + role | Create privilege on account entity |
| BC-2: FLS check on `parentaccountid` | `FLS write permission on parentaccountid` (VT-4) | FLS profile | Write permission on named field |
| BC-7: SQL storage layer | `internal service identity` (VT-5) | Internal | Service-to-service, no caller token |
| BC-4: Parent GUID relationship validation | `prvReadAccount` (VT-3) | System user | Read privilege on account entity |

**Auth contract locked. VT-SCOPE-COMMITS from TRACE CONTRACT confirm 5 distinct scope strings.**

---

### Step 4 — Boundary BC-1: OData API Entry

Per TRACE CONTRACT, BC-1 is declared as: "OData API entry -- HTTP request receipt and token presence check."

The HTTP POST arrives at `/api/data/v9.2/accounts`. The entry point performs: HTTP method check (must be POST), content-type validation (must be `application/json`), URL parsing to extract entity set name `accounts`, and immediate Bearer token presence check. A missing or expired token returns 401 before any routing occurs.

**Failure points at BC-1:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-01 | Missing or expired Bearer token → 401 | Y | No |
| F-02 | Wrong token audience (incorrect environment resource URI) → 401 | Y | No |
| F-03 | Entity set name `accounts` not found in OData metadata → 404 | N | No |
| F-04 | OData metadata cache miss on cold start → routing delay | N | Y |

---

### Step 5 — Boundary BC-2: Authentication

Per TRACE CONTRACT, BC-2 is declared as: "Authentication -- AAD token validation and system user privilege check."

After the routing layer accepts the request, authentication runs four sequential checks: (1) AAD token signature, expiry, audience, and issuer validation; (2) Dataverse system user resolution from AAD OID/UPN — disabled or missing = 403; (3) Privilege check: caller must hold `prvCreateAccount` at scope covering target business unit; (4) FLS pre-check on `parentaccountid`: the caller's FLS profile is evaluated for write access — denial results in silent field strip or hard 400 depending on environment configuration.

**Failure points at BC-2:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-05 | Token expired → 401 | Y | No |
| F-06 | System user not found or disabled → 403 | Y | No |
| F-07 | Missing `prvCreateAccount` → 403 | Y | No |
| F-08 | FLS profile denies write on `parentaccountid` — silent strip or hard 400 | Y | No |
| F-09 | Role/privilege cache miss → synchronous DB lookup latency | N | Y |

---

### Step 6 — Boundary BC-3: Routing

Per TRACE CONTRACT, BC-3 is declared as: "Routing -- OData entity set resolution and payload deserialization."

The OData routing layer resolves the entity set `accounts` to the `account` entity metadata, constructs the Create request handler, deserializes the JSON body into an internal `Entity` object, validates all property names and types against entity metadata, and validates `parentaccountid` as a GUID format. The caller's `ExecutionContext` is attached to the `Entity` object.

**Failure points at BC-3:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-10 | Malformed JSON body → 400 | N | No |
| F-11 | `parentaccountid` not a valid GUID format → 400 | N | No |
| F-12 | Unrecognized property name in payload → 400 | N | No |

---

### Step 7 — Boundaries BC-4, BC-5, BC-6: Plug-in Pipeline

Per TRACE CONTRACT, BC-4 is "PreValidation -- pre-transaction security context"; BC-5 is "PreOperation -- in-transaction, run-as divergence risk" (declared as the EXPECTED-HALT-BOUNDARY); BC-6 is "PostOperation -- post-commit, partial commit risk."

#### BC-4 — PreValidation Plug-in

Per TRACE CONTRACT, BC-4 is declared as a pre-transaction crossing. PreValidation fires before any database transaction is opened. Security context: caller's context (unless run-as user configured). If the plug-in queries Dataverse to validate the parent account, those queries run outside the main transaction and are subject to TOCTOU.

**Failure points — BC-4:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-13 | Plug-in throws `InvalidPluginExecutionException` → 400 | Y | No |
| F-14 | Plug-in timeout (2-min default) → 500 | Y | Y |
| F-15 | Plug-in read of parent account — caller lacks `prvReadAccount` | Y | No |
| F-16 | TOCTOU: parent account deleted between PreValidation check and INSERT | Y | No |

#### BC-5 — PreOperation Plug-in (HALT-EXPECTED-BOUNDARY per TRACE CONTRACT)

Per TRACE CONTRACT, BC-5 is declared as the EXPECTED-HALT-BOUNDARY: "BC-5 -- PreOperation elevated FLS bypass." The HALT-EXPECTED-TRIGGER is F-17. The trace is now executing at the declared halt boundary.

PreOperation fires inside the database transaction. Modifications to the `Target` entity here affect the final INSERT. If the plug-in adds or modifies `parentaccountid` under an elevated run-as context, the caller's FLS restriction is bypassed — the write proceeds under the run-as scope, which may have a broader FLS profile.

**Failure points — BC-5:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-17 | Plug-in modifies `parentaccountid` under elevated run-as context, bypassing caller FLS | Y | No |
| F-18 | Plug-in throws → transaction rollback → 400 | Y | No |
| F-19 | Plug-in latency under transaction lock → lock escalation risk | N | Y |

#### BC-6 — PostOperation Plug-in

Per TRACE CONTRACT, BC-6 is declared as "PostOperation -- post-commit, partial commit risk." PostOperation fires after the INSERT is committed. Cannot roll back the main account record.

**Failure points — BC-6:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-20 | PostOperation failure → partial commit (account created, dependent op failed) | Y | No |
| F-21 | Async misclassification: plug-in registered as sync but behaves async | Y | No |

---

### Step 8 — Auth Verification Checkpoint

Per TRACE CONTRACT, the CHECKER-CONTRACT declares the MATCH-RULE, HALT-RULE, and OUTPUT-RULE. This step applies the declared contract. The TRACE CONTRACT pre-declared HALT-EXPECTED-BOUNDARY: BC-5. The trace will now verify whether the actual execution matches the pre-declared expectation.

**Step 8 Header — VT# Token Reference Set and Checker Algorithm**

Per TRACE CONTRACT VT-SCOPE-COMMITS — verifying declared vs. actual scope strings:

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

**Contract validation — declared vs. actual scope strings:**

| TRACE CONTRACT declared | Step 8 actual | Match? |
|---|---|---|
| VT-1: "user_impersonation" | "user_impersonation" | Y |
| VT-2: "prvCreateAccount" | "prvCreateAccount" | Y |
| VT-3: "prvReadAccount" | "prvReadAccount" | Y |
| VT-4: "FLS write permission on parentaccountid" | "FLS write permission on parentaccountid" | Y |
| VT-5: "internal service identity" | "internal service identity" | Y |

TOKEN-COUNT declared: 5. TOKEN-COUNT actual: 5. Contract scope string declaration validated.

---

**Step 8a — Boundary Invocation Listing**

Per TRACE CONTRACT, boundaries BC-1 through BC-8 were declared. Mapping invoked scopes to each declared boundary:

| Boundary (per TRACE CONTRACT) | Step8a-Invoked Scope / Permission |
|---|---|
| BC-1: OData API entry | `user_impersonation` |
| BC-2: System user privilege check | `prvCreateAccount` |
| BC-2: FLS check on `parentaccountid` | `FLS write permission on parentaccountid` |
| BC-4: PreValidation plug-in read query | `prvReadAccount` |
| BC-7: SQL storage layer | `internal service identity` |
| BC-5: PreOperation elevated FLS bypass | elevated plug-in context (run-as) |

---

**Step 8b — Prose Coherence Confirmation (REQUIRED — one paragraph per Gap?=Y boundary)**

Per TRACE CONTRACT, HALT-EXPECTED-BOUNDARY is BC-5. The prose confirmation must evaluate BC-5 against the declared expectation.

*BC-1 — OData API entry (F-01, F-02) [per TRACE CONTRACT: BC-1]:*
Arm 1: The boundary "OData API entry" maps to `user_impersonation` in Step 3 (VT-1 per TRACE CONTRACT) — confirmed. Arm 2: Step 8a-Invoked `user_impersonation` matches VT-1: "user_impersonation" exactly — confirmed. Arm 3: Step 11 parameters (resource URI=Dataverse env endpoint, tenant ID, environment ID) consistent with `user_impersonation` audience — confirmed. All three arms coherent.

*BC-2 — System user privilege check (F-06, F-07) [per TRACE CONTRACT: BC-2]:*
Arm 1: Boundary maps to `prvCreateAccount` in Step 3 (VT-2) — confirmed. Arm 2: Step 8a-Invoked `prvCreateAccount` matches VT-2: "prvCreateAccount" — confirmed. Arm 3: Step 11 parameters (entity=account, op=Create) consistent — confirmed. All three arms coherent.

*BC-2 — FLS check on `parentaccountid` (F-08) [per TRACE CONTRACT: BC-2]:*
Arm 1: Boundary maps to `FLS write permission on parentaccountid` in Step 3 (VT-4) — confirmed. Arm 2: Step 8a-Invoked `FLS write permission on parentaccountid` matches VT-4 exactly — confirmed. Arm 3: Step 11 parameters (field=parentaccountid, op=write) consistent — confirmed. All three arms coherent.

*BC-4 — PreValidation plug-in read query (F-15) [per TRACE CONTRACT: BC-4]:*
Arm 1: Boundary maps to `prvReadAccount` in Step 3 (VT-3) — confirmed. Arm 2: Step 8a-Invoked `prvReadAccount` matches VT-3: "prvReadAccount" — confirmed. Arm 3: Step 11 parameters (entity=account, op=Read, context=plugin) consistent — confirmed. All three arms coherent.

*BC-5 — PreOperation elevated FLS bypass (F-17) [per TRACE CONTRACT: HALT-EXPECTED-BOUNDARY]:*
Arm 1: This boundary should map to `FLS write permission on parentaccountid` per Step 3 auth contract (VT-4) — the PreOperation plug-in modifies `parentaccountid`, governed by VT-4. Per TRACE CONTRACT, HALT-EXPECTED-BOUNDARY was declared as BC-5 with HALT-EXPECTED-TRIGGER F-17. Arm 1 asserts coherence with the contract declaration. Arm 2: Step 8a-Invoked = "elevated plug-in context (run-as)" does NOT match VT-4: "FLS write permission on parentaccountid" — mismatch confirmed; TRACE CONTRACT expectation is validated. Arm 3: Step 11 parameters confirm plug-in run-as user has different FLS profile than caller — inconsistent with VT-4. HALT-RULE fires. TRACE CONTRACT pre-declared expectation: CONFIRMED.

---

**Step 8c — Match? Table (REQUIRED — positioned before Step 9)**

| Boundary | Step3-Auth | Step8a-Invoked | Step11-Params | Match? | Row-Verdict |
|---|---|---|---|---|---|
| BC-1: OData API entry | `user_impersonation` | `user_impersonation` | resource URI=Dataverse env, tenant ID present | Y | PASS |
| BC-2: System user privilege check | `prvCreateAccount` | `prvCreateAccount` | entity=account, op=Create | Y | PASS |
| BC-2: FLS check on `parentaccountid` | `FLS write permission on parentaccountid` | `FLS write permission on parentaccountid` | field=parentaccountid, op=write | Y | PASS |
| BC-4: PreValidation plug-in read query | `prvReadAccount` | `prvReadAccount` | entity=account, op=Read, context=plugin | Y | PASS |
| BC-7: SQL storage layer | `internal service identity` | `internal service identity` | service-to-service, no caller token | Y | PASS |
| BC-5: PreOperation elevated FLS bypass | `FLS write permission on parentaccountid` | elevated plug-in context (run-as) | plug-in run-as user, FLS profile differs | N | HALT |

`CHECK RESULT: FAIL -- 6 rows, 1 HALT row`

`CONTRADICTION SIGNAL: Seq# 6`
`Scope String Correction (Rem#1): The PreOperation plug-in's run-as context must be constrained to the caller's FLS profile for parentaccountid. Per TRACE CONTRACT, the HALT-EXPECTED-BOUNDARY was BC-5 and the actual HALT fires at BC-5 row — contract expectation confirmed. Remediation: remove run-as user configuration from PreOperation plug-in step so invoked scope becomes "FLS write permission on parentaccountid" matching VT-4, OR add an explicit scope entry in the Step 3 auth contract for the elevated run-as context with a documented security exception.`

**TRACE CONTRACT validation: HALT fired at HALT-EXPECTED-BOUNDARY (BC-5). Contract prediction confirmed.**

---

### Step 9 — Boundary BC-7: Storage Access

Per TRACE CONTRACT, BC-7 is declared as: "Storage -- INSERT to AccountBase with FK constraint on parentaccountid."

The Dataverse SQL backend receives the INSERT request for `AccountBase`:

1. **Relationship validation:** `parentaccountid` GUID validated against `AccountBase.AccountId` via FK constraint. Non-existent GUID = 400.
2. **Transaction scope:** INSERT spans PreOperation and PostOperation in a single transaction. Row-level locks on the parent account record under concurrency may cause wait chains.
3. **Extension tables:** `AccountBase` and `AccountExtensionBase` written atomically. Extension table write failure rolls back the full transaction.
4. **Audit logging:** Audit record written in same transaction if auditing is enabled.

**Failure points at BC-7:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-22 | Parent GUID not found at INSERT → FK constraint violation → 400 | Y | No |
| F-23 | Lock wait on parent account row under concurrency | N | Y |
| F-24 | Extension table write failure → full transaction rollback | N | No |
| F-25 | Audit write latency under high volume | N | Y |

---

### Step 10 — Boundary BC-8: Response Assembly

Per TRACE CONTRACT, BC-8 is declared as: "Response assembly -- OData-EntityId header and Prefer: return=representation path."

On successful INSERT, the OData layer assembles the response. Default: 204 No Content with `OData-EntityId` header. If `Prefer: return=representation` is present, a SELECT on the new record returns 201 with full entity body — this SELECT re-applies FLS, which may strip `parentaccountid` from the response.

**Failure points at BC-8:**

| # | Failure | Gap?= | Latency source? |
|---|---|---|---|
| F-26 | FLS strips `parentaccountid` from returned representation | Y | No |
| F-27 | `Prefer: return=representation` adds read round-trip latency | N | Y |

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
| Plug-in run-as (PreOperation) | Configured run-as user on plug-in step | elevated plug-in context (run-as) |
| Prefer header | `return=representation` (optional) | triggers read FLS re-check |

---

### Step 12 — Error Paths (Complete)

| Error path | HTTP status | Trigger | Failure ref |
|---|---|---|---|
| Missing / expired Bearer token | 401 | BC-1 | F-01, F-05 |
| Wrong token audience | 401 | BC-1 | F-02 |
| System user disabled or not found | 403 | BC-2 | F-06 |
| Missing `prvCreateAccount` | 403 | BC-2 | F-07 |
| FLS hard block on `parentaccountid` | 400 | BC-2 | F-08 |
| Malformed JSON | 400 | BC-3 | F-10 |
| Invalid GUID format for `parentaccountid` | 400 | BC-3 | F-11 |
| PreValidation plug-in exception | 400 | BC-4 | F-13 |
| PreValidation plug-in timeout | 500 | BC-4 | F-14 |
| Missing `prvReadAccount` in plug-in context | 403 | BC-4 | F-15 |
| Parent GUID not found at INSERT | 400 | BC-7 | F-22 |
| PostOperation partial commit | 500 | BC-6 | F-20 |
| FLS strips `parentaccountid` from response | 204/201 field absent | BC-8 | F-26 |
| FLS bypass via elevated plug-in | 204 (security violation) | BC-5 | F-17 |

---

### Step 13 — Failure Catalog (Blast Radius Order)

1. **F-16 TOCTOU** — Parent deleted between PreValidation and INSERT. Blast: silent data integrity corruption.
2. **F-20 PostOperation partial commit** — Account created, dependent operations failed. Blast: orphaned records.
3. **F-17 FLS bypass via elevated plug-in** — Security policy violation. Blast: field written against caller FLS policy; audit risk. *(Per TRACE CONTRACT: this is the HALT-EXPECTED-TRIGGER for BC-5.)*
4. **F-22 Parent GUID not found at INSERT** — Clean 400, FK enforced, data integrity preserved.
5. **F-08 FLS silent strip** — Account created without parent relationship, caller unaware.
6. All other failures — clean HTTP error responses.

---

### Step 14 — Latency Source Summary

| Latency source | Boundary | Severity |
|---|---|---|
| Metadata cache miss on cold start | BC-1 | Low |
| Role/privilege cache miss | BC-2 | Medium |
| Plug-in timeout risk (2-min default) | BC-4 | High |
| Plug-in latency under transaction lock | BC-5 | High |
| Lock wait on parent account row | BC-7 | Medium |
| Audit write under high volume | BC-7 | Low–Medium |
| `Prefer: return=representation` round-trip | BC-8 | Low |

---

### Step 15 — Signal Output

```
signal: trace-request
topic: [topic name from invocation context]
date: 2026-03-15
scenario: POST /api/data/v9.2/accounts with parentaccountid, 3 sync plugins, FLS
variation-axis: output-format (pre-declared trace contract)
trace-contract-version: R16-V03
boundaries-declared: 8 (BC-1 through BC-8)
boundaries-traced: 8 (all declared boundaries executed)
failure-points: 27 (F-01 through F-27)
gap-flagged: 13
check-result: FAIL -- 6 rows, 1 HALT row
contradiction-signals: 1 (Seq# 6 -- BC-5 PreOperation elevated FLS bypass)
halt-expected-boundary: BC-5
halt-actual-boundary: BC-5
contract-prediction: CONFIRMED
latency-sources: 7
```
