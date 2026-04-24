# flow-throttle — Round 7 Variations (v7 Rubric, 148-point max)

## Variation Axes and Hypotheses

R6 confirmed that all five content-layer axes (role sequence, output format, lifecycle
emphasis, phrasing register, combined) are structurally inert with respect to C-23/C-24.
Every R6 variation hit the 142/142 ceiling. R7 must probe the two new v7 aspirational
criteria (C-25 and C-26) with deliberate isolation tests, not content-layer variation.

**C-25** (3 pts): Container name includes BOTH a positional qualifier (C-21 precondition)
AND an explicit boundary-event phrase: temporal form ("before [any/the] X begins") or
imperative form ("execute/read before entering/starting X").

**C-26** (3 pts): Pre-barrier container is the FIRST content element under the Round 2
heading — zero intervening prose, transitions, or preamble between heading and container.

Three single-axis tests (V-01, V-02, V-03), then two combined-axis tests (V-04, V-05):

| Variation | Axis | C-25 | C-26 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Boundary-event phrase isolation (positional-only name) | FAIL | PASS | 145/148 |
| V-02 | Round-head immediacy probe (transitional sentence before container) | PASS | FAIL | 145/148 |
| V-03 | Temporal boundary-event form ("before any X begins") | PASS | PASS | 148/148 |
| V-04 | Imperative boundary-event form ("execute before entering X") | PASS | PASS | 148/148 |
| V-05 | Combined double-failure (positional-only + transitional sentence) | FAIL | FAIL | 142/148 |

V-01 and V-02 are clean single-axis isolation tests. V-03 confirms the temporal form of
C-25 at ceiling. V-04 confirms the imperative form of C-25 at ceiling. V-05 confirms
C-25/C-26 independence: losing both costs exactly 6 pts, not more, because the criteria
share no dependency.

---

## V-01 — Boundary-Event Phrase Isolation

**Axis:** Boundary-event phrase isolation — positional qualifier only, no phrase
**Hypothesis:** Container name "PRE-EVALUATION ASSERTIONS" satisfies C-21 (positional
qualifier present) but fails C-25 (no "before X begins" or "execute before entering X"
phrase). Round-head immediacy is preserved (container first under Round 2 heading), so
C-26 passes. Expected score: 145/148.

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

*End of V-01 prompt body.*

---

## V-02 — Round-Head Immediacy Probe

**Axis:** Round-head immediacy probe — one transitional sentence between Round 2 heading
and pre-barrier container
**Hypothesis:** Container name includes temporal boundary-event phrase, satisfying C-25.
But one transitional sentence appears between the "## ROUND 2" heading and the
PRE-EVALUATION ASSERTIONS block, failing C-26 (heading-to-container adjacency violated).
Expected score: 145/148.

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

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.
If no gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs. A flat list of independent throttle risks without cascade
relationships does not pass.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, mechanism stated,
severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

PA expert: confirm exact documented term or provide corrected name. Generic terms must be
corrected here.

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior.
Internal system state is not user experience. Correct conflations.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Show arithmetic for at least one row. SAFE / MARGINAL / OVER-LIMIT.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings. "Add retries" and
"reduce load" do not count.

**Section 4.E — Monitoring Signals**

At least one PA-observable signal with the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

At least one entitlement boundary with material limit difference. State scenario impact.

**Section 4.G — Test Approach**

At least one concrete PA test step. "Test in staging" without a specific method does not
pass.

---

## ROUND 2 — Structural Precision Pass

Round 1 produced a complete throttle impact analysis. Round 2 now applies an independent
structural precision check to the constructs and cascade pairs identified above.

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or cascade
labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used
   in Power Automate documentation?

2. **Numeric limit precision:** Is the limit value documented or estimated? State source.

3. **Rate unit precision:** Confirm unit matches construct's documented enforcement
   granularity (per-minute vs. per-24-hours vs. per-user vs. per-environment).

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural or qualitative? Promote qualitative
   statements using TABLE 9 arithmetic.

2. **Load-added precision:** Numeric projection or directional? Compute from TABLE 9 data.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding | Correction if needed |
|------------------------|------------------------|---------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Temporal Boundary-Event Form

