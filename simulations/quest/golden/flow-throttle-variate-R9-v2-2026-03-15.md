# flow-throttle Skill Body — Round 9 Complete Variations
**Date:** 2026-03-15
**Rubric:** v9 (C-01 through C-28 + C-33 + C-34; 22 aspirational criteria)
**Baseline ceiling:** R8 V-05 (C-09 through C-28 all satisfied; v9 adds C-33 enumerated-block gate form and C-34 compound correction gate block)

---

## Round 9 Analysis

**C-33 — Enumerated-block gate form** (format)
When a gate governs three or more pass conditions, the not-cleared block uses an independent enumerated list rather than an inline dash-append. Each failure state appears as a separate scannable list item. GATE 1, GATE 2, and GATE 3 each govern three or more conditions and must use this form.

**C-34 — Compound correction gate block** (format)
The CORRECTION GATE governs two independent predicates: (1) item disposition — every row has an explicit pass/fail; (2) spatial co-location — corrected content appears immediately below the `[FAIL]` annotation. Both predicates must appear as distinct list items in a single compound not-cleared block. Separating them across two sentences requires cross-reference; the compound block makes gate state derivable by inspection of the block alone.

**Design hypothesis:** C-33 and C-34 are structural form criteria. All five content axes (role sequence, output format, lifecycle emphasis, phrasing register, inertia framing) are predicted to be inert for C-33/C-34. Any variation carrying enumerated blocks for GATE 1/2/3 and a compound block for the CORRECTION GATE will satisfy both criteria regardless of content choices.

**Round 9 variation map:**

| Variation | Axis | C-33 | C-34 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Role sequence (PA architect + connector engineer) + WHY-first rationale (C-20) + section-adjacent inertia callouts (C-21) | PASS | PASS | v9 ceiling |
| V-02 | Output format: prose-primary Phases 2–3 | PASS | PASS | v9 ceiling |
| V-03 | Lifecycle emphasis: cascade-first, Phase 2 compressed | PASS | PASS | v9 ceiling |
| V-04 | Phrasing register: conversational + phase-opening inertia barriers | PASS | PASS | v9 ceiling |
| V-05 | Combined: single throughput analyst + list-based Phases 2–3 | PASS | PASS | v9 ceiling |

---

## V-01 — Role Sequence + WHY-First Rationale + Section-Adjacent Inertia Callouts

**Axis:** Role sequence — Round 1 is owned by a Power Automate flow architect; Round 2 is owned by a connector support engineer. WHY-first rationale (C-20): each enforcement instruction is annotated inline with its purpose. Section-adjacent inertia callouts (C-21): each section with identified inertia risk opens with a targeted callout naming the specific artifact and structural limitation, distributed across sections rather than consolidated.

**Hypothesis:** v9 ceiling. Role assignment governs expertise framing, not gate block form. WHY-first rationale and section-adjacent inertia callouts are format criteria that operate on the surrounding prose — they do not affect the gate declaration block structure. C-33 evaluates whether failure states appear as independent enumerated list items; C-34 evaluates whether the CORRECTION GATE block enumerates both predicates as a compound list. Neither criterion is sensitive to role persona or instruction annotation style. Expected: v9 ceiling.

---

You are a Power Automate flow architect simulating throughput across a rate-limited Power Automate system. For Round 2, you will adopt the role of a connector support engineer to apply construct-precision verification.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 1 — Construct Inventory

**INERTIA CALLOUT — PHASE 1:** The constructs most commonly absent from informal throttle analyses are nested action quotas and premium connector per-user windows — they do not appear in the flow canvas, only in platform documentation and admin center telemetry. This callout is adjacent to PHASE 1 because inventory omissions are the most frequent source of cascade failures discovered only in production.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, each tier author uses an implicit baseline that may differ from others, producing STATUS columns that are internally inconsistent and making multi-volume sweep silent failures invisible by inspection.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min  |  5x: `[5 × baseline]` req/min
Unit conversion (if limit granularity differs from baseline units): `[show conversion factor]`

TABLE 1 STATUS columns must reference these three computed values. A STATUS column where the 1x, 2x, and 5x entries are all identical means VOLUME ARITHMETIC was not used — flag that row with `?`.

**TABLE 1 — Throttle Tier Map**
*(The reason for T-NN identifiers: each tier must be traceable by a stable short identifier through every downstream table and section; synonym-based matching produces silent audit failures.)*

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term — see domain list) | (N req/unit) | (arithmetic) | SAFE/MARGINAL/HIT/SAT | | | yes / no / N/A | (see QUOTA EXHAUSTION PROJECTION) |

Domain rule *(the reason: a generic term like "API limit" cannot be matched to a documented limit, breaking TABLE 9 arithmetic traceability)*: each PA construct type must be drawn exactly from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

WRONG: "API rate limit" — not a documented PA construct type.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" — exact documented term with enforcement scope.

---

**QUOTA EXHAUSTION PROJECTION**
*(The reason: `Failure visibility window` entries in TABLE 1 are assertions without arithmetic backing; this projection converts them to verifiable depletion intervals anchored to the VOLUME ARITHMETIC 2x rate.)*

For each T-NN with HIT or SAT status in TABLE 1: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x load." (assertion without arithmetic)
PASS: "T-01: 40,000 req quota / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion at 2x nominal."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) an exact PA construct type from the domain list, (b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown, (d) a populated Retry-After field, and (e) every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type rather than an exact PA term
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic shown
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation citing the VOLUME ARITHMETIC 2x rate

Rows in any of the above failure states receive a `?` flag — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**INERTIA CALLOUT — PHASE 2:** The first 429 in production is typically blamed on the most visible construct — usually the connector call — rather than the actual binding constraint. The real binding tier is often a per-user entitlement that accumulates across all flows sharing a principal, invisible from within a single flow's execution trace. This callout is adjacent to PHASE 2 because bottleneck misattribution is the direct cause of ineffective mitigations.

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:
*(The reason for the "naive assumption" sentence: it makes limits non-independence explicit, which is the structural cause of most cascade failures — without it, the bottleneck statement appears to describe an independent limit.)*

> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds at this aggregate volume].
> The naive assumption that limits are independent fails here because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| T-NN | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|------|--------------------------|-------|----------------------------------------|
| (bottleneck — first hit) | | | |
| (second hit) | | | |

**Section 2.B — Backpressure Hop Chain**

*(The reason for requiring a named terminal state: a propagation trace without a terminal state leaves the reader unable to determine whether the failure is user-visible or silently lost — the distinction determines which UX category to assign.)*

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops. Name the terminal state (user-visible error, flow run failure, or silent drop) in the final row.

**Section 2.C — User Experience per Throttle Tier**

**INERTIA CALLOUT — SECTION 2.C:** The most common UX mapping error is reporting internal system state ("queue depth increases," "retry loop activates") rather than what the user sees. This callout is adjacent to Section 2.C because UX category conflation is the specific failure mode that makes TABLE 4 entries unverifiable by a PA runtime reviewer.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ across tiers. Each row must state what the user sees — not what the system does internally.

