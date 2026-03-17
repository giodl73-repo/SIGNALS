Looking at the R2 scorecard, I can identify three new excellence patterns to extract:

1. **Evidence-before-verdict ordering** — V-02 explicitly mandates "Write the evidence quote, then the verdict; never the reverse." Not covered by C-02 (which only requires evidence be present).
2. **Per-criterion diagnostic question** — V-02 embeds a verification question in each criterion row to prevent lazy verdicts.
3. **Preamble gate instruction** — Both V-01 and V-02 include an explicit "do not open output files until preamble is complete" guard, enforcing the preamble-first discipline beyond what C-11/C-12 require.

These become C-13, C-14, C-15. N_aspirational rises from 5 → 8.

---

## quest-score Rubric — v3

_Updated from v2 after Round 2 scoring. Three new aspirational criteria added from R2 excellence signals. N\_aspirational changes from 5 → 8._

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 4 | Verdicts present, evidence quotes, correct composite score, ranked leaderboard |
| Recommended (30%) | 3 | Failure patterns, excellence signals, regression signals |
| Aspirational (10%) | 8 | Actionable diagnosis, score distribution commentary, worked-example in action line, auto-PASS rules at preamble, formula at preamble, evidence-before-verdict ordering, per-criterion diagnostic question, preamble gate instruction |

