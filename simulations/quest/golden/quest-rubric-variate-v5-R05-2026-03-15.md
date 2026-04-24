# quest-rubric Variate — Round 5 against rubric v5

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v5 (C-01 through C-25; essential C-01–C-05)
**Round:** R5 — 3 single-axis + 2 combination

**Round 5 design note:** Round 4 produced three excellence signals absorbed into v5 as aspirational
criteria: C-23 (structural verification phase gates Auditor entry, from V-05), C-24 (three-level
verification chain with non-overlapping defect classes, from V-05), C-25 (anti-deferral prohibition
co-located at sub-step level, from V-05). R4 V-05 is the leading variation at composite 77.6
(Acceptable). The universal floor blocking Golden is three criteria that R4's full three-axis
combination still fails:

- **C-06** (category diversity, recommended): requires >= 3 distinct categories across all criteria.
  R4's prompts derive criteria from failure modes with no explicit category audit — natural clustering
  in correctness and format leaves depth and coverage unrepresented.
- **C-07** (severity ordering, recommended): requires essential criteria ordered most to least
  structurally critical. R4's prompts sequence criteria by derivation order (order failure modes
  were enumerated), not by explicit severity ranking.
- **C-10** (no redundancy, aspirational): requires that no two criteria overlap such that passing
  one guarantees passing the other. R4's inertia test checks per-criterion specificity but not
  cross-criterion redundancy.

C-06 and C-07 are each worth 10 composite points. Either one alone lifts V-05 from 77.6 to >= 87.6,
clearing the Golden threshold of 80. C-10 contributes 0.6 points (1/17 × 10). Round 5 targets all
three gaps with explicit mechanism additions to the R4 V-05 base.

**Structural clarification in all R5 variations:** Phase 7 (heading-scan) is repositioned from
end-of-document (after Auditor) to between Author Phase end and Auditor Phase start. R4 V-05 had
"The Auditor phase cannot begin until all heading patterns are present" as language in a
post-Auditor Phase 7 — C-23 passed via language. R5 makes document order match: the heading-scan
now gates Auditor entry by position, not only by language.

---

## Round 5 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | lifecycle-emphasis | single-axis | CATEGORY-COVERAGE GATE after Author Phase 3 — requires >= 3 distinct categories before Structural Verification | C-06 |
| V-02 | lifecycle-emphasis | single-axis | SEVERITY-RANK step after Author Phase 1 — failure modes ranked, essential criteria assigned in ranked order | C-07 |
| V-03 | role-sequence | single-axis | REDUNDANCY-CHECK TABLE in Auditor phase — pairwise essential criterion pairs checked for overlap | C-10 |
| V-04 | lifecycle-emphasis × lifecycle-emphasis | combination (V-01 × V-02) | Category-coverage gate + severity-rank sequencing | C-06, C-07 |
| V-05 | lifecycle-emphasis × lifecycle-emphasis × role-sequence | combination (V-01 × V-02 × V-03) | Category gate + severity rank + redundancy check | C-06, C-07, C-10 |

**Anchor designation (preliminary):** V-04. See anchor section at end.

---

## V-01 — Lifecycle Emphasis: Category-Coverage Gate

**axis:** lifecycle-emphasis
**hypothesis:** C-06 requires at least 3 distinct categories (correctness / depth / format /
coverage / behavior) across all criteria. R4 V-05's Author phase derives criteria from failure
modes with no explicit category audit. The result clusters criteria in whatever categories the
failure modes naturally suggest — often correctness (does the output contain the right content?)
and format (is it structured correctly?), leaving depth and coverage unrepresented. V-01 adds one
gate at the end of Author Phase 3, after all criteria are drafted: count distinct categories across
the full criteria set and require >= 3 before proceeding to Structural Verification. The gate fires
after the full set is visible because category coverage is an emergent property — per-criterion
gates cannot enforce it. Failure condition: if C-06 pass rates do not improve relative to R4 V-05,
either (a) authors already produce >= 3 categories naturally without the gate, or (b) the gate
fires but authors patch it trivially (adding a coverage-category criterion with a weak pass
condition) without producing real coverage insight.

