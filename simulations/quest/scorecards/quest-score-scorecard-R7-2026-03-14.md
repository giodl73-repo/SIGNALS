Scorecard written to `simulations/quest/scorecards/quest-score-scorecard-R7-2026-03-14.md`.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-20 PASS requires a mandatory verb ('must', 'shall', 'is required to') in the primary preservation rule; interrogative form ('Has the worked example been carried forward?') earns C-19 PARTIAL + C-20 FAIL regardless of location -- form is the deciding factor", "C-21 FAIL when the worked example is relocated to SETUP even as an explicit named preservation checkpoint -- the instantiated worked example must appear in the FAILURE PATTERNS action line; SETUP may contain the C-19 imperative rule without absorbing the example"]}
```
C-10 FAIL + C-21 FAIL. The FAILURE PATTERNS action line is the only qualifying location. SETUP may contain the C-19 preservation rule without absorbing the instantiated example.
- **V-01 and V-05 both reach 100.00.** V-05 is the synthesis candidate for the R7 golden: its explicit C-21 location prohibition in the Preservation Rule and three-pattern C-20 enumeration reduce future versioning risk without altering any criterion verdict.
- **Spread = 1.43 pts** -- tightest across all rounds (R6: 3.33, R5: 3.64). Only targeted single-axis ablations produce score separation; the rubric has converged.

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["C-20 PASS requires a mandatory verb ('must', 'shall', 'is required to') in the primary preservation rule; interrogative form ('Has the worked example been carried forward?') earns C-19 PARTIAL + C-20 FAIL regardless of location -- form is the deciding factor", "C-21 FAIL when the worked example is relocated to SETUP even as an explicit named preservation checkpoint -- the instantiated worked example must appear in the FAILURE PATTERNS action line; SETUP may contain the C-19 imperative rule without absorbing the example"]}
```

---

### OUTPUT: V-01 -- Baseline R7 Full Stack

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "C-01 Per-criterion verdicts present \| \| \| ... C-21 Worked example FAILURE PATTERNS location lock \| \| \|" -- 21-row scoring table template, C-01 through C-21, no gaps | PASS |
| C-02 Evidence quote for every verdict | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse." -- explicit mandate ensures non-empty evidence before every verdict | PASS |
| C-03 Composite score computed correctly | "N_essential = 4, N_recommended = 3, N_aspirational = 14. PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0." -- v7 N values used; formula derivable from 21-row table | PASS |
| C-04 Ranked leaderboard present | "#### LEADERBOARD ... \| Rank \| Output \| Score \| Golden \|" -- four-column ranked table in Phase 3 | PASS |
| C-05 Failure patterns surfaced | "If no criterion fails universally: C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS." -- auto-PASS resolution logic present | PASS |
| C-06 Excellence signals surfaced | "#### EXCELLENCE SIGNALS ... For each output-criterion pair where one output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)" -- section present | PASS |
| C-07 Regression signals surfaced | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \| ... If no prior-round data: C-07 auto-PASS" -- named section with four-column table | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [fully instantiated action line with verb + real artifact filename + section location] ... No-placeholder mandate: All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs." | PASS |
| C-09 Score distribution commentary | "Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread). Note that N_aspirational=14 means each aspirational criterion contributes 10/14 = 0.714 pt to the composite; achieving composite >= 99 requires at most one aspirational FAIL." -- explicit numeric mandate with calibration language | PASS |
| C-10 Worked example in action line | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- in Phase 3 FAILURE PATTERNS; real artifact name (quest-score.md); real section (LEADERBOARD section) | PASS |
| C-11 Auto-PASS rules stated in preamble | "**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. **C-07 auto-PASS** when no prior-round scorecard is provided. **C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires)." -- all 5 declarations with criterion IDs and trigger phrases in Step 1.1 SETUP | PASS |
| C-12 Formula reproduced before first output section | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) ... N_essential = 4, N_recommended = 3, N_aspirational = 14." -- in Step 1.2 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit written mandate with named violation | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions \| ID \| Name \| Tier \| Auto-PASS Status \| Diagnostic Question \|" -- 21-row roster with non-empty Diagnostic Question for all criteria C-01 through C-21 | PASS |
| C-15 Preamble gate instruction present | "STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed." and "Do not open any output file until PHASE 1 is fully written." -- imperative gate at end of SETUP block | PASS |
| C-16 Named standalone auto-PASS block | "#### Step 1.1 -- Auto-PASS Conditions" -- dedicated named block separate from criterion roster (Step 1.3); each declaration names criterion ID and trigger phrase explicitly | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 21 verdict rows (C-01 through C-21)... A matrix with 19 or 20 rows fails C-01 even if all other rows are correct." (count); C-03: "Does the output use N_aspirational=14?... An output using N_aspirational=12 (v6 values) is a FAIL for C-03." (N-value); C-20: "Does the C-19 preservation rule contain a mandatory verb... Interrogative form... earns C-19 PARTIAL and C-20 FAIL. Conditional form... also earns C-20 FAIL." (form distinction) -- 3 mechanism-specific questions | PASS |
| C-18 Named standalone regression signals section | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \|" -- named standalone section in Phase 3, separate from SETUP and per-output tables | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Preservation Rule: The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder." -- in Step 1.1 SETUP; imperative; addresses versioning trigger | PASS |
| C-20 Preservation rule imperative form | "must be carried forward verbatim from the prior round" -- mandatory verb "must" present; imperative form | PASS |
| C-21 Worked example FAILURE PATTERNS location lock | Worked example appears in Phase 3 FAILURE PATTERNS ("Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md...'"); SETUP preservation rule does not absorb the instantiated example | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-21): 14/14 x 10 = 10.00 pts
- Composite = 100.00/100
- Golden: YES -- all 4 essentials PASS, 100.00 >= 80

