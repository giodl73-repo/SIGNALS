Here are the 5 R4 variations for `trace-request`:

---

## Summary

| V | Axis | Core C-14/C-15/C-16 mechanism | Predicted |
|---|------|-------------------------------|-----------|
| **V-01** | Role sequence | C-14: format examples per mechanism type (role vocabulary); C-15: exhaustiveness check paragraph; C-16: mandatory cross-reference block | 135/135 |
| **V-02** | Output format | C-14: separate Remediation Register with Parameters sub-column; C-15: All Applicable Seq# column + C-16 Candidate column; C-16: cross-reference block | 135/135 |
| **V-03** | Phrasing register (DISQUALIFIER) | C-14: DISQUALIFIER with concrete failing/passing examples; C-15: DISQUALIFIER banning single-boundary rows; C-16: DISQUALIFIER banning vague references | 120/135 |
| **V-04** | Role sequence + Output format | V-01 role-after-inventory + V-02 Remediation Register + exhaustiveness lifecycle gate | 135/135 |
| **V-05** | Full synthesis | All three axes + exhaustiveness gate + mandatory cross-reference block + full DISQUALIFIER register | 135/135 |

---

**What's new vs R3:**

**C-14** — R3's DISQUALIFIER bans "add error handling" and names "algorithm+values" but doesn't show what a passing value looks like. R4 adds concrete per-mechanism format examples (`algorithm=exponential, initial=100ms, multiplier=2x, max-attempts=5`). V-02/V-04/V-05 add a structural Remediation Register where `Parameters` is a distinct column — a blank cell is structurally visible as incomplete.

**C-15** — R3 V-01 has the "All Applicable Seq#" column rule but no verification step. R4 adds an exhaustiveness check paragraph (V-01/V-02/V-03) and promotes it to a lifecycle gate in V-04/V-05: Step 7 is blocked until the check is confirmed complete.

