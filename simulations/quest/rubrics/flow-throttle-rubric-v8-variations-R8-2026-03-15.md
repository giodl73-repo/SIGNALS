# flow-throttle — Round 8 Variations (v8 Rubric, 154-point max)

## Variation Axes and Hypotheses

R7 confirmed that both temporal and imperative boundary-event forms (C-25) paired with
round-head immediacy (C-26) reach the 148/148 v7 ceiling. R8 must probe the two new v8
aspirational criteria (C-27 and C-28) with deliberate isolation tests.

**C-27** (3 pts): The boundary-event phrase required by C-25 must contain the specific
round/phase/stage identifier from the barrier heading — not a generic activity category.
"before any construct evaluation begins" is a C-25 pass but a C-27 fail.
"before any **Round 2** construct evaluation begins" is both a C-25 and a C-27 pass.

**C-28** (3 pts): Both C-25 (trigger named in container header) and C-26 (round-head
immediacy) satisfied from the same container — making execution order dually machine-
verifiable. C-28 requires C-25 AND C-26. It does NOT require C-27 (independent).

Three single-axis tests (V-01, V-02, V-05), then two combined-ceiling tests (V-03, V-04):

| Variation | Axis | C-25 | C-26 | C-27 | C-28 | Predicted score |
|-----------|------|------|------|------|------|-----------------|
| V-01 | C-27 isolation: generic phrase, no round name, immediate | PASS | PASS | FAIL | PASS | 151/154 |
| V-02 | C-28 isolation via C-26 failure: round-named phrase, transitional sentence | PASS | FAIL | PASS | FAIL | 151/154 |
| V-03 | Ceiling: temporal form, round name, immediate | PASS | PASS | PASS | PASS | 154/154 |
| V-04 | Ceiling: imperative form, round name, immediate | PASS | PASS | PASS | PASS | 154/154 |
| V-05 | C-25 cascade failure: no phrase, immediate (C-27+C-28 both lose precondition) | FAIL | PASS | FAIL | FAIL | 145/154 |

V-01 and V-02 are clean single-axis C-27 and C-28 isolation tests.
V-03 and V-04 confirm ceiling with distinct phrase forms (temporal vs. imperative).
V-05 confirms C-25 failure cascades to both C-27 and C-28 — costing exactly 9 pts from
the v7 ceiling (3 pts each: C-25 + C-27 + C-28), not more, because C-26 still passes.

---

## V-01 — C-27 Isolation: Generic Phrase, Round-Head Immediate

**Axis:** C-27 isolation — boundary-event phrase present (C-25 passes) but no round
identifier in the phrase (C-27 fails). Round-head immediacy preserved (C-26 passes).
C-28 passes because it requires C-25 AND C-26, both of which hold. Only C-27 is lost.
**Hypothesis:** Container name `PRE-EVALUATION ASSERTIONS (before any construct evaluation
begins)` satisfies C-21 (positional qualifier) and C-25 (boundary-event phrase). Fails
C-27: the phrase does not contain "Round 2" or equivalent round-level identifier. C-26
passes (container is first element under Round 2 heading). C-28 passes (C-25 AND C-26
both hold). Expected score: 151/154.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call
limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.
Generic "API limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing
fields receive a `?` flag — correct before proceeding.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Rule: UX categories MUST differ across tiers. Repeating the same category across two rows
does not pass. Each row must state what the user sees or experiences — not what the system
does internally.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write explicit acknowledgment with guards currently
in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm (fixed-interval hammering), fixed-misalign (undershoots or
overshoots required wait), silent-discard (request dropped without retry). At least one
gap required. If no gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them. A flat list of independent throttle risks without cascade relationships
does not pass.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

PA expert: either confirm the exact documented term or provide the corrected name. Generic
terms must be corrected here. "Confirmed" requires the exact PA documentation name — not
paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior.
Note: internal system behavior (e.g., queue depth increase, internal retry count) is not
user experience. Correct any row that conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation
time or headroom]." A qualitative "this will hit the limit" without numeric projection
does not pass.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs (e.g., concurrency control settings,
flow run queuing, Delay action with Retry-After value, request batching via Data
Operations, premium connector entitlement upgrade). "Add retries" and "reduce load" do
not count. Each remediation must map to a specific finding from PHASES 2-3 by label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition
each signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs (e.g.,
Office 365 E3 vs. Power Apps per-user plan request entitlements). State the impact on this
scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE to
OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling: run flow with synthetic volume
in dev environment, inject throttle error via mock connector, observe run history for 429
patterns, use Power Platform admin center to monitor request consumption during test.
"Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or
cascade labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used
   in Power Automate documentation? Does it match the product-published limit source?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a
   derived estimate? State the source (PA documentation, connector certification, admin
   center observed value, or estimate with confidence level).

