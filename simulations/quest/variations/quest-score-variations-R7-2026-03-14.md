Written to `simulations/quest/variations/quest-score-variations-R7-2026-03-14.md`.

---

## R7 Variations Summary

**5 complete prompt body variations for `quest-score` (v7 rubric)**

| V-ID | Axis | Single/Combo | Predicted Score | Key test |
|------|------|-------------|-----------------|----------|
| V-01 | Baseline -- R7 full stack | -- | 100.00 | All v7 updates applied: 21-row matrix, N_aspirational=14, C-21 auto-PASS declaration, C-20/C-21 in roster |
| V-02 | C-20 ablation | Single | 98.93 | C-19 preservation rule uses interrogative form ("Has it been carried forward?") -- tests C-19 PARTIAL + C-20 FAIL |
| V-03 | C-21 ablation | Single | 98.57 | Worked example placed in SETUP only; FAILURE PATTERNS has format placeholder -- tests C-10 FAIL + C-21 FAIL |
| V-04 | Score distribution format | Single | 99.64 | LEADERBOARD uses prose commentary without min/max/spread mandate -- tests C-09 PARTIAL |
| V-05 | Combination | Combo | 100.00 | V-01 + C-21 location lock named in Preservation Rule + 0.714 pt weight in distribution note + C-20 form enumeration (3 patterns) |

**R7 design rationale:**

The two new criteria (C-20, C-21) directly codify the R6 excellence signals:
- C-20 tests whether the preservation rule uses imperative grammar (R6 learning: form decides C-19, not location)
- C-21 tests whether the worked example stays in FAILURE PATTERNS (R6 V-03 failure mode, now a named criterion)

V-02 and V-03 are clean single-axis ablations of each new criterion. V-04 retests the C-09 gap from R5/R6 under the new N_aspirational=14 weight. V-05 is the combination synthesis candidate for R7 golden.

**Predicted score spread:** 1.43 pts (V-03 at 98.57 through V-01/V-05 at 100.00). Tighter than R6's 3.33 pt spread -- confirms the remaining differentiable gaps are narrowing as the rubric matures.
 PARTIAL when
calibration terminology is implied but not explicitly required.

V-05 is the combination pass: V-01 baseline + C-21 location lock named explicitly in the C-10
Preservation Rule + C-21 named in the standalone Auto-PASS block + N_aspirational=14
per-criterion weight (0.714 pt) stated in score distribution note + C-20 diagnostic question
explicitly enumerates all three verb-form patterns (imperative/interrogative/conditional).

Single-axis isolation:
- V-02: C-20 axis (preservation rule grammar only)
- V-03: C-21 axis (worked example location only)
- V-04: C-09 format axis (score distribution format only)
- V-05: Combination pass (C-21 location lock + C-21 auto-PASS + weight note + C-20 form names)

---

## V-01

**Axis:** Baseline -- R7 full stack (N_aspirational=14, 21-row scoring matrix, C-20/C-21
diagnostic questions, C-21 auto-PASS declaration, all R6 V-05 structures carried forward)

**Hypothesis:** All 21 criteria PASS. C-19 earns PASS (imperative preservation rule). C-20
earns PASS (mandatory verb "must" present). C-21 earns PASS or auto-PASS (worked example
remains in FAILURE PATTERNS). C-09 earns PASS (score distribution note mandates min/max/spread
vocabulary). Composite = 100.00.

---

Score N skill outputs against the supplied rubric. Produce a per-criterion verdict matrix,
composite scores, and cross-output analysis sections.

---

### PHASE 1 -- Setup before scoring any output

Do not open any output file until PHASE 1 is fully written.

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output.
**C-07 auto-PASS** when no prior-round scorecard is provided.
**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. This rule is in force at every rubric version
change and applies regardless of whether C-10 auto-PASS fires this run.

**STOP-1.** Do not proceed to Step 1.2 until all five auto-PASS declarations are written.

