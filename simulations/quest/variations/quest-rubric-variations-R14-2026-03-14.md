Written to `simulations/quest/rubrics/quest-rubric-rubric-v14-variations-R14-2026-03-15.md`.

---

## R14 Variations — Round 14

**Axis map:**

| Variation | Single/Combo | Axis |
|-----------|-------------|------|
| V-01 | baseline | R14 full integration — R13/V-01 stack + C-39 checkpoint row added; both declaration paths (preamble + Contract item 7) active; C-39 PASS by construction |
| V-02 | single | C-39 preamble-only — Contract item 7 removed; preamble obligation retained; isolation of path (b) |
| V-03 | single | C-39 Contract-only — preamble "Maintain imperative register" bullet removed; Contract item 7 retained; isolation of path (a) |
| V-04 | single | Joint-failure-chain Notes block — R13/V-01 baseline + 8-item Contract + mandatory "Known Failure Chains" sub-section in Notes (>= 2 chains with structural-absence + jointly-failing-criteria + root-cause); v15 candidate probe |
| V-05 | combo | V-02 + V-04 — preamble-only C-39 (no Contract item 7) + Known Failure Chains block (renumbered to item 7); 7-item Contract |

**What R14 will answer:**

- V-02 vs V-03: which declaration path is independently sufficient for C-39 PASS? If V-02 passes and V-03 fails, preamble is the load-bearing mechanism. If both pass, both paths are independently sufficient.
- V-03: whether Contract item 7 alone maintains C-37 PASS when preamble clause is absent — this would falsify R13/V-02's finding that the preamble is the load-bearing mechanism.
- V-04/V-05: whether an explicit Contract-item-mandated Notes block produces structurally annotated joint-failure chains, and whether the Phase 1A/1B split surfaces as a named joint-enabler in that block (the `phase-1a-1b-split-is-joint-structural-enabler` v15 candidate).
