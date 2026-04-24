# flow-throttle Variate — Round 11 (v11 Rubric)
**Date:** 2026-03-15
**Rubric:** v11 (C-01 through C-35, N_essential=5, N_recommended=3, N_aspirational=27)
**Baseline ceiling:** R10 V-05 (110/110 under v10 rubric; confirmed passes C-01 through C-33)

---

## State Analysis: What R10 V-05 Has vs. What R11 Must Add

**R10 V-05 coverage under v11 (confirmed):**
- C-01 through C-30: all pass (verified through R10)
- C-31: passes — TABLE A `Limit` column carries `(C-27):` primary label (first in document
  order); all subsequent failure conditions carry `(C-27 extension):` labels
- C-32: passes — each extension site has a `*Violation type:*` field naming its specific
  precision failure independently legible without cross-reference
- C-33: passes — PRECISION-SITE INVENTORY section appears before TABLE A, enumerating
  six precision-requiring sites

**v11 gaps in R10 V-05:**

**C-34 failure:** R10 V-05's `*Violation type:*` fields are independently legible (C-32
PASS) but do not satisfy C-34's adjacency-contrast requirement. The `Load-shape verdict`
field says "structurally distinct from the Limit column's vague-label failure (imprecise
placeholder vs. absent classification)" — this names the adjacent column and gestures at a
distinction, but does not quote or name the adjacent site's violation type as the explicit
starting point of the contrast. C-34 requires that when two adjacent sites could be
confused, each field names or quotes the adjacent site's failure mode before establishing
the distinguishing characteristic. "Structurally distinct from X's failure" is an assertion
of distinctness; C-34 requires an explicit comparative construction that quotes X's failure
mode and then specifies what makes the current site different. TABLE F contrasts with both
`Limit` and `Load-shape verdict` using the same "structurally distinct from" pattern — both
cite adjacent columns but neither produces the explicit cross-site contrast C-34 requires.

**C-35 failure:** R10 V-05's PRECISION-SITE INVENTORY includes a "Violation type:" bullet
annotation after the hierarchy label for each site. This gets close but does not satisfy
C-35. C-35 requires the inventory to be a self-contained preview of the enforcement logic
at each definition site — the violation types must be structured as a parallel column or
field that a reader can scan independently to verify which specific failure each site
prevents, matching the domain-specific text at each downstream `*Violation type:*` field.
R10 V-05's inventory embeds the violation type as a dash-prefixed annotation on the same
line as hierarchy information, making the inventory a labeled roster with annotations rather
than a structured preview table. C-35 is satisfied when the inventory's violation type entry
is visually and structurally parallel to the downstream field — enabling an auditor to
confirm the match by scanning the inventory column alone without reconstructing each site's
definition block.

---

## Round 11 Variation Map

| Variation | Axes | C-34 | C-35 | Predicted composite |
|-----------|------|------|------|---------------------|
| V-01 | Output format: `*Violation type:*` fields quote adjacent site's failure before establishing current site's distinguishing characteristic | PASS | FAIL | 109/110 |
| V-02 | Lifecycle emphasis: PRECISION-SITE INVENTORY restructured as four-column table with standalone `Violation type` column matching downstream definition text | FAIL | PASS | 109/110 |
| V-03 | Role sequence: Cascade Analyst runs Steps 2E–2G before Rate Limit Analyst runs 2H; control — no C-34 or C-35 changes | FAIL | FAIL | 108/110 |
| V-04 | Combined: output format + lifecycle emphasis (C-34 + C-35) | PASS | PASS | 110/110 |
| V-05 | Combined: output format + lifecycle emphasis + phrasing register (formal SHALL/MUST/PROHIBITED throughout, C-34 + C-35 + maximum enforcement formality) | PASS | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs R10 baseline): Does adding explicit cross-site contrast to each `*Violation
type:*` field — quoting the adjacent site's failure mode before naming the current site's
distinguishing characteristic — satisfy C-34 without affecting C-35? Hypothesis: yes —
C-34 is a field-content criterion: it governs what the `*Violation type:*` text says
relative to adjacent sites. C-35 governs the inventory table structure. These sites are
separate and the inventory format is unchanged in V-01. Predicted: C-34 PASS, C-35 FAIL.

