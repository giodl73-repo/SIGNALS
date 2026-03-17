# quest-rubric Variate — Round 6 against rubric v6

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v6 (C-01 through C-28; essential C-01–C-05)
**Round:** R6 — 3 single-axis + 2 combination

**Round 6 design note:** Round 5 produced three excellence signals absorbed into v6 as
aspirational criteria: C-26 (phase-level workflow transitions marked by named section headings,
ES-R5-1), C-27 (cross-criterion verification produces named artifact with forward-blocking gate,
ES-R5-2), C-28 (scoring formula denominators annotated with criterion ID range, ES-R5-3).

R5 V-05 is the anchor. Under the v6 rubric:

**R5 V-05 score under v6:**
- Essential (5/5): all pass → 60
- Recommended (3/3): C-06 (category gate), C-07 (severity rank), C-08 (quick checklist) → 30
- Aspirational (18/20):
  - C-09–C-25: all pass (R5 V-05 satisfies each by construction)
  - C-26: PASS — `### AUTHOR PHASE`, `### STRUCTURAL VERIFICATION`, `### AUDITOR PHASE` are
    present in sequence; inter-phase gate position verifiable by heading scan alone
  - C-27: FAIL — redundancy check uses `**REDUNDANCY CHECK TABLE**` (bold), not a `###` heading;
    its omission would not produce a missing heading detectable by section scan
  - C-28: FAIL — formula uses variable `N_aspirational` with no criterion ID range annotation;
    maintainer cannot verify denominator correctness from the formula alone
  → 18/20 × 10 = 9.0

**Composite: 99.0 → Golden.**

The two gaps blocking 100.0 are C-27 and C-28. Both are structural format fixes: they change
HOW existing mechanisms present their output, not WHETHER they exist. Round 6 closes these with
the output-format axis and runs phrasing-register and inertia-framing as exploratory axes to
test whether generated rubric quality (C-07, C-11, C-12 compliance) improves under different
framing registers.

**Round 6 axis selection:**

| Axis | What changes | Criteria targeted |
|------|-------------|-------------------|
| phrasing-register | Formal declarative language: PRECONDITION, INVARIANT, CONSTRAINT labels for gates and anti-deferral instruction | C-07, C-22, C-25 (quality improvement in generated rubric) |
| inertia-framing | Named Status-Quo Rubric competitor throughout; GENERIC label → STATUS-QUO; inertia test question references the competitor explicitly | C-11, C-12 (quality improvement in generated rubric) |
| output-format | `**REDUNDANCY CHECK TABLE**` → `### REDUNDANCY-CHECK-TABLE`; scoring formula annotated with criterion ID range | C-27, C-28 (structural gap close) |

No interaction risk: phrasing changes only language, inertia-framing changes calibration-pair
labels and inertia test phrasing, output-format changes one heading and adds a formula annotation
instruction. None of the three modifies another's mechanism.

---

## Round 6 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | phrasing-register | single-axis | Formal/declarative: PRECONDITION, INVARIANT, CONSTRAINT for gates and anti-deferral | C-07, C-22, C-25 |
| V-02 | inertia-framing | single-axis | Named Status-Quo Rubric competitor; GENERIC → STATUS-QUO in calibration pairs; inertia test question names competitor | C-11, C-12 |
| V-03 | output-format | single-axis | `**REDUNDANCY CHECK TABLE**` → `### REDUNDANCY-CHECK-TABLE`; formula annotation requires criterion ID range | C-27, C-28 |
| V-04 | phrasing-register × inertia-framing | combination (V-01 × V-02) | Formal language + named competitor | C-07, C-11, C-12, C-22, C-25 |
| V-05 | phrasing-register × inertia-framing × output-format | combination (V-01 × V-02 × V-03) | Full: formal language + named competitor + annotated formula + named redundancy heading | C-07, C-11, C-12, C-22, C-25, C-27, C-28 |

**Anchor designation (preliminary):** V-05. See anchor section at end.

**Score projections under v6 rubric:**

| Variation | C-27 | C-28 | Asp/20 | Composite | Band |
|-----------|------|------|--------|-----------|------|
| R5 V-05 (base) | FAIL | FAIL | 18/20 | 99.0 | Golden |
| V-01 | FAIL | FAIL | 18/20 | 99.0 | Golden |
| V-02 | FAIL | FAIL | 18/20 | 99.0 | Golden |
| V-03 | PASS | PASS | 20/20 | 100.0 | Golden |
| V-04 | FAIL | FAIL | 18/20 | 99.0 | Golden |
| V-05 | PASS | PASS | 20/20 | 100.0 | Golden |

All variations are Golden. V-03 and V-05 achieve maximum composite under v6.

---

## V-01 — Phrasing Register: Formal/Technical Constraints

