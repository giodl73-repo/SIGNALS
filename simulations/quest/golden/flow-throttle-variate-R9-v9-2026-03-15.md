# flow-throttle Variate — Round 9 (v9 Rubric)
**Date:** 2026-03-15
**Rubric:** v9 (C-01 through C-30, N_essential=5, N_recommended=3, N_aspirational=22)
**Baseline ceiling:** R8 V-05 (110/110 under v8 rubric; confirmed passes C-01 through C-27)

---

## State Analysis: What R8 V-05 Has vs. What R9 Must Add

**R8 V-05 coverage under v9 (confirmed):**
- C-01 through C-26: all pass (verified through R8)
- C-27: passes — co-located failure condition present at C-24 schema definition (WHY-first
  form: "A row that names a category... fails this column's precision requirement")
  AND at TABLE F `Setting or API parameter` column definition ("Compliance failure condition
  (C-27 extension): A row that names a category of action rather than a specific parameter
  identifier fails this column's precision requirement")

**v9 gaps in R8 V-05:**

**C-28 failure:** The C-24 identification schema in STEP 4 uses a positive-example format:
"T-02 referenced as 'the connector limit' at Step 2A Hop 2 — should have been T-02." This
shows what a correct finding looks like but does not present the three identifiers as
explicitly named, individually-labeled slot positions. A model receiving the example can
infer the required structure from the positive case, but infers the slot labels rather than
filling them. C-28 requires a named slot template — a code block or table with INFORMAL-NAME,
SECTION:LOCATION, T-NN as distinct, labeled positions — so compliance becomes slot-filling
rather than example-mimicry.

**C-29 failure:** The failure condition co-located with the C-24 schema does not carry a
criterion ID label. R8 V-05 says "A finding that lists only a T-NN without INFORMAL-NAME or
SECTION:LOCATION fails C-24." This names the downstream criterion (C-24) but does not label
the condition itself with the criterion ID it enforces (C-27). C-29 requires the label
"Compliance failure condition (C-27):" or equivalent — making the condition self-identifying
as a C-27 enforcement mechanism. The TABLE F extension already uses "Compliance failure
condition (C-27 extension):" which satisfies C-29 for that site, but the primary C-24
schema does not carry a parallel "Compliance failure condition (C-27):" header.

**C-30 failure:** C-30 requires the co-located failure condition at *every* definition site
requiring output precision — not only C-24 and TABLE F. TABLE A's `Limit (number + unit)`
column requires precision (a number with unit, not a vague label). R8 V-05 defines the
column as "a number with a unit" with a calibration example but no co-located failure
condition. Adding a failure condition there (and labeling it as a C-27 extension) satisfies
C-30 by demonstrating the principle is portable across TABLE A, TABLE F, and any other
definition site requiring precision within the same prompt.

---

## Round 9 Variation Map

| Variation | Axes | C-28 | C-29 | C-30 | Predicted composite |
|-----------|------|------|------|------|---------------------|
| V-01 | Output format: named slot template at C-24 (C-28 only) | PASS | FAIL | FAIL | 108/110 |
| V-02 | Phrasing register: criterion ID labels on all failure conditions (C-29 only) | FAIL | PASS | FAIL | 108/110 |
| V-03 | Lifecycle emphasis: failure condition generalized to TABLE A Limit column (C-30 only) | FAIL | FAIL | PASS | 108/110 |
| V-04 | Combined: named slot template + criterion ID labels (C-28 + C-29) | PASS | PASS | FAIL | 109/110 |
| V-05 | Combined: named slot + criterion ID labels + TABLE A Limit extension (C-28 + C-29 + C-30) | PASS | PASS | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs baseline): Does replacing the positive example with a named slot template
satisfy C-28 without affecting any other criterion? Hypothesis: yes — slot-filling vs.
example-inference is a pure format distinction with no content effect.

