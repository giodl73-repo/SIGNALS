# flow-throttle Skill Body — Round 11 Complete Variations
**Date:** 2026-03-15
**Rubric:** v10 (C-01 through C-36; denominator 24)
**Baseline ceiling:** R10 V-04 (formal/technical imperative + ASSUMPTION GAP blocks in 4 sections + 4 WRONG/PASS exemplar sections; 24/24 aspirational, composite 100)

---

## Round 11 Analysis

**R10 confirmed:**
- C-35: WRONG/PASS exemplars in 3+ independent sections survive 3-role cascade and formal register. V-01 carried 3 exemplar sections (quota exhaustion, domain rule, absence form); V-04 carried 4 (adding mitigation urgency). V-02 carried 2 (insufficient). V-03 and V-05 carried zero.
- C-36: ASSUMPTION GAP three-part blocks (a: assumption displaced, b: structural failure reason, c: replacement analysis element) survive formal/technical register when explicitly declared per section. V-04 was the only R10 variation carrying C-36 → the only at 100. All others: 99 or 98.
- Confirmed: C-35 and C-36 are section-level structural declarations. Their presence in the prompt determines their presence in output. They do not depend on role count, phase count, or output format.

**What R10 did NOT test (for the C-35 + C-36 combination):**
- 2-role function split (evidence-compile vs. analysis-synthesize) with both C-35 + C-36 — R10 tested 3-role (V-01, C-35 only) and single-implicit-role (V-04, both)
- Prose-primary analytical sections (Phase 2 as narrative prose) with ASSUMPTION GAP blocks — R10 V-02 tested scorecard format without ASSUMPTION GAP
- Phase lifecycle reordering (exposure before bottleneck analysis) with C-35 + C-36 — untested
- ASSUMPTION GAP density above 4 blocks (Phase 0 risk forecast adding a 5th) — untested
- Combined: lifecycle reordering + maximum ASSUMPTION GAP density

**R11 design hypothesis:** C-35 and C-36 are axis-inert across role count, output format, and phase ordering when explicitly declared. Any variation placing ASSUMPTION GAP blocks and WRONG/PASS exemplars at their designated sections will carry both criteria. Expected: all five at v10 ceiling (100).

---

## Round 11 Variation Map

| Variation | Axes | C-35 | C-36 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Role sequence: 2-role evidence-to-analysis function split | PASS | PASS | v10 ceiling |
| V-02 | Output format: prose-primary Phase 2 + Phase 3 analytical sections | PASS | PASS | v10 ceiling |
| V-03 | Lifecycle emphasis: exposure-before-analysis phase reordering | PASS | PASS | v10 ceiling |
| V-04 | Role sequence (2-role) + output format (prose-primary) combined | PASS | PASS | v10 ceiling |
| V-05 | Lifecycle reordering + Phase 0 risk forecast (5 ASSUMPTION GAP blocks, 5 exemplar sections) | PASS | PASS | v10 ceiling |

Risk vectors: V-01 tests whether Role 2's larger scope (Phases 2–4 in one role) causes ASSUMPTION GAP blocks to be treated as a single preamble rather than per-section openers; V-02 tests whether prose-primary format reduces WRONG/PASS block visibility or causes C-16 domain rule exemplar omission; V-03 tests whether phase reordering displaces GATE preconditions (exposure findings must feed into bottleneck analysis, not replace it); V-04 tests combined-axis interference under prose-primary + 2-role load; V-05 tests whether Phase 0 competes with Phase 1's ASSUMPTION GAP for C-36 credit, and whether 5 exemplar sections diffuses model attention per section.

---

## V-01 — Role Sequence: 2-Role Evidence-to-Analysis Function Split

**Axis:** Role sequence — two roles split by function type rather than phase sequence. Role 1 (Evidence Compiler) builds all raw data tables without analytical inference. Role 2 (Throttle Analyst + Validator) performs all analysis, synthesis, and validation using Role 1's evidence base. ASSUMPTION GAP blocks are phase-anchored, not role-anchored — Role 2 opens each analytical section with a mandatory ASSUMPTION GAP block before producing section content.

**Hypothesis:** v10 ceiling. Role boundary cuts across phases (not between phases), but C-35 and C-36 are section-level declarations independent of role assignment. Role 2 owns all four ASSUMPTION GAP sections (Phase 2 entry, Section A.3 UX, Exposure Phase entry, Section E.4 test coverage). Risk vector: Role 2's large scope may cause section-level ASSUMPTION GAP blocks to be treated as a single Phase 2 preamble and omitted from subsequent sections; mitigated by declaring ASSUMPTION GAP as a mandatory section-opener list explicitly in the prompt.

---

You are simulating throughput across a rate-limited Power Automate system using a 2-role function split. Role 1 compiles evidence without analysis; Role 2 analyzes and synthesizes using Role 1's evidence base.

**Role assignments:**
- **Role 1 — Evidence Compiler:** Executes the Evidence-Build Phase. Owns VOLUME ARITHMETIC, TABLE 1 (construct inventory with numeric limits and Retry-After flags), QUOTA EXHAUSTION PROJECTION, TABLE 5 (burst path register), TABLE 6 (retry-after gap table), TABLE 7 (cascade risk register). Data fields only — no analytical inference.
- **Role 2 — Throttle Analyst + Validator:** Executes all Analysis, Exposure, Synthesis, and ROUND 2 phases using Role 1's evidence. Opens each analytical section with a mandatory ASSUMPTION GAP block before producing section content.

**Mandatory ASSUMPTION GAP section-openers for Role 2 (in declared order):**
1. Analysis Phase entry
2. Section A.3 (UX mapping)
3. Exposure Phase entry
4. Section E.4 (test coverage)

Each ASSUMPTION GAP block must carry all three components: (a) the status-quo assumption being displaced, (b) the structural reason it fails, (c) the analysis element this output provides in replacement.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### EVIDENCE-BUILD PHASE

*Role: Evidence Compiler.*

**ASSUMPTION GAP — EVIDENCE-BUILD:** Standard throttle analyses assume all rate-limiting constructs are visible in the flow canvas. This assumption fails: nested action quotas and premium connector per-user windows appear only in platform documentation and admin center telemetry. This analysis replaces canvas-inspection enumeration with documentation-sourced construct inventory.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers, making multi-volume sweep silent failures invisible by inspection.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if limit granularity differs from baseline units): `[show conversion factor]`

TABLE 1 STATUS columns must reference these three computed values. Identical STATUS entries across all three bands indicate VOLUME ARITHMETIC was not applied — flag that row with `?`.

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
*(The reason: converts TABLE 1 `Failure visibility window` entries from assertions to verifiable arithmetic depletion intervals anchored to the VOLUME ARITHMETIC 2x rate.)*

For each T-NN with HIT or SAT status: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x load." (assertion without arithmetic)
PASS: "T-01: 40,000 req quota / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion at 2x nominal."

---

**TABLE 5 — Burst Path Register** *(Evidence Compiler fills data fields; Role 2 annotates analysis in Exposure Phase.)*

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement applies at the environment level via [mechanism] at [location]; T-03's per-second window enforces at the connector action level with no bypass path through the [construct] action."

