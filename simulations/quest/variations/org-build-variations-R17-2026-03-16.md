**R17 variate written** to `simulations/quest/golden/org-build-variate-R17-2026-03-16.md`.

---

## R17 Gap Analysis

All R16 variations scored 98.9 (25/28) or 99.6 (27/28). The single universal blocker was **C-31**: `T2-ROLE-COUNT: [integer >= 20]` and `T2-AREA-COUNT: [integer >= 2]` are range annotations, not closed enumerations.

## R17 Variation Axes

| Var | Axis | C-31 Fix | Predicted |
|-----|------|----------|-----------|
| **V-01** | Count-field encoding: binary compliance tokens | `T2-COUNT-COMPLIANCE: [FLOOR-MET \| FLOOR-MISS]`, `T2-AREA-COMPLIANCE: [ADEQUATE \| INADEQUATE]` | 28/28 |
| **V-02** | Count-field encoding: depth-outcome class | `T2-ROLE-OUTCOME: [STANDARD-FLOOR-MET \| DEEP-FLOOR-MET \| FLOOR-MISS]`, table-dominant format | 28/28 |
| **V-03** | Count fields removed from record block | Count compliance verified in Constraints pre-emission; record block only emits T2-IA-SCOPE-SOURCE, T2-CATEGORY-A, T2-CATEGORY-B | 28/28 |
| **V-04** | Compliance tokens + terse imperative | V-01 fix + R16 V-04 phrasing register, zero advisory language | 28/28 |
| **V-05** | Depth-outcome class + complete artifact skeleton | `T2-ROLE-OUTCOME` / `T2-AREA-OUTCOME` + full ORG-CHART.MD skeleton with `{{T2-ROLE-OUTCOME}}` and `{{T2-AREA-OUTCOME}}` slots in Generation Metadata section | **28/28 = 100.0** |

## Design Decision Worth Noting

**V-05** introduces a "Generation Metadata" section in the org-chart.md skeleton. This solves the C-22 gap that existed in R16 V-01–V-04: count and area gate variables had no natural home in the artifact. Metadata section gives every Phase 2 gate variable an artifact slot, satisfying C-22 and C-31 simultaneously. If V-05 scores 100.0, the skeleton metadata section becomes a structural pattern worth extracting to the rubric as an excellence signal.
