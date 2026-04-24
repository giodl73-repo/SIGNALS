---
skill: quest-rubric
skill_target: draft-brainstorm
date: 2026-03-15
version: 1
---

# Rubric: draft-brainstorm

Scoring rubric for the `draft-brainstorm` skill. This skill generates a ranked idea pool for a topic — 20-40 candidates, grouped by category, top-5 marked, inertia check included, and an AMEND section with 3 pool-shift adjustments.

## Composite Score Formula

```
composite = (essential_pass/N_essential * 60)
          + (recommended_pass/N_recommended * 30)
          + (aspirational_pass/N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60%)

All must pass. If any essential fails, the output is not usable regardless of composite score.

### C-01 — Volume
- **Category**: correctness
- **Weight**: essential
- **Text**: The output contains between 20 and 40 distinct idea candidates (inclusive).
- **Pass condition**: Count the numbered or bulleted ideas. Pass if 20 <= count <= 40. Fail if fewer than 20 (insufficient pool) or more than 40 (unfocused dump).

### C-02 — Idea Anatomy
- **Category**: correctness
- **Weight**: essential
- **Text**: Every idea includes all four required fields: name, one-line pitch, category, and rationale.
- **Pass condition**: Sample at least 5 ideas (including first, last, and middle). Every sampled idea has all four fields present and non-empty. If any sampled idea is missing a field, fail. If all four fields are consistently present, pass.

### C-03 — Top-5 Marker
- **Category**: correctness
- **Weight**: essential
- **Text**: Exactly 5 ideas are marked with `**` to indicate immediate viability.
- **Pass condition**: Count ideas marked with `**` (double asterisk, typically as a bold marker or inline `**name**` or `**` suffix). Pass if exactly 5. Fail if 0, fewer than 5, or more than 5.

### C-04 — Inertia Check
- **Category**: coverage
- **Weight**: essential
- **Text**: A "do nothing" candidate is present that describes the status quo path.
- **Pass condition**: At least one idea explicitly represents the inertia/status-quo option (e.g., named "Do Nothing", "Status Quo", "No Change", or equivalent). The rationale must describe what the current state looks like, not just say "do nothing." Pass if present with rationale; fail if absent or present but unnamed/undescribed.

### C-05 — AMEND Section
- **Category**: correctness
- **Weight**: essential
- **Text**: The output contains an AMEND section with exactly 3 specific adjustments that would shift the pool.
- **Pass condition**: A labeled AMEND section exists (heading, label, or prefix "AMEND:"). It contains exactly 3 adjustment items. Each adjustment names a direction of change (e.g., "more ambitious," "conservative," "different audience") AND states what would change in the pool. Pass if all three are present and directional; fail if section is absent, has fewer than 3, or adjustments are vague.

---

## Recommended Criteria (weight: 30%)

Output is better with these. Missing one lowers the score but does not block golden.

### C-06 — Category Grouping
- **Category**: format
- **Weight**: recommended
- **Text**: Ideas are organized under explicit category headers, not presented as a flat list with category as a field only.
- **Pass condition**: The document uses visible grouping (e.g., markdown headers `## Category Name`, bold category labels, or clearly separated sections) so a reader can scan by category. A flat numbered list where category is only a field attribute fails. Pass if at least 3 distinct category groups are visually separated.

### C-07 — Rationale Specificity
- **Category**: depth
- **Weight**: recommended
- **Text**: Rationales are specific to the topic at hand, not generic reasoning that could apply to any brainstorm.
- **Pass condition**: Sample 5 rationales. Each must reference the topic by name, a specific user need, constraint, or opportunity tied to the topic. Generic rationales like "this is a good idea because it provides value" fail. Pass if 4 of 5 sampled rationales are topic-specific.

### C-08 — Category Diversity
- **Category**: coverage
- **Weight**: recommended
- **Text**: Ideas span at least 4 meaningfully distinct categories that represent different approaches or dimensions.
- **Pass condition**: Count distinct category labels across all ideas. Pass if >= 4 and categories represent genuinely different angles (not "Approach A" and "Approach A variant"). Fail if fewer than 4 or if categories are superficially different but cover the same dimension.

---

## Aspirational Criteria (weight: 10%)

Raise the bar once essential and recommended are stable.

### C-09 — AMEND Actionability
- **Category**: depth
- **Weight**: aspirational
- **Text**: Each AMEND adjustment is specific enough that a reader could immediately re-run the brainstorm in that direction — naming what changes and why it produces a meaningfully different pool.
- **Pass condition**: Each of the 3 AMEND items: (a) names a concrete shift axis, (b) explains what kind of ideas would appear or disappear, and (c) would produce a noticeably different ranked pool if applied. Pass if all 3 meet all three sub-conditions. Fail if any item is a generic restatement (e.g., "be more creative").

### C-10 — Top-5 Defensibility
- **Category**: depth
- **Weight**: aspirational
- **Text**: The 5 ideas marked ** are meaningfully differentiated from the rest — they are the strongest candidates for immediate viability, and the selection is defensible given the pool.
- **Pass condition**: The 5 marked ideas are neither the first 5 listed (suggesting no real selection occurred) nor obviously inferior to unmarked peers. If the rationale for any marked idea is weaker than an unmarked idea in the same category, fail. Pass if marked ideas collectively represent the pool's most actionable, lowest-barrier, or highest-confidence candidates.

---

## Scoring Summary

| ID   | Criterion              | Weight        | Category    |
|------|------------------------|---------------|-------------|
| C-01 | Volume (20-40)         | essential     | correctness |
| C-02 | Idea anatomy (4 fields)| essential     | correctness |
| C-03 | Top-5 marker (**)      | essential     | correctness |
| C-04 | Inertia check          | essential     | coverage    |
| C-05 | AMEND section (3 items)| essential     | correctness |
| C-06 | Category grouping      | recommended   | format      |
| C-07 | Rationale specificity  | recommended   | depth       |
| C-08 | Category diversity (4+)| recommended   | coverage    |
| C-09 | AMEND actionability    | aspirational  | depth       |
| C-10 | Top-5 defensibility    | aspirational  | depth       |

**Example scores:**

| Scenario | C-01 | C-02 | C-03 | C-04 | C-05 | C-06 | C-07 | C-08 | C-09 | C-10 | Composite | Golden? |
|----------|------|------|------|------|------|------|------|------|------|------|-----------|---------|
| All pass | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | 100 | Yes |
| Miss C-04 | Y | Y | Y | N | Y | Y | Y | Y | Y | Y | 48 | No (essential fail) |
| Essential only | Y | Y | Y | Y | Y | N | N | N | N | N | 60 | No (composite < 80) |
| Essential + rec | Y | Y | Y | Y | Y | Y | Y | Y | N | N | 90 | Yes |
| Essential + 1 rec | Y | Y | Y | Y | Y | Y | N | N | N | N | 70 | No (composite < 80) |