**Section 2.D — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: the same total request volume produces different throttle outcomes when concentrated versus distributed; a model that ignores arrival shape misses burst-triggered saturation events that nominal-volume planning cannot predict.)*

**LOAD SHAPE COMPARISON:** For each T-NN, state whether STATUS changes between UNIFORM and BURST arrival at the VOLUME ARITHMETIC 1x total volume. Positive case: show numeric comparison grounded in TABLE 1 limit. Null case: name the specific rate limit mechanism (per-minute bucket / per-second window / sliding window / token bucket) as the structural reason shape does not change that tier's status.

**BURST SHAPE MATRIX**
*(The reason for computing f* as a derived value: a matrix that names shapes without computing the critical threshold is a descriptive survey, not a threshold-finding analysis — the reader cannot determine the exact concentration boundary from named shapes alone.)*

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit
Derive from VOLUME ARITHMETIC 1x total volume and TABLE 1 binding T-NN limit.

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | below / above f* | SAFE / TRIGGERED | [specific mechanism for this shape] |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation. A single binary null finding does not satisfy this requirement — each shape requires its own mechanism evaluation.

---

**GATE 2** is cleared when and only when TABLE 3 has >= 2 complete hops with a named terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has a "why this order holds" explanation for each row; the BURST SHAPE MATRIX has f* computed as a derived value from VOLUME ARITHMETIC and TABLE 1; and each BURST SHAPE MATRIX row carries an independent mechanism citation.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 complete hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share the same UX category
- TABLE 2 has any row without a "why this order holds" explanation
- The BURST SHAPE MATRIX is absent or f* is not computed as a derived value from VOLUME ARITHMETIC and TABLE 1
- Any BURST SHAPE MATRIX row lacks an independent mechanism citation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure and Test Coverage Analysis

*(GATE 2 must pass before this phase executes.)*

**INERTIA CALLOUT — PHASE 3:** PA flows commonly deploy with `Apply to Each` at default concurrency (50 parallel iterations), parallel branches with no fan-out cap, and high-frequency triggers with no debounce. These are structural burst sources invisible from the flow canvas. The test environment typically runs at 10–20% of production concurrency, so these patterns are never surfaced before production.

**Section 3.A — Unprotected Burst Paths**

