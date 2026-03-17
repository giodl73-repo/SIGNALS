# flow-throttle Variate — Round 6
**Date:** 2026-03-15
**Rubric:** v5 (C-01 through C-19, essential/recommended/aspirational, denominator /11 aspirational)
**Baseline ceiling:** R5 V-05 (100/100 under v5)

---

## Round 6 Purpose

R5 confirmed that R4 V-05 achieves 100/100 under v5 with no modification required. All 11
aspirational criteria pass. The structural machinery — TABLE A through TABLE F, STAGE 1/2
with stage gate (C-17), LOAD SHAPE with null-case grounding (C-18), two-section exemplars
(C-19) — is proven stable.

R6 explores **presentation axes** for the first time. The previous rounds explored content
criteria (add TABLE F, add LOAD SHAPE, add stage gate). R6 tests whether alternative
ways of presenting the same structural content maintain 100/100 under v5.

**Presentation axes:**
1. **Phrasing register** — explanatory/WHY-first vs. imperative/prohibition-first
2. **Inertia framing** — distributed section-level callouts vs. front-loaded preamble block
3. **Role sequence** — dual-role (flow author UX pre-analysis → domain expert) vs. single role

**Predicted v5 scores — all variations target 100:**

| Variation | Axes | Aspirational pass | Composite | Score |
|-----------|------|-------------------|-----------|-------|
| V-01 | Phrasing register: explanatory | all 11 | 100 | **100** |
| V-02 | Inertia framing: distributed | all 11 | 100 | **100** |
| V-03 | Role sequence: dual-role | all 11 | 100 | **100** |
| V-04 | Register + distributed inertia | all 11 | 100 | **100** |
| V-05 | All three axes | all 11 | 100 | **100** |

**Risk profiles:**
- V-01: Explanatory text adds token cost; TABLE A/TABLE D may be compressed under pressure
- V-02: Removing opening block reduces early priming for cascade/burst sections
- V-03: Pre-analysis prose (~150 tokens before TABLE A) may compress downstream tables
- V-04: Cumulative token cost of V-01 register + V-02 callouts
- V-05: Maximum token cost; most vulnerable to output compression; also highest context richness

**Round 6 questions:**

Q1: Does the explanatory register produce more reliable WRONG/PASS contrast adherence than
the imperative register under token pressure? (C-16/C-19 sensitivity)

Q2: Does distributed inertia framing produce equivalent or better C-13/C-14 passage than
the front-loaded block? (Hypothesis: section-adjacent priming is more effective than
preamble-level priming that decays over token distance.)

Q3: Does the dual-role sequence improve C-03 UX catalog depth (TABLE C specificity) without
degrading TABLE A completeness?

---

## V-01 — Single Axis: Phrasing Register (Explanatory/WHY-First)

**Axis:** Replace the imperative/prohibition-first register of R5 V-05 with an explanatory
register. Instructions state the purpose before the requirement. Column definitions explain
why the format constraint exists. "Do not X" becomes "X ensures Y — without X, Z." All
structural elements from R5 V-05 are preserved: TABLE A through TABLE F, LOAD SHAPE with
null-case grounding (C-18), TABLE F exemplar (C-19), STAGE 1 with gate + catalog exemplar
(C-16, C-17), STAGE 2 with TABLE E column contrasts (C-19 second section).

**Hypothesis:** The imperative register works by prohibition. The explanatory register
works by purpose — making the structural reason visible at the point of use. If model
compliance is driven by understanding WHY a constraint exists rather than following a rule,
the explanatory register may be more robust under token pressure because the model can
reconstruct the required behavior from first principles. Primary risk: explanatory text
adds token cost and may compress TABLE A or TABLE D rows under pressure.

**v5 predicted scoring:** passes all 11 aspirational criteria = 11/11.
`composite = 60 + 30 + (11/11 × 10) = 100`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it
  fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint
- The integration test suite that reports green because it mocks the connector layer and
  never touches a real rate gate; the load test that runs at 10% of production concurrency
  and never exceeds a single throttle tier

