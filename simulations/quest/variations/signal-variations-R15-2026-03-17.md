Written to `simulations/quest/golden/signal-variate-R15-2026-03-17.md`.

---

## Round 15 -- 5 variations

**Base**: All 5 carry U+V+W (R14 V-01 convergence). Predicted baseline 99.17 under v14 (33/36 asp). Each new axis adds +0.278 if independent.

### Variation plan

| V | Axes | C-42 | C-43 | C-44 | Key change |
|---|------|------|------|------|------------|
| **V-01** | X | PASS | FAIL | FAIL | FILTER Check 3: positional `(1)(2)(3)` -> verbatim-embed + `Header:/Separator:/Footer:` labels |
| **V-02** | Y | FAIL | PASS | FAIL | Named `BARE GROUP OFFSET TABLE` added; BARE Check 3 references table instead of inline prose |
| **V-03** | Z | FAIL | FAIL | PASS | Matrix cells: check numbers -> dual-index `Ch1 (C-25)` format |
| **V-04** | X+Y | PASS | PASS | FAIL | V-01 + V-02 combined |
| **V-05** | X+Z | PASS | FAIL | PASS | V-01 + V-03 combined; FILTER Format cell in matrix -> `Ch3 (C-42)` |

### Predicted scores under v14

| V | Asp (36) | Predicted |
|---|----------|-----------|
| V-01, V-02, V-03 | 34/36 | **99.44** |
| V-04, V-05 | 35/36 | **99.72** |

**Independence test**: if all three single-axis variations score exactly 99.44, X/Y/Z are confirmed independent. R16 V-01 = X+Y+Z is then predicted to saturate v14 at **100.00**.
 OFFSET TABLE). Dual-axis test for X+Y independence. |
| **V-05** | U+V+W | +X+Z | Combines V-01 (labeled FILTER Check 3) and V-03 (criterion IDs in matrix). FILTER Format cell in matrix references C-42 (since X present). Dual-axis test for X+Z independence. |

**Post-R14 signals targeted** (X, Y, Z -- formalized as C-42/C-43/C-44 in v14):
- **X**: FILTER Check 3 verbatim-embed + labeled sub-elements (FILTER analog of C-40)
- **Y**: Named `BARE GROUP OFFSET TABLE` (table analog of C-41 inline offsets)
- **Z**: Coverage matrix dual-index with criterion IDs (elevation of C-39)

**R16 plan** if independence confirmed: single convergence V-01 = X+Y+Z saturates v14 at
100.00 (36/36 asp -> 10.00 -> composite 100.00).