*(The reason for requiring a named component and structural gap: generic statements like "bursts can be risky" provide no actionable mitigation target; naming the construct and the bypass mechanism does.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. If none found, write an explicit acknowledgment naming at least two specific guards and their locations as evidence.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement applies at the environment level via [mechanism] at [location]; T-03's per-second window enforces at the connector action level with no bypass path through the [construct] action."

**Section 3.B — Retry-After Gap Table**

*(The reason for requiring failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard is the basis for selecting a PA-native mitigation — without a named failure mode, the mitigation is a generic retry policy.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism linking each pair. A flat list of independent throttle risks without cascade relationships does not pass.

**Section 3.D — Test Coverage Gap Analysis**

**INERTIA CALLOUT — SECTION 3.D:** The integration test suite reports green because it uses mocked connector responses that suppress HTTP 429s. The load test runs at 10–20% of production concurrency. These structural properties mean the test suite cannot reach any of the throttle behaviors identified in PHASES 2–3 regardless of how many test cases are added. This callout is adjacent to Section 3.D because naming these artifacts before filling gap entries prevents generic gap field entries.

#### STAGE 1 — Test Infrastructure Inertia Catalog

*(The reason for naming specific artifacts before gap entries: a model that has the specific artifact and its structural limitation in scope at the point of writing a gap entry cannot produce generic `Structural reason` or `Test approach` fields without the failure being visible by inspection.)*

Name at least two specific existing test infrastructure artifacts that structurally cannot reach the throttle behaviors identified above. For each, state the architectural property causing the miss — not the test category.

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact — e.g., "the integration suite at `/tests/flow/connector.test.ts`"] | [architectural property — e.g., "uses `MockSharePointConnector` which suppresses all HTTP 429 responses"] |

WRONG: "Integration tests" — category, not artifact.
PASS: "The nightly integration suite at `/tests/flow/connector.test.ts` reports green because it uses `MockSharePointConnector.js` which never issues real HTTP 429 responses regardless of call volume."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

*(The reason for the GAP-NN template: missing a `Structural reason` field or using a generic `Test approach` field fails structurally by inspection without requiring a rubric audit — the template enforces completeness at the point of production.)*

For each throttle behavior from PHASES 2–3 that standard tests would miss, produce a labeled GAP-NN entry with all four fields.

**GAP-01**
- **Throttle behavior:** [specific behavior citing T-NN from TABLE 1 or Cascade-ID from TABLE 7]
- **Test type that misses it:** [unit / integration / load / chaos — specific test type, not category]
- **Structural reason:** [names an artifact from STAGE 1 and the architectural property that causes the miss]
- **Test approach:** [specific PA tooling step targeting this behavior]

WRONG approach: "Add load testing."
PASS approach: "Use Power Automate Performance Test Studio to replay [N] concurrent trigger events against the `Apply to Each` construct at [location], measuring requests/min against T-01's [limit] boundary and capturing HTTP 429 codes in flow run history."

*(Continue GAP-NN entries for each additional gap identified in PHASES 2–3.)*

---

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all required fields populated, distinct T-NN Tier A / Tier B constructs, a named throttle mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and a completed STAGE 2 register with at least two GAP-NN entries each carrying all four fields populated with non-generic values.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A T-NN equal to Tier B T-NN
- Any TABLE 7 row is missing a stated throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment
- Section 3.D STAGE 1 has fewer than two named artifacts with structural reasons
- Any Section 3.D GAP-NN entry is missing one or more of its four required fields

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and Precision Pass

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — Quantified Risk Register**

*(The reason for requiring arithmetic in at least one row: a Status entry of OVER-LIMIT without arithmetic is indistinguishable from a guess; arithmetic makes it a verifiable claim anchored to TABLE 1 limits and VOLUME ARITHMETIC rates.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row: "[N items] × [M connector calls] = [total req], against [limit req/unit] → [saturation arithmetic]."

**Section 4.B — Mitigation Registry**

*(The reason for `Source`, `Without this change`, and `Depends-on` columns: Source makes the mitigation traceable to a finding; Without-this-change makes urgency explicit rather than inferred; Depends-on converts TABLE 10 from a flat recommendation list into an execution plan. The `Depends-on` pre-load also supplies component-cause-effect vocabulary that improves GAP-NN Structural reason fields as a structural side effect. The Without-this-change column must be retained independently alongside Depends-on — no compression.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

- Without-this-change: name the component, failure mode, and threshold. WRONG: "Throttle errors will increase." PASS: "T-02 (SharePoint connector per-user quota): HTTP 429 storm affecting all flows sharing the service principal at 2x; flow run failure rate reaches 100% within [quota / 2x rate from VOLUME ARITHMETIC] minutes."
- Depends-on: MR-ID of prerequisite mitigation, or `--` if none.

Minimum: two PA-native remediations each mapped to a specific finding by T-NN, Path-ID, or Cascade-ID. Generic "add retries" or "reduce load" entries do not qualify.

**Section 4.C — Tier-ID Coverage Audit**

*(The reason: C-12 enforces identifier consistency within each section but does not enforce downstream representation — a tier absent from TABLE 3 passes C-12 on identifier grounds while creating a silent propagation gap. This audit closes that coverage gap.)*

For each T-NN in TABLE 1, verify it appears in each downstream section.

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section 3.D | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Any T-NN absent from a downstream section: annotate as COVERAGE GAP [T-NN → section name].

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call telemetry in Power Platform admin center, request usage dashboard. State the condition each signal surfaces and when it triggers.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State the impact: does the boundary shift any TABLE 9 row from SAFE to OVER-LIMIT or vice versa?

**Section 4.F — PA Construct Precision Pass**

*(Flow architect: confirm the exact documented term or flag for Round 2 connector engineer correction. The reason: "confirmed" is an assertion that the name matches PA documentation exactly — paraphrases and category names must be flagged here, not confirmed.)*

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row, write the corrected construct name, limit source, and precision note **immediately below the `[FAIL]` annotation** before writing any subsequent TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its `[FAIL]` annotation in the prescribed location.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and all remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling. "Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

*Role: Connector support engineer.*

**Independence:** Round 1's confidence as flow architect is not evidence of Round 2's connector-level precision. A thorough, coherent Round 1 analysis — with correct bottleneck ordering, complete cascade pairs, and precise UX mappings — can still contain PA construct names drawn from paraphrase rather than documentation, rate units from estimates rather than platform sources, or cascade load estimates using directional language where numeric precision is required. Round 2 operates independently of Round 1 output quality.

**Scope extension:** Corrected construct names from TABLE 11 (Section 4.F) that replaced imprecise TABLE 1 entries are now in scope for Round 2 precision checking. These were excluded from Round 1 because Round 1 closed before TABLE 11 corrections were finalized.

---

For each T-NN row in TABLE 11, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term in Power Automate documentation? Does it match the product-published limit source?
2. **Numeric limit precision:** Is the limit value the documented platform limit or a derived estimate? State the source (PA documentation, connector certification, admin center observed value, or estimate with confidence level).
3. **Rate unit precision:** Confirm the unit (per-minute, per-second, per-24-hours, per-user, per-environment) matches the construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact signal path and load calculation) or qualitative? Promote qualitative statements using TABLE 9 arithmetic.
2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a directional statement? If directional, compute the numeric projection from TABLE 9 data.
3. **QUOTA EXHAUSTION PROJECTION precision:** Does each depletion interval cite the VOLUME ARITHMETIC 2x rate by name? Flag any projection using an independently chosen rate.

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-01 prompt body.*

---

## V-02 — Output Format: Prose-Primary Phases 2–3

**Axis:** Labeled prose paragraphs replace markdown tables for Phase 2 sections (2.A–2.D) and Phase 3 sections (3.A–3.C). Phase 1 retains TABLE 1 (construct inventory requires structured data for cross-section traceability). Phase 4 retains all tables (precision pass, throttle budget, mitigations require structural verification). Section 3.D retains the STAGE 1/STAGE 2 table + GAP-NN structure. All gate declarations maintain C-33/C-34 structural form.

**Hypothesis:** v9 ceiling. Output format controls how analysis sections are expressed — replacing tables with labeled prose paragraphs does not affect the gate declaration, which is a structural block following each phase. C-33 evaluates whether not-cleared conditions appear as an independent enumerated-list block; prose format in Phases 2–3 does not change gate block structure. C-34 evaluates the CORRECTION GATE block in Phase 4.F, which retains table format across all format variations. Expected: v9 ceiling.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

**VOLUME ARITHMETIC**

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min  |  5x: `[5 × baseline]` req/min
Unit conversion: `[show if limit granularity differs from baseline units]`

TABLE 1 STATUS columns must reference these computed values. A STATUS column with identical 1x/2x/5x entries means VOLUME ARITHMETIC was not applied — flag that row with `?`.

**TABLE 1 — Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule: PA construct types must be exact documented terms — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic terms do not pass.

---

**QUOTA EXHAUSTION PROJECTION**

For each HIT or SAT tier in TABLE 1: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC. A prose statement of depletion risk without arithmetic does not pass.

---

**GATE 1** is cleared when and only when every TABLE 1 row has an exact PA construct type, a numeric limit with unit, a request contribution estimate with arithmetic, a populated Retry-After field, and every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type rather than an exact PA term
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic shown
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION entry with arithmetic

Rows in any of the above failure states receive a `?` flag — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write three labeled paragraphs:

**Bottleneck paragraph:** Identify the binding bottleneck by T-NN and construct name. State the PA construct type, the saturation rate under this scenario's volume, and the reason this tier saturates first. Explain in one sentence why limits are non-independent (cascade chain or shared principal pool).

**Hit order paragraph:** List each tier in saturation sequence — first, second, and any subsequent. For each, name the T-NN, construct, limit, and why it saturates at this volume before the next. An unordered enumeration without ordering rationale does not satisfy this section.

**Ordering validation paragraph:** Confirm in one sentence that the analysis accounts for shared resource pools that make per-construct limits interdependent.

**Section 2.B — Backpressure Hop Chain**

Write each hop as a labeled prose entry. Minimum: two hops, then a terminal state entry.

**Hop 1:** `[From T-NN construct]` emits `[signal type: error code / retry-after header / queue depth increase / other]` → `[To T-NN construct]` responds with `[behavior]`.

**Hop 2 (and further if applicable):** Continue from the last receiving component in the same format.

**Terminal state:** Name the terminal outcome (user-visible error, flow run failure, or silent drop) and the T-NN component at which it occurs.

**Section 2.C — User Experience per Throttle Tier**

Write one labeled paragraph per UX tier. Minimum: two tiers with distinct UX categories.

**Tier T-NN [X] — [UX category]:** The user experiences `[specific observable state]` at this throttle tier. The system action is `[internal behavior]`, which surfaces as `[what the user sees or does not see]`. UX category: transparent-retry / visible-delay / error-surfaced / silent-loss.

UX categories must differ across tiers. A paragraph stating only internal system action without specifying what the user observes does not satisfy this section.

**Section 2.D — Load Shape and Burst Sensitivity**

Write the LOAD SHAPE COMPARISON paragraph: state whether any T-NN STATUS changes between UNIFORM and BURST arrival at the VOLUME ARITHMETIC 1x total volume. If yes: show the numeric comparison grounded in TABLE 1 limits. If no tier changes: name the specific rate limit mechanism (per-minute bucket / per-second window / sliding window / token bucket) as the structural reason arrival shape does not affect that tier's status.

Then write the BURST SHAPE MATRIX paragraph: derive f* = smallest f such that (total_volume / (f × window)) > binding tier limit, from VOLUME ARITHMETIC and TABLE 1. For each shape — Uniform (f=1.0), Moderate burst (f=0.3), Severe burst (f=0.1) — state whether peak rate falls below or above f* and cite the mechanism independently. A single binary null finding does not pass; each shape requires its own mechanism evaluation.

---

**GATE 2** is cleared when and only when Section 2.B has >= 2 labeled hop entries with a named terminal state; Section 2.C has >= 2 tier paragraphs with distinct UX categories; Section 2.A has a hit-order paragraph with ordering rationale for each tier; and Section 2.D has f* computed as a derived value with per-shape independent mechanism citations.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section 2.B has fewer than 2 labeled hop entries, or is missing a named terminal state
- Section 2.C has fewer than 2 tier paragraphs, or any two paragraphs share the same UX category
- Section 2.A is missing a hit-order explanation for any tier in the sequence
- Section 2.D is absent or f* is not computed as a derived value from VOLUME ARITHMETIC and TABLE 1
- Any shape entry in Section 2.D lacks an independent mechanism citation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure and Test Coverage Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

For each burst-exposed path, write a labeled prose entry:

**Burst path [Path-ID]:** Flow construct `[name]` at `[location]` uses PA construct type `[type]`. Estimated peak rate: `[N req/unit]`. This path bypasses or overwhelms the tier-1 guard because `[mechanism]`.

Check all patterns: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger without debounce, nested loops, batch-size misconfigurations. No paths found: write an explicit acknowledgment naming at least two specific guards and their locations.

**Section 3.B — Retry-After Gaps**

For each gap, write a labeled prose entry:

**Gap [T-NN]:** Consumer construct `[name]` receives a 429 at `[location]`. Retry-After header: `[read / not read]`. Actual backoff: `[description]`. Failure mode: retry-storm / fixed-misalign / silent-discard.

At least one gap required.

**Section 3.C — Cascade Risk Pairs**

For each cascade pair, write a labeled prose entry:

**Cascade [Cascade-ID]:** Tier A — T-NN `[X]` `[construct]` throttled via `[mechanism]`. Load added to Tier B: `[estimate]`. Tier B — T-NN `[Y]` `[construct]`. Failure mode: `[description]`. Severity: critical / high / medium. Duration: `[estimated]`.

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B constructs.

**Section 3.D — Test Coverage Gap Analysis**

#### STAGE 1 — Test Infrastructure Inertia Catalog

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property] |

WRONG: "Integration tests." PASS: "The nightly suite at `/tests/flow/connector.test.ts` uses `MockSharePointConnector` which suppresses all HTTP 429 responses regardless of call volume."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact and architectural property]
- **Test approach:** [specific PA tooling step]