Q2 (V-02 vs baseline): Does adding "Compliance failure condition (C-27):" as a label
header to the C-24 failure condition satisfy C-29, and does it also propagate correctly to
the TABLE F extension label? Hypothesis: yes — the label converts the failure condition
from an implicit enforcement signal to a self-identified C-27 enforcement mechanism.

Q3 (V-03 vs baseline): Does adding a co-located failure condition at TABLE A's Limit column
(as a C-27 extension) satisfy C-30 when combined with the existing TABLE F failure condition?
Hypothesis: yes — C-30 requires the pattern at every precision-requiring definition site;
TABLE A Limit + TABLE F together represent more than one additional site, completing the
generalization requirement.

Q4 (V-04): Does the combination of C-28 + C-29 earn both without interaction effects?
Hypothesis: yes — they are orthogonal: one is a template presentation choice, the other
is a label on the failure condition.

Q5 (V-05): Does the full combination score 110/110? Hypothesis: yes — V-05 adds C-28,
C-29, and C-30 on top of a confirmed-110 R8 baseline, with no regressions introduced.

---

## V-01 — Single Axis: Output Format (named slot template — C-28)

**Axis:** Output format — the C-24 identification schema in STEP 4 is presented as a named
slot template: three labeled positions in a structured code block (INFORMAL-NAME,
SECTION:LOCATION, T-NN), not a positive example. The failure condition is co-located
(satisfying C-27) but is not labeled with a criterion ID header (C-29 not targeted). No
failure condition is added to TABLE A's Limit column (C-30 not targeted). Role, WHY-first
register, TABLE F C-27 extension, and all other R8 V-05 elements are preserved.

**Hypothesis:** Named slot template converts C-24 compliance from example-inference to
slot-filling. Each position is a discrete, labeled requirement rather than a structural
property of an example. The failure condition "A finding that omits any named slot position
fails the schema" is co-located (C-27 passes) but the label "Compliance failure condition"
does not carry "(C-27):" (C-29 fails). TABLE A Limit has no failure condition (C-30 fails).
Predicted: C-28 PASS, C-29 FAIL, C-30 FAIL. Composite = 108/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint
- The integration test suite reporting green because it mocks the connector layer

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output. Fill every cell. Produce sections in the order
shown.

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal — the volume nobody tested.)*

Complete Step 1 in full before opening any Step 2 section. Step 1 is the perspective-
separated enumeration phase: all tier discovery, numeric limits, and load-shape
classification happen here. Step 2 contains caller behavior and backpressure analysis only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
analysis are scope violations — evidence that the enumeration phase was incomplete, not a
routine fill-in opportunity. Return to TABLE A, register the tier with all columns filled,
then continue. This protocol is restated at each Step 2 section where mid-phase discovery
could occur.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section. The
  reason: synonyms make cross-section tracing unreliable.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min"). The
  reason: a vague entry ("limited", "throttled") cannot anchor the STATUS transitions or
  LOAD SHAPE COMPARISON numeric assertions.
- `STATUS Nx` — OK / HIT / SAT. Must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE, with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer load-shape classification
  to the LOAD SHAPE COMPARISON section (Step 2G).

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold
  is crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears to
  be a pure volume-threshold analysis table — making load-shape classification (which
  compares arrival patterns, not volume levels) appear out of scope for the registry and
  naturally belonging in the section explicitly named "LOAD SHAPE COMPARISON." This frame
  routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time, because SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined by
  whether the Limit is a per-second window (burst and uniform saturate differently) or a
  per-minute bucket (total volume determines saturation). Premise 2: Step 2G (LOAD SHAPE
  COMPARISON) depends on per-tier Load-shape verdicts to identify which tiers change STATUS
  between uniform and burst arrival — it cannot produce a meaningful numeric comparison
  without those verdicts already established. Consequence: deferring the verdict to Step 2G
  creates a circular dependency. The comparison depends on the verdict; the verdict is
  deferred to the comparison. The escape route does not defer the work to a more appropriate
  location — it makes the work structurally impossible to complete correctly.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

