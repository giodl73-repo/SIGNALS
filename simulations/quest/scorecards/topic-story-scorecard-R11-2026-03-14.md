# topic-story Rubric v11 — R11 Scorecard

**Round**: 11 | **Rubric**: v11 (39 criteria, C-37/C-38/C-39 new) | **Date**: 2026-03-15

---

## Score Summary

| Variation | Essential (60) | Recommended (30) | Aspirational (10) | Composite | All Essential |
|---|---|---|---|---|---|
| V-01 | 60 | 30 | 10.0 | **100.0** | YES |
| V-02 | 60 | 30 | 10.0 | **100.0** | YES |
| V-03 | 60 | 30 | 10.0 | **100.0** | YES |
| V-04 | 60 | 30 | 10.0 | **100.0** | YES |
| V-05 | 60 | 30 | 10.0 | **100.0** | YES |

All five variations score **100.0**. All preserve C-37/C-38/C-39 from the R10 V-05 baseline, and no variation removes any passing feature — all criteria hold.

---

## Ranking (Structural Differentiation)

Since scores are tied, rank reflects feature completeness and forward-compatibility:

1. **V-05** — Full compound: status-quo framing + Section column + entry conditions + entry-condition/inventory cross-referencing. Governance chain is complete.
2. **V-04** — Compound: status-quo framing + Section column. Two clean axes.
3. **V-01** — Single-axis: status-quo competitor named in S1 filter.
4. **V-02** — Single-axis: Section column extends placement auditability to inventory.
5. **V-03** — Single-axis: per-section entry conditions enforce writing sequence.

---

## Excellence Signals from V-05

**Signal 1 — Entry-condition/inventory governance chain**
S2–S4 entry conditions each cross-reference the inventory axis row for the prior section (e.g., "Falsifiability axis, S1 row") rather than naming prerequisite fields directly. Adding a field to an inventory row automatically propagates to the entry condition that references that row — single-artifact update, no independent checklist maintenance.

**Signal 2 — Extension procedure includes entry-condition update as required step**
Step 4 of the extension procedure is: "update the entry condition of the section FOLLOWING the new field's section, adding a cross-reference to the new inventory row." Without this, an author satisfying C-26 (register in checklist) could leave entry conditions stale. With it, the governance chain is maintained as a prescribed operation.

**Signal 3 — Checklist footer references inventory's axis-and-section structure**
Footer reads "organized by axis and section per the field inventory" — checklist organization is explicitly derived from the inventory's two-dimensional structure (axis × section), not from an independent grouping decision. Completes the organizational reference chain.

---

## Analytical Note

All five score 100.0 by design: R11 variations were constructed to preserve C-37/C-38/C-39 while adding only structural features. The rubric floor has converged. The three excellence signals above are clear v12 criterion candidates: governance-chain cross-referencing, extension-procedure entry-condition step, and footer/inventory structural mirroring.

---

```json
{"top_score": 100.0, "all_essential_pass": true, "new_patterns": ["Entry conditions cross-reference inventory axis rows rather than naming prerequisite fields independently, creating a governance chain where a single inventory row update propagates automatically to both the section template and the next section's entry condition", "Extension procedure explicitly names the entry-condition update as a required fifth step, making governance-chain maintenance a prescribed operation rather than an inferred obligation", "Checklist footer explicitly states that item organization mirrors the inventory's axis-and-section structure, completing the organizational reference chain from inventory to checklist"]}
```