Q2 (V-02 vs R10 baseline): Does restructuring the PRECISION-SITE INVENTORY as a four-
column table where the fourth column is `Violation type` (standalone, matching downstream
definition text) satisfy C-35 without affecting C-34? Hypothesis: yes — C-35 is an
inventory-structure criterion; the `*Violation type:*` fields at definition sites are
unchanged from R10 V-05 and retain their "structurally distinct from" form that passes
C-32 but fails C-34. Predicted: C-34 FAIL, C-35 PASS.

Q3 (V-03 control): Does changing the role sequence have any effect on C-34 or C-35?
Hypothesis: no — both criteria are structural: C-34 governs violation-type contrast in
definition blocks; C-35 governs inventory format. Role sequence governs which analyst
produces which output section. No content in the `*Violation type:*` fields or in the
PRECISION-SITE INVENTORY changes with role reordering. Both still fail.

Q4 (V-04): Does combining V-01's contrast language with V-02's inventory restructuring
achieve both C-34 and C-35 with no interaction effects? Hypothesis: yes — the changes
are orthogonal: V-01 modifies `*Violation type:*` field text; V-02 modifies the inventory
table structure. Neither change affects the other. Both should PASS simultaneously.

Q5 (V-05): Does adding formal prescriptive register (SHALL/MUST/PROHIBITED) throughout
V-04 elevate the output without regressions? Hypothesis: yes — formal register does not
alter the content of `*Violation type:*` fields or inventory structure; it affects the
enforcement language in prohibitions, failure conditions, and audit blocks, strengthening
the output without creating conflicts.

---

## V-01 — Single Axis: Output Format (violation-type contrast — C-34)

**Axis:** Output format — each `*Violation type:*` field at C-30 extension sites quotes
the adjacent site's failure mode first, then names the current site's distinguishing
characteristic. This is the C-34 contrast pattern: "TABLE A `Limit`'s failure is [X] —
the current site's failure is [Y], which differs because [Z]." The PRECISION-SITE INVENTORY
retains R10 V-05's bullet-annotation format without a standalone Violation type column.

**Hypothesis:** C-34 is satisfied by the explicit cross-site contrast language in the
`*Violation type:*` fields. C-35 still fails because the inventory does not have a
standalone Violation type column matching downstream definition text. Predicted:
C-34 PASS, C-35 FAIL. Composite = 109/110.

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
comparing this list against the prompt's definition sections.)*

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

*(Six precision-requiring sites. Site 1 is primary; Sites 2–6 are extensions.)*

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
    in place of "1,200 req/min"). Adjacent column contrast: TABLE A `Load-shape verdict`'s
    failure is a deferred verdict token — routing the classification to Step 2G rather than
    stating SHAPE-NEUTRAL/SHAPE-SENSITIVE at registration time. These two adjacent columns
    fail in different dimensions: the `Limit` column fails on value precision (the number
    is missing or imprecise); the `Load-shape verdict` column fails on classification
    timing (the verdict is present in kind but absent at the required moment). A vague
    Limit entry and a deferred verdict entry are both incomplete, but an entry that says
    "see Step 2G" is not the same failure as an entry that says "limited".*
  - Compliance failure condition (C-27): An entry that uses a vague label instead of a
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

  - *Violation type: deferred verdict token — routing the SHAPE-NEUTRAL/SHAPE-SENSITIVE
    classification to Step 2G rather than recording it at registration time. Adjacent column
    contrast: the `Limit` column's failure is a vague-label substitution — an imprecise
    placeholder where a measured number is required. The `Load-shape verdict` failure is
    structurally different: the verdict category is known (SHAPE-NEUTRAL or SHAPE-SENSITIVE)
    but the executor routes the act of stating it to a later section. A blank Limit entry
    and a "see Step 2G" verdict entry are both defective, but the Limit failure is content
    absence; the Load-shape verdict failure is classification deferral — a timing failure,
    not a value-precision failure.*
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

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). Adjacent column contrast: TABLE A
  `Limit`'s failure is a vague-label substitution — an imprecise placeholder for a measured
  numeric bound (e.g., "limited" in place of "500 req/min"). TABLE A `Load-shape verdict`'s
  failure is a deferred verdict token — routing the classification to Step 2G. This column's
  failure is different in kind from both: neither a missing number nor a timing deferral,
  but a category-for-identifier substitution — naming a class of action where a deployable
  configuration key is required. All three failures produce incomplete rows, but each fails
  on a different dimension: value precision (Limit), classification timing (Load-shape),
  parameter specificity (this column).*
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
  for this schema is omitting one or more of the three named slot positions. Adjacent
  contrast: TABLE A `Limit`'s failure is a vague-label substitution (imprecise placeholder
  for a number); TABLE F's failure is a category-for-parameter substitution (action label
  for a parameter identifier). This schema's failure is structural omission — a named slot
  position is left empty or collapsed into prose — not a vagueness or category failure.*
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
  the specific precision failure for this audit field is a FAIL verdict that names no
  specific evidence. Adjacent contrast: the C-24 finding schema's failure is structural
  omission (a required slot is missing from an individual finding); this audit field's
  failure is evidence absence (the FAIL verdict is present but the findings it covers are
  not enumerated). Both produce incomplete output but on different dimensions: the schema
  failure is within a single finding; the audit field failure is at the aggregate verdict
  level.*
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
  precision failure for this audit field is issuing one PASS/FAIL across all steps without
  individual step verdicts. Adjacent contrast: the C-13 audit field's failure is evidence
  absence on FAIL (informal references not enumerated); this field's failure is verdict
  granularity (per-step verdicts collapsed into an aggregate). Both fail at the audit level
  but on different dimensions: C-13 fails on what the FAIL entry contains; C-19 fails on
  whether individual items receive their own verdict before the aggregate.*
