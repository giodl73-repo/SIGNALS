# quest-rubric Variate — Round 5 against rubric v5

**Date:** 2026-03-16
**Skill:** quest-rubric
**Rubric:** v5 (C-01 through C-18; essential C-01–C-05, recommended C-06–C-08, aspirational C-09–C-18)
**Round:** R5 — 3 single-axis + 2 combination

**Round 5 design note:** v5 adds C-17 and C-18 from Round 4 excellence signals E-1 and E-2:

- **C-17** (E-1): SCHEMA BLOCK is *positionally first* — the first section output, making the
  anchoring check structural rather than instructional. A rubric where SCHEMA BLOCK appears after
  failure modes or after criteria violates C-17 even if SCHEMA BLOCK content is correct.
- **C-18** (E-2): CONVERSION-MAP uses a *boolean classification mechanism* (one YES/NO test per
  prohibition) with a *completion gate* — the phase cannot close until every specificity prohibition
  found in the spec has a corresponding row. INERTIA-RECORD's per-criterion inertia test is not
  equivalent: it converts only the prohibitions relevant to the criterion being written, leaving
  prohibitions that no single criterion adopts unresolved.

The v5 rubric notes "V-04 predicted to pass C-17 and C-18 by combining SCHEMA BLOCK + CONVERSION-MAP."
R5 tests whether that prediction holds under the stricter v5 definitions. Three specific gaps:

1. **C-17 positional gap**: Prior prompts instruct the model to *include* a SCHEMA BLOCK; they do
   not structurally enforce it as the first output. The model may output preamble analysis before
   the SCHEMA BLOCK, satisfying C-16 (fields have a structural home) while failing C-17 (first).
2. **C-18 gate gap**: Prior prompts surface the CONVERSION-MAP pattern via INERTIA-RECORD but do not
   run a pre-criteria systematic scan. A spec with two specificity prohibitions may have one
   converted (the one the author happened to write a criterion for) and one ignored.
3. **C-15/C-18 integration gap**: The CONVERSION-MAP rows must feed INTO criteria — criteria that
   address specificity must reference the conversion, not re-derive it, to close the loop.

---

## Round 5 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | output-format | single-axis | Output template declares SCHEMA BLOCK as Section 1 — positional, structural, not instructional | C-17 |
| V-02 | lifecycle-emphasis | single-axis | CONVERSION-MAP as pre-criteria phase with boolean table and completion gate | C-15, C-18 |
| V-03 | role-sequence | single-axis | Spec Analyst role runs before Author — produces SCHEMA BLOCK and CONVERSION-MAP as handoff artifacts | C-15, C-17, C-18 |
| V-04 | output-format × lifecycle-emphasis | combination (V-01 × V-02) | Positional SCHEMA BLOCK + CONVERSION-MAP boolean gate | C-17, C-18 |
| V-05 | output-format × lifecycle-emphasis × role-sequence | combination (all three) | Section template + CONVERSION-MAP gate + Spec Analyst role | C-15, C-17, C-18 |

**Anchor designation (preliminary):** V-04. The two mechanisms operate at non-competing positions:
SCHEMA BLOCK fires before any analysis is written (output template position); CONVERSION-MAP fires
after spec reading but before failure modes (Author Phase 0). Neither can produce the other's
effect. Combined, they should satisfy C-17 and C-18 simultaneously. Either one alone may be
sufficient to cross Golden if only one of the two gaps is blocking (each aspirational criterion
contributes 1/10 × 10 = 1 composite point; cumulative aspirational gap determines the floor).

---

## V-01 — Output Format: SCHEMA BLOCK as Section 1