3. **Rate unit precision:** Is the unit per-minute, per-second, per-24-hours, per-user,
   or per-environment? PA limits vary by unit type — confirm the unit matches the
   construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact
   signal path and load calculation) or qualitative ("will cause increased load")? Promote
   qualitative statements to structural ones using TABLE 9 arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a
   directional statement? If directional, compute the numeric projection from TABLE 9 data.

Write the Round 2 precision output as a structured table:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-01 prompt body.*

---

## V-02 — C-28 Isolation via C-26 Failure: Round-Named Phrase, Transitional Sentence

**Axis:** C-28 isolation via C-26 failure — boundary-event phrase names "Round 2"
(C-27 passes) but a transitional sentence appears between the `## ROUND 2` heading and
the pre-barrier container (C-26 fails, C-28 fails). C-28 cannot be satisfied without C-26.
**Hypothesis:** Container name `PRE-EVALUATION ASSERTIONS (before any Round 2 construct
evaluation begins)` satisfies C-25 (phrase present) and C-27 (phrase names "Round 2").
One transitional sentence before the container fails C-26 (heading-to-container adjacency
violated). C-28 fails because it requires both C-25 and C-26 and C-26 is absent.
Expected score: 151/154.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call
limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.
Generic "API limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing
fields receive a `?` flag — correct before proceeding.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Rule: UX categories MUST differ across tiers. Repeating the same category across two rows
does not pass. Each row must state what the user sees or experiences — not what the system
does internally.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write explicit acknowledgment with guards currently
in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm (fixed-interval hammering), fixed-misalign (undershoots or
overshoots required wait), silent-discard (request dropped without retry). At least one
gap required. If no gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them. A flat list of independent throttle risks without cascade relationships
does not pass.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

PA expert: either confirm the exact documented term or provide the corrected name. Generic
terms must be corrected here. "Confirmed" requires the exact PA documentation name — not
paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior.
Note: internal system behavior (e.g., queue depth increase, internal retry count) is not
user experience. Correct any row that conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation
time or headroom]." A qualitative "this will hit the limit" without numeric projection
does not pass.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs (e.g., concurrency control settings,
flow run queuing, Delay action with Retry-After value, request batching via Data
Operations, premium connector entitlement upgrade). "Add retries" and "reduce load" do
not count. Each remediation must map to a specific finding from PHASES 2-3 by label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition
each signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs (e.g.,
Office 365 E3 vs. Power Apps per-user plan request entitlements). State the impact on this
scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE to
OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling: run flow with synthetic volume
in dev environment, inject throttle error via mock connector, observe run history for 429
patterns, use Power Platform admin center to monitor request consumption during test.
"Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

Round 1 produced a complete throttle impact analysis. Round 2 now applies an independent
structural precision check to the constructs and cascade pairs identified above.

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or
cascade labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used
   in Power Automate documentation? Does it match the product-published limit source?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a
   derived estimate? State the source (PA documentation, connector certification, admin
   center observed value, or estimate with confidence level).

3. **Rate unit precision:** Is the unit per-minute, per-second, per-24-hours, per-user,
   or per-environment? PA limits vary by unit type — confirm the unit matches the
   construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact
   signal path and load calculation) or qualitative ("will cause increased load")? Promote
   qualitative statements to structural ones using TABLE 9 arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a
   directional statement? If directional, compute the numeric projection from TABLE 9 data.

Write the Round 2 precision output as a structured table:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Ceiling: Temporal Form, Round Name, Immediate

**Axis:** C-27 + C-28 ceiling confirmation — temporal boundary-event form names "Round 2",
container immediately follows `## ROUND 2` heading with zero intervening content.
**Hypothesis:** Container name `PRE-EVALUATION ASSERTIONS (before any Round 2 construct
evaluation begins)` satisfies C-25 (temporal phrase), C-26 (round-head immediacy), C-27
(phrase names "Round 2"), and C-28 (C-25 AND C-26 both pass from the same container).
Expected score: 154/154.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call
limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.
Generic "API limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing
fields receive a `?` flag — correct before proceeding.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Rule: UX categories MUST differ across tiers. Repeating the same category across two rows
does not pass. Each row must state what the user sees or experiences — not what the system
does internally.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write explicit acknowledgment with guards currently
in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm (fixed-interval hammering), fixed-misalign (undershoots or
overshoots required wait), silent-discard (request dropped without retry). At least one
gap required. If no gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them. A flat list of independent throttle risks without cascade relationships
does not pass.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

