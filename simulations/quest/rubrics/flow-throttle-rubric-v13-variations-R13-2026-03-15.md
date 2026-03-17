# flow-throttle — Round 13 Variations (v13 Rubric, 184-point max)

## Variation Axes and Hypotheses

R12 confirmed that C-35 (Pre-Analysis Baseline Heading Subtitle) and C-36 (Phase-4 Anchor
Heading Evaluation-Type Subtitle) are both inert to subtitle text — any conforming content-type
or output-class subtitle satisfies each criterion. R12 V-04 introduced the two new aspirational
properties now formalized as C-37 and C-38:

- C-37 (3 pts, no preconditions): A labeled evaluator-role declaration appears within the
  barrier section, carrying an explicit label ("Role:", "Evaluator:", "Analyst:", or equivalent)
  and naming a specific evaluator persona — before the first construct-by-construct evaluative
  output line. Generic framing sentences without an explicit label do not pass.

- C-38 (3 pts, requires C-32 AND C-37): The evaluation-class term in the barrier heading
  subtitle (C-32) and the evaluator-persona term in the role label (C-37) share a semantic root
  readable without domain knowledge. The shared root closes a heading-role consistency loop:
  the heading declares the evaluation class; the role label names who performs it; the shared
  root makes each mutually confirming.

R12 V-04 scores 184/184: "Entitlement Verification" + "Platform entitlement verifier" share
root "entitlement verif*." V-01 through V-03 and V-05 all fail C-37 (no labeled declaration),
scoring at most 178/184.

**R13 design goals:**
1. Confirm C-37 is label-keyword-inert: "Evaluator:" satisfies C-37 as well as "Role:" does.
2. Establish C-38 failure boundary: C-37 PASS + heading subtitle with no shared root → C-38 FAIL.
3. Establish C-37 failure boundary: a generic framing sentence without an explicit label → C-37 FAIL.
4. Confirm C-37 + C-38 with a third semantic pair and a third label keyword ("Analyst:").
5. Confirm C-37/C-38 absence costs exactly 6 points even under surface-level variation.

Three single-axis tests (V-01, V-02, V-03), then two combination tests (V-04, V-05):

| Variation | Axis | C-37 | C-38 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Single: "Evaluator:" label keyword + same semantic pair "entitlement verif*" | PASS | PASS | 184/184 |
| V-02 | Single: "Role:" label + named persona with no shared root to heading subtitle | PASS | FAIL | 181/184 |
| V-03 | Single: Generic framing sentence — no explicit label keyword | FAIL | FAIL | 178/184 |
| V-04 | Combination: "Analyst:" keyword + new semantic pair "documentation accuracy" + phrasing register (conversational) | PASS | PASS | 184/184 |
| V-05 | Combination: No role label (generic framing) + inertia framing as secondary axis (more prominent Phase 0) | FAIL | FAIL | 178/184 |

Score spread: 184 / 181 / 178 / 184 / 178.

V-01 and V-04 confirm the 184 ceiling with distinct label keywords and distinct semantic pairs.
V-02 at 181 establishes the C-38 failure boundary: a labeled declaration present but semantically
misaligned costs exactly 3 points. V-03 and V-05 at 178 establish the C-37 failure boundary:
no labeled declaration costs exactly 6 points, and this holds regardless of surface-level
variation (phrasing register in V-04-analog; inertia emphasis in V-05).

---

## V-01 — C-37 Label Keyword Inertness: "Evaluator:" Keyword

**Axis:** C-37 label keyword — the role declaration uses "Evaluator:" instead of "Role:"
while keeping the same semantic pair ("Entitlement Verification" + "Platform entitlement
verifier" sharing root "entitlement verif*"). If C-37 is label-keyword-inert (hypothesis),
any explicit label with a named persona satisfies the criterion — not only "Role:".

**Secondary axis:** Phrasing register — directive imperative throughout ("Fill," "State,"
"Name") for consistency, no mixing of directive and descriptive forms.

Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS)
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS)
Barrier heading: `## ROUND 2 — Entitlement Verification` (C-32 PASS)
Role label: `*Evaluator: Platform entitlement verifier.*` (C-37 hypothesis: PASS)
Semantic alignment: "Entitlement Verification" + "Platform entitlement verifier" share
"entitlement verif*" (C-38 hypothesis: PASS)

