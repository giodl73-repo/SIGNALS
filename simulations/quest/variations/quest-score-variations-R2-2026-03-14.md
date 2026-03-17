Written to `simulations/quest/variations/quest-score-variations-R2-2026-03-14.md`.

---

## Round 2 Variations — Summary

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | 12-row criterion roster in SETUP -- pre-prints C-10/C-11/C-12 rows that were absent from all R1 templates |
| **V-02** | Phrasing register | Diagnostic question per criterion -- interrogative column forces engagement with new criteria pass conditions before verdict |
| **V-03** | Lifecycle emphasis | Two-gate preamble -- Phase 1 is a mandatory output section (formula + auto-PASS declarations) before Phase 2 opens any output file |
| **V-04** | V-01 + V-03 | Roster + two-gate + evidence-first; closes C-01/C-11/C-12 structurally |
| **V-05** | Full synthesis | All of the above + "no fill-in-the-blank" mandate; closes C-10 explicitly |

**Three single-axis picks and rationale:**

- **Criterion roster** isolates C-01 on the expanded rubric — C-10/C-11/C-12 are invisible if not pre-printed
- **Diagnostic-question register** isolates C-10/C-11/C-12 — forces the model to answer "is the action line instantiated?" before assigning a verdict
- **Two-gate preamble** isolates C-11/C-12 — structural phase boundary enforces "preamble before first output section" without instruction compliance

**Key R2 constraint vs. R1:** N_aspirational changed from 2 to 5. Every variation updates the formula and denominator. Any R1 prompt body reused verbatim would FAIL C-03 and C-12. The TBD mechanism is new in R2 — C-05/C-08/C-10 auto-PASS conditions depend on post-scoring state, so they are declared "TBD" in the preamble and resolved at Phase 3.

**Predicted ceiling:** V-05, same conclusion as R1 but for different reasons: the 12-criterion expansion shifts the primary risk from C-03 (formula) to C-01 (row omission) and C-11/C-12 (structural self-reference). V-04 is the closest competitor; its likely gap is C-10 (worked example template present but no explicit "no placeholder" mandate).
ach criterion before
  assigning a verdict reduces shallow PASS/FAIL without engagement.
- **Two-gate preamble** isolates C-11 and C-12 directly -- these criteria require specific
  content before the first per-output section. A mandatory preamble phase enforces this
  structurally without relying on instruction compliance.

**Predicted ceiling:** V-05. Updated formula closes C-03/C-12 risk; full 12-row tables close
C-01; evidence-first closes C-02; preamble gate closes C-11/C-12; worked example mandate closes
C-10. V-04 is the closest structural competitor. Open question for R2: does the
diagnostic-question register (V-02) produce better C-10/C-11/C-12 compliance than V-01's
roster-only approach, given that V-02 has no structural guarantee on C-11?

---

## V-01: Criterion Roster Up-Front

**Axis:** Output format -- before any per-output section, print a full 12-row criterion roster
mapping each criterion to its tier and auto-PASS condition for this run. The roster anchors the
verdict tables structurally: every row is defined before any output is opened.

**Hypothesis:** Printing the full roster forces the model to enumerate all 12 criteria including
C-10/C-11/C-12, which were absent from every R1 variation template. Once the roster exists, the
scoring tables below reference it and a missing criterion row is visibly absent. N_aspirational=5
is established at the formula line, preventing C-03 drift.

