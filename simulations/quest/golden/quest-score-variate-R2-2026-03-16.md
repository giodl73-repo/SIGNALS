# quest-score Variations -- Round 2 (v2-2026-03-16 rubric)
**Skill**: quest-score
**Rubric**: v2-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-12 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=4**
**Date**: 2026-03-16
**Round**: 2

---

## Context: what informed this round

Round 2 targets the v2 rubric dated 2026-03-16. Round 1 against this rubric version
(R1-2026-03-16 scorecard) established that phase gates enforce synthesis presence and that
numbered blocks with explicit subelement checks enforce C-01/C-04 compliance. The champion
prompt from R1 carried forward those mechanisms. Two new Aspirational criteria in v2 were
extracted from R1 excellence signals:

| Change | R1 (v1) | R2 (v2) | Design consequence |
|--------|---------|---------|-------------------|
| C-11 (evidence positive anchor) | Not in rubric | **New Aspirational** -- at least one worked positive evidence cell must appear in the scored body | R1's anti-anchor (WEAK SCORER block) is confined to instructions; C-11 PASS requires a positive model within the scored body itself |
| C-12 (discrepancy declaration) | Not in rubric | **New Aspirational** -- labeled YES/NO declaration field in arithmetic verification | R1 V-01 produced this as an excellence signal via Step 4; other R1 variations omitted the labeled field, producing PARTIAL or FAIL on this criterion |
| N_aspirational denominator | 2 (C-09, C-10) | **4 (C-09, C-10, C-11, C-12)** | Scorers carrying over the R1 formula compute (aspirational_pass/2 * 10) -- double the correct weight -- silently inflating aspirational contribution by up to 5 points |

**v2 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=4 (C-09..C-12)

**Formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
```

**Golden threshold**: all 5 essentials PASS AND composite >= 80
**N/A condition**: C-09 PARTIAL (not FAIL) when scorer writes the prescribed no-prior-data statement

**Score landmarks:**
- All essential + all recommended + all aspirational: 100
- All essential + all recommended + no aspirational: 90
- All essential + no recommended + no aspirational: 60

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| D | Inertia framing -- positive body anchor | C-11 requires a positive evidence model *within the scored body*, not in the instructions. R1's WEAK SCORER anti-anchor earns PARTIAL on C-11 because it is confined to the preamble. Prompting the scorer to write the first evidence cell (V-01/C-01) as an explicit "model cell" -- one that others can refer to -- plants the positive anchor where C-11 requires it, at a natural moment when the scorer is writing their first verdict anyway. The cost is length; the risk is that one model cell is insufficient to prevent restatement in later cells. |
| E | Output format -- labeled declaration field | C-12 requires a labeled YES/NO declaration in the arithmetic verification step -- not prose. R1's V-01 produced this as an excellence signal via a Step 4 block with `Matches stated score: [YES | NO -- discrepancy: stated X, computed Y]`. Making this a required named slot (rather than a suggested format) directly enforces C-12's pass condition without inference. The hypothesis is that naming the field in the prompt causes it to appear in the output; omitting the field name causes the scorer to write prose that satisfies C-10 but not C-12. |
| F | Phrasing register -- formula denominator guard | N_aspirational changed from 2 (v1) to 4 (v2). A scorer carrying over the R1 formula silently inflates aspirational scores. A FORMULA CHANGE ALERT block at load time -- printing both the old and new denominators, naming the change explicitly, and requiring the scorer to copy the corrected formula into the load block -- surfaces this error class before it enters any composite score. This targets C-10 (arithmetic correctness) and C-12 (discrepancy detection) at the root cause rather than the symptom. |

Single-axis runs: V-01 (D), V-02 (E), V-03 (F)
Combinations: V-04 (D+E), V-05 (D+E+F)

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v2-2026-03-16.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/4 * 10)`
N_essential=5, N_recommended=3, N_aspirational=4
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 -- Inertia framing: positive body anchor

