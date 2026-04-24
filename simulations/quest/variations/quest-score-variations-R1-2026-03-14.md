Written to `simulations/quest/variations/quest-score-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — Summary

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Per-output section; one criterion-verdict table per output — structure prevents row omission |
| **V-02** | Lifecycle emphasis | Evidence-first: rubric map in Step 1, quote table filled before any verdict is written |
| **V-03** | Phrasing register | Conversational numbered checklist; no template slots; edge-case reasoning in plain English |
| **V-04** | V-01 + V-02 combined | Two-table pattern per output (evidence then verdict); formula pre-printed at top |
| **V-05** | Full synthesis | All of the above + auto-PASS rules at prompt top + golden column in leaderboard |

**Three single-axis picks and rationale:**

- **Output format** isolates C-01 (complete verdict matrix) — pre-printed rows prevent omission structurally.
- **Lifecycle emphasis** isolates C-02 (evidence quotes) — quote-before-verdict prevents fabrication.
- **Phrasing register** isolates C-05/C-07 auto-PASS handling — conversational latitude lets the model reason about conditional logic without getting locked in a template slot that doesn't accommodate it.

**Predicted ceiling:** V-05. All four essential criteria are structurally protected, auto-PASS rules are at prompt top (most visible), and the pre-printed formula prevents C-03 arithmetic drift. V-04 is the closest competitor. Open research question for R1: does V-03's conversational register produce better C-05/C-07 compliance than V-01's rigid template, even without evidence-first enforcement?
axis mechanisms.
V-05 is the synthesis target: all structural guarantees on every surface.

**Predicted ceiling:** V-05 — maximum surface coverage prevents any partial-omission failure and
explicitly prints the composite formula (C-03 guard) and auto-PASS rules (C-05/C-07 guard).
V-04 is the closest competitor. V-03 tests the floor: minimum structural overhead with full
semantic coverage.

---

## V-01: Per-Output Section Format

**Axis:** Output format — each scored output gets its own dedicated section with a
criterion-by-criterion verdict table (rows = criteria, columns = Verdict | Evidence Quote)
**Hypothesis:** Sectioning by output rather than by criterion prevents cross-output contamination
and makes C-01 (complete verdict matrix) trivially auditable: one table per output, every row
visible. C-02 (evidence quotes) is enforced by the column definition rather than by instruction.

```
You are running /quest-score. Score each provided skill output against the rubric.

Inputs available:
- Rubric file (path in your context): read it. Note every criterion ID, tier, and pass condition.
- Output files (paths in your context): read each one in turn.
- Prior-round scorecard (if provided): read it for regression detection.

---

## SETUP

List inputs before scoring:
- Rubric: [path] -- [N] criteria ([N_essential] essential, [N_recommended] recommended, [N_aspirational] aspirational)
- Outputs to score: [list each output path, one per line]
- Prior-round scorecard: [path, or "none provided"]
- Scoring date: [YYYY-MM-DD]

Composite formula (print once, use for every output):
  composite = (essential_pass/N_essential * 60) + (recommended_pass/N_recommended * 30) + (aspirational_pass/N_aspirational * 10)
  PARTIAL = 0.5 passes. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

---

## SCORING

Score each output in its own section. Complete the section fully before opening the next output.

---

### OUTPUT: [output-id or filename]

| Criterion | Verdict | Evidence Quote |
|-----------|---------|----------------|
| C-01 Verdicts present | PASS / PARTIAL / FAIL | "[verbatim or near-verbatim quote from the output supporting this verdict]" |
| C-02 Evidence quotes | PASS / PARTIAL / FAIL | "[quote]" |
| C-03 Composite score | PASS / PARTIAL / FAIL | "[quote showing score or formula]" |
| C-04 Leaderboard | PASS / PARTIAL / FAIL | "[quote]" |
| C-05 Failure patterns | PASS / PARTIAL / FAIL | "[quote, or: not present, or: auto-PASS -- no universal failures]" |
| C-06 Excellence signals | PASS / PARTIAL / FAIL | "[quote, or: not present]" |
| C-07 Regression signals | PASS / PARTIAL / FAIL | "[quote, or: auto-PASS -- no prior-round data]" |
| C-08 Actionable diagnosis | PASS / PARTIAL / FAIL | "[quote, or: not present]" |
| C-09 Score distribution | PASS / PARTIAL / FAIL | "[quote, or: not present]" |

