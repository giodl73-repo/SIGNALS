# flow-throttle Variate — Round 13
**Date:** 2026-03-15
**Rubric:** v13 (C-01 through C-39, N_essential=5, N_recommended=3, N_aspirational=31)
**Baseline ceiling:** R12 V-05 (passes C-01 through C-37 under v13 rubric)

---

## State Analysis: What R12 Established vs. What R13 Must Add

**R12 V-05 coverage under v13 (confirmed):**
- C-01 through C-37: all pass
- C-36: all four multi-adjacent sites (2, 3, 4, 5) name both neighbors in `*Violation type:*`
- C-37: PRECISION-SITE INVENTORY `C-27 hierarchy` column uses exact C-31 format
  (`primary (C-27):` / `extension (C-27 extension):`)

**v13 gaps in R12 V-05:**

**C-38 failure (four sites):** The four multi-adjacent `*Violation type:*` fields at sites
2, 3, 4, and 5 each name both immediate sequence neighbors and establish the distinguishing
contrast (C-36 passes). None include an explicit non-conflation count directive. C-38
requires the phrase "An executor MUST NOT conflate these N failure modes" (or equivalent)
to appear in the `*Violation type:*` field or an immediately adjacent enforcement note,
converting the contrast from implicit-by-enumeration to explicit-by-directive. Contrast
that is present by enumeration but absent as a count directive satisfies C-36 and fails
C-38.

**C-39 failure:** The PRECISION-SITE INVENTORY includes a `C-27 hierarchy` column with
values in the exact C-31 parenthetical format (satisfying C-37). No verification obligation
accompanies the column. C-39 requires an explicit instruction directing the executor to
confirm that each definition block's label matches the inventory's `C-27 hierarchy` value
for that site. An inventory that records hierarchy labels without a closing verification
obligation — leaving the inventory value as a record rather than a compliance target —
satisfies C-37 and fails C-39.

---

## Round 13 Variation Map

| Variation | Axes | C-38 | C-39 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | Output format: non-conflation count directive at all 4 multi-adjacent sites | PASS | FAIL | 109/110 |
| V-02 | Lifecycle emphasis: inventory verification obligation on C-27 hierarchy column | FAIL | PASS | 109/110 |
| V-03 | Role sequence control: Load-shape Analyst runs Step 2G before Cascade Analyst runs Step 2E; no C-38 or C-39 changes | FAIL | FAIL | 108/110 |
| V-04 | Combined: C-38 count directive (V-01) + C-39 verification obligation (V-02) | PASS | PASS | 110/110 |
| V-05 | Combined + phrasing register: V-04 + formal SHALL/MUST/PROHIBITED throughout | PASS | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs R12 baseline): Does adding "An executor MUST NOT conflate these 2 failure
modes." to each multi-adjacent `*Violation type:*` field satisfy C-38 without affecting
C-39? Hypothesis: yes — C-38 governs definition-site text at `*Violation type:*` fields;
C-39 governs the inventory table annotation. The two criteria modify separate locations.
Predicted: C-38 PASS, C-39 FAIL.

Q2 (V-02 vs R12 baseline): Does adding the verification obligation footer to the
PRECISION-SITE INVENTORY satisfy C-39 without affecting C-38? Hypothesis: yes — the
`*Violation type:*` fields in definition blocks retain all-neighbor contrast without count
directives; no count directive is added. Predicted: C-38 FAIL, C-39 PASS.

Q3 (V-03 control): Does role-sequence reordering affect C-38 or C-39? Hypothesis: no —
both criteria are structural and location-specific. C-38 governs text at definition-site
`*Violation type:*` fields; C-39 governs the inventory annotation. Neither depends on
analyst assignment order. Both still fail.

Q4 (V-04): Does combining V-01's count directive with V-02's verification obligation
achieve both C-38 and C-39 with no interaction effects? Hypothesis: yes — V-01 modifies
four `*Violation type:*` fields in definition blocks; V-02 modifies the inventory table
annotation. Changes are orthogonal and do not touch each other's location.

Q5 (V-05): Does formal register throughout V-04 elevate without regressions? Hypothesis:
yes — formal register affects enforcement language in prohibition blocks and audit headers;
count directive content and verification obligation wording are structurally intact and the
register change does not alter their location or criterion-satisfying content.

