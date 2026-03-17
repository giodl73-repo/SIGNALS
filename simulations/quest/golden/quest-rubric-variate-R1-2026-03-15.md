---
skill: quest-variate
skill_target: quest-rubric
date: 2026-03-15
round: R1
rubric_version: v1
status: variate
---

# quest-rubric Variate — Round 1

**Date:** 2026-03-15
**Skill:** quest-rubric
**Rubric:** v1 (C-01–C-10; essential C-01–C-05)
**Round:** R1 — single-axis (V-01/V-02/V-03/V-04) + combined (V-05)

**Round 1 design note:** First round against the current v1 rubric. The five essential criteria
are: C-01 (all 5 criterion fields present), C-02 (essential count 3–5), C-03 (pass conditions
self-contained / two-scorer test), C-04 (scoring formula with correct denominators), C-05
(golden threshold states both conditions: all-essential AND composite >= 80). The three
recommended criteria add: C-06 (all three tiers present), C-07 (essential criteria are
skill-specific rather than generic), C-08 (category variety across essential). The two
aspirational add: C-09 (frontmatter complete), C-10 (common failure modes section exists).

**Spread design:** R1 is a diagnostic pass. V-01 through V-04 each isolate one axis; V-05
combines two. The most diagnostic criterion gaps will be C-03 (pass condition vagueness,
historically the hardest to close) and C-07 (generic vs. skill-specific essential criteria).
V-01 and V-04 both target C-03 through different mechanisms. V-03 and V-05 both target C-07.

---

## Round 1 Variation Map

| V | Axis | C-03 probe | C-07 probe | Notes |
|---|------|-----------|-----------|-------|
| V-01 | Role sequence | Strong — AUDITOR role explicitly applies two-scorer test to each pass condition before DEFINER emits | Moderate — ANALYST names observable behaviors but does not require contrast against skill specifics | Two-role sequence: ANALYST identifies behaviors, AUDITOR rejects vague conditions, DEFINER emits |
| V-02 | Output format | Moderate — prose blocks give pass conditions unlimited space, reducing compression-induced vagueness | Weak — format does not constrain specificity; generic criteria still fit the prose block format | Per-criterion prose blocks replace table; format changes but no specificity gate |
| V-03 | Lifecycle emphasis | Moderate — failure-mode log anchors pass conditions to observable evidence | Strong — Phase 1 failure analysis surfaces skill-specific failure patterns before criteria are written | Failure-first phases; criteria derived from named failures; no hard gate on pass condition form |
| V-04 | Phrasing register | Strong — DO NOT prohibitions on vague language ("should", "generally") are binary and enforceable | Moderate — specificity gate present but phrased as a requirement, not a derivation step | Fully imperative DO/DO NOT register; explicit two-scorer test as a hard gate |
| V-05 | Inertia framing + lifecycle emphasis | Strong — STATUS QUO RUBRIC foil names vague-pass-condition as failure mode 2, forcing contrast | Strong — foil's failure mode 1 (generic presence checks) forces each essential criterion to name specific field/count/value | Combined: 5-item STATUS QUO RUBRIC foil + Phase 1 contrast analysis before criterion writing |

---

## V-01 — Role Sequence: Analyst → Auditor → Definer

**Axis:** role-sequence
**Hypothesis:** Splitting into three sequential roles — ANALYST (identify observable behaviors),
AUDITOR (reject vague pass conditions), DEFINER (emit the artifact) — will improve C-03
(pass condition clarity) and C-01 (all 5 fields present) because the AUDITOR creates a review
gate between behavior identification and criterion writing. Without role separation, the prompt
proceeds directly to criteria and pass conditions are written once with no check. With the
AUDITOR, a vague pass condition must be rewritten before the DEFINER is allowed to emit.
Falsifiable: if C-03 does not improve over baseline, the AUDITOR review gate adds no value
beyond what a single-role prompt achieves.

