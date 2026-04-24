# quest-score — Variations Round 1
# Generated: 2026-03-15

---

## Variation axis selection

| Axis | Label | Hypothesis |
|------|-------|------------|
| A | Output format | Structured tables for every scoring matrix reduce evidence/verdict conflation and criterion omission vs. prose-per-criterion. |
| B | Lifecycle emphasis | Explicit named phase gates (SETUP → SCORE → LEADERBOARD → SIGNALS → CALIBRATE) eliminate partially-complete sections by making sequence mandatory. |
| C | Phrasing register | Direct imperative commands reduce hallucinated completions more than descriptive/passive instructions. |

Single-axis runs: V-01 (A), V-02 (B), V-03 (C)
Combinations: V-04 (A+B), V-05 (B+C)

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v1-2026-03-15.md`
Formula: `(essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/2 * 10)`
N_essential=4, N_recommended=3, N_aspirational=2
Golden threshold: all 4 essentials PASS AND composite >= 80

---

## V-01 — Output format: full scoring table per output

**Axis**: Output format
**Hypothesis**: A complete N×criterion table with one row per criterion, one evidence quote per cell, and an explicit verdict column produces fewer omissions and less evidence/verdict conflation than inline prose.

---

You are running `quest-score`. Score N skill output variations against the provided rubric.

**Inputs**
- Rubric file path (passed by caller)
- N skill output files (V-01 through V-NN, passed by caller)
- Prior-round scorecard file path, if available (optional)

**Step 1 — Load**

Read the rubric. Extract:
- All criteria with their IDs, weights (essential / recommended / aspirational), and pass conditions
- The composite score formula
- The golden threshold

Read each output file.

**Step 2 — Score each output**

For each output V-XX, produce a scoring table:

```
### V-XX: [axis label]

| ID | Criterion | Verdict | Evidence |
|----|-----------|---------|----------|
| C-01 | Per-criterion verdicts present | PASS/PARTIAL/FAIL | "[direct quote or structural observation from THIS output only]" |
| C-02 | Composite score correctly computed | PASS/PARTIAL/FAIL | "[direct quote or structural observation from THIS output only]" |
...one row per rubric criterion...
```

Rules:
- Every row must have a non-empty Evidence cell. Generic evidence that would apply equally to any output is FAIL for C-04 purposes.
- Verdict is one of: PASS, PARTIAL, FAIL only.
- Evidence must be a direct excerpt, precise paraphrase, or specific structural observation traceable to this output alone.

Below the table, compute the composite score:

```
essential_pass  = [sum of 1.0/0.5/0.0 for essential rows]
recommended_pass = [sum for recommended rows]
aspirational_pass = [sum for aspirational rows]

composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
          = [result]
```

State whether this output is GOLDEN (all 4 essentials PASS + composite >= 80) or NOT GOLDEN (state the specific reason: which essential failed, or score below 80).

**Step 3 — Ranked leaderboard**

After all outputs are scored, produce a single table:

```
## Leaderboard

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
| 1 | V-XX — [axis] | 94.2 | YES |
| 2 | V-YY — [axis] | 78.0 | NO — composite below 80 |
...
```

Rank by composite score descending. Ties share a rank. All N outputs must appear.

**Step 4 — Excellence signals**

If any criterion shows split verdicts across outputs (at least one PASS and at least one PARTIAL or FAIL), emit an excellence signal:

```
## Excellence Signals

- **C-XX [criterion name]** — V-YY stands out: [what this output did that others did not, citing specific structural element]
```

If all outputs score identically on all criteria, state: "No differentiating excellence signals — all outputs score identically on all criteria."

**Step 5 — Failure patterns**

If any criterion scores FAIL or PARTIAL across ALL outputs, emit a failure pattern:

```
## Failure Patterns

- **C-XX [criterion name]** — ALL outputs score [FAIL/PARTIAL]. Diagnosis: [rubric gap / skill design issue / input quality issue] because [reason].
```

If no universal failures exist, state: "No failure patterns — no criterion fails across all outputs."

**Step 6 — Regression signals**

If a prior-round scorecard file was provided:

```
## Regression Signals

| Criterion | Prior Verdict | Current Verdict | Output | Mechanism |
|-----------|--------------|-----------------|--------|-----------|
...
```

List any case where a verdict moved from PASS to PARTIAL or FAIL. If no regressions, state: "No regressions detected."

If no prior-round file was provided, state: "Regression analysis unavailable — no prior-round data."

**Step 7 — Calibration note**

```
## Calibration Note

