Looking at the R3 scorecard, two excellence patterns emerge:

1. **Named standalone auto-PASS block** — Both V-01 and V-02 scored C-11 PARTIAL for the same reason: auto-PASS conditions were "implied rather than declared as a standalone rules block" / "embedded in question phrasing." C-11 only requires the rules to appear in the preamble; it doesn't require them to be an explicit named block. That gap is C-16.

2. **Criterion-specific diagnostic questions** — V-02's C-14 PASS was distinguished by "one question per criterion, criterion-specific (not generic)." C-14 requires a question to be present; it doesn't require the question to interrogate the specific mechanism of that criterion. That gap is C-17.

N_aspirational rises from 8 → 10.

---

## quest-score Rubric — v4

_Updated from v3 after Round 3 scoring. Two new aspirational criteria added from R3 excellence signals. N\_aspirational changes from 8 → 10._

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 4 | Verdicts present, evidence quotes, correct composite score, ranked leaderboard |
| Recommended (30%) | 3 | Failure patterns, excellence signals, regression signals |
| Aspirational (10%) | 10 | Actionable diagnosis, score distribution commentary, worked-example in action line, auto-PASS rules at preamble, formula at preamble, evidence-before-verdict ordering, per-criterion diagnostic question, preamble gate instruction, named standalone auto-PASS block, criterion-specific diagnostic questions |