---

You are running `/quest:rubric {skill}`.

Inputs:
- Skill spec for `{skill}` (signal.skills.yaml description block)
- Sample outputs: any available golden outputs or trace outputs for `{skill}`

Output: a scoring rubric at `simulations/quest/rubrics/{skill}-rubric-{date}.md`

---

**RUBRIC ANALYST**

Read the skill spec and sample outputs for `{skill}`. Produce a behavior inventory:
one entry per observable behavior in the skill's output.

For each behavior, write:

```
Behavior: {what the output does or contains}
Observable when present: {what a scorer sees when this behavior is satisfied}
Observable when absent: {what a scorer sees when this behavior is missing or wrong}
Failure severity: blocking | suboptimal | cosmetic
```

Blocking = the output is wrong or incomplete in a way that makes it unusable as a rubric.
Suboptimal = the output is usable but misses a quality signal.
Cosmetic = the output could be improved but the core is correct.

Write all behaviors before proceeding. Do not write criteria yet.

---

**RUBRIC AUDITOR**

Review each behavior from the ANALYST. Apply two tests:

1. **Two-scorer test** — can two independent scorers evaluate this behavior by reading
   only the rubric output, without consulting the skill spec, without any judgment calls
   about "generally", "should", or "appropriate"? If NO: mark VAGUE. Return to ANALYST
   with instruction to sharpen the "observable when absent" description.

2. **Specificity test** — is this behavior specific to `{skill}`, or would it pass as a
   criterion for any skill rubric? A criterion like "output contains a table" is generic.
   A criterion like "each table row has exactly 5 columns in order: ID, Text, Weight,
   Category, Pass Condition" is specific. If GENERIC: mark GENERIC. Return to ANALYST.

The AUDITOR does not pass a behavior that fails either test. Behaviors marked VAGUE or
GENERIC must be sharpened before the DEFINER receives them.

---

**RUBRIC DEFINER**

Receive the AUDITOR-approved behavior list. For each behavior:

1. Assign weight:
   - blocking severity → essential
   - suboptimal severity → recommended
   - cosmetic severity → aspirational

2. Assign category: correctness | depth | format | coverage | behavior

3. Write one criterion row:
   `| C-NN | {text} | {weight} | {category} | {pass condition} |`

Weight distribution:
- Essential: 3–5 criteria. A rubric output failing any essential criterion is not golden.
- Recommended: 2–3 criteria.
- Aspirational: 1–2 criteria.

Essential criteria must span at least 2 distinct categories.

---

**EMIT FORMAT**

Write the artifact to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

```yaml
---
skill: quest-rubric
skill_target: {skill}
date: {YYYY-MM-DD}
version: 1
---
```

Then three criterion tables — one per tier — each with columns:
`| ID | Text | Weight | Category | Pass Condition |`

Then the scoring formula section:
```
composite = (essential_pass / {E} * 60)
          + (recommended_pass / {R} * 30)
          + (aspirational_pass / {A} * 10)
```
Replace {E}, {R}, {A} with the actual count of criteria written in each tier.

Then: **Golden threshold: all essential criteria pass AND composite >= 80.**

Then a "Common Failure Modes" section with an empty table:
`| Finding | Criterion | Failure Pattern |`

---

**DEFINER OUTPUT GATE**

Do not emit until all of these are true:
- Every criterion has all five fields: ID, text, weight, category, pass condition
- Essential criterion count is between 3 and 5 inclusive
- Every pass condition passed the AUDITOR's two-scorer test
- Formula denominators {E}, {R}, {A} match the actual criterion counts in the tables
- The golden threshold statement names both conditions: all-essential AND composite >= 80

---

## V-02 — Output Format: Per-Criterion Prose Blocks

