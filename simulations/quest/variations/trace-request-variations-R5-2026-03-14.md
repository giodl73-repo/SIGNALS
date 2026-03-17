Here are the 5 R5 variations for `trace-request`, written to `simulations/quest/variations/trace-request-variations-R5-2026-03-14.md`.

---

## Summary

| V | Axis | New criteria targeted | Predicted |
|---|------|-----------------------|-----------|
| **V-01** | Output format | C-17 only — dedicated 5-column Remediation Register; inline column removed | 142/150 |
| **V-02** | Lifecycle emphasis | C-18 only — per-row named blocking gate with explicit FAILS conditions | 140/150 |
| **V-03** | Output format (catalog) | C-19 only — Adv? column filled during construction, forward-pointer rule | 142/150 |
| **V-04** | Output format + Lifecycle | C-17 + C-18 — register + per-row gate | 145/150 |
| **V-05** | Full synthesis | All three + R4 V-05 DISQUALIFIER register + role-after-inventory | 150/150 |

---

**What each variation does mechanically:**

**C-17 (V-01, V-04, V-05):** The `Remediation` column is completely removed from the traversal table. It's replaced by a `Rem#` cross-reference column. A separate Remediation Register table carries `Failure Reference | Mechanism Type | Parameters` as discrete columns. "Remediation may not appear as inline text in the traversal table" is stated explicitly — inline annotation is structurally blocked, not just discouraged.

**C-18 (V-02, V-04, V-05):** The exhaustiveness paragraph is replaced by a numbered per-row checklist between Steps 6 and 7. Each row must be named individually with its Seq# list and re-examination result. FAILS conditions are explicit: bare "confirmed," unfilled brackets, and confirmation-after-Step-7-begins all named as failures.

**C-19 (V-03, V-05):** The threat catalog gains an `Adv?` column. The construction rule says "fill Y/N as you write each row — not after reviewing the adversarial scenario." Step 7's cross-reference block must reference the Y-marked row. The DISQUALIFIER in V-05 names all four failure patterns: no column, zero Y, multiple Y, post-hoc filling.

**Why V-01/V-02/V-03 don't reach 150:** Each single-axis variation leaves the other two new criteria at R4 level — C-18 at advisory paragraph (PARTIAL), C-19 absent (FAIL), or C-17 absent (FAIL). This is intentional: the single-axis scoring reveals which of the three criteria is load-bearing for the gap from 142/145 to 150.
-marked row explicitly. V-03/V-04/V-05 add the column with forward-
pointer enforcement rules: "fill Y/N during catalog construction, not after reviewing the
adversarial result."

**Why V-01/V-02/V-03 each predict 150 when single-axis**: C-17, C-18, and C-19 each inherit
from existing criteria (C-17 from C-14 subject matter, C-18 from C-15, C-19 from C-16) but are
independently testable. V-01 fixes C-17 while leaving C-18 and C-19 at R4 V-01 level -- but R4
V-01 already had an exhaustiveness check paragraph (passes C-18 if demonstrated) and a catalog
cross-reference (passes C-19 if candidate column present). Wait -- R4 V-01 lacks the Adv?
column and lacks per-row confirmation. So V-01 predicts: C-18 PARTIAL (assertion without named
rows), C-19 FAIL (no candidate column). Correction to predicted scores below.

---

**Revised predicted scores:**

| V | C-17 | C-18 | C-19 | Other aspirationals | Total |
|---|------|------|------|---------------------|-------|
| V-01 | 5 | PARTIAL (2) | FAIL (0) | 50/50 (C-08 through C-16) | 142/150 |
| V-02 | FAIL (0) | 5 | FAIL (0) | 50/50 | 140/150 |
| V-03 | FAIL (0) | PARTIAL (2) | 5 | 50/50 | 142/150 |
| V-04 | 5 | 5 | FAIL (0) | 50/50 | 145/150 |
| V-05 | 5 | 5 | 5 | 50/50 | 150/150 |

Note: V-01 through V-04 each target one or two new criteria while leaving the third
underspecified -- this is intentional for single-axis testing. V-05 is the 150/150 target.

---

## V-01: Output Format -- Dedicated Remediation Register

