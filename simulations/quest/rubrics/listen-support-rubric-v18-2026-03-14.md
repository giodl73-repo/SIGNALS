Written to `simulations/quest/rubrics/listen-support-rubric-v18-2026-03-15.md`.

**What changed v17 → v18:**

| ID | Name | Tightens | Who satisfies |
|----|------|----------|---------------|
| C-53 | Role Allocation Pre-Commitment Table | C-20, C-24 | V-01, V-04, V-05 |
| C-54 | Phase Column in Coverage Table | C-17 | V-02, V-04, V-05 |

**Aspirational tier:** 220 pts → 230 pts. **Total ceiling:** 310 → 320.

**Signal logic:**
- **C-53** applies the three-gate phase-distribution architecture (C-45/C-48) to the role dimension — Step 3A pre-declares per-role counts, Constraint 1B fires pre-body, Part B item 4 re-checks post-generation. Closes role-saturation (all tickets to one role) which C-20 per-row vocabulary and C-24 collective-distribution both miss.
- **C-54** adds Phase as column 2 in the C-17 coverage table (4-column: Ticket ID / Phase / STATUS QUO element / Gap traced to), plus a post-table confirmation counting per-phase rows. Converts phase concentration from a prose-parseable implication into a cell-value scan on a single column.
