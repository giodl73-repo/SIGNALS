# flow-throttle Variate — Round 10 (v10 Rubric)
**Date:** 2026-03-15
**Rubric:** v10 (C-01 through C-33, N_essential=5, N_recommended=3, N_aspirational=25)
**Baseline ceiling:** R9 V-05 (110/110 under v9 rubric; confirmed passes C-01 through C-30)

---

## State Analysis: What R9 V-05 Has vs. What R10 Must Add

**R9 V-05 coverage under v10 (confirmed):**
- C-01 through C-26: all pass (verified through R8)
- C-27: passes — co-located failure conditions present at TABLE A `Limit`, TABLE A
  `Load-shape verdict`, TABLE F `Setting or API parameter`, STEP 4 C-24 schema, STEP 4
  C-13 audit field, STEP 4 C-19 audit field
- C-28: passes — named slot template at C-24 schema (three labeled positions in code block)
- C-29: passes — criterion ID labels present at multiple failure conditions
- C-30: passes — C-27 generalized across TABLE A Limit, TABLE A Load-shape, TABLE F,
  C-24 schema, C-13, C-19

**v10 gaps in R9 V-05:**

**C-31 failure:** R9 V-05 places `(C-27):` on the C-24 schema in STEP 4 and
`(C-27 extension):` on TABLE A `Limit` in STEP 1. But TABLE A `Limit` appears first in
document order — it is the first C-27 application. C-31 requires the first application
in document order to carry the `(C-27):` primary label. R9 V-05 reverses the hierarchy:
the earlier site (TABLE A) carries the extension label; the later site (C-24 schema)
carries the primary label. The hierarchy is present but inverted.

**C-32 failure:** R9 V-05's `Load-shape verdict` failure condition is embedded inside the
deferral prohibition block ("A Load-shape verdict entry left blank or deferred...") rather
than stated as a structurally isolated, independently legible failure condition. An executor
reading only the `Load-shape verdict` column definition sees the condition only after
parsing the full deferral prohibition narrative. C-32 requires each extension site to name
its specific violation type in a way that is independently legible without cross-referencing
other blocks. The `Load-shape verdict` condition is entangled with C-26 structural proof
prose.

**C-33 failure:** R9 V-05 has no pre-definition precision-site inventory. Precision-
requiring sites are defined inline throughout STEP 1 and STEP 4. An executor cannot verify
C-30 completeness (all precision sites covered) without scanning the full prompt. C-33
closes this gap by requiring an upfront enumeration before any table is defined.

---

## Round 10 Variation Map

| Variation | Axes | C-31 | C-32 | C-33 | Predicted composite |
|-----------|------|------|------|------|---------------------|
| V-01 | Phrasing register: relabel so first document-order site is primary | PASS | FAIL | FAIL | 108/110 |
| V-02 | Lifecycle emphasis: add precision-site inventory before TABLE A | FAIL | FAIL | PASS | 108/110 |
| V-03 | Output format: structure each failure condition with explicit violation-type field | FAIL | PASS | FAIL | 108/110 |
| V-04 | Combined: phrasing register + lifecycle emphasis (C-31 + C-33) | PASS | FAIL | PASS | 109/110 |
| V-05 | Combined: phrasing register + output format + lifecycle emphasis (C-31 + C-32 + C-33) | PASS | PASS | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs baseline): Does relabeling TABLE A `Limit` as the primary `(C-27):` site and
relabeling all later sites as `(C-27 extension):` satisfy C-31 without affecting other
criteria? Hypothesis: yes — C-31 is a labeling-order criterion; semantic content of each
failure condition is unchanged. C-32 still fails because `Load-shape verdict` condition
remains entangled with deferral prohibition prose. C-33 still fails.

Q2 (V-02 vs baseline): Does adding a pre-definition precision-site inventory section satisfy
C-33 independently? Hypothesis: yes — C-33 requires enumeration before first definition;
adding an inventory block before TABLE A closes scope. C-31 and C-32 remain in R9 V-05
state.

