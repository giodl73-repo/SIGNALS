# quest-rubric Variate — Round 4 (Round 1 against rubric v1)
**Date:** 2026-03-15
**Rubric:** v1 (distilled, filed as v16 in the iteration series)
**Criteria in scope:**
- Essential: C-01 (all 5 fields, count >= 6), C-02 (testable pass conditions), C-03 (essential covers non-negotiable), C-04 (formula + threshold), C-05 (>= 3 skill-specific)
- Recommended: C-06 (tier distribution), C-07 (>= 3 categories), C-08 (recommended tests quality)
- Aspirational: C-09 (causal linkage), C-10 (contrast example in at least 1 essential)

**Design note:** R1–R3 explored lifecycle gating, table format, contractual register, verification phases, and three-competitor inertia framing against older rubric versions where causal linkage and contrast examples were load-bearing structural requirements. In this rubric v1, C-09 and C-10 are intentionally aspirational — the essential tier is stable and well-specified, so the challenge shifts to whether the skill body prompt reliably produces outputs that reach the aspirational tier. This round probes five new mechanisms: a Critic role targeted at the aspirational gap (V-01), prose-spec format that favors causal narration (V-02), definitional register that front-loads the normative model (V-03), an aspirational-tier competitor as the inertia anchor (V-04), and an interrogative Examiner whose questions are calibrated to C-09 and C-10 (V-05).

---

## Round 4 Variation Map

| Variation | Axis | C-09 probe | C-10 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Role sequence (Builder + Critic) | Strong — Critic explicitly reviews causal linkage for each essential criterion and rewrites proxy pass conditions | Strong — Critic explicitly tests whether each essential can be transplanted to another skill | Single-axis; Critic targets only aspirational properties; risk: Builder produces mediocre foundation that Critic must overhaul |
| V-02 | Output format (prose specification) | Moderate — prose narration encourages causal reasoning but lacks structural enforcement | Strong — contrast examples flow naturally in prose, less awkward than structured blocks | Single-axis; five fields split across prose sections and metadata table; risk: C-01 completion failures at higher rates |
| V-03 | Phrasing register (definitional / normative-first) | Strong — definition of a criterion explicitly encodes "the observable whose absence IS the failure" | Moderate — definition encodes skill-specificity requirement but contrast example not explicitly required | Single-axis; definition front-loads the normative model before instruction; risk: definitional framing is abstract and may produce criteria that satisfy definitions syntactically |
| V-04 | Inertia framing (aspirational-tier competitor) | Strong — "the good rubric" competitor passes C-01–C-08 but fails C-09; naming it creates explicit pressure to go further | Strong — "the good rubric" competitor also fails C-10; naming it makes contrast examples a distinguishing property, not a decoration | Combined (lifecycle emphasis + inertia framing); risk: naming a competitor that passes the essential tier may lower the essential bar |
| V-05 | Role sequence + phrasing register (Examiner interrogation) | Very strong — Examiner's fixed questions are designed to surface whether pass conditions test causal observables or proxies | Very strong — Examiner's fixed questions require the Builder to name a generic rubric that would pass each essential criterion, then specify why it would fail | Combined; Examiner questions are structurally calibrated to C-09 and C-10; risk: question-driven format invites long analytical sections that displace criterion precision |

---

## V-01 — Role Sequence (Builder + Critic)

**Axis:** Role sequence
**Hypothesis:** The gap between a rubric that passes C-01–C-08 and one that also achieves C-09 and C-10 is a review gap, not an analysis gap. A Builder who drafts criteria from failure modes produces adequate essential criteria; a Critic who specifically interrogates causal linkage and skill-specificity of those criteria closes the aspirational gap. The Critic's scope is narrow: two properties, all essential criteria, specific rewrite instructions for failures. The hypothesis is that a narrow Critic scope produces more targeted revisions than a broad verification phase (R3 V-04), because the Critic only touches the properties that distinguish good from excellent.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence. The Builder builds the rubric. The Critic reviews it against two aspirational properties. The final output incorporates Critic revisions.

---

**BUILDER ROLE**

