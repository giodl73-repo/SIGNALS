# flow-throttle Variate — Round 12 (v12 Rubric)
**Date:** 2026-03-15
**Rubric:** v12 (C-01 through C-37, N_essential=5, N_recommended=3, N_aspirational=29)
**Baseline ceiling:** R11 V-05 (110/110 under v11 rubric; confirmed passes C-01 through C-35)

---

## State Analysis: What R11 V-05 Has vs. What R12 Must Add

**R11 V-05 coverage under v12 (confirmed):**
- C-01 through C-35: all pass (verified through R11)
- TABLE F (site 3) passes C-36 — V-01's design named both TABLE A `Limit` and TABLE A
  `Load-shape verdict` failures before establishing TABLE F's distinguishing characteristic.
  This was the C-36 origin: two same-section TABLE A column neighbors, both named.

**v12 gaps in R11 V-05:**

**C-36 failure (three sites):** R11 V-05's multi-adjacent sites 2, 4, and 5 each name only
one adjacent neighbor, satisfying C-34 but failing C-36's all-neighbor requirement.

- *Site 2 (TABLE A `Load-shape verdict`)* — bordered by Limit (left) and TABLE F (right).
  V-05 names Limit's failure (content-absence) but does not name TABLE F's failure
  (category-for-identifier substitution) before establishing Load-shape verdict's own
  distinguishing characteristic. C-36 requires naming BOTH.

- *Site 4 (STEP 4 C-24 finding schema)* — bordered by TABLE F (left) and C-13 audit FAIL
  (right). V-05 names TABLE F's failure (category substitution) but does not name C-13
  audit's failure (binary FAIL flag without evidence enumeration) before establishing
  C-24's own distinguishing characteristic. C-36 requires naming BOTH.

- *Site 5 (STEP 4 C-13 audit FAIL)* — bordered by C-24 schema (left) and C-19 audit FAIL
  (right). V-05 names C-24's failure (structural omission within a finding) but does not
  name C-19's failure (verdict granularity collapse) before establishing C-13's own
  distinguishing characteristic. C-36 requires naming BOTH.

**C-37 failure:** R11 V-05's PRECISION-SITE INVENTORY uses a `C-27 hierarchy` column with
values "Primary" (site 1) and "C-27 extension N" (sites 2-6). C-37 requires the column to
use the C-31 parenthetical labeling format — `primary (C-27):` for the primary site and
`extension (C-27 extension):` for extension sites — so the C-31 labeling structure is
auditable from the inventory without opening each definition block. "Primary" does not carry
the `(C-27):` criterion reference that makes the label machine-checkable against the
definition block label. "C-27 extension 1" does not match `extension (C-27 extension):`.
An auditor scanning the inventory cannot confirm C-31 compliance without opening each
definition block to verify the criterion-ID annotation.

---

## Round 12 Variation Map

| Variation | Axes | C-36 | C-37 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | Output format: all multi-adjacent sites name BOTH neighbors (right-neighbor contrast added at sites 2, 4, 5) | PASS | FAIL | 109/110 |
| V-02 | Lifecycle emphasis: inventory `C-27 hierarchy` column values use exact C-31 format (`primary (C-27):` / `extension (C-27 extension):`) | FAIL | PASS | 109/110 |
| V-03 | Role sequence control: Cascade Analyst runs 2E + 2G before Rate Limit Analyst runs 2F + 2H; no C-36 or C-37 changes | FAIL | FAIL | 108/110 |
| V-04 | Combined: C-36 all-neighbor contrast (V-01 axis) + C-37 exact C-31 format (V-02 axis) | PASS | PASS | 110/110 |
| V-05 | Combined + phrasing register: V-04 + formal SHALL/MUST/PROHIBITED throughout | PASS | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs R11 baseline): Does adding right-neighbor contrast at the three failing
multi-adjacent sites satisfy C-36 without affecting C-37? Hypothesis: yes — C-36 governs
`*Violation type:*` field content at definition sites; C-37 governs inventory column format.
The two criteria modify separate locations. Predicted: C-36 PASS, C-37 FAIL.

Q2 (V-02 vs R11 baseline): Does changing the inventory hierarchy column values to the exact
`primary (C-27):` / `extension (C-27 extension):` format satisfy C-37 without affecting
C-36? Hypothesis: yes — C-37 governs inventory column format; the `*Violation type:*`
fields in definition blocks are unchanged from R11 V-05 and retain single-neighbor contrast
that fails C-36. Predicted: C-36 FAIL, C-37 PASS.

Q3 (V-03 control): Does role-sequence reordering affect C-36 or C-37? Hypothesis: no —
both criteria are structural. C-36 governs violation-type contrast content; C-37 governs
inventory column format. Neither is affected by analyst assignment. Both still fail.

Q4 (V-04): Does combining V-01's all-neighbor contrast with V-02's inventory format fix
achieve both C-36 and C-37 with no interaction effects? Hypothesis: yes — V-01 modifies
`*Violation type:*` field text in definition blocks; V-02 modifies the inventory table.
The changes are orthogonal.

