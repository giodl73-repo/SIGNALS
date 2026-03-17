# quest-rubric Variate — Round 6 (Round 2 against rubric v2)
**Date:** 2026-03-15
**Rubric:** v2 (C-01–C-13; adds C-11: aspirational reference anchor; C-12: Text-argues-before-Pass-concludes; C-13: tier-grounded organic category diversity)
**Target criteria:** C-11, C-12, C-13 (three new aspirational criteria added to v2 since Round 2)

**Round 2 design note:** Rounds 1–5 explored mechanisms for C-01 through C-10 and C-17 in a parallel rubric track. Against rubric v2 specifically, Round 1 (R2) probed C-11 (causal linkage) and C-12 (contrast example in criterion text) — the two aspirational additions at that time. V-03 (extended table with causal-link and contrast-example columns) and V-05 (dual inertia — anti-vague + anti-generic) both scored 100 in that round. The current rubric v2 adds C-13: tier structure must be grounded in distinct failure dimensions, producing organic category diversity rather than label-count compliance. The scoring denominator shifts from /2 to /5 for aspirational; a rubric achieving only C-09+C-10 now scores 94. This round probes three new mechanisms for C-11/C-12/C-13 as a group, with each single-axis variation targeting the strongest new gap, and two combined variations closing multiple gaps simultaneously.

---

## Round 6 Variation Map

| Variation | Axis | C-11 probe | C-12 probe | C-13 probe | Notes |
|-----------|------|-----------|-----------|-----------|-------|
| V-01 | Inertia framing (aspirational-tier competitor) | Very strong — aspirational preamble must name the near-excellent reference before criteria written; contrast to prior competitor usage (which named at essential level) | Moderate — Text-first argument structure invited by competitor contrast but not gated | Weak — failure dimensions not explicitly designed | Single-axis; tests whether naming a competitor that passes C-01–C-08 creates aspirational pressure equivalent to naming a competitor that fails essential criteria |
| V-02 | Phrasing register (criterion-as-argument) | Weak — no reference named | Very strong — constitutive definition encodes Text=argument/Pass=conclusion; structural sequence check enforced per essential criterion | Moderate — failure dimension framing in failure mode analysis may invite tier separation but not formalized | Single-axis; definitional framing makes Text-before-Pass a structural requirement, not an aspiration; highest single-axis C-12 probe |
| V-03 | Lifecycle emphasis (tier-as-failure-dimension) | Moderate — reference invited at aspirational phase but not formalized | Moderate — failure-dimension context encourages causal Text fields but no explicit gate | Very strong — Phase 2 designs tiers from failure dimensions; predictability check enforced before criteria written; retrospective check after aspirational | Single-axis; highest single-axis C-13 probe; category diversity becomes consequence of design, not label assignment |
| V-04 | Lifecycle emphasis + Inertia framing | Strong — Phase 3 names reference before aspirational criteria written; reference must pass essential+recommended failure dimensions and fail aspirational | Moderate — failure-dimension context in Phase 2 encourages causal Text; no explicit gate | Very strong — Phase 2 designs tiers from failure dimensions with category-predictability check | Combined; closes C-11 and C-13 simultaneously; C-12 probed without gate; risk: C-12 compliance depends on quality of failure dimension descriptions |
| V-05 | Role sequence + Phrasing register (Scrutineer) | Strong — Interrogation 3 requires aspirational preamble naming reference if absent; revision instruction specified | Very strong — Interrogation 1 reviews Text-before-Pass structure per essential criterion; revision instruction if Text only labels | Strong — Interrogation 2 requires tier-to-category-dimension predictability; revision instruction if mapping is post-hoc | Combined; Scrutineer calibrated to exactly C-11, C-12, C-13; most comprehensive simultaneous coverage; risk: interrogation scope may produce verbose revision notes that displace analytical content |

---

## V-01 — Inertia Framing (Aspirational-Tier Competitor)

