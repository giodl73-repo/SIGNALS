# quest-rubric Variate — Round 3 against rubric v3

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v3 (C-01 through C-18; essential C-01–C-05)
**Round:** R3 — 3 single-axis passes + 2 combination passes

**Round 3 design note:** Round 2 (against rubric v2) produced five excellence signals absorbed into
v3 as aspirational criteria: C-14 (calibration pair lifecycle position, from V-03), C-15 (sub-step
output sequencing makes omission detectable, from V-03), C-16 (multi-level gate architecture,
from V-03), C-17 (audit role separation, from V-05), C-18 (audit trail captures reasoning, from
V-05). The R2 anchor is V-03 (lifecycle-emphasis with per-criterion sub-steps). Round 3 probes
whether skill body variations can reliably produce rubrics reaching C-14 through C-18. Three
single-axis variations isolate one mechanism each; two combinations test whether mechanism pairs
cover criteria that resist single-axis treatment.

---

## Round 3 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | lifecycle-emphasis | single-axis | Phase gate at Phase 2 entry; per-criterion gate sequences pair-writing before sealing, not after | C-14, C-16 |
| V-02 | output-format | single-axis | Named artifact blocks (`INERTIA-RECORD`, `CALIBRATION-PAIR`) required before the criterion table row | C-15 |
| V-03 | role-sequence | single-axis | Author drafts; separate Auditor produces audit table with Discriminating Element column | C-17, C-18 |
| V-04 | lifecycle-emphasis × output-format | combination (V-01 × V-02) | Temporal gates + named artifact blocks — gates reference the named blocks | C-14, C-15, C-16 |
| V-05 | role-sequence × lifecycle-emphasis | combination (V-03 × V-01, R2-V-03 anchor) | Author sub-steps enforce temporal ordering; Auditor produces discriminating-element table | C-14, C-16, C-17, C-18 |

**Anchor designation (C-14 of the quest-variate rubric):** V-03. See anchor section at end.

---

## V-01 — Lifecycle Emphasis: Two-Level Gate Architecture + Temporal Pair Ordering

**axis:** lifecycle-emphasis
**hypothesis:** Adding a phase gate at Phase 2 entry — blocking criterion-writing until a
sufficient failure-mode foundation is in place — combined with a per-criterion gate that enforces
the sequence (draft pass condition → write calibration pair → seal criterion) addresses C-14 and
C-16 simultaneously. C-14 fails most often not because builders forget the calibration pair but
because they defer it: they write all pass conditions first, seal the table, then go back to fill
in pairs from memory. The per-criterion gate makes deferral a visible protocol violation rather
than a quiet quality option, because the gate language explicitly requires the pair to "appear
above this line" before the criterion is recorded. C-16 fails because R2 V-03 had per-criterion
gates but no phase-level gate — a builder who starts Phase 2 with only one blocking failure mode
produces criteria that miss the skill's actual failure surface. The phase gate closes that gap.
Failure condition: if C-14 pass rates do not improve relative to R2 V-03 (which had per-criterion
sub-steps but no temporal-ordering gate language for the pair), the "appear above this line"
enforcement adds no compliance benefit over V-03's sub-step sequencing, and the additional gate
text costs prompt length without behavioral gain.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable two independent evaluators to reach the same pass/fail verdict for
any skill output, without discussion.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact type and its key fields.
2. What lifecycle phases does it have? Name them in order.
3. What would a completely non-functional output look like? Name the failure, not the absence
   of quality.

**PHASE 1: FAILURE MODES**