Q5 (V-05): Does formal register throughout V-04 elevate without regressions? Hypothesis:
yes — formal register affects enforcement language in prohibitions and audit blocks, not
the content of `*Violation type:*` fields or inventory column format.

---

## V-01 — Single Axis: Output Format (all-neighbor contrast — C-36)

**Axis:** Output format — the three multi-adjacent `*Violation type:*` fields that fail C-36
in R11 V-05 (sites 2, 4, 5) are each extended to name BOTH their left and right neighbor's
failure before establishing the current site's distinguishing characteristic. The
PRECISION-SITE INVENTORY retains R11 V-05's column format ("Primary", "C-27 extension N").

**Hypothesis:** C-36 is satisfied by the all-neighbor contrast at every multi-adjacent
definition site. C-37 still fails because the inventory does not use the exact C-31
parenthetical format. Predicted: C-36 PASS, C-37 FAIL. Composite = 109/110.

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

*(Required before any table is defined — C-33 + C-35. Every precision-requiring site in
this prompt is enumerated below in document order. The `Violation type` column states the
specific failure at each site, matching the domain-specific text that will appear at each
definition site. This makes the inventory a self-contained preview of enforcement logic —
an auditor can verify C-30 completeness by scanning the table without inspecting definition
blocks.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | Primary | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | C-27 extension 1 | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | C-27 extension 2 | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | C-27 extension 3 | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | C-27 extension 4 | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | C-27 extension 5 | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types match the domain-specific text at each
downstream definition site — enabling inventory-vs-definition verification.)*

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
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Adjacent column contrast: the `Load-shape verdict`
    column's violation type (right neighbor) is a deferred verdict token — the executor
    routes classification to Step 2G rather than recording it at registration time. That is
    a timing failure: the content exists but is placed at the wrong moment. This column's
    failure is a value-absence failure: the numeric bound is missing or replaced by an
    imprecise placeholder. A deferred verdict and a vague number are both incomplete but
    require different corrections — move the classification act (verdict) vs. supply the
    missing number (Limit).*
  - Compliance failure condition (C-27): An entry using a vague label instead of a
    specific number-with-unit fails this column's precision requirement.

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
  be a pure volume-threshold analysis table — making load-shape classification appear out
  of scope for the registry and naturally belonging in the section named "LOAD SHAPE
  COMPARISON." This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value at
  registration time. Premise 2: Step 2G depends on per-tier Load-shape verdicts to produce
  meaningful comparisons. Consequence: deferring creates a circular dependency.

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at registration
    time. All-neighbor contrast (C-36): the `Limit` column's violation type (left neighbor,
    site 1) is a value-absence failure — the measured number is missing or replaced by an
    imprecise placeholder. TABLE F `Setting or API parameter`'s violation type (right
    neighbor, site 3) is a parameter-specificity failure — a task category is named where a
    deployable parameter identifier is required. This column's violation type is neither:
    the value is not absent and the failure is not about parameter identity; the failure is
    purely temporal — the act of recording the verdict is deferred to a section that
    structurally depends on it. Three failures at the same registry level, three different
    corrections: supply the number (Limit), move the classification act to registration
    time (this column), name the parameter (TABLE F).*
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
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

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
the failure mode precisely — retry storm (exponential backoff) vs. quota exhaustion
(circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs at identical total count.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

A mitigation row that names a category of action ("add retry logic") requires further
research before it can be applied. A row that names the exact parameter can be applied
immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). Adjacent column contrast: TABLE A
  `Limit`'s violation type (left neighbor) is a vague-label substitution — an imprecise
  placeholder for a measured numeric bound. TABLE A `Load-shape verdict`'s violation type
  (left neighbor) is a deferred verdict token — the classification is placed in the wrong
  section. This column's violation type is neither: the value is a string identifier, not
  a number; and there is no timing constraint. The failure is category substitution —
  naming what kind of action to take (a task category) where the specific deployable
  parameter name is required. Three failures at the same registry level: missing number
  (Limit), deferred classification (Load-shape verdict), action category instead of
  parameter identifier (this column).*
- Compliance failure condition (C-27 extension): A row naming a category of action rather
  than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer; the load test running at 10% of production concurrency.)*

Execute two stages. Stage 1 pre-loads artifact names; Stage 2 uses them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. Complete after Stage 2. Each downstream section receives an
individual verdict on a distinct verdict line, with evidence on a distinct evidence line.

**C-24 format requirement:** Each field entry must use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE A
  `Limit`'s violation type (left neighbor, site 1) is value absence — the measured number
  is missing or imprecise. TABLE F `Setting or API parameter`'s violation type (left
  neighbor, site 3) is category substitution — a task label occupies the parameter field.
  The STEP 4 C-13 audit FAIL field's violation type (right neighbor, site 5) is evidence
  absence — a FAIL verdict is issued at the aggregate level without enumerating the
  specific informal references. This schema's violation type is distinct from all three:
  not a missing number, not a wrong category, not an absent evidence list — a labeled slot
  position within a single finding entry is left empty or merged with adjacent content.*
