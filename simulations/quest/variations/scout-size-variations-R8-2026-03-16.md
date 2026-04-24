**R8 variate complete** → `simulations/quest/golden/scout-size-variate-R8-2026-03-16.md`

---

## What was produced

5 complete, runnable prompt variations targeting the two new v8 criteria on top of the full R7 baseline:

| Variation | Axis | C-23 mechanism | C-24 mechanism |
|-----------|------|----------------|----------------|
| **V-01** | Charter completeness — explicit field lists | Prose charter names all 10 Phase 1 fields by name; Phase 2 charter lists 1 owned + 10 excluded | Prohibition names 4 content categories: integration points, API contracts, complexity drivers, team/timeline signals |
| **V-02** | Named category prohibition + falsifiability gate | `[Phase N Field N]` labels in every section header | 4 named prohibited categories + falsifiability gate: "if a reader could derive this from Phase 1 by negation, it's a restatement" |
| **V-03** | Role-tagged column headers (C-23 structural) | Every table column header includes `[Phase 1: Sizing Analyst]` or `[Phase 2: Risk Assessor]` | Gap column header lists all 4 prohibited categories inline at the moment of production |
| **V-04** | Reversed role sequence (gap-first) + complete charters | Phase 1 charter: 1 field owned + 10 explicitly excluded; Phase 2 charter: 10 fields owned + 1 excluded | Phase 2 (Sizing Analyst) non-access clause dynamically references the specific dimension Phase 1 identified |
| **V-05** | Three-phase + inertia-first + full charter + named prohibition + table encoding | Three charters: Phase 0 owns 1, Phase 1 owns 9, Phase 2 owns 1 — all by name; column headers back up prose | 4 named prohibited categories + falsifiability gate + column header encoding — three independent enforcement layers |

**Design consequence from R7 → R8**: Every variation passes C-20 (role separation was the R7 target). The C-23 gap (implicit field ownership) is closed by making every charter exhaustive. The C-24 gap (structural-property-only prohibition) is closed by naming the specific content class Phase 1 confirms, not just saying "address a different dimension."
