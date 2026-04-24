Written to `simulations/quest/golden/corps-chart-variate-R12-2026-03-17.md`.

---

**Round 12 -- corps-chart -- 5 variations**

| ID | Axis | Target | Baseline |
|----|------|--------|----------|
| V-01 | HALT-AND-CONFIRM for BEFORE-PRODUCE directives | C-31 | R11 V-01 |
| V-02 | Per-row vocabulary-type CHECK in governed tables | C-32 | R11 V-04 |
| V-03 | HALT-AND-CONFIRM, STOP variant + explicit count-record | C-31 | R11 V-03 |
| V-04 | C-31 + C-32 combined | C-31, C-32 | R11 V-04 |
| V-05 | Full integration | C-31, C-32, all prior | R11 V-05 |

**Key mechanics introduced:**

- **C-31** (V-01, V-03, V-04, V-05): Every BEFORE-PRODUCE directive upgraded from advisory prose to `HALT.` + enumerated per-field checklist + `Proceed only if all confirmed.` Closes the acknowledgement-without-verification failure mode. V-03 tests `STOP` + explicit count-record + prohibitive gate as a stricter phrasing variant.

- **C-32** (V-02, V-04, V-05): Per-row verification added to all three vocabulary-governed tables -- mechanism table (MECHANISM-TYPE VOCABULARY), trigger table (TRIGGER-TYPE VOCABULARY), Anti-Pattern Watch (CAT-N-CITATION-SCHEMA). Each table gets: "For each row: verify the governed field against the vocabulary before writing the next row -- do not complete the table and verify after." Closes the intra-table type-drift failure mode that parallels C-28's per-cell role-lock.
