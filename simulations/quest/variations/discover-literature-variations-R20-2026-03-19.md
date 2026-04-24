Written to `simulations/quest/variations/discover-literature-variations-R20-2026-03-20.md`.

---

## R20 Summary

**Axes explored**: Phrasing Register, Lifecycle Emphasis, Inertia Framing (3 single-axis; 2 combined)

| V | Axis | Predicted |
|---|------|-----------|
| V-01 | Phrasing Register -- conversational, all tokens preserved | 235/235 |
| V-02 | Lifecycle Emphasis -- C-29 consolidation block omitted | 195/235 |
| V-03 | Inertia Framing -- Phase-0 architecture, `inertia_committed` absent from PHASE 1 COMPLETE | 180/235 |
| V-04 | Combined: Conversational + single-obligation preamble (OBLIGATION B absent from contract) | 230/235 |
| V-05 | Full synthesis: Conversational + expanded inertia framing in Phase 1 and Phase 4, all tokens | 235/235 |

**Failure cascade logic:**

- **V-02** (195): Removing the C-29 block fails C-30, cascading through C-37 (8 × 5 = 40 pts). The in-token C-28/C-29 annotations are sufficient for C-29 itself but C-30's named-block requirement is strict.
- **V-03** (180): Moving inertia to Phase-0 removes `inertia_committed=[yes]` from PHASE 1 COMPLETE, failing C-27(a). C-27 FAIL cascades through C-37 (11 × 5 = 55 pts). C-14 may still pass (inertia is named somewhere) but the lifecycle-integration axis is broken at its first link.
- **V-04** (230): OBLIGATION B is present in Phase 3 inline but absent from the preamble's global enforcement contract. C-15 is a PARTIAL -- 5 pts.

**Key insight surfaced by V-01**: Register is fully orthogonal to structural compliance. A conversational voice can satisfy every criterion from C-01 through C-37 identically to formal prose, including the deep annotation chains. This suggests the rubric could add a C-38 register criterion (e.g., "prose surrounding tokens is in a register consistent with the skill's intended context") without any existing criterion needing modification.
