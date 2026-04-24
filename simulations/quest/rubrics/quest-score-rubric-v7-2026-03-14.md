## quest-score Rubric — v7

_Updated from v6 after Round 6 scoring. Two new aspirational criteria added from R6 excellence signals. N\_aspirational changes from 12 → 14._

**Structure:**

| Tier | Count | Criteria |
|------|-------|----------|
| Essential (60%) | 4 | Verdicts present, evidence quotes, correct composite score, ranked leaderboard |
| Recommended (30%) | 3 | Failure patterns, excellence signals, regression signals |
| Aspirational (10%) | 14 | Actionable diagnosis, score distribution commentary, worked-example in action line, auto-PASS rules at preamble, formula at preamble, evidence-before-verdict ordering, per-criterion diagnostic question, preamble gate instruction, named standalone auto-PASS block, criterion-specific diagnostic questions, named standalone regression signals section, worked-example carryforward preservation instruction, preservation rule imperative form, worked example FAILURE PATTERNS location lock |

**Composite formula (v7 N values):**

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 14 * 10)

N_essential = 4, N_recommended = 3, N_aspirational = 14.
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
- C-20 strengthens C-19: C-19 requires an explicit preservation rule; C-20 requires that the rule be stated in imperative grammar ("must be carried forward verbatim or updated"), not interrogative form ("has it been carried forward?"). Interrogative form converts the rule into a diagnostic probe — it earns C-19 PARTIAL but C-20 FAIL. The imperative form is what makes the instruction enforceable at version time, not merely checkable at scoring time.
- C-21 strengthens C-10: C-10 requires a worked example to appear in the action line; C-21 requires the worked example to appear specifically in the FAILURE PATTERNS action line, not in SETUP, not in a preservation checkpoint, not in a roster diagnostic question. The SETUP block may contain a C-19 preservation instruction without absorbing the C-10 instantiated example. Relocating the worked example into SETUP — even for lifecycle-clarity reasons — causes a C-10 FAIL because the action line in FAILURE PATTERNS is what triggers the instantiation requirement.

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

Every rubric criterion is scored for every output. The verdict matrix is complete: rows are rubric criteria, columns are scored outputs (or the inverse). Count of verdict cells == (number of outputs) × (number of rubric criteria). Even a single missing cell is a FAIL.

_Pass condition_: All criterion × output cells are present and carry a PASS / PARTIAL / FAIL label. A missing row or column is a FAIL.

---

**C-02 — Evidence quote for every verdict**

Each PASS / PARTIAL / FAIL verdict is accompanied by a verbatim or near-verbatim quote extracted from the scored output. The quote must be clearly tied to that criterion (not a generic excerpt).

_Pass condition_: Every verdict row or cell includes a non-empty quote field. The quote is sourced from the scored output, not paraphrased from the rubric criterion text.

---

**C-03 — Composite score computed correctly**

The composite score is computed from the visible verdict table using the formula with the correct N values for the rubric version. N_essential = 4, N_recommended = 3, N_aspirational = 14 (v7). A tolerance of ±1 is permitted for rounding.

_Pass condition_: The stated composite score can be re-derived from the visible verdict table within ±1. FAIL if the score cannot be verified from the table (catches hallucinated scores) or if N values from a prior rubric version are used.

---

**C-04 — Ranked leaderboard present**

A leaderboard table ranks all scored outputs from highest to lowest composite score. The table contains at minimum: Rank, Output, Score, Golden columns.

_Pass condition_: A ranked table with all four columns is present. All scored outputs appear in the table. Golden threshold is applied correctly (all 4 essentials PASS AND composite >= 80).

---

### RECOMMENDED

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-05 | **Failure patterns surfaced** | analysis | recommended |
| C-06 | **Excellence signals surfaced** | analysis | recommended |
| C-07 | **Regression signals surfaced** | analysis | recommended |

---

**C-05 — Failure patterns surfaced**

A dedicated FAILURE PATTERNS section identifies every criterion that received FAIL or PARTIAL in every scored output (universal failures). For each such criterion, the section names the pattern and provides an action line.

_Pass condition_: Section is present. All universal-failure criteria are listed with an associated action line. Auto-PASS when no criterion fails universally across all scored outputs.

