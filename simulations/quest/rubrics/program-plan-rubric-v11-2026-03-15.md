All edits are correct. Here is the complete v11 rubric output:

---

# program-plan Rubric — v11

Evaluates a `program:plan` prompt against Signal's plugin contract and evidence-quality bar.
30 aspirational criteria, 4 essential, 3 recommended. Total max: **240 pts**.

*(Essential through C-35 are unchanged from v10. New criteria below.)*

---

### C-36 — BAD PLAN Header Label Coverage Accuracy

- **Weight**: aspirational
- **Category**: depth
- **Text**: The BAD PLAN block's header comment accurately describes the criterion coverage scope of the block below it. When the block contains criterion tags for all 7 criteria — essential (C-01 through C-04) AND recommended (C-05 through C-07) — the header must not restrict its claimed scope to essential-tier only. A header reading "essential violations" or "essential-tier failures only" is accurate when the block body contains only essential tags; it becomes inaccurate when the block body also carries recommended-tier tags, creating a label-content mismatch that may cause a model to believe recommended criteria are not illustrated in the BAD PLAN. Evidence from R10: V-01 passes C-31 (all 7 criterion tags present in the BAD PLAN block) while carrying a header labeled "essential-tier violations only" — the first variate to build a complete-criterion BAD PLAN block while advertising narrower coverage than the block delivers.
- **Pass condition**: The BAD PLAN block's header comment does not falsely restrict the claimed coverage tier. If C-31 passes (all 7 criteria are tagged in the block), the header must not claim "essential violations only" or equivalent. Headers claiming full coverage or making no scope claim pass. Prerequisite: C-31.
- **Partial credit**: Not applicable — label accuracy is binary.

---

### C-37 — BAD PLAN Stage Name Field-Level Annotation

- **Weight**: aspirational
- **Category**: depth
- **Text**: Every wrong-format stage `name:` value in the BAD PLAN block that violates C-06 carries `# WRONG C-06` as an inline comment at the `name:` field itself — not at an adjacent gate field, not in a header comment, and not only via a tag at the skills line. C-22 requires C-06 coverage somewhere across error artifacts; C-31 requires C-06 to be tagged somewhere within the BAD PLAN block; C-37 requires the C-06 tag to be co-located with the violating `name:` field specifically. Evidence from R10: V-03's BAD PLAN uses non-namespace-label stage names that violate C-06, but neither name carries `# WRONG C-06` at the field — the violation pattern is physically untaught at the `name:` position. V-01's BAD PLAN tags namespace-label stage names with `# WRONG C-06` at the `name:` fields, establishing field-level annotation as an achievable design choice.
- **Pass condition**: Every stage `name:` value in the BAD PLAN block that violates C-06 carries `# WRONG C-06` inline at the `name:` field itself. C-22 and C-31 must both pass. Prerequisites: C-22, C-31.
- **Partial credit**: Field-level C-06 annotation is present on at least half the wrong-format `name:` fields but not all.

---

**Scoring**: 28 → 30 aspirational criteria, 140 → 150 pts, total **240 pts**. Formula: `aspirational_pass/30 * 150`. Golden threshold (>= 80) unchanged.

**Version history**: v10 added C-34/C-35 from R9; v11 adds C-36/C-37 from R10.

File written to `simulations/quest/rubrics/program-plan-rubric-v11-2026-03-16.md`.

---

**Two new criteria extracted from R10:**

| Criterion | Source | Gap closed |
|-----------|--------|-----------|
| **C-36 BAD PLAN Header Label Coverage Accuracy** | V-01 anomaly: C-31 PASS but header claims "essential-only" | Label-content mismatch after coverage expands to all 7 criteria |
| **C-37 BAD PLAN Stage Name Field-Level Annotation** | V-03 anomaly: wrong stage names untagged at `name:` field | C-06 tags present in block (C-31) but absent at the violating field position itself |

Both follow the co-location discipline established by C-26 (criterion tag at structural `gate_fail:` field) and C-34 (compound annotation at the field, not nearby). C-36 closes label-currency decay; C-37 closes field-position gap for stage name teaching.
