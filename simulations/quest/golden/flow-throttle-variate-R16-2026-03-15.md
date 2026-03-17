# flow-throttle Variate — Round 16 (v16 rubric, C-01 through C-43)
**Date:** 2026-03-15
**Rubric:** v16 (C-01 through C-43, N_essential=5, N_recommended=3, N_aspirational=35)
**Baseline ceiling:** R15 V-05 (passes C-01 through C-41 under v15)

---

## State Analysis: What R15 Established vs. What R16 Must Add

**R15 V-05 coverage under v16 (confirmed):**
- C-01 through C-41: all pass
- C-42: not yet addressed — R15 V-05's C-41 audit uses abbreviated block citations. The
  declared block name in the prompt body is "REGISTRY GAP PROHIBITION — Failure 5 prevention
  (C-17)" but the audit table cites it as "REGISTRY GAP PROHIBITION (STEP 1 phase boundary)".
  Dropping the "— Failure 5 prevention (C-17)" suffix and substituting a positional descriptor
  is a paraphrase. C-41 requires enumeration "by its block name"; C-42 upgrades that to
  "verbatim declared name exactly as it appears in the prompt body."
- C-43: not yet addressed — R15 V-05 enumerates 9 enforcement directives in the C-41 audit
  but misses two MUST NOT clauses embedded in *Violation type* italic fields within STEP 4:
  (1) the non-conflation directive in the C-24 finding schema *Violation type* field and
  (2) the non-conflation directive in the C-13 audit FAIL field *Violation type* field. Both
  use normative-register language (MUST NOT) in non-primary-location positions and qualify
  as enforcement directives subject to C-41 enumeration under C-43.

**Total enforcement directives in a correctly constructed v16 prompt: 11**

Named block directives (6):
1. REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17)
2. Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
3. Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
4. Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
5. Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)
6. Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT
   STEP 1B

Embedded non-primary-location directives (5):
7. TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive
8. TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive
9. PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note)
10. STEP 4 C-24 finding schema — *Violation type* field non-conflation directive
11. STEP 4 C-13 audit FAIL field — *Violation type* field non-conflation directive

---

## Round 16 Variation Map

| Variation | Axes | C-42 mechanism | C-43 mechanism | C-42 | C-43 | Predicted composite |
|-----------|------|----------------|----------------|------|------|---------------------|
| V-01 | Phrasing register — abbreviated block names | Drops criterion-ID parentheticals from all audit citations; uses positional descriptors | 9 of 11 (both STEP 4 embedded non-conflation directives absent) | FAIL | FAIL | 108/110 |
| V-02 | Output format — table-dense, verbatim names | All primary directive citations verbatim | 10 of 11 — discovers C-24 non-conflation, misses C-13 FAIL non-conflation | PASS | FAIL | 109/110 |
| V-03 | Lifecycle emphasis — verbatim, 11 entries, wrong container names | All 11 directive citations verbatim primary-location names; non-primary entries use wrong containing structure | Correct count (11) but two non-primary entries named by incorrect container (fails C-43 container-name requirement) | PASS | FAIL | 109/110 |
| V-04 | Combined: role sequence (1A/1B) + output format | Verbatim block names for all primary directives and 10 embedded directives | 10 of 11 with correct containers; misses C-13 FAIL non-conflation | PASS | FAIL | 109/110 |
| V-05 | All axes combined | Verbatim for all 11; explicit C-43 discovery annotation | All 11 discovered; non-primary entries named by exact containing structure per C-43 | PASS | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs R15 V-05): Does dropping criterion-ID parentheticals from block-name citations
("REGISTRY GAP PROHIBITION" instead of "REGISTRY GAP PROHIBITION — Failure 5 prevention
(C-17)") fail C-42 while satisfying C-41? Hypothesis: yes — C-42 requires "verbatim declared
name exactly as it appears in the prompt body"; the declared name includes the parenthetical;
omitting it is a paraphrase that satisfies C-41's block-name requirement but fails C-42's
verbatim requirement. Predicted: C-42 FAIL.

Q2 (V-02 vs R15 V-05): Does discovering 10 of 11 embedded directives (verbatim names for all
10, correct container names, but missing the C-13 audit FAIL *Violation type* MUST NOT clause)
fail C-43? Hypothesis: yes — C-43 requires all normative-register clauses regardless of
location; one omission fails the criterion. Predicted: C-43 FAIL.

Q3 (V-03 vs V-02): Does enumerating all 11 directives but using wrong containing-structure
names for the two STEP 4 non-primary entries fail C-43? Hypothesis: yes — C-43 specifies
"its containing structure name serves as its block name"; naming a non-primary directive under
a different container than where it appears constitutes a block-name error at the embedded-
directive level even when all directives are discovered. Predicted: C-43 FAIL.

Q4 (V-04 vs V-03): Does using verbatim block names for all primary directives and correctly
naming 10 embedded directives while omitting one still fail C-43? Hypothesis: yes —
completeness is the criterion; the omitted C-13 FAIL non-conflation directive uses MUST NOT
in a *Violation type* field and qualifies regardless of its depth in the audit subsection.
Predicted: C-43 FAIL.

Q5 (V-05): Does full 11-directive C-41 audit with verbatim primary-location block names,
correct containing-structure names for all 5 non-primary entries, and an explicit C-43
discovery annotation satisfy both C-42 and C-43 without regressions? Hypothesis: yes.
Predicted: C-42 PASS, C-43 PASS, composite 110/110.

---

## V-01 — Single Axis: Phrasing Register (Abbreviated Block Names in C-41 Audit)

**Axis:** Phrasing register — the C-41 audit table cites enforcement directives using
abbreviated block names (dropping criterion-ID parentheticals and substituting positional
descriptors). All enforcement directives in the prompt body use RFC 2119 normative register;
the citation failure is in the audit table only. Nine directives are enumerated; the two STEP
4 embedded non-conflation directives are absent.

**Hypothesis:** Abbreviated citations ("REGISTRY GAP PROHIBITION" for "REGISTRY GAP
PROHIBITION — Failure 5 prevention (C-17)"; "reminder at Step 2A" for "Step 2A — Standing
enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)") fail C-42 because the verbatim
declared name includes the parenthetical qualifier and the positional descriptor respectively.
C-43 also fails: the two STEP 4 *Violation type* non-conflation directives are not discovered.
Predicted: C-42 FAIL, C-43 FAIL. Composite = 108/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

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

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every precision-requiring
site in this prompt is enumerated below in document order. The `Violation type` column states
the specific failure at each site, matching the domain-specific text that SHALL appear at each
definition site. The `C-27 hierarchy` column uses the C-31 parenthetical labeling format —
`primary (C-27):` for the first site and `extension (C-27 extension):` for all subsequent
sites — making the C-31 labeling structure auditable from this inventory without opening each
definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (Step 1A) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (Step 1B) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at Step 1B | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at Step 1B |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types SHALL match the domain-specific text at each
downstream definition site — enabling inventory-vs-definition verification. An executor SHALL
verify that the label at each definition block matches the `C-27 hierarchy` value in this row
before producing that definition block — the inventory value is a compliance target, not a
record.)*

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or 5x
nominal — the volume nobody tested.)*