**axis:** phrasing-register
**hypothesis:** R5 V-05 uses imperative-conversational instructions ("Write essential criteria
in severity-rank order", "Produce it now — immediately after sub-step 2b, while this pass
condition is in working memory"). These convey the requirement correctly but permit
rationalization: a builder reading "write each pair at the moment..." can reinterpret it as
"approximately at that time — grouping them at the end of the phase is close enough in spirit."
V-01 replaces conversational framing with formal specification vocabulary: PRECONDITION marks
conditions that must hold before a step; INVARIANT names properties that must hold throughout a
phase; CONSTRAINT names an obligation that cannot be deferred. Formal vocabulary imports
programmer intuitions about preconditions and invariants — properties that are checked, not
merely recommended. Failure condition: if C-07 and C-22/C-25 pass rates do not improve relative
to R5 V-05, either (a) conversational language was already sufficient, or (b) the remaining gap
is in content quality (e.g., severity ranking is done but does not select the highest-stakes
failure mode correctly), which a register change cannot fix.

---

You are executing a scoring-rubric construction protocol for a Signal skill. This protocol
enforces quality through five mechanisms with formal invariants. Violating any invariant
invalidates the step it governs.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria appear in order from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure that makes the output non-functional
  regardless of other criteria
- **M-02 — named-blocks:** every mandatory check output appears as a `### HEADING [C-NN]`
  section block; a missing block is a missing section heading detectable by scan without
  reading content
- **M-03 — forward-blocking gates:** each per-criterion gate fires before the next criterion
  is written; gates prevent omission; retroactive repair is not a substitute for a gate
- **M-04 — category-coverage:** at least 3 of 5 canonical categories must appear across all
  criteria (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria are read before Auditor output is produced; a
  consolidated table and pairwise redundancy check are required

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear in the output unless all required preceding
  named blocks (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) for that
  criterion are confirmed present above it
- INVARIANT B: the `### CALIBRATION-PAIR [C-NN]` block for criterion C-NN is written
  immediately after the `### INERTIA-RECORD [C-NN]` block for C-NN — not after all
  INERTIA-RECORD blocks are complete

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking and 2 degrading failure modes must be listed before
advancing. DO NOT proceed to SEVERITY RANKING until this constraint is satisfied.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank the blocking failure modes from most to least critical.

DEFINITION (most critical): the failure that makes the output non-functional as an objective
function regardless of all other criteria passing — quest-golden cannot run at all if this
failure is present.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes listed above]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank is complete and every blocking
failure mode from Phase 1 appears in the rank.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed in Author Phase 1
- [ ] At least 2 degrading failure modes listed in Author Phase 1
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02
targets rank-2, and so on. For each essential criterion, apply sub-steps 2a through 2d in
sequence. The three named blocks must use the exact heading patterns shown.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: the pass condition must be specific and observable — verifiable by two
independent evaluators without discussion. A condition containing only vague language
("good", "sufficient", "appropriate") with no concrete anchor violates this constraint.

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

CONSTRAINT 2b: the INERTIA-RECORD block must be produced before the CALIBRATION-PAIR block
for the same criterion. Producing CALIBRATION-PAIR first violates INVARIANT A.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

VIOLATION: deferring calibration pair production to after all pass conditions are finalized
(batch-producing all `### CALIBRATION-PAIR` blocks at the end of the phase) satisfies the
structural block ordering (CALIBRATION-PAIR precedes CRITERION) while violating INVARIANT B.
Do not defer. Batch production is a violation even if structural order is preserved.

```
### CALIBRATION-PAIR [C-NN]
GENERIC: [condition text applying to any artifact — Status-Quo Rubric]
GROUNDED: [condition naming the skill-specific element from INERTIA-RECORD; references
  target skill by name or output-contract term]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion in the table and advancing to the next criterion:

- [ ] `### INERTIA-RECORD [C-NN]` present above with inertia test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above, written before this gate check and
      before this criterion's table row (INVARIANT B confirmed satisfied)
- [ ] Severity-rank alignment field confirms this criterion targets rank-N failure mode

CONSTRAINT 2d: this is a forward-blocking gate. If any precondition is false, do not record
the criterion row. Write the missing block or correct the alignment, then re-check. A criterion
row produced before its preconditions are satisfied violates INVARIANT A.

After all preconditions are confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format. Sub-step
protocol not required for recommended/aspirational tiers.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

PRECONDITION for Structural Verification: at least 3 distinct categories appear across all
criteria (essential + recommended + aspirational).

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count of distinct categories: ___ (minimum required: 3)

CONSTRAINT: if fewer than 3 categories are present, add or revise criteria in Phase 3 before
proceeding. A rubric clustering all criteria in one or two categories cannot detect
multi-dimensional failure patterns in the target skill and fails C-06.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

Scan the Author phase output for section headings matching the patterns below. This is a
heading-pattern scan — content is not evaluated here; a heading is present or absent.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A missing heading indicates a Phase 2 forward gate was bypassed. Write the missing block
using the exact heading pattern shown, then re-check.

CONSTRAINT: the Auditor Phase cannot begin until every required heading pattern is confirmed
present and correctly ordered. Structural completeness is a precondition for reasoning
analysis — the Auditor role never encounters structurally incomplete criteria.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing
any Auditor output — the Audit Table requires cross-criterion visibility.

CONSTRAINT: do not write audit rows one at a time as each criterion is processed. Write the
full Audit Table after reading all Author criteria.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the count, field name, structural pattern, or enumeration from
  this skill's output contract. Required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence noting whether discriminating
elements are varied across types (count, field name, structural pattern, enumeration) or
cluster in one type. Confirm C-01's pass condition addresses the rank-1 failure mode — if
not, flag for ordering revision.

**REDUNDANCY CHECK TABLE**

PRECONDITION for advancing past this step: all essential criteria pairs evaluated.

For each pair of essential criteria, ask: Is there a rubric output that passes one criterion
but fails the other for a non-trivial reason?

- **YES** — independent: each criterion adds unique signal. Keep both.
- **NO** — redundant: passing one always means passing the other. Revise, consolidate, or
  remove the redundant criterion.

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

[Add rows for any additional essential criteria pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
GENERIC: [condition in its weakest surviving form — Status-Quo Rubric]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Inertia Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] Redundancy Gate cleared: all pairs show YES or NO-flagged pairs resolved

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order (C-01 = most critical).

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

## V-02 — Inertia Framing: Named Status-Quo Competitor

**axis:** inertia-framing
**hypothesis:** R5 V-05's inertia test asks "Could 'the output is clear and comprehensive'
pass this?" — the Status-Quo Rubric is implicit, unnamed, and appears only inside the
INERTIA-RECORD block. A builder writing a pass condition does not have the Status-Quo Rubric
in working memory until the inertia test is reached, by which point the condition is already
drafted and the test becomes a post-hoc check rather than a shaping constraint. V-02 names
the Status-Quo Rubric explicitly in the opening framing and carries the competitor reference
forward into the CALIBRATION-PAIR labels (GENERIC → STATUS-QUO). When the builder drafts a
pass condition knowing from the start that they are competing against a named rubric, the
competition framing shapes the condition as it is written — not after the fact. The
CALIBRATION-PAIR label STATUS-QUO (vs. GENERIC) reinforces this framing at every criterion:
the builder is not producing an abstract "generic" example, they are producing what the named
competitor would say. Failure condition: if C-11 and C-12 pass rates do not improve relative
to R5 V-05, either (a) the inertia test already provides sufficient discrimination pressure
regardless of when the framing is introduced, or (b) the STATUS-QUO label in the calibration
pair produces no additional sharpening beyond GENERIC.

---

You are building a scoring rubric for a Signal skill. Your rubric competes against the
Status-Quo Rubric — a rubric that says nothing specific about the target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

The Status-Quo Rubric passes any output that looks reasonable. A scoring rubric for a named
skill must be harder to fool: every pass condition must name a specific count, field,
structural pattern, or enumeration that only the target skill's output contract can supply.
A pass condition that the Status-Quo Rubric would also accept is too weak — it adds no
evaluative signal beyond what a generic quality bar already provides.

Five mechanisms enforce this standard: named section blocks that make structural omission
detectable by heading scan; a severity-ranking step that sequences essential criteria from
most to least critical failure mode; forward-blocking per-criterion gates that prevent
deferral; a category-coverage gate verifying the rubric spans at least 3 canonical category
dimensions; and an Auditor phase that produces a consolidated audit table and a pairwise
redundancy check.

**Why five mechanisms plus the Status-Quo Rubric framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional — not the first failure
listed. The category gate prevents all criteria clustering in one dimension. The consolidated
Auditor table enables cross-criterion analysis. The Status-Quo Rubric framing makes the
discrimination requirement visceral: every criterion you write must catch something the
Status-Quo Rubric misses. If it does not, it belongs in the Status-Quo Rubric, not yours.

---

### AUTHOR PHASE

Read the skill spec. Answer:

1. What does this skill produce? Name the artifact and its key fields.
2. What lifecycle phases does it have?
3. What failure would make the output non-functional as an objective function?

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

- [ ] At least 3 blocking failure modes listed in Author Phase 1
- [ ] At least 2 degrading failure modes listed in Author Phase 1
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02
targets rank-2, and so on. For each essential criterion, produce the three named blocks in
order, then record the criterion row. Blocks must use the exact heading patterns shown.

**Sub-step 2a — Draft the pass condition.**

Write the pass condition: specific, observable, verifiable by two independent evaluators.
As you write it, ask: does this condition catch something the Status-Quo Rubric would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would the Status-Quo Rubric ("the output is clear, complete, and
  well-formatted") accept this condition? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration from this
  skill's contract that the Status-Quo Rubric cannot replicate]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

Produce it now — immediately after sub-step 2b, while this pass condition is in working
memory. Do not produce all calibration pairs after all pass conditions are finalized: write
each pair at the moment the pass condition it calibrates is drafted.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — a condition it would accept; this is
  the competitor's best attempt at evaluating this behavior]
GROUNDED: [what your rubric says — a condition the Status-Quo Rubric would reject because
  it names the skill-specific element from INERTIA-RECORD; references the target skill by
  name or output-contract term]
```

**Sub-step 2d — Per-criterion forward gate.**

**DO NOT record this criterion in the table and DO NOT advance to the next criterion until:**

- [ ] `### INERTIA-RECORD [C-NN]` block is present above with Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` block is present above with STATUS-QUO and GROUNDED
      fields filled, written before this gate check and before this criterion's table row

This is a forward-blocking gate, not a repair check.

After both blocks are confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE — DO NOT proceed to Structural Verification until:**

Count distinct categories across ALL criteria (essential + recommended + aspirational).
Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count of distinct categories: ___ (minimum required: 3)

If fewer than 3 categories appear: add or revise criteria in Phase 3 before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

Scan the Author phase output for section headings matching the patterns below. Pattern
scan only — content is not evaluated here.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO and GROUNDED fields), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A missing heading indicates a Phase 2 forward gate was bypassed. Write the missing block
using the exact heading pattern shown, then re-check.

**The Auditor Phase cannot begin until every required heading pattern is confirmed present
and correctly ordered. Structural completeness is a prerequisite for reasoning analysis.**

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing
any audit output. Do not write audit rows one at a time.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the count, field name, structural pattern, or enumeration that
  the Status-Quo Rubric cannot replicate. Required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence noting whether discriminating
elements are varied across types or cluster in one type. Confirm C-01 addresses the rank-1
failure mode.

**REDUNDANCY CHECK TABLE**

For each pair of essential criteria, ask: Is there a rubric output that passes one but fails
the other for a non-trivial reason?

- **YES** — independent: keep both.
- **NO** — redundant: revise, consolidate, or remove.

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

[Add rows for additional pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form — what the competitor would say]
GROUNDED: [Auditor-verified form naming the discriminating element the Status-Quo Rubric
  cannot replicate]
```

**AUDITOR GATE: DO NOT proceed to Final Rubric until:**

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
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

## V-03 — Output Format: Annotated Denominator + Named Redundancy Heading

**axis:** output-format
**hypothesis:** R5 V-05 fails two v6 criteria by format omission, not mechanism omission:
(1) C-27 requires the redundancy check to appear as a named `###` section block so that its
absence is detectable by heading scan — R5 V-05 uses `**REDUNDANCY CHECK TABLE**` (bold
text, not a heading), so a builder who skips the redundancy check produces no missing heading
and the omission passes Structural Verification. Changing the label to
`### REDUNDANCY-CHECK-TABLE` closes this gap: the omission becomes a missing heading
detectable by the same scan that checks INERTIA-RECORD and CALIBRATION-PAIR blocks. (2) C-28
requires the scoring formula to annotate each denominator with its criterion ID range so that
a maintainer can verify denominator correctness without counting the criteria table —
R5 V-05's formula uses symbolic `N_aspirational`, which a maintainer cannot verify from the
formula alone. Requiring the builder to replace variable names with actual counts and annotate
with criterion ID ranges closes this gap. Both fixes are pure output-format changes with no
mechanism modifications. Failure condition: if C-27 or C-28 fail, either (a) the `###`
heading does not satisfy C-27's named-block requirement (its heading scan check), or (b) the
formula annotation instruction is not followed (builder still writes variable names despite
the constraint).

---

You are building a scoring rubric for a Signal skill. Five mechanisms enforce quality: a
severity-ranking step that sequences essential criteria from most to least critical failure
mode; named section blocks that make structural omission detectable by heading scan;
forward-blocking per-criterion gates that prevent deferral; a category-coverage gate
verifying the rubric spans at least 3 canonical category dimensions; and an Auditor phase
that produces a consolidated audit table and a pairwise redundancy check under a named
section heading. All outputs appear in the final document.

**Why five mechanisms plus named redundancy heading and annotated formula?**

Named blocks catch skipped checks by making omission a missing heading. Forward-blocking
gates prevent the skip. The category gate ensures multi-dimensional failure coverage.
Severity ranking ensures C-01 targets the highest-stakes failure mode. The Auditor's
consolidated table enables cross-criterion specificity analysis; the redundancy check (under
a named `###` heading) enables cross-criterion independence analysis — and a named heading
makes the check's omission detectable by the same heading scan that verifies INERTIA-RECORD
and CALIBRATION-PAIR blocks. The annotated formula denominator makes scoring correctness
self-verifiable: a maintainer reading only the formula can confirm the denominator without
counting criteria.

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

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank the blocking failure modes from most to least critical.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 will target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

**DO NOT advance to Author Phase 2 Entry Gate until the severity rank is written.**

**AUTHOR PHASE 2 ENTRY GATE — DO NOT begin writing criteria until:**

- [ ] At least 3 blocking failure modes listed in Author Phase 1
- [ ] At least 2 degrading failure modes listed in Author Phase 1
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1, C-02 targets rank-2,
and so on. For each essential criterion, produce the three named blocks in order, then record
the criterion row.

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

Produce it now — immediately after sub-step 2b, while this pass condition is in working
memory. Do not produce all calibration pairs after all pass conditions are finalized: write
each pair at the moment the pass condition it calibrates is drafted.

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

This is a forward-blocking gate, not a repair check.

After both blocks are confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE — DO NOT proceed to Structural Verification until:**

Count distinct categories across ALL criteria (essential + recommended + aspirational).
Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count of distinct categories: ___ (minimum required: 3)

If fewer than 3 categories appear: add or revise criteria in Phase 3 before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

Scan the Author phase output for section headings matching the patterns below. This is a
heading-pattern scan — content is not evaluated here.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

A missing heading indicates a Phase 2 forward gate was bypassed. Write the missing block
using the exact heading pattern shown, then re-check.

Also verify that `### REDUNDANCY-CHECK-TABLE` will appear in the Auditor Phase. If the
Auditor Phase has not yet run, this check is deferred to the Auditor Phase entry.

**The Auditor Phase cannot begin until every required heading pattern is confirmed present
and correctly ordered. Structural completeness is a prerequisite for reasoning analysis.**

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing
any audit output. Do not write audit rows one at a time.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence noting whether discriminating
elements are varied or cluster in one type. Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria, ask: Is there a rubric output that passes one criterion
but fails the other for a non-trivial reason?

- **YES** — independent: each adds unique signal. Keep both.
- **NO** — redundant: passing one always means passing the other. Revise, consolidate, or
  remove the redundant criterion.

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

[Add rows for additional pairs if more than 5 essential criteria.]

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
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table with Auditor-revised conditions substituted where
Revision Required = YES. Essential criteria in severity-rank order.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

Record the criterion ID range for each tier, then write the formula with annotations.

```
Tier counts:
  essential:   C-[first] through C-[last-essential]   — count = [N_e]
  recommended: C-[first-rec] through C-[last-rec]     — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace each [N_x] with the actual criterion count. Replace [first]/[last] with actual
criterion IDs. DO NOT use symbolic variable names (N_essential, N_aspirational) as
denominators — the criterion ID range annotation makes the denominator self-verifiable
without counting the criteria table.

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

## V-04 — Phrasing Register × Inertia Framing (V-01 × V-02, Combination)

**axis:** phrasing-register × inertia-framing
**hypothesis:** V-01 introduces formal declarative language (PRECONDITION, INVARIANT,
CONSTRAINT) targeting improved compliance with severity ordering (C-07) and anti-deferral
constraints (C-22, C-25). V-02 names the Status-Quo Rubric as a concrete adversarial
competitor and changes GENERIC → STATUS-QUO in calibration pairs, targeting improved
discrimination in pass conditions (C-11) and calibration pair quality (C-12). These axes
operate at different cognitive layers: phrasing register shapes how constraints feel
(mandatory vs. advisory), while inertia framing shapes what the pass condition competes
against. Neither axis modifies the structural mechanisms (same named blocks, same gates,
same redundancy check). Combined, they should improve both compliance and quality without
interaction: formal language does not reduce the Status-Quo Rubric framing's effectiveness,
and named-competitor framing does not weaken the formal constraint vocabulary. Failure
condition: if V-04 underperforms V-01 or V-02 on their respective targets, investigate
whether formal language makes the STATUS-QUO label feel inconsistent with the declarative
register (e.g., a builder using specification vocabulary might find STATUS-QUO too
colloquial and skip the calibration pair).

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through five mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria appear from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure that makes the output non-functional
- **M-02 — named-blocks:** every mandatory check output appears as a `### HEADING [C-NN]`
  section block; a missing block is a missing heading detectable by scan
- **M-03 — forward-blocking gates:** each per-criterion gate fires before the next
  criterion is written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories required across all
  criteria (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check required

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear unless all required preceding named blocks
  (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) are confirmed present above it
- INVARIANT B: the `### CALIBRATION-PAIR [C-NN]` block is written immediately after the
  `### INERTIA-RECORD [C-NN]` block — not after all INERTIA-RECORD blocks are complete

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking and 2 degrading failure modes must be listed.
DO NOT proceed to SEVERITY RANKING until this constraint is satisfied.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank blocking failure modes from most to least critical.

DEFINITION (most critical): the failure that makes the output non-functional as an objective
function regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete, every blocking failure
mode from Phase 1 ordered.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02
targets rank-2. For each criterion, apply sub-steps 2a–2d in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. As you write
it: does this condition catch something the Status-Quo Rubric would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would the Status-Quo Rubric ("the output is clear, complete, and
  well-formatted") accept this condition? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration from this
  skill's contract that the Status-Quo Rubric cannot replicate]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must be produced before CALIBRATION-PAIR for the same
criterion. Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

VIOLATION: batch-producing all `### CALIBRATION-PAIR` blocks after all INERTIA-RECORD blocks
satisfies structural ordering (CALIBRATION-PAIR precedes CRITERION) while violating INVARIANT
B. Do not defer. Batch production is a violation even if structural order is preserved.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — a condition it would accept for
  any artifact; the competitor's best attempt at this criterion]
GROUNDED: [what your rubric says — the condition the Status-Quo Rubric rejects because
  it names the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above with STATUS-QUO and GROUNDED fields,
      written before this gate check and before this criterion's table row (INVARIANT B
      confirmed satisfied)
- [ ] Severity-rank alignment field confirms rank-N assignment

CONSTRAINT 2d: forward-blocking gate. If any precondition is false, write the missing block
or correct the alignment before recording the criterion row. Violating INVARIANT A is not
recoverable by retroactive addition.

After all preconditions confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

PRECONDITION for Structural Verification: at least 3 distinct categories across all criteria.

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: if fewer than 3 categories are present, add or revise criteria in Phase 3.
A rubric clustering in one or two categories cannot detect multi-dimensional failures.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

Scan Author phase output for section headings matching the patterns below. Pattern scan
only — content not evaluated.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED fields), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block using the exact heading pattern, then re-check.

CONSTRAINT: the Auditor Phase cannot begin until every required heading pattern is confirmed
present and correctly ordered. Structural completeness is a precondition for reasoning
analysis.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element the Status-Quo Rubric cannot replicate. Required
  for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

**REDUNDANCY CHECK TABLE**

For each pair of essential criteria, ask: Is there a rubric output that passes one but fails
the other for a non-trivial reason?

- **YES** — independent: keep both.
- **NO** — redundant: revise, consolidate, or remove.

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

[Add rows for additional pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] Redundancy Gate cleared: all pairs show YES or NO-flagged pairs resolved

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order (C-01 = most critical).

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

## V-05 — Phrasing Register × Inertia Framing × Output Format (V-01 × V-02 × V-03, Three-Axis Combination)

**axis:** phrasing-register × inertia-framing × output-format
**hypothesis:** V-01 adds formal declarative language targeting C-07/C-22/C-25 compliance.
V-02 adds named Status-Quo Rubric competitor targeting C-11/C-12 quality. V-03 adds
`### REDUNDANCY-CHECK-TABLE` heading and annotated formula denominator targeting C-27/C-28.
V-04 (V-01 × V-02) tests whether the two quality axes combine additively. V-05 extends V-04
by adding V-03's structural format fixes. The three axes operate at non-competing layers:
phrasing register shapes constraint language; inertia framing shapes calibration pair labels
and inertia test question; output format shapes one heading and the formula instruction. No
axis tension: formal language does not conflict with named-competitor framing, and neither
conflicts with changing a bold label to a `###` heading. Combined, V-05 should score 100.0
under v6 rubric (all five essentials + all three recommended + all twenty aspirationals).
Failure condition (for any single criterion): if C-27 fails in V-05 while passing in V-03,
the named heading is incompatible with an aspect of the formal register or Status-Quo framing
— investigate whether the AUDITOR GATE checklist item for `### REDUNDANCY-CHECK-TABLE`
conflicts with any PRECONDITION language in the formal register.

---

You are executing a scoring-rubric construction protocol for a Signal skill. Your rubric
competes against the Status-Quo Rubric — a rubric that says nothing specific about the
target skill's contract.

**THE STATUS-QUO RUBRIC:** "The output is clear, complete, and well-formatted."

This protocol enforces quality through five mechanisms with formal invariants. Violating
any invariant invalidates the step it governs. Every pass condition must name a specific
count, field, structural pattern, or enumeration that only the target skill's output
contract can supply — a condition the Status-Quo Rubric would also accept is too weak.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria sequenced from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure making the output non-functional
- **M-02 — named-blocks:** every mandatory check output appears as a `### HEADING [C-NN]`
  section block; a missing block is a missing heading detectable by scan
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under a named `###` section heading

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear unless all required preceding named blocks
  (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) are confirmed present above it
- INVARIANT B: `### CALIBRATION-PAIR [C-NN]` is written immediately after
  `### INERTIA-RECORD [C-NN]` — not after all INERTIA-RECORD blocks are complete

---

### AUTHOR PHASE

Read the skill spec. Answer before writing any criterion:

1. What does this skill produce? Name the artifact and its required fields.
2. What lifecycle phases does the skill have?
3. What failure would make the output non-functional as an objective function?

**AUTHOR PHASE 1: FAILURE MODES**

```
F-01: [failure mode] | blocking
F-02: [failure mode] | blocking
F-03: [failure mode] | blocking
F-04: [failure mode] | degrading
F-05: [failure mode] | degrading
```

CONSTRAINT P1-1: at least 3 blocking and 2 degrading failure modes must be listed.
DO NOT proceed to SEVERITY RANKING until satisfied.

**AUTHOR PHASE 1 — SEVERITY RANKING**

Rank blocking failure modes from most to least critical.

DEFINITION (most critical): the failure that makes the output non-functional as an objective
function regardless of all other criteria passing.

```
SEVERITY RANK:
1. [most critical blocking failure mode — C-01 MUST target this]
2. [second most critical]
3. [third most critical]
[continue for all blocking failure modes]
```

PRECONDITION for Author Phase 2 Entry Gate: severity rank complete; every blocking failure
mode from Phase 1 ordered.

**AUTHOR PHASE 2 ENTRY GATE**

PRECONDITION for writing any criterion:

- [ ] At least 3 blocking failure modes listed
- [ ] At least 2 degrading failure modes listed
- [ ] Severity rank complete with all blocking failure modes ordered
- [ ] At least 3 distinct output-contract categories identifiable (list them: ___, ___, ___)

CONSTRAINT: DO NOT write any criterion until all four preconditions are confirmed.

**AUTHOR PHASE 2: DRAFT ESSENTIAL CRITERIA (3–5)**

Write essential criteria in severity-rank order: C-01 targets rank-1 (most critical), C-02
targets rank-2. For each criterion, apply sub-steps 2a–2d in sequence.

**Sub-step 2a — Draft the pass condition.**

CONSTRAINT 2a: specific, observable, verifiable by two independent evaluators. As you draft:
does this condition catch something the Status-Quo Rubric would miss?

**Sub-step 2b — Produce the INERTIA-RECORD block.**

```
### INERTIA-RECORD [C-NN]
Draft condition: [condition from 2a]
Status-Quo test: Would the Status-Quo Rubric ("the output is clear, complete, and
  well-formatted") accept this condition? [YES / NO]
If YES — revised condition: [revision; re-run until NO]
Final condition: [condition the Status-Quo Rubric would reject]
Skill-specific element: [the count, field name, pattern, or enumeration that the
  Status-Quo Rubric cannot replicate]
Severity-rank alignment: [confirm: this criterion targets rank-N failure mode — "[failure mode]"]
```

CONSTRAINT 2b: INERTIA-RECORD must precede CALIBRATION-PAIR for the same criterion.
Violates INVARIANT A otherwise.

**Sub-step 2c — Produce the CALIBRATION-PAIR block.**

INVARIANT B (restated at point of action): produce the CALIBRATION-PAIR block now —
immediately after completing sub-step 2b, while this pass condition is in working memory.

VIOLATION: batch-producing all `### CALIBRATION-PAIR` blocks after all INERTIA-RECORD blocks
are complete satisfies structural ordering while violating INVARIANT B. Do not defer.
Batch production is a protocol violation even if block order is preserved.

```
### CALIBRATION-PAIR [C-NN]
STATUS-QUO: [what the Status-Quo Rubric would say — the condition it would accept for
  any artifact; the competitor's best attempt at this criterion]
GROUNDED: [what your rubric says — the condition the Status-Quo Rubric rejects because
  it names the skill-specific element from INERTIA-RECORD]
```

**Sub-step 2d — Per-criterion forward gate.**

PRECONDITION for recording this criterion and advancing to the next:

- [ ] `### INERTIA-RECORD [C-NN]` present above with Status-Quo test = NO
- [ ] `### CALIBRATION-PAIR [C-NN]` present above with STATUS-QUO and GROUNDED fields,
      written before this gate check and before this criterion's table row (INVARIANT B
      confirmed satisfied)
- [ ] Severity-rank alignment field confirms rank-N assignment

CONSTRAINT 2d: forward-blocking gate. If any precondition is false, do not record the
criterion row. Write the missing block or correct the alignment, then re-check.

After all preconditions confirmed, record:

```
### CRITERION [C-NN]
| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-NN | **[bold label]** — [text] | [category] | essential | [final condition from INERTIA-RECORD] |
```

Repeat sub-steps 2a–2d for each essential criterion in severity-rank order.

**AUTHOR PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Write 2–3 recommended and 1–2 aspirational criteria. Five-field table format.

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**AUTHOR CATEGORY-COVERAGE GATE**

PRECONDITION for Structural Verification: at least 3 distinct categories across all criteria.

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count: ___ (minimum: 3)

CONSTRAINT: if fewer than 3 categories present, add or revise criteria in Phase 3 before
proceeding. A rubric clustering all criteria in one or two categories fails C-06.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

Scan the Author phase output for section headings matching the patterns below. Pattern
scan only — content not evaluated.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block using the exact heading pattern, then re-check.

CONSTRAINT: the Auditor Phase cannot begin until every required heading pattern is confirmed
present and correctly ordered. Structural completeness is a precondition for reasoning
analysis.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks. Read them all before writing any Auditor output.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block):**

