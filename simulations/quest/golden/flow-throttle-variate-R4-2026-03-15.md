# flow-throttle Variate — Round 4
**Date:** 2026-03-15
**Rubric:** v4 (C-01 through C-16, essential/recommended/aspirational, denominator /8 aspirational)
**Baseline ceiling:** R3 V-05 (~99/100 under v4: 7/8 aspirational; C-09 and C-10 remain open)

---

## Round 4 State Analysis: What R3 Established vs. What R4 Must Add

**R3 confirmed (all carry forward):**
- C-01 through C-08: Essential and recommended criteria pass reliably across all R3 variations.
- C-11 (multi-volume sweep): TABLE A STATUS 1x/2x/5x columns force three-band coverage; binding
  constraint shift is visible as a column comparison.
- C-12 (cross-section T-NN traceability): T-NN identifiers propagate through TABLE B, C, D, and
  cascade scenario without synonym drift.
- C-13 (test coverage gap identification): Phase-required TABLE E with four-column template passes
  when structurally enforced.
- C-14 (test infrastructure inertia catalog): Named artifact catalog before TABLE E, with
  structural property per artifact, passes in R3 V-04 and V-05.
- C-15 (labeled gap entry completeness): TABLE E four-column format with column-level pass
  conditions enforces completeness by inspection.
- C-16 (negative exemplar contrast injection): R3 V-05's WRONG/PASS contrasts adjacent to
  Stage 1 catalog and TABLE E column definitions pass C-16. R3 V-04 lacks these contrasts and
  scores 6/8 aspirational under v4.

**R3 gaps (what Round 4 must close):**

C-09 — Mitigation prescriptions: R3 variations identify gaps (burst paths, missing retry-after,
cascade risk) but do not prescribe concrete remediations at the configuration or implementation
level. "Add retry logic" appears or equivalent generic advice is the best output. C-09 requires
component name + specific setting or API parameter + change + expected outcome. No R3 variation
included a structured mitigation section.

C-10 — Load shape sensitivity: R3's TABLE A STATUS 1x/2x/5x columns address volume magnitude
(different totals) but not arrival pattern (same total, different distribution). C-10 requires
demonstrating that the same total request count produces different throttle outcomes depending on
whether traffic arrives uniformly (e.g., 10 req/sec) vs. spiky (e.g., 60 req/sec for 10 seconds,
then idle). No R3 variation included a uniform-vs-burst comparison at fixed volume.

**What Round 4 must demonstrate:**

Q1 (V-01): Does a dedicated TABLE F (MITIGATION REGISTRY) with structured columns
(component / setting-or-parameter / change / expected-outcome) produce C-09-passing output by
making "add retry logic" fail the Setting-or-parameter column by inspection — the same way
TABLE E's column definitions make "add load testing" fail the Test-approach column?

Q2 (V-02): Does a standalone LOAD SHAPE COMPARISON section — requiring one numeric comparison
at fixed 1x volume between uniform arrival and burst arrival — produce C-10's arrival-pattern
distinction without a full separate table, relying on prose that the model can verify against
TABLE A's rate limit values?

Q3 (V-03): Does carrying R3 V-05's WRONG/PASS exemplar injection from the test coverage section
directly into an R3-V-04-based prompt (which lacks exemplars) produce reliable C-16 passage in
isolation — and does adding the contrast adjacent to TABLE E produce higher C-14/C-15 stability
compared to V-04 baseline without exemplars?

Q4 (V-04): Does combining TABLE F (C-09) + LOAD SHAPE COMPARISON (C-10) + test-section exemplars
(C-16) achieve 100/100 under v4 without one axis crowding another under token pressure — and
does the adjacency of the exemplar to TABLE F's column definitions simultaneously satisfy C-16
at the mitigation section as well as the test section?

Q5 (V-05): Does the maximum-density variant — V-04's TABLE F + LOAD SHAPE + exemplars plus
R3 V-03's stage gating (STAGE 1 catalog gates STAGE 2 TABLE E) — add structural robustness to
C-14 and C-15 without introducing token-budget pressure that degrades TABLE F or LOAD SHAPE?

---

## Round 4 Variation Map