#### Step 1.2 -- Composite Formula (v7 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 14.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**STOP-2.** Do not proceed to Step 1.3 until the formula and evidence mandate are written.

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | -- | Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated? A matrix with 19 or 20 rows fails C-01 even if all other rows are correct. |
| C-02 | Evidence quote for every verdict | Essential | -- | For every verdict cell, is the evidence field non-empty and sourced verbatim from the scored output -- not a fabricated summary or a copy of the rubric criterion text? |
| C-03 | Composite score computed correctly | Essential | -- | Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1? An output using N_aspirational=12 (v6 values) is a FAIL for C-03. |
| C-04 | Ranked leaderboard present | Essential | -- | Does the leaderboard contain exactly four columns: Rank, Output, Score, Golden? Are all scored outputs present in the table? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Are all criteria that received FAIL or PARTIAL in every scored output listed, with an action line per entry? If no criterion fails universally, write "C-05 auto-PASS." |
| C-06 | Excellence signals surfaced | Recommended | -- | Does the section identify at least one output-criterion pair where one output outperforms the group by >= one tier? Is a "no differentials" note written if none exist? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is the section present with prior/current verdict comparison columns? If no prior-round scorecard was provided, write "C-07 auto-PASS." |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 auto-PASS | Does each failure pattern entry include an action line with a verb + real artifact filename + section location, with no format placeholders? |
| C-09 | Score distribution commentary | Aspirational | -- | Does the LEADERBOARD section state minimum score, maximum score, spread, and a calibration note distinguishing clustering (< 5 pt spread) from discrimination (>= 10 pt spread)? Are actual numeric values used, not qualitative summaries only? |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 auto-PASS | Does at least one FAILURE PATTERNS action line contain a fully instantiated example with a real artifact name and exact section path -- not a format placeholder, and not located only in SETUP or a roster column? |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | -- | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present in the SETUP block, each naming the criterion ID and trigger phrase? Declarations embedded only in roster columns do not satisfy C-11. |
| C-12 | Formula reproduced before first output section | Aspirational | -- | Does the formula with N_aspirational=14 appear in SETUP before any per-output heading? A formula with N_aspirational=12 is a C-12 FAIL regardless of whether C-03 passes. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | -- | Is there an explicit written mandate in the template requiring evidence quote before verdict in every cell, with a stated prohibition on reversal? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | -- | Is a Diagnostic Question column present in the criterion roster? Do all 21 criterion rows (C-01 through C-21) have non-empty questions? A roster with 19 rows lacking questions for C-20 and C-21 fails C-14. |
| C-15 | Preamble gate instruction present | Aspirational | -- | Does an imperative gate statement (e.g., "Do not open any output file until SETUP is fully written") appear at or near the end of the SETUP block? |
| C-16 | Named standalone auto-PASS block | Aspirational | -- | Are the auto-PASS conditions in a dedicated named block separate from the criterion roster? Does each declaration name the criterion ID and trigger phrase explicitly -- not implied by roster columns? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | -- | Do at least three diagnostic questions name the specific mechanism of that criterion: a count (C-01), an N-value check (C-03), a form distinction (C-20), or a location check (C-10/C-21)? Generic questions like "Is this criterion satisfied?" do not satisfy C-17. |
| C-18 | Named standalone regression signals section | Aspirational | -- | Is a "### REGRESSION SIGNALS" section present in the template body, separate from SETUP and per-output scoring tables? Does it include Criterion, Prior Verdict, Current Verdict, and Mechanism columns? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | -- | Is there an explicit preservation rule near the C-10 definition or in SETUP stating the worked example must be carried forward? Is the rule imperative ("must be carried forward verbatim") rather than interrogative ("has it been carried forward?") or conditional ("if versioning, update")? |
| C-20 | Preservation rule imperative form | Aspirational | -- | Does the C-19 preservation rule contain a mandatory verb ("must", "shall", "is required to")? Interrogative form ("has it been carried forward?") earns C-19 PARTIAL and C-20 FAIL. Conditional form ("if versioning, update the example") also earns C-20 FAIL. Location alone does not satisfy C-20 -- form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 auto-PASS | Does the fully instantiated worked example appear specifically in the FAILURE PATTERNS action line -- not in SETUP, not in a roster column, not in a preservation checkpoint? The SETUP block may contain a C-19 preservation instruction without absorbing the instantiated example. |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Score each output

For each output in order:
1. Read the output in full before writing any verdict.
2. Produce the scoring table. Column order: **Criterion | Evidence Quote | Verdict**. Write
   evidence quote before verdict -- never reverse the order.
3. Compute the composite score using the v7 formula (N_aspirational=14). Show working.
4. Write the composite score and Golden status below the table.

**Scoring table template (21 rows, v7):**

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | | |
| C-02 Evidence quote for every verdict | | |
| C-03 Composite score computed correctly | | |
| C-04 Ranked leaderboard present | | |
| C-05 Failure patterns surfaced | | |
| C-06 Excellence signals surfaced | | |
| C-07 Regression signals surfaced | | |
| C-08 Actionable diagnosis in failure patterns | | |
| C-09 Score distribution commentary | | |
| C-10 Worked example in action line | | |
| C-11 Auto-PASS rules stated in preamble | | |
| C-12 Formula reproduced before first output section | | |
| C-13 Evidence-before-verdict ordering enforced | | |
| C-14 Per-criterion diagnostic question in roster | | |
| C-15 Preamble gate instruction present | | |
| C-16 Named standalone auto-PASS block | | |
| C-17 Criterion-specific diagnostic questions | | |
| C-18 Named standalone regression signals section | | |
| C-19 Worked-example carryforward preservation instruction | | |
| C-20 Preservation rule imperative form | | |
| C-21 Worked example FAILURE PATTERNS location lock | | |

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations visible in the scored outputs. Placeholders such as [artifact name],
[section], or [add here] are not permitted.

**Phase 2 STOP CONDITION:** Do not begin Phase 3 until all outputs have been scored. Do not
proceed to Phase 3 if any output's scoring table is incomplete.

---

### PHASE 3 -- Cross-output analysis

After scoring all outputs, write the following sections in order.

#### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output, write:
- Pattern name
- Observed in: [list of outputs]
- Root cause hypothesis
- Action: [fully instantiated action line with verb + real artifact filename + section location]

Example of a fully instantiated action line: "Add a 'Score distribution note:' instruction
to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max
score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty)
or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run."