**Axis:** Inertia framing
**Hypothesis:** Prior rounds named two inertia competitors: the vague rubric (fails C-02, qualitative pass conditions) and the generic rubric (fails C-05, skill-name swap passes). C-11 requires a third class of competitor at a higher level: the near-excellent rubric — one that passes all essential and recommended criteria but does not name a near-excellent reference in its aspirational section, does not ground its tiers in failure dimensions, and does not construct the Text-as-argument structure in its criterion Text fields. Naming this competitor explicitly, before writing aspirational criteria, creates structural pressure toward C-11 because the aspirational section must identify exactly what the near-excellent competitor lacks — not abstract stretch goals, but the specific gaps that distinguish the near-excellent rubric from an excellent one. Prior inertia framing worked at the essential level (beating the vague rubric motivated sharp pass conditions). The hypothesis is that inertia framing at the aspirational level produces C-11 compliance at the same rate — because the mechanism is the same: the competitor names what the criteria must surpass.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

Your rubric has a near-excellent competitor: the good rubric — a rubric that has cleared every essential and recommended criterion. Its pass conditions are anchored in counts, named fields, and structural patterns. Its criteria are skill-specific. Its tier distribution follows the spec. Its composite formula is present and correct. From the outside, it looks excellent.

But the good rubric does not name a reference at the aspirational level — no specific artifact or pattern that passes everything up to the aspirational bar and falls short only there. Its criterion Text fields state what must be true without arguing why — the causal link is implied in the pass condition but not constructed as an argument in the Text. Its category distribution passes the count requirement but was assigned after criteria were written, not derived from the tier design.

The good rubric scores approximately 94 against this rubric's formula. Your rubric must reach 100.

**Read the skill spec.**

What does the skill promise? What does each lifecycle phase deliver? What does a complete correct output contain?

**PHASE 1: FAILURE MODES**

Name at least 3 failure modes — things that make this skill's output non-functional. For each failure mode, name the observable whose absence IS the failure (not a proxy or symptom). State whether the good rubric would catch this failure (it would; the vague rubric would not).

```
FAIL-01: [failure] — causal observable: [X] — caught by good rubric? [yes/no]
FAIL-02: [failure] — causal observable: [X] — caught by good rubric? [yes/no]
FAIL-03: [failure] — causal observable: [X] — caught by good rubric? [yes/no]
```

DO NOT proceed to Phase 2 until at least 3 failure modes have causal observables, not proxies.

**PHASE 2: ESSENTIAL CRITERIA (3-5)**

Draft each essential criterion with all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence stating what must be true. The Text must establish the downstream consequence of the observable's absence — "without X, Y fails because Z" — before naming X. The good rubric's Text says only "what must be true." Your Text argues why: the Text is the premise, the Pass condition is the conclusion.
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence using observable anchors (counts, named fields, structural patterns, enumerations). No "is clear", "adequately covers", or equivalent qualitative language as the sole criterion.

**PHASE 3: RECOMMENDED CRITERIA (2-3)**

Recommended criteria identify what separates a passing rubric from a good one. Each pass condition tests a quality property — degree, precision, specificity — not just presence.

Ask: what does the good rubric achieve that the vague rubric does not? Those are your recommended criteria. The good rubric reaches them; your rubric must reach them too, and then go further.

**PHASE 4: ASPIRATIONAL CRITERIA (1-5)**

Before writing aspirational criteria, name the reference:

```
Reference: [Name the good rubric specifically — a prior version, a named pattern
  (e.g., "a rubric built using the failure-mode-first extended-table method, which
  reliably passes C-01 through C-08 with anchored pass conditions, skill-specific
  criteria, and correct tier distribution"), or a class of rubrics you can describe
  precisely enough to identify. Must be specific — not "a hypothetical good rubric."]

Passes: [Identify which criteria or tiers the reference satisfies — state the essential
  and recommended tiers explicitly.]

Fails: aspirational tier — specifically: [Name the exact dimension(s) in which the
  reference falls short. E.g., "The reference names no aspirational reference point,
  so its aspirational criteria are abstract stretch goals rather than documented gaps
  in a known artifact." Or: "The reference's criterion Text fields label what must be
  true without arguing why — the causal chain is in the pass conditions but not
  constructed as an argument in the Text field."]
```

Then write aspirational criteria that describe the exact dimensions in which the named reference falls short. Each aspirational criterion may state: "The good rubric (reference) passes [criteria/tiers] but [lacks this specific property] because [mechanism]."

The reference must be specific enough to be recognizable — not a hypothetical class.