Read the skill spec. Extract:
1. What the skill produces — artifact type, required fields, structural shape.
2. Lifecycle phases — what each phase delivers.
3. At least 3 failure modes — what makes an output of this skill non-functional or misleading?

For each failure mode, draft one essential criterion. Required fields for every criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence stating what must be true in a passing output
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence using observable anchors — count thresholds, presence/absence of named fields, structural patterns, explicit enumerations. Phrases like "is clear", "seems appropriate", "adequately covers" are not observable anchors.

Draft 3-5 essential criteria. Then draft 2-3 recommended criteria (pass conditions test quality properties, not just presence) and 1-2 aspirational criteria (go beyond essential and recommended). Continue sequential C-NN numbering across tiers.

---

**CRITIC ROLE**

The Critic reviews each essential criterion against two aspirational properties. The Critic does not rewrite the entire rubric — only the specific fields that fail the review.

**C-09 review — causal linkage:**

For each essential criterion (C-01 through C-NN where Weight = essential), ask:

> "If the observable named in this pass condition were absent, does that directly instantiate the failure mode — or is it a proxy for the failure?"

The distinction: a proxy observable is one that correlates with the failure but whose absence could coexist with a non-failing output. A causal observable is one whose absence IS the failure — if it were present, the failure could not occur.

If the pass condition tests a proxy: rewrite the pass condition to name the causal observable. State the revision:
```
C-NN pass condition revised:
  Before: [original pass condition]
  After:  [revised pass condition naming the causal observable]
  Reason: [why the original was a proxy and what the causal observable is]
```

**C-10 review — skill-specific contrast:**

For each essential criterion (C-01 through C-NN where Weight = essential), ask:

> "Could this criterion appear unchanged in a rubric for a different skill?"

If yes: add a contrast example to the Text field of that criterion:

> "Not: '[the generic formulation that could apply to any skill's rubric]' — but: '[the formulation that names a concrete property of {skill_target}'s output that does not exist in generic documents].'"

State the addition:
```
C-NN Text field addition:
  Contrast added: (generic: '...'; skill-specific: '...')
```

After the Critic's review, incorporate all revisions into the final criteria. Revised pass conditions replace originals. Contrast examples are embedded in Text fields. The Critic's revision notes do not appear in the final output.

---

**SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — name what the rubric evaluates and state that the Critic's causal linkage review and skill-specificity review are what close the gap between passing and excellent), then criteria ordered essential → recommended → aspirational (revision notes omitted, revisions applied), then scoring section.

---

## V-02 — Output Format (Prose Specification)

**Axis:** Output format
**Hypothesis:** Structured criterion blocks (ID / Text / Weight / Category / Pass condition) enforce C-01 completion but suppress causal narration — the mechanism that links a pass condition to its failure mode is cut off at one sentence. Prose-spec format allows a criterion's causal reasoning to be written out before the pass condition is stated, which may produce better C-09 outcomes (causal observables rather than proxies) because the mechanism is visible and auditable. Contrast examples also flow more naturally in prose than as a structured sub-field. The risk is C-01 failures at higher rates, since prose format does not enforce field presence through structure. The probe: does prose format produce better aspirational outcomes (C-09, C-10) at the cost of more frequent essential failures (C-01), and if so, is the tradeoff worth it?

---

You are writing a scoring specification for a Signal skill. The specification describes what a passing output contains, what a good output adds, and what an excellent output demonstrates.

Read the skill spec. Understand what the skill promises, what lifecycle phases it has, and what a complete correct output looks like.

---

**SPECIFICATION**

Write the specification in three tiers. Each property is a named section:

```
### [Property name]
Weight: essential | recommended | aspirational
Category: correctness | depth | format | coverage | behavior

[One sentence: what must be true in a passing output — state the property and why its absence makes the output non-functional or misleading.]

[One sentence: the pass condition — the observable a third party can check without subjective judgment. Use count thresholds, named fields, structural patterns, or explicit enumerations. Do not use "is clear", "seems appropriate", "adequately covers" as the sole criterion.]
```

**Essential properties (3-5):** Absence makes the output non-functional or misleading. Not merely worse.

**Recommended properties (2-3):** Presence distinguishes a passing output from a good one. The pass condition tests a quality property — degree, precision, specificity — not just whether the property exists.