---

### OUTPUT: V-02 -- C-20 Ablation (Interrogative Preservation Rule)

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "C-01 Per-criterion verdicts present \| \| \| ... C-21 Worked example FAILURE PATTERNS location lock \| \| \|" -- 21-row scoring table template, C-01 through C-21 | PASS |
| C-02 Evidence quote for every verdict | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- mandate requires non-empty evidence before every verdict | PASS |
| C-03 Composite score computed correctly | "N_essential = 4, N_recommended = 3, N_aspirational = 14. PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0." -- v7 N values used | PASS |
| C-04 Ranked leaderboard present | "#### LEADERBOARD ... \| Rank \| Output \| Score \| Golden \|" -- four-column ranked table in Phase 3 | PASS |
| C-05 Failure patterns surfaced | "If no criterion fails universally: C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS." -- section with universal-failure detection and auto-PASS resolution | PASS |
| C-06 Excellence signals surfaced | "#### EXCELLENCE SIGNALS ... For each output-criterion pair where one output outperforms the group by at least one tier, write the criterion, the output name, and what the output did differently." -- section present | PASS |
| C-07 Regression signals surfaced | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \| ... If no prior-round data: C-07 auto-PASS" -- named section with four-column table | PASS |
| C-08 Actionable diagnosis in failure patterns | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- verb + real artifact + section location in FAILURE PATTERNS | PASS |
| C-09 Score distribution commentary | "Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread). Note that N_aspirational=14 means each aspirational criterion contributes 10/14 = 0.714 pt to the composite." -- explicit numeric mandate | PASS |
| C-10 Worked example in action line | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- fully instantiated in Phase 3 FAILURE PATTERNS; real artifact name; real section | PASS |
| C-11 Auto-PASS rules stated in preamble | "**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. **C-07 auto-PASS** when no prior-round scorecard is provided. **C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires)." -- all 5 declarations in Step 1.1 | PASS |
| C-12 Formula reproduced before first output section | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) ... N_aspirational = 14" -- in Step 1.2 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit mandate with named violation | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions \| ID \| Name \| Tier \| Auto-PASS Status \| Diagnostic Question \|" -- 21-row roster with non-empty questions for all criteria including C-20 and C-21 | PASS |
| C-15 Preamble gate instruction present | "STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed." -- imperative gate at end of SETUP | PASS |
| C-16 Named standalone auto-PASS block | "#### Step 1.1 -- Auto-PASS Conditions" -- dedicated named block separate from criterion roster; each declaration names criterion ID and trigger phrase | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated?" (count); C-03: "Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1? An output using N_aspirational=12 is a FAIL." (N-value); C-20: "Does the preservation statement use a mandatory verb ('must', 'shall', 'is required to')? Interrogative form ('has it been carried forward?') earns C-19 PARTIAL + C-20 FAIL." (form distinction) | PASS |
| C-18 Named standalone regression signals section | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \|" -- named standalone section in Phase 3 | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Carryforward Check: Has the worked example in the FAILURE PATTERNS action line been carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion?" -- preservation concept present in SETUP near C-10 declaration; location satisfies criterion; form is interrogative ("Has...been carried forward?") not imperative ("must be carried forward") | PARTIAL |
| C-20 Preservation rule imperative form | "Has the worked example in the FAILURE PATTERNS action line been carried forward verbatim from the prior round" -- interrogative form; no mandatory verb ("must", "shall", "is required to") present in primary preservation statement; "restore it before proceeding" is a conditional recovery command, not the preservation rule | FAIL |
| C-21 Worked example FAILURE PATTERNS location lock | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- instantiated worked example in Phase 3 FAILURE PATTERNS, not only in SETUP | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-21): (12 x 1.0 + 0.5 + 0.0) / 14 x 10 = 12.5/14 x 10 = 8.929 pts
- Composite = 98.93/100
- Golden: YES -- all 4 essentials PASS, 98.93 >= 80

