Written to `simulations/quest/golden/file-issue-variate-R5-2026-03-17.md`.

---

## Round 5 — file-issue Variations Summary

**Context**: R4 ended with two 98.0 golden artifacts. V-01 had C-14+C-17, V-02 had C-15+C-16. No R4 variation held all four simultaneously.

**Round 5 variation axes:**

| Variation | Axis | C-14 | C-15 | C-16 | C-17 | Predicted |
|-----------|------|------|------|------|------|-----------|
| V-01 | Unified pipeline dispatch (single-axis, C-17) | PASS | FAIL | FAIL | PASS | 98.0 |
| V-02 | Completion condition in macro-phase (single-axis, C-16) | FAIL | PASS | PASS | FAIL | 98.0 |
| V-03 | C-14 + C-15 + C-16, severity gating without unified dispatch | PASS | PASS | PASS | FAIL | 99.0 |
| V-04 | Full combination: C-14 + C-15 + C-16 + C-17 | PASS | PASS | PASS | PASS | **100.0** |
| V-05 | Full combination, compressed | PASS | PASS | PASS | PASS | **100.0** |

**The key test for Round 5**: Does V-03 also pass C-17? If it does, then describing severity as "determines the collection form (A2) and the output template (A3)" is enough for C-17, and V-04/V-05's explicit "simultaneously dispatches both (a)...(b)" phrasing is redundant. If V-03 fails C-17, that language is the load-bearing distinction and V-04/V-05 are the canonical implementations.

**V-04 is the primary target** — the first skill to explicitly state that severity confirmation is "the single event that simultaneously dispatches both (a) the collection schema and (b) the output template, neither pipeline determined before, both determined at the moment of confirmation."
