Written to `simulations/quest/golden/topic-roadmap-variate-R12-2026-03-17.md`.

---

**Summary of R12 variations:**

| Variation | Axis | C-27 | C-28 | Stack |
|-----------|------|------|------|-------|
| V-01 | Lexical identity (C-27 only) | FULL | PARTIAL (exit criterion only, no preamble) | R10 V-04 base |
| V-02 | Dual-site blocking (C-28 only) | PARTIAL (column = "Consequence if HOLDS", exit criterion = "Consequence if unchanged") | FULL | R10 V-04 base |
| V-03 | C-27 + C-28 combined, minimal base | FULL | FULL | Essential only, no C-21--C-25 |
| V-04 | Full stack + C-27 + C-28 | FULL | FULL | C-21 through C-28 |
| V-05 | Full stack + C-27 + C-28 + schema pre-commitment | FULL | FULL | C-21 through C-28 + Output Schema CONTRACT annotation |

**Key structural choices:**

- **V-01** isolates C-27 by renaming the column to "Consequence if unchanged" and matching the exit criterion, with no preamble. C-28 partial (single enforcement site).
- **V-02** isolates C-28 by adding the CONSEQUENCE GATE preamble (Site 1) and updating the exit criterion (Site 2), both saying "Consequence if unchanged" — but deliberately leaving the column header as "Consequence if HOLDS". C-27 partial (column ≠ exit criterion).
- **V-03** is the minimal combination confirming C-27 + C-28 are independent of the C-21–C-25 machinery.
- **V-04** is the production-ready integration on the proven R10 V-04 foundation.
- **V-05** adds a `CONTRACT` annotation in the Output Schema block that pre-declares the column name before any file is read, creating a triple-site chain (schema → table column → exit criterion) verifiable at the schema boundary alone.