**Axis:** output-format
**Hypothesis:** Per-criterion prose blocks (each criterion as a named section with labeled
fields) will improve C-03 (pass condition unambiguity) because the format allocates unlimited
vertical space to the pass condition instead of compressing it into a table cell. When pass
conditions are written in a table, writers compress multi-condition checks into a single
sentence and strip precision in the process. With prose blocks, writers naturally produce
multi-sentence, specific pass conditions. Falsifiable: if prose blocks produce equally
vague pass conditions as the table format, compression is not the mechanism causing C-03
failures and this axis has no diagnostic value.

---

You are running `/quest:rubric {skill}`.

Read the skill spec for `{skill}` (signal.skills.yaml) and any available golden outputs.

---

**CRITERION FORMAT**

Write each criterion as a named block — not a table row. Use exactly this structure:

```
---
**C-NN: {one-line title}**
Weight: essential | recommended | aspirational
Category: correctness | depth | format | coverage | behavior
Pass condition: {Evaluation instructions for a scorer. Write as many sentences as the
condition requires. Name the specific fields, counts, labels, or conditions being checked.
Do not use "should", "generally", or "typically". State exactly what passes and exactly
what fails. A scorer reading only this rubric — without consulting the skill spec — must
be able to evaluate this condition without judgment calls.}
---
```

Write criteria in this sequence: essential first (C-01 onward), then recommended, then
aspirational. Do not write recommended or aspirational criteria until all essential criteria
are written and satisfy the pass condition requirements above.

---

**WEIGHT RULES**

Essential (3–5): Non-negotiable behaviors. Failing any essential criterion means the output
is not golden, regardless of score. These must cover the skill-specific behaviors of
`{skill}` — not generic rubric structure.

Recommended (2–3): Quality differentiators. Present in good outputs; absent in minimal ones.

Aspirational (1–2): Excellence patterns found in the best outputs.

---

**CATEGORY DEFINITIONS**

correctness — the output is correct or incorrect; binary
depth       — the output demonstrates required analysis, reasoning, or derivation
format      — the output meets structural or presentational requirements
coverage    — the output addresses all required areas or conditions
behavior    — the output follows a required process, sequence, or decision rule

Essential criteria must span at least 2 distinct categories.

---

**SCORING SECTION**

After the last criterion block, write:

## Scoring Formula

```
composite = (essential_pass / {E} * 60)
          + (recommended_pass / {R} * 30)
          + (aspirational_pass / {A} * 10)
```

where {E} = count of essential criteria, {R} = count of recommended, {A} = count of
aspirational. Replace these placeholders with the actual counts before emitting.

**Golden threshold: all essential criteria pass AND composite >= 80.**

---

**FAILURE MODES SECTION**

After the scoring section:

## Common Failure Modes

| Finding | Criterion | Failure Pattern |
|---------|-----------|-----------------|

This section is empty on v1. It is a structural placeholder for findings from golden rounds.

---

**FRONTMATTER**

The artifact begins with:

```yaml
---
skill: quest-rubric
skill_target: {skill}
date: {YYYY-MM-DD}
version: 1
---
```

---

Write the artifact to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

---

## V-03 — Lifecycle Emphasis: Failure-First Phase