**TABLE 6 — Retry-After Gaps** *(Evidence Compiler fills.)*

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**TABLE 7 — Cascade Risk Register** *(Evidence Compiler fills.)*

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism linking each pair.

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) an exact PA construct type from the domain list, (b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown, (d) a populated Retry-After field, and (e) every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type rather than an exact PA term
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic shown
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation citing the VOLUME ARITHMETIC 2x rate

Flag rows in any of the above failure states with `?` — Evidence Compiler corrects before Role 2 begins.
*Analysis phases are blocked until GATE 1 is cleared.*

---

### ANALYSIS PHASE

*Role: Throttle Analyst + Validator. (Evidence Compiler handoff complete — GATE 1 cleared.)*

*(GATE 1 must pass before this phase executes.)*

**ASSUMPTION GAP — ANALYSIS PHASE:** Standard bottleneck analyses assume the first construct to emit a 429 is the binding constraint. This assumption fails: the binding tier is frequently a per-user entitlement accumulating across all flows sharing a service principal, invisible from within a single flow's execution trace. This analysis replaces single-flow 429-first attribution with principal-pool-aware ordering.

**Section A.1 — Rate Limit Hit Ordering**

*(The reason for the "naive assumption" sentence: it makes limits non-independence explicit, the structural cause of most cascade failures.)*

Write the bottleneck statement:

> "[Specific T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds at this aggregate volume].
> The naive assumption that limits are independent fails here because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| T-NN | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|------|--------------------------|-------|----------------------------------------|
| (bottleneck — first hit) | | | |
| (second hit) | | | |

**Section A.2 — Backpressure Hop Chain**

*(The reason for requiring a named terminal state: a propagation trace without a terminal state leaves the reader unable to determine whether the failure is user-visible or silently lost.)*

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two hops. Name the terminal state in the final row.

**Section A.3 — User Experience per Throttle Tier**

**ASSUMPTION GAP — SECTION A.3:** Standard UX mapping assumes system behavior descriptions ("queue depth increases," "retry loop activates") constitute user experience entries. This assumption fails: system-internal descriptions are unverifiable by a PA runtime reviewer and do not capture what the user observes. This analysis replaces system-state descriptions with user-observable outcome statements categorized by UX impact type.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ across tiers. Each row must state what the user sees — not what the system does internally.

**Section A.4 — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: the same total request volume produces different throttle outcomes when concentrated versus distributed; arrival shape omission misses burst-triggered saturation events invisible to nominal-volume planning.)*

**LOAD SHAPE COMPARISON:** For each T-NN, state whether STATUS changes between UNIFORM and BURST arrival at the VOLUME ARITHMETIC 1x total volume. Positive case: numeric comparison grounded in TABLE 1 limit. Null case: name the specific rate limit mechanism as the structural reason.

**BURST SHAPE MATRIX**
*(The reason for computing f* as a derived value: a matrix without the critical threshold is a descriptive survey, not a threshold-finding analysis.)*

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
- The BURST SHAPE MATRIX is absent or f* is not computed as a derived value
- Any BURST SHAPE MATRIX row lacks an independent mechanism citation

*Exposure Phase is blocked until GATE 2 is cleared.*

---

### EXPOSURE PHASE

*(GATE 2 must pass before this phase executes.)*

**ASSUMPTION GAP — EXPOSURE PHASE:** Standard exposure analyses assume unprotected burst paths are identifiable by canvas inspection. This assumption fails: Apply to Each concurrency behavior and nested action quota accumulation require platform documentation cross-reference and production telemetry to discover. This analysis replaces canvas-inspection gap discovery with documentation-and-telemetry-anchored path analysis.

**Section E.1 — Unprotected Burst Path Analysis** *(Role 2 annotates TABLE 5)*

*(The reason for requiring a named component and structural gap: generic statements provide no actionable mitigation target.)*

Review TABLE 5 (Evidence Compiler). For each Path-ID row, confirm "Why it bypasses or overwhelms tier-1 guard" names a specific mechanism — not a category. Add Role 2 annotation where field is generic.

**Section E.2 — Retry-After Gap Analysis** *(Role 2 annotates TABLE 6)*

*(The reason for failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard is the basis for selecting a PA-native mitigation.)*

Review TABLE 6. Confirm each failure mode is classified as retry-storm / fixed-misalign / silent-discard — not described generically. Add Role 2 classification where absent.

**Section E.3 — Cascade Risk Analysis** *(Role 2 annotates TABLE 7)*

Review TABLE 7. Confirm: at least two cascade pairs with distinct T-NN Tier A / Tier B; named throttle mechanism per pair; severity and duration assessed.

**Section E.4 — Test Coverage Gap Analysis**

**ASSUMPTION GAP — SECTION E.4:** Standard test gap analyses identify missing test cases without naming the specific artifacts that structurally prevent those cases from reaching throttle behaviors. This assumption fails: a gap labeled "integration tests miss this" is unactionable — it names a category, not the artifact, and provides no structural reason why the category fails. This analysis replaces category-level gap declarations with artifact-named structural miss records traceable to specific architectural properties.

#### STAGE 1 — Test Infrastructure Inertia Catalog

*(The reason: a model with specific artifact and limitation in scope cannot produce generic Structural reason or Test approach fields without the failure being visible by inspection.)*

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property causing miss] |

WRONG: "Integration tests" — category, not artifact.
PASS: "The nightly integration suite at `/tests/flow/connector.test.ts` uses `MockSharePointConnector.js` which suppresses all HTTP 429 responses regardless of call volume."

Minimum two artifacts. **STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID behavior]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [names a STAGE 1 artifact and its architectural property]
- **Test approach:** [specific PA tooling step]

WRONG approach: "Add load testing."
PASS approach: "Use Power Automate Performance Test Studio to replay [N] concurrent trigger events against the `Apply to Each` construct at [location], measuring requests/min against T-01's [limit] boundary and capturing HTTP 429 codes in flow run history."

*(Continue GAP-NN entries for each additional gap.)*

---

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all required fields populated, distinct T-NN Tier A / Tier B, named throttle mechanisms, and severity and duration assessed; and Section E.4 has a completed STAGE 1 catalog with at least two named artifacts and a completed STAGE 2 register with at least two GAP-NN entries each carrying all four fields with non-generic values.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 7 has fewer than 2 cascade pairs, or any pair has Tier A T-NN equal to Tier B T-NN
- Any TABLE 7 row is missing a stated throttle mechanism, severity, or duration
- Section E.4 STAGE 1 has fewer than two named artifacts with structural reasons
- Any Section E.4 GAP-NN entry is missing one or more of its four required fields

*Synthesis Phase is blocked until GATE 3 is cleared.*

---

### SYNTHESIS PHASE

*(GATE 3 must pass before this phase executes.)*

**Section S.1 — Quantified Risk Register**