List failure modes. Each is a specific, detectable way the output can fail to function as intended.
Assign severity.

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
[F-06+: additional if present]
```

Minimum: 3 blocking, 2 degrading.

**PHASE 2 ENTRY GATE — DO NOT begin writing criteria until all three boxes are checked:**

- [ ] At least 3 blocking failure modes are present in Phase 1
- [ ] At least 2 degrading failure modes are present in Phase 1
- [ ] At least 3 distinct categories from the target skill's output contract are identifiable
      (list them: ___, ___, ___)

Advancing past this gate without satisfying all three conditions produces criteria detached from
the skill's actual failure surface. Stop here and complete Phase 1 if any box is unchecked.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

For each essential criterion, complete sub-steps 2a through 2d in order. Sub-step 2b does not
begin until 2a is written. Sub-step 2c does not begin until 2b produces a PASS result. The
criterion is not recorded in the summary table until sub-step 2d clears.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition text: a specific, observable outcome. State what an evaluator would look
for and what constitutes a pass.

**Sub-step 2b — Apply the inertia test.**

Ask: Could a rubric containing only "the output is clear and comprehensive" pass this condition?

- If YES: the condition is generic. Revise to name a count, field name, structural element, or
  enumeration from this skill's output contract. Re-run the test until the answer is NO.
- If NO: the condition is skill-specific. Record result.

Record inline:
`Inertia test: PASS [NO — condition requires {skill-specific element from this skill's contract}]`

**Sub-step 2c — Write the calibration pair. Write it now, while the pass condition is in
working memory. Do not defer to after the table is complete.**

```
GENERIC: [pass condition text that applies to any artifact — what belongs to the Status-Quo Rubric]
GROUNDED: [pass condition text naming the skill-specific element identified in sub-step 2b]
```

Both entries must reference the target skill by name or by a term from its output contract.

**Sub-step 2d — Per-criterion gate.**

**DO NOT record this criterion in the table until:**

- [ ] Sub-step 2b result is PASS [NO] — inertia test survived (original or revised condition)
- [ ] Sub-step 2c calibration pair appears in the output **above this line**, not below, not
      deferred to a later section

After all four sub-steps clear for this criterion, record it:

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

Repeat sub-steps 2a–2d for each essential criterion before moving to Phase 3.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Five-field table format. Inertia test applies but calibration
pair and inline documentation are not required.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Five-field table format.

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

## V-02 — Output Format: Independent Named Artifact Blocks

**axis:** output-format
**hypothesis:** Requiring each mandatory sub-step output to appear as a named, labeled section
block before the criterion table row — rather than embedded in a table cell or omitted silently —
addresses C-15 by making omission detectable as a structural gap rather than a quality shortfall.
When a builder skips the inertia test or calibration pair, the output will be missing a named
section (`INERTIA-RECORD [C-NN]` or `CALIBRATION-PAIR [C-NN]`). A reviewer scanning the output
sees the gap without reading table cells; the criterion row appears but its required precursor
blocks are absent. This converts a content-quality failure into a format-level failure: checkable
by block-counting, not by evaluating prose quality. Failure condition: if C-15 pass rates do not
improve relative to R2 V-03 (which required sub-step outputs but embedded them inline rather than
as named blocks), the named-block format adds no detectability benefit, and the structural overhead
is not justified.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable systematic scoring with independently auditable sub-step outputs.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output completely non-functional?

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**DO NOT proceed to Phase 2 until at least 3 blocking failure modes are present.**

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

For each essential criterion, produce three named output blocks in the sequence shown below, then
record the criterion in the summary table. The blocks must appear **before** the table row —
not embedded in a table cell, not deferred to the end of Phase 2.

**Required block sequence per criterion:**

```
### INERTIA-RECORD [C-NN]
Draft condition: [the pass condition as first written]
Inertia test question: Could a rubric containing only "the output is clear and
  comprehensive" pass this condition?
Result: [YES or NO]
If YES — revised condition: [revision naming a count, field, or enumeration from
  this skill's contract]
Final condition: [the condition that produced NO]
Skill-specific element: [the count, field name, structural pattern, or enumeration
  that ties this condition to the target skill's output contract — not a shared
  structural minimum]
```

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [pass condition text that applies to any artifact — belongs to the
  Status-Quo Rubric, not skill-specific]
GROUNDED: [pass condition text naming the skill-specific element from
  INERTIA-RECORD above — references the target skill by name or by a term
  from its output contract]
```

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

A reviewer scanning the output will find three named blocks per essential criterion before any
table row. A missing `### INERTIA-RECORD [C-NN]` or `### CALIBRATION-PAIR [C-NN]` block is a
structural gap detectable by inspection — the criterion was recorded without its required checks.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Standard five-field table format (named blocks not required).

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Standard five-field table format.

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

**PHASE 7: COMPLETENESS AUDIT**

Scan the output above. For each essential criterion C-NN, confirm:

- [ ] `### INERTIA-RECORD [C-NN]` block is present and appears before `### CRITERION [C-NN]`
- [ ] `### CALIBRATION-PAIR [C-NN]` block is present and appears before `### CRITERION [C-NN]`
- [ ] `### CRITERION [C-NN]` pass condition matches the final condition from its INERTIA-RECORD

If any block is absent: write the missing block now. A criterion with a missing block is not
complete regardless of its table row content.

---

## V-03 — Role Sequence: Author/Auditor Separation with Discriminating-Element Column

**axis:** role-sequence
**hypothesis:** Separating criterion-authoring (coverage concern: do criteria address the right
failure modes?) from criterion-auditing (specificity concern: are pass conditions discriminating?)
into distinct sequential roles addresses C-17 and C-18 simultaneously. C-17 fails when both
concerns are handled in one step — the author cannot simultaneously achieve coverage and evaluate
specificity without one degrading the other. The Author role removes the specificity burden from
drafting, allowing full attention to failure-mode coverage. C-18 fails when an audit produces only
pass/fail verdicts, leaving future maintainers unable to determine what made a condition survive.
The Auditor role's Discriminating Element column closes this gap: it requires the Auditor to name
the specific skill-contract element that makes each surviving condition non-generic. A rubric
maintainer reading the audit table can identify what to preserve when the pass condition is
rewritten, without re-running the full evaluation. Failure condition: if C-17 and C-18 pass rates
do not both improve relative to R2 V-05 (role-sequence with no structured audit table), the
Discriminating Element column adds no reasoning-capture benefit over a simple Challenger review,
and the column overhead is not justified.

---

You are building a scoring rubric for a Signal skill. Two phases operate in sequence: an Author
phase produces all criteria; an Auditor phase produces a structured audit of the Author's pass
conditions. Both outputs must appear in the final rubric document.

**Why two phases?**

Writing criteria for coverage (does each criterion address a real failure mode?) and auditing
criteria for specificity (is each pass condition discriminating for this skill only?) are competing
cognitive demands. When handled in a single step, neither receives full attention. The Author
focuses on coverage; the Auditor focuses on specificity. Both phases produce independently
readable artifacts.

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

Write all criteria. Each criterion targets a distinct failure mode from Author Phase 1. Focus on
coverage: ensure the essential criteria collectively surface all blocking failure modes. Do not
self-review pass conditions for skill-specificity — the Auditor handles that.

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

Read all Author-phase essential pass conditions. For each, apply the inertia test and record
findings in the Audit Table below.

**Inertia test:** Could a rubric containing only "the output is clear and comprehensive" pass
this condition?
- YES: condition is generic — it belongs to the Status-Quo Rubric, not this skill's rubric.
  Identify the revision that would make it skill-specific.
- NO: condition is skill-specific. Name the element that makes it discriminating.

**Audit Table:**

| Criterion ID | Pass Condition (quoted from Author phase) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------------------------|--------------|----------------------|-------------------|-------------------|

**Column definitions:**
- *Inertia Test*: YES (generic) or NO (skill-specific)
- *Discriminating Element*: the count, field name, structural pattern, or enumeration from the
  target skill's output contract that makes the condition non-generic. Required for every NO
  result. If Inertia Test is YES, leave blank and fill Revised Condition instead.
- *Revision Required?*: YES or NO
- *Revised Condition*: the rewritten pass condition for any YES-flagged row, naming the
  specific element added

**Auditor Calibration Pair** — for the essential criterion with the highest-stakes failure mode:

```
GENERIC: [weakest surviving form of the condition — what belongs to the Status-Quo Rubric]
GROUNDED: [the Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to the scoring section until every essential criterion in the
Audit Table shows Inertia Test = NO (original or Auditor-revised).**

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with Auditor-revised pass conditions substituted where
the Audit Table shows Revision Required = YES. This is the canonical criteria table.

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

## V-04 — Lifecycle Emphasis × Output Format (V-01 × V-02, Combination)

**axis:** lifecycle-emphasis × output-format
**hypothesis:** V-01's two-level gate structure tells the builder *when* to produce the
calibration pair (before sealing, not after). V-02's named artifact blocks make violations
*visible* (a missing block is a structural gap, not a quality drop). They address different
failure modes of the same behavior: V-01 prevents retrospective pair-writing; V-02 makes
retrospective pair-writing detectable after the fact. Combining them closes both gaps: a builder
who ignores the V-01 gate is caught by the V-02 block audit; a builder who produces blocks but
out of order is caught by the V-01 gate language requiring blocks to appear "above this line."
Together they enforce C-14 (temporal ordering), C-15 (detectable omission), and C-16 (two-level
gates). Failure condition: if C-14, C-15, and C-16 pass rates for this combination do not all
exceed the pass rates of V-01 and V-02 individually — specifically, if C-15 does not improve
over V-01 alone or C-14 does not improve over V-02 alone — then the mechanisms do not compound
and the combination adds no benefit over the single-axis variations run in sequence.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for
quest-golden: it must enable systematic scoring with independently auditable sub-step outputs,
each produced at the moment its pass condition is drafted.

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output completely non-functional?

**PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

Minimum: 3 blocking, 2 degrading.

**PHASE 2 ENTRY GATE — DO NOT begin writing criteria until all three boxes are checked:**

- [ ] At least 3 blocking failure modes are present in Phase 1
- [ ] At least 2 degrading failure modes are present in Phase 1
- [ ] At least 3 distinct categories identifiable from the target skill's output contract:
      ___, ___, ___

This is the phase gate. Advancing past it without satisfying all three conditions produces
criteria that miss the skill's actual failure surface.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

For each essential criterion, produce named output blocks in the order shown, then record the
criterion in the summary table. Blocks must appear before the table row. The per-criterion gate
(sub-step 2d) checks both the gate condition AND the block ordering.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition text.

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from sub-step 2a]
Inertia test: Could "the output is clear and comprehensive" pass this condition? [YES/NO]
If YES — revised condition: [revision naming a count, field, or enumeration from this
  skill's contract]
Final condition: [condition that produced NO]
Skill-specific element: [the count, field, structural pattern, or enumeration from
  this skill's output contract]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block. Produce it now, before recording the
criterion in the table.**

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [pass condition text that applies to any artifact — Status-Quo Rubric form]
GROUNDED: [pass condition text naming the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion gate.**

**DO NOT record this criterion in the table until:**

- [ ] `### INERTIA-RECORD [C-NN]` block is present above this line with Inertia test = NO
      (original or revised)
- [ ] `### CALIBRATION-PAIR [C-NN]` block is present above this line with both GENERIC
      and GROUNDED entries completed

After both blocks are present above, record the criterion:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Write 2-3 recommended criteria. Standard five-field table format. Named blocks not required.

**PHASE 4: ASPIRATIONAL CRITERIA (1-2)**

Write 1-2 aspirational criteria. Standard five-field table format.

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

**PHASE 7: BLOCK COMPLETENESS AUDIT**

Scan the output. For each essential criterion C-NN, confirm:

- [ ] `### INERTIA-RECORD [C-NN]` is present and precedes `### CRITERION [C-NN]`
- [ ] `### CALIBRATION-PAIR [C-NN]` is present and precedes `### CRITERION [C-NN]`
- [ ] Pass condition in `### CRITERION [C-NN]` matches the final condition in `### INERTIA-RECORD [C-NN]`

If any block is absent: write the missing block now.

---

## V-05 — Role Sequence × Lifecycle Emphasis (V-03 × V-01, R2-V-03 Anchor Combination)

**axis:** role-sequence × lifecycle-emphasis
**hypothesis:** V-01 (lifecycle-emphasis) enforces temporal pair-writing and two-level gates
inside the Author's drafting phase. V-03 (role-sequence) separates authoring from auditing and
requires the Auditor to capture discriminating elements in a structured table. Combined, they test
whether structural gating (which prevents retrospective pair-writing by the Author, addressing
C-14) and social auditing (which captures reasoning for future maintainers, addressing C-18)
address different failure surfaces or the same one. If complementary — Author gates prevent
shallow drafting, Auditor table captures the reasoning trail that gates cannot produce — the
combination addresses C-14, C-16, C-17, and C-18 simultaneously. Failure condition: if C-14 pass
rates for this combination do not exceed V-03 alone (which lacks Author-phase temporal gates), or
if C-18 pass rates do not exceed V-01 alone (which lacks an Auditor with a discriminating-element
column), then the two mechanisms do not compound and the combination adds no benefit over either
single-axis variation used alone. The single-axis comparison denominators are V-01 for C-14 and
C-16, and V-03 for C-17 and C-18.

---

You are building a scoring rubric for a Signal skill. Two phases operate in sequence: an Author
phase that drafts all criteria with structural enforcement of temporal sub-step ordering; an
Auditor phase that produces a structured audit table with discriminating-element reasoning. Both
outputs must appear in the final rubric document and are independently readable.

**Why two phases with sub-step enforcement?**

The Author phase enforces that calibration pairs are produced at drafting time — before criteria
are sealed — so pairs are derived alongside pass conditions, not rationalized afterward. The Auditor
phase captures why each condition survived the inertia test, so future maintainers can revise pass
conditions without re-running the full evaluation.

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

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3-5)**

For each essential criterion, complete sub-steps 2a through 2d in order.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition: a specific, observable outcome that two independent evaluators can
verify without discussion.

**Sub-step 2b — Apply the inertia test.**

Ask: Could a rubric containing only "the output is clear and comprehensive" pass this condition?

- If YES: generic — revise to name a count, field, structural element, or enumeration from this
  skill's output contract. Re-run until NO.
- If NO: skill-specific — proceed.

Record inline: `Inertia test: PASS [NO — condition requires {skill-specific element}]`

**Sub-step 2c — Write the calibration pair. Write it now, while this pass condition is in
working memory. Do not defer to after the Author phase is complete.**

```
GENERIC: [pass condition text belonging to the Status-Quo Rubric — applies to any artifact]
GROUNDED: [pass condition naming the skill-specific element from sub-step 2b]
```

**Sub-step 2d — Per-criterion gate.**

**DO NOT record this criterion in the Author table until:**

- [ ] Sub-step 2b is PASS [NO]
- [ ] Sub-step 2c calibration pair appears in the Author output above this criterion's table row

After clearing, record:

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

Repeat sub-steps 2a–2d for each essential criterion.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format. Sub-step protocol
not required.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### END AUTHOR PHASE

---

### AUDITOR PHASE

Read all Author-phase essential pass conditions (from the Author Phase 2 table). For each, apply
the inertia test and record findings in the Audit Table.

**Inertia test:** Could a rubric containing only "the output is clear and comprehensive" pass this
condition?
- YES: generic — write the revision in the Revised Condition column
- NO: skill-specific — identify and name the discriminating element

**Audit Table:**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the specific count, field name, structural pattern, or enumeration
  from the target skill's output contract that makes this condition non-generic. Required for
  every NO result. Leave blank for YES-flagged rows.
- *Revised Condition*: required for every YES-flagged row; blank otherwise.

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [the condition in its weakest form — Status-Quo Rubric territory]
GROUNDED: [the Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to the final rubric section until every essential criterion in
the Audit Table shows Inertia Test = NO (original or Auditor-revised). A table with any YES in
the Inertia Test column is an incomplete audit.**

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. For any criterion where the Audit Table shows Revision
Required = YES, substitute the Revised Condition. This is the canonical criteria table.

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

**Anchor: V-03**

V-03 is designated the combination anchor for all Round 3 combination runs.

**Structural impact**: V-03's Author/Auditor separation produces two independently readable
artifacts — the Author's draft table and the Auditor's structured audit table with Discriminating
Element column. This makes the authoring and auditing outputs separately inspectable in the
final document, satisfying C-17 (phase separation) and C-18 (reasoning captured per condition)
simultaneously. No other single-axis variation in this round targets both criteria.

**Isolation quality**: Only the role structure changes. The failure-mode enumeration protocol
(Phase 1), the criteria content format (five fields), and the scoring formula are structurally
identical to V-01 and V-02. The Author/Auditor split is the only variable; co-variation observed
in combination runs traces to this structure.

**Detectable failure condition**: If a combination-run builder collapses the Auditor phase into
the Author phase, the Discriminating Element column will be absent from the output or appear
as part of the Author's drafting inline text. The gap is visible as a missing Audit Table section,
not as degraded quality — mechanical and auditable. A builder who produces an audit table but
omits the Discriminating Element column fails C-18 with a structurally visible gap (empty column)
rather than a quality judgment.

**Combination priority**: V-05 (V-03 × V-01) is the highest-priority combination. V-03's Auditor
phase captures discriminating-element reasoning (C-18); V-01's Author-phase gates enforce
temporal pair-writing (C-14) and two-level gate structure (C-16). The combination tests whether
Author-phase structural enforcement and Auditor-phase reasoning capture address different failure
modes (C-14 fires when the Author defers; C-18 fires when the Auditor omits reasoning) or the
same failure mode (both fire when the builder rushes). If orthogonal, V-05 is the R3 candidate
for the golden prompt.

---

## Combination Roadmap (for Round 4)

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-03 × V-01 | role-sequence × lifecycle-emphasis | C-14, C-16, C-17, C-18 | 1 (= V-05 this round) | Tested in R3 |
| V-03 × V-02 | role-sequence × output-format | C-15, C-17, C-18 | 2 | V-02's named blocks make Auditor gaps visible; V-03's Discriminating Element column captures reasoning. Tests if structural visibility (V-02) and social auditing (V-03) address different failure modes. |
| V-01 × V-03 × V-02 | all three axes | C-14, C-15, C-16, C-17, C-18 | 3 | Three-axis full combination — run only if R3 two-axis combinations reveal orthogonal failure modes requiring all three mechanisms simultaneously. Axis tension: V-02's Phase 7 block audit and V-03's Auditor phase both review the essential criteria — determine which fires first to avoid confounded attribution. |

**Axis tension note before combination:** V-02 (output-format) and V-03 (role-sequence) both audit
essential pass conditions — V-02 via a Phase 7 completeness audit (block-level) and V-03 via the
Auditor's inertia-test table. In a three-axis combination, both mechanisms fire on the same
criteria. The dominant variable is expected to be V-03 (role-sequence): the Auditor's structured
table produces named reasoning artifacts, while V-02's Phase 7 audit only checks block presence.
If the combination result does not exceed V-03 alone on C-18, V-02's block audit is the
confounding variable and should be scoped to Phase 2 only in the three-axis run.
