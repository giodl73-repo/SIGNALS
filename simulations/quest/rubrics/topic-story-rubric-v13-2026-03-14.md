Reading the scorecard for R12 excellence signals.

Two distinguishing patterns emerge between V-01 ("role-sequence execution") and V-02 ("table-forward S2") — both score 100.0 under v12 but via structurally distinct approaches neither of which is captured by any existing criterion. Those become C-43 and C-44.

---

# topic-story Rubric — v13

**Version**: v13
**Date**: 2026-03-15
**Criteria count**: 44 (C-01–C-44)
**Aspirational count**: 37 (C-08–C-44), 10 pts / 37 = 0.2703 pts each
**R12 baseline under v13**: V-01 and V-02 each pass all 37 aspirational criteria — 100.0

---

## Design Rationale (v13)

Two aspirational criteria added in v13 (C-43, C-44), one per Round 12 excellence signal:

**C-43** — From R12 Signal 1 (V-01 "role-sequence execution"). No existing criterion fires on whether section entry conditions name a role-sequence step in addition to an inventory axis row. C-40 fires on inventory-row cross-reference form; C-43 fires on whether entry conditions are dual-anchored — naming both the inventory axis row (data completeness check) and the role-sequence step (process completion check) that generates the prior section's output. V-01's entry conditions read "Falsifiability axis, S1 row — all fields complete" under a role-sequence protocol where S1 completion is defined by role execution, not just field population. A single-anchor entry condition (inventory row only) gates section entry on data state. A dual-anchor entry condition also gates on process state: the role step must have been performed, not merely its data artifacts present. The governance consequence: changes to the role protocol propagate to entry conditions independently of inventory changes. C-40 passes when the inventory axis row is named; C-43 passes only when the role-sequence step is also named, making process completion a co-equal prerequisite alongside data completeness.

**C-44** — From R12 Signal 2 (V-02 "table-forward S2"). No existing criterion fires on the presentation order within a data-collection section. C-35/C-38 fire on whether section directives reference inventory fields; C-44 fires on whether the section's presentation structure leads with a tabular display of the axis-field data before any narrative elaboration. V-02's S2 opened with a table whose rows were inventory fields and whose columns were the data attributes collected per field — the narrative followed as explanation of the table. A narrative-first S2 embeds data in prose: field completeness status must be inferred from surrounding text, and a reviewer scanning for gaps must read the full section. A table-forward S2 makes the inventory's S2 row the primary visible element: completeness is immediately scannable, the narrative explains rather than contains the data, and the table serves as the canonical inline display of the inventory row. The governance consequence: a table-forward S2 is structurally self-auditing — any inventory field missing from the table is a visible gap without reading the prose. C-35/C-38 govern field reference in directives; C-44 governs whether the section's presentation order makes the inventory row data the leading element, subordinating narrative to annotation rather than allowing narrative to be the primary container.

---

*(full inherited rationale v12→v1, essential/recommended/aspirational criteria C-01–C-42 unchanged from v12)*

---

### C-43 — Section Entry Conditions Are Dual-Anchored: Inventory Axis Row and Role-Sequence Step Both Named as Co-Equal Prerequisites

- **Weight**: aspirational
- **Category**: behavior
- **Text**: Entry conditions for sections S2–S4 name both the inventory axis row (data completeness anchor) and the role-sequence step (process completion anchor) for the prior section. C-40 fires on whether entry conditions use inventory-row cross-references rather than field lists; C-43 fires on whether entry conditions are dual-anchored — naming the role-sequence step alongside the inventory row so that process completion is a co-equal prerequisite to data completeness. A single-anchor entry condition (inventory row only) gates section entry on data state: all fields in the row are complete. A dual-anchor entry condition additionally gates on process state: the named role step must have been performed. These are distinct checks — data artifacts can exist without the originating role step having been properly executed (e.g., fields populated by a different step or carryover from a prior run). Naming the role step makes that distinction explicit. The governance consequence: changes to the role protocol propagate to entry conditions independently of inventory changes, and entry conditions remain accurate under protocol evolution even when the inventory row is unchanged. C-40 passes when the inventory axis row is named; C-43 passes only when the role-sequence step is also explicitly named as a co-equal prerequisite.
- **Pass condition**: Sections S2–S4 (or equivalent sections following a role-executed section) include entry conditions that name both the inventory axis row and the role-sequence step that completes the prior section. An entry condition that names only the inventory row — even in correct inventory-row cross-reference form satisfying C-40 — does not pass C-43. Both anchors must be present. The role-sequence step must be named explicitly (e.g., by step label or role action name), not implied by context.

