Reading the scorecard carefully before writing.

The key excellence signals from Round 3:

1. **C-15 was listed in the v3 structure table but never defined** — the scorecard explicitly notes this omission. Round 3 points directly at what it should be: both V-01 and V-02 received C-07 PARTIAL for the same structural reason — "mechanism is a prohibition, not a scoreable criterion" / "input-analysis question, not a scoreable criterion." The pattern: a prompt-level specificity mechanism does not produce a specificity criterion in the output rubric.

2. **New C-16 signal — unanchored field declarations**: V-02's C-01 PARTIAL ("skill identity declaration is unanchored") and C-08 FAIL ("no frontmatter block defined") share a root cause: required fields were stated as obligations but had no structural home in the output schema. V-01 passed both because frontmatter was part of its output template.

These are the two new criteria. Here is the complete v4 rubric:

---

```markdown
---
skill: quest-rubric
skill_target: rubric produced by the quest-rubric skill for any target skill
date: 2026-03-16
version: 4
---

# Quest Rubric — Self-Assessment Rubric

## Structure Changes

| Tier | v1 | v2 | v3 | v4 |
|------|----|----|----|----|
| Essential | 5 | 5 | 5 (unchanged) | 5 (unchanged) |
| Recommended | 3 | 3 | 3 (unchanged) | 3 (unchanged) |
| Aspirational | 2 | 5 | 7 (+C-14, C-15†) | **8** (C-15 defined, +C-16) |

† C-15 was listed in v3 structure table but not defined in rubric body. Defined here.

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

**C-15 — Specificity criterion appears in the output rubric**: The produced rubric
must contain an explicit, named specificity criterion in its criterion list. A
prompt-level prohibition against generic criteria, or an input-analysis question
("what distinguishes a specific output from a generic template?"), does not
substitute — neither mechanism creates a scoreable criterion in the output. The
criterion must be present in the rubric body and must state what "specific" means
for the target skill. Root cause of C-07 PARTIAL in V-01 (prohibition mechanism)
and V-02 (analysis-question mechanism) in Round 3.

**C-16 — Output schema anchors required header fields**: The rubric's output schema
includes a frontmatter block as a structurally required section. Without a
structural anchor, C-01 (skill identity) and C-08 (version/date) are stated
obligations that can silently drop when the output schema changes format. A stated
requirement without a structural home is not enforced. Root cause of C-01 PARTIAL
and C-08 FAIL in V-02 (table-first schema with no frontmatter block) in Round 3.
```

---

**What changed and why:**

| Criterion | Change | Source signal |
|-----------|--------|---------------|
| C-15 | Defined (was a stub in v3) | Both V-01 and V-02 received C-07 PARTIAL; both failed for the same structural reason: specificity mechanism was not a criterion in the output |
| C-16 | New | V-02 C-01 PARTIAL + C-08 FAIL share one root cause — no frontmatter block in the output schema meant required fields had no structural home |
| Structure table | 7 → 8 aspirational | Reflects C-15 definition + C-16 addition |
