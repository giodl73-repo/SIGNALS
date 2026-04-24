**Scout-Size R20 — 5 variations written** to `simulations/quest/golden/scout-size-variate-R20-2026-03-17.md`.

---

## Summary

The two new v20 criteria (C-42/C-43) both trace to R19 V-01's same structural error: the standalone gap section was positioned *after* the compilation table, which meant (1) the pointer was a forward reference, and (2) the relational constraint label stayed in the compilation table's column header rather than inside the standalone section. The R20 fix is a single repositioning that resolves both simultaneously.

### Variation axes

| # | Axis | Key design choice | Expected score |
|---|---|---|---|
| **V-01** | Gap section ordering | Two-phase; standalone section before compilation table; defense cluster inside standalone section | 100 |
| **V-02** | Inertia-first framing | Same machinery as V-01; inertia check is the anchor frame for all subsequent judgments | 100 |
| **V-03** | Phrasing register (single-phase) | Direct second-person imperatives; no role separation; drops C-20/C-23-C-29; tests if same C-30/C-42/C-43 outcomes are achievable without role charters | ~87–90 |
| **V-04** | Three-role sequence + table-dominant | Inertia Auditor + Sizing Analyst + Risk Assessor; field ownership tables; three-column compilation table | 100 |
| **V-05** | Lifecycle emphasis + champion | Named transition gates between every phase; CONFIDENCE GAP CHECKPOINT is a formal phase gate, not just a section; four-field DIAGNOSTIC PATTERN with REMEDIATION; designed for all 35 aspirationals | 100 |

### The structural pattern all four high-scoring variations share

```
Phase 0: Entry Gate (CLOSED/OPEN)
Phase 1: Sizing Analyst → Inertia, Points, Tier, Basis
── CONFIDENCE GAP CHECKPOINT ──   ← standalone section HERE (before compilation table)
  [relational constraint label]   ← C-30 mechanism 1, inside standalone section (C-42)
  [self-test with failure class]  ← C-30 mechanism 2, inside standalone section
  [── DIAGNOSTIC PATTERN ──]      ← C-30 mechanism 3, inside standalone section
Phase 2: Risk Assessor → Tier-Up, Tier-Down
Output Compilation Table          ← AFTER standalone section (C-43); gap row = pointer (C-40)
```