**Axis:** Temporal boundary-event phrase — "before any Round 2 construct evaluation begins"
in container name, immediately after Round 2 heading
**Hypothesis:** Container name "PRE-EVALUATION ASSERTIONS (before any Round 2 construct
evaluation begins)" satisfies C-25 (temporal form present) and C-26 (container is first
element under Round 2 heading, zero intervening content). Expected score: 148/148 ceiling.

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
Generic "API limit" or "service limit" does not pass.

**GATE 1:** All TABLE 1 rows have (a) exact PA construct type, (b) numeric limit with
unit, (c) request contribution with arithmetic. Block: PHASE 2 is blocked until met.
Flag incomplete rows with `?`.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass.)*

**Section 2.A — Rate Limit Hit Ordering**

> "[Component] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] because [reason]. The naive assumption that limits are independent
> fails here because [cascade / shared-principal link]."

**TABLE 2 — Hit Order**

| Hit order | Construct | Limit | Why this order holds at scenario volume |
|-----------|-----------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Min 2 hops. Trace to terminal state.

**Section 2.C — UX Map**

**TABLE 4 — UX per Throttle Tier**

| Throttle tier | System action | User-visible experience | UX category |
|---------------|---------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
UX categories must differ across tiers.

**GATE 2:** TABLE 3 >= 2 hops, TABLE 4 >= 2 tiers with distinct UX, TABLE 2 "why" filled.
Block: PHASE 3 blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass.)*

**Section 3.A — Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location | Peak rate | Why it bypasses tier-1 guard |
|----------------|------------------|----------|-----------|------------------------------|

**Section 3.B — Retry-After Gaps**

**TABLE 6 — Retry-After Gaps**

| Consumer | 429 location | Retry-After read? | Backoff behavior | Failure mode |
|----------|-------------|------------------|-----------------|-------------|

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Label | Tier A | Mechanism | Load to Tier B | Tier B | Failure mode | Severity | Duration |
|-------|--------|-----------|----------------|--------|--------------|----------|---------|

Min 2 cascade pairs.

**GATE 3:** TABLE 7 >= 2 complete pairs. Block: PHASE 4 blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass.)*

**Section 4.A — PA Construct Validation**

**TABLE 8 — PA Construct Precision Pass**

| Construct | Confirmed / corrected | Correction reason | Precision note |
|-----------|-----------------------|------------------|----------------|

**Section 4.B — UX Validation**

Review TABLE 4. Internal system state is not user experience. Correct conflations.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume | Status | Headroom / Deficit |
|-----------|-------|-----------------|--------|--------------------|

Show arithmetic for >= 1 row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding | PA feature (exact name) | Configuration | Effect |
|---------|------------------------|---------------|--------|

Min 2 PA-native remediations. Each maps to a specific TABLE 5-7 finding by label.

**Section 4.E — Monitoring Signals**

At least one PA-observable signal with the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

At least one entitlement boundary with material limit difference and scenario impact.

**Section 4.G — Test Approach**

At least one concrete PA test step with a specific method named.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or cascade
labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Exact documented term or imprecise paraphrase?

2. **Numeric limit precision:** Documented platform limit or derived estimate? State source.

3. **Rate unit precision:** Confirm unit matches construct's documented enforcement
   granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural (names signal path + load calculation) or
   qualitative? Promote qualitative to structural using TABLE 9 arithmetic.

2. **Load-added precision:** Numeric projection or directional? Compute from TABLE 9.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check | Finding | Correction |
|------------------------|----------------|---------|------------|

---

*End of V-03 prompt body.*

---

## V-04 — Imperative Boundary-Event Form (Combined: Imperative Phrase + Heading Immediacy)

**Axis (combined):** Imperative boundary-event form ("execute before entering X") in
container name + round-head immediacy confirmed
**Hypothesis:** Container name "PRE-EVALUATION DIRECTIVES (execute before entering Round 2
evaluation)" satisfies C-25 via the imperative form ("execute before entering X" variant)
and C-26 via heading-to-container adjacency. This confirms that both temporal ("before X
begins") and imperative ("execute before entering X") forms satisfy C-25. Expected score:
148/148 ceiling.

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

**Domain rule:** PA construct types: Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. Generic labels do not pass.

**GATE 1:** All TABLE 1 rows have (a) exact PA construct type, (b) numeric limit with
unit, (c) request contribution arithmetic. Block: PHASE 2 blocked. Flag gaps with `?`.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass.)*

**Section 2.A — Rate Limit Hit Ordering**