The analysis below finds these before production does. Three volume bands are required —
1x nominal, 2x, 5x — because inertia lives at the volume nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that
prose cannot represent with the same auditability. Fill every cell: an empty cell and a
cell where no throttle behavior applies look identical in a scan, and the distinction
matters. Produce sections in the order shown.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section. TABLE A supplies the Tier-IDs that every
downstream section references — completing it first means no downstream section can invent
a tier name that was never established.)*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column notes:
- `Tier-ID` — Assign T-01, T-02, ... and use these identifiers verbatim in every downstream
  section. The reason: synonyms (e.g., "the connector limit" in TABLE B for what TABLE A
  called T-02) make cross-section tracing unreliable — an auditor cannot verify a finding
  without resolving name equivalences.
- `Limit` — a number with a unit (e.g., "600 req/min"). The reason: a vague entry such as
  "throttled" cannot anchor the numeric comparisons in LOAD SHAPE COMPARISON or determine
  whether a tier's STATUS changes across volume bands.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint should shift between bands — if all
  STATUS columns are identical across all bands, the multi-volume purpose of this table is
  not achieved.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use the 1x binding constraint as the source for Hop 1.)*

A two-hop minimum is required because a single-hop trace names an affected component but
does not show how the effect continues — downstream amplification remains invisible without
the causal chain.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` should be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade. A specific mechanism explains how pressure propagates;
a generic term such as "impact" does not.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. Every tier must appear — an omitted tier's user impact
is unknown, not absent.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

The `Failure if Retry-After ignored` column captures the escalation path — what happens
when a caller does not honor the backoff signal. This is where retry storms and quota
exhaustion originate.

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the absence conclusion and names at
least two specific controls as evidence. A bare conclusion cannot be verified; named
controls can be audited.)*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference `Failure visibility window` and `Recovery
time` from TABLE A — these determine the exposure window and recovery cost.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link: what happens at Tier N that triggers the
behavior at Tier N+1. A cascade requires at least three tiers where each step is caused
by the previous — two independent limits on the same request are not a cascade because
the second is not triggered by the first.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely — the precision matters because the remediation
for a retry storm (exponential backoff policy) differs from the remediation for quota
exhaustion (circuit breaker). If present, state whether callers respect it correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values, compare the 1x nominal volume at two arrival patterns.
The total request count is identical in both; only the arrival distribution differs. The
reason for this comparison: per-minute limits and per-second limits respond differently
to burst arrivals — a system that appears safe at uniform arrival may saturate under burst
at the same total volume.

- **UNIFORM arrival** — distribute total volume evenly across the measurement window.
  State the per-second arrival rate. State which TABLE A tiers are HIT or SAT and why.
- **BURST arrival** — same total volume concentrated in a fraction of the window (state
  the fraction). State the peak per-second arrival rate. State which TABLE A tiers are
  HIT or SAT and why.

Required: at least one numeric comparison where a tier's status differs between UNIFORM
and BURST at identical total request count. Ground in a specific TABLE A rate limit value
(e.g., "T-02's per-second limit of 20 req/sec is not exceeded at 10 req/sec uniform but
is exceeded at 60 req/sec burst, even though both deliver 600 req/min total").

If no tier changes status between the two patterns, name the specific rate limit mechanism
— per-minute bucket, per-second window, sliding window, token bucket — as the structural
reason arrival shape does not affect behavior at this volume. A null finding stated without
the cited mechanism is indistinguishable from an incomplete analysis.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after LOAD SHAPE COMPARISON. One row per gap from TABLE D, CASCADE SCENARIO,
RETRY-AFTER GAP ASSESSMENT, or LOAD SHAPE COMPARISON. Minimum two rows.)*

The purpose of TABLE F is to make remediations immediately actionable — specific parameter
names and values a team can apply without additional research. An entry that names a
category of action rather than the action itself has not achieved this purpose.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column notes:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — Tier-ID or Path-ID where the gap was identified.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key, connector property, or API
  attribute name. The reason this column requires a specific parameter: without it, the
  row names a category of action rather than the action itself and cannot be applied
  without further research.

  Calibration contrast — use this to judge your own entries:
  > WRONG: "Add retry logic for throttle handling."
  > *(No component named. No parameter named. This names a category, not the action.
  > Does not satisfy this column.)*
  >
  > PASS: "`connector.retryPolicy` on the SharePoint connector action — set
  > `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
  > `retryPolicy.maximumAttempts = 3`."
  > *(Names the connector property, sub-keys, values. Can be applied without additional
  > research.)*

