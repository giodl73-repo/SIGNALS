# flow-throttle Variate — Round 17 (v17 rubric, C-01 through C-44)
**Date:** 2026-03-15
**Rubric:** v17 (C-01 through C-44, N_essential=5, N_recommended=3, N_aspirational=36)
**Baseline ceiling:** R16 V-05 (passes C-01 through C-43 under v16; fails C-44)

---

## State Analysis: What R16 Established vs. What R17 Must Add

**R16 V-05 coverage under v17 (confirmed):**
- C-01 through C-43: all pass
- C-44: not yet addressed — R16 V-05's C-41 audit cites five embedded-directive entries.
  Three use verbatim containing-structure labels from the prompt body:
  1. "TABLE A `Load-shape verdict` column" — verbatim column name from TABLE A's header row ✓
  2. "TABLE F `Setting or API parameter` column" — verbatim column name from TABLE F's header row ✓
  3. "PRECISION-SITE INVENTORY" — verbatim section header ✓

  Two use paraphrased/contextually-derived labels that do not appear as structural labels in
  the prompt body:
  4. "STEP 4 C-24 finding schema" — NOT verbatim; the prompt body's bold header for that
     sub-section is "**C-24 format requirement:**" — "finding schema" is a contextual
     derivation from the three-slot template that follows, not the declared structural label.
  5. "STEP 4 C-13 audit FAIL field" — NOT verbatim; the prompt body's bold header for that
     sub-section is "**C-13 compliance — Tier-ID threading:**" — "audit FAIL field" describes
     a sub-element within the section, not the section's declared label.

  C-44 requires the containing-structure name to be "the verbatim label as it appears in the
  prompt body — the exact text of the italic field header, table footnote label, table
  annotation marker, or other structural label — not a contextual description, positional
  paraphrase, or label derived by inference from surrounding content."

**Verbatim containing-structure label inventory:**

| # | Embedded directive location | Verbatim structural label in prompt body | R16 V-05 citation | C-44 status |
|---|----------------------------|------------------------------------------|-------------------|-------------|
| 1 | TABLE A `Load-shape verdict` *Violation type* field | Column header `Load-shape verdict` in TABLE A | `TABLE A \`Load-shape verdict\` column` | PASS ✓ |
| 2 | TABLE F `Setting or API parameter` *Violation type* field | Column header `Setting or API parameter` in TABLE F | `TABLE F \`Setting or API parameter\` column` | PASS ✓ |
| 3 | PRECISION-SITE INVENTORY parenthetical obligation | Section header `PRECISION-SITE INVENTORY` | `PRECISION-SITE INVENTORY` | PASS ✓ |
| 4 | STEP 4 C-24 schema *Violation type* field | Bold sub-header `C-24 format requirement:` | `STEP 4 C-24 finding schema` | FAIL ✗ |
| 5 | STEP 4 C-13 compliance *Violation type* field | Bold sub-header `C-13 compliance — Tier-ID threading:` | `STEP 4 C-13 audit FAIL field` | FAIL ✗ |

**Corrected verbatim citations for C-44 compliance:**
- Entry 4: `STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive`
- Entry 5: `STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive`

**Total enforcement directives: 11** (unchanged from R16; C-44 adds no new named blocks or
embedded clauses — it refines the citation precision requirement for existing entries 7-11)

---

## Round 17 Variation Map

| Variation | Axes | C-44 mechanism | Verbatim count (entries 7-11) | C-44 | Predicted composite |
|-----------|------|----------------|-------------------------------|------|---------------------|
| V-01 | Phrasing register — all 5 paraphrased | All 5 embedded entries use positional/contextual descriptors; 0 verbatim | 0/5 | FAIL | ~109.44/110 |
| V-02 | Output format — R16 V-05 exact citation pattern | Entries 7-9 verbatim; entries 10-11 paraphrased (same as R16 V-05) | 3/5 | FAIL | ~109.44/110 |
| V-03 | Lifecycle emphasis — verbatim for 4, paraphrase for entry 11 only | Entries 7-10 verbatim; entry 11 paraphrased | 4/5 | FAIL | ~109.44/110 |
| V-04 | Combined: single-analyst role + output format, entries 10-11 paraphrased | Structural variant; C-41 pattern same as V-02 | 3/5 | FAIL | ~109.44/110 |
| V-05 | All axes combined: all 5 verbatim | All 5 corrected to verbatim structural labels from prompt body | 5/5 | PASS | 110/110 |

**Single-axis questions:**