**Hypothesis:** 184/184. C-37 passes because "Evaluator:" carries an explicit label with a
named persona. C-38 passes because the semantic root is unchanged from R12 V-04. If C-37
is label-keyword-inert, this variation proves "Role:" is not the only conforming form.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. For Round 2, you will operate as a platform entitlement
verifier confirming every numeric limit against the documented entitlement tier.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Inertia Baseline

*State what the system does today under load. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume
at the scenario load. State each construct's current configuration — default settings, no
explicit throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct named above, state the limit enforced under
the current configuration and license tier. This is the inertia profile — the ceiling the
system operates under whether the team has measured it or not.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the inertia state first breaks at this volume.
Name the construct, the limit it hits, and the user-visible consequence when no mitigation
is present. This is the outcome a team accepts by doing nothing.

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic "API
limit" does not pass. Use exact PA documentation terms.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type from the domain list, (b)
numeric limit with unit, (c) request contribution estimate with arithmetic shown. Rows with
missing fields receive a `?` flag. Block: PHASE 2 is blocked until every row satisfies all
three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck? Reference
the baseline failure point from Phase 0.*

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
Categories MUST differ across tiers. State what the user sees, not what the system does.

*Anchor to baseline: mark which TABLE 4 row represents the inertia state's outcome.*

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation per row. Block: PHASE 3
is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each loop with no concurrency cap, parallel branches with unbounded fan-out,
high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. If none
found, write explicit acknowledgment with current guards in place.

*Anchor to baseline: are these burst paths present and unguarded in the Phase 0 inertia state?*

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

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, mechanism stated,
severity assessed.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center observed),
LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2 audit. "Confirmed" requires
the exact PA documentation name — not a paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct the UX category against PA runtime
behavior. Internal system behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] →
[saturation or headroom]." Qualitative assessment without numeric projection does not pass.

*Anchor to baseline: mark each TABLE 9 row that would be OVER-LIMIT in the inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs. "Add retries" and "reduce load" do
not count. Each remediation must map to a specific finding from Phases 2–3 by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition each
signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State
the impact on this scenario's volume: does the entitlement change shift any TABLE 9 row from
SAFE to OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling with an observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model — however arithmetically grounded — is
not evidence of entitlement accuracy. The scenario model's TABLE 1 numeric limits may be
sourced from community data, admin center observations, or estimated from runtime behavior.
The internal arithmetic consistency of Round 1 does not confirm that any limit matches the
Microsoft-published documented value for the scenario's license tier. Round 2's evaluator
mandate operates independently of Round 1's model: every numeric limit and PA construct name
is evaluated against published entitlement documentation regardless of Round 1 confidence
assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are now in scope for Round 2 entitlement evaluation.

---

*Evaluator: Platform entitlement verifier.*

For each TABLE 8 row, apply entitlement verification:

1. **Documentation source:** Is the numeric limit sourced from Microsoft Power Platform
   documentation, connector certification pages, or admin center observed values? State the
   specific source. "Generally known limit" does not pass.

2. **License-tier match:** Confirm the limit applies to the scenario's entitlement tier
   (per-user plan / per-flow plan / Office 365 included / premium). A limit from a mismatched
   tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Confirm the unit matches the construct's documented enforcement
   granularity (per-minute / per-second / per-24-hours / per-user / per-environment).

For each cascade pair in TABLE 7, apply documentation checks:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or
   inferred? Inferred mechanisms require explicit flagging and a verification path.

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential? Justify HIGH severity where Tier B has significant headroom.

**TABLE 11 — Round 2 Entitlement Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

## V-02 — C-38 Failure Boundary: Semantic Mismatch

**Axis:** C-38 failure boundary — the barrier carries a labeled evaluator-role declaration
(C-37 PASS) but the role label's persona does not share a semantic root with the barrier
heading subtitle. If C-38 requires the shared semantic root (not merely C-37's presence),
this variation scores 181/184: +3 from C-37, 0 from C-38.

**Role label:** `*Role: Capacity ceiling analyst.*`
**Barrier heading subtitle:** "Entitlement Verification" (C-32 PASS)
**Semantic alignment check:** "Entitlement Verification" + "Capacity ceiling analyst" —
no shared root. "Entitlement" does not appear in the role label; "capacity" does not appear
in the heading subtitle. C-38 fails.

Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS)
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS)