---

### OUTPUT: V-03 -- C-21 Ablation (Worked Example Relocated to SETUP)

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "C-01 Per-criterion verdicts present \| \| \| ... C-21 Worked example FAILURE PATTERNS location lock \| \| \|" -- 21-row scoring table template, C-01 through C-21 | PASS |
| C-02 Evidence quote for every verdict | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse." -- mandate ensures non-empty evidence before every verdict | PASS |
| C-03 Composite score computed correctly | "N_essential = 4, N_recommended = 3, N_aspirational = 14. PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0." -- v7 N values used | PASS |
| C-04 Ranked leaderboard present | "#### LEADERBOARD ... \| Rank \| Output \| Score \| Golden \|" -- four-column ranked table present | PASS |
| C-05 Failure patterns surfaced | "If no criterion fails universally: C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS." -- section with auto-PASS logic present | PASS |
| C-06 Excellence signals surfaced | "#### EXCELLENCE SIGNALS ... For each output-criterion pair where one output outperforms the group by at least one tier, write the criterion, the output name, and what the output did differently." -- section present | PASS |
| C-07 Regression signals surfaced | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \| ... If no prior-round data: C-07 auto-PASS" -- named section with four-column table | PASS |
| C-08 Actionable diagnosis in failure patterns | "Action: [verb] [specific artifact filename] [section location] -- fully instantiated, no placeholders" -- action line format mandate present | PASS |
| C-09 Score distribution commentary | "Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster (< 5 pt spread) or discriminate (>= 10 pt spread). Note that N_aspirational=14 means each aspirational criterion contributes 10/14 = 0.714 pt to the composite." -- explicit numeric mandate | PASS |
| C-10 Worked example in action line | "Action: [verb] [specific artifact filename] [section location] -- fully instantiated, no placeholders" -- Phase 3 FAILURE PATTERNS action line is a format placeholder; "Current worked example (preserved from prior round): 'Add a Score distribution note: instruction to the LEADERBOARD section of quest-score.md...'" appears only in Step 1.1 SETUP, not in FAILURE PATTERNS | FAIL |
| C-11 Auto-PASS rules stated in preamble | "**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. **C-07 auto-PASS** when no prior-round scorecard is provided. **C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires)." -- all 5 declarations with criterion IDs in Step 1.1 | PASS |
| C-12 Formula reproduced before first output section | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) ... N_aspirational = 14" -- in Step 1.2 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit mandate with named violation | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions \| ID \| Name \| Tier \| Auto-PASS Status \| Diagnostic Question \|" -- 21-row roster with non-empty questions for all criteria including C-20 and C-21 | PASS |
| C-15 Preamble gate instruction present | "STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed." and "Do not open any output file until PHASE 1 is fully written." -- imperative gate at end of SETUP | PASS |
| C-16 Named standalone auto-PASS block | "#### Step 1.1 -- Auto-PASS Conditions" -- dedicated named block separate from criterion roster; each declaration names criterion ID and trigger phrase | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated?" (count); C-03: "Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1?" (N-value); C-20: "Does the preservation rule use a mandatory verb ('must', 'shall', 'is required to')? Interrogative or conditional form earns C-20 FAIL." (form distinction) | PASS |
| C-18 Named standalone regression signals section | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \|" -- named standalone section in Phase 3 | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Preservation Rule: The worked example below must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace it with a format instruction placeholder. This rule is in force at every rubric version change." -- imperative rule in Step 1.1 SETUP; addresses versioning trigger | PASS |
| C-20 Preservation rule imperative form | "must be carried forward verbatim from the prior round" -- mandatory verb "must" present; imperative form | PASS |
| C-21 Worked example FAILURE PATTERNS location lock | "Current worked example (preserved from prior round): 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md...'" -- fully instantiated example appears in Step 1.1 SETUP (preservation checkpoint), not in Phase 3 FAILURE PATTERNS action line; FAILURE PATTERNS has only "[verb] [specific artifact filename] [section location]" placeholder | FAIL |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-21): 12/14 x 10 = 8.571 pts (C-10 FAIL, C-21 FAIL)
- Composite = 98.57/100
- Golden: YES -- all 4 essentials PASS, 98.57 >= 80

