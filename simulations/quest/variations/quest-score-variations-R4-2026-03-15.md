Written to `simulations/quest/golden/quest-score-variate-R4-2026-03-16.md`.

---

## Summary

**5 variations targeting C-15 (post-scoring scan) and C-16 (pre-execution priming):**

| Variation | Axis | C-15 | C-16 | Skeleton | Key mechanism |
|-----------|------|------|------|----------|---------------|
| V-01 | I — Condensed 3-phase | FAIL | FAIL | Instructions | Baseline — removes phase manifest, carries D+E from R3 |
| V-02 | G — Named scan token | PASS | FAIL | Instructions | `[SCAN COMPLETE]` + field-presence table after last output block |
| V-03 | H — Pre-phase AF table | FAIL | PASS | Instructions | AF-code table before Phase 1; tabular format vs R3's narrative anti-examples |
| V-04 | G+E — Scan + skeleton | PASS | FAIL | Pre-printed | Pre-printed skeleton closes omission-by-decision; scan closes omission-by-neglect |
| V-05 | H+G — Priming + scan | PASS | PASS | Instructions | Full-envelope: AF table (incl. AF-6/AF-7 self-ref) + named scan; isolated from skeleton |

**Key design decisions:**

- V-01 is the clean baseline — not "weakened R3" but specifically condensed to isolate C-15/C-16 FAIL verdicts
- V-02 vs V-03 are single-axis isolations — each adds exactly one new axis while keeping the base identical  
- V-04 differentiates from V-02 by adding the pre-printed skeleton (E axis from R3), testing whether skeleton + scan compound
- V-05 adds AF-6 and AF-7 to its own anti-pattern table — a self-referential priming move that creates a measurable signal: does priming against scan-related failures improve scan execution?