**PHASE 5: SCORING AND OUTPUT**

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

Body: purpose statement (2-3 sentences — name the near-excellent competitor and state what the aspirational tier adds above passing all essential and recommended criteria), then criteria ordered essential → recommended → aspirational (aspirational preamble naming the reference retained; Phase 1 failure mode analysis omitted), then scoring section.

---

## V-02 — Phrasing Register (Criterion-as-Argument)

**Axis:** Phrasing register
**Hypothesis:** C-12 requires the Text field to state "without X, Y fails" before the Pass condition names X. This is a structural sequence constraint: Text argues, Pass concludes. Round 4 V-03 (definitional register) encoded "a pass condition IS the observable whose absence is the failure" as constitutive. V-02 extends that definitional move to the criterion's two-part structure: the Text IS the argument, the Pass condition IS the conclusion of that argument. A criterion whose Text only labels what must be true — without establishing the downstream consequence — is not a criterion; it is an assertion. Assertions can be copy-pasted to any rubric for any skill without losing content because they contain no reasoning. Arguments cannot, because the reasoning is specific to the failure mechanism of this skill. The hypothesis is that encoding C-12's structural sequence as constitutive (part of what a criterion IS) produces higher compliance than instructing the operator to "explain causally in the text" — because the constitutive definition cannot be satisfied by rearranging the same words.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

A criterion has two structural components that are not interchangeable:

**A criterion Text** is the argument. It names what must be true AND establishes why the observable's absence matters downstream — "without [observable], [specific failure] occurs because [mechanism]." A Text that only states "what must be true" without establishing why has not built an argument. It has labeled a conclusion. The evaluator reading only the Text cannot tell whether the criterion matters — only that the author thought it should.

**A criterion Pass condition** is the conclusion of the Text's argument. It names the observable a third party can check — a count, a named field, a structural pattern, or an explicit enumeration — whose presence or absence determines pass/fail. The Pass condition does not justify itself; the Text justifies it. A Pass condition that names an observable the Text never argued for produces an internally inconsistent criterion: the conclusion does not follow from the premises.

Together: **Text argues → Pass concludes.** A criterion where the Text only labels what must be true, with the causal reasoning absent, is an assertion. Assertions can be transplanted to a different rubric for a different skill by changing the skill name; arguments cannot, because the downstream consequence named in "without X, Y fails because Z" is specific to this skill's failure modes.

These definitions are constitutive. A five-field structure that satisfies them contains a criterion. One that does not contains a labeled assertion.

---

**Read the skill spec.**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

Name the failure modes — what makes an output of this skill non-functional? For each failure mode:
1. Name the mechanism: why the failure breaks downstream use of this specific skill's output.
2. Name the causal observable: the specific thing whose absence IS the failure, not a proxy.

---

**Build the rubric.**

Write criteria satisfying the definitions above. Each criterion requires all five fields — no blanks, no "TBD":

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence — the argument. Must state what must be true AND establish the downstream consequence: "without X, Y fails because Z." If the Text does not include a downstream consequence statement, it fails the constitutive definition of a criterion Text and must be rewritten before the next criterion is drafted.
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence — the conclusion. Names the observable from the Text's argument. Uses count thresholds, named fields, structural patterns, or explicit enumerations. No "is clear" or "adequately covers" as the sole criterion.

Before finalizing each **essential** criterion, apply the structural sequence check:

> "If I read only the Pass condition, would I understand WHY that observable matters — what downstream failure its absence causes? Or does the Text merely label what must be present, leaving the causal chain implicit?"

If the Text only labels: rewrite the Text to include the downstream consequence ("without X, Y fails because Z") before naming X. The Pass condition should read as the inevitable conclusion of the Text's argument — not a standalone assertion that the Text happens to precede.

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. All three tiers required.

Essential: the Text-argued observable whose absence makes the output non-functional or misleading.
Recommended: pass condition tests a quality property — degree, precision, specificity — not just presence. The Text argues a degree or precision consequence.
Aspirational: goes beyond what essential and recommended require. Must not restate an essential.

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

Body: purpose statement (2-3 sentences — invoke the constitutive definitions: a criterion Text IS the argument establishing why the observable matters downstream; a Pass condition IS the conclusion of that argument; a structure that omits the argument is an assertion, not a criterion), then criteria ordered essential → recommended → aspirational, then scoring section.