---

### OUTPUT: V-04 -- Score Distribution Format (Prose Commentary)

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "C-01 Per-criterion verdicts present \| \| \| ... C-21 Worked example FAILURE PATTERNS location lock \| \| \|" -- 21-row scoring table template, C-01 through C-21 | PASS |
| C-02 Evidence quote for every verdict | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- mandate requires non-empty evidence before every verdict | PASS |
| C-03 Composite score computed correctly | "N_essential = 4, N_recommended = 3, N_aspirational = 14. PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0." -- v7 N values used | PASS |
| C-04 Ranked leaderboard present | "#### LEADERBOARD ... \| Rank \| Output \| Score \| Golden \|" -- four-column ranked table present | PASS |
| C-05 Failure patterns surfaced | "If no criterion fails universally: C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS." -- section with auto-PASS logic present | PASS |
| C-06 Excellence signals surfaced | "#### EXCELLENCE SIGNALS ... For each output-criterion pair where one output outperforms the group by at least one tier" -- section present | PASS |
| C-07 Regression signals surfaced | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \| ... If no prior-round data: C-07 auto-PASS" -- named section with four-column table | PASS |
| C-08 Actionable diagnosis in failure patterns | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- verb + real artifact + section location | PASS |
| C-09 Score distribution commentary | "After the rank table, write a commentary paragraph describing the score distribution across all scored outputs: how tightly or loosely the scores cluster, what the spread indicates about rubric discriminability, and any notable calibration observations." -- qualitative prose instruction; no explicit mandate to state minimum score, maximum score, and spread as numeric values | PARTIAL |
| C-10 Worked example in action line | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- fully instantiated in Phase 3 FAILURE PATTERNS | PASS |
| C-11 Auto-PASS rules stated in preamble | "**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. **C-07 auto-PASS** when no prior-round scorecard is provided. **C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires)." -- all 5 declarations in Step 1.1 | PASS |
| C-12 Formula reproduced before first output section | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) ... N_aspirational = 14" -- in Step 1.2 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit mandate with named violation | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions \| ID \| Name \| Tier \| Auto-PASS Status \| Diagnostic Question \|" -- 21-row roster with non-empty questions for all criteria including C-20 and C-21 | PASS |
| C-15 Preamble gate instruction present | "STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed." -- imperative gate at end of SETUP | PASS |
| C-16 Named standalone auto-PASS block | "#### Step 1.1 -- Auto-PASS Conditions" -- dedicated named block separate from criterion roster; each declaration names criterion ID and trigger phrase | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 21 verdict rows (C-01 through C-21) in the scoring table, with none missing or duplicated?" (count); C-03: "Does the output use N_aspirational=14? Can you re-derive the composite from the 21 visible verdict values within +-1?" (N-value); C-20: "Does the preservation rule use a mandatory verb ('must', 'shall', 'is required to')?" (form distinction) | PASS |
| C-18 Named standalone regression signals section | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \|" -- named standalone section in Phase 3 | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Preservation Rule: The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. This rule is in force at every rubric version change and applies regardless of whether C-10 auto-PASS fires this run." -- imperative rule in Step 1.1 SETUP | PASS |
| C-20 Preservation rule imperative form | "must be carried forward verbatim from the prior round" -- mandatory verb "must" present; imperative form | PASS |
| C-21 Worked example FAILURE PATTERNS location lock | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- instantiated worked example in Phase 3 FAILURE PATTERNS, not only in SETUP | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-21): (13 x 1.0 + 0.5) / 14 x 10 = 13.5/14 x 10 = 9.643 pts
- Composite = 99.64/100
- Golden: YES -- all 4 essentials PASS, 99.64 >= 80

