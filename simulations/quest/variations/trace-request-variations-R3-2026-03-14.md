Here are the 5 R3 variations:

---

## Summary

| V | Axis | Core C-12/C-13 mechanism | Predicted |
|---|------|--------------------------|-----------|
| **V-01** | Lifecycle emphasis | C-12: sum-closure gate (must close before proceeding); C-13: post-traversal catalog maps each class to all applicable Seq# rows | 120/120 |
| **V-02** | Output format | C-12: budget columns baked into table schema with inline arithmetic rules; C-13: pre-filled catalog template with "All Applicable Boundaries (Seq#)" column | 120/120 |
| **V-03** | Phrasing register (DISQUALIFIER) | C-12: DISQUALIFIER for prose annotation + arithmetic mismatch; C-13: DISQUALIFIER for single-boundary rows | 111/120 |
| **V-04** | Phrasing register (interrogative) | C-12: direct question forcing sum verification; C-13: question asking for all applicable boundaries per class | 108/120 |
| **V-05** | Full synthesis | All R2 V-05 mechanisms + C-12 sum-closure gate + C-13 boundary-Seq catalog + DISQUALIFIERS for both | 120/120 |

---

**What's new vs R2:**

**C-12** — R2 V-05 already had a `Budget Draw p50/p99` column, which satisfies C-05. But C-12 requires *arithmetic consistency*: sequential draws must sum to the C-10 critical-path total, parallel draws provably excluded. R2 Step 5 computes a chain sum but never cross-checks it against Step 4's per-boundary cells. The fix: a **closure gate** that requires `Part A sequential sum = Part C critical-path total`, with a DISQUALIFIER naming all three failure modes (p50 mismatch, p99 mismatch, parallel double-counting).

**C-13** — R2 V-05's threat enumeration table mapped each class to one "highest-risk boundary." C-13 requires mapping to *all boundaries where each applies*, by Seq number. The fix: rename the column to `"All Applicable Boundaries (Seq#)"` with a rule that a class applicable at three boundaries lists all three, and a DISQUALIFIER for single-boundary rows.

**Why V-03/V-04 don't hit 120:** DISQUALIFIER text and interrogative questions are necessary but not sufficient for C-12 and C-13 — both criteria require structural scaffolding (a table column that's structurally incomplete without multiple Seq# values, or a gate that blocks forward progress until the sum closes) that text constraints alone can't enforce.
ll R2 V-05 mechanisms + C-12 sum-closure gate + C-13 boundary-Seq catalog + DISQUALIFIERS for both new criteria | 120/120 |

**What changed from R2:**

- **C-12 enforcement**: R2 V-05's budget draw column satisfies C-05 (latency annotation per boundary) but not C-12. C-12 requires the per-boundary values to be *arithmetically consistent* with the C-10 chain total: sequential draws must sum correctly, parallel draws must be provably excluded. V-01 adds a mandatory sum-closure gate; V-05 adds both the gate and a DISQUALIFIER.
- **C-13 enforcement**: R2 V-05's threat enumeration table names the highest-risk boundary per class. C-13 requires mapping each class to *all boundaries where it manifests*, referenced by Seq number. V-02 introduces the boundary-Seq column; V-05 combines it with a DISQUALIFIER.
- **C-07 regression prevention**: R2 V-01--V-03 failed C-07. All R3 variations preserve the batch section from R2 V-05 to ensure C-07 is not regressed.

---

## V-01: Lifecycle Emphasis -- Budget Sum-Closure Gate + Boundary-Mapped Threat Catalog

**Axis**: Lifecycle emphasis -- adds a mandatory sum-closure step that must "close" (sequential p50/p99 draws sum to critical-path total) before the trace can proceed; threat catalog built after traversal maps each class to all applicable boundary Seq numbers.

**Hypothesis**: Making the budget sum a lifecycle gate (not just a computation step) forces the model to treat the per-boundary p50/p99 values as load-bearing inputs, not optional annotations. If the sum doesn't close, the model must return to the traversal table and correct estimates -- making C-12 a structural forcing function rather than a post-hoc checklist item. The threat catalog maps each class to all applicable boundaries (not just the highest-risk one), which is the specific gap C-13 exposes versus R2 V-05's threat enumeration table.

