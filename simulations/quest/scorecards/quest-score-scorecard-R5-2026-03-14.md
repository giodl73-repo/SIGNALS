Scorecard written to `simulations/quest/scorecards/quest-score-scorecard-R5-2026-03-14.md`.

**Summary:**

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-05 | 100.00 | yes |
| 2 | V-04 | 98.18 | yes |
| 3 | V-01 | 97.27 | yes |
| 4 | V-02 | 96.36 | yes |
| 4 | V-03 | 96.36 | yes |

**Key findings:**
- C-18 closed universally — all 5 variations PASS the named regression section criterion regardless of implementation approach
- C-07 improved from PARTIAL to PASS across V-01–V-04 (the primary R5 goal)
- C-10 is carryforward-fragile — regressed in V-02, V-03, V-04 when their axes shifted
- Score distribution clusters tightly (3.64 pt spread), confirming C-18 was the dominant differentiator this round

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named REGRESSION SIGNALS section is axis-independent: all 5 variations achieve C-18 PASS regardless of implementation approach (standalone section, coupling declaration, lifecycle phase, structural trinity, full synthesis)", "C-10 worked example is carryforward-fragile: regresses in 3 of 5 variations when axis focus shifts to a new structural gap, requiring explicit preservation across rounds"]}
```
ecommended = 3, N_aspirational = 11.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.

---

## SCORING

---

### OUTPUT: V-01 -- Named Standalone REGRESSION SIGNALS Section

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | Scoring table lists C-01 through C-18 with PASS/PARTIAL/FAIL for each output column -- 18-row matrix structure complete | PASS |
| C-02 Evidence quote for every verdict | "Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse." -- structure mandates non-empty quote cell before verdict cell | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 11" -- correct v5 values | PASS |
| C-04 Ranked leaderboard present | "LEADERBOARD -- Rank all outputs from highest to lowest composite score ... | Rank | Output | Score | Golden |" -- four-column ranked table present | PASS |
| C-05 Failure patterns surfaced | "FAILURE PATTERNS -- For each criterion that received FAIL or PARTIAL in every scored output" -- universal-failure detection logic in section header | PASS |
| C-06 Excellence signals surfaced | "EXCELLENCE SIGNALS -- For each output-criterion pair where one output outperforms the group by >= one tier" -- section present | PASS |
| C-07 Regression signals surfaced | "### REGRESSION SIGNALS -- Active when prior-round scorecard was provided. If C-07 auto-PASS applies, write 'C-07 auto-PASS -- no prior data provided. Section present but not applicable.'" -- explicit structured section with Criterion | Prior Verdict | Current Verdict | Mechanism columns | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [specific artifact filename] [section location] -- e.g., 'Add a named ### REGRESSION SIGNALS section to quest-score.md after the EXCELLENCE SIGNALS section, with columns for Criterion | Prior Verdict | Current Verdict | Mechanism'" -- verb + artifact + location present | PASS |
| C-09 Score distribution commentary | No score distribution note, no min/max/spread/calibration language anywhere in template | FAIL |
| C-10 Worked example in action line | "e.g., 'Add a named ### REGRESSION SIGNALS section to quest-score.md after the EXCELLENCE SIGNALS section, with columns for Criterion | Prior Verdict | Current Verdict | Mechanism'" -- fully instantiated example with real artifact name and section location | PASS |
| C-11 Auto-PASS rules stated in preamble | "C-05 auto-PASS when no criterion fails universally across all scored outputs. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS when no failure patterns exist. ... C-10 auto-PASS when no failure patterns exist." -- four conditions in preamble block | PASS |
| C-12 Formula reproduced before first output section | "### Composite Formula (v5 N values)" appears in SETUP before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "### Evidence-Ordering Mandate -- Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit written mandate | PASS |
| C-14 Per-criterion diagnostic question in roster | Roster columns are "ID | Name | Tier | Auto-PASS Status" -- no Diagnostic Question column | FAIL |
| C-15 Preamble gate instruction present | "Do not open any output file until SETUP is fully written." -- imperative gate in SETUP | PASS |
| C-16 Named standalone auto-PASS block | "### Auto-PASS Conditions" block names C-05, C-07, C-08, C-10 each with criterion ID and trigger phrase -- standalone named block, not embedded in roster | PASS |
| C-17 Criterion-specific diagnostic questions | No diagnostic question column present; C-17 unaddressed | FAIL |
| C-18 Named standalone regression signals section | "### REGRESSION SIGNALS" section present in template body after EXCELLENCE SIGNALS with columns Criterion | Prior Verdict | Current Verdict | Mechanism -- named standalone section separate from SETUP and per-output tables | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-18): (1+0+1+1+1+1+0+1+1+0+1)/11 x 10 = 8/11 x 10 = 7.27 pts
- Composite = 97.27/100
- Golden: yes -- all 4 essentials PASS, 97.27 >= 80

---

### OUTPUT: V-02 -- C-07/C-18 Coupling Declaration

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | Scoring table covers C-01 through C-18, 18-row matrix structure per template design | PASS |
| C-02 Evidence quote for every verdict | "Evidence quote precedes verdict in every cell. Never write a verdict before its evidence." -- column order enforced | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 11" -- v5 values correct | PASS |
| C-04 Ranked leaderboard present | "LEADERBOARD -- | Rank | Output | Score | Golden |" -- ranked table present | PASS |
| C-05 Failure patterns surfaced | "FAILURE PATTERNS -- For each criterion that received FAIL or PARTIAL in every scored output" -- section present | PASS |
| C-06 Excellence signals surfaced | "EXCELLENCE SIGNALS -- For each output-criterion pair where one output outperforms the group by >= one tier" -- section present | PASS |
| C-07 Regression signals surfaced | "### REGRESSION SIGNALS -- This section is mandatory when C-07 auto-PASS does NOT apply (prior scorecard was provided), per the C-07 declaration in SETUP" -- structured section with Criterion | Prior Verdict | Current Verdict | Mechanism; activated by coupling declaration | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [specific artifact] [section] -- fully instantiated, no placeholders" -- verb + artifact + location format required | PASS |
| C-09 Score distribution commentary | No score distribution note or calibration language anywhere in template | FAIL |
| C-10 Worked example in action line | "Action: [verb] [specific artifact] [section] -- fully instantiated, no placeholders" -- format instruction only; no actual worked example with real artifact name and section path | FAIL |
| C-11 Auto-PASS rules stated in preamble | "C-05 auto-PASS when no criterion fails universally. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS when no failure patterns exist. ... C-10 auto-PASS when no failure patterns exist." -- four named declarations in preamble block | PASS |
| C-12 Formula reproduced before first output section | Formula with N_aspirational=11 reproduced in SETUP before first output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence quote precedes verdict in every cell. Never write a verdict before its evidence." -- explicit written mandate in Evidence-Ordering Mandate section | PASS |
| C-14 Per-criterion diagnostic question in roster | Criterion roster has "ID | Name | Tier | Auto-PASS Status" -- no Diagnostic Question column | FAIL |
| C-15 Preamble gate instruction present | "Do not open any output file until SETUP is fully written." -- imperative gate | PASS |
| C-16 Named standalone auto-PASS block | "C-05 auto-PASS when no criterion fails universally across all scored outputs." through C-10 -- four conditions each named by criterion ID and trigger phrase in standalone block | PASS |
| C-17 Criterion-specific diagnostic questions | No diagnostic question column in roster; C-17 not addressed in this axis | FAIL |
| C-18 Named standalone regression signals section | "### REGRESSION SIGNALS" section present in template body with Criterion | Prior Verdict | Current Verdict | Mechanism columns; activated by coupling to C-07 declaration | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-18): (1+0+0+1+1+1+0+1+1+0+1)/11 x 10 = 7/11 x 10 = 6.36 pts
- Composite = 96.36/100
- Golden: yes -- all 4 essentials PASS, 96.36 >= 80

---

### OUTPUT: V-03 -- REGRESSION SIGNALS as First-Class Lifecycle Phase

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | PHASE 2 scoring table covers C-01 through C-18 with verdict cells per output -- 18-row matrix | PASS |
| C-02 Evidence quote for every verdict | "Evidence-ordering mandate: Column order in every scoring table is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse." -- mandate present in PHASE 1 | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 11" -- v5 values in Step 1.2 | PASS |
| C-04 Ranked leaderboard present | "Step 3.5 -- LEADERBOARD: | Rank | Output | Score | Golden |" -- four-column ranked table in PHASE 3 | PASS |
| C-05 Failure patterns surfaced | "Step 3.3 -- FAILURE PATTERNS -- For each criterion that received FAIL or PARTIAL in every scored output" -- section in PHASE 3 | PASS |
| C-06 Excellence signals surfaced | "Step 3.4 -- EXCELLENCE SIGNALS -- For each output-criterion pair outperforming the group by >= one tier" -- section in PHASE 3 | PASS |
| C-07 Regression signals surfaced | "Step 3.2 -- REGRESSION SIGNALS -- Mandatory when prior-round scorecard was provided (C-07 auto-PASS does not apply). Write the section in all cases." -- dedicated named step with structured table; STOP-3 gate forces completion before leaderboard | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [artifact filename] [section location] -- fully instantiated" -- verb + artifact + location format in FAILURE PATTERNS | PASS |
| C-09 Score distribution commentary | No score distribution note, min/max/spread, or calibration language in LEADERBOARD or elsewhere | FAIL |
| C-10 Worked example in action line | "Action: [verb] [artifact filename] [section location] -- fully instantiated" -- format instruction only, no actual worked example with real artifact name and section | FAIL |
| C-11 Auto-PASS rules stated in preamble | "Step 1.1 -- Auto-PASS Resolution: C-05 auto-PASS when no criterion fails universally. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS. ... C-10 auto-PASS." -- four named declarations in PHASE 1 preamble | PASS |
| C-12 Formula reproduced before first output section | "Step 1.2 -- Composite Formula (v5 N values)" appears in PHASE 1 before any output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: Column order in every scoring table is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse." -- explicit written mandate in Step 1.2 | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster" has columns "ID | Name | Tier | Auto-PASS Status" -- no Diagnostic Question column | FAIL |
| C-15 Preamble gate instruction present | "STOP-1. PHASE 1 complete. Do not open any output file until STOP-1 is passed." -- imperative STOP gate in PHASE 1 | PASS |
| C-16 Named standalone auto-PASS block | Step 1.1 is a dedicated auto-PASS resolution block naming C-05, C-07, C-08, C-10 each with criterion ID and trigger phrase -- standalone named phase | PASS |
| C-17 Criterion-specific diagnostic questions | No diagnostic question column in roster; C-17 not addressed | FAIL |
| C-18 Named standalone regression signals section | "Step 3.2 -- REGRESSION SIGNALS" in PHASE 3 with Criterion | Prior Verdict | Current Verdict | Mechanism table; gated by STOP-3; mandatory when prior data exists -- named standalone section | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-18): (1+0+0+1+1+1+0+1+1+0+1)/11 x 10 = 7/11 x 10 = 6.36 pts
- Composite = 96.36/100
- Golden: yes -- all 4 essentials PASS, 96.36 >= 80

---

### OUTPUT: V-04 -- Structural Trinity: C-18 + C-16 + C-17

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | Scoring table lists C-01 through C-18 -- 18-row complete matrix | PASS |
| C-02 Evidence quote for every verdict | "Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- mandate enforces non-empty quote cell | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 11" -- correct v5 values | PASS |
| C-04 Ranked leaderboard present | "LEADERBOARD -- | Rank | Output | Score | Golden |" -- ranked table present | PASS |
| C-05 Failure patterns surfaced | "FAILURE PATTERNS -- For each criterion receiving FAIL or PARTIAL in every scored output" -- section present | PASS |
| C-06 Excellence signals surfaced | "EXCELLENCE SIGNALS -- For each output-criterion pair outperforming the group by >= one tier" -- section present | PASS |
| C-07 Regression signals surfaced | "### REGRESSION SIGNALS -- Active when prior-round scorecard was provided. Write the section in all cases; state 'C-07 auto-PASS -- no prior data' only if auto-PASS applies." -- standalone section with structured table; active handling | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [specific artifact filename] [exact section location] -- no placeholders" -- verb + artifact + location format required | PASS |
| C-09 Score distribution commentary | No score distribution note or calibration language present | FAIL |
| C-10 Worked example in action line | "Action: [verb] [specific artifact filename] [exact section location] -- no placeholders" -- instruction only; no worked example with real artifact and section instantiated | FAIL |
| C-11 Auto-PASS rules stated in preamble | "C-05 auto-PASS when no criterion fails universally. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS. ... C-10 auto-PASS." -- four declarations in Auto-PASS Conditions preamble block | PASS |
| C-12 Formula reproduced before first output section | "### Composite Formula (v5 N values)" in SETUP before first output section | PASS |
| C-13 Evidence-before-verdict ordering enforced | "### Evidence-Ordering Mandate -- Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit mandate | PASS |
| C-14 Per-criterion diagnostic question in roster | "### Criterion Roster with Mechanism-Level Diagnostic Questions -- | ID | Name | Tier | Auto-PASS Status | Diagnostic Question |" -- 18-row roster with Diagnostic Question column for all criteria including C-18 | PASS |
| C-15 Preamble gate instruction present | "Do not open any output file until SETUP is fully written." -- imperative gate | PASS |
| C-16 Named standalone auto-PASS block | "### Auto-PASS Conditions" block names C-05, C-07, C-08, C-10 each with criterion ID and trigger phrase -- standalone block, not roster column | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 18 verdict rows (C-01 through C-18)...?" C-02: "In the row for C-18 (the hardest to quote), is the evidence cell non-empty and verbatim...?" C-03: "Does the output use N_aspirational=11? Re-derive the composite..." -- questions name the specific mechanism of each criterion | PASS |
| C-18 Named standalone regression signals section | "### REGRESSION SIGNALS" section in template body after EXCELLENCE SIGNALS with "Criterion | Prior Verdict | Current Verdict | Mechanism" -- named standalone section | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-18): (1+0+0+1+1+1+1+1+1+1+1)/11 x 10 = 9/11 x 10 = 8.18 pts
- Composite = 98.18/100
- Golden: yes -- all 4 essentials PASS, 98.18 >= 80

---

### OUTPUT: V-05 -- Full Synthesis

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | PHASE 2 scoring table rows C-01 through C-18 with verdict cells per output -- 18-row complete matrix | PASS |
| C-02 Evidence quote for every verdict | "No-placeholder mandate: All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs. Placeholders ... are not permitted." -- structural enforcement guarantees non-empty evidence cells | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 11" -- v5 values in Step 1.2 | PASS |
| C-04 Ranked leaderboard present | "LEADERBOARD -- | Rank | Output | Score | Golden |" -- ranked table in PHASE 3 | PASS |
| C-05 Failure patterns surfaced | "FAILURE PATTERNS -- For each criterion receiving FAIL or PARTIAL in every scored output ... If C-05 auto-PASS: write 'C-05 auto-PASS -- no universal failures.'" -- section with auto-PASS resolution language | PASS |
| C-06 Excellence signals surfaced | "EXCELLENCE SIGNALS -- For each output-criterion pair outperforming the group by >= one tier" -- section present in PHASE 3 | PASS |
| C-07 Regression signals surfaced | "REGRESSION SIGNALS -- Write this section in all cases. Populate with structured rows when prior data exists." with Criterion | Prior Verdict | Current Verdict | Mechanism table -- section always written; properly activated when prior data exists | PASS |
| C-08 Actionable diagnosis in failure patterns | "Example of a fully instantiated action line: 'Add a named ### REGRESSION SIGNALS section to quest-score.md after the EXCELLENCE SIGNALS section, with four columns: Criterion | Prior Verdict | Current Verdict | Mechanism -- so C-18 is satisfied on every run where prior data exists.'" -- verb + artifact + location all present | PASS |
| C-09 Score distribution commentary | "Score distribution note: State min score, max score, and spread. State whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread). Note that N_aspirational=11 reduces the per-criterion aspirational weight to 0.91 pt (vs. 1.0 pt in v4)..." -- explicit calibration commentary mandated in LEADERBOARD | PASS |
| C-10 Worked example in action line | "Example of a fully instantiated action line: 'Add a named ### REGRESSION SIGNALS section to quest-score.md after the EXCELLENCE SIGNALS section, with four columns: Criterion | Prior Verdict | Current Verdict | Mechanism -- so C-18 is satisfied on every run where prior data exists.'" -- fully instantiated real artifact name and section location | PASS |
| C-11 Auto-PASS rules stated in preamble | "Step 1.1 -- Auto-PASS Conditions: C-05 auto-PASS when no criterion fails universally. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS. ... C-10 auto-PASS." -- four named declarations with trigger phrases in PHASE 1 preamble | PASS |
| C-12 Formula reproduced before first output section | "Step 1.2 -- Formula and Evidence Mandate: composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 11 * 10)" -- reproduced in PHASE 1 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: In every scoring table, column order is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit named mandate in Step 1.2 | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions" -- 18-row roster with non-empty question for each criterion including C-18: "Is there a named ### REGRESSION SIGNALS section in the template body... with columns for Criterion | Prior Verdict | Current Verdict | Mechanism?" | PASS |
| C-15 Preamble gate instruction present | "STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed." -- imperative gate in PHASE 1; three STOP gates enforce phase sequencing | PASS |
| C-16 Named standalone auto-PASS block | Step 1.1 is dedicated auto-PASS Conditions block naming C-05, C-07, C-08, C-10 each by criterion ID with trigger phrase -- standalone named phase, not roster column or TBD placeholder | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 18 verdict rows...?" C-03: "Does the output use N_aspirational=11? Can you re-derive the composite from the 18 visible verdict values within +-1?" C-18: "Is there a named ### REGRESSION SIGNALS section in the template body...?" -- questions name the specific mechanism not generic probes | PASS |
| C-18 Named standalone regression signals section | "REGRESSION SIGNALS -- Write this section in all cases. Populate with structured rows when prior data exists. | Criterion | Prior Verdict | Current Verdict | Mechanism |" -- named standalone section in PHASE 3 body, separate from SETUP and per-output tables | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-18): 11/11 x 10 = 10.00 pts
- Composite = 100.00/100
- Golden: yes -- all 4 essentials PASS, 100.00 >= 80

---

## FAILURE PATTERNS

Resolving C-05: No criterion received FAIL or PARTIAL in every variation. V-05 passes all 18.

C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS.

Near-universal patterns (not universal; noted for signal value):

C-09 -- Score distribution commentary: V-01 FAIL, V-02 FAIL, V-03 FAIL, V-04 FAIL; V-05 PASS.
- V-01: no calibration language present anywhere in template
- V-02: no calibration language present anywhere in template
- V-03: no score distribution note in LEADERBOARD step
- V-04: no calibration language present anywhere in template
Pattern: distribution commentary only appears in full-synthesis variants that explicitly model it. Base template gap.
Action: Add a "Score distribution note" instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, and spread, and whether scores cluster or discriminate -- so C-09 is satisfied in every run.

C-10 -- Worked example in action line: V-02 FAIL, V-03 FAIL, V-04 FAIL; V-01 PASS, V-05 PASS.
- V-02: "Action: [verb] [specific artifact] [section] -- fully instantiated, no placeholders" -- format instruction, no instantiated example
- V-03: "Action: [verb] [artifact filename] [section location] -- fully instantiated" -- format instruction only
- V-04: "Action: [verb] [specific artifact filename] [exact section location] -- no placeholders" -- format instruction only
Pattern: C-10 requires a real worked example with actual artifact name and section. Three R5 variations dropped the worked example when their axis shifted. C-10 is carryforward-fragile.

---

## EXCELLENCE SIGNALS

V-05 / C-09: V-05 PASS; V-01--V-04 FAIL.
What it did differently: "Score distribution note: State min score, max score, and spread. State whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread). Note that N_aspirational=11 reduces the per-criterion aspirational weight to 0.91 pt..." -- explicit mandated callout in LEADERBOARD section.

V-04 and V-05 / C-14: PASS; V-01--V-03 FAIL.
What they did differently: Five-column roster "ID | Name | Tier | Auto-PASS Status | Diagnostic Question" with non-empty questions for all 18 criteria. V-01--V-03 used four-column rosters with no question column.

V-04 and V-05 / C-17: PASS; V-01--V-03 FAIL.
What they did differently: Questions named the specific mechanism -- "Can you count exactly 18 verdict rows?", "Does the output use N_aspirational=11? Can you re-derive...?", "Is there a named ### REGRESSION SIGNALS section...?" -- not generic presence probes.

V-01 and V-05 / C-10: PASS; V-02--V-04 FAIL.
What they did differently: V-01 had "e.g., 'Add a named ### REGRESSION SIGNALS section to quest-score.md after the EXCELLENCE SIGNALS section, with columns for Criterion | Prior Verdict | Current Verdict | Mechanism'" -- actual worked example with real artifact name. V-05 similarly instantiated. V-02--V-04 provided format instructions without instantiation.

---

## REGRESSION SIGNALS

Prior-round data provided (R4 scorecard). C-07 auto-PASS does NOT apply.

Note: R5 axis assignments differ from R4 -- V-02 changed from C-17-diagnostic-questions axis to C-07/C-18-coupling axis; V-03 changed from DECLARATIONS-phase axis to lifecycle-STOP-gate axis. Regressions below reflect axis-change consequences, not quality degradation.

| Criterion | Prior Verdict (R4) | Current Verdict (R5) | Variation | Mechanism |
|-----------|-------------------|---------------------|-----------|-----------|
| C-10 Worked example in action line | PASS | FAIL | V-02 | R5 V-02 shifted axis from C-17-diagnostic-questions to C-07/C-18 coupling -- worked example present in R4 V-02 not carried forward |
| C-14 Per-criterion diagnostic question in roster | PASS | FAIL | V-02 | R5 V-02 dropped diagnostic question column in favor of coupling declaration axis; C-14 mechanism was the old V-02 axis, now carried by V-04/V-05 |
| C-17 Criterion-specific diagnostic questions | PASS | FAIL | V-02 | Same axis-change consequence as C-14 -- mechanism-interrogating questions were the defining feature of R4 V-02; now carried by V-04/V-05 |
| C-10 Worked example in action line | PASS | FAIL | V-03 | R5 V-03 adopted STOP-gated lifecycle axis; FAILURE PATTERNS action line became format instruction without the worked example present in R4 V-03 |
| C-10 Worked example in action line | PASS | FAIL | V-04 | R5 V-04 combined C-18+C-16+C-17 but dropped the worked example from FAILURE PATTERNS -- C-10 requires an explicit instantiated model, not just a format instruction |

Improvements (PARTIAL -> PASS): C-07 for V-01, V-02, V-03, V-04 -- all now include explicit REGRESSION SIGNALS sections.
No regressions for V-01 or V-05.

---

## LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-05 | 100.00 | yes |
| 2 | V-04 | 98.18 | yes |
| 3 | V-01 | 97.27 | yes |
| 4 | V-02 | 96.36 | yes |
| 4 | V-03 | 96.36 | yes |

Ties broken by essential-tier score (all equal: 60.0), then recommended-tier score (all equal: 30.0). V-02 and V-03 are a true tie at rank 4.

Score distribution: min = 96.36, max = 100.00, spread = 3.64 -- scores cluster tightly (< 5 pt spread). All 5 variations satisfy C-18, so the C-18 gap from R4 is closed. Remaining spread is driven by C-09, C-10, C-14, C-17. N_aspirational=11 means each aspirational criterion costs 0.91 pt; the 3-criterion gap between V-01 and V-05 costs 2.73 pts. Golden floor at 96.36 is well above the 80 threshold.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["Named REGRESSION SIGNALS section is axis-independent: all 5 variations achieve C-18 PASS regardless of implementation approach (standalone section, coupling declaration, lifecycle phase, structural trinity, full synthesis)", "C-10 worked example is carryforward-fragile: regresses in 3 of 5 variations when axis focus shifts to a new structural gap, requiring explicit preservation across rounds"]}
```
