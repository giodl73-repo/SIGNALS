# flow-throttle Skill Body -- Round 12 Complete Variations
**Date:** 2026-03-15
**Rubric:** v11 (C-01 through C-38; denominator 26)
**Baseline ceiling:** R11 V-05 (Phase 0 forecast section + Phase-boundary ASSUMPTION GAP; 26/26
aspirational, composite 100)

---

## Round 12 Analysis

**R11 confirmed:**
- C-37: Phase 0 forecast section (named section before TABLE 1 with 3 structural risk
  predictions and WRONG/PASS exemplar) is a new C-35-map section; V-01 through V-04 lack
  it, V-05 carries it. Phase 0 adds V-05's 5th independent WRONG/PASS exemplar section and
  5th ASSUMPTION GAP anchor point.
- C-38: Phase 0 ASSUMPTION GAP block operating at the Phase 0 / Phase 1 boundary. Three-part
  structure: (a) displaced assumption (reactive violation discovery), (b) structural failure
  reason (per-section volume interpretation diverges from VOLUME ARITHMETIC), (c) Phase 0
  replacement (committed predictions before Phase 1, making any deviation a verifiable
  forecast error). This is phase-boundary-level, not section-level.
- V-05's Phase 0 predicted categories (binding tier category, unprotected burst category,
  compounding failure mode) with structural reasons -- prose form, not tabular.
- V-05's Phase 4 Section 4.F reconciled Phase 0 predictions as CONFIRMED / FALSIFIED with
  TABLE 1 / TABLE 7 evidence -- binary outcome, no error taxonomy.
- C-35 confirmed inert to lifecycle ordering (exposure-first vs. analysis-first).
- C-36 confirmed inert to lifestyle reordering (ASSUMPTION GAP blocks fire in any phase
  sequence).

**What R11 did NOT test under v11:**
- C-37 under multi-role cardinality: V-05 used a single analyst for all phases. Whether
  Phase 0 survives 4-role attribution (Phase 0 to Role 1, Phase 1 to Role 2, etc.) has not
  been tested.
- C-38 under multi-role cardinality: Whether the phase-boundary ASSUMPTION GAP fires
  correctly when Phase 0 and Phase 1 are attributed to different roles has not been tested.
- C-37/C-38 under non-imperative register: V-05 used formal/technical imperative throughout.
  Conversational/descriptive register with identical structural blocks is untested.
- Phase 0 quantification: V-05's Phase 0 produced categorical prose predictions. Whether a
  Phase 0 TABLE 0 (tier prediction table with HIT/SAT/MISS states and arithmetic basis) can
  serve as a stronger excellence signal (potential C-39) has not been tested.
- Phase 4 reconciliation taxonomy: V-05 reconciled as CONFIRMED / FALSIFIED. Whether a
  3-axis error taxonomy (structural-miss / magnitude-miss / mechanism-miss) in Phase 4
  creates a new excellence signal (potential C-39 or C-40) has not been tested.

**R12 design hypotheses:**
- H1: C-37 and C-38 are role-cardinality-inert. Phase 0 by Role 1 satisfies C-37; the
  ASSUMPTION GAP at the Role 1 / Role 2 handoff boundary satisfies C-38. (V-01)
- H2: C-37 and C-38 are register-inert. Conversational phrasing with identical structural
  blocks satisfies both criteria. (V-03)
- H3: Phase 0 quantification -- TABLE 0 with HIT/SAT/MISS per tier category and arithmetic
  basis -- creates a potential C-39 excellence signal by establishing per-row prediction-
  verification pairing with TABLE 1 STATUS columns. (V-02)
- H4: Phase 4 error taxonomy (3-axis classification) creates a second potential C-39
  excellence signal by converting the CONFIRMED/FALSIFIED binary into a structured causal
  audit. (V-04)
- H5: Combination of 4-role + Phase 0 TABLE 0 + Phase 4 error taxonomy achieves v11
  ceiling and carries both potential C-39 excellence signals simultaneously. (V-05)

**R11 coverage map (axes confirmed at v11 ceiling):**

| Criterion | R11 V-01 | R11 V-02 | R11 V-03 | R11 V-04 | R11 V-05 |
|-----------|----------|----------|----------|----------|----------|
| C-35 (WRONG/PASS exemplars 3+) | PASS | PASS | PASS | PASS | PASS |
| C-36 (ASSUMPTION GAP blocks 3+) | PASS | PASS | PASS | PASS | PASS |
| C-37 (Phase 0 section) | FAIL | FAIL | FAIL | FAIL | PASS |
| C-38 (Phase 0 boundary ASSUMPTION GAP) | FAIL | FAIL | FAIL | FAIL | PASS |

**R12 variation map:**

| Variation | Axis | C-37 | C-38 | Potential C-39 | Predicted score |
|-----------|------|------|------|----------------|----------------|
| V-01 | Single: 4-role cardinality | PASS | PASS | N/A | v11 ceiling (26/26) |
| V-02 | Single: Phase 0 TABLE 0 (quantified HIT/SAT/MISS) | PASS | PASS | Candidate A | v11 ceiling + excellence |
| V-03 | Single: conversational register | PASS | PASS | N/A | v11 ceiling (26/26) |
| V-04 | Single: Phase 4 3-axis error taxonomy | PASS | PASS | Candidate B | v11 ceiling + excellence |
| V-05 | Combination: 4-role + TABLE 0 + error taxonomy | PASS | PASS | A + B | v11 ceiling + excellence |

**Risk vectors for R12:**
- V-01: A model attributing Phase 0 to Role 1 may drop the ASSUMPTION GAP block when Phase 0
  is attributed to a "forecast" role that doesn't carry section-level ASSUMPTION GAP
  obligations. Mitigation: declare the ASSUMPTION GAP as a Phase 0 structural requirement
  independently of role, not as a role obligation.
- V-02: TABLE 0 tier predictions require a preliminary VOLUME ARITHMETIC sketch before TABLE 1.
  A model may conflate the Phase 0 arithmetic sketch with the Phase 1 VOLUME ARITHMETIC block,
  satisfying only one. Mitigation: label Phase 0 arithmetic as a preliminary sketch and Phase 1
  VOLUME ARITHMETIC as the authoritative block; Phase 0 cites Phase 1 as ground truth.
- V-03: Conversational phrasing may cause the model to omit structural block labels (ASSUMPTION
  GAP, WRONG, PASS) in favor of flowing prose. Mitigation: declare that structural labels
  (ASSUMPTION GAP, WRONG, PASS) are required regardless of surrounding prose register.
- V-04: 3-axis error taxonomy in Phase 4 may cause the model to reclassify all CONFIRMED
  predictions as TYPE-0 (no error) without engaging the taxonomy structure. Mitigation:
  require at least one non-TYPE-0 classification with evidence, making the taxonomy
  structurally non-trivial.
- V-05: Maximum load. The 4-role split combined with TABLE 0 and Phase 4 taxonomy creates
  three simultaneous structural novelties. Risk: Phase 0 TABLE 0 may collapse into Phase 1
  TABLE 1 with "predicted" and "actual" columns, losing the phase-boundary structure. Mitigation:
  Phase 0 TABLE 0 must be completed before Phase 1 begins; it appears in Phase 0 not Phase 1.

---

## V-01 -- Single-Axis: 4-Role Cardinality (C-37/C-38 role-inertia test)

**Axis:** 4-role function split with Phase 0 attributed to Role 1 (Risk Forecaster). Tests
whether C-37 (Phase 0 section presence) and C-38 (Phase-boundary ASSUMPTION GAP) are inert to
role cardinality. R11 V-05 had a single analyst across all phases; this variation splits
forecasting (Role 1), enumeration (Role 2), analysis (Role 3), and synthesis (Role 4) into
separate roles with explicit handoff declarations at each phase transition.

**Hypothesis:** v11 ceiling (26/26). C-37 fires because Phase 0 is a named section before
TABLE 1 regardless of which role produces it. C-38 fires because the ASSUMPTION GAP block at
the Phase 0 / Phase 1 boundary is a structural requirement of Phase 0, not a role obligation.
C-36 fires at each phase-role transition (4 handoffs). C-35 fires at WRONG/PASS sections
across 4+ independent sections. Risk vector: model may omit ASSUMPTION GAP from Phase 0 when
Phase 0 is attributed to a "Forecaster" role without explicit ASSUMPTION GAP obligations.
Prompt mitigates by declaring ASSUMPTION GAP as a Phase 0 structural requirement independent
of role attribution.

---

You are simulating throughput across a rate-limited Power Automate system. 4-role function
split with Phase 0 risk forecast attributed to Role 1.

**Role assignments:**
- **Role 1 -- Risk Forecaster:** Phase 0 only. Produces the pre-inventory risk forecast
  and Phase-boundary ASSUMPTION GAP. No TABLE 1 enumeration -- all construct naming in Phase
  0 is categorical (tier category, not T-NN identifiers).
- **Role 2 -- Construct Enumerator:** Phase 1 only. VOLUME ARITHMETIC, TABLE 1, QUOTA
  EXHAUSTION PROJECTION. Data fields only -- no bottleneck inference. Opens with Role 1
  handoff confirmation.
- **Role 3 -- Impact Analyst:** Phase 2 and Phase 3. Bottleneck ordering, backpressure
  propagation, UX mapping, load shape analysis (Phase 2); burst path analysis, retry-after
  gaps, cascade risk, test coverage gaps (Phase 3). Opens each phase with prior-role handoff
  confirmation.