If no criterion fails universally: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS.
C-10 auto-PASS. C-21 auto-PASS.**

#### REGRESSION SIGNALS

Write this section in all cases. Populate with structured rows when prior-round scorecard data
is provided.

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|---------------|-----------------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided. Section present
but not applicable.**

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier
(PASS vs. PARTIAL or PARTIAL vs. FAIL), write:
- Criterion and output name
- What the output did differently

If no differentials: "No differentials detected -- all outputs scored the same tier on all
criteria."

#### LEADERBOARD

Rank all scored outputs from highest to lowest composite score.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread).
Note that N_aspirational=14 means each aspirational criterion contributes 10/14 = 0.714 pt to
the composite; achieving composite >= 99 requires at most one aspirational FAIL.

---

## V-02

**Axis:** C-20 ablation -- C-19 preservation rule uses interrogative grammar ("Has the worked
example been carried forward verbatim?") instead of imperative ("must be carried forward
verbatim"); all other structures identical to V-01

**Hypothesis:** C-19 earns PARTIAL (preservation concept present near C-10 definition, location
satisfied, but form is interrogative -- earns location credit, not form credit). C-20 FAILs
(mandatory verb absent from the preservation rule). Net cost vs. V-01: -0.357 pt (C-19
PARTIAL) + -0.714 pt (C-20 FAIL) = -1.071 pt. Predicted composite: 98.93.

---

Score N skill outputs against the supplied rubric. Produce a per-criterion verdict matrix,
composite scores, and cross-output analysis sections.

---

### PHASE 1 -- Setup before scoring any output

Do not open any output file until PHASE 1 is fully written.

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output.
**C-07 auto-PASS** when no prior-round scorecard is provided.
**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Carryforward Check:** Has the worked example in the FAILURE PATTERNS
action line been carried forward verbatim from the prior round, or updated to reflect the
current round's new axis criterion? If the worked example has been replaced with a format
instruction placeholder, restore it before proceeding.

**STOP-1.** Do not proceed to Step 1.2 until all five auto-PASS declarations are written.

#### Step 1.2 -- Composite Formula (v7 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 14.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**STOP-2.** Do not proceed to Step 1.3 until the formula and evidence mandate are written.

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | -- | Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | Essential | -- | For every verdict cell, is the evidence field non-empty and verbatim from the scored output? |
| C-03 | Composite score computed correctly | Essential | -- | Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1? An output using N_aspirational=12 is a FAIL. |
| C-04 | Ranked leaderboard present | Essential | -- | Does the leaderboard contain Rank, Output, Score, and Golden columns with all scored outputs present? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Are all universally-failing criteria listed with action lines? If none fail universally, write "C-05 auto-PASS." |
| C-06 | Excellence signals surfaced | Recommended | -- | Does the section identify output-criterion pairs with at least one tier differential? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is the section present with prior/current verdict comparison columns? |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 auto-PASS | Does each failure pattern have an action line with verb + real artifact + section location? |
| C-09 | Score distribution commentary | Aspirational | -- | Does the LEADERBOARD section state minimum score, maximum score, spread, and a calibration note? Are actual numeric values used? |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 auto-PASS | Does at least one FAILURE PATTERNS action line contain a fully instantiated example with a real artifact name and section path? |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | -- | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) in the SETUP block with criterion ID and trigger phrase? |
| C-12 | Formula reproduced before first output section | Aspirational | -- | Does the formula with N_aspirational=14 appear in SETUP before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | -- | Is there an explicit written mandate requiring evidence quote before verdict, with a prohibition on reversal? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | -- | Is a Diagnostic Question column present? Do all 21 rows have non-empty questions? |
| C-15 | Preamble gate instruction present | Aspirational | -- | Does an imperative gate statement appear at or near the end of the SETUP block? |
| C-16 | Named standalone auto-PASS block | Aspirational | -- | Are the auto-PASS conditions in a dedicated named block, not embedded in roster columns? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | -- | Do at least three questions name criterion-specific mechanisms (count, N-value, form distinction, location check)? |
| C-18 | Named standalone regression signals section | Aspirational | -- | Is a named "REGRESSION SIGNALS" section in the template body with prior/current verdict columns? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | -- | Is there a statement near the C-10 definition or in SETUP addressing carryforward of the worked example? Does it address the condition when the rubric is versioned forward? |
| C-20 | Preservation rule imperative form | Aspirational | -- | Does the preservation statement use a mandatory verb ("must", "shall", "is required to")? Interrogative form ("has it been carried forward?") earns C-19 PARTIAL + C-20 FAIL. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 auto-PASS | Does the instantiated worked example appear in the FAILURE PATTERNS action line, not only in SETUP or a roster column? |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Score each output

For each output in order:
1. Read the output in full before writing any verdict.
2. Produce the scoring table. Column order: **Criterion | Evidence Quote | Verdict**. Write
   evidence quote before verdict -- never reverse the order.
3. Compute the composite score using the v7 formula (N_aspirational=14). Show working.
4. Write the composite score and Golden status below the table.