Composite computation:
  Essential (C-01 to C-04): [sum of pass values, PARTIAL=0.5] / 4 * 60 = [pts]
  Recommended (C-05 to C-07): [sum] / 3 * 30 = [pts]
  Aspirational (C-08 to C-09): [sum] / 2 * 10 = [pts]
  Composite = [pts + pts + pts] = [SCORE]/100
  Golden: [yes / no -- reason if no]

[Repeat this complete section for every output before proceeding.]

---

## LEADERBOARD

Rank all outputs from highest to lowest composite score. Ties resolved alphabetically.

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [output-id] | [score] | [yes/no] |
| 2 | [output-id] | [score] | [yes/no] |

---

## FAILURE PATTERNS

For each criterion that received FAIL or PARTIAL in EVERY scored output:
- **[Criterion ID] -- [short name]**: All outputs scored [verdict]. Candidate explanation:
  [rubric gap / skill design issue / data gap]. Explanation: [one sentence on why].
  Action: [verb + artifact, e.g., "Add explicit instruction X to quest-score skill prompt."]

[If no criterion failed universally: "No universal failures -- C-05 auto-PASS."]

---

## EXCELLENCE SIGNALS

For each output-criterion pair where one output outperforms the group by at least one tier:
- **[Criterion ID] -- [short name]**: [output-id] scored PASS; group median was PARTIAL/FAIL.

[If all outputs scored identically on all criteria: "No differential excellence detected."]

---

## REGRESSION SIGNALS

[If prior-round scorecard was provided:]
For each output-criterion pair that was PASS in round N-1 and is now FAIL or PARTIAL:
- **[output-id] / [Criterion ID]**: Round [N-1] PASS -> Round [N] [verdict].
[If no regressions: "No regressions detected."]

[If no prior-round data: "No prior-round scorecard provided -- C-07 auto-PASS."]

---

## SCORE DISTRIBUTION