**Axis:** lifecycle-emphasis
**Hypothesis:** Requiring an explicit Phase 1 (failure mode analysis) before any criterion is
written will improve C-07 (skill-specific essential criteria) and C-08 (category variety)
because criteria derived from named failure modes are anchored to the skill's actual output
patterns rather than generic structural expectations. When a builder writes criteria without
first cataloging failures, they gravitate toward generic presence checks ("output has a
table"). When failures are cataloged first, the criteria that emerge are named-failure
contrasts: "the scoring formula's denominators do not match the actual tier counts" becomes
a specific, testable criterion rather than "formula is present". Falsifiable: if failure-first
phases do not increase criterion specificity, the issue is not framing but upstream reading
of the skill spec.

---

You are running `/quest:rubric {skill}`.

Read the skill spec for `{skill}` (signal.skills.yaml) and any available golden outputs.

---

**PHASE 1 — FAILURE ANALYSIS**

Before writing any criterion, catalog what failure looks like for `{skill}`.

For each observable failure mode, write:

```
Failure: {what is wrong in the output}
Severity: blocking | suboptimal | cosmetic
What a scorer sees: {the specific observable in the output that signals this failure}
```

Severity definitions:
- blocking — the output is wrong or unusable (missing required content, wrong structure)
- suboptimal — the output is usable but misses a quality signal or depth requirement
- cosmetic — the output could be improved but the core value is intact

Write at least 3 blocking failures and 2 suboptimal failures before proceeding to Phase 2.
Do not move to Phase 2 until Phase 1 has at least 5 entries.

---

**PHASE 2 — DERIVE CRITERIA FROM FAILURES**

For each failure from Phase 1:

1. Map severity to weight tier:
   - blocking → essential criterion
   - suboptimal → recommended criterion
   - cosmetic → aspirational criterion

2. Write the criterion's pass condition as the exact inverse of the failure:
   The pass condition names what a passing output contains or does differently from the
   failure. The scorer is checking for the absence of the failure mode, stated positively.

3. Verify: could two independent scorers evaluate this pass condition without consulting
   the skill spec? If not, sharpen by naming the specific field, count, label, or value.

Weight counts: 3–5 essential, 2–3 recommended, 1–2 aspirational.
Category variety: essential criteria must span at least 2 distinct categories.

---

**PHASE 3 — WRITE THE RUBRIC TABLES**

Group criteria by tier. For each tier, write a Markdown table:

```
| ID | Text | Weight | Category | Pass Condition |
|----|------|--------|----------|----------------|
```

Assign IDs sequentially: C-01, C-02, ...

---

**PHASE 4 — EMIT THE ARTIFACT**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Artifact structure:
1. YAML frontmatter: skill, skill_target, date (YYYY-MM-DD), version (integer >= 1)
2. Essential criteria table
3. Recommended criteria table
4. Aspirational criteria table
5. Scoring formula:
   `composite = (essential_pass / E * 60) + (recommended_pass / R * 30) + (aspirational_pass / A * 10)`
   where E, R, A are the actual counts of criteria written above. Recompute after Phase 3.
6. Golden threshold: "all essential criteria pass AND composite >= 80"
7. Common Failure Modes section — empty table, structural placeholder:
   `| Finding | Criterion | Failure Pattern |`

---

## V-04 — Phrasing Register: Imperative DO/DO NOT

**Axis:** phrasing-register
**Hypothesis:** Fully imperative DO/DO NOT register — replacing all procedural and descriptive
language with hard prohibitions — will improve C-01 (all 5 fields present) and C-03 (pass
condition unambiguity) because binary prohibitions prevent the omissions that procedural
phrasing leaves ambiguous. A procedural prompt says "write a clear pass condition." An
imperative prompt says "DO NOT use 'should', 'generally', or 'typically' in any pass
condition." The prohibition is checkable at a glance; the procedural instruction requires
a judgment call about what "clear" means. Falsifiable: if C-01 and C-03 failure rates are
unchanged from baseline, the register difference is not causal and the failures have a
different root cause.

---

You are running `/quest:rubric {skill}`.

DO read the skill spec for `{skill}` from signal.skills.yaml before writing any criterion.
DO read any available golden outputs for `{skill}` before writing any criterion.
DO NOT write criteria from the skill description alone.

---

**CRITERION FIELD REQUIREMENTS**

Every criterion MUST have all five of these fields, in this order:
1. ID — format: C-NN, sequential integers starting at C-01
2. Text — one-line description of what is being measured
3. Weight — exactly one of: essential | recommended | aspirational
4. Category — exactly one of: correctness | depth | format | coverage | behavior
5. Pass condition — evaluation instructions for a scorer

DO NOT emit a criterion missing any of these five fields.
DO NOT combine two fields into one column.
DO NOT use a weight label other than the three listed.
DO NOT use a category label other than the five listed.

---

**PASS CONDITION REQUIREMENTS**

DO write pass conditions that a scorer can evaluate by reading only the rubric output.
DO NOT write pass conditions that require consulting the skill spec.
DO NOT write pass conditions that require any judgment call.
DO NOT use the words "should", "generally", "typically", "usually", or "appropriate"
  in any pass condition.
DO write what specifically passes and what specifically fails.
DO NOT write "the output is clear" — write "the output names X and does not use Y".

TWO-SCORER TEST: before writing each pass condition, ask: could two independent scorers,
reading only this condition, agree on a clear case? If NO: rewrite.
DO NOT proceed with a condition that fails the two-scorer test.

---

**WEIGHT DISTRIBUTION**

DO write 3–5 essential criteria.
DO write 2–3 recommended criteria.
DO write 1–2 aspirational criteria.
DO NOT write fewer than 3 essential criteria.
DO NOT write more than 5 essential criteria.
DO NOT omit any tier.

---

**CATEGORY DISTRIBUTION (essential criteria)**

DO ensure essential criteria span at least 2 distinct categories.
DO NOT write all essential criteria in the same category.

---

**SCORING SECTION**

DO write a scoring formula section immediately after the last criterion table:

```
composite = (essential_pass / E * 60)
          + (recommended_pass / R * 30)
          + (aspirational_pass / A * 10)
```

DO replace E, R, A with the actual counts of criteria in each tier.
DO NOT emit a formula with placeholder text like {E} or N.
DO NOT emit a formula whose denominators do not match the actual criterion counts.

DO write the golden threshold as a separate statement:
"Golden threshold: all essential criteria pass AND composite >= 80."
DO NOT omit either condition (the all-essential requirement AND the score requirement).
DO NOT write only "score >= 80" without the all-essential gate.

---

**STRUCTURE REQUIREMENTS**

DO begin the artifact with YAML frontmatter:
```yaml
---
skill: quest-rubric
skill_target: {skill}
date: {YYYY-MM-DD}
version: 1
---
```
DO NOT omit the frontmatter block.
DO NOT use prose date format (e.g., "March 15, 2026") — use YYYY-MM-DD.
DO NOT use a string version (e.g., "v1") — use an integer (1).

DO write one Markdown table per tier using columns: ID | Text | Weight | Category | Pass Condition
DO write a "Common Failure Modes" section with an empty table after the scoring section:
`| Finding | Criterion | Failure Pattern |`
DO NOT omit this section.

---

**OUTPUT GATE**

DO NOT emit the artifact until all of these are confirmed:
- All criteria have all 5 required fields
- Essential count is 3–5
- All pass conditions pass the two-scorer test
- Formula denominators match actual criterion counts
- Both golden threshold conditions are stated (all-essential AND composite >= 80)

Write the artifact to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

---

## V-05 — Inertia Framing + Lifecycle Emphasis: STATUS QUO RUBRIC Competitor

**Axis:** inertia-framing + lifecycle-emphasis
**Hypothesis:** Naming the STATUS QUO RUBRIC (the rubric produced without this skill — one
spec read, first-pass criteria, no review) as a 5-item foil and then deriving criteria
explicitly as contrasts to foil failures will improve C-07 (skill-specific essential criteria)
and C-03 (pass condition unambiguity) simultaneously. A criterion defined against a named
failure mode cannot be generic — "present" or "complete" is not sufficient when the foil
also passes those tests. Combining the STATUS QUO RUBRIC foil with failure-first lifecycle
emphasis (Phase 1 contrast analysis before criterion writing) stacks both mechanisms. The
inertia framing targets C-07; the lifecycle phase targets C-03. Falsifiable: if C-07 and
C-03 do not jointly improve over single-axis V-03 and V-04, the combination adds no value
beyond the stronger single-axis variation.

---

You are running `/quest:rubric {skill}`.

Read the skill spec for `{skill}` (signal.skills.yaml) and any available golden outputs.

---

**THE STATUS QUO RUBRIC**

The STATUS QUO RUBRIC is the rubric you get without this skill: one spec read, criteria
written in a single pass, no review. It looks complete. It fails in five characteristic ways:

1. **Generic presence checks** — essential criteria test for the presence of rubric structure,
   not rubric quality. Pass condition: "the output contains criteria with IDs and pass
   conditions." Satisfied by any rubric-shaped output, including one with vague conditions.

2. **Vague pass conditions** — pass conditions use hedging language ("should be", "generally
   states", "is reasonably clear"). Two scorers reading the same output will disagree on
   borderline cases. This corruption propagates to every downstream scoring round.

3. **Format-heavy essential tier** — essential criteria cover structural requirements
   (frontmatter present, sections present, table present) rather than the skill-specific
   non-negotiable behaviors that determine whether the rubric can actually drive evaluation.
   Format criteria belong in recommended or aspirational; skill-specific correctness
   criteria belong in essential.

4. **Wrong tier assignments** — blocking behaviors (output is incomplete or wrong in a way
   that makes it unusable) get assigned as recommended. Excellence patterns get assigned
   as essential. The tier is guessed, not derived from failure severity.

5. **Formula with wrong denominators** — the formula says `(essential_pass / 5 * 60)` but
   only 4 essential criteria were written. The denominator was not recomputed after criteria
   were finalized.

---

**PHASE 1 — CONTRAST ANALYSIS**

For each STATUS QUO failure mode, derive the essential criterion that is immune to it:

| Foil failure | What an immune essential criterion must do |
|---|---|
| Generic presence checks | The pass condition names a specific value, count, or label — not a structural type. "Contains criteria" fails. "Each criterion row has exactly 5 columns in order: ID, Text, Weight, Category, Pass Condition" passes. |
| Vague pass conditions | The pass condition contains no hedging language. It names exactly what passes and exactly what fails, in terms a scorer can check without consulting the skill spec. |
| Format-heavy essential tier | At least one essential criterion measures a correctness or depth behavior of `{skill}` — not a format requirement. Format requirements may be recommended or aspirational. |
| Wrong tier assignments | Each criterion's tier is derived from failure severity: blocking → essential, suboptimal → recommended, cosmetic → aspirational. State the failure severity before assigning tier. |
| Formula with wrong denominators | The formula denominators are computed from the actual criterion counts written above. Compute last; never assume a count. |

---

**PHASE 2 — WRITE CRITERIA**

Using the contrast analysis from Phase 1, write:

Essential (3–5): Derived from blocking failures; immune to foil failures 1–4.
Recommended (2–3): Derived from quality-differentiating behaviors not covered by essential.
Aspirational (1–2): Derived from excellence patterns in the best golden outputs.

For each criterion, write one table row:
`| C-NN | {text} | {weight} | {category} | {pass condition} |`

Essential criteria must span at least 2 distinct categories.

---

**PHASE 3 — EMIT THE ARTIFACT**

Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Structure:
1. YAML frontmatter: skill, skill_target, date (YYYY-MM-DD), version (integer >= 1)
2. Essential criteria table: `| ID | Text | Weight | Category | Pass Condition |`
3. Recommended criteria table (same format)
4. Aspirational criteria table (same format)
5. Scoring formula — compute denominators from actual criterion counts:
   `composite = (essential_pass / E * 60) + (recommended_pass / R * 30) + (aspirational_pass / A * 10)`
   Immune to foil failure 5: E, R, A are the actual counts above.
6. **Golden threshold: all essential criteria pass AND composite >= 80.**
7. Common Failure Modes section — empty table, structural placeholder:
   `| Finding | Criterion | Failure Pattern |`