**Scoring table template (21 rows, v7):**

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | | |
| C-02 Evidence quote for every verdict | | |
| C-03 Composite score computed correctly | | |
| C-04 Ranked leaderboard present | | |
| C-05 Failure patterns surfaced | | |
| C-06 Excellence signals surfaced | | |
| C-07 Regression signals surfaced | | |
| C-08 Actionable diagnosis in failure patterns | | |
| C-09 Score distribution commentary | | |
| C-10 Worked example in action line | | |
| C-11 Auto-PASS rules stated in preamble | | |
| C-12 Formula reproduced before first output section | | |
| C-13 Evidence-before-verdict ordering enforced | | |
| C-14 Per-criterion diagnostic question in roster | | |
| C-15 Preamble gate instruction present | | |
| C-16 Named standalone auto-PASS block | | |
| C-17 Criterion-specific diagnostic questions | | |
| C-18 Named standalone regression signals section | | |
| C-19 Worked-example carryforward preservation instruction | | |
| C-20 Preservation rule imperative form | | |
| C-21 Worked example FAILURE PATTERNS location lock | | |

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholders such as [artifact name] or [section] are not permitted.

**Phase 2 STOP CONDITION:** Do not begin Phase 3 until all outputs have been scored.

---

### PHASE 3 -- Cross-output analysis

After scoring all outputs, write the following sections in order.

#### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output, write:
- Pattern name
- Observed in: [list of outputs]
- Root cause hypothesis
- Action: [fully instantiated action line with verb + real artifact filename + section location]

Example of a fully instantiated action line: "Add a 'Score distribution note:' instruction
to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max
score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty)
or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run."

If no criterion fails universally: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS.
C-10 auto-PASS. C-21 auto-PASS.**

#### REGRESSION SIGNALS

Write this section in all cases. Populate with structured rows when prior-round scorecard data
is provided.

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|---------------|-----------------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided. Section present
but not applicable.**

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier,
write the criterion, the output name, and what the output did differently. If no differentials:
"No differentials detected -- all outputs scored the same tier on all criteria."

#### LEADERBOARD

Rank all scored outputs from highest to lowest composite score.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread) or discriminate (>= 10 pt spread). Note that N_aspirational=14 means
each aspirational criterion contributes 10/14 = 0.714 pt to the composite.

---

## V-03

**Axis:** C-21 ablation -- worked example placed in SETUP block (Step 1.1 preservation
checkpoint) only; FAILURE PATTERNS action line contains format instruction with placeholders;
all other structures identical to V-01

**Hypothesis:** C-10 FAILs (no fully instantiated example in FAILURE PATTERNS action line --
example is only in SETUP). C-21 FAILs (instantiated example not in FAILURE PATTERNS; SETUP
is not a qualifying location per C-21). This replicates and formalizes the R6 V-03 failure
mode, now captured by an explicit criterion. Net cost vs. V-01: -0.714 pt (C-10 FAIL) +
-0.714 pt (C-21 FAIL) = -1.429 pt. Predicted composite: 98.57.

---

Score N skill outputs against the supplied rubric. Produce a per-criterion verdict matrix,
composite scores, and cross-output analysis sections.

---

### PHASE 1 -- Setup before scoring any output

Do not open any output file until PHASE 1 is fully written.

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output.
**C-07 auto-PASS** when no prior-round scorecard is provided.
**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example below must be carried forward
verbatim from the prior round, or updated to reflect the current round's new axis criterion,
whenever the rubric is versioned forward. Do not replace it with a format instruction
placeholder. This rule is in force at every rubric version change.

**Current worked example (preserved from prior round):** "Add a 'Score distribution note:'
instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min
score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration
difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run."

**STOP-1.** Do not proceed to Step 1.2 until all five auto-PASS declarations and the worked
example preservation checkpoint are written.

#### Step 1.2 -- Composite Formula (v7 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 14.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**STOP-2.** Do not proceed to Step 1.3 until the formula and evidence mandate are written.

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | -- | Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | Essential | -- | For every verdict cell, is the evidence field non-empty and verbatim from the scored output? |
| C-03 | Composite score computed correctly | Essential | -- | Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1? |
| C-04 | Ranked leaderboard present | Essential | -- | Does the leaderboard contain Rank, Output, Score, and Golden columns with all outputs present? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Are all universally-failing criteria listed with action lines? If none, write "C-05 auto-PASS." |
| C-06 | Excellence signals surfaced | Recommended | -- | Does the section identify output-criterion pairs with at least one tier differential? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is the section present with prior/current verdict columns? |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 auto-PASS | Does each failure pattern have an action line with verb + real artifact + section location? |
| C-09 | Score distribution commentary | Aspirational | -- | Does the LEADERBOARD state minimum score, maximum score, spread, and a calibration note? |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 auto-PASS | Does at least one FAILURE PATTERNS action line contain a fully instantiated example with a real artifact name and section path -- not only in SETUP? |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | -- | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) in the SETUP block with criterion ID and trigger phrase? |
| C-12 | Formula reproduced before first output section | Aspirational | -- | Does the formula with N_aspirational=14 appear in SETUP before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | -- | Is there an explicit written mandate requiring evidence quote before verdict with a prohibition on reversal? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | -- | Is a Diagnostic Question column present with non-empty questions for all 21 criterion rows? |
| C-15 | Preamble gate instruction present | Aspirational | -- | Does an imperative gate statement appear at or near the end of the SETUP block? |
| C-16 | Named standalone auto-PASS block | Aspirational | -- | Are the auto-PASS conditions in a dedicated named block? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | -- | Do at least three questions name criterion-specific mechanisms (count, N-value, form distinction, location check)? |
| C-18 | Named standalone regression signals section | Aspirational | -- | Is a named "REGRESSION SIGNALS" section in the template body with prior/current verdict columns? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | -- | Is there an explicit imperative preservation rule near the C-10 definition or in SETUP stating the worked example must be carried forward verbatim or updated? |
| C-20 | Preservation rule imperative form | Aspirational | -- | Does the preservation rule use a mandatory verb ("must", "shall", "is required to")? Interrogative or conditional form earns C-20 FAIL. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 auto-PASS | Does the instantiated worked example appear in the FAILURE PATTERNS action line -- not only in SETUP? |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Score each output

