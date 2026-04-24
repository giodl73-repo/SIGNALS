# flow-throttle Skill Body — Round 10 Complete Variations
**Date:** 2026-03-15
**Rubric:** v9 (C-01 through C-34, essential/recommended/aspirational; denominator 22)
**Baseline ceiling:** R9 V-05 (C-33 enumerated-block gate form + C-34 compound correction gate block; full-surface coverage confirmed across all five R9 content axes)

---

## Round 10 Analysis

**R9 confirmed:**
- C-33: Enumerated-list not-cleared blocks on GATE 1, GATE 2, and GATE 3 survive all five single-axis content variations — role persona, prose format, cascade-first lifecycle, conversational register + inertia framing, and single-analyst + list format do not disturb gate declaration structure.
- C-34: Compound CORRECTION GATE block (both item-disposition and spatial co-location predicates enumerated in a single not-cleared list) is equally axis-inert across all five R9 content axes.
- Confirmed design hypothesis: C-33/C-34 are structural gate declarations that depend only on block syntax, not on surrounding phase content, role persona, or output format.

**R9 single-axis coverage map:**

| R9 axis tested | Variation | Confirmed ceiling? |
|---------------|-----------|-------------------|
| Role sequence: PA architect (R1) + connector engineer (R2) | V-01 | Yes |
| Output format: prose-primary Phases 2–3 | V-02 | Yes |
| Lifecycle emphasis: cascade-first, Phase 2 compressed | V-03 | Yes |
| Phrasing register (conversational) + section-adjacent inertia | V-04 | Yes |
| Role sequence (single analyst) + list-based Phases 2–3 | V-05 | Yes |

**What R9 did NOT test:**
- Three-role topologies within ROUND 1 (R9 tested 1-role and 2-role only)
- Phase-level scorecard headers as a structural format overlay on tables
- Monitoring-anchored lifecycle (observability baseline declared before TABLE 1)
- Formal/technical imperative register (R9 covered conversational; formal untested)
- Multi-axis combinations beyond V-04/V-05's limited double combinations

**R10 structural additions required:** None. C-33/C-34 block structures are confirmed correct from R9 and carry unchanged across all five R10 variations. Goal: confirm they survive three-role handoffs, scorecard overlays, phase reordering, formal register, and maximum combined-axis load.

**R10 design hypothesis:** Combined axes will not produce structural interference with C-33/C-34 because gate block form is syntactically independent of phase content, role count, and output format. Any structural interference would manifest as a gate with inline dash-append rather than enumerated block — predicted not to occur when the block form is explicitly declared in the prompt. Expected: all five at v9 ceiling.

---

## Round 10 Variation Map

| Variation | Axes | C-33 | C-34 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Role sequence: 3-role cascade (connector specialist → throughput analyst → PA admin) | PASS | PASS | v9 ceiling |
| V-02 | Output format: phase-level scorecard header block preceding each phase's tables | PASS | PASS | v9 ceiling |
| V-03 | Lifecycle emphasis: monitoring-anchored (observability baseline TABLE 0 in Phase 1) | PASS | PASS | v9 ceiling |
| V-04 | Phrasing register (formal/technical imperative) + inertia framing (ASSUMPTION GAP per section) | PASS | PASS | v9 ceiling |
| V-05 | Three-axis: 3-role cascade + monitoring-anchored + scorecard format | PASS | PASS | v9 ceiling |

Risk vectors unique to R10: V-02 tests whether scorecard format overhead causes a model to treat scorecard `[PASS]` as a gate substitution; V-03 tests whether TABLE 0 in Phase 1 displaces GATE 1's not-cleared block; V-04 tests whether formal terse register drops list items from gate blocks; V-05 tests structural interference under maximum content load with three simultaneous format overlays.

---

## V-01 — Role Sequence: Three-Role Cascade

**Axis:** Role sequence — three named roles execute in declared sequence within ROUND 1. Role 1 (Connector Specialist) owns PHASE 1 construct inventory; Role 2 (Throughput Analyst) owns PHASES 2 and 3; Role 3 (Power Platform Admin) owns PHASE 4 including the CORRECTION GATE. ROUND 2 uses an independent Precision Auditor role. Each role opens with a role marker and closes at the next explicit handoff. Gate declarations are owned by the phase's active role but use identical block structure regardless of which role holds the gate.

**Hypothesis:** v9 ceiling. Role count does not affect gate declaration syntax. C-33 evaluates whether not-cleared conditions appear as an independent enumerated-list block — three roles executing phases produce the same gate block forms as one or two. C-34 evaluates the CORRECTION GATE block, which is owned by Role 3 (PA Admin) — the role's admin/remediation focus has no bearing on the compound block form. Risk vector: the Role 2 → Role 3 handoff at GATE 3 might cause a model to defer Phase 4's CORRECTION GATE to a new role context; mitigated by declaring CORRECTION GATE as part of Role 3's opening mandate.

---

You are simulating throughput across a rate-limited Power Automate system using a three-role analyst team. Roles execute in declared sequence. Each role is independent: prior role output is evidence to examine, not a conclusion to accept.

**Role assignments (declared before Phase 1 begins):**
- **Role 1 — Connector Specialist:** Executes PHASE 1. Owns exact PA construct identification, numeric limit sourcing from platform documentation, VOLUME ARITHMETIC, QUOTA EXHAUSTION PROJECTION, and Retry-After capability flags.
- **Role 2 — Throughput Analyst:** Executes PHASES 2 and 3. Owns bottleneck ordering, backpressure propagation, UX mapping, burst path identification, BURST SHAPE MATRIX, and cascade risk register. Accepts TABLE 1 as input — does not re-evaluate Role 1's construct names.
- **Role 3 — Power Platform Admin:** Executes PHASE 4. Owns PA construct validation, quantified risk register, mitigation registry, monitoring signals, license/entitlement boundary, and test approach. Carries the CORRECTION GATE.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

*Role: Connector Specialist.*

**INERTIA CALLOUT — PHASE 1:** The constructs most commonly absent from informal throttle analyses are nested action quotas and premium connector per-user windows — they do not appear in the flow canvas, only in platform documentation and admin center telemetry. Inventory omissions are the most frequent source of cascade failures discovered only in production.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers, producing entries that are internally inconsistent and making multi-volume sweep silent failures invisible by inspection.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
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

For each T-NN with HIT or SAT status: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC by name.

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

Rows in any of the above failure states receive a `?` flag — Role 1 corrects before handing off to Role 2.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*Role: Throughput Analyst. (Role 1 handoff complete — GATE 1 cleared.)*

*(GATE 1 must pass before this phase executes.)*

**INERTIA CALLOUT — PHASE 2:** The first 429 in production is typically blamed on the most visible construct — usually the connector call — rather than the actual binding constraint. The real binding tier is often a per-user entitlement that accumulates across all flows sharing a principal, invisible from within a single flow's execution trace. Bottleneck misattribution is the direct cause of ineffective mitigations.

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:
*(The reason for the "naive assumption" sentence: it makes limits non-independence explicit, which is the structural cause of most cascade failures.)*

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

**INERTIA CALLOUT — SECTION 2.C:** The most common UX mapping error is reporting internal system state ("queue depth increases," "retry loop activates") rather than what the user sees. UX category conflation makes TABLE 4 entries unverifiable by a PA runtime reviewer.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ across tiers. Each row must state what the user sees — not what the system does internally.

**Section 2.D — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: the same total request volume produces different throttle outcomes when concentrated versus distributed; arrival shape omission misses burst-triggered saturation events that nominal-volume planning cannot predict.)*

**LOAD SHAPE COMPARISON:** For each T-NN, state whether STATUS changes between UNIFORM and BURST arrival at the VOLUME ARITHMETIC 1x total volume. Positive case: show numeric comparison grounded in TABLE 1 limit. Null case: name the specific rate limit mechanism (per-minute bucket / per-second window / sliding window / token bucket) as the structural reason shape does not change that tier's status.