Q1 (V-01 vs R16 V-05): Does using step-location descriptors instead of verbatim structural
labels for all 5 embedded entries fail C-44? Hypothesis: yes — C-44 requires "the verbatim
label as it appears in the prompt body"; "Step 1B classification phase" is a location
descriptor, not a structural label appearing in the prompt; similarly for all 5. Predicted:
C-44 FAIL.

Q2 (V-02 vs V-01): Does correctly citing entries 7-9 with verbatim labels while leaving
entries 10-11 paraphrased (the R16 V-05 exact pattern) still fail C-44? Hypothesis: yes —
C-44 applies independently to each embedded-directive entry; partial verbatim compliance is
insufficient; any entry citing a containing structure by non-verbatim label fails. Predicted:
C-44 FAIL.

Q3 (V-03 vs V-02): Does correcting entry 10 to the verbatim "C-24 format requirement:" while
leaving entry 11 as "C-13 audit FAIL field" (paraphrase of "C-13 compliance — Tier-ID
threading:") still fail C-44? Hypothesis: yes — C-44's verbatim requirement applies to every
embedded-directive entry; the minimum failure threshold is one non-verbatim containing-
structure label regardless of how many others are correct. Predicted: C-44 FAIL.

Q4 (V-04 vs V-03): Does combining a structural role-sequence change with the V-02 citation
pattern fail C-44 on the same grounds as V-02? Hypothesis: yes — the structural change does
not affect the C-41 audit's verbatim-citation requirement; C-44 is about the audit table
entries, not the prompt structure. Predicted: C-44 FAIL.

Q5 (V-05): Do corrected verbatim citations for entries 10 ("STEP 4 C-24 format requirement:")
and 11 ("STEP 4 C-13 compliance — Tier-ID threading:") satisfy C-44 without regressions?
Hypothesis: yes — both use the exact text of bold section headers as they appear in the
prompt body; no structural criteria are affected by the citation correction in the audit table.
Predicted: C-44 PASS, composite 110/110.

---

## V-01 — Single Axis: Phrasing Register (All 5 Embedded Entries Paraphrased)

**Axis:** Phrasing register — the C-41 per-directive audit table cites all 5 embedded
non-primary-location directives using positional/contextual descriptors rather than verbatim
containing-structure labels. None of the 5 embedded entries uses the verbatim structural
label appearing in the prompt body; all 5 are step-location or content-category descriptions.
Primary-location directives (entries 1-6) retain verbatim declared block names.

**Hypothesis:** All 5 positional descriptors fail C-44 because none matches a structural
label appearing in the prompt body. "Step 1B classification phase" is not a structural label
for the Load-shape verdict column definition (the structural label is the TABLE A column
header `Load-shape verdict`). "PRECISION-SITE INVENTORY verification note" is close but
omits the exact label and adds a non-verbatim suffix. All 5 entries use descriptors derived
from surrounding content rather than from declared structural labels. C-43 passes (all 11
discovered); C-42 passes (primary-location entries verbatim); C-44 fails (0 of 5 embedded
entries verbatim). Predicted: C-44 FAIL. Composite = ~109.44/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

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
condition blocks. Clauses lacking a standalone block header are named by their containing
structure. Total enforcement directives in this prompt: 11.)*

*(C-44 note: this table cites all 5 embedded non-primary-location directives using
positional/contextual descriptors rather than the verbatim structural labels appearing in
the prompt body. "Step 1B classification phase" is a location descriptor, not the TABLE A
column header `Load-shape verdict`. "Step 2H mitigation section" is a positional descriptor,
not the TABLE F column header `Setting or API parameter`. "PRECISION-SITE INVENTORY
verification note" paraphrases the section header; the verbatim label is "PRECISION-SITE
INVENTORY". "STEP 4 finding-schema body" describes content, not the verbatim bold header
"C-24 format requirement:". "STEP 4 tier-threading compliance body" describes content, not
the verbatim bold header "C-13 compliance — Tier-ID threading:". C-44 fails: 0 of 5 embedded
entries use verbatim containing-structure labels.)*

For each enforcement directive in this prompt, verify that the primary directive uses RFC
2119-style normative language (SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED). An executor
SHALL enumerate each directive by its verbatim declared block name (for named blocks) or its
containing structure name (for embedded non-primary-location clauses) and record a
per-directive verdict:

| Directive block (verbatim declared name or containing structure) | Primary language used | C-40 verdict |
|-----------------------------------------------------------------|----------------------|-------------|
| REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17) | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19) | SHALL NOT | [PASS / FAIL] |
| Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B | PROHIBITED / SHALL | [PASS / FAIL] |
| Step 1B classification phase — *Violation type* non-conflation clause | MUST NOT | [PASS / FAIL] |
| Step 2H mitigation section — *Violation type* non-conflation clause | MUST NOT | [PASS / FAIL] |
| PRECISION-SITE INVENTORY verification note | SHALL verify | [PASS / FAIL] |
| STEP 4 finding-schema body — non-conflation clause | MUST NOT | [PASS / FAIL] |
| STEP 4 tier-threading compliance body — non-conflation clause | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 11 enforcement directives enumerated with individual per-directive
verdicts. C-42 satisfied: all 6 primary-location directives cited by verbatim declared block
name. C-43 satisfied: all 5 non-primary-location directives discovered. C-44 NOT satisfied:
entries 7-11 use positional/contextual descriptors — "Step 1B classification phase", "Step
2H mitigation section", "PRECISION-SITE INVENTORY verification note", "STEP 4 finding-schema
body", "STEP 4 tier-threading compliance body" — none is a verbatim structural label from the
prompt body.)*

---

## V-02 — Single Axis: Output Format (R16 V-05 Exact Citation Pattern — Entries 10-11 Paraphrased)

**Axis:** Output format — maximum table density throughout; C-41 audit uses the exact citation
pattern from R16 V-05: entries 7-9 (TABLE A, TABLE F, PRECISION-SITE INVENTORY) cite verbatim
structural labels from the prompt body; entries 10-11 (STEP 4 C-24 and C-13 sub-sections)
use paraphrased labels derived from context. This isolates the specific C-44 failure mode
present in R16 V-05 as a single-axis test.

**Hypothesis:** Entries 7-9 satisfy C-44 at those sites because "TABLE A `Load-shape verdict`
column", "TABLE F `Setting or API parameter` column", and "PRECISION-SITE INVENTORY" ARE
verbatim structural labels from the prompt body. But entries 10-11 still fail C-44: "STEP 4
C-24 finding schema" is not the verbatim bold header "C-24 format requirement:"; "STEP 4
C-13 audit FAIL field" is not the verbatim bold header "C-13 compliance — Tier-ID threading:".
C-44 requires all embedded-directive entries to use verbatim labels; partial correctness is
insufficient. Predicted: C-44 FAIL. Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

*(PRECISION-SITE INVENTORY: identical to V-01 — six sites, same hierarchy labels and violation
types, same verification obligation parenthetical.)*

*(STEP 1 — TIER REGISTRY: identical to V-01 structure. REGISTRY GAP PROHIBITION — Failure 5
prevention (C-17) block present. Step 1A GATE and PHASE EXIT CONDITION present. Failure 2 +
Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT STEP 1B block
present. Step 1B GATE and PHASE EXIT CONDITION present. All PHASE ENTRY CONDITIONS present.)*

*(STEP 2 through STEP 3: identical to V-01 — all sections present with PHASE ENTRY/EXIT
conditions, all four Standing enforcement reminder blocks at Steps 2A, 2C, 2E, 2G, all
*Violation type* italic fields and C-27 extension compliance failure conditions. TABLE F
`Setting or API parameter` *Violation type* field and C-27 extension failure condition
identical to V-01.)*

*(STEP 4 — INTEGRITY VERIFICATION through C-14 compliance: identical to V-01 — PHASE ENTRY
CONDITION, Failure 4 prevention block, C-24 format requirement with three-slot code block and
*Violation type* field, C-13 compliance with per-step verdicts and *Violation type* field,
C-19 compliance with C-25 format requirement and *Violation type* field, C-14 compliance.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-01. Total enforcement directives: 11.)*

*(C-44 note: entries 7-9 use verbatim structural labels from the prompt body — "TABLE A
`Load-shape verdict` column", "TABLE F `Setting or API parameter` column", and
"PRECISION-SITE INVENTORY" all appear as structural labels in the prompt. Entries 10-11
use paraphrased/derived labels: "STEP 4 C-24 finding schema" does not match the verbatim
bold header "**C-24 format requirement:**"; "STEP 4 C-13 audit FAIL field" does not match
the verbatim bold header "**C-13 compliance — Tier-ID threading:**". C-44 fails: 3 of 5
embedded entries verbatim; 2 of 5 use contextually-derived paraphrases. This is exactly the
R16 V-05 citation pattern.)*

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