---

## V-01 — Single Axis: Output Format (non-conflation count directive — C-38)

**Axis:** Output format — each multi-adjacent `*Violation type:*` field (sites 2, 3, 4,
and 5) is extended to include an explicit non-conflation count directive: "An executor
MUST NOT conflate these 2 failure modes." All-neighbor contrast from R12 V-05 is
preserved at all four sites. The PRECISION-SITE INVENTORY retains R12 V-05's format
without a verification obligation (C-39 not targeted).

**Hypothesis:** C-38 is satisfied by the count directive at each of the four multi-adjacent
sites. C-39 still fails because no verification obligation accompanies the C-27 hierarchy
column in the inventory. Predicted: C-38 PASS, C-39 FAIL. Composite = 109/110.

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
states the specific failure at each site, matching the domain-specific text that will
appear at each definition site. The `C-27 hierarchy` column uses the C-31 parenthetical
labeling format — `primary (C-27):` for the first site and `extension (C-27 extension):`
for all subsequent sites — making the C-31 labeling structure auditable from this
inventory without opening each definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

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
  - *Violation type: vague label substituted for numeric value (e.g., "limited",
    "throttled" in place of "1,200 req/min"). Site 1 has one immediate right neighbor
    (site 2: Load-shape verdict). Single-adjacency — C-36 and C-38 do not apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead
    of a specific number-with-unit fails this column's precision requirement.

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
    structurally depends on it. Three distinct failures at the same registry level, three
    different corrections: supply the number (Limit), move the classification act to
    registration time (this column), name the parameter (TABLE F). An executor MUST NOT
    conflate these 2 failure modes.*
  - Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry
    left blank or deferred ("see Step 2G", "analyzed below") fails the registration-time
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

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence.

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
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36):
  the `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred
  verdict token — the classification act is placed at the wrong moment, routed to a
  downstream section rather than recorded at registration time. The STEP 4 C-24 finding
  schema's violation type (right neighbor, site 4) is a structural omission — a labeled
  slot position within a single finding entry is left empty or merged with adjacent
  content. This column's violation type is neither: the value is a string identifier, not
  a number; there is no timing constraint; and the failure is not about a slot within a
  structured finding. The failure is category substitution — naming the class of action
  where the specific deployable parameter name is required. An executor MUST NOT conflate
  these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of
  action rather than a specific parameter identifier fails this column's precision
  requirement.

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
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F
  `Setting or API parameter`'s violation type (left neighbor, site 3) is category
  substitution — a task-class label occupies the parameter field. The STEP 4 C-13 audit
  FAIL field's violation type (right neighbor, site 5) is evidence absence — a FAIL
  verdict is issued at the aggregate level without enumerating the specific informal
  references found. This schema's violation type is distinct from both: the failure is not
  a wrong category in a parameter field and not an absent evidence list at aggregate level
  — a labeled slot position within a single finding entry is left empty or merged with
  adjacent content. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any
  named slot position — or presents findings as free-form prose — fails the identification
  schema.

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
  site 4) is structural omission within a finding entry — a labeled slot is missing or
  collapsed into prose. The STEP 4 C-19 audit FAIL field's violation type (right neighbor,
  site 6) is verdict granularity collapse — individual step verdicts are merged into a
  single aggregate without per-step assessments. This audit field's violation type is
  distinct from both: the failure is not within a single finding (C-24's domain) and not
  about per-step verdict granularity (C-19's domain). The failure is at the aggregate
  reporting level — the FAIL verdict is correctly present but the specific informal
  references are not enumerated. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does
  not enumerate specific informal references fails this audit field.

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
  absence on FAIL — a FAIL verdict that correctly fires but names no specific findings.
  This field's violation type is verdict granularity collapse: per-step verdicts are
  merged into a single aggregate before the FAIL branch. C-13 fails on what the FAIL
  entry contains; C-19 fails on whether each step receives its own verdict line. Both
  fail at the audit level; each requires a different correction. Site 6 has one immediate
  neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior
  appeared in the same step]

---

## V-02 — Single Axis: Lifecycle Emphasis (inventory verification obligation — C-39)

**Axis:** Lifecycle emphasis — the PRECISION-SITE INVENTORY is extended with an explicit
verification obligation on the `C-27 hierarchy` column, directing the executor to confirm
that each definition block's label matches the inventory value before producing that
block. The `*Violation type:*` fields in definition blocks retain R12 V-05's all-neighbor
contrast form without count directives (C-38 not targeted).

**Hypothesis:** C-39 is satisfied by the verification obligation in the inventory. C-38
still fails because no non-conflation count directive appears at any multi-adjacent
definition site. Predicted: C-38 FAIL, C-39 PASS. Composite = 109/110.

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

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every
precision-requiring site in this prompt is enumerated below in document order. The
`Violation type` column states the specific failure at each site, matching the
domain-specific text that will appear at each definition site. The `C-27 hierarchy`
column uses the C-31 parenthetical labeling format — `primary (C-27):` for the first site
and `extension (C-27 extension):` for all subsequent sites — making the C-31 labeling
structure auditable from this inventory without opening each definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types match the domain-specific text at each
downstream definition site. An executor SHALL verify that the label at each definition
block matches the `C-27 hierarchy` value in this row before producing that definition
block — the inventory value is a compliance target, not a record.)*

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
  - *Violation type: vague label substituted for numeric value (e.g., "limited",
    "throttled" in place of "1,200 req/min"). Site 1 has one immediate right neighbor
    (site 2: Load-shape verdict). Single-adjacency — C-36 and C-38 do not apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead
    of a specific number-with-unit fails this column's precision requirement.

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
    structurally depends on it. Three distinct failures at the same registry level, three
    different corrections: supply the number (Limit), move the classification act to
    registration time (this column), name the parameter (TABLE F).*
  - Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry
    left blank or deferred ("see Step 2G", "analyzed below") fails the registration-time
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

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence.

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
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36):
  the `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred
  verdict token — the classification act is placed at the wrong moment, routed to a
  downstream section rather than recorded at registration time. The STEP 4 C-24 finding
  schema's violation type (right neighbor, site 4) is a structural omission — a labeled
  slot position within a single finding entry is left empty or merged with adjacent
  content. This column's violation type is neither: the value is a string identifier, not
  a number; there is no timing constraint; and the failure is not about a slot within a
  structured finding. The failure is category substitution — naming the class of action
  where the specific deployable parameter name is required.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of
  action rather than a specific parameter identifier fails this column's precision
  requirement.

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
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F
  `Setting or API parameter`'s violation type (left neighbor, site 3) is category
  substitution — a task-class label occupies the parameter field. The STEP 4 C-13 audit
  FAIL field's violation type (right neighbor, site 5) is evidence absence — a FAIL
  verdict is issued at the aggregate level without enumerating the specific informal
  references found. This schema's violation type is distinct from both: the failure is not
  a wrong category in a parameter field and not an absent evidence list at aggregate level
  — a labeled slot position within a single finding entry is left empty or merged with
  adjacent content.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any
  named slot position — or presents findings as free-form prose — fails the identification
  schema.

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
  site 4) is structural omission within a finding entry — a labeled slot is missing or
  collapsed into prose. The STEP 4 C-19 audit FAIL field's violation type (right neighbor,
  site 6) is verdict granularity collapse — individual step verdicts are merged into a
  single aggregate without per-step assessments. This audit field's violation type is
  distinct from both: the failure is not within a single finding (C-24's domain) and not
  about per-step verdict granularity (C-19's domain). The failure is at the aggregate
  reporting level — the FAIL verdict is correctly present but the specific informal
  references are not enumerated.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does
  not enumerate specific informal references fails this audit field.

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
  absence on FAIL — a FAIL verdict that correctly fires but names no specific findings.
  This field's violation type is verdict granularity collapse: per-step verdicts are
  merged into a single aggregate before the FAIL branch. C-13 fails on what the FAIL
  entry contains; C-19 fails on whether each step receives its own verdict line. Both
  fail at the audit level; each requires a different correction. Site 6 has one immediate
  neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior
  appeared in the same step]

---

## V-03 — Single Axis: Role Sequence (control — no C-38 or C-39 changes)

**Axis:** Role sequence — two analyst roles are assigned. Load-shape Analyst owns Step 2G
and runs it immediately after the tier registry closes. Rate Limit Analyst owns Steps 2A,
2B, 2C, 2D, 2E, 2F, 2H and runs after Load-shape Analyst completes 2G. This reverses
the default 2E-before-2G ordering. No count directives added (C-38 not targeted). No
inventory verification obligation added (C-39 not targeted).

**Hypothesis:** Role-sequence reordering does not affect C-38 or C-39. Both criteria
govern structural text at specific locations (definition-site fields and inventory
annotation) that are unaffected by analyst assignment order. Both still fail. Predicted:
C-38 FAIL, C-39 FAIL. Composite = 108/110.

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

Two analysts operate in sequence:

**Load-shape Analyst** — owns Step 2G. Runs immediately after TABLE A is complete.
Responsible for load-shape comparison using TABLE A's registered Limit values and
Load-shape verdict column.

**Rate Limit Analyst** — owns Steps 2A, 2B, 2C, 2D, 2E, 2F, 2H. Runs after Load-shape
Analyst completes Step 2G. Responsible for backpressure trace, UX catalog, burst paths,
risk ranking, cascade scenario, retry-after assessment, and mitigation registry.

You are a Connectors / Power Automate throughput domain expert serving in both roles.
Treat the stated request volume as 1x nominal; also analyze at 2x and 5x. The tables
below are the primary output. Fill every cell. Produce sections in the order shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37. Every precision-requiring
site in this prompt is enumerated below in document order. The `Violation type` column
states the specific failure at each site, matching the domain-specific text that will
appear at each definition site. The `C-27 hierarchy` column uses the C-31 parenthetical
labeling format — `primary (C-27):` for the first site and `extension (C-27 extension):`
for all subsequent sites — making the C-31 labeling structure auditable from this
inventory without opening each definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types match the domain-specific text at each
downstream definition site — enabling inventory-vs-definition verification.)*