*(The reason for arithmetic: OVER-LIMIT without arithmetic is indistinguishable from a guess.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section S.2 — Mitigation Registry**

*(The reason for `Source`, `Without this change`, and `Depends-on`: traceable, urgency-explicit, execution-plan. No compression of Without-this-change alongside Depends-on.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source (T-NN / Path-ID / Cascade-ID) | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

- Without-this-change: name component, failure mode, and threshold. WRONG: "Throttle errors will increase." PASS: "T-02: HTTP 429 storm affecting all flows sharing the service principal at 2x; flow run failure rate reaches 100% within [quota / 2x rate] minutes."
- Depends-on: MR-ID or `--`.

Minimum: two PA-native remediations.

**Section S.3 — Tier-ID Coverage Audit**

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section E.4 | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Annotate absent T-NNs as COVERAGE GAP [T-NN → section name].

**Section S.4 — Monitoring Signals**

Name at least one PA-observable signal. State the condition it surfaces and the trigger.

**Section S.5 — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 row from SAFE to OVER-LIMIT or vice versa.

**Section S.6 — PA Construct Precision Pass**

*(The reason: "confirmed" is an assertion that the name matches PA documentation exactly.)*

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row, write the corrected construct name, limit source, and precision note **immediately below the `[FAIL]` annotation** before any subsequent TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its `[FAIL]` annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 11 `[FAIL]` row does not have corrected content immediately below its `[FAIL]` annotation

*TABLE 12 and remaining sections are blocked until CORRECTION GATE is cleared.*

**Section S.7 — Test Approach**

At least one concrete PA tooling test step. "Test in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

*Role: Throttle Analyst + Validator (continuing). Independent of Evidence Compiler output quality.*

**Independence:** Evidence Compiler thoroughness is not evidence of construct-level precision. ROUND 2 operates independently of ROUND 1 evidence quality. Corrected construct names from TABLE 11 are now in scope.

For each T-NN in TABLE 11:
1. **PA construct name precision:** Exact term in PA documentation?
2. **Numeric limit precision:** Documented platform limit or estimate? State source.
3. **Rate unit precision:** Unit matches construct's documented enforcement granularity?

For each cascade pair in TABLE 7:
1. **Causal mechanism precision:** Structural or qualitative? Promote using TABLE 9 arithmetic.
2. **Load-added precision:** Numeric projection or directional? Compute from TABLE 9 if directional.
3. **QUOTA EXHAUSTION PROJECTION precision:** Cites VOLUME ARITHMETIC 2x rate by name?

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-01 prompt body.*

---

## V-02 — Output Format: Prose-Primary Analytical Sections

**Axis:** Output format — Phase 2 and Phase 3 analytical sections (bottleneck ordering, backpressure propagation, UX mapping, burst path analysis, cascade analysis) are produced as structured prose paragraphs with inline T-NN citations rather than standalone tables. Tables are retained only for: TABLE 1 (construct inventory — tabular for C-12 identifier traceability), BURST SHAPE MATRIX (tabular for f* column alignment), TABLE 9 (throttle budget), TABLE 10 (mitigation registry), TABLE 11 (precision pass), TABLE 12 (precision audit). ASSUMPTION GAP blocks and WRONG/PASS exemplar blocks appear at their designated sections structurally unchanged — prose format applies only to analytical narrative sections.

**Hypothesis:** v10 ceiling. Prose-primary analytical sections do not affect C-35 or C-36. C-35 evaluates WRONG/PASS in 3+ distinct sections — these blocks are structurally independent of whether surrounding content is tabular or prose. C-36 evaluates whether ASSUMPTION GAP blocks carry all three components — block form is not format-dependent. Risk vector: prose-primary format may cause the model to fold UX tier descriptions into bottleneck narrative, losing per-tier coverage required by C-04; mitigated by a per-tier inventory mandate in the UX section instruction.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

**Format instruction:** Phase 2 and Phase 3 analytical outputs are produced as labeled prose paragraphs with inline T-NN citations. Tables are retained for TABLE 1, BURST SHAPE MATRIX, TABLE 9, TABLE 10, TABLE 11, TABLE 12. Gate declarations, ASSUMPTION GAP blocks, and WRONG/PASS exemplars are structurally unchanged — prose format applies to analytical narrative only.

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 1 — Construct Inventory

**ASSUMPTION GAP — PHASE 1:** Standard throttle analyses assume all rate-limiting constructs are visible in the flow canvas. This assumption fails: nested action quotas and premium connector per-user windows appear only in platform documentation and admin center telemetry. This analysis replaces canvas-inspection enumeration with documentation-sourced construct inventory.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers, making multi-volume sweep silent failures invisible by inspection.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if limit granularity differs): `[show conversion factor]`

TABLE 1 STATUS columns must reference these three computed values. Identical entries across all three bands indicate VOLUME ARITHMETIC was not applied — flag that row with `?`.

**TABLE 1 — Throttle Tier Map**
*(The reason for T-NN identifiers: each tier must be traceable through every downstream section by stable short identifier.)*

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | (see QUOTA EXHAUSTION PROJECTION) |

Domain rule *(the reason: a generic term cannot be matched to a documented limit, breaking TABLE 9 arithmetic traceability)*: each PA construct type must be drawn exactly from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

WRONG: "API rate limit" — not a documented PA construct type.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" — exact documented term with enforcement scope.

---

**QUOTA EXHAUSTION PROJECTION**
*(The reason: converts TABLE 1 `Failure visibility window` entries from assertions to arithmetic-backed depletion intervals.)*

For each T-NN with HIT or SAT status: `quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x load." (no arithmetic)
PASS: "T-01: 40,000 req quota / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion at 2x nominal."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) an exact PA construct type from the domain list, (b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown, (d) a populated Retry-After field, and (e) every HIT or SAT tier has a QUOTA EXHAUSTION PROJECTION entry with arithmetic citing the VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic or undocumented construct type
- Any T-NN row is missing a numeric limit with unit
- Any T-NN row is missing a request contribution estimate with arithmetic shown
- Any T-NN row has a blank Retry-After field
- Any HIT or SAT tier lacks a QUOTA EXHAUSTION PROJECTION arithmetic derivation

Flag rows in any of the above failure states with `?` — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis (Prose-Primary)

*(GATE 1 must pass before this phase executes.)*

**ASSUMPTION GAP — PHASE 2:** Standard bottleneck analyses assume the first construct to emit a 429 is the binding constraint. This assumption fails: the binding tier is frequently a per-user entitlement accumulating across all flows sharing a service principal, invisible from within a single flow's execution trace. This analysis replaces single-flow 429-first attribution with principal-pool-aware ordering that accounts for shared-principal quota aggregation.

**Section 2.A — Rate Limit Hit Ordering** *(prose paragraph with inline T-NN citations)*

Write a bottleneck identification paragraph in the following form:

> "The binding bottleneck is [T-NN: construct name] at [PA construct type]. It saturates at [N req/unit-time] under this scenario because [reason the ordering holds]. The naive assumption that limits are independent fails here because [cascade chain or shared principal pool]. In hit order: [T-NN first] at [limit], followed by [T-NN second] at [limit] because [ordering reason for each tier]."

Name every TABLE 1 tier in hit order with its numeric limit and causal reason for its position. If a tier is not reached at this volume, state explicitly why.

**Section 2.B — Backpressure Hop Chain** *(prose paragraph with inline T-NN citations)*

*(The reason for requiring a named terminal state: a propagation trace without a terminal state leaves the reader unable to determine whether the failure is user-visible or silently lost.)*

Write a propagation trace paragraph covering minimum two hops. Each hop must name: originating T-NN, signal type (error code / retry-after header / queue depth increase / other), receiving T-NN, response behavior. End with the named terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier** *(prose catalog with per-tier labeled entries)*

**ASSUMPTION GAP — SECTION 2.C:** Standard UX mapping assumes system behavior descriptions ("queue depth increases," "retry loop activates") constitute user experience entries. This assumption fails: system-internal descriptions are unverifiable by a PA runtime reviewer and do not capture what the user observes. This analysis replaces system-state descriptions with user-observable outcome statements categorized by UX impact type.

For every T-NN in TABLE 1, produce a labeled entry:

> **[T-NN — construct name]:** System action: [internal]. User-visible experience: [what the user sees]. UX category: [transparent-retry / visible-delay / error-surfaced / silent-loss].

UX categories must differ across tiers. No tier may be omitted. If a tier produces no user-visible signal, state that explicitly with the reason.

**Section 2.D — Load Shape and Burst Sensitivity**

*(The reason for LOAD SHAPE COMPARISON: the same total request volume produces different throttle outcomes when concentrated versus distributed.)*

**LOAD SHAPE COMPARISON:** For each T-NN, state whether STATUS changes between UNIFORM and BURST arrival at VOLUME ARITHMETIC 1x. Positive case: numeric comparison grounded in TABLE 1 limit. Null case: name the specific rate limit mechanism as the structural reason.

**BURST SHAPE MATRIX** *(tabular — retained for column alignment)*
*(The reason for computing f*: a matrix without the critical threshold is descriptive, not threshold-finding.)*

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | below / above f* | SAFE / TRIGGERED | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

---

**GATE 2** is cleared when and only when Section 2.A prose names every TABLE 1 tier in hit order with its limit and ordering reason; Section 2.B prose traces >= 2 hops with a named terminal state; Section 2.C has an entry for every TABLE 1 tier with distinct UX categories; the BURST SHAPE MATRIX has f* computed as a derived value; and each BURST SHAPE MATRIX row carries an independent mechanism citation.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section 2.A omits any TABLE 1 tier without explanation
- Section 2.B has fewer than 2 hops or is missing a named terminal state
- Section 2.C is missing an entry for any TABLE 1 tier, or any two tiers share the same UX category
- BURST SHAPE MATRIX absent or f* not derived from VOLUME ARITHMETIC and TABLE 1
- Any BURST SHAPE MATRIX row lacks an independent mechanism citation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure and Test Coverage Analysis (Prose-Primary)

*(GATE 2 must pass before this phase executes.)*

**ASSUMPTION GAP — PHASE 3:** Standard test coverage assessments assume that integration and load tests collectively reach throttle behaviors. This assumption fails: integration suites using mocked connectors suppress all HTTP 429 responses; load tests at 10–20% of production concurrency cannot reach saturation thresholds. This analysis replaces the green-suite assumption with artifact-named structural miss analysis.

**Section 3.A — Unprotected Burst Paths** *(prose with inline T-NN citations)*

Write a burst-path scan paragraph. Check: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. For each path found, name: flow construct, PA construct type, location, estimated peak rate, and mechanism by which it bypasses the tier-1 guard.

If no paths found, write an explicit absence statement naming at least two specific guards and their enforcement locations.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement applies at the environment level via [mechanism] at [location]; T-03's per-second window enforces at the connector action level with no bypass path through the [construct] action."

**Section 3.B — Retry-After Gap Analysis** *(prose with inline T-NN citations)*

*(The reason for failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard determines PA-native mitigation selection.)*

Write a retry-after gap paragraph. For each T-NN: whether the consumer construct reads the Retry-After header, actual backoff behavior when header is absent or ignored, and failure mode classification (retry-storm / fixed-misalign / silent-discard). At least one gap required.

**Section 3.C — Cascade Risk Register** *(prose with inline T-NN and Cascade-ID citations)*

Write a cascade trace paragraph for each cascade pair. Each pair must name: Tier A (T-NN and construct), throttle mechanism, load added to Tier B, Tier B (T-NN and construct), failure mode, severity, and duration. Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Assign a Cascade-ID to each pair for TABLE 10 reference.

**Section 3.D — Test Coverage Gap Analysis**

**ASSUMPTION GAP — SECTION 3.D:** Standard test gap analyses identify missing test cases without naming the specific artifacts that structurally prevent those cases from reaching throttle behaviors. This assumption fails: category-level gap declarations are unactionable. This analysis replaces category-level declarations with artifact-named structural miss records traceable to specific architectural properties.

#### STAGE 1 — Test Infrastructure Inertia Catalog

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property] |

WRONG: "Integration tests" — category, not artifact.
PASS: Named artifact with architectural suppression property.

Minimum two artifacts. **STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [STAGE 1 artifact + architectural property]
- **Test approach:** [specific PA tooling step]

WRONG approach: "Add load testing."
PASS approach: Named PA tooling step with construct location and HTTP 429 capture method.

*(Continue GAP-NN entries for each additional gap.)*

---

**GATE 3** is cleared when and only when Section 3.C has >= 2 cascade pairs with all required fields, distinct Tier A/B T-NNs, named mechanisms, and severity and duration assessed; and Section 3.D has a completed STAGE 1 catalog with at least two named artifacts and a completed STAGE 2 register with at least two GAP-NN entries each carrying all four fields non-generic.

**GATE 3 is not cleared when any of the following failure states are present:**
- Section 3.C has fewer than 2 cascade pairs, or any pair has Tier A T-NN equal to Tier B T-NN
- Any cascade pair in Section 3.C is missing mechanism, severity, or duration
- Section 3.D STAGE 1 has fewer than two named artifacts
- Any GAP-NN entry is missing one or more required fields

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and Precision Pass

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — Quantified Risk Register**

*(The reason for arithmetic: OVER-LIMIT without arithmetic is indistinguishable from a guess.)*

**TABLE 9 — Throttle Budget**

| T-NN | Construct | Limit | Projected volume at 1x scenario load | Status | Headroom / Deficit |
|------|-----------|-------|--------------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.B — Mitigation Registry**

*(Source = traceable to finding; Without-this-change = urgency explicit; Depends-on = execution plan. No compression.)*

**TABLE 10 — Mitigation Registry**

| MR-ID | Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect | Source | Without this change (at 2x nominal) | Depends-on |
|-------|------------------|------------------------|-----------------------------|---------|------------------------------------|-------------------------------------|------------|

Minimum: two PA-native remediations.

**Section 4.C — Tier-ID Coverage Audit**

| T-NN | Bottleneck section | Propagation section | UX section | Burst-path section | Section 3.D | TABLE 10 |
|------|-------------------|--------------------|-----------|--------------------|-------------|---------|

Annotate absent T-NNs as COVERAGE GAP [T-NN → section name].

**Section 4.D — Monitoring Signals** | **Section 4.E — License and Entitlement Boundary**

At least one PA-observable signal with condition and trigger. At least one entitlement boundary that materially shifts a TABLE 9 status.

**Section 4.F — PA Construct Precision Pass**

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row: corrected content **immediately below** `[FAIL]` annotation before next TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a disposition
- Any `[FAIL]` row is missing corrected content immediately below its annotation

*TABLE 12 and remaining sections are blocked until CORRECTION GATE is cleared.*

**Section 4.G — Test Approach**

At least one concrete PA tooling test step. "Test in staging" does not pass.

---

## ROUND 2 — Structural Precision Pass

*Role: Power Automate flow architect (continuing). Independent of ROUND 1 analytical quality.*

For each T-NN in TABLE 11: PA construct name precision, numeric limit precision (source), rate unit precision.
For each cascade pair in Section 3.C: causal mechanism precision, load-added precision, QUOTA EXHAUSTION PROJECTION precision (cites VOLUME ARITHMETIC 2x rate by name).

**TABLE 12 — Round 2 Precision Audit**

| Item (section ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Lifecycle Emphasis: Exposure-Before-Analysis Phase Ordering

**Axis:** Lifecycle emphasis — phases reordered so that exposure analysis (burst paths, retry-after gaps, cascade risk, test coverage) precedes bottleneck analysis (hit ordering, backpressure propagation, UX mapping). Rationale: production incidents begin with an observed failure — a cascade, a retry storm, a silent loss — rather than a theoretical bottleneck ordering. Exposure-first lifecycle matches incident-driven discovery and produces richer bottleneck evidence because the analyst has cataloged failure pathways before attempting to order limits. The GATE structure adapts: GATE 1 covers construct inventory; GATE 2 covers exposure findings; GATE 3 covers bottleneck and propagation analysis. ASSUMPTION GAP blocks reorder with their phases — C-35 and C-36 coverage is preserved at the same 4-section density.

**Hypothesis:** v10 ceiling. Phase reordering does not affect C-35 or C-36 since both evaluate section-level block presence. C-35 evaluates WRONG/PASS in 3+ sections — the four exemplar sections survive reordering because they appear in the phases governing them. C-36 evaluates ASSUMPTION GAP block presence — blocks reordered with their phases carry identical three-part structure. Risk vector: inverted order may produce bottleneck analysis (Phase 3) that contradicts exposure analysis (Phase 2); mitigated by requiring Phase 3 to cite Phase 2 Cascade-IDs as evidence.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system. This analysis uses an exposure-first lifecycle: failure pathways are cataloged before bottleneck ordering, ensuring bottleneck analysis is grounded in observed failure evidence rather than isolated limit comparisons.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 1 — Construct Inventory

**ASSUMPTION GAP — PHASE 1:** Standard throttle analyses assume all rate-limiting constructs are visible in the flow canvas. This assumption fails: nested action quotas and premium connector per-user windows appear only in platform documentation and admin center telemetry. This analysis replaces canvas-inspection enumeration with documentation-sourced construct inventory.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if needed): `[show conversion factor]`

**TABLE 1 — Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule *(the reason: a generic term cannot be matched to a documented limit)*: each PA construct type must be drawn exactly from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

WRONG: "API rate limit" — not a documented PA construct type.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" — exact documented term.

**QUOTA EXHAUSTION PROJECTION**

For each HIT/SAT T-NN: `quota / rate_at_2x = minutes_to_depletion`. Cite 2x rate from VOLUME ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x load." (no arithmetic)
PASS: "T-01: 40,000 req / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) exact PA construct type, (b) numeric limit with unit, (c) request contribution with arithmetic, (d) populated Retry-After field, and (e) every HIT/SAT tier has QUOTA EXHAUSTION PROJECTION citing VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic construct type
- Any T-NN row is missing numeric limit, contribution arithmetic, or Retry-After
- Any HIT/SAT tier lacks QUOTA EXHAUSTION PROJECTION with arithmetic

*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Exposure Analysis *(burst paths, retry-after, cascade risk, test coverage)*

*(GATE 1 must pass before this phase executes.)*

**ASSUMPTION GAP — PHASE 2:** Standard analyses assume exposure gaps are best identified after completing bottleneck analysis. This assumption fails: exposure gaps often reveal cascade pathways that contradict naive bottleneck ordering — discovering them first allows Phase 3 to be grounded in actual failure evidence. This analysis displaces analysis-first ordering with exposure-first discovery, using Phase 2 Cascade-IDs as evidence inputs to Phase 3 hit ordering.

**Section 2.A — Unprotected Burst Paths**

*(The reason for requiring named component and structural gap: generic statements provide no actionable mitigation target.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out), high-frequency trigger (no debounce), nested loops, batch-size misconfigurations.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement applies at environment level via [mechanism] at [location]; T-03's per-second window enforces at connector action level with no bypass path through the [construct] action."

**Section 2.B — Retry-After Gap Table**

*(The reason for failure mode classification: distinguishing retry-storm from fixed-misalign from silent-discard determines the PA-native mitigation.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 2.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Name the mechanism. Cascade-IDs assigned here are cited by Phase 3 hit-ordering rationale.

**Section 2.D — Test Coverage Gap Analysis**

**ASSUMPTION GAP — SECTION 2.D:** Standard test gap analyses identify missing test cases without naming specific artifacts that structurally prevent throttle behavior discovery. This assumption fails: category-level declarations are unactionable and unfalsifiable. This analysis replaces category-level declarations with artifact-named structural miss records.

#### STAGE 1 — Test Infrastructure Inertia Catalog

| Artifact | Structural reason for miss |
|----------|---------------------------|
| [named artifact] | [architectural property] |

WRONG: "Integration tests." PASS: Named artifact with architectural suppression property.
Minimum two artifacts. **STAGE 1 COMPLETE.**

#### STAGE 2 — Test Coverage Gap Register

**GAP-01**
- **Throttle behavior:** [specific T-NN or Cascade-ID]
- **Test type that misses it:** [specific test type]
- **Structural reason:** [STAGE 1 artifact + architectural property]
- **Test approach:** [specific PA tooling step]

WRONG: "Add load testing." PASS: Named PA tooling step with construct location and capture method.

*(Continue GAP-NN entries for each additional gap.)*

---

**GATE 2** is cleared when and only when TABLE 7 has >= 2 cascade pairs with all required fields, distinct T-NN Tier A / Tier B, named mechanisms, severity and duration; and Section 2.D has >= 2 STAGE 1 artifacts and >= 2 GAP-NN entries with all four fields non-generic.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 7 fewer than 2 pairs, or Tier A T-NN = Tier B T-NN
- Any TABLE 7 row missing mechanism, severity, or duration
- Section 2.D STAGE 1 fewer than two named artifacts
- Any GAP-NN missing required fields

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Bottleneck, Propagation, and UX Analysis

*(GATE 2 must pass before this phase executes. Phase 3 cites TABLE 7 Cascade-IDs as evidence for hit-ordering rationale.)*

**ASSUMPTION GAP — PHASE 3:** Standard bottleneck analyses assume the first construct to emit a 429 is the binding constraint. This assumption fails: the binding tier is frequently a per-user entitlement accumulating across all flows sharing a service principal, invisible from within a single flow's execution trace. This analysis grounds bottleneck ordering in Phase 2 cascade evidence, replacing naive 429-first attribution with principal-pool-aware sequencing.

**Section 3.A — Rate Limit Hit Ordering**

*(The reason for the "naive assumption" sentence: makes limits non-independence explicit — cite TABLE 7 cascade evidence where applicable.)*

Write the bottleneck statement:

> "[T-NN construct] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] because [reason — cite TABLE 7 Cascade-ID if applicable].
> The naive assumption that limits are independent fails because [shared principal pool or cascade chain]."

**TABLE 2 — Hit Order**

| T-NN | Construct (from TABLE 1) | Limit | Why this order holds (cite Cascade-ID if applicable) |
|------|--------------------------|-------|------------------------------------------------------|

**Section 3.B — Backpressure Hop Chain**

*(The reason for named terminal state: determines whether failure is user-visible or silently lost.)*

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Minimum: two hops. Named terminal state in final row.

**Section 3.C — User Experience per Throttle Tier**

**ASSUMPTION GAP — SECTION 3.C:** Standard UX mapping assumes system behavior descriptions constitute user experience entries. This assumption fails: system-internal descriptions are unverifiable by a PA runtime reviewer. This analysis replaces system-state descriptions with user-observable outcome statements categorized by UX impact type.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ. No tier may be omitted.

**Section 3.D — Load Shape and Burst Sensitivity**

*(LOAD SHAPE COMPARISON + BURST SHAPE MATRIX with f*. Same instruction as V-01/V-02.)*

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

---

**GATE 3** is cleared when and only when TABLE 3 has >= 2 hops with named terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has ordering reason for each row citing TABLE 7 evidence where applicable; BURST SHAPE MATRIX has f* derived from VOLUME ARITHMETIC and TABLE 1; each BURST SHAPE MATRIX row has independent mechanism citation.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 3 fewer than 2 hops or missing terminal state
- TABLE 4 fewer than 2 tiers or shared UX category
- TABLE 2 any row missing ordering explanation
- BURST SHAPE MATRIX absent or f* not derived
- Any BURST SHAPE MATRIX row missing mechanism citation

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and Precision Pass

*(GATE 3 must pass. Same structure as V-01/V-02 PHASE 4: TABLE 9, TABLE 10, Coverage Audit, Monitoring, License Boundary, TABLE 11 with CORRECTION GATE, Test Approach.)*

**TABLE 9 — Throttle Budget** | **TABLE 10 — Mitigation Registry**

*(Arithmetic required in TABLE 9. Without-this-change + Depends-on required in TABLE 10. No compression.)*

**Section: Tier-ID Coverage Audit**

| T-NN | TABLE 2 | TABLE 3 | TABLE 4 | TABLE 5 | Section 2.D | TABLE 10 |
|------|---------|---------|---------|---------|-------------|---------|

Annotate absent T-NNs as COVERAGE GAP.

**TABLE 11 — PA Construct Precision Pass**

For any `[FAIL: corrected below]` row: corrected content **immediately below** annotation before next TABLE 11 row.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks disposition
- Any `[FAIL]` row missing corrected content immediately below annotation

---

## ROUND 2 — Structural Precision Pass

*(Same structure as V-01. Independent of ROUND 1 quality. TABLE 12 precision audit.)*

---

*End of V-03 prompt body.*

---

## V-04 — Combined: 2-Role Function Split + Prose-Primary Analytical Sections

**Axis:** Combined — V-01 axis (2-role function split: Evidence Compiler builds raw data; Throttle Analyst + Validator analyzes and synthesizes) and V-02 axis (prose-primary analytical output for Phase 2 / Phase 3 sections) simultaneously. ASSUMPTION GAP blocks declared as mandatory section-openers for Role 2. WRONG/PASS exemplars at all four designated sections.

**Hypothesis:** v10 ceiling. The two axes are structurally independent — role-function split and prose-primary format each affect different dimensions (role attribution; output form) without interfering with C-35/C-36 block presence. Combined load test: prose-primary format plus Role 2's large scope simultaneously may cause ASSUMPTION GAP blocks to be compressed into a single preamble; mitigated by the mandatory section-opener declaration.

---

You are simulating throughput across a rate-limited Power Automate system. Two-role function split with prose-primary analytical output for Phase 2 and Phase 3.

**Role assignments:**
- **Role 1 — Evidence Compiler:** Evidence-Build Phase only. VOLUME ARITHMETIC, TABLE 1 (domain rule compliance), QUOTA EXHAUSTION PROJECTION, TABLE 5, TABLE 6, TABLE 7. Data fields — no inference.
- **Role 2 — Throttle Analyst + Validator:** All analytical, synthesis, and ROUND 2 phases. Mandatory ASSUMPTION GAP section-openers: Analysis Phase entry, Section A.3 (UX), Exposure Phase entry, Section E.4 (test coverage). Each block: (a) displaced assumption, (b) structural failure reason, (c) replacement analysis.

**Format instruction:** Phase 2 and Phase 3 analytical sections — bottleneck ordering, propagation, UX, burst path analysis, cascade analysis — are labeled prose paragraphs with inline T-NN citations. Tables retained for TABLE 1, BURST SHAPE MATRIX, TABLE 9, TABLE 10, TABLE 11, TABLE 12.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### EVIDENCE-BUILD PHASE

*Role: Evidence Compiler.*

**ASSUMPTION GAP — EVIDENCE-BUILD:** Standard throttle analyses assume all rate-limiting constructs are visible in the flow canvas. This assumption fails: nested action quotas and premium connector per-user windows appear only in platform documentation and admin center telemetry. This analysis replaces canvas-inspection enumeration with documentation-sourced construct inventory.

**VOLUME ARITHMETIC** | **TABLE 1** | **QUOTA EXHAUSTION PROJECTION** | **TABLE 5** | **TABLE 6** | **TABLE 7**

*(Identical to V-01 Evidence-Build Phase structures. Domain rule WRONG/PASS in TABLE 1. Quota exhaustion WRONG/PASS in QUOTA EXHAUSTION PROJECTION. Absence form WRONG/PASS in TABLE 5.)*

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) exact PA construct type, (b) numeric limit with unit, (c) contribution arithmetic, (d) populated Retry-After, and (e) every HIT/SAT tier has QUOTA EXHAUSTION PROJECTION citing VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses generic construct type, or is missing limit/arithmetic/Retry-After
- Any HIT/SAT tier lacks QUOTA EXHAUSTION PROJECTION arithmetic

*Analysis phases blocked until GATE 1 cleared.*

---

### ANALYSIS PHASE

*Role: Throttle Analyst + Validator. (GATE 1 cleared.)*

**ASSUMPTION GAP — ANALYSIS PHASE:** Standard bottleneck analyses assume the first construct to emit a 429 is the binding constraint. This assumption fails: the binding tier is frequently a per-user entitlement accumulating across all flows sharing a service principal. This analysis replaces 429-first attribution with principal-pool-aware ordering.

**Section A.1 — Bottleneck Ordering** *(prose)*

Write a bottleneck identification paragraph naming each TABLE 1 tier in hit order with its limit and causal ordering reason. End with the naive-assumption failure sentence citing shared principal pool or cascade chain.

**Section A.2 — Backpressure Hop Chain** *(prose)*

*(Terminal state required — determines UX category assignment.)*

Write a propagation trace paragraph: minimum two hops, each naming originating T-NN, signal type, receiving T-NN, response behavior. End with named terminal state.

**Section A.3 — UX per Throttle Tier** *(prose catalog)*

**ASSUMPTION GAP — SECTION A.3:** Standard UX mapping assumes system behavior descriptions constitute user experience entries. This assumption fails: system-internal descriptions are unverifiable by a PA runtime reviewer. This analysis replaces system-state descriptions with user-observable outcome statements by UX impact category.

For every TABLE 1 T-NN, produce a labeled entry: system action (internal), user-visible experience, UX category (transparent-retry / visible-delay / error-surfaced / silent-loss). Categories must differ. No tier omitted.

**Section A.4 — Load Shape and Burst Sensitivity**

*(LOAD SHAPE COMPARISON + BURST SHAPE MATRIX with f* — tabular. Same f* derivation as V-01.)*

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

---

**GATE 2** is cleared when and only when Section A.1 names every TABLE 1 tier in hit order; Section A.2 traces >= 2 hops with named terminal state; Section A.3 has an entry for every tier with distinct UX categories; BURST SHAPE MATRIX has f* derived; each row has independent mechanism citation.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section A.1 omits any tier without explanation
- Section A.2 fewer than 2 hops or missing terminal state
- Section A.3 missing any tier or shared UX category
- BURST SHAPE MATRIX absent or f* not derived
- Any BURST SHAPE MATRIX row lacking mechanism citation

*Exposure Phase blocked until GATE 2 cleared.*

---

### EXPOSURE PHASE

*(GATE 2 must pass.)*

**ASSUMPTION GAP — EXPOSURE PHASE:** Standard exposure analyses assume unprotected burst paths are identifiable by canvas inspection. This assumption fails: Apply to Each concurrency and nested action quota accumulation require documentation cross-reference to discover. This analysis replaces canvas-inspection gap discovery with documentation-and-telemetry-anchored path analysis.

**Section E.1 — Burst Path Analysis** *(prose with Role 2 annotation on TABLE 5)*

Review TABLE 5. Write burst-path summary confirming each Path-ID's bypass mechanism. Generic fields receive Role 2 correction.

**Section E.2 — Retry-After Gap Analysis** *(prose with Role 2 annotation on TABLE 6)*

Write gap classification paragraph: retry-storm / fixed-misalign / silent-discard per T-NN. At least one gap required.

**Section E.3 — Cascade Risk Analysis** *(prose with Role 2 annotation on TABLE 7)*

Confirm: >= 2 distinct cascade pairs, named mechanisms, severity and duration.

**Section E.4 — Test Coverage Gap Analysis**

**ASSUMPTION GAP — SECTION E.4:** Standard test gap analyses identify missing test cases without naming the specific artifacts that structurally prevent throttle behavior discovery. This assumption fails: category-level declarations are unactionable. This analysis replaces category-level declarations with artifact-named structural miss records.

*(STAGE 1 and STAGE 2 identical to V-01 Section E.4. WRONG/PASS for artifact naming and test approach.)*

---

**GATE 3** is cleared when and only when TABLE 7 has >= 2 cascade pairs (all fields, distinct Tier A/B, named mechanisms, severity/duration); and Section E.4 has >= 2 STAGE 1 artifacts and >= 2 GAP-NN entries with all four fields non-generic.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 7 fewer than 2 pairs, Tier A = Tier B, missing mechanism/severity/duration
- Section E.4 STAGE 1 fewer than two named artifacts
- Any GAP-NN missing required fields

*Synthesis Phase blocked until GATE 3 cleared.*

---

### SYNTHESIS PHASE

*(GATE 3 must pass. Identical to V-01 Synthesis Phase: TABLE 9, TABLE 10, Tier-ID Coverage Audit, Monitoring, License Boundary, TABLE 11 with CORRECTION GATE, Test Approach.)*

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks disposition
- Any `[FAIL]` row missing corrected content immediately below annotation

---

## ROUND 2 — Structural Precision Pass

*(Identical to V-01 ROUND 2. Independent of Role 1. TABLE 12.)*

---

*End of V-04 prompt body.*

---

## V-05 — Combined: Exposure-Before-Analysis Lifecycle + Phase 0 Risk Forecast (5 ASSUMPTION GAP Blocks)

**Axis:** Combined — V-03 axis (exposure-before-analysis phase ordering: Phase 2 = burst paths + retry-after + cascades + test coverage; Phase 3 = bottleneck + propagation + UX) and new axis (Phase 0 Risk Forecast before Phase 1, adding a 5th ASSUMPTION GAP block and 5th WRONG/PASS exemplar section). Phase 0 produces a pre-inventory risk forecast — a falsifiable prediction of which tier categories are most likely binding before any enumeration. Phase 4 reconciles the forecast against TABLE 1 evidence. Total: 5 ASSUMPTION GAP blocks (Phase 0, Phase 1, Phase 2, Phase 3, Section 3.C) and 5 WRONG/PASS sections (Phase 0 forecast form, domain rule, quota exhaustion, burst-path absence, test gap approach).

**Hypothesis:** v10 ceiling. Phase 0 adds a 5th ASSUMPTION GAP block, exceeding the C-35 floor (3+) and strengthening C-36 body of evidence beyond what any prior variation has tested. Phase reordering (V-03 axis) is confirmed C-36-safe. Risk vector: Phase 0 forecast may cause the model to treat the forecast as substitute for TABLE 1 inventory, causing GATE 1 to be treated as already cleared; mitigated by explicit statement that Phase 0 is a falsifiable prediction and GATE 1 still covers full TABLE 1 completion.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a rate-limited Power Automate system. 5-phase exposure-first lifecycle with a pre-inventory risk forecast.

**Phase structure:**
- Phase 0: Risk Forecast (falsifiable prediction — not inventory; does not substitute for GATE 1)
- Phase 1: Construct Inventory
- Phase 2: Exposure Analysis (burst paths, retry-after, cascade risk, test coverage)
- Phase 3: Bottleneck, Propagation, UX (grounded in Phase 2 cascade evidence)
- Phase 4: Synthesis, Precision Pass, Forecast Reconciliation

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 0 — Risk Forecast *(produce before any TABLE 1 enumeration)*

**ASSUMPTION GAP — PHASE 0:** Standard throttle analyses begin with construct enumeration and defer risk prediction until the inventory is complete. This assumption fails: beginning without a stated prediction produces no falsifiable claim — the analyst can silently revise expectations as evidence accumulates, hiding cognitive biases that cause systematic inventory omissions. This analysis displaces post-hoc risk labeling with a pre-inventory risk forecast that is revisited in Phase 4 to identify where prediction and evidence diverged.

Based on the scenario description alone (before TABLE 1 enumeration), produce a risk forecast:

1. Name the PA construct category most likely to be the binding bottleneck at 2x nominal load. State the structural reason (a property of the scenario, not a calculation).
2. Name the PA construct category most likely to have an unprotected burst path. State the structural reason.
3. Name the failure mode most likely to compound throttle recovery (retry-storm / silent-discard / fixed-misalign). State the structural reason.

WRONG forecast: "Connector throttling will likely be the binding constraint." (category without structural reason)
PASS forecast: "Power Platform per-user request entitlement is likely binding at 2x because the scenario describes multiple flows sharing a single service principal — per-user entitlement accumulates across all flows sharing that principal, making the shared-principal pool the aggregate bottleneck regardless of per-flow connector limits."

*Phase 0 forecast is a falsifiable prediction. Phase 4 reconciles it. GATE 1 still covers full TABLE 1 completion — Phase 0 does not substitute for inventory.*

---

### PHASE 1 — Construct Inventory

**ASSUMPTION GAP — PHASE 1:** Standard throttle analyses assume all rate-limiting constructs are visible in the flow canvas. This assumption fails: nested action quotas and premium connector per-user windows appear only in platform documentation and admin center telemetry. This analysis replaces canvas-inspection enumeration with documentation-sourced construct inventory.

**VOLUME ARITHMETIC**
*(The reason: without pre-computed volume bands, STATUS columns may use an implicit baseline that differs across tiers.)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 × baseline]` req/min | 5x: `[5 × baseline]` req/min
Unit conversion (if needed): `[show conversion factor]`

**TABLE 1 — Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule *(the reason: a generic term cannot be matched to a documented limit)*: each PA construct type must be drawn exactly from — Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.

WRONG: "API rate limit" — not a documented PA construct type.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" — exact documented term.

**QUOTA EXHAUSTION PROJECTION**

For each HIT/SAT T-NN: `quota / rate_at_2x = minutes_to_depletion`. Cite 2x rate from VOLUME ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x load." (no arithmetic)
PASS: "T-01: 40,000 req / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) exact PA construct type from the domain list, (b) numeric limit with unit, (c) request contribution with arithmetic, (d) populated Retry-After, and (e) every HIT/SAT tier has QUOTA EXHAUSTION PROJECTION citing VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic construct type
- Any T-NN row is missing limit, contribution arithmetic, or Retry-After
- Any HIT/SAT tier lacks QUOTA EXHAUSTION PROJECTION with arithmetic

*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Exposure Analysis *(burst paths, retry-after, cascade risk, test coverage)*

*(GATE 1 must pass before this phase executes.)*

**ASSUMPTION GAP — PHASE 2:** Standard analyses assume exposure gaps are best identified after completing bottleneck analysis. This assumption fails: exposure gaps often reveal cascade pathways that contradict naive bottleneck ordering — discovering them first allows Phase 3 to be grounded in actual failure evidence. This analysis displaces analysis-first ordering with exposure-first discovery, using Phase 2 Cascade-IDs as evidence inputs to Phase 3 hit ordering.

**Section 2.A — Unprotected Burst Paths**

*(The reason for named component and structural gap: generic statements provide no actionable mitigation target.)*

**TABLE 5 — Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out), high-frequency trigger (no debounce), nested loops, batch-size misconfigurations.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement applies at environment level via [mechanism] at [location]; T-03's per-second window enforces at connector action level with no bypass path through the [construct] action."

