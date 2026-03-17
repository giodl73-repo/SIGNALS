# quest-rubric Variate — Round 7 against rubric v7

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v7 (C-01 through C-30; essential C-01–C-05)
**Round:** R7 — 3 single-axis + 2 combination

**Round 7 design note:** Round 6 produced two excellence signals absorbed into v7 as
aspirational criteria: C-29 (mechanism overview declares structural output format requirement
alongside behavioral requirement, ES-R6-1) and C-30 (structural verification explicitly
declares its phase-bounded coverage scope and names the deferral destination for out-of-scope
heading checks, ES-R6-2).

R6 V-05 is the anchor. Under the v7 rubric:

**R6 V-05 score under v7:**
- Essential (5/5): all pass → 60
- Recommended (3/3): all pass → 30
- Aspirational (20/22):
  - C-09–C-28: all pass (R6 V-05 satisfies each by construction)
  - C-29: FAIL — the MECHANISMS preamble uses a generic placeholder (`### HEADING [C-NN]`)
    for M-02 and says "named `###` section heading" for M-05 without naming the actual heading
    patterns (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`, `### CRITERION [C-NN]`,
    `### REDUNDANCY-CHECK-TABLE`). A builder reading only the overview cannot construct the
    output heading skeleton before entering the Author Phase.
  - C-30: FAIL — the Structural Verification step lists the Author Phase heading patterns
    it checks but does not (a) declare it covers Author Phase output only, (b) name
    `### REDUNDANCY-CHECK-TABLE` as out-of-scope because it belongs to the Auditor Phase,
    or (c) state that the deferred check is performed at AUDITOR GATE entry.
  → 20/22 × 10 = 9.09

**Composite: 99.09 → Golden.**

Both gaps are structural-declaration fixes: they require the existing information
(which headings exist, which step they belong to) to be relocated — into the mechanism
overview for C-29, and into the Structural Verification scope statement for C-30. Neither
gap requires a new mechanism.

**Round 7 axis selection:**

| Axis | What changes | Criteria targeted |
|------|-------------|-------------------|
| mechanism-overview-format | MECHANISMS preamble M-02 and M-05 name actual heading patterns instead of placeholders | C-29 |
| structural-verification-scope | STRUCTURAL VERIFICATION adds explicit scope statement: phase covered, out-of-scope heading patterns named, deferral destination stated | C-30 |
| pre-build-skeleton | New "output skeleton" step between AUTHOR PHASE entry and Phase 1: builder produces the full heading skeleton before writing any content, front-loading structural awareness | C-29 and C-30 (from a different angle) |

No interaction risk: mechanism-overview-format changes only the preamble description text;
structural-verification-scope changes only the Structural Verification section header/preamble;
pre-build-skeleton adds a new step before Phase 1 that does not modify Phase 2 sub-steps or
Auditor Phase content. None of the three modifies another's mechanism.

---

## Round 7 Variation Map

| Variation | Axis | Pass Type | What Changes | Criteria Targeted |
|-----------|------|-----------|--------------|-------------------|
| V-01 | mechanism-overview-format | single-axis | M-02 and M-05 in MECHANISMS name actual `###` heading patterns | C-29 |
| V-02 | structural-verification-scope | single-axis | Structural Verification declares phase scope, names out-of-scope headings, names deferral destination | C-30 |
| V-03 | pre-build-skeleton | single-axis | Builder produces full heading skeleton before Author Phase 1; skeleton references all patterns from the overview | C-29 and C-30 (structural awareness front-loaded) |
| V-04 | mechanism-overview-format × structural-verification-scope | combination (V-01 × V-02) | Both fixes: named heading patterns in overview + scoped Structural Verification | C-29 and C-30 |
| V-05 | mechanism-overview-format × structural-verification-scope × phrasing-register × inertia-framing × output-format | combination (V-01 × V-02 × R6 V-01 × R6 V-02 × R6 V-03) | Full accumulation: all R6 V-05 axes + R7 C-29 and C-30 fixes | C-29, C-30, and all R6 axes |

