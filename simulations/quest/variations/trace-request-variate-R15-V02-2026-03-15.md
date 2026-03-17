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