---

## V-03 — Lifecycle Emphasis (Tier-as-Failure-Dimension)

**Axis:** Lifecycle emphasis
**Hypothesis:** C-13 requires category diversity to emerge from tier design, not from label-count compliance. A rubric achieves C-13 organically when each tier is assigned a distinct failure dimension — the kind of failure it was designed to catch — such that the categories naturally associated with that dimension are the ones that appear in those criteria, without consulting a category checklist. A rubric fails C-13 when the author assigns category labels after criteria are written to satisfy the count "at least 3 distinct categories." V-03 separates tier design from criteria writing: Phase 2 names the three failure dimensions and derives which categories they predict, before any criterion is written. Criteria then belong to their tier's failure dimension; category labels follow from the dimension rather than from the count. The hypothesis is that explicit tier-dimension design produces C-13-compliant rubrics at a higher rate than any framing that introduces category requirements post-hoc, because the category assignments are already structurally determined before criterion drafting begins.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

Before writing any criteria, design the tier structure from failure dimensions.

**PHASE 1: READ THE SKILL SPEC**

What does this skill produce? What lifecycle phases does it have? What does a complete correct output contain?

**PHASE 2: DESIGN THE TIER STRUCTURE**

A rubric with three tiers is most useful when each tier addresses a distinct failure dimension. If two tiers address the same failure dimension, clearing one tier tells you little about whether the other passes — the tiers become redundant rather than concentric.

Assign a failure dimension to each tier. For each tier, also predict which category from the allowed set is most likely to appear in that tier's criteria — derive the category from the failure dimension alone, not from any criterion you intend to write.

```
Essential tier
  Failure dimension: [The specific kind of failure that makes the output non-functional
    or misleading. Not "quality" — the structural or semantic property whose absence
    makes the output useless or produces incorrect downstream results. E.g., "required
    fields missing or untestable — the output cannot serve as an objective function
    because its pass conditions admit subjective judgment without observable anchors."]
  This tier catches: [Describe what an output looks like that fails only the essential
    tier. What is usable despite failing this?]
  Predicted majority category: [correctness | depth | format | coverage | behavior]
  Because: [one sentence explaining why this failure dimension naturally produces
    criteria in that category]

Recommended tier
  Failure dimension: [The specific kind of shortfall that makes an output passing but
    not good. Must be distinct from the essential failure dimension: an output can
    satisfy the essential dimension and still fail this one. E.g., "quality deficit —
    criteria pass structural checks but test presence, not quality properties; passing
    outputs are not reliably good outputs."]
  This tier catches: [Describe what an output looks like that passes essential but
    fails recommended.]
  Predicted majority category: [correctness | depth | format | coverage | behavior]
  Because: [one sentence]

Aspirational tier
  Failure dimension: [The specific kind of gap that makes an output good but not
    excellent. Must be distinct from both essential and recommended. E.g., "causal
    shallowness — criteria are anchored and skill-specific but their Text fields do
    not argue for the observable's causal role; the rubric catches the right things
    for the wrong reasons."]
  This tier catches: [Describe what an output looks like that passes essential and
    recommended but fails aspirational.]
  Predicted majority category: [correctness | depth | format | coverage | behavior]
  Because: [one sentence]
```

**Predictability check:** Given only the three failure dimension descriptions — without reading any criteria — could someone predict that each tier's majority category would be distinct? If two tiers share the same predicted majority category, the failure dimensions are not sufficiently distinct. Redesign until at least 2 of 3 tiers predict a different majority category.

DO NOT write any criteria until the predictability check passes.

**PHASE 3: WRITE ESSENTIAL CRITERIA (3-5)**

Write criteria for the essential tier's failure dimension. Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence. State what must be true AND include the downstream consequence: "without X, Y fails." The essential failure dimension should be audible in the Text.
- **Weight**: essential
- **Category**: assign the category that best names the essential tier's failure dimension. Use the predicted majority category from Phase 2 unless the specific criterion's failure is better described by another category — override explicitly if so.
- **Pass condition**: one auditable sentence using observable anchors. No "is clear", "adequately covers."