Step 1 has two sub-steps. An executor SHALL complete Step 1A and Step 1B in order before
opening any Step 2 section. The registry SHALL be closed only after Step 1B gate is cleared.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED:
assigning a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A,
register the tier with all columns filled, and SHALL restart from the point of discovery.
This prohibition SHALL be restated at each Step 2 section where mid-phase discovery could
occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

*(Volume analyst role: identify every rate-limiting component; record numeric limit, scope,
volume-band status, binding band, failure visibility window, and recovery time. Leave
`Load-shape verdict` as placeholder — assign at Step 1B.)*

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Site 1 has one immediate right neighbor (site 2:
    Load-shape verdict). Single-adjacency — C-36 and C-38 SHALL NOT apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead of a
    specific number-with-unit fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT; SHALL shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

**STEP 1A GATE:** Step 1A SHALL be considered closed when: (a) every identified rate-limiting
component in the target flow has a T-NN row in TABLE A; (b) every TABLE A row except
`Load-shape verdict` is populated with non-placeholder values; and (c) the `Limit` column
contains no vague labels. An executor SHALL NOT open Step 1B until this gate is cleared.

---

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

*(Load-shape analyst role activates here. Review each tier's `Limit` entry in TABLE A and
assign the `Load-shape verdict` column for every row. The registry closes after Step 1B.)*

**Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT
STEP 1B:** An executor SHALL assign `Load-shape verdict` for every TABLE A tier at this step.
PROHIBITED: leaving any `Load-shape verdict` cell as placeholder or deferring classification
to the LOAD SHAPE COMPARISON section (Step 2G).

**Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold is
crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears to be a
pure volume-threshold analysis table — making load-shape classification appear out of scope
for the registry and naturally belonging in the section named "LOAD SHAPE COMPARISON." The
Step 1B sub-step structure itself introduces a second escape route: because Step 1B is a named
analyst sub-step, an executor may reason that classification can be deferred to Step 2G where
"the analyst naturally encounters load patterns." Both frames route shape analysis to Step 2G.

**Structural rejection proof (C-26):** Both frames are structurally self-defeating. Premise 1:
load-shape classification requires the registered `Limit` value at registration time —
available in TABLE A now at Step 1B. Premise 2: Step 2G depends on per-tier Load-shape
verdicts to produce meaningful comparisons. Consequence: deferring to Step 2G creates a
circular dependency where the downstream section that would "receive" shape classification
is itself dependent on the per-tier verdict the registry was supposed to supply. Step 1B
exists precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

- *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
  SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.
  All-neighbor contrast (C-36): the `Limit` column's violation type (left neighbor, site 1)
  is a value-absence failure — the measured number is missing or replaced by an imprecise
  placeholder. TABLE F `Setting or API parameter`'s violation type (right neighbor, site 3)
  is a parameter-specificity failure — a task category is named where a deployable parameter
  identifier is required. This column's violation type is neither: the value is not absent
  and the failure is not about parameter identity; the failure is purely temporal — the act
  of recording the verdict is deferred to a section that structurally depends on it. Three
  distinct failures at the same registry level, three different corrections: supply the number
  (Limit), move the classification act to Step 1B (this column), name the parameter (TABLE F).
  An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry left
  blank or deferred ("see Step 2G", "analyzed below") at the end of Step 1B fails the
  registration-time classification requirement and invalidates Step 2G's numeric comparison.

**STEP 1B GATE:** Step 1B SHALL be considered closed when every TABLE A row has a populated
`Load-shape verdict` cell containing a SHAPE-NEUTRAL or SHAPE-SENSITIVE verdict with numeric
differential and mechanism. No placeholder SHALL remain. The registry is closed at this point.
An executor SHALL NOT begin STEP 2 until this gate is cleared.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed after Step 1B gate is cleared. An executor SHALL use T-NN
identifiers from TABLE A throughout all sections below.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second throttle
window into a 10-minute retry storm — invisible where the connector layer is mocked.)*

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

A minimum of two hops SHALL be present. `Mechanism` SHALL be specific: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per Tier-ID from TABLE A. No tier SHALL be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(What inertia conceals here: the burst path that bypasses rate limiting because no test has
ever run at the volume where it fires.)*

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

