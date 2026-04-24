Written to `simulations/quest/golden/corps-chart-variate-R11-2026-03-17.md`.

---

## corps-chart R11 — 5 Variations

**R11 targets**: C-29 (BEFORE-PRODUCE for non-FORMAT-CONTRACT structural forms) and C-30 (per-role-name CHECK within charter Membership/Decides multi-role lists).

| ID | Axis | Hypothesis |
|----|------|------------|
| **V-01** | C-29 only, on R10 V-02 baseline | Temporal gap applies equally to the ROLE-NAME LOCK block (C-13) and four-field Rebuttal form (C-14). BEFORE-PRODUCE directives naming required fields immediately before each production command close the structural-form recall gap that C-26 closes for FORMAT CONTRACT schemas. |
| **V-02** | C-30 only, on R10 V-02 baseline | Section-level CHECK [SITE 3] fires once before a Membership list is written; a four-role list can introduce a novel name at position 3 before the CHECK fades. Per-role-name verification before each append eliminates the intra-field compliance-drift failure mode — the field-level analogue of C-28's row-level directive. |
| **V-03** | C-29 only (imperative register), on R10 V-03 baseline | Same temporal-gap mechanism as V-01 but with prohibitive command phrasing ("DO NOT emit the ROLE-NAME LOCK until you have counted ROLES-LOADED entries") rather than schema-reference phrasing ("BEFORE PRODUCING THE ROLE-NAME LOCK: re-read..."). Tests whether command-register framing produces higher compliance than schema-reference framing for structural-form back-references. |
| **V-04** | C-29 + C-30 combined, on R10 V-04 baseline | Both mechanisms are non-overlapping: C-29 closes temporal gaps for structural forms declared outside the FORMAT CONTRACT; C-30 closes intra-field role drift in charter multi-role lists. C-28 (per-cell) deliberately absent to preserve clean V-04→V-05 delta. |
| **V-05** | Full integration: C-29 + C-30 on R10 V-05 baseline | Completes the two remaining enforcement gaps on the maximum-stack baseline. C-29 extends BEFORE-PRODUCE to ROLE-NAME LOCK and Rebuttal form. C-30 completes the four-level enforcement hierarchy: document declaration (C-13) → section CHECK (C-21) → column/field instruction (C-25/C-27) → row/name per-item verify (C-28/C-30). |

**Key mechanisms added in each variation:**

- **C-29 (V-01, V-03, V-04, V-05)**: Two `BEFORE PRODUCING THE [FORM]: re-read [required fields]` directives — one before the ROLE-NAME LOCK emission, one before the REBUTTAL FORM block. Both name the structural form's required content explicitly to close the multi-thousand-token recall gap.

- **C-30 (V-02, V-04, V-05)**: `Per-role-name directive` embedded in both `Membership` and `Decides` field instructions: *"verify each name against the ROLE-NAME LOCK before appending the next — do not write the full list and verify after."* This closes the within-list compliance-drift failure mode that section-level CHECKs cannot catch.