WRONG approach: "Add load testing." PASS approach: "Use Power Automate Performance Test Studio to replay [N] concurrent events against [construct] at [location], measuring requests/min against T-01's [limit] and capturing 429 codes in flow run history."

*(Continue GAP-NN entries for each additional gap.)*

---

**GATE 3** is cleared when and only when Section 3.C has >= 2 cascade pair prose entries with distinct T-NN Tier A / Tier B, a named mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and at least two GAP-NN entries each with all four fields populated.

**GATE 3 is not cleared when any of the following failure states are present:**
- Section 3.C has fewer than 2 cascade pair entries
- Any Section 3.C entry has Tier A T-NN equal to Tier B T-NN
- Any Section 3.C entry is missing a stated throttle mechanism
- Any Section 3.C entry is missing a severity or duration assessment
- Section 3.D STAGE 1 has fewer than two named artifacts
- Any Section 3.D GAP-NN entry is missing one or more of its four required fields

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and Precision Pass

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x | Status | Headroom / Deficit |
|------|-----------|-------|-----------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.B — Mitigation Registry**

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

Without-this-change: component + failure mode + threshold. Depends-on: MR-ID or `--`.

**Section 4.C — Tier-ID Coverage Audit**

| T-NN | Sec 2.A | Sec 2.B | Sec 2.C | Sec 3.A | Sec 3.D | TABLE 10 |
|------|---------|---------|---------|---------|---------|---------|

Flag any absent T-NN as COVERAGE GAP [T-NN → section].

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal and the condition it surfaces.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 status row.

**Section 4.F — PA Construct Precision Pass**

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row, write corrected construct name, limit source, and precision note immediately below the `[FAIL]` annotation before writing any subsequent row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

At least one concrete PA tooling test step. "Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

**Independence:** Round 1's coherence — whether expressed in tables or labeled prose paragraphs — is not evidence of Round 2 precision. A thorough prose-based analysis can still contain PA construct names drawn from paraphrase rather than documentation, rate units from estimates, or cascade descriptions using directional language where numeric precision is required. Round 2 operates independently of Round 1 output format and analytical depth.

**Scope extension:** Corrected construct names from TABLE 11 (Section 4.F) are now in scope for Round 2 precision checking.

---

For each T-NN row in TABLE 11, apply precision checks:

1. **PA construct name precision:** Exact PA documentation term?
2. **Numeric limit precision:** Documented or estimated? State source.
3. **Rate unit precision:** Matches documented enforcement granularity?

For each cascade entry in Section 3.C, apply precision checks:

1. **Causal mechanism precision:** Structural or qualitative? Promote using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric or directional? If directional, compute from TABLE 9 data.

**TABLE 12 — Round 2 Precision Audit**

