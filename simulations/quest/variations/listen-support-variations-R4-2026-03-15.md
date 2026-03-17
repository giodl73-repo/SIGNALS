Written to `simulations/quest/golden/listen-support-variate-R4-2026-03-15.md`.

---

## listen-support R4 — V-01 through V-05

**Target:** rubric v4, C-16 + C-17 (the two new aspirational criteria).

**The R3 gap:** V-01 had per-ticket commitment tables from phase-only pools (C-16 PASS, C-17 FAIL). V-03 had a role-phase matrix but no commitment table (C-17 PASS, C-16 FAIL). No R3 variation satisfied both simultaneously.

**R4 strategy:** all five variations combine both mechanisms.

---

### Single-Axis Variations

| Variation | Axis | Mechanism | C-16 path | C-17 path |
|-----------|------|-----------|-----------|-----------|
| **V-01** | Lifecycle emphasis | Role-phase vocabulary matrix (STEP 2) + commitment table with cell IDs (STEP 2B) | Commitment table with cell-ID column | STEP 2 matrix, 2D with distinct registers |
| **V-02** | Output format | VOCABULARY MANIFEST as named top-level section + CONSTRAINT/VERIFICATION MANIFEST trio | STEP 3 commitment table references VM row IDs | VOCABULARY MANIFEST is a named required section — cannot be absent |
| **V-03** | Role sequence | Per-role vocabulary declaration blocks with inline commitment sub-tables | Per-role commitment sub-table immediately before each role's bodies | Per-role vocabulary declaration has distinct phase rows per role |

### Combined Variations

| Variation | Stacks | New property |
|-----------|--------|-------------|
| **V-04** | V-01 + V-02 | VOCABULARY MANIFEST is both named manifest (V-02 form) and source for cell-referenced commitments (V-01 mechanism) |
| **V-05** | All R3 + all R4 | All 5 mechanisms present; composite 100 candidate under v4; scorer checks C-16/C-17 by named-section lookup, O(1) |

**V-05 is the composite-100 candidate:** VOCABULARY MANIFEST (C-17), CONSTRAINT + VERIFICATION MANIFEST (C-15), per-ticket commitment table with VM row references (C-16), character-embodiment PERFORMANCE MODE (C-03), dual-mechanism body instruction (C-14 + C-16 + C-17).
