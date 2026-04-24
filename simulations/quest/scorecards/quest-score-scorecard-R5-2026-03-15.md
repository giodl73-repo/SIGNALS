Scorecard written to `simulations/quest/scorecards/quest-score-scorecard-R5-2026-03-16.md`.

---

## Summary

**Rubric derivation:** E=5, R=3, A=10. Formula: `(E/5×60) + (R/3×30) + (A/10×10)`.

**Scores:**

| Rank | Variation | Composite | Golden |
|------|-----------|-----------|--------|
| 1 | V-03 (imperative + H+G) | 100 | YES |
| 1 | V-04 (H+G+S+T) | 100 | YES |
| 1 | V-05 (H+G+S+T+AF-8/9) | 100 | YES |
| 4 | V-02 (inline check + H-only) | 98 | YES |
| 5 | V-01 (condensed baseline) | 96 | YES |

**C-15/C-16/C-17/C-18 verdicts:**
- V-01: all four FAIL (no envelope at all)
- V-02: C-15 FAIL, C-16 PASS, C-17 PASS, C-18 FAIL — the clean decoupling case
- V-03/V-04/V-05: all four PASS

**Excellence signals:**
- V-02 reveals C-17 is structurally independent of C-15 — self-referential priming can PASS even when the mechanism it primes against fails
- V-03 is the minimum-surface 100: imperative register + H+G, no *Why*, no synthesis gate, same score
- V-05 confirms third-order priming ceiling: AF-8/AF-9 add architectural correctness but zero rubric points over V-04

```json
{"top_score": 100, "all_essential_pass": true, "new_patterns": ["third-order priming (AF-8/AF-9) produces no score differential over second-order once H+G floor is set — ceiling confirmed at second-order self-reference", "imperative register achieves full-envelope compliance equivalent to specification register — register choice does not affect C-15 through C-18 verdicts when H+G structure is present", "C-17 and C-18 are independently satisfiable — self-referential priming passes C-17 even when the scan it primes against fails C-15 (V-02 decoupling signal)"]}
```
