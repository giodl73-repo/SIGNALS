# quest-rubric Variate — Round 2
**Date:** 2026-03-15
**Rubric:** v2 (adds C-11: causal linkage of pass conditions to failure modes; C-12: worked example in essential criterion text distinguishing generic from skill-specific)
**Target criteria:** C-11 and C-12 (new aspirational criteria from v2, not tested in Round 1)

**Round 2 design note:** Round 1 explored axes that drove C-01 through C-05 (structure, testability, skill targeting). V-04 (failure-mode-first + table) produced the best essential-tier results; V-05 (inertia framing) produced the sharpest pass conditions. Round 2 adds v2's two new aspirational criteria. C-11 requires *causal* linkage — the observable must be the thing whose absence *is* the failure, not merely a symptom. C-12 requires the criterion *text* itself to contain a worked example showing the generic-vs-specific contrast. The five variations below each attack one or both of those properties through a distinct mechanism.

---

## Round 2 Variation Map

| Variation | Axis | C-11 probe | C-12 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Role sequence (causal chain) | Strong — explicit three-link chain (failure → mechanism → observable) | Weak — contrast example not required | Single-axis; causal chain enforced before criteria table |
| V-02 | Lifecycle emphasis (worked example gate) | Moderate — failure mode origins visible | Strong — hard gate requires contrast example per essential criterion | Single-axis; phase cannot proceed without example |
| V-03 | Output format (extended table) | Strong — dedicated "causal link" column | Strong — dedicated "contrast example" column | Single-axis; column constraints enforce both; risk: analytic depth displaced |
| V-04 | Role sequence + phrasing register | Strong — conversational questions force causal interrogation | Moderate — questions invite examples but don't require them | Combined; natural language causal chain; C-11 strongest of any variation |
| V-05 | Lifecycle emphasis + inertia framing | Moderate — inertia test grounds observable in failure | Strong — extended inertia test requires showing generic vs specific version | Combined; worked example emerges from anti-generic contrast test; C-12 strongest |

---

## V-01 — Role Sequence (Causal Chain)

**Axis:** Role sequence
**Hypothesis:** Requiring a three-link causal chain — (1) failure mode, (2) the mechanism by which it breaks downstream use, (3) the specific observable whose absence is that mechanism's symptom — forces C-11 by construction. The chain is written before any criteria are drafted; criteria can only reference observables that appear in the chain. The risk is that C-12 (worked examples in criterion text) is not addressed: the causal chain lives in the analysis phase, not in the criterion text itself.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden — it must be complete, testable, and precisely anchored to the failure modes it was designed to catch.

A rubric that names the right observable is good. A rubric where each pass condition is the observable whose *absence is the failure* — not merely a symptom — is excellent. Build the second kind.

**PHASE 1: ENUMERATE FAILURE MODES WITH CAUSAL CHAINS**

Read the skill spec. For each lifecycle phase, ask: what breaks if this phase produces the wrong output?

For each failure mode, write a three-link chain:

```
FAIL-NN:
  (1) Failure: [what the output lacks or does wrong]
  (2) Mechanism: [why that absence breaks downstream use — be specific]
  (3) Observable: [the specific thing a third party can check whose absence confirms the failure]
```

Minimum 3 failure modes. Each observable in link (3) must be the thing whose absence directly instantiates link (1) — not a symptom that correlates with it.

Example of weak causal chain:
  (1) Failure: pass conditions are vague
  (2) Mechanism: evaluators cannot agree on scores
  (3) Observable: pass conditions use specific language

Example of strong causal chain:
  (1) Failure: pass conditions use qualitative language only
  (2) Mechanism: a third party evaluating the rubric cannot determine pass/fail without subjective judgment, making scores evaluator-dependent
  (3) Observable: no pass condition uses phrases like "is clear", "seems appropriate", or "looks good" without an anchoring count, named field, structural pattern, or explicit enumeration

The strong version names the observable because its absence *is* the failure mode, not because it correlates with quality.

DO NOT proceed to Phase 2 until each failure mode has all three links, and link (3) names an observable that directly instantiates the failure in link (1).

**PHASE 2: CONVERT CAUSAL CHAINS TO CRITERIA**

For each causal chain from Phase 1, write one essential criterion. The pass condition is link (3) from the chain — verbatim or tightened, not rephrased into something weaker.

