Written to `simulations/quest/golden/quest-score-variate-R8-2026-03-16.md`.

---

**R8 variations summary:**

| Variation | Axes | Key structural change | Predicted composite |
|-----------|------|-----------------------|---------------------|
| V-01 | U | Binary `Locatability test: YES/NO` field added to MODEL CELL | 96.875 |
| V-02 | V | `Reason (if PARTIAL)` column added to bilateral audit table | 96.875 |
| V-03 | W | Advisory text only -- both C-23/C-24 stated in instructions, no schema | 96.5625 |
| V-04 | P+Q+R+U | R7 champion + locatability assertion; C-24 still PARTIAL | 99.375 |
| V-05 | P+Q+R+U+V | Full integration; C-23 and C-24 both PASS | 99.6875 |

**Three diagnostic questions this round resolves:**

1. **V-01 == V-02**: Confirms U and V are symmetric contributions -- each achieves PASS on its own target and PARTIAL on the other. Equal weight, equal composite.

2. **V-01/V-02 > V-03**: Schema enforcement (named field template, column constraint) vs instruction-only. Predicted 0.3125-point gap. If V-03 ties, instructions alone suffice; if lower, structural scaffolding is required for PASS.

3. **V-05 > V-04**: U and V target independent lifecycle phases (Phase 2 entry vs Phase 1 bilateral audit). V is predicted additive -- C-24 moves from PARTIAL to PASS, adding +0.3125. If tie, V is subsumed by U.
