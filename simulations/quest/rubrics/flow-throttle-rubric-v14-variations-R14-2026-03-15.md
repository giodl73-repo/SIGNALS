# flow-throttle — Round 14 Variations (v14 Rubric, 190-point max)

## Variation Axes and Hypotheses

R13 confirmed C-39 (barrier three-anchor completeness: C-31 ∩ C-32 ∩ C-37 simultaneously) as a
uniform ceiling property across all five R13 variations. C-40 (Phase 0 tabular baseline encoding)
was the sole R13 discriminator: V-05 at 190/190 carried a TABLE in Phase 0; V-01–V-04 at 187/190
used prose-only Phase 0 content regardless of axis (label keyword, phrasing register, heading form,
semantic alignment phrasing, inertia depth).

**R13 meta-findings carried into R14:**
- C-37 is label-keyword-inert: "Role:", "Evaluator:", "Analyst:" are all conforming forms.
- C-38 is keyword-inert: semantic root alignment tests heading subtitle and persona name terms, not
  the label keyword.
- C-39 is a stable barrier-level property: ASSERTIONS container (C-31) + evaluation-type heading
  subtitle (C-32) + labeled evaluator declaration (C-37) held uniformly across all five R13 content
  axes.
- C-40 minimum-TABLE criterion: prose-only or bullet-only Phase 0 fails regardless of depth or
  heading form.

**R14 design goals:**
1. Make C-40 uniform: all five variations carry a TABLE in Phase 0, confirming C-40 is a stable
   property independent of surface variation.
2. Explore Round-1 evaluator-role structure: does a labeled evaluator-role declaration at Round 1
   (not Round 2) operate as a structurally distinct property?
3. Explore Phase 0 TABLE schema depth: does a richer Phase 0 TABLE (expanded columns, forward
   cross-reference to TABLE 1) constitute a property distinct from C-40's minimum-TABLE requirement?
4. Confirm Phase 0 TABLE inertness to phrasing register: strict directive phrasing throughout
   should be inert to C-40.
5. Ceiling variation: introduce a structural analog to Round 2's PRE-EVALUATION ASSERTIONS
   container at Round 1 — a labeled container before Phase 0 naming the mechanism type of the
   Round 1 analysis, paralleling C-31 at Round 1 level.

Three single-axis tests (V-01, V-02, V-03), then two combination tests (V-04, V-05):

| Variation | Axis | C-39 | C-40 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Single: Round-1 labeled evaluator-role declaration (before Phase 0) | PASS | PASS | 190/190 |
| V-02 | Single: Phase-0 TABLE expanded schema — PA construct type + forward-reference column | PASS | PASS | 190/190 |
| V-03 | Single: Phrasing register — formal/technical directive imperative throughout | PASS | PASS | 190/190 |
| V-04 | Combination: Role sequence (Round-1 label) + Inertia framing (status-quo competitor prominent) | PASS | PASS | 190/190 |
| V-05 | Ceiling: Round-1 PRE-ANALYSIS SCENARIO MODEL container + Round-1 evaluator-role label | PASS | PASS | 190/190 |

Score spread under v14: 190/190 across all variations. C-39 and C-40 are both uniform. V-05
introduces a new structural property not yet formalized as a criterion — the Round-1 container with
mechanism-type declaration and evaluator-role label, structurally parallel to C-31 and C-37 at
Round 2.

---

## V-01 — Role Sequence: Round-1 Labeled Evaluator-Role Declaration

**Axis:** Role sequence — a labeled evaluator-role declaration appears at Round 1 (immediately after
the `## ROUND 1` heading, before Phase 0 content), paralleling the C-37 role label at Round 2. The
Round-1 label is `*Lead analyst: Throttle capacity modeler.*`. This tests whether the role-declaration
structure can exist symmetrically at both rounds, and whether Round-1 role labeling is inert to
C-01–C-40 (hypothesis: yes — it adds a new layer without displacing any prior structural element).

**Secondary axis:** "Evaluator:" keyword at Round 2, confirming C-37 label-keyword inertness.