*(C-41 satisfied: all 11 directives enumerated with per-directive verdicts. C-42 satisfied:
all 6 primary-location directives verbatim. C-43 satisfied: all 5 non-primary directives
discovered. C-44 NOT satisfied: "STEP 4 C-24 finding schema" paraphrases the verbatim bold
header "C-24 format requirement:"; "STEP 4 C-13 audit FAIL field" paraphrases the verbatim
bold header "C-13 compliance — Tier-ID threading:". Two embedded entries use derived rather
than verbatim structural labels.)*

---

## V-03 — Single Axis: Lifecycle Emphasis (Verbatim for 4 of 5, Entry 11 Paraphrased)

**Axis:** Lifecycle emphasis — explicit PHASE ENTRY/EXIT gate structure throughout; C-41 audit
corrects entry 10 to use the verbatim bold header "C-24 format requirement:" but retains entry
11 as "STEP 4 C-13 audit FAIL field" (paraphrase of the verbatim bold header "C-13 compliance
— Tier-ID threading:"). This is the minimum-failure test for C-44: four of five embedded
entries are verbatim; only the final C-13 entry remains paraphrased.

**Hypothesis:** Correcting entry 10 to the verbatim "C-24 format requirement:" partially
satisfies C-44 at that site. But entry 11 still fails: "C-13 audit FAIL field" is a
description of a sub-element within the C-13 compliance section — it names a condition
("FAIL field") rather than the section's declared structural label ("C-13 compliance —
Tier-ID threading:"). C-44 requires all embedded-directive entries to use verbatim labels;
even one paraphrase fails the criterion. Predicted: C-44 FAIL. Composite = ~109.44/110.

---

*(THE INERTIA PROBLEM: identical to V-01.)*

*(Role setup: identical to V-01.)*

*(PRECISION-SITE INVENTORY: identical to V-01.)*

*(STEP 1 through STEP 3: identical to V-01.)*

*(STEP 4 through C-14 compliance: identical to V-01.)*

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: identical to V-01. Total enforcement directives: 11.)*

*(C-44 note: entries 7-9 use verbatim structural labels ✓. Entry 10 corrected to verbatim
"STEP 4 C-24 format requirement:" — the exact text of the bold header "**C-24 format
requirement:**" as it appears in the prompt body ✓. Entry 11 retains "STEP 4 C-13 audit
FAIL field" — a paraphrase that describes a sub-element condition; the verbatim bold header
is "C-13 compliance — Tier-ID threading:" ✗. C-44 fails: 4 of 5 verbatim; 1 paraphrase
remains.)*

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
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 audit FAIL field — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 11 directives enumerated with per-directive verdicts. C-42 satisfied.
C-43 satisfied. C-44 NOT satisfied: "STEP 4 C-13 audit FAIL field" is not the verbatim bold
header "C-13 compliance — Tier-ID threading:" — it describes a sub-condition rather than
quoting the declared structural label. One paraphrase is sufficient to fail C-44.)*

---

## V-04 — Combined: Single-Analyst Role + Output Format (Entries 10-11 Paraphrased)

**Axis:** Combined — role sequence variation (single unified analyst role in Step 1, no
explicit Step 1A/Step 1B analyst split) and output format variation (narrative-first intro
before each table section), combined with the V-02 citation pattern in C-41 (entries 10-11
paraphrased). Tests whether the structural variation changes anything about C-44 compliance.

**Hypothesis:** The structural change (collapsing Step 1A/1B into a single analyst step)
does not affect the C-41 audit's verbatim-citation requirement for embedded directives.
C-44 is about the audit table entries, not the prompt structure. Entries 10-11 still use
paraphrased labels ("STEP 4 C-24 finding schema", "STEP 4 C-13 audit FAIL field"); the
verbatim bold headers in the prompt body remain "C-24 format requirement:" and "C-13
compliance — Tier-ID threading:" regardless of structural variant. Predicted: C-44 FAIL.
Composite = ~109.44/110.

---

**THE INERTIA PROBLEM**

*(Identical to V-01.)*

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
the rate-limited system described in the signal. Treat the stated request volume as 1x
nominal; also analyze at 2x and 5x.

Every table cell SHALL be filled. Produce sections in the order shown.

---

**PRECISION-SITE INVENTORY**

*(Required before any table is defined — C-33 + C-35 + C-37 + C-39. Every precision-requiring
site enumerated in document order. `C-27 hierarchy` column uses C-31 labeling format.)*