- Compliance failure condition (C-27 extension): A finding that omits any named slot
  position — or presents findings as free-form prose — fails the identification schema.

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

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  All-neighbor contrast (C-36): the C-24 finding schema's violation type (left neighbor,
  site 4) is structural omission — a labeled slot is missing from an individual finding
  entry. The STEP 4 C-19 audit FAIL field's violation type (right neighbor, site 6) is
  verdict granularity collapse — individual step verdicts are merged into a single
  aggregate without per-step assessments. This audit field's violation type is distinct
  from both: the failure is not within a single finding (C-24's domain) and not about
  per-step verdict granularity (C-19's domain). The failure is at the aggregate reporting
  level — the FAIL verdict is correctly present but the specific informal references are
  not enumerated. Three adjacent audit-level failures: schema-internal omission (C-24),
  evidence absence on FAIL (this field), verdict granularity collapse (C-19).*
- Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
  specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step before the
aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 audit field's violation type (left neighbor, site 5) is evidence
  absence on FAIL — a FAIL verdict that names no specific findings. This field's violation
  type is verdict granularity collapse: per-step verdicts are merged into a single
  aggregate before the FAIL branch. C-13 fails on what the FAIL entry contains; C-19 fails
  on whether each step receives its own verdict line. Both fail at the audit level; each
  requires a different correction.*
- Compliance failure condition (C-27 extension): A single aggregate verdict without
  per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

---

## V-02 — Single Axis: Lifecycle Emphasis (exact C-31 hierarchy format — C-37)

**Axis:** Lifecycle emphasis — the PRECISION-SITE INVENTORY `C-27 hierarchy` column
values are changed from the informal labels in R11 V-05 ("Primary", "C-27 extension N")
to the exact C-31 parenthetical format: `primary (C-27):` for the primary site and
`extension (C-27 extension):` for all extension sites. The `*Violation type:*` fields in
column and schema definitions retain R11 V-05's single-neighbor contrast form — C-36 is
not targeted.

**Hypothesis:** C-37 is satisfied by the exact C-31 format in the inventory hierarchy
column. C-36 still fails because the `*Violation type:*` fields at sites 2, 4, and 5
each name only one neighbor. Predicted: C-36 FAIL, C-37 PASS. Composite = 109/110.

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

*(Required before any table is defined — C-33 + C-35 + C-37. Every precision-requiring
site is enumerated below in document order. The `Violation type` column states the
specific failure at each site, matching the domain-specific text at each definition site.
The `C-27 hierarchy` column uses the C-31 parenthetical labeling format — `primary
(C-27):` for the first definition site and `extension (C-27 extension):` for all
subsequent sites — making the C-31 labeling structure auditable from this inventory
without opening each definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Site 1 carries `primary (C-27):` — the C-31 label that
appears at its definition block. Sites 2–6 carry `extension (C-27 extension):` — the C-31
label that appears at each extension definition block. An auditor can confirm C-31
compliance by comparing these column values against the criterion-ID annotations at each
definition site without reconstructing the labeling hierarchy from scratch.)*

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
continue. This protocol is restated at each Step 2 section.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value — an imprecise placeholder
    where a measured number is required, which is structurally distinct from the Load-shape
    verdict column's routing failure (absent classification at registration time)*
  - Compliance failure condition (C-27): An entry using a vague label fails this column.

- `STATUS Nx` — OK / HIT / SAT; must shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with rate differential and
  mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral prohibition
  with escape-route story and structural rejection proof:**

  Complete this column now, at registration time. Do not defer to Step 2G.

  **Escape-route story (C-23):** The "STATUS tracks volume thresholds" frame makes TABLE A
  appear to be a pure volume-threshold table, routing shape classification to Step 2G.

  **Structural rejection proof (C-26):** Load-shape classification requires the registered
  Limit value at registration time; Step 2G depends on per-tier verdicts to produce
  meaningful comparisons. Deferring creates a circular dependency.

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to a downstream section rather than recording it at
    registration time, which is structurally distinct from the Limit column's vague-label
    failure (imprecise placeholder vs. absent classification)*
  - Compliance failure condition (C-27 extension): A blank or deferred Load-shape verdict
    entry fails the registration-time classification requirement.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

*(Do not begin STEP 2 until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers appearing
here not in TABLE A are scope violations. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |

Minimum two hops. `Mechanism` must be specific.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers referenced
here not in TABLE A are scope violations. Return to TABLE A.

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during cascade trace that are not in TABLE A are scope violations. Return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs throughout.
Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? Name the failure
mode precisely if absent.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
here not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. At least one numeric comparison where status differs.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name.

- *Violation type: category of action substituted for named parameter identifier — the
  specific precision failure is naming a task class where a deployable parameter name is
  required, which is structurally distinct from the Limit column's vague-label failure
  (placeholder for a number) and the Load-shape verdict's routing failure (absent
  classification)*
- Compliance failure condition (C-27 extension): A row naming a category of action rather
  than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Execute two stages. Stage 1 pre-loads artifact names; Stage 2 uses them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Catalog entry 1: **Artifact:** [name] | **Structural property:** [reason]
Catalog entry 2: **Artifact:** [name] | **Structural property:** [reason]
State "Stage 1 complete" before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**

**C-24 format requirement:** Two distinct labeled lines per field entry. Each finding
MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose, structurally distinct from the Limit column's
  vague-label failure and TABLE F's category-substitution failure*
- Compliance failure condition (C-27 extension): A finding omitting any named slot fails.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B): Verdict: [PASS / FAIL] | If FAIL: [three-slot findings]
Step 2B (TABLE C): Verdict: [PASS / FAIL] | If FAIL: [three-slot findings]
Step 2C (TABLE D): Verdict: [PASS / FAIL] | If FAIL: [three-slot findings]
Step 2D (RISK RANKING): Verdict: [PASS / FAIL] | If FAIL: [three-slot findings]
Step 2E (CASCADE): Verdict: [PASS / FAIL] | If FAIL: [three-slot findings]
Step 2G (LOAD SHAPE): Verdict: [PASS / FAIL] | If FAIL: [three-slot findings]
Unregistered tiers: Verdict: [PASS / FAIL] | If FAIL: [tier name + step]

- *Violation type: binary FAIL flag without enumeration — structurally distinct from
  finding schema's missing-slot failure*
- Compliance failure condition (C-27 extension): A FAIL verdict without specific informal
  references fails this audit field.

**C-19 compliance — distributed reminder audit:**

- Step 2A (TABLE B): [Y / N]
- Step 2C (TABLE D): [Y / N]
- Step 2E (CASCADE SCENARIO): [Y / N]
- Step 2G (LOAD SHAPE COMPARISON): [Y / N]
- If any N: Verdict: FAIL | Missing steps: [list]

- *Violation type: aggregate verdict without per-step inline verdicts — structurally
  distinct from C-13's binary-flag failure*
- Compliance failure condition (C-27 extension): Aggregate verdict without per-step
  inline verdicts fails C-25 format.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [location]

---

## V-03 — Single Axis: Role Sequence (control — no C-36 or C-37 changes)

**Axis:** Role sequence — the Cascade Analyst runs Steps 2E and 2G before the Rate Limit
Analyst runs Steps 2F and 2H. The standard sequence in R11 V-05 has Rate Limit Analyst
owning all phases in document order; this variation ensures cascade findings are visible
before the mitigation registry is written. The PRECISION-SITE INVENTORY retains R11 V-05's
column format; `*Violation type:*` fields retain R11 V-05's single-neighbor contrast.
Neither C-36 nor C-37 is targeted.

**Hypothesis:** Role sequence has no effect on C-36 or C-37. Both criteria are structural:
C-36 governs violation-type contrast content; C-37 governs inventory column format.
Neither is affected by analyst assignment. Both still fail. Predicted: C-36 FAIL, C-37
FAIL. Composite = 108/110.

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

You are a throughput analysis team for Connectors / Power Automate. Analyze the
rate-limited system described in the signal at 1x, 2x, and 5x nominal volume.

**Role assignments (cascade-first sequence):**
- **Rate Limit Analyst** (Connectors / Power Automate throughput domain expert):
  STEP 1, Steps 2A, 2B, 2C, 2D, 2F, 2H, STEP 3, STEP 4
- **Cascade Analyst** (multi-tier failure propagation specialist):
  Steps 2E and 2G (runs between Step 2D and Step 2F)

The Cascade Analyst completes the cascade scenario and load-shape comparison before the
Rate Limit Analyst writes mitigation registry entries — ensuring the mitigation entries
are written with the full cascade chain visible.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35. Every precision-requiring site is
enumerated below in document order.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | Primary | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | C-27 extension 1 | SHAPE-NEUTRAL or SHAPE-SENSITIVE at registration time | Deferred verdict token — routes classification to Step 2G rather than recording at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | C-27 extension 2 | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier |
| 4 | STEP 4 C-24 finding schema | C-27 extension 3 | All three slots: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent |
| 5 | STEP 4 C-13 audit FAIL entries | C-27 extension 4 | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of specific informal references |
| 6 | STEP 4 C-19 audit FAIL entries | C-27 extension 5 | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Site 1 is primary; Sites 2–6 are extensions.)*