**Axis**: Output format -- removes the inline Remediation column from the traversal table and
replaces it with a dedicated Remediation Register table containing three required discrete
columns: Failure Reference, Mechanism Type, Parameters. The traversal table carries only a
cross-reference (Rem#) pointing into the register.

**Hypothesis**: Moving remediation out of the traversal table into a dedicated register makes
C-14 compliance structurally visible: a blank Parameters cell is a missing cell, not a hidden
inline annotation. The register's Mechanism Type column enforces the type-before-values contract
(C-08): a model filling the column in order is forced to name the type before writing parameters.
C-18 remains at R4 V-01 level (advisory exhaustiveness paragraph -- PARTIAL). C-19 absent (no
Adv? column -- FAIL). This variation isolates the C-17 structural mechanism.

```
You are running /trace-request for: {{topic}}

Available platform expert roles (select after Step 3):
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

---

## STEP 1 -- ENTRY POINT

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

DISQUALIFIER: "a POST request" (no path) / "a JSON body" (no field names) /
"an authenticated user" (no credential type) fails C-01.

---

## STEP 2 -- LATENCY BUDGET

Declare the end-to-end latency budget before the boundary inventory.
Source priority:
1. Documented SLA (cite it)
2. Caller configured timeout (state value)
3. UX threshold: 500ms (interactive) / 2000ms (synchronous background) / 10000ms (async)

**Budget: [N]ms** (source: [SLA / timeout value / UX])

Budget accounting rules:
- Sequential boundaries: draws are additive on the critical path
- Parallel branches: only the longest parallel branch draws; concurrent branches share one slot
- Cached steps: < 5ms on cache hit; draw synchronous cost on cache miss

---

## STEP 3 -- BOUNDARY INVENTORY (GATE)

List every boundary in traversal order before filling Step 4. A boundary is any transition
where a network call is made, identity context is evaluated, or data is read from or written
to a store. Token validation, gateway routing, cache lookup, and audit emission are boundaries.

1. [Entry point -- as declared in Step 1]
2. [Second boundary]
3. ...
[Continue until response is assembled and returned to caller]

GATE: Step 4 rows must correspond to the boundaries listed here, in order.
No boundary listed here may be absent from Step 4.

---

## ROLE SELECTION

Review the boundary inventory above and select the platform expert role whose domain covers
the majority of boundaries in scope:
- Dataverse platform expert
- Commerce platform expert
- Power Automate platform expert

**Selected role:** [role]
**Rationale:** [1-2 sentences citing the dominant boundary types identified in Step 3]

This role determines the parameter vocabulary for the Remediation Register below.

---

## STEP 4 -- BOUNDARY TRAVERSAL

One row per boundary from Step 3. All columns required.
Remediation is referenced by Rem# and detailed in the Remediation Register -- do not inline
remediation text here.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Draw type | Rem# |
|---|----------|-----------------|-------|---------------------------|----------|----------|-----------|------|
| 1 |          |                 |       |                           |          |          |           |      |
| 2 |          |                 |       |                           |          |          |           |      |

Column rules:

- **Failure Mode(s)**: Named mechanism required: HTTP status code, timeout threshold + behavior,
  throttle rate + breach behavior, auth rejection type, payload validation rule, network failure
  class. FAILS: "may fail," "could error," "an exception might be thrown."

- **Auth?**: Y or N.

- **Permission / Scope / Role**: Y rows: name the exact artifact (e.g., "prvReadAccount
  privilege," "`orders.write` OAuth scope"). N rows: "AUTH GAP -- [reason]."
  FAILS: "standard auth," "valid token," "handled upstream" without naming the upstream boundary.

- **p50 / p99**: Millisecond estimate or range. FAILS: "fast," "low," blank.
  Sub-5ms entries: "< 5ms -- [reason]."

- **Draw type**: Sequential (adds to chain) or Parallel with [boundary #] (shares slot).

- **Rem#**: Cross-reference to Remediation Register (R-1, R-2, ...). One entry per failure mode.
  A blank Rem# cell signals a missing remediation item.

---

## REMEDIATION REGISTER

One row per remediation item. Each row is a self-contained remediation record.
The register is the only location for remediation content -- remediation may not appear as
inline text in the traversal table.

Use the selected platform expert role's vocabulary for the Parameters column.

| Rem# | Failure Reference (Seq# + Failure Mode) | Mechanism Type | Parameters |
|------|-----------------------------------------|----------------|------------|
| R-1  |                                         |                |            |
| R-2  |                                         |                |            |

Column rules:

- **Failure Reference**: Boundary Seq# from Step 3 plus the failure mode name from Step 4.
  Example: "Seq#2 -- HTTP 429 throttle breach"

- **Mechanism Type**: One of: retry / circuit breaker / scope addition / validation guard.
  FAILS: blank or "handle the error."

- **Parameters**: Quantified operational parameters using the selected role's platform vocabulary.
  Required format by mechanism type:
  - retry: algorithm (linear/exponential/jitter) + initial delay (ms) + multiplier + max-attempts
    [+ jitter range if applicable]
    Example (Dataverse): algorithm=exponential, initial=500ms, multiplier=2x, max-attempts=3
    Example (Power Automate): algorithm=fixed, interval=2min, max-attempts=4 (connector limit)
    Example (Commerce): algorithm=jitter, initial=200ms, jitter=0-400ms, max-attempts=5
  - circuit breaker: failure threshold + time window + reset interval
    Example (Commerce): threshold=3 errors/5s, reset=30s (payment gateway pattern)
    Example (Dataverse): threshold=5 plugin errors/30s, reset=120s
  - scope addition: exact scope string or role identity
    Example: scope=prvWriteAccount, principal=sp-orders-api
    Example: scope=Dataverse.ReadWrite, spn=commerce-checkout-service
  - validation guard: field name + data type constraint + validation predicate at Seq#
    Example: field=orderId, type=GUID, predicate=reject-null-or-non-GUID, enforced-at=Seq#1
  FAILS: Parameters cell blank / "exponential backoff" without values / "reasonable timeout" /
  mechanism type named without numeric or identity-specific operational values.

---

## STEP 5 -- BUDGET RECONCILIATION (SUM CLOSURE GATE)

Review the p50, p99, and Draw type columns from Step 4.

**Part A: Sequential chain**

List every row where Draw type = Sequential, in traversal order:
[boundary #] -> [boundary #] -> ...

Sum their p50 draws: ___ms
Sum their p99 draws: ___ms

**Part B: Parallel branch exclusions**

List every row where Draw type = Parallel with #[N]. For each:
- Which boundary does it share a slot with?
- Confirmed concurrent execution (not a sequential dependency): ___
- Confirmed excluded from Part A sequential sum: ___

**Part C: Critical path totals**

Critical-path p50 = [= Part A p50 sum] ms
Critical-path p99 = [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Part A sequential p50 sum must equal critical-path p50 in Part C. Part A p99 sum
must equal critical-path p99 in Part C. If they differ, return to Step 4 and correct the per-
boundary estimates before continuing. Per-boundary rows are the source of truth.

Budget headroom:
- p50 headroom: [Step 2 budget] - [critical-path p50] = ___ms
- p99 headroom: [Step 2 budget] - [critical-path p99] = ___ms (negative = overrun)

---

## STEP 6 -- THREAT CLASS CATALOG

Build from Step 3's boundary inventory before Step 7. Reference boundary Seq numbers from Step 3.

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger |
|---|---|---|---|---|
| 1 | Malformed input | | | |
| 2 | Credential expiry | | | |
| 3 | Concurrent mutation | | | |
| 4 | Missing permission scope | | | |
| 5 | Network partition | | | |

Rules:
- Minimum 4 rows.
- **All Applicable Boundary Seq#**: list every Step 3 Seq# where this threat class can manifest
  -- not just the highest-risk one. A threat applicable at boundaries 2, 5, and 7 lists: 2, 5, 7.
- Severity: Low / Medium / High.
- After completing: identify the highest-severity row. Ties: prefer the most applicable Seq# entries.

**Exhaustiveness check (C-15)**: After completing the table, for each row, re-examine the
Step 3 boundary inventory. "Can this threat manifest at any boundary NOT already listed in this
row's Seq# column?" If yes, add the missing Seq# before proceeding.
A catalog row that lists one Seq# for a threat known to apply at multiple boundaries fails C-15.

---

## STEP 7 -- ADVERSARIAL SCENARIO

**Catalog cross-reference** (required before tracing):
- Catalog row #: [N from Step 6]
- Threat class: [exact name from Step 6 table]
- All catalog Seq#: [complete list from that Step 6 row]
- Selected divergence Seq#: [the specific Seq# from the catalog list where this scenario diverges]

An adversarial scenario that does not cite a catalog row #, exact threat class name, and a
divergence Seq# drawn from that catalog row's Seq# list fails C-16.

Selected threat class: [highest-severity class from Step 6]
Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Step 3 Seq# -- exact boundary where path splits from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [why this class at this boundary is the highest-risk gap]

---

## STEP 8 -- PASS 2: AUTHORIZATION AUDIT

Walk the full boundary list from Step 3 a second time. Exclusive focus: authorization correctness.

DISQUALIFIER: Fails if this section mirrors Step 4's Auth / Permission columns without raising
new questions. A PASS 2 is not a re-statement of inline auth fields.

For each boundary, assess:
1. Delegation: Is auth explicit here or assumed from an upstream check? If assumed: can a caller
   reach this boundary without the upstream check executing?
2. Escalation: Could adjacent permissions reach a higher-privilege resource through this boundary?
3. Minimum enforcement: Is minimum-required scope enforced? Would an over-permissioned token pass?

Required output: At least one gap or escalation path not raised in Step 4's auth columns.
Or: "PASS 2: no additional gaps --" with specific justification for the three highest-risk
boundaries confirming each is clean.

---

## STEP 9 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

DISQUALIFIER: Fails if it skips intermediate boundaries or states "error returned to caller"
without the propagation chain.

Origin: [boundary name and Step 3 row number]
Failure: [mechanism from Step 4]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## STEP 10 -- BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Step 3 boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?
- Cross-catalog interaction: does this limit interact with any concurrent mutation or
  malformed input class from Step 6?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## V-02: Lifecycle Emphasis -- Per-Row Exhaustiveness Blocking Gate

**Axis**: Lifecycle emphasis -- replaces the exhaustiveness check paragraph after the catalog
with a structured per-row blocking gate. The gate requires naming each catalog row by number,
referencing the Step 3 boundary inventory by name, and reporting the result of re-examination
for each row before the adversarial section is permitted to begin. A single assertion line
("Exhaustiveness check complete") fails. Each row must be named individually.

**Hypothesis**: C-18 fails on two patterns: (a) a bare assertion without named rows, and (b)
a confirmation that appears after the adversarial section begins. Structuring the gate as a
per-row numbered checklist eliminates (a) by requiring row names. Placing it between the catalog
and the adversarial header eliminates (b) by making the gate a mandatory intermediate section.
C-17 absent (inline Remediation column retained -- FAIL). C-19 absent (no Adv? column -- FAIL).
This variation isolates the C-18 lifecycle mechanism.

```
You are running /trace-request for: {{topic}}

Available platform expert roles (select after Step 3):
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

---

## STEP 1 -- ENTRY POINT

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

DISQUALIFIER: "a POST request" (no path) / "a JSON body" (no field names) /
"an authenticated user" (no credential type) fails C-01.

---

## STEP 2 -- LATENCY BUDGET

Declare the end-to-end latency budget before the boundary inventory.
Source priority:
1. Documented SLA (cite it)
2. Caller configured timeout (state value)
3. UX threshold: 500ms (interactive) / 2000ms (synchronous background) / 10000ms (async)

**Budget: [N]ms** (source: [SLA / timeout value / UX])

Budget accounting:
- Sequential boundaries: draws are additive on the critical path
- Parallel branches: only the longest parallel branch draws; concurrent branches share one slot
- Cached steps: < 5ms on cache hit; draw synchronous cost on cache miss

---

## STEP 3 -- BOUNDARY INVENTORY (GATE)

List every boundary in traversal order before filling Step 4. A boundary is any transition
where a network call is made, identity context is evaluated, or data is read from or written
to a store. Token validation, gateway routing, cache lookup, and audit emission are boundaries.

1. [Entry point -- as declared in Step 1]
2. [Second boundary]
3. ...
[Continue until response is assembled and returned to caller]

GATE: Step 4 rows must correspond to the boundaries listed here, in order.
No boundary listed here may be absent from Step 4.

---

## ROLE SELECTION

Review the boundary inventory above and select the platform expert role whose domain covers
the majority of boundaries in scope:
- Dataverse platform expert
- Commerce platform expert
- Power Automate platform expert

**Selected role:** [role]
**Rationale:** [1-2 sentences citing the dominant boundary types identified in Step 3]

This role determines the platform-specific parameter vocabulary for Step 4 Remediation cells.

---

## STEP 4 -- BOUNDARY TRAVERSAL

One row per boundary from Step 3. All columns required.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Draw type | Remediation |
|---|----------|-----------------|-------|---------------------------|----------|----------|-----------|-------------|
| 1 |          |                 |       |                           |          |          |           |             |
| 2 |          |                 |       |                           |          |          |           |             |

Column rules:

- **Failure Mode(s)**: Named mechanism required: HTTP status code, timeout threshold + behavior,
  throttle rate + breach behavior, auth rejection type, payload validation rule, network failure
  class. FAILS: "may fail," "could error," "an exception might be thrown."

- **Auth?**: Y or N.

- **Permission / Scope / Role**: Y rows: exact artifact. N rows: "AUTH GAP -- [reason]."
  FAILS: "standard auth," "valid token," "handled upstream" without naming the upstream boundary.

- **p50 / p99**: Millisecond estimate. FAILS: "fast," "low," blank. Sub-5ms: "< 5ms -- [reason]."

- **Draw type**: Sequential or Parallel with [boundary #].

- **Remediation**: Quantified mechanism required. Use selected role's platform vocabulary.
  Format by mechanism type:
  - Retry: algorithm + initial delay (ms) + multiplier + max-attempts [+ jitter range]
    Example: "exponential: initial=100ms, multiplier=2x, jitter=+/-20%, max-attempts=5"
  - Circuit breaker: failure threshold + time window + reset interval
    Example: "circuit breaker: threshold=5 errors/10s, reset=60s"
  - Scope fix: exact scope string or role identity
    Example: "add prvWriteAccount to service principal sp-orders-api"
  - Validation guard: field name + data type constraint + validation predicate
    Example: "validate customerId: UUID format, reject null at boundary #1"
  FAILS: "add error handling," "add retry logic" (no parameters), "exponential backoff" (no values).

---

## STEP 5 -- BUDGET RECONCILIATION (SUM CLOSURE GATE)

Review the p50, p99, and Draw type columns from Step 4.

**Part A: Sequential chain**

List every row where Draw type = Sequential, in traversal order:
[boundary #] -> [boundary #] -> ...

Sum their p50 draws: ___ms
Sum their p99 draws: ___ms

**Part B: Parallel branch exclusions**

List every row where Draw type = Parallel. For each:
- Which boundary does it share a slot with?
- Confirm concurrent execution (not a sequential dependency)
- Confirm excluded from Part A sum

**Part C: Critical path totals**

Critical-path p50 = [= Part A p50 sum] ms
Critical-path p99 = [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Part A sums must equal Part C totals exactly. If they differ, return to Step 4
and correct the per-boundary estimates. Per-boundary rows are the source of truth.

Budget headroom:
- p50 headroom: [Step 2 budget] - [critical-path p50] = ___ms
- p99 headroom: [Step 2 budget] - [critical-path p99] = ___ms (negative = overrun)

---

## STEP 6 -- THREAT CLASS CATALOG

Build from Step 3's boundary inventory before Step 7.

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger |
|---|---|---|---|---|
| 1 | Malformed input | | | |
| 2 | Credential expiry | | | |
| 3 | Concurrent mutation | | | |
| 4 | Missing permission scope | | | |
| 5 | Network partition | | | |

Rules:
- Minimum 4 rows.
- **All Applicable Boundary Seq#**: list every Step 3 Seq# where this threat can manifest.
  A class applicable at boundaries 2, 5, and 7 must list: 2, 5, 7.
- Severity: Low / Medium / High.
- After completing: identify the highest-severity row.

---

## EXHAUSTIVENESS GATE (required before Step 7)

For each row in the catalog above, re-examine the Step 3 boundary inventory.
For each threat class, answer: "Can this threat manifest at any Step 3 boundary NOT listed in
this row's All Applicable Seq# column?"

Complete the following checklist. Replace brackets with actual row names and Seq# findings.
Do not proceed to Step 7 until every row has a named entry here.

- Row 1 ([Threat Class name]): Re-examined against Step 3 inventory.
  Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 2 ([Threat Class name]): Re-examined against Step 3 inventory.
  Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 3 ([Threat Class name]): Re-examined against Step 3 inventory.
  Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 4 ([Threat Class name]): Re-examined against Step 3 inventory.
  Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
- Row 5 ([Threat Class name]): Re-examined against Step 3 inventory.
  Boundaries in catalog: [Seq# list]. Additional Seq# found: [Seq# added, or "none"].
[Add one line per additional catalog row]

GATE: Step 7 may not begin until this checklist is complete with named rows and Seq# results.
FAILS: a bare "Exhaustiveness check complete" without named rows / any row with brackets
unfilled / any row that omits the Boundaries-in-catalog value / confirmation that appears
after Step 7 has begun.

---

## STEP 7 -- ADVERSARIAL SCENARIO

**Catalog cross-reference** (required before tracing):
- Catalog row #: [N from Step 6]
- Threat class: [exact name from Step 6 table]
- All catalog Seq#: [complete list from that Step 6 row]
- Selected divergence Seq#: [the specific Seq# from the catalog list where this scenario diverges]

An adversarial scenario that does not cite a catalog row #, exact threat class name, and a
divergence Seq# from that row's Seq# list fails C-16.

Selected threat class: [highest-severity class from Step 6]
Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Step 3 Seq# -- exact boundary where path splits from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [why this class at this boundary is the highest-risk gap]

---

## STEP 8 -- PASS 2: AUTHORIZATION AUDIT

Walk the full boundary list from Step 3 a second time. Exclusive focus: authorization correctness.

DISQUALIFIER: Fails if this section mirrors Step 4's Auth / Permission columns without raising
new questions.

For each boundary, assess:
1. Delegation: Is auth explicit here or assumed from upstream? Can a caller bypass the upstream check?
2. Escalation: Could adjacent permissions reach a higher-privilege resource through this boundary?
3. Minimum enforcement: Is minimum-required scope enforced? Would an over-permissioned token pass?

Required: At least one gap or escalation path not raised in Step 4's auth columns.
Or: "PASS 2: no additional gaps --" with specific justification for the three highest-risk
boundaries confirming each is clean.

---

## STEP 9 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

DISQUALIFIER: Fails if it skips intermediate boundaries or states "error returned to caller"
without the propagation chain.

Origin: [boundary name and Step 3 row number]
Failure: [mechanism from Step 4]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## STEP 10 -- BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Step 3 boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?
- Cross-catalog interaction: does this limit interact with any concurrent mutation or
  malformed input class from Step 6?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## V-03: Output Format (Catalog) -- Adversarial Candidate Pre-Marked

**Axis**: Output format (threat catalog) -- adds an "Adv?" column to the threat class catalog.
The column must be filled Y/N during catalog construction (not post-hoc). Exactly one row is
marked Y -- the adversarial candidate. The adversarial section must reference the Y-marked row.

**Hypothesis**: C-19 requires the adversarial selection to be a forward pointer established
during systematic enumeration, not a backward rationalization after the scenario is chosen.
Adding "Adv?" as a column in the catalog table with a fill-during-construction rule creates
the commitment during Step 6 (enumeration mode), when the model reasons about threat severity
across the full catalog, rather than during Step 7 (adversarial selection mode), when it may
rationalize whatever scenario it already has in mind. The column-level rule ("fill Y/N for each
row as you complete the catalog, not after Step 7") is the key mechanism. C-17 absent (inline
Remediation retained -- FAIL). C-18 at advisory level (exhaustiveness paragraph -- PARTIAL).
This variation isolates the C-19 pre-marking mechanism.

```
You are running /trace-request for: {{topic}}

Available platform expert roles (select after Step 3):
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

---

## STEP 1 -- ENTRY POINT

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

DISQUALIFIER: "a POST request" (no path) / "a JSON body" (no field names) /
"an authenticated user" (no credential type) fails C-01.

---

## STEP 2 -- LATENCY BUDGET

Declare the end-to-end latency budget before the boundary inventory.
Source priority:
1. Documented SLA (cite it)
2. Caller configured timeout (state value)
3. UX threshold: 500ms (interactive) / 2000ms (synchronous background) / 10000ms (async)

**Budget: [N]ms** (source: [SLA / timeout value / UX])

Budget accounting:
- Sequential boundaries: draws are additive on the critical path
- Parallel branches: only the longest parallel branch draws; concurrent branches share one slot
- Cached steps: < 5ms on cache hit; draw synchronous cost on cache miss

---

## STEP 3 -- BOUNDARY INVENTORY (GATE)

List every boundary in traversal order before filling Step 4. A boundary is any transition
where a network call is made, identity context is evaluated, or data is read from or written
to a store. Token validation, gateway routing, cache lookup, and audit emission are boundaries.

1. [Entry point -- as declared in Step 1]
2. [Second boundary]
3. ...
[Continue until response is assembled and returned to caller]

GATE: Step 4 rows must correspond to the boundaries listed here, in order.
No boundary listed here may be absent from Step 4.

---

## ROLE SELECTION

Review the boundary inventory above and select the platform expert role whose domain covers
the majority of boundaries in scope:
- Dataverse platform expert
- Commerce platform expert
- Power Automate platform expert

**Selected role:** [role]
**Rationale:** [1-2 sentences citing the dominant boundary types identified in Step 3]

This role determines the platform-specific parameter vocabulary for Step 4 Remediation cells.

---

## STEP 4 -- BOUNDARY TRAVERSAL

One row per boundary from Step 3. All columns required.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Draw type | Remediation |
|---|----------|-----------------|-------|---------------------------|----------|----------|-----------|-------------|
| 1 |          |                 |       |                           |          |          |           |             |
| 2 |          |                 |       |                           |          |          |           |             |

Column rules:

- **Failure Mode(s)**: Named mechanism required. FAILS: "may fail," "could error," "might throw."

- **Auth?**: Y or N.

- **Permission / Scope / Role**: Y rows: exact artifact. N rows: "AUTH GAP -- [reason]."
  FAILS: "standard auth," "valid token," "handled upstream" without naming the upstream boundary.

- **p50 / p99**: Millisecond estimate. FAILS: "fast," "low," blank.

- **Draw type**: Sequential or Parallel with [boundary #].

- **Remediation**: Quantified mechanism. Use selected role's platform vocabulary.
  Format by mechanism type:
  - Retry: algorithm + initial delay (ms) + multiplier + max-attempts [+ jitter range]
    Example: "exponential: initial=100ms, multiplier=2x, jitter=+/-20%, max-attempts=5"
  - Circuit breaker: threshold + window + reset interval
    Example: "circuit breaker: threshold=5 errors/10s, reset=60s"
  - Scope fix: exact scope string or role identity
  - Validation guard: field + type constraint + predicate at boundary #
  FAILS: "add error handling," "exponential backoff" without values.

---

## STEP 5 -- BUDGET RECONCILIATION (SUM CLOSURE GATE)

Review p50, p99, and Draw type from Step 4.

**Part A: Sequential chain**
List every Sequential row: [boundary #] -> [boundary #] -> ...
Sum their p50 draws: ___ms | Sum their p99 draws: ___ms

**Part B: Parallel branch exclusions**
For each Parallel row: partner Seq#, confirmed concurrent, confirmed excluded from Part A.

**Part C: Critical path totals**
Critical-path p50 = [= Part A p50 sum] ms
Critical-path p99 = [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Part A sums must equal Part C totals. If they differ, correct Step 4 first.

Budget headroom:
- p50 headroom: [Step 2] - [critical p50] = ___ms
- p99 headroom: [Step 2] - [critical p99] = ___ms

---

## STEP 6 -- THREAT CLASS CATALOG

Build from Step 3's boundary inventory before Step 7. The "Adv?" column must be filled Y/N
as you complete each row during catalog construction -- not after reviewing the adversarial
scenario in Step 7.

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger | Adv? |
|---|---|---|---|---|---|
| 1 | Malformed input | | | | |
| 2 | Credential expiry | | | | |
| 3 | Concurrent mutation | | | | |
| 4 | Missing permission scope | | | | |
| 5 | Network partition | | | | |

Rules:
- Minimum 4 rows.
- **All Applicable Boundary Seq#**: list every Step 3 Seq# where this threat can manifest.
  A class applicable at boundaries 2, 5, and 7 must list: 2, 5, 7.
- Severity: Low / Medium / High.
- **Adv?** column rules:
  - Fill each cell Y or N as you write that row -- not after Step 7 begins.
  - Mark Y on exactly one row: the highest-severity threat class. Ties: prefer the row with
    the most applicable Seq# entries (highest boundary coverage).
  - All other rows: N.
  - FAILS: no Adv? column / Y on zero rows / Y on two or more rows / any cell left blank /
    any cell filled after the adversarial section begins.

**Exhaustiveness check (C-15)**: After completing the table, for each row, re-examine the
Step 3 boundary inventory. "Can this threat manifest at any boundary NOT already listed?"
If yes, add the missing Seq# before proceeding.

---

## STEP 7 -- ADVERSARIAL SCENARIO

**Catalog cross-reference** (required before tracing):
- Catalog row #: [N -- the row marked Adv? = Y]
- Threat class: [exact name from Step 6 catalog, Adv? = Y row]
- All catalog Seq#: [complete Seq# list from the Adv? = Y row]
- Selected divergence Seq#: [the specific Seq# from the list above where this scenario diverges]

An adversarial scenario that references a catalog row not pre-marked Adv? = Y fails C-19.
An adversarial scenario that omits the cross-reference block fails C-16.

Selected threat class: [from Adv? = Y row in Step 6]
Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Step 3 Seq# -- exact boundary where path splits from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [why this class at this boundary is the highest-risk gap]

---

## STEP 8 -- PASS 2: AUTHORIZATION AUDIT

Walk the full boundary list from Step 3 a second time. Exclusive focus: authorization correctness.

DISQUALIFIER: Fails if this section mirrors Step 4's Auth / Permission columns without raising
new questions.

For each boundary, assess:
1. Delegation: Is auth explicit here or assumed from upstream?
2. Escalation: Could adjacent permissions reach a higher-privilege resource through this boundary?
3. Minimum enforcement: Is minimum-required scope enforced?

Required: At least one gap not raised in Step 4.
Or: "PASS 2: no additional gaps --" with per-boundary justification for the three highest-risk.

---

## STEP 9 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

DISQUALIFIER: Fails if it skips boundaries or states "error returned to caller" without chain.

Origin: [boundary name and Seq#]
Failure: [mechanism from Step 4]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## STEP 10 -- BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Step 3 boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?
- Cross-catalog interaction: does this limit interact with any threat class from Step 6?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## V-04: Output Format + Lifecycle -- Dedicated Register + Per-Row Exhaustiveness Gate

**Axes**: Output format (C-17 Remediation Register from V-01) + Lifecycle emphasis (C-18 per-row
gate from V-02). Role is selected after Step 3 (R4 V-01 mechanism preserved). C-19 absent (no
Adv? column in this variation -- only two of the three new criteria are combined here).

**Hypothesis**: C-17 and C-18 are the two criteria most likely to interact: the register is
the source of remediation records, and the exhaustiveness gate confirms that threat records
are complete before the adversarial section. Combining both creates a document where (a)
remediation is structurally isolated and inspectable, and (b) threat coverage is demonstrably
confirmed row by row. A model generating this response cannot satisfy C-17 and C-18 without
explicitly completing both structures. C-19 is not included so R5 scoring can isolate whether
C-17+C-18 together reach 145/150 without C-19.

```
You are running /trace-request for: {{topic}}

Available platform expert roles (select after Step 3):
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

---

## STEP 1 -- ENTRY POINT

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

DISQUALIFIER: "a POST request" (no path) / "a JSON body" (no field names) /
"an authenticated user" (no credential type) fails C-01.

---

## STEP 2 -- LATENCY BUDGET

Declare the end-to-end latency budget before the boundary inventory.
Source priority:
1. Documented SLA (cite it)
2. Caller configured timeout (state value)
3. UX threshold: 500ms (interactive) / 2000ms (synchronous background) / 10000ms (async)

**Budget: [N]ms** (source: [SLA / timeout value / UX])

Budget accounting:
- Sequential boundaries: draws are additive on the critical path
- Parallel branches: only the longest parallel branch draws; concurrent branches share one slot
- Cached steps: < 5ms on cache hit; draw synchronous cost on cache miss

---

## STEP 3 -- BOUNDARY INVENTORY (GATE)

List every boundary in traversal order before filling Step 4. A boundary is any transition
where a network call is made, identity context is evaluated, or data is read from or written
to a store. Token validation, gateway routing, cache lookup, and audit emission are boundaries.

1. [Entry point -- as declared in Step 1]
2. [Second boundary]
3. ...
[Continue until response is assembled and returned to caller]

GATE: Step 4 rows must correspond to the boundaries listed here, in order.
No boundary listed here may be absent from Step 4.

---

## ROLE SELECTION

Review the boundary inventory above and select the platform expert role whose domain covers
the majority of boundaries in scope:
- Dataverse platform expert
- Commerce platform expert
- Power Automate platform expert

**Selected role:** [role]
**Rationale:** [1-2 sentences citing the dominant boundary types identified in Step 3]

This role determines the parameter vocabulary for the Remediation Register below.

---

## STEP 4 -- BOUNDARY TRAVERSAL

One row per boundary from Step 3. All columns required.
Remediation is cross-referenced by Rem# and detailed exclusively in the Remediation Register.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Draw type | Rem# |
|---|----------|-----------------|-------|---------------------------|----------|----------|-----------|------|
| 1 |          |                 |       |                           |          |          |           |      |
| 2 |          |                 |       |                           |          |          |           |      |

Column rules:

- **Failure Mode(s)**: Named mechanism required. FAILS: "may fail," "could error," "might throw."
- **Auth?**: Y or N.
- **Permission / Scope / Role**: Y rows: exact artifact. N rows: "AUTH GAP -- [reason]."
  FAILS: "standard auth," "valid token," "handled upstream" without naming the upstream boundary.
- **p50 / p99**: Millisecond estimate. FAILS: "fast," "low," blank.
- **Draw type**: Sequential or Parallel with [boundary #].
- **Rem#**: Cross-reference to Remediation Register entry. Every failure mode requires a Rem#.
  A blank Rem# signals a missing remediation record.

---

## REMEDIATION REGISTER

One row per remediation item, keyed by Rem#. This is the only location for remediation content.
Remediation must not appear as inline text in the traversal table.
Use the selected platform expert role's vocabulary for the Parameters column.

| Rem# | Failure Reference (Seq# + Failure Mode) | Mechanism Type | Parameters |
|------|-----------------------------------------|----------------|------------|
| R-1  |                                         |                |            |
| R-2  |                                         |                |            |

Column rules:

- **Failure Reference**: Boundary Seq# from Step 3 plus the failure mode name from Step 4.
  Example: "Seq#3 -- token expiry (HTTP 401)"

- **Mechanism Type**: retry / circuit breaker / scope addition / validation guard.
  FAILS: blank or "handle the error."

- **Parameters**: Quantified operational values using the selected role's platform vocabulary.
  Required format by mechanism type:
  - retry: algorithm=exponential, initial=Nms, multiplier=Nx, max-attempts=N [, jitter=+/-X%]
    Example (Dataverse): algorithm=exponential, initial=500ms, multiplier=2x, max-attempts=3
    Example (Power Automate): algorithm=fixed, interval=2min, max-attempts=4 (connector limit)
    Example (Commerce): algorithm=jitter, initial=200ms, jitter=0-400ms, max-attempts=5
  - circuit breaker: threshold=N errors/Xs, reset=Ns
    Example (Dataverse): threshold=5 plugin errors/30s, reset=120s
  - scope addition: scope=[exact string], principal=[identity]
    Example: scope=prvReadEntity, principal=sp-portal-service
  - validation guard: field=[name], type=[type], predicate=[rule], enforced-at=Seq#N
    Example: field=accountId, type=GUID, predicate=reject-null-or-non-GUID, enforced-at=Seq#1
  FAILS: blank / "retry logic" / "exponential backoff" without values / mechanism without numbers.

---

## STEP 5 -- BUDGET RECONCILIATION (SUM CLOSURE GATE)

Review p50, p99, and Draw type from Step 4.

**Part A: Sequential chain**

List every row where Draw type = Sequential, in traversal order:
[boundary #] -> [boundary #] -> ...

Sum their p50 draws: ___ms
Sum their p99 draws: ___ms

**Part B: Parallel branch exclusions**

For each Parallel row: partner Seq#, confirmed concurrent, confirmed excluded from Part A sum.

**Part C: Critical path totals**

Critical-path p50 = [= Part A p50 sum] ms
Critical-path p99 = [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Part A sums must equal Part C totals exactly. Mismatch: return to Step 4.

Budget headroom:
- p50 headroom: [Step 2 budget] - [critical-path p50] = ___ms
- p99 headroom: [Step 2 budget] - [critical-path p99] = ___ms (negative = overrun)

---

## STEP 6 -- THREAT CLASS CATALOG

Build from Step 3's boundary inventory. Complete before Step 7.

| # | Threat Class | All Applicable Boundary Seq# | Severity | Example Trigger |
|---|---|---|---|---|
| 1 | Malformed input | | | |
| 2 | Credential expiry | | | |
| 3 | Concurrent mutation | | | |
| 4 | Missing permission scope | | | |
| 5 | Network partition | | | |

Rules:
- Minimum 4 rows.
- **All Applicable Boundary Seq#**: list every Step 3 Seq# where this threat can manifest.
  A class applicable at boundaries 2, 5, and 7 must list: 2, 5, 7.
- Severity: Low / Medium / High.
- After completing: identify the highest-severity row.

---

## EXHAUSTIVENESS GATE (required before Step 7)

For each catalog row above, re-examine the Step 3 boundary inventory.
Complete the following per-row checklist. Name every row. Do not proceed to Step 7 until all
entries are filled with actual row names, actual Seq# values, and explicit findings.

- Row 1 ([Threat Class]): Boundaries in catalog: [Seq# list from table].
  Re-examined Step 3: boundary [X] applicable? [Yes/No]. [Seq# added, or "no additions"].
- Row 2 ([Threat Class]): Boundaries in catalog: [Seq# list].
  Re-examined Step 3: boundary [X] applicable? [Yes/No]. [Seq# added, or "no additions"].
- Row 3 ([Threat Class]): Boundaries in catalog: [Seq# list].
  Re-examined Step 3: boundary [X] applicable? [Yes/No]. [Seq# added, or "no additions"].
- Row 4 ([Threat Class]): Boundaries in catalog: [Seq# list].
  Re-examined Step 3: boundary [X] applicable? [Yes/No]. [Seq# added, or "no additions"].
- Row 5 ([Threat Class]): Boundaries in catalog: [Seq# list].
  Re-examined Step 3: boundary [X] applicable? [Yes/No]. [Seq# added, or "no additions"].
[One line per additional catalog row]

Gate summary: "Exhaustiveness check complete -- [N] rows reviewed against Step 3 inventory,
[X] Seq# additions made." Or: "no additions found for any row."

FAILS: bare "confirmed" / any row with brackets unfilled / confirmation after Step 7 begins /
gate section omitted entirely.

---

## STEP 7 -- ADVERSARIAL SCENARIO

**Catalog cross-reference** (required before tracing):
- Catalog row #: [N from Step 6]
- Threat class: [exact name from Step 6 table]
- All catalog Seq#: [complete list from that Step 6 row]
- Selected divergence Seq#: [the specific Seq# from the catalog list where this scenario diverges]

An adversarial scenario that does not cite catalog row #, exact threat class name, and a
divergence Seq# drawn from that catalog row's list fails C-16.

Selected threat class: [highest-severity class from Step 6]
Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Step 3 Seq# -- exact boundary where path splits from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [why this class at this boundary is the highest-risk gap]

---

## STEP 8 -- PASS 2: AUTHORIZATION AUDIT

Walk the full boundary list from Step 3 a second time. Exclusive focus: authorization correctness.

DISQUALIFIER: Fails if this section mirrors Step 4's Auth / Permission columns without raising
new questions.

For each boundary, assess:
1. Delegation: Is auth explicit here or assumed from upstream?
2. Escalation: Could adjacent permissions reach a higher-privilege resource through this boundary?
3. Minimum enforcement: Is minimum-required scope enforced?

Required: At least one gap not raised in Step 4.
Or: "PASS 2: no additional gaps --" with per-boundary justification for the three highest-risk.

---

## STEP 9 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

DISQUALIFIER: Fails if it skips boundaries or states "error returned to caller" without chain.

Origin: [boundary name and Seq#]
Failure: [mechanism from Step 4]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## STEP 10 -- BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Step 3 boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?
- Cross-catalog interaction: does this limit interact with any threat class from Step 6?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## V-05: Full Synthesis -- Register + Per-Row Gate + Adv? Column + DISQUALIFIER Register

**Axes**: All three new criteria (C-17 Remediation Register, C-18 per-row exhaustiveness gate,
C-19 Adv? pre-marking column) plus the full DISQUALIFIER register from R4 V-05 and the
role-after-inventory sequencing from R4 V-01. This is the maximum-enforcement variation: every
criterion has at least one structural mechanism plus a DISQUALIFIER that names the exact failure
pattern it prevents.

**Hypothesis**: C-17 is addressed structurally (register table) and by exclusion (Remediation
column removed from traversal, making inline annotation structurally impossible). C-18 is
addressed by per-row named confirmation with explicit FAILS conditions (bare "confirmed" named
as failing, brackets unfilled named as failing, post-section confirmation named as failing).
C-19 is addressed by the Adv? column construction rule (fill during enumeration) plus the
cross-reference block in Step 7 requiring the Y-marked row. Belt-and-suspenders on all three,
preserving all R4 V-05 mechanisms intact.

```
You are running /trace-request for: {{topic}}

Available platform expert roles (select after Step 3):
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

---

## STEP 1 -- ENTRY POINT

DISQUALIFIER (C-01): Entry points matching these patterns fail:
"a POST request" (no path) / "a JSON body" (no field names) / "an authenticated user" (no
credential type named)

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

---

## STEP 2 -- LATENCY BUDGET

Declare the end-to-end latency budget before the boundary inventory.
Source priority:
1. Documented SLA (cite it)
2. Caller configured timeout (state value)
3. UX threshold: 500ms (interactive) / 2000ms (synchronous background) / 10000ms (async)

**Budget: [N]ms** (source: [SLA / timeout value / UX])

Accounting: sequential boundaries sum on the critical path. Parallel branches share a slot.
Cached steps draw < 5ms on hit; draw synchronous cost on miss.

---

## STEP 3 -- BOUNDARY INVENTORY (GATE)

List every boundary in traversal order. Do not fill Step 4's table until this inventory is
complete.

A boundary: any transition where a network call is made, identity context is evaluated,
or data is read from or written to a store. Token validation, gateway routing, cache lookup,
and audit emission are boundaries.

1. [Entry point -- as declared in Step 1]
2. [Second boundary]
3. ...
[Continue until response is assembled and returned to caller]

GATE: Every row in Step 4 must correspond to a boundary listed here, in order.
No boundary listed here may be absent from Step 4.

---

## ROLE SELECTION

Review the boundary inventory above and select the platform expert role whose domain covers
the majority of boundaries in scope:
- Dataverse platform expert
- Commerce platform expert
- Power Automate platform expert

**Selected role:** [role]
**Rationale:** [1-2 sentences citing dominant boundary types from Step 3]

This role determines the platform-specific parameter vocabulary for the Remediation Register.

---

## STEP 4 -- PASS 1 TRAVERSAL TABLE

One row per boundary from Step 3. Every column required. Column DISQUALIFIERS apply per cell.
Remediation items are numbered (R-1, R-2, ...) and detailed exclusively in the Remediation
Register. Do not write remediation text inline in this table.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 draw (ms) | p99 draw (ms) | Draw type | Rem# |
|---|----------|-----------------|-------|---------------------------|---------------|---------------|-----------|------|
| 1 |          |                 |       |                           |               |               |           |      |
| 2 |          |                 |       |                           |               |               |           |      |

**Column DISQUALIFIERS:**

- **Failure Mode(s)**: FAILS if cell contains: "may fail," "could error," "might throw," "an
  exception could occur," "returns an error" without naming the mechanism.
  Required: HTTP status code / timeout threshold + behavior / throttle rate + breach behavior /
  auth rejection type (token expired / scope missing / role not assigned) / payload validation
  rule / network failure class.

- **Auth?**: Binary Y or N only.

- **Permission / Scope / Role**: FAILS for Y rows if cell contains: "standard auth," "valid
  token," "authenticated user," "authorization handled upstream" without naming the upstream
  boundary Seq#.
  Required Y rows: exact artifact (e.g., "Dataverse `prvReadAccount` security privilege,"
  "Commerce `orders.write` OAuth scope," "Automate `flows.run` Entra app permission").
  Required N rows: "AUTH GAP -- [specific reason authorization is absent at this boundary]."

- **p50 draw / p99 draw**: FAILS if cell contains: "fast," "low," "negligible," or is blank.
  Required: ms value or range. Sub-5ms: "< 5ms -- [reason]."

- **Draw type**: Required format: "Sequential" or "Parallel with #[Seq#]".

- **Rem#**: Cross-reference to Remediation Register (R-1, R-2, ...). Every failure mode requires
  at least one Rem# reference. A blank Rem# signals a missing remediation record.

---

## REMEDIATION REGISTER

One row per remediation item, keyed by Rem#. This is the only location for remediation content.
Remediation may not appear as inline text in the traversal table above.
Use the selected platform expert role's vocabulary for the Parameters column.

| Rem# | Failure Reference (Seq# + Failure Mode) | Mechanism Type | Parameters |
|------|-----------------------------------------|----------------|------------|
| R-1  |                                         |                |            |
| R-2  |                                         |                |            |

**Column DISQUALIFIERS (C-14, C-17):**

- **Mechanism Type**: retry / circuit breaker / scope addition / validation guard.
  FAILS: blank / "handle the error" / "add error handling."

- **Parameters**: FAILS if cell matches any of these patterns:
  - Blank
  - "retry logic" or "retry with backoff" (no algorithm, no values)
  - "exponential backoff" (no initial delay, no multiplier, no max-attempts)
  - "add retry" (no parameters)
  - "reasonable timeout" (no numeric value)
  - Any mechanism type named without associated numeric or identity-specific operational values
  PASSES (required format by type, using role-specific vocabulary):
  - retry: algorithm=exponential, initial=Nms, multiplier=Nx, max-attempts=N [, jitter=+/-X%]
    Example (Dataverse): algorithm=exponential, initial=500ms, multiplier=2x, max-attempts=3
    Example (Power Automate): algorithm=fixed, interval=2min, max-attempts=4 (connector limit)
    Example (Commerce): algorithm=jitter, initial=200ms, jitter=0-400ms, max-attempts=5
  - circuit breaker: threshold=N errors/Xs, reset=Ns
    Example (Dataverse): threshold=5 plugin errors/30s, reset=120s
    Example (Commerce): threshold=3 errors/5s, reset=30s (payment gateway timeout pattern)
  - scope addition: scope=[exact string], principal=[identity]
    Example: scope=prvWriteAccount, principal=sp-orders-api
  - validation guard: field=[name], type=[type], predicate=[rule], enforced-at=Seq#N
    Example: field=orderId, type=GUID, predicate=reject-null-or-non-GUID, enforced-at=Seq#1

---

## STEP 5 -- CRITICAL PATH AND BUDGET RECONCILIATION

Review p50 draw, p99 draw, and Draw type from Step 4.

**DISQUALIFIER (C-12)**: Fails if any of the following:
- Critical-path p50 does not equal the sum of Sequential p50 draw cells in Step 4
- Critical-path p99 does not equal the sum of Sequential p99 draw cells in Step 4
- A row marked "Parallel with #[N]" has its draw included in the sequential sum

**Part A: Sequential chain**

List every row where Draw type = Sequential, in traversal order:
[Seq#] -> [Seq#] -> ...

Sum their p50 draws: ___ms
Sum their p99 draws: ___ms

**Part B: Parallel branch exclusions**

For every row where Draw type = Parallel with #[Seq#]:
- Partner boundary Seq#
- Confirmed concurrent execution (not a sequential dependency)
- Confirmed excluded from Part A sum
- Longer of the pair (contributes to slot): [Seq# -- p99 value]

**Part C: Critical path statement**

Critical-path p50: [= Part A p50 sum] ms
Critical-path p99: [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Part C totals must equal Part A sums exactly. If they differ, return to Step 4.

Budget headroom:
- p50 headroom: [Step 2 budget] - [critical-path p50] = ___ms
- p99 headroom: [Step 2 budget] - [critical-path p99] = ___ms (negative = overrun)

---

## STEP 6 -- THREAT CLASS CATALOG

Build from Step 3's boundary inventory before Step 7. Complete before the Exhaustiveness Gate.

The "Adv?" column must be filled Y/N for each row during catalog construction -- as you write
each row. Do not fill the Adv? column after reviewing the adversarial scenario in Step 7.

**DISQUALIFIER (C-13)**: Fails if any of the following:
- Fewer than 4 threat class rows
- Any threat class row lists only one "highest-risk boundary" rather than all applicable Seq#
- Any Seq# does not correspond to a Step 3 boundary row
- Catalog is written after the adversarial scenario in Step 7

**DISQUALIFIER (C-15)**: Fails if any catalog row matches these patterns:
- Single Seq# for a threat class that can also manifest at additional Step 3 boundaries
- Uses "multiple," "various," "all boundaries" instead of enumerating Seq# values
- Gate checklist below is omitted or answered without per-row named entries

**DISQUALIFIER (C-19)**: Fails if any of the following:
- No Adv? column present in the catalog table
- Adv? column has zero Y values
- Adv? column has two or more Y values
- Any Adv? cell is blank
- Adv? column is filled after the adversarial section begins (post-hoc rationalization)

| # | Threat Class | All Applicable Boundaries (Seq#) | Severity | Example Trigger at Highest-Risk Boundary | Adv? |
|---|---|---|---|---|---|
| 1 | Malformed input | | | | |
| 2 | Credential expiry | | | | |
| 3 | Concurrent mutation | | | | |
| 4 | Missing permission scope | | | | |
| 5 | Network partition | | | | |

Rules:
- **All Applicable Boundaries (Seq#)**: list every Step 3 Seq# where this class can manifest.
  A class applicable at boundaries 1, 3, and 5 lists "1, 3, 5" -- not just "3."
- **Adv?**: Mark Y on exactly one row -- the highest-severity class. Ties: prefer the most
  applicable Seq# entries. All other rows: N. Fill each cell now, not after Step 7.
- Minimum 4 rows; add rows for additional threat classes relevant to this request.

---

## EXHAUSTIVENESS GATE (required before Step 7)

For each catalog row, re-examine the Step 3 boundary inventory.
Complete the following per-row checklist. Do not proceed to Step 7 until all entries are filled
with actual row names, actual Seq# values, and explicit findings.

- Row 1 ([Threat Class]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list from table].
  Re-examined Step 3 inventory: [new Seq# found, or "no additions"].
- Row 2 ([Threat Class]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list].
  Re-examined Step 3 inventory: [new Seq# found, or "no additions"].
- Row 3 ([Threat Class]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list].
  Re-examined Step 3 inventory: [new Seq# found, or "no additions"].
- Row 4 ([Threat Class]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list].
  Re-examined Step 3 inventory: [new Seq# found, or "no additions"].
- Row 5 ([Threat Class]): Adv? = [Y/N]. Boundaries in catalog: [Seq# list].
  Re-examined Step 3 inventory: [new Seq# found, or "no additions"].
[One line per additional catalog row]

Gate summary: "Exhaustiveness check complete -- [N] rows reviewed against Step 3 inventory,
[X] Seq# additions made." Or: "no additions for any row."

FAILS (C-18): bare "confirmed" without named rows / any row with brackets unfilled /
confirmation appearing after Step 7 has begun / gate section omitted.

---

## STEP 7 -- ADVERSARIAL SCENARIO

**DISQUALIFIER (C-16)**: Fails if any of the following:
- Adversarial scenario introduces a threat condition not drawn from the Step 6 catalog
- Scenario does not name the catalog threat class by its exact Step 6 label
- Scenario does not cite the specific Seq# from the catalog row's All Applicable Boundaries
  column where divergence occurs
- Reference is vague: "based on credential threats," "similar to row 2," "a token expiry
  scenario" without naming catalog row #, exact class, and divergence Seq#
- Adversarial scenario references a catalog row where Adv? = N (violates C-19)

**Catalog cross-reference** (required before the scenario trace):
- Catalog row #: [N -- the row marked Adv? = Y]
- Threat class: [exact name from Step 6 table, Adv? = Y row]
- All catalog Seq#: [complete list from the Adv? = Y catalog row]
- Selected divergence Seq#: [the specific Seq# from the catalog list where this scenario diverges]

Selected threat class: [from Adv? = Y row in Step 6]
Adversarial condition: [specific input or state -- not a generic category, a specific instance]
Divergence boundary: [Step 3 Seq# -- exact boundary where path separates from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [one sentence -- why this class at this boundary is the highest-risk gap
based on Step 4 and Step 8 findings]

---

## STEP 8 -- PASS 2: AUTHORIZATION AUDIT

Walk the full boundary list from Step 3 a second time. Exclusive focus: authorization correctness.

DISQUALIFIER (C-11): Fails if PASS 2 mirrors Step 4's Auth / Permission columns without raising
new questions. A PASS 2 is not a re-statement of inline auth fields.

For each boundary, assess:
1. **Delegation**: Is auth explicit here or assumed from an upstream check? If assumed: can a
   caller reach this boundary without the upstream check executing?
2. **Escalation**: Could adjacent permissions (broader scope, different role, borrowed identity)
   reach a higher-privilege resource through this boundary?
3. **Minimum enforcement**: Is minimum-required scope enforced? Would an over-permissioned
   token also be accepted?

Required: At least one gap or escalation path not raised in Step 4's auth columns.
Or: "PASS 2: no additional gaps --" with specific justification for the three highest-risk
boundaries confirming each is clean.

---

## STEP 9 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

DISQUALIFIER (C-06): Fails if states "error returned to caller" without propagation chain /
skips from origin to final response without showing intermediate boundaries.

Origin: [boundary name and Step 3 Seq#]
Failure: [mechanism from Step 4]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## STEP 10 -- BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Step 3 boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?
- Cross-catalog interaction: does this limit interact with the concurrent mutation or
  malformed input classes from Step 6?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## Predicted Scores

| Criterion | Pts | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|-----|------|------|------|------|------|
| C-01 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-02 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-03 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-04 | 15 | 15 | 15 | 15 | 15 | 15 |
| C-05 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-06 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-07 | 10 | 10 | 10 | 10 | 10 | 10 |
| C-08 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-09 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-10 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-11 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 2 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-17 | 5 | 5 | 0 | 0 | 5 | 5 |
| C-18 | 5 | 2 | 5 | 2 | 5 | 5 |
| C-19 | 5 | 0 | 0 | 5 | 0 | 5 |
| **Total** | **150** | **142** | **140** | **142** | **145** | **150** |
| All essential pass | -- | YES | YES | YES | YES | YES |
| Golden (>=80) | -- | YES | YES | YES | YES | YES |

**Score rationale by variation:**

- **V-01 (142)**: C-17 PASS (register present, inline column removed). C-18 PARTIAL (advisory
  exhaustiveness paragraph -- demonstrates check conceptually but no per-row named confirmation).
  C-19 FAIL (no Adv? column). Tests: does structural register alone reach 142?

- **V-02 (140)**: C-17 FAIL (inline Remediation column retained). C-18 PASS (per-row named
  gate, FAILS conditions named). C-19 FAIL (no Adv? column). Tests: does per-row gate alone
  reach 140 without register?

- **V-03 (142)**: C-17 FAIL (inline Remediation). C-18 PARTIAL (advisory paragraph).
  C-19 PASS (Adv? column with Y/N construction rule, cross-reference in Step 7). C-15 PARTIAL
  because exhaustiveness paragraph is advisory. Tests: does pre-marking alone reach 142?

- **V-04 (145)**: C-17 PASS + C-18 PASS + C-19 FAIL. Tests: does register + gate reach 145
  without candidate column?

- **V-05 (150)**: All three PASS. Maximum enforcement variation.