- `Change` — specific value or pattern to apply.
- `Expected outcome` — concrete behavioral change at the Source tier.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order.
The reason for the two-stage structure: Stage 1 pre-loads the artifact names and structural
properties that Stage 2's `Structural reason` column requires — without Stage 1 complete
before Stage 2 opens, TABLE E entries default to category labels rather than
artifact-grounded explanations.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: at least two artifacts named with structural properties before Stage 2
opens. The gate ensures the catalog is complete before gap entries reference it.*

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified in this analysis. Each entry names the artifact —
the specific test suite, fixture, harness, or mock configuration — and states the
architectural property that prevents it from reaching the behavior. The artifact name
supplies the traceability anchor for TABLE E's `Structural reason` column.

Calibration contrast — use this to judge your own entries:
> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> *(This names a test category — not an artifact. The reason "low volume" does not name
> an architectural property. This cannot supply the structural reason for a TABLE E entry
> — that column must trace back to a named artifact.)*
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

*Opens after Stage 1 is declared complete. Reference Stage 1 artifacts in `Structural
reason` — each gap entry should trace its structural reason back to a named Stage 1
artifact and the architectural property that produces the gap.*

Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column calibration contrasts — use these to judge your own entries:

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
> environment with tenant-level throttling enabled at production policy settings; assert
> that 429 error rate decrements to below 1% within 90 seconds after the burst window
> closes."

Every cell must satisfy the PASS form. An entry that matches the WRONG pattern does not
satisfy that column.

---

## V-02 — Single Axis: Distributed Inertia Framing

**Axis:** Remove the front-loaded INERTIA PROBLEM preamble block. Place targeted inertia
callouts immediately before the three sections where inertia concealment is most acute:
TABLE A (volume-band blindness), TABLE D (burst path blindness), and STAGE 1 (test
infrastructure blindness). Each callout is 2-3 sentences naming the specific inertia
concealment pattern that section is designed to surface. All other structural elements
from R5 V-05 are preserved unchanged; only the location of inertia framing changes.

**Hypothesis:** The opening inertia block provides general priming but is separated from
the sections it motivates by the full TABLE A through TABLE C chain. By the time the model
reaches TABLE D or STAGE 1, the opening block may have decayed in salience. Distributed
callouts place the inertia concept immediately before the section where it governs output
quality. Primary risk: removing the opening block reduces early priming for cascade and
burst-path sections that appear before the first distributed callout reaches them.

**v5 predicted scoring:** passes all 11 aspirational criteria = 11/11.
`composite = 60 + 30 + (11/11 × 10) = 100`

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Produce the tables and sections below in order. Do not
substitute prose for any table. Every cell must be filled.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section.)*

*What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal — the volume where the production incident happened. The multi-volume STATUS
columns exist because inertia lives at the volume nobody tested, not the volume in the
design document.*

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

*What inertia conceals here: the burst path that bypasses rate limiting because it was
never tested at the volume where it fires. It passed every test run because every test
run used 10% of production concurrency. "We've never seen it fail" describes the test
environment's volume ceiling, not the production system's protection.*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference `Failure visibility window` and `Recovery
time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link. Minimum three tiers. Generic cascade claims
do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely. If present, state whether callers respect it
correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values, compare the 1x nominal volume at two arrival patterns.
Total request count is identical in both; only the arrival distribution differs.

- **UNIFORM arrival** — distribute total volume evenly. State per-second arrival rate.
  State which TABLE A tiers are HIT or SAT and why.
- **BURST arrival** — same total volume concentrated in a fraction of the window (state
  the fraction). State peak per-second arrival rate. State which TABLE A tiers are HIT
  or SAT and why.

Required: at least one numeric comparison where a tier's status differs between UNIFORM
and BURST at identical total count. Ground in a specific TABLE A rate limit value.

If no tier changes status between the two patterns, state why — citing the specific rate
limit mechanism (per-minute bucket, per-second window, sliding window, token bucket) as
the structural reason. The absence of a shape-sensitive tier is itself a finding.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after LOAD SHAPE COMPARISON. One row per gap from TABLE D, CASCADE SCENARIO,
RETRY-AFTER GAP ASSESSMENT, or LOAD SHAPE COMPARISON. Minimum two rows.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — Tier-ID or Path-ID where the gap was identified.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key, connector property, or API
  attribute name.

  Calibration contrast:
  > WRONG: "Add retry logic for the throttled connector."
  > *(No component named. No parameter named. Does not satisfy this column.)*
  >
  > PASS: "`connector.retryPolicy` on the SharePoint connector action — set
  > `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
  > `retryPolicy.maximumAttempts = 3`."

  An entry that does not name a specific parameter fails this column.

