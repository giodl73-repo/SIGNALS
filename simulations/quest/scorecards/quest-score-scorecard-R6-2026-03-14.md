**Summary:**

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-05 | 100.00 | yes |
| 2 | V-04 | 99.17 | yes |
| 3 | V-02 | 98.75 | yes |
| 4 | V-01 | 97.50 | yes |
| 5 | V-03 | 96.67 | yes |

**Key findings:**

- **C-19 form test resolved.** Both V-01 (passive sentence) and V-03 (STOP gate) earn C-19 PASS. V-02 (interrogative in C-10 diagnostic) earns C-19 PARTIAL. Location alone is not enough — the rule must be imperative, not interrogative.
- **C-19 enforcement mode test.** Both enforcement approaches (passive imperative vs. active STOP gate) score identically on C-19. Only form matters.
- **C-10 is STOP-gate-fragile.** V-03's lifecycle emphasis migrated the worked example from FAILURE PATTERNS into Step 1.4 (SETUP checkpoint). The FAILURE PATTERNS action line had only a format instruction — C-10 FAIL per-output (mitigated at round level by C-05 auto-PASS cascade). V-03 scores 96.67, not the predicted 97.50.
- **V-02 surpasses V-01** despite C-19 PARTIAL: adding C-14 and C-17 PASS (+2.0 pts aspirational) outweighs the C-19 shortfall (−0.417 pt). Net: +1.25 pts.
- Spread = 3.33 pts (tighter than R5's 3.64). C-09 remains the only near-universal gap.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-19 PASS requires imperative form ('must be carried forward verbatim') placed near the C-10 definition or in the SETUP block; interrogative form ('has it been carried forward?') in the same location earns only PARTIAL -- form is the deciding factor, not location", "C-10 is STOP-gate-fragile: V-03's lifecycle emphasis relocated the worked example from FAILURE PATTERNS into the SETUP preservation checkpoint (Step 1.4), causing a per-output C-10 FAIL -- the worked example must remain specifically in the FAILURE PATTERNS action line to satisfy C-10"]}
```
lone Preservation Rule

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "For each output, produce a scoring table with 19 rows (C-01 through C-19)" -- 19-row matrix template, all criteria listed | PASS |
| C-02 Evidence quote for every verdict | "Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- non-empty quote mandated before every verdict | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 12" -- correct v6 values | PASS |
| C-04 Ranked leaderboard present | "### LEADERBOARD -- Rank all outputs from highest to lowest composite score: | Rank | Output | Score | Golden |" -- four-column ranked table | PASS |
| C-05 Failure patterns surfaced | "### FAILURE PATTERNS -- For each criterion that received FAIL or PARTIAL in every scored output" -- section with universal-failure detection logic | PASS |
| C-06 Excellence signals surfaced | "### EXCELLENCE SIGNALS -- For each output-criterion pair where one output outperforms the group by >= one tier" -- section present | PASS |
| C-07 Regression signals surfaced | "### REGRESSION SIGNALS -- Active when prior-round scorecard was provided. If C-07 auto-PASS applies, write 'C-07 auto-PASS -- no prior data provided. Section present but not applicable.'" -- structured section with prior/current verdict columns | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [specific artifact filename] [section location] -- e.g., 'Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block immediately after the C-10 auto-PASS declaration...'" -- verb + artifact + location with instantiated example | PASS |
| C-09 Score distribution commentary | No score distribution note, no min/max/spread/calibration language anywhere in template | FAIL |
| C-10 Worked example in action line | "e.g., 'Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block immediately after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated to reflect the current round's axis criterion when the rubric is versioned forward -- so C-19 is satisfied on every versioning run.'" -- fully instantiated: real artifact name and section location in FAILURE PATTERNS | PASS |
| C-11 Auto-PASS rules stated in preamble | "C-05 auto-PASS when no criterion fails universally across all scored outputs. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS when no failure patterns exist. ... C-10 auto-PASS when no failure patterns exist." -- four named declarations with trigger phrases in SETUP block | PASS |
| C-12 Formula reproduced before first output section | "### Composite Formula (v6 N values): composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) -- N_aspirational = 12" -- reproduced in SETUP before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit written mandate in Evidence-Ordering Mandate section | PASS |
| C-14 Per-criterion diagnostic question in roster | Criterion Roster columns are "ID | Name | Tier | Auto-PASS Status" -- four columns; no Diagnostic Question column; all 19 rows lack questions | FAIL |
| C-15 Preamble gate instruction present | "Do not open any output file until SETUP is fully written." -- imperative gate at end of SETUP | PASS |
| C-16 Named standalone auto-PASS block | "### Auto-PASS Conditions" block names C-05, C-07, C-08, C-10 each with criterion ID and trigger phrase -- standalone named block, not a roster column | PASS |
| C-17 Criterion-specific diagnostic questions | No diagnostic question column in roster; no mechanism-interrogating questions exist anywhere in template | FAIL |
| C-18 Named standalone regression signals section | "### REGRESSION SIGNALS" section in template body after EXCELLENCE SIGNALS with "Criterion | Prior Verdict | Current Verdict | Mechanism" columns -- named standalone section separate from SETUP and per-output tables | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Preservation Rule: The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. This rule is in force at every rubric version change." -- standalone imperative sentence in SETUP block immediately after C-10 auto-PASS declaration | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-19): (1+0+1+1+1+1+0+1+1+0+1+1)/12 x 10 = 9/12 x 10 = 7.50 pts
- Composite = 97.50/100
- Golden: yes -- all 4 essentials PASS, 97.50 >= 80

---

### OUTPUT: V-02 -- C-19 Embedded in C-10 Diagnostic Question

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "For each output, produce a scoring table with 19 rows (C-01 through C-19)" -- 19-row matrix template | PASS |
| C-02 Evidence quote for every verdict | "Column order in every scoring table: Criterion | Evidence Quote | Verdict. Evidence quote precedes verdict in every cell. Never write a verdict before its evidence." -- non-empty quote mandated before every verdict | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 12" -- correct v6 values | PASS |
| C-04 Ranked leaderboard present | "### LEADERBOARD -- | Rank | Output | Score | Golden |" -- four-column ranked table present | PASS |
| C-05 Failure patterns surfaced | "### FAILURE PATTERNS -- For each criterion that received FAIL or PARTIAL in every scored output" -- section present | PASS |
| C-06 Excellence signals surfaced | "### EXCELLENCE SIGNALS -- For each output-criterion pair where one output outperforms the group by >= one tier" -- section present | PASS |
| C-07 Regression signals surfaced | "### REGRESSION SIGNALS -- This section is mandatory when C-07 auto-PASS does NOT apply (prior scorecard was provided). Write 'C-07 auto-PASS -- section not applicable' if and only if the C-07 declaration resolves to auto-PASS." -- structured section with prior/current verdict columns | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [specific artifact] [section] -- fully instantiated, no placeholders -- e.g., 'Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block after the C-10 auto-PASS declaration...'" -- verb + artifact + location with instantiated example | PASS |
| C-09 Score distribution commentary | No score distribution note, no min/max/spread/calibration language anywhere in template | FAIL |
| C-10 Worked example in action line | "e.g., 'Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward -- so C-19 satisfies the imperative-rule requirement.'" -- fully instantiated example with real artifact name and section path in FAILURE PATTERNS | PASS |
| C-11 Auto-PASS rules stated in preamble | "C-05 auto-PASS when no criterion fails universally across all scored outputs. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS when no failure patterns exist. ... C-10 auto-PASS when no failure patterns exist." -- four named declarations in standalone SETUP block | PASS |
| C-12 Formula reproduced before first output section | "### Composite Formula (v6 N values): composite = ... N_aspirational = 12" -- in SETUP before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Column order in every scoring table: Criterion | Evidence Quote | Verdict. Evidence quote precedes verdict in every cell. Never write a verdict before its evidence." -- explicit written mandate in Evidence-Ordering Mandate section | PASS |
| C-14 Per-criterion diagnostic question in roster | "### Criterion Roster with Diagnostic Questions -- | ID | Name | Tier | Auto-PASS Status | Diagnostic Question |" -- 19-row roster with non-empty question for all criteria including C-19 | PASS |
| C-15 Preamble gate instruction present | "Do not open any output file until SETUP is fully written." -- imperative gate at end of SETUP | PASS |
| C-16 Named standalone auto-PASS block | "### Auto-PASS Conditions" block names C-05, C-07, C-08, C-10 each by criterion ID with trigger phrase spelled out -- standalone named block, not a roster column | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 19 verdict rows (C-01 through C-19) in the scoring table, with none missing or duplicated?" C-03: "Does the output use N_aspirational=12? Re-derive the composite from the 19 visible verdict values: does your derivation match the stated score within +-1?" C-19: "Does the C-10 diagnostic question in this roster contain an explicit statement mandating that the worked example be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward? Is the statement imperative (a rule: 'must be carried forward'), or merely interrogative (a probe: 'has it been carried forward')?" -- questions name specific mechanisms (count, N-value, form distinction) | PASS |
| C-18 Named standalone regression signals section | "### REGRESSION SIGNALS" section in template body with "Criterion | Prior Verdict | Current Verdict | Mechanism" columns -- named standalone section separate from SETUP and per-output tables | PASS |
| C-19 Worked-example carryforward preservation instruction | C-10 row: "Has the worked example been carried forward verbatim from the prior round, or updated to reflect this round's new axis criterion? A format instruction (e.g., 'Action: [verb] [artifact] [section]') without a real instantiated example does not satisfy C-10." -- preservation concept present near C-10 definition (criterion roster); location satisfies "near the C-10 definition"; form is interrogative (a probe: "has it been?") not imperative (a rule: "must be carried forward") -- explicit preservation rule not stated | PARTIAL |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-19): (1+0+1+1+1+1+1+1+1+1+1+0.5)/12 x 10 = 10.5/12 x 10 = 8.75 pts
- Composite = 98.75/100
- Golden: yes -- all 4 essentials PASS, 98.75 >= 80

---

### OUTPUT: V-03 -- C-19 as STOP-Gated Preservation Checkpoint

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "For each output, produce a scoring table with 19 rows (C-01 through C-19)" in PHASE 2 -- 19-row matrix template | PASS |
| C-02 Evidence quote for every verdict | "Evidence-ordering mandate: Column order in every scoring table is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse." -- mandate in Step 1.2 enforces non-empty quote cell | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 12" -- correct v6 values in Step 1.2 | PASS |
| C-04 Ranked leaderboard present | "Step 3.5 -- LEADERBOARD: | Rank | Output | Score | Golden |" -- four-column ranked table in PHASE 3 | PASS |
| C-05 Failure patterns surfaced | "Step 3.3 -- FAILURE PATTERNS -- For each criterion that received FAIL or PARTIAL in every scored output" -- section in PHASE 3 | PASS |
| C-06 Excellence signals surfaced | "Step 3.4 -- EXCELLENCE SIGNALS -- For each output-criterion pair outperforming the group by >= one tier" -- section in PHASE 3 | PASS |
| C-07 Regression signals surfaced | "Step 3.2 -- REGRESSION SIGNALS -- Mandatory when prior-round scorecard was provided (C-07 auto-PASS does not apply). Write the section in all cases." -- dedicated named step with structured table; STOP-3 gate forces completion | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [artifact filename] [section location] -- fully instantiated" -- format requiring verb + artifact + location present in Step 3.3 | PASS |
| C-09 Score distribution commentary | No score distribution note, no min/max/spread/calibration language in LEADERBOARD step or elsewhere | FAIL |
| C-10 Worked example in action line | Step 3.3 FAILURE PATTERNS: "Action: [verb] [artifact filename] [section location] -- fully instantiated" -- format instruction only; instantiated example ("e.g., 'Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md...'") appears only in Step 1.4 (SETUP preservation checkpoint), not in FAILURE PATTERNS action line | FAIL |
| C-11 Auto-PASS rules stated in preamble | "Step 1.1 -- Auto-PASS Resolution: C-05 auto-PASS when no criterion fails universally. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS when no failure patterns exist. ... C-10 auto-PASS when no failure patterns exist." -- four named declarations with trigger phrases in PHASE 1 | PASS |
| C-12 Formula reproduced before first output section | "Step 1.2 -- Composite Formula (v6 N values): composite = ... N_aspirational = 12" -- reproduced in PHASE 1 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: Column order in every scoring table is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse." -- explicit written mandate in Step 1.2 | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster -- | ID | Name | Tier | Auto-PASS Status |" -- four-column roster; no Diagnostic Question column; all 19 rows lack questions | FAIL |
| C-15 Preamble gate instruction present | "STOP-1. Roster complete. Do not open any output file until STOP-1 is passed." -- imperative STOP gate in PHASE 1; reinforced by STOP-PRESERVATION, STOP-2, STOP-3 | PASS |
| C-16 Named standalone auto-PASS block | "Step 1.1 -- Auto-PASS Resolution" is a dedicated block naming C-05, C-07, C-08, C-10 each with criterion ID and trigger phrase -- standalone named phase, not a roster column | PASS |
| C-17 Criterion-specific diagnostic questions | No diagnostic question column in roster; Step 1.3 has ID/Name/Tier/Auto-PASS Status columns only -- no mechanism-interrogating questions exist | FAIL |
| C-18 Named standalone regression signals section | "Step 3.2 -- REGRESSION SIGNALS" in PHASE 3 with "Criterion | Prior Verdict | Current Verdict | Mechanism" table; mandatory when prior data exists -- named standalone step separate from SETUP and per-output tables | PASS |
| C-19 Worked-example carryforward preservation instruction | "STOP-PRESERVATION. Before proceeding to PHASE 2 (SCORING): write the C-10 worked example below. If the rubric has been versioned since the last run (i.e., a new axis criterion was added), update the example to reflect this round's structural gap. Do not replace the example with a format instruction placeholder. The worked example must name a real artifact filename and a real section location." -- imperative rule in PHASE 1 Step 1.4; states what must happen when rubric is versioned forward | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-19): (1+0+0+1+1+1+0+1+1+0+1+1)/12 x 10 = 8/12 x 10 = 6.67 pts
- Composite = 96.67/100
- Golden: yes -- all 4 essentials PASS, 96.67 >= 80

---

### OUTPUT: V-04 -- Structural Quadruple: C-19 + C-18 + C-17 + C-16

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "For each output, produce a scoring table with 19 rows (C-01 through C-19)" -- 19-row complete matrix template | PASS |
| C-02 Evidence quote for every verdict | "Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- non-empty quote cell mandated | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 12" -- correct v6 values | PASS |
| C-04 Ranked leaderboard present | "### LEADERBOARD -- | Rank | Output | Score | Golden |" -- ranked table present | PASS |
| C-05 Failure patterns surfaced | "### FAILURE PATTERNS -- For each criterion receiving FAIL or PARTIAL in every scored output" -- section present | PASS |
| C-06 Excellence signals surfaced | "### EXCELLENCE SIGNALS -- For each output-criterion pair outperforming the group by >= one tier" -- section present | PASS |
| C-07 Regression signals surfaced | "### REGRESSION SIGNALS -- Active when prior-round scorecard was provided. Write the section in all cases; state 'C-07 auto-PASS -- no prior data' only if auto-PASS applies." -- standalone section with structured table; mandatory activation | PASS |
| C-08 Actionable diagnosis in failure patterns | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- verb + artifact + location all present | PASS |
| C-09 Score distribution commentary | No score distribution note or calibration language present in LEADERBOARD or elsewhere | FAIL |
| C-10 Worked example in action line | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- fully instantiated: real artifact name (quest-score.md), real section (LEADERBOARD section), real purpose clause | PASS |
| C-11 Auto-PASS rules stated in preamble | "C-05 auto-PASS when no criterion fails universally across all scored outputs. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS when no failure patterns exist. ... C-10 auto-PASS when no failure patterns exist." -- four declarations in Auto-PASS Conditions block | PASS |
| C-12 Formula reproduced before first output section | "### Composite Formula (v6 N values): composite = ... N_aspirational = 12" -- in SETUP before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "### Evidence-Ordering Mandate -- Column order in every scoring table: Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit named mandate | PASS |
| C-14 Per-criterion diagnostic question in roster | "### Criterion Roster with Mechanism-Level Diagnostic Questions -- | ID | Name | Tier | Auto-PASS Status | Diagnostic Question |" -- 19-row roster with non-empty question for all criteria including C-19 | PASS |
| C-15 Preamble gate instruction present | "Do not open any output file until SETUP is fully written." -- imperative gate | PASS |
| C-16 Named standalone auto-PASS block | "### Auto-PASS Conditions" block names C-05, C-07, C-08, C-10 each with criterion ID and trigger phrase -- standalone block, not a roster column | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 19 verdict rows (C-01 through C-19) in the scoring table, with none missing or duplicated?" C-02: "For the hardest-to-quote criterion this run (likely C-19 -- the preservation rule), is the evidence cell non-empty and verbatim from the scored output -- not a fabricated summary or template slot?" C-19: "Is there a standalone imperative preservation rule (not just a diagnostic question) in the SETUP block or near the C-10 definition, stating that the worked example must be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward?" -- questions name specific mechanisms (count, hardest-to-quote case, standalone vs. diagnostic distinction) | PASS |
| C-18 Named standalone regression signals section | "### REGRESSION SIGNALS" section in template body after EXCELLENCE SIGNALS with "Criterion | Prior Verdict | Current Verdict | Mechanism" -- named standalone section | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Preservation Rule: The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the example with a format instruction placeholder. This rule is in force at every rubric version change." -- standalone imperative sentence in SETUP block immediately after C-10 auto-PASS declaration | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-19): (1+0+1+1+1+1+1+1+1+1+1+1)/12 x 10 = 11/12 x 10 = 9.17 pts
- Composite = 99.17/100
- Golden: yes -- all 4 essentials PASS, 99.17 >= 80

---

### OUTPUT: V-05 -- Full Synthesis

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "For each output, produce a scoring table with 19 rows (C-01 through C-19)" in PHASE 2 -- 19-row complete matrix | PASS |
| C-02 Evidence quote for every verdict | "No-placeholder mandate: All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs. Placeholders such as [artifact name], [section], or [add here] are not permitted." -- structural enforcement guarantees non-empty evidence cells | PASS |
| C-03 Composite score computed correctly | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) -- N_essential = 4, N_recommended = 3, N_aspirational = 12" -- correct v6 values in Step 1.2 | PASS |
| C-04 Ranked leaderboard present | "LEADERBOARD -- | Rank | Output | Score | Golden |" -- four-column ranked table in PHASE 3 | PASS |
| C-05 Failure patterns surfaced | "FAILURE PATTERNS -- For each criterion receiving FAIL or PARTIAL in every scored output ... If C-05 auto-PASS: write 'C-05 auto-PASS -- no universal failures.'" -- section with auto-PASS resolution language | PASS |
| C-06 Excellence signals surfaced | "EXCELLENCE SIGNALS -- For each output-criterion pair outperforming the group by >= one tier" -- section present in PHASE 3 | PASS |
| C-07 Regression signals surfaced | "REGRESSION SIGNALS -- Write this section in all cases. Populate with structured rows when prior data exists." with "Criterion | Prior Verdict | Current Verdict | Mechanism" table -- always written; activated when prior data exists | PASS |
| C-08 Actionable diagnosis in failure patterns | "Example of a fully instantiated action line: 'Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated for the current round's new axis criterion when the rubric is versioned forward -- so C-19 is satisfied on every versioning run.'" -- verb + artifact + location all present | PASS |
| C-09 Score distribution commentary | "Score distribution note: State min score, max score, and spread. State whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread). Note that N_aspirational=12 reduces the per-criterion aspirational weight to 0.833 pt (vs. 0.909 pt in v5), meaning a single aspirational FAIL now costs slightly less -- but achieving composite >= 99 requires at most one aspirational FAIL." -- explicit mandated calibration note in LEADERBOARD section | PASS |
| C-10 Worked example in action line | "Example of a fully instantiated action line: 'Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated for the current round's new axis criterion when the rubric is versioned forward -- so C-19 is satisfied on every versioning run.'" -- fully instantiated with real artifact name and section location | PASS |
| C-11 Auto-PASS rules stated in preamble | "Step 1.1 -- Auto-PASS Conditions: C-05 auto-PASS when no criterion fails universally. ... C-07 auto-PASS when no prior-round scorecard is provided. ... C-08 auto-PASS when no failure patterns exist. ... C-10 auto-PASS when no failure patterns exist." -- four named declarations with trigger phrases in PHASE 1 | PASS |
| C-12 Formula reproduced before first output section | "Step 1.2 -- Formula and Evidence Mandate: composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10) -- N_aspirational = 12" -- reproduced in PHASE 1 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: In every scoring table, column order is Criterion | Evidence Quote | Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit named mandate in Step 1.2 | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions -- | ID | Name | Tier | Auto-PASS Status | Diagnostic Question |" -- 19-row roster with non-empty question for all criteria including C-19 | PASS |
| C-15 Preamble gate instruction present | "STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed." -- imperative gate; three STOP declarations enforce phase sequencing | PASS |
| C-16 Named standalone auto-PASS block | "Step 1.1 -- Auto-PASS Conditions" is a dedicated block naming C-05, C-07, C-08, C-10 each by criterion ID with trigger phrase spelled out -- standalone named phase, not a roster column | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 19 verdict rows (C-01 through C-19) in the scoring table, with none missing or duplicated?" C-03: "Does the output use N_aspirational=12? Can you re-derive the composite from the 19 visible verdict values within +-1?" C-19: "Is there a standalone imperative preservation rule in PHASE 1 (near the C-10 auto-PASS declaration or the C-10 roster row) stating that the worked example must be carried forward verbatim or updated for the current round's axis when the rubric is versioned forward? Is it a rule (imperative: 'must be carried forward'), not merely an interrogative probe?" -- all 19 questions name specific mechanism (count, N-value, verbatim carryforward, imperative/interrogative form distinction) | PASS |
| C-18 Named standalone regression signals section | "REGRESSION SIGNALS -- Write this section in all cases. Populate with structured rows when prior data exists. | Criterion | Prior Verdict | Current Verdict | Mechanism |" -- named standalone section in PHASE 3 body, separate from SETUP and per-output tables | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Preservation Rule: The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. This rule is in force at every rubric version change and applies regardless of whether C-10 auto-PASS fires this run." -- standalone imperative rule in PHASE 1 Step 1.1, near C-10 auto-PASS declaration | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-19): 12/12 x 10 = 10.00 pts
- Composite = 100.00/100
- Golden: yes -- all 4 essentials PASS, 100.00 >= 80

---

## FAILURE PATTERNS

Resolving C-05: C-09 FAILS in V-01, V-02, V-03, V-04; PASSES in V-05. C-10 FAILS in V-03 only. C-14 FAILS in V-01, V-03. C-17 FAILS in V-01, V-03. No criterion FAILS in all 5 outputs.

**C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS.**

Near-universal pattern (4 of 5 FAIL; noted for signal value):

C-09 -- Score distribution commentary: V-01 FAIL, V-02 FAIL, V-03 FAIL, V-04 FAIL; V-05 PASS.
Pattern: Score distribution commentary only appears in full-synthesis variants that explicitly inherit it; the base LEADERBOARD template is a rank table only -- the calibration note must be explicitly modeled.

---

## EXCELLENCE SIGNALS

**V-05 / C-09:** V-05 PASS; V-01, V-02, V-03, V-04 FAIL -- one tier above all others.
What it did differently: "Score distribution note: State min score, max score, and spread. State whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread). Note that N_aspirational=12 reduces the per-criterion aspirational weight to 0.833 pt (vs. 0.909 pt in v5)..." -- explicit mandated calibration instruction in LEADERBOARD section inherited from R5 V-05 and updated for v6 N values.

**V-01, V-03, V-04, V-05 / C-19 (vs V-02):** Four of five PASS; V-02 PARTIAL -- imperative form outperforms interrogative form by one tier.
What they did differently: All four used an explicit imperative statement ("The worked example ... must be carried forward verbatim") rather than V-02's interrogative probe ("Has the worked example been carried forward verbatim...?"). The distinction confirms C-19 requires a rule that states what must be done, not a question that probes whether it was done.

---

## REGRESSION SIGNALS

Prior-round scorecard provided (R5). C-07 auto-PASS does NOT apply.

Note: R5 and R6 variations have different axes (R5 tested C-18; R6 tests C-19). Slots are not axis-equivalent across rounds; comparison tracks criterion-level trajectories within slots.

| Criterion | Prior Verdict (R5) | Current Verdict (R6) | Variation | Mechanism |
|-----------|-------------------|---------------------|-----------|-----------|

No regressions detected -- no criterion degraded from R5 to R6 in any variation slot. All round-over-round changes are improvements:
- V-01: C-10 FAIL->PASS (R6 carries worked example in FAILURE PATTERNS); C-19 new PASS; 97.27->97.50
- V-02: C-10, C-14, C-17 FAIL->PASS (R6 V-02 adds full diagnostic question column); C-19 new PARTIAL; 96.36->98.75
- V-03: C-19 new PASS; C-10 FAIL persists (worked example in SETUP not FAILURE PATTERNS); 96.36->96.67
- V-04: C-19 new PASS; all other verdicts unchanged; 98.18->99.17
- V-05: C-19 new PASS; all 18 prior criteria unchanged at PASS; 100.00->100.00

---

## LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-05 | 100.00 | yes |
| 2 | V-04 | 99.17 | yes |
| 3 | V-02 | 98.75 | yes |
| 4 | V-01 | 97.50 | yes |
| 5 | V-03 | 96.67 | yes |

Ties broken by essential-tier score (all equal: 60.0), then recommended-tier score (all equal: 30.0). No ties.

Score distribution: min = 96.67, max = 100.00, spread = 3.33 -- scores cluster tightly (< 5 pt spread), consistent with R5 spread of 3.64. Tight clustering confirms the primary remaining differentiator is C-09 (0.833 pt), with C-19 form variation (PASS vs PARTIAL) costing only 0.417 pt additional. N_aspirational=12 means each aspirational criterion costs 0.833 pt; the 4-criterion gap between V-03 and V-05 accounts for the full 3.33 pt spread. All 5 variations are Golden.

**Key findings:**
- C-19 form test resolved: imperative ("must be carried forward") earns PASS; interrogative ("has it been carried forward?") earns PARTIAL -- form determines C-19 verdict regardless of location
- C-19 enforcement mode test: passive imperative sentence (V-01) and active STOP-PRESERVATION gate (V-03) both earn C-19 PASS -- enforcement strength does not differentiate; only form does
- C-10 is STOP-gate-fragile in V-03: lifecycle emphasis moved the worked example from FAILURE PATTERNS into SETUP Step 1.4, causing per-output C-10 FAIL (mitigated at round level by C-05 auto-PASS)
- V-02 ranks above V-01 despite C-19 PARTIAL because adding C-14 and C-17 PASS (+2.0 pts aspirational) outweighs the C-19 shortfall (-0.417 pt)

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-19 PASS requires imperative form ('must be carried forward verbatim') placed near the C-10 definition or in the SETUP block; interrogative form ('has it been carried forward?') in the same location earns only PARTIAL -- form is the deciding factor, not location", "C-10 is STOP-gate-fragile: V-03's lifecycle emphasis relocated the worked example from FAILURE PATTERNS into the SETUP preservation checkpoint (Step 1.4), causing a per-output C-10 FAIL -- the worked example must remain specifically in the FAILURE PATTERNS action line to satisfy C-10"]}
```