For each output in order:
1. Read the output in full before writing any verdict.
2. Produce the scoring table. Column order: **Criterion | Evidence Quote | Verdict**. Write
   evidence quote before verdict -- never reverse the order.
3. Compute the composite score using the v7 formula (N_aspirational=14). Show working.
4. Write the composite score and Golden status below the table.

**Scoring table template (21 rows, v7):**

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | | |
| C-02 Evidence quote for every verdict | | |
| C-03 Composite score computed correctly | | |
| C-04 Ranked leaderboard present | | |
| C-05 Failure patterns surfaced | | |
| C-06 Excellence signals surfaced | | |
| C-07 Regression signals surfaced | | |
| C-08 Actionable diagnosis in failure patterns | | |
| C-09 Score distribution commentary | | |
| C-10 Worked example in action line | | |
| C-11 Auto-PASS rules stated in preamble | | |
| C-12 Formula reproduced before first output section | | |
| C-13 Evidence-before-verdict ordering enforced | | |
| C-14 Per-criterion diagnostic question in roster | | |
| C-15 Preamble gate instruction present | | |
| C-16 Named standalone auto-PASS block | | |
| C-17 Criterion-specific diagnostic questions | | |
| C-18 Named standalone regression signals section | | |
| C-19 Worked-example carryforward preservation instruction | | |
| C-20 Preservation rule imperative form | | |
| C-21 Worked example FAILURE PATTERNS location lock | | |

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholders are not permitted.

**Phase 2 STOP CONDITION:** Do not begin Phase 3 until all outputs have been scored.

---

### PHASE 3 -- Cross-output analysis

After scoring all outputs, write the following sections in order.

#### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output, write:
- Pattern name
- Observed in: [list of outputs]
- Root cause hypothesis
- Action: [verb] [specific artifact filename] [section location] -- fully instantiated,
  no placeholders

If no criterion fails universally: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS.
C-10 auto-PASS. C-21 auto-PASS.**

#### REGRESSION SIGNALS

Write this section in all cases. Populate with structured rows when prior-round scorecard data
is provided.

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|---------------|-----------------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided. Section present
but not applicable.**

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier,
write the criterion, the output name, and what the output did differently. If no differentials:
"No differentials detected -- all outputs scored the same tier on all criteria."

#### LEADERBOARD

Rank all scored outputs from highest to lowest composite score.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread) or discriminate (>= 10 pt spread). Note that N_aspirational=14 means
each aspirational criterion contributes 10/14 = 0.714 pt to the composite.

---

## V-04

**Axis:** Score distribution format -- LEADERBOARD section instructs prose commentary on
score distribution rather than a structured mandate with explicit min/max/spread vocabulary;
all other structures identical to V-01

