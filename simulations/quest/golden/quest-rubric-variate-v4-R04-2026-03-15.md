# quest-rubric Variate — Round 4 against rubric v4

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v4 (C-01 through C-22; essential C-01–C-05)
**Round:** R4 — 3 single-axis passes + 2 combination passes

**Round 4 design note:** Round 3 produced four excellence signals absorbed into v4 as aspirational
criteria: C-19 (named-block artifact architecture, from V-02/V-04), C-20 (gate must block not
repair, from V-02), C-21 (cross-criterion audit consolidation, from V-03/V-05), C-22 (structural
enforcement paired with behavioral anti-deferral instruction, from V-01/V-04/V-05). Round 3's
anchor was V-03 (role-sequence with Author/Auditor separation and Discriminating Element column),
and the R3 combination roadmap nominated V-03×V-02 and V-01×V-03×V-02 as Round 4 priorities.
Round 4 reframes those combinations around the new target criteria: C-19 requires heading-scan
block architecture (strengthening C-15 beyond content inspection), C-20 requires forward-blocking
gate language (not retroactive repair), C-21 requires a single consolidated audit table (not
distributed per-criterion sections), and C-22 requires both a structural ordering constraint and
an explicit prohibition of batch-deferral. Three single-axis variations isolate one mechanism
each; two combinations test whether the mechanisms compound.

---

## Round 4 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | output-format | single-axis | Named blocks with heading-scan Phase 7 audit (pattern matching, not content inspection) | C-19 |
| V-02 | lifecycle-emphasis | single-axis | Forward-blocking per-criterion gates; calibration pair sub-step names the prohibited batch-deferral pattern | C-20, C-22 |
| V-03 | role-sequence | single-axis | Auditor reads all Author criteria before producing a single contiguous consolidated audit table | C-21 |
| V-04 | output-format × lifecycle-emphasis | combination (V-01 × V-02) | Heading-scan blocks + forward-blocking gates + anti-deferral prohibition | C-19, C-20, C-22 |
| V-05 | role-sequence × output-format × lifecycle-emphasis | combination (V-03 × V-01 × V-02) | Full three-axis: heading-scan blocks + forward-blocking gates + anti-deferral + consolidated audit table | C-19, C-20, C-21, C-22 |

**Anchor designation (preliminary):** V-03. See anchor section at end.

---

## V-01 — Output Format: Heading-Scan Block Architecture

**axis:** output-format
**hypothesis:** C-19 tightens C-15's detectability guarantee. C-15 (R2, V-03) requires mandatory
check outputs to appear as independent artifacts before the criterion row — omission is detectable
as a structural gap. C-19 specifies the mechanism: the blocks must use named markdown section
headings (`### INERTIA-RECORD [C-NN]`) so a heading scan — without reading content — catches the
absence. R3 V-02 introduced named blocks and a Phase 7 block audit, but Phase 7's check could be
satisfied by reading block content ("confirm the block is present and complete"). C-19 closes the
gap: the audit must check by heading pattern, not by prose evaluation. A reviewer who only scans
section headings should detect every skipped check. This variation makes the heading-pattern
requirement explicit in Phase 2 instructions and rewrites Phase 7 as a heading-pattern scan that
lists exact patterns to match — not a prose content check. Failure condition: if C-19 pass rates
do not improve relative to R3 V-02, the heading-pattern specification in Phase 7 adds no
detectability benefit beyond content inspection.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable systematic scoring with independently auditable sub-step outputs,
each verifiable by section-heading scan without reading prose content.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact type and its key fields.
2. What lifecycle phases does it have? Name them in order.
3. What would a completely non-functional output look like? Name the failure, not the absence
   of quality.

**PHASE 1: FAILURE MODES**

List failure modes — specific, detectable ways the output can fail to function as intended.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+ if additional failure modes exist]
```

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 2 until at least 3 blocking and 2 degrading failure modes are listed.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

For each essential criterion, produce the three named section blocks below in the exact order
shown, then record the criterion row. The blocks must appear before the row. Use the exact heading
pattern — the heading text including brackets is what makes structural omission scannable.

---

**Block sequence per criterion (repeat for each C-NN):**

```
### INERTIA-RECORD [C-NN]
Draft condition: [the pass condition text as first written]
Inertia test: Could a rubric containing only "the output is clear and comprehensive"
  pass this condition? [YES / NO]