| # | Site | C-27 hierarchy | Required precision | Violation type |
|---|------|----------------|--------------------|----------------|
| 1 | TABLE A `Limit (number + unit)` (Step 1) | `primary (C-27):` | Numeric rate with unit (e.g., "1,000 req/min") | Vague label substituted for numeric value (e.g., "limited" in place of "1,200 req/min") |
| 2 | TABLE A `Load-shape verdict` (Step 1) | `extension (C-27 extension):` | SHAPE-NEUTRAL or SHAPE-SENSITIVE recorded at Step 1 | Deferred verdict token — entry routes classification to Step 2G rather than recording verdict at Step 1 |
| 3 | TABLE F `Setting or API parameter` (Step 2H) | `extension (C-27 extension):` | Specific connector setting, policy parameter, or API attribute name | Category of action substituted for named parameter identifier (e.g., "add retry logic" instead of `connector.retryPolicy`) |
| 4 | STEP 4 C-24 finding schema | `extension (C-27 extension):` | All three slots populated: INFORMAL-NAME, SECTION:LOCATION, T-NN | Missing slot identifier — one or more named slot positions absent or collapsed into prose |
| 5 | STEP 4 C-13 audit FAIL entries | `extension (C-27 extension):` | Per-finding identification with specific informal references | Binary FAIL flag without enumeration of the specific informal references found |
| 6 | STEP 4 C-19 audit FAIL entries | `extension (C-27 extension):` | Per-step inline verdict before aggregate | Aggregate verdict without per-step inline verdict sequence |

*(Six precision-requiring sites. An executor SHALL verify that each definition block's label
matches the `C-27 hierarchy` value in this row before producing that block.)*

---

**STEP 1 — TIER REGISTRY AND LOAD-SHAPE CLASSIFICATION**

*(Single analyst role: identify all rate-limiting components, record numeric limits and
volume-band status, then immediately classify load-shape for each tier before the registry
closes. Both sub-tasks are part of Step 1; the registry SHALL be closed when both are
complete.)*

**REGISTRY GAP PROHIBITION — Failure 5 prevention (C-17):** Tiers discovered during Step 2
are scope violations — evidence that the enumeration phase was incomplete. PROHIBITED:
assigning a new T-NN during Step 2 as a fill-in step. An executor SHALL return to TABLE A,
register the tier with all columns filled, and SHALL restart from the point of discovery.
This prohibition SHALL be restated at each Step 2 section where mid-phase discovery could
occur.

**TABLE A — THROTTLE TIER INVENTORY ACROSS VOLUME BANDS**

| Tier-ID | Component | Limit (number + unit) | Scope | STATUS 1x | STATUS 2x | STATUS 5x | Binding at band | Load-shape verdict | Failure visibility window | Recovery time |
|---------|-----------|----------------------|-------|-----------|-----------|-----------|-----------------|-------------------|--------------------------|---------------|
| T-01    |           |                      |       |           |           |           |                 |                   |                          |               |
| T-02    |           |                      |       |           |           |           |                 |                   |                          |               |
| ...     |           |                      |       |           |           |           |                 |                   |                          |               |

Column definitions:
- `Tier-ID` — Assign T-01, T-02, ... and SHALL be used verbatim in every downstream section.
- `Limit (number + unit)` — a specific number with a unit (e.g., "1,000 req/min").
  - *Violation type: vague label substituted for numeric value. Single-adjacency (site 2 right
    neighbor only) — C-36 and C-38 SHALL NOT apply.*
  - Compliance failure condition `primary (C-27):` An entry using a vague label fails this
    column's precision requirement.
- `Load-shape verdict` — SHALL be populated at Step 1 (not deferred to Step 2G). State
  SHAPE-NEUTRAL or SHAPE-SENSITIVE with numeric rate differential and mechanism.
  - **Failure 2 + Failure 6 prevention (C-16, C-20, C-23, C-26) — CLASSIFICATION REQUIRED AT
    STEP 1B:** An executor SHALL assign `Load-shape verdict` for every row at Step 1.
    PROHIBITED: deferring to Step 2G.
  - *Escape-route story (C-23):* The escape route is the "STATUS tracks volume thresholds"
    frame — TABLE A appears to be a pure volume-threshold table, making load-shape
    classification appear out of scope. Both STATUS columns and the named "LOAD SHAPE
    COMPARISON" section title route shape analysis to Step 2G.
  - *Structural rejection proof (C-26):* Deferral is self-defeating. Step 2G depends on
    per-tier Load-shape verdicts to produce its numeric comparison; deferring creates a
    circular dependency where the receiving section depends on the value it was supposed to
    receive.
  - *Violation type: deferred verdict token — classification routed to Step 2G rather than
    recorded at Step 1. All-neighbor contrast (C-36): `Limit`'s violation type (left neighbor,
    site 1) is value-absence; TABLE F `Setting or API parameter`'s (right neighbor, site 3)
    is parameter-specificity. This column's failure is purely temporal. An executor MUST NOT
    conflate these 2 failure modes.*
  - Compliance failure condition `extension (C-27 extension):` A Load-shape verdict left blank
    or deferred at the end of Step 1 fails the registration-time classification requirement.
