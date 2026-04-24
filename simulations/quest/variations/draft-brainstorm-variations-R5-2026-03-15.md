Written to `simulations/quest/golden/draft-brainstorm-variate-R5-2026-03-16.md`.

---

## R5 Summary

**Target**: 130 (C-21 + C-22 close the lineage from C-10 to the tips)

**Root cause going in:**
- R4-V-03's order inversion (mark at Step 3, justify at Step 3b) made C-21 impossible by construction
- R4-V-04/V-05's "specific peer you named" phrasing left the free-swap loophole open for C-22

**Five variations:**

| Variation | Axis | C-21 | C-22 | Target |
|-----------|------|------|------|--------|
| **V-01** | Phrasing register: "Phase 3 gated -- no `**` marks until batch in output" | PASS | FAIL | 125 |
| **V-02** | Lifecycle emphasis: "replacement source is fixed: peer from this specific check" | FAIL | PASS | 125 |
| **V-03** | Output format: Pre-Selection Batch Registry gates Top-5? column (order fixed) | PASS | PASS | 130 |
| **V-04** | Combo: batch gate + source trace + explicit C-18 feedback links | PASS | PASS | 130 |
| **V-05** | Full stack: R4-V-05 + explicit batch-advance gate + "attempted to name" | PASS | PASS | 130 |

**Key design choices:**

- **V-03** fixes the order inversion: Registry lives at Step 2b (pre-selection), not post-selection. The `Top-5?` column is physically gated by section completion.
- **V-04** also fixes R4-V-04's marginal C-18: all four Phase 2 checks now have explicit downstream labels ("determines candidates for Check B", "determines marks in Phase 3", etc.).
- **V-02** isolates C-22 cleanly: interrogative preserved, so a fail here confirms C-22 requires the full consequence chain; a pass confirms source-specificity language works independently.
- The `C-22` signal phrase shifts from "the specific peer you named" (R4) to "the peer you attempted to name in this comparison -- not a different idea after reconsidering" (R5), closing the post-hoc substitution loophole.
