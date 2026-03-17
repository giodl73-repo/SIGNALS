v20 rubric written. Here's a summary of what was extracted and added:

---

### v20 Changes — Summary

**New ceiling: 293** (283 + 5 + 5)

**C-50 — CONVICTION GAP DIAGNOSIS STRUCTURAL FAIL Sentinel Column Enumeration** (+5):
- Signal source: V-03 and V-04 (R19) both carry CGD second sentinels that enumerate the five analysis columns by name; V-02 and V-05 use generic "substantive analysis cells" group-noun forms
- C-50 tests whether the C-48 STRUCTURAL FAIL sentinel names specific column identifiers rather than a generic group description — the column-identified upgrade parallel to how TRACEABILITY AUDIT uses "N + blank col 5" vs. a generic description
- Passes only when the second RULE sentinel text contains the actual column header labels (Sub-section, Register found, Register declared, Scout sub-skill, Evidence needed)

**C-51 — Complete Five-Table Column-Enumerated STRUCTURAL FAIL Architecture** (+5):
- Strict superset of C-49 + C-50
- All five tables' STRUCTURAL FAIL sentinels enumerate specific column identifiers; TRACEABILITY AUDIT's "N + blank col 5" already satisfies; the gap is MAP, CONVICTION DELTA, and STT upgrading from generic "blank analysis cells" to column-identified form
- No R19 variant earns C-51

**D20** establishes:
- **Orthogonality confirmed**: V-03 (C-50 FULL, C-49 NO CREDIT) and V-05 (C-49 FULL, C-50 NO CREDIT) — column-enumeration and dual-sentinel completeness are independent structural properties
- V-04 nearest ceiling at 288; gap is MAP/CONVICTION DELTA/STT column-enumeration
- Register invariance extends to C-50: conversational column names (V-03) and formal column names (V-04) both earn FULL
- 15-step chain test for C-51

**Retroactive R19 scores under v20:**

| Variant | v19 | C-50 | C-51 | v20 |
|---------|-----|------|------|-----|
| V-04 — Complete Five-Table Dual-Sentinel, Max Density | 283 | +5 | 0 | **288** |
| V-03 — Conversational CGD Dual-Sentinel | 278 | +5 | 0 | **283** |
| V-05 — Complete Five-Table Dual-Sentinel, Compressed | 283 | 0 | 0 | **283** |
| V-02 — Minimum CGD Dual-Sentinel | 278 | 0 | 0 | **278** |
| V-01 — Five-Sentinel Control | 273 | 0 | 0 | **273** |