---

You are building a scoring rubric for a Signal skill. Three mechanisms enforce quality: named
section blocks that make structural omission detectable by heading scan; forward-blocking per-
criterion gates that prevent deferral; and an Auditor phase that reads all criteria as a set
before producing a single consolidated audit table. All three outputs appear in the final document.
A category-coverage gate after criteria drafting verifies that the rubric spans at least 3 of the
5 canonical category dimensions.

**Why three mechanisms plus a category gate?**

Named blocks with heading-scan audit catch blocks that were skipped. Forward-blocking gates prevent
the skip from occurring in the first place. The Auditor's consolidated table enables cross-criterion
pattern analysis. The category gate ensures the rubric can detect failures across multiple
dimensions of the target skill — a rubric where all criteria cluster in one category (e.g., all
format checks) misses entire failure surfaces.

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

**DO NOT advance to Author Phase 2 Entry Gate until this minimum is met.**

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] At least 3 blocking failure modes are listed in Author Phase 1
- [ ] At least 2 degrading failure modes are listed in Author Phase 1
- [ ] At least 3 distinct output-contract categories are identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3-5)**

For each essential criterion, produce the three named blocks in order, then record the criterion
row. The blocks must use the exact heading patterns shown — these patterns are what the Structural
Verification heading-scan checks.

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
not required for these tiers.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE — DO NOT proceed to Structural Verification until:**