**Anchor designation (preliminary):** V-05. See anchor section at end.

**Score projections under v7 rubric:**

| Variation | C-29 | C-30 | Asp/22 | Composite | Band |
|-----------|------|------|--------|-----------|------|
| R6 V-05 (base) | FAIL | FAIL | 20/22 | 99.09 | Golden |
| V-01 | PASS | FAIL | 21/22 | 99.55 | Golden |
| V-02 | FAIL | PASS | 21/22 | 99.55 | Golden |
| V-03 | PASS (likely) | PASS (partial) | 21–22/22 | 99.55–100.0 | Golden |
| V-04 | PASS | PASS | 22/22 | 100.0 | Golden |
| V-05 | PASS | PASS | 22/22 | 100.0 | Golden |

All variations are Golden. V-04 and V-05 achieve maximum composite under v7.

---

## V-01 — Mechanism Overview Format: Named Heading Patterns

**axis:** mechanism-overview-format
**hypothesis:** R6 V-05's MECHANISMS preamble describes M-02 using the placeholder
`### HEADING [C-NN]` and describes M-05 as requiring "a named `###` section heading"
without naming the specific pattern. A builder reading only the preamble knows that named
headings are required but cannot construct the output heading skeleton — they don't know
which headings to produce (INERTIA-RECORD? CRITERION-RECORD? CHECK-RECORD?) until they
reach the operative sub-step instructions. V-01 replaces placeholders with actual heading
patterns in the overview: M-02 names `### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`,
`### CRITERION [C-NN]`; M-05 names `### REDUNDANCY-CHECK-TABLE`. The structural contract
is visible at orientation time, not only at execution time. Failure condition: if C-29 fails
despite named patterns in the overview, either (a) the pass condition requires something
more than naming patterns (e.g., a reasoning statement about why each pattern exists), or
(b) the heading names as listed are not sufficient for a builder to construct a pre-execution
skeleton without also reading the phase instructions.

---

You are executing a scoring-rubric construction protocol for a Signal skill. This protocol
enforces quality through five mechanisms with formal invariants. Violating any invariant
invalidates the step it governs.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria appear in order from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure that makes the output non-functional
  regardless of other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content
- **M-03 — forward-blocking gates:** each per-criterion gate fires before the next criterion
  is written; gates prevent omission; retroactive repair is not a substitute for a gate