```
You are running /quest-score. Score each provided skill output against the rubric.
Print the SETUP section fully before opening any output file.

---

## SETUP

List inputs before scoring:
- Rubric: [path] -- [N] criteria ([N_essential] essential, [N_recommended] recommended,
  [N_aspirational] aspirational)
- Outputs to score: [list each output path, one per line]
- Prior-round scorecard: [path, or "none provided"]
- Scoring date: [YYYY-MM-DD]

### Criterion Roster

Fill the "Auto-PASS status" column for this run before proceeding. Base on inputs above.
Write "auto-PASS" if the condition holds; "--" if scoring is required; "TBD" if it cannot
be resolved until after all outputs are scored.

| ID  | Name                                            | Tier        | Auto-PASS status for this run        |
|-----|-------------------------------------------------|-------------|--------------------------------------|
| C-01 | Per-criterion verdicts present                 | essential   | --                                   |
| C-02 | Evidence quote for every verdict               | essential   | --                                   |
| C-03 | Composite score computed correctly             | essential   | --                                   |
| C-04 | Ranked leaderboard present                     | essential   | --                                   |
| C-05 | Failure patterns surfaced                      | recommended | TBD                                  |
| C-06 | Excellence signals surfaced                    | recommended | --                                   |
| C-07 | Regression signals surfaced                    | recommended | [auto-PASS / -- based on prior data] |
| C-08 | Actionable diagnosis in failure patterns       | aspirational | TBD                                 |
| C-09 | Score distribution commentary                  | aspirational | --                                  |
| C-10 | Worked example in action line                  | aspirational | TBD                                 |
| C-11 | Auto-PASS rules stated in preamble             | aspirational | --                                  |
| C-12 | Formula reproduced before first output section | aspirational | --                                  |

### Composite Formula (v2 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 5 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 5.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

SETUP is complete when all roster rows are filled and the formula is printed above.
Do not open any output file until SETUP is complete.

---

## SCORING

Score each output in its own section. Complete one section fully before opening the next.

---

### OUTPUT: [output-id or filename]

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS / PARTIAL / FAIL | "[quote]" |
| C-02 Evidence quotes | PASS / PARTIAL / FAIL | "[quote]" |
| C-03 Composite score | PASS / PARTIAL / FAIL | "[quote showing score or formula; note N_aspirational value used]" |
| C-04 Leaderboard | PASS / PARTIAL / FAIL | "[quote]" |
| C-05 Failure patterns | PASS / PARTIAL / FAIL / auto-PASS | "[quote, or: auto-PASS -- see roster (TBD)]" |
| C-06 Excellence signals | PASS / PARTIAL / FAIL | "[quote, or: not found]" |
| C-07 Regression signals | PASS / PARTIAL / FAIL / auto-PASS | "[quote, or: auto-PASS -- see roster]" |
| C-08 Actionable diagnosis | PASS / PARTIAL / FAIL / auto-PASS | "[quote, or: auto-PASS -- see roster (TBD)]" |
| C-09 Score distribution | PASS / PARTIAL / FAIL | "[quote, or: not found]" |
| C-10 Worked example | PASS / PARTIAL / FAIL / auto-PASS | "[quote showing instantiated action line, or: auto-PASS (TBD)]" |
| C-11 Auto-PASS in preamble | PASS / PARTIAL / FAIL | "[quote from the output's preamble section, or: preamble not found]" |
| C-12 Formula at preamble | PASS / PARTIAL / FAIL | "[quote showing formula with N values before first output heading, or: not found]" |

Composite computation:
  Essential (C-01 to C-04):   [C-01_val + C-02_val + C-03_val + C-04_val] / 4 * 60 = [pts]
  Recommended (C-05 to C-07): [C-05_val + C-06_val + C-07_val] / 3 * 30 = [pts]
  Aspirational (C-08 to C-12): [C-08 + C-09 + C-10 + C-11 + C-12] / 5 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes -- all 4 essentials PASS and score >= 80 / no -- reason]

[Repeat this complete section for every output before proceeding.]

---

## LEADERBOARD

Rank all outputs from highest to lowest composite score. Ties resolved alphabetically.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [output-id] | [score] | yes / no |

---

## FAILURE PATTERNS

Resolve TBD entries (C-05, C-08, C-10) based on scoring above.

For each criterion that received FAIL or PARTIAL in EVERY scored output:
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design issue / data gap] -- [one sentence why].
  Action: [fully instantiated -- verb + artifact + location, e.g.,
  "Add a 12-row criterion roster to quest-score.md SETUP block so C-10/C-11/C-12
  rows are pre-printed for every run."]

Update roster: C-05=[resolved status], C-08=[resolved status], C-10=[resolved status].

[If no universal failures: "No universal failures -- C-05 auto-PASS."]

---

## EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by >= one tier:
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.

[If uniform: "No differential excellence detected."]

---

## REGRESSION SIGNALS

[Prior-round scorecard provided: list every output-criterion pair that regressed (PASS -> FAIL
or PARTIAL).]
[No regressions: "No regressions detected."]
[No prior-round data: "No prior-round scorecard provided -- C-07 auto-PASS."]

---

## SCORE DISTRIBUTION

[1-3 sentences: state min score, max score, spread, and calibration implication.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-02: Diagnostic-Question Register

**Axis:** Phrasing register -- each criterion in the verdict table is preceded by a diagnostic
question pre-printed as a column. The model must answer the question (via evidence quote) before
committing to a verdict label. Imperative template slots replaced by interrogative prompts.

**Hypothesis:** Diagnostic questions force engagement with each criterion's specific pass
condition before assigning a verdict. This is particularly important for the three new
aspirational criteria: C-10 asks "is the action line instantiated, not a template placeholder?",
C-11 asks "is there a preamble block before the first scoring section?", C-12 asks "is the
formula with N_aspirational=5 visible before the first output heading?". Template-slot registers
do not convey this interrogative intent; diagnostic questions do.

```
You are running /quest-score. Score a set of skill output files against a rubric (12 criteria,
v2) and produce a QuestScorecard artifact.

---

## PREAMBLE

Read the rubric completely before opening any output file. Then fill in this preamble.

### Auto-PASS Declaration

