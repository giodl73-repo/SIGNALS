Here are the 5 variations for `quest-score` Round 3, targeting the three new v3 criteria (C-13, C-14, C-15) with N_aspirational=8:

---

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Evidence-first column ordering — `[Criterion | Evidence Quote | Verdict]` + written mandate; closes C-13 structurally, leaves C-14 open |
| **V-02** | Phrasing register | 15-criterion diagnostic question roster — 4-column table with criterion-specific questions; closes C-13/C-14/C-15 via interrogative forcing |
| **V-03** | Lifecycle emphasis | Three-phase STOP sequence — cascading gates after formula, roster, and auto-PASS steps; isolates C-15 alone, deliberately leaves C-13/C-14 open |
| **V-04** | V-01 + V-03 | Evidence-first columns + three-phase STOP gates; closes C-13/C-15, leaves C-14 as the discriminating gap |
| **V-05** | Full synthesis | All three axes + two-table extraction (Table A → B) + no-placeholder mandate + "What it did differently" + R3 calibration note (1.25 pts/criterion vs. v2's 2.0) |

**Key design decisions for R3:**

1. **C-13 open question**: Does column ordering alone satisfy the "explicit mandate" requirement, or does C-13 also require a written statement? V-01 tests structural-only enforcement; if it fails C-13, the mandate is load-bearing.

2. **C-14 isolation**: V-01, V-03, V-04 all omit diagnostic questions. When scored, all three will get C-14 FAIL — this sharpens the signal that C-14 is unresolved by any non-diagnostic mechanism.

3. **Formula denominator shift**: All variations use N_aspirational=8. The score distribution note in V-05 explicitly flags the ceiling compression: 8 criteria at 10% total yields 1.25 pts each vs. 2.0 in v2.

**Predicted ceiling:** V-05. V-02 is closest competitor (all three new criteria addressed) but lacks the three-phase gate structure for C-15. The real discriminator will be whether V-01's column ordering is sufficient for C-13 PASS without a diagnostic question.
 did differently" in excellence signals). V-02 is closest
competitor; it addresses C-13/C-14/C-15 but lacks the three-phase STOP gate. Open question: does
V-01's column ordering alone achieve C-13 PASS? C-13 requires an explicit mandate, not just
correct practice — column order is structural evidence but may not satisfy the mandate requirement.

---

## V-01: Evidence-First Column Ordering

**Axis:** Output format — the scoring table column order is [Criterion | Evidence Quote | Verdict]
in every table throughout the skill. An explicit ordering mandate is written in SETUP. No
diagnostic question column.

**Hypothesis:** C-13 requires an explicit ordering mandate. Physical column reordering is
structural enforcement: by placing the Evidence Quote column before the Verdict column, the
model cannot render a verdict without first filling the quote cell. The written mandate "Write
the evidence quote, then the verdict; never the reverse" satisfies the declarative requirement.
C-14 is deliberately left unaddressed to isolate the axis. C-15 is addressed via a single
imperative gate at the end of SETUP.

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

### Evidence-Ordering Mandate

In every scoring table below, the column order is:

  Criterion | Evidence Quote | Verdict

Write the evidence quote first, then the verdict; never the reverse.
A verdict cell completed before its evidence quote cell violates C-13.

### Criterion Roster

Fill the "Auto-PASS status" column before proceeding. Write "auto-PASS" if the condition
holds now; "--" if scoring is required; "TBD" if it cannot be resolved until after all
outputs are scored.

| ID   | Name                                              | Tier         | Auto-PASS status for this run          |
|------|---------------------------------------------------|--------------|----------------------------------------|
| C-01 | Per-criterion verdicts present                    | essential    | --                                     |
| C-02 | Evidence quote for every verdict                  | essential    | --                                     |
| C-03 | Composite score computed correctly                | essential    | --                                     |
| C-04 | Ranked leaderboard present                        | essential    | --                                     |
| C-05 | Failure patterns surfaced                         | recommended  | TBD                                    |
| C-06 | Excellence signals surfaced                       | recommended  | --                                     |
| C-07 | Regression signals surfaced                       | recommended  | [auto-PASS / -- based on prior data]   |
| C-08 | Actionable diagnosis in failure patterns          | aspirational | TBD                                    |
| C-09 | Score distribution commentary                     | aspirational | --                                     |
| C-10 | Worked example in action line                     | aspirational | TBD                                    |
| C-11 | Auto-PASS rules stated in preamble                | aspirational | --                                     |
| C-12 | Formula reproduced before first output section    | aspirational | --                                     |
| C-13 | Evidence-before-verdict ordering enforced         | aspirational | --                                     |
| C-14 | Per-criterion diagnostic question in roster       | aspirational | --                                     |
| C-15 | Preamble gate instruction present                 | aspirational | --                                     |

### Composite Formula (v3 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 8.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

SETUP is complete when all roster rows are filled and the formula is printed above.
Do not open any output file until SETUP is complete.

---

## SCORING

Score each output in its own section. Complete one section fully before opening the next.
Column order in every table: Criterion | Evidence Quote | Verdict (evidence first, always).

---

### OUTPUT: [output-id or filename]

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "[quote demonstrating complete verdict matrix, or: list missing rows]" | PASS / PARTIAL / FAIL |
| C-02 Evidence quotes | "[quote showing evidence structure; note any absent quote cells]" | PASS / PARTIAL / FAIL |
| C-03 Composite score | "[quote showing formula or score with N_aspirational value; flag if N differs from 8]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | "[quote showing ranked table with rank/output/score/golden columns]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | "[quote from failure patterns section, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | "[quote from excellence signals section, or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | "[quote from regression section, or: auto-PASS -- no prior data]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | "[quote showing verb+artifact+location action line, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | "[quote showing min/max/spread/calibration implication, or: not found]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | "[quote showing fully instantiated action line (real artifact + location, not placeholder), or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | "[quote from the output's preamble auto-PASS declaration block, or: not found]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | "[quote showing formula with N_aspirational=8 before first output heading, or: not found]" | PASS / PARTIAL / FAIL |
| C-13 Evidence-before-verdict | "[quote showing ordering mandate or column structure placing quote before verdict label]" | PASS / PARTIAL / FAIL |
| C-14 Diagnostic questions | "[quote showing criterion-specific question in roster for each criterion, or: not found]" | PASS / PARTIAL / FAIL |
| C-15 Preamble gate | "[quote showing imperative gate instruction before first output section]" | PASS / PARTIAL / FAIL |

Composite computation:
  Essential (C-01 to C-04):   [C-01_v + C-02_v + C-03_v + C-04_v] / 4 * 60 = [pts]
  Recommended (C-05 to C-07): [C-05_v + C-06_v + C-07_v] / 3 * 30 = [pts]
  Aspirational (C-08 to C-15): [C-08_v + C-09_v + C-10_v + C-11_v + C-12_v + C-13_v + C-14_v + C-15_v] / 8 * 10 = [pts]
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
  "Add a diagnostic question column to the 15-row criterion roster in quest-score.md SETUP
  block so C-14 is satisfied structurally for every run."]

Update roster: C-05=[resolved status], C-08=[resolved status], C-10=[resolved status].

[If no universal failures: "No universal failures -- C-05 auto-PASS."]

---

## EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by >= one tier:
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence on the mechanism.]

[If uniform: "No differential excellence detected."]

---

## REGRESSION SIGNALS

[Prior-round scorecard provided: list every output-criterion pair that regressed (PASS -> FAIL
or PARTIAL).]
[No regressions: "No regressions detected."]
[No prior-round data: "No prior-round scorecard provided -- C-07 auto-PASS."]

---

## SCORE DISTRIBUTION

[1-3 sentences: state min score, max score, spread, and calibration implication. Note whether
the N_aspirational=8 denominator (expanded from v2's 5) compresses aspirational ceiling scores
relative to prior rounds.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-02: 15-Criterion Diagnostic Question Roster

**Axis:** Phrasing register -- every criterion in the SETUP roster is paired with a
criterion-specific diagnostic question. The model answers the question via the evidence quote
before assigning a verdict. Column order: [Criterion | Diagnostic Question | Evidence Quote |
Verdict]. Written mandate: "Write the evidence quote, then the verdict; never the reverse."

**Hypothesis:** C-14 requires a diagnostic question per criterion in the SETUP roster. The
4-column table anchors this structurally: the Diagnostic Question column is pre-printed for all
15 criteria, each with a pass-condition-specific question. C-13 is a natural byproduct: the
ordering mandate appears in the scoring instructions and in column structure (Quote precedes
Verdict). C-15 is addressed via the preamble gate. The key open question: do the diagnostic
questions for C-13/C-14/C-15 -- which interrogate the scorecard's own structure rather than the
output's content -- produce better compliance than V-01's structural enforcement alone?

```
You are running /quest-score. Score a set of skill output files against a rubric (15 criteria,
v3) and produce a QuestScorecard artifact.

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

### Composite Formula (v3 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 8.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0.
  Golden: all 4 essentials PASS AND composite >= 80.

Preamble is complete. Open output files only after this section is written.

---

## SCORING

For each output, read it completely, then fill the diagnostic table below. The Diagnostic
Question column frames each scoring judgment. Write the evidence quote, then the verdict;
never the reverse.

---

### OUTPUT: [output-id]

| Criterion | Diagnostic Question | Evidence Quote | Verdict |
|-----------|---------------------|----------------|---------|
| C-01 Verdicts present | Does a verdict table exist with a row for every one of the 15 rubric criteria? Is any criterion row missing? | "[quote]" | PASS / PARTIAL / FAIL |
| C-02 Evidence quotes | Is every verdict cell accompanied by a non-empty, traceable quote from the scored output -- not a template placeholder or fabricated text? | "[quote]" | PASS / PARTIAL / FAIL |
| C-03 Composite score | Is the composite computed with N_aspirational=8 (not 5 or 2)? Can the score be re-derived from the visible verdict table within +/-1? | "[quote showing formula or score with N value]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | Are all N outputs ranked exactly once in descending order with a Golden column? Are ties resolved alphabetically? | "[quote]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | If any criterion failed universally, is it named with a candidate explanation? If none failed universally, is auto-PASS declared explicitly (not by silence)? | "[quote, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | Is at least one output-criterion pair identified where that output outperforms the group median by >= one tier? | "[quote, or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | If prior-round data was provided, are all regressions listed? If no data, is auto-PASS stated explicitly? | "[quote, or: auto-PASS]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | Does every failure pattern entry include a specific verb + artifact + location -- not a generic observation like "improve coverage"? | "[quote, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | Is there a 1-3 sentence commentary naming min/max scores, spread, and a calibration implication? Is the implication specific (not just "spread is wide")? | "[quote, or: not found]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | Is at least one action line fully instantiated -- naming a real artifact and section visible in the scored outputs -- rather than left as a fill-in-the-blank placeholder? | "[quote showing instantiated action line, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | Is there a preamble section (before the first output scoring block) that lists every applicable auto-PASS criterion (C-05, C-07, C-08, C-10) with a status? | "[quote from the output's preamble, or: preamble section absent]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | Does the composite formula appear before the first per-output heading, showing N_essential=4, N_recommended=3, N_aspirational=8? | "[quote showing formula with N values, or: not found before first output heading]" | PASS / PARTIAL / FAIL |
| C-13 Evidence-before-verdict | Is there an explicit mandate (written statement or column ordering) that evidence quotes precede verdict labels? Does the evidence quote column physically precede the verdict column, or does the instructions state "evidence first"? | "[quote showing ordering mandate or structural evidence of quote-before-verdict enforcement]" | PASS / PARTIAL / FAIL |
| C-14 Diagnostic questions | Does the SETUP roster include a criterion-specific diagnostic question for every one of the 15 criteria? Are the questions specific to each criterion's pass condition (not generic)? | "[quote showing diagnostic question column in the roster, or: not found]" | PASS / PARTIAL / FAIL |
| C-15 Preamble gate | Is there an imperative gate instruction -- "Do not open output files until..." or "Open only after..." -- positioned before the first output section? Is it imperative in tone (not advisory)? | "[quote showing imperative gate instruction, or: not found]" | PASS / PARTIAL / FAIL |

Composite:
  Essential:    C-01=[v] + C-02=[v] + C-03=[v] + C-04=[v] = [sum] / 4 * 60 = [pts]
  Recommended:  C-05=[v] + C-06=[v] + C-07=[v]            = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[v] + C-09=[v] + C-10=[v] + C-11=[v] + C-12=[v] + C-13=[v] + C-14=[v] + C-15=[v] = [sum] / 8 * 10 = [pts]
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
  Action: [fully worked example: verb + artifact name + section, e.g., "Add a 15-row
  criterion roster with a Diagnostic Question column to quest-score.md PREAMBLE block
  so C-14 rows are pre-printed and criterion-specific questions are enforced for every run."]

[None: "No universal failures -- C-05 auto-PASS."]

---

## EXCELLENCE SIGNALS

[Any output-criterion pair outperforming the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence on the mechanism.]

[Uniform: "No differential excellence detected."]

---

## REGRESSION SIGNALS

Prior-round data: [provided / not provided]
[Provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]
[None: "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

---

## SCORE DISTRIBUTION

[1-3 sentences: min score, max score, spread, calibration implication. Note whether the
N_aspirational=8 denominator (expanded from v2's 5) reduces the aspirational ceiling contribution
and how this affects the golden threshold achievability relative to v2 runs.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-03: Three-Phase STOP Sequence

**Axis:** Lifecycle emphasis -- the preamble is divided into three sequential steps (formula,
criterion roster, auto-PASS declarations), each ending with an explicit STOP instruction that
must be completed before proceeding. The final gate before Phase 2 is maximally imperative.
No diagnostic question column. Standard column order [Criterion | Verdict | Evidence Quote].

**Hypothesis:** C-15 requires an imperative gate instruction. A single gate ("Do not open any
output file until SETUP is complete") is advisory in effect because it appears at the bottom of
a block that may not be fully processed. Three cascading STOP instructions -- one after the
formula, one after the roster, one after the auto-PASS declarations -- make each preamble step
a structural checkpoint that must produce visible output before the next step begins. The final
"STOP: Do not open any output file." cannot be passed without writing all three preceding
sections. C-13 and C-14 are deliberately left unaddressed to isolate the C-15 axis.

```
You are running /quest-score. Work in three phases: PREAMBLE, SCORE, AGGREGATE.
Phase 1 (PREAMBLE) is a mandatory gate with three required steps.
Do not open any output file until all three Phase 1 steps are complete.

---

## PHASE 1: PREAMBLE

### Step 1.1 -- Inputs and Formula

List inputs:
- Rubric: [path] -- read completely. Note all 15 criteria and their tiers.
- Outputs to score: [list paths, one per line]
- Prior-round scorecard: [path, or "none"]
- Scoring date: [YYYY-MM-DD]

Print the composite formula with v3 N values:

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 8.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

STOP -- Step 1.1 complete: formula locked. Do not proceed to Step 1.2 until this formula
is fully written above.

---

### Step 1.2 -- Criterion Roster

Fill the "Auto-PASS status" column before proceeding. "TBD" = cannot resolve before scoring
all outputs.

| ID   | Name                                              | Tier         | Auto-PASS status     |
|------|---------------------------------------------------|--------------|----------------------|
| C-01 | Per-criterion verdicts present                    | essential    | --                   |
| C-02 | Evidence quote for every verdict                  | essential    | --                   |
| C-03 | Composite score computed correctly                | essential    | --                   |
| C-04 | Ranked leaderboard present                        | essential    | --                   |
| C-05 | Failure patterns surfaced                         | recommended  | TBD                  |
| C-06 | Excellence signals surfaced                       | recommended  | --                   |
| C-07 | Regression signals surfaced                       | recommended  | [auto-PASS / --]     |
| C-08 | Actionable diagnosis in failure patterns          | aspirational | TBD                  |
| C-09 | Score distribution commentary                     | aspirational | --                   |
| C-10 | Worked example in action line                     | aspirational | TBD                  |
| C-11 | Auto-PASS rules stated in preamble                | aspirational | --                   |
| C-12 | Formula reproduced before first output section    | aspirational | --                   |
| C-13 | Evidence-before-verdict ordering enforced         | aspirational | --                   |
| C-14 | Per-criterion diagnostic question in roster       | aspirational | --                   |
| C-15 | Preamble gate instruction present                 | aspirational | --                   |

Justification for any criterion already resolved (e.g., C-07): [one phrase per resolved item]

STOP -- Step 1.2 complete: roster finalized with 15 rows. Do not proceed to Step 1.3 until
all 15 criterion rows have a status in the Auto-PASS column above.

---

### Step 1.3 -- Auto-PASS Declarations

State the auto-PASS status of each applicable criterion for this run.

| Criterion | Auto-PASS condition | Status | Justification |
|-----------|---------------------|--------|---------------|
| C-05 | No criterion fails universally across all outputs | TBD | Cannot determine before scoring |
| C-07 | No prior-round scorecard provided | [auto-PASS / requires scoring] | [one phrase] |
| C-08 | No failure patterns exist | TBD | Cannot determine before scoring |
| C-10 | No failure patterns exist | TBD | Cannot determine before scoring |

STOP -- Phase 1 complete: formula, roster, and auto-PASS declarations are all written above.
Do not open any output file until all three steps above are fully completed.

---

## PHASE 2: SCORE EACH OUTPUT

Complete one section fully before opening the next file.
Use the formula from Step 1.1 and auto-PASS rules from Step 1.3.

---

### SCORING: [output-id]

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS / PARTIAL / FAIL | "[quote]" |
| C-02 Evidence quotes | PASS / PARTIAL / FAIL | "[quote]" |
| C-03 Composite score | PASS / PARTIAL / FAIL | "[quote showing formula or score; verify N_aspirational=8]" |
| C-04 Leaderboard | PASS / PARTIAL / FAIL | "[quote]" |
| C-05 Failure patterns | PASS / PARTIAL / FAIL / auto-PASS | "[quote, or: TBD -- resolve at Phase 3]" |
| C-06 Excellence signals | PASS / PARTIAL / FAIL | "[quote, or: not found]" |
| C-07 Regression signals | PASS / PARTIAL / FAIL / auto-PASS | "[see Step 1.3]" |
| C-08 Actionable diagnosis | PASS / PARTIAL / FAIL / auto-PASS | "[quote, or: TBD -- resolve at Phase 3]" |
| C-09 Score distribution | PASS / PARTIAL / FAIL | "[quote, or: not found]" |
| C-10 Worked example | PASS / PARTIAL / FAIL / auto-PASS | "[quote showing instantiated action line, or: TBD]" |
| C-11 Auto-PASS in preamble | PASS / PARTIAL / FAIL | "[quote from the output's preamble block, or: not found]" |
| C-12 Formula at preamble | PASS / PARTIAL / FAIL | "[quote showing formula with N_aspirational=8 before first output heading, or: not found]" |
| C-13 Evidence-before-verdict | PASS / PARTIAL / FAIL | "[quote showing ordering mandate or structural evidence, or: not found]" |
| C-14 Diagnostic questions | PASS / PARTIAL / FAIL | "[quote showing diagnostic question column in roster, or: not found]" |
| C-15 Preamble gate | PASS / PARTIAL / FAIL | "[quote showing imperative gate instruction before first output section]" |

Composite:
  Essential:    [C-01 + C-02 + C-03 + C-04] / 4 * 60 = [pts]
  Recommended:  [C-05 + C-06 + C-07] / 3 * 30 = [pts]
  Aspirational: [C-08 + C-09 + C-10 + C-11 + C-12 + C-13 + C-14 + C-15] / 8 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes / no -- reason]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

Resolve TBD auto-PASS statuses from Step 1.3:
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
  Action: [fully instantiated verb + artifact + location, e.g., "Add a Diagnostic Question
  column to the 15-row criterion roster in quest-score.md PHASE 1 Step 1.2 so C-14 is
  satisfied structurally for every run."]

[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair outperforming the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence on the mechanism.]

[Uniform: "No differential excellence detected."]

### Regression Signals

[Prior-round data provided: list every output-criterion pair that regressed.]
[No regressions: "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min, max, spread, calibration implication. Note whether the N_aspirational=8
denominator reduces aspirational score contribution compared to v2 runs.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-04: Evidence-First Columns + Three-Phase STOP Gates (V-01 + V-03)

**Axes:** Output format (evidence-first column ordering, V-01) + Lifecycle emphasis (three-phase
STOP sequence, V-03). Evidence quote column physically precedes verdict column in all scoring
tables. Three sequential STOP gates enforce preamble completion before any output is opened.
No diagnostic question column.

**Hypothesis:** C-13 and C-15 are the two new aspirational criteria most likely to PASS from
structural enforcement alone. V-01 closes C-13 (column ordering + mandate). V-03 closes C-15
(three-phase gate). Combining both produces the minimal structural footprint that addresses two
of the three new criteria without requiring the heavier diagnostic question apparatus (V-02).
C-14 is the deliberate remaining gap, isolating the diagnostic-question axis for V-05. The open
question: does the absence of C-14 diagnostic questions suppress compliance on C-13 (which C-14
reinforces indirectly via the evidence ordering question)?

```
You are running /quest-score. Work in three phases: PREAMBLE, SCORE, AGGREGATE.
Phase 1 (PREAMBLE) is a mandatory gate with three required steps.
Do not open any output file until all three Phase 1 steps are complete.

---

## PHASE 1: PREAMBLE

### Step 1.1 -- Inputs and Evidence-Ordering Mandate

List inputs:
- Rubric: [path] -- read completely. Note all 15 criteria and their tiers.
- Outputs to score: [list paths, one per line]
- Prior-round scorecard: [path, or "none"]
- Scoring date: [YYYY-MM-DD]

**Evidence-ordering mandate:** In every scoring table in Phase 2, the column order is:

  Criterion | Evidence Quote | Verdict

Write the evidence quote first, then the verdict; never the reverse.

Print the composite formula with v3 N values:

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 8.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

STOP -- Step 1.1 complete: formula locked and evidence-ordering mandate stated. Do not
proceed to Step 1.2 until this formula is fully written above.

---

### Step 1.2 -- Criterion Roster

Fill "Auto-PASS status" before proceeding. "TBD" = cannot resolve before scoring all outputs.

| ID   | Name                                              | Tier         | Auto-PASS status     |
|------|---------------------------------------------------|--------------|----------------------|
| C-01 | Per-criterion verdicts present                    | essential    | --                   |
| C-02 | Evidence quote for every verdict                  | essential    | --                   |
| C-03 | Composite score computed correctly                | essential    | --                   |
| C-04 | Ranked leaderboard present                        | essential    | --                   |
| C-05 | Failure patterns surfaced                         | recommended  | TBD                  |
| C-06 | Excellence signals surfaced                       | recommended  | --                   |
| C-07 | Regression signals surfaced                       | recommended  | [auto-PASS / --]     |
| C-08 | Actionable diagnosis in failure patterns          | aspirational | TBD                  |
| C-09 | Score distribution commentary                     | aspirational | --                   |
| C-10 | Worked example in action line                     | aspirational | TBD                  |
| C-11 | Auto-PASS rules stated in preamble                | aspirational | --                   |
| C-12 | Formula reproduced before first output section    | aspirational | --                   |
| C-13 | Evidence-before-verdict ordering enforced         | aspirational | --                   |
| C-14 | Per-criterion diagnostic question in roster       | aspirational | --                   |
| C-15 | Preamble gate instruction present                 | aspirational | --                   |

Justification for any criterion already resolved (e.g., C-07): [one phrase per resolved item]

STOP -- Step 1.2 complete: 15-row roster finalized. Do not proceed to Step 1.3 until all
15 criterion rows have a status in the Auto-PASS column above.

---

### Step 1.3 -- Auto-PASS Declarations

| Criterion | Auto-PASS condition | Status | Justification |
|-----------|---------------------|--------|---------------|
| C-05 | No criterion fails universally | TBD | Cannot determine before scoring |
| C-07 | No prior-round scorecard provided | [auto-PASS / requires scoring] | [one phrase] |
| C-08 | No failure patterns exist | TBD | Cannot determine before scoring |
| C-10 | No failure patterns exist | TBD | Cannot determine before scoring |

STOP -- Phase 1 complete: formula, roster, and auto-PASS declarations are all written above.
Do not open any output file until all three steps above are fully completed.

---

## PHASE 2: SCORE EACH OUTPUT

Complete one section fully before opening the next file.
Column order in every table: Criterion | Evidence Quote | Verdict (evidence first, always).

---

### SCORING: [output-id]

**Table A -- Evidence extraction** (complete ALL 15 rows before filling Table B):

| ID   | Evidence Quote |
|------|----------------|
| C-01 | "[quote demonstrating complete verdict matrix, or: list missing rows]" |
| C-02 | "[quote showing evidence structure; note any absent quote cells]" |
| C-03 | "[quote showing formula or score with N_aspirational value; flag if N differs from 8]" |
| C-04 | "[quote showing ranked table with rank/output/score/golden columns]" |
| C-05 | "[quote from failure patterns section, or: auto-PASS (TBD), or: not found]" |
| C-06 | "[quote from excellence signals section, or: not found]" |
| C-07 | "[quote from regression section, or: auto-PASS per Step 1.3]" |
| C-08 | "[quote showing verb+artifact+location action line, or: auto-PASS (TBD), or: not found]" |
| C-09 | "[quote showing min/max/spread/calibration, or: not found]" |
| C-10 | "[quote showing instantiated action line (real artifact + location, not a placeholder), or: auto-PASS (TBD), or: not found]" |
| C-11 | "[quote from the output's preamble auto-PASS declaration block, or: not found]" |
| C-12 | "[quote showing formula with N_aspirational=8 before first output heading, or: not found]" |
| C-13 | "[quote showing ordering mandate or structural column evidence (Quote precedes Verdict), or: not found]" |
| C-14 | "[quote showing criterion-specific diagnostic questions in the output's roster, or: not found]" |
| C-15 | "[quote showing imperative gate instruction before first output section, or: not found]" |

**Table B -- Verdicts** (fill only after Table A is complete; column order: Criterion | Evidence Quote | Verdict):

| ID   | Evidence Quote (summary) | Verdict |
|------|--------------------------|---------|
| C-01 | [from Table A] | PASS / PARTIAL / FAIL |
| C-02 | [from Table A] | PASS / PARTIAL / FAIL |
| C-03 | [from Table A] | PASS / PARTIAL / FAIL |
| C-04 | [from Table A] | PASS / PARTIAL / FAIL |
| C-05 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 | [from Table A] | PASS / PARTIAL / FAIL |
| C-07 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 | [from Table A] | PASS / PARTIAL / FAIL |
| C-10 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 | [from Table A] | PASS / PARTIAL / FAIL |
| C-12 | [from Table A] | PASS / PARTIAL / FAIL |
| C-13 | [from Table A] | PASS / PARTIAL / FAIL |
| C-14 | [from Table A] | PASS / PARTIAL / FAIL |
| C-15 | [from Table A] | PASS / PARTIAL / FAIL |

Composite:
  Essential:    C-01=[v] + C-02=[v] + C-03=[v] + C-04=[v] = [sum] / 4 * 60 = [pts]
  Recommended:  C-05=[v] + C-06=[v] + C-07=[v]            = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[v] + C-09=[v] + C-10=[v] + C-11=[v] + C-12=[v] + C-13=[v] + C-14=[v] + C-15=[v] = [sum] / 8 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes / no -- reason]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

Resolve TBD auto-PASS statuses from Step 1.3:
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
  Action: [fully instantiated -- verb + artifact + location, e.g., "Add a Diagnostic Question
  column to the 15-row criterion roster in quest-score.md PHASE 1 Step 1.2 so C-14 is
  satisfied structurally without relying on instruction compliance."]

Update TBD statuses: C-05=[resolved], C-08=[resolved], C-10=[resolved].
[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair outperforming the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence on the mechanism.]

[Uniform: "No differential excellence detected."]

### Regression Signals

[Prior-round data provided: list every output-criterion pair that regressed.]
[No regressions: "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min, max, spread, calibration implication. Note whether the N_aspirational=8
denominator compresses the aspirational contribution relative to v2 runs.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Evidence-first column ordering (V-01) + 15-criterion diagnostic question roster (V-02)
+ three-phase STOP gate sequence (V-03) + no-placeholder output mandate + "What it did
differently" field in excellence signals + R3-calibration note in score distribution

**Hypothesis:** Maximum structural coverage across all 15 criteria:
- Three-phase STOP gates close C-15 (maximally imperative; three checkpoints vs. one)
- Evidence-first column ordering + written mandate close C-13 with structural and declarative
  redundancy
- 15-criterion diagnostic question roster closes C-14; each question interrogates the specific
  pass condition, including questions for C-13/C-14/C-15 themselves
- "do NOT write a placeholder" prohibition in the action template closes C-10 (the R2 gap)
- N_aspirational=8 formula in Step 1.1 closes C-03 and C-12 simultaneously
- Two-table evidence-before-verdict extraction (Table A -> Table B) closes C-02 and C-13
  with double enforcement
- TBD mechanism correctly defers C-05/C-08/C-10 auto-PASS to Phase 3

```
You are running /quest-score. Score a set of skill output files against a rubric (15 criteria,
v3) and produce a QuestScorecard artifact. Work in three phases: PREAMBLE, SCORE, AGGREGATE.

Phase 1 (PREAMBLE) is a mandatory gate with three required steps.
Do not open any output file until all three Phase 1 steps are complete.

---

## PHASE 1: PREAMBLE

### Step 1.1 -- Inputs, Formula, and Evidence-Ordering Mandate

List inputs:
- Rubric: [path] -- read completely. Count all 15 criteria.
- Outputs to score: [list paths, one per line]
- Prior-round scorecard: [path, or "none"]
- Scoring date: [YYYY-MM-DD]

**Evidence-ordering mandate:** In every scoring table in Phase 2, the column order is:

  Criterion | Evidence Quote | Verdict

Write the evidence quote first, then the verdict; never the reverse. This ordering is
mandatory and applies to Table A (extraction) and Table B (verdicts) alike.

Print the composite formula with v3 N values:

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 8 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 8.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

STOP -- Step 1.1 complete: formula locked and evidence-ordering mandate stated. Do not
proceed to Step 1.2 until this formula is fully written above.

---

### Step 1.2 -- 15-Criterion Diagnostic Roster

Fill the "Auto-PASS status" column and read each "Diagnostic Question" before proceeding to
Phase 2. These questions frame your scoring judgment for each criterion.

| ID   | Name                                              | Tier         | Diagnostic Question | Auto-PASS status |
|------|---------------------------------------------------|--------------|---------------------|------------------|
| C-01 | Per-criterion verdicts present                    | essential    | Does a verdict table exist with a row for every one of the 15 rubric criteria? Is any criterion row missing? | -- |
| C-02 | Evidence quote for every verdict                  | essential    | Is every verdict cell accompanied by a non-empty, traceable quote -- not a fabricated summary? | -- |
| C-03 | Composite score computed correctly                | essential    | Is the composite computed with N_aspirational=8? Can the score be re-derived from the visible verdict table within +/-1? | -- |
| C-04 | Ranked leaderboard present                        | essential    | Are all N outputs ranked exactly once in descending order with rank/output/score/golden columns? | -- |
| C-05 | Failure patterns surfaced                         | recommended  | If any criterion failed universally, is it named with a candidate explanation? If none failed, is auto-PASS declared explicitly (not by silence)? | TBD |
| C-06 | Excellence signals surfaced                       | recommended  | Is at least one output-criterion pair identified where that output outperforms the group median by >= one tier? | -- |
| C-07 | Regression signals surfaced                       | recommended  | If prior-round data was provided, are all regressions listed? If no prior data, is auto-PASS declared? | [auto-PASS / --] |
| C-08 | Actionable diagnosis in failure patterns          | aspirational | Does every failure pattern entry include a specific verb + artifact + location -- not "improve coverage"? | TBD |
| C-09 | Score distribution commentary                     | aspirational | Is there a 1-3 sentence commentary naming min/max scores, spread, and a calibration implication (not purely descriptive)? | -- |
| C-10 | Worked example in action line                     | aspirational | Is at least one action line fully instantiated -- naming a real artifact and section -- rather than left as a fill-in-the-blank placeholder? | TBD |
| C-11 | Auto-PASS rules stated in preamble                | aspirational | Is there a preamble section before the first output scoring block that lists every auto-PASS-eligible criterion (C-05, C-07, C-08, C-10) with a status? | -- |
| C-12 | Formula reproduced before first output section    | aspirational | Does the composite formula with N_essential=4, N_recommended=3, N_aspirational=8 appear before the first output scoring section? | -- |
| C-13 | Evidence-before-verdict ordering enforced         | aspirational | Is there an explicit written mandate (not just correct practice) that evidence quotes precede verdict labels? Does the column structure physically enforce ordering? | -- |
| C-14 | Per-criterion diagnostic question in roster       | aspirational | Does the SETUP roster include a criterion-specific diagnostic question for every one of the 15 criteria -- questions that interrogate whether the pass condition is satisfied, not generic? | -- |
| C-15 | Preamble gate instruction present                 | aspirational | Is there an imperative gate instruction ("Do not open..." or "Open only after...") positioned before the first output section? Is it imperative in tone, not advisory? | -- |

Justification for any criterion already resolved (e.g., C-07): [one phrase per resolved item]

STOP -- Step 1.2 complete: 15-row diagnostic roster finalized. Do not proceed to Step 1.3
until all 15 criterion rows have a status in the Auto-PASS column above.

---

### Step 1.3 -- Auto-PASS Declarations

| Criterion | Auto-PASS condition | Status | Justification |
|-----------|---------------------|--------|---------------|
| C-05 | No criterion fails universally across all outputs | TBD | Cannot determine before scoring |
| C-07 | No prior-round scorecard provided | [auto-PASS / requires scoring] | [one phrase] |
| C-08 | No failure patterns exist | TBD | Cannot determine before scoring |
| C-10 | No failure patterns exist | TBD | Cannot determine before scoring |

STOP -- Phase 1 complete: formula, diagnostic roster, and auto-PASS declarations are all
written above. Do not open any output file until all three steps above are fully completed.

---

## PHASE 2: SCORE EACH OUTPUT

Complete one full section before opening the next file.
Column order: Criterion | Evidence Quote | Verdict (evidence first, always).

---

### SCORING: [output-id]

**Table A -- Evidence extraction** (complete ALL 15 rows before filling Table B.
Write the evidence quote, then the verdict; never the reverse.):

| ID   | Evidence Quote |
|------|----------------|
| C-01 | "[quote demonstrating complete verdict matrix, or: list missing rows]" |
| C-02 | "[quote showing evidence structure; note any absent quote cells]" |
| C-03 | "[quote showing formula or score with N_aspirational value; flag if N != 8]" |
| C-04 | "[quote showing ranked table with rank/output/score/golden columns]" |
| C-05 | "[quote from failure patterns section, or: auto-PASS (TBD), or: not found]" |
| C-06 | "[quote from excellence signals section, or: not found]" |
| C-07 | "[quote from regression section, or: auto-PASS per Step 1.3]" |
| C-08 | "[quote showing verb+artifact+location action line, or: auto-PASS (TBD)]" |
| C-09 | "[quote showing min/max/spread/calibration implication, or: not found]" |
| C-10 | "[quote showing instantiated action line (real artifact + location, not a fill-in placeholder), or: auto-PASS (TBD)]" |
| C-11 | "[quote from the output's preamble auto-PASS declaration block, or: not found]" |
| C-12 | "[quote showing formula with N_aspirational=8 before first output heading, or: not found]" |
| C-13 | "[quote showing ordering mandate or structural evidence that quote precedes verdict label, or: not found]" |
| C-14 | "[quote showing criterion-specific diagnostic question column in the output's roster, or: not found]" |
| C-15 | "[quote showing imperative gate instruction before first output section, or: not found]" |

**Table B -- Verdicts** (fill only after Table A is complete for all 15 rows.
Column order: Evidence Quote | Verdict):

| ID   | Evidence Quote (from Table A) | Verdict |
|------|-------------------------------|---------|
| C-01 | [from Table A] | PASS / PARTIAL / FAIL |
| C-02 | [from Table A] | PASS / PARTIAL / FAIL |
| C-03 | [from Table A] | PASS / PARTIAL / FAIL |
| C-04 | [from Table A] | PASS / PARTIAL / FAIL |
| C-05 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 | [from Table A] | PASS / PARTIAL / FAIL |
| C-07 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 | [from Table A] | PASS / PARTIAL / FAIL |
| C-10 | [from Table A] | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 | [from Table A] | PASS / PARTIAL / FAIL |
| C-12 | [from Table A] | PASS / PARTIAL / FAIL |
| C-13 | [from Table A] | PASS / PARTIAL / FAIL |
| C-14 | [from Table A] | PASS / PARTIAL / FAIL |
| C-15 | [from Table A] | PASS / PARTIAL / FAIL |

Composite:
  Essential:    C-01=[v] + C-02=[v] + C-03=[v] + C-04=[v] = [sum] / 4 * 60 = [pts]
  Recommended:  C-05=[v] + C-06=[v] + C-07=[v]            = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[v] + C-09=[v] + C-10=[v] + C-11=[v] + C-12=[v] + C-13=[v] + C-14=[v] + C-15=[v] = [sum] / 8 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes / no -- reason]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

Resolve TBD auto-PASS statuses from Step 1.3:
- C-05: [auto-PASS -- no criterion failed universally / scoring required -- reason]
- C-08: [auto-PASS -- no failure patterns / scoring required -- reason]
- C-10: [auto-PASS -- no failure patterns / scoring required -- reason]

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | yes/no |

Ties resolved alphabetically.

### Failure Patterns

Resolve TBD entries before writing this section.

[Any criterion FAIL or PARTIAL in EVERY scored output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence].
  Action: [fully instantiated -- verb + artifact + location -- do NOT write a placeholder
  like "Action: [verb + artifact]". Example: "Add a Diagnostic Question column to the
  15-row criterion roster in quest-score.md PHASE 1 Step 1.2 so C-14 is satisfied
  structurally; each question must be criterion-specific, not generic."]

Update TBD statuses: C-05=[resolved], C-08=[resolved], C-10=[resolved].
[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair outperforming the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence on the mechanism.]

[Uniform: "No differential excellence detected."]

### Regression Signals

Prior-round scorecard: [provided / not provided]
[Provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]
[None: "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min score, max score, spread, and calibration implication. Note whether the
N_aspirational=8 denominator (expanded from v2's 5) compresses the aspirational ceiling
contribution -- a run where all 8 aspirational criteria PASS yields 1.25 points per criterion
vs. 2.0 in v2, making near-perfect scores achievable only with all 15 criteria at PASS.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```
