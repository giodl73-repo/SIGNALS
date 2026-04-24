Written to `simulations/quest/golden/signal-variate-R2-2026-03-17.md`.

---

## Round 2 Summary

**Partial Amplifier Trajectory** (axes that produced spread in R1, now combined in R2):

| R1 Signal | New Criterion | R2 Target |
|-----------|--------------|-----------|
| V-01 C-10 PARTIAL: `->` reference + table output mismatch | C-13 | V-03 (table-consistent path), V-01/V-02/V-04/V-05 (`->` consistent path) |
| V-03 C-07 PARTIAL: generic `<domain>` placeholder | C-11 | V-01 (explicit lookup table), V-05 (table in STEP 3 rules) |
| V-04 C-12 implicit: alignment instruction without example | C-12 | V-01 (char-count example), V-05 (example + rule) |

**Five variations and their spread design**:

- **V-01** — C-11+C-12: explicit domain noun lookup table + alignment character-count example. V-04(R1) structure with two targeted patches. Predicted 100.
- **V-02** — C-04+C-05 behavioral: pre-emit compliance gate + bare mode code fence showing first 6 lines. Tests whether gate-first ordering improves mode isolation. Predicted 98 (C-12 PARTIAL — no char-count rule).
- **V-03** — C-13 table path: table in both reference section and output spec, eliminating the R1 V-01 format mismatch via table consistency rather than `->` consistency. C-12 is N/A. Predicted 98.
- **V-04** — Phrasing economy: strips compliance gate and alignment instruction entirely. Intentional C-12 FAIL to test whether explicit instruction is necessary or decorative. Predicted 92.
- **V-05** — Full integration: V-05(R1) baseline + scout footer corrected from "your topic" to "your research goal" (C-11 repair) + character-count alignment example + bare mode fence + domain noun table in STEP 3. Golden candidate. Predicted 100.