**Section 2.B — Retry-After Gap Table**

*(The reason for failure mode classification: determines PA-native mitigation selection.)*

**TABLE 6 — Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 2.C — Cascade Risk Register**

**TABLE 7 — Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Cascade-IDs cited by Phase 3.

**Section 2.D — Test Coverage Gap Analysis**

**ASSUMPTION GAP — SECTION 2.D:** Standard test gap analyses identify missing test cases without naming specific artifacts that structurally prevent throttle behavior discovery. This assumption fails: category-level gap declarations are unactionable and unfalsifiable. This analysis replaces category-level declarations with artifact-named structural miss records traceable to specific architectural properties.

*(STAGE 1 and STAGE 2 identical to V-03 Section 2.D. WRONG/PASS for artifact naming and test approach.)*

---

**GATE 2** is cleared when and only when TABLE 7 has >= 2 cascade pairs (all fields, distinct Tier A/B, named mechanisms, severity/duration); and Section 2.D has >= 2 STAGE 1 artifacts and >= 2 GAP-NN entries all four fields non-generic.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 7 fewer than 2 pairs, or Tier A = Tier B T-NN
- Any TABLE 7 row missing mechanism, severity, or duration
- Section 2.D STAGE 1 fewer than two named artifacts
- Any GAP-NN entry missing required fields

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Bottleneck, Propagation, and UX Analysis

