v2 written. Summary of changes:

**Two new aspirational criteria from Round 1 signals:**

- **C-11** — Composite formula embedded inline with concrete denominators
  - Cause: V-01/V-02 scored 80; V-03/V-04/V-05 scored 68. The only structural difference was whether the formula was stated in the prompt body. Symbolic denominators (`N_essential`) also fail — the formula must resolve to the current criterion counts.

- **C-12** — Anti-conflation guard present in the dual-gate section
  - Cause: V-03/V-04 had explicit prohibitions ("Do not conflate"; "A single paragraph covering both is not acceptable"). Gate labeling alone is fragile — an operator can still write a compound check that nominally touches both gates. The prohibition must be stated.

**Formula updated**: aspirational denominator `/ 2` → `/ 4` (4 aspirational criteria now).

**New failure modes added**: QG-08 (matrix without formula) and QG-09 (gate labels without anti-conflation guard).

**Excellence Signals Log added** as a standing section — each round appends its QU2 findings with evidence, mechanism, and the principle that became a criterion.