- **Role 4 -- Synthesizer + Validator:** Phase 4. Quantified risk register, mitigation
  registry, tier-ID coverage audit, monitoring signals, license boundary, PA construct
  precision pass, forecast reconciliation, test approach. Opens Phase 4 with Role 3 handoff
  confirmation.

**Phase-entry handoff form (required at each phase opening after Phase 0):**
- Phase 1 opens with: `*(Role 1 Risk Forecaster handoff complete -- proceed to Phase 1.)*`
- Phase 2 opens with: `*(Role 2 Construct Enumerator handoff complete -- GATE 1 cleared.
  Proceed to Phase 2.)*`
- Phase 3 opens with: `*(Role 3 Impact Analyst Phase 2 handoff complete -- GATE 2 cleared.
  Proceed to Phase 3.)*`
- Phase 4 opens with: `*(Role 3 Impact Analyst Phase 3 handoff complete -- GATE 3 cleared.
  Proceed to Phase 4.)*`

A phase that omits the handoff confirmation line, or embeds it inside a section heading or
analytical paragraph, fails the phase-entry handoff requirement for that phase.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 0 -- Risk Forecast *(Role 1 -- Risk Forecaster)*

*Produce before any TABLE 1 enumeration. Role 1 produces only Phase 0; no T-NN identifiers
are assigned here. Phase 0 forecasts categories and failure modes.*

**ASSUMPTION GAP -- PHASE 0 / PHASE 1 BOUNDARY:** Standard throttle analyses assume that
construct enumeration should precede risk assessment -- that a risk forecast before inventory
is speculative and therefore worthless. This assumption fails: beginning Phase 1 without a
committed prediction produces no falsifiable claim. Per-section volume interpretation can
diverge from VOLUME ARITHMETIC silently, because there is no pre-committed baseline to detect
the divergence. This analysis displaces reactive violation discovery with a Phase 0 forecast
that commits to (a) the most likely binding tier category, (b) the most likely unprotected
burst category, (c) the most likely compounding failure mode -- each with a structural reason
grounded in the scenario description, before Phase 1 begins. Any Phase 1 finding that
contradicts a Phase 0 commitment is a structurally visible forecast discrepancy, not an
invisible revision.

Based on the scenario description alone (before TABLE 1 enumeration), produce:

1. **Binding tier prediction.** Name the PA construct category most likely to be the binding
   bottleneck at 2x nominal load. State the structural reason (a property of the scenario
   description, not a calculation).

2. **Burst path prediction.** Name the PA construct category most likely to have an
   unprotected burst path. State the structural reason.

3. **Compounding failure mode prediction.** Name the failure mode most likely to compound
   throttle recovery: retry-storm, silent-discard, or fixed-misalign. State the structural
   reason.

WRONG forecast: "The connector throttling tier is likely binding." (category without
structural reason)
PASS forecast: "Power Platform per-user request entitlement is likely binding at 2x because
the scenario describes multiple flows sharing a single service principal -- the entitlement
accumulates across all flows sharing that principal, making the shared principal pool the
aggregate bottleneck regardless of per-flow connector limits."

*This forecast is a falsifiable prediction. Phase 4 Section 4.F reconciles it against TABLE 1
and TABLE 7 evidence. Phase 0 does NOT substitute for Phase 1 enumeration. GATE 1 still
requires full TABLE 1 completion.*

---

## PHASE 1 -- Construct Inventory *(Role 2 -- Construct Enumerator)*

*(Role 1 Risk Forecaster handoff complete -- proceed to Phase 1.)*

**ASSUMPTION GAP -- PHASE 1:** Standard throttle analyses assume all rate-limiting constructs
are visible in the flow canvas. This assumption fails: nested action quotas and premium
connector per-user windows appear only in platform documentation and admin center telemetry.
This analysis replaces canvas-inspection enumeration with documentation-sourced construct
inventory.

**VOLUME ARITHMETIC**

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 x baseline]` req/min | 5x: `[5 x baseline]` req/min
Unit conversion (if needed): `[show conversion factor]`

**TABLE 1 -- Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule *(the reason: a generic term cannot be matched to a documented limit)*: each PA
construct type must be drawn exactly from -- Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits.

WRONG: "API rate limit" -- not a documented PA construct type.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" --
exact documented term.

**QUOTA EXHAUSTION PROJECTION**

For each HIT/SAT T-NN: `quota / rate_at_2x = minutes_to_depletion`. Cite 2x rate from
VOLUME ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x load." (no arithmetic)
PASS: "T-01: 40,000 req / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) exact PA construct
type from the domain list, (b) numeric limit with unit, (c) request contribution with
arithmetic, (d) populated Retry-After field, and (e) every HIT/SAT tier has QUOTA EXHAUSTION
PROJECTION citing VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic construct type not drawn from the domain list
- Any T-NN row is missing numeric limit with unit
- Any T-NN row is missing request contribution with arithmetic shown
- Any HIT/SAT tier lacks QUOTA EXHAUSTION PROJECTION with arithmetic

*PHASE 2 is blocked until GATE 1 is cleared.*

---

## PHASE 2 -- Bottleneck, Propagation, and UX Analysis *(Role 3 -- Impact Analyst)*

*(Role 2 Construct Enumerator handoff complete -- GATE 1 cleared. Proceed to Phase 2.)*

**ASSUMPTION GAP -- PHASE 2:** Standard bottleneck analyses assume the first construct to emit
a 429 is the binding constraint. This assumption fails: the binding tier is frequently a
per-user entitlement accumulating across all flows sharing a service principal. This analysis
replaces 429-first attribution with principal-pool-aware hit ordering grounded in TABLE 1
arithmetic.

### Section 2.A -- Rate Limit Hit Ordering

Write the bottleneck statement:

> "[T-NN construct] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] under this scenario because [reason the ordering holds at this aggregate
> volume]. The naive assumption that limits are independent fails here because [one sentence
> linking to cascade chain or shared principal pool]."

**TABLE 2 -- Hit Order**

| Hit order | T-NN (from TABLE 1) | Construct | Limit | Why this order holds at scenario volume |
|-----------|---------------------|-----------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | |
| 2 | | | | |

### Section 2.B -- Backpressure Hop Chain

**TABLE 3 -- Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two
hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).
Named terminal state required in final row.

### Section 2.C -- User Experience per Throttle Tier

**ASSUMPTION GAP -- SECTION 2.C:** Standard UX mapping assumes system behavior descriptions
constitute user experience entries. This assumption fails: system-internal descriptions are
unverifiable by a PA runtime reviewer. This analysis replaces system-state descriptions with
user-observable outcome statements categorized by UX impact type.

**TABLE 4 -- UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories
must differ. No tier omitted.

### Section 2.D -- Load Shape and Burst Sensitivity

f* = smallest f such that (total_volume / (f x window)) > binding_tier_limit

| Shape | Concentration f | Peak rate in window | Compared to f* | Result | Mechanism citation |
|-------|-----------------|--------------------|--------------------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row requires an independent mechanism citation.

---

**GATE 2** is cleared when and only when Section 2.A names every TABLE 1 tier in hit order
with reasoning; TABLE 3 traces >= 2 hops with named terminal state; TABLE 4 has an entry for
every tier with distinct UX categories; BURST SHAPE MATRIX has f* derived; each row has
independent mechanism citation.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section 2.A omits any TABLE 1 tier without explanation
- TABLE 3 fewer than 2 hops or missing terminal state
- TABLE 4 missing any tier, or any two tiers sharing UX category
- BURST SHAPE MATRIX absent or f* not derived
- Any BURST SHAPE MATRIX row lacking independent mechanism citation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

## PHASE 3 -- Exposure Analysis *(Role 3 -- Impact Analyst, continued)*

*(Role 3 Impact Analyst Phase 2 handoff complete -- GATE 2 cleared. Proceed to Phase 3.)*

**ASSUMPTION GAP -- PHASE 3:** Standard exposure analyses assume unprotected burst paths are
identifiable by canvas inspection. This assumption fails: Apply to Each concurrency and nested
action quota accumulation require documentation cross-reference to discover. This analysis
replaces canvas-inspection gap discovery with documentation-and-telemetry-anchored path
analysis.

### Section 3.A -- Unprotected Burst Paths

**TABLE 5 -- Burst Path Register**

| Path-ID | Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|---------|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out), high-
frequency trigger (no debounce), nested loops, batch-size misconfigurations.

WRONG absence: "No unprotected burst paths found."
PASS absence: "No unprotected burst paths found. T-01's Power Platform request entitlement
applies at environment level via [mechanism] at [location]; T-03's per-second window enforces
at connector action level with no bypass path through the [construct] action."

### Section 3.B -- Retry-After Gap Table

**TABLE 6 -- Retry-After Gaps**

| T-NN | Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|------|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

### Section 3.C -- Cascade Risk Register

**TABLE 7 -- Cascade Risk Register**

| Cascade-ID | Tier A (T-NN) | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B (T-NN) | Tier B construct | Failure mode | Severity | Duration |
|------------|-------------|-----------------|-------------------|---------------------|-------------|-----------------|-------------|----------|---------|

Minimum: two cascade pairs with distinct T-NN Tier A / Tier B. Named mechanisms. Non-generic
severity and duration entries.

### Section 3.D -- Test Coverage Gap Analysis

**ASSUMPTION GAP -- SECTION 3.D:** Standard test gap analyses identify missing test cases
without naming the specific artifacts that structurally prevent throttle behavior discovery.
This assumption fails: category-level gap declarations are unactionable. This analysis
replaces category-level declarations with artifact-named structural miss records.

STAGE 1 -- Enumerate testing artifacts currently covering throttle behavior:
- List each artifact by name (test file, environment config, pipeline stage)
- For each: what throttle behavior it covers, what it structurally cannot cover

STAGE 2 -- Enumerate gaps (minimum 2):

| Gap-NN | Throttle behavior not covered | Why structurally uncoverable by current artifacts | Consequence if undetected | Candidate test approach |
|--------|------------------------------|--------------------------------------------------|--------------------------|------------------------|

WRONG approach: "Add load tests to cover connector throttle behavior."
PASS approach: "Add Power Automate Analytics connector-request telemetry review to the
staging pipeline -- the current regression suite runs against a single service principal and
cannot observe cross-principal entitlement accumulation because the test environment does not
replicate multi-flow shared-principal topology."

---

**GATE 3** is cleared when and only when TABLE 7 has >= 2 cascade pairs (all fields, distinct
Tier A / Tier B T-NN, named mechanisms, severity and duration); and Section 3.D has >= 2
STAGE 1 artifacts and >= 2 GAP-NN entries with all four fields non-generic.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 7 fewer than 2 pairs, or Tier A T-NN = Tier B T-NN on any pair
- Any TABLE 7 row missing mechanism, severity, or duration
- Section 3.D STAGE 1 fewer than two named artifacts
- Any GAP-NN entry missing required fields

*PHASE 4 is blocked until GATE 3 is cleared.*

---

## PHASE 4 -- Synthesis, Precision Pass, and Forecast Reconciliation *(Role 4 -- Synthesizer)*

*(Role 3 Impact Analyst Phase 3 handoff complete -- GATE 3 cleared. Proceed to Phase 4.)*

### Section 4.A -- Quantified Risk Register

**TABLE 9 -- Quantified Risk Register**

| T-NN | Risk description | Probability | Impact | Risk score | Mitigation-ID | Arithmetic basis |
|------|-----------------|-------------|--------|------------|---------------|-----------------|

Probability and impact must have arithmetic basis from TABLE 1 STATUS and QUOTA EXHAUSTION
PROJECTION. Risk score = probability x impact (explicit). No directional qualifiers without
arithmetic.

### Section 4.B -- Mitigation Registry

**TABLE 10 -- Mitigation Registry**

| Mitigation-ID | Description | Without-this-change consequence | Depends-on (Mitigation-ID or None) | PA native mechanism |
|---------------|-------------|--------------------------------|-------------------------------------|---------------------|

No compression. Each mitigation has a distinct Without-this-change consequence. Depends-on
chain must be non-circular.

### Section 4.C -- Tier-ID Coverage Audit

Verify every T-NN from TABLE 1 appears in: TABLE 2 (hit order), TABLE 3 (propagation chain
or terminal state), TABLE 4 (UX map), TABLE 9 (risk register). Flag any T-NN absent from any
downstream table with reason.

### Section 4.D -- Monitoring Signals

For each T-NN: the PA-native telemetry signal that would detect throttle approach before hit.
Specify: signal name, threshold, alert action. Generic "enable monitoring" does not pass.

### Section 4.E -- License and Entitlement Boundary

For each T-NN: the license tier required to access the documented limit. Flag any T-NN whose
numeric limit changes across license tiers. Identify if current scenario license tier is
binding.

### Section 4.F -- Phase 0 Forecast Reconciliation

Revisit each Phase 0 prediction:
1. Binding tier prediction: CONFIRMED or FALSIFIED. The TABLE 1 evidence (T-NN, STATUS column,
   QUOTA EXHAUSTION arithmetic) that confirms or falsifies it. If FALSIFIED: what structural
   assumption in the Phase 0 prediction was incorrect.
2. Burst path prediction: CONFIRMED or FALSIFIED. The TABLE 5 evidence that confirms or
   falsifies it. If FALSIFIED: what structural property of the scenario made the prediction
   incorrect.
3. Compounding failure mode prediction: CONFIRMED or FALSIFIED. The TABLE 6 and TABLE 7
   evidence. If FALSIFIED: the actual failure mode and why the Phase 0 reasoning was
   structurally incorrect.

*(A CONFIRMED prediction with no divergence analysis does not pass -- state whether the
evidence strengthens or merely restates the Phase 0 structural reason.)*

### Section 4.G -- PA Construct Precision Pass

**TABLE 11 -- PA Construct Precision Pass**

| T-NN | Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|------|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL: corrected below]` row: corrected content **immediately below** the
`[FAIL: corrected below]` annotation, before the next TABLE 11 row.