- **M-04 — category-coverage:** at least 3 of 5 canonical categories must appear across all
  criteria (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria are read before Auditor output is produced; a
  consolidated table and pairwise redundancy check are required under `### REDUNDANCY-CHECK-TABLE`;
  a missing heading detects the omitted check by scan

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

### REDUNDANCY-CHECK-TABLE

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

## V-02 — Structural Verification Scope: Phase-Bounded Coverage Declaration

**axis:** structural-verification-scope
**hypothesis:** R6 V-05's Structural Verification step lists the Author Phase heading
patterns it checks but is silent about what it does NOT cover. A builder completing
the scan without knowing its scope might treat a clean scan as confirming all structural
requirements — including `### REDUNDANCY-CHECK-TABLE`, which belongs to the Auditor Phase
and has not yet been produced. V-02 adds three explicit scope statements to the Structural
Verification preamble: (1) the step covers Author Phase output only; (2) `### REDUNDANCY-CHECK-TABLE`
is an out-of-scope Auditor Phase heading not yet produced at this stage; (3) the deferred check
is performed at AUDITOR GATE entry. These three statements make the scan's coverage boundary
self-documenting: a builder reading only the Structural Verification step knows exactly what
is in scope, what is deferred, and where the deferred check will occur. Failure condition:
if C-30 fails despite explicit scope statements, either (a) the pass condition requires the
scope statement to appear in a more prominent position (e.g., at the top of the step, not
embedded in preamble prose), or (b) "at least one required heading pattern named as out-of-scope"
is not satisfied because `### REDUNDANCY-CHECK-TABLE` is not explicitly named by heading
pattern but only described behaviorally.

---

You are executing a scoring-rubric construction protocol for a Signal skill. This protocol
enforces quality through five mechanisms with formal invariants. Violating any invariant
invalidates the step it governs.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria appear in order from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure that makes the output non-functional
  regardless of other criteria passing
- **M-02 — named-blocks:** every mandatory check output appears as a `### HEADING [C-NN]`
  section block; a missing block is a missing heading detectable by scan without reading
  content
- **M-03 — forward-blocking gates:** each per-criterion gate fires before the next criterion
  is written; gates prevent omission; retroactive repair is not a substitute for a gate
- **M-04 — category-coverage:** at least 3 of 5 canonical categories must appear across all
  criteria (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria are read before Auditor output is produced; a
  consolidated table and pairwise redundancy check are required under a named `###` section
  heading

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
function regardless of all other criteria passing.

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

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced at this point in the workflow.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry (verified as part of the Auditor Gate checklist).

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

CONSTRAINT: the Auditor Phase cannot begin until every required Author Phase heading pattern
is confirmed present and correctly ordered. Structural completeness is a precondition for
reasoning analysis — the Auditor role never encounters structurally incomplete criteria.

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

### REDUNDANCY-CHECK-TABLE

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
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared
      (this is the deferred check from Structural Verification — `### REDUNDANCY-CHECK-TABLE`
      is an Auditor Phase heading verified here, not in the Author Phase scan)

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
criterion IDs. DO NOT use symbolic variable names as denominators.

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

## V-03 — Pre-Build Skeleton: Structural Awareness Front-Loaded

**axis:** pre-build-skeleton
**hypothesis:** C-29 and C-30 both address when a builder learns the structural contract.
V-01 surfaces it in the mechanism overview. V-02 scopes it at Structural Verification. V-03
tries a different approach: a "pre-build" step immediately after the orientation section
and before Author Phase 1 that asks the builder to produce the complete heading skeleton
for their output document before writing any content. The skeleton is produced from the
mechanism overview alone (the builder has read only the MECHANISMS section at this point).
The pre-build step forces the builder to demonstrate that the mechanism overview is sufficient
to construct the structural skeleton — a builder who cannot produce the skeleton from the
overview reveals that the overview is incomplete. This is both a quality mechanism and a
diagnostic: if the builder produces an incomplete skeleton despite a correct overview, the
gap is cognitive rather than informational. Failure condition: if C-29 fails despite a
pre-build step, the pass condition for C-29 requires that the overview itself declare the
formats — the pre-build step is an execution artifact that does not satisfy the requirement
for the overview text to declare them. If C-30 fails, the pre-build skeleton does not substitute
for the explicit scope declaration in the Structural Verification step itself. This variation
also tests whether a front-loaded skeleton step produces a new excellence signal (R8 candidate).

---

You are executing a scoring-rubric construction protocol for a Signal skill. This protocol
enforces quality through five mechanisms with formal invariants. Violating any invariant
invalidates the step it governs.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria appear in order from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure that makes the output non-functional
  regardless of other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content
- **M-03 — forward-blocking gates:** each per-criterion gate fires before the next criterion
  is written; gates prevent omission; retroactive repair is not a substitute for a gate
- **M-04 — category-coverage:** at least 3 of 5 canonical categories must appear across all
  criteria (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria are read before Auditor output is produced; a
  consolidated table and pairwise redundancy check are required under `### REDUNDANCY-CHECK-TABLE`;
  a missing heading detects the omitted check by scan

**INVARIANTS (hold throughout this protocol):**

- INVARIANT A: a criterion row may not appear in the output unless all required preceding
  named blocks (`### INERTIA-RECORD [C-NN]`, `### CALIBRATION-PAIR [C-NN]`) for that
  criterion are confirmed present above it
- INVARIANT B: the `### CALIBRATION-PAIR [C-NN]` block for criterion C-NN is written
  immediately after the `### INERTIA-RECORD [C-NN]` block for C-NN — not after all
  INERTIA-RECORD blocks are complete

---

### OUTPUT SKELETON (produce before any phase begins)

Before entering the Author Phase, produce the structural heading skeleton for your output.
Use only the MECHANISMS section above — do not read ahead into the phase instructions.

The skeleton lists the section headings your output will contain, in order, using the exact
heading patterns named in the MECHANISMS. Placeholders are permitted for per-criterion
headings where N is not yet known (e.g., `### INERTIA-RECORD [C-01]` through
`### INERTIA-RECORD [C-0N]`).

Produce the skeleton now:

```
### AUTHOR PHASE
### INERTIA-RECORD [C-01]
### CALIBRATION-PAIR [C-01]
### CRITERION [C-01]
[... repeat for each essential criterion ...]
### STRUCTURAL VERIFICATION
### AUDITOR PHASE
### REDUNDANCY-CHECK-TABLE
### END AUDITOR PHASE
[Final Rubric section]
```

This skeleton is a structural contract. Every named block must appear in the output or be
explicitly deferred (with the deferral location named). A block absent from both the skeleton
and the output is a structural omission.

PRECONDITION for Author Phase entry: skeleton is complete.

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
function regardless of all other criteria passing.

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
the criterion row. Write the missing block or correct the alignment, then re-check.

After all preconditions are confirmed, record:

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

PRECONDITION for Structural Verification: at least 3 distinct categories appear across all
criteria (essential + recommended + aspirational).

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count of distinct categories: ___ (minimum required: 3)

CONSTRAINT: if fewer than 3 categories are present, add or revise criteria in Phase 3
before proceeding.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan covers heading patterns from the Author Phase. It does not cover Auditor Phase
output, which has not yet been produced at this stage.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry.

Scan the Author phase output for section headings matching the patterns below. This is a
heading-pattern scan — content is not evaluated here; a heading is present or absent.

For each essential criterion C-NN produced in Author Phase 2:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present, precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Also verify the OUTPUT SKELETON produced before the Author Phase: confirm each heading in
the skeleton has a corresponding block in the output. Flag skeleton entries without blocks
for repair.

A missing heading indicates a Phase 2 forward gate was bypassed or a skeleton entry was
not fulfilled. Write the missing block using the exact heading pattern shown, then re-check.

CONSTRAINT: the Auditor Phase cannot begin until every required Author Phase heading pattern
is confirmed present and correctly ordered.

---

### AUDITOR PHASE

Read all `### CRITERION [C-NN]` blocks from the Author phase. Read them all before writing
any Auditor output — the Audit Table requires cross-criterion visibility.

CONSTRAINT: do not write audit rows one at a time. Write the full Audit Table after reading
all Author criteria.

**Audit Table (single contiguous block — write after reading all Author criteria):**

| Criterion ID | Pass Condition (quoted) | Inertia Test | Discriminating Element | Revision Required? | Revised Condition |
|-------------|------------------------|--------------|----------------------|--------------------|-------------------|

**Column definitions:**
- *Discriminating Element*: the count, field name, structural pattern, or enumeration from
  this skill's output contract. Required for every NO result. Blank for YES rows.
- *Revised Condition*: required for every YES row; blank otherwise.

**Cross-criterion pattern note (write after completing the full table):**

Scan the Discriminating Element column. Write one sentence noting whether discriminating
elements are varied across types or cluster in one type. Confirm C-01's pass condition
addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

PRECONDITION for advancing past this step: all essential criteria pairs evaluated.

For each pair of essential criteria, ask: Is there a rubric output that passes one criterion
but fails the other for a non-trivial reason?

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
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared
      (deferred from Structural Verification — verified here as part of Auditor Phase)

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
criterion IDs. DO NOT use symbolic variable names as denominators.

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

## V-04 — Mechanism Overview Format × Structural Verification Scope (V-01 × V-02, Combination)

**axis:** mechanism-overview-format × structural-verification-scope
**hypothesis:** V-01 names the actual heading patterns in the MECHANISMS overview, targeting
C-29. V-02 adds explicit scope declaration to Structural Verification, targeting C-30.
These axes operate at different positions in the workflow: V-01 changes the orientation
section (read once before all phases), V-02 changes a verification step (executed between
Author and Auditor phases). Neither axis modifies the Author Phase sub-steps or the Auditor
Phase content. Combined, they should close both C-29 and C-30 simultaneously, reaching
22/22 aspirational under v7 and a composite of 100.0. No interaction risk: naming heading
patterns in the overview does not affect the Structural Verification scope declaration,
and the scope declaration does not affect what the overview names. Failure condition:
if either C-29 or C-30 fails in V-04 but passes in its single-axis variation, there is an
interaction between the two changes — the most likely candidate is if the Structural
Verification scope statement referring to `### REDUNDANCY-CHECK-TABLE` by name is inconsistent
with how M-05 names it in the overview, creating ambiguity about the canonical heading pattern.

---

You are executing a scoring-rubric construction protocol for a Signal skill. This protocol
enforces quality through five mechanisms with formal invariants. Violating any invariant
invalidates the step it governs.

**MECHANISMS:**

- **M-01 — severity-ranking:** essential criteria appear in order from highest-stakes to
  lowest-stakes failure mode; C-01 targets the failure that makes the output non-functional
  regardless of other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content
- **M-03 — forward-blocking gates:** each per-criterion gate fires before the next criterion
  is written; gates prevent omission; retroactive repair is not a substitute for a gate
- **M-04 — category-coverage:** at least 3 of 5 canonical categories must appear across all
  criteria (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria are read before Auditor output is produced; a
  consolidated table and pairwise redundancy check are required under `### REDUNDANCY-CHECK-TABLE`;
  a missing heading detects the omitted check by scan

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
function regardless of all other criteria passing.

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
the criterion row. Write the missing block or correct the alignment, then re-check.

After all preconditions are confirmed, record:

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

PRECONDITION for Structural Verification: at least 3 distinct categories appear across all
criteria (essential + recommended + aspirational).

Canonical categories: `correctness` / `depth` / `format` / `coverage` / `behavior`

- [ ] Categories present (list each): ___________________________
- [ ] Count of distinct categories: ___ (minimum required: 3)

CONSTRAINT: if fewer than 3 categories are present, add or revise criteria in Phase 3
before proceeding. A rubric clustering all criteria in one or two categories fails C-06.

### END AUTHOR PHASE

---

### STRUCTURAL VERIFICATION (runs before Auditor Phase)

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced at this point in the workflow.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry (verified as part of the Auditor Gate checklist).

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

CONSTRAINT: the Auditor Phase cannot begin until every required Author Phase heading pattern
is confirmed present and correctly ordered. Structural completeness is a precondition for
reasoning analysis — the Auditor role never encounters structurally incomplete criteria.

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
elements are varied across types or cluster in one type. Confirm C-01's pass condition
addresses the rank-1 failure mode.

### REDUNDANCY-CHECK-TABLE

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
- [ ] `### REDUNDANCY-CHECK-TABLE` heading present and Redundancy Gate cleared
      (deferred from Structural Verification: this is the Auditor Phase heading verified here)

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
criterion IDs. DO NOT use symbolic variable names as denominators.

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

## V-05 — Full Accumulation: R6 V-05 × R7 C-29/C-30 Fixes (Five-Axis Combination)

**axis:** mechanism-overview-format × structural-verification-scope × phrasing-register × inertia-framing × output-format
**hypothesis:** V-05 carries all five axes simultaneously. The three R6 axes (phrasing-register
formal language, named Status-Quo Rubric competitor, annotated formula denominator + named
`### REDUNDANCY-CHECK-TABLE`) produce a 100.0 composite under v6. The two R7 axes close
C-29 and C-30, producing a 100.0 composite under v7. All five axes operate at non-competing
layers: mechanism-overview-format changes the MECHANISMS preamble description text;
structural-verification-scope changes the Structural Verification preamble; phrasing-register
changes constraint vocabulary throughout; inertia-framing changes calibration-pair labels
and inertia test question phrasing; output-format changes the redundancy heading and formula
annotation instruction. Combined, V-05 should score 100.0 under v7 rubric (5/5 essential +
3/3 recommended + 22/22 aspirational). Failure condition for any single criterion: if C-29
fails in V-05 while passing in V-01 or V-04, the phrasing-register or inertia-framing changes
interact with the heading-pattern naming in the overview — investigate whether CONSTRAINT
labels (formal register) or STATUS-QUO framing alter how M-02 or M-05 are read. If C-30
fails in V-05 while passing in V-02 or V-04, investigate whether the scope declaration's
reference to `### REDUNDANCY-CHECK-TABLE` conflicts with its PRECONDITION phrasing in the
AUDITOR GATE checklist item.

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
  regardless of all other criteria passing
- **M-02 — named-blocks:** per-criterion check outputs appear as `### INERTIA-RECORD [C-NN]`,
  `### CALIBRATION-PAIR [C-NN]`, and `### CRITERION [C-NN]` section blocks in sequence;
  a missing block produces a missing section heading detectable by scan without reading
  content; the Status-Quo Rubric produces no named blocks — omission is invisible to it
- **M-03 — forward-blocking gates:** per-criterion gates fire before the next criterion is
  written; gates prevent omission; retroactive repair is not a substitute
- **M-04 — category-coverage:** at least 3 of 5 canonical categories across all criteria
  (correctness / depth / format / coverage / behavior)
- **M-05 — Auditor review:** all criteria read before Auditor output produced; consolidated
  table and pairwise redundancy check under `### REDUNDANCY-CHECK-TABLE`; a missing heading
  detects the omitted check by scan

**Why five mechanisms plus the Status-Quo Rubric framing?**

Named blocks catch skipped checks. Forward-blocking gates prevent skips. Severity ranking
ensures C-01 targets the failure that makes the output non-functional — not the first failure
listed. The category gate prevents all criteria clustering in one dimension. The Auditor
table enables cross-criterion analysis under `### REDUNDANCY-CHECK-TABLE`. The Status-Quo
Rubric framing makes the discrimination requirement concrete: every criterion you write must
catch something the Status-Quo Rubric misses. If it does not, it belongs in the Status-Quo
Rubric, not yours.

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

**Coverage scope: Author Phase output only.**

This scan verifies heading patterns produced during the Author Phase. It does not cover
Auditor Phase output, which has not yet been produced at this point in the workflow.

**Out of scope at this step:**
- `### REDUNDANCY-CHECK-TABLE` — Auditor Phase heading, not yet produced.
  Deferred to: AUDITOR GATE entry (verified as part of the Auditor Gate checklist).

Scan the Author phase output for section headings matching the patterns below. Pattern
scan only — content not evaluated.

For each essential criterion C-NN:

```
- [ ] ### INERTIA-RECORD [C-NN]   present, precedes ### CALIBRATION-PAIR [C-NN]
- [ ] ### CALIBRATION-PAIR [C-NN] present (STATUS-QUO, GROUNDED), precedes ### CRITERION [C-NN]
- [ ] ### CRITERION [C-NN]        present
```

Write any missing block using the exact heading pattern, then re-check.

CONSTRAINT: the Auditor Phase cannot begin until every required Author Phase heading pattern
is confirmed present and correctly ordered. Structural completeness is a precondition for
reasoning analysis.

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
      (deferred from Structural Verification: this is the Auditor Phase heading, verified here)

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

## Anchor Designation

**Anchor: V-05**

V-05 is designated the combination anchor for Round 7.

**Structural impact:** V-05 carries all five axes. The two R7 additions (mechanism-overview-format
for C-29, structural-verification-scope for C-30) move the aspirational denominator coverage
from 20/22 to 22/22 under v7, from 99.09 to 100.0. The three R6 axes (phrasing-register,
inertia-framing, output-format) are preserved from R6 V-05 and continue to satisfy C-07,
C-11, C-12, C-22, C-25, C-27, and C-28.

**Isolation quality:**
- V-01 isolates mechanism-overview-format (C-29 only)
- V-02 isolates structural-verification-scope (C-30 only)
- V-03 isolates pre-build-skeleton (C-29 and C-30 from front-loaded angle; exploratory)
- V-04 tests V-01 × V-02 (C-29 + C-30 together, no R6 axes)
- V-05 extends V-04 with all three R6 axes (full accumulation)

**Detectable failure conditions:**
- C-29 fails in V-05 but passes in V-01: formal CONSTRAINT/INVARIANT phrasing in V-05's
  MECHANISMS section conflicts with how the heading patterns are read — investigate whether
  "CONSTRAINT" labels before M-02 and M-05 entries create parsing ambiguity about which
  mechanism requires the named heading
- C-30 fails in V-05 but passes in V-02: the scope declaration's PRECONDITION language
  is inconsistent with V-05's formal register — investigate whether the deferred check item
  in AUDITOR GATE reads as a PRECONDITION or a CONSTRAINT and whether that ambiguity
  is present in V-02 but absent in V-05 due to register change
- C-29 fails in V-03 despite pre-build skeleton: C-29's pass condition requires the
  mechanism overview text to name the heading patterns — a pre-build execution step does
  not substitute for the overview text declaration; this is the expected failure mode of V-03
  on C-29 if C-29's pass condition is interpreted strictly

**Combination priority for Round 8:**

| Combination | Axes | Criteria Targeted | Priority | Rationale |
|-------------|------|-------------------|----------|-----------|
| V-05 (this round) | all five | C-29, C-30 + R6 axes | 1 | Maximum score under v7; test for new excellence signals |
| V-03 pre-build-skeleton | exploratory | C-29/C-30 from different angle | 2 | If V-03 produces an excellence signal (builder skeleton completeness check), candidate for v8 as new criterion |
| V-04 × R6 V-02 | V-04 + inertia-framing | C-29, C-30, C-11, C-12 | 3 | If V-03 surfaces no signal, confirm whether inertia-framing interacts with C-29/C-30 in isolation from phrasing-register |

---

## Combination Roadmap (for Round 8)

**R7 outcome scenarios:**

| Scenario | Expected Outcome | Round 8 Action |
|----------|----------------|----------------|
| V-04 reaches 100.0, V-05 also reaches 100.0 | C-29 and C-30 both closed by their respective axes; R6 axes add no interference | Extract excellence signals from V-03 if pre-build skeleton improves output quality; absorb into v8 as new aspirational if pattern emerges |
| V-04 reaches 100.0, V-05 fails C-29 or C-30 | One of the R6 axes interacts with the R7 fixes | Isolate: test V-01 × R6 axis and V-02 × R6 axis separately to identify which R6 axis causes the interaction |
| V-01 passes C-29, V-02 passes C-30, V-04 fails one | The two fixes interact with each other | Investigate naming consistency: does `### REDUNDANCY-CHECK-TABLE` in the scope declaration match the heading name in M-05 of V-01's overview? |
| V-03 passes both C-29 and C-30 | Pre-build skeleton satisfies both criteria — either the pass conditions are less strict than assumed, or the skeleton output counts as the mechanism overview for C-29 and the scope declaration for C-30 | Re-read C-29 and C-30 pass conditions against V-03 output; if the skeleton satisfies them, reconsider whether the pass conditions require textual declaration or execution evidence |
| None of V-01/V-02/V-03 improves C-29 or C-30 | The changes are insufficient for the pass conditions as written | Re-read the exact pass condition text for C-29 and C-30 and diagnose precisely what element is still missing |