---

**C-06 — Excellence signals surfaced**

A dedicated EXCELLENCE SIGNALS section identifies output-criterion pairs where one output outperforms the group by at least one tier (e.g., PASS vs. PARTIAL, or PARTIAL vs. FAIL).

_Pass condition_: Section is present. At least one differentiating pattern is identified when such differentials exist. A note is added when no differential exists.

---

**C-07 — Regression signals surfaced**

When a prior-round scorecard was provided, a regression signals section compares current-round verdicts against prior-round verdicts and flags any criterion that declined.

_Pass condition_: Section is present with prior/current verdict comparison columns. Auto-PASS when no prior-round scorecard is provided.

---

### ASPIRATIONAL

| ID | Criterion | Category | Weight |
|----|-----------|----------|--------|
| C-08 | **Actionable diagnosis in failure patterns** | analysis | aspirational |
| C-09 | **Score distribution commentary** | analysis | aspirational |
| C-10 | **Worked example in action line** | format | aspirational |
| C-11 | **Auto-PASS rules stated in preamble** | structure | aspirational |
| C-12 | **Formula reproduced before first output section** | structure | aspirational |
| C-13 | **Evidence-before-verdict ordering enforced** | structure | aspirational |
| C-14 | **Per-criterion diagnostic question in roster** | structure | aspirational |
| C-15 | **Preamble gate instruction present** | structure | aspirational |
| C-16 | **Named standalone auto-PASS block** | structure | aspirational |
| C-17 | **Criterion-specific diagnostic questions** | structure | aspirational |
| C-18 | **Named standalone regression signals section** | structure | aspirational |
| C-19 | **Worked-example carryforward preservation instruction** | structure | aspirational |
| C-20 | **Preservation rule imperative form** | structure | aspirational |
| C-21 | **Worked example FAILURE PATTERNS location lock** | structure | aspirational |

---

**C-08 — Actionable diagnosis in failure patterns**

Each failure pattern entry includes an action line with a verb, a specific artifact filename, and a section location. The action line is fully instantiated — no format placeholders like `[verb]` or `[artifact]`. Example: _"Add a 'C-10 Worked-Example Preservation Rule:' sentence to quest-score.md in the SETUP block immediately after the C-10 auto-PASS declaration, stating that the worked example must be carried forward verbatim or updated to reflect the current round's axis criterion when the rubric is versioned forward."_

_Pass condition_: Every failure pattern entry has a fully instantiated action line with verb + real artifact filename + section location. Auto-PASS when no failure patterns exist.

---

**C-09 — Score distribution commentary**

The scorecard includes commentary on score distribution: minimum, maximum, spread, and a calibration note on what the spread indicates (e.g., well-discriminating rubric, ceiling effect, compression).

_Pass condition_: A distribution note with at least min/max/spread values is present. Calibration language appears somewhere in the scorecard summary.

---

**C-10 — Worked example in action line**

The FAILURE PATTERNS action line includes a fully instantiated worked example — a real artifact name and section location, not a format placeholder. The worked example must appear in the FAILURE PATTERNS action line specifically (not in SETUP, not in a roster column).

_Pass condition_: At least one action line in FAILURE PATTERNS contains a fully instantiated example with a real artifact name and section path. Format-only placeholders (e.g., `Action: [verb] [artifact] [section]`) with no instantiation do not satisfy this criterion. Auto-PASS when no failure patterns exist.

---

**C-11 — Auto-PASS rules stated in preamble**

The scoring template preamble (SETUP block) explicitly states all auto-PASS conditions by criterion ID and trigger phrase. Covered criteria: C-05, C-07, C-08, C-10.

_Pass condition_: All four auto-PASS declarations appear in the SETUP block, each naming the criterion ID and the trigger condition. Conditions buried in prose or roster columns without explicit preamble placement do not satisfy this criterion.

---

**C-12 — Formula reproduced before first output section**

The composite score formula with current-version N values is reproduced in the SETUP block before any per-output scoring section begins.

_Pass condition_: Formula with correct N values (N_essential=4, N_recommended=3, N_aspirational=14 for v7) appears in SETUP before the first per-output heading. Use of N values from a prior rubric version is a FAIL.