Count the distinct categories across all criteria written in Phases 2 and 3 (essential +
recommended + aspirational). The five canonical categories are:
`correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Distinct categories present (list each one): ___________________________
- [ ] Count of distinct categories: ___ (minimum required: 3)

If fewer than 3 distinct categories appear: add or revise criteria in Phase 3 to reach the
minimum before proceeding. A rubric where all criteria cluster in one or two categories (e.g.,
all correctness and format, with no depth, coverage, or behavior criterion) cannot detect
multi-dimensional failure patterns in the target skill and fails C-06.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (Phase 7 — runs before Auditor Phase)

Scan the Author phase output for section headings matching the patterns below. This is a
heading-pattern scan — a heading is present or absent; its content is not evaluated here.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A missing heading indicates a Phase 2 forward gate was bypassed. Write the missing block using
the exact heading pattern shown, then re-check.

**The Auditor Phase cannot begin until every required heading pattern is confirmed present and
correctly ordered. Structural completeness is a prerequisite for reasoning analysis.**

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
enumeration) or cluster in one type.

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to the Final Rubric until:**

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

---

## V-02 — Lifecycle Emphasis: Severity-Rank Sequencing

**axis:** lifecycle-emphasis
**hypothesis:** C-07 requires essential criteria ordered from most to least structurally critical —
the first essential criterion represents the highest-stakes failure mode. R4 V-05's Author phase
lists failure modes and then derives criteria, but the sequencing within Phase 2 follows the order
failure modes were enumerated, not an explicit severity ranking. A builder who lists "missing
checklist" before "missing field in every criterion" produces C-01 as the checklist criterion —
passing C-07 only by luck if the enumeration happened to go highest-stakes-first. V-02 adds a
SEVERITY-RANK step after the failure modes are listed but before Phase 2 begins: rank the blocking
failure modes from most to least critical, then carry that ranking into Phase 2 so that C-01
targets rank-1, C-02 targets rank-2, and so on. Failure condition: if C-07 pass rates do not
improve relative to R4 V-05, either (a) authors already enumerate failure modes in severity order
naturally, making the explicit ranking redundant, or (b) the ranking step produces severity-ordered
failure modes but the author does not maintain that order when writing the criteria table.

---

You are building a scoring rubric for a Signal skill. Three mechanisms enforce quality: named
section blocks that make structural omission detectable by heading scan; forward-blocking per-
criterion gates that prevent deferral; and an Auditor phase that reads all criteria as a set
before producing a single consolidated audit table. A severity-ranking step after failure mode
enumeration ensures essential criteria are sequenced from highest-stakes to lowest-stakes failure
mode.

**Why three mechanisms plus severity ranking?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. The consolidated audit
table enables cross-criterion pattern analysis. Severity ranking at the end of Phase 1 ensures
that the first essential criterion targets the failure that makes the output completely
non-functional — not the failure that happened to be listed first.

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

**AUTHOR PHASE 1 — SEVERITY RANKING**

Before writing any criterion, rank the blocking failure modes from most to least critical.

Most critical: the failure that makes the output non-functional as an objective function
regardless of all other criteria passing — a downstream evaluator (quest-golden) cannot run at
all if this failure is present.

Least critical (among blocking): the failure that makes the output structurally invalid but
whose absence could be patched most easily without re-running the skill.

```
SEVERITY RANK:
1. [most critical blocking failure mode from Phase 1 — C-01 will target this]
2. [second most critical]
3. [third most critical]
[continue if more than 3 blocking failure modes were listed]
```

**DO NOT advance to Author Phase 2 Entry Gate until the severity rank is written.**

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] At least 3 blocking failure modes are listed in Author Phase 1
- [ ] At least 2 degrading failure modes are listed in Author Phase 1
- [ ] Severity rank is complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories are identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3-5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02 targets
rank-2, and so on. The first criterion written must address the failure that makes the output
completely non-functional. If you write a criterion that does not address its corresponding
severity-rank entry, swap before proceeding to the next criterion.

For each essential criterion, produce the three named blocks in order, then record the criterion
row. The blocks must use the exact heading patterns shown.

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
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
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
- [ ] Severity-rank alignment field confirms this criterion targets the correct rank entry

This is a forward-blocking gate, not a repair check.

After all conditions are confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (Phase 7 — runs before Auditor Phase)

Scan the Author phase output for section headings matching the patterns below. Pattern scan only —
content is not evaluated here.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A missing heading indicates a Phase 2 forward gate was bypassed. Write the missing block, then
re-check.

**The Auditor Phase cannot begin until every required heading pattern is confirmed present and
correctly ordered.**

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing any
audit output. Do not write audit rows one at a time.

**Inertia test (apply to each essential pass condition):**
- YES: generic — write the revision in the Revised Condition column
- NO: skill-specific — name the discriminating element

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence noting whether discriminating elements
are varied or cluster in one type. Also confirm that C-01's pass condition addresses the rank-1
(most critical) failure mode — if not, flag for ordering revision.

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to Final Rubric until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank ordering confirmed: C-01 addresses the most critical failure mode

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with Auditor-revised conditions substituted where
Revision Required = YES. Essential criteria must appear in severity-rank order (C-01 = most
critical). This is the canonical criteria table.

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

## V-03 — Role Sequence: Pairwise Redundancy Check

**axis:** role-sequence
**hypothesis:** C-10 requires that no two criteria overlap such that passing one guarantees passing
the other. R4 V-05's Auditor phase checks per-criterion specificity (inertia test: does this
condition discriminate against the status-quo rubric?) but does not check cross-criterion
uniqueness (is there a rubric output that passes one but fails the other for a non-trivial reason?).
A builder can produce criteria that each individually pass the inertia test — each anchors to a
skill-specific element — while two criteria address the same failure mode from overlapping angles
(e.g., C-01 requires every criterion row to have five fields, and C-03 requires every pass
condition to be non-empty — passing C-03 does not guarantee C-01 passes if other fields are missing,
so they are independent; but if C-01 required "non-empty pass condition" and C-04 separately
required "non-empty pass condition," the pair would be redundant). V-03 adds a REDUNDANCY-CHECK
TABLE to the Auditor phase after the Audit Table and cross-criterion pattern note: for each pair
of essential criteria, ask whether there exists a rubric output that passes one but fails the other
for a non-trivial reason. If NO (they always agree), one criterion is redundant. Failure condition:
if C-10 pass rates do not improve relative to R4 V-05, either (a) the inertia test implicitly
prevents redundancy by forcing skill-specific anchors that are naturally distinct, or (b) the
redundancy check identifies redundant pairs but the builder does not revise.

---

You are building a scoring rubric for a Signal skill. Three mechanisms enforce quality: named
section blocks that make structural omission detectable by heading scan; forward-blocking per-
criterion gates that prevent deferral; and an Auditor phase that reads all criteria as a set before
producing a single consolidated audit table and a pairwise redundancy check. All outputs appear
in the final document.

**Why three mechanisms plus redundancy check?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. The Auditor's
consolidated table enables cross-criterion specificity analysis. The redundancy check verifies that
no two criteria are asking the same question from different angles — a rubric with redundant
criteria double-counts one failure mode while leaving another unmeasured.

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

**DO NOT advance to Author Phase 2 Entry Gate until this minimum is met.**

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] At least 3 blocking failure modes are listed in Author Phase 1
- [ ] At least 2 degrading failure modes are listed in Author Phase 1
- [ ] At least 3 distinct output-contract categories are identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3-5)**

For each essential criterion, produce the three named blocks in order, then record the criterion
row.

**Sub-step 2a — Draft the pass condition.**

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
Do not produce all calibration pairs after all pass conditions are finalized.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [condition text applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` block present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` block present above, written before this gate check

After both confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (Phase 7 — runs before Auditor Phase)

Scan for section headings matching the patterns below. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block using the exact heading pattern shown, then re-check.

**The Auditor Phase cannot begin until every required heading pattern is confirmed present and
correctly ordered.**

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing any
audit output.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:**

Scan the Discriminating Element column. Write one sentence noting whether discriminating elements
are varied or cluster in one type.

**REDUNDANCY CHECK TABLE**

For each pair of essential criteria, ask: Is there a rubric output that passes one criterion but
fails the other for a non-trivial reason?

- **YES**: the criteria are independent — each adds unique signal about a distinct failure mode.
  Keep both.
- **NO**: the criteria are redundant — passing one always means passing the other. One must be
  revised to address a distinct failure mode, consolidated, or removed.

| Pair | Pass-One-Fail-Other? | Non-trivial Reason (or Why Always-Agree) | Action |
|------|---------------------|------------------------------------------|--------|
| C-01 / C-02 | YES/NO | [reason a rubric output could pass one but fail the other — or why they always agree] | Keep / Revise |
| C-01 / C-03 | YES/NO | ... | ... |
| C-01 / C-04 | YES/NO | ... | ... |
| C-01 / C-05 | YES/NO | ... | ... |
| C-02 / C-03 | YES/NO | ... | ... |
| C-02 / C-04 | YES/NO | ... | ... |
| C-02 / C-05 | YES/NO | ... | ... |
| C-03 / C-04 | YES/NO | ... | ... |
| C-03 / C-05 | YES/NO | ... | ... |
| C-04 / C-05 | YES/NO | ... | ... |

[Add rows for any additional essential criteria pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs are evaluated
- [ ] All pairs show YES (each criterion adds unique signal), OR
- [ ] Any NO-flagged pair is resolved: the redundant criterion revised, consolidated, or removed,
      and the pair re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to Final Rubric until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Redundancy Gate cleared: all pairs show YES or NO-flagged pairs resolved

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with Auditor-revised conditions substituted where
Revision Required = YES.

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

## V-04 — Lifecycle Emphasis × Lifecycle Emphasis (V-01 × V-02, Combination)

**axis:** lifecycle-emphasis × lifecycle-emphasis
**hypothesis:** V-01 adds a CATEGORY-COVERAGE GATE after Author Phase 3, targeting C-06. V-02
adds a SEVERITY-RANK step after Author Phase 1, targeting C-07. These mechanisms operate at
different lifecycle positions (end of Phase 3 vs. end of Phase 1) and check orthogonal properties
(categorical breadth of the full criteria set vs. ordering of the essential criteria tier). They
do not compete or confound: the severity rank cannot produce category coverage, and the category
gate cannot produce severity ordering. Combined, they should pass both C-06 and C-07 simultaneously.
Either one alone is sufficient to reach Golden (each recommended criterion is worth 10 composite
points; Golden threshold is 80; V-05 R4 base scores 77.6). Both together reach 97.6. Failure
condition: if C-06 or C-07 fails in V-04 while passing in V-01 or V-02 respectively, the
mechanisms interact negatively — adding severity ranking disrupts category coverage, or vice versa.
Expected result: both pass independently, confirming orthogonality.

---

You are building a scoring rubric for a Signal skill. Four mechanisms enforce quality: named
section blocks that make structural omission detectable by heading scan; a severity-ranking step
that sequences essential criteria from most to least critical failure mode; forward-blocking per-
criterion gates that prevent deferral; and an Auditor phase that produces a consolidated audit
table. A category-coverage gate after criteria drafting verifies that the rubric spans at least
3 of the 5 canonical category dimensions. All outputs appear in the final document.

**Why four mechanisms?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking ensures
C-01 targets the failure that makes the output completely non-functional — not the failure that
was listed first. The category gate ensures the rubric detects failures across multiple dimensions
rather than clustering in one category. The consolidated Auditor table enables cross-criterion
pattern analysis.

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

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank the blocking failure modes from most to least critical before writing any criterion.
Most critical = the failure that makes the output non-functional as an objective function
regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 will target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

**DO NOT advance to Author Phase 2 Entry Gate until the severity rank is written.**

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] At least 3 blocking failure modes are listed in Author Phase 1
- [ ] At least 2 degrading failure modes are listed in Author Phase 1
- [ ] Severity rank is complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories are identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3-5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02 targets
rank-2, and so on.

For each essential criterion, produce the three named blocks in order, then record the criterion
row.

**Sub-step 2a — Draft the pass condition.**

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, pattern, or enumeration from this skill's contract]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

Produce it now — immediately after sub-step 2b. Do not produce all calibration pairs after all
pass conditions are finalized: write each pair at the moment the pass condition it calibrates is
drafted.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [condition text applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check
- [ ] Severity-rank alignment field confirms correct rank-N assignment

After all confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE — DO NOT proceed to Structural Verification until:**

Count distinct categories across ALL criteria (essential + recommended + aspirational).
Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list): ___________________________
- [ ] Count: ___ (minimum: 3)

If fewer than 3 categories appear: add or revise criteria in Phase 3 before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (Phase 7 — runs before Auditor Phase)

Scan for section headings matching the patterns below. Pattern scan only.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block using the exact heading pattern, then re-check.

**The Auditor Phase cannot begin until every required heading pattern is confirmed present and
correctly ordered.**

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing any
audit output. Do not write audit rows one at a time.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:**

Scan the Discriminating Element column. Write one sentence noting whether discriminating elements
are varied or cluster in one type. Also confirm C-01 addresses the rank-1 failure mode.

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to Final Rubric until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with Auditor-revised conditions substituted where
Revision Required = YES. Essential criteria in severity-rank order.

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

## V-05 — Lifecycle Emphasis × Lifecycle Emphasis × Role Sequence (V-01 × V-02 × V-03, Three-Axis Combination)

**axis:** lifecycle-emphasis × lifecycle-emphasis × role-sequence
**hypothesis:** V-01 adds CATEGORY-COVERAGE GATE targeting C-06. V-02 adds SEVERITY-RANK targeting
C-07. V-03 adds REDUNDANCY-CHECK TABLE targeting C-10. V-04 (V-01 × V-02) should already reach
Golden by clearing C-06 and C-07. V-05 extends V-04 by adding V-03's pairwise redundancy check
to also clear C-10, raising the aspirational score from 13/17 to 14/17 (from 7.6 to 8.2) and
pushing the composite from 97.6 to 98.2. The three mechanisms operate at non-competing lifecycle
positions: severity rank fires at end of Phase 1; per-criterion forward gates fire per-criterion
in Phase 2; category gate fires after Phase 3; redundancy check fires in the Auditor phase. No
axis tension between C-06/C-07 mechanisms (both lifecycle-emphasis additions in Author phase) and
C-10 mechanism (role-sequence addition in Auditor phase). Failure condition: if V-04 already
reaches Golden and V-05 does not improve over V-04 on C-10, the redundancy check adds no benefit
beyond what the inertia test already enforces.

---

You are building a scoring rubric for a Signal skill. Five mechanisms enforce quality: a severity-
ranking step that sequences essential criteria from most to least critical; named section blocks
that make structural omission detectable by heading scan; forward-blocking per-criterion gates
that prevent deferral; a category-coverage gate verifying the rubric spans at least 3 canonical
category dimensions; and an Auditor phase that produces both a consolidated audit table and a
pairwise redundancy check. All outputs appear in the final document.

**Why five mechanisms?**

Severity ranking ensures C-01 targets the highest-stakes failure mode — not the first one listed.
Named blocks make omission visible by section-heading scan without reading content. Forward-blocking
gates prevent the omission in the first place. The category gate ensures multi-dimensional failure
coverage. The Auditor's consolidated table enables cross-criterion specificity analysis; the
redundancy check ensures no two criteria address the same failure from overlapping angles.

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

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank the blocking failure modes from most to least critical.

```
SEVERITY RANK:
1. [most critical — C-01 will target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

**DO NOT advance to Author Phase 2 Entry Gate until the severity rank is written.**

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] At least 3 blocking failure modes are listed
- [ ] At least 2 degrading failure modes are listed
- [ ] Severity rank is complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories are identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3-5)**