PA expert: either confirm the exact documented term or provide the corrected name. Generic
terms must be corrected here. "Confirmed" requires the exact PA documentation name — not
paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior.
Note: internal system behavior (e.g., queue depth increase, internal retry count) is not
user experience. Correct any row that conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation
time or headroom]." A qualitative "this will hit the limit" without numeric projection
does not pass.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs (e.g., concurrency control settings,
flow run queuing, Delay action with Retry-After value, request batching via Data
Operations, premium connector entitlement upgrade). "Add retries" and "reduce load" do
not count. Each remediation must map to a specific finding from PHASES 2-3 by label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition
each signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs (e.g.,
Office 365 E3 vs. Power Apps per-user plan request entitlements). State the impact on this
scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE to
OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling: run flow with synthetic volume
in dev environment, inject throttle error via mock connector, observe run history for 429
patterns, use Power Platform admin center to monitor request consumption during test.
"Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or
cascade labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used
   in Power Automate documentation? Does it match the product-published limit source?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a
   derived estimate? State the source (PA documentation, connector certification, admin
   center observed value, or estimate with confidence level).

3. **Rate unit precision:** Is the unit per-minute, per-second, per-24-hours, per-user,
   or per-environment? PA limits vary by unit type — confirm the unit matches the
   construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact
   signal path and load calculation) or qualitative ("will cause increased load")? Promote
   qualitative statements to structural ones using TABLE 9 arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a
   directional statement? If directional, compute the numeric projection from TABLE 9 data.

Write the Round 2 precision output as a structured table:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Ceiling: Imperative Form, Round Name, Immediate

**Axis:** C-27 + C-28 ceiling confirmation via imperative phrase form — container name
uses "execute before entering Round 2 evaluation" rather than the temporal "before any
Round 2 construct evaluation begins" form used in V-03. Confirms form equivalence for
C-27 at the v8 ceiling, analogous to the R7 temporal/imperative form equivalence finding
for C-25.
**Hypothesis:** Container name `PRE-EVALUATION DIRECTIVES (execute before entering
Round 2 evaluation)` satisfies C-21 (positional qualifier: "PRE-EVALUATION DIRECTIVES"),
C-25 (imperative boundary-event phrase), C-26 (zero intervening content), C-27 (phrase
contains "Round 2"), and C-28 (C-25 AND C-26 both pass from same container).
Expected score: 154/154.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call
limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.
Generic "API limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing
fields receive a `?` flag — correct before proceeding.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Rule: UX categories MUST differ across tiers. Repeating the same category across two rows
does not pass. Each row must state what the user sees or experiences — not what the system
does internally.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write explicit acknowledgment with guards currently
in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm (fixed-interval hammering), fixed-misalign (undershoots or
overshoots required wait), silent-discard (request dropped without retry). At least one
gap required. If no gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them. A flat list of independent throttle risks without cascade relationships
does not pass.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

PA expert: either confirm the exact documented term or provide the corrected name. Generic
terms must be corrected here. "Confirmed" requires the exact PA documentation name — not
paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior.
Note: internal system behavior (e.g., queue depth increase, internal retry count) is not
user experience. Correct any row that conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation
time or headroom]." A qualitative "this will hit the limit" without numeric projection
does not pass.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs (e.g., concurrency control settings,
flow run queuing, Delay action with Retry-After value, request batching via Data
Operations, premium connector entitlement upgrade). "Add retries" and "reduce load" do
not count. Each remediation must map to a specific finding from PHASES 2-3 by label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition
each signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs (e.g.,
Office 365 E3 vs. Power Apps per-user plan request entitlements). State the impact on this
scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE to
OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling: run flow with synthetic volume
in dev environment, inject throttle error via mock connector, observe run history for 429
patterns, use Power Platform admin center to monitor request consumption during test.
"Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION DIRECTIVES (execute before entering Round 2 evaluation)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or
cascade labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used
   in Power Automate documentation? Does it match the product-published limit source?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a
   derived estimate? State the source (PA documentation, connector certification, admin
   center observed value, or estimate with confidence level).

3. **Rate unit precision:** Is the unit per-minute, per-second, per-24-hours, per-user,
   or per-environment? PA limits vary by unit type — confirm the unit matches the
   construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact
   signal path and load calculation) or qualitative ("will cause increased load")? Promote
   qualitative statements to structural ones using TABLE 9 arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a
   directional statement? If directional, compute the numeric projection from TABLE 9 data.

Write the Round 2 precision output as a structured table:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — C-25 Cascade Failure: No Phrase, Immediate