If YES — revised condition: [revision naming a count, field name, or enumeration
  from this skill's output contract; re-run until NO]
Final condition: [the condition that produced NO]
Skill-specific element: [the count, field name, structural pattern, or enumeration
  from this skill's contract that makes this condition non-generic]
```

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [pass condition text applying to any artifact — belongs to the Status-Quo Rubric,
  not this skill's rubric]
GROUNDED: [pass condition naming the skill-specific element from INERTIA-RECORD above;
  must reference the target skill by name or by a term from its output contract]
```

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [criterion text] | [category] | essential | [final condition
  from INERTIA-RECORD above] |
```

After producing all three blocks for C-NN, move to the next criterion and repeat.

---

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Standard five-field table format. Named blocks not required.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Standard five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

**PHASE 7: HEADING-SCAN AUDIT**

Scan the output for section headings matching the patterns listed below. This is a pattern scan,
not a content review — a heading is present or absent; its content is not evaluated here.

For each essential criterion C-NN (fill in the NN values from Phase 2):

```
Required headings for C-01:
  - [ ] ### INERTIA-RECORD [C-01]   (must appear before ### CALIBRATION-PAIR [C-01])
  - [ ] ### CALIBRATION-PAIR [C-01] (must appear before ### CRITERION [C-01])
  - [ ] ### CRITERION [C-01]

Required headings for C-02:
  - [ ] ### INERTIA-RECORD [C-02]
  - [ ] ### CALIBRATION-PAIR [C-02]
  - [ ] ### CRITERION [C-02]

[Continue for each essential criterion]
```

For any heading that is absent: write the missing named block now using the exact heading pattern
shown, then re-check. A criterion whose `### INERTIA-RECORD [C-NN]` or `### CALIBRATION-PAIR [C-NN]`
heading is absent is structurally incomplete regardless of its table row content.

The audit is complete when every required heading pattern is present and correctly ordered.

---

## V-02 — Lifecycle Emphasis: Forward-Blocking Gates + Named Anti-Deferral Prohibition

**axis:** lifecycle-emphasis
**hypothesis:** C-20 and C-22 identify two adjacent problems in gate design. C-20: a retroactive
repair step ("if block missing, write it now") is not a gate — it detects past omissions after
criterion rows are written, preserving criterion-first, check-second ordering. Gates must be
forward-blocking, positioned before the criterion row is produced. C-22: structural ordering
alone (calibration pair block before criterion block) permits batch-deferral — a builder can
produce all calibration pairs after all pass conditions are finalized, then write the blocks in
batch before starting Phase 3. The rubric must explicitly name this prohibited pattern, not just
require temporal proximity. R3 V-01 had anti-deferral language ("write it now, while the pass
condition is in working memory") but did not name the prohibited behavior. C-22 closes the gap:
the instruction must say "Do not produce all calibration pairs after all pass conditions are
finalized." Failure condition: if C-20 and C-22 pass rates do not both improve relative to R3
V-01, the explicit prohibition of batch-deferral adds no compliance benefit over "write it now."

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable two independent evaluators to reach the same pass/fail verdict for
any skill output without discussion.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact type and its key fields.
2. What lifecycle phases does it have? Name them in order.
3. What would a completely non-functional output look like? Name the failure, not the absence
   of quality.

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+ if additional failure modes exist]
```

Minimum: 3 blocking, 2 degrading.

**PHASE 2 ENTRY GATE — DO NOT begin writing criteria until all three boxes are checked:**

- [ ] At least 3 blocking failure modes are present in Phase 1
- [ ] At least 2 degrading failure modes are present in Phase 1
- [ ] At least 3 distinct categories from the target skill's output contract are identifiable
      (list them: ___, ___, ___)

This gate is forward-blocking: entering Phase 2 without satisfying it produces criteria that miss
the skill's actual failure surface. Check all three boxes before writing a single criterion.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

For each essential criterion, complete sub-steps 2a through 2d in order. Sub-step 2b does not
begin until 2a is written. The criterion is not recorded in the summary table until sub-step 2d
clears. These are forward-blocking gates: you cannot record the criterion row until each gate
condition is satisfied — these are not post-hoc checks.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition text: a specific, observable outcome an evaluator can verify without
subjective judgment. State what to look for and what constitutes a pass.

**Sub-step 2b — Apply the inertia test.**

Ask: Could a rubric containing only "the output is clear and comprehensive" pass this condition?

- If YES: the condition is generic. Revise to name a count, field name, structural element, or
  enumeration from this skill's output contract. Re-run the test until the answer is NO.
- If NO: condition is skill-specific. Proceed.

Record: `Inertia test: PASS [NO — condition requires {skill-specific element}]`

**Sub-step 2c — Write the calibration pair.**

Write it now — immediately after drafting this pass condition, before sub-step 2d, before moving
to the next criterion. Do not produce all calibration pairs after all pass conditions are
finalized: each pair belongs to the criterion it was derived alongside, while that pass condition
is still in working memory.

```
GENERIC: [pass condition text that applies to any artifact — belongs to the Status-Quo Rubric]
GROUNDED: [pass condition naming the skill-specific element from sub-step 2b; references the
  target skill by name or by a term from its output contract]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT advance to the next criterion until both conditions are satisfied:**

- [ ] Sub-step 2b result is PASS [NO] — inertia test survived on original or revised condition
- [ ] Sub-step 2c calibration pair appears in the output above this line, written immediately
      after sub-step 2b — not deferred to after the current criterion is recorded in the table

After both conditions are confirmed, record the criterion:

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

Repeat sub-steps 2a–2d for each essential criterion. Do not move to Phase 3 until all essential
criteria have cleared sub-step 2d.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Five-field table format. Inertia test applies; calibration pair
and inline documentation are not required.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-03 — Role Sequence: Consolidated Single Audit Table

**axis:** role-sequence
**hypothesis:** C-21 tightens C-18's reasoning-capture requirement. C-18 (R2, V-05) requires the
audit artifact to capture the discriminating element for each condition — not only pass/fail
verdicts. C-21 requires that reasoning to be consolidated in a single table where all criteria
appear as rows, enabling a maintainer to scan across criteria simultaneously and detect systemic
patterns (e.g., every criterion anchors to counts but no criterion anchors to named field
patterns). R3 V-03 and V-05 both produce Audit Tables. But the instruction structure allowed a
builder to process one criterion at a time: read the Author's C-01, audit C-01, add a row; read
C-02, audit C-02, add a row. This produces the correct table content but may be written as
distributed sections rather than a contiguous block. C-21 requires the Auditor to read ALL Author
criteria first, then produce the audit table as a single contiguous block — so cross-criterion
patterns are visible at write time, not only at read time. Failure condition: if C-21 pass rates
do not improve relative to R3 V-03, the "read all first" instruction adds no benefit over
per-criterion Auditor processing.

---

You are building a scoring rubric for a Signal skill. Two phases operate in sequence: an Author
phase produces all criteria; an Auditor phase reads all Author criteria simultaneously and
produces a single consolidated audit table. Both outputs appear in the final document.

**Why two phases?**

Writing criteria for coverage (do the criteria address the right failure modes?) and auditing
criteria for specificity (is each pass condition discriminating?) are competing cognitive demands.
The Author focuses on coverage without self-interrupting to evaluate specificity. The Auditor
reads all criteria as a set before writing any audit output, enabling cross-criterion analysis
that per-criterion sequential auditing cannot produce.

---

### AUTHOR PHASE

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output non-functional?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT advance to Author Phase 2 until this minimum is met.**

**AUTHOR PHASE 2: DRAFT CRITERIA**

Write all criteria. Each essential criterion targets a distinct failure mode from Author Phase 1.
Focus on coverage: ensure the essential criteria collectively surface all blocking failure modes.
Do not self-audit pass conditions for specificity — the Auditor handles that.

*Essential criteria (3-5):*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

*Recommended criteria (2-3):*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

*Aspirational criteria (1-2):*

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### END AUTHOR PHASE

---

### AUDITOR PHASE

Read all essential pass conditions from Author Phase 2. Read them all before writing any audit
output. Then produce the Audit Table as a single contiguous block — one table, all criteria as
rows. Do not write audit rows one at a time alongside the criteria; the table must be producible
as a unit after reading the full set.

**Why read all before writing?** Cross-criterion patterns — every condition anchors to counts but
none to named field patterns; every condition checks presence but none checks order — are only
visible when all criteria are in view simultaneously. Per-criterion sequential auditing misses
systemic gaps.

**Inertia test (apply to each essential pass condition):**

Could a rubric containing only "the output is clear and comprehensive" pass this condition?
- YES: condition is generic. Identify the revision naming a count, field, pattern, or enumeration
  from this skill's contract.
- NO: condition is skill-specific. Name the element that makes it discriminating.

**Audit Table (single contiguous block — all criteria as rows):**

| Criterion ID | Pass Condition (quoted from Author phase) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------------------------|--------------|----------------------|-------------------|-------------------|

**Column definitions:**
- *Inertia Test*: YES (generic) or NO (skill-specific)
- *Discriminating Element*: the count, field name, structural pattern, or enumeration from this
  skill's output contract that makes the condition non-generic. Required for every NO result.
  If YES, leave blank and fill Revised Condition instead.
- *Revision Required?*: YES or NO
- *Revised Condition*: the rewritten condition for YES-flagged rows; blank otherwise

After completing the Audit Table, scan across the Discriminating Element column. Note any
patterns: if multiple conditions share the same discriminating element type (e.g., all anchor to
counts), flag any category under-represented in the essential criteria.

**Cross-criterion pattern note (required):** [after scanning the completed table, write one
sentence noting whether the discriminating elements are varied or cluster in one type]

**Auditor Calibration Pair** — for the essential criterion with the highest-stakes failure mode:

```
GENERIC: [the condition in its weakest surviving form — Status-Quo Rubric territory]
GROUNDED: [the Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to the final rubric section until:**

- [ ] Every essential criterion in the Audit Table shows Inertia Test = NO (original or revised)
- [ ] The Discriminating Element column is filled for every NO-flagged row
- [ ] The cross-criterion pattern note is written

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with Auditor-revised pass conditions substituted where
the Audit Table shows Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

---

## V-04 — Output Format × Lifecycle Emphasis (V-01 × V-02, Combination)

**axis:** output-format × lifecycle-emphasis
**hypothesis:** V-01 (output-format) requires named blocks with heading-scan verification: a
missing block is a missing section heading detectable by pattern matching, not content evaluation.
V-02 (lifecycle-emphasis) requires forward-blocking per-criterion gates with explicit prohibition
of batch-deferral. They address related but distinct failure modes: V-01 makes omission
structurally visible after the fact (a missing heading is detectable); V-02 prevents the omission
in the first place (a forward gate blocks advancement before the block is produced). V-01 catches
V-02's gate failures as a structural backstop; V-02 prevents the scenarios V-01 would catch.
Combined, they target C-19 (heading-scan detectability), C-20 (forward-blocking gate position),
and C-22 (structural ordering + named anti-deferral prohibition) simultaneously. Failure condition:
if C-19 pass rates do not exceed V-02 alone, or C-20 and C-22 pass rates do not exceed V-01
alone, the mechanisms do not compound and the combination adds no benefit over either single-axis
variation.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable systematic scoring with independently auditable sub-step outputs,
each produced before the criterion row is sealed and each verifiable by section-heading scan
without reading prose content.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact type and its key fields.
2. What lifecycle phases does it have? Name them in order.
3. What would a completely non-functional output look like? Name the failure, not the absence
   of quality.

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+ if additional failure modes exist]
```

Minimum: 3 blocking, 2 degrading.

**PHASE 2 ENTRY GATE — DO NOT begin writing criteria until all three boxes are checked:**

- [ ] At least 3 blocking failure modes are present in Phase 1
- [ ] At least 2 degrading failure modes are present in Phase 1
- [ ] At least 3 distinct categories from the target skill's output contract are identifiable
      (list them: ___, ___, ___)

This gate is forward-blocking. Entering Phase 2 without satisfying it produces criteria detached
from the skill's actual failure surface. Stop here and complete Phase 1 if any box is unchecked.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

For each essential criterion, complete sub-steps 2a through 2d in order. Sub-step 2b does not
begin until 2a is written. The per-criterion gate (2d) is forward-blocking — it must clear before
the criterion row is recorded, not as a post-hoc repair step after the row is written.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition text.

**Sub-step 2b — Produce the INERTIA-RECORD block.**

Use the exact heading pattern shown. The heading text including brackets is required.

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from sub-step 2a]
Inertia test: Could "the output is clear and comprehensive" pass this condition? [YES / NO]
If YES — revised condition: [revision naming a count, field name, or enumeration from
  this skill's contract; re-run until NO]
Final condition: [the condition that produced NO]
Skill-specific element: [the count, field name, structural pattern, or enumeration
  from this skill's output contract that makes this condition non-generic]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block. Produce it now — immediately after
sub-step 2b, while this pass condition is in working memory. Do not produce all calibration
pairs after all pass conditions are finalized: each pair belongs to the criterion it was
derived from, at the moment of drafting.**

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [pass condition text applying to any artifact — belongs to the Status-Quo Rubric]
GROUNDED: [pass condition naming the skill-specific element from INERTIA-RECORD above;
  must reference the target skill by name or by a term from its output contract]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion in the table and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` block is present above with Final condition producing NO
- [ ] `### CALIBRATION-PAIR [C-NN]` block is present above, written before this gate check

This gate blocks forward progress. It is not a repair check: if either block is absent, the
criterion is not yet ready to record. Write the missing block and re-check before proceeding.

After both blocks are confirmed above, record the criterion:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion before moving to Phase 3.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Standard five-field table format. Named blocks not required.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Standard five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 5: SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**PHASE 6: QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

**PHASE 7: HEADING-SCAN AUDIT**

Scan the output for section headings matching the patterns below. This is a heading-pattern
scan — a heading is present or absent. Content is not evaluated here.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present and appears before ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present and appears before ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present; pass condition matches INERTIA-RECORD final condition
```

For any absent heading: write the missing block using the exact heading pattern shown, then
re-check. This audit is a structural verification, not a repair step — at this stage all blocks
should already be present (Phase 2's forward gates were designed to ensure this). A missing
heading after Phase 2 completion indicates a gate was bypassed.

---

## V-05 — Role Sequence × Output Format × Lifecycle Emphasis (V-03 × V-01 × V-02, Three-Axis Combination)

**axis:** role-sequence × output-format × lifecycle-emphasis
**hypothesis:** V-03 (role-sequence): Auditor reads all criteria before producing a single
consolidated audit table, enabling cross-criterion pattern analysis. V-01 (output-format): named
blocks with heading-scan verification make block omission detectable without content inspection.
V-02 (lifecycle-emphasis): forward-blocking per-criterion gates with explicit anti-deferral
prohibition. Together they target all four new criteria: C-19 (heading-scan blocks, from V-01),
C-20 (forward-blocking gates not retroactive repair, from V-02), C-21 (single consolidated audit
table, from V-03), C-22 (structural ordering + named anti-deferral, from V-02). The axis tension
from R3 roadmap applies: V-01's Phase 7 heading-scan and V-03's Auditor table both review
essential criteria. In this combination, V-01's heading-scan fires in Phase 7 (block-level
structural check); V-03's Auditor fires in the Auditor phase (reasoning-level specificity check).
They check different things and do not confound attribution. Failure condition: if C-21 pass rates
do not exceed V-01×V-02 alone, V-03's consolidated-table contribution adds no benefit; if C-19
pass rates do not exceed V-03 alone, V-01's heading-scan adds no benefit.

---

You are building a scoring rubric for a Signal skill. Three mechanisms enforce quality: named
section blocks that make structural omission detectable by heading scan; forward-blocking per-
criterion gates that prevent deferral; and an Auditor phase that reads all criteria as a set
before producing a single consolidated audit table. All three outputs appear in the final document.

**Why three mechanisms?**

Named blocks with heading-scan audit catch blocks that were skipped (C-19). Forward-blocking
gates prevent the skip from occurring in the first place by requiring blocks to appear before
the criterion row is written (C-20). Explicit anti-deferral language names the batch-deferral
pattern — producing all calibration pairs at the end of Phase 2 — that structural ordering alone
cannot prevent (C-22). The Auditor's consolidated table enables cross-criterion pattern analysis
that per-criterion auditing obscures (C-21).

---

### AUTHOR PHASE

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output non-functional?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] At least 3 blocking failure modes are listed in Author Phase 1
- [ ] At least 2 degrading failure modes are listed in Author Phase 1
- [ ] At least 3 distinct output-contract categories are identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3-5)**

For each essential criterion, produce the three named blocks in order, then record the criterion
row. The blocks must use the exact heading patterns shown — these patterns are what the Phase 7
heading-scan audit checks.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition: specific, observable, verifiable by two independent evaluators.

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [the count, field name, pattern, or enumeration from this
  skill's contract making this condition non-generic]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

Produce it now — immediately after sub-step 2b, while this pass condition is in working memory.
Do not produce all calibration pairs after all pass conditions are finalized: write each pair
at the moment the pass condition it calibrates is drafted.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [condition text applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD; references
  target skill by name or output-contract term]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion in the table and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` block is present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` block is present above, written before this gate check
      and before this criterion's table row

This is a forward-blocking gate, not a repair check. If either block is absent, write it before
proceeding. A criterion row without its preceding named blocks is incomplete.

After both blocks are confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format. Sub-step protocol
not required.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### END AUTHOR PHASE

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing any
audit output — the audit table requires cross-criterion visibility to detect systemic patterns.
Do not write audit rows one at a time as you process each criterion.

**Inertia test (apply to each essential pass condition from the Author phase):**
- YES: generic — write the revision in the Revised Condition column
- NO: skill-specific — name the discriminating element

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the count, field name, structural pattern, or enumeration from
  this skill's output contract. Required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column across all rows. Write one sentence noting whether
discriminating elements are varied across types (count, field name, structural pattern,
enumeration) or cluster in one type. If clustering is detected, note which essential criteria
cover under-represented types.

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to the final rubric section until:**

- [ ] Audit Table is complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element is filled for every NO-flagged row
- [ ] Cross-criterion pattern note is written

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where Revision
Required = YES. This is the canonical criteria table.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

| Band | Score | Interpretation |
|------|-------|----------------|
| Golden | all essential + >= 80 | Ship-ready rubric |
| Acceptable | all essential + 70-79 | Minor gaps, usable with reviewer awareness |
| Marginal | all essential + < 70 | Coverage or ordering gaps, iterate before use |
| Fail | any essential fails | Not a valid objective function regardless of total score |

**QUICK CHECKLIST**

One checkbox per criterion: `- [ ] C-NN: [one-line assertion]`

**PHASE 7: HEADING-SCAN AUDIT**

Scan the Author phase output for section headings matching the patterns below. Pattern match —
do not evaluate content.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present; pass condition matches INERTIA-RECORD final condition
```

A missing heading indicates a Phase 2 forward gate was bypassed. Write the missing block using
the exact heading pattern, then re-check. The Auditor phase cannot begin until all heading
patterns are present.

---

## Anchor Designation

**Anchor: V-03**

V-03 is designated the combination anchor for Round 4.

**Structural impact:** V-03's instruction to read all Author criteria before writing the audit
table — and to produce it as a single contiguous block with an explicit cross-criterion pattern
note — directly targets C-21. No other single-axis variation in this round isolates C-21. The
cross-criterion pattern note is the key mechanism: it forces the Auditor to synthesize across
rows rather than evaluate row by row, producing the pattern-level insight that C-21 requires.

**Isolation quality:** Only the Auditor's production protocol changes. The Author-phase structure
(failure modes, criteria format, five fields), the scoring formula, and the Phase 7 audit are
structurally identical to V-01 and V-02. The "read all before writing" and contiguous-block
instructions are the only variables. Co-variation observed in V-05 traces to this structure.

**Detectable failure condition:** A builder who processes Author criteria one at a time produces
an audit with the correct columns but written as distributed per-criterion sections, not a
contiguous table. The gap is visible: the Audit Table heading appears multiple times, or the
cross-criterion pattern note is absent. Both are structural signals detectable without reading
the audit content.

**Combination priority:** V-05 (all three axes) is the highest-priority combination. V-03's
consolidated audit table captures cross-criterion patterns (C-21); V-01's heading-scan makes
block omission visible (C-19); V-02's forward gates and anti-deferral prohibition prevent the
omissions V-01 catches (C-20, C-22). The combination tests whether all four new criteria require
all three mechanisms or whether a two-axis subset covers them.

---

## Combination Roadmap (for Round 5)

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-05 (this round) | all three | C-19, C-20, C-21, C-22 | 1 | Tested in R4; examine pass rate improvement |
| V-03 × V-02 | role-sequence × lifecycle-emphasis | C-20, C-21, C-22 | 2 | Tests whether forward-blocking gates + anti-deferral (V-02) and consolidated audit table (V-03) address orthogonal failure modes without named-block architecture overhead |
| V-03 × V-01 | role-sequence × output-format | C-19, C-21 | 3 | Tests whether heading-scan blocks and consolidated audit table compound: V-01's block audit (Phase 7) and V-03's Auditor table both review criteria — expected dominant variable is V-03 (reasoning depth) vs V-01 (structural presence). If C-21 does not improve over V-03 alone, V-01 confounds; scope heading-scan to Author phase only |

**R3 roadmap carryover:** The R3 roadmap nominated V-03×V-02 (role-sequence × output-format, C-15/C-17/C-18) and V-01×V-03×V-02 (all three, C-14–C-18) as Round 4 priorities. R4 fully executes the three-axis combination as V-05 (reframed around C-19–C-22). V-03×V-02 from the R3 roadmap corresponds to Round 5 Priority 2 (same axes, updated criteria targets).
