Reading the scorecard carefully to extract R20 excellence patterns before writing.

**R20 excellence patterns from the scorecard:**

**Pattern 1 — Table-merge and column-rename prohibitions embedded in Rule 5** (V-05 on C-64)
V-05's schema note adds "Do not merge the two tables. Do not rename the column in either table." V-02 passes C-64 but its schema note only declares symmetry — it does not prohibit the two structural escapes that dissolve compliance: merging tables (eliminating the split) or renaming the column in one table (making column names technically differ). C-64 requires symmetric columns; V-05 closes the gap where a model can appear to comply by eliminating the feature that makes symmetry meaningful.

**Pattern 2 — Rule 3 carries an explicit failure condition** (V-05 on C-63)
V-05's Rule 3 adds: "A single unlabeled 'No changes proposed' covering multiple change types fails Rule 3." V-03/V-04 pass C-63 but their Rule 3 is positive-form only — states what to do, not what constitutes violation. The failure-condition sentence makes the rule self-documenting at the point of enforcement, parallel to C-31's disqualification statement on C-25.

**Pattern 3 — Null-case labeling extended to all structured sections** (V-03 and V-04 on C-63)
V-03/V-04 extend the Rule 3 labeling requirement beyond proposal tables to ASSUMPTIONS, SIGNAL INVENTORY, DELTA FINDINGS, and CONFLICT AUDIT. C-63 as written covers change-type tables only. An unlabeled null in DELTA FINDINGS ("none") is ambiguous: skipped, failed extraction, or genuinely null outcome. Extending the labeling requirement to all structured sections makes null outcomes uniformly distinguishable across the entire output.

---