*(GATE 2 must pass. Phase 3 cites TABLE 7 Cascade-IDs as evidence for hit-ordering rationale.)*

**ASSUMPTION GAP — PHASE 3:** Standard bottleneck analyses assume the first construct to emit a 429 is the binding constraint. This assumption fails: the binding tier is frequently a per-user entitlement accumulating across all flows sharing a service principal. This analysis grounds bottleneck ordering in Phase 2 cascade evidence, replacing naive 429-first attribution with principal-pool-aware sequencing.

**Section 3.A — Rate Limit Hit Ordering**

Write the bottleneck statement citing TABLE 7 Cascade-IDs:

> "[T-NN construct] at [PA construct type] is the binding bottleneck at [N req/unit-time] because [reason — cite Cascade-ID].
> The naive assumption that limits are independent fails because [principal pool or cascade chain]."

**TABLE 2 — Hit Order**

| T-NN | Construct | Limit | Why this order holds (cite Cascade-ID) |
|------|-----------|-------|----------------------------------------|

**Section 3.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Minimum: two hops. Named terminal state in final row.

**Section 3.C — User Experience per Throttle Tier**

**ASSUMPTION GAP — SECTION 3.C:** Standard UX mapping assumes system behavior descriptions constitute user experience entries. This assumption fails: system-internal descriptions are unverifiable by a PA runtime reviewer. This analysis replaces system-state descriptions with user-observable outcome statements categorized by UX impact type.