- Compliance failure condition (C-27 extension): An audit field that issues a single
  aggregate verdict without per-step inline verdicts fails the C-25 format requirement at
  this field.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

---

## V-02 — Single Axis: Lifecycle Emphasis (precision-site inventory restructured — C-35)

**Axis:** Lifecycle emphasis — the PRECISION-SITE INVENTORY is restructured as a four-
column table with a standalone `Violation type` column. Each row states the site, its
C-27 hierarchy position, the required precision, and the violation type — in a format that
is independently auditable without reconstructing downstream definition blocks. The
`*Violation type:*` fields in individual column and schema definitions retain the R10 V-05
form: each is independently legible (C-32 satisfied) but uses "structurally distinct from"
phrasing without explicitly quoting adjacent site failure modes (C-34 not targeted).

**Hypothesis:** C-35 is satisfied by the structured four-column table in the PRECISION-SITE
INVENTORY — the violation type column matches the downstream field text and makes the
inventory a self-contained enforcement preview rather than a roster with annotations. C-34
still fails because the `*Violation type:*` fields do not explicitly contrast with adjacent
sites. Predicted: C-34 FAIL, C-35 PASS. Composite = 109/110.

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

*(Required before any table is defined — C-33 + C-35. Every precision-requiring site is
enumerated below in document order. The `Violation type` column states the specific failure
at each site — matching the domain-specific text that will appear at each definition site,
making this inventory a self-contained preview of the enforcement logic rather than a site
roster. An auditor can verify C-30 compliance by scanning the table without inspecting
individual definition blocks.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|---------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | Primary | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | C-27 extension 1 | SHAPE-NEUTRAL or SHAPE-SENSITIVE stated at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording the verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | C-27 extension 2 | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | C-27 extension 3 | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | C-27 extension 4 | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | C-27 extension 5 | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types in the table above are the same domain-
specific text that appears in each site's co-located failure condition below — enabling
independent audit of inventory completeness.)*

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
    in place of "1,200 req/min") — the specific precision failure for this column is an
    imprecise placeholder where a measured number is required, which is structurally distinct
    from the Load-shape verdict column's routing failure (absent classification at
    registration time)*
  - Compliance failure condition (C-27): An entry that uses a vague label instead of a
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
  deferring the verdict to Step 2G creates a circular dependency.

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
the failure mode precisely — retry storm (exponential backoff) vs. quota exhaustion
(circuit breaker). If present, state whether callers respect it correctly.

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at
two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; which tiers HIT or SAT.
- **BURST arrival** — state burst fraction and peak per-second rate; which tiers HIT or SAT.

At least one numeric comparison where status differs between patterns.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

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

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                   |                                                |
| GAP-02 |                                           |           |                                                   |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**