- `Change` — specific value or pattern to apply.
- `Expected outcome` — concrete behavioral change at the Source tier.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order.
Do not open Stage 2 until Stage 1 is declared complete.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: at least two artifacts named with structural properties before Stage 2
opens. A category label without artifact identification fails this gate.*

*What inertia conceals here: the integration test suite that reports green because it
mocks the connector layer and never invokes a real rate gate. The load test that runs at
10% of production concurrency and never causes a throttle tier to fire. These are not
failures — their architectural properties make specific throttle behaviors permanently
unreachable regardless of how long they run.*

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified above. Each entry names the artifact and states the
architectural property that prevents it from reaching the behavior. Do not name a test
category.

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

Produce TABLE E. Do not substitute prose for this table. Every cell must be filled.
Minimum two rows. Reference Stage 1 artifacts in `Structural reason`.

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
> environment with tenant-level throttling enabled at production policy settings; assert
> that 429 error rate decrements to below 1% within 90 seconds after the burst window
> closes."

Every cell must satisfy the PASS form. An entry that contains the WRONG pattern does not
satisfy that column.

---

## V-03 — Single Axis: Role Sequence (Flow Author Pre-Analysis → Domain Expert)

**Axis:** Open with a ROLE 1 block — the flow author who received a post-incident report —
that produces a 5-7 sentence UX impact statement before the full technical analysis. The
statement covers: what error codes or signals appeared in run history, what retry behavior
was observed, how the business process was affected, and what the first observable symptom
was. Then transition explicitly to ROLE 2 (domain expert) for the full table-based
analysis. All structural elements from R5 V-05 are preserved.

**Hypothesis:** TABLE C (UX catalog) requires specific error codes, retry delay signals,
queue depth visibility, and degraded response descriptions per tier. The pre-analysis
forces the model to articulate UX impact before it encounters TABLE C — loading the UX
vocabulary into working context before the table demands it. This may produce richer TABLE
C entries and improve C-03 passage reliability. Primary risk: the pre-analysis prose adds
token cost before TABLE A; downstream tables may be truncated under compression.

**v5 predicted scoring:** passes all 11 aspirational criteria = 11/11.
`composite = 60 + 30 + (11/11 × 10) = 100`

---

**ROLE 1 — FLOW AUTHOR PRE-ANALYSIS**

You are a flow author who has just received a post-incident report showing throttle-related
failures in a production Power Automate environment. Before the technical analysis, write
a UX impact statement of 5-7 sentences covering: what error codes or signals appeared in
run history, what retry behavior was observed (immediate retries, exponential backoff, or
silent drops), how the business process was affected (partial completions, queued work,
user-facing errors), and what the first observable symptom was. Write this as plain prose
— no tables, no section headers. This statement establishes the user-visible context that
TABLE C will later quantify per tier.

---

**ROLE 2 — DOMAIN EXPERT ANALYSIS**

You are a Connectors / Power Automate throughput domain expert. Using the UX context
established in the pre-analysis above, simulate throughput across the rate-limited system
described in the signal. Treat the stated request volume as 1x nominal; also analyze at
2x and 5x. Produce the tables and sections below in order. Do not substitute prose for
any table. Every cell must be filled.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:

- The burst path that was never rate-limited because no one tested at the volume where it
  fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite that reports green because it mocks the connector layer

Three volume bands are required — 1x nominal, 2x, 5x — because inertia lives at the
volume nobody tested.

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

`Mechanism` must be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. No tier may be omitted. Cross-reference the Role 1
pre-analysis to populate error codes and retry behavior accurately per tier.)*

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

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference `Failure visibility window` and `Recovery
time` from TABLE A.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link. Minimum three tiers. Generic cascade claims
do not satisfy this section.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely. If present, state whether callers respect it
correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values, compare the 1x nominal volume at two arrival patterns.
Total request count is identical in both; only the arrival distribution differs.

