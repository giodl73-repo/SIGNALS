Written to `simulations/quest/golden/org-rob-variate-R3-2026-03-16.md`.

---

## org-rob R3 -- Five Variations

**Rubric change from R2:** C-14 (lens-anchored findings), C-15 (column-invariant verdict format), C-16 (synthesis residual open items). Total max 100 → 106.

**R3 design intent:** Every variation structurally enforces at least one of C-14/C-15/C-16 while preserving R2's C-11/C-12/C-13 patterns where compatible.

---

### V-01 — Output Format: Lens-Citation-First Finding Schema
**Axis:** Output format  
**Targets:** C-14  
**Hypothesis:** When `Lens:` is the FIRST column in every finding table (before the finding text), role-loading is independently verifiable at the finding level. The Lens field must be cited from a published inventory of the loaded role file — a blank Lens column is a malformed row. A `Lens Coverage Check` table in synthesis confirms ≥50% coverage.

Finding schema: `ID | Lens | Finding | Severity | Owner | Resolution Path`

---

### V-02 — Output Format: Column-Invariant Verdict Registry
**Axis:** Output format  
**Targets:** C-15 + C-16  
**Hypothesis:** Two persistent tables maintained throughout the run — a Verdict Registry (one table row per stage verdict, never prose) and a Finding Registry (with `Acknowledged By` / `Acknowledged As` columns) — produce C-15 and C-16 as mechanical byproducts. The Residual Open Items section in synthesis is a filter of the Finding Registry where `Acknowledged As` is empty.

---

### V-03 — Lifecycle Emphasis: Residual-Accumulator Model
**Axis:** Lifecycle emphasis  
**Targets:** C-16  
**Hypothesis:** When synthesis is not written at the end but accumulated throughout — each stage appends `Adds to Ledger:` rows — then the Residual Open Items section always exists because the ledger is always present. An empty ledger is a valid and positive state, explicitly written.

---

### V-04 — Combination: Lens-Citations + Phase Gate Contracts
**Axes:** Output format (V-01 lens schema) + Lifecycle emphasis (R2 V-01 phase gates)  
**Targets:** C-14 + C-11 + C-12 + C-13  
**Hypothesis:** Phase gates give C-11/C-12/C-13; the Lens-column finding table gives C-14. The `Lens` column fits inside the gate's Review section without conflict. Exit blocks enforce dual-direction tracing and named blocker triads as before.

---

### V-05 — Combination: All Three R3 Criteria as Unified Schema
**Axes:** Output format × 3 (Lens findings + Verdict Registry + Residual synthesis)  
**Targets:** C-14 + C-15 + C-16 + C-09 through C-13 preserved  
**Hypothesis:** All three new criteria can be enforced simultaneously by a single schema: three persistent registries (Finding Registry with Lens column, Verdict Registry as table rows, Go/No-Go Registry). The Residual Open Items section is a filtered view of the Finding Registry. Phase gate Entry/Exit blocks preserve C-11/C-12/C-13. This is the maximalist variation targeting a perfect 106.