---

### OUTPUT: V-05 -- Combination Pass

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Per-criterion verdicts present | "C-01 Per-criterion verdicts present \| \| \| ... C-21 Worked example FAILURE PATTERNS location lock \| \| \|" -- 21-row scoring table template, C-01 through C-21 | PASS |
| C-02 Evidence quote for every verdict | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." and "No-placeholder mandate: All action lines in FAILURE PATTERNS must use real artifact names and exact section locations visible in the scored outputs." | PASS |
| C-03 Composite score computed correctly | "N_essential = 4, N_recommended = 3, N_aspirational = 14. PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0." -- v7 N values used | PASS |
| C-04 Ranked leaderboard present | "#### LEADERBOARD ... \| Rank \| Output \| Score \| Golden \|" -- four-column ranked table present | PASS |
| C-05 Failure patterns surfaced | "If no criterion fails universally: C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS." -- section with auto-PASS logic and universal-failure detection | PASS |
| C-06 Excellence signals surfaced | "#### EXCELLENCE SIGNALS ... For each output-criterion pair where one output outperforms the group by at least one tier (PASS vs. PARTIAL or PARTIAL vs. FAIL)" -- section present with differential instruction | PASS |
| C-07 Regression signals surfaced | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \| ... If no prior-round data: C-07 auto-PASS -- no prior-round scorecard provided. Section present but not applicable." -- named section with four-column table | PASS |
| C-08 Actionable diagnosis in failure patterns | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- verb + real artifact + section location | PASS |
| C-09 Score distribution commentary | "Score distribution note: State minimum score, maximum score, and spread. State whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread). Note that N_aspirational=14 means each aspirational criterion contributes 10/14 = 0.714 pt to the composite; a single aspirational FAIL costs 0.714 pt; achieving composite >= 99 requires at most one aspirational FAIL." -- explicit numeric mandate with calibration language and per-criterion weight | PASS |
| C-10 Worked example in action line | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- fully instantiated in Phase 3 FAILURE PATTERNS; SETUP preservation rule explicitly states example "must remain in the FAILURE PATTERNS action line" | PASS |
| C-11 Auto-PASS rules stated in preamble | "**C-05 auto-PASS** when no criterion receives FAIL or PARTIAL in every scored output. **C-07 auto-PASS** when no prior-round scorecard is provided. **C-08 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-10 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires). **C-21 auto-PASS** when no failure patterns exist (C-05 auto-PASS fires)." -- all 5 declarations with criterion IDs and trigger phrases in Step 1.1 | PASS |
| C-12 Formula reproduced before first output section | "composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 14 * 10) ... N_aspirational = 14" -- in Step 1.2 before any per-output heading | PASS |
| C-13 Evidence-before-verdict ordering enforced | "Evidence-ordering mandate: In every scoring table, column order is Criterion \| Evidence Quote \| Verdict. Write the evidence quote first, then the verdict; never the reverse. A verdict cell completed before its evidence quote cell violates C-13." -- explicit mandate with named violation | PASS |
| C-14 Per-criterion diagnostic question in roster | "Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions \| ID \| Name \| Tier \| Auto-PASS Status \| Diagnostic Question \|" -- 21-row roster with non-empty questions for all criteria C-01 through C-21 | PASS |
| C-15 Preamble gate instruction present | "STOP-3. PHASE 1 complete. Do not open any output file until STOP-3 is passed." and "Do not open any output file until PHASE 1 is fully written." -- imperative gates at multiple SETUP checkpoints | PASS |
| C-16 Named standalone auto-PASS block | "#### Step 1.1 -- Auto-PASS Conditions" -- dedicated named block separate from criterion roster; each of the 5 declarations names criterion ID and trigger phrase explicitly | PASS |
| C-17 Criterion-specific diagnostic questions | C-01: "Can you count exactly 21 verdict rows (C-01 through C-21)... A matrix with 19 or 20 rows fails C-01 even if all other rows are present." (count); C-03: "Does the output use N_aspirational=14?... An output using N_aspirational=12 (v6) is a C-03 FAIL regardless of other scores." (N-value); C-20: "Three form patterns: (1) imperative 'must be carried forward' earns C-20 PASS; (2) interrogative 'has it been carried forward?' earns C-19 PARTIAL + C-20 FAIL; (3) conditional 'if versioning, update the example' earns C-20 FAIL. Location alone does not satisfy C-20 -- verb form is the deciding factor." (form distinction, 3 patterns named) | PASS |
| C-18 Named standalone regression signals section | "#### REGRESSION SIGNALS ... \| Criterion \| Prior Verdict \| Current Verdict \| Mechanism \|" -- named standalone section in Phase 3 body | PASS |
| C-19 Worked-example carryforward preservation instruction | "C-10 Worked-Example Preservation Rule: The worked example in the FAILURE PATTERNS action line must be carried forward verbatim from the prior round, or updated to reflect the current round's new axis criterion, whenever the rubric is versioned forward. Do not replace the worked example with a format instruction placeholder. The worked example must remain in the FAILURE PATTERNS action line -- do not relocate it to SETUP, to a roster diagnostic question, or to a preservation checkpoint." -- imperative rule in Step 1.1; addresses versioning trigger and location constraint | PASS |
| C-20 Preservation rule imperative form | "must be carried forward verbatim from the prior round" and "must remain in the FAILURE PATTERNS action line" -- mandatory verb "must" present in both carryforward rule and location constraint; imperative form throughout | PASS |
| C-21 Worked example FAILURE PATTERNS location lock | "Example of a fully instantiated action line: 'Add a 'Score distribution note:' instruction to the LEADERBOARD section of quest-score.md directing the scorer to state min score, max score, spread, and whether scores cluster (< 5 pt spread, suggesting calibration difficulty) or discriminate (>= 10 pt spread) -- so C-09 is satisfied on every run.'" -- instantiated worked example in Phase 3 FAILURE PATTERNS; Preservation Rule explicitly prohibits relocation to SETUP | PASS |

