Written to `simulations/quest/golden/corps-pr-variate-R14-2026-03-17.md`.

---

## Summary

| Variation | Axis | New Criteria | Key Change from R13 V-05 |
|-----------|------|-------------|--------------------------|
| V-01 | Output format (block) | C-39 | STEP 2 folds UNSATISFIED path into same `## C2 RESULT` block via conditional derivation line; removes separate code fence |
| V-02 | Output format (column) | C-40 | F-01 format rules remove "or" inline-cell path; column headers mandatory; marks inline path as C-38-pass / C-40-fail |
| V-03 | Lifecycle emphasis | C-41 | Adds `Structural enforcement levels` table to pipeline declaration; assigns C-36/C-37+C-39/C-38+C-40 to exit-condition/block/table-column levels |
| V-04 | Block + declaration | C-39 + C-41 | V-01 + V-03 combined; tests block self-containment + declared partition without C-40 |
| V-05 | Full integration | C-39 + C-40 + C-41 | All three; self-contained block, column-only schema, declared three-level partition |

**Tightest integration point (as flagged in rubric)**: C-40 + C-41 — C-40 mandates column headers, and C-41 requires the pipeline to name the table-column level that C-40 occupies. V-04 tests whether block + declaration alone passes C-41 (the table-column level is declared in the partition even though C-40 output enforcement is absent). V-05 closes all three simultaneously.