**Axis**: D -- Inertia framing
**Hypothesis**: C-11 fails when the positive anchor exists only in the instructions rather than
in the scored body. The R1 WEAK SCORER block gives the scorer a negative template to avoid but
no positive template to copy, so borderline evidence cells recur once the preamble is out of
context. Asking the scorer to treat the *first evidence cell they write* as a demonstration cell
-- explicitly labeled as a model other cells should follow -- plants the positive anchor at the
earliest point in the scoring body, when the scorer is most likely to write carefully. If the
first cell is thorough, C-11 PASS is satisfied immediately and the anchor is visible to any
reader of the scorecard. The risk is that one early model cell does not transfer discipline to
later cells when output length grows; this round tests whether proximity-to-model is sufficient
or whether a per-cell reinforcement mechanism is also needed.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete all phases in order; each phase closes with its required EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE -- [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

---

**Phase 1 -- LOAD**

Read the rubric file. Read all N output files.

Write a load summary. All four items are required for C-01 PASS:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12
Formula: [exact composite formula text from rubric]
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

**MODEL CELL INSTRUCTION**: The very first evidence cell you write -- the cell for V-01/C-01 --
is a demonstration cell. Write it as though a new scorer will read it to understand what correct
evidence looks like. It must:
- Quote or specifically reference a phrase, section, or structural feature from the output
- Explain in one sentence why that reference supports the verdict
- Not restate the criterion name as the evidence

Label it: `[MODEL CELL -- other cells should follow this pattern]`

This model cell satisfies C-11 (evidence positive anchor) for the entire scorecard.

For each output V-XX, write a verdict table followed by per-output notes.

**Verdict table** (one row per criterion, all 12):

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-02 | Per-criterion verdict matrix | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-03 | Evidence for every verdict | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-04 | Composite score per output | E | PASS/PARTIAL/FAIL | [quote or specific structural reference; note whether E/R/A breakdown was shown] |
| C-05 | Failure patterns section | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-06 | Ranked leaderboard | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-07 | Excellence signals | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-08 | Per-output synthesis notes | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-09 | Regression signals | A | PASS/PARTIAL/FAIL | [quote, or "PARTIAL -- no prior round data available"] |
| C-10 | Score arithmetic verification | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-11 | Evidence positive anchor | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-12 | Discrepancy declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |

Evidence rules:
- Every cell must reference specific output content. Restating the criterion does not qualify.
- C-01: note which of the four sub-elements (IDs+tiers, formula, threshold, output count) are present.
- C-04: note whether the E/R/A breakdown appears before the final number, or only the final number.
- C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all six synthesis sections. Every section is required.

**3a. Composite Scores**
For each output, show the tier breakdown before the final number:
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/4
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/4 * 10) = [score]
      Golden: YES | NO ([reason if NO])