---

**STEP 1 — TIER REGISTRY** *(Rate Limit Analyst)*

Complete Step 1 in full before opening any Step 2 section.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. Return to TABLE A, register with all columns filled, then continue.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit.
  - *Violation type: vague label substituted for numeric value — structurally distinct from
    Load-shape verdict's routing failure*
  - Compliance failure condition (C-27): An entry using a vague label fails this column.

- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with rate differential.

  Complete this column now, at registration time. Do not defer to Step 2G.

  **Escape-route story (C-23):** The "STATUS tracks volume thresholds" frame routes shape
  classification to Step 2G.

  **Structural rejection proof (C-26):** Load-shape classification requires the registered
  Limit value; Step 2G depends on per-tier verdicts. Deferring creates a circular
  dependency.

  - *Violation type: deferred verdict token — routing classification to Step 2G, structurally
    distinct from the Limit column's vague-label failure*
  - Compliance failure condition (C-27 extension): A blank or deferred Load-shape verdict
    fails the registration-time requirement.

*(Do not begin STEP 2 until TABLE A is complete.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed. Use T-NN identifiers throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)** *(Rate Limit Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers appearing
here not in TABLE A are scope violations. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)** *(Rate Limit Analyst)*

One row per Tier-ID. No tier may be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)** *(Rate Limit Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers referenced
here not in TABLE A are scope violations. Return to TABLE A.

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

---

**Step 2D — TIER RISK RANKING** *(Rate Limit Analyst)*

Rank all TABLE A tiers by business risk. Every tier must appear.

---

**Step 2E — CASCADE SCENARIO** *(Cascade Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
here not in TABLE A are scope violations. Return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs. Minimum three
tiers, each step caused by the previous.

---

**Step 2G — LOAD SHAPE COMPARISON** *(Cascade Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
here not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x at two arrival
patterns. At least one numeric comparison where status differs.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT** *(Rate Limit Analyst)*

*(Runs after Cascade Analyst completes Steps 2E and 2G.)*

For the 1x binding constraint tier: is Retry-After present and surfaced? Name the failure
mode precisely if absent.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)** *(Rate Limit Analyst)*

*(Written with cascade chain from Step 2E fully visible.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

- *Violation type: category of action substituted for named parameter identifier —
  structurally distinct from Limit's vague-label failure and Load-shape verdict's routing
  failure*
- Compliance failure condition (C-27 extension): A row naming a category rather than a
  parameter identifier fails this column.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS** *(Rate Limit Analyst)*

**STAGE 1:** Catalog entry 1: [artifact + structural property] | Entry 2: [artifact + property]
State "Stage 1 complete" before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason | Test approach |
|--------|-------------------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                           |           |                   |               |
| GAP-02 |                                           |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION** *(Rate Limit Analyst)*

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25).**

Each finding MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally]
SECTION:LOCATION: [step name and location]
T-NN:             [registered tier ID]
```

- *Violation type: missing slot identifier — structurally distinct from Limit's vague-label
  failure and TABLE F's category-substitution failure*
- Compliance failure condition (C-27 extension): A finding omitting any slot fails.

**C-13:** Step 2A: [PASS/FAIL] | Step 2B: [PASS/FAIL] | Step 2C: [PASS/FAIL] |
Step 2D: [PASS/FAIL] | Step 2E: [PASS/FAIL] | Step 2G: [PASS/FAIL] |
Unregistered tiers: [PASS/FAIL]

- *Violation type: binary FAIL without enumeration — distinct from finding schema's
  missing-slot failure*
- Compliance failure condition (C-27 extension): FAIL without informal references fails.

**C-19:** Step 2A [Y/N] | Step 2C [Y/N] | Step 2E [Y/N] | Step 2G [Y/N]
If any N: Verdict: FAIL | Missing: [list]

- *Violation type: aggregate verdict without per-step verdicts — distinct from C-13's
  binary-flag failure*
- Compliance failure condition (C-27 extension): Aggregate without per-step verdicts fails.

**C-14:** Verdict: [PASS/FAIL] | If FAIL: [interleaving location]

---

## V-04 — Combined: Output Format + Lifecycle Emphasis (C-36 + C-37)

**Axes:** (1) Output format: all multi-adjacent `*Violation type:*` fields name BOTH
neighboring failures — same as V-01. (2) Lifecycle emphasis: inventory `C-27 hierarchy`
column uses exact C-31 parenthetical format — same as V-02.

**Hypothesis:** V-04 is the v12 ceiling candidate. C-36 is satisfied by all-neighbor
contrast at sites 2, 4, and 5. C-37 is satisfied by the exact C-31 format in the
inventory hierarchy column. No interaction effects. Predicted: C-36 PASS, C-37 PASS.
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

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37. Every precision-requiring
site is enumerated below in document order. The `Violation type` column states the
specific failure at each site, matching the domain-specific text at each definition site.
The `C-27 hierarchy` column uses the C-31 parenthetical labeling format — `primary
(C-27):` for the first definition site and `extension (C-27 extension):` for all
subsequent sites — making the C-31 labeling structure auditable from this inventory
without opening each definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Site 1 carries `primary (C-27):` matching the label at
its definition block. Sites 2–6 carry `extension (C-27 extension):` matching the label
at each extension definition block. An auditor can confirm C-31 compliance from this
inventory without opening each definition block. Violation types match the domain-specific
text at each downstream definition site.)*

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal — the volume nobody tested.)*

Complete Step 1 in full before opening any Step 2 section. All tier discovery, numeric
limits, and load-shape classification happen here. Step 2 contains caller behavior only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete, not a routine
fill-in opportunity. Return to TABLE A, register the tier with all columns filled, then
continue. This protocol is restated at each Step 2 section.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Adjacent column contrast: the `Load-shape verdict`
    column's violation type (right neighbor) is a deferred verdict token — the executor
    routes the classification to Step 2G rather than recording it at registration time.
    That is a timing failure: the verdict category is known but placed at the wrong moment.
    This column's failure is a value-absence failure: the measured number is missing or
    replaced by an imprecise placeholder. A deferred verdict and a vague number are both
    incomplete; each requires a different correction.*
  - Compliance failure condition (C-27): An entry using a vague label instead of a
    specific number-with-unit fails this column's precision requirement.

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
  be a pure volume-threshold analysis table — making load-shape classification appear out
  of scope for the registry and naturally belonging in the section named "LOAD SHAPE
  COMPARISON." This frame routes shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value at
  registration time. Premise 2: Step 2G depends on per-tier Load-shape verdicts to produce
  meaningful comparisons. Consequence: deferring creates a circular dependency.

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at registration
    time. All-neighbor contrast (C-36): the `Limit` column's violation type (left neighbor,
    site 1) is a value-absence failure — the measured number is missing or replaced by an
    imprecise placeholder. TABLE F `Setting or API parameter`'s violation type (right
    neighbor, site 3) is a parameter-specificity failure — a task category is named where
    a deployable parameter identifier is required. This column's violation type is neither:
    the value is not absent and the failure is not about parameter identity; the failure is
    purely temporal — the act of recording the verdict is deferred to a section that
    structurally depends on it. Three failures at the same registry level, three different
    corrections: supply the number (Limit), move the classification act to registration
    time (this column), name the parameter (TABLE F).*
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
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

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
the failure mode precisely — retry storm vs. quota exhaustion require different remediations.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. At least one numeric comparison where status differs at identical total
count.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

A mitigation row that names a category of action requires further research before it can
be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). Adjacent column contrast: TABLE A
  `Limit`'s violation type (left neighbor) is a vague-label substitution — an imprecise
  placeholder for a measured numeric bound. TABLE A `Load-shape verdict`'s violation type
  (left neighbor) is a deferred verdict token — the classification is placed in the wrong
  section. This column's violation type is neither: the value is a string identifier, not
  a number; and there is no timing constraint. The failure is category substitution —
  naming what kind of action to take where the specific deployable parameter name is
  required. Three failures at the same registry level: missing number (Limit), deferred
  classification (verdict), action category instead of parameter identifier (this column).*
- Compliance failure condition (C-27 extension): A row naming a category of action rather
  than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Execute two stages. Stage 1 pre-loads artifact names; Stage 2 uses them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. Complete after Stage 2. Each downstream section receives an
individual verdict on a distinct verdict line, with evidence on a distinct evidence line.

**C-24 format requirement:** Each field entry must use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE A
  `Limit`'s violation type (left neighbor, site 1) is value absence — the measured number
  is missing or imprecise. TABLE F `Setting or API parameter`'s violation type (left
  neighbor, site 3) is category substitution — a task label occupies the parameter field.
  The STEP 4 C-13 audit FAIL field's violation type (right neighbor, site 5) is evidence
  absence — a FAIL verdict is issued at the aggregate level without enumerating the
  specific informal references. This schema's violation type is distinct from all three:
  not a missing number, not a wrong category, not an absent evidence list — a labeled slot
  position within a single finding entry is left empty or merged with adjacent content.*
- Compliance failure condition (C-27 extension): A finding that omits any named slot
  position — or presents findings as free-form prose — fails the identification schema.

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

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  All-neighbor contrast (C-36): the C-24 finding schema's violation type (left neighbor,
  site 4) is structural omission — a labeled slot is missing from an individual finding
  entry. The STEP 4 C-19 audit FAIL field's violation type (right neighbor, site 6) is
  verdict granularity collapse — individual step verdicts are merged into a single
  aggregate without per-step assessments. This audit field's violation type is distinct
  from both: the failure is not within a single finding and not about per-step verdict
  granularity. The failure is at the aggregate reporting level — the FAIL verdict is
  correctly present but the specific informal references are not enumerated. Three adjacent
  audit-level failures: schema-internal omission (C-24), evidence absence on FAIL (this
  field), verdict granularity collapse (C-19).*
- Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
  specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict per step before aggregate.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 audit field's violation type (left neighbor, site 5) is evidence
  absence on FAIL — a FAIL verdict that names no specific findings. This field's violation
  type is verdict granularity collapse: per-step verdicts are merged into a single
  aggregate before the FAIL branch. C-13 fails on what the FAIL entry contains; C-19 fails
  on whether each step receives its own verdict line. Both fail at the audit level; each
  requires a different correction.*
- Compliance failure condition (C-27 extension): A single aggregate verdict without
  per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

---

## V-05 — Combined: All Three Axes (C-36 + C-37 + Phrasing Register)

**Axes:** (1) Output format: all-neighbor contrast at multi-adjacent sites — same as V-01
and V-04. (2) Lifecycle emphasis: exact C-31 parenthetical format in inventory hierarchy
column — same as V-02 and V-04. (3) Phrasing register: all enforcement obligations stated
using formal register (SHALL, MUST, PROHIBITED, MAY NOT) throughout prohibitions, failure
conditions, and audit requirements.

**Hypothesis:** V-05 is the v12 ceiling. C-36 is satisfied by all-neighbor contrast at
sites 2, 4, and 5. C-37 is satisfied by the exact C-31 format in the inventory hierarchy
column. The formal register strengthens enforcement posture without altering C-36 or C-37
content. Predicted: C-36 PASS, C-37 PASS. Composite = 110/110.

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

*(Required before any table is defined — C-33 + C-35 + C-37. Every precision-requiring
site in this prompt is enumerated below in document order. The `Violation type` column
states the specific failure at each site, matching the domain-specific text that SHALL
appear at each definition site. The `C-27 hierarchy` column uses the C-31 parenthetical
labeling format — `primary (C-27):` for the first definition site and `extension (C-27
extension):` for all subsequent sites — making the C-31 labeling structure auditable from
this inventory without opening each definition block. An executor SHALL verify that the
label at each definition block matches the `C-27 hierarchy` value in this row. Any
precision-requiring site discovered after this inventory closes constitutes a scope
violation.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Site 1 carries `primary (C-27):` — the label that SHALL
appear at its definition block. Sites 2–6 carry `extension (C-27 extension):` — the label
that SHALL appear at each extension definition block. An executor SHALL verify C-31
compliance by comparing these column values against the criterion-ID annotations at each
definition site.)*

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal — the volume nobody tested.)*

An executor SHALL complete Step 1 in full before opening any Step 2 section. Step 1 is
the perspective-separated enumeration phase: all tier discovery, numeric limits, and
load-shape classification MUST happen here. Step 2 MUST contain caller behavior and
backpressure analysis only.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete, not a routine
fill-in opportunity. An executor MUST return to TABLE A, register the tier with all
columns filled, then continue. This protocol SHALL be restated at each Step 2 section
where mid-phase discovery could occur.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit. An executor MUST NOT enter a
  vague label.
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Adjacent column contrast: the `Load-shape verdict`
    column's violation type (right neighbor) is a deferred verdict token — the executor
    routes the SHAPE-NEUTRAL/SHAPE-SENSITIVE classification to Step 2G rather than
    recording it at registration time. That is a timing failure: the content exists but
    is placed at the wrong moment. This column's failure is a value-absence failure: the
    numeric bound is missing or replaced by an imprecise placeholder. A deferred verdict
    and a vague number are both incomplete; each requires a different correction — move
    the classification act (verdict) vs. supply the missing number (Limit). An executor
    MUST NOT conflate these two failure modes.*
  - Compliance failure condition (C-27): An entry using a vague label instead of a
    specific number-with-unit FAILS this column's precision requirement.

- `STATUS Nx` — OK / HIT / SAT; MUST shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — deferral PROHIBITED:**

  An executor SHALL complete this column at registration time. Deferral to Step 2G is
  PROHIBITED.

  **Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
  frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold
  is crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears to
  be a pure volume-threshold analysis table — making load-shape classification appear out
  of scope for the registry and naturally belonging in the section named "LOAD SHAPE
  COMPARISON." This frame routes shape analysis to Step 2G. An executor following this
  frame will correctly fill the bottleneck ordering in Step 1 but leave the Load-shape
  verdict column blank or annotated "see Step 2G."

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value at
  registration time, because SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined by whether
  the Limit is expressed as a per-second window or a per-minute bucket. Premise 2: Step 2G
  depends on per-tier Load-shape verdicts to identify which tiers change STATUS between
  uniform and burst arrival. Consequence: deferring creates a circular dependency. The
  escape route does not defer the work to a more appropriate location — it makes correct
  completion structurally impossible.

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at registration
    time. All-neighbor contrast (C-36): the `Limit` column's violation type (left neighbor,
    site 1) is a value-absence failure — the measured number is missing or replaced by an
    imprecise placeholder. TABLE F `Setting or API parameter`'s violation type (right
    neighbor, site 3) is a parameter-specificity failure — a task category is named where
    a deployable parameter identifier is required. This column's violation type is neither:
    the value is not absent and the failure is not about parameter identity; the failure
    is purely temporal — the act of recording the verdict is deferred to a section that
    structurally depends on it. Three failures at the same registry level, three different
    corrections: supply the number (Limit), move the classification act to registration
    time (this column), name the parameter (TABLE F). An executor MUST NOT conflate these
    three failure modes — each requires a distinct remediation.*
  - Compliance failure condition (C-27 extension): A Load-shape verdict entry left blank
    or deferred ("see Step 2G", "analyzed below") FAILS the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

*(An executor SHALL NOT begin STEP 2 until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. An executor SHALL use T-NN identifiers from
TABLE A throughout. New tiers MUST NOT be introduced in Step 2.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible where the connector layer is
mocked.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers appearing in
backpressure analysis that are not in TABLE A are scope violations. An executor MUST NOT
assign a new T-NN here. The executor SHALL return to TABLE A, register the tier with all
required columns, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

Minimum two hops. `Mechanism` MUST be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier MAY be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has ever run at the volume where it fires.)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers referenced
in burst path analysis that are not in TABLE A are scope violations. The executor SHALL
return to TABLE A.

At least one row. If no unprotected path exists, row 1 MUST state the conclusion with at
least two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier MUST appear. One
sentence per tier with rationale. For the top-ranked tier, the executor SHALL reference
`Failure visibility window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during cascade trace that are not in TABLE A are scope violations. The executor MUST
return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs throughout.
State each causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the
executor MUST name the failure mode precisely — the remediation for a retry storm
(exponential backoff) differs from the remediation for quota exhaustion (circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. The executor MUST
return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs between patterns SHALL be present.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

A mitigation row that names a category of action ("add retry logic") requires further
research before it can be applied. A row that names the exact parameter can be applied
immediately. An executor MUST name the parameter, not the category.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API
attribute name. An executor MUST NOT enter a category-of-action label.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). Adjacent column contrast: TABLE A
  `Limit`'s violation type (left neighbor) is a vague-label substitution — an imprecise
  placeholder for a measured numeric bound. TABLE A `Load-shape verdict`'s violation type
  (left neighbor) is a deferred verdict token — the classification is placed in the wrong
  section. This column's violation type is neither: the value is a string identifier, not
  a number; and there is no timing constraint. The failure is category substitution —
  naming what kind of action to take where the specific deployable parameter name is
  required. Three failures at the same registry level: missing number (Limit), deferred
  classification (verdict), action category instead of parameter identifier (this column).
  An executor MUST NOT conflate these three failure modes.*
- Compliance failure condition (C-27 extension): A row naming a category of action rather
  than a specific parameter identifier FAILS this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

Execute two stages in order. Stage 1 pre-loads artifact names; Stage 2 uses them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts named with structural properties before Stage 2 opens. An
executor SHALL NOT open Stage 2 until this gate is satisfied.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. An executor SHALL complete this block after Stage 2. Each downstream
section MUST receive an individual verdict on a distinct verdict line, with evidence on a
distinct evidence line.

**C-24 format requirement:** Each field entry MUST use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots. An
executor SHALL fill every labeled position — no slot MAY be omitted or combined:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE A
  `Limit`'s violation type (left neighbor, site 1) is value absence — the measured number
  is missing or imprecise. TABLE F `Setting or API parameter`'s violation type (left
  neighbor, site 3) is category substitution — a task label occupies the parameter field.
  The STEP 4 C-13 audit FAIL field's violation type (right neighbor, site 5) is evidence
  absence — a FAIL verdict is issued at the aggregate level without enumerating the
  specific informal references. This schema's violation type is distinct from all three:
  not a missing number, not a wrong category, not an absent evidence list — a labeled slot
  position within a single finding entry is left empty or merged. An executor MUST NOT
  conflate structural omission (this schema) with evidence absence (C-13) — the schema
  failure is within a single finding; the audit field failure is at the reporting level.*
