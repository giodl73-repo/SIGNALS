Reading the v4 rubric body and the Round 4 scorecard carefully before writing.

The v4 rubric body shown ends at C-11, but the scorecard cross-reference table runs through C-16 — I need to reconstruct C-12 through C-16 from scorecard evidence before adding C-17 and C-18.

From the scorecard:
- **C-12**: "Both sequence failure modes before criteria" → failure modes are ordered before the criteria they inform
- **C-13**: "CONVERSION-MAP three-way contrast; V-01 has no foil pair" → at least one criterion includes a foil pair distinguishing pass from fail
- **C-14**: "closed enumeration absent in both" → at least one dimension uses a closed category list
- **C-15**: "V-02's axis; V-01 does not convert specificity prohibitions" → specificity prohibitions converted to output-testable properties
- **C-16**: "V-01's axis; V-02 has no SCHEMA block" → required fields have a declared structural home

New criteria from E-1 and E-2:
- **C-17** (E-1): SCHEMA BLOCK is *positionally first* — not just present, but the first section, converting the anchoring check from audit to structural pre-condition
- **C-18** (E-2): The specificity conversion uses a boolean classification mechanism with a completion gate (the CONVERSION-MAP pattern)

Structure table: Aspirational grows from 8 → 10.

---

```markdown
---
skill: quest-rubric
skill_target: rubric produced by the quest-rubric skill for any target skill
date: 2026-03-16
version: 5
---

# Quest Rubric — Self-Assessment Rubric

## Structure Changes

| Tier | v1 | v2 | v3 | v4 | v5 |
|------|----|----|----|----|-----|
| Essential | 5 | 5 | 5 (unchanged) | 5 (unchanged) | 5 (unchanged) |
| Recommended | 3 | 3 | 3 (unchanged) | 3 (unchanged) | 3 (unchanged) |
| Aspirational | 2 | 5 | 7 (+C-14, C-15†) | 8 (C-15 defined, +C-16) | **10** (+C-17, C-18) |

† C-15 was listed in v3 structure table but not defined in rubric body. Defined in v4.

C-17: SCHEMA BLOCK positional enforcement (E-1, Round 4). C-18: CONVERSION-MAP
classification gate for specificity (E-2, Round 4). Both aspirational — V-04 predicted
to pass C-17 and C-18 by combining SCHEMA BLOCK + CONVERSION-MAP.

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

**C-12 — Failure modes sequenced before criteria**: The failure mode catalog (C-06)
appears in the rubric before the criteria it informs, so reviewers encounter the
failure pattern before evaluating the criterion that catches it.

**C-13 — Foil pair present**: At least one criterion includes a foil pair — a concrete
example of what passes and a concrete example of what fails — to disambiguate
borderline cases without subjective judgment.

**C-14 — Closed category enumeration**: At least one evaluation dimension uses a
closed enumeration of named categories rather than an open-ended description. An
open list or "e.g." construction does not pass.

**C-15 — Specificity prohibitions converted to output-testable criteria**: Every
specificity element in the rubric is a testable property of the output artifact, not a
prohibition on the prompt or an input-analysis question. A mechanism is required that
reclassifies each element until it satisfies "testable property of the output."
A vague specificity mention or a prohibition list does not pass.

**C-16 — Required fields have a declared structural home**: All fields required in the
output artifact are declared in an explicit output schema block, not stated as
free-floating obligations. Fields declared without a structural home are unanchored
and cause cascading failures across C-01, C-08, and this criterion. Root cause of
C-01 PARTIAL, C-08 FAIL, and C-16 FAIL in V-02.

**C-17 — SCHEMA BLOCK is the first section of the artifact**: The output schema
declaration (SCHEMA BLOCK or equivalent) must appear as the *first* section of the
rubric artifact, before any failure modes, criteria, or scoring formula. Positional
enforcement converts unanchored field detection from a post-hoc audit into a
structural pre-condition: absence of a required field in the SCHEMA is a structural
error visible before Phase 2 begins, making the C-16 failure impossible rather than
detectable. A schema block present but not first does not pass. Root cause of E-1,
Round 4.

**C-18 — Specificity conversion uses a boolean classification mechanism with a
completion gate**: The rubric's specificity conversion mechanism (C-15) must classify
each specificity element using a closed boolean set — at minimum distinguishing
`is_prohibition`, `is_input_analysis`, and `conversion_complete` — and must include a
`DO NOT proceed` gate that blocks the next phase until all elements reach
`conversion_complete`. A prohibition list, a narrative instruction, or a single
boolean does not pass. Across all four rounds, the boolean triplet with gate is the
only pattern that achieves C-15 PASS. Root cause of E-2, Round 4.

---

## Scoring Formula

```
essential_score   = (C-01..C-05 passes) / 5
recommended_score = (C-06..C-08 passes + 0.5 * partials) / 3
aspirational_score = (C-09..C-18 passes + 0.5 * partials) / 10

composite = (essential_score * 50) + (recommended_score * 30) + (aspirational_score * 20)
```

A rubric with any Essential FAIL scores 0 regardless of composite.

---

## Known Failure Modes

**FM-01 — Advisory drift**: Criteria use "should" or "ideally" instead of "must" or
"required." Caught by C-03.

**FM-02 — Unanchored field declarations**: Required output fields stated as
obligations without a structural home in the output schema. Cascades into C-01, C-08,
C-16, C-17 failures. Caught by C-16 and eliminated by C-17.

**FM-03 — Specificity as prohibition**: Specificity criteria expressed as prompt-level
prohibitions or input-analysis questions rather than testable output properties.
Passes C-07 superficially but fails C-15. Caught by C-15 and C-18.

**FM-04 — Binary scoring formula**: Pass/fail only, no partial credit tier. Universal
miss in all rounds to date. Caught by C-10.

**FM-05 — Open category lists**: Evaluation dimensions that use "e.g." or open
enumeration rather than a closed named set, allowing silent omissions. Caught by
C-14.

**FM-06 — Schema present but not first**: An output schema exists but appears after
criteria or scoring sections, preserving the audit problem that C-17 is designed to
eliminate. Passes C-16 but fails C-17.
```