| Variation | Axis | New criteria targeted | Predicted composite |
|-----------|------|-----------------------|---------------------|
| V-01 | Single: C-09 structured mitigation registry (TABLE F) | C-09 | ~91/100 |
| V-02 | Single: C-10 arrival shape comparison (LOAD SHAPE section) | C-10 | ~90/100 |
| V-03 | Single: C-16 negative exemplar injection from R3 V-05 into R3 V-04 base | C-16 | ~92/100 |
| V-04 | Combined: TABLE F + LOAD SHAPE + test-section exemplars + TABLE F exemplar | C-09 + C-10 + C-16 | ~100/100 |
| V-05 | Maximum density: V-04 + stage gating (STAGE 1 catalog gates STAGE 2) | C-09 + C-10 + C-16 | ~100/100 |

---

## V-01 — Single Axis: C-09 Structured Mitigation Registry

**Axis:** C-09 mitigation prescriptions — a dedicated TABLE F (MITIGATION REGISTRY) follows the
RETRY-AFTER GAP ASSESSMENT section. TABLE F has five named columns: Source (Tier-ID or Path-ID),
Gap type, Component, Setting-or-API-parameter, Change, and Expected outcome. The
Setting-or-API-parameter column makes "add retry logic" fail structurally — a column requiring a
specific parameter name (e.g., `connector.retryPolicy.maxAttempts`) cannot be satisfied by a
generic phrase.

**Hypothesis:** C-09 passes when gap remediations name the component, the specific change, and
the expected outcome — not when they give generic advice. TABLE F enforces this through column
structure: the Setting-or-API-parameter column is the enforcement surface. A generic "add retry
logic" entry stands out against a column header that demands a specific key name, in the same
way that "integration tests don't cover throttle" stands out against TABLE E's Structural-reason
column header. R3 variations identified gaps but did not include a structured remediation section;
V-01 adds this single element to the R3 V-04 baseline. Primary risk: the model fills
Setting-or-API-parameter with a plausible-sounding but invented parameter name that doesn't
correspond to a real connector setting.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent for this analysis. Every downstream section that
  references a throttle tier uses these identifiers verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries such as "limited" or "throttled" invalidate
  the row.
- `STATUS Nx` — OK (limit not reached), HIT (throttling begins), SAT (fully saturated,
  requests failing). The binding constraint must shift between at least two bands, or a new
  tier must become primary as volume increases.
- `Binding at band` — the lowest band at which this tier is the primary bottleneck. N/A if
  never the binding constraint.