Round-1 role label: `*Lead analyst: Throttle capacity modeler.*` (new structural property — no criterion yet)
Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS)
Phase 0 TABLE: present — 3-column baseline state register (C-40 PASS)
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS)
Barrier heading: `## ROUND 2 — Entitlement Verification` (C-32 PASS)
Container header: `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` (C-31 PASS)
Barrier role label: `*Evaluator: Platform entitlement verifier.*` (C-37 PASS — "Evaluator:" keyword)
Semantic alignment: "Entitlement Verification" + "Platform entitlement verifier" → "entitlement verif*" (C-38 PASS)
C-39: C-31 ∩ C-32 ∩ C-37 simultaneously satisfied from the same barrier (C-39 PASS)

**Hypothesis:** 190/190. All C-01–C-40 pass. The Round-1 role label is a new structural layer not
captured by any existing criterion — inert to C-01–C-40 but a potential C-41 candidate.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Lead analyst: Throttle capacity modeler.*

### PHASE 0 — Inertia Baseline

*State what the system does today under load. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume at
the scenario load. State each construct's current configuration — default settings, no explicit
throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct named above, state the limit enforced under the
current configuration and license tier. This is the inertia profile — the ceiling the system
operates under whether the team has measured it or not.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency, and
principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the inertia state first breaks at this volume. Name
the construct, the limit it hits, and the user-visible consequence when no mitigation is present.
This is the outcome a team accepts by doing nothing.

**TABLE 0 — Inertia State Register**

| Construct | Enforced limit | Operational condition |
|-----------|---------------|----------------------|
| (fill) | (N req/unit — license tier) | (trigger frequency, principal context, default config) |

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. Generic "API limit" does not pass. Use
exact PA documentation terms.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type from the domain list, (b) numeric
limit with unit, (c) request contribution estimate with arithmetic shown. Rows with missing fields
receive a `?` flag. Block: PHASE 2 is blocked until every row satisfies all three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck. It
> saturates at [N req/unit-time] under this scenario because [reason the ordering holds at
> this aggregate volume]. The naive assumption that limits are independent fails here because
> [one sentence linking to cascade chain or shared principal pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck? Reference the
baseline failure point from TABLE 0.*

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops.
Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories MUST
differ across tiers. State what the user sees, not what the system does.

*Anchor to baseline: mark which TABLE 4 row represents the inertia state's outcome from TABLE 0.*

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX categories
AND TABLE 2 has a "why this order holds" explanation per row. Block: PHASE 3 is blocked until
GATE 2 passes.

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

*Anchor to baseline: are these burst paths present and unguarded in the TABLE 0 inertia state?*

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required. If no
gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, mechanism stated, severity
assessed.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B, mechanism
stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center observed),
LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2 audit. "Confirmed" requires the
exact PA documentation name — not a paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct the UX category against PA runtime
behavior. Internal system behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row: "[N items] x
[M connector calls] = [total req], against [limit req/unit] → [saturation or headroom]."
Qualitative assessment without numeric projection does not pass.

*Anchor to baseline: mark each TABLE 9 row that would be OVER-LIMIT in the TABLE 0 inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs. "Add retries" and "reduce load" do not
count. Each remediation must map to a specific finding from Phases 2–3 by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call telemetry
in Power Platform admin center, request usage dashboard. State the condition each signal surfaces
and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State the
impact on this scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE
to OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling with an observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model — however arithmetically grounded — is not
evidence of entitlement accuracy. The scenario model's TABLE 1 numeric limits may be sourced from
community data, admin center observations, or estimated from runtime behavior. The internal
arithmetic consistency of Round 1 does not confirm that any limit matches the Microsoft-published
documented value for the scenario's license tier. Round 2's evaluator mandate operates
independently of Round 1's model: every numeric limit and PA construct name is evaluated against
published entitlement documentation regardless of Round 1 confidence assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced imprecise
TABLE 1 entries are now in scope for Round 2 entitlement evaluation.

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

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or inferred?
   Inferred mechanisms require explicit flagging and a verification path.

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential? Justify HIGH severity where Tier B has significant headroom.

**TABLE 11 — Round 2 Entitlement Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

## V-02 — Output Format: Phase-0 TABLE Expanded Schema with Forward Reference