| Criterion ID | Pass Condition (quoted) | Status-Quo Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|-----------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the element the Status-Quo Rubric cannot replicate. Required
  for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence on variety vs. clustering.
Confirm C-01 addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

For each pair of essential criteria, ask: Is there a rubric output that passes one criterion
but fails the other for a non-trivial reason?

- **YES** — independent: each adds unique signal. Keep both.
- **NO** — redundant: passing one always means passing the other. Revise, consolidate, or
  remove the redundant criterion.

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

[Add rows for additional pairs if more than 5 essential criteria.]

**REDUNDANCY GATE: DO NOT proceed to Auditor Calibration Pair until:**

- [ ] All pairs evaluated
- [ ] All pairs show YES, OR NO-flagged pairs resolved and re-evaluated as YES

**Auditor Calibration Pair** — for the most critical essential criterion:

```
STATUS-QUO: [condition in its Status-Quo Rubric form]
GROUNDED: [Auditor-verified form naming the discriminating element]
```

**AUDITOR GATE**

PRECONDITION for Final Rubric:

- [ ] Audit Table complete with all essential criteria as rows
- [ ] Every essential criterion shows Status-Quo Test = NO (original or revised)
- [ ] Discriminating Element filled for every NO-flagged row
- [ ] Cross-criterion pattern note written
- [ ] Severity-rank order confirmed: C-01 addresses the most critical failure mode
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared

CONSTRAINT: DO NOT produce the Final Rubric until all preconditions are satisfied.

### END AUDITOR PHASE

---

**FINAL RUBRIC: APPLY AUDITOR REVISIONS**

Reproduce the complete criteria table. Substitute Auditor-revised conditions where
Revision Required = YES. Essential criteria in severity-rank order (C-01 = most critical).

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|

**SCORING FORMULA AND GOLDEN THRESHOLD**

Record the criterion ID range for each tier, then write the formula with annotations.

```
Tier counts:
  essential:    C-[first] through C-[last-essential]  — count = [N_e]
  recommended:  C-[first-rec] through C-[last-rec]    — count = [N_r]
  aspirational: C-[first-asp] through C-[last-asp]    — count = [N_a]

composite = (essential_pass / [N_e] * 60)     /* C-[first] through C-[last-essential] */
          + (recommended_pass / [N_r] * 30)   /* C-[first-rec] through C-[last-rec] */
          + (aspirational_pass / [N_a] * 10)  /* C-[first-asp] through C-[last-asp] */
```

Replace each [N_x] with the actual criterion count. Replace [first]/[last] with actual
criterion IDs. DO NOT use symbolic variable names as denominators — the criterion ID range
annotation makes the denominator self-verifiable without counting the criteria table.

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