- **UNIFORM arrival** — distribute total volume evenly. State per-second arrival rate.
  State which TABLE A tiers are HIT or SAT and why.
- **BURST arrival** — same total volume concentrated in a fraction of the window (state
  the fraction). State peak per-second arrival rate. State which TABLE A tiers are HIT
  or SAT and why.

Required: at least one numeric comparison where a tier's status differs between UNIFORM
and BURST at identical total count. Ground in a specific TABLE A rate limit value.

If no tier changes status between the two patterns, state why — citing the specific rate
limit mechanism (per-minute bucket, per-second window, sliding window, token bucket) as
the structural reason. The absence of a shape-sensitive tier is itself a finding.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after LOAD SHAPE COMPARISON. Minimum two rows. One row per gap from TABLE D,
CASCADE SCENARIO, RETRY-AFTER GAP ASSESSMENT, or LOAD SHAPE COMPARISON.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column definitions:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — Tier-ID or Path-ID where the gap was identified.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key, connector property, or API
  attribute name.

  Calibration contrast:
  > WRONG: "Add retry logic for the throttled connector."
  > *(No component named. No parameter named. Does not satisfy this column.)*
  >
  > PASS: "`connector.retryPolicy` on the SharePoint connector action — set
  > `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
  > `retryPolicy.maximumAttempts = 3`."

  An entry that does not name a specific parameter fails this column.

- `Change` — specific value or pattern to apply.
- `Expected outcome` — concrete behavioral change at the Source tier.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order.
Do not open Stage 2 until Stage 1 is declared complete.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: at least two artifacts named with structural properties before Stage 2
opens. A category label without artifact identification fails this gate.*

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified above. Each entry names the artifact and states the
architectural property that prevents it from reaching the behavior. Do not name a test
category.

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

Produce TABLE E. Do not substitute prose for this table. Every cell must be filled.
Minimum two rows. Reference Stage 1 artifacts in `Structural reason`.

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
> environment with tenant-level throttling enabled at production policy settings; assert
> that 429 error rate decrements to below 1% within 90 seconds after the burst window
> closes."

Every cell must satisfy the PASS form. An entry that contains the WRONG pattern does not
satisfy that column.

---

## V-04 — Combined: Explanatory Register + Distributed Inertia Framing

**Axis:** Merge V-01 (explanatory/WHY-first register) and V-02 (distributed section-level
inertia callouts, no opening preamble). Replace imperative prohibitions with explanatory
context. Add targeted inertia callouts before TABLE A, TABLE D, and STAGE 1. All
structural elements from R5 V-05 are preserved.

**Hypothesis:** The explanatory register and distributed inertia callouts are complementary
— both contextualize requirements rather than prohibiting violations. The "why this format
matters" explanations and the "what inertia hides here" callouts address different aspects
of the same constraint: structural purpose and business stakes. Combined, they may reduce
model resistance to constraint-dense instructions by making both reasons visible at the
point of use. Predicted composite: 100/100 under v5.

**v5 predicted scoring:** passes all 11 aspirational criteria = 11/11.
`composite = 60 + 30 + (11/11 × 10) = 100`

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that
prose cannot represent with the same auditability. Fill every cell: an empty cell and a
cell where no throttle behavior applies look identical in a scan, and the distinction
matters. Produce sections in the order shown.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section. TABLE A supplies the Tier-IDs all downstream
sections reference — completing it first ensures no downstream section invents a tier name
that was never established.)*

*What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal. The multi-volume STATUS columns exist because inertia lives at the volume
nobody tested — not the volume documented in the design.*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column notes:
- `Tier-ID` — Assign T-01, T-02, ... and use these identifiers verbatim in every downstream
  section. The reason: synonyms make cross-section tracing unreliable — an auditor cannot
  verify a finding without resolving name equivalences.
- `Limit` — a number with a unit. The reason: a vague entry cannot anchor the numeric
  comparisons in LOAD SHAPE COMPARISON or determine STATUS transitions across bands.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint should shift between bands — if all
  STATUS columns are identical, the multi-volume purpose of this table is not achieved.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source.)*

A two-hop minimum is required because a single-hop trace names an affected component but
does not show how the effect continues — downstream amplification remains invisible without
the causal chain.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` should be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. Every tier must appear — an omitted tier's user
impact is unknown, not absent.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence — a bare conclusion cannot be audited; named controls can.)*