*(Do not begin STEP 2 until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible where the connector layer is
mocked.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers appearing in
backpressure analysis that are not in TABLE A are scope violations. Do not assign a new
T-NN here — return to TABLE A, register the tier with all required columns, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |

Minimum two hops. `Mechanism` must be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has ever run at the volume where it fires.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers referenced in
burst path analysis that are not in TABLE A are scope violations. Return to TABLE A.

At least one row. If no unprotected path exists, row 1 states the conclusion with at least
two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear. One
sentence per tier with rationale. For the top-ranked tier, reference `Failure visibility
window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during cascade trace that are not in TABLE A are scope violations. Return to TABLE A.

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

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT,
  referencing the Load-shape verdict and specific Limit value.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs between patterns at identical total
count. Ground in a specific TABLE A Limit value and Load-shape verdict.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Why specific parameters matter: a mitigation row that names a category of action ("add
retry logic") requires further research before it can be applied. A row that names the
exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name. Compliance failure condition (C-27 extension): A row that names a category
of action rather than a specific parameter identifier fails this column's precision
requirement. "Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer; the load test running at 10% of production concurrency.)*

Execute two stages in order. Stage 1 pre-loads artifact names that Stage 2's `Structural
reason` column requires.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — GAP ENTRIES**

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                   |                                                |
| GAP-02 |                                           |           |                                                   |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25):** Self-contained per-section
compliance audit. Each downstream section receives an individual verdict on a distinct
verdict line, with evidence on a distinct evidence line.

**C-24 format requirement:** Each field entry uses two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots. Use this
template — fill every labeled position, do not omit any slot:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

Compliance failure condition: A finding that omits any named slot position — or presents
findings as a free-form sentence without the labeled slot structure — fails the
identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: "[tier name] introduced at [step]"]

**C-19 compliance — Failure 5 prevention distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step before the
aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

---

---

## V-02 — Single Axis: Phrasing Register (criterion ID labels on failure conditions — C-29)

**Axis:** Phrasing register — every co-located failure condition is labeled with the
criterion ID it enforces, using the header form "Compliance failure condition (C-27):" or
"Compliance failure condition (C-27 extension):" so the enforcement boundary is
self-identifying. The C-24 identification schema retains the positive-example format (C-28
not targeted). No failure condition is added to TABLE A's Limit column (C-30 not targeted).
All other R8 V-05 elements — single role, WHY-first prose, TABLE F extension, escape-route
story, structural rejection proof — are preserved.

**Hypothesis:** Adding the "(C-27)" label to each failure condition header satisfies C-29
without altering any structural property of the existing analysis. The TABLE F extension
already used "(C-27 extension):" in R8 V-05; this variation applies the same label pattern
to the primary C-24 failure condition and to any other co-located failure conditions in the
prompt. Predicted: C-28 FAIL (positive example only, no named slots), C-29 PASS, C-30 FAIL
(TABLE A Limit still has no failure condition). Composite = 108/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite reporting green because it mocks the connector layer

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Fill every cell in the tables below.

---

**STEP 1 — TIER REGISTRY**

Complete Step 1 in full before opening any Step 2 section. This is the perspective-
separated enumeration phase.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. Return to TABLE A, register with all columns filled, then continue.
Restated at each vulnerable Step 2 section.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit. Vague entries ("limited",
  "throttled") cannot anchor STATUS transitions or LOAD SHAPE COMPARISON assertions.
- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now. Do not defer load-shape classification to Step 2G.

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns track volume-threshold crossings using OK/HIT/SAT. Because
  STATUS is a volume-threshold metric, TABLE A appears to be a pure volume-threshold table
  — making load-shape classification appear out of scope and naturally belonging in
  LOAD SHAPE COMPARISON. This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** Premise 1: load-shape classification requires
  the registered `Limit` value in TABLE A at registration time — SHAPE-NEUTRAL vs.
  SHAPE-SENSITIVE is determined by whether the Limit is a per-second window or a per-minute
  bucket. Premise 2: Step 2G depends on per-tier Load-shape verdicts to identify which
  tiers change STATUS between uniform and burst. Consequence: deferring the verdict to
  Step 2G creates a circular dependency — the comparison depends on the verdict, the verdict
  is deferred to the comparison.

- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes after burst subsides.

*(Do not begin STEP 2 until TABLE A is complete.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers not in TABLE A
are scope violations. Return to TABLE A before continuing.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |

Minimum two hops. `Mechanism`: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? | Retry-After surfaced? | Visible in run history? | Failure if Retry-After ignored |
|---------|---------------------|---------------------|----------------------|------------------------|-------------------------------|

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if any unregistered tier is encountered here.

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst |
|---------|----------------|------------|-------------------|-----------------------|
| P-01    |                |            |                   |                       |

---

**Step 2D — TIER RISK RANKING**

All TABLE A tiers, highest to lowest business risk. One sentence with rationale per tier.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if any unregistered tier is encountered here.

Minimum three tiers by T-NN. Each step caused by the previous. Explicit causal links.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

1x binding constraint tier: Retry-After present and surfaced? Name the exact failure mode
if absent. State whether callers respect it if present.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if any unregistered tier is encountered here.

Compare 1x nominal under uniform vs. burst distribution. Reference TABLE A Load-shape
verdicts. At least one numeric comparison where status differs between patterns.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact configuration key, connector property, or API attribute.

Compliance failure condition (C-27 extension): A row that names a category of action
rather than a specific parameter identifier fails this column's precision requirement.
"Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY** (two catalog entries before Stage 2)

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (T-NN + failure mode) | Test type | Structural reason | Test approach |
|--------|----------------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                        |           |                   |               |
| GAP-02 |                                        |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25):** Per-section compliance audit.
Each downstream section receives an individual verdict on a distinct verdict line, with
evidence on a distinct evidence line.

**C-24 format requirement:** Verdict and evidence on distinct labeled lines. Each finding
uses the full identification schema: informal name used + section and location + T-NN it
should have been.
Example FAIL finding: `"T-02 referenced as 'the connector limit' at Step 2A Hop 2"`

Compliance failure condition (C-27): A finding that names only a T-NN without the informal
name used or the section and location fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each with full three-identifier schema]

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
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each]

Compliance failure condition (C-27): A FAIL verdict that does not enumerate specific
informal references — issuing a binary flag only — fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format:** Individual inline verdict per step before aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

Compliance failure condition (C-27 extension): An audit that issues a single aggregate
verdict without per-step inline verdicts fails the C-25 format requirement at this field.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe]

---

---

## V-03 — Single Axis: Lifecycle Emphasis (C-27 generalization to TABLE A Limit — C-30)

**Axis:** Lifecycle emphasis — the co-located failure condition pattern is extended to every
precision-requiring definition site encountered during the analysis lifecycle, not only at
the C-24 schema (STEP 4) and TABLE F (Step 2H). Specifically, TABLE A's `Limit (number +
unit)` column definition acquires a co-located failure condition at registration time. The
C-24 identification schema retains the positive-example format (C-28 not targeted). Failure
conditions are co-located but not labeled with criterion ID headers (C-29 not targeted).
All other R8 V-05 elements are preserved.

**Hypothesis:** TABLE A's `Limit` column requires precision output (a number with unit, not
a vague label). Adding a failure condition there — "An entry that uses a vague label rather
than a specific number-with-unit fails this column's precision requirement (C-27 extension)"
— alongside the existing TABLE F failure condition satisfies C-30's requirement that the
pattern appears at every precision-requiring definition site. Predicted: C-28 FAIL,
C-29 FAIL (no criterion ID label headers), C-30 PASS. Composite = 108/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite reporting green because it mocks the connector layer

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Fill every cell.

---

**STEP 1 — TIER REGISTRY**

Complete Step 1 before opening any Step 2 section. All tier discovery, numeric limits, and
load-shape classification happen here. Step 2 contains caller behavior only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. Return to TABLE A with all columns filled, then continue. Restated
at each vulnerable section.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min"). The
  reason: a vague entry cannot anchor STATUS transitions across volume bands or numeric
  comparisons in LOAD SHAPE COMPARISON. Compliance failure condition (C-27 extension): An
  entry that uses a vague label ("limited", "throttled", "restricted") instead of a specific
  number-with-unit fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now. Do not defer load-shape classification to Step 2G.

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns track whether a tier's volume threshold is crossed at each
  band (OK/HIT/SAT). Because STATUS is a volume-threshold metric, TABLE A appears to be a
  pure volume-threshold table — making load-shape classification (which compares arrival
  patterns, not volume levels) appear out of scope and naturally belonging in LOAD SHAPE
  COMPARISON. This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** Premise 1: load-shape classification requires the
  registered `Limit` value present in TABLE A at registration time — SHAPE-NEUTRAL vs.
  SHAPE-SENSITIVE is determined by whether the Limit is a per-second window (burst and
  uniform saturate differently) or a per-minute bucket (total volume determines saturation).
  Premise 2: Step 2G depends on per-tier Load-shape verdicts to identify which tiers change
  STATUS between uniform and burst. Consequence: deferring the verdict to Step 2G creates a
  circular dependency. The comparison depends on the verdict; the verdict is deferred to the
  comparison.

  Compliance failure condition (C-27 extension): A Load-shape verdict entry left blank or
  marked "see Step 2G" fails the registration-time classification requirement.

- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes after burst subsides.

*(Do not begin STEP 2 until TABLE A is complete.)*

---

**STEP 2 — ANALYSIS PHASES**

Tier registry closed. Use T-NN identifiers throughout.

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers not in TABLE A
are scope violations. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |

Minimum two hops. Specific mechanism required.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? | Retry-After surfaced? | Visible in run history? | Failure if Retry-After ignored |
|---------|---------------------|---------------------|----------------------|------------------------|-------------------------------|

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if unregistered tier encountered.

| Path-ID | Entry component | Gap reason | Tier-IDs | Consequence at burst |
|---------|----------------|------------|----------|----------------------|
| P-01    |                |            |          |                      |

---

**Step 2D — TIER RISK RANKING**

All TABLE A tiers, highest to lowest risk. One sentence with rationale per tier.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if unregistered tier encountered.

Minimum three tiers by T-NN. Explicit causal links.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

1x binding constraint: Retry-After present? Name exact failure mode if absent.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if unregistered tier encountered.

Uniform vs. burst comparison using TABLE A Limit values and Load-shape verdicts.
At least one numeric comparison where status differs.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact configuration key, connector property, or API attribute.
Compliance failure condition (C-27 extension): A row that names a category of action
rather than a specific parameter identifier fails this column's precision requirement.
"Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**STAGE 1 — INVENTORY** (two named artifacts with structural properties before Stage 2)

Catalog entry 1: **Artifact:** [name] | **Structural property:** [reason]
Catalog entry 2: **Artifact:** [name] | **Structural property:** [reason]

State "Stage 1 complete."

**STAGE 2 — TABLE E**

| GAP-ID | Throttle behavior (T-NN + mode) | Test type | Structural reason | Test approach |
|--------|--------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                |           |                   |               |
| GAP-02 |                                |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25):** Per-section compliance audit.

**C-24 format:** Verdict and evidence on distinct labeled lines. Each finding names all
three identifiers: informal name used + section and location + T-NN.
Example: `"T-02 referenced as 'the connector limit' at Step 2A Hop 2"`

Compliance failure condition: A finding that names only a T-NN without the informal name
or section/location fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each with name + location + T-NN]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Unregistered tiers after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — list each with step

**C-19 compliance (C-25 format — per-step inline verdicts):**

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N: Verdict: FAIL | Missing steps: [list]

**C-14 compliance:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving: [describe]

---

---

## V-04 — Combined: Output Format + Phrasing Register (C-28 + C-29)

**Axes:** (1) Output format: named slot template at C-24 schema (C-28). (2) Phrasing
register: criterion ID labels on all co-located failure conditions (C-29). TABLE A Limit
column failure condition not added (C-30 not targeted). Single role, WHY-first enforcement
blocks, TABLE F C-27 extension — all R8 V-05 elements preserved.

**Hypothesis:** C-28 and C-29 are orthogonal: named slot template is a presentation format
choice; criterion ID label is a phrasing property of the failure condition header. Both
can be satisfied simultaneously in the same schema definition block. The TABLE F extension
already carried "(C-27 extension):" in R8 V-05; V-04 adds the parallel "(C-27):" label to
the primary C-24 failure condition. Predicted: C-28 PASS, C-29 PASS, C-30 FAIL.
Composite = 109/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal
- The integration test suite reporting green because it mocks the connector layer

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Fill every cell.

---

**STEP 1 — TIER REGISTRY**

Complete Step 1 before opening any Step 2 section. Perspective-separated enumeration phase.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence of incomplete enumeration. Return to TABLE A, register with
all columns filled, then continue. Restated at each vulnerable Step 2 section.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — T-01, T-02, ... verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit. Vague labels cannot anchor
  STATUS transitions or LOAD SHAPE COMPARISON assertions.
- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now. Do not defer load-shape classification to Step 2G.

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. Because STATUS is a volume-threshold metric (OK/HIT/SAT tracks threshold crossings),
  TABLE A appears to be a pure volume-threshold table — making load-shape classification
  appear out of scope and naturally belonging in LOAD SHAPE COMPARISON. This frame routes
  shape analysis to Step 2G.

  **Structural rejection proof (C-26):** Premise 1: load-shape classification requires
  the registered `Limit` value in TABLE A at registration time — SHAPE-NEUTRAL vs.
  SHAPE-SENSITIVE is determined by whether the Limit is a per-second window or a per-minute
  bucket. Premise 2: Step 2G depends on per-tier Load-shape verdicts to identify which
  tiers change STATUS between uniform and burst. Consequence: deferring the verdict to
  Step 2G creates a circular dependency — the comparison depends on the verdict, the
  verdict is deferred to the comparison.

- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

*(Do not begin STEP 2 until TABLE A is complete.)*

---

**STEP 2 — ANALYSIS PHASES**

Tier registry closed. Use T-NN identifiers throughout.

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers not in TABLE A
are scope violations. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |

Minimum two hops. `Mechanism`: queue-fill, connection-hold, retry-amplification,
dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? | Retry-After surfaced? | Visible in run history? | Failure if Retry-After ignored |
|---------|---------------------|---------------------|----------------------|------------------------|-------------------------------|

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if unregistered tier encountered.

| Path-ID | Entry component | Gap reason | Tier-IDs | Consequence at burst |
|---------|----------------|------------|----------|----------------------|
| P-01    |                |            |          |                      |

---

**Step 2D — TIER RISK RANKING**

All TABLE A tiers, highest to lowest risk, one sentence per tier.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if unregistered tier encountered.

Minimum three tiers by T-NN, explicit causal links.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

1x binding constraint: Retry-After present and surfaced? Exact failure mode if absent.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Return to TABLE A
if unregistered tier encountered.

Uniform vs. burst using TABLE A values and Load-shape verdicts. At least one numeric
comparison where status differs.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact key, connector property, or API attribute.

Compliance failure condition (C-27 extension): A row that names a category of action
rather than a specific parameter identifier fails this column's precision requirement.
"Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**STAGE 1** (two catalog entries before Stage 2):

Catalog entry 1: **Artifact:** [name] | **Structural property:** [reason]
Catalog entry 2: **Artifact:** [name] | **Structural property:** [reason]

State "Stage 1 complete."

**STAGE 2 — TABLE E**

| GAP-ID | Throttle behavior (T-NN + mode) | Test type | Structural reason | Test approach |
|--------|--------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                |           |                   |               |
| GAP-02 |                                |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25):** Per-section compliance audit.
Each section receives an individual verdict on a distinct verdict line, with evidence on a
distinct evidence line.

**C-24 format requirement:** Each entry uses two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding MUST use the following named slot template. Fill all three labeled
positions — no slot may be omitted:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

Compliance failure condition (C-27): A finding that omits any named slot position — or
presents findings as free-form prose without the labeled slot structure — fails the
identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each using the named slot template above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references: [list each]

Unregistered tiers after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — list each with step

Compliance failure condition (C-27): A FAIL verdict that does not enumerate specific
informal references fails this audit field.

**C-19 compliance (C-25 format — per-step inline verdicts):**

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N: Verdict: FAIL | Missing steps: [list each]

Compliance failure condition (C-27 extension): An aggregate verdict without per-step inline
verdicts fails the C-25 format requirement.

**C-14 compliance:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving: [describe]

---

---

## V-05 — Combined: All Three Axes (C-28 + C-29 + C-30)

**Axes:** (1) Output format: named slot template at C-24 schema (C-28). (2) Phrasing
register: criterion ID labels on all co-located failure conditions (C-29). (3) Lifecycle
emphasis: failure condition extended to TABLE A `Limit` column at registration time (C-30).
Single role, WHY-first enforcement, TABLE F extension — all R8 V-05 elements preserved.

**Hypothesis:** V-05 is the v9 ceiling. C-28 + C-29 are satisfied at the C-24 schema
definition. C-30 is satisfied because the failure condition now appears at three definition
sites: C-24 schema (primary), TABLE F `Setting or API parameter` (C-27 extension, from
R8 V-05), and TABLE A `Limit` column (C-27 extension, new in V-05). Each site carries its
own labeled failure condition, demonstrating the principle is portable across any definition
site requiring precision output. Predicted: C-28 PASS, C-29 PASS, C-30 PASS.
Composite = 110/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development
and staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists
to displace.

What inertia conceals:
- The burst path that was never rate-limited because no one tested at the volume where it fires
- The missing Retry-After handler that turns a 30-second throttle window into a 10-minute
  retry storm that exhausts quota across the tenant
- The cascade that takes down three dependent flows when a single connector limit fires
- The tier whose limit nobody measured at 5x nominal — the volume a viral workflow hits on
  day one — while everyone assumed the documented limit was the binding constraint
- The integration test suite reporting green because it mocks the connector layer

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

The tables below are the primary output — each carries a distinct finding category that
prose cannot represent with the same auditability. Fill every cell. Produce sections in
the order shown.

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal — the volume nobody tested.)*

Complete Step 1 in full before opening any Step 2 section. Step 1 is the perspective-
separated enumeration phase: all tier discovery, numeric limits, and load-shape
classification happen here. Step 2 contains caller behavior and backpressure analysis only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete, not a routine
fill-in opportunity. Return to TABLE A, register the tier with all columns filled, then
continue. This protocol is restated at each Step 2 section where mid-phase discovery
could occur.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section. The
  reason: synonyms make cross-section tracing unreliable — an auditor cannot verify a
  finding without resolving name equivalences.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min"). The
  reason: a vague entry cannot anchor STATUS transitions across volume bands or the numeric
  comparisons in LOAD SHAPE COMPARISON. Compliance failure condition (C-27 extension): An
  entry that uses a vague label ("limited", "throttled", "restricted") instead of a specific
  number-with-unit fails this column's precision requirement. "API-enforced limit" is a
  vague label; "1,200 req/min" is a number-with-unit.
- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer load-shape classification
  to the LOAD SHAPE COMPARISON section (Step 2G).

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold
  is crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears to
  be a pure volume-threshold analysis table — making load-shape classification (which
  compares arrival patterns, not volume levels) appear out of scope for the registry and
  naturally belonging in the section explicitly named "LOAD SHAPE COMPARISON." This frame
  routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time, because SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined
  by whether the Limit is expressed as a per-second window (burst and uniform saturate
  differently) or a per-minute bucket (total volume determines saturation). Premise 2:
  Step 2G (LOAD SHAPE COMPARISON) depends on per-tier Load-shape verdicts to identify
  which tiers change STATUS between uniform and burst arrival — it cannot produce a
  meaningful numeric comparison without those verdicts already established. Consequence:
  deferring the verdict to Step 2G creates a circular dependency. The comparison depends
  on the verdict; the verdict is deferred to the comparison. The escape route does not
  defer the work to a more appropriate location — it makes the work structurally impossible
  to complete correctly.

  Compliance failure condition (C-27 extension): A Load-shape verdict entry left blank or
  deferred ("see Step 2G", "analyzed below") fails the registration-time classification
  requirement and invalidates Step 2G's numeric comparison.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

*(Do not begin STEP 2 until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible where the connector layer is
mocked.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers appearing in
backpressure analysis that are not in TABLE A are scope violations. Do not assign a new
T-NN here — return to TABLE A, register the tier with all required columns, then continue.

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

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has ever run at the volume where it fires.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers referenced
in burst path analysis that are not in TABLE A are scope violations. Return to TABLE A.

At least one row. If no unprotected path exists, row 1 states the conclusion with at least
two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear. One
sentence per tier with rationale. For the top-ranked tier, reference `Failure visibility
window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during cascade trace that are not in TABLE A are scope violations. Return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, name
the failure mode precisely — the remediation for a retry storm (exponential backoff)
differs from the remediation for quota exhaustion (circuit breaker). If present, state
whether callers respect it correctly.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at
two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT,
  referencing the Load-shape verdict and specific Limit value.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs between patterns at identical total
count. Ground in a specific TABLE A Limit value and Load-shape verdict.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

Why specific parameters matter: a mitigation row that names a category of action ("add
retry logic") requires further research before it can be applied. A row that names the
exact parameter can be applied immediately. The difference is operational — one produces
a task, the other produces a change.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name. Compliance failure condition (C-27 extension): A row that names a category
of action rather than a specific parameter identifier fails this column's precision
requirement. "Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer; the load test running at 10% of production concurrency.)*

Execute two stages in order. Stage 1 pre-loads artifact names that Stage 2's `Structural
reason` column requires — without Stage 1 complete, TABLE E entries default to category
labels.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — GAP ENTRIES**

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                   |                                                |
| GAP-02 |                                           |           |                                                   |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. Complete after Stage 2. Each downstream section receives an
individual verdict on a distinct verdict line, with evidence on a distinct evidence line.

**C-24 format requirement:** Each field entry must use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots using this
template. Fill every labeled position — no slot may be omitted or combined:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

Compliance failure condition (C-27): A finding that omits any named slot position — or
presents findings as free-form prose without the labeled slot structure — fails the
identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: "[tier name] introduced at [step]"]

Compliance failure condition (C-27): A FAIL verdict that does not enumerate specific
informal references — issuing a binary flag only — fails this audit field.

**C-19 compliance — Failure 5 prevention (C-17, C-19) distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step before the
aggregate failure list. Format: `[step name]: [Y — reminder present / N — missing]`
followed by the aggregate on FAIL.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

Compliance failure condition (C-27 extension): An audit field that issues a single
aggregate verdict without per-step inline verdicts fails the C-25 format requirement at
this field.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]
