Rubric written to `simulations/quest/rubrics/quest-score-rubric-2026-03-14.md`.

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 4 | Verdicts present, evidence quotes, correct composite score, ranked leaderboard |
| Recommended (30%) | 3 | Failure patterns, excellence signals, regression signals |
| Aspirational (10%) | 2 | Actionable diagnosis, score distribution commentary |

**Design notes:**

- C-01/C-02 are the hardest essential criteria to fake — they require the scoring matrix to be complete and grounded in actual quotes, not assertions.
- C-03 has a tolerance of ±1 for rounding but explicitly fails if the score can't be verified from the visible verdict table (catches hallucinated scores).
- C-07 is auto-PASS when no prior-round data exists — regression detection only fires when the comparison data is actually available.
- C-05 is also auto-PASS when no criterion fails universally — avoids penalizing clean runs.
- Golden threshold: all 4 essentials PASS + composite ≥ 80.
teria. Count of verdict cells == (number of outputs) * (number of rubric criteria).
Even a single missing cell is a FAIL.

---

**C-02 — Evidence quote for every verdict**

Each PASS / PARTIAL / FAIL verdict is accompanied by a verbatim or near-verbatim quote
extracted from the scored output. The quote must be clearly tied to that criterion (not a
generic excerpt).

_Pass condition_: Every verdict row or cell includes a non-empty quote field. The quote is
traceable to the source output (not fabricated). Verdicts with only a label and no quote
are a FAIL. A single missing quote anywhere is PARTIAL; more than 20% missing quotes is
FAIL.

---

**C-03 — Composite score computed correctly**

Each output receives a numeric composite score computed with the formula:

`composite = (essential_pass/N_essential * 60) + (recommended_pass/N_recommended * 30) + (aspirational_pass/N_aspirational * 10)`

PARTIAL counts as 0.5 passes. Score is expressed as a number 0-100.

_Pass condition_: Scores match the formula given the verdict data shown. Spot-check at
least one output: recompute from the verdict table and compare. Tolerance: ±1 point for
rounding. A score that cannot be verified from the verdict table is a FAIL.

---

**C-04 — Ranked leaderboard present**

The output includes a leaderboard table ranking all scored outputs from highest to lowest
composite score. Ties are resolved consistently (e.g., alphabetically or by round number).

_Pass condition_: A leaderboard table exists. All N outputs appear in the table exactly
once. Ordering matches the composite scores. Missing outputs or incorrect ordering is a
FAIL.

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-05 | **Failure patterns surfaced** | coverage | recommended |
| C-06 | **Excellence signals surfaced** | coverage | recommended |
| C-07 | **Regression signals surfaced (if prior round data available)** | behavior | recommended |

---

**C-05 — Failure patterns surfaced**

Criteria that receive FAIL or PARTIAL across ALL scored outputs are called out explicitly
as failure patterns with a candidate explanation: rubric gap (criterion is too strict or
ambiguous), skill design issue (the skill systematically cannot satisfy this criterion),
or data gap (outputs lack the content needed).

_Pass condition_: If any criterion fails in every output, it appears in a "Failure
Patterns" section with at least one candidate explanation. If no criterion fails across
all outputs, this criterion is auto-PASS (nothing to report).

---

**C-06 — Excellence signals surfaced**

Outputs that score unusually high (all PASS, or PASS on a criterion where most outputs
fail) on a specific criterion are flagged as excellence signals. The signal names the
criterion and the output that excelled.

_Pass condition_: A non-empty "Excellence Signals" section exists. It identifies at least
one output-criterion pair where the output outperforms the group average by at least one
tier (e.g., PASS vs. group median of PARTIAL). If all outputs score identically on every
criterion, PARTIAL is acceptable.

---

**C-07 — Regression signals surfaced**

When prior-round scorecard data is provided, outputs that passed a criterion in round N-1
but fail in round N are flagged as regressions. Each regression names the output, the
criterion, and the round comparison.

_Pass condition_: If prior-round data is provided, a "Regression Signals" section appears.
It lists every output-criterion pair that regressed. If no regressions exist, the section
says so explicitly. If no prior-round data was provided, this criterion is auto-PASS
(cannot be evaluated).

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-08 | **Actionable diagnosis in failure patterns** | depth | aspirational |
| C-09 | **Score distribution commentary** | depth | aspirational |

---

**C-08 — Actionable diagnosis in failure patterns**

Failure pattern entries include a specific, actionable recommendation: rewrite the
rubric criterion, add a skill instruction, or change the output format. Generic
observations ("this criterion seems hard") do not qualify.

_Pass condition_: Every failure pattern entry concludes with a concrete next-step
recommendation (verb + artifact, e.g., "Add an explicit leaderboard format requirement
to the quest-score skill prompt"). If there are no failure patterns, auto-PASS.

---

**C-09 — Score distribution commentary**

The output includes a brief (1-3 sentence) commentary on whether scores cluster tightly
(rubric may be too easy or too coarse) or spread widely (rubric is discriminating well).
This helps the user calibrate rubric difficulty over time.

_Pass condition_: A commentary section exists and mentions score range (min/max) and
whether clustering suggests a calibration issue.

---

## Composite Score Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

- PASS = 1.0 point, PARTIAL = 0.5 points, FAIL = 0.0 points
- N_essential = 4, N_recommended = 3, N_aspirational = 2
- Score range: 0 – 100

**Golden threshold**: All essential criteria PASS + composite >= 80.

---

## Criterion Summary Table

| ID | Text (short) | Weight | Category |
|----|-------------|--------|----------|
| C-01 | Per-criterion verdicts present | essential | correctness |
| C-02 | Evidence quote for every verdict | essential | correctness |
| C-03 | Composite score computed correctly | essential | correctness |
| C-04 | Ranked leaderboard present | essential | format |
| C-05 | Failure patterns surfaced | recommended | coverage |
| C-06 | Excellence signals surfaced | recommended | coverage |
| C-07 | Regression signals surfaced | recommended | behavior |
| C-08 | Actionable diagnosis in failure patterns | aspirational | depth |
| C-09 | Score distribution commentary | aspirational | depth |