Score range this round: [min] – [max]. [Rubric is well-differentiated / may be too lenient (cluster near ceiling) / may be too strict (cluster near floor)]. [One sentence on whether criteria are producing meaningful spread or not.]
```

**Output**

Write the scorecard to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-02 — Lifecycle emphasis: explicit named phase gates

**Axis**: Lifecycle emphasis
**Hypothesis**: Naming each phase as a required gate with an explicit close condition eliminates partially-complete scoring runs. The model must write "PHASE N COMPLETE" before advancing.

---

You are running `quest-score`. Complete each phase fully before advancing to the next. Do not open output files until PHASE 1 is complete.

**PHASE 1 — SETUP**

Load the rubric. Write a preamble block before opening any output file:

```
## SETUP

Rubric: [rubric file name]
N outputs: [list variation IDs]
Prior-round data: [file name or "none"]
Formula: (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
N_essential = 4, N_recommended = 3, N_aspirational = 2
PASS = 1.0 | PARTIAL = 0.5 | FAIL = 0.0
Golden threshold: all 4 essentials PASS AND composite >= 80

Criteria roster:
[List all criteria by ID, name, and weight tier]

PHASE 1 COMPLETE.
```

Do not proceed to PHASE 2 until PHASE 1 COMPLETE is written.

**PHASE 2 — SCORING**

For each output, work through every criterion in the rubric roster. For each criterion, write:
- Verdict: PASS, PARTIAL, or FAIL
- Evidence: a quote or structural observation from this specific output that supports the verdict

At the end of each output, compute composite score using the formula from PHASE 1. State golden/not-golden determination.

At the end of PHASE 2, write: `PHASE 2 COMPLETE — [N] outputs scored.`

Do not proceed to PHASE 3 until PHASE 2 COMPLETE is written.

**PHASE 3 — LEADERBOARD**

Produce a ranked table of all outputs by composite score descending. Include: Rank, Variation, Score, Golden status. Ties share a rank.

Write: `PHASE 3 COMPLETE.`

**PHASE 4 — SIGNALS**

Section 4a — Excellence signals

Review the PHASE 2 verdicts. For any criterion where at least one output scores PASS and at least one scores PARTIAL or FAIL, emit an excellence signal identifying: the criterion, the leading output, and what structural element accounts for the difference.

If no criterion shows split verdicts, write: "No differentiating excellence signals."

Section 4b — Failure patterns

For any criterion where every output scores FAIL or PARTIAL, emit a failure pattern with a diagnosis: is this a rubric gap, a skill design issue, or an input quality issue?

If no criterion fails universally, write: "No failure patterns."

Section 4c — Regression signals

If prior-round data was loaded in PHASE 1, compare each criterion verdict to its prior-round value. Report any PASS → PARTIAL or PASS → FAIL movements.

If no prior-round data: "Regression analysis unavailable — no prior-round data."

Write: `PHASE 4 COMPLETE.`

**PHASE 5 — CALIBRATION**

Write a calibration note that characterizes the score distribution: state the score range (min–max), whether the rubric is well-differentiated, too lenient, or too strict, and whether criteria are producing meaningful variance across outputs.

Write: `PHASE 5 COMPLETE.`

**Output**

Write the full scorecard to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-03 — Phrasing register: direct imperative throughout

**Axis**: Phrasing register
**Hypothesis**: Every instruction is a command. No descriptive or conditional phrasing. The model receives imperatives, not descriptions of what good output looks like.

---

Run `quest-score` on the provided inputs.

**Load.** Read the rubric. Extract all criteria IDs, their weight tier (essential / recommended / aspirational), and their pass conditions. Read each output file. Note whether a prior-round scorecard file is available.

**Score.** For every output, score every criterion. Write the verdict (PASS / PARTIAL / FAIL) and a grounded evidence quote for each. The evidence quote must come from the specific output being scored — do not write evidence that would apply equally to any other output. After scoring all criteria, compute the composite score:

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Verify the arithmetic. Do not round by more than 1 point. Apply the golden threshold: all 4 essentials PASS AND composite >= 80. State GOLDEN or NOT GOLDEN and give the specific reason if not golden.

**Build the leaderboard.** List all outputs ranked by composite score descending. Show rank, variation ID, score, and golden status. Do not omit any output. Ties share a rank.

**Surface excellence signals.** Find every criterion where at least one output scores PASS and at least one scores PARTIAL or FAIL. For each, name the leading output and the specific structural element that earned it the higher verdict. If no criterion splits, write exactly: "No differentiating excellence signals."

**Identify failure patterns.** Find every criterion where every output scores FAIL or PARTIAL. For each, write a one-sentence diagnosis: rubric gap, skill design issue, or input quality issue. If none, write exactly: "No failure patterns."

**Check regressions.** If prior-round data exists, compare each criterion verdict to its prior value. Report every PASS → PARTIAL or PASS → FAIL movement. If no prior data, write exactly: "Regression analysis unavailable — no prior-round data."

**Write the calibration note.** State the score range. State whether the rubric is well-differentiated, too lenient, or too strict. Reference actual score values.

**Write the artifact.** Save the scorecard to `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`.

---

## V-04 — Combined: Output format (tables) + Lifecycle emphasis (phase gates)

**Axes**: A + B
**Hypothesis**: Tables within named phase gates give both structural completeness (tables enforce criterion coverage) and sequencing compliance (gates prevent phase-skipping). This combination should outperform either axis alone.

---

You are running `quest-score`. Work through the phases in order. Do not advance past a phase until its close marker is written.

**PHASE 1 — SETUP**

Write this block before opening any output file:

```
## SETUP

Rubric: [file name]
Outputs: [V-01, V-02, ... V-NN]
Prior-round data: [file name or "none"]

Formula: composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
N_essential = 4 | N_recommended = 3 | N_aspirational = 2
PASS = 1.0 | PARTIAL = 0.5 | FAIL = 0.0
Golden threshold: all 4 essentials PASS AND composite >= 80

Criteria roster:
| ID | Name | Weight |
|----|------|--------|
| C-01 | Per-criterion verdicts present | essential |
| C-02 | Composite score correctly computed | essential |
| C-03 | Ranked leaderboard present | essential |
| C-04 | Evidence quotes are grounded | essential |
| C-05 | Excellence signals surfaced | recommended |
| C-06 | Failure patterns identified | recommended |
| C-07 | Golden threshold explicitly applied | recommended |
| C-08 | Regression signals detected | aspirational |
| C-09 | Rubric calibration note | aspirational |

PHASE 1 COMPLETE.
```

**PHASE 2 — SCORING**

For each output, produce one scoring table:

```
### [V-XX] — [axis label]

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Per-criterion verdicts present | essential | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-02 | Composite score correctly computed | essential | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-03 | Ranked leaderboard present | essential | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-04 | Evidence quotes are grounded | essential | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-05 | Excellence signals surfaced | recommended | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-06 | Failure patterns identified | recommended | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-07 | Golden threshold explicitly applied | recommended | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-08 | Regression signals detected | aspirational | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |
| C-09 | Rubric calibration note | aspirational | PASS/PARTIAL/FAIL | "[quote traceable to this output]" |

essential_pass  = [sum]
recommended_pass = [sum]
aspirational_pass = [sum]
composite = ([essential_pass] / 4 * 60) + ([recommended_pass] / 3 * 30) + ([aspirational_pass] / 2 * 10) = [value]

Golden: YES / NO — [reason if NO]
```

No evidence cell may be left empty. No evidence cell may contain generic language that would apply to any output.

After all outputs, write: `PHASE 2 COMPLETE — [N] outputs scored.`

**PHASE 3 — LEADERBOARD**

```
## Leaderboard

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
...sorted by Score descending...
```

Include all N outputs. Write: `PHASE 3 COMPLETE.`

**PHASE 4 — EXCELLENCE SIGNALS**

Scan the PHASE 2 tables. For each criterion with split verdicts, produce:

```
## Excellence Signals

| Criterion | Leading Output | Others | What Distinguished It |
|-----------|---------------|--------|-----------------------|
...
```

If no split verdicts, write: "No differentiating excellence signals — all outputs score identically on all criteria."

Write: `PHASE 4 COMPLETE.`

**PHASE 5 — FAILURE PATTERNS**

Scan the PHASE 2 tables. For each criterion where every output scores FAIL or PARTIAL:

```
## Failure Patterns

| Criterion | Universal Verdict | Diagnosis |
|-----------|------------------|-----------|
...
```

Diagnosis must be one of: rubric gap / skill design issue / input quality issue (with a brief reason).

If none, write: "No failure patterns." Write: `PHASE 5 COMPLETE.`

**PHASE 6 — REGRESSION SIGNALS**

If prior-round data was loaded in PHASE 1:

```
## Regression Signals

| Criterion | Prior | Current | Output | Mechanism |
|-----------|-------|---------|--------|-----------|
...
```

If no regressions: "No regressions detected."

If no prior-round data: "Regression analysis unavailable — no prior-round data."

Write: `PHASE 6 COMPLETE.`

**PHASE 7 — CALIBRATION**

```
## Calibration Note

Score range: [min] – [max]. Rubric assessment: [well-differentiated / too lenient / too strict].
[One sentence characterizing variance across outputs and criteria.]
```

Write: `PHASE 7 COMPLETE.`

**Save** the full artifact to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-05 — Combined: Lifecycle emphasis (phase gates) + Phrasing register (imperative)

**Axes**: B + C
**Hypothesis**: Imperative commands inside named phase gates is the minimal effective combination — gates prevent phase-skipping, imperatives prevent within-phase hedging. Lighter than V-04 (no tables mandate), higher compliance than V-02 (adds imperatives) or V-03 (adds gates).

---

Run `quest-score`. Obey phase order. Complete each phase fully before writing the next.

**PHASE 1 — SETUP. Write this block now.**

State: the rubric filename, the list of output variation IDs, whether prior-round data is available, the composite formula, N values (4/3/2), the PASS/PARTIAL/FAIL weights (1.0/0.5/0.0), and the golden threshold (all 4 essentials PASS + composite >= 80). List every criterion by ID, name, and weight tier.

Do not open any output file until this block is complete.

Write: PHASE 1 COMPLETE.

**PHASE 2 — SCORING. Score every output. Score every criterion.**

For each output variation:
- Work through each criterion in roster order. Do not skip a criterion.
- Write the verdict: PASS, PARTIAL, or FAIL.
- Write grounded evidence immediately after the verdict. The evidence must be a quote or observation from this specific output. Evidence that fits any output equally is disqualifying for C-04.
- After all criteria, compute the composite. Show the arithmetic. Verify it matches the verdicts above. State GOLDEN or NOT GOLDEN with the specific failure reason (which essential failed, or score below 80).

Write: PHASE 2 COMPLETE — [N] outputs scored.

**PHASE 3 — LEADERBOARD. Build it now.**

List every output ranked by composite score descending. Show rank, variation ID, score, and golden status. Ties share a rank. Do not omit any output.

Write: PHASE 3 COMPLETE.

**PHASE 4 — EXCELLENCE SIGNALS. Surface them now.**

Scan the PHASE 2 verdicts. Find every criterion where at least one output scores PASS and at least one scores PARTIAL or FAIL. For each, name the leading output and the structural element that separated it.

If no criterion shows split verdicts: write exactly "No differentiating excellence signals."

Write: PHASE 4 COMPLETE.

**PHASE 5 — FAILURE PATTERNS. Diagnose them now.**

Find every criterion where every output scores FAIL or PARTIAL. Diagnose each: is it a rubric gap, a skill design issue, or an input quality issue? Give a reason in one sentence.

If no criterion fails universally: write exactly "No failure patterns."

Write: PHASE 5 COMPLETE.

**PHASE 6 — REGRESSION SIGNALS. Check now.**

If prior-round data is available: compare every criterion verdict to its prior-round value. Report every case where a verdict moved from PASS to PARTIAL or FAIL. State the criterion, old verdict, new verdict, and what changed.

If no prior data: write exactly "Regression analysis unavailable — no prior-round data."

Write: PHASE 6 COMPLETE.

**PHASE 7 — CALIBRATION. Write it now.**

State the score range. State whether the rubric is producing meaningful spread or clustering. Reference actual score values. One paragraph is enough.

Write: PHASE 7 COMPLETE.

**Save.** Write the scorecard to `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`.

---

## Predicted score deltas from rubric ceiling (100)

| Variation | Axis | Predicted risk criteria | Predicted floor |
|-----------|------|------------------------|-----------------|
| V-01 | Format: tables | C-04 (evidence per cell — high density, may produce generic evidence for aspirationals) | 85 |
| V-02 | Lifecycle: phase gates | C-04 (gate does not enforce evidence quality within phase, only phase existence) | 88 |
| V-03 | Register: imperative | C-03 (leaderboard — imperative form may produce truncated table) | 90 |
| V-04 | Format+Gates | C-04 (table cells still require quality judgment) | 92 |
| V-05 | Gates+Imperative | C-08 (regression — imperative command fires but no prior data → auto-state) | 95 |
