# flow-throttle Variate — Round 7 (v6 Rubric)
**Date:** 2026-03-15
**Rubric:** v6 (C-01 through C-23, 5 essential / 3 recommended / 15 aspirational, denominator 15)
**Baseline:** R6 V-05 passes C-01 through C-20 (12 pre-v6 aspirational); C-21, C-22, C-23 unachieved.

---

## Round 7 Purpose

The v6 rubric derived three new criteria from R6 V-05 excellence patterns. R6 V-05 labeled
enforcement blocks with failure-mode identifiers (C-21), used FAIL-entry itemization in audit
fields (C-22), and embedded the escape-route mechanism in the deferral prohibition (C-23).
These patterns appear in R6 V-05 output but are not required by any prior criterion.

Round 7 isolates each as a single structural axis, then combines.

**New v6 axes:**
1. **C-21 labeling axis** — enforcement blocks labeled with the failure mode they prevent
2. **C-22 itemization axis** — audit FAIL entries enumerate specific missing items
3. **C-23 escape-route axis** — deferral prohibition embeds the behavioral temptation

**Predicted v6 scores:**

| Variation | Axes | C-21 | C-22 | C-23 | Aspirational | Composite |
|-----------|------|------|------|------|--------------|-----------|
| V-01 | C-21 minimal labels only | PASS | FAIL | FAIL | 13/15 | ~107 |
| V-02 | C-22 inline bracket format only | FAIL | PASS | FAIL | 13/15 | ~107 |
| V-03 | C-23 one-sentence escape-route only | FAIL | FAIL | PASS | 13/15 | ~107 |
| V-04 | C-21 rich labels + C-22 | PASS | PASS | FAIL | 14/15 | ~109 |
| V-05 | C-21 extended + C-22 structured + C-23 extended | PASS | PASS | PASS | 15/15 | 110 |

**Composite formula:**
```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 15 * 20)
```

**Round 7 questions:**

Q1: Does C-21 minimal labeling (criterion ID + failure mode name only) satisfy C-21 passage?
Hypothesis: PASS — "Failure N prevention (C-NN)" satisfies both "by name" and "by identifier"
sub-requirements. Risk: a judge may expect the label to explain what "Failure 5" means.

Q2: Does C-22 inline bracket format `[PASS / FAIL: list T-NNs with informal references]`
produce reliable FAIL-branch enumeration, or does the model collapse it to `[PASS / FAIL]`
under output pressure?

Q3: Does a one-sentence C-23 escape-route (names the inertia frame without extended rejection
proof) satisfy C-23? Hypothesis: PASS at minimum depth — the rubric requires naming the
label/heuristic that makes deferral tempting; the one-sentence form does this without the
full mechanism explanation present in V-05.

**Risk profiles:**
- V-01: Minimal labels; primary risk is auditors expecting more than a failure-mode number.
- V-02: Clean C-22 isolation; primary risk is model collapsing inline brackets under pressure.
- V-03: One-sentence escape-route; risk is whether naming the frame is sufficient for C-23.
- V-04: Cumulative token cost of rich labels + itemization; practical ceiling for most contexts.
- V-05: Maximum density with dual-role opening; primary risk is output compression at TABLE D.

---

## V-01 — Single Axis: C-21 Failure-Mode Labels (Minimal Style)