*What inertia conceals here: the burst path that bypasses rate limiting because it was
never tested at the volume where it fires. "We've never seen it fail" describes the test
environment's volume ceiling, not the production system's safety margin.*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference `Failure visibility window` and `Recovery
time` from TABLE A — these determine the exposure window and recovery cost.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link: what happens at Tier N that triggers the
behavior at Tier N+1. A cascade requires at least three tiers where each step is caused
by the previous — two independent limits on the same request are not a cascade.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely — the precision matters because different failure
modes have different remediations. If present, state whether callers respect it correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values, compare the 1x nominal volume at two arrival patterns.
Total request count is identical in both; only the arrival distribution differs. The reason
for this comparison: per-minute limits and per-second limits respond differently to burst
arrivals — a system that appears safe at uniform arrival may saturate under burst at the
same total volume.

- **UNIFORM arrival** — distribute total volume evenly. State per-second arrival rate.
  State which TABLE A tiers are HIT or SAT and why.
- **BURST arrival** — same total volume concentrated in a fraction of the window (state
  the fraction). State peak per-second arrival rate. State which TABLE A tiers are HIT
  or SAT and why.

Required: at least one numeric comparison where a tier's status differs between UNIFORM
and BURST at identical total count. Ground in a specific TABLE A rate limit value.

If no tier changes status between the two patterns, name the specific rate limit mechanism
— per-minute bucket, per-second window, sliding window, token bucket — as the structural
reason. A null finding without the cited mechanism is indistinguishable from an incomplete
analysis.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after LOAD SHAPE COMPARISON. Minimum two rows. One row per gap from TABLE D,
CASCADE SCENARIO, RETRY-AFTER GAP ASSESSMENT, or LOAD SHAPE COMPARISON.)*

