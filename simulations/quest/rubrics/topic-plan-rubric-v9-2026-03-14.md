Written to `simulations/quest/rubrics/topic-plan-rubric-v9-2026-03-15.md`.

---

**Two new criteria extracted from Round 9:**

**C-34 — Enumerated-column valid-value specificity at both declaration sites** (`enforcement`)

The discriminating signal: V-02 declares the Reversibility column in the upfront schema but without the closed three-value enum or a prose-prohibition rule — and fails C-32. V-01 and V-05 embed "select one; prose is not a valid value" in both the upfront schema and the commitment checkpoint — and pass. The gap: C-26 requires the schema block to name columns; C-32 requires the three-value enum. Neither required the constraint to be expressed *at both declaration sites* (upfront schema + commitment checkpoint). A column name in the schema without its valid values leaves the model free to produce prose that is nominally compliant. C-34 requires every enumerated column to carry the closed value list and prose-prohibition rule in both the upfront schema block and at each schema-commitment checkpoint.

**C-35 — Assumption table columns must be independently populated content** (`depth`)

The discriminating signal: V-01 declares a five-column upfront schema and fails C-33 because "Implicit evidence" was replaced by the row key — four content columns + one key column. Row keys are navigational, not analytical. C-33 requires all five columns declared; C-35 requires each to be populated with content that cannot be derived from the row identity or any adjacent column. A declared column whose content is structurally reconstructable from the row key is a navigational alias, not a dimension, and is treated as absent for scoring.

**Updated totals:** 35 criteria, 225 pts. Formula: `(essential_pass/5 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/27 × 135)`. Golden threshold bumped to 130.

**Phase 7 added to the arc:** *schema specificity and column independence* — constraints must be expressed at both declaration sites with their valid values, and every declared column must carry independent analytical content.
