File written to `simulations/quest/golden/mock-review-variate-R19-2026-03-16.md`.

---

## mock-review Variate — Round 19

**5 complete variants targeting the v19 C-42/C-43 named-level definitions.**

### Design matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| **C-42** | PARTIAL | **FAIL** | **PASS** | PASS | PASS |
| **C-43** | PASS | PASS | PASS | **FAIL** | PASS |
| C-35 (Strategy-first) | ✓ | — | ✓ | — | — |
| C-36 (Arch-first) | — | ✓ | — | ✓ | ✓ |

### Variation axes

**V-01** — C-42 PARTIAL boundary: TRIAD header is the sole unlabeled element (per the v19 definition). All guard headers, step headings, gate headers, slot headers, and canary carry labels. Evaluation SQs in `| Row # |` table (C-43 PASS). Strategy-first.

**V-02** — C-42 FAIL floor: only core decision-block template slot headers labeled (`reason-code`, `Structural position`, `Contrast`, `Artifact state`). TRIAD header, guard headers, step headings, canary all unlabeled. C-43 PASS independent of labeling level. Arch-first.

**V-03** — C-42 PASS: adds `[C-11][C-27]` to the TRIAD header, the single-element gap between PARTIAL and PASS. All other elements already labeled from V-01. C-43 PASS. Strategy-first.

**V-04** — Independence test: C-42 PASS (TRIAD header labeled, all elements labeled) + C-43 FAIL (inline `SQ-N (C-15):` prefix, row number in cell content). Confirms the two criteria are independently satisfiable. Arch-first.

**V-05** — Ceiling with Arch-first: C-42 PASS with belt-and-suspenders (per-row `[C-15]` inside table cells on top of column header label) + C-43 PASS + `| Row # | Sub-question [C-15] |` column header. Establishes ceiling is reachable under C-36 as well as C-35 (V-03).

### Key findings encoded

- **C-42 boundary is exactly the TRIAD header label** — V-01 vs V-03 differ only there
- **C-42 and C-43 are independent** — V-02 proves FAIL/PASS; V-04 proves PASS/FAIL
- **Both role orderings reach the ceiling** — V-03 (C-35) and V-05 (C-36) both achieve C-42+C-43 PASS