**Axis:** Add failure-mode labels to enforcement blocks using minimal style — each label
cites the criterion ID and a failure-mode name or number (e.g., "Failure 5 prevention
(C-17)"). No extended mechanism description. C-22 (FAIL-entry itemization) and C-23
(escape-route mechanism) are not present.

**Hypothesis:** The C-21 rubric requires labels that reference "the failure mode by name
or by failure-mode identifier." Minimal labels of the form "Failure N prevention (C-NN)"
satisfy both sub-requirements: "Failure N" is the failure-mode identifier; the criterion
ID provides the traceability link. Labels that cite only a criterion ID without naming the
failure mode fail C-21. Labels that name the failure mode without a criterion ID also fail.
The minimal style satisfies both at lowest token cost. Primary risk: a judge may expect the
label to explain what "Failure 5" means, not just cite it.

**v6 predicted scoring:**
- C-21: PASS — criterion ID + failure-mode identifier on each enforcement block
- C-22: FAIL — audit fields use binary [PASS / FAIL] without FAIL-branch itemization
- C-23: FAIL — deferral prohibition names target section only; no escape-route story
- Aspirational 13/15 → composite = `60 + 30 + (13/15 x 20) = 107.3`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where
  it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite that reports green because it mocks the connector layer

Three volume bands required — 1x nominal, 2x, 5x — because inertia lives at the volume
nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Produce the tables and sections below in order. Do
not substitute prose for any table. Every cell must be filled.

---

**STEP 1 — TIER REGISTRY**

Complete Step 1 in full before opening any Step 2 section. Step 1 is the perspective-
separated enumeration phase: all tier discovery, numeric limits, and load-shape
classification happen here. Step 2 contains caller behavior and backpressure analysis
only. Any tier discovered during Step 2 that is not in TABLE A is a scope violation —
do not assign a new T-NN during Step 2; return to TABLE A, register the tier with all
required columns, then continue.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream section. No synonyms;
  synonym resolution makes cross-section tracing unreliable.
- `Limit` — A number with a unit (e.g., "600 req/min"). Vague entries cannot anchor
  LOAD SHAPE COMPARISON calculations or STATUS transition analysis.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands; identical STATUS
  across all bands means the multi-volume purpose is not achieved.
- `Binding at band` — Lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, with numeric rate differential
  and mechanism (e.g., "SHAPE-SENSITIVE — per-second window of 20 req/sec; burst peak of
  60 req/sec exceeds it; uniform 10 req/sec does not"). **Failure 6 prevention (C-20):
  do not defer load-shape classification to the LOAD SHAPE COMPARISON section. Complete
  this column now.**
- `Failure visibility window` — How quickly saturation becomes observable (time + signal).
- `Recovery time` — How long until normal operation resumes.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.
Do not introduce a tier in Step 2 that was not registered in TABLE A.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**Failure 5 prevention (C-17) — REGISTRY GAP scope violation:** Tiers appearing here
that are not in TABLE A require a return to TABLE A before this section continues. Do
not assign a new T-NN here.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Failure 5 prevention (C-17) — REGISTRY GAP scope violation:** Tiers referenced here
that are not in TABLE A require a return to TABLE A before continuing.

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence in `Gap reason`.

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every TABLE A tier must appear.
One sentence per tier with rationale. For the top-ranked tier, reference `Failure visibility
window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**Failure 5 prevention (C-17) — REGISTRY GAP scope violation:** Tiers introduced during
cascade trace that are not in TABLE A require a return to TABLE A before continuing.

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, name
the failure mode precisely. If present, state whether callers respect it correctly.

---

**Step 2G — LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at
two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — State per-second arrival rate. State which tiers are HIT or SAT
  and why, referencing the specific Limit value.
- **BURST arrival** — State the fraction and peak per-second rate. State which tiers are
  HIT or SAT and why.

At least one numeric comparison where status differs between patterns. Ground in a specific
TABLE A Limit value. If no tier changes status, name the rate limit mechanism (per-minute
bucket, per-second window, sliding window, token bucket) as the structural reason.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Minimum two rows. One per gap from TABLE D, CASCADE, RETRY-AFTER, or LOAD SHAPE.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact configuration key or API attribute. Generic labels fail.

Calibration contrast:
> WRONG: "Add retry logic for throttle handling."
> PASS: "`connector.retryPolicy` on the SharePoint connector action — set
> `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
> `retryPolicy.maximumAttempts = 3`."

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Execute Stage 1 before Stage 2. Stage 1 pre-loads artifact names that Stage 2's
`Structural reason` column requires.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2.

Calibration contrast:
> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> PASS: "The integration test suite exercising connector calls via an HttpMessageHandler
> stub. Structural property: stub injects preconfigured 429 responses; real connector
> rate gate is never invoked, so Retry-After timing is never produced."

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

---

**STAGE 2 — GAP ENTRIES**

Produce TABLE E. Fill every cell. Minimum two rows. Reference Stage 1 artifacts.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column calibration contrasts:
> `Throttle behavior` PASS: "Retry storm on T-02 connector limit when Retry-After header
> is absent; caller retries at full concurrency, exhausting tenant quota within 10 minutes."
>
> `Test approach` PASS: "Load test: 800 concurrent flow runs against a live connector in
> staging with tenant-level throttling at production settings; assert 429 rate decrements
> to below 1% within 90 seconds."

---

**STEP 4 — INTEGRITY VERIFICATION — Failure 4 prevention (C-18)**

Self-contained audit block. Complete after Stage 2. Report compliance per section.

**C-13 compliance — Tier-ID threading (individual per-section verdicts):**
- Step 2A (TABLE B): [PASS / FAIL]
- Step 2B (TABLE C): [PASS / FAIL]
- Step 2C (TABLE D): [PASS / FAIL]
- Step 2D (TIER RISK RANKING): [PASS / FAIL]
- Step 2E (CASCADE SCENARIO): [PASS / FAIL]
- Step 2G (LOAD SHAPE COMPARISON): [PASS / FAIL]

Unregistered tiers introduced after TABLE A closed: [0 unregistered tiers]

**C-14 compliance — Perspective separation:**
New tiers introduced in Step 2 sections: [0 — PASS / count + list — FAIL]

---

## V-02 — Single Axis: C-22 FAIL-Entry Itemization (Inline Bracket Format)

**Axis:** Add FAIL-entry itemization to audit block fields using inline bracket notation.
Each audit verdict field shows `[PASS / FAIL: list T-NNs with informal references found]`.
C-21 (failure-mode labels) and C-23 (escape-route mechanism) are not present.

**Hypothesis:** C-22 requires that when an audit field reports FAIL, it enumerates specific
non-compliant items rather than a binary flag. The inline bracket format places the
enumeration requirement inside the field definition, making it visible at the exact point
where the verdict is filled. This is more likely to produce itemized FAIL entries than a
general instruction preceding the field. Primary risk: under output pressure the model
may collapse `[PASS / FAIL: list X]` to `[PASS]` or `[FAIL]` without the enumeration.

**v6 predicted scoring:**
- C-21: FAIL — enforcement blocks have no failure-mode labels
- C-22: PASS — inline bracket format with FAIL-branch enumeration in audit fields
- C-23: FAIL — deferral prohibition names target section but no escape-route story
- Aspirational 13/15 → composite = `60 + 30 + (13/15 x 20) = 107.3`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where
  it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite that reports green because it mocks the connector layer

Three volume bands required — 1x nominal, 2x, 5x — because inertia lives at the volume
nobody tested.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Produce the tables and sections below in order. Do
not substitute prose for any table. Every cell must be filled.

---

**STEP 1 — TIER REGISTRY**

Complete Step 1 before any Step 2 section. All tier discovery, numeric limits, and
load-shape classification happen here. Step 2 contains caller behavior and backpressure
analysis only. Tiers discovered during Step 2 that are not in TABLE A are scope violations
— return to TABLE A before continuing.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use verbatim in every downstream section. No synonyms.
- `Limit` — A number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — Lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, with numeric rate differential
  and mechanism. **Do not defer load-shape classification to LOAD SHAPE COMPARISON —
  complete this column now, at registration time.**
- `Failure visibility window` — How quickly saturation becomes observable.
- `Recovery time` — How long until normal operation resumes.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed. Use T-NN identifiers throughout. Tiers discovered in Step 2
that are not in TABLE A are registry gaps — return to TABLE A, register the tier, then
continue.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*REGISTRY GAP scope-violation reminder: any tier appearing here that is not in TABLE A
requires a return to TABLE A before this section continues.*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*REGISTRY GAP scope-violation reminder: tiers referenced here that are not in TABLE A
require a return to TABLE A before continuing.*

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence.

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk. Every tier must appear. One sentence per tier.
For the top-ranked tier, reference `Failure visibility window` and `Recovery time`.

---

**Step 2E — CASCADE SCENARIO**

*REGISTRY GAP scope-violation reminder: tiers introduced during cascade trace that are
not in TABLE A require a return to TABLE A before continuing.*

Trace one concrete cascade starting at the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, name
the failure mode precisely. If present, state whether callers respect it.

---

**Step 2G — LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at
two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — State per-second rate. State which tiers are HIT or SAT and why.
- **BURST arrival** — State fraction and peak per-second rate. State which tiers are HIT
  or SAT and why.

At least one numeric comparison where status differs between patterns. Ground in a specific
TABLE A Limit value. If no tier changes status, name the rate limit mechanism.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Minimum two rows.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact config key or API attribute. Generic labels fail.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**STAGE 1** — Gate: at least two artifacts named. Catalog entry 1:
- **Artifact:** [specific name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2** — Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

---

**STEP 4 — INTEGRITY VERIFICATION**

Self-contained audit block. Complete after Stage 2.

**C-13 compliance — Tier-ID threading (individual per-section verdicts):**
- Step 2A (TABLE B): [PASS / FAIL: list T-NNs with informal references found]
- Step 2B (TABLE C): [PASS / FAIL: list T-NNs with informal references found]
- Step 2C (TABLE D): [PASS / FAIL: list T-NNs with informal references found]
- Step 2D (TIER RISK RANKING): [PASS / FAIL: list T-NNs with informal references found]
- Step 2E (CASCADE SCENARIO): [PASS / FAIL: list T-NNs with informal references found]
- Step 2G (LOAD SHAPE COMPARISON): [PASS / FAIL: list T-NNs with informal references found]

Unregistered tiers introduced after TABLE A closed: [0 / list specific tiers and sections]

**C-14 compliance — Perspective separation:**
New tiers introduced in Step 2 sections: [0 — PASS / count + list — FAIL]

---

## V-03 — Single Axis: C-23 Escape-Route Mechanism (One-Sentence Style)

**Axis:** Embed the escape-route mechanism in the load-shape deferral prohibition using a
one-sentence style — name the specific behavioral frame that makes deferral tempting,
without extended explanation or rejection proof. C-21 (failure-mode labels) and C-22
(FAIL-entry itemization) are not present.

**Hypothesis:** C-23 requires the prohibition to embed "the specific behavioral mechanism
that makes deferral tempting — the escape route story — naming the label, heuristic, or
framing that would cause a compliant executor to route shape classification away from the
registry." A one-sentence escape-route names this frame but does not explain the rejection
mechanism. This may satisfy C-23 at minimum depth — the frame is named, directing attention
to the temptation. Primary risk: the rubric may require the mechanism explanation to
constitute a true escape-route story, not just a frame label.

**v6 predicted scoring:**
- C-21: FAIL — no failure-mode labels on enforcement blocks
- C-22: FAIL — audit fields use binary [PASS / FAIL]
- C-23: PASS — escape-route frame named in deferral prohibition
- Aspirational 13/15 → composite = `60 + 30 + (13/15 x 20) = 107.3`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where
  it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite that reports green because it mocks the connector layer

Three volume bands required — 1x nominal, 2x, 5x.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Produce the tables and sections below in order. Every
cell must be filled.

---

**STEP 1 — TIER REGISTRY**

Complete Step 1 before any Step 2 section. All tier discovery, numeric limits, and
load-shape classification happen here. Tiers discovered during Step 2 that are not in
TABLE A are scope violations — return to TABLE A before continuing.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use verbatim everywhere. No synonyms.
- `Limit` — A number with a unit. Vague entries invalidate the row.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — Lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, with numeric rate differential
  and mechanism. **Do not defer load-shape classification to the LOAD SHAPE COMPARISON
  section. The escape route is the "STATUS tracks volume thresholds" frame — because TABLE A
  STATUS columns track OK/HIT/SAT threshold crossings, shape classification appears to belong
  in the section named LOAD SHAPE COMPARISON; reject this frame and complete the column now.**
- `Failure visibility window` — How quickly saturation becomes observable.
- `Recovery time` — How long until normal operation resumes.

---

**STEP 2 — ANALYSIS PHASES**

Tier registry closed. Use T-NN identifiers. Tiers discovered in Step 2 not in TABLE A
are scope violations — return to TABLE A before continuing.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*REGISTRY GAP scope-violation reminder: any tier appearing here that is not in TABLE A
requires a return to TABLE A.*

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*REGISTRY GAP scope-violation reminder: tiers referenced here not in TABLE A require
a return to TABLE A.*

At least one row. If no unprotected path exists, row 1 states conclusion with two named
controls as evidence.

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers. Every tier must appear. One sentence per tier. For the top-ranked
tier, reference `Failure visibility window` and `Recovery time`.

---

**Step 2E — CASCADE SCENARIO**

*REGISTRY GAP scope-violation reminder: tiers introduced during cascade trace not in
TABLE A require a return to TABLE A.*

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs. State each
causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? Name the failure
mode precisely if absent.

---

**Step 2G — LOAD SHAPE COMPARISON**

Compare 1x nominal at two arrival patterns. Identical total count; only distribution differs.
- **UNIFORM arrival** — State per-second rate. State which tiers are HIT or SAT.
- **BURST arrival** — State fraction and peak per-second rate. State which tiers are HIT or SAT.

At least one numeric comparison where status differs. Ground in a specific Limit value.
If no tier changes status, name the rate limit mechanism.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Minimum two rows.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**STAGE 1** — Gate: at least two artifacts named. Catalog entry 1:
- **Artifact:** [name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2** — Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

---

**STEP 4 — INTEGRITY VERIFICATION**

**C-13 compliance (individual per-section verdicts):**
- Step 2A (TABLE B): [PASS / FAIL]
- Step 2B (TABLE C): [PASS / FAIL]
- Step 2C (TABLE D): [PASS / FAIL]
- Step 2D (TIER RISK RANKING): [PASS / FAIL]
- Step 2E (CASCADE SCENARIO): [PASS / FAIL]
- Step 2G (LOAD SHAPE COMPARISON): [PASS / FAIL]

Unregistered tiers introduced after TABLE A closed: [0 unregistered tiers]

**C-14 compliance:** New tiers in Step 2: [0 — PASS / count + list — FAIL]

---

## V-04 — Combined: C-21 Rich Labels + C-22 Inline Bracket Itemization

**Axis:** Combine C-21 rich labels (criterion ID + failure mode name + one-line mechanism
description) with C-22 inline bracket itemization. C-23 (escape-route) is not present.

**Hypothesis:** C-21 rich labels and C-22 itemization are complementary: rich labels make
each control traceable to the failure mode at the enforcement point; inline itemization
makes the audit FAIL branch actionable by forcing enumeration at the verdict point.
Neither requires C-23 to function. Primary risk: cumulative token cost may compress TABLE A
or TABLE D rows under tight output budgets.

**v6 predicted scoring:**
- C-21: PASS — rich labels with criterion ID + failure mode name + mechanism description
- C-22: PASS — inline bracket format with FAIL-branch enumeration
- C-23: FAIL — deferral prohibition names target section but no escape-route story
- Aspirational 14/15 → composite = `60 + 30 + (14/15 x 20) = 108.7`

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where
  it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite that reports green because it mocks the connector layer

Three volume bands required — 1x nominal, 2x, 5x.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Produce the tables and sections below in order. Every
cell must be filled.

---

**STEP 1 — TIER REGISTRY**

Complete Step 1 before any Step 2 section. All tier discovery, numeric limits, and
load-shape classification happen here. Step 2 contains caller behavior and backpressure
analysis only. Tiers discovered during Step 2 not in TABLE A are scope violations — return
to TABLE A, register with all columns, then continue.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... Use verbatim everywhere. Synonyms make cross-section
  tracing unreliable.
- `Limit` — A number with a unit. Vague entries cannot anchor LOAD SHAPE COMPARISON.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — Lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, with numeric rate differential
  and mechanism. **Failure 2 + Failure 6 prevention (C-16, C-20): do not defer load-shape
  classification to LOAD SHAPE COMPARISON. Load-shape verdict requires the registered Limit
  value (available here) and must be present before caller analysis begins. Complete this
  column now.**
- `Failure visibility window` — How quickly saturation becomes observable.
- `Recovery time` — How long until normal operation resumes.

---

**STEP 2 — ANALYSIS PHASES**

Tier registry closed after Step 1. Use T-NN identifiers throughout. Tiers discovered in
Step 2 not in TABLE A are scope violations — return to TABLE A before continuing.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**Failure 5 prevention (C-17) — REGISTRY GAP SCOPE VIOLATION: tiers appearing here that
are not in TABLE A are evidence the enumeration phase was incomplete. Do not assign a new
T-NN here — return to TABLE A.**

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. Every tier must appear.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Failure 5 prevention (C-17) — REGISTRY GAP SCOPE VIOLATION: tiers referenced here that
are not in TABLE A are evidence of incomplete enumeration. Return to TABLE A.**

At least one row. If no unprotected path exists, row 1 states conclusion with two named
controls as evidence.

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers. Every tier must appear. One sentence per tier with rationale.
For the top-ranked tier, reference `Failure visibility window` and `Recovery time`.

---

**Step 2E — CASCADE SCENARIO**

**Failure 5 prevention (C-17) — REGISTRY GAP SCOPE VIOLATION: tiers introduced during
cascade trace that are not in TABLE A are evidence of incomplete enumeration. Return to
TABLE A.**

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs. State each
causal link. Minimum three tiers.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? Name the failure
mode precisely if absent.

---

**Step 2G — LOAD SHAPE COMPARISON**

Compare 1x nominal at two arrival patterns. Identical total count; only distribution differs.
- **UNIFORM arrival** — State per-second rate. State which tiers are HIT or SAT and why.
- **BURST arrival** — State fraction and peak per-second rate. State which tiers are HIT
  or SAT and why.

At least one numeric comparison where status differs. Ground in a specific Limit value.
If no tier changes status, name the rate limit mechanism as the structural reason.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Minimum two rows. One per gap from TABLE D, CASCADE, RETRY-AFTER, or LOAD SHAPE.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact config key or API attribute. Generic labels fail.

Calibration contrast:
> WRONG: "Add retry logic for throttle handling."
> PASS: "`connector.retryPolicy` — set `retryPolicy.type = ExponentialBackoff`,
> `retryPolicy.interval = PT2S`, `retryPolicy.maximumAttempts = 3`."

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Execute Stage 1 before Stage 2.

**STAGE 1** — Gate: at least two artifacts named. Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2** — Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

---

**STEP 4 — INTEGRITY VERIFICATION — Failure 4 prevention (C-18)**

Self-contained audit block. Complete after Stage 2. Report compliance per section.

**C-13 compliance — Tier-ID threading (individual per-section verdicts):**
- Step 2A (TABLE B): [PASS / FAIL: list T-NNs with informal references found]
- Step 2B (TABLE C): [PASS / FAIL: list T-NNs with informal references found]
- Step 2C (TABLE D): [PASS / FAIL: list T-NNs with informal references found]
- Step 2D (TIER RISK RANKING): [PASS / FAIL: list T-NNs with informal references found]
- Step 2E (CASCADE SCENARIO): [PASS / FAIL: list T-NNs with informal references found]
- Step 2G (LOAD SHAPE COMPARISON): [PASS / FAIL: list T-NNs with informal references found]

Unregistered tiers after TABLE A closed: [0 / list tiers + sections]

**C-14 compliance:** New tiers in Step 2: [0 — PASS / count + list — FAIL]

---

## V-05 — Maximum Density: C-21 Extended + C-22 Structured + C-23 Extended

**Axis:** Combine all three new v6 axes at maximum depth.
- **C-21 extended labels**: each enforcement block labeled with failure-mode identifier +
  name + one-sentence mechanism description (what the failure mode produces)
- **C-22 structured itemization**: audit FAIL branch is a named sub-entry listing specific
  missing items, not an inline bracket abbreviation
- **C-23 extended escape-route**: deferral prohibition names the inertia frame, explains
  why it routes analysis away from the registry, and shows why the frame is wrong

**Hypothesis:** The three axes are synergistic at maximum depth. C-21 extended labels make
each failure mode named and mechanism-explained at the enforcement point. C-22 structured
format makes the FAIL branch a first-class output entry rather than a bracket annotation.
C-23 extended escape-route addresses the temptation at its root — the "STATUS tracks volume
thresholds" frame — rather than only naming the prohibited section. The dual-role opening
loads UX vocabulary into working context before TABLE C demands it. Primary risk: maximum
density is the highest token cost; TABLE D or LOAD SHAPE may compress under tight budgets.

**v6 predicted scoring:**
- C-21: PASS — extended labels with failure mode name + mechanism description
- C-22: PASS — structured sub-entry FAIL format with explicit enumeration
- C-23: PASS — full escape-route story in deferral prohibition
- Aspirational 15/15 → composite = `60 + 30 + (15/15 x 20) = 110`

---

**ROLE 1 — FLOW AUTHOR PRE-ANALYSIS**

You are a flow author who has received a post-incident report showing throttle-related
failures in a production Power Automate environment. Before the technical analysis, write
a UX impact statement of 5-7 sentences covering: what error codes or signals appeared in
run history, what retry behavior was observed (immediate retries, exponential backoff, or
silent drops), how the business process was affected (partial completions, queued work,
user-facing errors), and what the first observable symptom was. Write as plain prose —
no tables, no section headers. This statement establishes the user-visible context that
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

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x
or 5x nominal. The multi-volume STATUS columns exist because inertia lives at the volume
nobody tested — not the volume in the design document.)*

Complete Step 1 in full before opening any Step 2 section. Step 1 is the perspective-
separated enumeration phase: all tier discovery, numeric limits, and load-shape
classification happen here. Step 2 contains caller behavior and backpressure analysis only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17): tiers discovered during Step 2
analysis are scope violations — evidence that the enumeration phase was incomplete, not
a routine fill-in opportunity. Return to TABLE A, register the tier with all columns
filled, then continue. This protocol is restated at each Step 2 section where mid-phase
discovery could occur.**

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
  The reason: synonyms make cross-section tracing unreliable — an auditor cannot verify
  a finding without resolving name equivalences.
- `Limit` — A number with a unit. The reason: a vague entry cannot anchor the numeric
  comparisons in LOAD SHAPE COMPARISON or determine STATUS transitions across bands.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands — if all STATUS
  columns are identical, the multi-volume purpose of this table is not achieved.
- `Binding at band` — Lowest band at which this tier is primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20) — deferral prohibition with escape-route
  mechanism: Complete this column now, at registration time. Do not defer load-shape
  classification to the LOAD SHAPE COMPARISON section (Step 2G).**

  **The escape route is the "STATUS tracks volume thresholds" frame:** TABLE A STATUS
  columns use OK/HIT/SAT to track whether a tier's volume threshold is crossed at each
  band. Because STATUS is a volume-threshold metric, TABLE A appears to be a pure
  volume-threshold analysis table — making load-shape classification (which compares
  arrival patterns, not volume levels) appear out of scope for the registry and naturally
  belonging in the section explicitly named "LOAD SHAPE COMPARISON." This frame routes
  shape analysis to Step 2G. **Reject this frame:** load-shape classification requires
  the registered Limit value (present in TABLE A at registration time) and produces a
  per-tier verdict that Step 2G depends on to ground its numeric comparison. Deferring
  the verdict to Step 2G creates a circular dependency and leaves the registry incomplete
  before caller analysis begins.

- `Failure visibility window` — How quickly saturation becomes observable (time + signal).
- `Recovery time` — How long until normal operation resumes after burst traffic subsides.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible in a development environment
where the connector layer is mocked.)*