| Criterion | Auto-PASS condition | Status for this run | Justification |
|-----------|---------------------|---------------------|---------------|
| C-05 | No criterion fails across ALL outputs | TBD (resolve after scoring) | |
| C-07 | No prior-round scorecard provided | [auto-PASS / scoring required] | [one phrase] |
| C-08 | No failure patterns exist | TBD (resolve after scoring) | |
| C-10 | No failure patterns exist | TBD (resolve after scoring) | |

### Composite Formula (v2 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 5 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 5.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0.
  Golden: all 4 essentials PASS AND composite >= 80.

Preamble is complete. Open output files only after this section is written.

---

## SCORING

For each output, read it completely, then fill the diagnostic table below. The diagnostic
question column frames each scoring judgment. Write the evidence quote, then the verdict;
never the reverse.

---

### OUTPUT: [output-id]

| Criterion | Diagnostic Question | Evidence Quote | Verdict |
|-----------|---------------------|----------------|---------|
| C-01 Verdicts present | Does a verdict table exist with a row for every one of the 12 rubric criteria? Is any criterion row missing? | "[quote]" | PASS / PARTIAL / FAIL |
| C-02 Evidence quotes | Is every verdict cell accompanied by a non-empty, traceable quote from the scored output -- not a template placeholder? | "[quote]" | PASS / PARTIAL / FAIL |
| C-03 Composite score | Is the composite computed with N_aspirational=5 (not 2)? Can the score be re-derived from the visible verdict table within +-1? | "[quote showing formula or score]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | Are all N outputs ranked exactly once in descending order with a Golden column? | "[quote]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | If any criterion failed universally, is it named with a candidate explanation? If none failed universally, is auto-PASS declared? | "[quote, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | Is at least one output-criterion pair identified where the output outperforms the group median by >= one tier? | "[quote, or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | If prior-round data was provided, are all regressions listed? If no data, is auto-PASS stated? | "[quote, or: auto-PASS]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | Does every failure pattern entry conclude with a specific verb + artifact recommendation -- not a generic observation? | "[quote, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | Is there a 1-3 sentence commentary naming the min/max scores and interpreting tight vs. wide spread? | "[quote, or: not found]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | Is each action line fully instantiated -- naming a real artifact and location -- rather than left as a fill-in-the-blank placeholder? | "[quote showing instantiated example, or: auto-PASS (TBD), or: not found]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | Is there a preamble section (before the first output scoring block) that lists every applicable auto-PASS criterion with a one-phrase justification? | "[quote from the output's preamble, or: preamble section absent]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | Does the composite formula appear before the first per-output heading, showing N_essential=4, N_recommended=3, N_aspirational=5? | "[quote showing formula with N values, or: not found before first output heading]" | PASS / PARTIAL / FAIL |

Composite:
  Essential:    C-01=[val] + C-02=[val] + C-03=[val] + C-04=[val] = [sum] / 4 * 60 = [pts]
  Recommended:  C-05=[val] + C-06=[val] + C-07=[val]             = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[val] + C-09=[val] + C-10=[val] + C-11=[val] + C-12=[val] = [sum] / 5 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes / no -- reason]

[Repeat for every output.]

---

## LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | yes/no |

Ties resolved alphabetically.

---

## FAILURE PATTERNS

Resolve TBD statuses (C-05, C-08, C-10) before writing this section.

[Any criterion FAIL or PARTIAL in EVERY output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence].
  Action: [fully worked example: verb + artifact name + section, e.g., "Add a preamble gate
  section to quest-score.md (before any SCORING heading) requiring auto-PASS declarations
  for C-05, C-07, C-08, and C-10."]

[None: "No universal failures -- C-05 auto-PASS."]

---

## EXCELLENCE SIGNALS

[Any output-criterion pair outperforming the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.

[Uniform: "No differential excellence detected."]

---

## REGRESSION SIGNALS

Prior-round data: [provided / not provided]
[Provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]
[None: "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

---

## SCORE DISTRIBUTION

[1-3 sentences: min score, max score, spread, calibration implication.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-03: Two-Gate Preamble

**Axis:** Lifecycle emphasis -- Phase 1 is a mandatory preamble gate (formula, auto-PASS
declarations, input listing). Phase 2 opens output files. Phase 3 aggregates. The model
cannot proceed to Phase 2 without completing Phase 1.

**Hypothesis:** C-11 and C-12 require specific content to appear before the first per-output
scoring block. A structural gate enforces this without relying on instruction compliance. V-05
from R1 placed auto-PASS rules and formula at the top of the prompt but within the scoring
document itself; this variation makes Phase 1 an explicit output section that must be rendered
before any scoring begins. The TBD mechanism handles auto-PASS conditions (C-05, C-08, C-10)
that cannot be resolved until all outputs are scored.

```
You are running /quest-score. Work in three phases: PREAMBLE, SCORE, AGGREGATE.
Phase 1 (PREAMBLE) is a mandatory gate: write it fully before opening any output file.

---

## PHASE 1: PREAMBLE

### Step 1.1 -- Inputs

- Rubric: [path] -- read completely. Note all 12 criteria and their tiers.
- Outputs to score: [list paths, one per line]
- Prior-round scorecard: [path, or "none"]
- Scoring date: [YYYY-MM-DD]

### Step 1.2 -- Composite Formula (print with v2 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 5 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 5.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0.
  Golden: all 4 essentials PASS AND composite >= 80.

### Step 1.3 -- Auto-PASS Declaration

State the auto-PASS status of each applicable criterion for this run. Write "auto-PASS" if the
condition holds now; "TBD" if it can only be resolved after scoring all outputs.

| Criterion | Auto-PASS condition | Status | Justification |
|-----------|---------------------|--------|---------------|
| C-05 | No criterion fails universally across all outputs | TBD | Cannot determine before scoring |
| C-07 | No prior-round scorecard provided | [auto-PASS / requires scoring] | [one phrase] |
| C-08 | No failure patterns exist | TBD | Cannot determine before scoring |
| C-10 | No failure patterns exist | TBD | Cannot determine before scoring |

Phase 1 is complete when Steps 1.1 through 1.3 are written above.
Proceed to Phase 2 only after Phase 1 is complete.

---

## PHASE 2: SCORE EACH OUTPUT

Complete one section fully before opening the next file.
Scoring uses the formula from Phase 1 Step 1.2 and auto-PASS rules from Step 1.3.

---

### SCORING: [output-id]

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS / PARTIAL / FAIL | "[quote]" |
| C-02 Evidence quotes | PASS / PARTIAL / FAIL | "[quote]" |
| C-03 Composite score | PASS / PARTIAL / FAIL | "[quote showing formula or score; verify N_aspirational=5]" |
| C-04 Leaderboard | PASS / PARTIAL / FAIL | "[quote]" |
| C-05 Failure patterns | PASS / PARTIAL / FAIL / auto-PASS | "[quote, or: TBD -- resolve at Phase 3]" |
| C-06 Excellence signals | PASS / PARTIAL / FAIL | "[quote, or: not found]" |
| C-07 Regression signals | PASS / PARTIAL / FAIL / auto-PASS | "[see Phase 1 Step 1.3]" |
| C-08 Actionable diagnosis | PASS / PARTIAL / FAIL / auto-PASS | "[quote, or: TBD -- resolve at Phase 3]" |
| C-09 Score distribution | PASS / PARTIAL / FAIL | "[quote, or: not found]" |
| C-10 Worked example | PASS / PARTIAL / FAIL / auto-PASS | "[quote showing fully instantiated action line, or: TBD]" |
| C-11 Auto-PASS in preamble | PASS / PARTIAL / FAIL | "[quote from the output's preamble block, or: not found]" |
| C-12 Formula at preamble | PASS / PARTIAL / FAIL | "[quote showing formula with N_aspirational=5 before first output heading, or: not found]" |

Composite:
  Essential:    [C-01 + C-02 + C-03 + C-04] / 4 * 60 = [pts]
  Recommended:  [C-05 + C-06 + C-07] / 3 * 30 = [pts]
  Aspirational: [C-08 + C-09 + C-10 + C-11 + C-12] / 5 * 10 = [pts]
  Composite = [SCORE]/100
  Golden: [yes / no -- reason]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

Resolve TBD auto-PASS statuses from Phase 1 Step 1.3. Update the declaration table:
- C-05: [auto-PASS -- no criterion failed universally / scoring required -- reason]
- C-08: [auto-PASS -- no failure patterns / scoring required -- reason]
- C-10: [auto-PASS -- no failure patterns / scoring required -- reason]

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | yes/no |

Ties resolved alphabetically.

### Failure Patterns

[Any criterion FAIL or PARTIAL in EVERY output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence].
  Action: [fully instantiated verb + artifact + location, e.g., "Add a mandatory
  PHASE 1 PREAMBLE gate to quest-score.md that requires formula and auto-PASS
  declarations before any per-output SCORING section is rendered."]

[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair outperforming the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.

[Uniform: "No differential excellence detected."]

### Regression Signals

[Prior-round data provided: list every output-criterion pair that regressed.]
[No regressions: "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min, max, spread, calibration implication.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-04: Criterion Roster + Two-Gate Preamble (V-01 + V-03)

**Axes:** Criterion roster up-front (V-01) + two-gate preamble (V-03) + evidence-first
ordering (R1 V-04)

**Hypothesis:** The roster prevents C-01 row omission on the expanded 12-criterion rubric.
The two-gate preamble structurally ensures C-11 (auto-PASS declarations before first output)
and C-12 (formula before first output). Evidence-first ordering protects C-02. Together: roster
closes the new-criteria coverage gap (C-01), preamble gate closes the structural self-referential
gap (C-11, C-12), and evidence-first closes the fabrication risk (C-02). C-10 is the likely
remaining gap: the worked example template is present but the mandate is not explicit.

```
You are running /quest-score. Work in three phases: PREAMBLE, SCORE, AGGREGATE.
Phase 1 (PREAMBLE) is a mandatory gate. Complete it fully before opening any output file.

---

## PHASE 1: PREAMBLE

### Inputs
- Rubric: [path] -- read completely
- Outputs to score: [list paths, one per line]
- Prior-round scorecard: [path, or "none"]
- Scoring date: [YYYY-MM-DD]

### Criterion Roster

Fill "auto-PASS status" before proceeding. "TBD" = cannot resolve before scoring all outputs.

| ID  | Name                                            | Tier         | Auto-PASS status     |
|-----|-------------------------------------------------|--------------|----------------------|
| C-01 | Per-criterion verdicts present                 | essential    | --                   |
| C-02 | Evidence quote for every verdict               | essential    | --                   |
| C-03 | Composite score computed correctly             | essential    | --                   |
| C-04 | Ranked leaderboard present                     | essential    | --                   |
| C-05 | Failure patterns surfaced                      | recommended  | TBD                  |
| C-06 | Excellence signals surfaced                    | recommended  | --                   |
| C-07 | Regression signals surfaced                    | recommended  | [auto-PASS / --]     |
| C-08 | Actionable diagnosis in failure patterns       | aspirational | TBD                  |
| C-09 | Score distribution commentary                  | aspirational | --                   |
| C-10 | Worked example in action line                  | aspirational | TBD                  |
| C-11 | Auto-PASS rules stated in preamble             | aspirational | --                   |
| C-12 | Formula reproduced before first output section | aspirational | --                   |

Justification for any criterion already resolved (e.g., C-07): [one phrase per resolved item]

### Composite Formula (v2 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 5 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 5.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden: all 4 essentials PASS AND composite >= 80.

Phase 1 complete when all roster rows have a status and the formula is printed.
Do not open any output file before Phase 1 is complete.

---

## PHASE 2: SCORE EACH OUTPUT

Complete the full section for one output before opening the next file.
Use the criterion roster to confirm all 12 rows appear in every verdict table.

---

### SCORING: [output-id]

**Table A -- Evidence extraction** (complete ALL 12 rows before filling Table B):

| ID  | Evidence Quote |
|-----|----------------|
| C-01 | "[quote]" |
| C-02 | "[quote]" |
| C-03 | "[quote showing formula or score; note N_aspirational value used]" |
| C-04 | "[quote showing leaderboard]" |
| C-05 | "[quote from failure patterns, or: auto-PASS (TBD), or: not found]" |
| C-06 | "[quote from excellence signals, or: not found]" |
| C-07 | "[quote from regression section, or: auto-PASS per roster]" |
| C-08 | "[quote showing verb+artifact recommendation, or: auto-PASS (TBD), or: not found]" |
| C-09 | "[quote from score distribution, or: not found]" |
| C-10 | "[quote showing fully instantiated action line (real artifact + location, no placeholder), or: auto-PASS (TBD), or: not found]" |
| C-11 | "[quote from the output's preamble block declaring auto-PASS conditions, or: not found]" |
| C-12 | "[quote showing formula with N values before first per-output heading, or: not found]" |

**Table B -- Verdicts** (fill only after Table A is complete):

| ID  | Verdict | Rationale |
|-----|---------|-----------|
| C-01 | PASS / PARTIAL / FAIL | [all 12 rows present? single missing row = FAIL] |
| C-02 | PASS / PARTIAL / FAIL | [every verdict cell has a non-empty quote?] |
| C-03 | PASS / PARTIAL / FAIL | [verify formula; check N_aspirational=5; unverifiable = FAIL] |
| C-04 | PASS / PARTIAL / FAIL | [all N outputs ranked once in descending order?] |
| C-05 | PASS / PARTIAL / FAIL / auto-PASS | [TBD: resolve at Phase 3] |
| C-06 | PASS / PARTIAL / FAIL | [at least one output-criterion pair named?] |
| C-07 | PASS / PARTIAL / FAIL / auto-PASS | [per Phase 1 roster] |
| C-08 | PASS / PARTIAL / FAIL / auto-PASS | [TBD: verb+artifact present per failure pattern entry?] |
| C-09 | PASS / PARTIAL / FAIL | [min/max named and clustering interpreted?] |
| C-10 | PASS / PARTIAL / FAIL / auto-PASS | [TBD: action lines instantiated with real artifact + location?] |
| C-11 | PASS / PARTIAL / FAIL | [preamble block with auto-PASS declarations exists before first scoring section?] |
| C-12 | PASS / PARTIAL / FAIL | [formula with N_essential=4, N_recommended=3, N_aspirational=5 visible before first output heading?] |

Composite:
  Essential:    C-01=[v] + C-02=[v] + C-03=[v] + C-04=[v] = [sum] / 4 * 60 = [pts]
  Recommended:  C-05=[v] + C-06=[v] + C-07=[v]            = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[v] + C-09=[v] + C-10=[v] + C-11=[v] + C-12=[v] = [sum] / 5 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes / no -- reason]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

Resolve TBD auto-PASS statuses from Phase 1 roster:
- C-05: [auto-PASS -- no criterion failed universally / scoring required -- reason]
- C-08: [auto-PASS -- no failure patterns / scoring required -- reason]
- C-10: [auto-PASS -- no failure patterns / scoring required -- reason]

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | yes/no |

Ties resolved alphabetically.

### Failure Patterns

[Any criterion FAIL or PARTIAL in EVERY scored output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence].
  Action: [fully instantiated -- verb + artifact + section, e.g., "Add criterion roster
  (12 rows, with auto-PASS column) to quest-score.md PHASE 1 PREAMBLE block."]

[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair where one outperforms the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.

[Uniform: "No differential excellence detected."]

### Regression Signals

[Prior-round data provided: list regressions or "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min, max, spread, calibration implication.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Criterion roster (V-01) + diagnostic questions on new criteria (V-02) + two-gate
preamble (V-03) + evidence-first ordering + worked example mandate + TBD resolution at Phase 3

**Hypothesis:** Maximum structural coverage across all 12 criteria:
- Roster prevents C-01 row omission on expanded rubric (C-10/C-11/C-12 visible before scoring)
- Preamble gate structurally enforces C-11 (auto-PASS declarations before first output heading)
- Formula at preamble with N_aspirational=5 closes C-03 and C-12 simultaneously
- Evidence-first Step A -> Step B prevents C-02 quote fabrication
- Diagnostic questions in Step B prevent shallow verdicts on C-10/C-11/C-12
- "No fill-in-the-blank" instruction closes C-10 (worked example mandate)
- TBD mechanism correctly defers C-05/C-08/C-10 auto-PASS to Phase 3

```
You are running /quest-score. Score a set of skill output files against a rubric (12 criteria,
v2) and produce a QuestScorecard artifact. Work in three phases: PREAMBLE, SCORE, AGGREGATE.

Phase 1 (PREAMBLE) is a mandatory gate. Write it fully before opening any output file.

---

## PHASE 1: PREAMBLE

### Inputs

- Rubric: [path] -- read completely. Count all 12 criteria.
- Outputs to score: [list paths, one per line]
- Prior-round scorecard: [path, or "none"]
- Scoring date: [YYYY-MM-DD]

### Criterion Roster

Fill all rows before proceeding to Phase 2. This table drives the verdict templates below.

| ID  | Name                                            | Tier         | Auto-PASS status for this run         |
|-----|-------------------------------------------------|--------------|---------------------------------------|
| C-01 | Per-criterion verdicts present                 | essential    | --                                    |
| C-02 | Evidence quote for every verdict               | essential    | --                                    |
| C-03 | Composite score computed correctly             | essential    | --                                    |
| C-04 | Ranked leaderboard present                     | essential    | --                                    |
| C-05 | Failure patterns surfaced                      | recommended  | TBD (resolve at Phase 3)              |
| C-06 | Excellence signals surfaced                    | recommended  | --                                    |
| C-07 | Regression signals surfaced                    | recommended  | [auto-PASS if no prior-round / else --] |
| C-08 | Actionable diagnosis in failure patterns       | aspirational | TBD (resolve at Phase 3)              |
| C-09 | Score distribution commentary                  | aspirational | --                                    |
| C-10 | Worked example in action line                  | aspirational | TBD (resolve at Phase 3)              |
| C-11 | Auto-PASS rules stated in preamble             | aspirational | --                                    |
| C-12 | Formula reproduced before first output section | aspirational | --                                    |

Justification for any criterion already resolved (e.g., C-07): [one phrase per resolved item]

### Composite Formula (v2 -- print with correct N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 5 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 5.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

Phase 1 complete when all roster rows have a status and the formula is printed above.
Do not open any output file before Phase 1 is complete.

---

## PHASE 2: SCORE EACH OUTPUT

Open and fully score one output before opening the next.
For each output: Step A (extract evidence for ALL 12 criteria), then Step B (render verdicts).
Do not write any verdict before its evidence quote in Step A is written.

---

### SCORING: [output-id]

**Step A -- Evidence extraction** (complete ALL 12 rows before filling Step B):

| ID  | Evidence Quote |
|-----|----------------|
| C-01 | "[verbatim or near-verbatim quote showing a verdict table with rows for all criteria]" |
| C-02 | "[quote showing an evidence-quote column or quote field in the scored output]" |
| C-03 | "[quote showing a composite score or formula computation; note N_aspirational value used]" |
| C-04 | "[quote showing a ranked leaderboard with a Golden column]" |
| C-05 | "[quote from failure patterns section, or: auto-PASS (TBD), or: not found]" |
| C-06 | "[quote from excellence signals section, or: not found]" |
| C-07 | "[quote from regression section, or: auto-PASS per Phase 1 roster]" |
| C-08 | "[quote showing a specific verb+artifact action recommendation, or: auto-PASS (TBD), or: not found]" |
| C-09 | "[quote from score distribution commentary mentioning min/max, or: not found]" |
| C-10 | "[quote showing a fully instantiated action line with a real artifact name and location -- NOT a template placeholder like '[verb + artifact]' -- or: auto-PASS (TBD), or: not found]" |
| C-11 | "[quote from the output's preamble block that declares auto-PASS conditions before the first scoring section, or: not found in preamble]" |
| C-12 | "[quote showing the composite formula with N_essential=4, N_recommended=3, N_aspirational=5 appearing before the first per-output heading, or: formula not found before first output section]" |

**Step B -- Verdicts** (fill only after Step A is complete):

| ID  | Verdict | Rationale (tie to diagnostic question) |
|-----|---------|----------------------------------------|
| C-01 | PASS / PARTIAL / FAIL | Does a verdict row exist for each of the 12 criteria? Single missing row = FAIL. |
| C-02 | PASS / PARTIAL / FAIL | Is every verdict cell accompanied by a non-empty, traceable quote? >20% missing = FAIL; any 1 missing = PARTIAL. |
| C-03 | PASS / PARTIAL / FAIL | Is the composite computed with N_aspirational=5? Can it be re-derived from the verdict table within +-1? Unverifiable = FAIL. |
| C-04 | PASS / PARTIAL / FAIL | Are all N outputs ranked exactly once in descending order with a Golden column? |
| C-05 | PASS / PARTIAL / FAIL / auto-PASS | If any criterion failed universally: named with candidate explanation? If none: auto-PASS declared? [TBD] |
| C-06 | PASS / PARTIAL / FAIL | At least one output-criterion pair named where the output outperforms the group median by >= one tier? |
| C-07 | PASS / PARTIAL / FAIL / auto-PASS | Per Phase 1 roster: prior-round data provided? If yes: all regressions listed? |
| C-08 | PASS / PARTIAL / FAIL / auto-PASS | Does every failure pattern entry conclude with a specific verb + artifact? Generic observations = FAIL. [TBD] |
| C-09 | PASS / PARTIAL / FAIL | 1-3 sentence commentary naming min/max scores and interpreting clustering vs. spread? |
| C-10 | PASS / PARTIAL / FAIL / auto-PASS | Are action lines instantiated with real artifact names and locations -- not left as fill-in-the-blank? Mix of instantiated and placeholder = PARTIAL. [TBD] |
| C-11 | PASS / PARTIAL / FAIL | Is there a preamble section (before the first "SCORING: [output]" heading) that explicitly declares auto-PASS status for each applicable criterion with a one-phrase justification? Inline-only (no preamble summary) = PARTIAL. |
| C-12 | PASS / PARTIAL / FAIL | Does the composite formula appear before the first per-output heading, showing N_essential=4, N_recommended=3, N_aspirational=5? Formula embedded only within output sections = PARTIAL. |

Composite:
  Essential:    C-01=[v] + C-02=[v] + C-03=[v] + C-04=[v] = [sum] / 4 * 60 = [pts]
  Recommended:  C-05=[v] + C-06=[v] + C-07=[v]            = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[v] + C-09=[v] + C-10=[v] + C-11=[v] + C-12=[v] = [sum] / 5 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes -- all 4 essentials PASS and score >= 80 / no -- which essential(s) failed or score < 80]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

Before writing any section, resolve TBD auto-PASS statuses from Phase 1 roster:
- C-05: [auto-PASS -- no criterion failed universally / scoring required -- reason]
- C-08: [auto-PASS -- no failure patterns / scoring required -- reason]
- C-10: [auto-PASS -- no failure patterns / scoring required -- reason]

Update any TBD cells in Phase 2 scoring tables to reflect resolved statuses.

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | yes/no |

Ties resolved alphabetically.

### Failure Patterns

[Any criterion FAIL or PARTIAL in EVERY scored output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design issue / data gap] -- [one sentence on why].
  Action: [fully instantiated: verb + artifact name + exact section -- do NOT write a
  placeholder like "Action: [verb + artifact]". Example: "Rewrite the criterion roster
  in quest-score.md PHASE 1 PREAMBLE to add C-10/C-11/C-12 rows so the model cannot
  omit them without a visibly empty table row."]

[If no universal failures: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair where one output outperforms the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence on the mechanism.]

[If all outputs scored identically: "No differential excellence detected."]

### Regression Signals

Prior-round scorecard: [provided / not provided]
[Provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]
[No regressions: "No regressions detected."]
[No data: "No prior-round scorecard provided -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: state min score, max score, whether scores cluster tightly or spread widely.
Comment on calibration: tight clustering may mean the rubric is too easy or too coarse; wide
spread means it discriminates well. Note if the expanded N_aspirational=5 denominator affected
ceiling scores relative to R1.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## Round 2 Design Notes

### Axis coverage

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Criterion roster (12 rows) | yes | -- | -- | yes | yes |
| Diagnostic questions (C-10/C-11/C-12) | -- | yes | -- | -- | yes |
| Two-gate preamble | -- | -- | yes | yes | yes |
| Evidence-first (Step A -> Step B) | -- | -- | -- | yes | yes |
| Worked example mandate ("no fill-in-the-blank") | partial | partial | partial | partial | yes |
| TBD resolution at Phase 3 | yes | yes | yes | yes | yes |
| Formula at preamble with N_aspirational=5 | yes | yes | yes | yes | yes |

### C-01 risk model (expanded rubric)

C-01 now requires 12 rows x N outputs. Any variation using a 9-row R1 template will FAIL C-01.
The criterion roster (V-01, V-04, V-05) prints all 12 rows in setup, making omission structurally
visible. V-02 and V-03 rely on instruction compliance ("read the rubric; note all 12 criteria")
without a structural row guarantee.

### C-11 and C-12 risk model

C-11 and C-12 are self-referential: they test whether the scored output has a preamble and
formula before its first per-output section. A variation that does not have a preamble gate
cannot reliably score C-11/C-12 on other outputs while satisfying them itself. The two-gate
preamble (V-03, V-04, V-05) enforces this structurally. V-01 and V-02 put formula and auto-PASS
rules in a setup section, which satisfies C-11/C-12 for the scorecard output, but the diagnostic
questions in V-02 are the only mechanism ensuring the model actually evaluates these criteria on
the scored outputs.

### C-10 risk model

C-10 is the same mechanism as C-08 in R1: template hints produced PARTIAL; worked examples
produced PASS. R2 variations address this three ways:
- V-01/V-03/V-04: include a worked example in the failure patterns template
- V-02: diagnostic question explicitly asks "is the action line instantiated, not a template
  placeholder?"
- V-05: both a worked example AND the explicit "do NOT write a placeholder" instruction

### C-03 formula risk (N_aspirational change)

Any variation reproducing the v1 formula (aspirational_pass / 2 * 10) will produce wrong
composite scores. All R2 variations explicitly print N_aspirational = 5 and use the correct
denominator. C-12 additionally requires the formula with correct N values to appear before the
first per-output section, creating a double-enforcement surface.

### Predicted differentiation

| Dimension | Strongest | Why |
|-----------|----------|-----|
| C-01 structural guarantee | V-01, V-04, V-05 | 12-row roster pre-printed |
| C-02 structural guarantee | V-04, V-05 | Evidence-first Step A -> Step B |
| C-03 / C-12 formula accuracy | All five | N_aspirational=5 explicit in all |
| C-11 / C-12 structural guarantee | V-03, V-04, V-05 | Two-gate preamble phase |
| C-10 worked example | V-05 | "No fill-in-the-blank" mandate + worked template |
| C-10/C-11/C-12 interrogation depth | V-02, V-05 | Diagnostic questions force engagement |

### V-golden candidate

**V-05** is the synthesis target:
- Roster closes C-01 (12 rows, expanded rubric)
- Evidence-first closes C-02 (quote before verdict structurally enforced)
- Formula at preamble with N_aspirational=5 closes C-03 and C-12
- Preamble gate closes C-11 (auto-PASS declarations before first output heading)
- Worked example mandate + "no fill-in-the-blank" instruction closes C-10
- TBD mechanism correctly defers C-05/C-08/C-10 resolution to Phase 3
- Diagnostic questions in Step B prevent shallow verdicts on new criteria

**V-04** is the closest structural competitor: roster + two-gate + evidence-first.
C-10 is its likely gap: worked example template present but no explicit mandate.

**Open question for R2:** Does V-02's diagnostic-question register produce higher C-11/C-12
compliance than V-01's roster-only approach, even without a preamble gate? The diagnostic
questions force the model to interrogate whether the scored output has a preamble -- but they
do not enforce that the scorecard output itself has one.