**Axis:** Output format — the Phase 0 TABLE uses a 5-column schema that includes (a) PA construct
type (using the same exact-term vocabulary required of TABLE 1), (b) a license-tier column, and
(c) a forward-reference column (`→ TABLE 1 row`) that maps each baseline construct row to its
Phase 1 TABLE 1 counterpart. This makes the Phase 0 → Phase 1 delta machine-addressable: each
TABLE 0 row has a declared pointer to its corresponding TABLE 1 row, and a scorer can verify
the cross-phase traceability without reading narrative prose. If this is a distinct structural
property from C-40 (which requires only that a TABLE exists in Phase 0), then the forward-reference
column constitutes a new dimension — the baseline encoding is traceable, not merely present.

Phase 0 heading: `### PHASE 0 — Current-State Inventory` (C-35 PASS — new confirmed subtitle form)
Phase 0 TABLE: 5-column schema with PA construct type + forward-reference column (C-40 PASS)
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS)
Barrier heading: `## ROUND 2 — Entitlement Verification` (C-32 PASS)
Container header: `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` (C-31 PASS)
Barrier role label: `*Role: Platform entitlement verifier.*` (C-37 PASS — standard "Role:" form)
Semantic alignment: "Entitlement Verification" + "Platform entitlement verifier" → "entitlement verif*" (C-38 PASS)
C-39: C-31 ∩ C-32 ∩ C-37 simultaneously satisfied (C-39 PASS)

**Hypothesis:** 190/190. All C-01–C-40 pass. The 5-column Phase 0 TABLE schema — particularly
the forward-reference column — is a new structural dimension not captured by C-40, which requires
only tabular encoding. Cross-phase forward referencing is a candidate for a new criterion
independent of C-40.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Round 2 verifies every numeric limit from Round 1
against its published entitlement source.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Current-State Inventory

*Establish the baseline state of the system under load before any throttle analysis begins.
No mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume at
the scenario load. State each construct's current configuration — default settings, no explicit
throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct, state the enforced limit under the current
configuration and license tier. This is the operational ceiling the system runs against from
the moment it is deployed.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the inertia state first breaks at this volume. Name
the construct, the limit it hits, and the user-visible consequence with no mitigation in place.

**TABLE 0 — Current-State Inventory**

| Construct | PA construct type | Enforced limit | License tier | → TABLE 1 row |
|-----------|------------------|---------------|--------------|---------------|
| (fill) | (exact PA term) | (N req/unit) | (per-user / per-flow / M365 / premium) | (row N) |

*Fill the `→ TABLE 1 row` column after completing TABLE 1. Each TABLE 0 row must map to the
corresponding TABLE 1 row. If a TABLE 0 construct does not appear in TABLE 1, flag it: it
is either missing from the Phase 1 inventory or out of scope at scenario volume.*

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1. Each row must correspond
to a TABLE 0 entry; the `→ TABLE 1 row` column in TABLE 0 maps to this table.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types must be drawn from: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs.
standard connector tiers, Microsoft 365 service protection limits. Generic "API limit" does
not pass. Use exact PA documentation terms.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type from the domain list, (b) numeric
limit with unit, (c) request contribution estimate with arithmetic shown. Rows with missing fields
receive a `?` flag. Block: PHASE 2 is blocked until every row satisfies all three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck. It
> saturates at [N req/unit-time] under this scenario because [reason the ordering holds at
> this aggregate volume]. The naive assumption that limits are independent fails here because
> [one sentence linking to cascade chain or shared principal pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck? The TABLE 0
baseline failure point and the Phase 2 bottleneck should match or the discrepancy must be
explained.*

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops.
Trace until terminal state.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories MUST
differ across tiers. State what the user sees, not what the system does.

*Mark which TABLE 4 row represents the TABLE 0 inertia state's outcome.*

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX categories
AND TABLE 2 has ordering rationale per row. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out), high-frequency
trigger (no debounce), nested loops, batch misconfigurations. If none, name current guards.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two pairs with distinct Tier A / Tier B constructs, mechanism stated, severity assessed.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs. Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center), LOW (runtime
estimate). Flag MEDIUM or LOW for Round 2 audit.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system state
is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

*Mark TABLE 9 rows that would be OVER-LIMIT in the TABLE 0 inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to findings from Phases 2–3 by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition, trigger, and when it fires.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material capacity impact. State which TABLE 9 row
shifts status if the entitlement tier changes.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step with an observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model is not evidence of entitlement accuracy.
The model's TABLE 1 numeric limits may be sourced from community data, admin center observations,
or estimated from runtime behavior. Internal arithmetic consistency does not confirm that any
limit matches the Microsoft-published documented value for the scenario's license tier. Round 2
evaluates every numeric limit and PA construct name against published sources, independent of
Round 1 confidence assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced imprecise
TABLE 1 entries are in scope for Round 2 entitlement evaluation.