The purpose of TABLE F is to make remediations immediately actionable — specific parameter
names and values a team can apply without additional research. An entry that names a
category of action rather than the action itself has not achieved this purpose.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column notes:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — Tier-ID or Path-ID where the gap was identified.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key or API attribute name. The reason
  this column requires a specific parameter: without it, the row names a category of action
  and cannot be applied without further research.

  Calibration contrast:
  > WRONG: "Add retry logic for throttle handling."
  > *(No component named. No parameter named. Names a category, not the action. Does not
  > satisfy this column.)*
  >
  > PASS: "`connector.retryPolicy` on the SharePoint connector action — set
  > `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
  > `retryPolicy.maximumAttempts = 3`."
  > *(Names the connector property, sub-keys, values. Can be applied without additional
  > research.)*

- `Change` — specific value or pattern to apply.
- `Expected outcome` — concrete behavioral change at the Source tier.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order.
The reason for the two-stage structure: Stage 1 pre-loads the artifact names and structural
properties that Stage 2's `Structural reason` column requires — without Stage 1 complete,
TABLE E entries default to category labels rather than artifact-grounded explanations.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: at least two artifacts named with structural properties before Stage 2
opens. The gate ensures the catalog is complete before gap entries can reference it.*

*What inertia conceals here: the integration test suite that reports green because it mocks
the connector layer. The load test that runs at 10% of production concurrency. These are
not failures — their architectural properties make specific throttle behaviors permanently
unreachable regardless of how long they run.*

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified in this analysis. Each entry names the artifact and
states the architectural property that prevents it from reaching the behavior.

Calibration contrast — use this to judge your own entries:
> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> *(Names a category — not an artifact. The reason "low volume" does not name an
> architectural property. Cannot supply the structural reason for a TABLE E entry — that
> column must trace back to a named artifact.)*
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

*Opens after Stage 1 is declared complete. Reference Stage 1 artifacts in `Structural
reason` — each entry should trace its structural reason back to a named Stage 1 artifact
and the architectural property that produces the gap.*

Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column calibration contrasts:

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
> environment with tenant-level throttling enabled at production policy settings; assert
> that 429 error rate decrements to below 1% within 90 seconds after the burst window
> closes."

Every cell must satisfy the PASS form. An entry that matches the WRONG pattern does not
satisfy that column.

---

## V-05 — Maximum Density: All Three Axes (Explanatory + Distributed Inertia + Dual-Role)

**Axis:** Combine all three R6 axes: explanatory/WHY-first register (V-01) + distributed
section-level inertia callouts with no opening preamble (V-02) + dual-role sequence with
flow author pre-analysis (V-03). All structural elements from R5 V-05 are preserved.

**Hypothesis:** The three axes are potentially synergistic. The dual-role sequence
establishes full UX context before the technical analysis. The distributed inertia callouts
reinforce that context at the sections where it governs output quality. The explanatory
register connects instructions to their structural purpose. Primary risk: cumulative token
cost of three axis additions may push the prompt to a point where TABLE A or TABLE D is
compressed. Secondary hypothesis: the combined form may be more robust than R5 V-05 under
token pressure because each structural element is motivated rather than only mandated.

**v5 predicted scoring:** passes all 11 aspirational criteria = 11/11.
`composite = 60 + 30 + (11/11 × 10) = 100`

---

**ROLE 1 — FLOW AUTHOR PRE-ANALYSIS**

You are a flow author who has just received a post-incident report showing throttle-related
failures in a production Power Automate environment. Before the technical analysis, write
a UX impact statement of 5-7 sentences covering: what error codes or signals appeared in
run history, what retry behavior was observed (immediate retries, exponential backoff, or
silent drops), how the business process was affected (partial completions, queued work,
user-facing errors), and what the first observable symptom was. Write this as plain prose
— no tables, no section headers. This statement establishes the user-visible context that
TABLE C will later quantify per tier.

---

**ROLE 2 — DOMAIN EXPERT ANALYSIS**

You are a Connectors / Power Automate throughput domain expert. Using the UX context
established above, simulate throughput across the rate-limited system described in the
signal. Treat the stated request volume as 1x nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that
prose cannot represent with the same auditability. Fill every cell: an empty cell and a
cell where no throttle behavior applies look identical in a scan, and the distinction
matters. Produce sections in the order shown.

---

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

*(Complete before any other table or section. TABLE A supplies the Tier-IDs all downstream
sections reference — completing it first ensures no downstream section invents a tier name
that was never established.)*

*What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal. The multi-volume STATUS columns exist because inertia lives at the volume
nobody tested.*

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                          |               |
| ...     |           |                      |       |           |           |           |                 |                          |               |

Column notes:
- `Tier-ID` — Assign T-01, T-02, ... and use these identifiers verbatim in every downstream
  section. The reason: synonyms make cross-section tracing unreliable.
- `Limit` — a number with a unit. The reason: a vague entry cannot anchor LOAD SHAPE
  COMPARISON comparisons or determine STATUS transitions across bands.
- `STATUS Nx` — OK / HIT / SAT. The binding constraint should shift between bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

---

**TABLE B — BACKPRESSURE PROPAGATION TRACE**

*(Complete after TABLE A. Use 1x binding constraint as source.)*

A two-hop minimum is required because a single-hop trace names an affected component but
does not show how the effect continues — downstream amplification remains invisible without
the causal chain.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

`Mechanism` should be specific: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**TABLE C — USER EXPERIENCE CATALOG**

*(One row per Tier-ID from TABLE A. Every tier must appear. Cross-reference the Role 1
pre-analysis to populate error codes and retry behavior accurately — the pre-analysis
stated what the flow author observed; this table quantifies it per tier.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                               |
| T-02    |                     |                           |                                      |                               |
| ...     |                     |                           |                                      |                               |

---

**TABLE D — UNPROTECTED BURST PATHS**

*(At least one row. If no path exists, row 1 states the conclusion with at least two named
controls as evidence — a bare conclusion cannot be audited; named controls can.)*

*What inertia conceals here: the burst path that bypasses rate limiting because no test
has ever run at the volume where it fires. "We've never seen it fail" describes the test
environment's volume ceiling, not the production system's safety margin.*

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**TIER RISK RANKING**

Rank TABLE A tiers by business risk, highest to lowest. One sentence per tier with
rationale. For the top-ranked tier, reference `Failure visibility window` and `Recovery
time` from TABLE A — these determine the exposure window and recovery cost.

---

**CASCADE SCENARIO**

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs from
TABLE A throughout. State each causal link: what happens at Tier N that triggers the
behavior at Tier N+1. A cascade requires at least three tiers where each step is caused
by the previous — two independent limits on the same request are not a cascade.

---

**RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After handling present in the caller? If
absent, name the failure mode precisely — the precision matters because different failure
modes have different remediations. If present, state whether callers respect it correctly.

---

**LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values, compare the 1x nominal volume at two arrival patterns.
Total request count is identical in both; only the arrival distribution differs. The reason
for this comparison: per-minute limits and per-second limits respond differently to burst
arrivals — a system safe at uniform arrival may saturate under burst at the same total
volume.

- **UNIFORM arrival** — distribute total volume evenly. State per-second arrival rate.
  State which TABLE A tiers are HIT or SAT and why.
- **BURST arrival** — same total volume concentrated in a fraction of the window (state
  the fraction). State peak per-second arrival rate. State which TABLE A tiers are HIT
  or SAT and why.

Required: at least one numeric comparison where a tier's status differs between UNIFORM
and BURST at identical total count. Ground in a specific TABLE A rate limit value.

If no tier changes status between the two patterns, name the specific rate limit mechanism
— per-minute bucket, per-second window, sliding window, token bucket — as the structural
reason. A null finding without the cited mechanism is indistinguishable from an incomplete
analysis.

---

**TABLE F — MITIGATION REGISTRY**

*(Complete after LOAD SHAPE COMPARISON. Minimum two rows. One row per gap from TABLE D,
CASCADE SCENARIO, RETRY-AFTER GAP ASSESSMENT, or LOAD SHAPE COMPARISON.)*

The purpose of TABLE F is to make remediations immediately actionable — specific parameter
names and values a team can apply without additional research. An entry that names a
category of action rather than the action itself has not achieved this purpose.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

Column notes:
- `MR-ID` — MR-01, MR-02, ...
- `Source` — Tier-ID or Path-ID where the gap was identified.
- `Gap type` — unprotected-burst-path, missing-retry-after, cascade-risk, quota-exhaustion.
- `Component` — specific named component where the change is applied.
- `Setting or API parameter` — the exact configuration key or API attribute name. The reason
  this column requires a specific parameter: without it, the row names a category of action
  and cannot be applied without further research.

  Calibration contrast — use this to judge your own entries:
  > WRONG: "Add retry logic for throttle handling."
  > *(No component named. No parameter named. Names a category, not the action. Does not
  > satisfy this column.)*
  >
  > PASS: "`connector.retryPolicy` on the SharePoint connector action — set
  > `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
  > `retryPolicy.maximumAttempts = 3`."
  > *(Names the connector property, sub-keys, values. Can be applied without additional
  > research.)*