```
You are running /trace-request for: {{topic}}

Select your platform expert role:
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

State your role before Step 1.

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

List every boundary in traversal order before filling Step 4.

A boundary is any transition where a network call is made, identity context is evaluated,
or data is read from or written to a store. Token validation, gateway routing, cache lookup,
and audit emission are boundaries.

1. [Entry point -- as declared in Step 1]
2. [Second boundary]
3. ...
[Continue until response is assembled and returned to caller]

GATE: Step 4 rows must correspond to the boundaries listed here, in order.
No boundary listed here may be absent from Step 4.

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

- **Remediation**: Specific mechanism only (retry -- algorithm + values; circuit breaker --
  threshold + interval; scope addition -- exact scope + identity; validation guard -- boundary +
  field + rule). FAILS: "add error handling," "improve resilience."

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
- "All Applicable Boundary Seq Numbers" column: list every Step 3 Seq # where this threat
  class can manifest -- not just the highest-risk one. A threat class that applies to three
  boundaries must list all three.
- Severity: Low / Medium / High.
- After completing the table: mark the highest-severity row. If two rows tie on severity,
  prefer the one with the most applicable boundaries.

---

## STEP 7 -- ADVERSARIAL SCENARIO

Select the highest-severity threat class from Step 6. Show:

Selected threat class: [class from Step 6]
Highest-risk boundary: [Step 3 Seq # -- name]
Adversarial condition: [specific input or state -- not a generic category]
Divergence boundary: [Step 3 Seq # -- exact boundary where path splits from nominal]
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

## V-02: Output Format -- Table-First Schema with Budget Columns + Boundary-Mapped Threat Catalog

**Axis**: Output format -- the traversal table schema is declared with dedicated p50/p99 budget columns from the first row, with inline arithmetic rules for sequential vs. parallel draws; the threat catalog is a pre-filled table template requiring one row per threat class with a multi-value Seq# column.

**Hypothesis**: Prescribing the exact table schema forces every cell to be populated; the p50/p99 columns become structural inputs that the budget sum can be checked against later. The threat catalog template with a "Boundaries Where Applicable (all Seq#)" column makes it structurally impossible to write a catalog row without mapping to specific boundaries -- the table cell won't be complete without them. Risk: structural completeness without depth; a model may populate all cells with thin values to satisfy format requirements.

```
You are running /trace-request for: {{topic}}

Select your platform expert role:
- Dataverse platform expert (entity model, OData pipeline, security roles, plugin execution, audit)
- Commerce platform expert (pricing, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls, flow runtime)

State your role.

---

## ENTRY POINT

Required: HTTP method + full path (or event type + source), payload field names + data types +
size constraints, caller identity type, credential type.

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

Every column required. Per-column rules appear below the table.

