All 5 variations written to `simulations/quest/golden/flow-lifecycle-variate-R10-2026-03-15-v10c31c32c33.md` (1955 lines).

---

**Variation summary:**

| V | Axis | New AC(s) | Key Mechanism |
|---|------|-----------|---------------|
| V-01 | C-33 only | AC-17 | STEP 0 LIFECYCLE ENTRY INVENTORY before all sections; GATE 0 with LT-ID table (trigger source + initial state per entry); Phase Index and Role Registry carry LT-ID trace fields |
| V-02 | C-32 only | AC-17 | Exception Catalog reordered before Terminal Declaration; explicit UPSTREAM GATE (State Tables + Decision Tables → Exception Catalog) + DOWNSTREAM GATE (Exception Catalog → Terminal Declaration); both name source and target sections; bracketing language |
| V-03 | C-31 only | AC-17 | Decision Table Condition column header carries BOTH taxonomy list (`dollar amount, day count, retry count`) AND quoted concrete example (`"Invoice total > $5,000"`) simultaneously |
| V-04 | C-33 + C-32 | AC-17, AC-18 | Step 0 inventory + bidirectional gates + reordering; structural grounding at entry + bounded exception node |
| V-05 | C-33 + C-32 + C-31 | AC-17, AC-18, AC-19 | Full floor + all three; AC-17/18/19 must show distinct non-overlapping evidence in Coverage Scan |

**Three design decisions worth flagging:**

1. **V-02 reordering** — the existing floor places Terminal Declaration before Exception Catalog, which structurally conflicts with C-32 (downstream gate requires terminals after exceptions). V-02 and V-04/V-05 correct this ordering.

2. **V-04 Decision Table** — deliberately holds C-29 (taxonomy-only) not C-31, to keep the combination clean and verify the axes are orthogonal.

3. **Defect Taxonomy** — each variation extends the Scan Summary Defect Type table with entries specific to its new criteria, making the production gate's causal mechanism claim verifiable against a named taxonomy entry (satisfying C-25/C-27 continuity).