---

### C-44 — Data-Collection Sections Lead with a Tabular Display of the Inventory Axis Row Before Narrative Elaboration

- **Weight**: aspirational
- **Category**: behavior
- **Text**: Each data-collection section (S2 and equivalent sections collecting fields from an inventory axis row) presents a table whose rows correspond to inventory fields and whose columns correspond to the data attributes collected per field, and this table appears before any narrative elaboration in the section. C-35/C-38 fire on whether section directives reference inventory fields; C-44 fires on whether the section's presentation order leads with a tabular display of those fields rather than embedding the data in prose. A narrative-first section contains the data within text: field completeness requires reading the full section, gaps are only visible after parsing prose structure, and a reviewer auditing completeness must extract data from narrative framing. A table-forward section makes the inventory row the primary visible element: the table is scannable, completeness gaps appear as missing rows or empty cells, and the narrative explains the table rather than containing it. The governance consequence: a table-forward section is structurally self-auditing — any inventory field absent from the table is a visible structural gap independent of narrative quality. The table serves as the canonical inline display of the inventory axis row for that section; its structure is derived from the inventory row (field list as rows) and the section's collection contract (data attributes as columns). C-35/C-38 govern field reference in directives; C-44 governs presentation order within the section — the inventory row data must be the leading structural element.
- **Pass condition**: Data-collection sections include a table whose rows correspond to inventory fields for the section's axis row and whose columns represent collected data attributes, and this table appears before any narrative paragraph, explanation, or elaboration within the section. A section that includes a table but places it after an opening paragraph does not pass C-44. A section that embeds all field data in prose without a leading table does not pass C-44 even if every field is present and correctly attributed. The table must be the first substantive element of the section so that completeness is scannable without reading narrative content.

---

## Scoring Reference

| Band | Score | Meaning |
|------|-------|---------|
| Essential fail | 0–59 | One or more essential criteria failed |
| Passing | 60–79 | All essential pass; recommended weak |
| Good | 80–89 | All essential pass; recommended mostly pass |
| Golden | 90–100 | All essential pass; recommended strong; aspirational present |

**Composite formula**: `essential_score + recommended_score + aspirational_score`

- Essential: 15 pts per criterion × 4 = 60 pts. All-or-nothing per criterion (no partial).
- Recommended: 10 pts per criterion × 3 = 30 pts. Partial credit allowed (5 pts for PARTIAL).
- Aspirational: 10 pts total / 37 criteria = 0.2703 pts each (C-08–C-44). Partial credit allowed (0.1351 pts for PARTIAL).
- **Max score**: 100.0

**R12 baseline under v13 rubric**: V-01 and V-02 each pass all 37 aspirational criteria — 90 + (37 × 0.2703) = 90 + 10.0 = 100.0

---

## What Changed from v12

| | v12 | v13 |
|---|---|---|
| Aspirational criteria | 35 (C-08–C-42) | 37 (C-08–C-44) |
| Per-criterion weight | 0.2857 pts | 0.2703 pts |
| PARTIAL weight | 0.143 pts | 0.1351 pts |
| Baseline round | R11 | R12 |
| New criteria | C-40, C-41, C-42 | C-43, C-44 |