- `STATUS Nx` — OK / HIT / SAT; SHALL shift between at least two bands.
- `Binding at band` — lowest band at which this tier is the primary bottleneck. N/A if never.
- `Failure visibility window` — how quickly saturation becomes observable.
- `Recovery time` — how long until normal operation resumes.

**STEP 1 GATE:** TABLE A SHALL be considered closed when every row has a non-placeholder
value in all columns including `Load-shape verdict`. An executor SHALL NOT open Step 2 until
this gate is cleared.

---

**STEP 2 — ANALYSIS PHASES**

The tier registry is closed. An executor SHALL use T-NN identifiers from TABLE A throughout.

**Step 2A — BACKPRESSURE PROPAGATION TRACE (TABLE B)**

*(Backpressure: the missing Retry-After handler that turns a 30-second throttle window into
a 10-minute retry storm.)*

**Step 2A — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
appearing here that are not in TABLE A are scope violations. An executor SHALL NOT assign a
new T-NN here. An executor SHALL return to TABLE A.

| Hop | From (Tier-ID) | To component | Mechanism | Observable effect |
|-----|----------------|--------------|-----------|-------------------|
| 1   |                |              |           |                   |
| 2   |                |              |           |                   |

Minimum two hops. `Mechanism` SHALL be specific: queue-fill, connection-hold,
retry-amplification, dependency-stall, timeout-cascade.

**Step 2B — USER EXPERIENCE CATALOG (TABLE C)**

One row per TABLE A Tier-ID. No tier SHALL be omitted.

| Tier-ID | Error code or signal | Retry-After present? (Y/N) | Retry-After surfaced to caller? (Y/N) | Visible in run history? (Y/N/SILENT) | Failure if Retry-After ignored |
|---------|---------------------|---------------------------|--------------------------------------|--------------------------------------|-------------------------------|
| T-01    |                     |                           |                                      |                                      |                               |

**Step 2C — UNPROTECTED BURST PATHS (TABLE D)**

*(Burst paths: the path never rate-limited because no test ran at the volume where it fires.)*

**Step 2C — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
referenced here that are not in TABLE A are scope violations. An executor SHALL NOT assign
a new T-NN here. An executor SHALL return to TABLE A.

At least one row. If no unprotected path exists, name at least two controls as evidence.

| Path-ID | Entry component | Gap reason | Tier-IDs involved | Consequence at burst volume |
|---------|----------------|------------|-------------------|-----------------------------|
| P-01    |                |            |                   |                             |

**Step 2D — TIER RISK RANKING**

All TABLE A tiers, ordered by business risk. One sentence with rationale per tier.
Top-ranked tier: reference `Failure visibility window` and `Recovery time` from TABLE A.

**Step 2E — CASCADE SCENARIO**

**Step 2E — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced here that are not in TABLE A are scope violations. An executor SHALL NOT assign
a new T-NN here. An executor SHALL return to TABLE A.

Trace one cascade from the 1x binding constraint. T-NN identifiers throughout. Explicit
causal links. Minimum three tiers, each step caused by the previous.

**Step 2F — RETRY-AFTER GAP ASSESSMENT**

For the 1x binding constraint: is Retry-After present and surfaced? Name the failure mode
precisely: retry storm (exponential backoff) vs. quota exhaustion (circuit breaker).

**Step 2G — LOAD SHAPE COMPARISON**

**Step 2G — Standing enforcement reminder — REGISTRY GAP PROHIBITED (C-17, C-19):** Tiers
introduced here that are not in TABLE A are scope violations. An executor SHALL NOT assign
a new T-NN here. An executor SHALL return to TABLE A.

Using TABLE A `Load-shape verdict` (classified at Step 1), compare 1x nominal at two patterns.
Identical total count; only arrival distribution differs. At least one numeric comparison where
status differs at identical total count SHALL be present.