**Anchor: V-05**

V-05 is designated the combination anchor for Round 6.

**Structural impact:** V-05 carries all three axes simultaneously. V-03's output-format
changes (C-27 heading, C-28 annotation) move the score from 99.0 to 100.0 under v6 rubric.
V-01's formal language and V-02's named-competitor framing do not add new criteria passes
under v6 (no new criteria target these axes directly), but they address the two categories
of quality failure that remain in generated rubrics: severity ordering that follows the
template mechanically rather than by judgment (C-07 compliance variance), and pass conditions
that are technically skill-specific but not viscerally competitive (C-11 and C-12 depth).

**Isolation quality:** V-01 isolates phrasing register; V-02 isolates inertia framing;
V-03 isolates output format. V-04 tests V-01 × V-02. V-05 extends V-04 with V-03. If V-05
fails a criterion that V-03 alone passes, the phrasing or framing axes interact with the
output-format fix — the most likely candidate is if the AUDITOR GATE's PRECONDITION language
(formal) is inconsistent with the `### REDUNDANCY-CHECK-TABLE` heading check item.

**Detectable failure conditions:**
- C-27 fails in V-05 but passes in V-03: the formal PRECONDITION language in AUDITOR GATE
  conflicts with the `### REDUNDANCY-CHECK-TABLE` heading check — investigate whether
  rewriting the gate item as "PRECONDITION: `### REDUNDANCY-CHECK-TABLE` heading present"
  resolves the inconsistency
