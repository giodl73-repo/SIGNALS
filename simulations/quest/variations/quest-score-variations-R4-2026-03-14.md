Here are the 5 variations for `quest-score` Round 4, targeting the two new v4 criteria (C-16, C-17) with N_aspirational=10:

---

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Named standalone auto-PASS declarations block — four conditions spelled out by criterion ID + trigger phrase; C-16 axis alone |
| **V-02** | Phrasing register | Criterion-specific mechanism-level diagnostic questions — each question names the count, named block, or format being tested; C-17 axis alone |
| **V-03** | Lifecycle emphasis | Front-loaded DECLARATIONS phase with three STOP gates — auto-PASS resolution is a first-class phase before formula or roster; structural C-16 variant |
| **V-04** | V-01 + V-02 | Named declarations + mechanism-level questions; both C-16 and C-17 addressed in combination |
| **V-05** | Full synthesis | All three axes + three-phase STOP gates + evidence-before-verdict mandate + no-placeholder mandate + score distribution calibration note |

**Key design decisions for R4:**

1. **C-16 isolation**: V-01 and V-03 test named-declaration enforcement via different structures — V-01 uses a standalone named block, V-03 makes it a first-class lifecycle phase. If both pass C-16, the mechanism is robust.

2. **C-17 isolation**: V-02 tests whether mechanism-interrogating questions ("Can you count exactly 17 verdict rows?") are qualitatively different from R3's V-02 questions ("Are the questions specific?"). The scoring will reveal whether C-17 is satisfied by any non-generic question or only by questions that name the specific trigger mechanism.

3. **N_aspirational shift**: v4 uses N=10. A FAIL on C-16 or C-17 now costs 1.0 pt (vs. 1.25 for a v3 aspirational fail). The golden threshold is marginally more achievable for near-complete runs.

4. **Regression hypothesis**: V-01 should inherit C-11 PASS from R3 V-05 (the named block satisfies both C-11 and C-16 simultaneously). If C-11 regresses in any variation, that's a signal the two criteria have diverged.
 single FAIL costs 1.0 pt. The ceiling for perfect aspirational is still 10 pts but is now spread across 10 criteria.

4. **Regression hypothesis**: V-01 through V-04 should inherit C-11 PASS (named block is the same mechanism that earned V-05's C-11 PASS in R3) and C-13/C-14/C-15 per their R3 performance. If any previously-passing criterion regresses, the regression is a signal.

**Predicted ceiling:** V-05. V-04 is closest competitor. Open question: does V-02's criterion-specific question formulation for C-16 (a structural criterion) earn C-17 PASS, or does C-17 require mechanism-interrogating questions that are qualitatively different from V-02's generic-but-criterion-paired questions from R3?

---

## V-01: Named Standalone Auto-PASS Declarations Block

**Axis:** Output format — the auto-PASS conditions are written as a named standalone block with
four explicit condition declarations, each keyed to a criterion ID and trigger phrase. Not a
roster column, not TBD markers, not conditions embedded in question phrasing.

**Hypothesis:** C-16 requires each auto-PASS condition to be spelled out as a named declaration
(e.g., "C-05 auto-PASS when no criterion fails universally across all scored outputs") rather
than implied by TBD placeholders or embedded in diagnostic question text. A standalone block
titled "Auto-PASS Conditions" with four named declarations achieves C-16 PASS. C-17 is
deliberately left unaddressed (uses generic placeholder questions). C-11 should also PASS
because the block satisfies both C-11's "stated in preamble" and C-16's "named standalone"
requirements simultaneously.

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

### Auto-PASS Conditions

The following criteria have auto-PASS conditions that may apply before any output is opened.
Evaluate each condition now and record the status for this run.

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status for this run: TBD (cannot resolve before scoring; resolve after all outputs are scored)

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status for this run: [auto-PASS if no prior scorecard listed above / "scoring required" if one is listed]
Justification: [one phrase]

**C-08 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS).**
Status for this run: TBD (resolves after C-05)

**C-10 auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS).**
Status for this run: TBD (resolves after C-05)

### Evidence-Ordering Mandate

In every scoring table below, the column order is:

  Criterion | Evidence Quote | Verdict

Write the evidence quote first, then the verdict; never the reverse.
A verdict cell completed before its evidence quote cell violates C-13.

### Criterion Roster

Fill the "Auto-PASS status" column using the conditions declared above. Write "auto-PASS"
if a condition above already resolves it; "--" if scoring is required; "TBD" if it depends
on scoring results.

| ID   | Name                                               | Tier         | Auto-PASS status |
|------|----------------------------------------------------|--------------|------------------|
| C-01 | Per-criterion verdicts present                     | essential    | --               |
| C-02 | Evidence quote for every verdict                   | essential    | --               |
| C-03 | Composite score computed correctly                 | essential    | --               |
| C-04 | Ranked leaderboard present                         | essential    | --               |
| C-05 | Failure patterns surfaced                          | recommended  | TBD              |
| C-06 | Excellence signals surfaced                        | recommended  | --               |
| C-07 | Regression signals surfaced                        | recommended  | [from above]     |
| C-08 | Actionable diagnosis in failure patterns           | aspirational | TBD              |
| C-09 | Score distribution commentary                      | aspirational | --               |
| C-10 | Worked example in action line                      | aspirational | TBD              |
| C-11 | Auto-PASS rules stated in preamble                 | aspirational | --               |
| C-12 | Formula reproduced before first output section     | aspirational | --               |
| C-13 | Evidence-before-verdict ordering enforced          | aspirational | --               |
| C-14 | Per-criterion diagnostic question in roster        | aspirational | --               |
| C-15 | Preamble gate instruction present                  | aspirational | --               |
| C-16 | Named standalone auto-PASS block                   | aspirational | --               |
| C-17 | Criterion-specific diagnostic questions            | aspirational | --               |