Q3 (V-03 vs baseline): Does structuring each failure condition with an explicit `Violation
type:` field satisfy C-32 without fixing C-31 or C-33? Hypothesis: yes — the `Violation
type:` field forces the author to name the domain-specific precision failure at each site
in a named, independently-readable position. The `Load-shape verdict` condition becomes
independently legible when its violation type is extracted into a labeled field. C-31
labeling order and C-33 inventory are unchanged.

Q4 (V-04): Does combining relabeling (C-31) + inventory (C-33) achieve both without
interaction effects? Hypothesis: yes — C-31 is a label-content change; C-33 is a
structural-position change; they are orthogonal. C-32 still fails.

Q5 (V-05): Does the full combination score 110/110? Hypothesis: yes — V-05 corrects all
three gaps on top of the confirmed-110 R9 V-05 baseline, with no regressions.

---

## V-01 — Single Axis: Phrasing Register (primary/extension label order — C-31)

**Axis:** Phrasing register — TABLE A `Limit` column carries the `(C-27):` primary label
(it is the first precision-requiring definition site in document order). All subsequent
C-27 failure conditions carry `(C-27 extension):` labels. In R9 V-05, the C-24 schema in
STEP 4 carried the primary label despite appearing after TABLE A. This variation corrects
that inversion. No precision-site inventory is added (C-33 not targeted). The `Load-shape
verdict` failure condition retains its entangled form inside the deferral prohibition block
(C-32 not targeted).

**Hypothesis:** C-31 is a pure labeling-order criterion. Placing `(C-27):` on TABLE A
`Limit` (first in document order) and `(C-27 extension):` on all later sites (TABLE A
`Load-shape verdict`, TABLE F, C-24 schema, C-13 audit, C-19 audit) satisfies C-31 without
any content change to the failure conditions. C-32 still fails because the `Load-shape
verdict` condition is not independently legible as a standalone failure statement. C-33
still fails. Predicted: C-31 PASS, C-32 FAIL, C-33 FAIL. Composite = 108/110.

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
  comparisons in LOAD SHAPE COMPARISON.

  Compliance failure condition (C-27): An entry that uses a vague label ("limited",
  "throttled", "restricted") instead of a specific number-with-unit fails this column's
  precision requirement. "API-enforced limit" is a vague label; "1,200 req/min" is a
  number-with-unit.

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
  on the verdict; the verdict is deferred to the comparison.

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
attribute name.

Compliance failure condition (C-27 extension): A row that names a category of action
rather than a specific parameter identifier fails this column's precision requirement.
"Add retry logic" is a category; `connector.retryPolicy` is a parameter.

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

Compliance failure condition (C-27 extension): A finding that omits any named slot
position — or presents findings as free-form prose without the labeled slot structure —
fails the identification schema.

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

Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
specific informal references — issuing a binary flag only — fails this audit field.

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

---

---

## V-02 — Single Axis: Lifecycle Emphasis (precision-site inventory — C-33)

**Axis:** Lifecycle emphasis — a named PRECISION-SITE INVENTORY section appears before
TABLE A is defined. This section enumerates every precision-requiring definition site in
the prompt as a numbered list, with the required precision type and location for each. The
C-27 labeling order is unchanged from R9 V-05: the C-24 schema in STEP 4 retains the
`(C-27):` primary label; TABLE A `Limit` retains `(C-27 extension):` — C-31 is not
targeted. The `Load-shape verdict` failure condition retains its entangled form (C-32 not
targeted).

**Hypothesis:** Adding a pre-definition inventory section satisfies C-33 independently.
C-33 requires enumeration of all precision-requiring sites before any table is defined; a
numbered list before STEP 1 closes scope and makes omitted sites detectable during C-30
audit. C-31 and C-32 remain in R9 V-05 state. Predicted: C-31 FAIL, C-32 FAIL, C-33
PASS. Composite = 108/110.

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

**PRECISION-SITE INVENTORY**

*(Read before any table is defined — C-33. This list enumerates every precision-requiring
definition site in this prompt. An executor checking C-30 compliance at the end can verify
that each site below carries a co-located failure condition.)*

1. **TABLE A `Limit (number + unit)` column** (STEP 1) — required precision: specific
   number with unit; vague labels ("limited", "throttled") are a precision failure.
