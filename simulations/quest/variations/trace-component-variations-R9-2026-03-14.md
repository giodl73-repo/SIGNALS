Written to `simulations/quest/rubrics/trace-component-rubric-v9-variations-R9-2026-03-14.md`.

---

# trace-component — Round 9 Variations (V-01 through V-05)

## Variation axes

| V# | Axis | Hypothesis summary |
|----|------|-------------------|
| V-01 | Output format — schema evolution | R8 V-01 already satisfies C-31 and C-32 implicitly. Add `N=direct, M=inherited` + `Type` column to TABLE 3. Zero proliferation. |
| V-02 | Lifecycle emphasis — per-phase schema manifests | Each phase header declares which criteria → schema fields it enforces, making C-31/C-32 mapping explicit at every gate. |
| V-03 | Inertia framing — targeted extraction | Keep `↔ inert pass-through` from R8 V-05, drop TABLE 3b entirely. Dual count absorbed as C-30 requires — no sub-table. Tests whether the framing was the value and the table was the cost. |
| V-04 | Output format + role sequence | Full V-01 schema trace (Role 1) + trimmed auditor that runs only three compliance tables for C-30/C-31/C-32 (Role 2). Avoids R8 V-04's coherence penalty from full-size auditor. |
| V-05 | Lifecycle emphasis + phrasing register | Rescues R8 V-03's failed formal/technical register by pairing formal prose with schema anchor tables per phase. Tests whether the register's failure was structural (fixable) or intrinsic. |

## Key design decisions

**C-30 implementation**: All five variations absorb the direct/inherited dual count into the existing `TABLE 3` mutation pre-declaration line (`Mutations: N=___ direct, M=___ inherited`) and add a `Type` column (`direct / inherited`) to the mutation table body. No sub-table. This is the exact constraint C-30 specifies ("absorbed into existing structure without structural proliferation") and the targeted fix for V-05 R8's 2-point TABLE 3b penalty.

**C-31 compliance**: V-01 already maps all 10 of C-20–C-29 to schema fields via R8's self-reinforcing pipeline. V-04 makes this mapping explicit in AUDIT TABLE B (a 10-row criteria → field compliance table). V-02 surfaces it per-phase via schema field manifests.

**C-32 compliance**: All five variations back all five essentials with blank-blocked TABLE 1–TABLE 6 columns. V-05 uses "anchor tables" per section to satisfy this even in the formal-register format.

## Predicted ranking

**V-01 > V-03 ≥ V-02 > V-04 > V-05** (134–136 / 132–135 / 130–133 / 130–134 / 122–128 out of 138)

**Key structural test**: If V-03 scores within 1–2 pts of V-01, targeted inertia extraction (framing without the sub-table) is the right path to explore in R10. If V-03 scores below V-02, the inertia framing itself — not just TABLE 3b — carries coherence cost.
