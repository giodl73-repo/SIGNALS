All edits land correctly. Here is the complete updated rubric:

---

# topic-story Rubric — v12

**Version**: v12
**Date**: 2026-03-15
**Criteria count**: 42 (C-01--C-42)
**Aspirational count**: 35 (C-08--C-42), 10 pts / 35 = 0.2857 pts each
**R11 baseline under v12**: V-05 passes all 35 aspirational criteria -- 100.0

---

## Design Rationale (v12)

Three aspirational criteria added in v12 (C-40, C-41, C-42), one per Round 11 excellence signal:

**C-40** -- From R11 Signal 1. No existing criterion fires on the form of section entry conditions; C-40 fires on whether entry conditions for sections S2–S4 cross-reference the prior section's inventory axis row rather than enumerating prerequisite field names directly. V-05's entry conditions named "Falsifiability axis, S1 row -- all fields complete" rather than listing individual field names. A field-list entry condition requires independent maintenance each time the prior section's inventory changes; an inventory-row cross-reference delegates maintenance to the inventory. Adding a field to the inventory row automatically satisfies the entry condition for the following section -- no entry condition update required. The governance chain consequence: a single inventory row update propagates to the section template, to the section directive (via C-35/C-38), and to the following section's entry condition -- three surfaces, one operation. C-40 passes only when entry conditions reference the inventory axis row and the reference form makes field membership an inventory-owned property.

**C-41** -- From R11 Signal 2 (C-26 PASS extension). C-26 fires on whether incorporating a new design axis includes registering its fields in the checklist at incorporation time; C-41 fires on whether the extension procedure also names the entry-condition update of the following section as a required step. V-05 named Step 4 of the extension procedure: "update the entry condition of the section FOLLOWING the new field's section, adding a cross-reference to the new inventory row." Without this step, an author satisfying C-26 could leave entry conditions stale. With the step named, governance-chain maintenance under C-40 becomes a prescribed operation. C-26 fires on checklist registration; C-41 fires on whether the entry-condition update is also prescribed in the same extension operation.

**C-42** -- From R11 Signal 3 (C-36/C-39 organizational extension). C-36 fires on constraint content authority (inventory governs checklist constraint items); C-42 fires on whether the checklist's organizational structure is explicitly declared as derived from the inventory's two-dimensional structure (axis x section). V-05's footer read "organized by axis and section per the field inventory" -- closing the organizational reference chain. Without this declaration, checklist item groupings are an independent design decision. With the declaration, checklist structure is a downstream reflection of inventory structure: reorganizing the checklist requires reorganizing the inventory first. C-36 and C-39 govern constraint content; C-42 governs organizational structure -- together they complete the checklist's reference-chain dependency on the inventory.

---

*(full inherited rationale v11→v1, essential/recommended/aspirational criteria C-01–C-39 unchanged from v11)*

---

### C-40 -- Section Entry Conditions Cross-Reference the Prior Section's Inventory Axis Row Rather Than Naming Prerequisite Fields Independently
- **Weight**: aspirational
- **Category**: behavior
- **Text**: Entry conditions for sections S2–S4 cross-reference the inventory axis row for the prior section rather than enumerating prerequisite field names. No existing criterion fires on the form of section entry conditions; C-40 fires on whether those conditions use inventory cross-references as their grounding artifact. A field-list entry condition names the specific fields that must be completed -- this form requires independent maintenance each time the prior section's inventory changes. An inventory-row cross-reference entry condition names the axis row instead -- this form delegates maintenance to the inventory. Adding a field to the axis row automatically captures it in the entry condition; the entry condition never needs updating independently. The governance chain consequence: a single inventory row update propagates to the section template, to the section directive (via C-35/C-38), and to the following section's entry condition -- three surfaces, one operation. C-40 passes only when entry conditions reference the inventory axis row and the reference form makes field membership an inventory-owned property.
- **Pass condition**: Sections S2–S4 (or equivalent sections following an inventoried section) include entry conditions that name the inventory axis row for the prior section as the prerequisite rather than listing individual field names. A section entry condition that directly names fields -- even correctly, even completely -- does not pass C-40. The reference must name the inventory axis row so that field additions propagate automatically without independent entry-condition maintenance.

