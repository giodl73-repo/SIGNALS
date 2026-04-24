# quest-score Variations -- Round 3 (v3-2026-03-16 rubric)
**Skill**: quest-score
**Rubric**: v3-2026-03-16 (C-01--C-05 essential, C-06--C-08 recommended, C-09--C-14 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=6**
**Date**: 2026-03-16
**Round**: 3

---

## Context: what informed this round

Round 3 targets the v3 rubric dated 2026-03-16. Round 2 against the v2 rubric established three
mechanisms that address C-11 and C-12: Axis D (MODEL CELL advisory at Phase 2 entry), Axis E
(labeled YES/NO declaration field), and Axis F (FORMULA CHANGE ALERT at load time). The R2 champion
was V-05 (D+E+F combined). All R3 variations carry D+E+F forward as the established base, updating
F for the new denominator. Two new Aspirational criteria in v3 were extracted from R2 excellence
signals:

| Change | R2 (v2) | R3 (v3) | Design consequence |
|--------|---------|---------|-------------------|
| C-13 (formula version delta declaration) | Not in rubric | **New Aspirational** -- the scorer's output must explicitly name the prior and current N_aspirational values before any composite score | R2's Axis F put the alert in the PROMPT instructions; C-13 PASS requires the delta to appear in the SCORER'S OUTPUT. A prompt alert that prevents wrong computation does not satisfy C-13 if the scorer never writes the delta down. |
| C-14 (pre-scoring mechanism placement) | Not in rubric | **New Aspirational** -- the evidence positive anchor must appear at Phase 2 entry (first evidence cell), not just somewhere in the scoring body | R2's Axis D used an advisory instruction above the table. C-14 distinguishes between the anchor existing (C-11) and being placed early enough to prevent errors rather than correct them. |
| N_aspirational denominator | 4 (C-09..C-12) | **6 (C-09..C-14)** | Scorers carrying over the R2 formula compute (aspirational_pass/4 * 10) -- inflating aspirational contribution by up to 1.67 points. |

**v3 rubric counts**: E=5 (C-01..C-05), R=3 (C-06..C-08), A=6 (C-09..C-14)

**Formula**:
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essentials PASS AND composite >= 80
**N/A conditions**: C-09 PARTIAL (not FAIL) when scorer writes the prescribed no-prior-data statement;
C-13 PARTIAL (not FAIL) when scorer writes the prescribed no-prior-version-delta statement

**Score landmarks:**
- All essential + all recommended + all aspirational: 100
- All essential + all recommended + no aspirational: 90
- All essential + no recommended + no aspirational: 60

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| G | Output-level delta declaration | C-13 requires the delta notice to appear in the SCORER'S OUTPUT before any composite score -- not merely in the prompt instructions. R2's FORMULA CHANGE ALERT (Axis F) prevents wrong computation by alerting the scorer in the prompt, but never requires them to write the prior/current comparison into their scorecard. A scorer can follow F perfectly (compute /6 correctly) while still producing C-13 PARTIAL (no delta declared in output). Axis G adds a required output block: the scorer writes an explicit `FORMULA VERSION DELTA` block naming prior=4 and current=6, satisfying C-13's pass condition at Phase 1 entry. The risk: the block may be filled mechanically without genuine version verification, satisfying C-13 structurally while bypassing the verification intent. |
| H | In-template Phase 2 entry lock | C-14 requires the evidence positive anchor at Phase 2 entry -- the first evidence cell. R2's Axis D was advisory: prose above the table told the scorer to write a model cell first. Advisory placement has two failure modes: (1) the scorer produces the model cell as a caption or heading outside the table; (2) the scorer starts with a formula-standard cell and defers the model cell. Both produce C-11 PASS (anchor exists) but C-14 FAIL or PARTIAL (anchor not at Phase 2 entry). Axis H replaces the advisory with a structural first row: the verdict table template pre-stamps the C-01 evidence cell as `[PHASE 2 ENTRY -- MODEL CELL]`, locking the anchor to Phase 2 entry by position in the template rather than by instruction. The risk: the pre-labeled slot is filled with a placeholder ("V-01 has a load summary"), satisfying placement while failing quality -- C-14 PASS but C-11 PARTIAL. |
| I | Per-calculation denominator annotation | Axes F and G enforce formula correctness at Phase 1. Axis I tests whether calculation-site enforcement is an effective alternative path. In Phase 3a, every composite score row annotates the denominator inline: `A=[n]/6 [N_aspirational=6, v3]`. If the scorer carries over /4, the template annotation `6` is visually inconsistent with their calculation, making stale-denominator errors visible at the calculation site rather than caught only at load time. Secondary hypothesis: whether repeated inline denominator annotation satisfies C-13's pass condition (which requires explicit prior/current comparison) or only produces C-13 PARTIAL (current value stated, but no prior named). |

Single-axis runs: V-01 (G), V-02 (H), V-03 (I)
Combinations: V-04 (G+H), V-05 (G+H+I)

Base mechanisms in all variations: D (MODEL CELL advisory), E (labeled declaration field), F (formula alert, updated for v3: prior=/4, current=/6)
Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v3-2026-03-16.md`
Formula: `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/6 * 10)`
N_essential=5, N_recommended=3, N_aspirational=6
Golden threshold: all 5 essentials PASS AND composite >= 80

---

## V-01 -- Output-level delta declaration

**Axis**: G -- Output-level delta declaration
**Hypothesis**: C-13 PASS requires the delta notice to appear in the scorer's output, naming (a) the
prior N_aspirational value and (b) the current value. R2's Axis F put a FORMULA CHANGE ALERT in the
prompt instructions, preventing wrong computation, but never required the scorer to write the
prior/current comparison into their scorecard. A scorer can follow F perfectly -- compute with /6
correctly -- while still producing C-13 PARTIAL because no delta was declared in their output.
Axis G closes this gap by requiring an explicit `FORMULA VERSION DELTA` output block at Phase 1
that names prior=4 and current=6 before the load summary. The block is a required output artifact,
not a pre-filled instruction: the scorer copies the template and fills in the values. If they fill
it in with the wrong values, that is a detectable error (C-13 FAIL). If they fill it in correctly,
C-13 is satisfied at the earliest lifecycle point. The risk is that the block becomes rote -- filled
mechanically without genuine verification. This round tests whether the output declaration
requirement is sufficient for C-13 PASS or whether the declaration must also be tied to an active
verification step.

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

**FORMULA CHANGE ALERT -- v3 rubric change from v2:**

```
PRIOR formula (v2, DO NOT USE):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 4 * 10)   <-- WRONG for v3 (N_aspirational was 4)