**axis:** output-format
**hypothesis:** C-17 requires the SCHEMA BLOCK to be positionally first. Instructional language
("begin with the SCHEMA BLOCK", "output the schema before any analysis") can be overridden by the
model's tendency to contextualize before committing to structure. V-01 changes the enforcement
mechanism from instructional to structural: the prompt declares a numbered section template, and
Section 1 is SCHEMA BLOCK. There is no Section 0 preamble — the model's first output token after
receiving the prompt is the Section 1 heading. Positional violation becomes detectable by section-
number scan without reading content: if Section 2 appears before Section 1 SCHEMA BLOCK is closed,
the template is structurally broken. Failure condition: if C-17 still fails, the model may declare
"Section 1 — SCHEMA BLOCK" as a heading but leave content deferred ("will be completed after spec
review"), satisfying the heading scan while violating the positional intent. Counter in V-02 or V-04:
require SCHEMA BLOCK content to be complete before advancing to Section 2 — no TBD, no forward
references.

---

You are building a scoring rubric for a Signal skill. Your output follows a fixed section template.
The first section is SCHEMA BLOCK. It appears before any analysis, before failure modes, before
criteria. There is no preamble.

**Output section template (follow this order exactly):**

```
Section 1 — SCHEMA BLOCK
Section 2 — Failure Modes
Section 3 — Essential Criteria
Section 4 — Recommended and Aspirational Criteria
Section 5 — Structural Verification
Section 6 — Audit Table
Section 7 — Final Rubric
Section 8 — Scoring Formula and Quick Checklist
```

Three mechanisms enforce quality within this template: named blocks in Section 3 (INERTIA-RECORD,
CALIBRATION-PAIR, CRITERION) that make structural omission detectable by heading scan; forward-
blocking per-criterion gates that prevent deferral; and a consolidated Audit Table in Section 6
that reads all criteria before producing any audit output.

**Why SCHEMA BLOCK first?**

The SCHEMA BLOCK declares the output contract before the rubric is written. It names the fields
every criterion row must have and the closed value sets for each field. Writing it first means the
Author cannot inadvertently introduce a field that has no declared structural home (C-16) or a
category value that is not in the closed enumeration (C-14).

---

### Section 1 — SCHEMA BLOCK

Output this section before reading the skill spec or writing anything else. Fill every field
completely. Do not use TBD, placeholders, or forward references.

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
scoring_formula: >
  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
golden_threshold: "all essential pass AND composite >= 80"
```

**Section 1 complete.** Advance to Section 2.

---

### Section 2 — Failure Modes

Read the skill spec. List failure modes:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT advance to Section 3 Entry Gate until minimum is met.**

---

### Section 3 — Essential Criteria (3-5)

**Section 3 Entry Gate — DO NOT write criteria until:**

- [ ] Failure modes minimum met (Section 2)
- [ ] At least 3 distinct category values from the SCHEMA BLOCK output_contract are identifiable
      in the skill spec (list them: ___, ___, ___)

For each essential criterion, produce the three named blocks in order. The blocks use exact heading
patterns — these patterns are what Section 5 heading-scan checks.

**Sub-step 3a — Draft pass condition.**

Write a pass condition that is specific, observable, and verifiable by two independent evaluators
who have not seen this prompt.

**Sub-step 3b — Produce the INERTIA-RECORD block.** Write immediately after 3a.

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 3a]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [the count, field name, structural pattern, or enumeration from this
  skill's output contract making this condition non-generic]
```

**Sub-step 3c — Produce the CALIBRATION-PAIR block.** Write immediately after 3b, while the pass
condition is in working memory. Do not produce all calibration pairs after all conditions are final.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [weakest passing condition that could apply to any skill's rubric — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD; references target
  skill by name or output-contract term]
```

**Sub-step 3d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` block is present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` block is present above, written before this gate check

This is a forward-blocking gate, not a repair check. If either block is absent, write it before
proceeding. A criterion row without its preceding named blocks is structurally incomplete.

After both blocks are confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 3a–3d for each essential criterion.

---

### Section 4 — Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Use the five-field table format. Sub-step
protocol is not required for these tiers.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

---

### Section 5 — Structural Verification

Scan Section 3 output for headings matching the patterns below. This is a heading-pattern scan
only — content is not evaluated here.

For each essential criterion C-NN produced in Section 3:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A missing heading indicates a Section 3 forward gate was bypassed. Write the missing block using
the exact heading pattern shown, then re-check.

**Section 6 cannot begin until every required heading pattern is confirmed present and correctly
ordered. Structural completeness is a prerequisite for reasoning analysis.**

---

### Section 6 — Audit Table

Read all `### CRITERION [C-NN]` blocks from Section 3. Read them all before writing any audit
output — the audit table requires cross-criterion visibility to detect systemic patterns.
Do not write audit rows one at a time as you process each criterion.

**Audit Table (write as a single contiguous block after reading all criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the count, field name, structural pattern, or enumeration from this
  skill's output contract. Required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column across all rows. Write one sentence noting whether
discriminating elements are varied across types (count, field name, structural pattern,
enumeration) or cluster in one type.

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**Section 7 Entry Gate — DO NOT proceed until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note is written

---

### Section 7 — Final Rubric

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. This is the canonical criteria table.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

---

### Section 8 — Scoring Formula and Quick Checklist

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

## V-02 — Lifecycle Emphasis: CONVERSION-MAP Pre-Criteria Gate

**axis:** lifecycle-emphasis
**hypothesis:** C-18 requires the CONVERSION-MAP to use boolean classification (one YES/NO test per
prohibition) with a completion gate. The prior mechanism — per-criterion INERTIA-RECORD — converts
prohibitions opportunistically: only the prohibitions that align with criteria the author chooses to
write get converted. A skill spec with two specificity prohibitions may produce one converted (the
author wrote a specificity criterion) and one ignored (the author wrote no criterion that surfaces
it). V-02 adds a CONVERSION-MAP phase between spec reading and failure mode listing: scan the full
spec for prohibitions, build a boolean table with one row per prohibition, require the completion
gate to clear before proceeding. The completion gate is binary: either all prohibitions have a row,
or an explicit empty declaration is written (zero prohibitions found). This eliminates the
opportunistic gap. Additionally, requiring that the INERTIA-RECORD block reference the CONVERSION-MAP
row (if applicable) enforces C-15/C-18 integration: converted prohibition tests feed into criteria
rather than living in a dead letter. Failure condition: if C-18 still fails, the CONVERSION-MAP is
built but criteria do not reference it — the conversion remains parallel to criteria rather than
feeding into them. Counter: add explicit cross-reference check to INERTIA-RECORD sub-step.

---

You are building a scoring rubric for a Signal skill. Four mechanisms enforce quality: a
CONVERSION-MAP phase that converts all specificity prohibitions to boolean tests before any criteria
are written; named section blocks (INERTIA-RECORD, CALIBRATION-PAIR, CRITERION) that make
structural omission detectable by heading scan; forward-blocking per-criterion gates that prevent
deferral; and an Auditor phase that reads all criteria as a set before producing a single
consolidated audit table.

**Why CONVERSION-MAP before failure modes?**

Specificity prohibitions define what the output must NOT be. They are constraints on pass
conditions, not on failure modes. Converting them to boolean tests before criteria drafting gives
the Author explicit reference material: when writing a pass condition for a specificity requirement,
reference the CONVERSION-MAP row rather than re-deriving the conversion from scratch. This prevents
each criterion from interpreting the same prohibition differently.

---

### CONVERSION-MAP PHASE

Read the skill spec. Identify all specificity prohibitions — language that says what the output
should NOT be or what it must be specifically:

- "not generic"
- "not boilerplate"
- "specific to input"
- "tailored to [X]"
- "not copy-paste from another rubric or skill"
- Any phrase of the form "output must not ___" or "must be specific to ___"

For each prohibition found, produce one row:

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question scoreable by inspection] | [observable pass state] | [observable fail state] |

If no prohibitions found:

```
CONVERSION-MAP: empty — no specificity prohibitions identified in skill spec.
```

**CONVERSION-MAP COMPLETION GATE — DO NOT advance to Failure Modes until:**

- [ ] Every specificity prohibition found has exactly one row in the table, OR the empty
      declaration is written
- [ ] Every PASS condition is scoreable by inspection without knowing the spec
- [ ] Every FAIL condition is the Boolean complement of PASS — not a new concept or partial negation
- [ ] No row is left blank or deferred

---

### AUTHOR PHASE 1 — Failure Modes

List failure modes:

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT advance to Author Phase 2 Entry Gate until minimum is met.**

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] CONVERSION-MAP Completion Gate cleared (above)
- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] At least 3 distinct output-contract categories identifiable (list: ___, ___, ___)

