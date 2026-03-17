The file is fully written. Here is the complete updated rubric as Markdown:

---

# Rubric -- topic-plan (v18)

**Skill**: `topic:plan`
**Version**: v18 (promoted from v17 after Round 18 excellence signal extraction)
**Date**: 2026-03-15

---

## Summary

| Tier | Count | Points | Criteria |
|------|-------|--------|----------|
| Essential | 5 | 60 | Read strategy, read signals, identify delta, type proposals, confirm gate |
| Recommended | 3 | 30 | Evidence citations, before/after view, all three change types |
| Aspirational | 53 | 265 | ...+ Inertia recurrence as unforgeable verbatim block; slot architecture generalized to all decision sites; Narrative Format Contract declared upfront |

**Total possible: 355 pts**

---

## Changes v17 → v18

Three new aspirational criteria extracted from three R18 variation axes.

**C-59 — Inertia recurrence as unforgeable verbatim block template** (`behavior`)
Extends C-56. C-56 requires recurrence markers at named downstream decision gates — but allows any form, including inline recalled sentences. C-59 closes the gap: a recalled sentence ("Recall: inertia is a co-equal option. See above.") can be silently compressed or omitted without leaving a visible gap. A named verbatim block template (`[INERTIA-GATE]`) defined once in the preamble and reproduced at each gate is structurally unforgeable — block absence is immediately visible, parallel to C-57's pre-printed calibration slot and C-40's null-case CONTRACT rule. A C-56 pass whose recurrence markers are inline prose rather than reproduced verbatim blocks fails C-59. Source: V-01 (INERTIA-GATE block defined in preamble; reproduced at Steps 4, 4b, 7; V-04's recalled-sentence recurrence confirms the discriminating signal).

**C-60 — Pre-printed slot architecture generalized to all binary decision sites** (`enforcement`)
Extends C-57. C-57 requires the calibration check to use a pre-printed slot. C-60 generalizes this to every binary decision/commitment site throughout the prompt — schema-commitment decisions, null-case section markers, empty-type row declarations, checkpoint verdicts. Each such site is a composition-risk site: a conditional branch lets the model paraphrase, partially emit, or produce hybrid output; a pre-printed `[ ] A / [ ] B` slot eliminates composition risk at that site. A C-57 pass that applies the slot only to the calibration check while leaving other decision sites as conditional branches fails C-60. Source: V-02 (pre-printed slots at schema commitment, null cases, empty-type rows, schema checkpoints, and calibration check — all with "select exactly one and write it as output").

**C-61 — Narrative Format Contract declared upfront as a named block before Step 1** (`enforcement`)
Extends C-58. C-58 requires narrative gate rows to name the degenerate register; those gate rows are encountered mid-execution under context pressure. C-61 requires the narrative register requirement to be declared as a named Narrative Format Contract block before Step 1 — before any step is executed — naming both the required register ("conclusion before evidence") and the degenerate register ("step-description narrative — FAIL"). Parallel to C-26 (output schema before file reading) and C-36 (COLUMN CONTRACT before schema): the model holds the register commitment before encountering any narrative requirement. A C-58 pass whose gate rows name the degenerate form but define the requirement only at gate locations fails C-61. Source: V-03 (Narrative Format Contract block defined upfront; enforced at all five analytical steps; PHASE 3 EXIT GATE checks register compliance across all five sites).

**Updated totals**: 61 criteria, 355 pts | Formula: `(essential/5×60) + (recommended/3×30) + (aspirational/53×265)` | Golden threshold: **210**

---

The file is written to `simulations/quest/rubrics/topic-plan-rubric-v18-2026-03-15.md`. The v17 file is restored to its original content.
