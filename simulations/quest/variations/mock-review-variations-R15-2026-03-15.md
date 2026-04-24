Written to `simulations/quest/golden/mock-review-variate-R15-2026-03-15.md`.

---

## Summary

**R15 gap from R14:** Two new criteria added to the v15 rubric, both deriving from the same structural escalation pattern (named constraint → header declaration):

| New criterion | What's required | Implementation approach |
|---|---|---|
| **C-40** | Criterion-ID parenthetical labels in named structural block headers | `FORBIDDEN OUTPUTS TRIAD (C-27, C-29, C-31, C-39, C-40):` etc. |
| **C-41** | Row-position annotations in CROSS-TEMPLATE RELATIONSHIP BLOCK | Either inline `Row N:` prefix or dedicated leftmost `Row #` column |

**Five variations — single-axis first, then combined:**

| Variation | Axis | Key structural move |
|---|---|---|
| **V-01** | C-40 minimal (4 core blocks), C-41 inline, Strategy-first | Labels only the 4 blocks named in C-40 definition; misses C-36 (structurally unreachable, Strat-first) |
| **V-02** | C-41 dedicated row column, Arch-first, table-centric | Leftmost `Row #` column — row position always in first cell, independent of field name length; misses C-35 |
| **V-03** | C-40 maximum (all named elements), Arch-first | Every step gate, canary block, and error block gets criterion-ID label; misses C-35 |
| **V-04** | C-40 minimal + C-41 inline + Arch-first + verbose step-name anchors | Deepens C-28; every gate names both step number and descriptive label; misses C-35 |
| **V-05** | C-40 maximum + C-41 dedicated column + polarity asymmetry + SQ propagation | Ceiling: FIELD SYMMETRY AND ASYMMETRY block encodes both structural analogy and opposite polarity vs DEFAULT DECISION POSITION; SQ-1 annotated at collection site with explicit forward-propagation note; misses C-35 |

**Expected score:** 32/33 aspirational = **99.7** across all variants (same ceiling as R14; the structural C-35/C-36 exclusion by role sequence is unavoidable at denominator 33).

**Excellence signal for V-05** beyond R14: the polarity asymmetry block now makes the DEFAULT DECISION POSITION inertia structure verifiable from the template comparison alone — two blocks (FIELD SYMMETRY + POLARITY ASYMMETRY) replace the need to reference the standalone DEFAULT DECISION POSITION block, closing the last advisory dependency in the skill.