```
PARTIAL counts as 0.5. Show as decimal: "E=3.5/5" not "E=3/5" when a PARTIAL exists.

**3b. Ranked Leaderboard**
All N outputs, descending by composite score. Ties stated explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|
| 1 | V-XX | XX.X | YES/NO |

**3c. Failure Patterns**
Any criterion with zero PASS across all N outputs (PARTIAL is not PASS for this test).
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3d. Excellence Signals**
Any output-criterion pair where one output structurally leads the field on that criterion.
Each signal: name the output, the criterion, and the structural feature that produced the outlier.
"V-XX scored highest overall" is not an excellence signal.
Required even when empty: `No excellence signals identified in this scoring run.`

**3e. Per-Output Synthesis Notes**
One paragraph per output: what did it do structurally that drove its score up or down relative
to the other outputs? Do not recount verdicts -- explain the mechanism.

**3f. Regression Signals**
If prior-round data was provided: flag any PASS->FAIL or PASS->PARTIAL regressions by criterion
and output ID.
If not: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all six sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-02 -- Output format: labeled declaration field

**Axis**: E -- Output format
**Hypothesis**: C-12 fails when arithmetic verification is written as prose ("the score checks
out", "verification performed") rather than as a labeled declaration field. The distinction is
mechanical: prose allows a silent pass-through where the scorer affirms correctness without
naming the specific numbers that were matched. A labeled declaration field with an explicit
`YES | NO -- discrepancy: stated X, computed Y` slot forces a binary choice and names the
discrepancy slot whether or not an error exists. When this field appears in the prompt as a
required named slot -- not a suggested format -- the scorer treats it as a template to fill in
rather than a style to approximate. R1 V-01 produced this as an excellence signal; this
variation tests whether extracting the field as an explicit named requirement causes it to
appear in V-02, V-04, V-05 equivalents where it was absent in R1. The risk is that scorers fill
in the field mechanically ("YES") without performing the underlying arithmetic, satisfying C-12
structurally while C-10 remains weak.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete all phases in order; each phase closes with its required EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE -- [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

---

**Phase 1 -- LOAD**

Read the rubric file. Read all N output files.

Write a load summary containing all four required items:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12
Formula: [exact composite formula text from rubric]
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

For each output V-XX, write a verdict table covering all 12 criteria.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-02 | Per-criterion verdict matrix | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-03 | Evidence for every verdict | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-04 | Composite score per output | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-05 | Failure patterns section | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-06 | Ranked leaderboard | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-07 | Excellence signals | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-08 | Per-output synthesis notes | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-09 | Regression signals | A | PASS/PARTIAL/FAIL | [quote, or "PARTIAL -- no prior round data available"] |
| C-10 | Score arithmetic verification | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-11 | Evidence positive anchor | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-12 | Discrepancy declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |

Evidence cells must reference specific output content. Restating the criterion does not qualify.
For C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all six synthesis sections in order. Every section is required.

**3a. Composite Scores**
For each output, show the tier breakdown before the final number:
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/4
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/4 * 10) = [score]
      Golden: YES | NO
```
PARTIAL = 0.5 toward pass count.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite score from the verdict table. Write this block:

```
Verification target: [output ID]
E verdicts: [list all 5 E verdicts for this output]
  E pass count: [count, counting PARTIAL as 0.5]
R verdicts: [list all 3 R verdicts]
  R pass count: [count]
A verdicts: [list all 4 A verdicts]
  A pass count: [count]
Computed composite: ([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/4 * 10) = [result]
Matches stated score: [YES | NO -- discrepancy: stated [X], computed [Y]]
```

The `Matches stated score:` field is required. It must contain YES or NO and, if NO, name the
exact discrepancy. Prose like "the score checks out" does not satisfy this requirement.

**3c. Ranked Leaderboard**
All N outputs, descending by composite score. Ties stated explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|
| 1 | V-XX | XX.X | YES/NO |

**3d. Failure Patterns**
Criteria with zero PASS across all N outputs. PARTIAL is not PASS for this test.
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3e. Excellence Signals**
Output-criterion pairs where one output structurally leads. Each signal: output, criterion, mechanism.
"V-XX scored highest overall" is not an excellence signal.
Required even when empty: `No excellence signals identified in this scoring run.`

**3f. Per-Output Synthesis Notes**
One paragraph per output: what structural choices drove its score? Do not recount verdicts.

**3g. Regression Signals**
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-03 -- Phrasing register: formula denominator guard

