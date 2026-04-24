Written to `simulations/quest/rubrics/topic-plan-rubric-v13-2026-03-15.md`.

---

## Changes from v12 → v13

**Two new aspirational criteria** extracted from Round 13:

**C-42 — Column-complete pass/fail pairing within each CONTRACT rule** (`depth`)

The discriminating signal is the PARTIAL on C-38 for V-03/V-04/V-05. C-38 requires equal *specificity* (both examples are concrete, quoted, labeled). C-42 requires equal *coverage*: the PASS column set and FAIL column set must be identical within each rule. V-03 misses 1 FAIL column, V-04 misses 2, V-05 misses 3 — all have more PASS columns than FAIL columns in Rule 1. V-01 provides PASS+FAIL for all 5 governed columns. The test: enumerate the columns represented in PASS examples and in FAIL examples — both sets must match exactly.

**C-43 — Cross-rule example coverage: pass/fail symmetry applied to all CONTRACT rules** (`enforcement`)

The discriminating signal is V-01's Rule 2 (4+4 paired examples for the independence test) and Rule 3 (paired examples for both null-case enforcement components). V-02/V-03/V-04/V-05 concentrate example symmetry in Rule 1. C-43 requires every CONTRACT rule that governs a column constraint or operational test to carry symmetric paired examples — not only the primary rule. A C-42 pass for Rule 1 that leaves Rules 2+ unilluminated fails C-43.

**Relationship**: C-42 is the within-rule requirement (column-complete pairing inside each exhibit); C-43 is the across-rules requirement (that within-rule discipline applied uniformly). Together they complete the exemplification architecture that C-38 initiated.

**Updated totals**: 43 criteria, 265 pts | Formula: `(essential/5×60) + (recommended/3×30) + (aspirational/35×175)` | Golden threshold bumped to **155**.