At least one row SHALL be present. If no unprotected path exists, row 1 SHALL state the
conclusion with at least two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

All TABLE A tiers SHALL appear in the ranking, ordered by business risk, highest to lowest.
One sentence per tier with rationale SHALL be provided. For the top-ranked tier, `Failure
visibility window` and `Recovery time` from TABLE A SHALL be referenced.

---

**Step 2E — CASCADE SCENARIO**

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. T-NN identifiers SHALL be used
throughout. Each causal link SHALL be stated explicitly. A minimum of three tiers SHALL be
present, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the failure
mode SHALL be named precisely — retry storm (exponential backoff) vs. quota exhaustion
(circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis that are not in TABLE A are scope violations. An
executor SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column (classified at Step 1B), compare
1x nominal at two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs at identical total count SHALL be present.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36): the
  `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred verdict
  token — the classification act is placed at the wrong moment, routed to Step 2G rather than
  recorded at Step 1B. The STEP 4 C-24 finding schema's violation type (right neighbor, site 4)
  is a structural omission — a labeled slot position within a single finding entry is left
  empty or merged with adjacent content. This column's violation type is neither: the value is
  a string identifier, not a number; there is no timing constraint; and the failure is not
  about a slot within a structured finding. The failure is category substitution — naming the
  class of action where the specific deployable parameter name is required. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of action
  rather than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(What inertia conceals here: the integration test suite reporting green because it mocks the
connector layer; the load test running at 10% of production concurrency.)*

Execute two stages. Stage 1 SHALL pre-load artifact names; Stage 2 SHALL use them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts SHALL be named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

"Stage 1 complete" SHALL be stated before Stage 2 opens.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. An executor SHALL complete this block after Stage 2. Each downstream
section SHALL receive an individual verdict on a distinct verdict line, with evidence on a
distinct evidence line.

**C-24 format requirement:** Each field entry SHALL use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot positions
  absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F `Setting or API
  parameter`'s violation type (left neighbor, site 3) is category substitution — a task-class
  label occupies the parameter field. The STEP 4 C-13 audit FAIL field's violation type (right
  neighbor, site 5) is evidence absence — a FAIL verdict is issued at the aggregate level
  without enumerating the specific informal references found. This schema's violation type is
  distinct from both: the failure is not a wrong category in a parameter field and not an
  absent evidence list at aggregate level — a labeled slot position within a single finding
  entry is left empty or merged with adjacent content. An executor MUST NOT conflate these
  2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any named
  slot position — or presents findings as free-form prose — fails the identification schema.

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
  Adjacent contrast: the C-24 finding schema's violation type (left neighbor, site 4) is
  structural omission within a finding entry — a labeled slot is missing or collapsed into
  prose. The STEP 4 C-19 audit FAIL field's violation type (right neighbor, site 6) is verdict
  granularity collapse — individual step verdicts are merged into a single aggregate without
  per-step assessments. This audit field's violation type is distinct from both: the failure
  is not within a single finding (C-24's domain) and not about per-step verdict granularity
  (C-19's domain). The failure is at the aggregate reporting level — the FAIL verdict is
  correctly present but the specific informal references are not enumerated. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does not
  enumerate specific informal references fails this audit field.

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
  contrast: the C-13 audit field's violation type (left neighbor, site 5) is evidence absence
  on FAIL — a FAIL verdict that correctly fires but names no specific findings. This field's
  violation type is verdict granularity collapse: per-step verdicts are merged into a single
  aggregate before the FAIL branch. C-13 fails on what the FAIL entry contains; C-19 fails
  on whether each step receives its own verdict line. Both fail at the audit level; each
  requires a different correction. Site 6 has one immediate neighbor — C-36 and C-38 do
  not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-42 note: this table uses abbreviated block names — criterion-ID parentheticals are dropped
and positional descriptors substituted. "REGISTRY GAP PROHIBITION" appears without the
declared "— Failure 5 prevention (C-17)" suffix. Step reminder entries appear as "reminder at
Step 2A" rather than the verbatim block name "Step 2A — Standing enforcement reminder —
REGISTRY GAP PROHIBITED (C-17, C-19)". These citations satisfy C-41's block-name requirement
but fail C-42's verbatim-declared-name requirement.)*

For each enforcement directive block in this prompt, verify that the primary directive uses
RFC 2119-style normative language:

| Directive block | Primary language used | C-40 verdict |
|----------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION | PROHIBITED / SHALL | [PASS / FAIL] |
| Reminder at Step 2A | SHALL NOT | [PASS / FAIL] |
| Reminder at Step 2C | SHALL NOT | [PASS / FAIL] |
| Reminder at Step 2E | SHALL NOT | [PASS / FAIL] |
| Reminder at Step 2G | SHALL NOT | [PASS / FAIL] |
| Load-shape classification deferral prohibition (Step 1B) | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A Load-shape verdict non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F parameter non-conflation directive | MUST NOT | [PASS / FAIL] |
| Inventory verification obligation | SHALL verify | [PASS / FAIL] |

*(C-41 satisfied by block-name coverage — nine directives enumerated. C-42 not satisfied:
"Reminder at Step 2A/2C/2E/2G" are step-number locators, not the verbatim declared block
names; "REGISTRY GAP PROHIBITION" drops "— Failure 5 prevention (C-17)." C-43 not satisfied:
the non-conflation directives embedded in the STEP 4 C-24 finding schema *Violation type*
field and the STEP 4 C-13 audit FAIL field *Violation type* field are absent from this
enumeration.)*

---

## V-02 — Single Axis: Output Format (Table-Dense, Verbatim Names, 10 of 11 Embedded Directives)

**Axis:** Output format — maximum table density throughout; all obligation language in RFC
2119 normative register; C-41 audit uses verbatim declared block names for all primary-location
directives; discovers 10 of 11 embedded non-primary-location directives. The STEP 4 C-24
finding schema *Violation type* field non-conflation directive is discovered and enumerated;
the STEP 4 C-13 audit FAIL field *Violation type* field non-conflation directive is absent.

**Hypothesis:** Verbatim block names satisfy C-42. Discovering 10 of 11 embedded directives
fails C-43: the C-13 FAIL *Violation type* MUST NOT clause is embedded in a *Violation type*
italic field within STEP 4 and qualifies as an enforcement directive under C-43. One omission
fails the completeness requirement regardless of how many are correctly discovered.
Predicted: C-42 PASS, C-43 FAIL. Composite = 109/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Every cell SHALL be filled. Produce sections in the
order shown.

---

*(PRECISION-SITE INVENTORY: identical to V-01 — six sites, same hierarchy labels and violation
types. Inventory verification obligation parenthetical note uses "An executor SHALL verify"
— normative register.)*

---

*(STEP 1 — TIER REGISTRY: identical to V-01 structure. REGISTRY GAP PROHIBITION —
Failure 5 prevention (C-17) block present with PROHIBITED and SHALL. Step 1A and Step 1B
gates with explicit SHALL NOT conditions. Failure 2 + Failure 6 prevention (C-16, C-20,
C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B block present with PROHIBITED and SHALL.
All-neighbor contrast text and compliance failure conditions identical to V-01.)*

---

*(STEP 2 — ANALYSIS PHASES: identical to V-01. All four standing enforcement reminder blocks
present with their declared names: "Step 2A — Standing enforcement reminder — REGISTRY GAP
PROHIBITED (C-17, C-19)", "Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED
(C-17, C-19)", "Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17,
C-19)", "Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19)".
TABLE F *Violation type* field and all compliance failure conditions identical to V-01.)*

---

*(STEP 3 — TEST COVERAGE GAP ANALYSIS: identical to V-01.)*

---

**STEP 4 — INTEGRITY VERIFICATION**

*(C-13, C-19, C-14 compliance fields: identical structure to V-01, including both *Violation
type* fields with their MUST NOT conflate directives embedded inline.)*

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template]

Step 2B (TABLE C):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template]

Step 2C (TABLE D):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template]

Step 2D (TIER RISK RANKING):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template]

Step 2E (CASCADE SCENARIO):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template]

Step 2G (LOAD SHAPE COMPARISON):
- Verdict: [PASS / FAIL]
- If FAIL — informal references found: [list each using the three-slot template]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: "[tier name] introduced at [step]"]

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  Adjacent contrast: [identical to V-01 C-13 *Violation type* text]. An executor MUST NOT
  conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does not
  enumerate specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

*(C-25 format requirement and per-step inline verdict structure: identical to V-01.)*

- Step 2A (TABLE B): [Y — reminder present / N — missing]
- Step 2C (TABLE D): [Y — reminder present / N — missing]
- Step 2E (CASCADE SCENARIO): [Y — reminder present / N — missing]
- Step 2G (LOAD SHAPE COMPARISON): [Y — reminder present / N — missing]
- If any N:
  - Verdict: FAIL
  - Missing steps: [list each step where N was recorded]

- *Violation type: aggregate verdict without per-step inline verdict sequence. [identical
  to V-01]. Site 6 has one immediate neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

For each enforcement directive block in this prompt, verify that the primary directive uses
RFC 2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An
executor SHALL enumerate each directive by its verbatim declared block name and record a
per-directive verdict:

| Directive block (verbatim declared name) | Primary language used | C-40 verdict |
|-----------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 finding schema — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific informal phrase found and its normative replacement.

*(C-42 satisfied: all ten cited directives use verbatim declared block names as they appear
in the prompt body. C-43 not satisfied: the STEP 4 C-13 audit FAIL field *Violation type*
field contains "An executor MUST NOT conflate these 2 failure modes" — a normative-register
obligation clause embedded in a non-primary location. This clause is absent from the
enumeration above, leaving the total directive count at 10 of 11. C-43 requires all
normative-register clauses regardless of structural location.)*

---

## V-03 — Single Axis: Lifecycle Emphasis (Verbatim Names, 11 Entries, Wrong Container References)

**Axis:** Lifecycle emphasis — each phase carries explicit PHASE ENTRY and PHASE EXIT
condition blocks, making control flow self-documenting; these gate blocks introduce additional
SHALL NOT clauses. All obligation language is in RFC 2119 register. The C-41 audit enumerates
all 11 enforcement directives using verbatim block names for primary-location entries; however,
the two STEP 4 non-primary-location entries are named using incorrect container references
("STEP 4 C-24 schema compliance note" and "STEP 4 C-13 FAIL annotation") rather than their
actual containing structure names.

**Hypothesis:** Discovering all 11 directives satisfies the completeness aspect of C-43 but
the criterion requires "its containing structure name serves as its block name for enumeration
purposes." Using "STEP 4 C-24 schema compliance note" when the actual containing structure
is "STEP 4 C-24 finding schema *Violation type* field" constitutes a block-name error at
the embedded-directive level. C-43 fails on location-reference accuracy even when count is
correct. Predicted: C-42 PASS, C-43 FAIL. Composite = 109/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Every cell SHALL be filled. Produce sections in the
order shown.

---

*(PRECISION-SITE INVENTORY: identical to V-01.)*

---

*(STEP 1 — TIER REGISTRY: identical to V-01, with additional PHASE ENTRY CONDITION block at
Step 1A: "PHASE ENTRY CONDITION: Step 1A SHALL be entered when the signal input has been read
in full." and PHASE EXIT CONDITION at Step 1B gate: "PHASE EXIT CONDITION: The registry is
closed only after this gate is cleared. An executor SHALL NOT begin STEP 2 until this
condition is met.")*

---

*(STEP 2 — ANALYSIS PHASES: identical to V-01, with PHASE ENTRY CONDITION and PHASE EXIT
CONDITION blocks added at each sub-step. Each standing enforcement reminder block present
with verbatim declared names as in V-01.)*

---

*(STEP 3 — TEST COVERAGE GAP ANALYSIS: identical to V-01, with PHASE ENTRY CONDITION:
"Stage 2 SHALL be entered only after Stage 1 complete is declared.")*

---

**STEP 4 — INTEGRITY VERIFICATION**

*(C-24 format requirement, C-13 compliance, C-19 compliance, C-14 compliance fields:
identical to V-01, including both *Violation type* fields with MUST NOT conflate directives
embedded inline.)*

**C-13 compliance — Tier-ID threading:**
*(per-section verdict structure: identical to V-01)*

**C-19 compliance — distributed reminder audit:**
*(per-step inline verdict structure: identical to V-01)*

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

For each enforcement directive block in this prompt, verify that the primary directive uses
RFC 2119-style normative language. An executor SHALL enumerate each directive by its verbatim
declared block name (for primary-location directives) or its containing structure name (for
embedded non-primary-location directives) and record a per-directive verdict:

| Directive block | Primary language used | C-40 verdict |
|----------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 schema compliance note — non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 FAIL annotation — non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-42 satisfied: all six primary-location directives cited by verbatim declared block name.
C-43 not satisfied: the two STEP 4 non-primary-location entries are cited under incorrect
container names. The actual containing structures are "STEP 4 C-24 finding schema *Violation
type* field" and "STEP 4 C-13 audit FAIL field *Violation type* field". Citing them as
"STEP 4 C-24 schema compliance note" and "STEP 4 C-13 FAIL annotation" does not use the
containing structure name as it appears in the prompt body. C-43 requires the containing
structure name as the block name; misidentifying the containing structure fails C-43 on
location-reference accuracy despite correct directive count.)*

---

## V-04 — Combined: Role Sequence (1A/1B Analyst Split) + Output Format (Table-Dense)

**Axis:** Combined — V-04 from R15's role sequence (explicit Volume Analyst and Load-Shape
Analyst sub-step split) plus V-02's table-dense output format throughout. RFC 2119 normative
register throughout. C-41 audit uses verbatim declared block names and discovers 10 of 11
embedded directives — same omission pattern as V-02 (C-13 FAIL *Violation type* non-conflation
absent) but with the combined structural variation.

**Hypothesis:** The combined structural variation does not affect directive count or block-name
precision. C-42 passes because verbatim names are used for all 10 cited directives. C-43 fails
for the same reason as V-02: the C-13 audit FAIL *Violation type* non-conflation directive is
an enforcement clause in a non-primary location and must be discovered under C-43 regardless
of whether the structural variant uses a 1A/1B split. Predicted: C-42 PASS, C-43 FAIL.
Composite = 109/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x. Every cell SHALL be filled. Produce sections in the
order shown.

---

*(PRECISION-SITE INVENTORY: identical to V-01. Six sites, same hierarchy, same violation
types, same inventory verification obligation parenthetical.)*

---

*(STEP 1 — TIER REGISTRY: identical to V-01 1A/1B structure. REGISTRY GAP PROHIBITION —
Failure 5 prevention (C-17) block at phase boundary. Step 1A: Volume Analyst role, TABLE A
with [Step 1B] placeholder in Load-shape verdict, STEP 1A GATE. Step 1B: Load-Shape Analyst
role, Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT
STEP 1B block, escape-route story, structural rejection proof, all-neighbor contrast text,
compliance failure conditions, STEP 1B GATE.)*

---

*(STEP 2 — ANALYSIS PHASES: all four standing enforcement reminder blocks present with
verbatim declared names. TABLE F with *Violation type* non-conflation directive and compliance
failure condition. All structure identical to V-01.)*

---

*(STEP 3 — TEST COVERAGE GAP ANALYSIS: identical to V-01.)*

---

**STEP 4 — INTEGRITY VERIFICATION**

*(C-24 format requirement, three-slot template, *Violation type* fields with MUST NOT
non-conflation directives, compliance failure conditions: identical to V-01.)*

**C-13 compliance — Tier-ID threading:**
*(per-section verdict structure: identical to V-01, including *Violation type* MUST NOT
non-conflation directive embedded in italic field)*

**C-19 compliance — distributed reminder audit:**
*(per-step inline verdict structure and *Violation type* field: identical to V-01)*

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

For each enforcement directive block in this prompt, verify that the primary directive uses
RFC 2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An
executor SHALL enumerate each directive by its verbatim declared block name and record a
per-directive verdict:

| Directive block (verbatim declared name) | Primary language used | C-40 verdict |
|-----------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 finding schema — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-42 satisfied: all ten cited directives use verbatim declared block names as they appear
in the prompt body. C-43 not satisfied: the STEP 4 C-13 audit FAIL field *Violation type*
field contains "An executor MUST NOT conflate these 2 failure modes" — a normative-register
MUST NOT obligation embedded in a non-primary *Violation type* field in STEP 4. The combined
1A/1B structural variant does not alter the scope of C-43: embedded MUST NOT clauses in STEP
4 *Violation type* fields qualify as enforcement directives regardless of how Phase 1 is
structured. One omission fails C-43.)*

---

## V-05 — All Axes Combined (C-42 + C-43 Full Per-Directive Audit)

**Axis:** Full combination — V-04's role sequence (Step 1A/1B analyst split), V-02's
table-dense output format, V-03's explicit PHASE ENTRY/EXIT lifecycle gates, comprehensive
RFC 2119 register throughout all obligation positions, and a STEP 4 C-41 compliance field
that enumerates all 11 enforcement directives: 6 primary-location directives by verbatim
declared block name, and 5 non-primary-location directives by their exact containing
structure name per C-43.

**Hypothesis:** Verbatim declared names for all primary-location directives satisfies C-42.
Discovering all 11 directives including both STEP 4 *Violation type* non-conflation clauses
and naming them by their exact containing structures satisfies C-43. No structural criteria
are affected by the combined variation. Predicted: C-42 PASS, C-43 PASS, composite 110/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first production
incident is the discovery mechanism. That is the status quo this skill exists to displace.

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

The tables below are the primary output — each carries a distinct finding category that prose
cannot represent with the same auditability. Every cell SHALL be filled. Produce sections in
the order shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every precision-requiring
site in this prompt is enumerated below in document order. The `Violation type` column states
the specific failure at each site, matching the domain-specific text that SHALL appear at each
definition site. The `C-27 hierarchy` column uses the C-31 parenthetical labeling format —
`primary (C-27):` for the first site and `extension (C-27 extension):` for all subsequent
sites — making the C-31 labeling structure auditable from this inventory without opening each
definition block.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (Step 1A) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (Step 1B) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at Step 1B | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at Step 1B |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. Violation types SHALL match the domain-specific text at each
downstream definition site — enabling inventory-vs-definition verification. An executor SHALL
verify that the label at each definition block matches the `C-27 hierarchy` value in this row
before producing that definition block — the inventory value is a compliance target, not a
record.)*

---

**STEP 1 — TIER REGISTRY**

*(What inertia conceals here: the tier whose per-second limit was never measured at 2x or 5x
nominal — the volume nobody tested.)*

Step 1 has two sub-steps. An executor SHALL complete Step 1A and Step 1B in order before
opening any Step 2 section. The registry SHALL be closed only after Step 1B gate is cleared.

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED:
assigning a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A,
register the tier with all columns filled, and SHALL restart from the point of discovery.
This prohibition SHALL be restated at each Step 2 section where mid-phase discovery could
occur.

---

**Step 1A — VOLUME ANALYST: TIER IDENTIFICATION AND LIMITS**

**PHASE ENTRY CONDITION:** Step 1A SHALL be entered after the signal input has been read in
full.

*(Volume analyst role: identify every rate-limiting component; record numeric limit, scope,
volume-band status, binding band, failure visibility window, and recovery time. Leave
`Load-shape verdict` as placeholder — assign at Step 1B.)*

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| T-02    |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |
| ...     |           |                      |       |           |           |           |                 | [Step 1B]         |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value (e.g., "limited", "throttled"
    in place of "1,200 req/min"). Site 1 has one immediate right neighbor (site 2:
    Load-shape verdict). Single-adjacency — C-36 and C-38 SHALL NOT apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label instead of a
    specific number-with-unit fails this column's precision requirement.
- `STATUS Nx` — OK / HIT / SAT; SHALL shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable (time + signal).
- `Recovery time` — how long until normal operation resumes after burst traffic subsides.

**STEP 1A GATE:** Step 1A SHALL be considered closed when: (a) every identified rate-limiting
component in the target flow has a T-NN row in TABLE A; (b) every TABLE A row except
`Load-shape verdict` is populated with non-placeholder values; and (c) the `Limit` column
contains no vague labels. An executor SHALL NOT open Step 1B until this gate is cleared.

**PHASE EXIT CONDITION:** Step 1A is exited when the STEP 1A GATE is cleared.

---

**Step 1B — LOAD-SHAPE ANALYST: CLASSIFICATION**

**PHASE ENTRY CONDITION:** Step 1B SHALL be entered only after the STEP 1A GATE is cleared.

*(Load-shape analyst role activates here. Review each tier's `Limit` entry in TABLE A and
assign the `Load-shape verdict` column for every row. The registry closes after Step 1B.)*

**Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT
STEP 1B:** An executor SHALL assign `Load-shape verdict` for every TABLE A tier at this step.
PROHIBITED: leaving any `Load-shape verdict` cell as placeholder or deferring classification
to the LOAD SHAPE COMPARISON section (Step 2G).

**Escape-route story (C-23):** The escape route is the "STATUS tracks volume thresholds"
frame. TABLE A STATUS columns use OK/HIT/SAT to track whether a tier's volume threshold is
crossed at each band. Because STATUS is a volume-threshold metric, TABLE A appears to be a
pure volume-threshold analysis table — making load-shape classification appear out of scope
for the registry and naturally belonging in the section named "LOAD SHAPE COMPARISON." The
Step 1B sub-step structure itself introduces a second escape route: because Step 1B is a named
analyst sub-step, an executor may reason that classification can be deferred to Step 2G where
"the analyst naturally encounters load patterns." Both frames route shape analysis to Step 2G.

**Structural rejection proof (C-26):** Both frames are structurally self-defeating. Premise 1:
load-shape classification requires the registered `Limit` value at registration time —
available in TABLE A now at Step 1B. Premise 2: Step 2G depends on per-tier Load-shape
verdicts to produce meaningful comparisons. Consequence: deferring to Step 2G creates a
circular dependency where the downstream section that would "receive" shape classification
is itself dependent on the per-tier verdict the registry was supposed to supply. Step 1B
exists precisely to foreclose this dependency.

For each TABLE A tier, update `Load-shape verdict`:
- State SHAPE-NEUTRAL or SHAPE-SENSITIVE
- State the numeric rate differential between uniform and burst arrival at this tier's limit
- State the mechanism that explains the differential

- *Violation type: deferred verdict token — the executor routes the SHAPE-NEUTRAL/
  SHAPE-SENSITIVE classification to Step 2G rather than recording it at Step 1B.
  All-neighbor contrast (C-36): the `Limit` column's violation type (left neighbor, site 1)
  is a value-absence failure — the measured number is missing or replaced by an imprecise
  placeholder. TABLE F `Setting or API parameter`'s violation type (right neighbor, site 3)
  is a parameter-specificity failure — a task category is named where a deployable parameter
  identifier is required. This column's violation type is neither: the value is not absent
  and the failure is not about parameter identity; the failure is purely temporal — the act
  of recording the verdict is deferred to a section that structurally depends on it. Three
  distinct failures at the same registry level, three different corrections: supply the number
  (Limit), move the classification act to Step 1B (this column), name the parameter (TABLE F).
  An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A Load-shape verdict entry left
  blank or deferred ("see Step 2G", "analyzed below") at the end of Step 1B fails the
  registration-time classification requirement and invalidates Step 2G's numeric comparison.

**STEP 1B GATE:** Step 1B SHALL be considered closed when every TABLE A row has a populated
`Load-shape verdict` cell containing a SHAPE-NEUTRAL or SHAPE-SENSITIVE verdict with numeric
differential and mechanism. No placeholder SHALL remain. The registry is closed at this point.

**PHASE EXIT CONDITION:** Step 1B is exited when the STEP 1B GATE is cleared. An executor
SHALL NOT begin STEP 2 until this phase exit condition is met.

---

**STEP 2 — ANALYSIS PHASES**

**PHASE ENTRY CONDITION:** Step 2 SHALL be entered only after the STEP 1B GATE is cleared.
The tier registry is closed. An executor SHALL use T-NN identifiers from TABLE A throughout
all sections below.

---

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

**PHASE ENTRY CONDITION:** Step 2A SHALL be entered only after TABLE A is closed.

*(What inertia conceals here: the missing Retry-After handler that turns a 30-second throttle
window into a 10-minute retry storm — invisible where the connector layer is mocked.)*

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing in backpressure analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A (complete Step 1A +
Step 1B), register the tier with all required columns, then continue.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |
| ... |                |              |           |                   |

A minimum of two hops SHALL be present. `Mechanism` SHALL be specific: queue-fill,
connection-hold, retry-amplification, dependency-stall, timeout-cascade.

**PHASE EXIT CONDITION:** Step 2A SHALL be considered closed when at least two hops are
documented with T-NN identifiers and specific mechanisms.

---

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

**PHASE ENTRY CONDITION:** Step 2B SHALL be entered after Step 2A PHASE EXIT CONDITION
is cleared. One row per TABLE A Tier-ID. No tier SHALL be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |
| T-02    |                     |                           |                                      |                                      |                               |

---

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

**PHASE ENTRY CONDITION:** Step 2C SHALL be entered after Step 2B is closed.

*(What inertia conceals here: the burst path that bypasses rate limiting because no test has
ever run at the volume where it fires.)*

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced in burst path analysis that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

At least one row SHALL be present. If no unprotected path exists, row 1 SHALL state the
conclusion with at least two named controls as evidence.

| Path-ID | Entry component | Gap reason (structural gap or named controls) | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|-----------------------------------------------|-------------------|-----------------------------|
| P-01    |                |                                               |                   |                             |

---

**Step 2D — TIER RISK RANKING**

**PHASE ENTRY CONDITION:** Step 2D SHALL be entered after Step 2C is closed.

All TABLE A tiers SHALL appear in the ranking, ordered by business risk, highest to lowest.
One sentence per tier with rationale SHALL be provided. For the top-ranked tier, `Failure
visibility window` and `Recovery time` from TABLE A SHALL be referenced.

---

**Step 2E — CASCADE SCENARIO**

**PHASE ENTRY CONDITION:** Step 2E SHALL be entered after Step 2D is closed.

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during cascade trace that are not in TABLE A are scope violations. An executor
SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Trace one concrete cascade from the 1x binding constraint. T-NN identifiers SHALL be used
throughout. Each causal link SHALL be stated explicitly. A minimum of three tiers SHALL be
present, each step caused by the previous.

---

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

**PHASE ENTRY CONDITION:** Step 2F SHALL be entered after Step 2E is closed.

For the 1x binding constraint tier: is Retry-After present and surfaced? If absent, the failure
mode SHALL be named precisely — retry storm (exponential backoff) vs. quota exhaustion
(circuit breaker).

---

**Step 2G — LOAD SHAPE COMPARISON**

**PHASE ENTRY CONDITION:** Step 2G SHALL be entered after Step 2F is closed.

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced during load shape analysis that are not in TABLE A are scope violations. An
executor SHALL NOT assign a new T-NN here. An executor SHALL return to TABLE A.

Using TABLE A's Limit values and Load-shape verdict column (classified at Step 1B), compare
1x nominal at two arrival patterns. Identical total count; only arrival distribution differs.

- **UNIFORM arrival** — state per-second arrival rate; state which tiers are HIT or SAT.
- **BURST arrival** — state the burst fraction and peak per-second rate; state which tiers
  are HIT or SAT and why.

At least one numeric comparison where status differs at identical total count SHALL be present.

---

**Step 2H — MITIGATION REGISTRY (TABLE F)**

**PHASE ENTRY CONDITION:** Step 2H SHALL be entered after Step 2G is closed.

A mitigation row that names a category of action ("add retry logic") requires further research
before it can be applied. A row that names the exact parameter can be applied immediately.

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — the exact configuration key, connector property, or API attribute
name SHALL be recorded here.

- *Violation type: category of action substituted for named parameter identifier (e.g.,
  "add retry logic" instead of `connector.retryPolicy`). All-neighbor contrast (C-36): the
  `Load-shape verdict` column's violation type (left neighbor, site 2) is a deferred verdict
  token — the classification act is placed at the wrong moment, routed to Step 2G rather than
  recorded at Step 1B. The STEP 4 C-24 finding schema's violation type (right neighbor, site 4)
  is a structural omission — a labeled slot position within a single finding entry is left
  empty or merged with adjacent content. This column's violation type is neither: the value is
  a string identifier, not a number; there is no timing constraint; and the failure is not
  about a slot within a structured finding. The failure is category substitution — naming the
  class of action where the specific deployable parameter name is required. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of action
  rather than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

**PHASE ENTRY CONDITION:** STEP 3 SHALL be entered only after Step 2H is closed.

*(What inertia conceals here: the integration test suite reporting green because it mocks the
connector layer; the load test running at 10% of production concurrency.)*

Execute two stages. Stage 1 SHALL pre-load artifact names; Stage 2 SHALL use them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts SHALL be named with structural properties before Stage 2 opens.

Catalog entry 1:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason it cannot reach the throttle behavior]

Catalog entry 2:
- **Artifact:** [specific artifact name]
- **Structural property:** [architectural reason]

"Stage 1 complete" SHALL be stated before Stage 2 opens.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason (Stage 1 artifact + property) | Test approach (component + volume + assertion) |
|--------|-------------------------------------------|-----------|--------------------------------------------------|------------------------------------------------|
| GAP-01 |                                           |           |                                                  |                                                |
| GAP-02 |                                           |           |                                                  |                                                |

---

**STEP 4 — INTEGRITY VERIFICATION**

**PHASE ENTRY CONDITION:** STEP 4 SHALL be entered only after Stage 2 of STEP 3 is complete.

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. An executor SHALL complete this block after Stage 2. Each downstream
section SHALL receive an individual verdict on a distinct verdict line, with evidence on a
distinct evidence line.

**C-24 format requirement:** Each field entry SHALL use two distinct labeled lines:
`- Verdict: [PASS / FAIL]`
`- If FAIL — [field label]: [list each finding]`

Each individual finding within a FAIL list MUST populate all three named slots:

```
INFORMAL-NAME:    [exact label used informally in the text]
SECTION:LOCATION: [step name and specific location within the step]
T-NN:             [the registered tier ID it should have referenced]
```

- *Violation type: missing slot identifier in finding entry — one or more named slot positions
  absent or collapsed into prose. All-neighbor contrast (C-36): TABLE F `Setting or API
  parameter`'s violation type (left neighbor, site 3) is category substitution — a task-class
  label occupies the parameter field. The STEP 4 C-13 audit FAIL field's violation type (right
  neighbor, site 5) is evidence absence — a FAIL verdict is issued at the aggregate level
  without enumerating the specific informal references found. This schema's violation type is
  distinct from both: the failure is not a wrong category in a parameter field and not an
  absent evidence list at aggregate level — a labeled slot position within a single finding
  entry is left empty or merged with adjacent content. An executor MUST NOT conflate these
  2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any named
  slot position — or presents findings as free-form prose — fails the identification schema.

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
  Adjacent contrast: the C-24 finding schema's violation type (left neighbor, site 4) is
  structural omission within a finding entry — a labeled slot is missing or collapsed into
  prose. The STEP 4 C-19 audit FAIL field's violation type (right neighbor, site 6) is verdict
  granularity collapse — individual step verdicts are merged into a single aggregate without
  per-step assessments. This audit field's violation type is distinct from both: the failure
  is not within a single finding (C-24's domain) and not about per-step verdict granularity
  (C-19's domain). The failure is at the aggregate reporting level — the FAIL verdict is
  correctly present but the specific informal references are not enumerated. An executor MUST
  NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does not
  enumerate specific informal references fails this audit field.

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
  contrast: the C-13 audit field's violation type (left neighbor, site 5) is evidence absence
  on FAIL — a FAIL verdict that correctly fires but names no specific findings. This field's
  violation type is verdict granularity collapse: per-step verdicts are merged into a single
  aggregate before the FAIL branch. C-13 fails on what the FAIL entry contains; C-19 fails
  on whether each step receives its own verdict line. Both fail at the audit level; each
  requires a different correction. Site 6 has one immediate neighbor — C-36 and C-38 do
  not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL — interleaving found: [describe where tier discovery and caller behavior appeared
  in the same step]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: this field covers all SHALL, SHALL NOT, MUST, MUST NOT, and PROHIBITED
obligation clauses in the prompt regardless of structural location — named enforcement block
headers, *Violation type* italic fields, inventory parenthetical notes, and PHASE ENTRY/EXIT
condition blocks. Clauses lacking a standalone block header are named by their exact containing
structure. Total enforcement directives in this prompt: 11.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
exact containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict:

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| TABLE A `Load-shape verdict` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| TABLE F `Setting or API parameter` column — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY — inventory verification obligation (parenthetical note) | SHALL verify | [PASS / FAIL] |
| STEP 4 C-24 finding schema — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 audit FAIL field — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 11 enforcement directives enumerated by their declared or containing-
structure names with individual per-directive verdicts. Aggregate statements are not used.
C-42 satisfied: all 6 primary-location directives cited by their verbatim declared block name
exactly as they appear in the prompt body — including criterion-ID parentheticals (e.g.,
"(C-17, C-19)" in step reminder names, "(C-16, C-20, C-23, C-26)" in the deferral prohibition
name). C-43 satisfied: all 5 non-primary-location directives discovered — TABLE A and TABLE F
*Violation type* field non-conflation directives, PRECISION-SITE INVENTORY parenthetical
obligation, and both STEP 4 *Violation type* field non-conflation directives (C-24 schema and
C-13 audit FAIL field) — named by their exact containing structure per C-43 requirement.)*