**Standing enforcement reminder — C-17 + Failure 5 prevention (REGISTRY GAP SCOPE
VIOLATION): tiers appearing in backpressure analysis that are not in TABLE A are evidence
that the enumeration phase was incomplete. Do not assign a new T-NN here — this is not
a fill-in step. Return to TABLE A, register the tier with all required columns, then
continue.**

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

Minimum two hops. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade. The reason: a specific mechanism
explains how pressure propagates; a generic term does not.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

*(Cross-reference the Role 1 pre-analysis to populate error codes and retry behavior —
the pre-analysis stated what the flow author observed; this table quantifies it per tier.)*

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |
| ...     |                     |                           |                                      |                                      |                               |

`Failure if Retry-After ignored` — name the escalation path precisely. Precision matters
because each failure mode has a different remediation.

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has ever run at the volume where it fires. "We've never seen it fail" describes the test
environment's volume ceiling, not the production system's safety margin.)*

**Standing enforcement reminder — C-17 + Failure 5 prevention (REGISTRY GAP SCOPE
VIOLATION): tiers referenced in burst path analysis that are not in TABLE A are evidence
of incomplete enumeration. Return to TABLE A before continuing.**

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence.

| Path-ID | Entry component | Gap reason (why no rate limit applies, or named controls as evidence) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                                                       |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear —
a tier absent from this ranking has unknown risk. One sentence per tier with rationale.
For the top-ranked tier, reference `Failure visibility window` and `Recovery time`.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — C-17 + Failure 5 prevention (REGISTRY GAP SCOPE
VIOLATION): tiers introduced during cascade trace that are not in TABLE A are evidence
of incomplete enumeration. Return to TABLE A before continuing.**

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, name
the failure mode precisely — the remediation for a retry storm (exponential backoff) differs
from the remediation for quota exhaustion (circuit breaker). If present, state whether
callers respect it correctly.