**Axis:** C-25 cascade failure baseline — positional qualifier only in container name,
no boundary-event phrase. C-26 preserved (container immediately follows Round 2 heading).
Because C-25 fails, C-27 (requires C-25) and C-28 (requires C-25 AND C-26) both fail.
Only C-26 earns its 3 pts. Total loss from v7 ceiling: 9 pts (C-25 + C-27 + C-28).
**Hypothesis:** Container name `PRE-EVALUATION ASSERTIONS` satisfies C-21 (positional
qualifier present) but fails C-25 (no boundary-event phrase). C-26 passes (container is
the first element under the Round 2 heading, zero intervening content). C-27 cannot pass
because C-25 is its precondition. C-28 cannot pass because C-25 is required. This
establishes the three-way C-25 cascade as the maximum single-criterion cost in the v8
rubric. Expected score: 145/154.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput
across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call
limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.
Generic "API limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing
fields receive a `?` flag — correct before proceeding.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Rule: UX categories MUST differ across tiers. Repeating the same category across two rows
does not pass. Each row must state what the user sees or experiences — not what the system
does internally.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write explicit acknowledgment with guards currently
in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm (fixed-interval hammering), fixed-misalign (undershoots or
overshoots required wait), silent-discard (request dropped without retry). At least one
gap required. If no gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them. A flat list of independent throttle risks without cascade relationships
does not pass.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

PA expert: either confirm the exact documented term or provide the corrected name. Generic
terms must be corrected here. "Confirmed" requires the exact PA documentation name — not
paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior.
Note: internal system behavior (e.g., queue depth increase, internal retry count) is not
user experience. Correct any row that conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation
time or headroom]." A qualitative "this will hit the limit" without numeric projection
does not pass.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs (e.g., concurrency control settings,
flow run queuing, Delay action with Retry-After value, request batching via Data
Operations, premium connector entitlement upgrade). "Add retries" and "reduce load" do
not count. Each remediation must map to a specific finding from PHASES 2-3 by label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition
each signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs (e.g.,
Office 365 E3 vs. Power Apps per-user plan request entitlements). State the impact on this
scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE to
OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling: run flow with synthetic volume
in dev environment, inject throttle error via mock connector, observe run history for 429
patterns, use Power Platform admin center to monitor request consumption during test.
"Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or
cascade labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used
   in Power Automate documentation? Does it match the product-published limit source?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a
   derived estimate? State the source (PA documentation, connector certification, admin
   center observed value, or estimate with confidence level).

3. **Rate unit precision:** Is the unit per-minute, per-second, per-24-hours, per-user,
   or per-environment? PA limits vary by unit type — confirm the unit matches the
   construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact
   signal path and load calculation) or qualitative ("will cause increased load")? Promote
   qualitative statements to structural ones using TABLE 9 arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a
   directional statement? If directional, compute the numeric projection from TABLE 9 data.

Write the Round 2 precision output as a structured table:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*

---

## Predicted Score Table

| Variation | Axis | C-25 | C-26 | C-27 | C-28 | C-01..C-24 | Total / 154 |
|-----------|------|------|------|------|------|------------|-------------|
| V-01 | C-27 isolation: generic phrase, no round name | PASS | PASS | FAIL | PASS | 142 | **151** |
| V-02 | C-28 isolation via C-26 failure: round name, transitional sentence | PASS | FAIL | PASS | FAIL | 142 | **151** |
| V-03 | Ceiling: temporal form, "Round 2", immediate | PASS | PASS | PASS | PASS | 142 | **154** |
| V-04 | Ceiling: imperative form, "Round 2", immediate | PASS | PASS | PASS | PASS | 142 | **154** |
| V-05 | C-25 cascade: no phrase, immediate (C-27+C-28 lose precondition) | FAIL | PASS | FAIL | FAIL | 142 | **145** |

Three-level spread: 154 / 151 / 145.

**Key isolations this round delivers:**

1. **V-01 vs V-03/V-04**: C-27 pure isolation. Everything else equal (phrase present,
   immediate placement). Only the round name in the phrase differs. Confirms C-27 costs
   exactly 3 pts and is independent of C-28.

2. **V-02 vs V-03/V-04**: C-28 isolation via C-26 failure. Round name present (C-27 passes).
   One transitional sentence before container (C-26 fails, C-28 fails). Confirms C-28 costs
   exactly 3 pts independently of C-27.

3. **V-01 vs V-02**: C-27 and C-28 fail in opposite directions but same total (-3 each).
   Confirms symmetry: losing the round name costs the same as losing round-head immediacy.

4. **V-03 vs V-04**: Temporal ("before any Round 2 construct evaluation begins") vs.
   imperative ("execute before entering Round 2 evaluation") at v8 ceiling. Confirms form
   equivalence extends to C-27 — the round identifier satisfies C-27 regardless of phrase
   grammatical form.

5. **V-05**: C-25 failure cascades to C-27 + C-28 (both lose their precondition), costing
   9 pts from the 154 ceiling (not 3). The deepest single-criterion cascade in the rubric.
   Confirms the precondition chain cost: C-25 absence = C-25 fail + C-27 fail + C-28 fail.