**C-16** — R3 V-05 had "Step 6 row cited: [# and class name]" informally. R4 makes it a formal cross-reference block with four required fields (catalog row #, exact threat class, complete Seq# list, selected divergence Seq#) that must appear before the adversarial trace begins. V-02/V-04 add a `C-16 Candidate` column to the catalog to pre-mark the selection source.

**Why V-03 doesn't reach 135**: C-15 and C-16 require structural scaffolding that text constraints alone can't enforce — a model can write plausible-looking catalog rows that technically avoid the DISQUALIFIER text while missing a boundary, or reference the catalog loosely without a mandatory format block. C-14 PASSES because it's a binary text test (banned string without numeric values is detectable). C-11/C-12/C-13 remain PARTIAL, inherited from R3 V-03.
 complete.

**C-16** — R3 V-05 Step 7 already includes "Step 6 row cited: [# and class name]" which
established a precedent. C-16 makes this a formal requirement with a structured cross-reference
block that names catalog row #, threat class, complete Seq# list from that row, and the
selected divergence Seq# — before the adversarial trace begins. All R4 variations add this
cross-reference block to Step 7 (or the equivalent adversarial section).

---

## V-01: Role Sequence — Role Selected After Boundary Inventory

**Axis**: Role sequence — role selection deferred to after Step 3 boundary inventory. The
platform expert role is chosen with full knowledge of the specific boundaries in scope.

**Hypothesis**: Selecting the role with a concrete boundary list in view gives the model a
platform-specific referent for remediation parameter vocabulary. A Dataverse expert filling
Step 4 remediation cells knows OData batch-limit retry semantics, plugin execution circuit
breaker thresholds, and Dataverse-specific scope strings. A Commerce expert names payment
gateway idempotency retry windows and cart-lock TTLs. A Power Automate expert names connector
throttle reset intervals and flow-level retry counts. This contextualization improves C-14
compliance — quantified parameters drawn from the selected role's platform are more specific
than generic algorithm+values. C-15 and C-16 are enforced via an exhaustiveness check
paragraph (C-15) and a mandatory cross-reference block (C-16), both structurally new vs R3 V-01.

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

This role determines the platform-specific parameter vocabulary for Step 4 Remediation cells.

---

## STEP 4 -- BOUNDARY TRAVERSAL

One row per boundary from Step 3. All columns required.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 draw (ms) | p99 draw (ms) | Draw type | Remediation |
|---|----------|-----------------|-------|---------------------------|---------------|---------------|-----------|-------------|
| 1 |          |                 |       |                           |               |               |           |             |
| 2 |          |                 |       |                           |               |               |           |             |

**Column rules:**

- **Failure Mode(s)**: Name the specific mechanism: HTTP status code, timeout threshold +
  behavior, throttle rate + breach behavior, auth rejection type (token expired / scope missing /
  role not assigned), payload validation rule, network failure class.
  FAILS: "may fail," "could error," "an exception might be thrown."

- **Auth?**: Y or N.

- **Permission / Scope / Role**: Y rows: name the exact artifact (e.g., "prvReadAccount privilege,"
  "`orders.write` OAuth scope"). N rows: write "AUTH GAP -- [reason]."
  FAILS: "standard auth," "valid token," "handled upstream" without naming the upstream boundary.

- **p50 draw / p99 draw**: Millisecond estimate or range. FAILS: "fast," "low," blank.

- **Draw type**: Sequential (adds to chain) or Parallel with [boundary #] (shares slot, not additive).

- **Remediation**: Quantified mechanism required. Use your selected role's platform vocabulary.
  Format by mechanism type:
  - Retry: algorithm (linear/exponential/jitter) + initial delay (ms) + multiplier + max-attempts
    [+ jitter range if applicable]
    Example: "exponential backoff: initial=100ms, multiplier=2x, jitter=+/-20%, max-attempts=5"
  - Circuit breaker: failure threshold + time window + reset interval
    Example: "circuit breaker: threshold=5 errors/10s, reset=60s"
  - Scope fix: exact scope string or role identity
    Example: "add prvWriteAccount to service principal sp-orders-api"
  - Validation guard: field name + data type constraint + validation predicate
    Example: "validate customerId: UUID format, reject null at boundary #1"
  FAILS: "add error handling," "improve resilience," "add retry logic" (no parameters),
  "exponential backoff" (no values), any mechanism named without its operational parameters.

---

## STEP 5 -- BUDGET RECONCILIATION (SUM CLOSURE GATE)

Review the p50 draw, p99 draw, and draw type columns from Step 4.

**Part A: Sequential chain**

List every row where Draw type = Sequential, in traversal order:
[boundary #] -> [boundary #] -> ...

Sum their p50 draws: ___ms
Sum their p99 draws: ___ms

**Part B: Parallel branch exclusions**

List every row where Draw type = Parallel. For each:
- Which boundary does it share a slot with?
- Confirm it is genuinely concurrent (not a dependency)
- Confirm it is excluded from the Part A sequential sum

**Part C: Critical path totals**

Critical-path p50 = [= Part A p50 sum] ms
Critical-path p99 = [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: The sequential p50 sum in Part A and the critical-path p50 in Part C must be
the same number. The sequential p99 sum and the critical-path p99 must be the same number.
If they differ, return to Step 4 and correct the per-boundary estimates before continuing.
The per-boundary budget rows are the source of truth; Part C is derived from them.

Budget headroom:
- p50 headroom: [Step 2 budget] - [critical-path p50] = ___ms
- p99 headroom: [Step 2 budget] - [critical-path p99] = ___ms (negative = overrun)

---

## STEP 6 -- THREAT CLASS CATALOG

Build this catalog from Step 3's boundary inventory. Reference boundary Seq numbers from Step 3.
Build this catalog before Step 7's adversarial selection -- the adversarial scenario must be
selected from this catalog, not chosen independently.

| # | Threat Class | All Applicable Boundary Seq Numbers | Severity | Example Trigger |
|---|---|---|---|---|
| 1 | Malformed input | | | |
| 2 | Credential expiry | | | |
| 3 | Concurrent mutation | | | |
| 4 | Missing permission scope | | | |
| 5 | Network partition | | | |

Rules:
- Minimum 4 rows (add more if applicable to this request type).
- "All Applicable Boundary Seq Numbers": list every Step 3 Seq# where this threat class can
  manifest -- not just the highest-risk one. A threat class that applies to three boundaries
  must list all three.
- Severity: Low / Medium / High.
- After completing the table: mark the highest-severity row. If two rows tie on severity,
  prefer the one with the most applicable boundaries.

**Exhaustiveness check (C-15)**: After completing the table, for each row, re-examine your
Step 3 boundary inventory. For each threat class: "Can this threat manifest at any boundary
NOT already listed in this row's Seq# column?" If yes, add the missing Seq# before proceeding.
A catalog row that lists one Seq# for a threat known to apply at multiple boundaries fails C-15.

---

## STEP 7 -- ADVERSARIAL SCENARIO

**Catalog cross-reference** (required before tracing -- C-16):
- Catalog row #: [N from Step 6]
- Threat class: [exact name from Step 6 table]
- All catalog Seq#: [complete Seq# list from that Step 6 row]
- Selected divergence Seq#: [the specific Seq# from the catalog list where this scenario diverges]

An adversarial scenario that does not cite a catalog row number, the exact threat class name,
and a divergence Seq# drawn from that catalog row's Applicable Seq# list fails C-16.

Select the highest-severity threat class from Step 6. Show:

Selected threat class: [class from Step 6]
Highest-risk boundary: [Step 3 Seq# -- name]
Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Step 3 Seq# -- exact boundary where path splits from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [why this class at this boundary is the highest-risk gap based on
Step 4 and Step 5 findings]

---

## STEP 8 -- PASS 2: AUTHORIZATION AUDIT

Walk the full boundary list from Step 3 a second time. Exclusive focus: authorization correctness.

DISQUALIFIER: Fails if this section mirrors Step 4's Auth / Permission columns without raising
new questions. A PASS 2 is not a re-statement of inline auth fields.

For each boundary, assess:
1. Delegation: Is auth explicit here or assumed from an upstream check? If assumed: can a caller
   reach this boundary without the upstream check executing?
2. Escalation: Could adjacent permissions (broader scope, different role, borrowed identity)
   reach a higher-privilege resource through this boundary?
3. Minimum enforcement: Is minimum-required scope enforced? Would an over-permissioned token pass?

Required output: At least one gap or escalation path not raised in Step 4's auth columns.
Or: "PASS 2: no additional gaps --" with specific justification for the three highest-risk
boundaries confirming each is clean.

---

## STEP 9 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

DISQUALIFIER: Fails if it skips from origin to final response without showing intermediate
boundaries, or states "error returned to caller" without the propagation chain.

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

## V-02: Output Format -- Remediation Register with Parameters Sub-Schema

**Axis**: Output format -- the traversal table hands off remediation to a dedicated Remediation
Register section whose schema enforces C-14 structurally: `Mechanism Type` and `Parameters` are
separate columns, making a blank or vague Parameters cell immediately visible as incomplete.
The threat catalog gains a `C-16 Candidate` column marking the adversarial selection source.

**Hypothesis**: When `Parameters` is a distinct table column rather than part of a prose
Remediation cell, the model cannot embed "retry logic" inside a longer narrative sentence that
passes visual inspection. The column is either populated with quantified values (algorithm name,
ms values, thresholds, scope strings) or it is visibly blank. This structural gap is harder to
obscure than a narratively complete sentence that names the mechanism type without values. C-15
is enforced by the `All Applicable Seq#` column inherited from R3 V-02 (pre-filled template,
column header signals multi-value intent). C-16 is enforced by the `C-16 Candidate` column
(exactly one row marked Y -- that row is the mandatory adversarial selection source).
Risk: structural completeness may be achieved with thin values that satisfy the column schema
without real operational specificity (e.g., Parameters = "initial=Xms" with a placeholder).

```
You are running /trace-request for: {{topic}}

Select your platform expert role:
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

State your role before the Entry Point section.

---

## ENTRY POINT

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type (bearer token / API key / managed
identity / session cookie / none).

DISQUALIFIER: "a POST request" (no path) / "a JSON body" (no field names) /
"an authenticated user" (no credential type) fails C-01.

---

## LATENCY BUDGET

Declare end-to-end budget before the boundary inventory.
Source: 1) Documented SLA (cite it) 2) Caller timeout (state value) 3) UX threshold
(500ms interactive / 2000ms sync background / 10000ms async)

**Budget: [N]ms** (source: ...)

---

## BOUNDARY INVENTORY

List every boundary before filling the traversal table. A boundary is crossed when a network
call is made, identity context is evaluated, or data is read from or written to a store.
Token validation, gateway routing, cache lookup, and audit emission are boundaries.

| Seq | Boundary Name | Protocol | From -> To |
|-----|---------------|----------|------------|
| 1   |               |          |            |
| 2   |               |          |            |
| ... |               |          |            |

GATE: The traversal table must have exactly one row per Seq entry above, in the same order.

---

## TRAVERSAL TABLE

One row per Seq from the Boundary Inventory. All columns required.
Remediation items are numbered (R-1, R-2, ...) and detailed in the Remediation Register below.

| Seq | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Draw type | Rem# |
|-----|----------|-----------------|-------|---------------------------|----------|----------|-----------|------|
| 1   |          |                 |       |                           |          |          |           |      |
| 2   |          |                 |       |                           |          |          |           |      |

Column rules:
- **Failure Mode(s)**: Named mechanism required (HTTP status, timeout threshold, throttle limit,
  auth rejection type, payload validation rule, network failure class).
  FAILS: "may fail," "could error," "an exception might be thrown."
- **Auth?**: Y or N.
- **Permission / Scope / Role**: Y rows: exact artifact. N rows: "AUTH GAP -- [reason]."
  FAILS: "standard auth," "valid token," "handled upstream" without naming the upstream boundary.
- **p50 / p99**: Millisecond estimate. FAILS: "fast," "low," blank.
- **Draw type**: Sequential (adds to chain) or Parallel with [Seq#] (shares slot, not additive).
- **Rem#**: Reference to a Remediation Register entry (e.g., R-1). Every row requires at least
  one Rem#. A blank Rem# is a missing remediation item.

---

## REMEDIATION REGISTER

One row per remediation item. Referenced by Rem# from the Traversal Table above.

| Rem# | Boundary Seq# | Failure Mode Addressed | Mechanism Type | Parameters |
|------|---------------|------------------------|----------------|------------|
| R-1  |               |                        |                |            |
| R-2  |               |                        |                |            |

Column rules:
- **Mechanism Type**: retry / circuit breaker / scope addition / validation guard
  (or other named type)
- **Parameters** (required -- no blanks, no placeholder values):
  - retry: algorithm (linear/exponential/jitter), initial delay (ms), multiplier (if exponential),
    max-attempts, jitter range (if applicable)
    Example: algorithm=exponential, initial=100ms, multiplier=2x, max-attempts=5, jitter=+/-20%
  - circuit breaker: failure threshold, time window, reset interval
    Example: threshold=5errors/10s, reset=60s
  - scope addition: exact scope string or role identity
    Example: scope=Dataverse.ReadWrite, principal=sp-orders-api
  - validation guard: field name, data type constraint, validation predicate
    Example: field=customerId, type=UUID, predicate=reject-null-or-non-UUID at Seq#1
  FAILS: Parameters cell blank / mechanism type named without numeric or identity-specific values /
  "reasonable timeout" / "retry with backoff" / any placeholder without derived values.

---

## BUDGET RECONCILIATION (SUM CLOSURE GATE)

**Part A: Sequential chain**
List every Sequential row in traversal order: [Seq#] -> [Seq#] -> ...
Sum p50 draws: ___ms | Sum p99 draws: ___ms

**Part B: Parallel branch exclusions**
For each Parallel row: which Seq# does it share a slot with? Confirm genuinely concurrent.
Confirm excluded from Part A sum.

**Part C: Critical path totals**
Critical-path p50 = [= Part A p50 sum] ms
Critical-path p99 = [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Part A sums must equal Part C totals exactly. If they differ, return to the
Traversal Table and correct per-boundary estimates. Per-boundary rows are the source of truth.

Budget headroom:
- p50 headroom: [budget] - [critical-path p50] = ___ms
- p99 headroom: [budget] - [critical-path p99] = ___ms

---

## THREAT CLASS CATALOG

Build from the Boundary Inventory Seq entries. Complete this catalog before the Adversarial
Scenario section.

| # | Threat Class | All Applicable Seq# | Severity | Example Trigger | C-16 Candidate |
|---|---|---|---|---|---|
| 1 | Malformed input | | | | |
| 2 | Credential expiry | | | | |
| 3 | Concurrent mutation | | | | |
| 4 | Missing permission scope | | | | |
| 5 | Network partition | | | | |

Column rules:
- **All Applicable Seq#**: list every Seq# where this threat class can manifest. Not just the
  highest-risk boundary. A threat class applying at boundaries 2, 5, and 7 must list: 2, 5, 7.
- **Severity**: Low / Medium / High.
- **C-16 Candidate**: Mark Y on exactly one row -- the highest-severity entry. This is the
  row the Adversarial Scenario must draw from. Ties on severity: prefer the row with the most
  applicable Seq# entries.

---

## PASS 2: AUTHORIZATION AUDIT

Walk the full Boundary Inventory a second time. Exclusive focus: authorization correctness.

DISQUALIFIER: Fails if this section mirrors the Traversal Table's Auth / Permission columns
without raising new questions. A PASS 2 is not a re-statement of inline auth fields.

For each boundary, assess:
1. Delegation: Is auth explicit here or assumed from upstream? Can a caller reach this boundary
   without the upstream check executing?
2. Escalation: Could adjacent permissions reach a higher-privilege resource through this boundary?
3. Minimum enforcement: Is minimum-required scope enforced? Would a broader token also be accepted?

Required: At least one new gap not surfaced in the primary traversal.
Or: "PASS 2: no additional gaps --" with specific justification for the three highest-risk
boundaries confirming each is clean.

---

## ADVERSARIAL SCENARIO

**Cross-reference block** (required before the scenario trace -- C-16):
- Catalog row #: [N -- the row marked C-16 Candidate = Y]
- Threat class: [exact name from catalog]
- All applicable Seq#: [complete list from that catalog row]
- Selected divergence Seq#: [specific Seq# from the list above where this scenario diverges]

An adversarial scenario that omits this cross-reference block, uses a threat class not in the
catalog, or cites a Seq# not in the catalog row's All Applicable Seq# list fails C-16.

Selected threat class: [from C-16 Candidate row]
Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Seq# -- exact boundary where path splits from nominal]
Path after divergence: [each boundary from divergence to final response]
Outcome: [what the adversary achieves or receives -- concrete impact]
Selection rationale: [why this class at this boundary is the highest-risk gap]

---

## ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from the Traversal Table.

DISQUALIFIER: Fails if it skips intermediate boundaries or states "error returned to caller"
without the propagation chain.

Origin: [boundary name and Seq#]
Failure: [mechanism from Traversal Table]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Seq# boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?
- Cross-catalog interaction: does this limit interact with any Threat Class Catalog entry?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## V-03: Phrasing Register (DISQUALIFIER) -- Three New Blocks for C-14, C-15, C-16

**Axis**: Phrasing register (DISQUALIFIER) -- three new DISQUALIFIER blocks appended to R3
V-03's existing register, each targeting one of the new criteria with concrete failing and
passing examples. No structural scaffolding changes beyond what R3 V-03 already established.

**Hypothesis**: Naming the exact failure patterns for C-14 ("exponential backoff" without
values), C-15 (a catalog row citing only the highest-risk boundary), and C-16 (adversarial
scenario without catalog cross-reference) activates constraint-satisfaction reasoning. The model
is given both the prohibited pattern AND a concrete passing counterexample -- a different
cognitive operation than being told what to produce. C-14 is the strongest case for DISQUALIFIER
enforcement because the failing pattern is a binary text test: "exponential backoff" without
numeric parameters is detectable and banned. C-15 and C-16 are weaker cases because the
DISQUALIFIER bans a specific form without providing a template that makes correct multi-boundary
enumeration structurally visible. Expected: C-14 PASS, C-15 and C-16 PARTIAL.

```
You are running /trace-request for: {{topic}}

Select your platform expert role:
- Dataverse platform expert (entity model, OData pipeline, security roles, plugin execution, audit)
- Commerce platform expert (pricing, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls, flow runtime)

State your role: "I am the [role] for this trace."

---

## ENTRY POINT

DISQUALIFIER (C-01): Any entry point matching these patterns fails:
- "a POST request" (no path)
- "a JSON body" (no field names)
- "an authenticated user" (no credential type)

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type.

---

## LATENCY BUDGET

Before listing any boundary: declare the end-to-end latency budget.
Source: SLA (cite it) / caller timeout (state value) / UX threshold (500ms interactive /
2000ms background / 10000ms async).

**Budget: [N]ms** (source: [SLA / timeout / UX])

---

## BOUNDARY TRAVERSAL

DISQUALIFIER (C-03): Any failure mode field containing these patterns fails:
"may fail" / "could error" / "might throw" / "an exception could occur" /
"returns an error" without naming the error or cause.
Required: HTTP status code, timeout threshold + behavior, throttle rate + breach behavior,
auth rejection type (token expired / scope missing / role not assigned), payload validation
rule, or network failure class.

DISQUALIFIER (C-04): Any auth field containing these patterns fails:
"standard auth" / "valid token" / "authenticated user" / "authorization handled upstream"
without naming the upstream boundary.
Required for Y rows: exact permission artifact. N rows: "AUTH GAP -- [reason]."

DISQUALIFIER (C-12 -- latency column): Any latency section matching these patterns fails:
- Prose-only annotation without a structured p50/p99 per boundary
- "fast" or "low latency" without a ms value
- A blank latency cell for any boundary

DISQUALIFIER (C-12 -- arithmetic): Any critical path computation matching these patterns fails:
- Sequential p50 values in the traversal do not sum to the critical-path p50 stated later
- Sequential p99 values do not sum to the critical-path p99 stated later
- A parallel boundary's draw is included in the sequential sum (double-counting)
Required: verify that per-boundary sequential draws sum to the critical-path total.

DISQUALIFIER (C-08/C-14 -- remediation): Any remediation item matching these patterns fails:
- "add error handling" / "improve resilience" / "add retry logic" (no algorithm or values)
- "exponential backoff" without specifying: algorithm name, initial delay (ms), multiplier,
  max-attempts [and jitter range if applicable]
- "circuit breaker" without specifying: failure threshold, time window, reset interval
- "add [scope]" without naming the exact scope string or role identity
- "validate [field]" without naming the field, type constraint, and validation predicate
PASSES (examples):
- "exponential backoff: initial=100ms, multiplier=2x, jitter=+/-20%, max-attempts=5"
- "circuit breaker: threshold=5 errors/10s, reset=60s"
- "add prvWriteAccount to service principal sp-orders-api"
- "validate customerId: UUID format, reject null at boundary #1"

For each boundary in traversal order:

**Boundary: [name] [Seq#]**
Input: [what crosses this boundary]
Failure mode(s): [disqualifier rules above apply]
Auth check: [disqualifier rules above apply]
p50 (ms): [disqualifier rules above apply]
p99 (ms): [disqualifier rules above apply]
Draw type: Sequential (adds to chain) / Parallel with [Seq#] (slot shared, not additive)
Remediation: [disqualifier rules above apply]

---

## CRITICAL PATH

DISQUALIFIER (C-10): Any critical path section matching these patterns fails:
- Lists latency contributors without naming the sequential chain
- States a p99 total without showing which Seq# rows sum to produce it
- Omits whether parallel paths are excluded from the sum

Required: sequential chain (Seq# -> Seq# -> ...), excluded parallel branches, cumulative p50,
cumulative p99, dominant boundary.

Sequential sum verification: p50 draws [Seq#] + [Seq#] + ... = ___ms / p99 draws = ___ms.
Critical-path p50 = ___ms (must equal sequential p50 sum).
Critical-path p99 = ___ms (must equal sequential p99 sum).

Budget headroom:
- p50 headroom: [budget] - [critical-path p50] = ___ms
- p99 headroom: [budget] - [critical-path p99] = ___ms

---

## THREAT CLASS CATALOG

DISQUALIFIER (C-13): Any threat catalog matching these patterns fails:
- Lists threat classes without referencing specific boundary Seq numbers
- Provides only one "highest-risk boundary" per threat class rather than all applicable boundaries
- Derives the catalog from the adversarial scenario rather than building it before selection
- Fewer than 4 threat classes

DISQUALIFIER (C-15): Any catalog row matching these patterns fails:
- Lists a single Seq# for a threat class known to manifest at multiple boundaries in this request
- Uses "multiple boundaries," "various," or "all" instead of enumerating individual Seq numbers
- Lists "highest-risk boundary only" explicitly or implicitly
PASSES: "Boundaries: 1, 4, 7" (enumerates every applicable Seq# from the boundary inventory)
FAILS: "Boundary: 4" (when the threat also applies at Seq# 1 and 7)

Required: a structured table mapping at least 4 threat classes to ALL applicable boundary
Seq numbers (not just the highest-risk one), built before adversarial scenario selection.

| Threat Class | All Applicable Boundaries (Seq#) | Severity | Example Trigger |
|---|---|---|---|
| Malformed input | | | |
| Credential expiry | | | |
| Concurrent mutation | | | |
| Missing permission scope | | | |
| Network partition | | | |

Add rows for additional applicable threat classes. Build this table before the Adversarial
Scenario section.

---

## AUTHORIZATION RE-WALK

DISQUALIFIER (C-11): Any re-walk matching these patterns fails:
- Re-states auth fields from the boundary traversal without raising new questions
- "No additional auth gaps found" without per-boundary justification for high-risk boundaries
- Covers only AUTH GAP rows, ignoring rows where auth was marked present

Required: walk every boundary a second time, focused on privilege escalation, scope gaps,
and assumed-but-unverified auth. Must name at least one gap not surfaced in the primary
traversal -- or "Re-walk found no additional gaps --" with specific justification for the
three highest-risk boundaries.

---

## ADVERSARIAL SCENARIO

DISQUALIFIER (C-16): Any adversarial scenario matching these patterns fails:
- Introduces a threat condition not drawn from the Threat Class Catalog above
- Does not name the catalog threat class by its exact catalog label
- Does not cite the specific boundary Seq# from that catalog row's All Applicable Boundaries
  column where divergence occurs
- Provides a vague reference: "based on credential threats" or "similar to catalog row 2"
  without naming the exact threat class, row number, and divergence Seq#
PASSES: Scenario that states "Catalog row [#], threat class: [exact name], divergence at
Seq# [N] (listed in that catalog row's All Applicable Boundaries)" before the trace begins.

Select the highest-severity threat class from the catalog (prefer the class with the most
applicable boundaries if severity ties). Show:

Catalog cross-reference: row [#], threat class: [exact name], all applicable Seq#: [list],
selected divergence Seq#: [N]

Adversarial condition: [specific input or state -- not a generic category]
Path after divergence: [each boundary from divergence to final response]
Outcome: [concrete impact]

---

## ERROR PATH

DISQUALIFIER (C-06): Fails if: states "error returned to caller" without propagation chain /
skips from origin to final response without showing intermediate boundaries.

Trace one complete error path. Select the highest-probability failure from the traversal.
Show every boundary between origin and caller.

---

## BATCH AND EDGE CASES

Platform limit, enforcement boundary (Seq#), N-1/N/N+1 behavior, per-item overhead.
Cross-catalog interaction: does this limit interact with any threat class in the catalog?
"Batch not applicable -- [specific reason]" if not applicable.
```

---

## V-04: Role Sequence + Output Format -- Contextualized Remediation Register

**Axes**: Role sequence (V-01) + Output format / remediation register (V-02). Role is selected
after Step 3 boundary inventory to contextualize the Remediation Register's platform-specific
parameter vocabulary. The Remediation Register with sub-schema columns enforces C-14 structurally.

**Hypothesis**: The role-after-inventory sequencing (V-01) ensures platform expert identity is
established with full knowledge of the boundary landscape before any remediation items are
written. Combined with V-02's structural Remediation Register, the Parameters column is filled
by a named platform expert with a concrete boundary list in view -- reducing the likelihood of
generic or placeholder values. This is a tighter causal chain for C-14 than either mechanism
alone: the role names the expert vocabulary; the Register column names the parameter slot; the
boundary inventory names the specific failure mode being addressed. C-15 is enforced by the
All Applicable Seq# column + an exhaustiveness gate (Step 7 blocked until confirmed complete).
C-16 is enforced by the C-16 Candidate column in the catalog + cross-reference block in Step 7.

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

Budget accounting: sequential boundaries sum on the critical path. Parallel branches share a
slot. Cached steps draw < 5ms on hit; draw synchronous cost on miss.

---

## STEP 3 -- BOUNDARY INVENTORY (GATE)

List every boundary in traversal order before filling Step 4. A boundary is any transition
where a network call is made, identity context is evaluated, or data is read from or written
to a store. Token validation, gateway routing, cache lookup, and audit emission are boundaries.

| Seq | Boundary Name | Protocol | From -> To |
|-----|---------------|----------|------------|
| 1   |               |          |            |
| 2   |               |          |            |
| ... |               |          |            |

GATE: Every row in Step 4 must correspond to a boundary listed here, in the same order.
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

This role determines the parameter vocabulary for the Remediation Register below.

---

## STEP 4 -- TRAVERSAL TABLE

One row per Seq from Step 3. All columns required.
Remediation items are referenced by Rem# and detailed in the Remediation Register.

| Seq | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Draw type | Rem# |
|-----|----------|-----------------|-------|---------------------------|----------|----------|-----------|------|
| 1   |          |                 |       |                           |          |          |           |      |
| 2   |          |                 |       |                           |          |          |           |      |

Column rules:
- **Failure Mode(s)**: Named mechanism required. FAILS: "may fail," "could error," "might throw."
- **Auth?**: Y or N.
- **Permission / Scope / Role**: Y rows: exact artifact. N rows: "AUTH GAP -- [reason]."
  FAILS: "standard auth," "valid token," "handled upstream" without naming the upstream boundary.
- **p50 / p99**: Millisecond estimate. FAILS: "fast," "low," blank.
- **Draw type**: Sequential or Parallel with [Seq#].
- **Rem#**: Reference to Remediation Register entry. Blank = missing remediation.

---

## REMEDIATION REGISTER

One row per remediation item. Use the selected platform expert role's vocabulary for Parameters.

| Rem# | Boundary Seq# | Failure Mode Addressed | Mechanism Type | Parameters |
|------|---------------|------------------------|----------------|------------|
| R-1  |               |                        |                |            |
| R-2  |               |                        |                |            |

Column rules:
- **Mechanism Type**: retry / circuit breaker / scope addition / validation guard
- **Parameters** (no blanks, no placeholder values -- use role-specific platform vocabulary):
  - retry: algorithm, initial delay (ms), multiplier, max-attempts [, jitter range]
    Example (Dataverse): algorithm=exponential, initial=500ms, multiplier=2x, max-attempts=3
    Example (Power Automate): algorithm=fixed, interval=2min, max-attempts=4 (connector limit)
  - circuit breaker: failure threshold, time window, reset interval
    Example (Commerce): threshold=3 errors/5s, reset=30s (payment gateway timeout pattern)
  - scope addition: exact scope string or role identity
    Example: scope=Dataverse.ReadWrite, principal=sp-orders-api
  - validation guard: field name, data type constraint, validation predicate at boundary Seq#
    Example: field=orderId, type=GUID, predicate=reject-null-or-non-GUID at Seq#1
  FAILS: Parameters cell blank / mechanism type named without numeric or identity values /
  "reasonable timeout" / "retry with backoff" / any placeholder without derived values.

---

## STEP 5 -- BUDGET RECONCILIATION (SUM CLOSURE GATE)

**Part A: Sequential chain**
Identify every Sequential row in order: [Seq#] -> [Seq#] -> ...
Sum p50 draws: ___ms | Sum p99 draws: ___ms

**Part B: Parallel branch exclusions**
For each Parallel row: partner Seq#, confirmed concurrent, confirmed excluded from Part A sum.

**Part C: Critical path totals**
Critical-path p50 = [= Part A p50 sum] ms
Critical-path p99 = [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Part A sums must equal Part C totals exactly. If they differ, return to Step 4
and correct the per-boundary estimates. The per-boundary rows are the source of truth.

Budget headroom:
- p50 headroom: [Step 2 budget] - [critical-path p50] = ___ms
- p99 headroom: [Step 2 budget] - [critical-path p99] = ___ms

---

## STEP 6 -- THREAT CLASS CATALOG

Build from Step 3's boundary Seq entries. Complete before Step 7.

| # | Threat Class | All Applicable Seq# | Severity | Example Trigger | C-16 Candidate |
|---|---|---|---|---|---|
| 1 | Malformed input | | | | |
| 2 | Credential expiry | | | | |
| 3 | Concurrent mutation | | | | |
| 4 | Missing permission scope | | | | |
| 5 | Network partition | | | | |

Column rules:
- **All Applicable Seq#**: list every Seq# where this threat can manifest -- not just the
  highest-risk one. A threat applying at boundaries 2, 5, and 7 must list: 2, 5, 7.
- **Severity**: Low / Medium / High.
- **C-16 Candidate**: Mark Y on exactly one row -- the highest-severity row. Ties: prefer the
  row with the most Applicable Seq# entries.

**Exhaustiveness gate (C-15)**: After completing the table, for each row, re-examine your
Step 3 boundary inventory. "Can this threat class manifest at any boundary NOT already listed
in this row's All Applicable Seq# column?" If yes, add the missing Seq# before proceeding.

GATE: Step 7 may not begin until this exhaustiveness check is confirmed complete for all rows.
Confirm: "Exhaustiveness check complete -- [N] rows reviewed, [X] Seq# additions made."
Or: "Exhaustiveness check complete -- no additional Seq# found for any row."

---

## STEP 7 -- ADVERSARIAL SCENARIO

**Cross-reference block** (required before the scenario trace -- C-16):
- Catalog row #: [N -- the row marked C-16 Candidate = Y]
- Threat class: [exact name from Step 6 catalog]
- All applicable Seq#: [complete list from that catalog row]
- Selected divergence Seq#: [specific Seq# from the list above where this scenario diverges]

An adversarial scenario that omits this cross-reference block, uses a threat class not in the
catalog, or cites a Seq# not in the catalog row's All Applicable Seq# list fails C-16.

Selected threat class: [from C-16 Candidate row]
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
1. Delegation: Is auth explicit here or assumed from upstream? Can a caller reach this boundary
   without the upstream check executing?
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

Origin: [boundary name and Seq#]
Failure: [mechanism from Step 4]
At [next boundary]: [propagated unchanged / wrapped as {type} / retried {N} times / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## STEP 10 -- BATCH AND EDGE CASES

If the request supports batch operations, pagination, or concurrent access:
- Platform limit: name the constraint and which Seq# boundary enforces it
- N-1 / N / N+1 behavior: what changes at each threshold
- Per-item overhead: does it multiply under batch load? At which boundary?
- Cross-catalog interaction: does this limit interact with any Step 6 threat class?

"Batch not applicable -- [specific reason this request is always single-item or stateless]."
```

---

## V-05: Full Synthesis -- Role Sequence + Remediation Register + DISQUALIFIERS + Exhaustiveness Gate

**Axes**: All three single-axis mechanisms (role sequence, output format, DISQUALIFIER register)
plus a lifecycle exhaustiveness gate that makes the C-15 check a blocking condition and a
mandatory cross-reference block that makes C-16 structurally complete. This is the maximum-
enforcement variation: every criterion has at least one structural mechanism AND a DISQUALIFIER
that names the exact failure pattern it prevents.

**Hypothesis**: C-14 is addressed at three levels simultaneously: role-contextualized vocabulary
(role after inventory narrows the parameter space to one platform's semantics), structural column
(Remediation Register makes blank Parameters cells visible), and DISQUALIFIER text (banning the
exact patterns that pass the mechanism-naming test but fail parameterization). C-15 is addressed
by the exhaustiveness check paragraph AND a lifecycle gate that blocks Step 7 progress -- "Step 7
may not begin until the exhaustiveness check is confirmed complete." C-16 is addressed by the
mandatory cross-reference block AND a DISQUALIFIER that names what a vague reference looks like.
Belt-and-suspenders on all three new criteria, preserving all R3 V-05 mechanisms intact.

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

GATE: Every row in Step 4 must correspond to a boundary listed here, in the same order.
No boundary listed here may be absent from Step 4. No boundary may appear in Step 4 that is
not listed here.

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
Remediation items are numbered (R-1, R-2, ...) and detailed in the Remediation Register below.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 draw (ms) | p99 draw (ms) | Draw type | Rem# |
|---|----------|-----------------|-------|---------------------------|---------------|---------------|-----------|------|
| 1 |          |                 |       |                           |               |               |           |      |
| 2 |          |                 |       |                           |               |               |           |      |

**Column DISQUALIFIERS:**

- **Failure Mode(s)**: FAILS if cell contains: "may fail," "could error," "might throw," "an
  exception could occur," "returns an error" without naming the error or cause.
  Required: HTTP status code, timeout threshold + behavior, throttle rate + breach behavior,
  auth rejection type (token expired / scope missing / role not assigned), payload validation
  rule, or network failure class.

- **Auth?**: Binary Y or N only.

- **Permission / Scope / Role**: FAILS for Y rows if cell contains: "standard auth," "valid
  token," "authenticated user," "authorization handled upstream" without naming the boundary.
  Required for Y rows: exact artifact (e.g., "Dataverse `prvReadAccount` security privilege,"
  "Commerce `orders.write` OAuth scope," "Automate `flows.run` Entra app permission").
  Required for N rows: "AUTH GAP -- [specific reason authorization is absent at this boundary]."

- **p50 draw / p99 draw**: FAILS if cell contains: "fast," "low," "negligible," or is blank.
  Required: ms value or range. Sub-5ms: "< 5ms -- [reason]."

- **Draw type**: Required format: "Sequential" or "Parallel with #[Seq#]".
  Sequential rows are additive on the critical path.
  Parallel rows share a latency slot with their partner; only the longer of the pair draws.

- **Rem#**: Reference to Remediation Register entry (e.g., R-1). Blank = missing remediation.
  Every row requires at least one Rem# entry.

---

## REMEDIATION REGISTER

One row per remediation item. Referenced by Rem# from Step 4.
Use the selected platform expert role's vocabulary for the Parameters column.

| Rem# | Boundary Seq# | Failure Mode Addressed | Mechanism Type | Parameters |
|------|---------------|------------------------|----------------|------------|
| R-1  |               |                        |                |            |
| R-2  |               |                        |                |            |

**Column DISQUALIFIERS (C-14):**

- **Mechanism Type**: retry / circuit breaker / scope addition / validation guard (or name it).
  FAILS: blank or "handle the error."

- **Parameters**: FAILS if cell matches any of these patterns:
  - Blank
  - "retry logic" or "retry with backoff" (no algorithm, no values)
  - "exponential backoff" (no initial delay, no multiplier, no max-attempts)
  - "add retry" (no parameters)
  - "reasonable timeout" (no numeric value)
  - Any mechanism type named without associated numeric or identity-specific operational values
  PASSES (required format by type):
  - retry: algorithm=exponential, initial=100ms, multiplier=2x, max-attempts=5 [, jitter=+/-20%]
  - circuit breaker: threshold=5errors/10s, reset=60s
  - scope addition: scope=Dataverse.ReadWrite, principal=sp-orders-api
  - validation guard: field=customerId, type=UUID, predicate=reject-null-or-non-UUID at Seq#1

---

## STEP 5 -- CRITICAL PATH AND BUDGET RECONCILIATION

Review the p50 draw, p99 draw, and Draw type columns from Step 4.

**DISQUALIFIER (C-12)**: Fails if any of the following:
- The critical-path p50 stated here does not equal the sum of Sequential p50 draw cells in Step 4
- The critical-path p99 stated here does not equal the sum of Sequential p99 draw cells in Step 4
- A row marked "Parallel with #[N]" has its draw included in the sequential sum (double-counting)

**Part A: Sequential chain**

Identify every row where Draw type = Sequential:
[Seq#] -> [Seq#] -> ... (in traversal order)

Sum their p50 draws: ___ms
Sum their p99 draws: ___ms

**Part B: Parallel branch exclusions**

For every row where Draw type = Parallel with #[Seq#]:
- Partner boundary: [Seq# from Step 3]
- Confirm concurrent execution (not a sequential dependency): ___
- Confirm excluded from Part A sum: ___
- Longer of the pair (contributes to slot draw): [Seq# -- p99 value]

**Part C: Critical path statement**

Sequential chain: [Seq# -> Seq# -> ...]
Excluded parallel rows: [list each pair]
Critical-path p50: [= Part A p50 sum] ms
Critical-path p99: [= Part A p99 sum] ms
Dominant boundary: [name -- p99 draw -- % of chain p99]

CLOSURE GATE: Critical-path p50 (Part C) = Part A sequential p50 sum. Critical-path p99
(Part C) = Part A sequential p99 sum. If these do not match, return to Step 4 and correct
the per-boundary estimates before continuing.

Budget headroom:
- p50 headroom: [Step 2 budget] - [critical-path p50] = ___ms
- p99 headroom: [Step 2 budget] - [critical-path p99] = ___ms (negative = overrun)

---

## STEP 6 -- THREAT CLASS CATALOG

Build this catalog from Step 3's boundary inventory before Step 7.

**DISQUALIFIER (C-13)**: Fails if any of the following:
- Any threat class row lists only one "highest-risk boundary" rather than all applicable
  Seq numbers from Step 3 where the class can manifest
- Any Seq number in the "All Applicable Boundaries" column does not correspond to a Step 3 row
- Fewer than 4 threat class rows
- The catalog is derived from or written after the adversarial scenario in Step 7

**DISQUALIFIER (C-15)**: Fails if any catalog row matches these patterns:
- Lists a single Seq# for a threat class that can also manifest at additional Step 3 boundaries
- Uses "multiple," "various," "all boundaries," or "several" instead of enumerating Seq numbers
- The exhaustiveness gate below is skipped or answered without per-row re-examination
PASSES: every row where All Applicable Boundaries lists every Step 3 Seq# where that threat
can manifest -- verified by re-examining the Step 3 inventory after filling.

| # | Threat Class | All Applicable Boundaries (Seq#) | Severity | Example Trigger at Highest-Risk Boundary |
|---|---|---|---|---|
| 1 | Malformed input | | | |
| 2 | Credential expiry | | | |
| 3 | Concurrent mutation | | | |
| 4 | Missing permission scope | | | |
| 5 | Network partition | | | |

Rules:
- "All Applicable Boundaries" column: list every Step 3 Seq# where this threat class can
  manifest. A class applicable at boundaries 1, 3, and 5 lists "1, 3, 5" -- not just "3."
- Minimum 4 rows; add rows for additional threat classes relevant to this request.
- Severity: Low / Medium / High.
- After completing: mark the highest-severity class. Ties: prefer the row with the most
  applicable boundaries.

**Exhaustiveness gate (C-15)**: For each row in the table above, re-examine the Step 3
boundary inventory. Ask: "Can this threat manifest at any boundary NOT already listed in
this row's All Applicable Boundaries column?" If yes, add the missing Seq# before proceeding.

GATE: Step 7 may not begin until the exhaustiveness check is confirmed complete for every
row. Confirm: "Exhaustiveness check complete -- [N] rows reviewed, [X] Seq# additions made"
or "Exhaustiveness check complete -- no additional Seq# found for any row."

---

## STEP 7 -- ADVERSARIAL SCENARIO

**DISQUALIFIER (C-16)**: Fails if any of the following:
- The adversarial scenario introduces a threat condition not drawn from the Step 6 catalog
- The scenario does not name the catalog threat class by its exact Step 6 label
- The scenario does not cite the specific boundary Seq# from that catalog row's All Applicable
  Boundaries column where divergence occurs
- Reference is vague: "based on credential threats," "similar to row 2," "a token expiry scenario"
  without naming catalog row #, exact threat class, and divergence Seq# from the catalog row
PASSES: cross-reference block present with catalog row #, exact threat class name, complete
Seq# list from catalog row, and selected divergence Seq# before the scenario trace begins.

**Catalog cross-reference** (required before tracing):
- Catalog row #: [N from Step 6]
- Threat class: [exact name from Step 6 table]
- All catalog Seq#: [complete list from that Step 6 row]
- Selected divergence Seq#: [the specific Seq# from the catalog list where this scenario diverges]

Selected threat class: [highest-severity class from Step 6, most PASS 2 overlap]
Step 6 row cited: [# and class name]
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

Required output: At least one gap or escalation path not raised in Step 4's auth columns.
Or: "PASS 2: no additional gaps --" with specific justification for the three highest-risk
boundaries confirming each is clean.

---

## STEP 9 -- ERROR PATH

Trace one complete error path from origin to caller response.
Select the highest-probability failure from Step 4.

DISQUALIFIER (C-06): Fails if: states "error returned to caller" without propagation chain /
skips from origin to final response without showing intermediate boundaries.

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
| C-11 | 5 | 5 | 5 | 2 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 2 | 5 | 5 |
| C-13 | 5 | 5 | 5 | 2 | 5 | 5 |
| C-14 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-15 | 5 | 5 | 5 | 2 | 5 | 5 |
| C-16 | 5 | 5 | 5 | 2 | 5 | 5 |
| **Total** | **135** | **135** | **135** | **120** | **135** | **135** |
| All essential pass | -- | YES | YES | YES | YES | YES |
| Golden (>=80) | -- | YES | YES | YES | YES | YES |

**Ranking**: V-01 = V-02 = V-04 = V-05 (135) > V-03 (120)

---

### Per-criterion notes

**C-14 in V-03 PASS**: The C-08/C-14 DISQUALIFIER block gives both prohibited patterns
("exponential backoff" without values) and required passing format per mechanism type
(algorithm=exponential, initial=100ms, multiplier=2x, max-attempts=5). This is a binary text
test -- the presence of "exponential backoff" without a numeric value is detectable and banned.
C-08 DISQUALIFIERs in R3 V-03 already reliably fired. C-14 extends the same pattern with
quantified-value requirements, expected to behave similarly. Predicted PASS (5/5).

**C-11/C-12/C-13 in V-03 PARTIAL**: Inherited from R3 V-03 (2/5 each). DISQUALIFIERs name
the failure patterns but provide no structural scaffolding (no gate, no column template, no
pre-filled rows). The R4 V-03 additions do not address C-11/C-12/C-13, so no change expected.

**C-15 in V-03 PARTIAL**: The DISQUALIFIER bans "listing a single Seq# for a multi-boundary
threat" and enumeration shortcuts ("multiple," "various"). But without a pre-filled column
template that is structurally incomplete without Seq# values, the model may produce rows that
technically avoid the DISQUALIFIER text while missing a boundary. Predicted PARTIAL (2/5).

**C-16 in V-03 PARTIAL**: The DISQUALIFIER bans vague cross-references ("based on credential
threats," "similar to row 2"). But without the mandatory cross-reference block format as a
structural element in Step 7 (catalog row #, exact threat class, Seq# list, divergence Seq#),
the model may provide a reference that names the class without the full block. Predicted PARTIAL.

**Why V-01 reaches 135 vs R3 V-01's 120**: Three additive mechanisms:
1. Role-after-inventory provides platform-specific parameter vocabulary for C-14 -- not just a
   format requirement but a contextualized source for the correct values.
2. Exhaustiveness check paragraph is a directed re-examination step with a named failure mode
   ("adds missing Seq# before proceeding") -- structurally new vs R3 V-01 which had no check.
3. Mandatory cross-reference block in Step 7 with four required fields (row #, class name,
   Seq# list, divergence Seq#) is a structured output requirement vs R3 V-05's informal
   "Step 6 row cited" annotation.

**V-04 vs V-01**: V-04 adds V-02's structural Remediation Register (C-14 enforced by column
schema) to V-01's role sequence (C-14 enforced by vocabulary contextualization). These are
complementary enforcement mechanisms for the same criterion. V-04's exhaustiveness check is
a lifecycle gate (GATE: Step 7 may not begin until confirmed), stronger than V-01's check
paragraph. V-04 also inherits V-02's C-16 Candidate column in the catalog -- the adversarial
selection source is pre-marked, making Step 7's cross-reference a forward reference to a
Y-marked row rather than a backward lookup. Expected equivalent score, stronger C-14/C-15/C-16
precision.

**V-05 excellence signals** (beyond R3 V-05):
1. Role-after-inventory + Remediation Register + DISQUALIFIER = three-layer C-14 enforcement:
   vocabulary source (role), structural column (Parameters), and banned patterns (DISQUALIFIER).
2. Exhaustiveness gate is a blocking lifecycle condition ("Step 7 may not begin until confirmed
   complete"), not a suggestion or paragraph -- the strongest possible C-15 enforcement short
   of a pre-computed oracle.
3. C-16 is enforced by mandatory cross-reference block + DISQUALIFIER that explicitly names
   the "vague reference" failure pattern ("based on credential threats" -- the exact phrasing
   a model uses when referencing the catalog loosely rather than precisely).
4. Step 10 cross-catalog interaction is inherited from R3 V-05: batch analysis is explicitly
   linked to Step 6 threat classes (concurrent mutation, malformed input), the only variation
   where C-07 and C-13 structurally reinforce each other.