**Step 2H — MITIGATION REGISTRY (TABLE F)**

| MR-ID | Source | Gap type | Component | Setting or API parameter | Change | Expected outcome |
|-------|--------|----------|-----------|--------------------------|--------|-----------------|
| MR-01 |        |          |           |                          |        |                 |
| MR-02 |        |          |           |                          |        |                 |

`Setting or API parameter` — exact configuration key, connector property, or API attribute.

- *Violation type: category of action substituted for named parameter identifier. All-neighbor
  contrast (C-36): `Load-shape verdict`'s violation type (left neighbor, site 2) is a deferred
  verdict token. The STEP 4 C-24 finding schema's violation type (right neighbor, site 4) is
  a structural omission. This column's failure is category substitution. An executor MUST NOT
  conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A row naming a category of action
  rather than a specific parameter identifier fails this column's precision requirement.

---

**STEP 3 — TEST COVERAGE GAP ANALYSIS**

*(Test gaps: the suite reporting green because it mocks the connector layer.)*

Execute two stages. Stage 1 SHALL pre-load artifact names; Stage 2 SHALL use them.

**STAGE 1 — TEST INFRASTRUCTURE INVENTORY**

Gate: at least two artifacts with structural properties before Stage 2.

- **Artifact 1:** [name] / **Structural property:** [architectural reason]
- **Artifact 2:** [name] / **Structural property:** [architectural reason]

"Stage 1 complete" SHALL be stated before Stage 2.

**TABLE E — TEST COVERAGE GAP REGISTRY**

| GAP-ID | Throttle behavior (Tier-ID + failure mode) | Test type | Structural reason | Test approach |
|--------|-------------------------------------------|-----------|-------------------|---------------|
| GAP-01 |                                           |           |                   |               |
| GAP-02 |                                           |           |                   |               |

---

**STEP 4 — INTEGRITY VERIFICATION**