> "[Component] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] because [reason]. The naive assumption that limits are independent
> fails here because [cascade / shared-principal link]."

**TABLE 2 — Hit Order**

| Hit order | Construct | Limit | Why this order holds at scenario volume |
|-----------|-----------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Min 2 hops to terminal state.

**Section 2.C — UX Map**

**TABLE 4 — UX per Throttle Tier**

| Throttle tier | System action | User-visible experience | UX category |
|---------------|---------------|------------------------|-------------|

UX categories must differ across tiers.

**GATE 2:** TABLE 3 >= 2 hops, TABLE 4 >= 2 distinct UX categories, TABLE 2 "why" filled.
Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass.)*

**Section 3.A — Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location | Peak rate | Why it bypasses tier-1 guard |
|----------------|------------------|----------|-----------|------------------------------|

**Section 3.B — Retry-After Gaps**

**TABLE 6 — Retry-After Gaps**

| Consumer | 429 location | Retry-After read? | Backoff behavior | Failure mode |
|----------|-------------|------------------|-----------------|-------------|

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Label | Tier A | Mechanism | Load to Tier B | Tier B | Failure mode | Severity | Duration |
|-------|--------|-----------|----------------|--------|--------------|----------|---------|

Min 2 cascade pairs.

**GATE 3:** TABLE 7 >= 2 complete pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass.)*

**Section 4.A — PA Construct Validation**

**TABLE 8 — PA Construct Precision Pass**

| Construct | Confirmed / corrected | Correction reason | Precision note |
|-----------|-----------------------|------------------|----------------|

**Section 4.B — UX Validation**

Review TABLE 4. Correct internal-system-state conflations with user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume | Status | Headroom / Deficit |
|-----------|-------|-----------------|--------|--------------------|

Arithmetic required for >= 1 row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding | PA feature (exact name) | Configuration | Effect |
|---------|------------------------|---------------|--------|

Min 2 PA-native, each mapped to a specific finding.

**Section 4.E — Monitoring Signals**

At least one PA signal with condition surfaced.

**Section 4.F — License and Entitlement Boundary**

At least one boundary with material limit difference and scenario volume impact.

**Section 4.G — Test Approach**

At least one concrete PA test step with method named.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION DIRECTIVES (execute before entering Round 2 evaluation)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or cascade
labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Exact documented term?

2. **Numeric limit precision:** Documented or estimated? State source.

3. **Rate unit precision:** Matches construct's documented enforcement granularity?

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural or qualitative? Promote using TABLE 9.

2. **Load-added precision:** Numeric or directional? Compute from TABLE 9.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check | Finding | Correction |
|------------------------|----------------|---------|------------|

---

*End of V-04 prompt body.*

---

## V-05 — Combined Double-Failure (Positional-Only + Transitional Sentence)

**Axis (combined):** Both C-25 and C-26 deliberately fail — positional-only container name
(no boundary-event phrase) plus one transitional sentence between Round 2 heading and
pre-barrier container
**Hypothesis:** V-05 fails C-25 (no boundary-event phrase) and fails C-26 (transitional
sentence between heading and container). All C-01 through C-24 criteria are preserved.
Expected score: 142/148 (6-point loss from ceiling, 3 pts each for C-25 and C-26).
This confirms that C-25 and C-26 are independent of each other: losing both costs exactly
6 pts, consistent with their separate 3-pt weights. Combined with V-01 (-3 pts, C-25
only) and V-02 (-3 pts, C-26 only), the three variations triangulate independence.

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

**Domain rule:** PA construct types: Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. Generic labels do not pass.

**GATE 1:** All TABLE 1 rows have (a) exact PA construct type, (b) numeric limit with
unit, (c) request contribution arithmetic. Block: PHASE 2 blocked. Flag gaps with `?`.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass.)*

**Section 2.A — Rate Limit Hit Ordering**

> "[Component] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] because [reason]. The naive assumption that limits are independent
> fails here because [cascade / shared-principal link]."

**TABLE 2 — Hit Order**

| Hit order | Construct | Limit | Why this order holds at scenario volume |
|-----------|-----------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Min 2 hops to terminal state.

**Section 2.C — UX Map**

**TABLE 4 — UX per Throttle Tier**

| Throttle tier | System action | User-visible experience | UX category |
|---------------|---------------|------------------------|-------------|

UX categories must differ across tiers.