**Composite formula (v4 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 10 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 10.
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
- C-16 strengthens C-11: C-11 requires auto-PASS rules to appear in the preamble; C-16 requires each condition to be spelled out as a named declaration (e.g., "C-05 auto-PASS when no universal failures exist"), not implied by TBD placeholders or embedded in diagnostic question phrasing.
- C-17 strengthens C-14: C-14 requires a diagnostic question per criterion; C-17 requires each question to interrogate the specific mechanism of that criterion rather than a generic probe that could apply to any row.

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

The composite score is derived from the verdict table using the formula stated in the
preamble. The scorer shows the per-tier subtotals so the arithmetic is verifiable.

_Pass condition_: Composite matches the formula within ±1 rounding tolerance. If the score
cannot be independently verified from the visible verdict table (e.g., tallies are missing
or the formula is absent), the criterion FAILS regardless of the stated score.

---

**C-04 — Ranked leaderboard present**

All scored outputs appear in a single ranked table ordered from highest to lowest composite
score. The table includes at minimum: rank, output identifier, composite score, and Golden
status.

_Pass condition_: Leaderboard is present, covers all outputs, and is correctly ordered.
Ties may share a rank. Missing Golden column is PARTIAL.

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-05 | **Failure patterns surfaced** | diagnosis | recommended |
| C-06 | **Excellence signals surfaced** | diagnosis | recommended |
| C-07 | **Regression signals surfaced** | diagnosis | recommended |

---

**C-05 — Failure patterns surfaced**

_Auto-PASS when no criterion received FAIL or PARTIAL in every scored output._

When at least one criterion fails universally (every output scores FAIL or PARTIAL), the
scorecard includes a FAILURE PATTERNS section that names each universally-failing criterion,
quotes the failure evidence, and identifies the shared root cause.

_Pass condition_: Every universal failure has a named entry. A section present but missing
any universal failure is PARTIAL.

---

**C-06 — Excellence signals surfaced**

The scorecard includes an EXCELLENCE SIGNALS section listing every output-criterion pair
where one output outperforms the group by at least one tier (PASS where others are PARTIAL
or FAIL, or PARTIAL where others are FAIL).

_Pass condition_: All qualifying pairs are named with their distinguishing evidence.
Section absent is FAIL; present but incomplete is PARTIAL.

---

**C-07 — Regression signals surfaced**

_Auto-PASS when no prior-round scorecard data is available to the scorer._

When prior-round data is available, the scorecard includes a REGRESSION SIGNALS section
listing every output-criterion pair that regressed from the prior round (PASS → PARTIAL,
PASS → FAIL, or PARTIAL → FAIL).

_Pass condition_: All regressions are named with the prior-round and current-round verdicts.
Section absent when regressions exist is FAIL; present but incomplete is PARTIAL.

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-08 | **Actionable diagnosis** | actionability | aspirational |
| C-09 | **Score distribution commentary** | calibration | aspirational |
| C-10 | **Worked example in action line** | actionability | aspirational |
| C-11 | **Auto-PASS rules stated in preamble** | structure | aspirational |
| C-12 | **Formula at preamble** | structure | aspirational |
| C-13 | **Evidence-before-verdict ordering** | structure | aspirational |
| C-14 | **Per-criterion diagnostic question** | structure | aspirational |
| C-15 | **Preamble gate instruction** | structure | aspirational |
| C-16 | **Named standalone auto-PASS block** | structure | aspirational |
| C-17 | **Criterion-specific diagnostic questions** | correctness | aspirational |

---

**C-08 — Actionable diagnosis**

_Auto-PASS when no failure patterns exist._

Each failure pattern entry includes an Action line of the form: verb + artifact + location.
The line is fully instantiated — it names a real artifact and a real location in that
artifact where the fix should be made. Placeholder phrasing ("fix the rubric", "improve
coverage") is a FAIL.

_Pass condition_: Every failure pattern entry has a fully instantiated Action line.
A single placeholder is PARTIAL; more than one is FAIL.

---

**C-09 — Score distribution commentary**

The scorecard includes a note on score distribution across the scored outputs: whether
scores cluster, whether the aspirational denominator compresses the ceiling relative to
prior rounds, and whether the spread distinguishes meaningful quality differences.

_Pass condition_: Commentary is present and references the current N_aspirational value.
Generic filler without calibration observation is PARTIAL.

---

**C-10 — Worked example in action line**

_Auto-PASS when no failure patterns exist._

At least one Action line in the failure patterns section is a fully instantiated worked
example (real artifact + real location), demonstrating the expected specificity for all
action lines.

_Pass condition_: One or more action lines meet the worked-example standard. A section
present but all lines are generic is FAIL.

---

**C-11 — Auto-PASS rules stated in preamble**

The preamble (SETUP block) lists the criteria that carry auto-PASS conditions and states
the condition for each. This appears before any output is scored.

_Pass condition_: Every auto-PASS-eligible criterion is listed with its named condition in
the SETUP block. Absent from preamble is FAIL; present but incomplete is PARTIAL.

---

**C-12 — Formula at preamble**

The composite scoring formula appears in the SETUP block before any output is scored.
The formula shows the N values for the current rubric version.

_Pass condition_: Formula is present in SETUP with correct N_essential, N_recommended,
N_aspirational values. Formula appearing only after the first scored output is PARTIAL.

---

**C-13 — Evidence-before-verdict ordering**

Within each scoring table, the column order is: Criterion | Evidence Quote | Verdict.
The evidence quote column precedes the verdict column. An explicit instruction enforcing
this column order appears in the rubric or preamble.

_Pass condition_: All scoring tables observe this column order AND the rubric or preamble
contains a declared column-order instruction. Tables with verdict before evidence are FAIL.
Tables in correct order without an explicit instruction are PARTIAL.

---

**C-14 — Per-criterion diagnostic question**

The SETUP block contains a criterion roster that includes a diagnostic question column.
Every criterion row has a question entry. The presence of this column before scoring begins
structurally enforces deliberate criterion-by-criterion scoring.

_Pass condition_: Criterion roster with diagnostic question column is present in SETUP.
Roster present but question column missing is FAIL. Roster present with some questions
missing is PARTIAL.

---

**C-15 — Preamble gate instruction**

The SETUP block contains an explicit sequencing instruction that prohibits opening any
output file until the preamble is complete. This instruction appears as a named imperative
before the first output section.

_Pass condition_: Gate instruction is present in SETUP as a standalone line or block.
Absent is FAIL. Present but positioned after the first output section is PARTIAL.

---

**C-16 — Named standalone auto-PASS block**

_Strengthens C-11._

Auto-PASS conditions appear as an explicit named-condition block in the SETUP, with each
eligible criterion declared by ID and condition in a form such as:
"C-05 auto-PASS when no criterion fails universally across all scored outputs."
Conditions implied by TBD placeholders, roster status columns, or embedded within
diagnostic question phrasing do not satisfy this criterion.

_Pass condition_: Every auto-PASS-eligible criterion has a standalone named declaration in
the SETUP block. Conditions implied rather than declared are PARTIAL. No explicit block is
FAIL.

---

**C-17 — Criterion-specific diagnostic questions**

_Strengthens C-14._

Each diagnostic question in the criterion roster interrogates the specific mechanism or
failure mode of that criterion — it could not be lifted and applied to a different criterion
without revision. Generic questions (e.g., "Did the scorer address this criterion?",
"Is this criterion satisfied?") that apply equally to any row do not satisfy this criterion.

_Pass condition_: All diagnostic questions are criterion-specific. A single generic question
is PARTIAL; more than 20% generic is FAIL. C-14 must also PASS for C-17 to be scored
(no roster → auto-FAIL).