---

**C-13 — Evidence-before-verdict ordering enforced**

The scoring template contains an explicit written mandate requiring that the evidence quote precede the verdict label within every scoring table cell. Column order is stated as: Criterion | Evidence Quote | Verdict. The mandate must prohibit reversing the order.

_Pass condition_: An explicit, written mandate stating evidence-before-verdict ordering is present in the template. Preferred-order suggestions without a prohibition on reversal do not satisfy this criterion.

---

**C-14 — Per-criterion diagnostic question in roster**

The criterion roster in the SETUP block includes a Diagnostic Question column. Every criterion row (all 21 rows for v7) has a non-empty diagnostic question.

_Pass condition_: A Diagnostic Question column is present in the roster. All 21 criterion rows have non-empty questions. A roster without the column, or with any empty question row, is a FAIL.

---

**C-15 — Preamble gate instruction present**

The SETUP block ends with an explicit gate instruction prohibiting the scorer from opening any output file until the SETUP block is fully written.

_Pass condition_: An imperative gate statement (e.g., "Do not open any output file until SETUP is fully written") appears at or near the end of the SETUP block.

---

**C-16 — Named standalone auto-PASS block**

The auto-PASS conditions appear in a dedicated named section (e.g., "### Auto-PASS Conditions") rather than embedded in roster columns, diagnostic questions, or inline commentary. Each declaration names the criterion ID and trigger phrase explicitly.

_Pass condition_: A standalone named block for auto-PASS conditions is present. Conditions embedded in prose or roster columns without a standalone section header do not satisfy this criterion.

---

**C-17 — Criterion-specific diagnostic questions**

Each diagnostic question in the criterion roster interrogates the specific mechanism of that criterion — not a generic probe that could apply to any row. Questions must name what to count, what to verify, or what distinction to apply for that specific criterion.

_Pass condition_: At least three criterion rows have questions naming criterion-specific mechanisms (e.g., a count for C-01, the N-value for C-03, the form distinction for C-19/C-20). Generic questions like "Is this criterion satisfied?" do not satisfy C-17.

---

**C-18 — Named standalone regression signals section**

The regression detection logic is encapsulated in a dedicated named section (e.g., "### REGRESSION SIGNALS") in the scoring template body — not handled through SETUP notes or inline commentary.

_Pass condition_: A standalone named section for regression signals is present in the template body, separate from SETUP and per-output scoring tables. The section includes prior/current verdict comparison columns.

---

**C-19 — Worked-example carryforward preservation instruction**

An explicit preservation rule states that the worked example in the FAILURE PATTERNS action line must be carried forward verbatim or updated to reflect the current round's axis criterion when the rubric is versioned forward. The rule must appear near the C-10 definition or in the SETUP block — not implied by a general update protocol.

_Pass condition_: An explicit preservation rule is present near the C-10 definition or in the SETUP block. Interrogative form ("has it been carried forward?") earns PARTIAL. Imperative form ("must be carried forward verbatim or updated") earns PASS.

---

**C-20 — Preservation rule imperative form**

The C-19 preservation rule uses imperative grammar — a mandatory verb such as "must", "shall", or "is required to" — rather than interrogative form ("has it been carried forward?") or conditional form ("if versioning, update the example"). Interrogative and conditional forms convert the rule into a probe and are unenforceable at version time.

_Pass condition_: The preservation rule contains an imperative construction with a mandatory verb. An interrogative probe in the same location earns C-19 PARTIAL but C-20 FAIL. Location alone does not satisfy C-20 — form is the deciding factor.

---

**C-21 — Worked example FAILURE PATTERNS location lock**

The fully instantiated worked example satisfying C-10 appears specifically in the FAILURE PATTERNS action line — not in SETUP, not in a preservation checkpoint, not in a roster diagnostic question. The SETUP block may reference or mandate carryforward of the worked example (for C-19/C-20 purposes) but must not be the sole location of the instantiated example.

_Pass condition_: A fully instantiated worked example with a real artifact name and section path appears in the FAILURE PATTERNS action line. If the worked example exists only in SETUP or elsewhere, C-21 FAIL (and C-10 FAIL). Auto-PASS when no failure patterns exist.