| Item (Section ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|---------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Lifecycle Emphasis: Cascade-First, Phase 2 Compressed

**Axis:** Phase 3 (cascade and exposure analysis) is elevated to primary analytical emphasis with expanded cascade coverage including priority ranking and cross-tier load estimation. Phase 2 is compressed to a mandatory minimum: a single bottleneck statement, a two-tier hit-order table, a one-sentence terminal propagation path, and two named UX outcomes. VOLUME ARITHMETIC and QUOTA EXHAUSTION PROJECTION are retained in Phase 1. The BURST SHAPE MATRIX moves to Phase 3 as part of the expanded burst exposure section. Gate declarations maintain C-33/C-34 structure; GATE 2 conditions match the compressed Phase 2 minimum.

**Hypothesis:** v9 ceiling. Lifecycle emphasis controls relative analytical volume per phase. The enumerated not-cleared blocks (C-33) and the compound CORRECTION GATE block (C-34) are structural markers at phase boundaries — their content is phase-allocation-independent. Compressing Phase 2 to minimum does not reduce the gate declaration to a simpler form. Expected: v9 ceiling.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system. This analysis emphasizes cascade risk: the most dangerous throttle failures occur not at first saturation but when Tier A saturation triggers Tier B overload before any recovery path is available. Phase 2 establishes minimum required context; Phase 3 is the primary analytical investment.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Cascade Risk Analysis

### PHASE 1 — Construct Inventory

**VOLUME ARITHMETIC**

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min  |  5x: `[5 × baseline]` req/min
Unit conversion: `[show if limit granularity differs from baseline units]`

TABLE 1 STATUS columns must reference these computed values. Identical 1x/2x/5x STATUS entries mean VOLUME ARITHMETIC was not used — flag that row.

**TABLE 1 — Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule: PA construct types must be exact documented terms — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

---

**QUOTA EXHAUSTION PROJECTION**

For each HIT or SAT tier: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC.

---

**GATE 1** is cleared when and only when every TABLE 1 row has an exact PA construct type, a numeric limit with unit, a request contribution estimate with arithmetic, a populated Retry-After field, and every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation

Rows in any failure state receive a `?` flag — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck Identification (Compressed Minimum)

*(GATE 1 must pass before this phase executes.)*

**Bottleneck statement (required):**
> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario because [reason]. Limits are non-independent because [one sentence on cascade chain or shared pool]."

**TABLE 2 — Hit Order (minimum two tiers)**

| T-NN | Construct | Limit | Why this order holds at scenario volume |
|------|-----------|-------|----------------------------------------|
| (bottleneck) | | | |
| (second) | | | |

**Terminal propagation path (one sentence minimum):** "`[T-NN bottleneck construct]` emits `[signal type]` → `[next T-NN component]` → `[terminal state: user-visible error / flow run failure / silent drop]`."

**UX minimum — two tiers, distinct categories:**
- T-NN [X]: `[UX category]` — user sees: `[observable state]`
- T-NN [Y]: `[UX category, distinct]` — user sees: `[observable state]`

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.

---

**GATE 2** is cleared when and only when the bottleneck statement is present with ordering rationale; TABLE 2 has >= 2 rows each with a "why this order holds" explanation; a terminal propagation path sentence names a terminal state; and two UX outcomes with distinct categories are stated.

**GATE 2 is not cleared when any of the following failure states are present:**
- The bottleneck statement is absent or missing its ordering rationale
- TABLE 2 has fewer than 2 rows, or any row is missing a "why this order holds" explanation
- The terminal propagation path sentence is absent or does not name a terminal state
- Fewer than 2 UX outcomes are stated, or any two share the same UX category

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Cascade Risk Analysis (Primary)

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Path Register**

**TABLE 3 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location | Estimated peak rate | Guard in place (or NONE) | Why bypass occurs |
|---------|----------------|------------------|----------|--------------------|--------------------------|--------------------|

Check all patterns: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger without debounce, nested loops, batch-size misconfigurations.

**Section 3.B — Retry-After Gap Analysis**

**TABLE 4 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Header read? | Backoff behavior | Failure mode |
|------|-------------------|-------------|--------------|------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register (Primary)**

For each cascade pair: identify the exact state change at Tier A, the load mechanism added to Tier B, a numeric Tier B load estimate, and the recovery window.

**TABLE 5 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle trigger | Load added to Tier B (numeric) | Tier B (T-NN) | Tier B limit | Headroom after load | Failure mode | Severity | Recovery window |
|------------|-------------|-----------------|-----------------|-------------------------------|-------------|-------------|---------------------|-------------|----------|----------------|

Minimum: two pairs with distinct T-NN Tier A / Tier B constructs. At least one pair where Tier B belongs to a different PA construct type than Tier A. Numeric load estimate required — directional estimates must be converted using TABLE 9 arithmetic.

**Section 3.D — Cascade Priority Ranking**

Rank TABLE 5 cascade pairs by severity × estimated exposure window. One sentence per pair justifying its rank.

**Section 3.E — Load Shape and Burst Sensitivity**

Write the LOAD SHAPE COMPARISON: for each T-NN, state whether STATUS changes between UNIFORM and BURST at VOLUME ARITHMETIC 1x total volume. Null case: name the specific mechanism as the structural reason.

Derive f* = smallest f such that (total_volume / (f × window)) > binding tier limit, from VOLUME ARITHMETIC and TABLE 1.

**TABLE 6 — Burst Shape Matrix**

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation. f* must be a derived value.

**Section 3.F — Test Coverage Gap Analysis**

#### STAGE 1 — Test Infrastructure Inertia Catalog

| Artifact | Structural reason for miss |
|----------|---------------------------|

At least two named artifacts. WRONG: "Integration tests." PASS: "[Named suite] at [path] uses [MockClass] which never issues real 429s."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact]
- **Test approach:** [specific PA tooling step]

WRONG approach: "Add load testing." PASS approach: "Use Power Automate Performance Test Studio to replay [N] concurrent events targeting [construct] at [location], measuring requests/min against T-NN [X]'s [limit] boundary."

*(Continue GAP-NN entries.)*

---

**GATE 3** is cleared when and only when TABLE 5 has >= 2 cascade pairs with all columns filled, distinct T-NN Tier A / Tier B, numeric Tier B load estimates, severity and recovery window assessed; Section 3.D has a ranked list with one justification sentence per pair; Section 3.E has f* as a derived value with per-shape citations; and Section 3.F has a completed STAGE 1 and at least two GAP-NN entries each with all four fields.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 5 has fewer than 2 cascade pairs
- Any TABLE 5 row has Tier A T-NN equal to Tier B T-NN
- Any TABLE 5 row has a directional (non-numeric) Tier B load estimate
- Any TABLE 5 row is missing a severity or recovery window
- Section 3.D is absent or missing a justification sentence for any pair
- Section 3.E is absent or f* is not a derived value
- Any Section 3.E BURST SHAPE MATRIX row lacks an independent mechanism citation
- Section 3.F STAGE 1 has fewer than two named artifacts
- Any Section 3.F GAP-NN entry is missing one or more of its four required fields

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — Quantified Risk Register**

**TABLE 7 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x | Status | Headroom / Deficit |
|------|-----------|-------|-----------------------|--------|--------------------|

Show arithmetic for at least one row.

**Section 4.B — Mitigation Registry**

**TABLE 8 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

Map at least two PA-native remediations to specific TABLE 5 cascade findings by Cascade-ID. Without-this-change: component + failure mode + threshold. Depends-on: MR-ID or `--`.

**Section 4.C — Tier-ID Coverage Audit**

| T-NN | TABLE 2 | TABLE 3 / UX min | TABLE 5 | Sec 3.F | TABLE 8 |
|------|---------|------------------|---------|---------|---------|

Flag absent T-NN entries as COVERAGE GAP.

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal and the condition it surfaces.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 7 status row.

**Section 4.F — PA Construct Precision Pass**