Write essential criteria in severity-rank order: C-01 targets rank-1, C-02 targets rank-2, and
so on. For each essential criterion, produce the three named blocks in order, then record the
criterion row.

**Sub-step 2a — Draft the pass condition.**

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Inertia test: Could "the output is clear and comprehensive" pass this? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition producing NO]
Skill-specific element: [count, field name, pattern, or enumeration from this skill's contract]
Severity-rank alignment: [confirm: this criterion targets rank-N — "[failure mode]"]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

Produce it now — immediately after sub-step 2b, while this pass condition is in working memory.
Do not produce all calibration pairs after all pass conditions are finalized: write each pair
at the moment the pass condition it calibrates is drafted.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [condition text applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check
- [ ] Severity-rank alignment field confirms correct rank-N assignment

After all confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2-3 recommended and 1-2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE — DO NOT proceed to Structural Verification until:**

Count distinct categories across ALL criteria (essential + recommended + aspirational).
Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list): ___________________________
- [ ] Count: ___ (minimum: 3)

If fewer than 3 categories appear: add or revise criteria in Phase 3 before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (Phase 7 — runs before Auditor Phase)

Scan for section headings matching the patterns below. Pattern scan only — content not evaluated.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block using the exact heading pattern, then re-check.

**The Auditor Phase cannot begin until every required heading pattern is confirmed present and
correctly ordered. Structural completeness is a prerequisite for reasoning analysis.**

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing any
audit output. Do not write audit rows one at a time.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Cross-criterion pattern note:**

Scan the Discriminating Element column. Write one sentence noting whether discriminating elements
are varied or cluster in one type. Confirm C-01 addresses the rank-1 failure mode.

**REDUNDANCY CHECK TABLE**

For each pair of essential criteria, ask: Is there a rubric output that passes one but fails the
other for a non-trivial reason?

- **YES**: independent — each adds unique signal. Keep both.
- **NO**: redundant — passing one always means passing the other. One must be revised.

| Pair | Pass-One-Fail-Other? | Non-trivial Reason (or Why Always-Agree) | Action |
|------|---------------------|------------------------------------------|--------|
| C-01 / C-02 | YES/NO | [reason] | Keep / Revise |
| C-01 / C-03 | YES/NO | ... | ... |
| C-01 / C-04 | YES/NO | ... | ... |
| C-01 / C-05 | YES/NO | ... | ... |
| C-02 / C-03 | YES/NO | ... | ... |
| C-02 / C-04 | YES/NO | ... | ... |
| C-02 / C-05 | YES/NO | ... | ... |
| C-03 / C-04 | YES/NO | ... | ... |
| C-03 / C-05 | YES/NO | ... | ... |
| C-04 / C-05 | YES/NO | ... | ... |

[Add rows for additional essential criteria pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE: DO NOT proceed to Final Rubric until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] Redundancy Gate cleared: all pairs show YES or NO-flagged pairs resolved

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with Auditor-revised conditions substituted where
Revision Required = YES. Essential criteria in severity-rank order.

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

**Structural impact:** V-04 targets C-06 and C-07 simultaneously — the two recommended criteria
whose failure holds V-05 R4 below Golden. Either one alone is sufficient to cross the Golden
threshold (77.6 + 10 = 87.6). Both together reach 97.6. The mechanisms are non-competing: the
severity-rank step fires at Author Phase 1 end and governs intra-essential-tier ordering; the
category-coverage gate fires at Author Phase 3 end and governs the full criteria set's categorical
breadth. Neither mechanism can produce the other's effect.

**Isolation quality:** Each mechanism in V-04 is tested independently in V-01 and V-02. V-01
isolates C-06 improvement; V-02 isolates C-07 improvement. If V-04 passes both while V-01 only
passes C-06 and V-02 only passes C-07, the combination is confirmed additive with no interaction
effect. If V-04 fails one that the single-axis variation passed, an interaction effect exists and
must be investigated.

**Detectable failure conditions:**
- C-06 fails in V-04 but passes in V-01: the severity-rank step disrupts category coverage (e.g.,
  severity ranking causes the author to write all essential criteria in the same high-criticality
  domain, reducing category diversity). Fix: add category-diversity check to the Phase 2 entry
  gate, not only Phase 3.
- C-07 fails in V-04 but passes in V-02: the category gate disrupts severity ordering (unlikely —
  category gate fires after Phase 3, which is after essential criteria are written). If this occurs,
  investigate whether the author revises essential criteria during Phase 3 expansion.

**Combination priority for Round 6:**

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-05 (this round) | all three | C-06, C-07, C-10 | 1 | Golden + maximum aspirational — test if C-10 adds without interfering |
| V-04 × phrasing-register | category-gate × severity-rank × formal framing | C-06, C-07 | 2 | Test whether formal/technical phrasing register improves compliance with the severity-rank step (if C-07 still fails in V-02, the mechanism is understood but not followed — register change may help) |
| V-01 × inertia-framing | category-gate × prominent status-quo competitor | C-06, C-11 | 3 | Test whether making the Status-Quo Rubric a named competitor framing (not just an implicit test) improves both category diversity and inertia test depth |

---

## Combination Roadmap (for Round 6)

**R4 roadmap carryover:** R4 nominated V-03×V-02 (role-sequence × lifecycle-emphasis, C-20/C-21/C-22)
and V-03×V-01 (role-sequence × output-format, C-19/C-21) as R5 priorities. These are absorbed: R5's
gaps are C-06, C-07, C-10, not C-19–C-22 (all of which V-05 R4 already passes by construction).
The C-19–C-22 combinations from R4's roadmap are retired — they are maintenance variations, not
gap-closing variations.

**R5 outcome scenarios:**

| Scenario | Expected Outcome | Round 6 Action |
|----------|-----------------|----------------|
| V-04 reaches Golden | C-06 and C-07 both fixed | Run V-05 to test C-10 gain; investigate remaining aspirational gaps if any |
| V-01 passes C-06, V-02 fails C-07 | Severity-rank step is insufficient | Investigate: is the rank written but ordering not maintained? Add severity-order verification to FINAL RUBRIC step |
| V-01 fails C-06 | Category gate fires but authors add trivial criteria | Tighten: require the gate to verify that each new criterion has a distinct discriminating element from existing criteria, not just a different category label |
| V-03 passes C-10 | Redundancy check produces revisions | Examine what pairs were flagged — these reveal structural patterns in how criteria cluster |
| V-03 fails C-10 | Redundancy check produces no revisions | Investigate: are criteria always non-redundant by construction (inertia test prevents overlapping anchors), or are builders declaring YES without genuine analysis? |