**TABLE 4 — UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories must differ. No tier omitted.

**Section 3.D — Load Shape and Burst Sensitivity**

f* = smallest f such that (total_volume / (f × window)) > binding_tier_limit

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

---

**GATE 3** is cleared when and only when TABLE 3 has >= 2 hops with named terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has ordering reason for each row citing TABLE 7 evidence; BURST SHAPE MATRIX has f* derived; each row has independent mechanism citation.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 3 fewer than 2 hops or missing terminal state
- TABLE 4 fewer than 2 tiers or shared UX category
- TABLE 2 any row missing ordering explanation
- BURST SHAPE MATRIX absent or f* not derived
- Any row missing mechanism citation

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis, Precision Pass, and Forecast Reconciliation

*(GATE 3 must pass.)*

**Section 4.A — Quantified Risk Register** | **Section 4.B — Mitigation Registry** | **Section 4.C — Tier-ID Coverage Audit**

*(TABLE 9 with arithmetic; TABLE 10 with Without-this-change + Depends-on, no compression; Coverage Audit across all downstream sections. Same structure as V-03 PHASE 4.)*

**Section 4.D — Monitoring Signals** | **Section 4.E — License and Entitlement Boundary**

**Section 4.F — Phase 0 Forecast Reconciliation**

Revisit the Phase 0 risk forecast. For each of the three Phase 0 predictions: CONFIRMED or FALSIFIED, the TABLE 1 / TABLE 7 evidence that confirms or falsifies it, and what the divergence reveals about the structural assumption embedded in the forecast.

