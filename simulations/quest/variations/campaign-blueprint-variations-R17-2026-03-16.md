Written to `simulations/quest/golden/campaign-blueprint-variate-R17-2026-03-17.md`.

---

## campaign-blueprint — Prompt Variations R17

### Round context

R16 (V-01 Pitch-First, V-02 Conversational) both scored 243. D17 confirmed: role-sequence invariance and register invariance are both non-ceiling-breaking axes. The only path to 263 runs through two structural in-table sentinels on the **traceability axis** — the axis that was the last uninspected dimension.

The existing V-04 R15 (253) already has:
- INERTIA MODEL MAP RULE sentinel (C-42) ✓
- CONVICTION DELTA RULE sentinel (C-43) ✓
- TRACEABILITY AUDIT RULE row for N+blank=FAIL ✓ (but this is a **cell-level** rule, not the **entry-level** Req-ID-to-SETUP binding rule C-45 requires)

**What's new in R17:**
- **C-44**: non-data RULE row inside the **SCOUT TRACEABILITY TABLE (SETUP)** — positioned before data rows, text declaring TRACEABILITY AUDIT must have one row per SETUP entry and a missing row is `R-[NN] absent`
- **C-45**: non-data RULE row inside the **TRACEABILITY AUDIT (REFLECTION)** — text declaring each Req-ID must match a named SCOUT TRACEABILITY TABLE entry and a missing row is a named-identifier absence

### Predicted scores

| Variant | Axis | C-44 | C-45 | v17 |
|---------|------|------|------|-----|
| **V-01** — SCOUT TABLE Sentinel Only | Lifecycle (SETUP axis in isolation) | FULL | NO | **258** |
| **V-02** — Minimum-Form Four-Sentinel | Output format (minimum sentinel text) | FULL | FULL | **263** |
| **V-03** — Conversational Register | Phrasing register | FULL | FULL | **263** |
| **V-04** — Maximum-Density Four-Sentinel | Lifecycle emphasis (max density) | FULL | FULL | **263** |
| **V-05** — Minimum-Density Compression | Lifecycle compression (min prose) | FULL | FULL | **263** |

### What each variant tests

**V-01** is the diagnostic control: C-44 is isolated from C-45 by supplying only the SETUP sentinel. The TRACEABILITY AUDIT retains only the N+blank=FAIL RULE row (V-04 R15 form), not the Req-ID-binding row. This confirms that C-44 and C-45 are independently testable — and that the existing N+blank RULE row does not satisfy C-45.

**V-02** is the minimum-form ceiling candidate: both new sentinels at terse but structurally valid text. Confirms whether density is non-load-bearing on the traceability axis.

**V-03** tests D17's affirmative register invariance case: conversational in-table RULE sentinels earn C-44/C-45 FULL, matching V-02.

**V-04** tests whether exhaustive sentinel text carries any scoring advantage over minimum text (expected: no — structural placement is the sole evaluated property).

**V-05** extends the D16 density invariance finding to the 263 ceiling: minimum surrounding prose with all four sentinels present.
