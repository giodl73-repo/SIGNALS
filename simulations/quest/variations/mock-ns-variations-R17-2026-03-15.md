Written to `simulations/quest/golden/mock-ns-variate-R17-2026-03-15.md`.

---

## Summary

**Three single-axis variations + two combinations:**

| # | Axis | C-44 form | C-45 form | Predicted |
|---|------|-----------|-----------|-----------|
| V-01 | Output format | Standalone instruction above table | R16 V-05 abbreviated ("without reading cells") | 36/37 = 9.73 |
| V-02 | Phrasing register | R16 V-05 caption "(fill Match field only)" | Full cell naming: "without reading the Step and Row type cells" | 37/37 = 10.0 |
| V-03 | Lifecycle emphasis | R16 V-05 caption | Dedicated "Anti-bypass echo" row in chain table, full cell naming | 37/37 = 10.0 |
| V-04 | V-01 + V-02 | Standalone instruction | Full cell naming, sub-text form | 37/37 = 10.0 |
| V-05 | Full convergence | Standalone instruction | Dedicated row + full naming + P-0 back-reference | 37/37 = 10.0; seeds v17 |

**Key differentials being tested:**
- **C-44**: Does the annotation need to be a standalone imperative above the table, or does the caption parenthetical suffice? (V-01 vs R16 V-05)
- **C-45 phrasing**: Is "without reading cells" a PARTIAL because it omits "the Step and Row type" cell names? (V-02 isolates this)
- **C-45 structure**: Does the reminder need to be a dedicated chain-table row to avoid being skipped as trailing sub-text? (V-03 isolates this)

**V-05 seeds v17**: The `(P-0 anti-bypass declaration)` navigation pointer in the Anti-bypass echo row creates a bidirectional chain between the protocol definition and every use site -- the same structural pattern that C-28/C-29 applied to the S-3 ↔ A-1 cross-reference, now applied to P-0 ↔ use-site echoes.