**C-24 format requirement:** Each field entry must use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each finding MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose, structurally distinct from the Limit column's
  vague-label failure (imprecise content in a required field) and the Load-shape verdict's
  routing failure (absent classification)*
- Compliance failure condition (C-27 extension): A finding that omits any named slot
  position fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template above]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using three-slot template]

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
- If FAIL — unregistered tiers found: [list each: "[tier name] introduced at [step]"]

- *Violation type: binary FAIL flag without enumeration of specific informal references —
  structurally distinct from the finding schema's missing-slot failure (structural omission
  in a single finding)*
- Compliance failure condition (C-27 extension): A FAIL verdict that does not enumerate
  specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** Issue an individual inline verdict for each step.

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence — structurally
  distinct from the C-13 audit field's binary-flag failure (missing finding enumeration on
  FAIL)*
- Compliance failure condition (C-27 extension): An audit field that issues a single
  aggregate verdict without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe location]

---

## V-03 — Single Axis: Role Sequence (control — no C-34 or C-35 changes)

**Axis:** Role sequence — the Cascade Analyst runs Steps 2E and 2G before the Rate Limit
Analyst runs Step 2H. The standard sequence in R10 V-05 runs Rate Limit Analyst for all
of 2H immediately after 2G. This variation reorders the analytical roles so the cascade
and load-shape sections (2E, 2G) complete under the Cascade Analyst's ownership before
the Rate Limit Analyst produces the mitigation registry. The PRECISION-SITE INVENTORY
retains R10 V-05's bullet-annotation format; `*Violation type:*` fields retain the R10
V-05 "structurally distinct from" form. Neither C-34 nor C-35 is targeted.

**Hypothesis:** Role sequence changes have no effect on C-34 or C-35. C-34 is a
field-content criterion; C-35 is an inventory-structure criterion. Neither is governed by
which analyst produces which section. The reordering demonstrates that the structural
criteria are orthogonal to analytical role assignments. Predicted: C-34 FAIL, C-35 FAIL.
Composite = 108/110.

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

**Role assignments (this variation — cascade-first sequence):**
- **Rate Limit Analyst** (Connectors / Power Automate throughput domain expert):
  Steps 1, 2A, 2B, 2C, 2D, 2F, 2H, Step 3, Step 4
- **Cascade Analyst** (multi-tier failure propagation specialist):
  Steps 2E and 2G (runs between Step 2D and Step 2F in this variation)

The Cascade Analyst runs the cascade scenario and load-shape comparison before the Rate
Limit Analyst produces the mitigation registry. This sequencing ensures cascade findings
are visible to mitigation analysis — the Rate Limit Analyst sees the cascade chain before
writing MR entries.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33. Every precision-requiring site in this
prompt is enumerated below, in document order, with the site's position in the C-27
labeling hierarchy.)*

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

*(Six precision-requiring sites. Site 1 is primary; Sites 2–6 are extensions.)*

---

**STEP 1 — TIER REGISTRY** *(Rate Limit Analyst)*

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or
5x nominal.)*

Complete Step 1 in full before opening any Step 2 section.