2. **TABLE A `Load-shape verdict` column** (STEP 1) — required precision: verdict token
   (SHAPE-NEUTRAL / SHAPE-SENSITIVE) at registration time; deferred or blank entries are
   a precision failure.
3. **TABLE F `Setting or API parameter` column** (Step 2H) — required precision: specific
   parameter name (e.g., `connector.retryPolicy`); category descriptions are a precision
   failure.
4. **STEP 4 C-24 finding schema** (STEP 4) — required precision: three named slots all
   populated (INFORMAL-NAME, SECTION:LOCATION, T-NN); missing any slot is a precision
   failure.
5. **STEP 4 C-13 audit FAIL entries** (STEP 4) — required precision: specific informal
   references enumerated; binary flag without enumeration is a precision failure.
6. **STEP 4 C-19 audit FAIL entries** (STEP 4) — required precision: per-step inline
   verdicts for each step; aggregate-only verdict is a precision failure.

*(Six precision-requiring sites total. Every site above must carry a co-located failure
condition in its definition section.)*

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
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min"). The
  reason: a vague entry cannot anchor STATUS transitions or LOAD SHAPE COMPARISON numeric
  assertions. Compliance failure condition (C-27 extension): An entry that uses a vague
  label ("limited", "throttled", "restricted") instead of a specific number-with-unit
  fails this column's precision requirement. "API-enforced limit" is a vague label;
  "1,200 req/min" is a number-with-unit.
- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer load-shape classification
  to the LOAD SHAPE COMPARISON section (Step 2G).

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track volume-threshold crossings. Because
  STATUS is a volume-threshold metric, TABLE A appears to be a pure volume-threshold
  analysis table — making load-shape classification appear out of scope and naturally
  belonging in "LOAD SHAPE COMPARISON." This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time. Premise 2: Step 2G depends on per-tier Load-shape verdicts
  to produce a meaningful numeric comparison. Consequence: deferring creates a circular
  dependency — the comparison depends on the verdict; the verdict is deferred to the
  comparison.

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
the failure mode precisely. If present, state whether callers respect it correctly.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Compare 1x nominal under uniform vs. burst distribution. Reference TABLE A Load-shape
verdicts. At least one numeric comparison where status differs between patterns.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key or API attribute name.

Compliance failure condition (C-27 extension): A row that names a category of action
rather than a specific parameter identifier fails this column's precision requirement.
"Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer.)*

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY** (two catalog entries before Stage 2)

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason | Test approach |
|--------|-------------------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                           |           |                   |               |
| GAP-02 |                                           |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. Complete after Stage 2.

**C-24 format requirement:** Two distinct labeled lines per field:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each finding within a FAIL list MUST populate all three named slots:

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

Unregistered tiers after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — tiers: [list each]

Compliance failure condition (C-27): A FAIL verdict that does not enumerate specific
informal references — issuing a binary flag only — fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format:** Per-step inline verdicts before aggregate.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

Compliance failure condition (C-27 extension): An audit field that issues a single
aggregate verdict without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe]

---

---

## V-03 — Single Axis: Output Format (domain-specific violation-type field — C-32)