---

*Role: Platform entitlement verifier.*

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

## V-03 — Phrasing Register: Formal/Technical Directive Imperative Throughout

**Axis:** Phrasing register — all phase instructions use strict directive imperatives with no
descriptive framing, no "your goal here is to" constructions, no parenthetical explanations within
instruction lines. Instructions are short command-form sentences. Tests phrasing-register inertness
to C-40 and the full barrier structure: a variation with maximum phrasing compression should still
pass all structural criteria.

**Secondary axis:** New barrier evaluation class ("Limit Source Verification") and new Phase 4
subtitle ("Bottleneck Correction Registry") — both from the rubric's confirmed-passing examples
list — confirming subtitle-text inertness at C-32 and C-36.

Phase 0 heading: `### PHASE 0 — Throttle Baseline` (C-35 PASS — new confirmed subtitle form)
Phase 0 TABLE: present — 3-column baseline register (C-40 PASS)
Phase 4 heading: `### PHASE 4 — Bottleneck Correction Registry` (C-36 PASS — from C-36 examples)
Barrier heading: `## ROUND 2 — Limit Source Verification` (C-32 PASS — analysis-class subtitle)
Container header: `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` (C-31 PASS)
Barrier role label: `*Analyst: Limit source verifier.*` (C-37 PASS — "Analyst:" keyword)
Semantic alignment: "Limit Source Verification" + "Limit source verifier" → "limit source verif*" (C-38 PASS)
C-39: C-31 ∩ C-32 ∩ C-37 simultaneously satisfied (C-39 PASS)

**Hypothesis:** 190/190. All C-01–C-40 pass. Confirms that phrasing compression does not affect
any structural criterion. "Throttle Baseline" is a third confirmed C-35 passing form after
"Inertia Baseline" and "Current-State Inventory." "Limit Source Verification" / "Limit source
verifier" is a fourth confirmed C-38 semantic pair.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Round 2 verifies every construct limit against its
documented source.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Throttle Baseline

State the current system state. No mitigations applied.

**Construct stack:** Name every PA construct carrying request volume at scenario load. State
current configuration — defaults only, no throttle controls applied.

**Active limits:** State the enforced limit for each construct at current configuration and
license tier.

**Operational conditions:** State request volume, trigger frequency, principal context.

**Failure point:** Name the first construct to hit its limit at this volume. State the limit
and the user-visible consequence.

**TABLE 0 — Throttle Baseline Register**

| Construct | Enforced limit | Operational condition |
|-----------|---------------|----------------------|
| (fill) | (N req/unit — license tier) | (volume, frequency, principal context) |

*Phase 0 produces no gate.*

---

### PHASE 1 — Construct Inventory

Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types from: Power Platform request entitlements, connector throttling
policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers,
Microsoft 365 service protection limits. Exact PA documentation terms only.

**GATE 1:** Every TABLE 1 row: (a) exact PA construct type, (b) numeric limit with unit,
(c) request contribution with arithmetic. Block: PHASE 2 is blocked until every row passes.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[PA construct component] at [PA construct type] is the binding bottleneck. It saturates
> at [N req/unit-time] because [ordering reason]. The naive independence assumption fails
> because [cascade chain or shared principal pool linkage]."

*Anchor to Phase 0 failure point.*

**TABLE 2 — Hit Order**

| Hit order | Construct | Limit | Why this order holds |
|-----------|-----------|-------|----------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Two hops minimum. Trace to terminal state.

**Section 2.C — UX per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action | User-visible experience | UX category |
|---------------|--------------|------------------------|-------------|

Categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Must differ across
tiers. User-visible only — no internal system state.

*Mark the TABLE 4 row corresponding to the Phase 0 inertia outcome.*

**GATE 2:** TABLE 3 >= 2 hops. TABLE 4 >= 2 tiers, distinct UX categories. TABLE 2 ordering
rationale per row. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass.)*

**Section 3.A — Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location | Peak rate | Bypass mechanism |
|----------------|------------------|----------|-----------|-----------------|