---

**Step 2G — LOAD SHAPE COMPARISON**

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at
two arrival patterns. Identical total count; only arrival distribution differs. The reason:
per-minute limits and per-second limits respond differently to burst arrivals — a system
safe at uniform arrival may saturate under burst at the same total volume.

- **UNIFORM arrival** — State per-second arrival rate. State which tiers are HIT or SAT
  and why, referencing the specific Limit value.
- **BURST arrival** — State the burst fraction and peak per-second rate. State which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs between patterns at identical total
count. Ground in a specific TABLE A Limit value. If no tier changes status, name the
specific rate limit mechanism (per-minute bucket, per-second window, sliding window, token
bucket) as the structural reason.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

*(The purpose of TABLE F is to make remediations immediately actionable — specific parameter
names and values a team can apply without additional research.)*

Minimum two rows. One per gap from TABLE D, CASCADE, RETRY-AFTER, or LOAD SHAPE.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact config key, connector property, or API attribute.
Without a specific parameter, the row names a category and cannot be applied without
further research.

Calibration contrast:
> WRONG: "Add retry logic for throttle handling."
> PASS: "`connector.retryPolicy` on the SharePoint connector action — set
> `retryPolicy.type = ExponentialBackoff`, `retryPolicy.interval = PT2S`,
> `retryPolicy.maximumAttempts = 3`."

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer. The load test running at 10% of production concurrency. Their
architectural properties make specific throttle behaviors permanently unreachable.)*