**Axis:** Output format — each co-located failure condition uses a two-field structure:
`Violation type:` (names the specific precision failure category for this column or schema)
followed by `Compliance failure condition:` (the full statement). This structure makes each
extension site's violation type independently legible — a reader scanning the `Load-shape
verdict` column definition sees `Violation type: deferred verdict token` before reading
the full condition, without needing to parse the deferral prohibition narrative. The C-27
labeling order is unchanged from R9 V-05 (C-31 not targeted). No precision-site inventory
is added (C-33 not targeted).

**Hypothesis:** The two-field structure satisfies C-32 because the `Violation type:` field
extracts the domain-specific precision failure category into a named, labeled position.
The `Load-shape verdict` condition — which in R9 V-05 is entangled with the deferral
prohibition — becomes independently intelligible when its violation type appears as a
discrete labeled field. C-31 and C-33 remain as-in R9 V-05. Predicted: C-31 FAIL, C-32
PASS, C-33 FAIL. Composite = 108/110.

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
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min"). The
  reason: a vague entry cannot anchor STATUS transitions or LOAD SHAPE COMPARISON numeric
  assertions.
  - *Violation type: vague label substituted for numeric value*
  - Compliance failure condition (C-27 extension): An entry that uses a vague label
    ("limited", "throttled", "restricted") instead of a specific number-with-unit fails
    this column's precision requirement. "API-enforced limit" is a vague label;
    "1,200 req/min" is a number-with-unit.
- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer load-shape classification
  to the LOAD SHAPE COMPARISON section (Step 2G).

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track volume-threshold crossings. Because
  STATUS is a volume-threshold metric, TABLE A appears to be a pure volume-threshold table
  — making load-shape classification appear out of scope and naturally belonging in "LOAD
  SHAPE COMPARISON." This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time. Premise 2: Step 2G depends on per-tier Load-shape verdicts
  to produce a meaningful numeric comparison. Consequence: deferring creates a circular
  dependency — the comparison depends on the verdict; the verdict is deferred to the
  comparison.

  - *Violation type: deferred verdict token — entry routes load-shape classification to
    Step 2G rather than recording a verdict token at registration time*
  - Compliance failure condition (C-27 extension): A Load-shape verdict entry left blank
    or deferred ("see Step 2G", "analyzed below") fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

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

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during cascade trace that are not in TABLE A are scope violations. Return to TABLE A.

Minimum three tiers, each step caused by the previous. Use Tier-IDs throughout.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: Retry-After present and surfaced? Name the failure
mode precisely if absent.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Compare 1x nominal under uniform vs. burst distribution. Reference TABLE A Load-shape
verdicts. At least one numeric comparison where status differs between patterns.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key or API attribute name.
- *Violation type: category of action substituted for named parameter identifier*
- Compliance failure condition (C-27 extension): A row that names a category of action
  rather than a specific parameter identifier fails this column's precision requirement.
  "Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer.)*

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY** (two catalog entries before Stage 2)

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason | Test approach |
|--------|-------------------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                           |           |                   |               |
| GAP-02 |                                           |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**

**C-24 format requirement:** Two distinct labeled lines per field. Each finding within a
FAIL list populates all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry*
- Compliance failure condition (C-27): A finding that omits any named slot position — or
  presents findings as free-form prose without the labeled slot structure — fails the
  identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

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

Unregistered tiers after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — tiers: [list each]

- *Violation type: binary FAIL flag without enumeration of specific informal references*
- Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
  specific informal references — issuing a binary flag only — fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format:** Per-step inline verdicts before aggregate.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence*
- Compliance failure condition (C-27 extension): An audit field that issues a single
  aggregate verdict without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe]

---

---

## V-04 — Combined: Phrasing Register + Lifecycle Emphasis (C-31 + C-33)

**Axes:** (1) Phrasing register: TABLE A `Limit` column carries the primary `(C-27):` label
(first in document order); all subsequent failure conditions carry `(C-27 extension):`.
This corrects the inverted labeling in R9 V-05. (2) Lifecycle emphasis: a PRECISION-SITE
INVENTORY section appears before TABLE A. This closes C-33. The `Load-shape verdict`
failure condition retains its entangled form inside the deferral prohibition — no `Violation
type:` field is added (C-32 not targeted).

**Hypothesis:** C-31 and C-33 are orthogonal: one is a label-ordering change (which site
gets `(C-27):`), the other is a structural-position change (add inventory before TABLE A).
Combining them should not create interaction effects. C-32 still fails because the
`Load-shape verdict` condition is embedded in deferral prohibition prose without an
isolated violation-type label. Predicted: C-31 PASS, C-32 FAIL, C-33 PASS.
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

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33. Every precision-requiring site in this
prompt is enumerated below, in document order. An executor auditing C-30 compliance can
verify all sites carry co-located failure conditions by checking this list. Site 1 is the
primary C-27 site; Sites 2–6 carry C-27 extension labels.)*

1. **TABLE A `Limit (number + unit)` column** (STEP 1 — *primary C-27 site*) — required
   precision: specific number with unit; vague labels are a precision failure.
2. **TABLE A `Load-shape verdict` column** (STEP 1 — *C-27 extension 1*) — required
   precision: verdict token at registration time; deferred entries are a precision failure.
3. **TABLE F `Setting or API parameter` column** (Step 2H — *C-27 extension 2*) —
   required precision: specific parameter name; category descriptions are a precision
   failure.
4. **STEP 4 C-24 finding schema** (STEP 4 — *C-27 extension 3*) — required precision:
   three named slots all populated; missing any slot is a precision failure.
5. **STEP 4 C-13 audit FAIL entries** (STEP 4 — *C-27 extension 4*) — required precision:
   specific informal references enumerated; binary flag is a precision failure.
6. **STEP 4 C-19 audit FAIL entries** (STEP 4 — *C-27 extension 5*) — required precision:
   per-step inline verdicts; aggregate-only verdict is a precision failure.

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
  reason: synonyms make cross-section tracing unreliable.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min"). The
  reason: a vague entry cannot anchor STATUS transitions across volume bands or the numeric
  comparisons in LOAD SHAPE COMPARISON.

  Compliance failure condition (C-27): An entry that uses a vague label ("limited",
  "throttled", "restricted") instead of a specific number-with-unit fails this column's
  precision requirement. "API-enforced limit" is a vague label; "1,200 req/min" is a
  number-with-unit.

- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer load-shape classification
  to the LOAD SHAPE COMPARISON section (Step 2G).

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track volume-threshold crossings. Because
  STATUS is a volume-threshold metric, TABLE A appears to be a pure volume-threshold table
  — making load-shape classification appear out of scope and naturally belonging in "LOAD
  SHAPE COMPARISON." This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time. Premise 2: Step 2G depends on per-tier Load-shape verdicts
  to produce a meaningful numeric comparison. Consequence: deferring creates a circular
  dependency — the comparison depends on the verdict; the verdict is deferred to the
  comparison.

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
the failure mode precisely. If present, state whether callers respect it correctly.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Compare 1x nominal under uniform vs. burst distribution. Reference TABLE A Load-shape
verdicts. At least one numeric comparison where status differs between patterns.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key or API attribute name.

Compliance failure condition (C-27 extension): A row that names a category of action
rather than a specific parameter identifier fails this column's precision requirement.
"Add retry logic" is a category; `connector.retryPolicy` is a parameter.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer.)*

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY** (two catalog entries before Stage 2)

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**STAGE 2 — TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason | Test approach |
|--------|-------------------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                           |           |                   |               |
| GAP-02 |                                           |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. Complete after Stage 2.

**C-24 format requirement:** Two distinct labeled lines per field. Each finding within a
FAIL list populates all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

Compliance failure condition (C-27 extension): A finding that omits any named slot
position — or presents findings as free-form prose without the labeled slot structure —
fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

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

Unregistered tiers after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — tiers: [list each]

Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
specific informal references — issuing a binary flag only — fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format:** Per-step inline verdicts before aggregate.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

Compliance failure condition (C-27 extension): An audit field that issues a single
aggregate verdict without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe]

---

---

## V-05 — Combined: All Three Axes (C-31 + C-32 + C-33)

**Axes:** (1) Phrasing register: TABLE A `Limit` column carries the `(C-27):` primary label
(first in document order); all subsequent failure conditions carry `(C-27 extension):`.
(2) Output format: each failure condition uses the two-field structure with an explicit
`Violation type:` field naming the domain-specific precision failure for that column.
(3) Lifecycle emphasis: a PRECISION-SITE INVENTORY section appears before TABLE A, with
each site annotated to show it is the primary or an extension.

**Hypothesis:** V-05 is the v10 ceiling. C-31 is satisfied by placing `(C-27):` on TABLE A
`Limit` (first in document) and `(C-27 extension):` on all later sites. C-32 is satisfied
by the `Violation type:` field at each extension site, which names the specific precision
failure category independently — a reader scanning any single extension site understands
the violation without cross-referencing the primary. C-33 is satisfied by the pre-
definition inventory. All R9 V-05 elements (C-01 through C-30) are preserved with no
regressions. Predicted: C-31 PASS, C-32 PASS, C-33 PASS. Composite = 110/110.

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

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33. Every precision-requiring site in this
prompt is enumerated below, in document order, with the site's position in the C-27
labeling hierarchy. An executor auditing C-30 compliance can verify all sites carry co-
located failure conditions. Undiscovered or omitted precision sites are detectable by
comparing this list against the prompt's definition sections — the same function the tier
registry performs for tiers.)*

1. **TABLE A `Limit (number + unit)` column** (STEP 1)
   — *Primary C-27 site (first in document order)*
   — Violation type: vague label substituted for numeric value
2. **TABLE A `Load-shape verdict` column** (STEP 1)
   — *C-27 extension 1*
   — Violation type: deferred verdict token; entry routes classification to Step 2G rather
     than recording SHAPE-NEUTRAL or SHAPE-SENSITIVE at registration time
3. **TABLE F `Setting or API parameter` column** (Step 2H)
   — *C-27 extension 2*
   — Violation type: category of action substituted for named parameter identifier
4. **STEP 4 C-24 finding schema** (STEP 4)
   — *C-27 extension 3*
   — Violation type: missing slot identifier; one or more named slot positions absent
5. **STEP 4 C-13 audit FAIL entries** (STEP 4)
   — *C-27 extension 4*
   — Violation type: binary FAIL flag without enumeration of specific informal references
6. **STEP 4 C-19 audit FAIL entries** (STEP 4)
   — *C-27 extension 5*
   — Violation type: aggregate verdict without per-step inline verdict sequence

*(Six precision-requiring sites. Site 1 is primary; Sites 2–6 are extensions. Each site's
violation type above is the domain-specific precision failure for that column or schema —
independently legible without cross-referencing the primary site.)*

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
  comparisons in LOAD SHAPE COMPARISON.
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min") — the specific precision failure for this column is an
    imprecise placeholder where a measured number is required*
  - Compliance failure condition (C-27): An entry that uses a vague label instead of a
    specific number-with-unit fails this column's precision requirement. "API-enforced
    limit" is a vague label; "1,200 req/min" is a number-with-unit.

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

  - *Violation type: deferred verdict token — the specific precision failure for this
    column is routing the SHAPE-NEUTRAL/SHAPE-SENSITIVE classification to a downstream
    section rather than recording it at registration time, which is structurally distinct
    from the Limit column's vague-label failure (imprecise placeholder vs. absent
    classification)*
  - Compliance failure condition (C-27 extension): A Load-shape verdict entry left blank
    or deferred ("see Step 2G", "analyzed below") fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

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
attribute name.

- *Violation type: category of action substituted for named parameter identifier — the
  specific precision failure for this column is naming a task class ("add retry logic")
  where a deployable parameter name is required, which is structurally distinct from the
  Limit column's vague-label failure (placeholder for a number) and the Load-shape
  verdict's routing failure (absent classification)*
- Compliance failure condition (C-27 extension): A row that names a category of action
  rather than a specific parameter identifier fails this column's precision requirement.
  "Add retry logic" is a category; `connector.retryPolicy` is a parameter.

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

- *Violation type: missing slot identifier in finding entry — the specific precision failure
  for this schema is omitting one or more of the three named slot positions, which is
  structurally distinct from the Limit column's vague-label failure (imprecise content in
  a required field) and the Load-shape verdict's routing failure (absent classification)*
- Compliance failure condition (C-27 extension): A finding that omits any named slot
  position — or presents findings as free-form prose without the labeled slot structure —
  fails the identification schema.

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

- *Violation type: binary FAIL flag without enumeration of specific informal references —
  the specific precision failure for this audit field is a FAIL verdict that provides no
  actionable evidence, which is distinct from the finding schema's missing-slot failure
  (structural omission in a single finding)*
- Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
  specific informal references — issuing a binary flag only — fails this audit field.

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

- *Violation type: aggregate verdict without per-step inline verdict sequence — the specific
  precision failure for this audit field is issuing one PASS/FAIL for all four steps without
  individual step verdicts, which is distinct from the C-13 audit field's binary-flag
  failure (missing finding enumeration on FAIL) and the finding schema's missing-slot
  failure (structural omission)*
- Compliance failure condition (C-27 extension): An audit field that issues a single
  aggregate verdict without per-step inline verdicts fails the C-25 format requirement at
  this field.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]
