Written to `simulations/quest/golden/mock-ns-variate-R19-2026-03-17.md`.

---

## mock-ns -- Round 19 Variations (rubric v18)

**Axes selected** (all CONSTRAINT-form axes exhausted in R17/R18; R19 pivots to three new orthogonal axes):

| Axis | Label | Rubric target |
|------|-------|---------------|
| A | Phrasing register | C-31 -- deontic "must" in S-0 closing sentence |
| B | Output format | C-22 -- HS-critical-tier-1 row collapsed into catch-all |
| C | Lifecycle emphasis | structural only -- phase-grouped lifecycle with entry/exit state annotations |

All five variations use the **golden parenthetical CONSTRAINT** form -- C-44/C-45/C-46/C-47 pass in every variation.

**Variation summary:**

| Variation | Axis | Key change | Fails | Expected score |
|-----------|------|------------|-------|----------------|
| V-01 | A single | Closing sentence: "This step **must** emit..." | C-31 | 156/158 |
| V-02 | B single | S-3.3 FLAG table: 4 rows, HS-critical-tier-1 absorbed into catch-all | C-22 | 156/158 |
| V-03 | C single | LIFECYCLE: phase-grouped with entry/exit state annotations per step | -- | 158/158 |
| V-04 | A+B | Deontic closing + 4-row collapsed FLAG | C-31, C-22 | 154/158 |
| V-05 | A+B+C (golden) | "Only this step emits..." + 5-row table + phase-grouped lifecycle | -- | 158/158 |

**Key findings from R19 design:**

- **V-01 vs V-04**: C-31 is an isolated -2 penalty. The first declarative sentence ("Before any other step begins, this step emits...") satisfies C-25/C-28 even when the closing sentence is deontic -- C-31 fires independently per the v10 discriminator.
- **V-02**: C-22 fires for any table that folds HS-critical-tier-1 into the non-critical catch-all. C-11 survives because the 4-row table still functionally covers all 5 cases.
- **V-03 = 158/158**: Phase groupings and state annotations are purely additive structural sugar. No existing sentence is displaced, no step content is removed. Lifecycle expansion does not affect any scored criterion.
- **V-05 confirms axis independence**: Running all three axes at golden simultaneously still produces 158/158, confirming the axes do not interact or create cascade effects.

**Open questions for R20** (filed in the document): passive closing sentence (C-33 chain), wh-pseudo-cleft (C-39 chain), prose FLAG computation without table (C-11/C-22 boundary), three-axis failure combination (deontic + collapsed FLAG + collapsed S-3), and lifecycle annotation replacement form (C-32/C-43).
