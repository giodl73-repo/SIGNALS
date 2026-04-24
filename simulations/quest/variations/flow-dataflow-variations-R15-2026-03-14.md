**R15 variations written** to `simulations/quest/rubrics/flow-dataflow-rubric-v15-R15-2026-03-15.md`.

---

## Summary

| Variation | Axis | Domain | Role Sequence | Register | C-46 | C-47 |
|-----------|------|--------|---------------|----------|------|------|
| V-01 | Role sequence | Freight billing / cost allocation | Fin → Ops → Com | Tabular | SC-13 in closed-chain paragraph | n/a |
| V-02 | Output format | Energy trade settlement | Fin → Com → Ops | Prose | SC-13 in closed-chain paragraph | SC-14 in closed-chain paragraph |
| V-03 | Lifecycle emphasis | SaaS revenue recognition (4 stages/role) | Com → Fin → Ops | Tabular | SC-13 in closed-chain paragraph | n/a |
| V-04 | Role seq + inertia | Pharma procurement-to-payment | Ops → Com → Fin | Tabular | SC-13 in closed-chain paragraph | n/a |
| V-05 | Format + phrasing | Federal contracting payment | Ops → Fin → Com | Prose (imperative) | SC-13 in closed-chain paragraph | SC-14 in closed-chain paragraph |

**Key C-46/C-47 design decision across all variations**: The closed-chain paragraph in REGISTER DECLARATION now explicitly names SC-13 BASELINE CLOSURE as a governing authority in bold, making baseline-closure failures navigable from the register index without scanning STRUCTURAL CONSTRAINTS. Prose variants additionally name SC-14. V-03 is the stress test — 9 boundary blocks means SC-13's inline callbacks must fire across the longest elapsed chain in R15, verifying that the closed-chain registration holds under boundary density.