**CORRECTION GATE** is cleared when and only when every TABLE 11 row carries an explicit
disposition and every `[FAIL: corrected below]` row has corrected content immediately below
its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 11 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any `[FAIL: corrected below]` row is missing corrected content immediately below its
  annotation before the next row

### Section 4.H -- Test Approach

At least one concrete PA tooling test step. "Test in staging" does not pass. The step must
name the PA tooling artifact (test flow, analytics query, admin center report) and the
throttle behavior it is designed to surface.

---

## ROUND 2 -- Structural Precision Pass *(Role 4 -- Synthesizer, continued)*

**Independence:** ROUND 1 coherence -- including Phase 0 forecast reconciliation -- is not
evidence of construct-level precision. ROUND 2 operates independently. Corrected construct
names from TABLE 11 are now in scope.

For each T-NN in TABLE 11: PA construct name precision, numeric limit precision (source),
rate unit precision (matches documented enforcement granularity).

For each cascade pair in TABLE 7: causal mechanism precision (structural vs. qualitative --
promote with TABLE 9 arithmetic), load-added precision (numeric vs. directional -- compute
from TABLE 9 if directional), QUOTA EXHAUSTION PROJECTION precision (cites VOLUME ARITHMETIC
2x rate by name).

**TABLE 12 -- Round 2 Precision Audit**

| Item (TABLE ref + T-NN / Cascade-ID) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-01 prompt body.*

---

## V-02 -- Single-Axis: Phase 0 Quantified Tier-State Forecast (TABLE 0 form, potential C-39)

**Axis:** Phase 0 now produces TABLE 0 -- a tier prediction table with HIT/SAT/MISS state
commitments per tier category and arithmetic basis from a preliminary VOLUME ARITHMETIC sketch.
Phase 0 commits to a specific per-tier status prediction before Phase 1 enumerates T-NN rows.
TABLE 1's STATUS columns verify TABLE 0 predictions row-by-row. Phase 4 Section 4.F
reconciles TABLE 0 vs. TABLE 1 per tier-category row.

