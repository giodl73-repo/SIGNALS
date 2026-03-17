---
skill: quest-rubric
skill_target: rubric produced by the quest-rubric skill for any target skill
date: 2026-03-15
version: 2
---

# Quest Rubric — Rubric for quest-rubric

Evaluates whether a rubric produced by the `quest-rubric` skill is structurally correct,
internally consistent, and actually constraining — not just syntactically complete.

---

## Criteria

### Essential (60 pts total — all must pass)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-01 | Every criterion row contains all five required fields | essential | format | Every criterion in the output has all five fields: ID, text, weight, category, pass condition. A criterion missing any field fails C-01 for the entire rubric. A field present but empty (blank cell, dash) also fails. |
| C-02 | Essential criterion count is exactly 3–5 | essential | correctness | The output contains between 3 and 5 essential criteria, inclusive. Fewer than 3 means the rubric under-constrains the skill. More than 5 means the author confused essential with recommended. |
| C-03 | Pass conditions are unambiguous and self-contained | essential | correctness | Each pass condition can be evaluated by a scorer reading only the rubric and the skill output — no external spec, no judgment calls, no hedging language. Two-scorer test: if two independent scorers read the pass condition and disagree on a clear case, the condition fails C-03. Words like "should", "generally", "typically", "usually", "appropriate", "adequate", or "reasonable" in a pass condition are automatic fails. |
| C-04 | Scoring formula is present and mathematically correct | essential | correctness | The output contains the composite scoring formula: (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10) where N is the actual count of criteria in each tier. Each denominator must match the actual criterion count in that tier. Missing formula or wrong denominators is a hard fail. |
| C-05 | Golden threshold states both conditions | essential | correctness | The output contains an explicit statement of the golden threshold: all essential criteria must pass AND composite >= 80. Omitting either condition is a hard fail. Stating only "score >= 80" without the all-essential gate fails. Stating only "all essential pass" without the composite floor fails. |

### Recommended (30 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-06 | All three weight tiers are present with correct counts | recommended | coverage | The output contains all three tiers: 3–5 essential, 2–3 recommended, 1–2 aspirational. Tier counts in the formula denominators must match the actual criterion rows. Missing a tier entirely (e.g., no aspirational) fails. |
| C-07 | Essential criteria are skill-specific, not generic presence checks | recommended | depth | At least 3 of the essential criteria are specific to the target skill's unique outputs — not checks that would pass any skill rubric. Foil: "output contains a table" is generic; "table has one row per component with an explicit GREEN/YELLOW/RED label" is specific. A rubric whose essential set passes the foil test (all criteria survive substituting a different skill name) fails C-07. |
| C-08 | Category variety across essential criteria | recommended | coverage | Essential criteria span at least 2 distinct categories (correctness, depth, format, coverage, behavior). An all-correctness or all-format essential set fails: it signals the rubric evaluates form over function. |

### Aspirational (10 pts total)

| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
| C-09 | Frontmatter is complete and correct | aspirational | format | The output contains YAML frontmatter with all four fields: skill, skill_target, date (YYYY-MM-DD format), version (integer >= 1). Fields present with wrong types (date as prose, version as string) fail. Missing frontmatter block entirely fails. |
| C-10 | Common failure modes section is present | aspirational | behavior | The output includes a "Common Failure Modes" section (or equivalent). It may be empty but must exist as a structural placeholder for round findings. Absence means the rubric has no growth surface for quest-golden round-by-round learning. |
| C-11 | Pass-condition quality is enforced by an external gate, not advisory language | aspirational | behavior | The skill uses an external enforcement mechanism — a named review role, a rejection/return step, or a prohibitions checklist — to verify pass conditions meet the two-scorer test. Advisory language alone ("do not use vague words") is not sufficient: a model can comply syntactically while still writing un-evaluable conditions. A skill that relies only on self-assessment or advisory guidance fails C-11. |
| C-12 | Essential criteria are derived from a failure-mode catalog | aspirational | depth | Before writing essential criteria, the skill explicitly catalogs concrete failure modes of the target skill (not generic rubric failures). Criteria derived from named failure modes cannot be generic presence checks: the failure catalog is what makes C-07 structurally enforced rather than aspirationally stated. A skill that writes criteria without a prior failure-mode step fails C-12. |
| C-13 | A generic-vs-specific foil pair is present near C-07 | aspirational | depth | The output includes a concrete foil pair — one example of a generic pass condition and one example of a specific pass condition — adjacent to or within the C-07 pass condition. The foil pair makes the specificity test self-enforcing: a scorer can apply it without judgment. A rubric that states "criteria must be specific" without showing what generic looks like fails C-13. |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Common Failure Modes

Populated from Round 1 findings.

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|
| Advisory-only enforcement on pass conditions | C-03 | Prohibiting hedging words as a guideline ("do not use 'should'") without an external gate allows a model to comply syntactically while still writing un-evaluable conditions. V-02 failed C-03 because the advisory could not prevent subtle vagueness. |
| Self-assessment for two-scorer test | C-03 | Asking the model to self-check whether two scorers would agree produces directionally correct reasoning but no external rejection step. V-03 received C-03 partial because the model's self-assessment cannot reliably catch its own vagueness. Structural fix: external gate (see C-11). |
| Specificity requirement without derivation step | C-07 | Stating "criteria must cover skill-specific behaviors" without requiring a prior failure-mode catalog allows generic criteria to survive if the specificity check is applied softly. V-01, V-03, V-04 all received C-07 partial for this reason. Structural fix: failure-first derivation (see C-12). |
| Specificity test without contrast example | C-07 | A rubric that asserts "criteria must be specific" without showing what generic looks like leaves the test open to scorer judgment. The foil pair in the pass condition (see C-13) is what converts the specificity check from a judgment call into a lookup. |