**Hypothesis:** 181/184. C-37 passes — "Role:" is an explicit label and "Capacity ceiling
analyst" names a specific evaluator persona. C-38 fails — the heading subtitle names an
entitlement class; the role label names a capacity persona; no shared semantic root exists.
All C-01–C-36 are unaffected: the role label text does not interact with the construct
inventory, gate structure, cascade tables, or barrier container chain. This variation
establishes that C-38 cannot be satisfied by C-37 alone — semantic root overlap is required.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. For Round 2, you will operate as a capacity ceiling
analyst reviewing the throttle model against documented entitlement constraints.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Inertia Baseline

*State what the system does today under load. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume
at the scenario load. State each construct's current configuration — default settings, no
explicit throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct named above, state the limit enforced under
the current configuration and license tier. This is the inertia profile — the ceiling the
system runs against whether or not the team has measured it.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the inertia state first breaks at this volume.
Name the construct, the limit it hits, and the user-visible consequence with no mitigation.
This is the outcome a team accepts by doing nothing.

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types must be drawn from: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs.
standard connector tiers, Microsoft 365 service protection limits. Generic "API limit" does
not pass. Use exact PA documentation terms.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type, (b) numeric limit with unit,
(c) request contribution estimate with arithmetic shown. Block: PHASE 2 is blocked until
every row satisfies all three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck? Reference
the baseline failure point from Phase 0.*

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
two hops. Trace until terminal state.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers. State what the user sees, not internal system action.

*Anchor to baseline: mark which TABLE 4 row represents the inertia state's outcome.*

**GATE 2:** TABLE 3 >= 2 complete hops AND TABLE 4 >= 2 tiers with distinct UX categories
AND TABLE 2 ordering rationale per row. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch misconfigurations. If none,
name current guards in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two pairs with distinct Tier A / Tier B constructs, mechanism stated, severity
assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 is blocked until GATE 3
passes.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center), LOW
(runtime estimate). Flag MEDIUM or LOW for Round 2 audit.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
state is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

*Anchor to baseline: mark TABLE 9 rows that would be OVER-LIMIT in the inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings from Phases 2–3 by section
label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition, trigger, and when it fires in this
scenario.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material capacity impact. State which TABLE 9
row shifts status if the entitlement tier changes.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step with an observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model is not evidence of entitlement accuracy.
The model's TABLE 1 numeric limits may be sourced from community data, admin center
observations, or estimated from runtime behavior. Internal arithmetic consistency does not
confirm that any limit matches the Microsoft-published documented value for the scenario's
license tier. Round 2's analyst mandate operates independently: every numeric limit and PA
construct name is evaluated against published entitlement documentation regardless of Round 1
confidence assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are now in scope for Round 2 entitlement verification.

---

*Role: Capacity ceiling analyst.*

For each TABLE 8 row, apply entitlement verification:

1. **Documentation source:** Is the numeric limit sourced from Microsoft Power Platform
   documentation, connector certification pages, or admin center observed values? State the
   specific source.

2. **License-tier match:** Confirm the limit applies to the scenario's entitlement tier.
   A limit from a mismatched tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Confirm the unit matches the construct's documented enforcement
   granularity (per-minute / per-second / per-24-hours / per-user / per-environment).

For each cascade pair in TABLE 7, apply documentation checks:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or
   inferred? Inferred mechanisms require explicit flagging and a verification path.

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential?

**TABLE 11 — Round 2 Entitlement Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

## V-03 — C-37 Failure Boundary: Generic Framing Sentence

**Axis:** C-37 failure boundary — the barrier carries a generic framing sentence where a
labeled declaration would appear, but the sentence has no explicit label keyword and does
not name a specific evaluator persona. If C-37 requires the explicit label (hypothesis),
generic framing fails and the variation scores 178/184.

**Framing sentence (replacing the role label):**
`*This section applies documentation-standard verification to all construct limits from
Round 1 before issuing findings.*`

**C-37 analysis:** The sentence is a contextual orienter, not a labeled declaration. No
"Role:", "Evaluator:", or "Analyst:" keyword. No named evaluator persona. A reader knows
that verification is happening but cannot identify the declared evaluator. The C-37 pass
condition requires explicit label + named persona — this satisfies neither.

Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS)
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS)
Barrier heading: `## ROUND 2 — Entitlement Verification` (C-32 PASS)