**Aspirational properties (1-2):** Presence distinguishes a good output from an excellent one. Must go beyond what essential and recommended already require.

For at least one essential property: after the pass condition sentence, add a contrast example in the same section:

> "Not: '[formulation applicable to any rubric for any skill]' — but: '[formulation naming a concrete property of {skill_target}'s output that cannot be transplanted to a rubric for a different skill].'"

---

**CRITERION INDEX**

After all specification sections, write a compact criterion index:

| ID | Property name | Weight | Category |
|----|--------------|--------|----------|

Assign C-NN IDs sequentially in the order the sections appear. This index is the structured anchor that allows automated scoring; the prose sections are the specification that supports human judgment.

---

**SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences), then specification sections (essential → recommended → aspirational), then criterion index table, then scoring section. The specification sections and criterion index together constitute the criteria — a scorer needs both.

---

## V-03 — Phrasing Register (Definitional / Normative-First)

**Axis:** Phrasing register
**Hypothesis:** Prior rounds used instructional register ("write", "produce", "draft") and conversational register ("what breaks?", "what matters?"). Both are process-oriented — they instruct the operator how to produce output. Definitional register is normative-oriented: it defines what a rubric criterion IS before instructing how to write one. If the definition of a rubric criterion encodes "the observable whose absence IS the failure mode" as a constitutive property, then a criterion that fails C-09 (causal linkage) is by definition not a criterion — it is a heuristic. This reframes C-09 as a non-negotiable structural requirement rather than an aspirational property. The hypothesis is that definitional framing raises the floor by excluding non-criteria from the essential tier, producing rubrics that achieve C-09 on the essential criteria not by reaching for excellence but by satisfying the definition.

---

You are building a scoring rubric for a Signal skill.

A scoring rubric is a document where:

**A criterion** is a named property of an output with five fields (ID, Text, Weight, Category, Pass condition) where the pass condition names the observable whose absence or presence constitutes the property — not a symptom, not a correlate, but the specific thing that, if present, would have prevented the failure the criterion guards against.

**A pass condition** is an auditable sentence a third party can evaluate without subjective judgment by checking a count, verifying the presence or absence of a named field, recognizing a structural pattern, or confirming an explicit enumeration. A pass condition that requires judgment about quality, clarity, or sufficiency is not a pass condition — it is an opinion.

**An essential criterion** is a criterion whose failure makes the output non-functional or misleading. Not merely worse. An essential criterion that could be removed without changing whether the output serves its purpose is not essential — it is recommended.

**The composite formula** is the scoring mechanism that converts criterion-level pass/fail signals into an output-level score. Without it, quest-golden cannot compute whether an output passes the rubric. A rubric without a composite formula is not a rubric — it is a list.

These definitions are not aspirational. They are constitutive: a document that fails them is not a rubric.

---

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

Name the failure modes — what makes an output of this skill non-functional? Name the observable for each failure mode: the specific thing whose absence IS the failure.

---

**Build the rubric.**

Write criteria that satisfy the definitions above. For each criterion, fill in all five fields — no blanks, no "TBD":

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence — what must be true in a passing output
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence. The observable must be the thing whose absence constitutes the failure the criterion guards against, not a proxy for it.

Before finalizing a pass condition, verify: "Is this the observable whose absence IS the failure — or is it a proxy that correlates with the failure?" If it is a proxy, name the causal observable.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. All three tiers required.

Essential: absence makes the output non-functional or misleading (see definition above).
Recommended: presence makes the output good, not just passing. The pass condition tests a quality property, not just presence.
Aspirational: presence makes the output excellent. Must go beyond what essential and recommended already require.

For at least one essential criterion, embed a contrast example in the Text field to show what the specific criterion catches that a generic formulation would miss:
> "Not: '[formulation applicable to any document]' — but: '[formulation naming a concrete property of {skill_target}'s output].'"

---

**Write the composite formula:**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — state what the rubric evaluates and invoke the definitional principle: a pass condition that names a proxy instead of the causal observable is not a pass condition), then criteria ordered essential → recommended → aspirational, then scoring section.

---

