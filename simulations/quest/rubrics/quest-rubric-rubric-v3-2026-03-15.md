```markdown
---
skill: quest-rubric
skill_target: rubric produced by the quest-rubric skill for any target skill
date: 2026-03-15
version: 3
---

# Quest Rubric — Self-Assessment Rubric

## Structure Changes

| Tier | v1 | v2 | v3 |
|------|----|----|-----|
| Essential | 5 | 5 | 5 (unchanged) |
| Recommended | 3 | 3 | 3 (unchanged) |
| Aspirational | 2 | 5 | **7** (+C-14, C-15) |

---

## Essential Criteria (must all pass)

**C-01 — Skill identity declared**: The rubric names the target skill in the header.

**C-02 — Criteria are testable**: Every criterion can be evaluated pass/fail/partial
without subjective interpretation of intent.

**C-03 — Pass condition is enforced**: Each criterion specifies what constitutes a
passing artifact, not just what a good artifact looks like. Advisory language ("should",
"ideally") is insufficient; pass language ("must", "required") is required.

**C-04 — Scoring formula is explicit**: The rubric states the exact formula used to
compute the final score, including denominator.

**C-05 — Tier structure present**: Criteria are grouped into Essential, Recommended,
and Aspirational tiers.

---

## Recommended Criteria

**C-06 — Failure modes cataloged**: The rubric lists known failure modes of the target
skill that the criteria are designed to catch.

**C-07 — Specificity test included**: At least one criterion tests that output is
specific to the input (not generic boilerplate). The criterion must state what
"specific" means for this skill — a vague specificity mention does not pass.

**C-08 — Version and date stamped**: The rubric carries a version number and date so
score comparisons across rounds are unambiguous.

---

## Aspirational Criteria

**C-09 — Coverage of all output sections**: The rubric contains at least one criterion
per named output section of the target skill, so no section can silently regress.

**C-10 — Scoring formula includes partial credit**: The formula distinguishes PARTIAL
from PASS for recommended and aspirational tiers rather than collapsing them to
binary.

**C-11 — External enforcement gate**: The skill uses a named review role, rejection
step, or prohibition checklist to enforce pass-condition quality — not advisory
language. Root cause of C-03 FAIL in V-02 and C-03 PARTIAL in V-03.

**C-12 — Failure-first derivation**: Before writing criteria, the skill catalogs
concrete failure modes of the target skill. Criteria derived from named failures
cannot be generic. This is the only pattern that fully solved C-07 (V-03, Phase 1).

**C-13 — Generic-vs-specific foil pair**: A concrete before/after contrast example is
present near C-07, making the specificity test a lookup rather than a judgment call.
Absent in every variant that received C-07 PARTIAL.

**C-14 — Explicit category enumeration in field rules**: Field-level rules use a
closed enumeration (e.g., `one of: correctness / depth / format / coverage /
behavior`) rather than open prose. This is the only pattern that closes the
enumeration at prompt-authoring time and converts C-07 from PARTIAL to PASS — open
prose leaves the enumeration open at evaluation time, which allows drift.

**C-15 — F-NN failure column present in criteria table**: Each criterion row includes
an `F-NN` column that references the named failure mode it was derived from. An empty
cell is a structural failure detectable without reading content, making C-12
(failure-first derivation) a column-presence check rather than a prose-quality
judgment.

---

## Scoring Formula (v3)

```
essential_score     = essential_pass / 5 * 100        (binary — any fail = 0)
recommended_score   = recommended_pass / 3 * 100
aspirational_score  = aspirational_pass / 7 * 10

final_score = essential_score * 0.5
            + recommended_score * 0.3
            + aspirational_score * 0.2
```

A rubric with any Essential FAIL receives a final score of 0 regardless of other
tiers.

---

## Common Failure Modes

| ID | Failure | Caught by |
|----|---------|-----------|
| F-01 | Pass condition uses advisory language ("should") | C-03 |
| F-02 | Specificity criterion is itself generic | C-07, C-13 |
| F-03 | Criteria not traceable to a named failure mode | C-12, C-15 |
| F-04 | Category field left open — evaluator must invent values | C-14 |
| F-05 | F-NN column absent — failure-first derivation unverifiable | C-15 |
```
