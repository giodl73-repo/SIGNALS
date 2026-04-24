Done. File written to `simulations/quest/rubrics/flow-trigger-rubric-v9-R15-2026-03-15.md` (1821 lines, 5 complete variations).

---

**R15 summary:**

| Variation | Axis | New criterion targeted |
|-----------|------|------------------------|
| V-01 | Gate formalization | C-33 — GATE-STATE blocks emitted at every structural transition; Role 5 checks gate artifacts alongside chain links |
| V-02 | Full-column key references | C-34 — all five certificate columns carry `<- key ref` annotations; absent CHAIN-LINK produces named COLUMN-GAP in specific column |
| V-03 | PCR as fourth independent terminal artifact | C-35 — PCR Analyst declared distinct from Inertia Analyst; four-owner terminal architecture |
| V-04 | V-01 + V-02 | C-33 + C-34 combined; maximum gap-detectability without new terminal owners |
| V-05 | V-01 + V-02 + V-03 + triple-entity Role 5 | C-33 + C-34 + C-35 + triple-entity independence declaration at role definition AND certificate header |

**New signal candidates for v12:**
- **C-33**: Gate-state artifacts — named GATE-STATE blocks emitted at bidirectional transitions (Gate 4→4B, Gate 4B→5 at minimum); Role 5 gate integrity section reports absent gate artifacts separately from chain integrity
- **C-34**: Full-column key references — every certificate column names its upstream CHAIN-LINK key; absent link produces COLUMN-GAP in that column (schema-detectable vs. chain-integrity-detectable)
- **C-35**: PCR as independent terminal artifact — PCR Analyst declared distinct from Inertia Analyst at role definition; four-owner architecture with independence declarations at each terminal