CURRENT formula (v3, USE THIS):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 6 * 10)   <-- CORRECT (N_aspirational is now 6)
```

Using the prior formula inflates aspirational contribution by up to 1.67 points per output.

**FORMULA VERSION DELTA DECLARATION (write this block in your output before the load summary):**

```
FORMULA VERSION DELTA:
  Prior rubric version: v2
  Prior N_aspirational: 4
  Current rubric version: v3
  Current N_aspirational: 6
  Change: aspirational denominator increased 4 -> 6
  Impact: v2 formula would compute (aspirational_pass / 4 * 10) instead of (/ 6 * 10),
          inflating aspirational contribution by up to 1.67 points per output
```

Write this block verbatim with the values filled in. It must appear in your output before the load
summary below. This block satisfies C-13 (formula version delta declaration) for the scorecard.

Write a load summary containing all four required items:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12, C-13, C-14   [N=6, denominator=6]
Formula (v3, corrected):
  (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 10)
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

This model cell satisfies C-11 (evidence positive anchor). Because it appears as the first evidence
cell written, it also satisfies C-14 (pre-scoring mechanism placement).

For each output V-XX, write a verdict table covering all 14 criteria:

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
| C-13 | Formula version delta declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; does the output name prior=4 and current=6?] |
| C-14 | Pre-scoring mechanism placement | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; is the MODEL CELL the first evidence cell?] |

Evidence rules:
- Every cell must reference specific output content. Restating the criterion does not qualify.
- C-01: note which of the four sub-elements (IDs+tiers, formula, threshold, output count) are present.
- C-04: note whether the E/R/A breakdown appears before the final number, or only the final number.
- C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.
- C-13: check whether the scored output contains an explicit prior/current delta notice with both
  values named. PARTIAL if current formula loaded correctly but no prior value is stated.
- C-14: check whether the MODEL CELL or equivalent anchor appears as the first evidence cell in
  Phase 2. PARTIAL if anchor exists but appears after the first three evidence cells. FAIL if absent.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all seven synthesis sections. Every section is required.

**3a. Composite Scores**
For each output, show the tier breakdown before the final number:
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/6
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/6 * 10) = [score]
      Golden: YES | NO ([reason if NO])
```
PARTIAL counts as 0.5. Show as decimal: "E=3.5/5" not "E=3/5" when a PARTIAL exists.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite score from the verdict table. Write this block:

```
Verification target: [output ID]
E verdicts: [list all 5 E verdicts for this output]
  E pass count: [count, counting PARTIAL as 0.5]
R verdicts: [list all 3 R verdicts]
  R pass count: [count]
A verdicts: [list all 6 A verdicts]
  A pass count: [count]
Computed composite: ([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/6 * 10) = [result]
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
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions by criterion and output ID.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-02 -- In-template Phase 2 entry lock

**Axis**: H -- In-template Phase 2 entry lock
**Hypothesis**: C-14 PASS requires the evidence positive anchor at Phase 2 entry -- the first
evidence cell in the scoring section. R2's Axis D was advisory: prose above the verdict table told
the scorer to write the first cell as a model cell. Advisory placement has two failure modes: (1)
the scorer produces the model cell as a caption or heading outside the evidence rows, placing the
anchor outside the cells C-14 measures; (2) the scorer skims the instruction and begins with a
formula-standard row, deferring the model cell to later. Both modes produce C-11 PASS (anchor
exists somewhere) but C-14 FAIL or PARTIAL (anchor not at Phase 2 entry). Axis H replaces the
advisory instruction with a structural first row: the verdict table template itself pre-stamps the
C-01 evidence cell as `[PHASE 2 ENTRY -- MODEL CELL: fill before all other criteria]`. The scorer
fills a pre-slotted row at the position where C-14 requires the anchor, not an instruction above
the table. After filling it, the scorer writes a placement verification line confirming the anchor
position. The risk: the pre-labeled cell is filled with minimal content ("V-01 has a load summary")
that satisfies placement structurally while falling short of quality -- C-14 PASS but C-11 PARTIAL.
This tests whether structural placement is sufficient or whether a quality enforcement mechanism
(such as D's explicit quality criteria list) must accompany the structural lock.

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

**FORMULA CHANGE ALERT -- v3 rubric change from v2:**

```
PRIOR formula (v2, DO NOT USE):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 4 * 10)   <-- WRONG for v3 (N_aspirational was 4)

