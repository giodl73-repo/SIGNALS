Written to `simulations/quest/golden/trace-skill-variate-R8-v7-2026-03-15.md`.

---

**R8 variations summary** — 5 complete prompt bodies targeting C-27, C-28, C-29:

| Variation | Axis | Target |
|-----------|------|--------|
| **V-01** | Role sequence | **C-27**: `RequiredVocabulary = {YES, VIOLATION}` declared as named closed type; relay schema column header becomes `Required (RequiredVocabulary)`; row type self-validating without sub-table inspection |
| **V-02** | Output format | **C-28**: `(TypeName)` annotation applied uniformly to every typed column across all 10+ schema tables — Coverage Matrix, Schema 1-5, relay schema, findings table, binding summary, Stage 1 table |
| **V-03** | Phrasing register | **C-29**: Defect Classification Registry (5 codes) declared before Stage 1; every structural mandate cites its defect code inline; Verdict compliance ledger adds `Defect code (DefectCodeVocab)` column — FAIL rows cite by code, not prose |
| **V-04** | C-27 + C-28 | Both vocabulary closure and uniform type annotation — `Required (RequiredVocabulary)` satisfies both criteria simultaneously via the same column header |
| **V-05** | C-27 + C-28 + C-29 | Complete R8 target — Defect registry itself carries `(DefectCodeVocab)` annotation (C-28), making the three axes additive at distinct structural layers: vocabulary, column-header, mandate-to-code |

**Key architectural decisions**:
- C-27 and C-28 are additive rather than conflicting — the relay schema's `Required (RequiredVocabulary)` column satisfies C-27 (closed vocabulary) and C-28 (typed annotation) simultaneously in V-04/V-05
- C-29 defect codes are cited in-mandate (inline at the mandate site) AND in-Verdict (via the Defect code column), satisfying the "citable by code in the ledger" requirement
- All five variations inherit V-04 R7's full architecture (Role-binding + Compliance Ledger) — no regression on C-01 through C-26