Execute two stages in order. Stage 1 pre-loads artifact names that Stage 2's `Structural
reason` column requires — without Stage 1 complete, TABLE E entries default to category
labels rather than artifact-grounded explanations.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2 opens.

Calibration contrast:
> WRONG: "Integration tests do not cover throttle behavior because they run at low volume."
> PASS: "The integration test suite exercising connector calls via an HttpMessageHandler
> stub. Structural property: stub injects 429 responses; real rate gate is never invoked,
> so Retry-After timing is never produced and concurrent retry amplification is never
> observed."

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — GAP ENTRIES**

*Each gap entry traces its structural reason to a named Stage 1 artifact and the
architectural property that produces the gap.*

Produce TABLE E. Fill every cell. Minimum two rows.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + architectural property) | Test approach (component + volume/concurrency + assertion) |
|--------|-------------------------------------------|-----------|---------------------------------------------------------------|-----------------------------------------------------------|
| GAP-01 |                                           |           |                                                               |                                                           |
| GAP-02 |                                           |           |                                                               |                                                           |

Column calibration contrasts:
> `Throttle behavior` PASS: "Retry storm on T-02 connector limit when Retry-After header
> is absent; caller retries at full concurrency, exhausting tenant quota within 10 minutes."
>
> `Test approach` PASS: "Load test: 800 concurrent flow runs against a live connector in
> staging with tenant-level throttling enabled; assert 429 rate decrements to below 1%
> within 90 seconds."

Every cell must satisfy the PASS form.

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-18) — per-section compliance audit.** Self-contained block.
Complete after Stage 2. Each downstream section receives an individual verdict. An
aggregate count does not satisfy this block.

**C-13 compliance — Tier-ID threading:**

Each section's verdict is PASS if all T-NNs match TABLE A identifiers verbatim; FAIL if
any informal reference (synonym, component name used in place of T-NN) appears. FAIL
entries enumerate the specific informal references found.

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each, e.g., "T-02 referenced as 'the
  connector limit' at Hop 2"]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [0 unregistered tiers — PASS]
- If FAIL: [list each — name used, section where introduced, T-NN that should have been
  assigned in TABLE A]

**C-19 compliance — Failure 5 prevention (C-17 + C-19) distributed reminder audit:**
Scope-violation reminders must appear at each Step 2 section where mid-phase discovery
could occur.
- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- If any N: [list missing steps]

**C-14 compliance — Perspective separation:**
New tiers introduced in Step 2:
- Verdict: [PASS — 0 unregistered tiers]
- If FAIL: [count + list tiers and sections]