- `Failure visibility window` — how quickly saturation becomes observable after the limit is
  exceeded (time + observable signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`From` must use a Tier-ID from TABLE A. `Mechanism` must be specific: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with rationale.
For the top-ranked tier, reference the `Failure visibility window` and `Recovery time` values
from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from TABLE A
throughout. State each causal link. Minimum three tiers. Generic cascade claims do not satisfy
this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If absent,
name the failure mode precisely (retry storm, missing exponential backoff, silent quota
exhaustion). If present, state whether callers respect it correctly.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after RETRY-AFTER GAP ASSESSMENT. One row per identified gap from TABLE D, the
CASCADE SCENARIO, or the RETRY-AFTER GAP ASSESSMENT. Minimum two rows.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — the Tier-ID from TABLE A or Path-ID from TABLE D where this gap was identified.
- `Gap type` — one of: unprotected-burst-path, missing-retry-after, cascade-risk,
  quota-exhaustion.
- `Component` — the specific named component where the configuration or code change is applied
  (e.g., "SharePoint connector action in flow designer", "API Management throttle policy",
  "Power Automate concurrency control").
- `Setting or API parameter` — the exact configuration key, connector property, or API
  attribute name that addresses this gap. This column requires a specific named parameter.
  Generic entries such as "add retry logic", "improve error handling", or "configure
  throttling" do not satisfy this column — a cell without a specific parameter name is
  incomplete.
- `Change` — the specific value to set or pattern to apply (e.g., "set to 3 with base delay
  2 seconds exponential", "reduce to 10 concurrent runs", "add Retry-After header parsing
  before each retry attempt").
- `Expected outcome` — the concrete behavioral change at the Source tier: what stops
  happening or starts happening (e.g., "retry amplification capped at 3 attempts per flow
  run; tenant quota exhaustion within 10-minute throttle window eliminated").

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite.

**TEST INFRASTRUCTURE CATALOG**

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified above. Each entry names the artifact — the specific
test suite, fixture, harness, or mock configuration — and states the architectural property
that prevents it from reaching the behavior. Do not name a test category.

Required format:
1. **Artifact:** [specific artifact name, not a category] | **Structural property:** [architectural reason]
2. **Artifact:** [specific artifact name, not a category] | **Structural property:** [architectural reason]

A category label without artifact identification ("integration tests don't cover throttle
behavior") does not satisfy a catalog slot.

---

After the catalog, produce TABLE E. Do not substitute prose for this table. Every cell must
be filled. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

*(Complete after the catalog above. Reference catalog artifacts in `Structural reason`.)*

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type that misses it | Structural reason (artifact name + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |                          |                                                           |                                                           |
| GAP-02 |                                           |                          |                                                           |                                                           |

Column definitions:
- `Throttle behavior` — specific throttle behavior from this analysis, referenced by Tier-ID
  and failure mode.
- `Test type that misses it` — one type: unit, integration, load, or chaos.
- `Structural reason` — name a specific artifact from the catalog above and the architectural
  property. A category label without artifact identification does not satisfy this column.
- `Test approach` — component under test + volume or concurrency level + specific assertion.
  "Add load testing" does not satisfy this column.

---

## V-02 — Single Axis: C-10 Arrival Shape Comparison

**Axis:** C-10 load shape sensitivity — a standalone LOAD SHAPE COMPARISON section is added
after RETRY-AFTER GAP ASSESSMENT. The section requires a side-by-side comparison of the 1x
nominal volume at two arrival patterns: UNIFORM (requests distributed evenly) and BURST
(same total requests concentrated in a fraction of the measurement window). The comparison
must state a numeric arrival rate for each pattern and identify whether the outcome at each
TABLE A tier differs — demonstrating that arrival shape, not volume magnitude, is the
variable that changes throttle behavior.

**Hypothesis:** C-10's pass condition requires that "the same total request count produces
different throttle outcomes depending on arrival shape." A dedicated comparison section forces
this by framing the task as a fixed-volume contrast. Without the section, the model interprets
volume analysis as the 1x/2x/5x sweep in TABLE A (which changes the total) and never produces
the within-volume shape comparison C-10 requires. V-02 tests whether a prose section with
explicit numeric-comparison requirements produces a reliable C-10 pass using TABLE A's rate
limit values as the comparison denominator. Primary risk: the model states the numeric arrival
rates but does not derive different per-tier status values, producing a comparison that is
formally present but not analytically grounded.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent. Every downstream section uses these identifiers
  verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with rationale.
For the top-ranked tier, reference the `Failure visibility window` and `Recovery time` values
from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from TABLE A
throughout. State each causal link. Minimum three tiers. Generic cascade claims do not satisfy
this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If absent,
name the failure mode precisely. If present, state whether callers respect it correctly.

---

**LOAD SHAPE COMPARISON**

Using the TABLE A rate limit values, compare the 1x nominal volume under two arrival patterns.
The total request count is the same in both patterns — only the arrival distribution differs.

State:
- **UNIFORM arrival** — requests distributed evenly across the measurement window. Express as:
  total volume (from signal) distributed over [window], yielding [N] req/sec or req/min average.
  State which TABLE A tiers are HIT or SAT at this arrival rate and why.
- **BURST arrival** — same total requests concentrated in a fraction of the window (state the
  fraction). Express as: total volume arriving in first [fraction] of window, yielding [N]
  req/sec peak. State which TABLE A tiers are HIT or SAT at this arrival rate and why.

Required: at least one numeric comparison showing a TABLE A tier that is OK under UNIFORM
arrival but HIT or SAT under BURST arrival at the identical total request count. If no tier
changes status between the two patterns, state why — citing the specific rate limit type
(per-minute vs. per-second, token bucket vs. sliding window) as the reason the shape
distinction does not affect this system's behavior.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite.

**TEST INFRASTRUCTURE CATALOG**

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified above. Each entry names the artifact and states the
architectural property that prevents it from reaching the behavior. Do not name a test category.

Required format:
1. **Artifact:** [specific artifact name, not a category] | **Structural property:** [architectural reason]
2. **Artifact:** [specific artifact name, not a category] | **Structural property:** [architectural reason]

A category label without artifact identification does not satisfy a catalog slot.

---

After the catalog, produce TABLE E.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type that misses it | Structural reason (artifact name + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |                          |                                                           |                                                           |
| GAP-02 |                                           |                          |                                                           |                                                           |

Column definitions:
- `Throttle behavior` — Tier-ID + specific failure mode. Generic entries invalidate the row.
- `Test type` — unit, integration, load, or chaos.
- `Structural reason` — catalog artifact name + architectural property. Category label fails.
- `Test approach` — component + volume/concurrency + specific assertion. "Add load testing"
  does not satisfy this column.

---

## V-03 — Single Axis: C-16 Negative Exemplar Injection in Test Section

**Axis:** C-16 negative exemplar contrast — the R3 V-05 WRONG/PASS exemplar injection pattern
is applied to the R3 V-04 base (which lacks exemplars). Two contrast pairs are added: one
adjacent to the Stage 1 catalog instruction (making category labels recognizable as WRONG by
sight), one adjacent to TABLE E's column definitions (making "add load testing" in the Test
approach column recognizable as WRONG before the model writes it). The baseline structure is
R3 V-04 (catalog + TABLE E without stage gating, without exemplars).

**Hypothesis:** R3 V-04 passes C-14 and C-15 via structural constraints (catalog section
before TABLE E, TABLE E column definitions). R3 V-05 adds WRONG/PASS contrasts and scores
higher on C-14 and C-15 consistency. C-16 requires "at least one section includes a paired
contrast adjacent to the instruction it enforces." V-03 tests whether adding these contrasts
to an otherwise-identical R3 V-04 base produces reliable C-16 passage in isolation — and
whether the adjacency of the contrast to the catalog instruction improves C-14 artifact
specificity. Primary risk: contrast verbosity increases test-coverage-section token cost,
compressing TABLE A or TABLE D under total token pressure.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent. Every downstream section uses these identifiers
  verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Binding constraint must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with rationale.
For the top-ranked tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from TABLE A
throughout. State each causal link. Minimum three tiers. Generic cascade claims do not satisfy
this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If absent,
name the failure mode precisely. If present, state whether callers respect it correctly.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite.

**TEST INFRASTRUCTURE CATALOG**

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified above. Each entry names the artifact and states the
architectural property that prevents it from reaching the behavior.

Calibration contrast — use this to judge your own catalog entries:

> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> *(This names a test category and a generic reason — no artifact is identified, no
> architectural property is stated. This does not satisfy a catalog slot.)*
>
> PASS: "The integration test suite that exercises connector calls via an HttpMessageHandler
> stub registered in the DI container at test startup. Structural property: the stub injects
> preconfigured 429 responses; the real connector rate gate at the API Management layer is
> never invoked, so Retry-After header timing is never produced and concurrent retry
> amplification is never exercised under real throttle conditions."

Required format:
1. **Artifact:** [specific artifact name] | **Structural property:** [architectural reason]
2. **Artifact:** [specific artifact name] | **Structural property:** [architectural reason]

---

After the catalog, produce TABLE E. Do not substitute prose for this table. Every cell must
be filled. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

*(Complete after the catalog above. Reference catalog artifacts in `Structural reason`.)*

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type that misses it | Structural reason (artifact name + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |                          |                                                           |                                                           |
| GAP-02 |                                           |                          |                                                           |                                                           |

Column pass condition contrasts — use these to calibrate each cell:

`Throttle behavior`:
> WRONG: "Rate limiting can cause failures at high volume."
> PASS: "Retry storm on T-02 connector limit when Retry-After header is absent from 429
> response; caller retries at full concurrency, exhausting tenant quota within 10 minutes."

`Structural reason`:
> WRONG: "Integration tests don't exercise high-volume scenarios."
> PASS: "The integration test suite from the catalog above — the HttpMessageHandler stub
> injects 429 responses without real rate gate timing, so Retry-After header values are
> never produced at real concurrency and retry amplification is never observed."

`Test approach`:
> WRONG: "Add load testing to cover this scenario."
> PASS: "Load test: 800 concurrent flow runs against a live connector in a staging
> environment with tenant-level throttling enabled at production policy settings; assert
> that 429 error rate decrements to below 1% within 90 seconds after the burst subsides."

Every cell must satisfy the PASS form. An entry that contains the WRONG pattern does not
satisfy that column.

---

## V-04 — Combined: TABLE F + LOAD SHAPE + Test-Section Exemplars + TABLE F Exemplar

**Axis:** Combined maximum-coverage for all three open criteria — TABLE F (C-09 mitigation
registry) + LOAD SHAPE COMPARISON section (C-10 arrival shape) + WRONG/PASS exemplars in
the test section (C-16 adjacent to catalog instruction) + WRONG/PASS exemplar adjacent to
TABLE F's Setting-or-API-parameter column instruction (C-16 in mitigation section). All of
R3 V-04's structural elements carry forward: TABLE A through TABLE E, artifact catalog preamble,
TABLE E column definitions.

**Hypothesis:** The three open criteria are orthogonal: TABLE F addresses C-09 without affecting
the TABLE A–TABLE E chain; LOAD SHAPE COMPARISON is a standalone section that uses TABLE A's
already-stated rate limit values without requiring additional data collection; test-section
exemplars carry forward from R3 V-05 without structural change. The fourth element — TABLE F's
adjacent exemplar — extends C-16 to a second section, making the negative exemplar contrast
present in two sections simultaneously (test coverage + mitigation). C-16's pass condition
requires "at least one section," so the mitigation exemplar creates redundancy: if the test
section exemplar is compressed, the mitigation exemplar independently satisfies C-16. Combined
predicted composite: 100/100 under v4 (all 8 aspirational criteria pass simultaneously without
mutual crowding).

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent for this analysis. Every downstream section that
  references a throttle tier uses these identifiers verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries such as "limited" or "throttled" invalidate
  the row.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint must shift between at least two bands,
  or a new tier must become primary as volume increases.
- `Binding at band` — the lowest band at which this tier is the primary bottleneck. N/A if
  never the binding constraint.
- `Failure visibility window` — how quickly saturation becomes observable after the limit is
  exceeded (time + observable signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`From` must use a Tier-ID from TABLE A. `Mechanism` must be specific: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with rationale.
For the top-ranked tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from TABLE A
throughout. State each causal link. Minimum three tiers. Generic cascade claims do not satisfy
this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If absent,
name the failure mode precisely. If present, state whether callers respect it correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values, compare the 1x nominal volume at two arrival patterns.
The total request count is identical in both; only the arrival distribution differs.

- **UNIFORM arrival** — same total requests distributed evenly. State the per-second or
  per-minute arrival rate and which TABLE A tiers are HIT or SAT at that rate.
- **BURST arrival** — same total requests concentrated in a fraction of the window. State the
  peak arrival rate during the burst window and which TABLE A tiers are HIT or SAT at that rate.

Required: at least one numeric comparison showing a tier whose status differs between UNIFORM
and BURST at identical total request count. Ground the comparison in a specific TABLE A rate
limit value (e.g., "T-02's per-second limit of 20 req/sec is not exceeded at 10 req/sec
uniform but is exceeded at 60 req/sec burst, even though both deliver 600 req/min total").

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after LOAD SHAPE COMPARISON. One row per gap identified in TABLE D, CASCADE
SCENARIO, RETRY-AFTER GAP ASSESSMENT, or LOAD SHAPE COMPARISON. Minimum two rows.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — Tier-ID (from TABLE A) or Path-ID (from TABLE D) where the gap was identified.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — the specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key, connector property, or API
  attribute name.

  Calibration contrast:
  > WRONG: "Add retry logic for the throttled connector."
  > *(No component named. No parameter named. Does not satisfy this column.)*
  >
  > PASS: "`connector.retryPolicy` on the SharePoint connector action — set
  > `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
  > `retryPolicy.maximumAttempts = 3`."
  > *(Names the connector, names the policy key and sub-keys, names the values.)*

  An entry in this column that does not name a specific parameter fails this column by the
  same structural inspection that makes "add load testing" fail TABLE E's Test-approach column.

- `Change` — the specific value to set or pattern to apply.
- `Expected outcome` — the concrete behavioral change at the Source tier: what stops
  happening or starts happening after the change.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite.

**TEST INFRASTRUCTURE CATALOG**

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified above. Each entry names the artifact and states the
architectural property that prevents it from reaching the behavior.

Calibration contrast:

> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> *(Category label. No artifact identified. No architectural property stated. Does not
> satisfy a catalog slot.)*
>
> PASS: "The integration test suite that exercises connector calls via an HttpMessageHandler
> stub registered in the DI container at test startup. Structural property: the stub injects
> preconfigured 429 responses; the real connector rate gate at the API Management layer is
> never invoked, so Retry-After header timing is never produced and concurrent retry
> amplification under real throttle conditions is never exercised."

Required format:
1. **Artifact:** [specific artifact name] | **Structural property:** [architectural reason]
2. **Artifact:** [specific artifact name] | **Structural property:** [architectural reason]

---

After the catalog, produce TABLE E.

**TABLE E — TEST COVERAGE GAP REGISTRY**

*(Complete after the catalog above. Reference catalog artifacts in `Structural reason`.)*

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type that misses it | Structural reason (artifact name + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|--------------------------|-----------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |                          |                                                           |                                                           |
| GAP-02 |                                           |                          |                                                           |                                                           |

Column pass condition contrasts:

`Structural reason`:
> WRONG: "Integration tests don't exercise high-volume scenarios."
> PASS: "The integration test suite from the catalog — the HttpMessageHandler stub injects
> 429 responses without real rate gate timing; Retry-After header values are simulated and
> concurrent retry amplification at the connector layer is never observed."

`Test approach`:
> WRONG: "Add a load test for this scenario."
> PASS: "Load test: 800 concurrent flow runs against a live connector in a staging
> environment with tenant-level throttling enabled; assert that 429 error rate decrements
> to below 1% within 90 seconds after the burst window closes."

Every cell must satisfy the PASS form. An entry that contains the WRONG pattern does not
satisfy that column.

---

## V-05 — Maximum Density: V-04 + Stage Gating

**Axis:** Maximum-density variant — all V-04 elements (TABLE F + LOAD SHAPE COMPARISON +
exemplars in both test and mitigation sections) plus R3 V-03's sequential stage gating applied
to the test coverage section. STAGE 1 (artifact catalog) must be declared complete before
STAGE 2 (TABLE E) opens. The stage gate prevents the most common C-14 failure mode: the model
writing TABLE E entries before it has named the artifacts, removing the catalog's structural
pre-loading function.

**Hypothesis:** V-04 achieves 100/100 under v4. V-05 tests whether the stage gate — which adds
no new criteria coverage — improves C-14 and C-15 structural reliability under token pressure.
The gate was proven in R3 V-03 to prevent gap entries before catalog completion; when combined
with V-04's exemplar adjacency, it creates a double enforcement: the gate condition prevents
premature entry generation, and the exemplar makes incomplete entries recognizable when the
model finally produces them. V-05 is not predicted to score higher than V-04 under v4 (both
should achieve 100/100) but it tests whether V-04's score stability holds under higher token
budget consumption from stage-gate overhead plus exemplar verbosity.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute retry
  storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on day
  one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and never
  touches a real rate gate; the load test that runs at 10% of production concurrency and never
  exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x nominal;
also analyze at 2x and 5x. Produce the tables and sections below in order. Do not substitute
prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Permanent for this analysis. Every downstream section that
  references a throttle tier uses these identifiers verbatim, no synonyms.
- `Limit` — a number with a unit. Vague entries such as "limited" or "throttled" invalidate
  the row.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint must shift between at least two bands,
  or a new tier must become primary as volume increases.
- `Binding at band` — the lowest band at which this tier is the primary bottleneck. N/A if
  never the binding constraint.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source. Minimum two hops.)*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`From` must use a Tier-ID from TABLE A where the source is a named throttle tier.
`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence in `Gap reason`.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with rationale.
For the top-ranked tier, reference `Failure visibility window` and `Recovery time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from TABLE A
throughout. State each causal link. Minimum three tiers. Generic cascade claims do not satisfy
this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If absent,
name the failure mode precisely. If present, state whether callers respect it correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values, compare the 1x nominal volume at two arrival patterns.
Total request count is identical in both; only the arrival distribution differs.

- **UNIFORM arrival** — distribute total volume evenly across the measurement window. State
  the resulting per-second arrival rate. State which TABLE A tiers are HIT or SAT and why.
- **BURST arrival** — same total volume concentrated in a fraction of the window (state the
  fraction). State the peak per-second arrival rate. State which TABLE A tiers are HIT or SAT
  and why.

Required: at least one numeric comparison where a tier's status differs between UNIFORM and
BURST at identical total count. Ground in a specific TABLE A rate limit value. If no tier
changes status between patterns, explain why by citing the rate limit type (per-minute bucket
vs. per-second window) — the absence of a shape-sensitive tier is itself a finding.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after LOAD SHAPE COMPARISON. Minimum two rows. Reference the Source gap from
TABLE D, CASCADE SCENARIO, RETRY-AFTER GAP ASSESSMENT, or LOAD SHAPE COMPARISON.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — Tier-ID or Path-ID identifying the gap.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key or API attribute.

  Calibration contrast for this column:
  > WRONG: "Add retry logic for throttle handling."
  > *(No component named. No parameter named. This does not satisfy this column.)*
  >
  > PASS: "`connector.retryPolicy` on the SharePoint connector action — set
  > `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
  > `retryPolicy.maximumAttempts = 3`."

  A cell that cannot be matched to a specific named parameter in the system's configuration
  interface does not satisfy this column.

- `Change` — the specific value or pattern to apply.
- `Expected outcome` — the concrete behavioral change at the Source tier.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order. Do
not open Stage 2 until Stage 1 is declared complete.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: at least two artifacts named with structural properties before Stage 2 opens.
A category label without artifact identification fails this gate.*

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified in this analysis.

Calibration contrast — use this to judge your own entries:

> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> *(This is a category label with a generic reason. No artifact is identified. No
> architectural property is stated. This does not satisfy a catalog slot.)*
>
> PASS: "The integration test suite that exercises connector calls via an HttpMessageHandler
> stub registered in the DI container at test startup. Structural property: the stub injects
> preconfigured 429 responses; the real connector rate gate at the API Management layer is
> never invoked, so Retry-After header timing is never produced and concurrent retry
> amplification under real throttle conditions is never exercised."

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before opening Stage 2.

---

**STAGE 2 — GAP ENTRIES**

*Opens after Stage 1 is declared complete.*

Produce TABLE E. Do not substitute prose for this table. Every cell must be filled. Minimum
two rows. Reference Stage 1 artifacts in the `Structural reason` column.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column pass condition contrasts:

`Throttle behavior`:
> WRONG: "Rate limiting can cause failures at high volume."
> PASS: "Retry storm on T-02 connector limit when Retry-After header is absent from 429
> response; caller retries at full concurrency, exhausting tenant quota within 10 minutes."

`Structural reason`:
> WRONG: "Integration tests don't exercise high-volume scenarios."
> PASS: "The integration test suite from Stage 1 — the HttpMessageHandler stub injects 429
> responses without real rate gate timing; concurrent retry amplification at the connector
> layer is never observed under real throttle conditions."

`Test approach`:
> WRONG: "Add a load test for this scenario."
> PASS: "Load test: 800 concurrent flow runs against a live connector in a staging
> environment with tenant-level throttling enabled at production policy settings; assert that
> 429 error rate decrements to below 1% within 90 seconds after the burst window closes."

Every cell must satisfy the PASS form. An entry that contains the WRONG pattern in any cell
does not satisfy that column.