**Composite formula (v3 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 8.
PASS = 1.0, PARTIAL = 0.5, FAIL = 0.0. Score range: 0-100.
Golden threshold: all 4 essentials PASS AND composite >= 80.
```

**Design notes:**

- C-01/C-02 are the hardest essential criteria to fake — they require the scoring matrix to be complete and grounded in actual quotes, not assertions.
- C-03 has a tolerance of ±1 for rounding but explicitly fails if the score can't be verified from the visible verdict table (catches hallucinated scores).
- C-07 is auto-PASS when no prior-round data exists — regression detection only fires when the comparison data is actually available.
- C-05 is also auto-PASS when no criterion fails universally — avoids penalizing clean runs.
- C-08 auto-PASS when no failure patterns exist (nothing to diagnose).
- C-10 auto-PASS when no failure patterns exist (nothing to exemplify).
- C-13 strengthens C-02: C-02 requires evidence to be present; C-13 requires evidence to precede the verdict label within each cell.
- C-14 is independent of C-01: C-01 requires all verdict cells be filled; C-14 requires a diagnostic question alongside each criterion in the SETUP roster before scoring begins.
- C-15 is independent of C-11/C-12: those require formula and auto-PASS rules to appear in the preamble; C-15 requires an explicit sequencing gate that prohibits opening output files until the preamble block is fully written.

---

### ESSENTIAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-01 | **Per-criterion verdicts present** | correctness | essential |
| C-02 | **Evidence quote for every verdict** | correctness | essential |
| C-03 | **Composite score computed correctly** | correctness | essential |
| C-04 | **Ranked leaderboard present** | format | essential |

---

**C-01 — Per-criterion verdicts present**

Every rubric criterion is scored for every output. The verdict matrix is complete: rows are
rubric criteria, columns are scored outputs (or the inverse). Count of verdict cells ==
(number of outputs) × (number of rubric criteria). Even a single missing cell is a FAIL.

_Pass condition_: All criterion × output cells are present and carry a PASS / PARTIAL / FAIL
label. A missing row or column is a FAIL.

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

PARTIAL counts as 0.5 passes. Score is expressed as a number 0-100. N values must match
the rubric version in use (v3: N_essential=4, N_recommended=3, N_aspirational=8).

_Pass condition_: Scores match the formula given the verdict data shown. Spot-check at
least one output: recompute from the verdict table and compare. Tolerance: ±1 point for
rounding. A score that cannot be verified from the verdict table is a FAIL.

---

**C-04 — Ranked leaderboard present**

The output includes a leaderboard table ranking all scored outputs from highest to lowest
composite score. Ties resolved alphabetically. Columns must include at minimum: rank,
output ID, composite score, and golden status.

_Pass condition_: Leaderboard table present, all scored outputs appear, sorted correctly,
golden column populated.

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-05 | **Failure patterns surfaced** | diagnosis | recommended |
| C-06 | **Excellence signals surfaced** | diagnosis | recommended |
| C-07 | **Regression signals surfaced** | diagnosis | recommended |

---

**C-05 — Failure patterns surfaced**

_Auto-PASS when no criterion fails universally across all scored outputs._

A "failure pattern" is any rubric criterion that received FAIL (or majority FAIL) across
all scored outputs in this run. Each failure pattern is listed with the criterion ID, the
count of failing outputs, and a one-sentence characterization of why it failed.

_Pass condition_: Every universal failure is listed. If no universal failures exist, the
scorecard explicitly states "No universal failures — C-05 auto-PASS." Both branches must
be covered; silence is a FAIL.

---

**C-06 — Excellence signals surfaced**

An "excellence signal" is any output-criterion pair where one output outperforms the group
by at least one tier (e.g., PASS where all others scored PARTIAL or FAIL). Each signal is
listed with output ID, criterion ID, and a one-sentence description of what made it
superior.

_Pass condition_: At least one signal identified per run (unless the score distribution is
perfectly flat). If no signals exist, the scorecard states so explicitly.

---

**C-07 — Regression signals surfaced**

_Auto-PASS when no prior-round scorecard is provided._

A "regression" is any output-criterion pair that scored lower than in the previous round
(PASS → PARTIAL, PASS → FAIL, or PARTIAL → FAIL). Each regression is listed with output
ID, criterion ID, prior verdict, and current verdict.

_Pass condition_: All regressions listed when prior-round data is available. If no
regressions exist, the scorecard states so explicitly. Silence when prior data is provided
is a FAIL.

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-08 | **Actionable diagnosis in failure patterns** | diagnosis | aspirational |
| C-09 | **Score distribution commentary** | analysis | aspirational |
| C-10 | **Worked example in action line** | diagnosis | aspirational |
| C-11 | **Auto-PASS rules stated in preamble** | format | aspirational |
| C-12 | **Formula reproduced before first output section** | format | aspirational |
| C-13 | **Evidence-before-verdict ordering enforced** | correctness | aspirational |
| C-14 | **Per-criterion diagnostic question in roster** | correctness | aspirational |
| C-15 | **Preamble gate instruction present** | format | aspirational |

---

**C-08 — Actionable diagnosis in failure patterns**

_Auto-PASS when no failure patterns exist (C-05 auto-PASS)._

For each failure pattern, the scorecard includes a concrete action line: a verb, a named
artifact, and a location. Generic prescriptions ("improve coverage") are a FAIL.

_Pass condition_: Every failure pattern has an action line of the form `[verb] [artifact]
[location]`. Action lines that name a real file, section, or structural element PASS;
action lines that are fill-in-the-blank placeholders or generic advice are PARTIAL or FAIL
depending on proportion.

---

**C-09 — Score distribution commentary**

The scorecard includes 1-3 sentences characterizing the score distribution across all
outputs: minimum score, maximum score, spread, and the calibration implication (e.g.,
"tight cluster near ceiling suggests rubric may be insufficiently discriminating").

_Pass condition_: Distribution commentary present, states min/max/spread, and includes at
least one calibration implication. Purely descriptive commentary with no implication is
PARTIAL.

---

**C-10 — Worked example in action line**

_Auto-PASS when no failure patterns exist (C-05 auto-PASS)._

At least one action line in the failure patterns section is fully instantiated — not a
template with fill-in-the-blank placeholders, but a complete, copy-pasteable instruction
naming a real artifact and section visible in the scored outputs.

_Pass condition_: At least one action line demonstrates the fully-worked form. Template
framing (e.g., "e.g., …" without committing to the example) is PARTIAL. A placeholder
with no concrete instantiation is FAIL.

---

**C-11 — Auto-PASS rules stated in preamble**

Before any output scoring section, the scorecard declares which criteria are auto-PASS for
this run and why. The declaration appears in a SETUP or PREAMBLE block with a column or
field for each auto-PASS-eligible criterion (C-05, C-07, C-08, C-10).

_Pass condition_: Auto-PASS declarations present in preamble before first scoring section.
Each auto-PASS-eligible criterion has an explicit status (auto-PASS or TBD-resolve-after-
scoring). Missing any eligible criterion is PARTIAL; missing all is FAIL.

---

**C-12 — Formula reproduced before first output section**

The composite formula with explicit N values (N_essential, N_recommended, N_aspirational)
appears in the SETUP or PREAMBLE block before any output is scored. The N values must
match the rubric version in use.

_Pass condition_: Formula present in preamble with correct N values. Formula appearing
only inside an output scoring section (not in preamble) is FAIL. Formula with wrong N
values is FAIL.

---

**C-13 — Evidence-before-verdict ordering enforced**

The scorecard explicitly mandates — in its structural framing or scoring instructions —
that evidence quotes are written before verdict labels in each scored cell. A statement
such as "Write the evidence quote, then the verdict; never the reverse" or structural
enforcement via column ordering (quote column precedes verdict column) satisfies this
criterion.

_Pass condition_: An explicit ordering mandate is present in the scorecard structure or
instructions. Evidence quotes consistently preceding verdicts in the actual scoring table
is supporting evidence but not sufficient alone — the mandate must be stated. Absence of
any ordering instruction is FAIL even if the ordering happens to be correct.

---

**C-14 — Per-criterion diagnostic question in roster**

The criterion roster in SETUP includes a diagnostic question for each criterion — a single
question the scorer answers before rendering a verdict. The question must be criterion-
specific (not generic) and must interrogate whether the criterion was actually satisfied
rather than merely whether it was attempted.

_Pass condition_: Every criterion in the roster has a diagnostic question. Questions that
are generic ("Is this criterion met?") without criterion-specific content are PARTIAL.
Missing diagnostic questions for more than half the criteria is FAIL.

---

**C-15 — Preamble gate instruction present**

The SETUP or PREAMBLE block includes an explicit sequencing instruction prohibiting the
scorer from opening or reading any output file until the preamble block (formula, auto-
PASS declarations, criterion roster) is complete. The instruction must be imperative ("Do
not open output files until…" / "Open output files only after…") rather than advisory.

_Pass condition_: Gate instruction present in preamble, imperative in tone, and positioned
before the first output section heading. Advisory or passive framing ("It is recommended
to complete the preamble first") is PARTIAL. Absence of any gate instruction is FAIL.

---
