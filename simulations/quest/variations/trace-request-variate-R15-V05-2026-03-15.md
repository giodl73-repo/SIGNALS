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