---

### AUTHOR PHASE 2 — Essential Criteria (3-5)

For each essential criterion, produce the three named blocks in order, then record the criterion row.

**Sub-step 2a — Draft pass condition.**

If this criterion addresses a specificity requirement, state which CONVERSION-MAP row applies:
"This criterion operationalizes CM-[N]: [prohibition]."

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 2a]
Conversion-Map reference: [CM-NN, if this is a specificity criterion; "N/A — not a specificity
  criterion" otherwise]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration from this
  skill's output contract]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block.** Immediately after 2b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [weakest condition applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check

After both confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion.

---

### AUTHOR PHASE 3 — Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (before Auditor Phase)

Scan Author phase output for heading patterns. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block, then re-check. Auditor Phase cannot begin until all confirmed.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks before writing any audit output. Do not write rows one
at a time.

**Audit Table (single contiguous block — write after reading all criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:** [one sentence on discriminating element variety]

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE — DO NOT proceed to Final Rubric until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written

### END AUDITOR PHASE

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

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

## V-03 — Role Sequence: Spec Analyst Before Author

**axis:** role-sequence
**hypothesis:** Both C-17 (SCHEMA BLOCK first) and C-18 (CONVERSION-MAP boolean gate) require the
model to produce structural pre-conditions before criteria are written. When a single Author role
handles both structural setup and criteria drafting, the structural steps are optional in practice:
the author can drift into criteria writing and treat SCHEMA BLOCK and CONVERSION-MAP as afterthoughts
or fill them in post-hoc. V-03 separates roles: the Spec Analyst runs first and is solely responsible
for producing the SCHEMA BLOCK and the CONVERSION-MAP. It has no criteria-writing responsibility.
The Author cannot begin until the Spec Analyst's output is complete. This makes positional enforcement
emerge from execution order rather than from instruction: the Spec Analyst outputs always precede
Author outputs because the Spec Analyst runs first. Failure condition: if C-17 and C-18 still fail,
the Spec Analyst produces the outputs but the Author re-derives them or ignores them — writing a
new SCHEMA BLOCK inline or addressing specificity via INERTIA-RECORD without referencing the
CONVERSION-MAP. Counter in V-05: require the Author Phase 2 Entry Gate to explicitly confirm the
Spec Analyst Completion Gate was cleared and to reference the SCHEMA BLOCK fields in the criteria
table header.

---

You are building a scoring rubric for a Signal skill. Two roles execute in sequence:

1. **Spec Analyst** — reads the skill spec; produces the SCHEMA BLOCK and CONVERSION-MAP; does
   not write criteria
2. **Author** — reads the Spec Analyst output; writes failure modes, criteria, and the final rubric;
   references SCHEMA BLOCK fields and CONVERSION-MAP rows

A third role, **Auditor**, reads all Author criteria as a set before producing the consolidated
audit table.

**Why Spec Analyst before Author?**

The SCHEMA BLOCK declares the output contract. The CONVERSION-MAP converts specificity prohibitions
to boolean tests. Both are structural inputs to criteria writing, not products of it. The Spec
Analyst runs first so these inputs are complete before the Author writes a single criterion. The
Author cannot produce a criterion that violates the output contract (wrong field, wrong category
value) or re-derives a prohibition conversion (different criterion, same prohibition, different
conversion) if those structures are fixed in advance.

---

## SPEC ANALYST PHASE

You are the Spec Analyst. Read the skill spec. Do not write criteria.

### Spec Analyst Output 1 — SCHEMA BLOCK

Identify the output contract of the target skill: what fields does every criteria row require?
What are the closed value sets for each categorical field?

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [field1, field2, ...]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
scoring_formula: >
  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
golden_threshold: "all essential pass AND composite >= 80"
```

Fill every field. Do not use TBD or placeholders.

### Spec Analyst Output 2 — CONVERSION-MAP

Scan the skill spec for specificity prohibitions ("not generic", "specific to input",
"tailored to X", "not boilerplate", etc.).

| Row | Prohibition (quoted) | Boolean test | PASS | FAIL |
|-----|---------------------|--------------|------|------|
| CM-01 | [quote] | [yes/no test] | [observable pass] | [observable fail] |

If no prohibitions found:

```
CONVERSION-MAP: empty — no specificity prohibitions in skill spec.
```

**SPEC ANALYST COMPLETION GATE — DO NOT hand off to Author until:**

- [ ] SCHEMA BLOCK complete with all fields filled (no TBD)
- [ ] CONVERSION-MAP has one row per prohibition found, OR empty declaration written
- [ ] Each PASS condition is scoreable by inspection
- [ ] Each FAIL condition is the Boolean complement of PASS

### END SPEC ANALYST PHASE

---

## AUTHOR PHASE

You are the Author. The Spec Analyst output is above. Do not re-derive the SCHEMA BLOCK or
CONVERSION-MAP. Reference them.

### Author Phase 1 — Failure Modes

Read the skill spec (not the Spec Analyst output — read the spec directly for failure analysis).

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] Spec Analyst Completion Gate is cleared (confirmed above)
- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] At least 3 distinct categories from the Spec Analyst SCHEMA BLOCK output_contract are
      identifiable in this skill (list: ___, ___, ___)

---

### Author Phase 2 — Essential Criteria (3-5)

For each essential criterion, produce the three named blocks in order, then record the criterion row.
The criteria table must use the fields declared in the Spec Analyst SCHEMA BLOCK.

**Sub-step 2a — Draft pass condition.**

If this criterion addresses a specificity requirement: state "This criterion operationalizes
CM-[N] from the Spec Analyst CONVERSION-MAP: [prohibition]."

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 2a]
Conversion-Map row: [CM-NN, if a specificity criterion; "not a specificity criterion" otherwise]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration from this
  skill's output contract]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block.** Immediately after 2b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [condition applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element; references target skill by name or
  output-contract term]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check

After both confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion.

---

### Author Phase 3 — Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (before Auditor Phase)

Scan Author phase output for heading patterns. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block, then re-check. Auditor Phase cannot begin until all confirmed.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing any
audit output. Do not write rows one at a time.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:** [one sentence on discriminating element variety]

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE — DO NOT proceed to Final Rubric until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written

### END AUDITOR PHASE

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Fields must match the Spec Analyst SCHEMA BLOCK
output_contract. Substitute Auditor-revised conditions where Revision Required = YES.

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
**hypothesis:** V-01 adds SCHEMA BLOCK as Section 1 of the output template, targeting C-17. V-02
adds CONVERSION-MAP as a pre-criteria lifecycle phase with boolean gate, targeting C-18. These
mechanisms operate at non-competing positions: the SCHEMA BLOCK fires before any analysis is written
(it is the first section of the output); the CONVERSION-MAP fires after spec reading but before
failure mode listing (it is the pre-Phase-1 step). Neither can produce the other's effect — the
SCHEMA BLOCK positional constraint cannot enforce that prohibitions are converted, and the
CONVERSION-MAP gate cannot enforce that the SCHEMA BLOCK appears first. Combined, V-04 should
satisfy both C-17 and C-18 simultaneously. Failure condition: if C-17 or C-18 fails despite
both mechanisms being present, either (a) the SCHEMA BLOCK is Section 1 but lacks complete
content (SCHEMA BLOCK present passes C-16 but incomplete content means C-17's structural
pre-condition intent is not met — update scoring definition), or (b) the CONVERSION-MAP table is
built but criteria do not reference it (C-15/C-18 integration gap). V-05 adds the Spec Analyst
role to enforce the integration gap.

---

You are building a scoring rubric for a Signal skill. Your output follows a fixed section template.
The CONVERSION-MAP phase runs before failure modes and before criteria, converting all specificity
prohibitions in the skill spec to boolean-testable pass conditions. Named blocks in the Essential
Criteria section (INERTIA-RECORD, CALIBRATION-PAIR, CRITERION) make structural omission detectable
by heading scan. An Auditor phase reads all criteria as a set before producing the consolidated
audit table.

**Output section template (follow this order exactly):**

```
Section 1 — SCHEMA BLOCK
Section 2 — CONVERSION-MAP
Section 3 — Failure Modes
Section 4 — Essential Criteria
Section 5 — Recommended and Aspirational Criteria
Section 6 — Structural Verification
Section 7 — Audit Table
Section 8 — Final Rubric
Section 9 — Scoring Formula and Quick Checklist
```

**Why SCHEMA BLOCK first, CONVERSION-MAP second?**

The SCHEMA BLOCK declares the output contract before any analysis. The CONVERSION-MAP converts
specificity prohibitions to boolean tests before any criteria are written. Both are structural
pre-conditions: the SCHEMA BLOCK prevents criteria from introducing undeclared fields; the
CONVERSION-MAP prevents criteria from interpreting prohibitions inconsistently.

---

### Section 1 — SCHEMA BLOCK

Output this section first, before reading the skill spec, before any analysis. Fill every field
completely. Do not use TBD, placeholders, or forward references.

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
scoring_formula: >
  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
golden_threshold: "all essential pass AND composite >= 80"
```

**Section 1 complete.** Advance to Section 2.

---

### Section 2 — CONVERSION-MAP

Read the skill spec. Identify all specificity prohibitions.

| Row | Prohibition (quoted from spec) | Boolean test | PASS: output ___ | FAIL: output ___ |
|-----|-------------------------------|--------------|------------------|------------------|
| CM-01 | [exact quote] | [yes/no question] | [observable pass] | [observable fail] |

If no prohibitions found:

```
CONVERSION-MAP: empty — no specificity prohibitions identified in skill spec.
```

**CONVERSION-MAP COMPLETION GATE — DO NOT advance to Section 3 until:**

- [ ] Every specificity prohibition found has exactly one row, OR empty declaration written
- [ ] Every PASS condition is scoreable by inspection
- [ ] Every FAIL condition is the Boolean complement of PASS
- [ ] No row is blank or deferred

---

### Section 3 — Failure Modes

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT advance to Section 4 Entry Gate until minimum is met.**

---

### Section 4 — Essential Criteria (3-5)

**Section 4 Entry Gate — DO NOT write criteria until:**

- [ ] CONVERSION-MAP Completion Gate cleared (Section 2)
- [ ] Failure modes minimum met (Section 3)
- [ ] At least 3 distinct category values from the SCHEMA BLOCK output_contract are identifiable
      in this skill (list: ___, ___, ___)

For each essential criterion, produce the three named blocks in order, then record the criterion row.

**Sub-step 4a — Draft pass condition.**

If addressing a specificity requirement: "This criterion operationalizes CM-[N]: [prohibition]."

**Sub-step 4b — Produce the INERTIA-RECORD block.** Write immediately after 4a.

```
### INERTIA-RECORD [C-NN]
Draft condition: [from 4a]
Conversion-Map reference: [CM-NN if specificity criterion; "N/A" otherwise]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration]
```

**Sub-step 4c — Produce the CALIBRATION-PAIR block.** Immediately after 4b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [weakest condition applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD]
```

**Sub-step 4d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check

After both confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 4a–4d for each essential criterion.

---

### Section 5 — Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

---

### Section 6 — Structural Verification

Scan Section 4 output for heading patterns. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block, then re-check. Section 7 cannot begin until all confirmed.

---

### Section 7 — Audit Table

Read all `### CRITERION [C-NN]` blocks before writing. Do not write rows one at a time.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:** [one sentence on discriminating element variety]

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**Section 8 Entry Gate — DO NOT proceed until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written

---

### Section 8 — Final Rubric

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

---

### Section 9 — Scoring Formula and Quick Checklist

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

## V-05 — Output Format × Lifecycle Emphasis × Role Sequence (All Three, Combination)

**axis:** output-format × lifecycle-emphasis × role-sequence
**hypothesis:** V-04 (V-01 × V-02) should satisfy C-17 and C-18 through structural template
enforcement and CONVERSION-MAP gate. V-05 extends V-04 by adding V-03's Spec Analyst role. The
key gap V-04 may leave open is C-15/C-18 integration: the CONVERSION-MAP exists and the criteria
exist, but the criteria may not reference the CONVERSION-MAP (specificity criteria re-derive their
pass conditions independently). The Spec Analyst role addresses this by producing SCHEMA BLOCK and
CONVERSION-MAP as explicit handoff artifacts that the Author is instructed to reference, not
duplicate. Additionally, the Spec Analyst's SCHEMA BLOCK is the FIRST thing in the document (the
Spec Analyst runs before everything, so Spec Analyst Output 1 appears before the CONVERSION-MAP,
failure modes, and criteria), reinforcing C-17 through role-ordering rather than section templates.
Three mechanisms, three non-competing lifecycle positions: Spec Analyst (pre-Author), Section 1
template position (first output token), CONVERSION-MAP gate (post-spec-read, pre-failure-modes).
Failure condition: if V-04 already reaches Golden and V-05 does not improve C-15 integration, the
criteria-CONVERSION-MAP gap either doesn't exist (authors naturally reference it) or exists but
contributes no additional criteria (C-15 is already passing). Either outcome closes the investigation.

---

You are building a scoring rubric for a Signal skill. Three roles execute in sequence:

1. **Spec Analyst** — reads the skill spec; produces the SCHEMA BLOCK and CONVERSION-MAP;
   does not write criteria
2. **Author** — reads Spec Analyst output; writes failure modes and criteria; references SCHEMA
   BLOCK fields and CONVERSION-MAP rows; does not re-derive them
3. **Auditor** — reads all Author criteria as a set; produces consolidated audit table

Your output follows a fixed role-execution template. The Spec Analyst outputs appear first —
before failure modes, before criteria, before any analysis.

**Output template (follow this order exactly):**

```
--- SPEC ANALYST ---
SA-1: SCHEMA BLOCK
SA-2: CONVERSION-MAP
--- END SPEC ANALYST ---

--- AUTHOR ---
A-1: Failure Modes
A-2: Essential Criteria
A-3: Recommended and Aspirational Criteria
--- END AUTHOR ---

--- STRUCTURAL VERIFICATION ---

--- AUDITOR ---
AU-1: Audit Table
AU-2: Cross-Criterion Pattern Note
AU-3: Auditor Calibration Pair
--- END AUDITOR ---

FINAL RUBRIC
SCORING FORMULA AND QUICK CHECKLIST
```

---

### --- SPEC ANALYST ---

You are the Spec Analyst. Your sole output is SA-1 (SCHEMA BLOCK) and SA-2 (CONVERSION-MAP).
Do not write failure modes. Do not write criteria.

#### SA-1: SCHEMA BLOCK

Read the target skill name and output contract from the skill spec. Fill completely.

```yaml
skill: [target skill name]
version: 1
date: [today's date]
output_contract:
  criteria_fields: [id, criterion, category, weight, pass_condition]
  category_values: [correctness, depth, format, coverage, behavior]
  weight_values: [essential, recommended, aspirational]
scoring_formula: >
  composite = (essential_pass / N_essential * 60)
            + (recommended_pass / N_recommended * 30)
            + (aspirational_pass / N_aspirational * 10)
golden_threshold: "all essential pass AND composite >= 80"
```

#### SA-2: CONVERSION-MAP

Scan the skill spec for specificity prohibitions.

| Row | Prohibition (quoted) | Boolean test | PASS | FAIL |
|-----|---------------------|--------------|------|------|
| CM-01 | [quote] | [yes/no test] | [observable pass] | [Boolean complement of PASS] |

If no prohibitions: `CONVERSION-MAP: empty — no specificity prohibitions in skill spec.`

**SPEC ANALYST COMPLETION GATE — DO NOT hand off to Author until:**

- [ ] SA-1 complete with all fields filled (no TBD)
- [ ] SA-2 has one row per prohibition, OR empty declaration written
- [ ] Each PASS scoreable by inspection; each FAIL is Boolean complement of PASS

### --- END SPEC ANALYST ---

---

### --- AUTHOR ---

You are the Author. The Spec Analyst outputs (SA-1 and SA-2) are above. Do not re-derive them.
Reference them explicitly when writing criteria.

#### A-1: Failure Modes

Read the skill spec directly for failure analysis.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**AUTHOR ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] Spec Analyst Completion Gate cleared (confirmed above)
- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] At least 3 distinct category_values from SA-1 output_contract are identifiable
      in this skill (list: ___, ___, ___)