**Hypothesis:** v11 ceiling (26/26) + potential C-39 excellence signal. C-37 satisfied: Phase
0 has a named section before TABLE 1 with a TABLE 0 (stronger than V-05's prose form). C-38
satisfied: Phase 0 ASSUMPTION GAP at phase boundary, three-part structure. Potential C-39:
TABLE 0 tier-state predictions with arithmetic create a per-row prediction-verification
pairing -- Phase 1 TABLE 1 STATUS columns confirm or contradict each TABLE 0 entry, making any
divergence structurally visible in both tables simultaneously. Risk vector: model may place
TABLE 0 inside Phase 1 alongside TABLE 1 instead of in Phase 0. Prompt mitigates by
specifying TABLE 0 is completed in Phase 0, before Phase 1 begins, and is never modified
during Phase 1.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system. 5-phase lifecycle with Phase 0 quantified tier-state
forecast (TABLE 0).

**Phase structure:**
- Phase 0: Quantified Risk Forecast (TABLE 0 tier-state predictions with arithmetic; does not
  substitute for Phase 1 TABLE 1 enumeration)
- Phase 1: Construct Inventory (TABLE 1 -- authoritative)
- Phase 2: Bottleneck, Propagation, UX Analysis
- Phase 3: Exposure Analysis (burst paths, retry-after, cascades, test coverage)
- Phase 4: Synthesis, Precision Pass, TABLE 0 Reconciliation

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 0 -- Quantified Risk Forecast *(produce before Phase 1; TABLE 0 is frozen after Phase 0)*

**ASSUMPTION GAP -- PHASE 0 / PHASE 1 BOUNDARY:** Standard throttle analyses assume that
volume arithmetic should begin with a complete construct inventory -- that pre-inventory
arithmetic is speculative and produces unreliable predictions. This assumption fails: the
structural failure of beginning without a committed forecast is not imprecision but invisibility.
Without TABLE 0 tier-state commitments made before TABLE 1 enumeration, any STATUS entry in
TABLE 1 is a reactive assignment: the analyst can revise their expectation per-section as
evidence accumulates, and per-section volume interpretation can diverge from the aggregate
VOLUME ARITHMETIC baseline silently. TABLE 0 makes each divergence structurally visible --
a TABLE 1 STATUS that contradicts the TABLE 0 commitment for its category is a forecast
discrepancy, not an invisible revision.

**Phase 0 Volume Arithmetic Sketch** *(preliminary -- Phase 1 VOLUME ARITHMETIC is authoritative)*

1x baseline estimate: `[estimate from {{topic}} scenario description, show reasoning]` req/min
2x estimate: `[2 x baseline estimate]` req/min | 5x estimate: `[5 x baseline estimate]` req/min

*(Phase 1 VOLUME ARITHMETIC will compute the authoritative values. If Phase 1 values differ
from Phase 0 estimates, the Phase 0 Arithmetic column in TABLE 0 stands; Phase 4 Section 4.F
records the estimate-vs-actual discrepancy.)*

**TABLE 0 -- Tier-State Forecast**

| Category-ID | PA construct category | Predicted status at 1x | Predicted status at 2x | Predicted status at 5x | Arithmetic basis (Phase 0 estimate) | Structural reason |
|-------------|----------------------|------------------------|------------------------|------------------------|-------------------------------------|------------------|
| C-01 | (PA construct category) | HIT / SAT / MISS | HIT / SAT / MISS | HIT / SAT / MISS | (req/min from Phase 0 sketch vs. category limit) | (structural property of scenario) |

*Instructions for TABLE 0:*
- Each row names a PA construct category (not a T-NN -- T-NN identifiers are Phase 1 outputs).
- Predicted status values (HIT/SAT/MISS) must have arithmetic basis from the Phase 0 volume
  arithmetic sketch and a structural reason grounded in the scenario description.
- TABLE 0 is frozen at the end of Phase 0. No modifications during Phase 1 or Phase 2.
- Phase 1 TABLE 1 STATUS columns will confirm or contradict TABLE 0 predictions per category.

WRONG TABLE 0 entry: "C-01 | Connector throttling | HIT | HIT | HIT | Likely to be hit"
(no arithmetic, no structural reason)
PASS TABLE 0 entry: "C-01 | Power Platform per-user entitlement | HIT at 2x | HIT at 5x |
SAT at 1x | 400 req/min (1x estimate) vs. 40,000 req/24h = 1,667 req/min capacity;
1x < capacity, 2x = 800 req/min > hourly burst ceiling | Scenario describes shared service
principal across 3 flows; per-user entitlement accumulates across all flows sharing the
principal."

*Phase 0 does NOT substitute for Phase 1 TABLE 1 enumeration. GATE 1 still requires full
TABLE 1 completion with exact T-NN rows, documented construct types, and QUOTA EXHAUSTION
PROJECTION arithmetic. TABLE 0 is a prediction layer -- TABLE 1 is the authoritative
inventory.*

---

## PHASE 1 -- Construct Inventory

*(Role: Power Automate flow architect.)*

**ASSUMPTION GAP -- PHASE 1:** Standard throttle analyses assume all rate-limiting constructs
are visible in the flow canvas. This assumption fails: nested action quotas and premium
connector per-user windows appear only in platform documentation and admin center telemetry.
This analysis replaces canvas-inspection enumeration with documentation-sourced construct
inventory.

**VOLUME ARITHMETIC** *(authoritative -- may differ from Phase 0 sketch; record discrepancy
in Phase 4 Section 4.F if values differ)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 x baseline]` req/min | 5x: `[5 x baseline]` req/min
Unit conversion (if needed): `[show conversion factor]`

**TABLE 1 -- Throttle Tier Map**

| T-NN | Construct | PA construct type | PA construct category (maps to TABLE 0 Category-ID) | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|-----------------------------------------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (maps to C-NN) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule: each PA construct type must be drawn exactly from -- Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits.

WRONG: "Service rate limit" -- not a documented PA construct type.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" --
exact documented term.

**QUOTA EXHAUSTION PROJECTION**

For each HIT/SAT T-NN: `quota / rate_at_2x = minutes_to_depletion`. Cite 2x rate from
VOLUME ARITHMETIC by name.

WRONG: "T-01 will hit its quota." (no arithmetic)
PASS: "T-01: 40,000 req / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) exact PA construct
type from the domain list, (b) numeric limit with unit, (c) request contribution with
arithmetic, (d) populated Retry-After field, (e) PA construct category mapping to a TABLE 0
Category-ID, and (f) every HIT/SAT tier has QUOTA EXHAUSTION PROJECTION citing VOLUME
ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic construct type
- Any T-NN row is missing limit, contribution arithmetic, or Retry-After
- Any T-NN row is missing PA construct category mapping
- Any HIT/SAT tier lacks QUOTA EXHAUSTION PROJECTION with arithmetic

*PHASE 2 is blocked until GATE 1 is cleared.*

---

## PHASE 2 -- Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**ASSUMPTION GAP -- PHASE 2:** Standard bottleneck analyses assume the first construct to emit
a 429 is the binding constraint. This assumption fails: the binding tier is frequently a
per-user entitlement accumulating across all flows sharing a service principal. This analysis
replaces 429-first attribution with principal-pool-aware hit ordering grounded in TABLE 1
arithmetic.

### Section 2.A -- Rate Limit Hit Ordering

Write the bottleneck statement. Reference TABLE 0 Category-ID for the binding tier:

> "[T-NN construct] at [PA construct type] ([TABLE 0 Category-ID]) is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds].
> The naive assumption that limits are independent fails because [cascade chain or shared pool].
> TABLE 0 predicted [TABLE 0 Category-ID] as [HIT/SAT/MISS] at 2x -- this finding is
> [CONFIRMED / CONTRADICTS TABLE 0: state discrepancy]."

**TABLE 2 -- Hit Order**

| Hit order | T-NN | Construct | TABLE 0 Category-ID | Limit | Why this order holds |
|-----------|------|-----------|---------------------|-------|---------------------|
| 1 (bottleneck) | | | | | |
| 2 | | | | | |

### Section 2.B -- Backpressure Hop Chain

**TABLE 3 -- Backpressure Propagation**

| From component (T-NN) | Signal emitted | Signal type | To component (T-NN) | Response behavior |
|----------------------|---------------|-------------|---------------------|------------------|

Minimum: two hops. Named terminal state in final row.

### Section 2.C -- User Experience per Throttle Tier

**ASSUMPTION GAP -- SECTION 2.C:** Standard UX mapping assumes system behavior descriptions
constitute user experience entries. This assumption fails: system-internal descriptions are
unverifiable by a PA runtime reviewer. This analysis replaces system-state descriptions with
user-observable outcome statements categorized by UX impact type.

**TABLE 4 -- UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories
must differ. No tier omitted.

### Section 2.D -- Load Shape and Burst Sensitivity

f* = smallest f such that (total_volume / (f x window)) > binding_tier_limit

| Shape | f | Peak rate | vs. f* | Result | Mechanism citation |
|-------|---|-----------|--------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

---

**GATE 2** is cleared when and only when Section 2.A names every TABLE 1 tier in hit order;
TABLE 3 has >= 2 hops with named terminal state; TABLE 4 has entry for every tier with
distinct UX categories; BURST SHAPE MATRIX has f* derived; each row has independent mechanism
citation.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section 2.A omits any tier without explanation
- TABLE 3 fewer than 2 hops or missing terminal state
- TABLE 4 missing any tier or any two tiers sharing UX category
- f* not derived or any row missing mechanism citation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

## PHASE 3 -- Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**ASSUMPTION GAP -- PHASE 3:** Standard exposure analyses assume unprotected burst paths are
identifiable by canvas inspection. This assumption fails: Apply to Each concurrency and nested
action quota accumulation require documentation cross-reference to discover. This analysis
replaces canvas-inspection gap discovery with documentation-and-telemetry-anchored path
analysis.

### Section 3.A -- Unprotected Burst Paths (TABLE 5)
### Section 3.B -- Retry-After Gap Table (TABLE 6)
### Section 3.C -- Cascade Risk Register (TABLE 7)
### Section 3.D -- Test Coverage Gap Analysis

*(Sections 3.A through 3.D are structurally identical to V-01 PHASE 3 Sections 3.A through
3.D. All ASSUMPTION GAP blocks, WRONG/PASS exemplars, table structures, and gate conditions
are the same. Reproduce in full.)*

---

**GATE 3** is cleared when and only when TABLE 7 has >= 2 cascade pairs (all fields, distinct
Tier A / Tier B T-NN, named mechanisms, severity and duration); and Section 3.D has >= 2
STAGE 1 artifacts and >= 2 GAP-NN entries with all four fields non-generic.

*PHASE 4 is blocked until GATE 3 is cleared.*

---

## PHASE 4 -- Synthesis, Precision Pass, and TABLE 0 Reconciliation

*(GATE 3 must pass before this phase executes.)*

*(Sections 4.A through 4.E are structurally identical to V-01 PHASE 4 Sections 4.A through
4.E. TABLE 9, TABLE 10, Tier-ID Coverage Audit, Monitoring Signals, License Boundary.)*

### Section 4.F -- TABLE 0 Reconciliation

For each TABLE 0 Category-ID row:

1. Map to the TABLE 1 T-NN rows in that category.
2. Compare TABLE 0 predicted status (at 1x, 2x, 5x) to TABLE 1 actual STATUS columns.
3. Record: CONFIRMED (prediction matches TABLE 1 STATUS) or DIVERGED (prediction contradicts
   TABLE 1 STATUS; state which load band diverged and why).
4. For DIVERGED entries: identify the structural assumption in the Phase 0 prediction that was
   incorrect.
5. If Phase 0 Volume Arithmetic Sketch estimates differ from Phase 1 VOLUME ARITHMETIC
   authoritative values: record the estimate delta and its effect on prediction accuracy.

WRONG reconciliation: "TABLE 0 C-01 predicted HIT at 2x; TABLE 1 T-01 STATUS shows HIT
at 2x -- CONFIRMED." (no divergence analysis for CONFIRMED entries)
PASS reconciliation: "TABLE 0 C-01 predicted HIT at 2x; TABLE 1 T-01 STATUS shows HIT at 2x
-- CONFIRMED. The Phase 0 structural reason (shared service principal accumulation) is
strengthened by the TABLE 1 arithmetic: T-01 reaches 96% of limit at 1x, not the 60% the
Phase 0 estimate implied. The estimate-vs-actual delta (60% predicted vs. 96% actual) reflects
the Phase 0 sketch's undercount of flows sharing the principal."

### Section 4.G -- PA Construct Precision Pass (TABLE 11)
### Section 4.H -- Test Approach

*(Identical to V-01 PHASE 4 Sections 4.G and 4.H.)*

---

## ROUND 2 -- Structural Precision Pass

*(Identical to V-01 ROUND 2. TABLE 12. Independent of ROUND 1 coherence.)*

---

*End of V-02 prompt body.*

---

## V-03 -- Single-Axis: Conversational/Descriptive Register (C-37/C-38 register-inertia test)

**Axis:** Conversational/descriptive register throughout. ASSUMPTION GAP blocks, WRONG/PASS
exemplars, gate declarations, and Phase 0 forecast are present but phrased in an exploratory,
first-person-plural register ("you'll want to...", "the key question here is...", "notice that
...") rather than formal/technical imperative. All structural block labels (ASSUMPTION GAP,
WRONG, PASS) are retained unchanged. Tests whether C-37 and C-38 are register-inert.

**Hypothesis:** v11 ceiling (26/26). The rubric criteria operate on structural presence of
block labels and block types -- not on surrounding prose register. C-37 satisfied: Phase 0
section present with WRONG/PASS exemplar in conversational form. C-38 satisfied: Phase 0
ASSUMPTION GAP block with three-part structure, phrased conversationally but structurally
complete. C-35 satisfied: 5 WRONG/PASS exemplar sections (Phase 0 forecast, domain rule,
quota exhaustion, burst-path absence, test gap). C-36 satisfied: 5 ASSUMPTION GAP blocks
(Phase 0 boundary, Phase 1, Phase 2, Phase 3, Section 3.D). Risk vector: conversational
register may cause the model to collapse ASSUMPTION GAP blocks into flowing prose without
the three-part labeled structure. Prompt mitigates by explicitly requiring the ASSUMPTION GAP
label and three-part content regardless of surrounding tone.

---

You are a Connectors / Power Automate throughput domain expert. Let's walk through a thorough
simulation of throughput across a rate-limited Power Automate system together. The structure
here is designed to catch the things that standard analyses miss -- we'll start with a risk
forecast before touching any constructs, then inventory carefully, then analyze impact and
exposure, and finish with a precision pass.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 0 -- Risk Forecast *(produce before looking up any constructs)*

Here's the key methodological move that most throttle analyses skip: we're going to commit
to a prediction before we start enumerating anything. The reason this matters is explained
in the ASSUMPTION GAP block below.

**ASSUMPTION GAP -- PHASE 0 / PHASE 1 BOUNDARY:** You might assume that the right time to
assess throttle risk is after you've built the full construct inventory -- that any prediction
before enumeration is just guessing. This assumption turns out to cause a structural problem:
when you have no committed forecast, you can revise your per-section volume interpretation as
you go, and those revisions are invisible. Each table section can quietly adopt a different
implicit baseline, producing STATUS entries that diverge from each other without anyone
noticing. The fix is to commit the forecast before Phase 1 begins -- then any Phase 1 finding
that contradicts the forecast is a visible discrepancy, not a silent revision.

With just the scenario description in hand (no T-NN identifiers yet), give us:

1. **Which PA construct category is most likely to be the binding bottleneck at 2x load?**
   Walk us through the structural property of the scenario that makes you think so -- not
   a calculation, just the scenario property.

2. **Which PA construct category is most likely to have an unprotected burst path?**
   Again, the structural reason from the scenario description.

3. **What failure mode is most likely to make throttle recovery worse** -- retry-storm,
   silent-discard, or fixed-misalign? Why does the scenario point to that one?

Here's the form we're looking for:

WRONG: "The connector throttling limit will probably be hit." (no structural reason)
PASS: "Power Platform per-user entitlement is likely binding at 2x because the scenario
describes three flows sharing one service principal -- the entitlement accumulates across all
of them, so even if each flow looks fine in isolation, the shared principal pool fills up
faster than any per-flow analysis would suggest."

*Just to be explicit: this forecast doesn't let us skip Phase 1. GATE 1 still requires full
TABLE 1 completion. The forecast is a prediction we'll check in Phase 4 -- it doesn't
substitute for the inventory.*

---

## PHASE 1 -- Construct Inventory

*(Role: Power Automate flow architect.)*

**ASSUMPTION GAP -- PHASE 1:** Here's the tricky thing about construct enumeration: you'd
think you could get the full picture by inspecting the flow canvas, but nested action quotas
and premium connector per-user windows only show up in platform documentation and admin center
telemetry. You can't see them in the canvas. So we're replacing canvas inspection with a
documentation-sourced approach here.

**VOLUME ARITHMETIC**

Let's pin down the request volumes first so every STATUS column in TABLE 1 is working from
the same baseline.

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 x baseline]` req/min | 5x: `[5 x baseline]` req/min
Unit conversion (if needed): `[show conversion factor]`