CURRENT formula (v3, USE THIS):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 6 * 10)   <-- CORRECT (N_aspirational is now 6)
```

Using the prior formula inflates aspirational contribution by up to 1.67 points per output.

Write a load summary containing all four required items:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12, C-13, C-14   [N=6, denominator=6]
Formula (v3, corrected):
  (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 10)
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

For each output V-XX, write a verdict table covering all 14 criteria.

The first evidence cell -- V-01/C-01 -- is a required Phase 2 entry anchor. It is pre-labeled
in the template below. Fill it before scoring any other criterion. The cell must:
- Quote or specifically reference a phrase, section, or structural feature from the output
- Explain in one sentence why that reference supports the verdict
- Not restate the criterion name as the evidence

After filling in the first row, write:
```
MODEL CELL PLACEMENT VERIFIED: anchor is at Phase 2 entry (first evidence cell)
```
This line confirms C-11 (evidence positive anchor) and C-14 (pre-scoring mechanism placement).

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | **[PHASE 2 ENTRY -- MODEL CELL: fill this cell with a specific quote and one-sentence explanation before scoring any other criterion. This cell anchors C-11 and C-14 for the entire scorecard.]** |
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
| C-13 | Formula version delta declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; does the output name prior=4 and current=6?] |
| C-14 | Pre-scoring mechanism placement | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; confirm MODEL CELL PLACEMENT VERIFIED line appears after a substantive first cell] |

Evidence rules:
- Every cell must reference specific output content. Restating the criterion does not qualify.
- C-01: note which of the four sub-elements (IDs+tiers, formula, threshold, output count) are present.
- C-04: note whether the E/R/A breakdown appears before the final number, or only the final number.
- C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.
- C-13: PARTIAL if current formula loaded correctly but no prior/current comparison exists in output.
- C-14: PASS if MODEL CELL PLACEMENT VERIFIED line exists and the pre-labeled cell was filled with a
  specific reference (not a placeholder). PARTIAL if placement line exists but cell is perfunctory.
  FAIL if the pre-labeled slot was left as a placeholder or the placement verification line is absent.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all seven synthesis sections. Every section is required.

**3a. Composite Scores**
For each output, show the tier breakdown before the final number:
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/6
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/6 * 10) = [score]
      Golden: YES | NO ([reason if NO])
```
PARTIAL counts as 0.5. Show as decimal: "E=3.5/5" not "E=3/5" when a PARTIAL exists.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite score from the verdict table. Write this block:

```
Verification target: [output ID]
E verdicts: [list all 5 E verdicts for this output]
  E pass count: [count, counting PARTIAL as 0.5]
R verdicts: [list all 3 R verdicts]
  R pass count: [count]
A verdicts: [list all 6 A verdicts]
  A pass count: [count]
Computed composite: ([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/6 * 10) = [result]
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
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions by criterion and output ID.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-03 -- Per-calculation denominator annotation

**Axis**: I -- Per-calculation denominator annotation
**Hypothesis**: Axes F and G enforce formula correctness at Phase 1 -- the FORMULA CHANGE ALERT
prevents wrong computation, and the FORMULA VERSION DELTA block (G) produces a C-13-satisfying
output declaration. Both fire at load time, before any calculation. Axis I tests whether
calculation-site enforcement is an effective alternative: rather than alerting upfront, every
composite score row in Phase 3a annotates the denominator inline as `A=[n]/6 [N_aspirational=6,
v3]`. If the scorer carries over the v2 denominator, writing `A=[n]/4` conflicts with the
template's `6` annotation, making the stale denominator visually inconsistent with the format
requirement rather than silently wrong. Two empirical questions: (1) Does per-row annotation catch
stale-denominator errors at Phase 3 as effectively as Phase 1 alerting? (2) Does the repeated
inline annotation satisfy C-13's pass condition, which requires explicit prior/current comparison?
C-13 requires naming (a) the prior value and (b) the current value. Axis I names only the current
value in each row (`6, v3`); the prior value (4) is never stated. The prediction: Axis I alone
produces C-13 PARTIAL (current stated, prior not named) while C-10 PASS (denominator correct).
The combination with G (V-05) would close both. Risk: scorers treat the annotation as boilerplate
and fill in `6` from the template without checking the formula, satisfying the form while
bypassing verification.

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

**FORMULA CHANGE ALERT -- v3 rubric change from v2:**

```
PRIOR formula (v2, DO NOT USE):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 4 * 10)   <-- WRONG for v3 (N_aspirational was 4)