**PHASE 4: WRITE RECOMMENDED CRITERIA (2-3)**

Write criteria for the recommended tier's failure dimension. Weight: recommended. Each pass condition tests a quality property, not just presence. Assign category based on the recommended tier's predicted majority category from Phase 2.

**PHASE 5: WRITE ASPIRATIONAL CRITERIA (1-2)**

Write criteria for the aspirational tier's failure dimension. Weight: aspirational. Must go beyond what essential and recommended require. Assign category based on the aspirational tier's predicted majority category.

After writing aspirational criteria, apply the retrospective check:

> "Are the category assignments across each tier consistent with the predicted majority categories from Phase 2? If two tiers share the same majority category in the final criteria, either the criteria drifted from their tier's failure dimension (reassign) or the failure dimensions were too similar (redesign Phase 2)."

At least 2 of 3 tiers must have a majority category distinct from the other tiers' majority categories.

**PHASE 6: SCORING AND OUTPUT**

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

Body: purpose statement (2-3 sentences — state the tier-as-failure-dimension principle: category diversity is a consequence of tier design, not a label-count compliance; criteria that belong to a tier's failure dimension naturally concentrate in that dimension's associated category), then criteria ordered essential → recommended → aspirational (tier failure dimensions from Phase 2 may appear as section subheadings if they make the structure self-evident; otherwise omit), then scoring section.

---

## V-04 — Lifecycle Emphasis + Inertia Framing (Tier Dimensions + Reference Anchor)

**Axis:** Lifecycle emphasis (tier-as-failure-dimension) + inertia framing (aspirational-tier reference)
**Hypothesis:** V-03 grounds C-13 by explicitly designing tiers from failure dimensions before criteria are written. V-01 grounds C-11 by naming a near-excellent reference in the aspirational preamble. Combined: Phase 2 designs the tier structure from failure dimensions with a predictability check (C-13); Phase 3 names the near-excellent reference before the aspirational criteria are written (C-11). The combination closes both structural gaps simultaneously. C-12 is probed but not explicitly gated: the failure-dimension context established in Phase 2 may encourage causal Text fields because the tier's failure dimension already names the "why" that each criterion's Text should argue — but this is contextual pressure, not a structural check. The hypothesis is that the combination produces higher C-11 and C-13 compliance than either single-axis variation alone, and that the failure-dimension framing incidentally improves C-12 without requiring an explicit gate.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Build it structure-first: tier architecture from failure dimensions, then criteria from tiers, then aspirational reference before aspirational criteria.

**PHASE 1: READ THE SKILL SPEC**

What does the skill produce? What lifecycle phases does it have? What does a complete correct output contain? Name at least 3 failure modes — what makes an output non-functional?

**PHASE 2: DESIGN THE TIER STRUCTURE**

Before writing any criteria, assign a failure dimension and a predicted majority category to each tier:

```
Essential tier
  Failure dimension: [The property whose absence makes the output non-functional.
    Name the specific structural or semantic gap — not "quality."]
  Predicted majority category: [correctness | depth | format | coverage | behavior]
  Because: [one sentence — why this failure dimension naturally produces criteria
    in this category]

Recommended tier
  Failure dimension: [The property whose absence makes the output passing but not good.
    Must be distinct from essential: an output can satisfy essential and still fail this.]
  Predicted majority category: [correctness | depth | format | coverage | behavior]
  Because: [one sentence]

Aspirational tier
  Failure dimension: [The property whose absence makes the output good but not excellent.
    Must be distinct from both essential and recommended.]
  Predicted majority category: [correctness | depth | format | coverage | behavior]
  Because: [one sentence]
```

The three failure dimensions must be distinct. At least 2 of 3 tiers must predict a different majority category. If two tiers share the same predicted majority category, redesign the failure dimensions until they diverge.

DO NOT write criteria until Phase 2 is complete with distinct failure dimensions and divergent predicted categories.

**PHASE 3: NAME THE ASPIRATIONAL REFERENCE**

Before writing aspirational criteria, identify the near-excellent reference — an artifact, pattern, or class of rubrics that satisfies the essential and recommended failure dimensions but not the aspirational one.