### C-41 -- Extension Procedure Names Entry-Condition Update as a Required Step Following New Field Registration
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The extension procedure explicitly names updating the entry condition of the section following the new field's section as a required step, making governance-chain maintenance a prescribed operation rather than an inferred obligation. C-26 fires on whether incorporating a new design axis includes registering its fields in the checklist at incorporation time; C-41 fires on whether the extension procedure also includes the entry-condition update as a named step. Without this step, an author correctly satisfying C-26 could leave entry conditions stale -- the obligation is not stated, and a procedurally complete author would not know to perform it. With the step named, the governance chain established by C-40 is maintained by prescription. C-26 fires on checklist registration at incorporation time; C-41 fires on whether the entry-condition update is also prescribed as a required step in the same extension operation.
- **Pass condition**: The extension procedure includes an explicit named step that prescribes updating the entry condition of the section following the new field's section, with sufficient specificity that an author knows to add a cross-reference to the new inventory row. An extension procedure that prescribes checklist registration (C-26) but omits the entry-condition update step does not pass C-41, even if C-40 is satisfied. The step must be a named, required operation -- not a parenthetical note or optional guidance.

### C-42 -- Checklist Footer Explicitly Derives Its Organizational Structure from the Inventory's Axis-and-Section Dimensions
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The checklist footer explicitly states that checklist item organization is derived from the inventory's two-dimensional structure (axis x section) rather than from an independent grouping decision. C-36 fires on constraint content authority; C-42 fires on whether the checklist's organizational structure -- how items are grouped -- is explicitly declared as a downstream reflection of the inventory's axis-and-section dimensions. Without this declaration, checklist organization is a free variable: a future editor could reorganize items by section type or enforcement surface with no criterion flagging the divergence. With the declaration, reorganizing the checklist requires reorganizing the inventory first. C-36 and C-39 govern constraint content; C-42 governs organizational structure -- completing the checklist's reference-chain dependency on the inventory. C-36 passes on constraint content authority; C-42 passes only when organizational structure is explicitly declared as derived from the inventory's two-dimensional structure.
- **Pass condition**: The checklist contains an explicit statement -- in the footer, preamble, or organizational header -- that its item groupings are organized by axis and section as defined in the field inventory. A checklist that happens to mirror inventory organization without declaring the derivation does not pass C-42. The declaration must name both organizational dimensions (axis and section) to make the structural dependency unambiguous.

---

## Scoring Reference

| Band | Score | Meaning |
|------|-------|---------|
| Essential fail | 0-59 | One or more essential criteria failed |
| Passing | 60-79 | All essential pass; recommended weak |
| Good | 80-89 | All essential pass; recommended mostly pass |
| Golden | 90-100 | All essential pass; recommended strong; aspirational present |

**Composite formula**: `essential_score + recommended_score + aspirational_score`

- Essential: 15 pts per criterion x 4 = 60 pts. All-or-nothing per criterion (no partial).
- Recommended: 10 pts per criterion x 3 = 30 pts. Partial credit allowed (5 pts for PARTIAL).
- Aspirational: 10 pts total / 35 criteria = 0.2857 pts each (C-08--C-42). Partial credit allowed (0.143 pts for PARTIAL).
- **Max score**: 100.0

**R11 baseline under v12 rubric**: V-05 passes all 35 aspirational criteria -- 90 + (35 x 0.2857) = 90 + 10.0 = 100.0

---

Written to `simulations/quest/rubrics/topic-story-rubric-v12-2026-03-15.md`.

**What changed from v11:**

| | v11 | v12 |
|---|---|---|
| Aspirational criteria | 32 (C-08--C-39) | 35 (C-08--C-42) |
| Per-criterion weight | 0.3125 pts | 0.2857 pts |
| PARTIAL weight | 0.156 pts | 0.143 pts |
| Baseline round | R10 | R11 |

**C-40** closes the governance chain at the entry-condition level: field additions propagate to entry conditions automatically via inventory row reference, not independent field lists.

**C-41** closes the extension procedure: registering a field (C-26) now includes a mandatory step to update the following section's entry condition, making C-40 maintenance prescribed rather than inferred.

**C-42** closes the organizational reference chain: checklist groupings are explicitly declared as derived from the inventory's axis × section structure, making checklist organization a downstream consequence of inventory structure rather than a free design variable.