```markdown
---

# Rubric -- topic-plan (v20)

**Skill**: `topic:plan`
**Version**: v20 (promoted from v19 after Round 20 excellence signal extraction)
**Date**: 2026-03-15

---

## Summary

| Tier | Count | Points | Criteria |
|------|-------|--------|----------|
| Essential | 5 | 60 | Read strategy, read signals, identify delta, type proposals, confirm gate |
| Recommended | 3 | 30 | Evidence citations, before/after view, all three change types |
| Aspirational | 59 | 280 | ...+ Table-merge/column-rename prohibitions in C-64 enforcement; Rule 3 explicit failure condition; null-case labeling extended to all structured sections |

**Total possible: 370 pts**

---

## Changes v19 → v20

Three new aspirational criteria extracted from three R20 variation signals.

**C-65 — Table-merge and column-rename prohibitions embedded in symmetric-column enforcement** (`enforcement`)
Extends C-64. C-64 requires symmetric justification columns across all change-type proposal tables — same column name, same schema, same REQUIRED status, same prose-prohibition rule. C-65 closes the gap where a model satisfies C-64's symmetry requirement by dissolving the structural feature that makes it meaningful: merging the two tables into one (so there is no longer a per-table question of symmetry) or renaming the column in one table (so column names technically differ while content is equivalent). Without explicit prohibitions, both escapes are silent — the reviewer must reason about structural intent rather than reading a stated constraint. With "Do not merge the two tables. Do not rename the column in either table" embedded in the Rule 5 schema note, both escapes create a visible structural violation. A C-64 pass whose Rule 5 schema note does not include both prohibitions fails C-65. The merge prohibition and the rename prohibition are required together: a note that prohibits renaming but not merging leaves one escape open. Source: V-05 (schema note reads "Do not merge the two tables. Do not rename the column in either table." — both prohibitions present; V-02, which passes C-64 without these prohibitions, confirms the discriminating gap).

**C-66 — Rule 3 carries an explicit null-declaration failure condition** (`enforcement`)
Extends C-63. C-63 requires type-labeled null-case declarations in change-type tables — each absent change type independently labeled (e.g., "ADDITIONS: none — inertia holds for all candidate additions"). C-66 closes the gap where Rule 3 defines the positive requirement but does not state the exact failure mode, leaving the constraint open to ambiguous interpretation. When a rule declares only what to do, a model that produces a single unlabeled "No changes proposed" near multiple change-type tables can claim compliance — there is no stated disqualification. Adding the failure condition "A single unlabeled 'No changes proposed' covering multiple change types fails Rule 3" to Rule 3 makes the rule self-documenting at the point of enforcement, parallel to C-31's disqualification statement ("a proposal that cannot answer this is a preference, not a decision") which converts the If-unchanged column from a formatting requirement into a reasoning gate. A C-63 pass whose Rule 3 lacks an explicit failure condition fails C-66. The failure condition must be embedded in Rule 3 itself, not in a separate prose note, so it is encountered at the point of constraint definition. Source: V-05 (Rule 3 reads "A single unlabeled 'No changes proposed' covering multiple change types fails Rule 3." — explicit failure mode stated inline; V-03/V-04, which pass C-63 without this addition, confirm the discriminating gap).

**C-67 — Null-case type-labeling extended to all structured sections** (`behavior`)
Extends C-63. C-63 requires type-labeled null-case declarations in change-type proposal tables. C-67 closes the gap where the labeling requirement applies only to the proposals tables but not to other structured sections that can also have null outcomes: ASSUMPTIONS, SIGNAL INVENTORY, DELTA FINDINGS, and CONFLICT AUDIT. When these sections yield no content, an unlabeled null ("none" or blank) is ambiguous — it could mean the section was intentionally skipped, the model failed to extract, or the outcome is genuinely empty. Each cause requires a different reviewer action: skipped sections require investigation, extraction failures require re-run, genuine nulls are acceptable. Type-labeled null declarations make the distinction explicit at the section level without requiring the reviewer to re-read surrounding context. The label form matches the C-63 pattern: section name + "none — inertia holds" or equivalent null affirmation. A C-63 pass that restricts type-labeled null declarations to proposal tables but omits them from ASSUMPTIONS, SIGNAL INVENTORY, DELTA FINDINGS, and CONFLICT AUDIT fails C-67. The extension must be stated in Rule 3 (or an adjacent note) so the requirement is encountered at the same point as the base C-63 constraint. Source: V-03 and V-04 (both extend null-case labeling to ASSUMPTIONS, SIGNAL INVENTORY, DELTA FINDINGS, CONFLICT AUDIT — V-01/V-02, which pass C-63 without this extension, confirm the discriminating gap; V-05 includes the extension as well).

**Updated totals**: 67 criteria, 370 pts | Formula: `(essential/5×60) + (recommended/3×30) + (aspirational/59×280)` | Golden threshold: **220**

---

## Design Rationale

- **C-01/C-02** separated because fabricated signals and strategy-ignoring are independent failure modes.
- **C-03** is the core correctness gate: inventory != delta.
- **C-04** enforces the three-type mandate at output time.
- **C-05** is essential because auto-applying is destructive.
- **C-09/C-10** require reasoning beyond the immediate diff — ceiling behaviors.
- **C-11–C-15** are prompt-engineering craft extracted from Round 1: they make the essential/recommended criteria *structurally self-enforcing* rather than merely instructed.
- **C-16** closes the gap in C-06: single-hop citation (proposal → artifact) leaves the causal reasoning implicit; the two-level chain (proposal → delta → artifact) makes it auditable without re-reading the delta section.
- **C-17** is the null-case complement to C-10: requires an explicit declaration when no conflicts exist — parallel to C-12's no-change rows for proposals.
- **C-18** mandates "Strategy assumed [X] / Signal revealed [Y]" per finding — makes the assumption-vs-signal distinction self-enforcing and fabricated deltas visible.
- **C-19/C-20** address navigability: the diff and proposals tables are linked by pointer columns so the reviewer can reach any evidence in two hops from any starting point.
- **C-21/C-22/C-23** address constraint explicitness: the enforcement layer between "the instruction is present" and "the model cannot deviate from it."
- **C-24** extends C-01: stated field extraction is necessary but not sufficient — unstated assumptions are the most likely delta candidates.
- **C-25** extends C-20: a Delta Finding column names what changed; an "If unchanged" column names what fails to improve if the change is deferred — cost framing forces causal depth.
- **C-26** extends C-21: adjacent declarations prevent per-table omissions; an upfront schema declaration before file reading primes the structural contract before any content is encountered.
- **C-27** extends C-22: a single anti-pattern checkpoint at the delta step is verifiable at one point; cascading schema-commitment checkpoints to proposals and diff create three independent verification points across the output.
- **C-28** extends C-24: extraction instructed without a named role is easy to execute shallowly; a named role and enumerated scan dimensions scope the model's assumption-hunt to a specific cognitive register and prevent both scope-drift and dimension-skipping.
- **C-29** extends C-24 in the reverse direction: C-24 is forward (strategy → assumptions extracted); C-29 is backward (signals → assumptions back-filled). An assumption that was extracted but never checked against signal evidence is inert; the back-fill column forces every assumption to be signal-adjudicated.
- **C-30** extends C-29 by completing the assumption table's forward arc: once a signal has confirmed or contradicted an assumption (C-29), the table must also carry a relevance column and a delta-candidate designation column. Together, C-29 and C-30 make the assumption table a complete two-way bridge between Step 1 and Step 3.
- **C-31** extends C-25: an "If unchanged" column introduced with an explicit disqualification statement ("a proposal that cannot answer this is a preference, not a decision") becomes a reasoning gate rather than a formatting requirement.
- **C-32** extends C-25 and C-31: the reversibility taxonomy column — with three enumerated values (Reversible at same cost / Gets harder / Becomes impossible) — adds temporal precision to the inertia cost argument.
- **C-33** extends C-26 and C-30: the upfront schema block must include the complete assumption table column set before Step 1 — not deferred to the extraction step.
- **C-34** extends C-26 and C-32: a schema declaration is falsifiable only when it lists valid values explicitly and appends a prose-prohibition rule.
- **C-35** extends C-33: each of the five assumption-table columns must carry content that cannot be derived from the row key or adjacent columns.
- **C-36** extends C-34 and C-27: a named "COLUMN CONTRACT" block preceding the schema consolidates enumerated-column constraints; commitment checkpoints cite rule IDs rather than re-inlining constraint text.
- **C-37** extends C-35: the independence requirement expressed as a named, operationalized test (e.g., "Can I fill this cell without reading the source document?") with explicit PASS/FAIL examples.
- **C-38** extends C-37: pass and fail examples carry equal specificity — both concrete quoted values, both labeled.
- **C-39–C-58** (inherited from v14–v17 rounds): Pre-signal Defense Register, SIGNAL READ-LOCK, Defender Challenge Table, calibration check with forced-abstention provision, anti-pattern checkpoint with per-step recurrence, and cascading schema-commitment checkpoints. Each closes a specific escape route against compliant-looking outputs that leave one enforcement layer absent.
- **C-59** requires a named verbatim block (`[INERTIA-GATE]`) defined in the preamble and reproduced verbatim at each inertia decision gate — the preamble block definition must enumerate the sites where reproduction is required.
- **C-60/C-61** (inherited from v18): per-step recurrence of the SIGNAL READ-LOCK and Defender Challenge Table with step-specific headings, closing the gap where a single upfront declaration covers steps that follow but are not individually gated.
- **C-62** extends C-59: the `[INERTIA-GATE]` block definition must include an explicit numbered enumeration of all reproduction sites ("This block is reproduced verbatim at Steps 3, 4b, 6, and 7. Its presence is required at each site."). Without the manifest, C-59's reproduction contract is unverifiable at definition time. Source: R19/V-01.
- **C-63** extends C-40: type-labeled null-case declarations — each absent change type independently labeled with a type label and "inertia holds" affirmation. A C-40 pass whose null declarations lack change-type labels when multiple change-type tables are present fails C-63. Source: R19/V-01.
- **C-64** extends C-56: symmetric justification columns across all change-type proposal tables — same column name, schema, REQUIRED status, and prose-prohibition rule in every table. C-56's column can be selectively present; C-64 requires it to be universally present. Source: R19/V-01 and R19/V-04.
- **C-65** extends C-64: table-merge and column-rename prohibitions embedded in Rule 5's schema note. C-64 requires column symmetry; C-65 closes the two structural escapes (merging tables, renaming columns) that let a model dissolve the feature while claiming compliance. Both prohibitions must appear together in the Rule 5 schema note. Source: R20/V-05.
- **C-66** extends C-63: Rule 3 must carry an explicit failure condition ("A single unlabeled 'No changes proposed' covering multiple change types fails Rule 3") inline in the rule, not in a separate note. Converts the labeling requirement from positive-form to self-documenting constraint, parallel to C-31's disqualification statement. Source: R20/V-05.
- **C-67** extends C-63: null-case type-labeling extended to all structured sections (ASSUMPTIONS, SIGNAL INVENTORY, DELTA FINDINGS, CONFLICT AUDIT), not only proposal tables. An unlabeled null in any structured section is ambiguous — skipped, extraction failure, or genuinely empty — each requiring different reviewer action. The extension must be stated in Rule 3 or an adjacent note, co-located with the base C-63 requirement. Source: R20/V-03 and R20/V-04.
```
