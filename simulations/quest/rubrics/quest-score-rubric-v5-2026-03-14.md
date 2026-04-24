Reading the R4 scorecard, one new excellence pattern emerges from V-01's C-07 PARTIAL verdict:

**Named standalone regression signals section** — C-07 was PARTIAL because "regression handling is implicit, not structured" — regression detection was noted in SETUP but had no dedicated named section in the template body. C-07 only requires regression signals to be surfaced when prior-round data exists; it doesn't require a named structural section. That gap is C-18.

This mirrors the R3 → R4 pattern exactly: C-11 (auto-PASS rules at preamble) was PARTIAL because conditions were implied → C-16 required a named standalone block. Now C-07 (regression signals surfaced) was PARTIAL because regression handling was implicit → C-18 requires a named standalone section.

N_aspirational rises from 10 → 11.

---

## quest-score Rubric — v5

_Updated from v4 after Round 4 scoring. One new aspirational criterion added from R4 excellence signals. N\_aspirational changes from 10 → 11._

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 4 | Verdicts present, evidence quotes, correct composite score, ranked leaderboard |
| Recommended (30%) | 3 | Failure patterns, excellence signals, regression signals |
| Aspirational (10%) | 11 | Actionable diagnosis, score distribution commentary, worked-example in action line, auto-PASS rules at preamble, formula at preamble, evidence-before-verdict ordering, per-criterion diagnostic question, preamble gate instruction, named standalone auto-PASS block, criterion-specific diagnostic questions, named standalone regression signals section |

**Composite formula (v5 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 11.
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
- C-18 strengthens C-07: C-07 requires regression signals to be surfaced when prior-round data exists; C-18 requires the regression detection logic to be encapsulated in a dedicated named section (e.g., "### REGRESSION SIGNALS") in the scoring template body, not handled implicitly through SETUP notes or inline commentary.

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
are a FAIL.

---

**C-03 — Composite score computed correctly**

The composite score is derived from the visible verdict table using the rubric formula. It
can be independently verified from the PASS/PARTIAL/FAIL counts in the scorecard.

_Pass condition_: Score matches the formula result within ±1 (rounding tolerance). FAIL if
the score cannot be verified from the visible verdict table, or if the formula used differs
from the stated rubric formula.

---

**C-04 — Ranked leaderboard present**

A leaderboard section ranks all scored outputs from highest to lowest composite score.

_Pass condition_: Table present with at minimum columns for Rank, Output identifier, Score,
and Golden status. All scored outputs appear. Ties broken by essential-tier score then
recommended-tier score.

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-05 | **Failure patterns surfaced** | diagnosis | recommended |
| C-06 | **Excellence signals surfaced** | diagnosis | recommended |
| C-07 | **Regression signals surfaced** | diagnosis | recommended |

---

**C-05 — Failure patterns surfaced**

_Auto-PASS when no criterion receives FAIL or PARTIAL in every scored output._

For each criterion that failed or was partial in every scored output, a failure pattern
entry identifies the criterion, quotes the evidence, and states the pattern across outputs.

_Pass condition_: All universal failures are documented. PARTIAL if some are documented but
others are omitted. FAIL if the section is absent when universal failures exist.

---

**C-06 — Excellence signals surfaced**

For each output-criterion pair where one output outperforms the group by at least one
verdict tier, an excellence signal entry names the output, the criterion, and quotes the
distinguishing evidence.

_Pass condition_: All tier-differential pairs are documented. PARTIAL if some are documented
but others are omitted. FAIL if the section is absent or empty when signals exist.

---

**C-07 — Regression signals surfaced**

_Auto-PASS when no prior-round scorecard is provided to the scorer._

When prior-round data exists, the scorecard compares current scores to prior-round scores
and calls out criteria where the score dropped.

_Pass condition_: All regressions (score decrease of any magnitude) are named with
prior-round vs. current-round verdict. PARTIAL if regressions are noted implicitly but not
structured. FAIL if no comparison is made when prior data exists.

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-08 | **Actionable diagnosis in failure patterns** | diagnosis | aspirational |
| C-09 | **Score distribution commentary** | analysis | aspirational |
| C-10 | **Worked example in action line** | diagnosis | aspirational |
| C-11 | **Auto-PASS rules stated in preamble** | structure | aspirational |
| C-12 | **Formula reproduced before first output section** | structure | aspirational |
| C-13 | **Evidence-before-verdict ordering enforced** | structure | aspirational |
| C-14 | **Per-criterion diagnostic question in roster** | structure | aspirational |
| C-15 | **Preamble gate instruction present** | structure | aspirational |
| C-16 | **Named standalone auto-PASS block** | structure | aspirational |
| C-17 | **Criterion-specific diagnostic questions** | structure | aspirational |
| C-18 | **Named standalone regression signals section** | structure | aspirational |

---

**C-08 — Actionable diagnosis in failure patterns**

_Auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-08 auto-PASS)._