**Hypothesis:** 178/184. C-37 fails — framing sentence lacks explicit label keyword.
C-38 fails by C-37 dependency. All C-01–C-36 pass: the absence of a labeled declaration
does not affect construct inventory, gate structure, or barrier container chain. This
variation establishes that "This section applies X verification" phrasing is not a
conforming C-37 form even when semantically adjacent to the heading subtitle's evaluation
class.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. For Round 2, apply documentation-standard verification
across all construct limits established in Round 1.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Inertia Baseline

*State what the system does today under load. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume
at the scenario load. State each construct's current configuration — default settings, no
explicit throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct named above, state the limit enforced under
the current configuration and license tier. This is the inertia profile the system operates
under whether the team is aware of it or not.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the inertia state first breaks at this volume.
Name the construct, the limit it hits, and the user-visible consequence with no mitigation.
This is the outcome a team accepts by doing nothing.

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types must be drawn from: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs.
standard connector tiers, Microsoft 365 service protection limits. Generic "API limit" does
not pass. Use exact PA documentation terms.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type, (b) numeric limit with unit,
(c) request contribution estimate with arithmetic shown. Block: PHASE 2 blocked until all
rows satisfy all three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [cascade chain or shared principal pool linkage]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck?*

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
two hops. Terminal state: user-visible error, flow run failure, or silent drop.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers.

*Anchor to baseline: mark which TABLE 4 row represents the inertia state's outcome.*

**GATE 2:** TABLE 3 >= 2 complete hops AND TABLE 4 >= 2 tiers with distinct UX categories
AND TABLE 2 ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch misconfigurations. If none,
name current guards in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two pairs. Distinct Tier A / Tier B. Mechanism stated. Severity assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center), LOW
(runtime estimate). Flag MEDIUM or LOW for Round 2 audit.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
state is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

*Anchor to baseline: mark TABLE 9 rows that would be OVER-LIMIT in the inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings from Phases 2–3 by section
label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition, trigger, and when it fires.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material capacity impact. State which TABLE 9
row shifts status if the entitlement tier changes.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step with an observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model is not evidence of entitlement accuracy.
The scenario model's TABLE 1 numeric limits may be sourced from community data, admin center
observations, or estimated from runtime behavior. Internal arithmetic consistency does not
confirm that any limit matches the Microsoft-published documented value for the scenario's
license tier. Round 2 operates independently: every numeric limit and PA construct name is
evaluated against published entitlement documentation regardless of Round 1 confidence
assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are now in scope for Round 2 evaluation.

---

*This section applies documentation-standard verification to all construct limits from
Round 1 before issuing findings.*

For each TABLE 8 row, apply entitlement verification:

1. **Documentation source:** Is the numeric limit sourced from Microsoft Power Platform
   documentation, connector certification pages, or admin center observed values? State the
   specific source.

2. **License-tier match:** Confirm the limit applies to the scenario's entitlement tier.
   A limit from a mismatched tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair in TABLE 7, apply documentation checks:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or
   inferred?

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential?

**TABLE 11 — Round 2 Entitlement Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

## V-04 — Combination: "Analyst:" Keyword + "Documentation Accuracy" Semantic Pair + Conversational Register

**Axes:** (1) C-37 with "Analyst:" label keyword — a third label form after "Role:" (V-01,
V-02, V-03) and "Evaluator:" (V-01). (2) C-38 with a third semantic pair: barrier heading
"Documentation Accuracy Review" + role label "Documentation accuracy analyst" sharing root
"documentation accuracy." (3) Secondary axis: phrasing register — conversational rather
than directive imperative; sections use descriptive framing ("your task here is to...") over
command verbs ("Fill," "State," "Name").

**Role label:** `*Analyst: Documentation accuracy analyst.*`
**Barrier heading:** `## ROUND 2 — Documentation Accuracy Review` (C-32 PASS)
**Semantic root:** "documentation accuracy" shared across heading and role label (C-38 PASS)

Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS)
Phase 4 heading: `### PHASE 4 — Remediation Registry and Throttle Budget Corrections`
(C-36 PASS — "Remediation Registry" is a confirmed output-class subtitle from C-36 examples)