---

**STEP 1 — TIER REGISTRY**

*(Load-shape Analyst: complete TABLE A entirely, then proceed immediately to Step 2G
before Rate Limit Analyst opens any other Step 2 section.)*

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
  - *Violation type: vague label substituted for numeric value (e.g., "limited",
    "throttled" in place of "1,200 req/min"). Site 1 has one immediate right neighbor
    (site 2: Load-shape verdict). Single-adjacency — C-36 and C-38 do not apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead
    of a specific number-with-unit fails this column's precision requirement.

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
    structurally depends on it. Three distinct failures at the same registry level, three
    different corrections: supply the number (Limit), move the classification act to
    registration time (this column), name the parameter (TABLE F).*
  - Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry
    left blank or deferred ("see Step 2G", "analyzed below") fails the registration-time
    classification requirement and invalidates Step 2G's numeric comparison.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

*(Do not begin any Step 2 section until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers from TABLE A throughout.

**Load-shape Analyst proceeds to Step 2G now. Rate Limit Analyst proceeds to Step 2A
after Step 2G is complete.**

---

**Step 2G — LOAD SHAPE COMPARISON** *(Load-shape Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs at identical total count.

*(Load-shape Analyst complete. Rate Limit Analyst proceeds below.)*

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)** *(Rate Limit Analyst)*

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

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence.

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
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36):
  the `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred
  verdict token — the classification act is placed at the wrong moment. The STEP 4 C-24
  finding schema's violation type (right neighbor, site 4) is a structural omission — a
  labeled slot position within a single finding entry is left empty or merged with adjacent
  content. This column's violation type is neither: the failure is category substitution
  — naming the class of action where the specific deployable parameter name is required.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of
  action rather than a specific parameter identifier fails this column's precision
  requirement.

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
Self-contained block. Complete after Stage 2.

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
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F
  `Setting or API parameter`'s violation type (left neighbor, site 3) is category
  substitution — a task-class label occupies the parameter field. The STEP 4 C-13 audit
  FAIL field's violation type (right neighbor, site 5) is evidence absence — a FAIL
  verdict is issued without enumerating the specific informal references. This schema's
  violation type is distinct from both — a labeled slot position within a single finding
  entry is left empty or merged with adjacent content.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any
  named slot position fails the identification schema.

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
  site 4) is structural omission within a finding entry. The STEP 4 C-19 audit FAIL
  field's violation type (right neighbor, site 6) is verdict granularity collapse. This
  audit field's violation type is distinct from both — the FAIL verdict is correctly
  present but specific informal references are not enumerated.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does
  not enumerate specific informal references fails this audit field.

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
  absence on FAIL. This field's violation type is verdict granularity collapse. C-13
  fails on what the FAIL entry contains; C-19 fails on whether each step receives its own
  verdict line. Site 6 has one immediate neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior
  appeared in the same step]

---

## V-04 — Combined: C-38 + C-39

**Axis:** Combined — V-01's non-conflation count directive at all four multi-adjacent
sites (C-38) plus V-02's inventory verification obligation on the C-27 hierarchy column
(C-39). V-01 modifies `*Violation type:*` field text at four definition sites. V-02
modifies the PRECISION-SITE INVENTORY table annotation. The changes are orthogonal.

**Hypothesis:** C-38 is satisfied by the count directive at all four multi-adjacent sites.
C-39 is satisfied by the verification obligation in the inventory. No interaction effects.
Predicted: C-38 PASS, C-39 PASS. Composite = 110/110.

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

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every
precision-requiring site in this prompt is enumerated below in document order. The
`Violation type` column states the specific failure at each site, matching the
domain-specific text that will appear at each definition site. The `C-27 hierarchy`
column uses the C-31 parenthetical labeling format — `primary (C-27):` for the first site
and `extension (C-27 extension):` for all subsequent sites — making the C-31 labeling
structure auditable from this inventory without opening each definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types match the domain-specific text at each
downstream definition site. An executor SHALL verify that the label at each definition
block matches the `C-27 hierarchy` value in this row before producing that definition
block — the inventory value is a compliance target, not a record.)*

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
  - *Violation type: vague label substituted for numeric value (e.g., "limited",
    "throttled" in place of "1,200 req/min"). Site 1 has one immediate right neighbor
    (site 2: Load-shape verdict). Single-adjacency — C-36 and C-38 do not apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead
    of a specific number-with-unit fails this column's precision requirement.

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
    structurally depends on it. Three distinct failures at the same registry level, three
    different corrections: supply the number (Limit), move the classification act to
    registration time (this column), name the parameter (TABLE F). An executor MUST NOT
    conflate these 2 failure modes.*
  - Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry
    left blank or deferred ("see Step 2G", "analyzed below") fails the registration-time
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

At least one row. If no unprotected path exists, row 1 states the conclusion with at
least two named controls as evidence.

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
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36):
  the `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred
  verdict token — the classification act is placed at the wrong moment, routed to a
  downstream section rather than recorded at registration time. The STEP 4 C-24 finding
  schema's violation type (right neighbor, site 4) is a structural omission — a labeled
  slot position within a single finding entry is left empty or merged with adjacent
  content. This column's violation type is neither: the value is a string identifier, not
  a number; there is no timing constraint; and the failure is not about a slot within a
  structured finding. The failure is category substitution — naming the class of action
  where the specific deployable parameter name is required. An executor MUST NOT conflate
  these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of
  action rather than a specific parameter identifier fails this column's precision
  requirement.

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
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F
  `Setting or API parameter`'s violation type (left neighbor, site 3) is category
  substitution — a task-class label occupies the parameter field. The STEP 4 C-13 audit
  FAIL field's violation type (right neighbor, site 5) is evidence absence — a FAIL
  verdict is issued at the aggregate level without enumerating the specific informal
  references found. This schema's violation type is distinct from both: the failure is not
  a wrong category in a parameter field and not an absent evidence list at aggregate level
  — a labeled slot position within a single finding entry is left empty or merged with
  adjacent content. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any
  named slot position — or presents findings as free-form prose — fails the identification
  schema.

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
  site 4) is structural omission within a finding entry — a labeled slot is missing or
  collapsed into prose. The STEP 4 C-19 audit FAIL field's violation type (right neighbor,
  site 6) is verdict granularity collapse — individual step verdicts are merged into a
  single aggregate without per-step assessments. This audit field's violation type is
  distinct from both: the failure is not within a single finding (C-24's domain) and not
  about per-step verdict granularity (C-19's domain). The failure is at the aggregate
  reporting level — the FAIL verdict is correctly present but the specific informal
  references are not enumerated. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does
  not enumerate specific informal references fails this audit field.

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
  absence on FAIL — a FAIL verdict that correctly fires but names no specific findings.
  This field's violation type is verdict granularity collapse: per-step verdicts are
  merged into a single aggregate before the FAIL branch. C-13 fails on what the FAIL
  entry contains; C-19 fails on whether each step receives its own verdict line. Both
  fail at the audit level; each requires a different correction. Site 6 has one immediate
  neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior
  appeared in the same step]

---

## V-05 — Combined + Phrasing Register (C-38 + C-39 + Formal SHALL/MUST)

**Axis:** Combined + phrasing register — V-04 (C-38 count directives + C-39 verification
obligation) with formal SHALL/MUST/PROHIBITED register applied throughout. Imperative
framing upgrades all enforcement language: "Do not" becomes "SHALL NOT", "Complete" at
phase boundaries becomes "SHALL complete", "Return to" becomes "SHALL return to",
REGISTRY GAP and standing reminder headers add explicit PROHIBITED markers.

**Hypothesis:** C-38 and C-39 are satisfied identically to V-04; formal register
strengthens enforcement signal without altering the structural locations of count
directives or verification obligation. No regressions on prior criteria. Predicted:
C-38 PASS, C-39 PASS. Composite = 110/110.

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
prose cannot represent with the same auditability. Every cell SHALL be filled. Produce
sections in the order shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every
precision-requiring site in this prompt is enumerated below in document order. The
`Violation type` column states the specific failure at each site, matching the
domain-specific text that SHALL appear at each definition site. The `C-27 hierarchy`
column uses the C-31 parenthetical labeling format — `primary (C-27):` for the first site
and `extension (C-27 extension):` for all subsequent sites — making the C-31 labeling
structure auditable from this inventory without opening each definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types match the domain-specific text at each
downstream definition site. An executor SHALL verify that the label at each definition
block matches the `C-27 hierarchy` value in this row before producing that definition
block — the inventory value is a compliance target, not a record. Non-compliance with a
definition block label SHALL be corrected before the block is produced.)*

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal — the volume nobody tested.)*