---

#### A-2: Essential Criteria (3-5)

For each essential criterion, produce the three named blocks in order, then record the criterion row.
Category and field values must be drawn from SA-1 output_contract closed lists.

**Sub-step A2a — Draft pass condition.**

If this criterion addresses a specificity requirement: "This criterion operationalizes SA-2
CM-[N]: [prohibition]." Do not re-derive — cite the row.

**Sub-step A2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [from A2a]
SA-2 reference: [CM-NN if specificity criterion; "not a specificity criterion" otherwise]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, structural pattern, or enumeration from SA-1
  output_contract]
```

**Sub-step A2c — Produce the CALIBRATION-PAIR block.** Immediately after A2b.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [weakest condition applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD; references
  target skill by name or SA-1 output-contract term]
```

**Sub-step A2d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check

After both confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[label]** — [text] | [category from SA-1] | essential | [final condition] |
```

Repeat A2a–A2d for each essential criterion.

---

#### A-3: Recommended and Aspirational Criteria

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format. Category values
must be drawn from SA-1 output_contract.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### --- END AUTHOR ---

---

### --- STRUCTURAL VERIFICATION ---

Scan Author A-2 output for heading patterns. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block, then re-check. Auditor cannot begin until all confirmed.

### --- END STRUCTURAL VERIFICATION ---

---

### --- AUDITOR ---

You are the Auditor. Read all `### CRITERION [C-NN]` blocks from Author A-2 before writing any
audit output. Do not write rows one at a time.