**GATE 2:** TABLE 3 >= 2 hops, TABLE 4 >= 2 distinct UX, TABLE 2 "why" filled. Block:
PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass.)*

**Section 3.A — Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location | Peak rate | Why it bypasses tier-1 guard |
|----------------|------------------|----------|-----------|------------------------------|

**Section 3.B — Retry-After Gaps**

**TABLE 6 — Retry-After Gaps**

| Consumer | 429 location | Retry-After read? | Backoff behavior | Failure mode |
|----------|-------------|------------------|-----------------|-------------|

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Label | Tier A | Mechanism | Load to Tier B | Tier B | Failure mode | Severity | Duration |
|-------|--------|-----------|----------------|--------|--------------|----------|---------|

Min 2 cascade pairs.

**GATE 3:** TABLE 7 >= 2 complete pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass.)*

**Section 4.A — PA Construct Validation**

**TABLE 8 — PA Construct Precision Pass**

| Construct | Confirmed / corrected | Correction reason | Precision note |
|-----------|-----------------------|------------------|----------------|

**Section 4.B — UX Validation**

Review TABLE 4. Correct internal-system-state conflations.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume | Status | Headroom / Deficit |
|-----------|-------|-----------------|--------|--------------------|

Arithmetic required for >= 1 row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding | PA feature (exact name) | Configuration | Effect |
|---------|------------------------|---------------|--------|

Min 2 PA-native remediations, each mapped to a specific finding.

**Section 4.E — Monitoring Signals**

At least one PA signal with the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

At least one boundary with material limit difference and scenario volume impact.

**Section 4.G — Test Approach**

At least one concrete PA test step with method named.

---

## ROUND 2 — Structural Precision Pass

Round 1 produced a complete throttle impact analysis. Round 2 applies an independent
structural precision check to the constructs and cascade pairs identified above.

### PRE-EVALUATION ASSERTIONS

**Independence:** Round 1's confidence in the analysis is not evidence of Round 1's
structural precision. A thorough, coherent Round 1 output can still contain PA construct
names that are imprecise, rate units that are estimated rather than documented, or cascade
labels that are qualitative where numeric precision is required. Round 2 operates
independently of Round 1's output quality and score.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Exact documented term?

2. **Numeric limit precision:** Documented or estimated? State source.

3. **Rate unit precision:** Matches construct's documented enforcement granularity?

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural or qualitative? Promote using TABLE 9.

2. **Load-added precision:** Numeric or directional? Compute from TABLE 9.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check | Finding | Correction |
|------------------------|----------------|---------|------------|

---

*End of V-05 prompt body.*

---

## Round 7 Variation Design Notes

### Why these axes, not the R6 axes

R6 tested content-layer axes (role sequence, output format, lifecycle emphasis, register,
combined). All were inert — the structural pre-barrier block survived every content-level
perturbation. R7 must probe the two new aspirational criteria directly.

C-25 and C-26 require deliberate structural targeting:
- C-25 fails only when the container name lacks a boundary-event phrase — content axes
  cannot cause this failure because they do not touch the container name.
- C-26 fails only when intervening content appears between the Round 2 heading and the
  pre-barrier container — content axes that operate on evaluation section ordering, table
  formats, or phrasing register cannot cause this failure.

The only axes that can isolate C-25 and C-26 are: (1) container name vocabulary — does it
include a boundary-event phrase or only a positional qualifier? — and (2) heading-to-
container adjacency — is there intervening content between the heading and the container?

### Predicted score spread

| Score | Variations |
|-------|-----------|
| 148/148 | V-03, V-04 (ceiling) |
| 145/148 | V-01 (C-25 fail), V-02 (C-26 fail) |
| 142/148 | V-05 (C-25 + C-26 fail) |

This produces a three-level spread — the clearest diagnostic pattern possible for two
independent 3-point criteria. If V-05 scores 142 (not 139 or lower), it confirms C-25 and
C-26 have no additional hidden dependencies beyond what C-21 through C-24 already require.

### C-25 form disambiguation

V-03 uses temporal form: "before any Round 2 construct evaluation begins"
V-04 uses imperative form: "execute before entering Round 2 evaluation"

Both should satisfy C-25 per the rubric pass condition. If both reach 148, the rubric
confirms that either form is sufficient. If one fails, the rubric reveals a form-specificity
the v7 criterion text does not currently articulate — and R8 should probe the boundary.