An executor SHALL complete Step 1 in full before opening any Step 2 section. Step 1 is
the perspective-separated enumeration phase: all tier discovery, numeric limits, and
load-shape classification SHALL occur here. Step 2 SHALL contain caller behavior and
backpressure analysis only.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during
Step 2 are scope violations — evidence that the enumeration phase was incomplete.
PROHIBITED: assigning a new T-NN during Step 2 as a fill-in step. An executor SHALL
return to TABLE A, register the tier with all columns filled, and restart from the point
of discovery. This prohibition is restated at each Step 2 section where mid-phase
discovery could occur.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and use verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited",
    "throttled" in place of "1,200 req/min"). Site 1 has one immediate right neighbor
    (site 2: Load-shape verdict). Single-adjacency — C-36 and C-38 SHALL NOT apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead
    of a specific number-with-unit fails this column's precision requirement.

- `STATUS Nx` — OK / HIT / SAT; SHALL shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential
  and mechanism explanation.

  **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — DEFERRAL PROHIBITED:**

  An executor SHALL complete this column at registration time. PROHIBITED: deferring
  load-shape classification to the LOAD SHAPE COMPARISON section (Step 2G).

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
    structurally depends on it. Three distinct failures at the same registry level, three
    different corrections: supply the number (Limit), move the classification act to
    registration time (this column), name the parameter (TABLE F). An executor MUST NOT
    conflate these 2 failure modes.*
  - Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry
    left blank or deferred ("see Step 2G", "analyzed below") SHALL be treated as a
    registration-time compliance failure that invalidates Step 2G's numeric comparison.

- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

*(An executor SHALL NOT begin STEP 2 until TABLE A is complete with all columns filled.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. An executor SHALL use T-NN identifiers from
TABLE A throughout all sections below.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second
throttle window into a 10-minute retry storm — invisible where the connector layer is
mocked.)*

**Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An
executor SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A, register
the tier with all required columns, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

Minimum two hops. `Mechanism` SHALL be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier SHALL be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test
has ever run at the volume where it fires.)*

**Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An
executor SHALL return to TABLE A.

At least one row SHALL be present. If no unprotected path exists, row 1 SHALL state the
conclusion with at least two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

Rank all TABLE A tiers by business risk, highest to lowest. Every tier SHALL appear. One
sentence per tier with rationale. For the top-ranked tier, reference `Failure visibility
window` and `Recovery time` from TABLE A.

---

**Step 2E — CASCADE SCENARIO**

**Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs throughout. State
each causal link. Minimum three tiers, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the
failure mode SHALL be named precisely — retry storm (exponential backoff) vs. quota
exhaustion (circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis that are not in TABLE A are scope violations. An
executor SHALL return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison SHALL differ in status at identical total count.

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
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36):
  the `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred
  verdict token — the classification act is placed at the wrong moment, routed to a
  downstream section rather than recorded at registration time. The STEP 4 C-24 finding
  schema's violation type (right neighbor, site 4) is a structural omission — a labeled
  slot position within a single finding entry is left empty or merged with adjacent
  content. This column's violation type is neither: the value is a string identifier, not
  a number; there is no timing constraint; and the failure is not about a slot within a
  structured finding. The failure is category substitution — naming the class of action
  where the specific deployable parameter name is required. An executor MUST NOT conflate
  these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of
  action rather than a specific parameter identifier SHALL be treated as a precision
  failure for this column.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer; the load test running at 10% of production concurrency.)*

Execute two stages. Stage 1 pre-loads artifact names; Stage 2 uses them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts SHALL be named with structural properties before Stage 2
opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

An executor SHALL state "Stage 1 complete" before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. An executor SHALL complete this block after Stage 2. Each
downstream section SHALL receive an individual verdict on a distinct verdict line, with
evidence on a distinct evidence line.

**C-24 format requirement:** Each field entry SHALL use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list SHALL populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F
  `Setting or API parameter`'s violation type (left neighbor, site 3) is category
  substitution — a task-class label occupies the parameter field. The STEP 4 C-13 audit
  FAIL field's violation type (right neighbor, site 5) is evidence absence — a FAIL
  verdict is issued at the aggregate level without enumerating the specific informal
  references found. This schema's violation type is distinct from both: the failure is not
  a wrong category in a parameter field and not an absent evidence list at aggregate level
  — a labeled slot position within a single finding entry is left empty or merged with
  adjacent content. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any
  named slot position — or presents findings as free-form prose — SHALL be treated as a
  schema compliance failure.

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
  site 4) is structural omission within a finding entry — a labeled slot is missing or
  collapsed into prose. The STEP 4 C-19 audit FAIL field's violation type (right neighbor,
  site 6) is verdict granularity collapse — individual step verdicts are merged into a
  single aggregate without per-step assessments. This audit field's violation type is
  distinct from both: the failure is not within a single finding (C-24's domain) and not
  about per-step verdict granularity (C-19's domain). The failure is at the aggregate
  reporting level — the FAIL verdict is correctly present but specific informal references
  are not enumerated. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does
  not enumerate specific informal references SHALL be treated as an audit field failure.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** An executor SHALL issue an individual inline verdict for
each step before the aggregate failure list.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: the C-13 audit field's violation type (left neighbor, site 5) is evidence
  absence on FAIL — a FAIL verdict that correctly fires but names no specific findings.
  This field's violation type is verdict granularity collapse: per-step verdicts are
  merged into a single aggregate before the FAIL branch. C-13 fails on what the FAIL
  entry contains; C-19 fails on whether each step receives its own verdict line. Both
  fail at the audit level; each requires a different correction. Site 6 has one immediate
  neighbor — C-36 and C-38 SHALL NOT apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts SHALL be treated as a C-25 format failure.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior
  appeared in the same step]