#### AU-1: Audit Table (single contiguous block)

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

#### AU-2: Cross-Criterion Pattern Note

Scan the Discriminating Element column across all rows. Write one sentence: are discriminating
elements varied across types (count, field name, structural pattern, enumeration) or clustered?

#### AU-3: Auditor Calibration Pair — most critical essential criterion

```
GENERIC: [weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE — DO NOT proceed to Final Rubric until:**

- [ ] AU-1 complete with all essential criteria as rows
- [ ] Every essential criterion: Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] AU-2 written

### --- END AUDITOR ---

---

**FINAL RUBRIC — APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Category and field values drawn from SA-1 output_contract.
Substitute Auditor-revised conditions where Revision Required = YES.

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

## Anchor Designation

**Anchor: V-04**

V-04 is designated the combination anchor for Round 5.

**Structural impact:** V-04 targets C-17 and C-18 simultaneously — the two new aspirational
criteria in v5. The mechanisms are non-competing:

- SCHEMA BLOCK Section 1 (V-01): fires before any output is written; enforced by section template
  position; detectable by section-number scan
- CONVERSION-MAP gate (V-02): fires after spec reading, before failure modes; enforced by completion
  gate checklist; detectable by phase-order scan

Neither mechanism can produce the other's effect. The SCHEMA BLOCK positional constraint says nothing
about whether prohibitions are converted. The CONVERSION-MAP gate says nothing about where the SCHEMA
BLOCK appears.

**Isolation quality:** V-01 and V-02 isolate C-17 and C-18 respectively. If V-04 passes both while
V-01 only passes C-17 and V-02 only passes C-18, the combination is confirmed additive with no
interaction effect. If V-04 fails one that its single-axis variation passed:

- C-17 fails in V-04 but passes in V-01: the CONVERSION-MAP phase (Section 2) between SCHEMA BLOCK
  and Failure Modes may be lengthening the output in a way that makes the model treat Section 1 as
  a preamble rather than a contract. Fix: add explicit Section 1 completion marker before Section 2.
- C-18 fails in V-04 but passes in V-02: the section template may suppress the CONVERSION-MAP gate
  (model treats Section 2 as a table to fill in rather than a blocking gate). Fix: reinforce the
  completion gate in Section 2 with explicit blocking language.

**Detectable interaction with V-05:**

If V-04 reaches Golden and V-05 does not improve the score, the Spec Analyst role adds no benefit
beyond the section template + CONVERSION-MAP gate — the integration gap (C-15) is either already
closed by V-02's CONVERSION-MAP reference mechanism or does not exist. If V-05 improves over V-04
on C-15, the integration gap is real and the Spec Analyst handoff pattern is the correct fix.

---

## Combination Roadmap (for Round 6)

**R5 outcome scenarios:**

| Scenario | Expected Outcome | Round 6 Action |
|----------|-----------------|----------------|
| V-04 reaches Golden | C-17 and C-18 both fixed | Run V-05 to test C-15 integration gain; V-04 becomes new base |
| V-01 passes C-17, V-02 fails C-18 | Section template enforces position but CONVERSION-MAP gate is insufficient | Investigate: is the gate checklist present but bypassed? Tighten: add an explicit "CONVERSION-MAP CLOSED" declaration that the author must write before proceeding |
| V-02 passes C-18, V-01 fails C-17 | CONVERSION-MAP gate works but SCHEMA BLOCK drifts from Section 1 position | Investigate: does the model output an opening preamble before Section 1? Fix: add "Output Section 1 as your first token" language or change heading to a numbered marker |
| Both V-01 and V-02 fail C-17/C-18 | Mechanisms insufficient alone | Investigate whether the mechanisms are present but the scoring definitions of C-17/C-18 are tighter than what the prompts enforce — may require rubric definition clarification |
| V-03 passes C-15 where V-02 does not | Spec Analyst role closes integration gap | The handoff artifact pattern (Spec Analyst produces CONVERSION-MAP, Author cites CM-NN) is the correct mechanism for C-15; absorb as E-1 for Round 6 rubric update |
| V-05 adds no improvement over V-04 | Role separation is redundant given section template | Retire the Spec Analyst role as a standalone mechanism; consider it only in combination with other axes that benefit from explicit role-scope constraints |

**Combination priority for Round 6:**

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-04 × phrasing-register | output-format × lifecycle-emphasis × formal-imperative | C-17, C-18 | 1 | If V-02's CONVERSION-MAP gate fails due to advisory language ("should build the map"), imperative register ("CONVERSION-MAP is required; the phase CANNOT close until...") may improve compliance |
| V-04 × inertia-framing | output-format × lifecycle-emphasis × named-competitor | C-07, C-17, C-18 | 2 | Making the Status-Quo Rubric a named entity in the prompt framing (not just an implicit foil in CALIBRATION-PAIR) tests whether explicit competitor naming improves specificity criteria and SCHEMA BLOCK completeness |
| V-03 (role-sequence) solo re-run | role-sequence | C-15, C-17, C-18 | 3 | Only if V-03's single-axis run produces a substantially different C-17/C-18 score than V-01 and V-02, suggesting role separation has orthogonal benefits beyond the section template |
