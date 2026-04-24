Reading the R5 scorecard, one new excellence pattern generates a new criterion:

**Worked-example carryforward preservation instruction** — C-10 was FAIL in V-02, V-03, V-04 because the worked example regressed when the axis shifted. V-05 (100.00) addressed this by including an explicit instruction mandating that the C-10 example be preserved or updated when the rubric is versioned forward. C-10 only requires a worked example to be present; it doesn't require a preservation rule. That gap is C-19.

N_aspirational rises from 11 → 12.

---

## quest-score Rubric — v6

_Updated from v5 after Round 5 scoring. One new aspirational criterion added from R5 excellence signals. N\_aspirational changes from 11 → 12._

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 4 | Verdicts present, evidence quotes, correct composite score, ranked leaderboard |
| Recommended (30%) | 3 | Failure patterns, excellence signals, regression signals |
| Aspirational (10%) | 12 | Actionable diagnosis, score distribution commentary, worked-example in action line, auto-PASS rules at preamble, formula at preamble, evidence-before-verdict ordering, per-criterion diagnostic question, preamble gate instruction, named standalone auto-PASS block, criterion-specific diagnostic questions, named standalone regression signals section, worked-example carryforward preservation instruction |

**Composite formula (v6 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 12 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 12.
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
- C-19 strengthens C-10: C-10 requires a worked example to appear in the action line; C-19 requires an explicit preservation rule stating that the worked example must be carried forward verbatim or updated to match the current round's axis when the rubric is versioned forward. The rule must appear near the C-10 definition or in the SETUP block — not implied by the general update protocol. Without C-19, the worked example regresses when the axis shifts to a new structural gap.

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
sourced from the scored output, not paraphrased from the rubric criterion text.

---

**C-03 — Composite score computed correctly**

The composite score reported for each output matches the formula applied to that output's
verdict table. Scoring uses the formula declared in the rubric with the current-version N
values.

_Pass condition_: Reported composite is within ±1 of the formula result derivable from the
verdict table. If the score cannot be verified from the visible verdict table, FAIL.

---

**C-04 — Ranked leaderboard present**

A ranked table listing all scored outputs from highest to lowest composite score is present.
Minimum columns: Rank, Output, Score, Golden.

_Pass condition_: Table is present, outputs are sorted by descending score, and the Golden
column correctly applies the golden threshold rule.

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-05 | **Failure patterns surfaced** | analysis | recommended |
| C-06 | **Excellence signals surfaced** | analysis | recommended |
| C-07 | **Regression signals surfaced** | analysis | recommended |

---

**C-05 — Failure patterns surfaced**

_Auto-PASS when no criterion fails universally across all scored outputs._

For each criterion that received FAIL or PARTIAL in every scored output, a failure pattern
entry is present describing what was missing and why it matters.

_Pass condition_: Every universally-failing criterion has a named pattern entry. Auto-PASS
applies when no such criterion exists.

---

**C-06 — Excellence signals surfaced**

For each output-criterion pair where one output outperforms the group by at least one tier
(e.g., PASS where others PARTIAL or FAIL), an excellence signal entry is present naming the
output, the criterion, and the distinguishing behavior.

_Pass condition_: At least one excellence signal entry present when score variance exists
across outputs. If all outputs score identically on all criteria, may be omitted.

---

**C-07 — Regression signals surfaced**

_Auto-PASS when no prior-round scorecard was provided._

When a prior-round scorecard is available, any criterion that dropped a tier (PASS →
PARTIAL, PASS → FAIL, PARTIAL → FAIL) between rounds is flagged with the criterion ID,
prior verdict, current verdict, and a mechanism note.

_Pass condition_: All regressions are named. Auto-PASS applies when no prior-round data is
provided.

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-08 | **Actionable diagnosis in failure patterns** | analysis | aspirational |
| C-09 | **Score distribution commentary** | analysis | aspirational |
| C-10 | **Worked-example in action line** | format | aspirational |
| C-11 | **Auto-PASS rules stated in preamble** | structure | aspirational |
| C-12 | **Formula reproduced before first output section** | structure | aspirational |
| C-13 | **Evidence-before-verdict ordering enforced** | correctness | aspirational |
| C-14 | **Per-criterion diagnostic question in roster** | structure | aspirational |
| C-15 | **Preamble gate instruction present** | structure | aspirational |
| C-16 | **Named standalone auto-PASS block** | structure | aspirational |
| C-17 | **Criterion-specific diagnostic questions** | correctness | aspirational |
| C-18 | **Named standalone regression signals section** | structure | aspirational |
| C-19 | **Worked-example carryforward preservation instruction** | structure | aspirational |

---

**C-08 — Actionable diagnosis in failure patterns**

_Auto-PASS when no failure patterns exist._

Each failure pattern entry includes an action line specifying: a verb, a specific artifact
filename, and a section location. No placeholder text permitted (no "[artifact]" or "TBD").

_Pass condition_: Every failure pattern action line is fully instantiated — verb + real
artifact name + real section path. Auto-PASS applies when no failure patterns exist.

---

**C-09 — Score distribution commentary**

The scorecard includes a note on score distribution: minimum score, maximum score, spread,
and a calibration observation (e.g., whether scores cluster tightly or spread widely, and
what that implies about rubric discrimination).

_Pass condition_: A score distribution note is present covering at least spread and a
calibration observation. May appear in the summary block or a dedicated section.

---

**C-10 — Worked-example in action line**

_Auto-PASS when no failure patterns exist._

At least one failure pattern action line is fully instantiated with a real example — a real
artifact name and a real section location — rather than a format template with placeholders.

_Pass condition_: At least one action line reads as a concrete instruction, not a format
spec. Example: "Add a named `### REGRESSION SIGNALS` section to `quest-score.md` after the
EXCELLENCE SIGNALS section, with columns for Criterion | Prior Verdict | Current Verdict |
Mechanism." Auto-PASS applies when no failure patterns exist.

---

**C-11 — Auto-PASS rules stated in preamble**

All auto-PASS conditions applicable to the current rubric version are declared in the SETUP
block before any per-output scoring begins. Each condition names the criterion ID and the
trigger phrase.

_Pass condition_: All auto-PASS conditions present in preamble block, each identified by
criterion ID.

---

**C-12 — Formula reproduced before first output section**

The composite formula with current-version N values is reproduced in full in the SETUP block
before the first per-output heading. A reference to the rubric document is not sufficient.

_Pass condition_: Formula with current N_essential, N_recommended, N_aspirational values
appears in the scoring template before the first output section heading.

---

**C-13 — Evidence-before-verdict ordering enforced**

The scoring template includes an explicit written mandate that the evidence quote column must
be written before the verdict column in every scoring table cell. The mandate names the
column order and states that reversing the order violates C-13.

_Pass condition_: A named section or declaration (e.g., "### Evidence-Ordering Mandate")
states the column order and prohibits verdict-before-evidence ordering. Implied order is not
sufficient.

---

**C-14 — Per-criterion diagnostic question in roster**

The SETUP criterion roster includes a Diagnostic Question column. Each row carries a
question the scorer should answer before rendering the verdict for that criterion.

_Pass condition_: Roster table includes a Diagnostic Question column with a non-empty entry
for every criterion row.

---

**C-15 — Preamble gate instruction present**

The SETUP block contains an explicit imperative instruction prohibiting the scorer from
opening any output file until the entire SETUP block is fully written.

_Pass condition_: A gate instruction in imperative form (e.g., "Do not open any output file
until SETUP is fully written.") is present in the SETUP block.

---

**C-16 — Named standalone auto-PASS block**

The auto-PASS conditions appear in a dedicated named block (e.g., "### Auto-PASS
Conditions") rather than embedded in the criterion roster, diagnostic questions, or inline
commentary. Each condition is a named declaration with criterion ID and trigger phrase.

_Pass condition_: A standalone named section contains all auto-PASS declarations. Each
declaration is self-contained — criterion ID + trigger phrase — not implied by surrounding
text.

---

**C-17 — Criterion-specific diagnostic questions**

Each diagnostic question in the C-14 roster interrogates the specific mechanism of its
criterion rather than a generic probe that could apply to any row (e.g., "Is this present?"
is generic; "Does the action line name a real artifact filename and section path?" is
criterion-specific).

_Pass condition_: Every diagnostic question in the roster is specific to the criterion it
accompanies. A question that could be moved to any other row without changing its meaning
fails this criterion.

---

**C-18 — Named standalone regression signals section**

The scoring template body contains a dedicated named section (e.g., "### REGRESSION
SIGNALS") for regression detection, appearing after the EXCELLENCE SIGNALS section. The
section is structurally separate from SETUP notes and per-output scoring tables. It includes
column headers: Criterion | Prior Verdict | Current Verdict | Mechanism. When C-07 auto-PASS
applies, the section is present but marked not applicable.

_Pass condition_: A named standalone section for regression signals is present in the
template body with the required columns. The section is present regardless of whether
prior-round data exists (auto-PASS inapplicability is noted inside the section, not by
omitting the section).

---

**C-19 — Worked-example carryforward preservation instruction**

The scoring template includes an explicit rule mandating that the C-10 worked example — the
fully instantiated action line — must be carried forward verbatim or updated to match the
current round's axis when the rubric is versioned forward. The instruction must appear near
the C-10 definition or in the SETUP block. An implicit expectation that the example will be
maintained is not sufficient.

_Pass condition_: A named instruction states that the C-10 worked example must be preserved
or updated on each rubric version increment, and identifies where the example lives (section
name or criterion ID). The instruction is explicit — not derivable only from the general
update protocol.
