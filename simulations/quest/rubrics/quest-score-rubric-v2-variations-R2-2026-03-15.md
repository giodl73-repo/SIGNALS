# quest-score — Variations Round 2
# Generated: 2026-03-15

---

## Context: what Round 1 established

| Variation | Axes | Score | C-04 |
|-----------|------|-------|------|
| V-04 Tables + Gates | A+B | 90 | PARTIAL |
| V-05 Gates + Imperative | B+C | 89 | PARTIAL |
| V-02 Phase Gates | B | 86 | PARTIAL |
| V-03 Imperative | C | 69 | PARTIAL |
| V-01 Tables | A | 66 | PARTIAL |

**Universal ceiling**: C-04 (evidence grounded) scored PARTIAL across all five variations.
Structural enforcement (tables) and procedural enforcement (phase gates) address evidence *presence*, not evidence *specificity*.

**New aspirationals in v2** added to capture Round 1 design patterns:
- C-10: Phase completion gates present (mechanism behind V-02 and V-04's gate designs)
- C-11: Layered enforcement on coverage-critical criteria (mechanism behind V-04's top score)
- C-12: Evidence specificity self-check (the uncaptured pattern — no R1 variation attempted it)

---

## Variation axis selection for Round 2

| Axis | Label | Hypothesis |
|------|-------|------------|
| D | Role sequence | Assigning named Analyst and Judge roles in sequence separates evidence coverage (Analyst) from evidence quality (Judge), breaking the C-04 universal-PARTIAL ceiling through role-level accountability. |
| E | Inertia framing | Opening with a concrete contrast — a weak scorecard excerpt and a strong scorecard excerpt — anchors the evidence quality standard before scoring begins, reducing generic fill by giving the model an explicit anti-target. |
| F | Evidence audit phase | A dedicated post-scoring phase that re-reads every evidence cell and challenges each for output-specificity creates the procedural obligation C-12 requires. The leaderboard phase is gated on the audit's completion. |

Single-axis runs: V-01 (D), V-02 (E), V-03 (F)
Combinations: V-04 (A+B+F), V-05 (D+B+F)

Rubric in scope: `simulations/quest/rubrics/quest-score-rubric-v2-2026-03-15.md`
Formula: `(essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10)`
N_essential=4, N_recommended=3, N_aspirational=5
Golden threshold: all 4 essentials PASS AND composite >= 80

---

## V-01 — Role sequence: Analyst + Judge

**Axis**: Role sequence (D)
**Hypothesis**: Two named roles in sequence — Analyst scores every criterion, Judge audits every evidence cell for specificity — separates coverage from quality. The Analyst role eliminates criterion omission; the Judge role creates the named obligation C-12 requires. Neither role is redundant: the Analyst produces the filled scorecard; the Judge challenges it.

---

You are running `quest-score`. Complete this task in two named roles. Finish Role 1 entirely before beginning Role 2.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (provided by caller)
- Prior-round scorecard file path, if available (optional)

---

### ROLE 1 — ANALYST

Your task as Analyst: cover every criterion for every output. Do not skip a criterion. Do not skip an output.

**Step A — Load and roster**

Read the rubric. Extract all 12 criteria. Write this preamble before opening any output file:

```
## Analyst Preamble

Rubric: [file name]
Outputs: [list all variation IDs]
Prior-round data: [file name or "none"]

Formula: composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10)
N_essential = 4 | N_recommended = 3 | N_aspirational = 5
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
| C-10 | Phase completion gates present | aspirational |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational |
| C-12 | Evidence specificity self-check | aspirational |

ANALYST PREAMBLE COMPLETE.
```

**Step B — Score each output**

For each output, produce one scoring table:

```
### [V-XX — axis label]

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Per-criterion verdicts present | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-02 | Composite score correctly computed | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-03 | Ranked leaderboard present | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-04 | Evidence quotes are grounded | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-05 | Excellence signals surfaced | recommended | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-06 | Failure patterns identified | recommended | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-07 | Golden threshold explicitly applied | recommended | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-08 | Regression signals detected | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-09 | Rubric calibration note | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-10 | Phase completion gates present | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-12 | Evidence specificity self-check | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |

essential_pass  = [sum of 1.0/0.5/0.0 for C-01–C-04]
recommended_pass = [sum for C-05–C-07]
aspirational_pass = [sum for C-08–C-12]
composite = ([essential_pass] / 4 * 60) + ([recommended_pass] / 3 * 30) + ([aspirational_pass] / 5 * 10) = [value]
Golden: YES / NO — [reason if NO]
```

Rules while acting as Analyst:
- Every row must be filled. No row may be skipped.
- Evidence must reference the specific output. Write what the output does, not what a good output would do.
- Verdict must be exactly PASS, PARTIAL, or FAIL.

Write: `ANALYST COMPLETE — [N] outputs scored.`

Do not begin Role 2 until ANALYST COMPLETE is written.

---

### ROLE 2 — JUDGE

Your task as Judge: audit every evidence cell the Analyst wrote. You are reading the Analyst's tables, not the original output files.

**Step C — Evidence audit**

For each output, for each row in the scoring table, apply one test:

> Could this evidence — word for word, or close paraphrase — have been written about a different output?

- If YES: mark [GENERIC]. Either replace with a specific excerpt or structural observation, or note "best available — no output-specific evidence found" and mark [FLAGGED].
- If NO: mark [SPECIFIC]. No change required.

After auditing all cells, write:

```
## Judge: Evidence Audit Summary

Total cells audited: [N]
SPECIFIC: [N] | GENERIC replaced: [N] | GENERIC flagged: [N]

Replacements: ["V-XX C-YY: [old generic text] → [new specific text]"]
Flags: ["V-XX C-YY: best available — no output-specific evidence found"]
```

**Step D — Ranked leaderboard**

```
## Leaderboard

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
...all N outputs, sorted by composite score descending, ties share a rank...
```

**Step E — Excellence signals**

For each criterion where at least one output scores PASS and at least one scores PARTIAL or FAIL, emit a signal:

```
## Excellence Signals

- **[C-XX — criterion name]** — [V-YY] stands out: [what this output did that others did not, citing a specific structural element]
```

If no split verdicts: "No differentiating excellence signals — all outputs score identically on all criteria."

**Step F — Failure patterns**

For each criterion where every output scores FAIL or PARTIAL:

```
## Failure Patterns

- **[C-XX — criterion name]** — ALL outputs score [FAIL/PARTIAL]. Diagnosis: [rubric gap / skill design issue / input quality issue] because [reason].
```

If none: "No failure patterns — no criterion fails across all outputs."

**Step G — Regression signals**

If prior-round data is available, compare current verdicts to prior-round values. Report every PASS to PARTIAL or PASS to FAIL movement:

```
## Regression Signals

| Criterion | Prior | Current | Output | What Changed |
|-----------|-------|---------|--------|--------------|
```

If no regressions: "No regressions detected."
If no prior-round data: "Regression analysis unavailable — no prior-round data."

**Step H — Calibration note**

State the score range (min–max). State whether the rubric is well-differentiated, too lenient, or too strict. Note whether the new v2 aspirationals (C-10, C-11, C-12) are producing spread across outputs or scoring uniformly. Reference actual score values.

**Save** the artifact to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-02 — Inertia framing: contrast anchor

**Axis**: Inertia framing (E)
**Hypothesis**: Generic evidence is the inertia state — the path of least resistance for any scoring model is to write something that satisfies the structural presence check without being traceable to the specific output. Opening with a concrete contrast (a weak-scorecard excerpt and a strong-scorecard excerpt) gives the model an explicit anti-target before scoring begins. The contrast anchor reduces generic fill by making "this could apply to any output" a named failure mode, not an invisible one.

---

You are running `quest-score`.

**Before you score anything, study this contrast.**

**Weak evidence (avoid this):**
> C-01 on V-03: "The output covers all criteria with verdicts."
> C-03 on V-01: "A leaderboard section is included."

This is generic evidence. It could have been written about any output. It tells you nothing about what V-03 or V-01 specifically do differently from each other. Evidence like this will score FAIL for C-04.

**Strong evidence (produce this):**
> C-01 on V-03: "V-03 opens its SETUP phase by pre-printing a 12-row criterion table with one row per criterion ID; the model cannot proceed to scoring until every row header exists, eliminating the possibility of silently missing a criterion."
> C-03 on V-01: "V-01 mandates a leaderboard section with an explicit template (rank, variation ID, score, golden status) but provides no phase gate preventing the model from skipping directly to signals; the leaderboard is structurally required but not sequentially enforced."

This is specific evidence. It names a mechanism, cites a structural choice, and could not be transplanted into a different output's row without being wrong.

Your goal: every evidence cell must be strong evidence. Treat "this output specifically does X via mechanism Y" as the target for every cell.

---

**Step 1 — Load**

Read the rubric. Extract all 12 criteria (IDs, weight tiers, pass conditions), the composite formula, and the golden threshold. Read each output file. Record whether prior-round data is available.

---

**Step 2 — Score each output**

For each output, produce one scoring table:

```
### [V-XX — axis label]

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Per-criterion verdicts present | essential | PASS/PARTIAL/FAIL | [strong evidence — name the mechanism, cite the structure, use text traceable to this output only] |
| C-02 | Composite score correctly computed | essential | PASS/PARTIAL/FAIL | [strong evidence] |
| C-03 | Ranked leaderboard present | essential | PASS/PARTIAL/FAIL | [strong evidence] |
| C-04 | Evidence quotes are grounded | essential | PASS/PARTIAL/FAIL | [strong evidence] |
| C-05 | Excellence signals surfaced | recommended | PASS/PARTIAL/FAIL | [strong evidence] |
| C-06 | Failure patterns identified | recommended | PASS/PARTIAL/FAIL | [strong evidence] |
| C-07 | Golden threshold explicitly applied | recommended | PASS/PARTIAL/FAIL | [strong evidence] |
| C-08 | Regression signals detected | aspirational | PASS/PARTIAL/FAIL | [strong evidence] |
| C-09 | Rubric calibration note | aspirational | PASS/PARTIAL/FAIL | [strong evidence] |
| C-10 | Phase completion gates present | aspirational | PASS/PARTIAL/FAIL | [strong evidence] |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational | PASS/PARTIAL/FAIL | [strong evidence] |
| C-12 | Evidence specificity self-check | aspirational | PASS/PARTIAL/FAIL | [strong evidence] |

essential_pass  = [sum]
recommended_pass = [sum]
aspirational_pass = [sum]
composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10) = [value]
Golden: YES / NO — [specific reason if NO]
```

Before writing any evidence cell: ask yourself — could this sentence appear unchanged in a different output's row? If yes, rewrite it.

---

**Step 3 — Ranked leaderboard**

```
## Leaderboard

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
...all N outputs, sorted by composite score descending, ties share a rank...
```

---

**Step 4 — Excellence signals**

Scan the Step 2 tables. For each criterion where at least one output earns PASS and at least one earns PARTIAL or FAIL:

```
## Excellence Signals

- **[C-XX — criterion name]** — [V-YY] distinguishes itself: [what structural element, instruction pattern, or mechanism this output uses that others do not]
```

If all outputs score identically on all criteria: "No differentiating excellence signals."

---

**Step 5 — Failure patterns**

For each criterion where every output scores FAIL or PARTIAL:

```
## Failure Patterns

- **[C-XX — criterion name]** — ALL outputs score [FAIL/PARTIAL]. Diagnosis: [rubric gap / skill design issue / input quality issue] — [one-sentence reason].
```

If none: "No failure patterns."

---

**Step 6 — Regression signals**

If prior-round data exists: compare each current verdict to its prior-round value. Report any PASS to PARTIAL or PASS to FAIL movement. If no prior-round data: "Regression analysis unavailable — no prior-round data."

---

**Step 7 — Calibration note**

State the score range. Characterize the spread: well-differentiated, too lenient, or too strict. Note whether C-10, C-11, and C-12 (the new v2 aspirationals) are producing variance or scoring uniformly. Reference actual values.

---

**Save** the artifact to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-03 — Evidence audit phase: dedicated post-scoring audit

**Axis**: Lifecycle emphasis — evidence audit phase (F)
**Hypothesis**: Grafting a dedicated EVIDENCE AUDIT phase onto the V-02 phase-gate structure (the best single-axis Round 1 design) creates the procedural obligation C-12 requires: the model must revisit every evidence cell and challenge it for specificity before the leaderboard opens. The audit is gated: LEADERBOARD cannot begin until EVIDENCE AUDIT is marked complete. This makes evidence quality a sequenced obligation, not an implicit expectation embedded in the scoring step.

---

You are running `quest-score`. Complete each phase fully before advancing. Do not begin a phase until the previous phase's close marker is written.

**PHASE 1 — SETUP**

Write this block before opening any output file:

```
## SETUP

Rubric: [file name]
Outputs: [list all variation IDs]
Prior-round data: [file name or "none"]

Formula: composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10)
N_essential = 4 | N_recommended = 3 | N_aspirational = 5
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
| C-10 | Phase completion gates present | aspirational |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational |
| C-12 | Evidence specificity self-check | aspirational |

PHASE 1 COMPLETE.
```

Do not proceed to PHASE 2 until PHASE 1 COMPLETE is written.

**PHASE 2 — SCORING**

For each output, work through every criterion in the PHASE 1 roster in order. For each criterion, write:
- Verdict: PASS, PARTIAL, or FAIL
- Evidence: a quote or structural observation from this specific output that supports the verdict

At the end of each output, compute the composite score using the PHASE 1 formula. Show the arithmetic. State: GOLDEN or NOT GOLDEN, with the specific reason (which essential failed, or score below 80).

Write: `PHASE 2 COMPLETE — [N] outputs scored.`

Do not proceed to PHASE 3 until PHASE 2 COMPLETE is written.

**PHASE 3 — EVIDENCE AUDIT**

Re-read every evidence cell produced in PHASE 2. For each cell, apply this test:

> If I moved this evidence text into a different output's row, would it still be accurate?

- If YES: the evidence is GENERIC. Replace it with output-specific text. If no specific evidence can be found, note: "best available — no output-specific evidence found" and mark [FLAGGED].
- If NO: the evidence is SPECIFIC. Mark [VERIFIED] and leave unchanged.

After reviewing all cells, write:

```
## Evidence Audit

Cells reviewed: [N]
VERIFIED (specific): [N]
Replaced (was generic): [N]
Flagged (no specific available): [N]

Replacements:
- V-XX C-YY: "[old text]" → "[new text]"
...

Flags:
- V-XX C-YY: best available — no output-specific evidence found
...
```

Write: `PHASE 3 COMPLETE.`

Do not proceed to PHASE 4 until PHASE 3 COMPLETE is written.

**PHASE 4 — LEADERBOARD**

```
## Leaderboard

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
...all N outputs, sorted by composite score descending, ties share a rank...
```

Write: `PHASE 4 COMPLETE.`

**PHASE 5 — SIGNALS**

5a — Excellence signals

Scan the PHASE 2 verdicts (as updated by the PHASE 3 audit). For any criterion with split verdicts (at least one PASS, at least one PARTIAL or FAIL), emit a signal: criterion ID and name, the leading output, and the structural element that separated it.

If no split verdicts: "No differentiating excellence signals."

5b — Failure patterns

For any criterion where every output scores FAIL or PARTIAL, emit a diagnosis: rubric gap / skill design issue / input quality issue, with a brief reason.

If none: "No failure patterns."

5c — Regression signals

If prior-round data was loaded in PHASE 1: compare each criterion verdict to its prior-round value. Report any PASS to PARTIAL or PASS to FAIL movement. If no prior-round data: "Regression analysis unavailable — no prior-round data."

Write: `PHASE 5 COMPLETE.`

**PHASE 6 — CALIBRATION**

State the score range. Characterize the distribution: well-differentiated, too lenient, or too strict. Note separately whether C-10, C-11, C-12 (the three new v2 aspirationals) showed variance across outputs or scored uniformly. Reference actual score values.

Write: `PHASE 6 COMPLETE.`

**Save** the artifact to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-04 — Combined: Tables + Phase gates + Evidence audit (A+B+F)

**Axes**: Output format (A) + Lifecycle emphasis/phase gates (B) + Evidence audit phase (F)
**Hypothesis**: The Round 1 winner (V-04, A+B, 90pts) is the proven structural baseline: tables enforce criterion coverage, gates enforce phase sequencing. Its one unresolved problem is C-04 (evidence specificity). Adding a dedicated EVIDENCE AUDIT phase (F) between SCORING and LEADERBOARD adds the third enforcement layer: tables mandate evidence presence (A), phase gates enforce sequencing (B), and the audit phase enforces evidence quality (F). Each layer catches a different failure mode; all three must fail for a cell to remain generic.

---

You are running `quest-score`. Work through the phases in order. Do not advance past a phase until its close marker is written.

**PHASE 1 — SETUP**

Write this block before opening any output file:

```
## SETUP

Rubric: [file name]
Outputs: [V-01, V-02, ... V-NN]
Prior-round data: [file name or "none"]

Formula: composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10)
N_essential = 4 | N_recommended = 3 | N_aspirational = 5
PASS = 1.0 | PARTIAL = 0.5 | FAIL = 0.0
Golden threshold: all 4 essentials PASS AND composite >= 80

Criteria roster (copy this table verbatim into each PHASE 2 scoring block):
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
| C-10 | Phase completion gates present | aspirational |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational |
| C-12 | Evidence specificity self-check | aspirational |

PHASE 1 COMPLETE.
```

Do not open any output file until PHASE 1 COMPLETE is written.

**PHASE 2 — SCORING**

For each output, copy the PHASE 1 criteria roster and fill it:

```
### [V-XX] — [axis label]

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Per-criterion verdicts present | essential | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-02 | Composite score correctly computed | essential | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-03 | Ranked leaderboard present | essential | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-04 | Evidence quotes are grounded | essential | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-05 | Excellence signals surfaced | recommended | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-06 | Failure patterns identified | recommended | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-07 | Golden threshold explicitly applied | recommended | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-08 | Regression signals detected | aspirational | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-09 | Rubric calibration note | aspirational | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-10 | Phase completion gates present | aspirational | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |
| C-12 | Evidence specificity self-check | aspirational | PASS/PARTIAL/FAIL | "[quote or structural observation traceable to this output only]" |

essential_pass  = [sum of 1.0/0.5/0.0 for C-01–C-04]
recommended_pass = [sum for C-05–C-07]
aspirational_pass = [sum for C-08–C-12]
composite = ([essential_pass] / 4 * 60) + ([recommended_pass] / 3 * 30) + ([aspirational_pass] / 5 * 10) = [value]

Golden: YES / NO — [reason if NO]
```

No evidence cell may be left empty. No evidence cell may contain text that would apply equally to a different output.

After all outputs: `PHASE 2 COMPLETE — [N] outputs scored.`

Do not proceed to PHASE 3 until PHASE 2 COMPLETE is written.

**PHASE 3 — EVIDENCE AUDIT**

Re-read every evidence cell from PHASE 2. For each cell, apply the specificity test:

> If this evidence were moved to a different output's row, would it still be accurate?

- If YES: GENERIC. Replace with specific text. If no specific text exists, mark [FLAGGED — best available: no output-specific evidence found].
- If NO: SPECIFIC. Mark [VERIFIED]. No change.

After reviewing all cells:

```
## Evidence Audit

Total cells: [N]
VERIFIED: [N] | Replaced: [N] | Flagged: [N]

Replacements:
- V-XX C-YY: "[old text]" → "[new text]"

Flags:
- V-XX C-YY: best available — no output-specific evidence found
```

Write: `PHASE 3 COMPLETE.`

Do not proceed to PHASE 4 until PHASE 3 COMPLETE is written.

**PHASE 4 — LEADERBOARD**

```
## Leaderboard

| Rank | Variation | Essential | Recommended | Aspirational | Score | Golden? |
|------|-----------|-----------|-------------|--------------|-------|---------|
...sorted by Score descending, all N outputs, ties share a rank...
```

Write: `PHASE 4 COMPLETE.`

**PHASE 5 — EXCELLENCE SIGNALS**

Scan PHASE 2 tables (post-audit). For each criterion with split verdicts:

```
## Excellence Signals

| Criterion | Leading Output | Others | What Distinguished It |
|-----------|---------------|--------|-----------------------|
```

If no split verdicts: "No differentiating excellence signals."

Write: `PHASE 5 COMPLETE.`

**PHASE 6 — FAILURE PATTERNS**

Scan PHASE 2 tables. For each criterion where every output scores FAIL or PARTIAL:

```
## Failure Patterns

| Criterion | Universal Verdict | Diagnosis |
|-----------|------------------|-----------|
```

Diagnosis must identify: rubric gap / skill design issue / input quality issue, with brief reason.

If none: "No failure patterns." Write: `PHASE 6 COMPLETE.`

**PHASE 7 — REGRESSION SIGNALS**

If prior-round data was loaded in PHASE 1:

```
## Regression Signals

| Criterion | Prior | Current | Output | What Changed |
|-----------|-------|---------|--------|--------------|
```

If no regressions: "No regressions detected."
If no prior-round data: "Regression analysis unavailable — no prior-round data."

Write: `PHASE 7 COMPLETE.`

**PHASE 8 — CALIBRATION**

```
## Calibration Note

Score range: [min] – [max]. [Well-differentiated / too lenient / too strict].
v2 aspirationals (C-10, C-11, C-12): [uniform across outputs / showing spread — note which].
[One to two sentences characterizing overall variance.]
```

Write: `PHASE 8 COMPLETE.`

**Save** the artifact to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## V-05 — Combined: Role sequence + Phase gates + Evidence audit (D+B+F)

**Axes**: Role sequence (D) + Lifecycle emphasis/phase gates (B) + Evidence audit phase (F)
**Hypothesis**: V-04 keeps a single cognitive track throughout: fill cells in Phase 2, then audit them in Phase 3. V-05 creates a harder role boundary: the Analyst role operates inside Phases 1–3 (setup, scoring, leaderboard); the Judge role takes over in Phases 4–5 (evidence audit, signals). The role switch is a stronger cognitive reset than a phase name alone. The Judge's explicit mandate is to find what the Analyst missed, not to continue the Analyst's work in a new section. If both produce different results on C-04, the mechanism is role attribution, not phase structure.

---

You are running `quest-score`. Two named roles complete this task. Each role has its own phase group. Complete all phases in Role 1 before switching to Role 2.

**Inputs**
- Rubric file path (provided by caller)
- N skill output files (provided by caller)
- Prior-round scorecard file path, if available (optional)

---

### ROLE 1 — ANALYST

Your task: score all outputs against all criteria and produce the first-pass leaderboard.

**PHASE 1 — SETUP**

Write this block before reading any output:

```
## Analyst: Setup

Rubric: [file name]
Outputs: [list variation IDs]
Prior-round data: [file name or "none"]

Formula: composite = (essential_pass / 4 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 5 * 10)
N_essential = 4 | N_recommended = 3 | N_aspirational = 5
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
| C-10 | Phase completion gates present | aspirational |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational |
| C-12 | Evidence specificity self-check | aspirational |

PHASE 1 COMPLETE.
```

Do not open any output file until PHASE 1 COMPLETE is written.

**PHASE 2 — SCORING**

For each output, produce one scoring table:

```
### [V-XX] — [axis label]

| ID | Criterion | Weight | Verdict | Evidence |
|----|-----------|--------|---------|----------|
| C-01 | Per-criterion verdicts present | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-02 | Composite score correctly computed | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-03 | Ranked leaderboard present | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-04 | Evidence quotes are grounded | essential | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-05 | Excellence signals surfaced | recommended | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-06 | Failure patterns identified | recommended | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-07 | Golden threshold explicitly applied | recommended | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-08 | Regression signals detected | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-09 | Rubric calibration note | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-10 | Phase completion gates present | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-11 | Layered enforcement on coverage-critical criteria | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |
| C-12 | Evidence specificity self-check | aspirational | PASS/PARTIAL/FAIL | [evidence from this output] |

essential_pass  = [sum of 1.0/0.5/0.0 for C-01–C-04]
recommended_pass = [sum for C-05–C-07]
aspirational_pass = [sum for C-08–C-12]
composite = ([essential_pass] / 4 * 60) + ([recommended_pass] / 3 * 30) + ([aspirational_pass] / 5 * 10) = [value]
Golden: YES / NO — [reason if NO]
```

Every row must be filled. No evidence cell may be blank.

Write: `PHASE 2 COMPLETE — [N] outputs scored.`

**PHASE 3 — LEADERBOARD**

```
## Analyst: Leaderboard (first pass)

| Rank | Variation | Score | Golden? |
|------|-----------|-------|---------|
...all N outputs, sorted by composite score descending, ties share a rank...
```

Write: `PHASE 3 COMPLETE.`

Do not begin Role 2 until PHASE 3 COMPLETE is written.

---

### ROLE 2 — JUDGE

You are now the Judge. Your mandate: find what the Analyst missed or weakened. You are not continuing the Analyst's work — you are challenging it.

You are reading the Analyst's tables. You are not re-reading the original output files.

**PHASE 4 — EVIDENCE AUDIT**

For each output, for each evidence cell in the Analyst's PHASE 2 tables, apply one test:

> Could this evidence — word for word, or close paraphrase — appear in a different output's row without being wrong?

- If YES: GENERIC. Replace with specific evidence from the Analyst's table context, or mark [FLAGGED — best available: no output-specific evidence found].
- If NO: SPECIFIC. Accept and move on.

After auditing all cells:

```
## Judge: Evidence Audit

Total cells: [N]
SPECIFIC: [N] | Replaced: [N] | Flagged: [N]

Replacements: ["V-XX C-YY: [old text] → [new text]"]
Flags: ["V-XX C-YY: best available — no output-specific evidence found"]
```

Note: if replacements alter a verdict's justification, update the verdict and recompute the composite. State any score corrections explicitly.

Write: `PHASE 4 COMPLETE.`

Do not proceed to PHASE 5 until PHASE 4 COMPLETE is written.

**PHASE 5 — SIGNALS AND SYNTHESIS**

5a — Excellence signals

Using the post-audit verdicts: for each criterion where at least one output scores PASS and at least one scores PARTIAL or FAIL, emit a signal naming the leading output and the structural element that separated it. If no split verdicts: "No differentiating excellence signals."

5b — Failure patterns

For each criterion where every output scores FAIL or PARTIAL, emit a diagnosis: rubric gap / skill design issue / input quality issue, with a brief reason. If none: "No failure patterns."

5c — Regression signals

If prior-round data was loaded in PHASE 1: compare each criterion verdict to its prior-round value. Report any PASS to PARTIAL or PASS to FAIL movement. If no prior-round data: "Regression analysis unavailable — no prior-round data."

Write: `PHASE 5 COMPLETE.`

**PHASE 6 — CALIBRATION**

State the score range (using post-audit scores). State whether the rubric is well-differentiated, too lenient, or too strict. Note separately whether C-10, C-11, C-12 are showing spread or uniformity across outputs. Reference actual score values.

Write: `PHASE 6 COMPLETE.`

**Save** the artifact to: `simulations/quest/scorecards/{skill}-scorecard-R{round}-{date}.md`

---

## Predicted score deltas from rubric ceiling (100)

| Variation | Axes | C-04 mechanism | C-10/C-11/C-12 mechanism | Predicted floor |
|-----------|------|----------------|--------------------------|-----------------|
| V-01 | Role seq (D) | Judge role audits every cell for specificity | C-10: no phase structure, N/A PARTIAL; C-11: none; C-12: Judge audit satisfies | 82 |
| V-02 | Inertia framing (E) | Contrast anchor reduces generic fill; no structural enforcement | C-10: none; C-11: none; C-12: none (implicit, not explicit) | 78 |
| V-03 | Audit phase (F) | PHASE 3 audit forces specificity check, gated on completion | C-10: phases present; C-11: none (single-layer); C-12: PHASE 3 satisfies | 85 |
| V-04 | Tables+Gates+Audit (A+B+F) | Tables force presence; PHASE 3 audit forces specificity | C-10: explicit gates; C-11: tables+gates = two layers; C-12: PHASE 3 satisfies | 90 |
| V-05 | Roles+Gates+Audit (D+B+F) | Analyst fills; Judge role challenges — harder reset than phase rename | C-10: explicit gates; C-11: analyst+judge = two layers on scoring; C-12: Judge mandate | 88 |