**BURST SHAPE MATRIX**
*(The reason for computing f* as a derived value: a matrix that names shapes without computing the critical threshold is a descriptive survey, not a threshold-finding analysis.)*

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit
Derive from VOLUME ARITHMETIC 1x total volume and TABLE 1 binding T-NN limit.

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | below / above f* | SAFE / TRIGGERED | [specific mechanism] |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

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

*Role: Throughput Analyst (continued). (GATE 2 cleared.)*

*(GATE 2 must pass before this phase executes.)*

**INERTIA CALLOUT — PHASE 3:** PA flows commonly deploy with `Apply to Each` at default concurrency (50 parallel iterations), parallel branches with no fan-out cap, and high-frequency triggers with no debounce. The test environment typically runs at 10–20% of production concurrency, so these patterns are never surfaced before production.

**Section 3.A — Unprotected Burst Paths**

*(The reason for requiring a named component and structural gap: generic statements like "bursts can be risky" provide no actionable mitigation target.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. If none found, write an explicit acknowledgment naming at least two specific guards and their locations as evidence.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement applies at the environment level via [mechanism] at [location]; T-03's per-second window enforces at the connector action level with no bypass path through the [construct] action."

**Section 3.B — Retry-After Gap Table**

*(The reason for requiring failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard is the basis for selecting a PA-native mitigation.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism linking each pair.

**Section 3.D — Test Coverage Gap Analysis**

**INERTIA CALLOUT — SECTION 3.D:** The integration test suite reports green because it uses mocked connector responses that suppress HTTP 429s. The load test runs at 10–20% of production concurrency. These structural properties mean the test suite cannot reach any of the throttle behaviors identified in PHASES 2–3 regardless of how many test cases are added. Naming these artifacts before filling gap entries prevents generic gap field entries.

#### STAGE 1 — Test Infrastructure Inertia Catalog

*(The reason for naming specific artifacts before gap entries: a model that has the specific artifact and its structural limitation in scope cannot produce generic `Structural reason` or `Test approach` fields without the failure being visible by inspection.)*

Name at least two specific existing test infrastructure artifacts that structurally cannot reach the throttle behaviors identified above. For each, state the architectural property causing the miss — not the test category.

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact — e.g., "the integration suite at `/tests/flow/connector.test.ts`"] | [architectural property — e.g., "uses `MockSharePointConnector` which suppresses all HTTP 429 responses"] |

WRONG: "Integration tests" — category, not artifact.
PASS: "The nightly integration suite at `/tests/flow/connector.test.ts` reports green because it uses `MockSharePointConnector.js` which never issues real HTTP 429 responses regardless of call volume."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

*(The reason for the GAP-NN template: missing a `Structural reason` field or using a generic `Test approach` fails structurally by inspection without requiring a rubric audit.)*

**GAP-01**
- **Throttle behavior:** [specific behavior citing T-NN from TABLE 1 or Cascade-ID from TABLE 7]
- **Test type that misses it:** [unit / integration / load / chaos — specific test type]
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

*Role: Power Platform Admin. (Role 2 handoff complete — GATE 3 cleared.)*

*Role 3 mandate: PA construct validation, quantified risk, PA-native remediations, monitoring signals, license/entitlement boundary, test approach. The CORRECTION GATE is owned by Role 3 and governs Sections 4.B through 4.G.*

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — Quantified Risk Register**

*(The reason for requiring arithmetic in at least one row: a Status entry of OVER-LIMIT without arithmetic is indistinguishable from a guess; arithmetic makes it a verifiable claim anchored to TABLE 1 limits and VOLUME ARITHMETIC rates.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row: "[N items] × [M connector calls] = [total req], against [limit req/unit] → [saturation arithmetic]."

**Section 4.B — Mitigation Registry**

*(The reason for `Source`, `Without this change`, and `Depends-on` columns: Source makes the mitigation traceable to a finding; Without-this-change makes urgency explicit rather than inferred; Depends-on converts TABLE 10 from a flat recommendation list into an execution plan. The Without-this-change column must be retained independently alongside Depends-on — no compression.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

- Without-this-change: name the component, failure mode, and threshold. WRONG: "Throttle errors will increase." PASS: "T-02 (SharePoint connector per-user quota): HTTP 429 storm affecting all flows sharing the service principal at 2x; flow run failure rate reaches 100% within [quota / 2x rate] minutes."
- Depends-on: MR-ID of prerequisite mitigation, or `--` if none.

Minimum: two PA-native remediations each mapped to a specific finding by T-NN, Path-ID, or Cascade-ID.

**Section 4.C — Tier-ID Coverage Audit**

*(The reason: C-12 enforces identifier consistency within each section but does not enforce downstream representation — a tier absent from TABLE 3 passes C-12 while creating a silent propagation gap.)*

For each T-NN in TABLE 1, verify it appears in each downstream section.

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section 3.D | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Any T-NN absent from a downstream section: annotate as COVERAGE GAP [T-NN → section name].

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call telemetry in Power Platform admin center, request usage dashboard. State the condition each signal surfaces and when it triggers.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State the impact: does the boundary shift any TABLE 9 row from SAFE to OVER-LIMIT or vice versa?

**Section 4.F — PA Construct Precision Pass**

*(Role 3 confirms exact documented PA term or flags for correction. The reason: "confirmed" is an assertion that the name matches PA documentation exactly — paraphrases and category names must be flagged here, not confirmed.)*

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

*Role: Precision Auditor (independent of all three ROUND 1 roles).*

**Independence:** ROUND 1's coherence across three roles — clean handoffs, complete cascade pairs, precise UX mappings — is not evidence of construct-level precision. A thorough, well-structured ROUND 1 analysis can still contain PA construct names drawn from paraphrase rather than documentation, rate units from estimates rather than platform sources, or cascade load estimates using directional language where numeric precision is required. ROUND 2 operates independently of ROUND 1 output quality.

**Scope extension:** Corrected construct names from TABLE 11 (Section 4.F) that replaced imprecise TABLE 1 entries are now in scope for ROUND 2 precision checking. These were excluded from ROUND 1 because ROUND 1 closed before TABLE 11 corrections were finalized.

---

For each T-NN row in TABLE 11, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term in PA documentation? Does it match the product-published limit source?
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

## V-02 — Output Format: Phase-Level Scorecard Headers

**Axis:** Output format — each phase opens with a PHASE SCORECARD block listing the criteria the phase must satisfy, with status cells initialized to `[ ]`. The scorecard is filled (`[PASS]` or `[FAIL: reason]`) after the phase's analytical content is produced but before the gate declaration fires. The analytical tables are structurally unchanged. Gate declarations (C-33 enumerated block, C-34 compound block) are unchanged — the scorecard is an additive format layer, not a replacement. Explicit constraint: scorecard update does NOT substitute for the gate declaration.

**Hypothesis:** v9 ceiling. The scorecard header is a format overlay; it does not displace gate declarations. C-33 evaluates the not-cleared block following the gate predicate — the scorecard block precedes the tables and does not interfere with gate position after phase content. C-34 evaluates the CORRECTION GATE block in Phase 4.F — scorecard format does not change Phase 4's table structure. Risk vector: a model may treat a `[PASS]` in the scorecard as the gate itself and omit the block-form gate declaration; prompt explicitly states "scorecard update does NOT substitute for gate declaration."

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

**Format instruction:** Each phase opens with a PHASE SCORECARD block. Cells are initialized `[ ]` and updated to `[PASS]` or `[FAIL: reason]` after the phase's analytical content is produced. Updating the scorecard does **NOT** substitute for the gate declaration — both must appear.

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 1 — Construct Inventory

**PHASE 1 SCORECARD** *(initialize now; update after producing TABLE 1 and QUOTA EXHAUSTION PROJECTION, before GATE 1)*

| Criterion | Status |
|-----------|--------|
| Every TABLE 1 row has exact PA construct type from domain list | [ ] |
| Every TABLE 1 row has numeric limit with unit | [ ] |
| Every TABLE 1 row has request contribution with arithmetic shown | [ ] |
| Every TABLE 1 row has populated Retry-After field | [ ] |
| Every HIT/SAT tier has QUOTA EXHAUSTION PROJECTION with arithmetic citing VOLUME ARITHMETIC 2x rate | [ ] |

**INERTIA CALLOUT — PHASE 1:** Nested action quotas and premium connector per-user windows do not appear in the flow canvas, only in platform documentation and admin center telemetry. These are the most frequently omitted constructs and the most common source of cascade failures discovered only in production.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers, producing internally inconsistent entries that make multi-volume sweep silent failures invisible by inspection.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if limit granularity differs from baseline units): `[show conversion factor]`

TABLE 1 STATUS columns must reference these three computed values. A STATUS column where all three bands are identical means VOLUME ARITHMETIC was not used — flag that row with `?`.

**TABLE 1 — Throttle Tier Map**
*(The reason for T-NN identifiers: each tier must be traceable by a stable short identifier through every downstream table and section.)*

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | (see QUOTA EXHAUSTION PROJECTION) |

Domain rule: PA construct types must be exact documented terms from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

---

**QUOTA EXHAUSTION PROJECTION**
*(The reason: this converts TABLE 1 `Failure visibility window` entries from assertions to verifiable depletion intervals.)*

For each T-NN with HIT or SAT status: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC.

---

*(Update PHASE 1 SCORECARD cells to `[PASS]` or `[FAIL: reason]` before evaluating GATE 1. Scorecard update does NOT substitute for the gate declaration below.)*

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

**PHASE 2 SCORECARD** *(initialize now; update after producing TABLE 2, TABLE 3, TABLE 4, and BURST SHAPE MATRIX, before GATE 2)*

| Criterion | Status |
|-----------|--------|
| TABLE 3 has >= 2 complete hops with named terminal state | [ ] |
| TABLE 4 has >= 2 tiers with distinct UX categories | [ ] |
| TABLE 2 has "why this order holds" explanation for each row | [ ] |
| BURST SHAPE MATRIX has f* computed as derived value from VOLUME ARITHMETIC and TABLE 1 | [ ] |
| Each BURST SHAPE MATRIX row has independent mechanism citation | [ ] |

**INERTIA CALLOUT — PHASE 2:** The first 429 in production is typically blamed on the most visible construct — usually the connector call — rather than the actual binding constraint. The real binding tier is often a per-user entitlement that accumulates across all flows sharing a principal, invisible from within a single flow's execution trace.

**Section 2.A — Rate Limit Hit Ordering**

*(The reason for the "naive assumption" sentence: it makes limits non-independence explicit, the structural cause of most cascade failures.)*

> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds].
> The naive assumption that limits are independent fails here because [cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| T-NN | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|------|--------------------------|-------|----------------------------------------|
| (bottleneck) | | | |
| (second hit) | | | |

**Section 2.B — Backpressure Hop Chain**

*(The reason for requiring a named terminal state: without it, the reader cannot determine whether the failure is user-visible or silently lost.)*

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops. Name the terminal state in the final row.

**Section 2.C — User Experience per Throttle Tier**

**INERTIA CALLOUT — SECTION 2.C:** The most common UX mapping error is reporting internal system state rather than what the user sees. A UX category entry that names system behavior without specifying the user-visible outcome is unverifiable by a PA runtime reviewer.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ across tiers.

**Section 2.D — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: arrival shape omission misses burst-triggered saturation events that nominal-volume planning cannot predict.)*

**LOAD SHAPE COMPARISON:** For each T-NN, state whether STATUS changes between UNIFORM and BURST arrival at the VOLUME ARITHMETIC 1x total volume. Positive: show numeric comparison grounded in TABLE 1 limit. Null: name the specific mechanism (per-minute bucket / per-second window / sliding window / token bucket) as the structural reason.

**BURST SHAPE MATRIX**
*(The reason for computing f* as a derived value: a matrix without the critical threshold is a descriptive survey, not a threshold-finding analysis.)*

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | below / above f* | SAFE / TRIGGERED | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

*(Update PHASE 2 SCORECARD cells to `[PASS]` or `[FAIL: reason]` before evaluating GATE 2. Scorecard update does NOT substitute for the gate declaration below.)*

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

**PHASE 3 SCORECARD** *(initialize now; update after producing TABLE 5, TABLE 6, TABLE 7, and Section 3.D STAGE 1/STAGE 2, before GATE 3)*

| Criterion | Status |
|-----------|--------|
| TABLE 7 has >= 2 cascade pairs with distinct T-NN Tier A / Tier B | [ ] |
| All TABLE 7 rows have stated throttle mechanism | [ ] |
| All TABLE 7 rows have severity and duration assessed | [ ] |
| Section 3.D STAGE 1 names >= 2 artifacts with structural reasons | [ ] |
| Section 3.D STAGE 2 has >= 2 GAP-NN entries with all four fields | [ ] |

**INERTIA CALLOUT — PHASE 3:** PA flows commonly deploy with `Apply to Each` at default concurrency, parallel branches with no fan-out cap, and high-frequency triggers with no debounce. The test environment typically runs at 10–20% of production concurrency, so these patterns are never surfaced before production.

**Section 3.A — Unprotected Burst Paths**

*(The reason for requiring a named component and structural gap: generic statements provide no actionable mitigation target.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. Explicit absence acknowledgment required if none found.

**Section 3.B — Retry-After Gap Table**

*(The reason for failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard is the basis for selecting a PA-native mitigation.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism linking each pair.

**Section 3.D — Test Coverage Gap Analysis**

**INERTIA CALLOUT — SECTION 3.D:** The integration test suite reports green because it uses mocked connector responses that suppress HTTP 429s. The load test runs at 10–20% of production concurrency. These structural properties mean the test suite cannot reach any of the throttle behaviors identified in PHASES 2–3. Naming these artifacts before filling gap entries prevents generic gap field entries.

#### STAGE 1 — Test Infrastructure Inertia Catalog

*(The reason: a model that has the specific artifact and its structural limitation in scope cannot produce generic Structural reason or Test approach fields without the failure being visible by inspection.)*

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property] |

WRONG: "Integration tests." PASS: "The nightly suite at `/tests/flow/connector.test.ts` uses `MockSharePointConnector.js` which suppresses all HTTP 429 responses regardless of call volume."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

*(The reason for the GAP-NN template: the template enforces completeness at the point of production without requiring a rubric audit.)*

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact and architectural property causing the miss]
- **Test approach:** [specific PA tooling step]

*(Continue GAP-NN entries for each additional gap.)*

*(Update PHASE 3 SCORECARD cells to `[PASS]` or `[FAIL: reason]` before evaluating GATE 3. Scorecard update does NOT substitute for the gate declaration below.)*

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all required fields populated, distinct T-NN Tier A / Tier B constructs, a named throttle mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and a completed STAGE 2 register with at least two GAP-NN entries each carrying all four fields with non-generic values.

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

**PHASE 4 SCORECARD** *(initialize now; update after producing TABLE 9, TABLE 10, TABLE 11, before CORRECTION GATE)*

| Criterion | Status |
|-----------|--------|
| TABLE 9 has arithmetic shown for at least one row | [ ] |
| TABLE 10 has >= 2 PA-native remediations with Without-this-change and Depends-on columns | [ ] |
| Every TABLE 11 row has explicit disposition | [ ] |
| Every TABLE 11 [FAIL] row has corrected content immediately below its annotation | [ ] |

**Section 4.A — Quantified Risk Register**

*(The reason for requiring arithmetic: OVER-LIMIT without arithmetic is indistinguishable from a guess.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.B — Mitigation Registry**

*(The reason for Without-this-change and Depends-on: urgency becomes explicit; the registry becomes an execution plan. The Without-this-change column must be retained independently alongside Depends-on — no compression.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

**Section 4.C — Tier-ID Coverage Audit**

*(The reason: a tier absent from TABLE 3 passes identifier consistency checks while creating a silent propagation gap.)*

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section 3.D | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Any T-NN absent from a downstream section: annotate as COVERAGE GAP [T-NN → section name].

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal and state the condition it surfaces and when it triggers.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 status row.

**Section 4.F — PA Construct Precision Pass**

*(The reason: "confirmed" is an assertion; paraphrases and category names must be flagged, not confirmed.)*

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row, write the corrected construct name, limit source, and precision note **immediately below the `[FAIL]` annotation** before any subsequent TABLE 11 row.

*(Update PHASE 4 SCORECARD cells to `[PASS]` or `[FAIL: reason]` before evaluating the CORRECTION GATE. Scorecard update does NOT substitute for the CORRECTION GATE declaration below.)*

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its `[FAIL]` annotation in the prescribed location.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and all remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

Describe at least one concrete PA-tooling test step. "Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

*Role: Connector support engineer.*

**Independence:** ROUND 1 flow architect output is not evidence of ROUND 2 precision. A thorough, scorecard-verified ROUND 1 analysis — with all scorecard cells marked [PASS] — can still contain PA construct names drawn from paraphrase rather than documentation. ROUND 2 operates independently of ROUND 1 scorecard status.

**Scope extension:** Corrected construct names from TABLE 11 that replaced imprecise TABLE 1 entries are now in scope. These were excluded from ROUND 1 because ROUND 1 closed before TABLE 11 corrections were finalized.

---

For each T-NN row in TABLE 11, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term in PA documentation?
2. **Numeric limit precision:** Is the limit value the documented platform limit or a derived estimate? State the source.
3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural (exact signal path + load calculation) or qualitative? Promote qualitative statements using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric projection or directional statement? Compute from TABLE 9 if directional.
3. **QUOTA EXHAUSTION PROJECTION precision:** Does each depletion interval cite the VOLUME ARITHMETIC 2x rate by name?

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Lifecycle Emphasis: Monitoring-Anchored

**Axis:** Lifecycle emphasis — Phase 1 is expanded with a Section 1.0 Observability Baseline (TABLE 0) that must be completed before TABLE 1. TABLE 0 declares what monitoring signals are already observable in the current PA environment for this flow. GATE 1 is extended to check TABLE 0 completion in addition to TABLE 1 requirements. Phase 4.D (Monitoring Signals) must explicitly cross-reference TABLE 0: for each signal recommended, state whether it was already active in TABLE 0, inactive, or newly recommended. Phase ordering is otherwise unchanged.

**Hypothesis:** v9 ceiling. The monitoring pre-declaration expands Phase 1's footprint but does not alter gate predicate structure. GATE 1 fires after both TABLE 0 and TABLE 1 are complete — the not-cleared block remains an enumerated list below the gate predicate, satisfying C-33. C-34 evaluates the CORRECTION GATE in Phase 4.F — unaffected by Phase 1 expansion. Risk vector: the model might conflate the TABLE 0 monitoring baseline with Phase 4.D and produce a truncated Phase 4.D; mitigated by requiring Phase 4.D to explicitly reference TABLE 0 entries by signal name.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system. This analysis is monitoring-anchored: before mapping throttle constructs, you declare what observability signals are already in place. This baseline governs what the monitoring and remediation sections must connect back to.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 1 — Construct Inventory

**INERTIA CALLOUT — PHASE 1:** Nested action quotas and premium connector per-user windows do not appear in the flow canvas, only in platform documentation and admin center telemetry. Omitting them from inventory is the most frequent source of cascade failures discovered only in production.

#### Section 1.0 — Observability Baseline *(complete before TABLE 1)*

*(The reason for completing TABLE 0 before TABLE 1: construct inventory decisions are influenced by what is already observable — a construct with active monitoring can be treated differently in mitigation planning than one with no telemetry.)*

Declare the current monitoring signals already available in the PA environment for this flow:

**TABLE 0 — Observability Baseline**

| Signal name | PA tooling surface | What it measures | Current visibility (active / inactive / unknown) |
|-------------|-------------------|-----------------|--------------------------------------------------|

List at minimum: flow run history status (throttled vs. failed vs. succeeded), any connector call telemetry in Power Platform admin center, and any request usage dashboard entries. If a signal is inactive or unknown, flag it — do not omit it. Phase 4.D must reference at least one TABLE 0 signal by name and state whether it was already active, inactive, or is newly recommended.

#### Section 1.1 — Throttle Construct Inventory

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers, producing internally inconsistent entries.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if limit granularity differs from baseline units): `[show conversion factor]`

TABLE 1 STATUS columns must reference these computed values. A STATUS column where all three bands are identical means VOLUME ARITHMETIC was not used — flag with `?`.

**TABLE 1 — Throttle Tier Map**
*(The reason for T-NN identifiers: each tier must be traceable by a stable short identifier through every downstream table and section.)*

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | (see QUOTA EXHAUSTION PROJECTION) |

Domain rule: PA construct types must be exact documented terms from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

---

**QUOTA EXHAUSTION PROJECTION**
*(The reason: converts TABLE 1 `Failure visibility window` entries from assertions to verifiable depletion intervals.)*

For each T-NN with HIT or SAT status: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC.

---

**GATE 1** is cleared when and only when TABLE 0 has at least three signals listed with current visibility declared; and every TABLE 1 row carries (a) an exact PA construct type from the domain list, (b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown, (d) a populated Retry-After field, and (e) every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- TABLE 0 has fewer than three signals listed, or any signal is missing a current visibility declaration
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

**INERTIA CALLOUT — PHASE 2:** The first 429 in production is typically blamed on the most visible construct rather than the actual binding constraint. The real binding tier is often a per-user entitlement accumulating across all flows sharing a principal, invisible from within a single flow's execution trace.

**Section 2.A — Rate Limit Hit Ordering**

*(The reason for the "naive assumption" sentence: it makes limits non-independence explicit, the structural cause of most cascade failures.)*

> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason].
> The naive assumption that limits are independent fails here because [cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| T-NN | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|------|--------------------------|-------|----------------------------------------|
| (bottleneck) | | | |
| (second hit) | | | |

**Section 2.B — Backpressure Hop Chain**

*(The reason for requiring a named terminal state: without it, the reader cannot determine whether the failure is user-visible or silently lost.)*

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops. Name the terminal state in the final row.

**Section 2.C — User Experience per Throttle Tier**

**INERTIA CALLOUT — SECTION 2.C:** The most common UX mapping error is reporting internal system state rather than what the user sees. Each TABLE 4 row must state the user-visible experience — not the system action.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ across tiers.

**Section 2.D — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: arrival shape omission misses burst-triggered saturation events that nominal-volume planning cannot predict.)*

**LOAD SHAPE COMPARISON:** For each T-NN, state whether STATUS changes between UNIFORM and BURST arrival at the VOLUME ARITHMETIC 1x total volume. Positive: numeric comparison grounded in TABLE 1. Null: name the specific mechanism as the structural reason.

**BURST SHAPE MATRIX**
*(The reason for computing f* as a derived value: a matrix without the critical threshold is a descriptive survey, not a threshold-finding analysis.)*

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | SAFE / TRIGGERED | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

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

**INERTIA CALLOUT — PHASE 3:** PA flows commonly deploy with `Apply to Each` at default concurrency, parallel branches with no fan-out cap, and high-frequency triggers with no debounce. These are structural burst sources invisible from the flow canvas that test environments running at 10–20% of production concurrency never surface.

**Section 3.A — Unprotected Burst Paths**

*(The reason for requiring a named component and structural gap: generic statements provide no actionable mitigation target.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. Explicit absence acknowledgment required.

**Section 3.B — Retry-After Gap Table**

*(The reason for failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard is the basis for selecting a PA-native mitigation.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism linking each pair.

**Section 3.D — Test Coverage Gap Analysis**

**INERTIA CALLOUT — SECTION 3.D:** The integration test suite reports green because it uses mocked connector responses that suppress HTTP 429s. The load test runs at 10–20% of production concurrency. Naming these artifacts before filling gap entries prevents generic Structural reason and Test approach fields.

#### STAGE 1 — Test Infrastructure Inertia Catalog

*(The reason: a model with specific artifact and structural limitation in scope cannot produce generic fields without the failure being visible by inspection.)*

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property] |

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

*(The reason for the GAP-NN template: enforces completeness at the point of production.)*

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact and architectural property]
- **Test approach:** [specific PA tooling step]

*(Continue GAP-NN entries for each additional gap.)*

---

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all required fields populated, distinct T-NN Tier A / Tier B constructs, a named throttle mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and a completed STAGE 2 register with at least two GAP-NN entries each carrying all four fields with non-generic values.

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

*(The reason: OVER-LIMIT without arithmetic is indistinguishable from a guess.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.B — Mitigation Registry**

*(The reason for Without-this-change and Depends-on: urgency becomes explicit; the registry becomes an execution plan. Without-this-change must be retained independently — no compression.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

**Section 4.C — Tier-ID Coverage Audit**

*(The reason: a tier absent from TABLE 3 creates a silent propagation gap that passes identifier consistency checks.)*

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section 3.D | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Any T-NN absent: annotate as COVERAGE GAP [T-NN → section name].

**Section 4.D — Monitoring Signals (with TABLE 0 cross-reference)**

*(The reason for TABLE 0 cross-reference: a monitoring recommendation that duplicates an already-active signal wastes remediation effort; a recommendation that activates an already-declared-inactive signal is higher priority than a net-new signal.)*

For each PA-observable signal recommended: state whether it appears in TABLE 0 as active, inactive, or is newly recommended. At least one TABLE 0 signal must be explicitly referenced by name. Flag any TABLE 0 inactive signal that would have surfaced the Phase 2 binding bottleneck as a missed-signal gap.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 status row.

**Section 4.F — PA Construct Precision Pass**

*(The reason: "confirmed" is an assertion; paraphrases and category names must be flagged, not confirmed.)*

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row, write the corrected construct name, limit source, and precision note **immediately below the `[FAIL]` annotation** before any subsequent TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its `[FAIL]` annotation in the prescribed location.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and all remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

Describe at least one concrete PA-tooling test step.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

*Role: Connector support engineer.*

**Independence:** ROUND 1 output — including TABLE 0 monitoring baseline — is not evidence of ROUND 2 precision. A flow architect can declare an active monitoring signal in TABLE 0 while using an imprecise PA construct name in TABLE 1. ROUND 2 operates independently.

**Scope extension:** Corrected construct names from TABLE 11 are now in scope.

---

For each T-NN in TABLE 11, apply precision checks:

1. **PA construct name precision:** Exact PA documentation term?
2. **Numeric limit precision:** Documented platform limit or derived estimate? State the source.
3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement granularity.

For each cascade pair in TABLE 7:

1. **Causal mechanism precision:** Structural or qualitative? Promote qualitative statements using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric projection or directional statement? Compute from TABLE 9 if directional.
3. **QUOTA EXHAUSTION PROJECTION precision:** Does each depletion interval cite the VOLUME ARITHMETIC 2x rate by name?

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Phrasing Register: Formal/Technical Imperative + ASSUMPTION GAP Inertia Framing

**Axis:** Phrasing register — formal/technical imperative throughout: instructions use declarative imperative form ("Identify every throttle-relevant construct"; "Produce TABLE 1 before proceeding"; "The analyst shall flag any row...") rather than second-person advisory ("you will/should"). No conversational asides. Additionally: each section with identified inertia risk opens with an ASSUMPTION GAP block that names the status-quo assumption being displaced and states the structural consequence of leaving it unchallenged. The ASSUMPTION GAP form is more explicit than an inertia callout: it names (a) what the standard approach assumes, (b) why that assumption fails here, and (c) what the gap analysis replaces.

**Hypothesis:** v9 ceiling. Phrasing register controls instruction delivery style — formal vs. conversational — not gate declaration structure. C-33 evaluates whether not-cleared conditions appear as an enumerated list block; register does not affect block structure. C-34 evaluates the CORRECTION GATE compound block; formal register produces the same block structure as conversational. Risk vector: formal terse register might compress gate not-cleared blocks into single dense sentences; mitigated by explicit instruction that gate declarations use enumerated list form.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across a rate-limited Power Automate system. Produce all outputs in formal/technical imperative register.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

**Register instruction:** Use declarative imperative form throughout. Avoid second-person advisory phrasing. Gate declarations use enumerated-list block form regardless of register.

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 1 — Construct Inventory

**ASSUMPTION GAP — PHASE 1:** Standard throttle analyses assume that all rate-limiting constructs are visible in the flow canvas. This assumption fails: nested action quotas and premium connector per-user windows appear only in platform documentation and admin center telemetry. Gap: the standard approach produces an incomplete construct inventory that discovers cascade failures only in production. This analysis replaces the canvas-inspection assumption with documentation-sourced construct enumeration.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers, making multi-volume sweep silent failures invisible by inspection.)*

Compute the following before filling TABLE 1:

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if limit granularity differs from baseline units): `[show conversion factor]`

TABLE 1 STATUS columns shall reference these three computed values. A STATUS column with identical 1x/2x/5x entries indicates VOLUME ARITHMETIC was not applied — flag that row with `?`.

**TABLE 1 — Throttle Tier Map**
*(The reason for T-NN identifiers: each tier must be traceable by a stable short identifier through every downstream table and section; synonym-based matching produces silent audit failures.)*

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | (see QUOTA EXHAUSTION PROJECTION) |

Domain rule *(the reason: a generic term cannot be matched to a documented limit, breaking TABLE 9 arithmetic traceability)*: each PA construct type shall be drawn exactly from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

WRONG: "API rate limit."
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)."

---

**QUOTA EXHAUSTION PROJECTION**
*(The reason: converts TABLE 1 `Failure visibility window` entries from assertions to arithmetic-backed depletion intervals.)*

For each T-NN with HIT or SAT status: derive `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x load."
PASS: "T-01: 40,000 req quota / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion at 2x nominal."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) an exact PA construct type from the domain list, (b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown, (d) a populated Retry-After field, and (e) every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type rather than an exact PA term
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic shown
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation citing the VOLUME ARITHMETIC 2x rate

Flag rows in any of the above failure states with `?` and correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**ASSUMPTION GAP — PHASE 2:** Standard bottleneck analyses assume that the first construct to emit a 429 is the binding constraint. This assumption fails: the binding tier is frequently a per-user entitlement that accumulates across all flows sharing a service principal, invisible from within a single flow's execution trace. Gap: the standard approach produces incorrect bottleneck attribution and ineffective mitigations. This analysis replaces single-flow attribution with principal-pool-aware ordering.

**Section 2.A — Rate Limit Hit Ordering**

Produce the bottleneck statement in the following form:
*(The reason for the "naive assumption" sentence: it makes limits non-independence explicit, the structural cause of most cascade failures.)*

> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds].
> The naive assumption that limits are independent fails here because [cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| T-NN | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|------|--------------------------|-------|----------------------------------------|
| (bottleneck) | | | |
| (second hit) | | | |

**Section 2.B — Backpressure Hop Chain**

*(The reason for requiring a named terminal state: a propagation trace without a terminal state leaves the reader unable to determine whether the failure is user-visible or silently lost.)*

Produce TABLE 3 with minimum two complete hops and an explicit terminal state in the final row.

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Signal types: error code / retry-after header / queue depth increase / other.

**Section 2.C — User Experience per Throttle Tier**

**ASSUMPTION GAP — SECTION 2.C:** Standard UX mapping assumes that system behavior descriptions (queue depth increases, retry loop activates) constitute user experience entries. This assumption fails: system-internal descriptions are unverifiable by a PA runtime reviewer and do not capture what the user observes. Gap: the standard approach produces UX entries that cannot be validated against production runtime. This analysis replaces system-state descriptions with user-observable outcome statements.

Produce TABLE 4. Each row shall state the user-visible experience — not the system action.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories shall differ across tiers.

**Section 2.D — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: the same total request volume produces different throttle outcomes when concentrated versus distributed; omitting arrival shape analysis misses burst-triggered saturation events invisible to nominal-volume planning.)*

Produce the LOAD SHAPE COMPARISON: for each T-NN, state whether STATUS changes between UNIFORM and BURST arrival at the VOLUME ARITHMETIC 1x total volume. Positive case: numeric comparison grounded in TABLE 1 limit. Null case: name the specific rate limit mechanism (per-minute bucket / per-second window / sliding window / token bucket) as the structural reason.

Derive f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit, from VOLUME ARITHMETIC and TABLE 1.
*(The reason for computing f* as a derived value: a matrix without the critical threshold is a descriptive survey, not a threshold-finding analysis.)*

**BURST SHAPE MATRIX**

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | below / above f* | SAFE / TRIGGERED | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row shall carry an independent mechanism citation.

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

**ASSUMPTION GAP — PHASE 3:** Standard test coverage assessments assume that integration tests and load tests collectively reach throttle behaviors. This assumption fails: integration test suites that use mocked connectors suppress all HTTP 429 responses; load tests running at 10–20% of production concurrency cannot reach saturation thresholds. Gap: the standard approach produces a green test suite that cannot detect any of the throttle behaviors identified in Phases 2–3. This analysis replaces the green-suite assumption with artifact-named structural miss analysis.

**Section 3.A — Unprotected Burst Paths**

*(The reason for requiring a named component and structural gap: generic statements provide no actionable mitigation target.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Examine: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. Produce explicit absence acknowledgment naming at least two specific guards if no paths are found.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement applies at the environment level via [mechanism] at [location]; T-03's per-second window enforces at the connector action level with no bypass path through the [construct] action."

**Section 3.B — Retry-After Gap Table**

*(The reason for failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard is the basis for selecting a PA-native mitigation.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap is required.

**Section 3.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism linking each pair. A flat list of independent throttle risks does not pass.

**Section 3.D — Test Coverage Gap Analysis**

**ASSUMPTION GAP — SECTION 3.D:** Standard test gap analyses identify missing test cases without naming the specific artifacts that structurally prevent those cases from reaching throttle behaviors. This assumption fails: a gap labeled "integration tests miss this" without naming the artifact and architectural property producing the miss is unactionable and unfalsifiable. Gap: the standard approach produces gap entries that a model can populate generically without inspection failure. This analysis replaces category-level gap declarations with artifact-named structural miss records.

#### STAGE 1 — Test Infrastructure Inertia Catalog

*(The reason: a model with specific artifact and limitation in scope cannot produce generic Structural reason or Test approach fields without the failure being visible by inspection.)*

Name at least two specific existing test infrastructure artifacts that structurally cannot reach the throttle behaviors identified above. For each, state the architectural property causing the miss — not the test category.

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property] |

WRONG: "Integration tests" — category, not artifact.
PASS: "The nightly suite at `/tests/flow/connector.test.ts` uses `MockSharePointConnector.js` which suppresses all HTTP 429 responses regardless of call volume."

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

*(The reason for the GAP-NN template: the template enforces completeness at the point of production, making generic entries structurally visible as failures before any rubric audit.)*

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact and architectural property]
- **Test approach:** [specific PA tooling step — not "add load testing"]

*(Continue GAP-NN entries for each additional gap.)*

---

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all required fields populated, distinct T-NN Tier A / Tier B constructs, a named throttle mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and a completed STAGE 2 register with at least two GAP-NN entries each carrying all four fields with non-generic values.

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

*(The reason for requiring arithmetic: OVER-LIMIT without arithmetic is indistinguishable from a guess; arithmetic makes the status a verifiable claim anchored to TABLE 1 limits and VOLUME ARITHMETIC rates.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Arithmetic is required for at least one row.

**Section 4.B — Mitigation Registry**

*(The reason for `Source`, `Without this change`, and `Depends-on` columns: Source makes the mitigation traceable; Without-this-change makes urgency explicit; Depends-on converts the registry into an execution plan. The Without-this-change column shall be retained independently alongside Depends-on — no compression.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

Without-this-change: name the component, failure mode, and threshold. WRONG: "Throttle errors will increase." PASS: "T-02 (SharePoint connector per-user quota): HTTP 429 storm affecting all flows sharing the service principal at 2x; flow run failure rate reaches 100% within [quota / 2x rate] minutes."

**Section 4.C — Tier-ID Coverage Audit**

*(The reason: a tier absent from TABLE 3 creates a silent propagation gap that passes identifier consistency checks.)*

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section 3.D | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Annotate any T-NN absent from a downstream section as COVERAGE GAP [T-NN → section name].

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal. State the condition each signal surfaces and the trigger condition.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 row from SAFE to OVER-LIMIT or vice versa.

**Section 4.F — PA Construct Precision Pass**

*(The reason: "confirmed" is an assertion that the name matches PA documentation exactly — paraphrases and category names shall be flagged here, not confirmed.)*

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row, produce the corrected construct name, limit source, and precision note **immediately below the `[FAIL]` annotation** before any subsequent TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its `[FAIL]` annotation in the prescribed location.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and all remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

Produce at least one concrete test step using PA tooling. "Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

*Role: Connector support engineer.*

**Independence:** ROUND 1 analytical coherence — including formal documentation of ASSUMPTION GAPs — is not evidence of construct-level precision. A formally documented ROUND 1 can still contain PA construct names drawn from paraphrase rather than PA documentation. ROUND 2 operates independently of ROUND 1 output quality.

**Scope extension:** Corrected construct names from TABLE 11 are now in scope.

---

For each T-NN row in TABLE 11, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term in PA documentation?
2. **Numeric limit precision:** Is the limit value the documented platform limit or a derived estimate? State the source.
3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement granularity.

For each cascade pair in TABLE 7:

1. **Causal mechanism precision:** Structural or qualitative? Promote qualitative statements using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric projection or directional statement? Compute from TABLE 9 if directional.
3. **QUOTA EXHAUSTION PROJECTION precision:** Does each depletion interval cite the VOLUME ARITHMETIC 2x rate by name?

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — Three-Axis: Three-Role Cascade + Monitoring-Anchored + Scorecard Format

**Axis:** Combined — three simultaneous structural overlays: (1) three-role cascade (connector specialist → throughput analyst → PA admin) from V-01; (2) monitoring-anchored lifecycle with TABLE 0 in Phase 1 from V-03; (3) phase-level scorecard headers from V-02. Each overlay is independently satisfied; no overlay displaces another. Gate declarations (C-33 enumerated blocks, C-34 compound block) remain structurally unchanged beneath all three overlays.

**Hypothesis:** v9 ceiling. The three overlays affect role attribution, Phase 1 footprint, and scorecard format respectively — none of these dimensions affects gate declaration syntax. C-33 evaluates whether each gate's not-cleared block is an independent enumerated list — this is independent of which role holds the gate, whether Phase 1 includes TABLE 0, and whether a scorecard precedes the phase content. C-34 evaluates the CORRECTION GATE compound block — owned by Role 3, appearing after TABLE 11, unchanged by scorecard format. Risk vectors: (a) combined role+scorecard load may cause the model to treat the Phase N scorecard `[PASS]` as the gate substitute (scorecard-not-gate risk); (b) TABLE 0 in Phase 1 may expand GATE 1 beyond the model's attention for the gate block form (gate displacement risk); (c) three-role handoffs may fragment phase ownership of the not-cleared blocks. All three risks are mitigated explicitly in the prompt.

---

You are simulating throughput across a rate-limited Power Automate system using a three-role analyst team with a monitoring-anchored Phase 1 and phase-level scorecards throughout.

**Role assignments:**
- **Role 1 — Connector Specialist:** Executes PHASE 1. Owns TABLE 0 observability baseline, VOLUME ARITHMETIC, TABLE 1 construct inventory, and QUOTA EXHAUSTION PROJECTION.
- **Role 2 — Throughput Analyst:** Executes PHASES 2 and 3. Owns bottleneck ordering, backpressure propagation, UX mapping, BURST SHAPE MATRIX, and cascade risk register. Accepts TABLE 0 and TABLE 1 as inputs — does not re-evaluate Role 1's construct names.
- **Role 3 — Power Platform Admin:** Executes PHASE 4. Owns PA construct validation, quantified risk, mitigation registry, monitoring signal recommendations (with TABLE 0 cross-reference), license/entitlement boundary, and test approach. Carries the CORRECTION GATE.

**Format instruction:** Each phase opens with a PHASE SCORECARD block. Cells are initialized `[ ]` and updated to `[PASS]` or `[FAIL: reason]` after the phase's analytical content is produced. Updating the scorecard does **NOT** substitute for the gate declaration — both must appear.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

*Role: Connector Specialist.*

**PHASE 1 SCORECARD** *(initialize now; update after TABLE 0, TABLE 1, and QUOTA EXHAUSTION PROJECTION, before GATE 1)*

| Criterion | Status |
|-----------|--------|
| TABLE 0 has >= 3 signals with current visibility declared | [ ] |
| Every TABLE 1 row has exact PA construct type from domain list | [ ] |
| Every TABLE 1 row has numeric limit with unit | [ ] |
| Every TABLE 1 row has request contribution with arithmetic shown | [ ] |
| Every TABLE 1 row has populated Retry-After field | [ ] |
| Every HIT/SAT tier has QUOTA EXHAUSTION PROJECTION with arithmetic citing VOLUME ARITHMETIC 2x rate | [ ] |

**INERTIA CALLOUT — PHASE 1:** Nested action quotas and premium connector per-user windows do not appear in the flow canvas — only in platform documentation and admin center telemetry. Omitting them from inventory is the most frequent source of cascade failures discovered only in production.

#### Section 1.0 — Observability Baseline *(complete before TABLE 1)*

*(The reason for completing TABLE 0 before TABLE 1: construct inventory decisions are influenced by what is already observable — a construct with active monitoring can be treated differently in mitigation planning than one with no telemetry.)*

**TABLE 0 — Observability Baseline**

| Signal name | PA tooling surface | What it measures | Current visibility (active / inactive / unknown) |
|-------------|-------------------|-----------------|--------------------------------------------------|

List at minimum: flow run history status (throttled vs. failed vs. succeeded), any connector call telemetry in Power Platform admin center, and any request usage dashboard entries. Flag inactive or unknown signals — do not omit them. Phase 4.D must reference at least one TABLE 0 signal by name.

#### Section 1.1 — Throttle Construct Inventory

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers, making multi-volume sweep silent failures invisible by inspection.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if limit granularity differs): `[show conversion factor]`

TABLE 1 STATUS columns must reference these computed values. Identical 1x/2x/5x entries indicate VOLUME ARITHMETIC was not applied — flag with `?`.

**TABLE 1 — Throttle Tier Map**
*(The reason for T-NN identifiers: each tier must be traceable through every downstream table and section by stable short identifier.)*

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | (see QUOTA EXHAUSTION PROJECTION) |

Domain rule: PA construct types must be exact documented terms from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

---

**QUOTA EXHAUSTION PROJECTION**
*(The reason: converts TABLE 1 `Failure visibility window` entries from assertions to arithmetic-backed depletion intervals.)*

For each T-NN with HIT or SAT status: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC by name.

---

*(Update PHASE 1 SCORECARD cells before evaluating GATE 1. Scorecard update does NOT substitute for the gate declaration below.)*

**GATE 1** is cleared when and only when TABLE 0 has at least three signals listed with current visibility declared; and every TABLE 1 row carries (a) an exact PA construct type from the domain list, (b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown, (d) a populated Retry-After field, and (e) every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- TABLE 0 has fewer than three signals listed, or any signal is missing a current visibility declaration
- Any T-NN row uses a generic or undocumented construct type rather than an exact PA term
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic shown
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation citing the VOLUME ARITHMETIC 2x rate

Rows in any of the above failure states receive a `?` flag — Role 1 corrects before handing off to Role 2.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*Role: Throughput Analyst. (Role 1 handoff complete — GATE 1 cleared.)*

*(GATE 1 must pass before this phase executes.)*

**PHASE 2 SCORECARD** *(initialize now; update after TABLE 2, TABLE 3, TABLE 4, and BURST SHAPE MATRIX, before GATE 2)*

| Criterion | Status |
|-----------|--------|
| TABLE 3 has >= 2 complete hops with named terminal state | [ ] |
| TABLE 4 has >= 2 tiers with distinct UX categories | [ ] |
| TABLE 2 has "why this order holds" explanation for each row | [ ] |
| BURST SHAPE MATRIX has f* computed as derived value | [ ] |
| Each BURST SHAPE MATRIX row has independent mechanism citation | [ ] |

**INERTIA CALLOUT — PHASE 2:** The first 429 in production is typically blamed on the most visible construct rather than the actual binding constraint. The real binding tier is often a per-user entitlement accumulating across all flows sharing a principal, invisible from within a single flow's execution trace.

**Section 2.A — Rate Limit Hit Ordering**

*(The reason for the "naive assumption" sentence: it makes limits non-independence explicit, the structural cause of most cascade failures.)*

> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason].
> The naive assumption that limits are independent fails here because [cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| T-NN | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|------|--------------------------|-------|----------------------------------------|
| (bottleneck) | | | |
| (second hit) | | | |

**Section 2.B — Backpressure Hop Chain**

*(The reason for requiring a named terminal state: without it, the reader cannot determine whether the failure is user-visible or silently lost.)*

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops. Name the terminal state in the final row.

**Section 2.C — User Experience per Throttle Tier**

**INERTIA CALLOUT — SECTION 2.C:** The most common UX mapping error is reporting internal system state rather than what the user sees. Each TABLE 4 row must state the user-visible experience.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ across tiers.

**Section 2.D — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: arrival shape omission misses burst-triggered saturation events invisible to nominal-volume planning.)*

**LOAD SHAPE COMPARISON:** For each T-NN, state whether STATUS changes between UNIFORM and BURST at the VOLUME ARITHMETIC 1x total volume. Positive: numeric comparison grounded in TABLE 1. Null: name the specific mechanism as the structural reason.

**BURST SHAPE MATRIX**
*(The reason for computing f* as a derived value: a matrix without the critical threshold is a descriptive survey, not a threshold-finding analysis.)*

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | SAFE / TRIGGERED | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

*(Update PHASE 2 SCORECARD cells before evaluating GATE 2. Scorecard update does NOT substitute for the gate declaration below.)*

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

*Role: Throughput Analyst (continued). (GATE 2 cleared.)*

*(GATE 2 must pass before this phase executes.)*

**PHASE 3 SCORECARD** *(initialize now; update after TABLE 5, TABLE 6, TABLE 7, and Section 3.D STAGE 1/STAGE 2, before GATE 3)*

| Criterion | Status |
|-----------|--------|
| TABLE 7 has >= 2 cascade pairs with distinct T-NN Tier A / Tier B | [ ] |
| All TABLE 7 rows have stated throttle mechanism | [ ] |
| All TABLE 7 rows have severity and duration assessed | [ ] |
| Section 3.D STAGE 1 names >= 2 artifacts with structural reasons | [ ] |
| Section 3.D STAGE 2 has >= 2 GAP-NN entries with all four fields | [ ] |

**INERTIA CALLOUT — PHASE 3:** PA flows commonly deploy with `Apply to Each` at default concurrency, parallel branches with no fan-out cap, and high-frequency triggers with no debounce. Test environments running at 10–20% of production concurrency never surface these patterns.

**Section 3.A — Unprotected Burst Paths**

*(The reason for requiring a named component and structural gap: generic statements provide no actionable mitigation target.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. Explicit absence acknowledgment required.

**Section 3.B — Retry-After Gap Table**

*(The reason for failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard is the basis for selecting a PA-native mitigation.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism linking each pair.

**Section 3.D — Test Coverage Gap Analysis**

**INERTIA CALLOUT — SECTION 3.D:** The integration test suite reports green because it uses mocked connector responses that suppress HTTP 429s. The load test runs at 10–20% of production concurrency. Naming these artifacts before gap entries prevents generic Structural reason and Test approach fields.

#### STAGE 1 — Test Infrastructure Inertia Catalog

*(The reason: a model with specific artifact and limitation in scope cannot produce generic fields without the failure being visible by inspection.)*

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property] |

**STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

*(The reason for the GAP-NN template: enforces completeness at the point of production.)*

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names STAGE 1 artifact and architectural property]
- **Test approach:** [specific PA tooling step]

*(Continue GAP-NN entries for each additional gap.)*

*(Update PHASE 3 SCORECARD cells before evaluating GATE 3. Scorecard update does NOT substitute for the gate declaration below.)*

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all required fields populated, distinct T-NN Tier A / Tier B constructs, a named throttle mechanism, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and a completed STAGE 2 register with at least two GAP-NN entries each carrying all four fields with non-generic values.

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

*Role: Power Platform Admin. (Role 2 handoff complete — GATE 3 cleared.)*

*Role 3 mandate: PA construct validation, quantified risk, PA-native remediations, monitoring signals (with TABLE 0 cross-reference), license/entitlement boundary, test approach. The CORRECTION GATE is owned by Role 3.*

*(GATE 3 must pass before this phase executes.)*

**PHASE 4 SCORECARD** *(initialize now; update after TABLE 9, TABLE 10, TABLE 11, before CORRECTION GATE)*

| Criterion | Status |
|-----------|--------|
| TABLE 9 has arithmetic shown for at least one row | [ ] |
| TABLE 10 has >= 2 PA-native remediations with Without-this-change and Depends-on | [ ] |
| Phase 4.D references at least one TABLE 0 signal by name | [ ] |
| Every TABLE 11 row has explicit disposition | [ ] |
| Every TABLE 11 [FAIL] row has corrected content immediately below its annotation | [ ] |

**Section 4.A — Quantified Risk Register**

*(The reason: OVER-LIMIT without arithmetic is indistinguishable from a guess.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Arithmetic required for at least one row.

**Section 4.B — Mitigation Registry**

*(The reason for Without-this-change and Depends-on: urgency becomes explicit; registry becomes an execution plan. Without-this-change must be retained independently — no compression.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

**Section 4.C — Tier-ID Coverage Audit**

*(The reason: a tier absent from TABLE 3 creates a silent propagation gap passing identifier consistency checks.)*

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section 3.D | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Annotate any T-NN absent from a downstream section as COVERAGE GAP [T-NN → section name].

**Section 4.D — Monitoring Signals (with TABLE 0 cross-reference)**

*(The reason for TABLE 0 cross-reference: a monitoring recommendation duplicating an active signal wastes remediation effort; activating an inactive signal already in TABLE 0 is higher priority than a net-new signal.)*

For each PA-observable signal recommended: state whether it appears in TABLE 0 as active, inactive, or is newly recommended. At least one TABLE 0 signal must be explicitly referenced by name. Flag any TABLE 0 inactive signal that would have surfaced the Phase 2 binding bottleneck as a missed-signal gap.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary materially shifting a TABLE 9 row.

**Section 4.F — PA Construct Precision Pass**

*(The reason: "confirmed" is an assertion; paraphrases must be flagged, not confirmed.)*

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row, write the corrected construct name, limit source, and precision note **immediately below the `[FAIL]` annotation** before any subsequent TABLE 11 row.

*(Update PHASE 4 SCORECARD cells before evaluating the CORRECTION GATE. Scorecard update does NOT substitute for the CORRECTION GATE declaration below.)*

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its `[FAIL]` annotation in the prescribed location.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have a corrected construct name, limit source, and precision note immediately below its `[FAIL]` annotation

*TABLE 12 and all remaining sections are blocked until the CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

Describe at least one concrete PA-tooling test step.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS

*Role: Precision Auditor (independent of all three ROUND 1 roles).*

**Independence:** ROUND 1 coherence across three roles — clean scorecard cells, complete TABLE 0, complete TABLE 11 corrections — is not evidence of construct-level precision. A well-structured ROUND 1 with all scorecard cells marked [PASS] can still contain PA construct names drawn from paraphrase. ROUND 2 operates independently of ROUND 1 output quality.

**Scope extension:** Corrected construct names from TABLE 11 are now in scope.

---

For each T-NN row in TABLE 11, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term in PA documentation?
2. **Numeric limit precision:** Documented platform limit or derived estimate? State the source.
3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement granularity.

For each cascade pair in TABLE 7:

1. **Causal mechanism precision:** Structural or qualitative? Promote qualitative statements using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric projection or directional statement? Compute from TABLE 9 if directional.
3. **QUOTA EXHAUSTION PROJECTION precision:** Does each depletion interval cite the VOLUME ARITHMETIC 2x rate by name?

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*

---

## R10 Structural Checklist (verify before scoring)

For each variation, confirm C-33/C-34 structures are present and intact:

| Check | V-01 | V-02 | V-03 | V-04 | V-05 |
|-------|------|------|------|------|------|
| GATE 1 enumerated not-cleared block (5 items) | yes | yes | yes (6 items — TABLE 0 + 5 TABLE 1) | yes | yes (6 items) |
| GATE 2 enumerated not-cleared block (5 items) | yes | yes | yes | yes | yes |
| GATE 3 enumerated not-cleared block (6 items) | yes | yes | yes | yes | yes |
| CORRECTION GATE compound not-cleared block (2 items: disposition + spatial) | yes | yes | yes | yes | yes |
| No gate uses inline dash-append for multiple failure conditions | yes | yes | yes | yes | yes |
| Scorecard update explicitly does NOT substitute for gate declaration (V-02, V-05) | N/A | yes | N/A | N/A | yes |
| TABLE 0 present before TABLE 1 (V-03, V-05) | N/A | N/A | yes | N/A | yes |
| Phase 4.D cross-references TABLE 0 by signal name (V-03, V-05) | N/A | N/A | yes | N/A | yes |
| Formal register throughout, ASSUMPTION GAP blocks per section (V-04) | N/A | N/A | N/A | yes | N/A |
| Three named role markers with explicit handoff declarations (V-01, V-05) | yes | N/A | N/A | N/A | yes |
| ROUND 2 with independence declaration present in all variations | yes | yes | yes | yes | yes |