Each failure pattern entry includes an action line specifying verb + artifact + location:
what to change, in which file, in which section.

_Pass condition_: Every failure pattern entry has a fully instantiated action line. PARTIAL
if action lines are present but vague (missing artifact or location). FAIL if no action
lines exist.

---

**C-09 — Score distribution commentary**

The scorecard includes a commentary note on score spread: min, max, range, and whether
scores cluster (indicating calibration issues) or spread (indicating discriminating rubric).

_Pass condition_: A distribution note appears in the leaderboard section or immediately
after it. FAIL if absent.

---

**C-10 — Worked example in action line**

_Auto-PASS when no failure patterns exist (C-05 auto-PASS triggers C-10 auto-PASS)._

At least one action line in the failure patterns section is a fully instantiated example:
concrete verb, specific artifact name, and exact location within that artifact.

_Pass condition_: One or more action lines are fully concrete with no placeholders. PARTIAL
if action lines are templated but not instantiated. FAIL if all action lines are generic.

---

**C-11 — Auto-PASS rules stated in preamble**

All criteria with auto-PASS conditions are listed in the SETUP section of the scorecard
before any output is scored.

_Pass condition_: All auto-PASS conditions appear in SETUP. PARTIAL if some are stated but
others are absent. FAIL if no auto-PASS conditions are stated in SETUP.

---

**C-12 — Formula reproduced before first output section**

The composite formula — including N values for all three tiers — appears in the SETUP
section before the first output is scored.

_Pass condition_: Formula block with N_essential, N_recommended, N_aspirational present in
SETUP. FAIL if formula is absent from SETUP or appears only after output scoring begins.

---

**C-13 — Evidence-before-verdict ordering enforced**

In every scoring table, the column order is Criterion | Evidence Quote | Verdict. The
evidence quote precedes the verdict in every cell.

_Pass condition_: Column order is correct in all output scoring tables and no verdict
appears before its evidence. FAIL if any scoring table has verdict before evidence, or if
column order is not stated.

---

**C-14 — Per-criterion diagnostic question in roster**

The SETUP criterion roster includes a diagnostic question column. Each criterion row has a
question associated with it before scoring begins.

_Pass condition_: Roster table has a Diagnostic Question column and every row has a
non-empty question. PARTIAL if some rows have questions and others do not. FAIL if the
column is absent.

---

**C-15 — Preamble gate instruction present**

The SETUP section contains an explicit sequencing gate instruction that prohibits the
scorer from opening any output file until SETUP is fully written.

_Pass condition_: A gate instruction (e.g., "Do not open any output file until SETUP is
complete") appears in SETUP. FAIL if absent.

---

**C-16 — Named standalone auto-PASS block**

_Strengthens C-11._

The auto-PASS conditions appear as a standalone named block in the SETUP section. Each
condition is declared as an explicit named statement keyed to its criterion ID and trigger
phrase (e.g., "C-05 auto-PASS when no criterion fails universally across all scored
outputs"), not implied by TBD placeholders or embedded in diagnostic question phrasing.

_Pass condition_: Block is present as a named section; all auto-PASS conditions are keyed
to criterion IDs with trigger phrases. PARTIAL if conditions are present but not keyed to
IDs or triggers. FAIL if no standalone block exists.

---

**C-17 — Criterion-specific diagnostic questions**

_Strengthens C-14._

Each diagnostic question in the SETUP roster interrogates the specific mechanism of its
criterion. The question could not apply unchanged to a different criterion row.

_Pass condition_: Every diagnostic question is criterion-specific — it names the mechanism,
artifact, or behavior unique to that criterion. PARTIAL if some questions are
criterion-specific and others are generic. FAIL if all questions are generic placeholders.

---

**C-18 — Named standalone regression signals section**

_Strengthens C-07._

When prior-round data exists, regression detection is encapsulated in a dedicated named
section (e.g., "### REGRESSION SIGNALS") in the scoring template body. Regression handling
is not implicit through SETUP notes or inline commentary embedded within individual output
scoring tables.

_Pass condition_: A named regression signals section appears in the template body, separate
from SETUP and from per-output scoring tables, and contains structured comparison entries
(criterion, prior verdict, current verdict). PARTIAL if regressions are noted but not in
a dedicated named section. FAIL if no regression section exists when prior data is
available.
