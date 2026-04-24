Here are the 5 variations for `flow-throttle` Round 7 (v7 rubric), written to `simulations/quest/golden/flow-throttle-variate-R7-v7-2026-03-16.md`.

---

## Summary

**Variation axes used:**

| Variation | Axis | New v7 Criteria Targeted | Predicted Composite |
|-----------|------|--------------------------|---------------------|
| **V-01** | C-20 only — prose-restriction declaration as a labeled block before the first table | C-20 PASS, C-21 FAIL, C-22 FAIL | ~152/160 |
| **V-02** | C-21 only — cross-artifact referential integrity header line on every derived table | C-20 FAIL, C-21 PASS, C-22 FAIL | ~152/160 |
| **V-03** | C-22 only — typed-row risk taxonomy (TABLE E inserted; Type = Burst/Cascade/RetryAfter; per-type minimum-row gate) | C-20 FAIL, C-21 PARTIAL, C-22 PASS | ~153/160 |
| **V-04** | C-20 + C-21 combined — declaration + source headers on all artifacts | C-20 PASS, C-21 PASS, C-22 FAIL | ~156/160 |
| **V-05** | C-20 + C-21 + C-22 combined — all three; TABLE D2/E1/E2/E3 fully table-ized; TABLE F cites TABLE E3 not TABLE A | C-20 PASS, C-21 PASS, C-22 PASS | 160/160 |

**Key structural decisions:**

- **V-01** adds a `PROSE-RESTRICTION DECLARATION (C-20)` block at the top with a closed 4-item list; prose-in-sections (2D, 2E, 2F, 2G) are explicitly named as permitted contexts. Tests whether the declaration being present (not zero-prose) satisfies C-20.

- **V-02** adds `*[TABLE X — Source: TABLE A. One row per T-NN from TABLE A. No tier may be omitted...]*` as a header italic line on every derived table. Tests whether moving the coverage obligation from the phase entry condition into the table header itself satisfies C-21.

- **V-03** inserts `Step 2G2 — RISK INVENTORY (TABLE E)` with a `TYPE SCAN GATE` before 2H. The gate requires explicit scan confirmation of Burst/Cascade/RetryAfter before proceeding. Tests whether model compliance holds when the gap is structural (missing type category) rather than count-based.

- **V-05** promotes 2D, 2E, and 2F to tables (`TABLE D2`, `TABLE E1`, `TABLE E2`) to minimize non-declared prose, and routes TABLE F's source reference to `TABLE E3` rather than `TABLE A` — the critical C-21/C-22 interaction test.