**Hypothesis:** 184/184. C-37 passes — "Analyst:" is an explicit label carrying a named
persona; the criterion is label-keyword-inert. C-38 passes — "documentation accuracy" is
a shared semantic root readable without domain knowledge. C-35 and C-36 pass — the Phase 0
and Phase 4 headings carry content-type and output-class subtitles, respectively, using
confirmed passing forms. C-01–C-36 are unaffected: phrasing register variation does not
interact with construct types, gate logic, cascade pairs, or barrier container structure.
This variation confirms C-37 label-keyword inertness using a third distinct label form and
confirms C-38 semantic-root inertness using a third distinct semantic pair.

---

You are a Connectors / Power Automate throughput domain expert. Your task in this simulation
is to trace how request volume moves through a rate-limited Power Automate system until it
breaks. Start by describing what the system does today — the inertia state — then work
forward through the throttle tier stack to find where ceilings are hit, how pressure
propagates, and what users actually experience at each limit tier. Round 2 shifts to
documentation accuracy: you'll review every construct limit in the Round 1 model against
published entitlement sources.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Inertia Baseline

*Describe the system as it currently operates under load, before any throttle mitigations
are applied.*

**Current construct stack:** Your goal here is to enumerate every PA construct in the flow
that carries meaningful request volume at the scenario load level. For each construct,
describe the current configuration — assume default settings, no explicit throttle handling,
no backpressure controls, no concurrency limits deliberately applied.

**Active limits in effect:** For each construct you named, identify the enforced limit that
applies under the current configuration and license tier. This is the operational ceiling
the system is already working against, whether or not the team knows it.

**Baseline operational conditions:** Describe the scenario's request volume, trigger
frequency, and principal context (per-user plan, per-flow plan, or environment-level).
These numbers anchor all downstream projections.

**Baseline failure point:** Identify where things break first at this volume. Which
construct hits its limit, what is that limit, and what does the user experience when there
is no mitigation in place? This is the do-nothing outcome — the scenario's current
failure mode.

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Your goal in Phase 1 is to map every throttle-relevant construct to its enforced limit and
estimate the request volume it handles at the scenario load. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain constraint:** PA construct types must come from one of the following: Power
Platform request entitlements, connector throttling policies, flow run concurrency limits,
action call limits, premium vs. standard connector tiers, Microsoft 365 service protection
limits. "API limit" or "service limit" without the exact PA documentation term does not pass.

**GATE 1:** Every TABLE 1 row must have (a) an exact PA construct type from the list above,
(b) a numeric limit with unit, and (c) a request contribution estimate showing arithmetic.
Rows missing any field get a `?` flag and must be corrected before Phase 2 opens.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Identify the binding bottleneck and explain why it saturates first at this volume:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [cascade chain or shared principal pool linkage]."

*Connect this back to Phase 0: how does the inertia baseline reach this specific construct
first? The Phase 0 failure point and the Phase 2 bottleneck should be the same or you
should explain why they differ.*

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

Trace how throttle pressure moves through the system once the bottleneck saturates. Fill
TABLE 3.

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. You need at
least two hops. Trace until you reach a terminal state — user-visible error, flow run
failure, or silent drop.

**Section 2.C — User Experience per Throttle Tier**

For each throttle tier, describe what the user actually experiences. Fill TABLE 4.

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories available: transparent-retry / visible-delay / error-surfaced / silent-loss.
Each tier must have a different category — if two tiers produce the same UX, your tier
definition is too coarse. Describe what the user sees, not what the system does internally.

*Mark which TABLE 4 row corresponds to the inertia state's outcome from Phase 0.*

**GATE 2:** TABLE 3 needs at least two complete hops. TABLE 4 needs at least two tiers with
distinct UX categories. TABLE 2 needs an ordering rationale for each row. Phase 3 is blocked
until all three conditions are met.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

Find flow constructs that can generate uncapped request bursts. Fill TABLE 5.

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Look for: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out,
high-frequency triggers with no debounce, nested loops, batch-size misconfigurations. If
the flow genuinely has no unprotected burst paths, name the guards that are currently in
place to justify that claim.

*Are these burst paths present and unguarded in the Phase 0 inertia state?*

**Section 3.B — Retry-After Gap Table**

For each consumer that could receive a 429, identify whether it reads and respects the
Retry-After header. Fill TABLE 6.

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. You need at least one gap.
If every consumer correctly honors Retry-After, explain why — that is a rare finding.

**Section 3.C — Cascade Risk Pairs**

Identify pairs of constructs where the throttling of one generates additional load on the
other. Fill TABLE 7.

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

