Written to `simulations/quest/rubrics/trace-component-rubric-v19-2026-03-15.md`.

---

**Changes from v18 to v19:**

**One new criterion promoted from R18:**

| # | Name | Source | What it adds over v18 |
|---|------|--------|----------------------|
| **C-58** | Schema Area 3 Structured Enforcement Table | R18 C-12 differential -- V-02 PASS (Schema Area 3 is a boundary table with `Enforcement Rationale` column), V-01 FAIL (Schema Area 3 is prose with sub-sections, no table format) | C-56 requires the compound-header template to be declared as a named schema field. C-57 requires that template to include a worked exemplar. C-58 requires the template section itself to be in **table format** with an `Enforcement Rationale` column populated for every row -- so the enforcement logic for each template component is a discrete, independently verifiable cell rather than embedded in prose. |

**Ceiling: 188 → 190 pts. 58 criteria.**

**R18 dependency structure:**
- C-58 requires C-56 as a structural precondition (enforcement table requires a declared template to organize into rows)
- C-58 is independent of C-57 (exemplar can be in prose and still fail C-58; exemplar as a table row with Enforcement Rationale column passes both)
- V-02: carries C-56 + C-57 + C-58
- V-01: carries C-56 + C-57, fails C-58 (prose Area 3, no table format)
