---
skill: quest-rubric
skill_target: quest-rubric
date: 2026-03-15
version: 1
---

# Scoring Rubric: quest-rubric

## Purpose

Evaluate outputs produced by the `quest-rubric` skill. A rubric is the objective function
for `quest-golden` — it must be complete, testable, and targeted. A rubric that is vague,
structurally incomplete, or untethered to the target skill cannot drive meaningful evaluation.

---

## Criteria

### C-01 — Structural completeness of all criteria
- **Weight**: essential
- **Category**: format
- **Text**: Every criterion in the rubric contains all five required fields: ID (C-NN format),
  text description, weight (essential/recommended/aspirational), category
  (correctness/depth/format/coverage/behavior), and pass condition.
- **Pass condition**: No criterion is missing any of the five fields. A criterion with a blank,
  null, or "TBD" field fails this check.

---

### C-02 — Essential tier covers non-negotiable behaviors
- **Weight**: essential
- **Category**: correctness
- **Text**: The rubric contains 3–5 essential criteria. Each essential criterion targets a
  behavior whose absence would make the target skill's output useless or untrustworthy —
  not merely suboptimal. Essential criteria should be necessary conditions, not desirable ones.
- **Pass condition**: Count of essential criteria is in [3, 5]. Each essential criterion
  describes a failure mode that produces a non-functional or misleading artifact when violated.

---

### C-03 — Pass conditions are objectively testable
- **Weight**: essential
- **Category**: correctness
- **Text**: Every pass condition can be evaluated by a third party without subjective judgment.
  Conditions must describe what to check, what to count, or what to find — not characterize
  quality in vague terms ("is clear", "seems appropriate", "looks good").
- **Pass condition**: No pass condition uses purely qualitative language without an anchoring
  observable. Accepted anchors: count thresholds, presence/absence of named fields, structural
  patterns, explicit strings or enumerations. Reject: "is clear", "is well-written",
  "adequately covers".

---

### C-04 — Composite scoring formula and golden threshold present
- **Weight**: essential
- **Category**: format
- **Text**: The rubric states the composite scoring formula (essential/recommended/aspirational
  contribution weights) and the golden threshold condition (all essential pass + composite >= N).
  Without these, the rubric cannot function as an objective function for quest-golden.
- **Pass condition**: Document contains a formula of the form
  `(essential_pass/N * W1) + (recommended_pass/N * W2) + (aspirational_pass/N * W3)` and a
  golden threshold statement. Weights W1+W2+W3 = 100.

---

### C-05 — Criteria are targeted to the specific skill
- **Weight**: essential
- **Category**: correctness
- **Text**: The criteria reflect the actual outputs and behaviors of the named `skill_target`,
  not generic writing quality or formatting conventions that apply to any document. A rubric
  for `quest-rubric` must evaluate rubric-specific properties; a rubric for `draft-pitch`
  must evaluate pitch-specific properties.
- **Pass condition**: At least 3 of the essential criteria can only apply to the named
  `skill_target`. Generic criteria ("has a title", "uses markdown") do not count toward this
  threshold unless they are genuinely non-negotiable for the skill's function.

---

### C-06 — Weight tier distribution is balanced
- **Weight**: recommended
- **Category**: coverage
- **Text**: The rubric includes all three tiers — essential, recommended, aspirational — in
  proportions consistent with the spec: 3–5 essential, 2–3 recommended, 1–2 aspirational.
  Rubrics with only essential criteria cannot distinguish between passing outputs. Rubrics
  with too many aspirational criteria inflate scores without grounding.
- **Pass condition**: Count of recommended criteria in [2, 3]. Count of aspirational criteria
  in [1, 2]. All three tiers present.

---

### C-07 — Category diversity across criteria
- **Weight**: recommended
- **Category**: coverage
- **Text**: The criteria span at least 3 distinct categories from the allowed set
  (correctness, depth, format, coverage, behavior). Rubrics that cluster all criteria in
  one category (e.g., all format) miss failure modes that live in other dimensions.
- **Pass condition**: Count of distinct categories used across all criteria >= 3.

---

### C-08 — Recommended criteria address output quality, not just presence
- **Weight**: recommended
- **Category**: depth
- **Text**: Recommended criteria evaluate qualitative properties of the output — not just
  whether a field exists, but whether it serves its purpose. For example, not just "pass
  conditions are present" but "pass conditions are testable." They should describe the
  difference between a passing output and a good output.
- **Pass condition**: Each recommended criterion's pass condition tests a quality property
  (e.g., degree, precision, specificity) rather than pure presence/absence. A recommended
  criterion whose pass condition is "field exists" fails this check.

---

### C-09 — Aspirational criteria distinguish excellent from merely passing
- **Weight**: aspirational
- **Category**: depth
- **Text**: Aspirational criteria capture the patterns that separate excellent rubric outputs
  from rubrics that merely pass. They should be achievable but not expected on first pass —
  their value is raising the bar once essential and recommended are stable. Good aspirational
  criteria often describe self-consistency, internal rationale, or predictive power.
- **Pass condition**: Each aspirational criterion describes a property that: (a) goes beyond
  what essential/recommended require, and (b) would meaningfully improve the rubric's utility
  as an objective function if present. A criterion that is merely a rephrasing of an essential
  criterion fails.

---

### C-10 — Frontmatter is complete and correct
- **Weight**: aspirational
- **Category**: format
- **Text**: The rubric's YAML frontmatter contains all four required fields (`skill`,
  `skill_target`, `date`, `version`) with valid values. `date` matches the current session
  date. `version` is a positive integer. `skill` and `skill_target` identify the rubric's
  scope unambiguously.
- **Pass condition**: All four frontmatter fields present. `date` is a valid ISO-8601 date.
  `version` >= 1. `skill` equals the rubric generator skill name. `skill_target` equals the
  skill being evaluated.

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60 pts total |
| Recommended | C-06, C-07, C-08 | 30 pts total |
| Aspirational | C-09, C-10 | 10 pts total |