**REGISTRY GAP protocol — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations. Return to TABLE A, register the tier with all columns filled, then
continue.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Limit (number + unit)` — a specific number with a unit.
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min") — the specific precision failure for this column is an
    imprecise placeholder where a measured number is required, which is structurally
    distinct from the Load-shape verdict column's routing failure (absent classification)*
  - Compliance failure condition (C-27): An entry using a vague label fails this column.

- `Load-shape verdict` — SHAPE-NEUTRAL or SHAPE-SENSITIVE with rate differential and
  mechanism explanation.

  Complete this column now, at registration time. Do not defer to Step 2G.

  **Escape-route story (C-23):** The "STATUS tracks volume thresholds" frame makes TABLE A
  appear to be a pure volume-threshold table, routing shape classification to Step 2G.

  **Structural rejection proof (C-26):** Load-shape classification requires the registered
  Limit value at registration time; Step 2G depends on per-tier verdicts to produce
  meaningful comparisons. Deferring creates a circular dependency.

  - *Violation type: deferred verdict token — the specific precision failure is routing
    the SHAPE-NEUTRAL/SHAPE-SENSITIVE classification to a downstream section rather than
    recording it at registration time, which is structurally distinct from the Limit
    column's vague-label failure (imprecise placeholder vs. absent classification)*
  - Compliance failure condition (C-27 extension): A blank or deferred Load-shape verdict
    entry fails the registration-time classification requirement.

*(Do not begin STEP 2 until TABLE A is complete.)*

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1. Use T-NN identifiers throughout.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)** *(Rate Limit Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers appearing
here not in TABLE A are scope violations. Return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)** *(Rate Limit Analyst)*

One row per Tier-ID from TABLE A. No tier may be omitted.

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

Rank all TABLE A tiers by business risk, highest to lowest. Every tier must appear.

---

**Step 2E — CASCADE SCENARIO** *(Cascade Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during cascade trace that are not in TABLE A are scope violations. Return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. Use Tier-IDs throughout.
Minimum three tiers, each step caused by the previous.

---

**Step 2G — LOAD SHAPE COMPARISON** *(Cascade Analyst)*

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
here not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's rate limit values and Load-shape verdict column, compare 1x nominal at
two arrival patterns. At least one numeric comparison where status differs.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT** *(Rate Limit Analyst)*

For the 1x binding constraint tier: is Retry-After present and surfaced? Name the failure
mode precisely if absent.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)** *(Rate Limit Analyst)*

*(Note: Cascade Analyst's Steps 2E and 2G complete first; Rate Limit Analyst writes MR
entries with the full cascade chain visible.)*

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

- *Violation type: category of action substituted for named parameter identifier — the
  specific precision failure for this column is naming a task class where a deployable
  parameter name is required, which is structurally distinct from the Limit column's
  vague-label failure (placeholder for a number) and the Load-shape verdict's routing
  failure (absent classification)*
- Compliance failure condition (C-27 extension): A row naming a category of action rather
  than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS** *(Rate Limit Analyst)*

Execute two stages. Stage 1 pre-loads artifact names; Stage 2 uses them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

State "Stage 1 complete" before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason | Test approach |
|--------|-------------------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                           |           |                   |               |
| GAP-02 |                                           |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION** *(Rate Limit Analyst)*

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**

**C-24 format requirement:** Two distinct labeled lines per field entry.

Each finding MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier — structurally distinct from the Limit column's
  vague-label failure and Load-shape verdict's routing failure*
- Compliance failure condition (C-27 extension): A finding omitting any named slot fails.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B): Verdict: [PASS / FAIL] | If FAIL — informal references: [three-slot template]
Step 2B (TABLE C): Verdict: [PASS / FAIL] | If FAIL — informal references: [three-slot template]
Step 2C (TABLE D): Verdict: [PASS / FAIL] | If FAIL — informal references: [three-slot template]
Step 2D (RISK RANKING): Verdict: [PASS / FAIL] | If FAIL — informal references: [three-slot template]
Step 2E (CASCADE): Verdict: [PASS / FAIL] | If FAIL — informal references: [three-slot template]
Step 2G (LOAD SHAPE): Verdict: [PASS / FAIL] | If FAIL — informal references: [three-slot template]
Unregistered tiers: Verdict: [PASS / FAIL] | If FAIL — list: [tier name + step]

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

## V-04 — Combined: Output Format + Lifecycle Emphasis (C-34 + C-35)

**Axes:** (1) Output format: `*Violation type:*` fields at each extension site explicitly
quote the adjacent site's failure mode before naming the current site's distinguishing
characteristic — same as V-01. (2) Lifecycle emphasis: PRECISION-SITE INVENTORY
restructured as a four-column table with a standalone `Violation type` column matching
downstream definition text — same as V-02. The two changes are applied simultaneously.

**Hypothesis:** V-04 is the v11 ceiling candidate. C-34 is satisfied by the explicit
cross-site contrast language in the `*Violation type:*` fields (V-01 axis). C-35 is
satisfied by the structured four-column inventory with standalone Violation type column
(V-02 axis). No interaction effects: V-01's changes are in column definition blocks;
V-02's changes are in the inventory table at the top of the prompt. Both should pass.
Predicted: C-34 PASS, C-35 PASS. Composite = 110/110.

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
nominal; also analyze at 2x and 5x.

The tables below are the primary output. Fill every cell. Produce sections in the order
shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35. Every precision-requiring site is
enumerated below in document order. The `Violation type` column states the specific failure
at each site, matching the domain-specific text that will appear at each definition site.
This makes the inventory a self-contained preview of enforcement logic — an auditor can
verify C-30 completeness by scanning the table without inspecting definition blocks.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|---------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | Primary | Numeric rate with unit | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | C-27 extension 1 | SHAPE-NEUTRAL or SHAPE-SENSITIVE at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | C-27 extension 2 | Specific connector setting, policy parameter, or API attribute | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | C-27 extension 3 | All three slots: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | C-27 extension 4 | Per-finding identification | Binary FAIL flag without enumeration of specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | C-27 extension 5 | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types above match the domain-specific text at
each downstream definition site — enabling inventory-vs-definition verification.)*

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
    in place of "1,200 req/min"). Adjacent column contrast: TABLE A `Load-shape verdict`'s
    failure is a deferred verdict token — the executor knows the verdict category but routes
    the act of stating it to Step 2G. That is a timing failure, not a value-precision
    failure. An entry that says "limited" fails on missing content; an entry that says
    "see Step 2G" fails on deferred placement. Both produce incomplete rows, but they are
    not the same failure: one lacks the measured number; the other defers the classification
    act to a section that depends on it.*
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
  be a pure volume-threshold analysis table — making load-shape classification (which
  compares arrival patterns, not volume levels) appear out of scope for the registry and
  naturally belonging in the section named "LOAD SHAPE COMPARISON." This frame routes
  shape analysis to Step 2G.

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time, because SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined
  by whether the Limit is expressed as a per-second window or a per-minute bucket. Premise
  2: Step 2G depends on per-tier Load-shape verdicts to identify which tiers change STATUS
  between uniform and burst arrival — it cannot produce a meaningful comparison without
  those verdicts. Consequence: deferring creates a circular dependency.

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at registration
    time. Adjacent column contrast: the `Limit` column's failure is a vague-label
    substitution — an imprecise placeholder for a measured numeric bound (e.g., "limited"
    instead of "500 req/min"). That is a content-absence failure: the number is missing.
    This column's failure is a timing failure: the classification act is performed, but
    at the wrong moment and in the wrong location. A Limit failure and a Load-shape verdict
    failure are both incomplete rows, but they require different corrections: supply the
    missing number (Limit) vs. move the classification act to registration time (verdict).*
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

For the 1x binding constraint tier: is Retry-After present and surfaced? Name the failure
mode precisely if absent (retry storm vs. quota exhaustion require different remediations).

---

**Step 2G — LOAD SHAPE COMPARISON**

**Standing enforcement reminder — Failure 5 prevention (C-17, C-19):** Tiers introduced
during load shape analysis that are not in TABLE A are scope violations. Return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column, compare 1x nominal at two
arrival patterns. At least one numeric comparison where status differs at identical total
count.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). Adjacent column contrast: TABLE A
  `Limit`'s failure is a vague-label substitution — an imprecise placeholder for a measured
  number. TABLE A `Load-shape verdict`'s failure is a deferred verdict token — the
  classification is known but placed in the wrong section. This column's failure is neither
  a missing number nor a timing deferral: it is a category-for-identifier substitution —
  naming what kind of action to take (a task) rather than the specific parameter that
  implements it (a change). All three produce incomplete rows; each requires a different
  correction: supply the number (Limit), move the classification (verdict), name the
  parameter (this column).*
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

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose. Adjacent contrast: TABLE A `Limit`'s failure is
  missing content in a value field (vague number); TABLE F's failure is a wrong content
  category in a parameter field (action label for identifier). This schema's failure is
  structural omission — a labeled slot position is left empty or merged — distinct from a
  vagueness failure (present but imprecise) or a category failure (present but wrong type).*
- Compliance failure condition (C-27 extension): A finding omitting any named slot position
  — or presenting findings as free-form prose — fails the identification schema.

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
  Adjacent contrast: the C-24 finding schema's failure is structural omission (a slot is
  missing from an individual finding); this audit field's failure is evidence absence (the
  FAIL verdict is issued but the findings it covers are not listed). One failure is within
  a single finding; the other is at the aggregate reporting level.*
- Compliance failure condition (C-27 extension): A FAIL verdict without specific informal
  references fails this audit field.

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
  contrast: the C-13 audit field's failure is evidence absence on FAIL (informal references
  not listed); this field's failure is verdict granularity (per-step verdicts collapsed
  into a single aggregate). C-13 fails on what the FAIL entry contains; C-19 fails on
  whether each step receives its own verdict line before the aggregate.*
- Compliance failure condition (C-27 extension): A single aggregate verdict without per-
  step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

---

## V-05 — Combined: All Three Axes (C-34 + C-35 + Phrasing Register)

**Axes:** (1) Output format: `*Violation type:*` fields explicitly quote adjacent site
failure modes before establishing the current site's distinguishing characteristic —
same as V-01 and V-04. (2) Lifecycle emphasis: PRECISION-SITE INVENTORY as four-column
table with standalone `Violation type` column — same as V-02 and V-04. (3) Phrasing
register: all enforcement obligations stated using formal register (SHALL, MUST,
PROHIBITED, MAY NOT) throughout prohibitions, failure conditions, and audit requirements.

**Hypothesis:** V-05 is the v11 ceiling. C-34 is satisfied by the explicit cross-site
contrast language (V-01 axis). C-35 is satisfied by the structured inventory table (V-02
axis). The formal register does not alter C-34 or C-35 content but strengthens the
enforcement posture of all structural constraints — every prohibition becomes
machine-checkable rather than advisory. Predicted: C-34 PASS, C-35 PASS. Composite =
110/110.

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
this prompt is enumerated below in document order. The `Violation type` column states
the specific failure at each site, matching the domain-specific text that will appear at
each downstream definition site. An auditor SHALL verify C-30 compliance by scanning this
table — the inventory is a self-contained preview of enforcement logic. Any site not
listed here that is discovered to carry a precision requirement after this inventory closes
constitutes a scope violation.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|---------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (STEP 1) | Primary | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (STEP 1) | C-27 extension 1 | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at registration time | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at registration time |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | C-27 extension 2 | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | C-27 extension 3 | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | C-27 extension 4 | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | C-27 extension 5 | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. An executor SHALL confirm that each site in this table
carries a co-located failure condition at its definition location — and that the violation
type stated here matches the domain-specific text at the definition site. Mismatch between
this inventory and a downstream definition site constitutes a C-30 gap.)*

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
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min"). An
  executor MUST NOT enter a vague label.
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Adjacent column contrast: the `Load-shape verdict`
    column's violation type is a deferred verdict token — the executor routes the
    SHAPE-NEUTRAL/SHAPE-SENSITIVE classification to Step 2G rather than recording it at
    registration time. That failure is a timing failure: the content exists but is placed
    at the wrong moment. This column's failure is a value-absence failure: the numeric
    bound is missing or replaced by an imprecise placeholder. A deferred verdict and a
    vague number are both incomplete, but they are not the same failure — one lacks the
    measured number entirely; the other defers the classification act. Conflating them
    produces incorrect corrections: deferral requires moving the classification; vagueness
    requires supplying the number.*
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
  be a pure volume-threshold analysis table — making load-shape classification (which
  compares arrival patterns, not volume levels) appear out of scope for the registry and
  naturally belonging in the section named "LOAD SHAPE COMPARISON." This frame routes
  shape analysis to Step 2G. An executor following this frame will complete the bottleneck
  ordering in Step 1 correctly but leave the Load-shape verdict column blank or annotated
  "see Step 2G."

  **Structural rejection proof (C-26):** This frame is structurally self-defeating.
  Premise 1: load-shape classification requires the registered `Limit` value present in
  TABLE A at registration time, because SHAPE-NEUTRAL vs. SHAPE-SENSITIVE is determined
  by whether the Limit is expressed as a per-second window (burst and uniform saturate
  differently) or a per-minute bucket (total volume determines saturation). Premise 2:
  Step 2G (LOAD SHAPE COMPARISON) depends on per-tier Load-shape verdicts to identify
  which tiers change STATUS between uniform and burst arrival — it cannot produce a
  meaningful numeric comparison without those verdicts already established. Consequence:
  deferring creates a circular dependency. The comparison depends on the verdict; the
  verdict is deferred to the comparison. The escape route does not defer the work to a
  more appropriate location — it makes the work structurally impossible to complete
  correctly.

  - *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
    SHAPE-SENSITIVE classification to Step 2G rather than recording it at registration
    time. Adjacent column contrast: the `Limit` column's violation type is a vague-label
    substitution — an imprecise placeholder where a measured numeric bound is required
    (e.g., "limited" instead of "500 req/min"). That is a content-absence failure. This
    column's failure is a timing failure: the classification category is well-defined, but
    the executor places the act of recording it in a downstream section that structurally
    depends on it. Correcting a Limit vagueness failure means supplying the number.
    Correcting a Load-shape verdict deferral failure means moving the classification act
    to registration time. They are adjacent failures in the same table but require
    different corrections.*
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
|-----|---------------|--------------|-----------|-------------------|
| 1   |               |              |           |                   |
| 2   |               |              |           |                   |
| ... |               |              |           |                   |

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

At least one row. If no unprotected path exists, row 1 MUST state the conclusion with
at least two named controls as evidence.

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

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT,
  referencing the Load-shape verdict and specific Limit value.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs between patterns SHALL be present.
Ground in a specific TABLE A Limit value and Load-shape verdict.

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
  `Limit`'s violation type is a vague-label substitution — an imprecise placeholder for a
  measured numeric bound (e.g., "limited" in place of "500 req/min"). TABLE A `Load-shape
  verdict`'s violation type is a deferred verdict token — the classification is placed in
  the wrong section. This column's violation type is neither: the value is a string, not a
  number; and there is no timing constraint. The failure is category substitution — naming
  what kind of action to take (a task category) where the specific deployable parameter
  name is required (a change identifier). All three failures produce rows that cannot be
  used without additional investigation, but each for a different reason: missing number
  (Limit), deferred classification (verdict), action category instead of parameter
  identifier (this column).*
- Compliance failure condition (C-27 extension): A row naming a category of action rather
  than a specific parameter identifier FAILS this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks
the connector layer; the load test running at 10% of production concurrency.)*

Execute two stages in order. Stage 1 pre-loads artifact names that Stage 2's `Structural
reason` column requires — without Stage 1 complete, TABLE E entries default to category
labels.

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
| GAP-01 |                                           |           |                                                   |                                                |
| GAP-02 |                                           |           |                                                   |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. An executor SHALL complete this block after Stage 2. Each downstream
section MUST receive an individual verdict on a distinct verdict line, with evidence on a
distinct evidence line.

**C-24 format requirement:** Each field entry MUST use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots using this
template. An executor SHALL fill every labeled position — no slot MAY be omitted or
combined:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot
  positions absent or collapsed into prose. Adjacent contrast: TABLE A `Limit`'s violation
  type is value absence (vague label where a number is required); TABLE F's violation type
  is category substitution (action label where a parameter identifier is required). This
  schema's violation type is structural omission: a slot position that MUST be populated is
  left empty or merged with adjacent content. The three violation types are adjacent in the
  enforcement hierarchy (all produce incomplete output) but each constitutes a different
  class of failure: absent value, wrong value category, missing structural slot.*
- Compliance failure condition (C-27 extension): A finding that omits any named slot
  position — or presents findings as free-form prose without the labeled slot structure —
  FAILS the identification schema.

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
  Adjacent contrast: the C-24 finding schema's violation type is structural omission (a
  named slot is missing from an individual finding). This audit field's violation type is
  evidence absence: the FAIL verdict is present and correctly formatted, but the findings
  it covers are not identified. The schema failure is within a single finding entry; the
  audit field failure is at the reporting level — both produce unusable output, but the
  schema failure requires adding a slot to a finding; the audit field failure requires
  listing the specific informal references that triggered the verdict.*
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
  contrast: the C-13 audit field's violation type is evidence absence on FAIL (a FAIL
  verdict issues with no informal references listed). This field's violation type is
  verdict granularity collapse: individual step verdicts are merged into a single aggregate
  before the FAIL branch. The C-13 failure produces an unactionable FAIL (the reader
  cannot identify which references were informal); this field's failure produces a FAIL
  where the reader cannot identify which steps are missing reminders. Both fail at the
  audit level, but the correction differs: C-13 requires listing the informal references;
  C-19 requires issuing per-step inline verdicts.*
- Compliance failure condition (C-27 extension): A single aggregate verdict without per-
  step inline verdicts FAILS the C-25 format requirement at this field.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]