**Hypothesis:** C-09 earns PARTIAL. The prose instruction ("write a commentary paragraph on
score distribution") produces qualitative calibration language without guaranteeing minimum
score, maximum score, and spread values are explicitly stated as numbers. The rubric requires
"at least min/max/spread values" and "calibration language" -- prose instruction satisfies the
calibration language requirement but not the numeric mandate. Net cost vs. V-01: -0.357 pt
(C-09 PARTIAL). Predicted composite: 99.64.

---

Score N skill outputs against the supplied rubric. Produce a per-criterion verdict matrix,
composite scores, and cross-output analysis sections.

---

### PHASE 1 -- Setup before scoring any output

Do not open any output file until PHASE 1 is fully written.

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output.
**C-07 auto-PASS** when no prior-round scorecard is provided.
**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. This rule is in force at every rubric version
change and applies regardless of whether C-10 auto-PASS fires this run.

**STOP-1.** Do not proceed to Step 1.2 until all five auto-PASS declarations are written.

#### Step 1.2 -- Composite Formula (v7 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 14.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**STOP-2.** Do not proceed to Step 1.3 until the formula and evidence mandate are written.

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | -- | Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated? |
| C-02 | Evidence quote for every verdict | Essential | -- | For every verdict cell, is the evidence field non-empty and verbatim from the scored output? |
| C-03 | Composite score computed correctly | Essential | -- | Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1? |
| C-04 | Ranked leaderboard present | Essential | -- | Does the leaderboard contain Rank, Output, Score, and Golden columns with all outputs present? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Are all universally-failing criteria listed with action lines? If none, write "C-05 auto-PASS." |
| C-06 | Excellence signals surfaced | Recommended | -- | Does the section identify output-criterion pairs with at least one tier differential? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is the section present with prior/current verdict columns? |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 auto-PASS | Does each failure pattern have an action line with verb + real artifact + section location? |
| C-09 | Score distribution commentary | Aspirational | -- | Does the LEADERBOARD include a score distribution commentary? Does it state numeric values for minimum score, maximum score, and spread -- not qualitative description only? |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 auto-PASS | Does at least one FAILURE PATTERNS action line contain a fully instantiated example with a real artifact name and section path? |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | -- | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) in the SETUP block with criterion ID and trigger phrase? |
| C-12 | Formula reproduced before first output section | Aspirational | -- | Does the formula with N_aspirational=14 appear in SETUP before any per-output heading? |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | -- | Is there an explicit written mandate requiring evidence quote before verdict with a prohibition on reversal? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | -- | Is a Diagnostic Question column present with non-empty questions for all 21 criterion rows? |
| C-15 | Preamble gate instruction present | Aspirational | -- | Does an imperative gate statement appear at or near the end of the SETUP block? |
| C-16 | Named standalone auto-PASS block | Aspirational | -- | Are the auto-PASS conditions in a dedicated named block? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | -- | Do at least three questions name criterion-specific mechanisms (count, N-value, form distinction, location check)? |
| C-18 | Named standalone regression signals section | Aspirational | -- | Is a named "REGRESSION SIGNALS" section in the template body with prior/current verdict columns? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | -- | Is there an explicit imperative preservation rule near the C-10 definition or in SETUP? |
| C-20 | Preservation rule imperative form | Aspirational | -- | Does the preservation rule use a mandatory verb ("must", "shall", "is required to")? |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 auto-PASS | Does the instantiated worked example appear in the FAILURE PATTERNS action line -- not only in SETUP? |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Score each output

For each output in order:
1. Read the output in full before writing any verdict.
2. Produce the scoring table. Column order: **Criterion | Evidence Quote | Verdict**. Write
   evidence quote before verdict -- never reverse the order.
3. Compute the composite score using the v7 formula (N_aspirational=14). Show working.
4. Write the composite score and Golden status below the table.

**Scoring table template (21 rows, v7):**

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | | |
| C-02 Evidence quote for every verdict | | |
| C-03 Composite score computed correctly | | |
| C-04 Ranked leaderboard present | | |
| C-05 Failure patterns surfaced | | |
| C-06 Excellence signals surfaced | | |
| C-07 Regression signals surfaced | | |
| C-08 Actionable diagnosis in failure patterns | | |
| C-09 Score distribution commentary | | |
| C-10 Worked example in action line | | |
| C-11 Auto-PASS rules stated in preamble | | |
| C-12 Formula reproduced before first output section | | |
| C-13 Evidence-before-verdict ordering enforced | | |
| C-14 Per-criterion diagnostic question in roster | | |
| C-15 Preamble gate instruction present | | |
| C-16 Named standalone auto-PASS block | | |
| C-17 Criterion-specific diagnostic questions | | |
| C-18 Named standalone regression signals section | | |
| C-19 Worked-example carryforward preservation instruction | | |
| C-20 Preservation rule imperative form | | |
| C-21 Worked example FAILURE PATTERNS location lock | | |

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations. Placeholders are not permitted.

**Phase 2 STOP CONDITION:** Do not begin Phase 3 until all outputs have been scored.

---

### PHASE 3 -- Cross-output analysis

After scoring all outputs, write the following sections in order.

#### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output, write:
- Pattern name
- Observed in: [list of outputs]
- Root cause hypothesis
- Action: [fully instantiated action line with verb + real artifact filename + section location]

Example of a fully instantiated action line: "Add a 'Score distribution note:' instruction
to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max
score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty)
or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run."

If no criterion fails universally: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS.
C-10 auto-PASS. C-21 auto-PASS.**

#### REGRESSION SIGNALS

Write this section in all cases. Populate with structured rows when prior-round scorecard data
is provided.

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|---------------|-----------------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided. Section present
but not applicable.**

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier,
write the criterion, the output name, and what the output did differently. If no differentials:
"No differentials detected -- all outputs scored the same tier on all criteria."

#### LEADERBOARD

Rank all scored outputs from highest to lowest composite score.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

After the rank table, write a commentary paragraph describing the score distribution across
all scored outputs: how tightly or loosely the scores cluster, what the spread indicates about
rubric discriminability, and any notable calibration observations.

---

## V-05

**Axis:** Combination pass -- V-01 baseline + C-21 location lock named explicitly in C-10
Preservation Rule + C-21 named in standalone Auto-PASS block + per-criterion aspirational
weight (0.714 pt) stated in score distribution note + C-20 diagnostic question explicitly
enumerates all three verb-form patterns (imperative/interrogative/conditional)