**TABLE 9 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]`, write corrected construct name, limit source, and precision note immediately below the `[FAIL]` annotation.

**CORRECTION GATE** is cleared when and only when every TABLE 9 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 9 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 9 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 10 and remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

At least one concrete PA tooling test step targeting cascade behavior specifically.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

**Independence:** Round 1's cascade depth and priority ranking are not evidence of Round 2 precision. A thorough cascade analysis with numeric load estimates and ranked severity can still contain construct names from paraphrase rather than documentation, or cascade load estimates that are directional. Round 2 operates independently.

**Scope extension:** Corrected construct names from TABLE 9 (Section 4.F) are now in scope for Round 2.

---

For each T-NN row in TABLE 9, apply precision checks:

1. **PA construct name precision:** Exact PA documentation term?
2. **Numeric limit precision:** Documented or estimated? State source.
3. **Rate unit precision:** Matches documented enforcement granularity?

For each cascade pair in TABLE 5:

1. **Causal mechanism precision:** Structural or qualitative? Promote using TABLE 7 arithmetic.
2. **Load-added precision:** Numeric or directional? If directional, compute from TABLE 7.
3. **Recovery window precision:** Derived from PA retry or queue mechanism, or estimated?

**TABLE 10 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding | Correction if needed |
|--------------------------------------|------------------------|---------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Phrasing Register: Conversational + Phase-Opening Inertia Barriers

**Axis:** Conversational and descriptive register throughout ROUND 1 ("your job is to," "consider how," "think through," "when you see"). Each phase and major section opens with a current-state barrier paragraph describing what is typically absent or broken in production before stating the analytical task. Gate declarations use the same enumerated-block structure; only the surrounding prose register changes.

**Hypothesis:** v9 ceiling. Conversational register affects sentence structure and framing. Current-state barrier preambles add context before analytical tasks — they precede the gate declarations, not replace them. C-33 tests whether not-cleared conditions appear as an independent enumerated list; this is a structural property of the gate block, unaffected by the register of phase instructions that precede it. C-34 tests the CORRECTION GATE block structure, insulated from register choices in Phases 1–3. Expected: v9 ceiling.

---

You are a Connectors / Power Automate throughput domain expert. Your job is to simulate what actually happens when a rate-limited Power Automate flow is pushed to its operational volume — tracing where it breaks, how fast, and what the user experiences.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

**Current-state barrier:** Most PA flows are deployed without anyone mapping which throttle tiers are present. The constructs most commonly missed are nested action quotas and premium connector per-user limits — they don't appear in the flow canvas, only in platform docs and admin telemetry. The result is reactive firefighting when the first 429 surfaces weeks after go-live.

Your first job is to compute your volume arithmetic before touching any tier entries. Without pre-computed bands, STATUS columns have no shared baseline — and a STATUS column where 1x, 2x, and 5x are all identical means the volume sweep never ran.

**VOLUME ARITHMETIC**

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min  |  5x: `[5 × baseline]` req/min
Unit conversion: `[show if limit and baseline use different time granularities]`

When you fill TABLE 1 STATUS columns, use these three bands. A row with identical 1x/2x/5x STATUS means VOLUME ARITHMETIC was not applied — flag it.

Now map every throttle-relevant construct in the flow. Use the exact documented PA term for each construct type — a generic term like "API limit" cannot be traced to a documented limit, which breaks downstream arithmetic.

**TABLE 1 — Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Valid PA construct types: Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

---

**QUOTA EXHAUSTION PROJECTION**

Once you've found any HIT or SAT tiers, compute when they run out — not just that they will. For each HIT or SAT tier: `quota / rate_at_2x = minutes_to_depletion`. Use the 2x rate from VOLUME ARITHMETIC.

WRONG: "T-01 will exhaust quota at 2x load." (no arithmetic)
PASS: "T-01: 40,000 req quota / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion."

---

**GATE 1** is cleared when and only when every TABLE 1 row has an exact PA construct type, a numeric limit with unit, a request contribution estimate with arithmetic, a populated Retry-After field, and every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation

Rows in any failure state get a `?` flag — resolve before moving to PHASE 2.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass first.)*

**Current-state barrier:** The first 429 in production usually gets blamed on the most visible construct — often the connector call — rather than the actual binding constraint. The real binding tier is often a per-user entitlement that accumulates across all flows sharing a principal, invisible from within a single flow's execution trace. Think through which tier hits its limit first at this scenario volume and why that ordering holds even when constructs appear independent.

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason].
> The naive assumption that limits are independent fails here because [cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| T-NN | Construct | Limit | Why this order holds at scenario volume |
|------|-----------|-------|----------------------------------------|

**Section 2.B — Backpressure Hop Chain**

**Current-state barrier:** When a 429 surfaces in logs, the signal has traveled through intermediate constructs that absorbed, transformed, or dropped it — which is why the user experience rarely matches what logs show.

**TABLE 3 — Backpressure Propagation**

| From T-NN | Signal emitted | Signal type | To T-NN | Response behavior |
|-----------|---------------|-------------|---------|------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops. Name the terminal state in the final row.

**Section 2.C — User Experience per Throttle Tier**

**Current-state barrier:** The most common UX mapping error is reporting what the system does internally — "queue depth increases," "retry loop activates" — rather than what the user sees. Think about what the user's experience actually is when each tier activates.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ across tiers.

**Section 2.D — Load Shape and Burst Sensitivity**

**Current-state barrier:** Flow volume planning is almost always done against a single nominal rate. Burst behavior is only discovered in production when a batch event or concurrent spike triggers a throttle that nominal-rate planning never anticipated.

Think through whether arrival shape changes the outcome: does concentrating the same total volume into a shorter window tip any T-NN from SAFE to HIT? Write the LOAD SHAPE COMPARISON. Then compute f*: the smallest concentration fraction f where (total_volume / (f × window)) exceeds the binding tier limit. Use VOLUME ARITHMETIC and TABLE 1.

**TABLE 5 — Burst Shape Matrix**

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row needs its own mechanism citation — a single binary null finding doesn't satisfy this structure.

---

**GATE 2** is cleared when and only when TABLE 3 has >= 2 complete hops with a named terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has a "why this order holds" explanation for each row; and TABLE 5 has f* computed as a derived value with per-shape mechanism citations.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 complete hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share the same UX category
- TABLE 2 has any row without a "why this order holds" explanation
- TABLE 5 is absent or f* is not computed as a derived value from VOLUME ARITHMETIC and TABLE 1
- Any TABLE 5 row lacks an independent mechanism citation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure and Test Coverage Analysis

*(GATE 2 must pass first.)*

**Current-state barrier:** PA flows routinely deploy with `Apply to Each` loops at default concurrency (50 parallel), parallel branches with no fan-out cap, and triggers firing without debounce. These are structural burst sources invisible from the flow canvas. The test environment typically runs at 10–20% of production concurrency.

**Section 3.A — Unprotected Burst Paths**

**TABLE 6 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location | Estimated peak rate | Why it bypasses tier-1 guard |
|---------|----------------|------------------|----------|--------------------|-----------------------------|

Check: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger without debounce, nested loops, batch misconfigs. No paths found? Name at least two specific guards and their locations as evidence.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. The trigger is debounced at [location] via [PA construct]; the Apply to Each is capped at [N] concurrent via Concurrency Control."

**Section 3.B — Retry-After Gap Analysis**

**Current-state barrier:** The most common retry implementation in PA is a fixed-interval `Do Until` loop — which ignores Retry-After headers and turns a 30-second throttle window into a 10-minute retry storm.

**TABLE 7 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Header read? | Backoff behavior | Failure mode |
|------|-------------------|-------------|--------------|------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**Current-state barrier:** Cascade failures are the hardest to reproduce in testing because they require Tier A to be genuinely throttled before Tier B sees the excess load — a condition that only exists at production volume.

**TABLE 8 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two pairs with distinct T-NN Tier A / Tier B constructs.

**Section 3.D — Test Coverage Gap Analysis**

**Current-state barrier:** The test suite you're about to enumerate gaps in was designed to verify behavior, not load. It almost certainly misses every throttle behavior identified above because the connector layer is mocked and the load fixtures run at a fraction of production volume.

#### STAGE 1 — Test Infrastructure Inertia Catalog

Name at least two specific test artifacts — not categories — that structurally miss the throttle behaviors.

| Artifact | Structural reason for miss |
|----------|---------------------------|

WRONG: "Integration tests." PASS: "The regression suite at `/tests/regression/flow-ops.spec.ts` uses `MockSPConnector.js` which returns HTTP 200 for all connector calls regardless of load."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

For each gap, consider: which T-NN or Cascade-ID behavior is missed? Which specific test type is responsible? What's the architectural reason it can't reach that behavior? What's the concrete PA tooling step to test it?

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact and architectural property]
- **Test approach:** [specific PA tooling step]

WRONG approach: "Add load testing." PASS approach: "Use Power Automate Performance Test Studio at [environment] to replay [N] concurrent trigger events against [construct] at [location], capturing HTTP 429 codes and retry-after intervals in run history."

*(Continue GAP-NN entries.)*

---

**GATE 3** is cleared when and only when TABLE 8 has >= 2 cascade pairs with distinct T-NN Tier A / Tier B, a named throttle mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and at least two GAP-NN entries each with all four fields populated.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 8 has fewer than 2 cascade pairs
- Any TABLE 8 row has Tier A T-NN equal to Tier B T-NN
- Any TABLE 8 row is missing a stated throttle mechanism
- Any TABLE 8 row is missing a severity or duration assessment
- Section 3.D STAGE 1 has fewer than two named artifacts
- Any Section 3.D GAP-NN entry is missing one or more of its four required fields

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and Validation

*(GATE 3 must pass first.)*

**Section 4.A — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x | Status | Headroom / Deficit |
|------|-----------|-------|-----------------------|--------|--------------------|

Show arithmetic for at least one row.

**Section 4.B — Mitigation Registry**

Think through which PA-native configurations directly address the findings from PHASES 2–3. Generic entries don't qualify — every row needs an exact PA feature name and specific configuration value.

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

Without-this-change: component + failure mode + threshold. WRONG: "Errors will increase." PASS: "T-02 SharePoint connector per-user quota: HTTP 429 storm affecting all flows sharing the service principal at 2x; flow run failure rate reaches 100% within [quota / 2x rate] minutes."

Depends-on: MR-ID of prerequisite, or `--`. Converts TABLE 10 into a dependency-ordered execution plan.

**Section 4.C — Tier-ID Coverage Audit**

Consider how well downstream sections covered each tier from TABLE 1. A tier absent from a downstream section passes C-12 on identifier grounds while creating a silent coverage gap.

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 6 | Sec 3.D | TABLE 10 |
|------|---------|---------|---------|---------|---------|---------|

Flag absent T-NN entries as COVERAGE GAP [T-NN → section].

**Section 4.D — Monitoring Signals**

What PA signal would surface this throttle condition before it becomes a user-visible failure?

**Section 4.E — License and Entitlement Boundary**

How does the entitlement tier change what's at risk? Name one boundary that shifts a TABLE 9 status row.

**Section 4.F — PA Construct Precision Pass**

When you mark "confirmed," you're asserting the name exactly matches the PA documentation term. When you mark "corrected," explain why the original was imprecise.

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|-----------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]`, write corrected name, limit source, and precision note immediately below the `[FAIL]` annotation before writing the next row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