You need at least two pairs. Tier A and Tier B must be different constructs. State the
mechanism linking them and your severity assessment.

**GATE 3:** TABLE 7 needs at least two complete cascade pairs with all fields filled.
Phase 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Remediation Registry and Throttle Budget Corrections

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Go back through every construct in TABLE 1 and verify the PA construct name is exact.
Fill TABLE 8.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence levels: HIGH (directly from Microsoft documentation), MEDIUM (community source
or admin center observed), LOW (estimated from runtime). Flag MEDIUM and LOW rows — they
will be re-examined in Round 2.

**Section 4.B — UX Validation**

Go back through TABLE 4. For each tier, write one sentence confirming or correcting the
UX category based on what PA actually does at runtime. Remember: internal system state
is not user experience.

**Section 4.C — Quantified Risk Register**

Build the throttle budget. Fill TABLE 9.

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status must be SAFE, MARGINAL, or OVER-LIMIT. Show your arithmetic for at least the
binding bottleneck row: "[N items] x [M connector calls] = [total req], against [limit
req/unit] → [saturation or headroom]."

*Mark each TABLE 9 row that would be OVER-LIMIT in the inertia state from Phase 0.*

**Section 4.D — PA-Specific Remediations**

For each finding from Phases 2–3, identify the PA-native feature that addresses it.
Fill TABLE 10.

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

You need at least two remediations using PA-native constructs. "Add retries" and "reduce
load" are not PA features — name the specific PA construct and configuration.

**Section 4.E — Monitoring Signals**

Identify at least one observable PA signal for detecting throttle events: flow run history
throttle status, connector call telemetry in Power Platform admin center, or the request
usage dashboard. For each signal, describe the condition it surfaces and when it would fire
in this scenario.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit changes materially. Identify
which TABLE 9 row would shift status if the scenario's license tier changed.

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling. The test must produce an
observable pass/fail result — not just "test in staging."

---

## ROUND 2 — Documentation Accuracy Review

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle model — however arithmetically grounded — is not
evidence of documentation accuracy. The model's TABLE 1 numeric limits may come from
community sources, admin center observations, or runtime estimates. The internal consistency
of Round 1's arithmetic does not confirm that any limit matches the Microsoft-published
documented value for the scenario's license tier. Round 2 evaluates every numeric limit and
PA construct name against published sources, independent of what Round 1 said.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are in scope for Round 2 documentation accuracy evaluation.

---

*Analyst: Documentation accuracy analyst.*

For each TABLE 8 row, evaluate documentation accuracy:

1. **Documentation source:** Where is this numeric limit documented? Cite a specific source
   — Microsoft Power Platform documentation, connector certification page, or admin center
   observed value. "Generally known limit" does not pass.

2. **License-tier match:** Does this limit apply to the scenario's entitlement tier
   (per-user plan / per-flow plan / Office 365 included / premium)? A limit from a
   mismatched tier is a documentation error regardless of whether the number looks right.

3. **Rate unit source:** Does the unit match the construct's documented enforcement
   granularity (per-minute / per-second / per-24-hours / per-user / per-environment)?
   Unit mismatches are documentation errors.

For each cascade pair in TABLE 7, evaluate documentation accuracy:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior, or
   is it inferred from observed behavior? Inferred mechanisms need explicit flagging and a
   path to verification.

2. **Severity calibration:** Does the severity rating hold up against the documented limit
   differential between Tier A and Tier B?

**TABLE 11 — Round 2 Documentation Accuracy Review**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

## V-05 — Combination: No Role Label + Prominent Inertia Framing

**Axes:** (1) No labeled role declaration in the barrier — C-37 fails (generic framing
sentence used). (2) Secondary axis: inertia framing — Phase 0 receives more prominent
treatment with a dedicated "do-nothing outcome" subsection and an explicit link to the
status-quo competitor (SharePoint + manual processing) that the flow would replace. The
enhanced Phase 0 tests that inertia framing depth is inert to C-37/C-38: a more developed
inertia section does not substitute for a labeled role declaration at the barrier.

**Barrier framing sentence:** `*Round 2 examines every numeric limit from TABLE 8 against
its documented entitlement source.*` (generic — no explicit label, no named evaluator)

Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS — same confirmed subtitle)
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS)
Barrier heading: `## ROUND 2 — Entitlement Verification` (C-32 PASS)