CURRENT formula (v3, USE THIS):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 6 * 10)   <-- CORRECT (N_aspirational is now 6)
```

Using the prior formula inflates aspirational contribution by up to 1.67 points per output.

Write a load summary containing all four required items:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12, C-13, C-14   [N=6, denominator=6]
Formula (v3, corrected):
  (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 10)
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

**MODEL CELL INSTRUCTION**: The very first evidence cell you write -- the cell for V-01/C-01 --
is a demonstration cell. Write it as though a new scorer will read it to understand what correct
evidence looks like. It must quote or specifically reference a phrase, section, or structural
feature from the output (not restate the criterion name), and explain in one sentence why that
reference supports the verdict. Label it: `[MODEL CELL -- other cells should follow this pattern]`

For each output V-XX, write a verdict table covering all 14 criteria:

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
| C-13 | Formula version delta declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; does the output name prior=4 and current=6?] |
| C-14 | Pre-scoring mechanism placement | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; is the MODEL CELL the first evidence cell?] |

Evidence rules:
- Every cell must reference specific output content. Restating the criterion does not qualify.
- C-01: note which of the four sub-elements (IDs+tiers, formula, threshold, output count) are present.
- C-04: note whether the E/R/A breakdown appears before the final number, or only the final number.
- C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.
- C-13: PARTIAL if current formula loaded correctly but no prior/current comparison exists in output.
- C-14: PASS if MODEL CELL is the first evidence cell. PARTIAL if after first three cells. FAIL if absent.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all seven synthesis sections. Every section is required.

**3a. Composite Scores**
For each output, annotate the aspirational denominator inline on every row to make the formula
version visible at the calculation site:

```
V-XX: E=[n]/5, R=[n]/3, A=[n]/6 [N_aspirational=6, v3]
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/6 * 10) = [score]
      Golden: YES | NO ([reason if NO])
```

The `[N_aspirational=6, v3]` annotation is required on every row. Its purpose: if you carried
over the v2 denominator (4), the annotation value `6` will be inconsistent with your calculation.
Confirm the annotation matches your formula before computing each score.
PARTIAL counts as 0.5. Show as decimal: "E=3.5/5" not "E=3/5" when a PARTIAL exists.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite score from the verdict table. Write this block:

```
Verification target: [output ID]
E verdicts: [list all 5 E verdicts for this output]
  E pass count: [count, counting PARTIAL as 0.5]
R verdicts: [list all 3 R verdicts]
  R pass count: [count]
A verdicts: [list all 6 A verdicts]
  A pass count: [count]