How would you validate this throttle analysis before production? Describe at least one concrete step using PA tooling.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

**Independence:** Round 1's conversational depth and thorough current-state framing are not evidence of Round 2 precision. A well-framed analysis with clear barrier narratives can still contain PA construct names from paraphrase rather than documentation, numeric limits from estimates, or cascade load descriptions that are directional. Round 2 operates independently.

**Scope extension:** Corrected construct names from TABLE 11 (Section 4.F) are now in scope for Round 2 precision checking.

---

For each T-NN row in TABLE 11:

1. **PA construct name precision:** Exact PA documentation term?
2. **Numeric limit precision:** Documented or estimated? State source.
3. **Rate unit precision:** Matches documented enforcement granularity?

For each cascade pair in TABLE 8:

1. **Causal mechanism precision:** Structural or qualitative? Promote using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric or directional? If directional, compute from TABLE 9.

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding | Correction if needed |
|--------------------------------------|------------------------|---------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — Combined: Single Throughput Analyst + List-Based Phases 2–3

**Axis:** Role sequence (single Connectors / Power Automate throughput analyst throughout — Round 2 applies a precision filter under declared scope independence from the same analytical perspective, not a separate role persona) combined with output format (bulleted list entries replace markdown tables for Phases 2–3 analysis sections; Phase 1 TABLE 1 and Phase 4 tables are retained). Gate declarations maintain C-33/C-34 structural form.

**Hypothesis:** v9 ceiling. The single-analyst axis affects how Round 2 independence is declared — without reference to a separate persona. The list-format axis affects how Phase 2–3 findings are expressed. Neither changes gate declaration block structure. C-33/C-34 evaluate block form at phase boundaries — enumerated blocks and the compound correction gate block are structural markers that survive both content axis choices. Expected: v9 ceiling.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system. This analysis runs in two rounds: Round 1 builds the throttle tier model and exposure analysis; Round 2 applies a precision filter under declared scope independence to confirm every construct name and numeric claim against documented platform sources.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

**VOLUME ARITHMETIC**

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min  |  5x: `[5 × baseline]` req/min
Unit conversion: `[show if limit granularity differs from baseline units]`

TABLE 1 STATUS columns reference these three bands. Identical 1x/2x/5x entries mean VOLUME ARITHMETIC was not applied — flag that row.

**TABLE 1 — Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule: PA construct types must be exact documented terms — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

---

**QUOTA EXHAUSTION PROJECTION**

For each HIT or SAT tier: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC.

---

**GATE 1** is cleared when and only when every TABLE 1 row has an exact PA construct type, a numeric limit with unit, a request contribution estimate with arithmetic, a populated Retry-After field, and every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation

*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:
> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck. It saturates at [N req/unit-time] under this scenario because [reason]. Limits are non-independent because [cascade chain or shared pool]."

List the hit order. For each tier:
- **Hit [N] — T-NN [X]:** `[construct]` — limit: `[N req/unit]` — why this order holds: `[reason]`

**Section 2.B — Backpressure Hop Chain**

List the propagation hops. Minimum: two hops, then terminal state.

- **Hop 1:** `[from T-NN construct]` emits `[signal type: error code / retry-after header / queue depth increase / other]` → `[to T-NN construct]` responds with `[behavior]`
- **Hop 2:** `[continue chain]`
- **Terminal state:** `[user-visible error / flow run failure / silent drop]` at T-NN `[component]`

**Section 2.C — User Experience per Throttle Tier**

List UX outcomes. Minimum: two tiers with distinct UX categories.

- **T-NN [X] ([UX category]):** User sees `[observable state]`. System action: `[internal behavior]`. UX category: transparent-retry / visible-delay / error-surfaced / silent-loss.

UX categories must differ across tiers. Each entry must state what the user sees — not what the system does internally.

**Section 2.D — Load Shape and Burst Sensitivity**

Write the LOAD SHAPE COMPARISON: for each T-NN, state whether STATUS changes between UNIFORM and BURST at VOLUME ARITHMETIC 1x total volume. Null case: name the specific rate limit mechanism as the structural reason.

Derive f* = smallest f such that (total_volume / (f × window)) > binding tier limit, from VOLUME ARITHMETIC and TABLE 1.