Composite:
- Essential (C-01--C-04): 4/4 x 60 = 60.00 pts
- Recommended (C-05--C-07): 3/3 x 30 = 30.00 pts
- Aspirational (C-08--C-21): 14/14 x 10 = 10.00 pts
- Composite = 100.00/100
- Golden: YES -- all 4 essentials PASS, 100.00 >= 80

---

## FAILURE PATTERNS

Checking for criteria with FAIL or PARTIAL in every scored output:
- C-09: PASS/PASS/PASS/PARTIAL/PASS -- not universal
- C-19: PASS/PARTIAL/PASS/PASS/PASS -- not universal
- C-20: PASS/FAIL/PASS/PASS/PASS -- not universal
- C-10: PASS/PASS/FAIL/PASS/PASS -- not universal
- C-21: PASS/PASS/FAIL/PASS/PASS -- not universal

**C-05 auto-PASS -- no universal failures. C-08 auto-PASS. C-10 auto-PASS. C-21 auto-PASS.**

---

## REGRESSION SIGNALS

Prior-round scorecard (R6) provided. C-07 auto-PASS does NOT apply.

Note: R6 and R7 variation axes differ (R6 tested C-19 form and C-10 location; R7 tests C-20 grammar and C-21 as new named criteria). Criterion-level trajectory is the appropriate comparison unit.

