Written to `simulations/quest/golden/quest-score-variate-R2-2026-03-16.md`.

---

## Summary

**5 variations against rubric v2-2026-03-16** (N_essential=5, N_recommended=3, N_aspirational=4):

| Variation | Axis | Target | Hypothesis |
|-----------|------|--------|------------|
| V-01 | D — Inertia framing: positive body anchor | C-11 | First evidence cell (V-01/C-01) written as a labeled `[MODEL CELL]`, planting the positive anchor in the scored body where C-11 requires it — not just in the instructions |
| V-02 | E — Output format: labeled declaration field | C-12 | Arithmetic verification block has a required `Matches stated score: [YES \| NO -- discrepancy: stated X, computed Y]` named slot, forcing binary declaration instead of prose pass-through |
| V-03 | F — Phrasing register: formula denominator guard | C-10/C-12 arithmetic | `FORMULA CHANGE ALERT` block at load time showing the old (A/2) and new (A/4) denominators, requiring the scorer to copy the corrected formula before proceeding |
| V-04 | D+E | C-11 + C-12 | Model cell in body + labeled declaration field — independent failure modes at Phase 2 and Phase 3 respectively |
| V-05 | D+E+F | C-11 + C-12 + arithmetic | All three: denominator guard at load, model cell at scoring entry, labeled declaration at verification — each axis fires at a different lifecycle point with no overlap |

**Key structural difference from R1 variations**: all 5 prompts score 12 criteria (C-01 through C-12) and use `(aspirational_pass/4 * 10)` — scorers who carry over R1's `A/2` formula will produce inflated scores that V-03/V-05's guard makes visible.
