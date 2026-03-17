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