**Hypothesis:** All 21 criteria PASS. C-20 diagnostic question explicitly names the three
distinguishable verb-form patterns, reducing boundary-case ambiguity and strengthening C-17
(criterion-specific diagnostic question for C-20). C-21 earns PASS due to the explicit
FAILURE PATTERNS location lock instruction in the C-10 Preservation Rule. C-09 earns PASS
due to the explicit per-criterion weight (0.714 pt) in the score distribution note. The
combination of these targeted additions is predicted to achieve the same 100.00 as V-01
while providing additional structural specificity on the two new R7 criteria. Composite =
100.00. Prediction: V-01 and V-05 both score 100.00; V-05 excellence signal on C-17 if
scored individually.

---

Score N skill outputs against the supplied rubric. Produce a per-criterion verdict matrix,
composite scores, and cross-output analysis sections.

---

### PHASE 1 -- Setup before scoring any output

Do not open any output file until PHASE 1 is fully written.

#### Step 1.1 -- Auto-PASS Conditions

**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output.
**C-07 auto-PASS** when no prior-round scorecard is provided.
**C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).
**C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires).

**C-10 Worked-Example Preservation Rule:** The worked example in the FAILURE PATTERNS action
line must be carried forward verbatim from the prior round, or updated to reflect the current
round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked
example with a format instruction placeholder. The worked example must remain in the FAILURE
PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a
preservation checkpoint. The SETUP block may contain this C-19 preservation rule for C-19/C-20
compliance purposes without absorbing the instantiated example. This rule is in force at every
rubric version change and applies regardless of whether C-10 auto-PASS fires this run.

**STOP-1.** Do not proceed to Step 1.2 until all five auto-PASS declarations and the C-10
Preservation Rule are written.

#### Step 1.2 -- Composite Formula (v7 N values)

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 14.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Evidence-ordering mandate:** In every scoring table, column order is Criterion | Evidence
Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict
cell completed before its evidence quote cell violates C-13.

**STOP-2.** Do not proceed to Step 1.3 until the formula and evidence mandate are written.

#### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

| ID | Name | Tier | Auto-PASS Status | Diagnostic Question |
|----|------|------|-----------------|---------------------|
| C-01 | Per-criterion verdicts present | Essential | -- | Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated? A matrix with 19 or 20 rows fails C-01 even if all other rows are present. |
| C-02 | Evidence quote for every verdict | Essential | -- | For the hardest-to-quote criterion this run (likely C-19 or C-20), is the evidence cell non-empty and verbatim from the scored output -- not a fabricated summary or template slot? |
| C-03 | Composite score computed correctly | Essential | -- | Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1? An output using N_aspirational=12 (v6) is a C-03 FAIL regardless of other scores. |
| C-04 | Ranked leaderboard present | Essential | -- | Does the leaderboard contain exactly four columns (Rank, Output, Score, Golden) and include all scored outputs? |
| C-05 | Failure patterns surfaced | Recommended | auto-PASS when no universal failures | Are all criteria with universal FAIL/PARTIAL listed, each with an action line? If no criterion fails universally, write "C-05 auto-PASS." |
| C-06 | Excellence signals surfaced | Recommended | -- | Does the section identify at least one output-criterion pair where one output outperforms by >= one tier? Is a "no differentials" note written if none exist? |
| C-07 | Regression signals surfaced | Recommended | auto-PASS when no prior-round data | Is the section present with prior/current verdict comparison columns? If no prior data, write "C-07 auto-PASS." |
| C-08 | Actionable diagnosis in failure patterns | Aspirational | auto-PASS when C-05 auto-PASS | Does each failure pattern entry include an action line with verb + real artifact filename + section location? No format placeholders. |
| C-09 | Score distribution commentary | Aspirational | -- | Does the LEADERBOARD section state minimum score, maximum score, and spread as numeric values? Does it include a calibration note distinguishing clustering (< 5 pt) from discrimination (>= 10 pt) and stating the per-criterion aspirational weight (10/14 = 0.714 pt)? |
| C-10 | Worked example in action line | Aspirational | auto-PASS when C-05 auto-PASS | Does at least one FAILURE PATTERNS action line contain a fully instantiated example with a real artifact name and exact section path -- not in SETUP, not in a roster row, not in a preservation checkpoint? |
| C-11 | Auto-PASS rules stated in preamble | Aspirational | -- | Are all five auto-PASS declarations (C-05, C-07, C-08, C-10, C-21) present in the SETUP block, each naming the criterion ID and trigger phrase? |
| C-12 | Formula reproduced before first output section | Aspirational | -- | Does the formula with N_aspirational=14 appear in SETUP before any per-output heading? A formula with N_aspirational=12 is a FAIL. |
| C-13 | Evidence-before-verdict ordering enforced | Aspirational | -- | Is there an explicit written mandate in the template requiring evidence quote before verdict in every cell, with a stated prohibition on reversal? |
| C-14 | Per-criterion diagnostic question in roster | Aspirational | -- | Is a Diagnostic Question column present in the criterion roster? Do all 21 criterion rows (C-01 through C-21) have non-empty questions? |
| C-15 | Preamble gate instruction present | Aspirational | -- | Does an imperative gate statement (e.g., "Do not open any output file until SETUP is fully written") appear at or near the end of the SETUP block? |
| C-16 | Named standalone auto-PASS block | Aspirational | -- | Are the auto-PASS conditions in a dedicated named block, not embedded in roster columns? Does each declaration name the criterion ID and trigger phrase explicitly? |
| C-17 | Criterion-specific diagnostic questions | Aspirational | -- | Do at least three questions name the specific mechanism: a count (C-01), an N-value check (C-03), a form distinction (C-20: three patterns -- imperative/interrogative/conditional), or a location check (C-10/C-21: FAILURE PATTERNS vs. SETUP)? Generic questions like "Is this criterion satisfied?" do not satisfy C-17. |
| C-18 | Named standalone regression signals section | Aspirational | -- | Is a "### REGRESSION SIGNALS" section present in the template body, separate from SETUP and per-output scoring tables, with Criterion, Prior Verdict, Current Verdict, and Mechanism columns? |
| C-19 | Worked-example carryforward preservation instruction | Aspirational | -- | Is there an explicit preservation rule near the C-10 definition or in SETUP stating the worked example must be carried forward? Is the rule imperative ("must be carried forward verbatim") rather than interrogative or conditional? |
| C-20 | Preservation rule imperative form | Aspirational | -- | Does the C-19 preservation rule use a mandatory verb ("must", "shall", "is required to")? Three form patterns: (1) imperative "must be carried forward" earns C-20 PASS; (2) interrogative "has it been carried forward?" earns C-19 PARTIAL + C-20 FAIL; (3) conditional "if versioning, update the example" earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor. |
| C-21 | Worked example FAILURE PATTERNS location lock | Aspirational | auto-PASS when C-05 auto-PASS | Does the fully instantiated worked example appear specifically in the FAILURE PATTERNS action line -- not in SETUP, not in a roster column, not in a preservation checkpoint? The SETUP block may contain the C-19/C-20 preservation rule without absorbing the instantiated example. |

**STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed.**

---

### PHASE 2 -- Score each output

For each output in order:
1. Read the output in full before writing any verdict.
2. Produce the scoring table. Column order: **Criterion | Evidence Quote | Verdict**. Write
   evidence quote before verdict -- never reverse the order.
3. Compute the composite score using the v7 formula (N_aspirational=14). Show working.
4. Write the composite score and Golden status below the table.

**Scoring table template (21 rows, v7):**

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | | |
| C-02 Evidence quote for every verdict | | |
| C-03 Composite score computed correctly | | |
| C-04 Ranked leaderboard present | | |
| C-05 Failure patterns surfaced | | |
| C-06 Excellence signals surfaced | | |
| C-07 Regression signals surfaced | | |
| C-08 Actionable diagnosis in failure patterns | | |
| C-09 Score distribution commentary | | |
| C-10 Worked example in action line | | |
| C-11 Auto-PASS rules stated in preamble | | |
| C-12 Formula reproduced before first output section | | |
| C-13 Evidence-before-verdict ordering enforced | | |
| C-14 Per-criterion diagnostic question in roster | | |
| C-15 Preamble gate instruction present | | |
| C-16 Named standalone auto-PASS block | | |
| C-17 Criterion-specific diagnostic questions | | |
| C-18 Named standalone regression signals section | | |
| C-19 Worked-example carryforward preservation instruction | | |
| C-20 Preservation rule imperative form | | |
| C-21 Worked example FAILURE PATTERNS location lock | | |

**No-placeholder mandate:** All action lines in FAILURE PATTERNS must use real artifact names
and exact section locations visible in the scored outputs. Placeholders such as [artifact name],
[section], or [add here] are not permitted.

**Phase 2 STOP CONDITION:** Do not begin Phase 3 until all outputs have been scored. Do not
proceed to Phase 3 if any output's scoring table is incomplete.

---

### PHASE 3 -- Cross-output analysis

After scoring all outputs, write the following sections in order.

#### FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in every scored output, write:
- Pattern name
- Observed in: [list of outputs]
- Root cause hypothesis
- Action: [fully instantiated action line with verb + real artifact filename + section location]

Example of a fully instantiated action line: "Add a 'Score distribution note:' instruction
to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max
score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty)
or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run."

If no criterion fails universally: **C-05 auto-PASS -- no universal failures. C-08 auto-PASS.
C-10 auto-PASS. C-21 auto-PASS.**

#### REGRESSION SIGNALS

Write this section in all cases. Populate with structured rows when prior-round scorecard data
is provided.

| Criterion | Prior Verdict | Current Verdict | Mechanism |
|-----------|---------------|-----------------|-----------|

If no prior-round data: **C-07 auto-PASS -- no prior-round scorecard provided. Section present
but not applicable.**

#### EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier
(PASS vs. PARTIAL or PARTIAL vs. FAIL), write:
- Criterion and output name
- What the output did differently

If no differentials: "No differentials detected -- all outputs scored the same tier on all
criteria."

#### LEADERBOARD

Rank all scored outputs from highest to lowest composite score.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|

Score distribution note: State minimum score, maximum score, and spread. State whether scores
cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread).
Note that N_aspirational=14 means each aspirational criterion contributes 10/14 = 0.714 pt to
the composite; a single aspirational FAIL costs 0.714 pt; achieving composite >= 99 requires
at most one aspirational FAIL.