Check: Apply to Each (no cap), parallel fan-out (unbounded), high-frequency trigger (no debounce),
nested loops, batch misconfig. If none, name current guards.

**Section 3.B — Retry-After Gaps**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After read? | Backoff behavior | Failure mode |
|-------------------|-------------|------------------|-----------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A | Mechanism | Load to Tier B | Tier B | Failure mode | Severity | Duration |
|---------------|--------|-----------|----------------|--------|--------------|----------|---------|

Two pairs minimum. Distinct Tier A / Tier B. Mechanism stated. Severity assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Bottleneck Correction Registry

*(GATE 3 must pass.)*

**Section 4.A — PA Construct Validation**

Fill TABLE 8 for every TABLE 1 construct.

**TABLE 8 — PA Construct Precision Pass**

| Construct | PA construct (confirmed / corrected) | Correction reason | Confidence |
|-----------|-------------------------------------|------------------|------------|

Confidence: HIGH (Microsoft docs) / MEDIUM (community or admin center) / LOW (runtime).
Flag MEDIUM and LOW for Round 2.

**Section 4.B — UX Validation**

One sentence per TABLE 4 tier: confirm or correct UX category. Internal state is not UX.

**Section 4.C — Throttle Budget**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume | Status | Headroom / Deficit |
|-----------|-------|-----------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

*Mark TABLE 9 rows OVER-LIMIT in the Phase 0 baseline.*

**Section 4.D — Remediations**

**TABLE 10 — Remediations**

| Finding (section ref) | PA feature (exact name) | Configuration | Effect |
|----------------------|------------------------|--------------|--------|

Two PA-native remediations minimum, each mapped to a Phase 2–3 section finding.

**Section 4.E — Monitoring Signals**

Name one PA-observable signal. State condition surfaced, trigger, when it fires.

**Section 4.F — Entitlement Boundary**

Name one boundary where the limit materially differs. Identify the TABLE 9 row that shifts
status if the license tier changes.

**Section 4.G — Test Step**

One concrete PA tooling test with observable pass/fail result.

---

## ROUND 2 — Limit Source Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's arithmetic consistency is not evidence of documentation accuracy.
TABLE 1 limits may come from community sources, admin center observations, or runtime estimates.
Round 2 verifies every limit against published sources independently of Round 1 confidence ratings.

**Scope extension:** Corrected construct names from TABLE 8 that replaced TABLE 1 entries are
in scope for Round 2 limit source verification.

---

*Analyst: Limit source verifier.*

For each TABLE 8 row:

1. **Documentation source:** Cite the specific Microsoft source for the numeric limit.
   "Generally known limit" does not pass.

2. **License-tier match:** Does this limit apply to the scenario's entitlement tier? A limit
   from a mismatched tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Does the unit match the construct's documented enforcement granularity?

For each TABLE 7 cascade pair:

1. **Mechanism documentation:** Documented platform behavior or inferred? Flag inferred
   mechanisms with a verification path.

2. **Severity calibration:** Does severity hold against the documented limit differential?

**TABLE 11 — Round 2 Limit Source Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

## V-04 — Combination: Role Sequence + Inertia Framing

**Axes:** (1) Role sequence — a labeled evaluator-role declaration appears at Round 1 (V-01
axis), using `*Lead analyst: Throttle scenario modeler.*`. (2) Inertia framing — Phase 0
explicitly names the status-quo process as the inertia competitor: the do-nothing baseline
includes not just the PA construct state but the organizational process the flow is meant
to replace. Phase 0 TABLE includes a status-quo row encoding the manual-process failure
mode alongside PA construct rows.

Round-1 role label: `*Lead analyst: Throttle scenario modeler.*` (V-01 axis)
Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS)
Phase 0 TABLE: present — 4-column schema including status-quo row (C-40 PASS)
Phase 4 heading: `### PHASE 4 — Remediation Registry and Throttle Budget Corrections` (C-36 PASS)
Barrier heading: `## ROUND 2 — Documentation Accuracy Review` (C-32 PASS — confirmed R13 V-04)
Container header: `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` (C-31 PASS)
Barrier role label: `*Analyst: Documentation accuracy analyst.*` (C-37 PASS — confirmed R13 V-04)
Semantic alignment: "Documentation Accuracy Review" + "Documentation accuracy analyst" → "documentation accuracy" (C-38 PASS)
C-39: C-31 ∩ C-32 ∩ C-37 simultaneously satisfied (C-39 PASS)