List the BURST SHAPE MATRIX:
- **Uniform (f=1.0):** peak rate `[N]` — `[below / above]` f*=`[value]` → `[SAFE / TRIGGERED]` — mechanism: `[specific citation]`
- **Moderate burst (f=0.3):** peak rate `[N]` — `[below / above]` f* → `[result]` — mechanism: `[specific citation]`
- **Severe burst (f=0.1):** peak rate `[N]` — `[below / above]` f* → `[result]` — mechanism: `[specific citation]`

Each entry requires an independent mechanism citation. f* must be a derived value.

---

**GATE 2** is cleared when and only when Section 2.B has >= 2 listed hops with a named terminal state; Section 2.C has >= 2 tier entries with distinct UX categories; Section 2.A has a "why this order holds" entry for each tier; and Section 2.D has f* computed as a derived value with per-shape independent mechanism citations.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section 2.B has fewer than 2 listed hops, or is missing a named terminal state
- Section 2.C has fewer than 2 tier entries, or any two entries share the same UX category
- Section 2.A is missing a "why this order holds" entry for any tier
- Section 2.D is absent or f* is not a computed derived value from VOLUME ARITHMETIC and TABLE 1
- Any Section 2.D burst shape entry lacks an independent mechanism citation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure and Test Coverage Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

List each burst-exposed path:
- **Burst path [Path-ID]:** `[flow construct]` at `[location]` — PA type: `[type]` — peak rate: `[N req/unit]` — bypass reason: `[mechanism]`

Check: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger without debounce, nested loops, batch misconfigs. No paths found: list at least two named guards with locations.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. Trigger debounced at [location] via [PA construct]; Apply to Each capped at [N] via Concurrency Control."

**Section 3.B — Retry-After Gaps**

List each gap:
- **Gap [T-NN]:** `[consumer construct]` receives 429 at `[location]` — Retry-After read: `[yes/no]` — backoff: `[description]` — failure mode: retry-storm / fixed-misalign / silent-discard

At least one gap required.

**Section 3.C — Cascade Risk Pairs**

List each cascade pair:
- **Cascade [Cascade-ID]:** Tier A T-NN `[X]` `[construct]` throttled via `[mechanism]` — load added to Tier B: `[estimate]` — Tier B T-NN `[Y]` `[construct]` — failure mode: `[description]` — severity: critical / high / medium — duration: `[estimated]`

Minimum: two pairs with distinct T-NN Tier A / Tier B constructs.

**Section 3.D — Test Coverage Gap Analysis**

#### STAGE 1 — Test Infrastructure Inertia Catalog

| Artifact | Structural reason for miss |
|----------|---------------------------|

At least two named artifacts. WRONG: "Integration tests." PASS: "The suite at `/tests/integration/connector-ops.test.ts` using `MockConnector` which suppresses all HTTP 429 responses."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact and architectural property]
- **Test approach:** [specific PA tooling step]

WRONG approach: "Add load testing."
PASS approach: "Use Power Automate Performance Test Studio to replay [N] concurrent events against [construct] at [location], measuring requests/min against T-NN [X]'s [limit] boundary and capturing 429 codes in run history."

*(Continue GAP-NN entries.)*

---

**GATE 3** is cleared when and only when Section 3.C has >= 2 cascade pair entries with distinct T-NN Tier A / Tier B, a stated throttle mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and at least two GAP-NN entries each with all four fields populated.

**GATE 3 is not cleared when any of the following failure states are present:**
- Section 3.C has fewer than 2 cascade pair entries
- Any Section 3.C entry has Tier A T-NN equal to Tier B T-NN
- Any Section 3.C entry is missing a stated throttle mechanism
- Any Section 3.C entry is missing a severity or duration assessment
- Section 3.D STAGE 1 has fewer than two named artifacts
- Any Section 3.D GAP-NN entry is missing one or more of its four required fields

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and Precision Pass

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x | Status | Headroom / Deficit |
|------|-----------|-------|-----------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.B — Mitigation Registry**

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

Without-this-change: component + failure mode + threshold. Depends-on: MR-ID or `--`.

**Section 4.C — Tier-ID Coverage Audit**

| T-NN | Sec 2.A | Sec 2.B | Sec 2.C | Sec 3.A | Sec 3.D | TABLE 10 |
|------|---------|---------|---------|---------|---------|---------|

Flag absent T-NN entries as COVERAGE GAP [T-NN → section].

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal and the condition it surfaces.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 status row.

**Section 4.F — PA Construct Precision Pass**

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]`, write corrected construct name, limit source, and precision note immediately below the `[FAIL]` annotation before writing the next TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

At least one concrete PA tooling test step. "Test in staging" without a specific method does not pass.

---

## ROUND 2 — Precision Filter Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 precision evaluation begins)

**Scope independence:** The analytical perspective that produced the throttle tier model, burst sensitivity sweep, cascade pairs, and test gap register in Round 1 operates under the same cognitive frame that produced the TABLE 1 construct names. Round 2 applies a precision filter that is independent of Round 1's analytical confidence: a well-structured throttle model with correctly computed f* and complete cascade pairs can still contain construct names drawn from paraphrase rather than documentation, numeric limits from estimates, or cascade load figures that are directional. Round 2 evaluates precision, not analytical depth.

**Scope extension:** Corrected construct names from TABLE 11 (Section 4.F) that replaced imprecise TABLE 1 entries are now in scope for Round 2 precision checking. These were excluded from Round 1 because Round 1 closed before TABLE 11 corrections were finalized.

---

For each T-NN row in TABLE 11, apply precision checks:

1. **PA construct name precision:** Exact PA documentation term?
2. **Numeric limit precision:** Documented or estimated? State source.
3. **Rate unit precision:** Matches documented enforcement granularity (per-minute, per-24-hours, per-user, per-environment)?

For each cascade entry in Section 3.C, apply precision checks:

1. **Causal mechanism precision:** Structural (exact signal path and load calculation) or qualitative? Promote using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric or directional? If directional, compute from TABLE 9 data.

**TABLE 12 — Precision Audit**

| Item (TABLE ref / Section ref + T-NN or Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|-----------------------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*

---

## Round 9 Score Projection

| Variation | Axis | C-09..C-28 | C-33 | C-34 | Aspirational pass | Predicted score |
|-----------|------|-----------|------|------|-------------------|-----------------|
| V-01 | Role sequence + WHY-first (C-20) + inertia callouts (C-21) | 20/20 | PASS | PASS | 22/22 | **100** |
| V-02 | Prose-primary Phases 2–3 | 20/20 | PASS | PASS | 22/22 | **100** |
| V-03 | Cascade-first, Phase 2 compressed | 20/20 | PASS | PASS | 22/22 | **100** |
| V-04 | Conversational register + inertia barriers | 20/20 | PASS | PASS | 22/22 | **100** |
| V-05 | Single analyst + list-based Phases 2–3 | 20/20 | PASS | PASS | 22/22 | **100** |

Differentiation restored at the v9 rubric level: any variation missing C-33 or C-34 scores 21/22 aspirational (composite 99.55 → **99**). All five achieve 100 only by carrying both new structural criteria.