### Composite Formula (v4 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 10.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

SETUP is complete when the Auto-PASS Conditions block is filled, all roster rows are filled,
and the formula is printed above.
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
| C-03 Composite score | "[quote showing formula or score; flag if N_aspirational differs from 10]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | "[quote showing ranked table with rank/output/score/golden columns]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | "[quote from failure patterns section, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | "[quote from excellence signals section, or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | "[quote from regression section, or: auto-PASS -- no prior data]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | "[quote showing verb+artifact+location action line, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | "[quote showing min/max/spread/calibration implication, or: not found]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | "[quote showing fully instantiated action line, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | "[quote from the output's preamble auto-PASS section, or: not found]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | "[quote showing formula with N_aspirational=10 before first output heading]" | PASS / PARTIAL / FAIL |
| C-13 Evidence-before-verdict | "[quote showing ordering mandate or structural evidence of quote-before-verdict]" | PASS / PARTIAL / FAIL |
| C-14 Diagnostic questions | "[quote showing diagnostic question column in roster, or: not found]" | PASS / PARTIAL / FAIL |
| C-15 Preamble gate | "[quote showing imperative gate instruction before first output section]" | PASS / PARTIAL / FAIL |
| C-16 Named standalone auto-PASS block | "[quote from the output's named auto-PASS block with explicit condition declarations, or: conditions implied/embedded/absent]" | PASS / PARTIAL / FAIL |
| C-17 Criterion-specific diagnostic questions | "[quote showing a question that interrogates the specific mechanism of a criterion (not a generic probe), or: not found / generic only]" | PASS / PARTIAL / FAIL |

Composite computation:
  Essential (C-01 to C-04):    [C-01_v + C-02_v + C-03_v + C-04_v] / 4 * 60 = [pts]
  Recommended (C-05 to C-07):  [C-05_v + C-06_v + C-07_v] / 3 * 30 = [pts]
  Aspirational (C-08 to C-17): [sum of 10 values] / 10 * 10 = [pts]
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
  "Add a named Auto-PASS Conditions block to the SETUP section in quest-score.md with four
  explicit declarations (C-05, C-07, C-08, C-10) so C-16 is satisfied structurally for every run."]

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
the N_aspirational=10 denominator (expanded from v3's 8) further compresses the aspirational
ceiling contribution to 1.0 pt per criterion vs. v3's 1.25 pts, and how this affects golden
threshold achievability.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-02: Criterion-Specific Diagnostic Questions

**Axis:** Phrasing register — every diagnostic question in the SETUP roster interrogates the
specific mechanism of that criterion. Not "Is C-01 satisfied?" but "Can you count exactly
[N] verdict rows — one per rubric criterion from C-01 through C-17?" Each question names the
mechanism, the trigger phrase, or the structural feature that the criterion is testing.

**Hypothesis:** C-17 requires questions that interrogate the specific mechanism of the criterion
rather than a generic pass-condition paraphrase. R3's V-02 earned C-14 PASS because it had
"one question per criterion, criterion-specific (not generic)" — but the questions were written
at the pass-condition level, not the mechanism level. V-02 here upgrades every question to name
the measurable mechanism: count, presence of a named block, explicit verb+artifact+location
format, etc. C-16 is deliberately left unaddressed (auto-PASS block uses TBD markers, not
named declarations) to isolate the C-17 axis.

```
You are running /quest-score. Score a set of skill output files against a rubric (17 criteria,
v4) and produce a QuestScorecard artifact.

---

## PREAMBLE

Read the rubric completely before opening any output file. Then fill in this preamble.

### Auto-PASS Status

| Criterion | Condition | Status for this run |
|-----------|-----------|---------------------|
| C-05 | No criterion fails across ALL scored outputs | TBD |
| C-07 | No prior-round scorecard provided | [auto-PASS / scoring required] |
| C-08 | No failure patterns exist | TBD |
| C-10 | No failure patterns exist | TBD |

### Composite Formula (v4 N values)

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 10.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0.
  Golden: all 4 essentials PASS AND composite >= 80.

Preamble is complete. Open output files only after this section is written.

---

## SCORING

For each output, read it completely, then fill the diagnostic table below. Each Diagnostic
Question names the specific mechanism to check. Write the evidence quote first, then the
verdict; never the reverse.

---

### OUTPUT: [output-id]

| Criterion | Diagnostic Question | Evidence Quote | Verdict |
|-----------|---------------------|----------------|---------|
| C-01 Verdicts present | Can you count exactly 17 verdict rows — one for each rubric criterion from C-01 through C-17 — in the output's scoring table? Name any missing rows. | "[quote]" | PASS / PARTIAL / FAIL |
| C-02 Evidence quotes | For each of the 17 verdict rows, is there a non-empty quote cell? Pick the hardest-to-fake row (most specific criterion) and verify the quote traces to actual output text rather than a template placeholder. | "[quote]" | PASS / PARTIAL / FAIL |
| C-03 Composite score | Does the output use N_aspirational=10 (not 8 or 5)? Can you re-derive the composite from the 17 visible verdict values within ±1? State the re-derived value. | "[quote showing formula or score with N value]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | Are all N scored outputs ranked exactly once in descending order? Is there a Golden column? Are ties broken alphabetically? | "[quote]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | Is there a FAILURE PATTERNS section? If any criterion received FAIL or PARTIAL from every output, is it named? If no universal failure, does the section explicitly declare "no universal failures" rather than being silent? | "[quote, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | Does the output name at least one output-criterion pair where that output outperforms the rest by >= one tier (FAIL→PARTIAL or PARTIAL→PASS)? | "[quote, or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | If prior-round data was provided: are regressions (PASS→FAIL/PARTIAL) listed by output-criterion pair? If no prior data: does the output say so explicitly and declare auto-PASS rather than being silent? | "[quote, or: auto-PASS]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | Does each failure pattern entry include a specific verb, a named artifact (e.g., "quest-score.md SETUP block"), and a section location — not a generic observation like "improve coverage"? | "[quote, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | Does the output name min score, max score, spread in points, and a calibration implication specific to N_aspirational=10 (not just "spread is wide")? | "[quote, or: not found]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | Is at least one action line in the failure patterns fully instantiated — naming a real artifact filename and section visible in the scored outputs — rather than a fill-in-the-blank like "[artifact name]"? | "[quote, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | Is there a preamble section before the first output scoring block that lists each of C-05, C-07, C-08, C-10 with a status for this run? | "[quote from output's preamble, or: absent]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | Does the composite formula appear before the first per-output heading, and does it show N_essential=4, N_recommended=3, N_aspirational=10 explicitly? | "[quote showing formula with N values, or: not found before first output]" | PASS / PARTIAL / FAIL |
| C-13 Evidence-before-verdict | Is there a written mandate or structural column ordering that places the evidence quote before the verdict label — not just correct practice but an explicit enforcement mechanism? | "[quote showing ordering mandate or column structure evidence]" | PASS / PARTIAL / FAIL |
| C-14 Diagnostic questions | Does the SETUP roster include a diagnostic question for each of the 17 criteria? Are the questions specific (not identical boilerplate that could apply to any row)? | "[quote showing diagnostic question column, or: not found / generic only]" | PASS / PARTIAL / FAIL |
| C-15 Preamble gate | Is there an imperative instruction — using language like "Do not open" or "Open only after" — positioned before the first output section? Is it imperative (not advisory)? | "[quote showing imperative gate, or: not found]" | PASS / PARTIAL / FAIL |
| C-16 Named standalone auto-PASS block | Does the output contain a dedicated auto-PASS block (a named subsection, not a roster column) that spells out each condition by criterion ID and trigger phrase — e.g., "C-07 auto-PASS when no prior-round scorecard is provided"? | "[quote from the output's named auto-PASS block, or: conditions implied/embedded/absent]" | PASS / PARTIAL / FAIL |
| C-17 Criterion-specific diagnostic questions | For each criterion that has a diagnostic question, does the question interrogate the specific mechanism of that criterion (count, named block, verb+artifact+location format) rather than a generic probe that could apply to any row ("Is this criterion satisfied?")? | "[quote showing a mechanism-specific question, or: generic only]" | PASS / PARTIAL / FAIL |

Composite:
  Essential:    C-01=[v] + C-02=[v] + C-03=[v] + C-04=[v] = [sum] / 4 * 60 = [pts]
  Recommended:  C-05=[v] + C-06=[v] + C-07=[v]             = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[v]+C-09=[v]+C-10=[v]+C-11=[v]+C-12=[v]+C-13=[v]+C-14=[v]+C-15=[v]+C-16=[v]+C-17=[v] = [sum] / 10 * 10 = [pts]
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
  Action: [fully worked example: verb + artifact name + section, e.g., "Add a named
  Auto-PASS Conditions block to quest-score.md PREAMBLE with four declarations (C-05, C-07,
  C-08, C-10) so C-16 is satisfied structurally for every run."]

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

[1-3 sentences: min score, max score, spread, calibration implication specific to N_aspirational=10
(1.0 pt per aspirational criterion vs. v3's 1.25 pts) and how the two new criteria (C-16, C-17)
affect ceiling achievability relative to R3 runs.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-03: Front-Loaded DECLARATIONS Phase

**Axis:** Lifecycle emphasis — the skill is structured as three explicit phases: DECLARATIONS,
SCORING, AGGREGATE. The DECLARATIONS phase is front-loaded and heavyweight: it requires the
scorer to explicitly resolve and name every auto-PASS condition before the criterion roster is
filled, before the formula is printed, and before the first output file is opened. Each
DECLARATIONS step ends with a labeled STOP that must produce visible output.

**Hypothesis:** C-16 can be achieved through lifecycle structure rather than block naming: if
the auto-PASS resolution step is a first-class phase with its own STOP gate, the model is
structurally forced to produce named condition statements rather than TBD placeholders. The
phase framing makes "write the condition then stop" the default behavior. C-17 is deliberately
left unaddressed to isolate the lifecycle axis. Evidence-before-verdict mandate is preserved
from R3 V-01.

```
You are running /quest-score. Work in three phases: DECLARATIONS, SCORING, AGGREGATE.
Phase 1 (DECLARATIONS) is a mandatory gate — do not open any output file until all three
DECLARATIONS steps are complete.

---

## PHASE 1: DECLARATIONS

### Step 1.1 -- Auto-PASS Conditions

Before opening any output file, resolve each auto-PASS condition and write its declaration.
Each declaration must name the criterion ID and its trigger phrase.

Write each declaration now:

C-05: [Write "C-05 auto-PASS when no criterion fails universally across all scored outputs.
       Status: TBD — cannot resolve before scoring." or score if resolvable now.]

C-07: [Write "C-07 auto-PASS when no prior-round scorecard is provided to the scorer.
       Status: [auto-PASS / scoring required]." Fill from inputs above.]

C-08: [Write "C-08 auto-PASS when no failure patterns exist (depends on C-05).
       Status: TBD — resolves after C-05."]

C-10: [Write "C-10 auto-PASS when no failure patterns exist (depends on C-05).
       Status: TBD — resolves after C-05."]

STOP -- Step 1.1 complete: all four auto-PASS conditions declared. Each declaration must be
written above with criterion ID and trigger phrase before proceeding to Step 1.2.

---

### Step 1.2 -- Composite Formula

Print the composite formula with v4 N values:

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 10.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

STOP -- Step 1.2 complete: formula locked. Do not proceed to Step 1.3 until this formula
is fully written above.

---

### Step 1.3 -- Criterion Roster

List all 17 criteria and fill the Auto-PASS status column. Use the declarations from
Step 1.1 to populate TBD/auto-PASS/-- as appropriate.

| ID   | Name                                               | Tier         | Auto-PASS status |
|------|----------------------------------------------------|--------------|------------------|
| C-01 | Per-criterion verdicts present                     | essential    | --               |
| C-02 | Evidence quote for every verdict                   | essential    | --               |
| C-03 | Composite score computed correctly                 | essential    | --               |
| C-04 | Ranked leaderboard present                         | essential    | --               |
| C-05 | Failure patterns surfaced                          | recommended  | TBD              |
| C-06 | Excellence signals surfaced                        | recommended  | --               |
| C-07 | Regression signals surfaced                        | recommended  | [from Step 1.1]  |
| C-08 | Actionable diagnosis in failure patterns           | aspirational | TBD              |
| C-09 | Score distribution commentary                      | aspirational | --               |
| C-10 | Worked example in action line                      | aspirational | TBD              |
| C-11 | Auto-PASS rules stated in preamble                 | aspirational | --               |
| C-12 | Formula reproduced before first output section     | aspirational | --               |
| C-13 | Evidence-before-verdict ordering enforced          | aspirational | --               |
| C-14 | Per-criterion diagnostic question in roster        | aspirational | --               |
| C-15 | Preamble gate instruction present                  | aspirational | --               |
| C-16 | Named standalone auto-PASS block                   | aspirational | --               |
| C-17 | Criterion-specific diagnostic questions            | aspirational | --               |

STOP -- Step 1.3 complete: roster locked. All 17 rows filled. Do not open any output file
until Steps 1.1, 1.2, and 1.3 are all complete.

---

## PHASE 2: SCORING

### Evidence-Ordering Mandate

Column order in every scoring table: Criterion | Evidence Quote | Verdict
Write the evidence quote, then the verdict; never the reverse.

---

### OUTPUT: [output-id or filename]

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "[quote demonstrating complete 17-criterion verdict matrix, or: list missing rows]" | PASS / PARTIAL / FAIL |
| C-02 Evidence quotes | "[quote showing evidence present for verdicts; note any absent quote cells]" | PASS / PARTIAL / FAIL |
| C-03 Composite score | "[quote showing formula or score; flag if N_aspirational differs from 10]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | "[quote showing ranked table]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | "[quote from failure patterns section, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | "[quote from excellence signals section, or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | "[quote from regression section, or: auto-PASS]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | "[quote showing verb+artifact+location, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | "[quote showing min/max/spread/calibration, or: not found]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | "[quote showing instantiated action line, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | "[quote from the output's preamble auto-PASS section, or: not found]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | "[quote showing formula with N_aspirational=10, or: not found before first output]" | PASS / PARTIAL / FAIL |
| C-13 Evidence-before-verdict | "[quote showing ordering mandate or column evidence]" | PASS / PARTIAL / FAIL |
| C-14 Diagnostic questions | "[quote showing diagnostic question column, or: not found]" | PASS / PARTIAL / FAIL |
| C-15 Preamble gate | "[quote showing imperative gate, or: not found]" | PASS / PARTIAL / FAIL |
| C-16 Named standalone auto-PASS block | "[quote from output's named auto-PASS block with condition declarations, or: implied/embedded/absent]" | PASS / PARTIAL / FAIL |
| C-17 Criterion-specific diagnostic questions | "[quote showing mechanism-specific question, or: not found / generic only]" | PASS / PARTIAL / FAIL |

Composite:
  Essential:    [C-01+C-02+C-03+C-04] / 4 * 60 = [pts]
  Recommended:  [C-05+C-06+C-07] / 3 * 30 = [pts]
  Aspirational: [C-08 through C-17 sum] / 10 * 10 = [pts]
  Composite = [SCORE]/100 | Golden: [yes / no]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

### Resolve TBD Conditions

From Step 1.1, update C-05/C-08/C-10 status based on scoring above.

C-05: [auto-PASS / PASS / FAIL -- one sentence]
C-08: [auto-PASS / PASS / FAIL -- one sentence]
C-10: [auto-PASS / PASS / FAIL -- one sentence]

---

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [output-id] | [score] | yes / no |

Ties resolved alphabetically.

---

### Failure Patterns

[Any criterion FAIL or PARTIAL in EVERY output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence].
  Action: [verb + artifact + location, e.g., "Add a DECLARATIONS phase with three STOP-gated
  steps (auto-PASS conditions, formula, roster) to quest-score.md so C-16 declarations are
  structurally required before scoring begins."]

[None: "No universal failures -- C-05 auto-PASS."]

---

### Excellence Signals

[Any output-criterion pair outperforming group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence.]

[Uniform: "No differential excellence detected."]

---

### Regression Signals

[Prior scorecard provided: list regressions.]
[None: "No regressions."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

---

### Score Distribution

[1-3 sentences: min, max, spread, calibration implication for N_aspirational=10. Note that
the two new R4 criteria (C-16, C-17) expand N from 8 to 10, reducing per-criterion aspirational
weight to 1.0 pt each vs. v3's 1.25 pts.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-04: Named Declarations + Criterion-Specific Questions

**Axis:** V-01 + V-02 — named standalone auto-PASS block (C-16) combined with criterion-specific
diagnostic questions (C-17). Both new aspirational criteria addressed simultaneously. Inherits
the evidence-before-verdict mandate (C-13) and three-phase STOP gates (C-15) from R3 V-04,
upgrading the auto-PASS column to a named block and the diagnostic questions to mechanism-level.

**Hypothesis:** C-16 and C-17 are orthogonal: the named-declaration requirement (each condition
spelled out by criterion ID + trigger phrase) does not interfere with the diagnostic question
mechanism (each question interrogating the specific mechanism of its criterion). Combining both
in a single prompt produces PASS on both without degrading C-11, C-13, C-14, or C-15. The
combination should also capture V-03's lifecycle benefit because the named declarations block
forces auto-PASS resolution before scoring begins.

```
You are running /quest-score. Work in three phases: PREAMBLE, SCORE, AGGREGATE.
Phase 1 (PREAMBLE) is a mandatory gate with three required steps.
Do not open any output file until all three PREAMBLE steps are complete.

---

## PHASE 1: PREAMBLE

### Step 1.1 -- Auto-PASS Conditions

Resolve each auto-PASS condition before filling the criterion roster. Write each condition
as a named declaration using the format: "[Criterion ID] auto-PASS when [trigger phrase].
Status: [auto-PASS / TBD / scoring required]. [Optional one-phrase justification.]"

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status: TBD -- cannot resolve until all outputs are scored.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status: [Fill from inputs -- auto-PASS if no prior scorecard listed / "scoring required" if one is]
Justification: [one phrase]

**C-08 auto-PASS when no failure patterns exist (C-08 auto-PASS triggers when C-05 auto-PASS).**
Status: TBD -- resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-10 auto-PASS triggers when C-05 auto-PASS).**
Status: TBD -- resolves after C-05.

STOP -- Step 1.1 complete: declarations written. Proceed to Step 1.2 only after all four
declarations are written above with criterion ID and trigger phrase.

---

### Step 1.2 -- Formula

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 10.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

STOP -- Step 1.2 complete: formula locked. Proceed to Step 1.3.

---

### Step 1.3 -- Criterion Roster with Diagnostic Questions

Fill the "Auto-PASS" column using Step 1.1 declarations. Each Diagnostic Question names the
specific mechanism this criterion is testing -- not a generic probe. Write the evidence quote,
then the verdict; never the reverse.

| ID   | Name                                               | Tier         | Auto-PASS | Diagnostic Question |
|------|----------------------------------------------------|--------------|-----------|---------------------|
| C-01 | Per-criterion verdicts present                     | essential    | --        | Can you count exactly 17 verdict rows (C-01 through C-17) in the scoring table, with none missing? |
| C-02 | Evidence quote for every verdict                   | essential    | --        | For the hardest-to-fake row (most specific criterion), is the quote verbatim from the scored output rather than a template placeholder or invented text? |
| C-03 | Composite score computed correctly                 | essential    | --        | Does the score use N_aspirational=10? Can you re-derive the composite from the 17 visible verdict values within ±1? |
| C-04 | Ranked leaderboard present                         | essential    | --        | Are all N outputs ranked exactly once in descending order with a Golden column, ties broken alphabetically? |
| C-05 | Failure patterns surfaced                          | recommended  | TBD       | If no criterion failed universally, does the output explicitly declare "no universal failures" (not just omit the section)? |
| C-06 | Excellence signals surfaced                        | recommended  | --        | Is at least one output-criterion pair named where that output outperforms the group median by >= one tier? |
| C-07 | Regression signals surfaced                        | recommended  | [Step 1.1]| If prior-round data was provided, are regressions listed by output-criterion pair? If not provided, is auto-PASS stated explicitly? |
| C-08 | Actionable diagnosis in failure patterns           | aspirational | TBD       | Does every failure pattern action line name a specific artifact filename and section location (not "add to the skill" as a placeholder)? |
| C-09 | Score distribution commentary                      | aspirational | --        | Is there a calibration implication specific to N_aspirational=10 (names the per-criterion weight: 1.0 pt each)? |
| C-10 | Worked example in action line                      | aspirational | TBD       | Is at least one action line fully instantiated with a real artifact name visible in the scored outputs -- not [artifact name] or similar fill-in? |
| C-11 | Auto-PASS rules stated in preamble                 | aspirational | --        | Is there a preamble section before the first output heading that lists each of C-05, C-07, C-08, C-10 with a status for this run? |
| C-12 | Formula reproduced before first output section     | aspirational | --        | Does the composite formula appear before the first per-output heading, showing N_aspirational=10 explicitly? |
| C-13 | Evidence-before-verdict ordering enforced          | aspirational | --        | Is there an explicit mandate or column structure that places the evidence quote before the verdict -- not just correct practice but an enforcement mechanism? |
| C-14 | Per-criterion diagnostic question in roster        | aspirational | --        | Does the SETUP roster include a diagnostic question for each of the 17 criteria, and are they specific (not identical boilerplate for every row)? |
| C-15 | Preamble gate instruction present                  | aspirational | --        | Is there an imperative instruction ("Do not open" or equivalent) before the first output section -- imperative in tone, not advisory? |
| C-16 | Named standalone auto-PASS block                   | aspirational | --        | Does the output contain a dedicated block (not a roster column) that spells out each auto-PASS condition by criterion ID and trigger phrase, e.g., "C-07 auto-PASS when no prior-round scorecard is provided"? |
| C-17 | Criterion-specific diagnostic questions            | aspirational | --        | For each criterion that has a diagnostic question, does the question interrogate the specific mechanism (count, named block, format) rather than a generic probe ("Is this criterion satisfied?")? |

STOP -- Step 1.3 complete: 17-row roster filled with diagnostic questions. Do not open any
output file until Steps 1.1, 1.2, and 1.3 are all written above.

---

## PHASE 2: SCORING

Score each output in its own section. Column order: Criterion | Evidence Quote | Verdict.
Write the evidence quote first, then the verdict; never the reverse.

---

### OUTPUT: [output-id]

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "[quote demonstrating 17-row verdict matrix, or: list missing rows]" | PASS / PARTIAL / FAIL |
| C-02 Evidence quotes | "[quote showing evidence present; note any absent cells]" | PASS / PARTIAL / FAIL |
| C-03 Composite score | "[quote showing formula/score with N_aspirational=10]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | "[quote showing ranked table]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | "[quote from failure patterns section, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | "[quote from excellence signals, or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | "[quote from regression section, or: auto-PASS]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | "[quote showing verb+artifact+location, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | "[quote showing min/max/spread/calibration with N_aspirational=10]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | "[quote showing instantiated action line, or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | "[quote from output's preamble auto-PASS section, or: not found]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | "[quote showing formula before first output, N_aspirational=10]" | PASS / PARTIAL / FAIL |
| C-13 Evidence-before-verdict | "[quote showing ordering mandate or structural column evidence]" | PASS / PARTIAL / FAIL |
| C-14 Diagnostic questions | "[quote showing diagnostic question column with 17 rows, or: not found]" | PASS / PARTIAL / FAIL |
| C-15 Preamble gate | "[quote showing imperative gate before first output]" | PASS / PARTIAL / FAIL |
| C-16 Named standalone auto-PASS block | "[quote from output's named declarations block, or: conditions implied/embedded/absent]" | PASS / PARTIAL / FAIL |
| C-17 Criterion-specific diagnostic questions | "[quote showing a mechanism-interrogating question vs. generic probe]" | PASS / PARTIAL / FAIL |

Composite:
  Essential:    [C-01+C-02+C-03+C-04] / 4 * 60 = [pts]
  Recommended:  [C-05+C-06+C-07] / 3 * 30 = [pts]
  Aspirational: [C-08+C-09+C-10+C-11+C-12+C-13+C-14+C-15+C-16+C-17] / 10 * 10 = [pts]
  Composite = [SCORE]/100 | Golden: [yes / no -- reason]

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

### Resolve TBD Conditions (from Step 1.1)

Update C-05/C-08/C-10 based on scoring above. Reference the Step 1.1 declarations.

C-05: [auto-PASS / PASS / FAIL -- one sentence]
C-08: [auto-PASS / PASS / FAIL -- depends on C-05]
C-10: [auto-PASS / PASS / FAIL -- depends on C-05]

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [output-id] | [score] | yes / no |

Ties resolved alphabetically.

### Failure Patterns

[Any criterion FAIL or PARTIAL in EVERY output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence].
  Action: [verb + artifact name + section, e.g., "Add four named condition declarations
  (C-05, C-07, C-08, C-10 by ID and trigger phrase) to quest-score.md PREAMBLE block,
  replacing TBD markers, so C-16 is satisfied structurally for every run."]

[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair outperforming group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence.]

[Uniform: "No differential excellence detected."]

### Regression Signals

Prior-round data: [provided / not provided]
[Provided: list regressions (PASS -> FAIL or PARTIAL) by output-criterion pair.]
[None: "No regressions detected."]
[No data: "No prior-round scorecard -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min, max, spread, and calibration implication for N_aspirational=10.
Flag whether the two new R4 criteria (C-16, C-17) are the differentiating axis across scored
outputs, and whether any R3-era golden output would remain golden under v4 scoring.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```

---

## V-05: Full Synthesis

**Axis:** All three — named standalone auto-PASS declarations (C-16) + criterion-specific
mechanism-interrogating diagnostic questions (C-17) + front-loaded DECLARATIONS phase
(lifecycle emphasis) — combined with every mechanism that achieved PASS in R3: evidence-before-
verdict mandate (C-13), single-imperative preamble gate (C-15), formula at preamble (C-12),
three-phase STOP gates (C-15 strengthened), no-placeholder mandate, and "What it did
differently" in excellence signals.

**Hypothesis:** All 17 criteria can be simultaneously addressed by combining three structural
layers: (1) a named DECLARATIONS step with four explicit condition statements closes C-11 and
C-16; (2) a 17-row diagnostic question roster with mechanism-level questions closes C-14 and
C-17; (3) the evidence-before-verdict mandate plus column ordering closes C-13. All
aspirational criteria PASS. N_aspirational=10 (v4) means full aspirational score = 10 pts,
same total ceiling as v3 but lower per-criterion weight (1.0 vs 1.25 pts). A single FAIL now
costs less, so the golden threshold is more achievable for near-complete runs.

```
You are running /quest-score. Work in three phases: PREAMBLE, SCORE, AGGREGATE.
PREAMBLE is a mandatory gate with three steps — each step ends with a STOP instruction.
Do not open any output file until all three PREAMBLE steps are complete.

---

## PHASE 1: PREAMBLE

### Step 1.1 -- Auto-PASS Conditions

Resolve each auto-PASS condition before filling the criterion roster. Write each as a named
declaration: "[Criterion ID] auto-PASS when [trigger phrase]. Status: [status]. [Justification]."

**C-05 auto-PASS when no criterion fails universally across all scored outputs.**
Status: TBD -- cannot resolve before scoring all outputs.

**C-07 auto-PASS when no prior-round scorecard is provided to the scorer.**
Status: [auto-PASS if no prior scorecard in inputs / "scoring required" if one is listed]
Justification: [one phrase]

**C-08 auto-PASS when no failure patterns exist (C-08 auto-PASS triggers when C-05 auto-PASS).**
Status: TBD -- resolves after C-05.

**C-10 auto-PASS when no failure patterns exist (C-10 auto-PASS triggers when C-05 auto-PASS).**
Status: TBD -- resolves after C-05.

STOP-1 -- Step 1.1 complete: all four auto-PASS conditions declared by criterion ID and trigger
phrase. Do not proceed to Step 1.2 until all four declarations are written above.

---

### Step 1.2 -- Formula and Evidence Mandate

  composite = (essential_pass / 4 * 60)
            + (recommended_pass / 3 * 30)
            + (aspirational_pass / 10 * 10)

  N_essential = 4, N_recommended = 3, N_aspirational = 10.
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

Evidence-ordering mandate: In every scoring table, column order is Criterion | Evidence Quote |
Verdict. Write the evidence quote first, then the verdict; never the reverse.
A verdict cell completed before its evidence quote cell violates C-13.

STOP-2 -- Step 1.2 complete: formula and evidence mandate locked. Do not proceed to Step 1.3
until formula and mandate are fully written above.

---

### Step 1.3 -- Criterion Roster with Mechanism-Level Diagnostic Questions

Fill the Auto-PASS column using Step 1.1 declarations. Each Diagnostic Question names the
specific mechanism the criterion is testing. No generic probes: every question must be
unanswerable without reading the scored output and knowing the criterion's specific trigger.

| ID   | Name                                               | Tier         | Auto-PASS  | Mechanism-Level Diagnostic Question |
|------|----------------------------------------------------|--------------|------------|--------------------------------------|
| C-01 | Per-criterion verdicts present                     | essential    | --         | Can you count exactly 17 verdict rows in the scoring table (C-01 through C-17), with none missing or duplicated? |
| C-02 | Evidence quote for every verdict                   | essential    | --         | In the row for the most specific criterion (pick C-16 or C-17), is the quote verbatim from scored output text -- not a template slot or fabricated summary? |
| C-03 | Composite score computed correctly                 | essential    | --         | Does the output use N_aspirational=10? Re-derive the composite from the 17 visible verdict values: does your derivation match the stated score within ±1? |
| C-04 | Ranked leaderboard present                         | essential    | --         | Are all N scored outputs listed exactly once, ranked highest to lowest, with a Golden column, and ties broken alphabetically? |
| C-05 | Failure patterns surfaced                          | recommended  | TBD        | If any criterion received FAIL or PARTIAL from every output: is it named with a diagnosis label (rubric gap / skill design / data gap)? If no universal failure: is auto-PASS declared explicitly in text (not by omission)? |
| C-06 | Excellence signals surfaced                        | recommended  | --         | Is at least one output-criterion pair identified where that output is >= one tier above the rest of the group? Is the "What it did differently" field present? |
| C-07 | Regression signals surfaced                        | recommended  | [Step 1.1] | If prior-round data was provided: are regressions listed by output-criterion pair with direction (PASS→FAIL or PASS→PARTIAL)? If no data: is auto-PASS stated explicitly in text? |
| C-08 | Actionable diagnosis in failure patterns           | aspirational | TBD        | For each failure pattern entry, does the action line name a specific artifact filename (not [artifact]) and a section location within that file? |
| C-09 | Score distribution commentary                      | aspirational | --         | Does the distribution note state N_aspirational=10 and name the per-criterion aspirational weight (1.0 pt each), not just report the spread in points? |
| C-10 | Worked example in action line                      | aspirational | TBD        | Is at least one action line fully instantiated -- naming a real artifact filename and section visible in the scored outputs -- not a fill-in-the-blank template? |
| C-11 | Auto-PASS rules stated in preamble                 | aspirational | --         | Is there a preamble section (before the first output heading) that lists each of C-05, C-07, C-08, C-10 with a status for this run? |
| C-12 | Formula reproduced before first output section     | aspirational | --         | Does the composite formula appear before the first per-output heading, showing all three N values (N_essential=4, N_recommended=3, N_aspirational=10) explicitly? |
| C-13 | Evidence-before-verdict ordering enforced          | aspirational | --         | Is there a written mandate (not just correct column order) stating that the evidence quote must precede the verdict label? |
| C-14 | Per-criterion diagnostic question in roster        | aspirational | --         | Does the SETUP or PREAMBLE roster include a diagnostic question for each of the 17 criteria, with no two questions being identical? |
| C-15 | Preamble gate instruction present                  | aspirational | --         | Is there an imperative instruction ("Do not open output files until..." or equivalent) positioned before the first output section -- imperative in tone, not advisory? |
| C-16 | Named standalone auto-PASS block                   | aspirational | --         | Does the output contain a dedicated block (not a column in the roster, not a TBD marker) that names each of C-05, C-07, C-08, C-10 by criterion ID with its trigger phrase spelled out? |
| C-17 | Criterion-specific diagnostic questions            | aspirational | --         | For each criterion that has a diagnostic question, does the question interrogate the specific mechanism of that criterion (count, named block, format, explicit declaration) rather than a generic probe ("Is this criterion satisfied?" or "Is evidence present?")? |

STOP-3 -- Step 1.3 complete: 17-row roster filled with mechanism-level diagnostic questions.
Do not open any output file until Steps 1.1, 1.2, and 1.3 are all written above.

---

## PHASE 2: SCORING

Score each output in its own section. Complete one section fully before opening the next.
Column order: Criterion | Evidence Quote | Verdict. Evidence first, always.

---

### OUTPUT: [output-id or filename]

| Criterion | Evidence Quote | Verdict |
|-----------|----------------|---------|
| C-01 Verdicts present | "[quote demonstrating 17-row verdict matrix; list any missing rows by ID]" | PASS / PARTIAL / FAIL |
| C-02 Evidence quotes | "[quote showing evidence for the hardest-to-fake row; note any absent cells]" | PASS / PARTIAL / FAIL |
| C-03 Composite score | "[quote showing formula or score with N_aspirational=10; state re-derived value]" | PASS / PARTIAL / FAIL |
| C-04 Leaderboard | "[quote showing ranked table with Golden column; note if ties broken]" | PASS / PARTIAL / FAIL |
| C-05 Failure patterns | "[quote from failure patterns section; or: auto-PASS per Step 1.1 (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-06 Excellence signals | "[quote from excellence signals including 'What it did differently'; or: not found]" | PASS / PARTIAL / FAIL |
| C-07 Regression signals | "[quote from regression section; or: auto-PASS per Step 1.1]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-08 Actionable diagnosis | "[quote showing verb+artifact+location action line; or: auto-PASS per Step 1.1 (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-09 Score distribution | "[quote showing min/max/spread with N_aspirational=10 weight (1.0 pt each) named]" | PASS / PARTIAL / FAIL |
| C-10 Worked example | "[quote showing instantiated action line with real artifact; or: auto-PASS (TBD)]" | PASS / PARTIAL / FAIL / auto-PASS |
| C-11 Auto-PASS in preamble | "[quote from output's preamble auto-PASS section listing C-05/C-07/C-08/C-10]" | PASS / PARTIAL / FAIL |
| C-12 Formula at preamble | "[quote showing formula before first output, all three N values present]" | PASS / PARTIAL / FAIL |
| C-13 Evidence-before-verdict | "[quote showing written mandate or column structure enforcing quote-before-verdict]" | PASS / PARTIAL / FAIL |
| C-14 Diagnostic questions | "[quote showing 17-row diagnostic question column; note if any are generic/identical]" | PASS / PARTIAL / FAIL |
| C-15 Preamble gate | "[quote showing imperative gate instruction before first output section]" | PASS / PARTIAL / FAIL |
| C-16 Named standalone auto-PASS block | "[quote from output's named declarations block with criterion IDs and trigger phrases; or: conditions implied/embedded/absent]" | PASS / PARTIAL / FAIL |
| C-17 Criterion-specific diagnostic questions | "[quote showing a mechanism-interrogating question (names count, block, format) vs. generic probe; note if all 17 are mechanism-level or only some]" | PASS / PARTIAL / FAIL |

Composite:
  Essential:    [C-01+C-02+C-03+C-04] / 4 * 60 = [pts]
  Recommended:  [C-05+C-06+C-07] / 3 * 30 = [pts]
  Aspirational: [C-08+C-09+C-10+C-11+C-12+C-13+C-14+C-15+C-16+C-17] / 10 * 10 = [pts]
  Composite = [sum] = [SCORE]/100
  Golden: [yes -- all 4 essentials PASS and score >= 80 / no -- reason]

All action lines must use real artifact names and file locations visible in the scored outputs;
placeholders like "[artifact name]" or "[section]" are not permitted.

[Repeat for every output.]

---

## PHASE 3: AGGREGATE

### Resolve TBD Conditions

Update C-05/C-08/C-10 declarations from Step 1.1 based on Phase 2 scoring.

C-05: [auto-PASS / PASS / FAIL -- one sentence]
C-08: [auto-PASS / PASS / FAIL -- C-05 resolution propagates here]
C-10: [auto-PASS / PASS / FAIL -- C-05 resolution propagates here]

### Leaderboard

Rank all outputs from highest to lowest composite score. Ties resolved alphabetically.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [output-id] | [score] | yes / no |

### Failure Patterns

[Any criterion FAIL or PARTIAL in EVERY output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence why].
  Action: [fully instantiated: verb + artifact name + section, e.g., "Add a STEP 1.1 DECLARATIONS
  block with four named condition statements (C-05, C-07, C-08, C-10 by criterion ID and trigger
  phrase) to quest-score.md PREAMBLE so C-16 is satisfied structurally for every run."]

[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair outperforming group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.
  What it did differently: [one sentence on the mechanism that enabled the higher tier.]

[Uniform: "No differential excellence detected."]

### Regression Signals

Prior-round data: [provided / not provided]
[Provided: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]
[None: "No regressions detected."]
[No data: "No prior-round scorecard provided -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: state min score, max score, spread, and calibration implication. Name that
N_aspirational=10 (expanded from v3's 8) reduces the per-criterion aspirational weight to 1.0 pt
vs. v3's 1.25 pts. Flag whether C-16 and C-17 are the differentiating axis across the scored
outputs, and whether a V-03-era output (strong C-15 but no named declarations) would score lower
under v4's C-16 than under v3's C-11 PARTIAL.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min,
scores_max.
```