- `Change` — specific value or pattern to apply.
- `Expected outcome` — concrete behavioral change at the Source tier.

---

**TEST COVERAGE GAP ANALYSIS**

This section surfaces what inertia hides in the test suite. Execute two stages in order.
The reason for the two-stage structure: Stage 1 pre-loads the artifact names and structural
properties that Stage 2's `Structural reason` column requires — without Stage 1 complete,
TABLE E entries default to category labels that cannot be traced to a named artifact.

---

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

*Gate condition: at least two artifacts named with structural properties before Stage 2
opens. The gate ensures the catalog is complete before gap entries can reference it.*

*What inertia conceals here: the integration test suite that reports green because it
mocks the connector layer. The load test that runs at 10% of production concurrency. Their
architectural properties make specific throttle behaviors permanently unreachable regardless
of how long they run.*

Name the specific test infrastructure artifacts currently in place that structurally cannot
reach the throttle behaviors identified in this analysis. Each entry names the artifact and
states the architectural property that prevents it from reaching the behavior.

Calibration contrast — use this to judge your own entries:
> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> *(Names a category — not an artifact. "Low volume" does not name an architectural
> property. Cannot supply the structural reason for a TABLE E entry — that column must
> trace back to a named artifact.)*
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

*Opens after Stage 1 is declared complete. Reference Stage 1 artifacts in `Structural
reason` — each entry should trace its structural reason back to a named Stage 1 artifact
and the architectural property that produces the gap.*

Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column calibration contrasts — use these to judge your own entries:

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
> environment with tenant-level throttling enabled at production policy settings; assert
> that 429 error rate decrements to below 1% within 90 seconds after the burst window
> closes."

Every cell must satisfy the PASS form. An entry that matches the WRONG pattern does not
satisfy that column.
