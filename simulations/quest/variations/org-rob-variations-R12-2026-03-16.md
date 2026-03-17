Written to `simulations/quest/golden/corps-rob-variate-R12-2026-03-16.md`.

---

## R12 -- org-rob: 5 Variations

**Focus**: V-05 R11 saturated the rubric at 136/136. R12 probes beyond the ceiling toward C-32 candidates.

### Variation Axes

| V | Axis | Hypothesis |
|---|------|-----------|
| V-01 | **Verdict Registry** | VERDICT REGISTRY before Stage 1 tracks every stage's verdict (PENDING/ISSUED/INVALIDATED). VIOLATION-16 if a verdict is written without a registry update. Tests whether document-level verdict history is a structural property distinct from C-15 and C-13. |
| V-02 | **Blocker Resolution Registry** | BLOCKER REGISTRY before Stage 1 tracks every named blocker lifecycle (OPEN -> RESOLVED). Each inline BLOCKER: must also register. VIOLATION-16 + VIOLATION-17. Tests whether blocker lifecycle tracking is distinct from C-09/C-13. |
| V-03 | **Synthesis Schema Manifest** | SYNTHESIS MANIFEST at synthesis open lists all required subsections with COMPLETE/MISSING status. VIOLATION-16 + VIOLATION-17. Tests whether synthesis completeness certification is a structural property parallel to STAGE PREREQUISITE REGISTRY for execution order. |
| V-04 | **Verdict Registry + Blocker Registry** (V-01 + V-02) | Both registries coexist. VIOLATION-16 (verdict), VIOLATION-17 (blocker inline), VIOLATION-18 (synthesis Blocker Final State). 10 enforcement loops total. |
| V-05 | **Full convergence** (all three + extended taxonomy) | All three dimensions. VIOLATION-16 through VIOLATION-20. Taxonomy reaches VIOLATION-20, giving 12 enforcement loops (VIOLATION-09 through VIOLATION-20) across 7 structural families. |

### Structural Summary

The three new dimensions follow the same **write-as-you-go registry** pattern already present in STAGE PREREQUISITE REGISTRY and FINDING LEDGER: initialize before Stage 1 (or section start), populate as events occur, reproduce at synthesis for completeness verification. V-05 asks whether this pattern is itself a generalizable structural principle worthy of a single C-32 criterion covering registry completeness across all governance dimensions.

**C-32 extraction hypothesis**: Verdict Registry (Dimension A) is the strongest single-criterion candidate -- it closes a governance gap at the same structural level as STAGE PREREQUISITE REGISTRY with one new violation and one new synthesis subsection. Dimension C (Synthesis Manifest) introduces two violations at once, suggesting it may be two criteria.