**Hypothesis:** 190/190. All C-01–C-40 pass. The V-01 + inertia-depth combination confirms
that Round-1 role labeling and prominent status-quo framing are both inert to C-01–C-40 when
combined. The 4-column Phase 0 TABLE with a status-quo row confirms C-40 schema-inertness:
the pass condition requires a TABLE encoding the baseline state, and including the manual-process
row as a baseline state row satisfies this regardless of schema width.

---

You are a Connectors / Power Automate throughput domain expert. Your task is to trace how
request volume moves through a rate-limited Power Automate system. The starting point is
inertia: what the organization does today without this flow, why that process fails at scale,
and how the proposed flow's throttle profile compares. Round 2 reviews every construct limit
for documentation accuracy.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Lead analyst: Throttle scenario modeler.*

### PHASE 0 — Inertia Baseline

*Establish the full inertia picture: what the organization does today (the status-quo process),
why it cannot scale, and what the proposed flow's baseline throttle profile looks like — before
any bottleneck analysis begins.*

**Status-quo process:** Describe what the organization currently does without this flow. Name
the manual process, the tools in use (SharePoint, Outlook, manual data entry, or equivalent),
and the human steps involved. This is the inertia competitor — the process the team abandons
if this flow is adopted.

**Inertia failure mode at scale:** At the scenario's request volume, where does the status-quo
process break? State the volume, the step that cannot keep up, and the user-visible consequence.
This is the problem the flow is supposed to solve.

**Current construct stack:** Name every PA construct in the proposed flow that carries request
volume at the scenario load. State each construct's current configuration — defaults only, no
throttle controls applied.

**Active limits in effect:** For each PA construct named, state the enforced limit at current
configuration and license tier.

**Baseline operational conditions:** State request volume, trigger frequency, and principal
context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Where does the proposed flow fail first at this volume? Name the
construct, the limit it hits, and the user-visible consequence. Compare explicitly to the
status-quo failure mode: is the flow's failure mode better, worse, or different?

**TABLE 0 — Inertia Baseline Register**

| Process / Construct | Type | Failure mode at scenario volume | Baseline limit / capacity |
|---------------------|------|--------------------------------|--------------------------|
| (status-quo process) | Manual process | (describe breakdown) | (human throughput ceiling) |
| (PA construct 1) | (exact PA term) | (N req/unit — license tier) | (trigger frequency, principal context) |

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
standard connector tiers, Microsoft 365 service protection limits. Exact PA documentation
terms only.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type, (b) numeric limit with unit,
(c) request contribution estimate with arithmetic shown. Block: PHASE 2 is blocked until
every row satisfies all three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Identify the binding bottleneck and explain why it saturates first at this volume:

> "[PA construct component] at [PA construct type] is the binding bottleneck. It saturates
> at [N req/unit-time] under this scenario because [reason]. The naive assumption that limits
> are independent fails here because [cascade chain or shared principal pool linkage]."

*Connect to Phase 0: how does the TABLE 0 inertia baseline reach this construct first? Is
this the same failure point as the status-quo process, or does the flow fail at a different
layer?*

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops.
Trace to terminal state.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

Categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Must differ across
tiers. Compare the flow's UX failure modes to the status-quo failure mode where applicable.

*Mark which TABLE 4 row represents the TABLE 0 inertia state's outcome.*

**GATE 2:** TABLE 3 >= 2 complete hops AND TABLE 4 >= 2 tiers with distinct UX categories AND
TABLE 2 ordering rationale per row. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out), high-frequency
trigger (no debounce), nested loops, batch misconfigurations. If none, name current guards.

*Are these burst paths present and unguarded in the TABLE 0 inertia state?*

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Two pairs minimum. Distinct Tier A / Tier B. Mechanism stated. Severity assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Remediation Registry and Throttle Budget Corrections

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft docs) / MEDIUM (community or admin center) / LOW (runtime).
Flag MEDIUM and LOW for Round 2.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal state is
not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

*Mark TABLE 9 rows OVER-LIMIT in the TABLE 0 inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Two PA-native remediations minimum, each mapped to a Phase 2–3 section finding.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition, trigger, and when it fires.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material capacity impact. State which TABLE 9
row shifts if the license tier changes.