**TABLE 1 -- Throttle Tier Map**

| T-NN | Construct | PA construct type | Numeric limit | Request contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------|---------------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Watch out for this -- it's the most common mistake here:

WRONG: "API rate limit" -- that's not a documented PA construct type. We can't match it to a
documented limit, which means we can't do the STATUS arithmetic.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" -- that's
the exact documented term. We can look up the numeric limit and compute the STATUS.

The types you can draw from: Power Platform request entitlements, connector throttling policies,
flow run concurrency limits, action call limits, premium vs. standard connector tiers,
Microsoft 365 service protection limits.

**QUOTA EXHAUSTION PROJECTION**

For any T-NN that's HIT or SAT: let's compute how fast it depletes at 2x. The formula is
`quota / rate_at_2x = minutes_to_depletion`. Cite the 2x rate from VOLUME ARITHMETIC.

WRONG: "T-01 will exhaust quota at 2x." (we need to see the arithmetic)
PASS: "T-01: 40,000 req / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion."

---

**GATE 1** -- we can move to Phase 2 once every TABLE 1 row has (a) exact PA construct type
from the domain list, (b) numeric limit with unit, (c) contribution arithmetic, (d) populated
Retry-After, and (e) QUOTA EXHAUSTION PROJECTION for every HIT/SAT tier citing VOLUME
ARITHMETIC 2x rate.

**We're blocked on GATE 1 if any of these are true:**
- Any row uses a generic construct type not from the domain list
- Any row is missing limit, contribution arithmetic, or Retry-After
- Any HIT/SAT tier lacks QUOTA EXHAUSTION PROJECTION with arithmetic

---

## PHASE 2 -- Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass.)*

**ASSUMPTION GAP -- PHASE 2:** It seems natural to declare the binding constraint as whichever
tier emits a 429 first. But this leads you astray when the real constraint is a per-user
entitlement that accumulates across flows sharing a service principal -- that tier might not
emit a 429 before other tiers, but it's the one that determines behavior at 2x load. So we're
grounding the bottleneck ordering in TABLE 1 arithmetic rather than 429-arrival order.

### Section 2.A -- Rate Limit Hit Ordering

Walk through the bottleneck statement for this scenario. The form we're looking for:

> "[T-NN construct] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] under this scenario because [why this ordering holds at aggregate volume].
> The naive assumption that limits are independent fails here because [cascade chain or shared
> principal pool]."

Then fill TABLE 2 with the hit ordering and the reason each ordering holds.

**TABLE 2 -- Hit Order**

| Hit order | T-NN | Construct | Limit | Why this order holds at scenario volume |
|-----------|------|-----------|-------|-----------------------------------------|
| 1 (bottleneck) | | | | |
| 2 | | | | |

### Section 2.B -- Backpressure Hop Chain

Let's trace what happens when the bottleneck fires. **TABLE 3** needs at least two hops and
a named terminal state in the final row -- we need to know where this ends up (user error,
flow run failure, or silent drop).

**TABLE 3 -- Backpressure Propagation**

| From (T-NN) | Signal emitted | Signal type | To (T-NN) | Response |
|-------------|---------------|-------------|-----------|----------|

Signal types: error code / retry-after header / queue depth increase / other.

### Section 2.C -- UX per Throttle Tier

**ASSUMPTION GAP -- SECTION 2.C:** It's tempting to describe what the system does internally
and call that the user experience. But a PA runtime reviewer can't observe internal system
state -- they can only observe what shows up for the user. So we're replacing system-state
descriptions with user-observable outcomes, classified by impact type.

**TABLE 4 -- UX Map**

| T-NN | Throttle tier | System action (internal) | User-visible experience | UX category |
|------|---------------|--------------------------|------------------------|-------------|

The UX categories to use: transparent-retry / visible-delay / error-surfaced / silent-loss.
Pick different categories for different tiers -- if two tiers share a category, we lose
information. Don't omit any tier.

### Section 2.D -- Load Shape and Burst Sensitivity

f* is the smallest concentration factor f at which the binding tier tips from SAT to HIT:
`f* = f such that (total_volume / (f x window)) > binding_tier_limit`

| Shape | f | Peak rate | vs. f* | Result | Mechanism citation |
|-------|---|-----------|--------|--------|--------------------|
| Uniform | 1.0 | | | | |
| Moderate burst | 0.3 | | | | |
| Severe burst | 0.1 | | | | |

Each row needs its own mechanism citation.

---

**GATE 2** -- we can proceed to Phase 3 once Section 2.A covers every tier in hit-order
reasoning; TABLE 3 has at least two hops with a named terminal state; TABLE 4 has an entry
per tier with distinct UX categories; and every BURST SHAPE MATRIX row has a mechanism
citation with f* derived.

---

## PHASE 3 -- Exposure Analysis