## V-04 — Lifecycle Emphasis + Inertia Framing (Aspirational-Tier Competitor)

**Axis:** Lifecycle emphasis + inertia framing (aspirational-tier competitor)
**Hypothesis:** R1-R3 used the vague rubric as the status-quo competitor — one that fails C-02 (testable pass conditions) because it uses qualitative language. The vague rubric motivates the essential tier but offers no pressure toward the aspirational tier: once your pass conditions are anchored, you've beaten the vague rubric. V-04 introduces a second competitor: the good rubric — one that passes C-01 through C-08 (all essential and recommended criteria) but has no causal linkage (C-09 fail) and no contrast examples (C-10 fail). The good rubric looks excellent from the outside. Its pass conditions are anchored, its criteria are skill-specific, its tiers are balanced. It simply doesn't go further. By naming this competitor explicitly and asking at each phase "would the good rubric survive this gate?", the prompt creates pressure toward the aspirational tier that the vague rubric competitor cannot supply. The hypothesis is that naming the near-excellent competitor produces more aspirational criterion properties than naming the obviously-failing one.

---

You are building a scoring rubric for a Signal skill. Your rubric has two competitors.

**Competitor 1: The Vague Rubric.** Pass conditions that say "the output is clear and well-organized." Cannot be evaluated by a third party. Fails C-02 (testable pass conditions). Your essential criteria must name observables sharp enough that Competitor 1 fails every one.

**Competitor 2: The Good Rubric.** Pass conditions are sharp. Criteria are anchored. Tier distribution is correct. Formula is present. From the outside it looks like an excellent rubric. But its essential criteria name observables that correlate with failure modes — not the observables whose absence IS the failure. Its criteria could appear unchanged in a rubric for a different skill. Competitor 2 passes all essential and recommended criteria in this rubric. It fails C-09 (causal linkage) and C-10 (contrast example). Your rubric must go further than Competitor 2.

---

**PHASE 1 — SPEC ANALYSIS**

Read the skill spec. Extract:
1. What the skill produces.
2. Lifecycle phases and what each delivers.
3. At least 3 failure modes — what makes an output of this skill non-functional?

For each failure mode: name the observable whose absence IS the failure — not a proxy, not a correlate. The causal observable.