```
Reference: [Name specifically — e.g., "a rubric built using the failure-mode-first
  table prompt (V-04, Round 2), which reliably passes C-01 through C-08 with anchored
  pass conditions and skill-specific criteria, but was built without tier-dimension
  design and without naming an aspirational reference point." Must be recognizable —
  not a hypothetical.]

Passes: [State which failure dimensions or criteria tiers the reference satisfies —
  essential and recommended explicitly.]

Fails: aspirational failure dimension — specifically: [Name what the reference lacks
  that the aspirational tier requires. This is the delta the aspirational criteria
  will measure.]
```

**PHASE 4: WRITE ESSENTIAL CRITERIA (3-5)**

Each criterion requires all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence. State what must be true AND include "without X, Y fails because Z." The essential failure dimension should be audible in the Text — the criterion should feel like it belongs to the essential tier's failure dimension.
- **Weight**: essential
- **Category**: assign based on the essential tier's predicted majority category. Override only if the specific criterion's failure clearly belongs to a different category.
- **Pass condition**: one auditable sentence using observable anchors. No qualitative language as sole criterion.

**PHASE 5: WRITE RECOMMENDED CRITERIA (2-3)**

Write criteria for the recommended tier's failure dimension. Weight: recommended. Each pass condition tests a quality property, not just presence. Assign category based on the recommended tier's predicted majority category.

**PHASE 6: WRITE ASPIRATIONAL CRITERIA (1-2)**

Write criteria for the aspirational tier's failure dimension. Each criterion addresses what the reference from Phase 3 lacks. May state: "A rubric that satisfies the essential and recommended failure dimensions — such as [reference] — but was built without [aspirational failure dimension] [fails this specific property] because [mechanism]."

Weight: aspirational. Must go beyond what essential and recommended require.

**PHASE 7: SCORING AND OUTPUT**

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

Body: purpose statement (2-3 sentences — state the tier-dimension design principle and name the near-excellent reference as what the aspirational tier is measured against), then criteria ordered essential → recommended → aspirational (tier failure dimension descriptions and aspirational reference preamble retained in artifact if they add clarity; Phase analysis notes omitted), then scoring section.

---

## V-05 — Role Sequence + Phrasing Register (Scrutineer Targeting C-11, C-12, C-13)

**Axis:** Role sequence (Builder + Scrutineer) + phrasing register (interrogative)
**Hypothesis:** Round 4 V-01 (Builder + Critic) targeted C-09 and C-10 with a narrow Critic scope: two properties, applied per criterion and per rubric, with specific revision instructions. That pattern produced reliable results because the Critic's interrogation was calibrated to exactly the properties being tested. V-05 applies the same two-role architecture to the three new aspirational criteria: the Scrutineer interrogates C-12 per essential criterion (does the Text argue before the Pass concludes?), C-13 for the rubric as a whole (could the tier categories be predicted from failure dimensions before criteria were written?), and C-11 for the aspirational section (is a recognizable near-excellent reference named?). Each interrogation produces a revision instruction if the property is not satisfied. The hypothesis is that calibrated post-draft interrogation of exactly the three new properties produces higher compliance than building those properties into the generation phase, because (a) the Builder's draft is unencumbered by all three requirements simultaneously, and (b) the Scrutineer's targeted questions produce precise revisions rather than generic improvement.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence: the Builder drafts the rubric, the Scrutineer interrogates three structural properties and issues revision instructions, and the Builder incorporates all required revisions. The final artifact reflects the post-revision state; Scrutineer notes do not appear in the output.

---

**BUILDER ROLE**

Read the skill spec. Extract:
1. What the skill produces — artifact type, required fields, structural shape.
2. Lifecycle phases — what each phase delivers.
3. At least 3 failure modes — what makes an output of this skill non-functional?

For each failure mode, draft one essential criterion with all five fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence stating what must be true in a passing output
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with an observable anchor — count thresholds, presence/absence of named fields, structural patterns, explicit enumerations. Phrases like "is clear", "seems appropriate", "adequately covers" are not observable anchors.

Draft 3-5 essential criteria. Then draft 2-3 recommended criteria (pass conditions test quality properties, not just presence) and 1-2 aspirational criteria (go beyond essential and recommended). Continue sequential C-NN numbering.

---

**SCRUTINEER ROLE**

