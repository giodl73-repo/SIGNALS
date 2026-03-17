**R6 variations written** to `simulations/quest/golden/trace-component-variate-R6-2026-03-15.md`.

---

## Round 6 Summary

**New criteria targeted**: C-18 (role-level vocabulary enforcement gate) and C-19 (pre-declared named column schemas).

**The core insight driving all five variations**: R5's gap was structural — the vocabulary constraint was a *passive instruction* and the schemas were *inline content*, not pre-declared artifacts. R6 fixes both by making each a named blocking artifact.

### Variation axes and C-18/C-19 mechanisms

| | C-19: How schemas are pre-declared | C-18: How the gate blocks |
|--|---|---|
| **V-01** Schema-first | Standalone Role 1 (sole output: TABLE-01 + TABLE-04 schemas) | Standalone Role 3 (sole output: GATE-VOCAB token; Role 4 blocked) |
| **V-02** Contract-first | Role 2 declares schemas *after* contract using neutral column names | Step 2c embedded in Role 2; gate stated before role emits completion |
| **V-03** Imperative checklist | PRE-FLIGHT Step P-1 and P-2 with explicit PASS/FAIL conditions | Boxed STOP BLOCK requiring `[GATE-VOCAB: PASS]` token before trace checklist |
| **V-04** Phase-gated | Phase 1 has schemas as its *only* output artifact | Phase 3 is the gate phase; Phase 4 gated on `GATE-ARTIFACT: PASS` |
| **V-05** TA fusion | First two blocks of the TRACE ARCHITECTURE named artifact | Final step of TRACE ARCHITECTURE; sealed only after GATE-VOCAB: PASS |

**Key hypothesis to watch**: V-01 uses the most explicit role separation (5 roles) while V-05 fuses architecture down to 3 roles. If V-05 matches V-01's score, role fusion is safe — if V-01 outperforms, the explicit blocking transition outweighs the structural overhead cost.
