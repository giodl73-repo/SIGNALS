Reading the scorecard notes to extract both new patterns, then writing the full v4 rubric.

**C-15 — Post-scoring completeness scan:** explicit verification step after all N output blocks, before `[SCORING COMPLETE]`, that confirms required in-block fields are present. Distinguishes scan-equipped variations (V-02/V-04/V-05) from instruction-only variations (V-01/V-03).

**C-16 — Pre-execution failure mode priming:** anti-patterns placed before Phase 1 so failure mode context loads before any structural work begins. Distinguishes V-03/V-05 from all other variations.

A_count goes 6 → 8.

```markdown
# quest-score Rubric — v4

**Version:** v4
**Date:** 2026-03-16
**Prior version:** quest-score-rubric-v3-2026-03-16.md

---

## What changed v3 -> v4

**Two new aspirational criteria, sourced directly from R3 excellence signals:**

**C-15 — Post-scoring completeness scan** (from V-02/V-04/V-05 scan-equipped variations)
- Root pattern in R3: V-02, V-04, and V-05 included an explicit verification step after all
  N output blocks were written but before `[SCORING COMPLETE]` was emitted; V-01 and V-03
  had the required-field instructions but no post-pass confirmation; the scan converts
  "instructions were present" into "compliance was verified before the report closed"
- The gate is structurally different from C-14: C-14 requires fields to be in-block;
  C-15 requires a named verification pass that confirms C-14 compliance across all outputs
  before the report is sealed; a variation satisfying C-14 can still fail C-15 if no scan
  step is present
- Pass condition: the score report contains an explicit post-output-block verification step
  (named scan, checklist pass, or equivalent audit token) that confirms required in-block
  fields are present across all outputs, placed after the last output block and before any
  `[SCORING COMPLETE]` marker or equivalent terminal token; absence of the scan step fails
  even if all output blocks are individually complete; PARTIAL if the scan is present but
  covers only a subset of outputs or a subset of required fields

**C-16 — Pre-execution failure mode priming** (from V-03/V-05 anti-pattern placement)
- Root pattern in R3: V-03 and V-05 placed anti-pattern descriptions before Phase 1 so that
  failure mode context was loaded into the execution window before any structural work began;
  all other variations either omitted anti-patterns or placed them in a later phase where
  they arrive after the first structural decisions are already made
- The principle: failure modes described after structural work begins can only correct
  in-progress execution; failure modes described before Phase 1 prime the model to avoid
  the pattern from the first token of structural output
- Pass condition: the score report (or the rubric driving it) surfaces anti-patterns or
  named failure modes in a section that precedes Phase 1 structural work; placement in a
  preamble, pre-phase warning block, or "before you begin" section satisfies the criterion;
  placement in Phase 3 or later, or in an appendix consulted after scoring, fails; PARTIAL
  if some failure modes are pre-placed but the most structurally critical ones (e.g.,
  in-block field omission, derivation skipping) appear only post-Phase 1

**Formula update:** A_count denominator `/6` → `/8` (8 aspirational criteria now:
C-09 through C-16). Max score and golden threshold unchanged.

---

## Criterion Summary

| ID | Criterion | Tier | Category |
|----|-----------|------|----------|
| C-01 | Complete verdict matrix — one block or row per criterion for each output; no cell blank or omitted | essential | completeness |
| C-02 | Evidence per verdict — each verdict cell cites a specific structural reference from the output | essential | correctness |
| C-03 | Formula-correct composite score — formula, weights, tier counts, and arithmetic applied correctly | essential | correctness |
| C-04 | Ranked leaderboard — all N outputs in a single descending list by composite score | essential | format |
| C-05 | Failure patterns identified — criteria failing across ALL outputs surfaced; absence stated if none | essential | coverage |
| C-06 | Excellence signals — outlier-high criterion-output pairs identified with structural mechanism named | recommended | depth |
| C-07 | Regression signals — degraded criterion-output pairs flagged when prior-round data is available | recommended | depth |
| C-08 | Per-output summary note — 1–3 sentence structural differentiator or miss per output | recommended | depth |
| C-09 | Golden threshold declaration per output — explicit YES/NO field in each output block | aspirational | format |
| C-10 | Failure-pattern root-cause diagnosis — "rubric gap" vs "skill design issue" label on each universal failure | aspirational | depth |
| C-11 | Rubric-adaptive formula derivation — tier counts derived from active rubric, not hardcoded literals | aspirational | correctness |
| C-12 | Structured diagnosis template — failure entries follow a fixed labeled template enforcing parallel structure | aspirational | format |
| C-13 | Derivation-complete gate marker — explicit completion marker after derivation block proves derivation preceded scoring | aspirational | correctness |
| C-14 | Required fields in primary output block — Golden and summary note appear as labeled slots inside the per-output verdict block, not deferred to synthesis | aspirational | format |
| C-15 | Post-scoring completeness scan — explicit verification pass after all output blocks confirms required in-block fields are present before the report is sealed | aspirational | correctness |
| C-16 | Pre-execution failure mode priming — anti-patterns placed before Phase 1 so failure mode context loads before any structural work begins | aspirational | format |

**Formula:** `(essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/8 * 10)`, max 100.
**Golden threshold:** all 5 essentials PASS + composite >= 80.

---

## Criterion Definitions

### ESSENTIAL — output fails without these

**C-01 — Complete verdict matrix**
Every output must have a verdict for every active criterion, with no blank or omitted cells.
A missing row or cell means the scoring pass was incomplete regardless of the composite score.
PARTIAL not applicable — any missing cell is a FAIL.

**C-02 — Evidence per verdict**
Each verdict cell must cite a specific structural reference from the output being scored
(section heading, field name, line, marker). "Passes" or "Yes" without a citation does not
satisfy this criterion. PARTIAL if the majority of cells have citations but a minority do not.

**C-03 — Formula-correct composite score**
The composite score must apply the correct formula with correct weights, correct tier counts
for the active rubric, and correct arithmetic. Using hardcoded tier counts from a prior
rubric version fails even if the arithmetic is internally consistent. PARTIAL if the formula
structure is correct but arithmetic contains a single minor error.

**C-04 — Ranked leaderboard**
All N outputs must appear in a single descending list by composite score. A leaderboard
missing any output, or presenting outputs in non-score order without explanation, fails.
PARTIAL if the leaderboard is present but one output is misplaced by one rank.

**C-05 — Failure patterns identified**
Criteria failing across ALL outputs must be explicitly surfaced as universal failures. If no
criterion fails universally, that absence must be stated. Silence on universal failures fails.
PARTIAL if universal failures are surfaced but without naming the failing criterion IDs.

---

### RECOMMENDED — output is stronger with these

**C-06 — Excellence signals**
Outlier-high criterion-output pairs (a criterion where one output distinctly outperforms
others) must be identified, with the structural mechanism that caused the excellence named —
not just "V-02 passes C-14" but "V-02 places the Golden field as a labeled slot inside the
verdict block, making omission structurally visible." PARTIAL if signals are identified
without mechanism.

**C-07 — Regression signals**
When prior-round data is available, degraded criterion-output pairs (criteria that passed
in a prior round but fail in the current round for a given output) must be flagged. If no
prior data is available, this criterion is not applicable for that scoring pass. PARTIAL if
regressions are flagged but without citing the prior-round pass state.

**C-08 — Per-output summary note**
Each output block must include a 1–3 sentence note naming the structural differentiator
(what the output does that others do not) or the structural miss (what it omits that others
include). Generic notes ("this output scores well") do not satisfy the criterion. PARTIAL
if notes are present for most outputs but absent for one.

---

### ASPIRATIONAL — separates good scorecards from excellent ones

**C-09 — Golden threshold declaration per output**
Each output block must contain an explicit `Golden: YES` or `Golden: NO` field (or
structurally equivalent labeled field). The golden determination must not be deducible
only from the composite score or leaderboard position — it must be stated. PARTIAL if
the field is present for some outputs but absent for others.

**C-10 — Failure-pattern root-cause diagnosis**
Each universal failure (C-05) must carry a root-cause label: either "rubric gap" (the
criterion does not have a strong enough specification to enforce the behavior) or "skill
design issue" (the prompt structure fails to produce the behavior even with a clear
criterion). A failure identified without a root-cause label does not satisfy this criterion.
PARTIAL if some failures have root-cause labels but others do not.

**C-11 — Rubric-adaptive formula derivation**
The tier counts used in the formula (E_count, R_count, A_count) must be explicitly derived
from the active rubric version at the time of scoring, not hardcoded from memory or a prior
version. The derivation must be shown (e.g., "counting active criteria: E=5, R=3, A=8").
PARTIAL if derivation is shown but contains an error corrected before scoring.

**C-12 — Structured diagnosis template**
Failure entries must follow a fixed labeled template enforcing parallel structure across all
failures (e.g., `Criterion:` / `Scope:` / `Root cause:` / `Evidence:`). Failure entries
written as free prose without a consistent template fail. PARTIAL if a template is used
but not all fields are populated for every entry.

**C-13 — Derivation-complete gate marker**
The score report must contain an explicit completion marker (e.g., `[DERIVE COMPLETE]` or
equivalent handoff token) immediately following the rubric derivation block, confirming
E_count/R_count/A_count were resolved before the first output verdict was written. A report
where derivation completeness can only be inferred from the presence of named variables does
not satisfy this criterion. Pre-printing the marker as static text in the prompt body without
an explicit `Write: [token]` emission instruction also fails — the marker must be emitted
as a deliberate act. Binary — PARTIAL not applicable.

**C-14 — Required fields in primary output block**
The `Golden:` field and per-output summary note must appear as labeled slots within the same
structural block as the verdict matrix for each output. Placement of either field exclusively
in a leaderboard, synthesis, or separate aggregation section fails, even if C-09 is otherwise
satisfied. PARTIAL if some output blocks carry the fields in-block but others defer to
synthesis.

**C-15 — Post-scoring completeness scan**
The score report must contain an explicit post-output-block verification step — a named scan,
checklist pass, or equivalent audit token — that confirms required in-block fields (verdict
matrix, Golden, summary note) are present across all outputs. This step must appear after
the last output block and before any `[SCORING COMPLETE]` marker or terminal token.
Absence of the scan fails even if all output blocks are individually complete. Satisfying
C-14 does not imply C-15 — the scan is a separate structural element. PARTIAL if the scan
is present but covers only a subset of outputs or a subset of required fields.

**C-16 — Pre-execution failure mode priming**
Anti-patterns or named failure modes must appear in a section that precedes Phase 1
structural work — a preamble, pre-phase warning block, or "before you begin" section.
Placement in Phase 3 or later, or in an appendix consulted after scoring, fails. The intent
is that failure mode context loads before any structural decisions are made, not as a
correction mid-execution. PARTIAL if some failure modes are pre-placed but the most
structurally critical ones (in-block field omission, derivation skipping, hardcoded tier
counts) appear only post-Phase 1.
```