**Failure 4 prevention (C-15, C-18, C-22, C-24, C-25) — per-section compliance audit.**
Self-contained block. Each downstream section SHALL receive an individual verdict on a
distinct verdict line, with evidence on a distinct evidence line.

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
  parameter`'s violation type (left neighbor, site 3) is category substitution. The STEP 4
  C-13 audit FAIL field's violation type (right neighbor, site 5) is evidence absence.
  This schema's violation type is structural omission within a finding entry. An executor
  MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A finding that omits any named
  slot position fails the identification schema.

---

**C-13 compliance — Tier-ID threading:**

Step 2A (TABLE B): [Verdict / If FAIL — informal references found: list]
Step 2B (TABLE C): [Verdict / If FAIL — informal references found: list]
Step 2C (TABLE D): [Verdict / If FAIL — informal references found: list]
Step 2D (TIER RISK RANKING): [Verdict / If FAIL — informal references found: list]
Step 2E (CASCADE SCENARIO): [Verdict / If FAIL — informal references found: list]
Step 2G (LOAD SHAPE COMPARISON): [Verdict / If FAIL — informal references found: list]

Unregistered tiers introduced after TABLE A closed:
- Verdict: [PASS / FAIL]
- If FAIL — unregistered tiers found: [list each: "[tier name] introduced at [step]"]

- *Violation type: binary FAIL flag without enumeration of specific informal references.
  Adjacent contrast: the C-24 finding schema's violation type (left neighbor, site 4) is
  structural omission within a finding entry. The STEP 4 C-19 audit FAIL field's violation
  type (right neighbor, site 6) is verdict granularity collapse. This field's failure is
  evidence absence at the aggregate level. An executor MUST NOT conflate these 2 failure modes.*
- Compliance failure condition `extension (C-27 extension):` A FAIL verdict that does not
  enumerate specific informal references fails this audit field.

**C-19 compliance — distributed reminder audit:**

**C-25 format requirement:** Individual inline verdict per step before aggregate.

- Step 2A: [Y / N] / Step 2C: [Y / N] / Step 2E: [Y / N] / Step 2G: [Y / N]
- If any N: Verdict: FAIL / Missing steps: [list]

- *Violation type: aggregate verdict without per-step inline verdict sequence. Adjacent
  contrast: C-13 field's violation type (left neighbor, site 5) is evidence absence on FAIL.
  This field's violation type is verdict granularity collapse. Site 6 has one immediate
  neighbor — C-36 and C-38 do not apply.*
- Compliance failure condition `extension (C-27 extension):` A single aggregate verdict
  without per-step inline verdicts fails the C-25 format requirement.

**C-14 compliance — Perspective separation:**
- Verdict: [PASS / FAIL]
- If FAIL: [describe interleaving location]

**C-40 / C-41 compliance — Per-directive normative-register audit:**

*(C-43 discovery scope: all SHALL, SHALL NOT, MUST, MUST NOT, PROHIBITED clauses regardless
of location. Total: 11 directives.)*

*(C-44 note: entries 7-9 verbatim ✓; entries 10-11 use paraphrased labels — same V-02
pattern. "STEP 4 C-24 finding schema" is not the verbatim bold header "C-24 format
requirement:"; "STEP 4 C-13 audit FAIL field" is not the verbatim bold header "C-13
compliance — Tier-ID threading:". C-44 FAIL.)*

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

*(C-41 satisfied. C-42 satisfied. C-43 satisfied. C-44 NOT satisfied: entries 10-11
paraphrased — same failure mode as V-02; structural variant does not affect the audit table's
verbatim-citation obligation.)*

---

## V-05 — All Axes Combined (C-44 Full Verbatim Compliance)

**Axis:** Full combination — V-04's single-analyst role sequence, V-01's table-dense output
format with PHASE ENTRY/EXIT lifecycle gates (from R16 V-05 base), RFC 2119 register
throughout, and a STEP 4 C-41 compliance field that corrects all 5 embedded-directive entries
to use verbatim structural labels from the prompt body. Entries 10 and 11 are corrected:
entry 10 cites "STEP 4 C-24 format requirement:" (the exact text of the bold header
`**C-24 format requirement:**`); entry 11 cites "STEP 4 C-13 compliance — Tier-ID threading:"
(the exact text of the bold header `**C-13 compliance — Tier-ID threading:**`).

**Hypothesis:** All 5 embedded-directive entries now cite verbatim structural labels from the
prompt body. Entries 7-9 were already verbatim in R16 V-05; entries 10-11 are now corrected.
No structural criteria are affected by the audit table correction. C-42 and C-43 remain
satisfied. C-44 passes. Predicted: C-44 PASS, composite 110/110.

---

**THE INERTIA PROBLEM**

Throttle failures reach production undiscovered because the system passed at development and
staging volumes. Teams reason: "it worked in dev" — and skip the analysis. The first
production incident is the discovery mechanism. That is the status quo this skill exists to
displace.

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

*(C-44 compliance note: all 5 embedded non-primary-location directives are cited using the
verbatim structural labels as they appear in the prompt body. Entry 7: "TABLE A `Load-shape
verdict` column" — verbatim column name from TABLE A header row. Entry 8: "TABLE F `Setting
or API parameter` column" — verbatim column name from TABLE F header row. Entry 9:
"PRECISION-SITE INVENTORY" — verbatim section header. Entry 10: "STEP 4 C-24 format
requirement:" — verbatim bold sub-header "**C-24 format requirement:**" as it appears in
STEP 4. Entry 11: "STEP 4 C-13 compliance — Tier-ID threading:" — verbatim bold sub-header
"**C-13 compliance — Tier-ID threading:**" as it appears in STEP 4. No contextual
derivations or paraphrases in entries 7-11.)*

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
| STEP 4 C-24 format requirement: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |
| STEP 4 C-13 compliance — Tier-ID threading: — *Violation type* field non-conflation directive | MUST NOT | [PASS / FAIL] |

If any row is FAIL: state the specific phrase found and its normative replacement.

*(C-41 satisfied: all 11 enforcement directives enumerated by their declared or containing-
structure names with individual per-directive verdicts. Aggregate statements are not used.
C-42 satisfied: all 6 primary-location directives cited by their verbatim declared block name
exactly as they appear in the prompt body — including criterion-ID parentheticals. C-43
satisfied: all 5 non-primary-location directives discovered — TABLE A and TABLE F *Violation
type* field non-conflation directives, PRECISION-SITE INVENTORY parenthetical obligation, and
both STEP 4 *Violation type* field non-conflation directives — named by their exact containing
structure. C-44 satisfied: all 5 embedded-directive entries cite their containing structures
using the verbatim structural labels from the prompt body — "TABLE A `Load-shape verdict`
column", "TABLE F `Setting or API parameter` column", "PRECISION-SITE INVENTORY",
"STEP 4 C-24 format requirement:" (verbatim bold header), and "STEP 4 C-13 compliance —
Tier-ID threading:" (verbatim bold header). No contextually-derived or paraphrased container
labels remain.)*