*(GATE 2 must pass.)*

**ASSUMPTION GAP -- PHASE 3:** Canvas inspection seems like it should catch burst paths --
you can see the flow structure. But Apply to Each concurrency caps and nested action quota
accumulation only become visible when you cross-reference documentation and admin telemetry.
So we're replacing canvas inspection with a documentation-and-telemetry-anchored approach.

*(Sections 3.A through 3.D structurally identical to V-01 PHASE 3 -- TABLE 5, TABLE 6,
TABLE 7, test coverage gap analysis. Translate all structural requirements, gate conditions,
WRONG/PASS exemplars, and ASSUMPTION GAP blocks into conversational register. ASSUMPTION GAP
and WRONG/PASS labels must appear unchanged regardless of surrounding prose tone.)*

---

**GATE 3** -- structurally identical to V-01 GATE 3 conditions. *(TABLE 7 >= 2 cascade pairs,
Section 3.D >= 2 STAGE 1 artifacts and >= 2 GAP-NN entries.)*

---

## PHASE 4 -- Synthesis, Precision Pass, and Forecast Reconciliation

*(GATE 3 must pass.)*

*(Sections 4.A through 4.H structurally identical to V-01 PHASE 4, translated into
conversational register. Phase 4 Section 4.F forecast reconciliation: revisit each Phase 0
prediction with TABLE 1 and TABLE 7 evidence, CONFIRMED or FALSIFIED, divergence analysis
required for CONFIRMED entries. All labels -- ASSUMPTION GAP, WRONG, PASS, CORRECTION GATE,
disposition tags -- must appear unchanged.)*

---

## ROUND 2 -- Structural Precision Pass

*(Structurally identical to V-01 ROUND 2, translated into conversational register. TABLE 12.)*

---

*End of V-03 prompt body.*

---

## V-04 -- Single-Axis: Phase 4 Forecast Reconciliation with 3-Axis Error Taxonomy (potential C-39)

**Axis:** Phase 4 Section 4.F now applies a 3-axis error taxonomy to each Phase 0 prediction
outcome rather than a binary CONFIRMED / FALSIFIED classification. Error types:
- TYPE-0: CONFIRMED (prediction matches TABLE 1 STATUS and TABLE 7 mechanism evidence)
- TYPE-1 STRUCTURAL-MISS: Wrong PA construct category predicted as binding/burst-prone --
  the category itself was incorrect
- TYPE-2 MAGNITUDE-MISS: Correct PA construct category, wrong predicted severity (e.g.,
  predicted SAT, actual HIT) -- the category was right but the volume reasoning was incorrect
- TYPE-3 MECHANISM-MISS: Correct tier category, correct severity, wrong failure mode --
  the propagation mechanism was mispredicted

Each non-TYPE-0 entry requires: (a) the error type, (b) the TABLE 1 / TABLE 7 evidence
demonstrating the mis-prediction, (c) the root-cause structural assumption in Phase 0 that
produced the error, (d) the corrected reasoning that Phase 0 should have used.

**Hypothesis:** v11 ceiling (26/26) + potential C-39 excellence signal. C-37 satisfied: Phase
0 present. C-38 satisfied: Phase 0 ASSUMPTION GAP at phase boundary. Potential C-39: the
3-axis taxonomy converts Phase 4 reconciliation from a binary outcome pass/fail into a
structured causal audit -- each Phase 0 prediction is diagnosed not just as right-or-wrong
but with a root-cause classification, making the forecast a learning instrument rather than
a confirmation exercise. Risk vector: the model may classify all Phase 0 predictions as
TYPE-0 (confirmed) to avoid engaging the taxonomy. Prompt mitigates by requiring at least one
non-TYPE-0 entry with full evidence, and by declaring that TYPE-0 entries still require
divergence analysis (a confirmed prediction with no divergence analysis fails).

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system. 5-phase lifecycle with Phase 0 risk forecast and Phase 4
3-axis forecast error taxonomy.

**Phase structure:**
- Phase 0: Risk Forecast (3 structural predictions; ASSUMPTION GAP at phase boundary)
- Phase 1: Construct Inventory
- Phase 2: Bottleneck, Propagation, UX Analysis
- Phase 3: Exposure Analysis
- Phase 4: Synthesis, Precision Pass, 3-Axis Forecast Error Taxonomy

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 0 -- Risk Forecast

*(Produce before any TABLE 1 enumeration.)*

**ASSUMPTION GAP -- PHASE 0 / PHASE 1 BOUNDARY:** Standard throttle analyses assume that
risk prediction before construct enumeration is speculative and therefore unreliable. This
assumption fails: the structural failure of beginning without a forecast is not imprecision
but undetectability. Without Phase 0 commitments, per-section volume interpretations can
diverge from the aggregate VOLUME ARITHMETIC baseline as the analyst encounters each tier --
and each such divergence is invisible, because there is no prior commitment to contradict.
Phase 0 makes forecast errors structurally detectable. Phase 4 uses a 3-axis error taxonomy
to classify each Phase 0 prediction outcome -- not as right-or-wrong, but as which structural
assumption failed and why. This converts the forecast from a qualitative prediction into a
learning instrument: the type of error reveals the type of structural blind spot in pre-
inventory reasoning.

Produce three predictions using only the scenario description (no T-NN identifiers):

1. **Binding tier prediction:** The PA construct category most likely to be the binding
   bottleneck at 2x load. State the structural reason.

2. **Burst path prediction:** The PA construct category most likely to have an unprotected
   burst path. State the structural reason.

3. **Compounding failure mode prediction:** The failure mode most likely to compound throttle
   recovery. Options: retry-storm / silent-discard / fixed-misalign. State the structural
   reason.

WRONG forecast: "Connector throttling limits will be binding." (category without structural
reason)
PASS forecast: "Power Platform per-user request entitlement is likely binding at 2x because
the scenario describes multiple flows sharing one service principal -- that shared-principal
pool accumulation is not visible per-flow and causes the entitlement to fill faster than
any per-flow analysis predicts."

*Phase 0 does NOT substitute for Phase 1. GATE 1 still covers full TABLE 1 completion.*

---

## PHASE 1 -- Construct Inventory

*(ASSUMPTION GAP, VOLUME ARITHMETIC, TABLE 1, QUOTA EXHAUSTION PROJECTION, GATE 1 --
structurally identical to V-01 PHASE 1. Reproduce in full.)*

---

## PHASE 2 -- Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass. Sections 2.A through 2.D -- structurally identical to V-01 PHASE 2.
ASSUMPTION GAP blocks, WRONG/PASS exemplars, TABLE 2, TABLE 3, TABLE 4, BURST SHAPE MATRIX,
GATE 2 -- reproduce in full.)*

---

## PHASE 3 -- Exposure Analysis

*(GATE 2 must pass. Sections 3.A through 3.D -- structurally identical to V-01 PHASE 3.
TABLE 5, TABLE 6, TABLE 7, test coverage gap analysis, GATE 3 -- reproduce in full.)*

---

## PHASE 4 -- Synthesis, Precision Pass, and 3-Axis Forecast Error Taxonomy

*(GATE 3 must pass.)*

*(Sections 4.A through 4.E -- structurally identical to V-01 PHASE 4 Sections 4.A through
4.E: TABLE 9, TABLE 10, Tier-ID Coverage Audit, Monitoring Signals, License Boundary.)*

### Section 4.F -- 3-Axis Forecast Error Taxonomy

For each Phase 0 prediction, apply the following taxonomy:

**Error types:**
- TYPE-0 CONFIRMED: The prediction matches TABLE 1 STATUS and TABLE 7 evidence.
- TYPE-1 STRUCTURAL-MISS: The predicted PA construct category was incorrect -- a different
  category is the actual binding/burst/compounding construct.
- TYPE-2 MAGNITUDE-MISS: The predicted category was correct, but the predicted severity
  (HIT/SAT/MISS or failure mode severity) was incorrect.
- TYPE-3 MECHANISM-MISS: The predicted category and severity were correct, but the
  structural mechanism was mispredicted (e.g., predicted single-flow saturation; actual is
  cross-flow shared-principal accumulation).

**For each prediction (1 through 3), produce:**

```
Prediction [N]: [restate the Phase 0 prediction]
Error type: TYPE-[0/1/2/3] [type name]
Evidence: [TABLE 1 / TABLE 7 evidence demonstrating the outcome]
Root cause (if non-TYPE-0): [the structural assumption in Phase 0 that produced the error]
Corrected reasoning (if non-TYPE-0): [the reasoning that Phase 0 should have used, given
the scenario properties visible before enumeration]
```

**Requirements:**
- At least one prediction must be classified as non-TYPE-0 with full evidence and root cause.
  (A simulation where all three Phase 0 predictions are perfectly TYPE-0-confirmed is a signal
  that the forecast was not ambitious enough -- restate Phase 0 predictions with more specific
  claims if needed to produce at least one non-TYPE-0 finding.)
- TYPE-0 entries still require a divergence analysis: state whether the TABLE 1 / TABLE 7
  evidence strengthens the Phase 0 structural reason or merely restates it. A TYPE-0 with no
  divergence analysis fails.

WRONG TYPE-0: "Prediction 1: Power Platform entitlement -- TYPE-0 CONFIRMED. TABLE 1 T-01
shows HIT at 2x." (no divergence analysis)
PASS TYPE-0: "Prediction 1: Power Platform entitlement -- TYPE-0 CONFIRMED. TABLE 1 T-01
shows HIT at 2x at 96% of limit. The Phase 0 structural reason (shared-principal accumulation)
is strengthened: the TABLE 1 QUOTA EXHAUSTION PROJECTION shows depletion in 50 min at 2x,
which is faster than any single-flow analysis would predict -- confirming that the shared-
principal pool was the correct structural frame, not just the most likely category."