**Axis**: F -- Phrasing register
**Hypothesis**: N_aspirational changed from 2 (v1-2026-03-16) to 4 (v2-2026-03-16). A scorer
who carries over the R1 formula computes (aspirational_pass/2 * 10), doubling the aspirational
weight and silently inflating scores by up to 5 points. This error is invisible in the scored
body unless the scorer re-states the formula explicitly in their composite calculations -- and
even then it requires the reader to know the prior denominator to notice the discrepancy. A
FORMULA CHANGE ALERT block at load time, naming the old and new denominators explicitly and
requiring the scorer to copy the corrected formula before proceeding, surfaces this error class
before it enters any calculation. The hypothesis is that naming the change (not just providing
the correct formula) causes the scorer to actively update their formula rather than passively
copying from R1 memory. The risk is that scorers read the alert but still use the wrong
denominator in the calculation body; this round tests whether the alert-and-copy mechanism is
sufficient or whether a per-calculation echo is also needed.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete all phases in order; each phase closes with its required EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE -- [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

---

**Phase 1 -- LOAD**

Read the rubric file. Read all N output files.

**FORMULA CHANGE ALERT -- read before writing anything**:

The v2-2026-03-16 rubric changed the aspirational denominator.

```
PRIOR formula (v1, DO NOT USE):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 2 * 10)   <-- WRONG for v2 (N_aspirational was 2)

CURRENT formula (v2, USE THIS):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 4 * 10)   <-- CORRECT (N_aspirational is now 4)
```

If you use the prior formula, aspirational scores will be inflated by up to 5 points. Any
output that passes only aspirational criteria (and not essential/recommended) will appear to
score approximately 5 points higher than it should.

Write a load summary containing all four required items, including the corrected formula:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12   [N=4, denominator=4]
Formula (v2, corrected):
  (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 4 * 10)
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

For each output V-XX, write a verdict table covering all 12 criteria.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-02 | Per-criterion verdict matrix | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-03 | Evidence for every verdict | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-04 | Composite score per output | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-05 | Failure patterns section | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-06 | Ranked leaderboard | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-07 | Excellence signals | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-08 | Per-output synthesis notes | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-09 | Regression signals | A | PASS/PARTIAL/FAIL | [quote, or "PARTIAL -- no prior round data available"] |
| C-10 | Score arithmetic verification | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-11 | Evidence positive anchor | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-12 | Discrepancy declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |

Evidence cells must reference specific output content. Restating the criterion does not qualify.
For C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all six synthesis sections in order. Every section is required.

**3a. Composite Scores**
Use the v2 formula. N_aspirational=4. Check your denominator before computing.
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/4
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/4 * 10) = [score]
      Golden: YES | NO
```
PARTIAL = 0.5 toward pass count.

**3b. Ranked Leaderboard**
All N outputs, descending by composite score. Ties stated explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|
| 1 | V-XX | XX.X | YES/NO |

**3c. Failure Patterns**
Criteria with zero PASS across all N outputs. PARTIAL is not PASS for this test.
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3d. Excellence Signals**
Output-criterion pairs where one output structurally leads. Each signal: output, criterion, mechanism.
Required even when empty: `No excellence signals identified in this scoring run.`

**3e. Per-Output Synthesis Notes**
One paragraph per output: what structural choices drove its score? Do not recount verdicts.

**3f. Regression Signals**
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all six sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-04 -- Combination: positive body anchor + labeled declaration field (D+E)

**Axes**: D + E -- Inertia framing + Output format
**Hypothesis**: V-01 (positive body anchor) targets C-11 by embedding a model evidence cell
in the scoring body; V-02 (labeled declaration field) targets C-12 by requiring an explicit
YES/NO field in arithmetic verification. These two failures are independent: C-11 is a per-cell
evidence quality property observable during Phase 2; C-12 is a synthesis-phase verification
property in Phase 3. A scorer can produce a well-formed model cell and still omit the labeled
declaration; or produce the labeled declaration and still write restatement evidence. The
combination closes both gaps simultaneously. The risk is that two separate requirements increase
prompt complexity, causing one to be treated as optional. This round tests whether the
combination is additive (both criteria pass) or whether one axis dominates and the other
produces a shallow response.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete all phases in order; each phase closes with its required EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE -- [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

---

**Phase 1 -- LOAD**

Read the rubric file. Read all N output files.

Write a load summary containing all four required items:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12
Formula: [exact composite formula text from rubric]
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

**MODEL CELL INSTRUCTION**: The very first evidence cell you write -- the cell for V-01/C-01 --
is a demonstration cell. Write it as though a new scorer will use it as a reference for all
subsequent evidence cells. It must quote or specifically reference a phrase, section, or
structural feature from the output (not restate the criterion), and explain in one sentence
why that reference supports the verdict. Label it: `[MODEL CELL]`

This model cell satisfies C-11 (evidence positive anchor) for the entire scorecard.

For each output V-XX, write a verdict table covering all 12 criteria.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-02 | Per-criterion verdict matrix | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-03 | Evidence for every verdict | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-04 | Composite score per output | E | PASS/PARTIAL/FAIL | [quote or specific structural reference; note whether E/R/A breakdown was shown] |
| C-05 | Failure patterns section | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-06 | Ranked leaderboard | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-07 | Excellence signals | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-08 | Per-output synthesis notes | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-09 | Regression signals | A | PASS/PARTIAL/FAIL | [quote, or "PARTIAL -- no prior round data available"] |
| C-10 | Score arithmetic verification | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-11 | Evidence positive anchor | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-12 | Discrepancy declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |

Evidence cells must reference specific output content. Restating the criterion does not qualify.
For C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all seven synthesis sections in order. Every section is required.

**3a. Composite Scores**
For each output, show the tier breakdown before the final number:
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/4
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/4 * 10) = [score]
      Golden: YES | NO
```
PARTIAL = 0.5 toward pass count.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite from the verdict table:

```
Verification target: [output ID]
E verdicts: [list all 5 E verdicts]
  E pass count: [count, PARTIAL=0.5]
R verdicts: [list all 3 R verdicts]
  R pass count: [count]
A verdicts: [list all 4 A verdicts]
  A pass count: [count]
Computed composite: ([E]/5 * 60) + ([R]/3 * 30) + ([A]/4 * 10) = [result]
Matches stated score: [YES | NO -- discrepancy: stated [X], computed [Y]]
```

The `Matches stated score:` field is required. Prose like "the score checks out" does not satisfy
this requirement; the labeled YES/NO field with discrepancy slot is required.

**3c. Ranked Leaderboard**
All N outputs, descending by composite score. Ties stated explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|
| 1 | V-XX | XX.X | YES/NO |

**3d. Failure Patterns**
Criteria with zero PASS across all N outputs. PARTIAL is not PASS.
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3e. Excellence Signals**
Output-criterion pairs where one output structurally leads. Each signal: output, criterion, mechanism.
Required even when empty: `No excellence signals identified in this scoring run.`

**3f. Per-Output Synthesis Notes**
One paragraph per output: what structural choices drove its score? Do not recount verdicts.

**3g. Regression Signals**
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-05 -- Combination: positive body anchor + labeled declaration field + formula denominator guard (D+E+F)

**Axes**: D + E + F -- Inertia framing + Output format + Phrasing register
**Hypothesis**: V-04 (D+E) closes C-11 and C-12 gaps independently. V-03 (F) closes the
arithmetic denominator gap that silently inflates scores when scorers carry over the R1 formula.
These three axes operate at different points in the scoring lifecycle: D fires at the first
evidence cell (Phase 2 entry), E fires in the arithmetic verification block (Phase 3 mid), and
F fires at load time before any scoring begins (Phase 1 exit). No two axes address the same
failure mode or the same lifecycle point, so the combination should be fully additive. The risk
is cognitive overhead: the formula alert and model cell instruction add to Phase 1 and Phase 2
respectively, and the labeled declaration adds to Phase 3. A scorer who reads all three
mechanisms carefully will produce a scorecard that passes C-10, C-11, and C-12 simultaneously --
but a scorer who skims may drop the denominator check or collapse the model cell to a label
without substance. This round tests whether the three-mechanism combination achieves higher
composite scores than any single-axis variation.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (V-01 through V-NN, provided by caller)
- Prior-round scorecard file path, if available (optional)

**Phase manifest** -- complete all phases in order; each phase closes with its required EXIT TOKEN:

| Phase | EXIT TOKEN (write verbatim) |
|-------|-----------------------------|
| LOAD | `=== LOAD COMPLETE ===` |
| SCORING | `=== SCORING COMPLETE -- [N] outputs scored ===` |
| SYNTHESIS | `=== SYNTHESIS COMPLETE ===` |
| WRITE | `=== WRITE COMPLETE ===` |

---

**Phase 1 -- LOAD**

Read the rubric file. Read all N output files.

**FORMULA CHANGE ALERT -- v2 rubric change from v1:**

```
PRIOR formula (v1, DO NOT USE):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 2 * 10)   <-- WRONG for v2

CURRENT formula (v2, USE THIS):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 4 * 10)   <-- N_aspirational is now 4
```

Using the prior formula inflates aspirational contribution by up to 5 points.

Write a load summary containing all four required items, including the corrected formula:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12   [N=4, denominator=4]
Formula (v2, corrected):
  (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 4 * 10)
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

**MODEL CELL INSTRUCTION**: The very first evidence cell you write -- the cell for V-01/C-01 --
is a demonstration cell. Write it to model what correct evidence looks like: quote or
specifically reference a phrase, section, or structural feature from the output (not the
criterion name), and explain in one sentence why that reference supports the verdict.
Label it: `[MODEL CELL -- this is what correct evidence looks like]`

This model cell satisfies C-11 (evidence positive anchor) for the entire scorecard. Subsequent
evidence cells should follow the same pattern: specific reference, not restatement.

For each output V-XX, write a verdict table covering all 12 criteria.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-02 | Per-criterion verdict matrix | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-03 | Evidence for every verdict | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-04 | Composite score per output | E | PASS/PARTIAL/FAIL | [quote or specific structural reference; note whether E/R/A breakdown was shown] |
| C-05 | Failure patterns section | E | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-06 | Ranked leaderboard | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-07 | Excellence signals | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-08 | Per-output synthesis notes | R | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-09 | Regression signals | A | PASS/PARTIAL/FAIL | [quote, or "PARTIAL -- no prior round data available"] |
| C-10 | Score arithmetic verification | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-11 | Evidence positive anchor | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |
| C-12 | Discrepancy declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference] |

Evidence cells must reference specific output content. Restating the criterion does not qualify.
For C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all seven synthesis sections in order. Every section is required.

**3a. Composite Scores**
Use the v2 formula. Confirm your denominator: N_aspirational=4.
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/4
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/4 * 10) = [score]
      Golden: YES | NO
```
PARTIAL = 0.5 toward pass count. Show decimals when applicable.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite score from the verdict table:

```
Verification target: [output ID]
E verdicts: [list all 5 verdicts]
  E pass count: [count, PARTIAL=0.5]
R verdicts: [list all 3 verdicts]
  R pass count: [count]
A verdicts: [list all 4 verdicts]
  A pass count: [count]
Computed composite: ([E]/5 * 60) + ([R]/3 * 30) + ([A]/4 * 10) = [result]
Matches stated score: [YES | NO -- discrepancy: stated [X], computed [Y]]
```

The `Matches stated score:` field requires an explicit YES or NO. If YES, no further action.
If NO, name the stated score, the computed score, and the likely source of the discrepancy.
Prose like "verified" or "the score checks out" does not satisfy this requirement.

**3c. Ranked Leaderboard**
All N outputs, descending by composite score. Ties stated explicitly.

| Rank | Output | Composite | Golden |
|------|--------|-----------|--------|
| 1 | V-XX | XX.X | YES/NO |

**3d. Failure Patterns**
Criteria with zero PASS across all N outputs. PARTIAL is not PASS.
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3e. Excellence Signals**
Output-criterion pairs where one output structurally leads. Each signal: output, criterion, mechanism.
Required even when empty: `No excellence signals identified in this scoring run.`

**3f. Per-Output Synthesis Notes**
One paragraph per output: what structural choices drove its score? Do not recount verdicts.

**3g. Regression Signals**
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.