- Compliance failure condition (C-27 extension): A finding that omits any named slot
  position — or presents findings as free-form prose — FAILS the identification schema.

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

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  All-neighbor contrast (C-36): the C-24 finding schema's violation type (left neighbor,
  site 4) is structural omission — a labeled slot is missing from an individual finding
  entry. The STEP 4 C-19 audit FAIL field's violation type (right neighbor, site 6) is
  verdict granularity collapse — individual step verdicts are merged into a single
  aggregate without per-step assessments. This audit field's violation type is distinct
  from both: the failure is not within a single finding and not about per-step verdict
  granularity. The failure is at the aggregate reporting level — the FAIL verdict is
  correctly present but the specific informal references are not enumerated. Three adjacent
  audit-level failures: schema-internal omission (C-24), evidence absence on FAIL (this
  field), verdict granularity collapse (C-19). An executor MUST NOT conflate evidence
  absence with structural omission or verdict granularity collapse.*
- Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
  specific informal references FAILS this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** An executor SHALL issue an individual inline verdict for each
step before the aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 audit field's violation type (left neighbor, site 5) is evidence
  absence on FAIL — a FAIL verdict that names no specific findings. This field's violation
  type is verdict granularity collapse: per-step verdicts are merged into a single
  aggregate before the FAIL branch. C-13 FAILS on what the FAIL entry contains; this
  field FAILS on whether each step receives its own verdict line before the aggregate.
  Both fail at the audit level; each requires a different correction: C-13 requires
  listing the informal references; this field requires issuing per-step inline verdicts.
  An executor MUST NOT conflate these two audit-level failure modes.*
- Compliance failure condition (C-27 extension): A single aggregate verdict without
  per-step inline verdicts FAILS the C-25 format requirement at this field.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]