WRONG TYPE-1: "Prediction 2: Apply to Each concurrency -- TYPE-1 STRUCTURAL-MISS. The actual
burst path is the connector retry loop." (no root cause, no corrected reasoning)
PASS TYPE-1: "Prediction 2: Apply to Each concurrency as the unprotected burst path --
TYPE-1 STRUCTURAL-MISS. TABLE 5 shows the actual unprotected burst path is the connector
retry loop (Path-ID P-02), not the Apply to Each iterator. Root cause: Phase 0 predicted
Apply to Each because the scenario description mentioned nested iteration, but the structural
property that enables unprotected burst is the absence of Retry-After header reading in the
connector action -- which is a property of the action implementation, not the iterator.
Corrected reasoning: in scenarios where the trigger is connector-action-based, examine the
action's Retry-After read status before predicting Apply to Each as the burst path."

### Section 4.G -- PA Construct Precision Pass (TABLE 11)
### Section 4.H -- Test Approach

*(Identical to V-01 PHASE 4 Sections 4.G and 4.H.)*

---

## ROUND 2 -- Structural Precision Pass

*(Identical to V-01 ROUND 2. TABLE 12. Independent of ROUND 1 coherence.)*

---

*End of V-04 prompt body.*

---

## V-05 -- Combination: 4-Role + Phase 0 TABLE 0 + Phase 4 3-Axis Error Taxonomy

**Axis:** Full combination of V-01 (4-role cardinality), V-02 (Phase 0 TABLE 0 with quantified
HIT/SAT/MISS predictions and arithmetic basis), and V-04 (Phase 4 3-axis forecast error
taxonomy). Maximum structural load: Role 1 produces Phase 0 TABLE 0 with preliminary arithmetic
sketch; Role 2 enumerates Phase 1 TABLE 1 with category mapping to TABLE 0; Roles 3 and 4
carry ASSUMPTION GAP blocks and WRONG/PASS exemplars as in prior combinations; Phase 4
Section 4.F applies the 3-axis taxonomy to each TABLE 0 Category-ID row.

**Hypothesis:** v11 ceiling (26/26) + both potential excellence signals (TABLE 0 quantified
predictions from V-02, 3-axis error taxonomy from V-04). C-37: Phase 0 TABLE 0 is a named
phase with a section before TABLE 1 -- stronger than V-05's R11 prose form. C-38: Phase 0
ASSUMPTION GAP at the Role 1 / Role 2 phase boundary. C-35: 5+ WRONG/PASS exemplar sections
(Phase 0 forecast form, domain rule, quota exhaustion, burst-path absence, test gap, TABLE 0
reconciliation). C-36: 5+ ASSUMPTION GAP blocks (Phase 0 boundary, Phase 1, Phase 2,
Phase 3, Section 3.D). Risk vector: maximum load may cause Role 2 to collapse TABLE 0 and
TABLE 1 into a single table with predicted and actual columns. Prompt mitigates by declaring
TABLE 0 belongs to Phase 0 (Role 1 output), is frozen before Phase 1 begins, and TABLE 1 is
a separate Phase 1 (Role 2) output that maps back to TABLE 0 categories.

---

You are simulating throughput across a rate-limited Power Automate system. 4-role function
split with Phase 0 quantified tier-state forecast (TABLE 0) and Phase 4 3-axis error taxonomy.

**Role assignments:**
- **Role 1 -- Risk Forecaster:** Phase 0 only. Produces TABLE 0 (tier-state predictions with
  preliminary arithmetic sketch) and Phase-boundary ASSUMPTION GAP. TABLE 0 is frozen at end
  of Phase 0 and is never modified by Role 2 or later roles.
- **Role 2 -- Construct Enumerator:** Phase 1 only. VOLUME ARITHMETIC (authoritative), TABLE 1
  with PA construct category mapping to TABLE 0 Category-IDs, QUOTA EXHAUSTION PROJECTION.
  Opens Phase 1 with Role 1 handoff confirmation.
- **Role 3 -- Impact Analyst:** Phase 2 and Phase 3. Bottleneck, propagation, UX, load shape
  (Phase 2); burst paths, retry-after, cascade risk, test coverage (Phase 3). Opens each phase
  with prior-role handoff confirmation.
- **Role 4 -- Synthesizer + Validator:** Phase 4. Quantified risk register, mitigation registry,
  tier-ID coverage audit, monitoring, license boundary, TABLE 11 precision pass, TABLE 0
  3-axis reconciliation, test approach. Opens Phase 4 with Role 3 handoff confirmation.

**Phase-entry handoff form (required):**
- Phase 1: `*(Role 1 Risk Forecaster handoff complete -- proceed to Phase 1.)*`
- Phase 2: `*(Role 2 Construct Enumerator handoff complete -- GATE 1 cleared. Proceed to Phase 2.)*`
- Phase 3: `*(Role 3 Impact Analyst Phase 2 handoff complete -- GATE 2 cleared. Proceed to Phase 3.)*`
- Phase 4: `*(Role 3 Impact Analyst Phase 3 handoff complete -- GATE 3 cleared. Proceed to Phase 4.)*`

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 0 -- Quantified Risk Forecast *(Role 1 -- Risk Forecaster)*

*Produce before Phase 1. TABLE 0 is Role 1's output and is frozen at the end of Phase 0.
Role 2 maps TABLE 1 rows to TABLE 0 Category-IDs; Role 2 does not modify TABLE 0.*

**ASSUMPTION GAP -- PHASE 0 / PHASE 1 BOUNDARY:** Standard throttle analyses assume that
construct enumeration should precede risk assessment, and that any pre-inventory prediction
is unreliable because it lacks T-NN-level arithmetic. This assumption fails at two levels:
(1) the structural failure is not imprecision but invisibility -- without TABLE 0 commitments,
Role 2's per-tier STATUS entries in TABLE 1 can silently diverge from Role 1's volume
arithmetic baseline because there is no committed prediction to detect the divergence; (2) a
quantified TABLE 0 with preliminary arithmetic is not arbitrary -- it uses the same scenario-
level volume properties that Role 2's VOLUME ARITHMETIC will formalize, making TABLE 0
predictions verifiable against TABLE 1 STATUS, not merely qualitative. The Phase 4 3-axis
taxonomy classifies each TABLE 0 / TABLE 1 divergence by error type, converting the
prediction layer into a structural learning instrument rather than a one-time qualitative
exercise.

**Phase 0 Volume Arithmetic Sketch** *(preliminary; Phase 1 VOLUME ARITHMETIC is authoritative)*

1x baseline estimate: `[estimate from {{topic}} scenario description, show reasoning]` req/min
2x estimate: `[2 x baseline estimate]` req/min | 5x: `[5 x baseline estimate]` req/min

*(If Phase 1 VOLUME ARITHMETIC values differ from Phase 0 estimates, Phase 0 Arithmetic
Basis entries in TABLE 0 stand as committed predictions. Phase 4 Section 4.F records the
estimate-vs-actual delta.)*

**TABLE 0 -- Tier-State Forecast** *(Role 1 output; frozen after Phase 0)*

| Category-ID | PA construct category | Predicted status at 1x | Predicted status at 2x | Predicted status at 5x | Arithmetic basis (Phase 0 estimate) | Structural reason |
|-------------|----------------------|------------------------|------------------------|------------------------|-------------------------------------|------------------|
| C-01 | (PA construct category) | HIT / SAT / MISS | HIT / SAT / MISS | HIT / SAT / MISS | (req/min from Phase 0 sketch vs. category limit) | (structural property) |

*Instructions for TABLE 0:*
- Each row names a PA construct category (not a T-NN identifier -- T-NN rows are Phase 1
  outputs).
- Predicted status values (HIT/SAT/MISS) must have arithmetic basis from the Phase 0 volume
  sketch and a structural reason from the scenario description.
- TABLE 0 is frozen after Phase 0. Role 2 maps TABLE 1 T-NN rows to TABLE 0 Category-IDs;
  neither Role 2 nor later roles modify TABLE 0 entries.
- Phase 4 Section 4.F applies the 3-axis taxonomy to compare TABLE 0 predictions against
  TABLE 1 STATUS columns.

WRONG TABLE 0 entry: "C-01 | Connector throttling | HIT | HIT | HIT | Will be hit"
(no arithmetic, no structural reason)
PASS TABLE 0 entry: "C-01 | Power Platform per-user entitlement | SAT at 1x | HIT at 2x |
HIT at 5x | 400 req/min (1x estimate) vs. 40,000 req/24h = 1,667 req/min capacity; 1x is
24% of capacity (SAT), 2x = 800 req/min exceeds burst ceiling (HIT), 5x is far over |
Scenario describes 3 flows sharing one service principal; entitlement accumulates across
all three flows."

*Phase 0 does NOT substitute for Phase 1 inventory. GATE 1 still requires full TABLE 1
completion. TABLE 0 is a prediction layer only.*

---

## PHASE 1 -- Construct Inventory *(Role 2 -- Construct Enumerator)*

*(Role 1 Risk Forecaster handoff complete -- proceed to Phase 1.)*

**ASSUMPTION GAP -- PHASE 1:** Standard throttle analyses assume all rate-limiting constructs
are visible in the flow canvas. This assumption fails: nested action quotas and premium
connector per-user windows appear only in platform documentation and admin center telemetry.
This analysis replaces canvas-inspection enumeration with documentation-sourced construct
inventory.