Computed composite: ([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/6 * 10) = [result]
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
Criteria with zero PASS across all N outputs. PARTIAL is not PASS for this test.
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3e. Excellence Signals**
Output-criterion pairs where one output structurally leads. Each signal: output, criterion, mechanism.
"V-XX scored highest overall" is not an excellence signal.
Required even when empty: `No excellence signals identified in this scoring run.`

**3f. Per-Output Synthesis Notes**
One paragraph per output: what structural choices drove its score? Do not recount verdicts.

**3g. Regression Signals**
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions by criterion and output ID.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-04 -- Combination: output-level delta declaration + in-template Phase 2 entry lock (G+H)

**Axes**: G + H -- Output-level delta declaration + In-template Phase 2 entry lock
**Hypothesis**: V-01 (G) targets C-13 by requiring the scorer to write an explicit FORMULA VERSION
DELTA output block naming prior=4 and current=6 before the load summary. V-02 (H) targets C-14 by
pre-stamping the first evidence cell in the verdict table, locking the MODEL CELL to Phase 2 entry
structurally rather than by advisory instruction. These two criteria address different lifecycle
points and different output properties: C-13 fires at Phase 1 (has the scorer declared the delta
before any score?), C-14 fires at Phase 2 entry (is the anchor at the first evidence cell?). They
share no mechanism overlap. The combination should be fully additive: G satisfies C-13 PASS by
requiring the declaration block at Phase 1; H satisfies C-14 PASS by locking the anchor cell
location at Phase 2 entry. The risk: the delta block (Phase 1) and the pre-labeled first row
(Phase 2 entry) are two distinct output requirements landing close together. A scorer who produces
both correctly gains on both aspirational criteria; a scorer who skims may fill one perfunctorily.
The specific failure mode to watch: delta block written with prior=6 and current=4 (values swapped),
which would produce C-13 FAIL while C-14 passes -- indicating mechanical block-filling without
comprehension. This round tests whether G+H is additively effective (both C-13 and C-14 PASS) or
whether one axis dominates.

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

**FORMULA CHANGE ALERT -- v3 rubric change from v2:**

```
PRIOR formula (v2, DO NOT USE):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 4 * 10)   <-- WRONG for v3 (N_aspirational was 4)

CURRENT formula (v3, USE THIS):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 6 * 10)   <-- CORRECT (N_aspirational is now 6)
```

Using the prior formula inflates aspirational contribution by up to 1.67 points per output.

**FORMULA VERSION DELTA DECLARATION (write this block in your output before the load summary):**

```
FORMULA VERSION DELTA:
  Prior rubric version: v2
  Prior N_aspirational: 4
  Current rubric version: v3
  Current N_aspirational: 6
  Change: aspirational denominator increased 4 -> 6
  Impact: v2 formula would compute (aspirational_pass / 4 * 10) instead of (/ 6 * 10),
          inflating aspirational contribution by up to 1.67 points per output
```

Write this block verbatim with the values filled in. It must appear before the load summary.
This block satisfies C-13 (formula version delta declaration) for the scorecard.

Write a load summary containing all four required items:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12, C-13, C-14   [N=6, denominator=6]
Formula (v3, corrected):
  (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 10)
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

For each output V-XX, write a verdict table covering all 14 criteria.

The first evidence cell -- V-01/C-01 -- is a required Phase 2 entry anchor. It is pre-labeled
in the template below. Fill it before scoring any other criterion. The cell must:
- Quote or specifically reference a phrase, section, or structural feature from the output
- Explain in one sentence why that reference supports the verdict
- Not restate the criterion name as the evidence

After filling in the first row, write:
```
MODEL CELL PLACEMENT VERIFIED: anchor is at Phase 2 entry (first evidence cell)
```
This line confirms C-11 (evidence positive anchor) and C-14 (pre-scoring mechanism placement).

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | **[PHASE 2 ENTRY -- MODEL CELL: fill this cell with a specific quote and one-sentence explanation before scoring any other criterion. This cell anchors C-11 and C-14 for the entire scorecard.]** |
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
| C-13 | Formula version delta declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; reference the FORMULA VERSION DELTA block in Phase 1] |
| C-14 | Pre-scoring mechanism placement | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; confirm MODEL CELL PLACEMENT VERIFIED line exists after a substantive first cell] |

Evidence rules:
- Every cell must reference specific output content. Restating the criterion does not qualify.
- C-01: note which of the four sub-elements (IDs+tiers, formula, threshold, output count) are present.
- C-04: note whether the E/R/A breakdown appears before the final number, or only the final number.
- C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.
- C-13: reference the delta block by name. PARTIAL if current formula loaded but no prior value named.
- C-14: PASS if PLACEMENT VERIFIED line exists and the pre-labeled cell was filled with a specific
  reference (not a placeholder). PARTIAL if placement line exists but cell is perfunctory. FAIL if
  absent entirely.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all seven synthesis sections. Every section is required.

**3a. Composite Scores**
For each output, show the tier breakdown before the final number:
```
V-XX: E=[n]/5, R=[n]/3, A=[n]/6
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/6 * 10) = [score]
      Golden: YES | NO ([reason if NO])
```
PARTIAL counts as 0.5. Show as decimal: "E=3.5/5" not "E=3/5" when a PARTIAL exists.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite score from the verdict table. Write this block:

```
Verification target: [output ID]
E verdicts: [list all 5 E verdicts for this output]
  E pass count: [count, counting PARTIAL as 0.5]
R verdicts: [list all 3 R verdicts]
  R pass count: [count]
A verdicts: [list all 6 A verdicts]
  A pass count: [count]
Computed composite: ([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/6 * 10) = [result]
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
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions by criterion and output ID.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.

---

## V-05 -- Combination: output-level delta declaration + in-template Phase 2 entry lock + per-calculation denominator annotation (G+H+I)

**Axes**: G + H + I -- Output-level delta declaration + In-template Phase 2 entry lock + Per-calculation denominator annotation
**Hypothesis**: V-04 (G+H) closes C-13 and C-14 with two mechanisms at different lifecycle points:
G fires at Phase 1 entry (delta block in the output before the load summary), H fires at Phase 2
entry (pre-labeled first evidence cell in the verdict template). Axis I adds a third mechanism at
Phase 3 (calculation time): every composite score row annotates the aspirational denominator inline
as `A=[n]/6 [N_aspirational=6, v3]`. These three axes operate at three distinct lifecycle points
with no overlap: G at Phase 1 output, H at Phase 2 first cell, I at Phase 3 per-row. Each targets
a different failure mode: G prevents C-13 FAIL by requiring the explicit delta declaration; H
prevents C-14 FAIL by structural cell pre-labeling; I prevents stale-denominator arithmetic errors
by making the formula version visible at every calculation site. A scorer who follows all three
produces: (1) a delta block satisfying C-13 PASS, (2) a model cell at Phase 2 entry satisfying
C-14 PASS, (3) per-row annotations making denominator errors visually inconsistent with the
template. The three mechanisms are mutually reinforcing by lifecycle position: a scorer who misses
Phase 1 (skips the delta block) will encounter Phase 2 (pre-labeled first cell); a scorer who skips
Phase 2 (doesn't fill the first cell substantively) will encounter Phase 3 (denominator annotation).
The hypothesis is that lifecycle distribution increases the probability that at least one mechanism
fires even when the scorer is rushed. The risk: three mandatory structural elements may cause all
three to be satisfied mechanically -- the delta block filled with values from memory, the model cell
filled with a placeholder, the denominator annotation echoed from the template -- satisfying C-13,
C-14, and C-10 structurally while none of the underlying verification was performed. This round
tests whether the three-mechanism combination achieves higher composite scores than any single or
two-axis variation.

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

**FORMULA CHANGE ALERT -- v3 rubric change from v2:**

```
PRIOR formula (v2, DO NOT USE):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 4 * 10)   <-- WRONG for v3 (N_aspirational was 4)

CURRENT formula (v3, USE THIS):
  composite = (essential_pass / 5 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 6 * 10)   <-- CORRECT (N_aspirational is now 6)
```

Using the prior formula inflates aspirational contribution by up to 1.67 points per output.

**FORMULA VERSION DELTA DECLARATION (write this block in your output before the load summary):**

```
FORMULA VERSION DELTA:
  Prior rubric version: v2
  Prior N_aspirational: 4
  Current rubric version: v3
  Current N_aspirational: 6
  Change: aspirational denominator increased 4 -> 6
  Impact: v2 formula would compute (aspirational_pass / 4 * 10) instead of (/ 6 * 10),
          inflating aspirational contribution by up to 1.67 points per output
```

Write this block verbatim with the values filled in. It must appear before the load summary.
This block satisfies C-13 (formula version delta declaration) for the scorecard.

Write a load summary containing all four required items:

```
Criteria loaded:
  Essential (E): C-01, C-02, C-03, C-04, C-05
  Recommended (R): C-06, C-07, C-08
  Aspirational (A): C-09, C-10, C-11, C-12, C-13, C-14   [N=6, denominator=6]
Formula (v3, corrected):
  (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 10)