| Criterion | Prior Verdict (R6) | Current Verdict (R7) | Variation | Mechanism |
|-----------|-------------------|---------------------|-----------|-----------|
| C-09 | FAIL | PASS | V-01 | R7 V-01 baseline inherits score distribution mandate from R6 V-05; R6 V-01 lacked it |
| C-09 | FAIL | PASS | V-02 | R7 V-02 carries score distribution mandate despite C-20 ablation axis |
| C-09 | FAIL | PASS | V-03 | R7 V-03 carries score distribution mandate despite C-21 ablation axis |
| C-09 | FAIL | PARTIAL | V-04 | R7 V-04 axis is C-09 prose format -- FAIL->PARTIAL improvement; numeric mandate still absent |
| C-14 | FAIL | PASS | V-01 | R7 baseline carries 21-row diagnostic question roster from R6 V-05 |
| C-17 | FAIL | PASS | V-01 | R7 baseline carries mechanism-specific questions from R6 V-05 |
| C-20 | N/A (new in v7) | FAIL | V-02 | C-20 is new in R7 rubric; V-02 ablation intentionally fails it via interrogative preservation rule |
| C-21 | N/A (new in v7) | FAIL | V-03 | C-21 is new in R7 rubric; V-03 ablation intentionally fails it by relocating worked example to SETUP |

No regressions detected. All round-over-round changes are improvements (C-09, C-14, C-17 FAIL->PASS in V-01) or intentional ablation signals. C-09 in V-04 improves from FAIL to PARTIAL -- directionally correct but not yet a full PASS.

---

## EXCELLENCE SIGNALS

**C-09 -- V-01, V-02, V-03, V-05 PASS vs. V-04 PARTIAL:**
What they did differently: All four used a structured mandate ("Score distribution note: State minimum score, maximum score, and spread") requiring numeric values explicitly. V-04 used prose instruction ("write a commentary paragraph describing the score distribution...how tightly or loosely the scores cluster") that satisfies the calibration concept but omits the numeric mandate. The phrase "State minimum score, maximum score, and spread" is what guarantees C-09 PASS on every run.

**C-19 -- V-01, V-03, V-04, V-05 PASS vs. V-02 PARTIAL:**
What they did differently: All four used an imperative statement with mandatory verb: "The worked example...must be carried forward verbatim." V-02 used interrogative form: "Has the worked example...been carried forward verbatim?" Imperative states what must be done; interrogative probes whether it was done. Form determines verdict regardless of location.

**C-20 -- V-01, V-03, V-04, V-05 PASS vs. V-02 FAIL:**
What they did differently: All four preservation rules contain "must" as mandatory verb. V-02's primary preservation statement is interrogative and contains no mandatory verb -- absence of "must", "shall", or "is required to" causes C-20 FAIL regardless of any conditional recovery instruction.

**C-10 and C-21 -- V-01, V-02, V-04, V-05 PASS vs. V-03 FAIL:**
What they did differently: All four placed the fully instantiated worked example in Phase 3 FAILURE PATTERNS. V-03 relocated the example to Step 1.1 SETUP as a named preservation checkpoint and left FAILURE PATTERNS with a format placeholder. The FAILURE PATTERNS action line is the only qualifying location for both C-10 and C-21.

**V-05 vs. V-01 -- C-17 structural superiority (no tier differential, noted for signal value):**
V-05's C-20 diagnostic question explicitly enumerates all three form patterns (imperative/interrogative/conditional) with verdict consequences. V-01's C-20 question names two patterns. Both earn C-17 PASS. V-05's three-pattern enumeration reduces versioning risk at the C-20 boundary.

---

## LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | V-01 | 100.00 | YES |
| 1 | V-05 | 100.00 | YES |
| 3 | V-04 | 99.64 | YES |
| 4 | V-02 | 98.93 | YES |
| 5 | V-03 | 98.57 | YES |

Score distribution note: Min = 98.57 (V-03), max = 100.00 (V-01, V-05), spread = 1.43 pts. Scores cluster tightly (< 5 pt spread) -- tightest spread across all rounds (R6: 3.33, R5: 3.64). Narrowing confirms rubric convergence: R7 moved the previously differentiable gaps (C-20 grammar, C-21 location) into named criteria, so the baseline carries all passing structures and only deliberate single-axis ablations produce separation. N_aspirational=14 means each aspirational criterion contributes 10/14 = 0.714 pt; V-03's C-10 FAIL + C-21 FAIL = 1.429 pts accounts for the full spread floor. All 5 variations are Golden.