**VOLUME ARITHMETIC** *(authoritative; record delta from Phase 0 estimate if values differ)*

1x baseline: `[compute from {{topic}} scenario description]` req/min with explicit units
2x: `[2 x baseline]` req/min | 5x: `[5 x baseline]` req/min
Unit conversion (if needed): `[show conversion factor]`

**TABLE 1 -- Throttle Tier Map**

| T-NN | Construct | PA construct type | TABLE 0 Category-ID | Numeric limit | Contribution at 1x | Status at 1x | Status at 2x | Status at 5x | Retry-After read? | Failure visibility window |
|------|-----------|------------------|---------------------|---------------|-------------------|-------------|-------------|-------------|-------------------|-----------------------------|
| T-01 | (fill) | (exact PA term) | (C-NN from TABLE 0) | (N req/unit) | (arithmetic) | | | | yes / no / N/A | |

Domain rule: each PA construct type must be drawn exactly from -- Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits.

WRONG: "API rate limit" -- generic, not a documented PA construct type.
PASS: "Power Platform per-user request entitlement (licensed user, per-24-hour window)" --
exact documented term.

**QUOTA EXHAUSTION PROJECTION**

For each HIT/SAT T-NN: `quota / rate_at_2x = minutes_to_depletion`. Cite 2x from VOLUME
ARITHMETIC by name.

WRONG: "T-01 will exhaust quota at 2x." (no arithmetic)
PASS: "T-01: 40,000 req / 800 req/min (2x from VOLUME ARITHMETIC) = 50 min to depletion."

---

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) exact PA construct
type from the domain list, (b) numeric limit with unit, (c) contribution arithmetic, (d)
populated Retry-After field, (e) TABLE 0 Category-ID mapping, and (f) every HIT/SAT tier
has QUOTA EXHAUSTION PROJECTION citing VOLUME ARITHMETIC 2x rate.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any T-NN row uses a generic construct type
- Any T-NN row is missing limit, arithmetic, Retry-After, or TABLE 0 Category-ID
- Any HIT/SAT tier lacks QUOTA EXHAUSTION PROJECTION with arithmetic

*PHASE 2 is blocked until GATE 1 is cleared.*

---

## PHASE 2 -- Bottleneck, Propagation, and UX Analysis *(Role 3 -- Impact Analyst)*

*(Role 2 Construct Enumerator handoff complete -- GATE 1 cleared. Proceed to Phase 2.)*

**ASSUMPTION GAP -- PHASE 2:** Standard bottleneck analyses assume the first construct to emit
a 429 is the binding constraint. This assumption fails: the binding tier is frequently a
per-user entitlement accumulating across flows sharing a service principal. This analysis
replaces 429-first attribution with principal-pool-aware hit ordering grounded in TABLE 1
arithmetic.

*(Sections 2.A through 2.D structurally identical to V-01 PHASE 2. For Section 2.A bottleneck
statement, reference TABLE 0 Category-ID of the binding tier and note whether TABLE 1 confirms
the TABLE 0 prediction for that category at 2x. ASSUMPTION GAP blocks, WRONG/PASS exemplars,
TABLE 2, TABLE 3, TABLE 4, BURST SHAPE MATRIX, GATE 2 -- reproduce in full.)*

---

## PHASE 3 -- Exposure Analysis *(Role 3 -- Impact Analyst, continued)*

*(Role 3 Impact Analyst Phase 2 handoff complete -- GATE 2 cleared. Proceed to Phase 3.)*

*(Sections 3.A through 3.D structurally identical to V-01 PHASE 3. ASSUMPTION GAP blocks,
TABLE 5, TABLE 6, TABLE 7, test coverage gap analysis, GATE 3 -- reproduce in full.)*

---

## PHASE 4 -- Synthesis, Precision Pass, and TABLE 0 3-Axis Reconciliation *(Role 4 -- Synthesizer)*

*(Role 3 Impact Analyst Phase 3 handoff complete -- GATE 3 cleared. Proceed to Phase 4.)*

*(Sections 4.A through 4.E structurally identical to V-01 PHASE 4 Sections 4.A through 4.E.)*

### Section 4.F -- TABLE 0 3-Axis Reconciliation

For each TABLE 0 Category-ID row:

**Step 1 -- TABLE 1 mapping:** List the TABLE 1 T-NN rows that map to this Category-ID.

**Step 2 -- Status comparison:** Compare TABLE 0 predicted status (at 1x, 2x, 5x) to TABLE 1
actual STATUS columns for each mapped T-NN. Note any load-band divergence.

**Step 3 -- Error type classification:**
- TYPE-0 CONFIRMED: Predicted status matches TABLE 1 STATUS for all load bands.
- TYPE-1 STRUCTURAL-MISS: A different PA construct category (a different Category-ID or a
  category not in TABLE 0) is the actual binding/burst/compounding construct.
- TYPE-2 MAGNITUDE-MISS: Correct category, wrong predicted severity at one or more load bands.
- TYPE-3 MECHANISM-MISS: Correct category and severity, wrong structural mechanism.

**Step 4 -- Divergence analysis (all types including TYPE-0):**
- TYPE-0: State whether TABLE 1 arithmetic strengthens or merely restates the Phase 0
  structural reason. A TYPE-0 with no divergence analysis fails.
- TYPE-1/2/3: State (a) the root-cause structural assumption in Phase 0 that produced the
  error, (b) the corrected reasoning Phase 0 should have used, (c) whether the error type
  is predictable from scenario description alone (i.e., could a better Phase 0 have avoided
  this error type).

**Step 5 -- Estimate delta (if Phase 1 VOLUME ARITHMETIC values differ from Phase 0 sketch):**
Record the delta and its effect on prediction accuracy for this category.

**Requirements:**
- At least one Category-ID must be classified as non-TYPE-0 with full 4-step content.
- A simulation where all Category-IDs are TYPE-0 is a signal the TABLE 0 predictions were
  not specific enough. Restating Phase 0 predictions with more granular claims is required
  to produce at least one non-TYPE-0 finding.

WRONG Type-0: "C-01 -- TYPE-0 CONFIRMED. T-01 shows HIT at 2x." (no divergence analysis)
PASS TYPE-2: "C-01 -- TYPE-2 MAGNITUDE-MISS. TABLE 0 predicted SAT at 1x; TABLE 1 T-01
shows HIT at 1x (contribution = 1,450 req/min vs. limit of 1,667 req/min, 87% -- HIT
threshold). Root cause: Phase 0 sketch used 400 req/min as 1x baseline estimate vs. TABLE 1
VOLUME ARITHMETIC authoritative 1x of 967 req/min -- a 2.4x undercount. The Phase 0 estimate
failed to account for background flows on the same service principal that are visible in
admin center telemetry but not in the scenario description. Corrected Phase 0 reasoning:
scenarios describing shared-principal architectures should assume background flow contribution
at minimum 20% of the stated scenario volume, adjusting the 1x baseline accordingly. This
error type (TYPE-2 MAGNITUDE-MISS) is partially predictable from scenario description -- the
phrase 'shared service principal' implies background accumulation risk."

### Section 4.G -- PA Construct Precision Pass (TABLE 11)
### Section 4.H -- Test Approach

*(Identical to V-01 PHASE 4 Sections 4.G and 4.H.)*

---

## ROUND 2 -- Structural Precision Pass *(Role 4 -- Synthesizer, continued)*

*(Identical to V-01 ROUND 2. TABLE 12. Independent of ROUND 1 coherence.)*

---

*End of V-05 prompt body.*

---

## Round 12 Scorecard Predictions

| Variation | Axis | C-37 | C-38 | C-35 | C-36 | Prior criteria | Total (/26) | Composite |
|-----------|------|------|------|------|------|----------------|-------------|-----------|
| V-01 | 4-role cardinality | PASS | PASS | PASS | PASS | PASS | 26/26 | 100 |
| V-02 | Phase 0 TABLE 0 | PASS | PASS | PASS | PASS | PASS | 26/26 + excellence | 100 |
| V-03 | Conversational register | PASS | PASS | PASS | PASS | PASS | 26/26 | 100 |
| V-04 | Phase 4 3-axis taxonomy | PASS | PASS | PASS | PASS | PASS | 26/26 + excellence | 100 |
| V-05 | 4-role + TABLE 0 + taxonomy | PASS | PASS | PASS | PASS | PASS | 26/26 + excellence | 100 |

**Excellence signal candidates for rubric v12:**
- C-39 candidate A (V-02 / V-05): Phase 0 TABLE 0 -- quantified tier-state predictions with
  HIT/SAT/MISS per category and arithmetic basis from preliminary volume sketch, enabling per-
  row prediction-verification pairing with TABLE 1 STATUS columns. Creates a structurally
  visible divergence layer between Phase 0 and Phase 1 that prose predictions cannot provide.
- C-39 candidate B (V-04 / V-05): Phase 4 3-axis forecast error taxonomy -- classifying Phase 0
  prediction outcomes as TYPE-0/1/2/3 (CONFIRMED / STRUCTURAL-MISS / MAGNITUDE-MISS /
  MECHANISM-MISS) with root-cause analysis and corrected reasoning. Converts the forecast
  reconciliation from a binary correctness check into a causal learning audit.
- If both candidates confirm in R12 scoring: they may be extracted as C-39 (TABLE 0 form) and
  C-40 (3-axis taxonomy) in rubric v12, advancing the denominator from 26 to 28.