Golden threshold: [exact condition text from rubric]
N/A rules: [each criterion with special N/A handling, or "none"]
Outputs to score: [list V-XX identifiers, count = N]
```

Write `=== LOAD COMPLETE ===` before proceeding.

---

**Phase 2 -- SCORING**

For each output V-XX, write a verdict table covering all 14 criteria.

The first evidence cell -- V-01/C-01 -- is a required Phase 2 entry anchor. It is pre-labeled
in the template below. Fill it before scoring any other criterion. The cell must:
- Quote or specifically reference a phrase, section, or structural feature from the output
- Explain in one sentence why that reference supports the verdict
- Not restate the criterion name as the evidence

After filling in the first row, write:
```
MODEL CELL PLACEMENT VERIFIED: anchor is at Phase 2 entry (first evidence cell)
```
This line confirms C-11 (evidence positive anchor) and C-14 (pre-scoring mechanism placement).
Subsequent evidence cells should follow the same pattern: specific reference, not restatement.

| ID | Criterion | Tier | Verdict | Evidence |
|----|-----------|------|---------|----------|
| C-01 | Rubric load verification | E | PASS/PARTIAL/FAIL | **[PHASE 2 ENTRY -- MODEL CELL: fill this cell with a specific quote and one-sentence explanation before scoring any other criterion. This cell anchors C-11 and C-14 for the entire scorecard.]** |
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
| C-13 | Formula version delta declaration | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; reference the FORMULA VERSION DELTA block in Phase 1] |
| C-14 | Pre-scoring mechanism placement | A | PASS/PARTIAL/FAIL | [quote or specific structural reference; confirm MODEL CELL PLACEMENT VERIFIED line exists after a substantive first cell] |

Evidence rules:
- Every cell must reference specific output content. Restating the criterion does not qualify.
- C-01: note which of the four sub-elements (IDs+tiers, formula, threshold, output count) are present.
- C-04: note whether the E/R/A breakdown appears before the final number, or only the final number.
- C-09: if no prior-round scorecard was provided, write `PARTIAL -- no prior round data available`.
- C-13: reference the delta block by name. PARTIAL if current formula loaded but no prior value named.
- C-14: PASS if PLACEMENT VERIFIED line exists and the pre-labeled cell was filled with a specific
  reference (not a placeholder). PARTIAL if placement line exists but cell is perfunctory. FAIL if
  absent entirely.

After the last output's verdict table, write `=== SCORING COMPLETE -- [N] outputs scored ===`.

---

**Phase 3 -- SYNTHESIS**

Write all seven synthesis sections. Every section is required.

**3a. Composite Scores**
For each output, annotate the aspirational denominator inline on every row:

```
V-XX: E=[n]/5, R=[n]/3, A=[n]/6 [N_aspirational=6, v3]
      composite = ([n]/5 * 60) + ([n]/3 * 30) + ([n]/6 * 10) = [score]
      Golden: YES | NO ([reason if NO])
```

The `[N_aspirational=6, v3]` annotation is required on every row. If your calculation uses
a different denominator, the annotation value `6` will be inconsistent with your formula -- a
signal that you may be carrying over the v2 denominator. Confirm the annotation matches your
formula before computing each score.
PARTIAL counts as 0.5. Show as decimal: "E=3.5/5" not "E=3/5" when a PARTIAL exists.

**3b. Arithmetic Verification**
Pick one output. Re-derive its composite score from the verdict table. Write this block:

```
Verification target: [output ID]
E verdicts: [list all 5 E verdicts for this output]
  E pass count: [count, counting PARTIAL as 0.5]
R verdicts: [list all 3 R verdicts]
  R pass count: [count]
A verdicts: [list all 6 A verdicts]
  A pass count: [count]
Computed composite: ([E_count]/5 * 60) + ([R_count]/3 * 30) + ([A_count]/6 * 10) = [result]
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
Criteria with zero PASS across all N outputs. PARTIAL is not PASS for this test.
Required even when empty: `No failure patterns -- all criteria passed in at least one output.`

**3e. Excellence Signals**
Output-criterion pairs where one output structurally leads. Each signal: output, criterion, mechanism.
"V-XX scored highest overall" is not an excellence signal.
Required even when empty: `No excellence signals identified in this scoring run.`

**3f. Per-Output Synthesis Notes**
One paragraph per output: what structural choices drove its score? Do not recount verdicts.

**3g. Regression Signals**
Prior-round data provided: flag PASS->FAIL or PASS->PARTIAL regressions by criterion and output ID.
Not provided: `No prior round data -- regression analysis cannot be performed.`

Write `=== SYNTHESIS COMPLETE ===` after all seven sections.

---

**Phase 4 -- WRITE**

Write the complete scorecard to:
`simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

Write `=== WRITE COMPLETE ===`.