**Section 4.G — Test Approach**

One concrete PA tooling test step with observable pass/fail result.

---

## ROUND 2 — Documentation Accuracy Review

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle model — however arithmetically grounded — is not evidence
of documentation accuracy. The model's TABLE 1 numeric limits may come from community sources,
admin center observations, or runtime estimates. The internal consistency of Round 1's arithmetic
does not confirm that any limit matches the Microsoft-published documented value for the
scenario's license tier. Round 2 evaluates every numeric limit and PA construct name against
published sources, independent of what Round 1 said.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced imprecise
TABLE 1 entries are in scope for Round 2 documentation accuracy evaluation.

---

*Analyst: Documentation accuracy analyst.*

For each TABLE 8 row, evaluate documentation accuracy:

1. **Documentation source:** Where is this numeric limit documented? Cite a specific source —
   Microsoft Power Platform documentation, connector certification page, or admin center observed
   value. "Generally known limit" does not pass.

2. **License-tier match:** Does this limit apply to the scenario's entitlement tier? A limit from
   a mismatched tier is a documentation error regardless of whether the number looks correct.

3. **Rate unit source:** Does the unit match the construct's documented enforcement granularity?
   Unit mismatches are documentation errors.

For each TABLE 7 cascade pair, evaluate documentation accuracy:

1. **Mechanism documentation:** Documented platform behavior or inferred from observed behavior?
   Inferred mechanisms require explicit flagging and a path to verification.

2. **Severity calibration:** Does the severity rating hold against the documented limit
   differential between Tier A and Tier B?

**TABLE 11 — Round 2 Documentation Accuracy Review**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

## V-05 — Ceiling: Round-1 PRE-ANALYSIS SCENARIO MODEL Container

**Axes:** Ceiling combination introducing a new structural element: a labeled container block
within Round 1, positioned between the `## ROUND 1` heading and Phase 0. This container is the
Round-1 structural analog of the Round-2 PRE-EVALUATION ASSERTIONS container (C-31): it names the
mechanism type of the Round 1 analysis ("SCENARIO MODEL"), declares the scope and baseline
independence of Phase 0, and carries a labeled evaluator-role declaration (`*Lead analyst: Throttle
scenario modeler.*`). The structural pattern at Round 1 thus parallels Round 2 at two layers: a
mechanism-type container declaration and an evaluator-role label.

Round-1 container: `### PRE-ANALYSIS SCENARIO MODEL (before any Phase 1 bottleneck analysis begins)` (new structural property — no criterion yet)
Round-1 role label within container: `*Lead analyst: Throttle scenario modeler.*` (new structural property)
Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS)
Phase 0 TABLE: present — 3-column baseline register (C-40 PASS)
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS)
Barrier heading: `## ROUND 2 — Entitlement Verification` (C-32 PASS)
Container header: `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` (C-31 PASS)
Barrier role label: `*Role: Platform entitlement verifier.*` (C-37 PASS)
Semantic alignment: "Entitlement Verification" + "Platform entitlement verifier" → "entitlement verif*" (C-38 PASS)
C-39: C-31 ∩ C-32 ∩ C-37 simultaneously satisfied from Round 2 barrier (C-39 PASS)

**Hypothesis:** 190/190 under v14. All C-01–C-40 pass. The Round-1 PRE-ANALYSIS SCENARIO MODEL
container is a new structural property not captured by any existing criterion. It introduces two
new structural anchors at Round 1:
- **Round-1 container mechanism-type declaration** — "SCENARIO MODEL" names the content authority
  of the Round 1 analysis, parallel to C-31 ("ASSERTIONS" names the content authority at Round 2)
- **Round-1 evaluator-role label** — `*Lead analyst: Throttle scenario modeler.*` declares the
  evaluator persona governing Round 1, parallel to C-37 at Round 2

Together these establish a potential Round-1 analog of the C-31 ∩ C-32 ∩ C-37 three-anchor
completeness pattern (C-39) — a second instance of the same structural pattern at Round 1.
Whether this constitutes new criteria (C-41, C-42) or a new conjunction criterion depends on
whether the two Round-1 anchors can be independently confirmed in subsequent rounds.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Round 2 verifies every numeric limit from Round 1 against
its published entitlement source.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PRE-ANALYSIS SCENARIO MODEL (before any Phase 1 bottleneck analysis begins)