Each criterion requires all five fields:

- **ID**: C-01, C-02, ... (sequential)
- **Text**: one sentence stating what must be true in a passing output
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: the observable from link (3), stated as one auditable sentence

After essential criteria (3-5), write recommended criteria (2-3) and aspirational criteria (1-2) using the same field structure. Recommended pass conditions test quality properties, not presence. Aspirational criteria must go beyond what essential and recommended require.

**PHASE 3: SCORING AND OUTPUT**

Write the composite formula:

```
composite = (essential_pass / N_e * 60)
          + (recommended_pass / N_r * 30)
          + (aspirational_pass / N_a * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences stating what the rubric evaluates and why causal precision matters), then criteria ordered essential → recommended → aspirational, then scoring section.

---

## V-02 — Lifecycle Emphasis (Worked Example Gate)

**Axis:** Lifecycle emphasis
**Hypothesis:** An explicit phase that requires writing a "generic vs skill-specific" contrast example for every essential criterion forces C-12 by construction. The phase gate prevents proceeding until at least one essential criterion's *text* (not just its analysis) contains a worked example. The causal chain (C-11) is present implicitly — failure modes are named before criteria — but the observable's causal role is not explicitly enforced. V-02 is the strongest single probe for C-12.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

A criterion that says "the rubric targets the specific skill" can be satisfied by a generic rubric with a find-replace on the skill name. A criterion whose text demonstrates specificity — showing what a generic rubric misses and what the skill-specific version catches — cannot. Build the second kind.

**STEP 1 — READ THE SKILL SPEC**

Read the skill spec. Extract:

1. What the skill promises to produce: artifact type, required fields, structural shape.
2. Lifecycle phases and what each delivers.
3. At least 3 failure modes — what makes an output of this skill non-functional or misleading?

Write failure modes explicitly before proceeding:
```
FAIL-01: [description]
FAIL-02: [description]
FAIL-03: [description]
```

DO NOT proceed to Step 2 until at least 3 failure modes are written.

**STEP 2 — GENERATE ESSENTIAL CRITERIA**

For each failure mode, draft one essential criterion with all five fields:

- **ID**: C-01, C-02, ...
- **Text**: one sentence — what must be true
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence using observable anchors (counts, named fields, structural patterns, enumerations). No "is clear", "seems appropriate", "adequately covers."

**STEP 3 — WRITE A CONTRAST EXAMPLE FOR EACH ESSENTIAL CRITERION**

For each essential criterion, write a contrast example in this format:

```
Generic formulation: "[a criterion that could apply to any document or any skill]"
Skill-specific formulation: "[a criterion that can only apply to {skill_target}]"
Why the generic fails: [one sentence explaining what failure mode the generic misses]
```

The contrast example must be embedded in or immediately follow the criterion's **Text** field — not placed in a separate analysis section. A criterion whose text could be copy-pasted unchanged into a rubric for a different skill, with only the skill name swapped, fails this requirement.

DO NOT proceed to Step 4 until every essential criterion has a contrast example embedded in its text or as a labeled sub-field.

**STEP 4 — GENERATE RECOMMENDED AND ASPIRATIONAL CRITERIA**

Recommended (2-3): What separates a passing output from a good one? Each pass condition must test a quality property, not presence/absence.

Aspirational (1-2): What separates a good output from an excellent one? Must go beyond what essential and recommended require.

Continue sequential C-NN numbering. Verify: all three tiers present.

**STEP 5 — WRITE COMPOSITE FORMULA AND GOLDEN THRESHOLD**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

**WRITE THE ARTIFACT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — state what the rubric evaluates and name the generic-vs-specific problem explicitly), then criteria ordered essential → recommended → aspirational (with contrast examples embedded), then scoring section.

---

## V-03 — Output Format (Extended Table)

**Axis:** Output format
**Hypothesis:** Extending the criteria table to include two additional columns — "causal link" and "contrast example" — enforces C-11 and C-12 structurally: a blank cell is immediately visible and constitutes a format failure. The column constraint is the strongest forcing function because it cannot be satisfied by a vague narrative. The risk is Round 1's V-02 finding: table format can displace analytical depth, producing correct-looking rows with shallow content.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Inputs:** skill spec (required), sample outputs (optional).

**Analysis**

Read the skill spec. Identify:
- What the skill produces: artifact shape, required fields, content structure.
- Lifecycle phases: what each phase delivers.
- Failure modes: what makes an output of this skill non-functional?

**Criteria table**

Produce a criteria table. All seven columns are required for every row. No cell may be blank, null, or "TBD."

| ID | Text | Weight | Category | Pass condition | Causal link | Contrast example |
|----|------|--------|----------|----------------|-------------|------------------|

Column definitions:

- **ID**: C-01, C-02, ... sequential.
- **Text**: one sentence — what must be true in a passing output.
- **Weight**: `essential` | `recommended` | `aspirational`. Exactly 3-5 essential, 2-3 recommended, 1-2 aspirational.
- **Category**: `correctness` | `depth` | `format` | `coverage` | `behavior`.
- **Pass condition**: one auditable sentence using observable anchors (count thresholds, named fields, structural patterns, enumerations). Phrases like "is clear" or "adequately covers" are not observable anchors and must not appear.
- **Causal link**: one sentence identifying why the observable in the pass condition is the thing whose absence *is* the failure mode — not merely correlated with it. Format: "If [observable] is absent, then [specific downstream failure] occurs because [mechanism]." Required for essential criteria; recommended for recommended criteria; optional for aspirational.
- **Contrast example**: for essential criteria only — one parenthetical showing the generic formulation and the skill-specific formulation side by side. Format: "(generic: 'X'; skill-specific: 'Y')". The skill-specific version must name a concrete property of {skill_target}'s output, not a generic quality attribute.

Tier rules:
- Essential: absence makes the output non-functional. Both causal link and contrast example columns required.
- Recommended: pass condition tests a quality property, not just presence. Causal link required. Contrast example optional.
- Aspirational: goes beyond essential and recommended. Causal link optional. Contrast example optional. Must not restate an essential criterion.

**Scoring section**

After the criteria table, write:

```
composite = (essential_pass / N_e * 60)
          + (recommended_pass / N_r * 30)
          + (aspirational_pass / N_a * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

**Output**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {skill}
date: {today}
version: 1
```

Body: purpose statement (2-3 sentences), then the criteria table (essential → recommended → aspirational), then scoring section.

---

## V-04 — Role Sequence + Phrasing Register (Conversational Causal Chain)

**Axis:** Role sequence (causal interrogation) + phrasing register (conversational)
**Hypothesis:** Conversational questions force the analyst to articulate the causal chain in natural language before any formal structure is imposed. The question "what is the thing whose absence *is* the failure — not just a symptom of it?" is harder to answer vaguely than an instruction to "enumerate failure modes." Combined with a role sequence where the causal interrogation happens before any criterion drafting, the hypothesis is that V-04 produces the most causally precise pass conditions (C-11) of any variation. C-12 is probed but not enforced — the conversational register may invite examples naturally, but they are not gated.

---

You are building the objective function for a Signal skill. Before writing any criteria, interrogate the failure chain.

**What does this skill promise?**

Read the skill spec. What does a complete, correct output contain? What does each lifecycle phase deliver? What would a user of this skill go looking for in the artifact it produces?

**What is the thing that breaks — not just what breaks?**

For each promise the skill makes, ask two questions in sequence:

First: *What breaks if this promise is not kept?* Name the failure.

Second: *What is the specific thing whose absence is that failure — not a symptom, not a correlate, but the thing that, if present, would have prevented the failure entirely?* Name the observable.

There is a difference between "the output is hard to evaluate" (a symptom) and "the pass condition contains only qualitative language with no count, field name, or structural pattern" (the observable whose absence IS the failure). The second question forces you to the second kind of answer.

Name at least 3 failure modes. For each, write both answers — the failure and the observable — before drafting any criterion.

**What makes a passing output good?**

After you have the failure observables, ask: what does a *good* version of a passing output look like? These become recommended criteria. Their pass conditions test quality properties — precision, specificity, degree — not presence.

**What makes a good output excellent?**

Ask: what would an excellent output have that a merely passing one lacks? These become aspirational criteria. They must go beyond what essential and recommended already require.

**Now write the rubric.**

For each criterion, fill in all five fields:

- **ID**: C-01, C-02, ... (sequential, starting at C-01)
- **Text**: one sentence — what must be true in a passing output
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one sentence a third party can evaluate without judgment. The pass condition for an essential criterion should be the observable you identified in the "second question" above — the thing whose absence is the failure, not a symptom.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. All three tiers required.

**Write the scoring formula and golden threshold.**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

**Write the artifact** to `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Frontmatter: `skill` (quest-rubric), `skill_target` (the named skill), `date` (today), `version` (1).

Structure: purpose statement (state what the rubric evaluates and name the distinction between symptoms and the observable whose absence is the failure), then criteria ordered essential → recommended → aspirational, then scoring section.

---

## V-05 — Lifecycle Emphasis + Inertia Framing (Worked Example + Anti-Generic Contrast Test)

**Axis:** Lifecycle emphasis (worked example gate) + inertia framing (anti-generic contrast test)
**Hypothesis:** The inertia test in Round 1 (V-05) sharpened pass conditions by asking "would a rubric that says 'the output is clear and comprehensive' still pass this condition?" Round 2 extends the inertia test from the pass condition to the criterion text itself: "could a generic rubric satisfy this criterion by simply swapping the skill name?" If yes, the criterion is not yet skill-specific, and the operator must embed a worked example showing what the generic version misses. This extended inertia test is the strongest single mechanism for C-12. Combined with an explicit lifecycle phase that cannot be bypassed, V-05 is designed to produce the highest C-12 compliance. C-11 is addressed through the causal grounding implicit in the original inertia test: the observable that "the vague rubric cannot reach" is precisely the causal observable that prevents the failure.

---

You are building the objective function for a Signal skill. Your rubric has two competitors to beat.

**Competitor 1: The Vague Rubric.** It says "the output is clear and well-organized," "the response adequately covers the key areas," and "the analysis seems thorough." Its pass conditions cannot be evaluated by a third party. Its golden threshold is undefined. Every rubric that uses qualitative language without observable anchors is the vague rubric.

**Competitor 2: The Generic Rubric.** It has specific pass conditions, but they apply to any document in any domain. "Contains at least 5 criteria" passes for a rubric about any skill. "All criteria have an ID, text, and weight" passes for a rubric about any skill. The generic rubric looks like it targets the skill, but its criteria could be satisfied by replacing the skill name in a template. It produces the same score for a good rubric and a bad one, as long as they share the same structure.

Your rubric must make both competitors fail.

**Read the skill spec.**

What does this skill promise? What does a complete correct output contain? For each lifecycle phase, what does passing look like?

**PHASE 1: ENUMERATE FAILURE MODES**

Name at least 3 failure modes — things that make this skill's output non-functional. Write them explicitly before proceeding.

For each failure mode, apply the **observable test**: what is the specific thing whose absence IS this failure? Not a symptom. Not a correlate. The thing that, if present, prevents the failure. Write that observable next to each failure mode.

**PHASE 2: DRAFT ESSENTIAL CRITERIA**

Convert each failure mode into an essential criterion with all five fields. The pass condition for each essential criterion is the observable from Phase 1 — the thing whose absence is the failure.

After drafting each essential criterion, apply two tests before finalizing:

**Inertia test (anti-vague):** Could a rubric that says "the output is clear and comprehensive" still pass this condition? If yes, sharpen the anchor. Add a count. Name a specific field. Require an explicit structural pattern.

**Generic test (anti-generic):** Could this criterion be satisfied by a rubric for any other skill, with only the skill name changed? If yes, embed a contrast example in the criterion text:

> "Not: '[generic formulation]' — but: '[skill-specific formulation that names a concrete property of {skill_target}'s output]'."

The contrast example must appear in the criterion's **Text** field, not in a separate analysis section. The skill-specific formulation must name something that only exists in {skill_target}'s output — not a generic quality attribute.

DO NOT finalize an essential criterion until both tests pass.

**PHASE 3: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Recommended (2-3): Apply the inertia test to each recommended criterion's pass condition. A presence-only pass condition fails the inertia test.

Aspirational (1-2): Must go beyond essential and recommended. Must not restate an essential criterion.

Continue sequential C-NN numbering. All three tiers required.

**PHASE 4: SCORING AND OUTPUT**

Write the composite formula:

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`.

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Structure: purpose statement (name both the vague-rubric and generic-rubric problems explicitly), then criteria ordered essential → recommended → aspirational (contrast examples embedded in essential criterion texts), then scoring section.
