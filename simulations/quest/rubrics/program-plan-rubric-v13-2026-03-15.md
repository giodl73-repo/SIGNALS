Here is the complete updated rubric written to `simulations/quest/rubrics/program-plan-rubric-v13-2026-03-16.md`.

---

## Summary of v13 changes

Three new aspirational criteria extracted from R12 excellence signals:

### C-41 — BAD PLAN Header Meta-Commentary: Per-Criterion Annotation-Type Index
The header goes beyond C-38's affirmative coverage claim and enumerates *which annotation type satisfies which criterion* inline — e.g., `# C-39: skills entries annotated`, `# C-37: name entries annotated`, `# C-26: gate_fail: entries annotated`. Converts the header from a scope declaration into a criterion-indexed navigation aid. **Prerequisite: C-38. Partial: 2 of 4 annotation types mapped.**

### C-42 — Co-Location Family Declared as a Named Document Section
A dedicated named section before the BAD PLAN block (e.g., "FIELD CO-LOCATION RULE") presents all three field-level co-location criteria (C-26/gate_fail:, C-37/name:, C-39/skills:) as a structured family table. Converts three independent criteria into a named architectural principle with a document home — future field types become structurally predictable. **Prerequisites: C-26, C-37, C-39. Partial: 2 of 3 field types in structured format.**

### C-43 — Recommended-Tier strategy: Field Structurally Pre-Populated in YAML Template
The YAML template scaffold pre-populates `strategy:` with a non-empty placeholder string, applying C-11's structural-enforcement principle to the recommended tier. C-07 compliance becomes scaffold-enforced by default rather than prose-attention-dependent — mirrors exactly how echo pre-positioning enforces C-02. **Prerequisites: C-07, C-11. No partial credit.**

**Scoring delta**: 33 → 36 aspirational · 165 → 180 aspirational pts · **255 → 270 total pts**. Formula denominator: `aspirational_pass/36 * 180`. Golden threshold unchanged (>= 80).
