Written to `simulations/quest/golden/scout-size-variate-R4-2026-03-17.md`.

---

## R4 Variations — Summary

**What R3 established**: V-05 scored 100/100 but achieved C-09 + C-10 via a *post-write* self-check — scope boundary and break-even resolved after analysis, not before. C-18 and C-19 formalize the two structural gaps sourced from R3.

**Five variations, two axes:**

| ID | Axes | C-18 bet | C-19 bet |
|----|------|----------|----------|
| **V-01** | Pre-write gate only | PRE-FLIGHT GATE before INERTIA CHECK — scope boundary + break-even as preconditions | Not targeted |
| **V-02** | Prohibition guards only | Not targeted | SCOPE EXCLUSIONS canonical section + explicit guards on CONFIDENCE, SURFACE AREA, COMPLEXITY, SYNTHESIS |
| **V-03** | Gate + guards (minimal) | Gate fires before all sections | Prohibition guards throughout, no R3 machinery |
| **V-04** | Gate + guards + R3 V-05 (17-criterion self-check) | Gate before PRELIMINARY HYPOTHESIS | Guards on all adjacent sections |
| **V-05** | Full integration + 19-criterion self-check | Gate + post-write enforcement via C-18 checklist item | Guards + C-19 checklist item specifying exactly which adjacent sections must be closed |

**Key design decisions:**
- **Gate placement**: fires before MANDATORY OPENING: PRELIMINARY HYPOTHESIS (the hypothesis is itself an analysis commitment — scope boundary must precede it)
- **C-19 minimum pass**: CONFIDENCE must say "do not list unknowns here"; at least one section adjacent to scope exclusion canonical home must be closed
- **V-04 vs V-05**: V-04 keeps 17-criterion self-check to isolate whether structural mechanisms alone are sufficient; V-05 adds C-18/C-19 checklist items for dual enforcement