**Hypothesis:** 178/184. C-37 fails — barrier framing sentence carries no explicit label
keyword and names no evaluator persona. C-38 fails by C-37 dependency. C-35 PASS — Phase 0
heading carries "Inertia Baseline" subtitle. C-36 PASS — Phase 4 heading carries "Capacity
Synthesis and PA Validation." This variation confirms that inertia framing depth is not a
substitute for the C-37 labeled declaration and that the absence of C-37/C-38 costs exactly
6 points even when Phase 0 content is significantly more developed.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. The starting point is inertia: what the system does
today, why that fails at scale, and what adopting this flow would change versus the
do-nothing baseline. Then trace through the throttle tier stack to identify every bottleneck,
backpressure chain, and exposure. Round 2 verifies the numeric limits against documented
entitlement sources.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Inertia Baseline

*Establish the full inertia picture: what the organization does today (the status-quo
process), why it cannot scale, and what the proposed flow changes — before any throttle
mitigation is analyzed.*

**Status-quo process:** Describe what the organization currently does without this flow.
Name the manual process, the tools in use (likely SharePoint, Outlook, or manual data
entry), and the human steps involved. This is the inertia competitor — the process the
team will abandon if this flow is adopted.

**Inertia failure mode at scale:** At the scenario's request volume, where does the
status-quo process break? State the volume, the process step that cannot keep up, and
the user-visible consequence. This is what the flow is supposed to fix.

**Current construct stack:** Name every PA construct in the proposed flow that carries
request volume at the scenario load. State each construct's current configuration —
default settings, no explicit throttle handling, no backpressure controls, no concurrency
caps applied.

**Active limits in effect:** For each construct named above, state the enforced limit
under the current configuration and license tier. This is the throttle ceiling the flow
operates under from the moment it is deployed.

**Baseline operational conditions:** State the scenario's request volume, trigger
frequency, and principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Where does the proposed flow fail first at this volume? Name
the construct, the limit it hits, and the user-visible consequence with no mitigation
in place. Compare this explicitly to the status-quo failure mode: is the flow's failure
mode better, worse, or different?

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types must be drawn from: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs.
standard connector tiers, Microsoft 365 service protection limits. Generic "API limit" does
not pass. Use exact PA documentation terms.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type from the domain list, (b)
numeric limit with unit, (c) request contribution estimate with arithmetic shown. Block:
PHASE 2 is blocked until every row satisfies all three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [cascade chain or shared principal pool linkage]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck? Is this
the same construct as the Phase 0 baseline failure point?*

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
two hops. Trace until terminal state.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers. Compare the flow's UX failure modes to the inertia
state's user experience where applicable.

*Mark which TABLE 4 row represents the inertia state's outcome.*

**GATE 2:** TABLE 3 >= 2 complete hops AND TABLE 4 >= 2 tiers with distinct UX categories
AND TABLE 2 ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch misconfigurations. If none,
name current guards in place.

*Are these burst paths present and unguarded in the Phase 0 inertia state?*

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two pairs. Distinct Tier A / Tier B. Mechanism stated. Severity assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center), LOW
(runtime estimate). Flag MEDIUM or LOW for Round 2 audit.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
state is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

*Mark each TABLE 9 row that would be OVER-LIMIT in the inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings from Phases 2–3 by section
label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition, trigger, and when it fires.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material capacity impact. State which TABLE 9
row shifts status if the entitlement tier changes.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step with an observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model is not evidence of entitlement accuracy.
The model's TABLE 1 numeric limits may be sourced from community data, admin center
observations, or estimated from runtime behavior. Internal arithmetic consistency does not
confirm that any limit matches the Microsoft-published documented value for the scenario's
license tier. Round 2 operates independently: every numeric limit and PA construct name is
evaluated against published entitlement documentation regardless of Round 1 confidence
assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are now in scope for Round 2 entitlement verification.

---

*Round 2 examines every numeric limit from TABLE 8 against its documented entitlement
source.*

For each TABLE 8 row, apply entitlement verification:

1. **Documentation source:** Is the numeric limit sourced from Microsoft Power Platform
   documentation, connector certification pages, or admin center observed values? State the
   specific source.

2. **License-tier match:** Confirm the limit applies to the scenario's entitlement tier.
   A limit from a mismatched tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair in TABLE 7, apply documentation checks:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or
   inferred?

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential?

**TABLE 11 — Round 2 Entitlement Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|