| Seq | Boundary | Failure Mode | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Sequential? | Remediation |
|-----|----------|-------------|-------|---------------------------|----------|----------|-------------|-------------|
| 1   |          |             |       |                           |          |          | Y / N (#)   |             |
| 2   |          |             |       |                           |          |          |             |             |

**p50 / p99 column rules (C-12 arithmetic):**
- Required: a specific millisecond value or range for every row. "Fast," "low," or blank fails.
- Sub-5ms: "< 5ms -- [reason]" is accepted.
- Sequential? column: Y if this boundary is on the longest sequential chain. N if it runs
  parallel with another boundary -- write N (#) where # identifies the partner boundary Seq.
- Parallel rows are NOT additive. They share a latency slot with their partner. Only the longer
  of the two parallel rows contributes to the critical-path sum.

**Other column rules:**
- Failure Mode: name the specific mechanism (HTTP status, timeout value, throttle limit,
  auth rejection type, payload rule). "May fail" fails.
- Auth?: Y or N.
- Permission / Scope / Role: Y rows name the exact artifact. N rows write "AUTH GAP -- [reason]."
  "Standard auth" or "valid token" fails.
- Remediation: name the specific mechanism. "Add error handling" fails.

---

## CRITICAL PATH SUMMARY TABLE

Derived from the traversal table. Include only Sequential = Y rows.

| Seq | Boundary | p50 (ms) | p99 (ms) | Excluded parallel pair |
|-----|----------|----------|----------|------------------------|
|     |          |          |          | N/A                    |
|     |          |          |          | N/A                    |
| **TOTAL** |     |          |          |                        |

**Consistency check**: The TOTAL p50 in this table must equal the sum of the p50 column values
for all Sequential = Y rows in the traversal table above. Same for p99. If they differ, correct
the traversal table before proceeding.

List all excluded parallel rows: [Seq# pair -- confirm genuinely concurrent, not sequential].

---

## THREAT CLASS CATALOG

Build before selecting the adversarial scenario. Reference Seq numbers from the boundary inventory.

| # | Threat Class | Boundaries Where Applicable (all Seq#) | Severity | Example Trigger at Highest-Risk Boundary |
|---|---|---|---|---|
| 1 | Malformed input | | | |
| 2 | Credential expiry | | | |
| 3 | Concurrent mutation | | | |
| 4 | Missing permission scope | | | |
| 5 | Network partition | | | |

Rules:
- "Boundaries Where Applicable" column: list every Seq# where this threat class can manifest.
  A threat class with three applicable boundaries lists all three (e.g., "1, 4, 7").
  Writing only the highest-risk boundary fails C-13.
- Minimum 4 rows; add rows for additional threat classes relevant to this request.
- Severity: Low / Medium / High.

After the table: mark the highest-severity class. This is the adversarial scenario source.

---

## PASS 2: AUTHORIZATION AUDIT

Walk the traversal table a second time. Exclusive focus: authorization correctness.
Do not mirror the Auth / Permission columns from the traversal table.

For each boundary:
1. Is auth explicitly checked here or assumed from upstream? If assumed: can a caller reach
   this boundary without the upstream check executing?
2. Could adjacent permissions access a higher-privilege resource through this boundary?
3. Is minimum-required scope enforced?

Required: at least one gap not raised in the traversal table. Or: "PASS 2: no additional gaps --"
with specific justification for the three highest-risk boundaries.

---

## ADVERSARIAL SCENARIO

Selected threat class: [highest-severity class from catalog]
Adversarial condition: [specific input or state]
Divergence boundary: [Seq# from inventory]
Path after divergence: [boundary-by-boundary to final response]
Outcome: [concrete impact]

---

## ERROR PATH TRACE

Select the highest-probability failure from the traversal table. Trace the full path from
origin to caller surface. Show every intermediate boundary -- do not skip steps.

Origin: [Seq# and boundary name]
Failure: [mechanism from traversal table]
At [next boundary]: [propagated / wrapped / retried / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

## BATCH AND EDGE CASES

Platform limit, enforcement boundary (Seq#), N-1/N/N+1 behavior, per-item overhead.
"Batch not applicable -- [specific reason]" if not applicable.
```

---

## V-03: Phrasing Register -- DISQUALIFIER Blocks for C-12 and C-13

**Axis**: Phrasing register -- negative-space enforcement: every section opens with explicit text patterns that auto-fail that criterion; C-12 and C-13 each receive their own DISQUALIFIER block naming the specific failure modes extracted from the rubric's pass conditions.

**Hypothesis**: Naming the exact failure modes for C-12 ("budget column whose sequential rows don't sum to the critical-path total") and C-13 ("threat catalog that lists one boundary per class rather than all applicable boundaries") activates constraint-satisfaction mode. The model is told what patterns to avoid in exact wording -- a different cognitive operation than being told what to produce. Building on R2 V-03's proven DISQUALIFIER pattern (100/110 on v2 rubric), C-12 and C-13 get the same treatment. Risk: disqualifiers add instruction surface without structural scaffolding; a model may produce the disqualifier-compliant form with thin content that passes the literal test but fails depth.

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

DISQUALIFIER (C-12 -- latency column): Any latency section matching these patterns fails C-12:
- Prose-only annotation without a structured p50/p99 per boundary
- "fast" or "low latency" without a ms value
- "negligible" without a number and reason
- A blank latency cell for any boundary
Required: a dedicated p50 and p99 value (ms or range) for every boundary row.

DISQUALIFIER (C-12 -- arithmetic): Any critical path computation matching these patterns fails:
- Sequential p50 values in the traversal do not sum to the critical-path p50 stated later
- Sequential p99 values do not sum to the critical-path p99 stated later
- A parallel boundary's p50/p99 is included in the sequential sum (double-counting)
Required: verify that per-boundary sequential draws sum to the critical-path total. State
both numbers and confirm they match.

For each boundary in traversal order:

**Boundary: [name] [Seq#]**
Input: [what crosses this boundary]
Failure mode(s): [disqualifier rules above apply]
Auth check: [disqualifier rules above apply]
p50 (ms): [disqualifier rules above apply]
p99 (ms): [disqualifier rules above apply]
Draw type: Sequential (adds to chain) / Parallel with [Seq#] (slot shared, not additive)
Remediation: [disqualifier rules below apply]

---

## CRITICAL PATH

DISQUALIFIER (C-10): Any critical path section matching these patterns fails:
- Lists latency contributors without naming the sequential chain
- States a p99 total without showing which Seq# rows sum to produce it
- Omits whether parallel paths are excluded from the sum

Required: sequential chain (Seq# -> Seq# -> ...), excluded parallel branches, cumulative
p50, cumulative p99, dominant boundary.

Sequential sum verification: p50 draws [Seq#] + [Seq#] + ... = ___ms / p99 draws = ___ms.
Critical-path p50 = ___ms (must equal sequential p50 sum).
Critical-path p99 = ___ms (must equal sequential p99 sum).

---

## THREAT CLASS CATALOG

DISQUALIFIER (C-13): Any threat catalog matching these patterns fails:
- Lists threat classes without referencing specific boundary Seq numbers
- Provides only one "highest-risk boundary" per threat class rather than all applicable boundaries
- Derives the catalog from the adversarial scenario rather than building it before selection
- Fewer than 4 threat classes

Required: a structured table mapping at least 4 threat classes to all applicable boundary
Seq numbers (not just the highest-risk one), built before adversarial scenario selection.

| Threat Class | All Applicable Boundaries (Seq#) | Severity | Example Trigger |
|---|---|---|---|
| Malformed input | | | |
| Credential expiry | | | |
| Concurrent mutation | | | |
| Missing permission scope | | | |
| Network partition | | | |

Add rows for additional applicable threat classes. Build this table before selecting the
adversarial scenario below.

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

Select the highest-severity threat class from the catalog above (prefer the class with the
most applicable boundaries if severity ties). Show:

- Divergence boundary: [Seq# -- exact boundary where path splits from nominal]
- Adversarial condition: [specific input or state]
- Path after divergence: [each boundary to final response]
- Outcome: [concrete impact]

---

## ERROR PATH

DISQUALIFIER (C-06): Fails if: states "error returned to caller" without the propagation chain /
skips from origin to final response without showing intermediate boundaries.

Trace one complete error path. Select the highest-probability failure from the traversal.
Show every boundary between origin and caller.

---

## REMEDIATION

DISQUALIFIER (C-08): Any remediation matching these patterns fails:
"add error handling" / "improve resilience" / "add retry logic" without named values /
"fix the authorization gap" without naming the permission artifact to add.

For every failure mode from the traversal and every gap from the re-walk: one specific
mechanism at a named boundary.

---

## BATCH AND EDGE CASES

Platform limit, enforcement boundary (Seq#), N-1/N/N+1 behavior, per-item overhead.
"Batch not applicable -- [specific reason]" if not applicable.
```

---

## V-04: Phrasing Register -- Interrogative with Explicit C-12 and C-13 Questions

**Axis**: Phrasing register -- conversational/interrogative: each section is structured as questions to answer; C-12 gets a dedicated arithmetic verification question; C-13 gets a question that explicitly asks for all applicable boundaries per threat class before adversarial scenario selection.

**Hypothesis**: Question-driven framing activates a reflective, exploratory reasoning mode that is particularly effective for C-12 and C-13 because both require the model to step back and check its own work. "Do your per-boundary p50 values sum to your critical-path total?" and "For each threat class, which specific boundaries -- not just the worst one -- does it apply to?" are more likely to surface omissions than imperative commands because they cast the model as a self-verifier rather than a producer. Risk: question-driven prompts are less structurally coercive than table schemas; a model may answer questions at a low depth that satisfies the literal form without the analytical substance.

```
You are running /trace-request for: {{topic}}

Based on the request context, identify yourself: are you a Dataverse API specialist, a Commerce
platform engineer, or a Power Automate connector expert? State this at the top.

Answer each question below in order. For table questions, fill the table. For prose questions,
write at least a paragraph. No question may be skipped.

---

**Q1. What is the entry point?**

Name the full entry point: HTTP method + path (or event type + source), the required payload
fields and their types, the caller identity type, and the credential at entry.

---

**Q2. What is your latency budget for this request?**

Before listing any boundary: what end-to-end latency budget applies?
Derive from the first applicable source: documented SLA (cite it), caller configured timeout
(state the value), or UX threshold (500ms interactive / 2000ms background / 10000ms async).

State: "Budget: [N]ms (source: [SLA / timeout / UX threshold])."

---

**Q3. What is the complete list of boundaries this request crosses?**

A boundary is any point where a network call is made, identity context is evaluated, or data
is read from or written to a store. Token validation, gateway routing, cache lookups, and
audit emission are boundaries.

| Seq | Boundary Name | Protocol | Component From -> To |
|-----|---------------|----------|----------------------|
| 1   |               |          |                      |
| ... |               |          |                      |

Do not collapse multiple hops into one row.

---

**Q4. At each boundary, what can go wrong, what auth check runs, and how long does it take?**

| Seq | Boundary | Failure Mode (specific) | Auth? | Permission / Scope / Role | p50 (ms) | p99 (ms) | Sequential? |
|-----|----------|-------------------------|-------|---------------------------|----------|----------|-------------|

Column rules:
- Failure Mode: name the mechanism (HTTP status, timeout value, throttle limit, auth rejection
  type, payload rule). "May fail" without a named mechanism fails.
- Auth? Y or N. Y rows: name the exact permission artifact. N rows: "AUTH GAP -- [reason]."
- p50/p99: specific ms values. "Fast" without a number fails.
- Sequential?: Y if additive on the critical path. N ([Seq#]) if parallel with another row.

---

**Q5. Do your per-boundary latency values add up correctly?**

From Q4's p50 and p99 columns:
- Which rows are Sequential (additive on the critical path)?
- Which rows are Parallel (share a slot with a partner row)?

Compute:
Sequential p50 sum = ___ms
Sequential p99 sum = ___ms

Now verify: does your sequential p50 sum equal your intended critical-path p50?
Does your sequential p99 sum equal your intended critical-path p99?
Are all parallel rows confirmed as genuinely concurrent (not sequential dependencies)?

If any sum does not close: which boundary estimate needs correction? Return to Q4 and fix
it before continuing.

**State the verified critical path:**
Sequential chain: [Q3 Seq# -> Seq# -> ...]
Excluded parallel rows: [list each with partner Seq# and concurrency confirmation]
Critical-path p50: ___ms (= sequential p50 sum above)
Critical-path p99: ___ms (= sequential p99 sum above)
Budget headroom (p99): [Q2 budget] - [critical-path p99] = ___ms

---

**Q6. For each threat class, which specific boundaries does it apply to -- not just the worst one?**

Before choosing an adversarial scenario, map every relevant threat class to all the boundaries
(by Seq# from Q3) where it can manifest. If a class applies at three boundaries, list all three.

| # | Threat Class | All Applicable Seq Numbers | Severity | Example Trigger |
|---|---|---|---|---|
| 1 | Malformed input | | | |
| 2 | Credential expiry | | | |
| 3 | Concurrent mutation | | | |
| 4 | Missing permission scope | | | |
| 5 | Network partition | | | |

Add rows for additional applicable classes. Minimum 4 rows.

For each row, ask: "Does this threat class apply only at Seq# X, or also at Seq# Y and Z?"
List all of them.

---

**Q7. Looking at the authorization picture again -- anything you missed the first time?**

Walk Q4's auth columns a second time. This time, ask:
1. Is auth actually checked here, or assumed from an upstream result? If assumed: could a
   caller reach this boundary without the upstream check executing?
2. Could a caller with adjacent permissions escalate through this boundary?
3. Is minimum-required scope enforced, or would a broader token also be accepted?

State at least one gap not surfaced in Q4. Or: "Re-walk found no additional gaps --" with
specific justification for the three highest-risk boundaries.

---

**Q8. What adversarial scenario does the threat catalog suggest?**

From Q6: select the highest-severity threat class (prefer the one with the most applicable
boundaries if severity ties). Show:

Selected class: [from Q6]
Why this class: [one sentence connecting it to Q4 and Q7 findings]
Divergence boundary: [Q3 Seq# where nominal and adversarial paths split]
Adversarial condition: [specific input or state -- not a generic category]
Path after divergence: [each boundary to final response]
Outcome: [concrete impact]

---

**Q9. If the highest-probability failure occurs, what does the caller see?**

Trace the full error path from the originating boundary to the caller surface. Show every
intermediate boundary -- do not skip steps.

Origin: [Q3 Seq# and boundary name]
Failure: [mechanism from Q4]
At [next boundary]: [propagated / wrapped / retried / swallowed]
...
Caller receives: [status + body, timeout, or silent empty response]

---

**Q10. Are there batch, pagination, or concurrent-access edge cases?**

For each batch or paginated operation: what is the limit, which boundary enforces it, and
what happens at N-1 / N / N+1? Does per-item overhead multiply under batch load?
Does the batch behavior interact with any threat class from Q6?

"Batch not applicable -- [reason]" if not applicable.
```

---

## V-05: Full Synthesis -- R2 V-05 + C-12 Sum-Closure Gate + C-13 Boundary-Mapped Catalog + DISQUALIFIERS

**Axes**: All R2 V-05 mechanisms (boundary inventory gate, PASS 1 traversal table with column DISQUALIFIERS, critical path accounting, PASS 2 auth audit, threat enumeration table, error path, batch section) + C-12 enforcement (explicit sum-closure gate in Step 5 that requires sequential draws to equal the critical-path total, with DISQUALIFIER naming the three failure modes: p50 mismatch, p99 mismatch, parallel double-counting) + C-13 enforcement (threat catalog expanded with "All Applicable Boundaries (Seq#)" column requiring multi-value entries, DISQUALIFIER for single-boundary rows, built and completed before adversarial selection).

**Hypothesis**: Every criterion in the v3 rubric has at least one structural enforcement mechanism. C-01 (entry point DISQUALIFIER gate), C-02 (boundary inventory gate before table), C-03 (column DISQUALIFIER: "may fail"), C-04 (column DISQUALIFIER: "standard auth"), C-05 (column DISQUALIFIER: "fast"), C-06 (error path with propagation chain DISQUALIFIER), C-07 (dedicated batch section with cross-catalog link), C-08 (remediation column DISQUALIFIER: "add error handling"), C-09 (threat catalog selects adversarial class by Seq# before scenario), C-10 (critical path accounting step with chain-naming DISQUALIFIER), C-11 (PASS 2 as structural peer of PASS 1 with mirroring DISQUALIFIER), C-12 (sum-closure gate in Step 5: sequential draws must equal critical-path total; DISQUALIFIER for three specific arithmetic failure modes), C-13 (threat catalog with "All Applicable Boundaries (Seq#)" column; DISQUALIFIER for single-boundary rows; completed before adversarial selection with citation requirement). R2 V-05's proven foundation is preserved intact; C-12 and C-13 enforcement is added without removing or replacing what already works.

```
You are running /trace-request for: {{topic}}

Select your platform expert role:
- Dataverse platform expert (entity reads/writes, OData pipeline, security roles, plugin
  execution, audit log emission)
- Commerce platform expert (pricing engine, cart session, order lifecycle, payment gateway, tax)
- Power Automate platform expert (trigger evaluation, action execution, connector calls,
  flow runtime, throttle and retry behavior)

State your role before Step 1.

---

## STEP 1 -- ENTRY POINT

DISQUALIFIER: Entry points matching these patterns fail C-01:
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

List every boundary in traversal order. Do not fill Step 4's table until this inventory is complete.

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

## STEP 4 -- PASS 1 TRAVERSAL TABLE

One row per boundary from Step 3. Every column required. Column DISQUALIFIERS apply per cell.

| # | Boundary | Failure Mode(s) | Auth? | Permission / Scope / Role | p50 draw (ms) | p99 draw (ms) | Draw type | Remediation |
|---|----------|-----------------|-------|---------------------------|---------------|---------------|-----------|-------------|
| 1 |          |                 |       |                           |               |               |           |             |
| 2 |          |                 |       |                           |               |               |           |             |

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

- **Remediation**: FAILS if cell contains: "add error handling," "improve resilience," "handle
  the error," "add retry logic" without named values.
  Required: specific mechanism at this boundary (exponential backoff -- algorithm + max retries +
  base delay; circuit breaker -- threshold + window + half-open; exact scope to add + identity;
  validation boundary + field + rule).

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
- After completing the table: identify the highest-severity class with the most Step 8 PASS 2
  overlap. This is the adversarial scenario source.

---

## STEP 7 -- ADVERSARIAL SCENARIO

Selected threat class: [highest-severity class from Step 6, with most PASS 2 overlap]
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
| C-11 | 5 | 5 | 5 | 5 | 5 | 5 |
| C-12 | 5 | 5 | 5 | 3 | 3 | 5 |
| C-13 | 5 | 5 | 5 | 3 | 3 | 5 |
| **Total** | **120** | **120** | **120** | **111** | **108** | **120** |
| All essential pass | -- | ✓ | ✓ | ✓ | ✓ | ✓ |
| Golden (>=80) | -- | ✓ | ✓ | ✓ | ✓ | ✓ |

**Ranking**: V-01 = V-02 = V-05 (120) > V-03 (111) > V-04 (108)

---

### Per-criterion notes

**C-12 gap in V-03 and V-04**: V-03's DISQUALIFIER names the failure pattern but provides no structural forcing function to prevent non-additive values. The constraint text is necessary but not sufficient -- a model can write values that happen to pass the literal disqualifier test without the arithmetic being sound. V-04's interrogative question puts the check in the model's hands. Expected 3/5 not 5/5.

**C-13 gap in V-03 and V-04**: Same pattern. V-03's DISQUALIFIER names the "single-boundary row" failure mode but doesn't supply a table column template requiring multi-value Seq# entries. V-04's question ("which specific boundaries does it apply to?") is weaker than V-01/V-02/V-05's column schema that has an "All Applicable Boundaries (Seq#)" cell that is structurally incomplete without multiple values.

**Why V-01 and V-02 both reach 120**: Different structural mechanisms, same result. V-01's sum-closure gate is a lifecycle mechanism (cannot proceed until the sum closes; the model must return to the traversal table if it doesn't). V-02's table schema is a format mechanism (the column template requires a multi-value Seq# cell; a table with only one value per row is visually incomplete). V-05 combines both mechanisms plus DISQUALIFIERS for belt-and-suspenders coverage.

**V-05 excellence signals**:
1. Sum-closure gate (Part C = Part A) with a three-failure-mode DISQUALIFIER (p50 mismatch, p99 mismatch, parallel double-counting) -- any of the three failure modes named in the rubric's C-12 pass condition is now explicitly disqualified
2. C-13 DISQUALIFIER names the exact R2 failure mode: "lists only one highest-risk boundary rather than all applicable boundaries"
3. Step 7 requires citing the Step 6 catalog row by # and class name -- prevents post-hoc catalog rationalization where the adversarial scenario is chosen first and the catalog is written to match
4. Step 10 cross-catalog interaction links C-07 batch analysis to C-13's concurrent mutation and malformed input classes -- the only variation where C-07 and C-13 reinforce each other structurally