*(The reason for forecast reconciliation: converts Phase 0 from a cognitive exercise into a falsifiable claim audit, surfacing assumption gaps that TABLE 1 enumeration reveals. A CONFIRMED forecast with no divergence analysis does not pass — state whether the evidence strengthens or merely restates the Phase 0 reasoning.)*

**Section 4.G — PA Construct Precision Pass**

**TABLE 11 — PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row: corrected content **immediately below** `[FAIL]` annotation before next TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit disposition and every `[FAIL]` row has corrected content immediately below its `[FAIL]` annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any `[FAIL]` row is missing corrected content immediately below its annotation

*TABLE 12 and remaining sections are blocked until CORRECTION GATE is cleared.*

**Section 4.H — Test Approach**

At least one concrete PA tooling test step. "Test in staging" does not pass.

---

## ROUND 2 — Structural Precision Pass

*Role: Power Automate flow architect (continuing). Independent of ROUND 1 quality.*

**Independence:** ROUND 1 coherence — including Phase 0 forecast reconciliation — is not evidence of construct-level precision. ROUND 2 operates independently. Corrected construct names from TABLE 11 are now in scope.

For each T-NN in TABLE 11: PA construct name precision, numeric limit precision (source), rate unit precision (matches documented enforcement granularity).

For each cascade pair in TABLE 7: causal mechanism precision (structural vs. qualitative — promote with TABLE 9 arithmetic), load-added precision (numeric vs. directional — compute from TABLE 9 if directional), QUOTA EXHAUSTION PROJECTION precision (cites VOLUME ARITHMETIC 2x rate by name).

**TABLE 12 — Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*