[1-3 sentences: state score range (min/max), whether scores cluster tightly or spread widely,
and whether clustering suggests a rubric calibration issue.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold.
```

---

## V-02: Evidence-First Ordering

**Axis:** Lifecycle emphasis -- extract all evidence quotes for each criterion before rendering
any verdict; verdict follows the quote, never the reverse
**Hypothesis:** Forcing the model to locate and write a quote before committing to a verdict
prevents post-hoc rationalization and fabricated evidence. This is the primary risk for C-02:
a model that assigns verdicts first and then invents supporting quotes. Requiring the quote first
grounds the verdict in the actual text of the output.

```
You are running /quest-score. Work in three steps: load rubric, score outputs (evidence first,
then verdicts), aggregate signals.

---

## STEP 1: RUBRIC MAP

Read the rubric file completely. Then fill in this map before opening any output file.
This step is complete when every criterion has a pass condition summary.

| Criterion | Tier | Pass condition (your own words, 1-2 sentences) |
|-----------|------|------------------------------------------------|
| C-01 | essential | |
| C-02 | essential | |
| C-03 | essential | |
| C-04 | essential | |
| C-05 | recommended | |
| C-06 | recommended | |
| C-07 | recommended | |
| C-08 | aspirational | |
| C-09 | aspirational | |

Auto-PASS notes (copy these, they govern scoring below):
- C-05: auto-PASS when no criterion scored FAIL or PARTIAL across ALL outputs.
- C-07: auto-PASS when no prior-round scorecard was provided.

---

## STEP 2: SCORE EACH OUTPUT

For each output, follow this order: (a) read the output fully, (b) extract evidence for ALL
criteria, (c) write verdicts. Do not write any verdict before completing the evidence table.

---

### [output-id]

**(a) Evidence extraction** -- complete this table before writing any verdict:

| Criterion | Evidence quote (verbatim or near-verbatim from the output, or "not found") |
|-----------|---------------------------------------------------------------------------|
| C-01 | "[quote]" |
| C-02 | "[quote]" |
| C-03 | "[quote showing score computation or formula]" |
| C-04 | "[quote showing leaderboard]" |
| C-05 | "[quote from failure patterns section, or: not found, or: auto-PASS]" |
| C-06 | "[quote from excellence signals section, or: not found]" |
| C-07 | "[quote from regression signals section, or: auto-PASS, or: not found]" |
| C-08 | "[quote showing an actionable recommendation, or: not found]" |
| C-09 | "[quote from score distribution commentary, or: not found]" |

**(b) Verdicts** -- fill only after evidence table above is complete:

| Criterion | Verdict | Rationale (one clause tying quote to pass condition) |
|-----------|---------|------------------------------------------------------|
| C-01 | PASS / PARTIAL / FAIL | |
| C-02 | PASS / PARTIAL / FAIL | |
| C-03 | PASS / PARTIAL / FAIL | |
| C-04 | PASS / PARTIAL / FAIL | |
| C-05 | PASS / PARTIAL / FAIL / auto-PASS | |
| C-06 | PASS / PARTIAL / FAIL | |
| C-07 | PASS / PARTIAL / FAIL / auto-PASS | |
| C-08 | PASS / PARTIAL / FAIL / auto-PASS | |
| C-09 | PASS / PARTIAL / FAIL | |

**(c) Composite:**
  Essential (C-01 to C-04): [C-01_val + C-02_val + C-03_val + C-04_val] / 4 = [fraction]
  Recommended (C-05 to C-07): [sum] / 3 = [fraction]
  Aspirational (C-08 to C-09): [sum] / 2 = [fraction]
  Score = ([essential] * 60) + ([recommended] * 30) + ([aspirational] * 10) = [SCORE]/100
  Golden: [yes if all 4 essentials PASS and score >= 80 / no -- reason]

[Repeat for every output before proceeding to Step 3.]

---

## STEP 3: AGGREGATION

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | [yes/no] |

Ties resolved alphabetically.

### Failure Patterns

[Any criterion with FAIL or PARTIAL in EVERY output:]
- **[Criterion ID] -- [name]**: all [N] outputs scored [verdict]. Candidate explanation:
  [rubric gap / skill design / data gap]. Action: [verb + artifact].

[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair where one output outperforms the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.

[Uniform: "No differential excellence detected."]

### Regression Signals

[Prior-round data provided? Yes/no.]
[Yes: list all output-criterion pairs that regressed (PASS -> FAIL or PARTIAL).]
[No regressions: "No regressions detected."]
[No data: "No prior-round scorecard provided -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min, max, spread, calibration implication.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold.
```

---

## V-03: Conversational Checklist Register

**Axis:** Phrasing register -- numbered step-by-step checklist in plain English instead of
template slots; imperative instructions replaced by descriptive guidance
**Hypothesis:** Conversational register reduces compliance failures caused by rigid template
formatting and gives the model latitude to reason about edge cases (the auto-PASS rules for
C-05 and C-07) without getting locked into a template slot that doesn't accommodate conditional
logic. The numbered checklist also makes the output structure easier to audit than a free-form
response.

```
You are running /quest-score. Your job is to score a set of skill output files against a rubric
and produce a QuestScorecard artifact.

Here is how to do it.

**Before you start:** Read the rubric all the way through. Understand each criterion and its
pass condition. Notice that two criteria have special rules: C-05 is automatically passing if no
criterion failed in every single output (nothing to report), and C-07 is automatically passing
if you weren't given a prior-round scorecard (no comparison data). Then read the prior-round
scorecard if one was provided. Then open each output file.

---

**Score each output one at a time. For each output, follow these steps:**

1. Read the entire output before scoring any criterion.

2. Go through the rubric criteria in order (C-01 through C-09). For each criterion:
   - Find the section of the output that speaks to this criterion, or notice its absence.
   - Copy a short verbatim or near-verbatim quote. If nothing addresses the criterion, write
     "not found."
   - Decide: PASS, PARTIAL, or FAIL? Write one sentence explaining why, tied to the pass
     condition.

3. Compute the composite score after scoring all 9 criteria:
   - Add up essential passes (C-01 through C-04): PARTIAL = 0.5.
   - Add up recommended passes (C-05 through C-07): PARTIAL = 0.5.
   - Add up aspirational passes (C-08 through C-09): PARTIAL = 0.5.
   - Score = (essential_sum/4 * 60) + (recommended_sum/3 * 30) + (aspirational_sum/2 * 10).
   - Show the arithmetic.
   - Note whether this output is golden: all 4 essentials PASS and score >= 80.

Repeat steps 1-3 for every output before moving on.

---

**After scoring all outputs, do these things:**

4. **Leaderboard.** List all outputs from highest to lowest composite score. Break ties
   alphabetically. Include a "Golden" column.

5. **Failure patterns.** Is there any criterion that every single output failed or partially
   failed? If yes, name it and guess why: is the rubric criterion unclear (rubric gap), does
   the skill systematically not produce this content (skill design issue), or do the outputs
   just lack the needed content (data gap)? Give one concrete suggestion for fixing it -- a
   specific thing to change in a specific file. If no criterion failed universally, say so
   and move on (C-05 auto-PASS).

6. **Excellence signals.** Is any output noticeably better than the others on a specific
   criterion -- PASS where the rest were PARTIAL or FAIL? Name the output and the criterion.
   If all outputs scored the same on every criterion, say so.

7. **Regression signals.** If you were given a prior-round scorecard, compare each
   output-criterion score to last round. Flag any pair that was PASS last round and is FAIL
   or PARTIAL now. If no prior-round data was provided, say so (C-07 auto-PASS).

8. **Score distribution.** Write 1-3 sentences: what was the min and max score, did scores
   cluster tightly or spread out, and what does that tell you about rubric difficulty or
   calibration?

---

Format your output with these headings so each section is easy to find:

- ## Scoring: [Output Name]  (one section per output, containing the criterion-by-criterion
  table and composite computation)
- ## Leaderboard
- ## Failure Patterns
- ## Excellence Signals
- ## Regression Signals
- ## Score Distribution

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold.
```

---

## V-04: Per-Output Sections + Evidence-First (V-01 + V-02)

**Axes:** Per-output section format (V-01) + evidence-extraction-before-verdict ordering (V-02)
**Hypothesis:** The section structure prevents criterion-row omission (C-01 guard) while
evidence-first extraction prevents fabricated quotes (C-02 guard). Together they close the two
hardest-to-fake essential criteria simultaneously. The two-table pattern per output (evidence
table then verdict table) makes the separation structurally unavoidable -- no verdict cell can
be filled before its evidence cell exists.

```
You are running /quest-score. Work in two phases per output: EXTRACTION (quotes first),
then SCORING (verdicts after). Do not write any verdict before locating its evidence quote.

---

## PHASE 1: RUBRIC LOAD

Read the rubric file. Record these auto-PASS rules before scoring:
- C-05: auto-PASS when no criterion scored FAIL or PARTIAL across ALL scored outputs.
- C-07: auto-PASS when no prior-round scorecard was provided.

Composite formula (print once):
  composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

---

## PHASE 2: SCORE EACH OUTPUT

Complete the full section for each output before opening the next file.

---

### SCORING: [output-id]

**Table A -- Evidence extraction** (complete for ALL criteria before filling Table B):

| Criterion | Evidence Quote | Traceable? |
|-----------|----------------|------------|
| C-01 Verdicts present | "[verbatim or near-verbatim quote]" | yes / partial / not found |
| C-02 Evidence quotes | "[quote]" | yes / partial / not found |
| C-03 Composite score | "[quote showing score or computation]" | yes / partial / not found |
| C-04 Leaderboard | "[quote]" | yes / partial / not found |
| C-05 Failure patterns | "[quote, or: auto-PASS, or: not found]" | yes / partial / not found |
| C-06 Excellence signals | "[quote, or: not found]" | yes / partial / not found |
| C-07 Regression signals | "[quote, or: auto-PASS, or: not found]" | yes / partial / not found |
| C-08 Actionable diagnosis | "[quote, or: not found]" | yes / partial / not found |
| C-09 Score distribution | "[quote, or: not found]" | yes / partial / not found |

**Table B -- Verdicts** (fill only after Table A is complete):

| Criterion | Verdict | Rationale |
|-----------|---------|-----------|
| C-01 | PASS / PARTIAL / FAIL | [tie to pass condition] |
| C-02 | PASS / PARTIAL / FAIL | [tie to pass condition] |
| C-03 | PASS / PARTIAL / FAIL | [verify formula from quote; +/-1 tolerance] |
| C-04 | PASS / PARTIAL / FAIL | [confirm all outputs ranked exactly once] |
| C-05 | PASS / PARTIAL / FAIL / auto-PASS | [explain or cite auto-PASS rule] |
| C-06 | PASS / PARTIAL / FAIL | [name output-criterion pair if any] |
| C-07 | PASS / PARTIAL / FAIL / auto-PASS | [cite prior-round data or auto-PASS rule] |
| C-08 | PASS / PARTIAL / FAIL / auto-PASS | [check verb + artifact per failure pattern entry] |
| C-09 | PASS / PARTIAL / FAIL | [check min/max mention and clustering comment] |

Composite:
  Essential: C-01=[val] + C-02=[val] + C-03=[val] + C-04=[val] = [sum] / 4 * 60 = [pts]
  Recommended: C-05=[val] + C-06=[val] + C-07=[val] = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[val] + C-09=[val] = [sum] / 2 * 10 = [pts]
  Composite = [pts] + [pts] + [pts] = [SCORE]/100
  Golden: [yes / no -- reason if no]

[Repeat for every output.]

---

## PHASE 3: SIGNALS + LEADERBOARD

### Leaderboard

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | [yes/no] |

Ties resolved alphabetically.

### Failure Patterns

[Any criterion FAIL or PARTIAL in EVERY output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design / data gap] -- [one sentence why].
  Action: [verb + specific artifact].

[None: "No universal failures -- C-05 auto-PASS."]

### Excellence Signals

[Any output-criterion pair where one outperforms the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.

[Uniform: "No differential excellence detected."]

### Regression Signals

Prior-round data: [provided / not provided]
[Yes: list every output-criterion pair that regressed (PASS -> FAIL or PARTIAL).]
[No regressions: "No regressions detected."]
[No data: "No prior-round scorecard provided -- C-07 auto-PASS."]

### Score Distribution

[1-3 sentences: min, max, spread, calibration implication.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold.
```

---

## V-05: Full Synthesis (All Axes)

**Axes:** Per-output sections (V-01) + evidence-first (V-02) + conversational setup (V-03) +
explicit auto-PASS rules at prompt top + formula pre-printed + golden gate column in leaderboard
**Hypothesis:** Maximum structural coverage: section structure prevents row omission (C-01),
evidence-first prevents fabricated quotes (C-02), pre-printed formula prevents computation
errors (C-03), explicit auto-PASS rules prevent false FAILs on C-05/C-07, and the golden gate
column in the leaderboard makes the convergence signal unambiguous to the user. This is the
direct synthesis target.

```
You are running /quest-score. Score a set of skill output files against a rubric and produce
a QuestScorecard artifact.

---

## BEFORE YOU SCORE

Read the rubric file completely. Read the prior-round scorecard if one was provided.
Do not open any output file yet.

Copy these rules -- they govern scoring below:
- **C-05 auto-PASS**: If no criterion scored FAIL or PARTIAL in EVERY output, there are no
  failure patterns to report. Mark C-05 auto-PASS and do not penalize clean runs.
- **C-07 auto-PASS**: If no prior-round scorecard was provided, regression detection cannot
  run. Mark C-07 auto-PASS.

Composite formula -- print once, use for every output:
  composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)
  PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
  Golden threshold: all 4 essentials PASS AND composite >= 80.

---

## SCORING: ONE SECTION PER OUTPUT

Open and fully score one output before opening the next. Complete all three steps below for
each output.

---

### SCORING: [output-id]

**Step A -- Extract evidence** (do this before writing any verdict):

Read the output completely. For each criterion, locate a verbatim or near-verbatim quote from
the output that addresses whether the criterion is satisfied. If nothing addresses it, write
"not found."

| Criterion | Evidence Quote |
|-----------|----------------|
| C-01 Verdicts present | "[quote]" |
| C-02 Evidence quotes | "[quote showing an example evidence quote in the scored output]" |
| C-03 Composite score | "[quote showing a score value or formula computation]" |
| C-04 Leaderboard | "[quote showing the leaderboard]" |
| C-05 Failure patterns | "[quote from failure patterns section, or: not found, or: auto-PASS]" |
| C-06 Excellence signals | "[quote from excellence signals section, or: not found]" |
| C-07 Regression signals | "[quote from regression section, or: auto-PASS, or: not found]" |
| C-08 Actionable diagnosis | "[quote showing a verb + artifact recommendation, or: not found]" |
| C-09 Score distribution | "[quote from score distribution commentary, or: not found]" |

**Step B -- Render verdicts** (do this only after Step A is complete):

| Criterion | Verdict | Rationale |
|-----------|---------|-----------|
| C-01 | PASS / PARTIAL / FAIL | [tie to pass condition; count verdict cells] |
| C-02 | PASS / PARTIAL / FAIL | [is every verdict cell accompanied by a non-empty quote?] |
| C-03 | PASS / PARTIAL / FAIL | [verify formula from quote; +/-1 tolerance; unverifiable = FAIL] |
| C-04 | PASS / PARTIAL / FAIL | [are all N outputs in the leaderboard exactly once, ordered correctly?] |
| C-05 | PASS / PARTIAL / FAIL / auto-PASS | [cite auto-PASS rule if applicable, else evaluate] |
| C-06 | PASS / PARTIAL / FAIL | [name the output-criterion pair that excels, or note absence] |
| C-07 | PASS / PARTIAL / FAIL / auto-PASS | [cite prior-round data or auto-PASS rule] |
| C-08 | PASS / PARTIAL / FAIL / auto-PASS | [each failure pattern entry must end with verb + artifact] |
| C-09 | PASS / PARTIAL / FAIL | [must mention min/max and clustering] |

**Step C -- Composite:**
  Essential:   C-01=[val] + C-02=[val] + C-03=[val] + C-04=[val] = [sum] / 4 * 60 = [pts]
  Recommended: C-05=[val] + C-06=[val] + C-07=[val]             = [sum] / 3 * 30 = [pts]
  Aspirational: C-08=[val] + C-09=[val]                         = [sum] / 2 * 10 = [pts]
  Composite = [pts] + [pts] + [pts] = [SCORE]/100
  Golden: [yes -- all 4 essentials PASS and score >= 80 / no -- which essential(s) failed or score < 80]

[Repeat for every output.]

---

## LEADERBOARD

| Rank | Output | Score | Golden |
|------|--------|-------|--------|
| 1 | [id] | [score] | yes / no |

Ties resolved alphabetically.

---

## FAILURE PATTERNS

[Any criterion FAIL or PARTIAL in EVERY scored output:]
- **[Criterion ID] -- [name]**: All [N] outputs scored [verdict].
  Diagnosis: [rubric gap / skill design issue / data gap] -- [one sentence on why].
  Action: [verb + specific artifact, e.g., "Rewrite C-02 pass condition to clarify
  partial-quote threshold in quest-score-rubric.md"].

[If no universal failures: "No universal failures -- C-05 auto-PASS."]

---

## EXCELLENCE SIGNALS

[Any output-criterion pair where one output outperforms the group by >= one tier:]
- **[Criterion ID] -- [name]**: [output-id] = PASS; group median = PARTIAL/FAIL.

[If all outputs scored identically on all criteria: "No differential excellence detected."]

---

## REGRESSION SIGNALS

Prior-round scorecard: [provided / not provided]
[Yes: compare each output-criterion pair to prior round. List every pair that regressed.]
  - [output-id] / [Criterion ID]: Round [N-1] PASS -> Round [N] [verdict].
[No regressions: "No regressions detected."]
[No data: "No prior-round scorecard provided -- C-07 auto-PASS."]

---

## SCORE DISTRIBUTION

[1-3 sentences: state min score, max score, whether scores cluster tightly or spread.
Comment on calibration: tight clustering may mean the rubric is too easy or too coarse;
wide spread means it discriminates well.]

---

Write artifact: simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md
Frontmatter: skill, round, date, rubric_version, outputs_scored, golden_threshold, scores_min, scores_max.
```

---

## Round 1 Design Notes

### Axis coverage

| Axis | Variations |
|------|-----------|
| Output format (per-output sections) | V-01, V-04, V-05 |
| Lifecycle emphasis (evidence-first) | V-02, V-04, V-05 |
| Phrasing register (conversational) | V-03, V-05 |
| Auto-PASS rules explicit at top | V-05 only |
| Formula pre-printed at top | V-04, V-05 |

### C-01/C-02 risk model

C-01 (complete verdict matrix): The risk is a missing criterion row. Per-output section
templates prevent this structurally -- every row is pre-printed. V-01, V-04, V-05 address
this. V-02 and V-03 rely on instruction compliance, not structure.

C-02 (evidence quotes): The risk is a hallucinated quote or a verdict with no quote at all.
Evidence-first ordering (V-02, V-04, V-05) prevents this by forcing the quote before the
verdict. Per-output section templates (V-01) reduce it by making the quote column mandatory
in the table definition.

### C-03 risk model

C-03 (correct composite score): The risk is arithmetic error or a score that cannot be
verified from the verdict table. Pre-printing the formula at prompt top (V-04, V-05) makes
the formula available without referencing the rubric during scoring. V-02 and V-03 require
the model to recall the formula from the rubric read in Step 1.

### C-05/C-07 auto-PASS risk

All five variations mention C-05 and C-07 auto-PASS. V-05 puts both rules at prompt top
before any scoring begins. V-02 puts them in the rubric map step. V-01 puts them inline
as notes in the verdict table rows. V-03 explains them in prose. V-04 puts them in Phase 1
before Phase 2 scoring begins. The question for live runs: does placement at prompt top
(V-05) vs. inline (V-01) vs. prose (V-03) affect auto-PASS compliance rate?

### Predicted differentiation

| Dimension | Strongest | Why |
|-----------|----------|-----|
| C-01 structural guarantee | V-01, V-04, V-05 | Pre-printed row per criterion |
| C-02 structural guarantee | V-02, V-04, V-05 | Evidence-before-verdict enforced |
| C-03 formula accuracy | V-04, V-05 | Formula at prompt top, not implicit |
| C-05/C-07 auto-PASS compliance | V-05 | Rules at top, most visible |
| Edge-case reasoning flexibility | V-03 | Conversational; least rigid |

### V-golden candidate

**V-05** is the synthesis target:
- Per-output sections prevent C-01 row omission
- Evidence-first prevents C-02 quote fabrication
- Formula printed once at top prevents C-03 arithmetic drift
- Auto-PASS rules at top prevent C-05/C-07 false FAILs
- Golden column in leaderboard makes convergence signal unambiguous

**V-04** is the closest structural competitor (two-table pattern + formula).
The open question for R1: does V-03's conversational register produce better C-05/C-07
reasoning than V-01's rigid template, even without evidence-first enforcement?