The Scrutineer interrogates three properties of the Builder's draft. For each property, the Scrutineer applies a diagnostic question, evaluates the current state, and issues a specific revision instruction if the property fails. The Builder executes all revisions before writing the artifact.

**Interrogation 1 — C-12: Text-argues-before-Pass-concludes (applied per essential criterion)**

For each essential criterion (weight = essential):

> "If I read only the Pass condition, would I understand WHY that observable matters — what downstream failure its absence causes? Or does the Text only label what must be present, leaving the causal chain implicit?"

If the Text does not establish the downstream consequence of the observable's absence before the Pass condition names the observable:

```
C-NN Text revision required:
  Current Text: [quote as drafted]
  Issue: the Text labels what must be true without arguing why — the downstream
         consequence of the observable's absence is not stated before the Pass
         condition names the observable.
  Instruction: Rewrite the Text to state "without [observable], [specific failure]
               occurs because [mechanism]" — establishing the causal argument before
               the Pass condition invokes the observable as the testable conclusion.
               The Pass condition itself does not change; only the Text is revised.
```

**Interrogation 2 — C-13: Tier-grounded category diversity (applied to the rubric as a whole)**

> "For each tier, what failure dimension does it address — the specific kind of failure the tier was designed to catch? Given only that failure dimension description, could a reader predict which category would be most common in that tier's criteria — without reading any criteria? Or were the category labels assigned after criteria were written to hit a count?"

Evaluate:

```
Tier analysis:
  Essential tier — criteria categories: [list] — majority: [X]
    Could this be predicted from a failure dimension description? [yes/no]
  Recommended tier — criteria categories: [list] — majority: [Y]
    Could this be predicted from a failure dimension description? [yes/no]
  Aspirational tier — criteria categories: [list] — majority: [Z]
    Could this be predicted from a failure dimension description? [yes/no]
```

If two or more tiers share a majority category that appears post-hoc rather than derived from distinct failure dimensions:

```
Tier diversity revision required:
  Issue: [name which tiers have category assignments that appear label-assigned
          rather than failure-dimension-derived]
  Instruction: Add a tier-failure-dimension preamble before each affected tier's
               criteria. Format:
                 "This tier addresses [failure dimension]: [description of what
                 this tier was designed to catch that the other tiers do not].
                 Criteria in this tier are expected to fall in the [category]
                 category because [mechanism]."
               The preamble must make it possible to predict the tier's majority
               category from the failure dimension description alone. At least 2 of
               3 tiers must have a majority category distinct from the other tiers.
```

**Interrogation 3 — C-11: Aspirational reference anchor (applied to the aspirational section)**

> "Does the aspirational section name a specific reference — a prior artifact, a named pattern, or a class of rubrics that passes all essential and recommended criteria — against which the aspirational criteria are measured? Or does the aspirational section list abstract stretch goals without anchoring them to a near-excellent artifact that fails only the aspirational bar?"

If no specific reference is named, or the reference is too vague (e.g., "a hypothetical good rubric"):

```
Aspirational preamble required:
  Instruction: Before the first aspirational criterion, add a preamble:
    Reference: [Name specifically — e.g., "a rubric built using the failure-mode-first
               extended table method (V-03, Round 2), which reliably passes C-01
               through C-08 but was built without tier-failure-dimension design and
               names no causal argument in criterion Text fields." Must be specific
               enough that someone familiar with this skill's rubric history can
               identify it.]
    Passes: [State the essential and recommended criteria or failure dimensions
             the reference satisfies.]
    Fails: [Name the specific aspirational dimension(s) the reference lacks
            and why — the delta the aspirational criteria are designed to measure.]
```

After all three interrogations are complete and all revision instructions are addressed, the Builder writes the final artifact. Scrutineer interrogation notes are omitted; revisions are incorporated silently.

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

Body: purpose statement (2-3 sentences — state what the rubric evaluates and name the Scrutineer's three interrogation targets: Text-argues-before-Pass-concludes per essential criterion, tier-to-category predictability from failure dimensions, and aspirational reference anchoring against a near-excellent artifact), then criteria ordered essential → recommended → aspirational (tier failure dimension preambles and aspirational reference preamble retained if added by Scrutineer; revision notes omitted), then scoring section.
