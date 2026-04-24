Written to `simulations/quest/rubrics/topic-story-rubric-v7-variations-R7-2026-03-14.md`.

---

## R7 Variations — `topic-story` (Round 7)

### Architecture Summary

All five variations inherit the full R5/R6 inheritance (C-01 through C-24 all PASSing). The exclusive R7 focus is satisfying C-25, C-26, C-27 — which require that the checklist be extended under composition with discipline, not just as a patch.

**The compound R7 design problem from R6:**
R6 V-05 (99.4) failed C-24 because `**Prior position**:`, `**Baseline distance**:`, `**Signals establish**:` were required labeled fields with no checklist items — three fields from the inertia-framing axis that were never registered. The mechanical fix (add 3 items) is obvious, but R7's new criteria require the *procedure* to be demonstrable, not just the *outcome*.

---

### V-01 — Explicit Design-Axis Registration *(single-axis: inertia framing)*

**Hypothesis**: Naming both design axes in a preamble table, listing each axis's fields, and building the checklist by a single pass over the complete inventory satisfies C-26 through a visible audit trail. Section architecture unchanged from R6 V-05.

**Key mechanism**: The axis table doubles as the C-26 registration document. Any future extension must name its axis and register its fields in the table before writing a section. Checklist grows from 9 → 12 items (adds items 10–12 for the three inertia-framing fields).

---

### V-02 — Field-Inventory-First Derivation *(single-axis: checklist architecture)*

**Hypothesis**: Prefacing the checklist with an explicit "Required Labeled Fields" inventory table (8 rows, one per field, with axis annotation) from which checklist items are mechanically derived — one item per row, annotated *(F-01)* through *(F-08)* — makes the C-27 single-pass procedure maximally explicit and prevents orphaning structurally (a field cannot be added to a section without first appearing in the inventory).

**Key mechanism**: The inventory is the authoritative source of truth. The checklist is a mechanical projection of it. Adding a labeled field to a section without updating the inventory is a visible violation.

---

### V-03 — Lean Imperative Register *(single-axis: phrasing register)*

**Hypothesis**: The same 12-item checklist, same 8 labeled fields, same failure modes — expressed in stripped-down imperative sentences ("Locate each element or stop") — reduces cognitive overhead without any structural change. If the rubric scores V-03 identically to V-01, register is confirmed orthogonal to structural compliance.

**Key mechanism**: Pure phrasing compression. Every structural requirement from V-01 is present; all meta-explanation and framing language is removed. Tests whether the rubric fires on structure vs. presentation.

---

### V-04 — Baseline-First Architecture *(compound: lifecycle emphasis + role sequence)*

**Hypothesis**: Moving the prior position into a dedicated opening section (Section 0: Baseline) before findings changes the narrative arc — the document measures from a named position rather than arriving at one. The Inertia-framing axis fields are split across two sections (`**Prior position**:` in Section 0; `**Baseline distance**:`/`**Signals establish**:` in Recommendation). The checklist has 13 items (adds section-structure item for Baseline + 3 field items).

**Key test**: Whether C-26 fires on the distributed-field case — the axis registration table must show fields in two sections, which is a stronger test of the procedure's completeness.

---

### V-05 — Consolidated Position-Delta Field *(compound: output format + inertia framing)*

**Hypothesis**: Replacing the three inertia-framing fields with a single `**Position delta**:` field (internal structure: `Prior: / Delta: / Established by:`) reduces the checklist to 10 items with zero orphaning surface. Tests whether semantic consolidation is a valid C-27 strategy — one field, one checklist item, all three semantic components enforced by the field's internal template structure.

**Key test**: Whether C-24 fires on the consolidated field (the inventory has one entry for the inertia axis, fully covered), whether C-13 still passes (inertia test visible in two non-synthesis sections: `**Inertia verdict**:` in Findings + `**Position delta**:` in Recommendation), and whether C-27 accepts consolidation as equivalent to one-field-one-item derivation.

---

### The R7 Critical Experiment

The four open questions the scorecards should resolve:

1. **Does the axis-table preamble (V-01) constitute demonstrable C-26**, or does C-26 require the registration to be tied to a procedure note?
2. **Does V-05's `**Position delta**:` satisfy C-13** (inertia test in two non-synthesis sections), or does the field consolidation break the inertia-test requirement?
3. **Does C-01 fire on V-04's five-section structure**, or does it pass because all four required sections are present?
4. **Is lean register (V-03) structurally neutral**, or does it produce a detectable scoring difference?