Would Competitor 1 catch this failure? (No — its pass conditions are qualitative.)
Would Competitor 2 catch this failure? (Maybe — if the observable is a proxy, Competitor 2's anchored pass condition might catch it without identifying the cause.)

Write the failure mode list:
```
FAIL-01: [failure] — causal observable: [X] — is X the causal observable or a proxy? [causal/proxy]
FAIL-02: ...
FAIL-03: ...
```

DO NOT proceed to Phase 2 until each failure mode has a causal observable, not a proxy.

---

**PHASE 2 — ESSENTIAL CRITERIA**

Draft essential criteria from failure modes. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence. For criteria where the skill-specific formulation is non-obvious, add a contrast example: "Not: '[generic formulation]' — but: '[formulation naming a concrete property of {skill_target}'s output].'"
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: the causal observable from Phase 1, stated as one auditable sentence.

After each essential criterion, apply the competitor tests:

> **Competitor 1 test:** Could Competitor 1's rubric (with qualitative-only pass conditions) pass this criterion? If yes, the pass condition is not anchored enough.

> **Competitor 2 test:** Could Competitor 2's good rubric pass this criterion WITHOUT satisfying C-09 or C-10 — i.e., using a proxy observable rather than the causal one? If yes, the pass condition needs to explicitly require causal grounding.

Draft 3-5 essential criteria. Apply both tests before finalizing each.

DO NOT proceed to Phase 3 until 3-5 essential criteria pass both competitor tests.

---

**PHASE 3 — RECOMMENDED AND ASPIRATIONAL CRITERIA**

Recommended (2-3): What does Competitor 2 do well that Competitor 1 does not? Those are your recommended criteria — the quality properties above the essential floor that Competitor 2 achieves. Each recommended criterion's pass condition tests a quality property, not just presence.

Aspirational (1-2): What does your rubric do that Competitor 2 cannot? Those are your aspirational criteria — the properties that require causal linkage or skill-specific contrast, which Competitor 2 omits. An aspirational criterion that Competitor 2 would also pass is not aspirational in this context.

Continue sequential C-NN numbering. All three tiers required.

---

**PHASE 4 — SCORING AND OUTPUT**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
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

Body: purpose statement (2-3 sentences — name both competitors and state that the good rubric competitor is what distinguishes passing from excellent), then criteria ordered essential → recommended → aspirational (competitor test notes omitted, contrast examples retained in Text fields), then scoring section.

---

## V-05 — Role Sequence + Phrasing Register (Interrogative Examiner)

**Axis:** Role sequence + phrasing register
**Hypothesis:** R1 V-03 used a conversational register with open questions ("what breaks?", "what matters?") — good for surfacing failure modes but not specifically calibrated to C-09 and C-10. V-05 uses a fixed interrogative Examiner whose questions are structurally designed to reveal C-09 failures (proxy observables) and C-10 failures (transferable criteria). The Examiner does not approve or reject criteria — it asks questions the Builder must answer before the criterion can be finalized. The answers to the Examiner's questions become the causal links and contrast examples in the final criteria. The hypothesis is that question-answering in context of a specific criterion produces better C-09 and C-10 outcomes than asking those questions in the abstract (as analysis steps), because the Builder cannot produce a generic answer — the Examiner's question is already tied to a specific criterion and its pass condition.

---

You are building a scoring rubric for a Signal skill. Two roles operate alternately: the Builder drafts criteria, and the Examiner interrogates each criterion before it is finalized. No criterion is finalized until the Examiner's questions are answered.

---

**BUILDER: SPEC ANALYSIS**

Read the skill spec. Name:
- What the skill produces.
- Lifecycle phases and what each delivers.
- At least 3 failure modes — what makes an output of this skill non-functional?

---

**BUILDER + EXAMINER: CRITERION DRAFTING**

For each failure mode, the Builder drafts one essential criterion with all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence — what must be true in a passing output
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with an observable anchor

Then the Examiner asks four questions about that criterion. The Builder answers each question before the criterion is finalized.

**Examiner question set (asked for each essential criterion):**

1. **The failure question:** "What is the failure mode this criterion guards against? Name it in one sentence."

2. **The causal question:** "If the observable in your pass condition were absent from an output, would that directly instantiate the failure mode — or would the failure mode still be possible even if the observable were present?"
   - If the observable is causal: the pass condition stands.
   - If the observable is a proxy: the Builder revises the pass condition to name the observable whose absence IS the failure before proceeding.

3. **The transplant question:** "If I changed only the skill name in this criterion's Text and Pass condition fields, would this criterion still apply to a rubric for a different skill?"
   - If no (skill-specific): the criterion stands.
   - If yes (transplantable): the Builder adds a contrast example to the Text field: "Not: '[the generic formulation that would survive the transplant]' — but: '[the formulation naming a concrete property of {skill_target}'s output].'"

4. **The anchor question:** "Does the pass condition use an observable anchor — a count threshold, a named field, a structural pattern, or an explicit enumeration? Or does it rely on a phrase like 'is clear', 'seems appropriate', 'adequately covers'?"
   - If anchored: the criterion stands.
   - If unanchored: the Builder replaces the qualitative language with an observable anchor before proceeding.

After all four questions are answered and any revisions are applied, the criterion is finalized.

---

**BUILDER: RECOMMENDED AND ASPIRATIONAL CRITERIA**

Draft 2-3 recommended criteria and 1-2 aspirational criteria using the same five-field structure. Recommended criteria: pass conditions test quality properties, not just presence. Aspirational criteria: go beyond essential and recommended.

Apply only the anchor question (question 4) to recommended and aspirational criteria. Questions 2 and 3 apply to essential criteria only.

Continue sequential C-NN numbering. All three tiers required.

---

**BUILDER: SCORING**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

---

**OUTPUT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences — state what the rubric evaluates and name the Examiner's interrogation principle: no criterion is finalized until its causal observable is confirmed and its skill-specificity is verified), then criteria ordered essential → recommended → aspirational (Examiner dialogue omitted from final output, causal revisions and contrast examples retained in criterion fields), then scoring section.