- C-11 fails in V-02 but passes in V-01: the STATUS-QUO framing reduces pass-condition
  specificity — investigate whether naming a concrete competitor leads builders to write
  against the competitor's framing rather than against the skill contract

**Combination priority for Round 7:**

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-05 (this round) | all three | C-27, C-28 + quality | 1 | Maximum score under v6; test quality axes for R7 excellence signal candidates |
| V-03 × lifecycle-emphasis | output-format × phase-structure | C-27, C-28 | 2 | If V-03 passes C-27/C-28 cleanly without phrasing change, confirm output-format alone is sufficient before combining with other axes |
| V-02 × output-format | inertia-framing × denominator annotation | C-11, C-12, C-28 | 3 | If V-02 improves C-11 quality, test whether annotated denominator (which requires naming criterion ID ranges) reinforces the skill-specific anchoring already sharpened by Status-Quo framing |

---

## Combination Roadmap (for Round 7)

**R6 outcome scenarios:**

| Scenario | Expected Outcome | Round 7 Action |
|----------|----------------|----------------|
| V-03 reaches 100.0, V-05 also reaches 100.0 | C-27 and C-28 both fixed by output-format axis; phrasing/framing axes add no new v6 criteria passes | Extract excellence signals from V-02/V-04/V-05 if generated rubric quality improves (C-11, C-12 pass rates); absorb into v7 as new aspirationals if patterns emerge |
| V-03 reaches 100.0, V-05 fails C-27 | Formal phrasing interacts with named-heading check | Investigate AUDITOR GATE phrasing; fix in V-05 and re-run |
| V-02 improves C-11 pass rate | STATUS-QUO label sharpens pass conditions | Add named-competitor framing as permanent baseline in v7 prompt body |
| V-01 improves C-07 pass rate | PRECONDITION language improves severity-rank compliance | Add formal gate vocabulary for severity alignment check in v7 |
| Neither V-01 nor V-02 improves their respective criteria | Conversational register already sufficient; competitor framing already implicit | Retire both axes; focus Round 7 on remaining aspirational gap investigation (which aspirationals still fail in practice?) |