**Scope of Round 1:** This round establishes the current construct stack, active throttle limits,
and scenario volume baseline (Phase 0), then traces bottleneck ordering, backpressure propagation,
exposure paths, and UX impact through Phases 1–4. Phase 0 establishes facts about the system as
currently configured. Phases 1–4 perform analysis on those facts to identify where the system
fails and why.

**Baseline independence:** Phase 0 rows are facts — the system as configured, the limits as
enforced, the volume as stated. Phase 1 analysis identifies which Phase 0 rows become binding
constraints at scenario volume. Phase 0 does not predetermine the bottleneck; that is Phase 1's
analysis contribution. A Phase 0 row that shows a limit of N does not mean N is the bottleneck —
Phase 1 determines ordering by comparing all rows against scenario volume simultaneously.

---

*Lead analyst: Throttle scenario modeler.*

### PHASE 0 — Inertia Baseline

*State what the system does today under load. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume at
the scenario load. State each construct's current configuration — default settings, no explicit
throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct named above, state the limit enforced under the
current configuration and license tier. This is the inertia profile — the ceiling the system
operates under whether the team has measured it or not.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency, and
principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the inertia state first breaks at this volume. Name
the construct, the limit it hits, and the user-visible consequence when no mitigation is present.
This is the outcome a team accepts by doing nothing.

**TABLE 0 — Inertia State Register**

| Construct | Enforced limit | Operational condition |
|-----------|---------------|----------------------|
| (fill) | (N req/unit — license tier) | (trigger frequency, principal context, default config) |

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. Generic "API limit" does not pass. Use
exact PA documentation terms.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type from the domain list, (b) numeric
limit with unit, (c) request contribution estimate with arithmetic shown. Rows with missing fields
receive a `?` flag. Block: PHASE 2 is blocked until every row satisfies all three conditions.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck. It
> saturates at [N req/unit-time] under this scenario because [reason the ordering holds at
> this aggregate volume]. The naive assumption that limits are independent fails here because
> [one sentence linking to cascade chain or shared principal pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck? Reference the
TABLE 0 baseline failure point. If the Phase 1 bottleneck differs from the Phase 0 failure point,
state why.*

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops.
Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories MUST
differ across tiers. State what the user sees, not what the system does.

*Anchor to baseline: mark which TABLE 4 row represents the TABLE 0 inertia state's outcome.*

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX categories
AND TABLE 2 has ordering rationale per row. Block: PHASE 3 is blocked until GATE 2 passes.

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

*Anchor to baseline: are these burst paths present and unguarded in the TABLE 0 inertia state?*

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required. If no
gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, mechanism stated, severity
assessed.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B, mechanism
stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center observed),
LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2 audit. "Confirmed" requires the
exact PA documentation name — not a paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct the UX category against PA runtime
behavior. Internal system behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row: "[N items] x
[M connector calls] = [total req], against [limit req/unit] → [saturation or headroom]."
Qualitative assessment without numeric projection does not pass.

*Anchor to baseline: mark each TABLE 9 row that would be OVER-LIMIT in the TABLE 0 inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs. "Add retries" and "reduce load" do not
count. Each remediation must map to a specific finding from Phases 2–3 by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call telemetry
in Power Platform admin center, request usage dashboard. State the condition each signal surfaces
and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State the
impact on this scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE
to OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling with an observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model — however arithmetically grounded — is not
evidence of entitlement accuracy. The scenario model's TABLE 1 numeric limits may be sourced from
community data, admin center observations, or estimated from runtime behavior. The internal
arithmetic consistency of Round 1 does not confirm that any limit matches the Microsoft-published
documented value for the scenario's license tier. Round 2's evaluator mandate operates
independently of Round 1's model: every numeric limit and PA construct name is evaluated against
published entitlement documentation regardless of Round 1 confidence assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced imprecise
TABLE 1 entries are now in scope for Round 2 entitlement evaluation.

---

*Role: Platform entitlement verifier.*

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

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or inferred?
   Inferred mechanisms require explicit flagging and a verification path.

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential? Justify HIGH severity where Tier B has significant headroom.

**TABLE 11 — Round 2 Entitlement Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|
