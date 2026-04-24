# quest-rubric Variate — Round 5 (Round 2 against rubric v1 / first round against v5)
**Date:** 2026-03-15
**Rubric:** v5 (17 criteria)
**Criteria in scope:**
- Essential: C-01 (all 5 fields, count >= 6), C-02 (essential covers non-negotiable), C-03 (testable pass conditions), C-04 (formula + threshold), C-05 (>= 3 skill-specific)
- Recommended: C-06 (tier distribution), C-07 (>= 3 categories), C-08 (recommended tests quality)
- Aspirational: C-09 (aspirational distinguishes excellent from passing), C-10 (frontmatter), C-11 (causal linkage), C-12 (contrast example in at least 1 essential), C-13 (hard gate at checkpoints), C-14 (critical properties as required fields), C-15 (per-criterion gate), C-16 (slot semantic constraints), C-17 (traceable severity derivation)

**Design note:** R4 explored five mechanisms for producing C-09 (causal linkage) and C-10 (contrast examples): narrow Critic role (V-01), prose-spec format (V-02), definitional register (V-03), aspirational-tier competitor (V-04), and interrogative Examiner (V-05). C-09 and C-10 are now well-probed; R4 produced a clear winner pattern (Examiner interrogation + competitor inertia both reliably produce causal and skill-specific criteria). C-17 is the new aspirational criterion in v5: tier assignment must be traceable to a pre-authoring severity classification (blocking/degrading/cosmetic -> essential/recommended/aspirational). This round probes five mechanisms for producing C-17 compliance: a Severity Classifier role that runs before the Builder (V-01), a format that requires a severity-labeled failure mode table as the first mandatory section (V-02), a lifecycle emphasis that isolates Phase 0 as severity-classification-only with a hard gate (V-03), a definitional register that makes "essential" constitutively equal to "blocking" (V-04), and a combined lifecycle + inertia framing that names a Correct-Tier competitor — a rubric whose tier assignments happen to be right but are not derivable (V-05).

---

## Round 5 Variation Map

| Variation | Axis | C-17 probe | Notes |
|-----------|------|-----------|-------|
| V-01 | Role sequence (Classifier + Builder) | Strong -- Classifier enumerates failure modes and assigns severity labels in a dedicated role before Builder writes any criterion; tier assignment becomes a table lookup | Single-axis; risk: Classifier produces thorough enumeration but Builder ignores it when assigning tiers, so link between failure mode and criterion may not be explicit in output |
| V-02 | Output format (severity-labeled failure mode table) | Strong -- format structurally requires a failure-mode table with severity labels as the first section; each criterion references its root failure mode by ID, making derivation auditable by construction | Single-axis; risk: C-01 completion failures if the required failure-mode table section is skipped or abbreviated; format adds a section not in the standard five-field structure |
| V-03 | Lifecycle emphasis (Phase 0 severity classification, hard gate) | Moderate -- Phase 0 is explicitly scoped to severity classification only and blocked from proceeding until all failure modes have labels; but the link from Phase 0 output to criterion tier is still asserted by the author rather than structurally required | Single-axis; probes whether naming severity classification as a distinct phase (rather than an implied pre-step) produces better traceability than an implicit analysis step |
| V-04 | Phrasing register (definitional -- essential IS blocking) | Strong -- making "essential" constitutively equal to "blocks the output from functioning" reframes C-17 from a procedural step to a definitional requirement: a criterion labeled essential with no blocking failure mode is, by definition, not essential | Single-axis; risk: definitional framing is abstract; the model may satisfy the definition syntactically (by labeling everything blocking) without doing the actual severity classification |
| V-05 | Lifecycle emphasis + inertia framing (Correct-Tier competitor) | Very strong -- introduces a Correct-Tier competitor whose tier assignments happen to be correct but cannot be audited (no failure-mode enumeration); naming this competitor makes auditability a distinguishing property rather than a bonus, and requires the Builder to go beyond correctness to derivability | Combined; risk: identifying a competitor that is mostly correct may raise the question "why go further?" -- the prompt must clearly explain that C-17 is about audit, not correctness |

---

## V-01 -- Role Sequence (Classifier + Builder)

**Axis:** Role sequence
**Hypothesis:** The gap between a rubric that assigns tiers correctly and one whose tier assignments are auditable (C-17) is an enumeration gap, not a labeling gap. A Builder who labels tiers without a prior enumeration step may happen to be right but cannot be verified. A Severity Classifier who enumerates failure modes and assigns blocking/degrading/cosmetic labels before any criteria are written provides the derivation table that makes tier assignment mechanical. The Builder then reads the Classifier's table and maps severity labels to tiers: blocking -> essential, degrading -> recommended, cosmetic -> aspirational. The hypothesis is that making the Classifier's output a required input to the Builder -- not an optional analysis step -- produces tier assignments that are traceable by construction, because the Builder cannot write an essential criterion without a corresponding blocking failure mode in the Classifier's table.

---

You are building a scoring rubric for a Signal skill. Two roles operate in sequence. The Classifier enumerates failure modes and assigns severity labels. The Builder writes criteria from the Classifier's output. The Classifier's enumeration is a required input to the Builder's criteria; the Builder cannot assign a tier without citing a Classifier entry.

---

**CLASSIFIER ROLE**

Read the skill spec. Enumerate every failure mode -- every way an output of this skill can be non-functional, degraded, or cosmetically flawed.

For each failure mode, assign a severity label:

- **blocking** -- the output fails entirely if this failure mode is present. The output cannot serve its purpose.
- **degrading** -- the output is functional but materially diminished. It works, but worse.
- **cosmetic** -- the output serves its purpose but is less polished. Fixing it improves presentation, not function.

Write the Classifier output as a numbered list:

```
FAIL-01: [failure mode description] -- severity: blocking | degrading | cosmetic
FAIL-02: [failure mode description] -- severity: blocking | degrading | cosmetic
...
```

Minimum: 3 blocking failure modes, 2 degrading failure modes, 1 cosmetic failure mode. If fewer than 3 blocking failure modes exist, re-examine the spec -- a well-specified skill has at least 3 ways to fail entirely.

DO NOT proceed to the Builder role until the Classifier list contains at least 3 blocking, 2 degrading, and 1 cosmetic failure mode, each with a severity label.

---

**BUILDER ROLE**

The Builder writes criteria from the Classifier's enumeration. Every criterion must cite its root failure mode from the Classifier list.

Tier assignment is a lookup, not a judgment:
- blocking failure mode -> essential criterion
- degrading failure mode -> recommended criterion
- cosmetic failure mode -> aspirational criterion

Required fields for every criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence stating what must be true in a passing output
- **Weight**: essential | recommended | aspirational (derived from severity label of root failure mode)
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence using observable anchors -- count thresholds, presence/absence of named fields, structural patterns, explicit enumerations. Phrases like "is clear", "seems appropriate", "adequately covers" are not observable anchors.
- **Root failure mode**: FAIL-NN (the Classifier entry that motivated this criterion)

For at least one essential criterion: embed a contrast example in the Text field showing what a generic rubric for any skill would miss vs. what this criterion catches specifically -- "Not: '[generic formulation]' -- but: '[formulation naming a concrete property of {skill_target}'s output].'"

Tier targets: 3-5 essential (from blocking failure modes), 2-3 recommended (from degrading), 1-2 aspirational (from cosmetic). All three tiers required.

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

Body: purpose statement (2-3 sentences -- name the Classifier-Builder sequence and state that the Root failure mode field makes every tier assignment auditable: an evaluator can verify any essential criterion by finding FAIL-NN in the Classifier list and confirming its severity is "blocking"), then the Classifier enumeration (labeled "Failure Mode Enumeration"), then criteria ordered essential -> recommended -> aspirational with Root failure mode fields retained, then scoring section.

---

## V-02 -- Output Format (Severity-Labeled Failure Mode Table)

**Axis:** Output format
**Hypothesis:** Prior rounds enforced causal linkage (C-11) and skill-specificity (C-12) by adding required fields to each criterion row. C-17 requires a different kind of enforcement: it is not a property of a criterion in isolation but a property of the relationship between the criterion's tier label and a pre-authoring severity classification. This relationship cannot be encoded within the criterion fields alone -- it requires a separate section that precedes the criteria and is referenced by them. V-02 tests whether adding a mandatory failure-mode table (with severity labels) as the first required output section, and requiring each criterion to cite a row from that table, structurally enforces C-17 compliance in the same way that required column fields enforced C-14 compliance in earlier rounds. The probe: does a format-level requirement for a cross-referencing severity table produce more consistent C-17 compliance than a procedural instruction to do the classification?

---

You are writing a scoring rubric for a Signal skill. The rubric has two sections: a Failure Mode Registry followed by the criteria. The criteria reference the registry; the registry makes the tier assignments auditable.

Read the skill spec. Understand what the skill produces, what lifecycle phases it runs through, and what a complete correct output contains.

---

**SECTION 1 -- FAILURE MODE REGISTRY**

Before writing any criterion, build the Failure Mode Registry: a table of every way an output of this skill can fail, classified by severity.

| ID | Failure mode | Severity |
|----|-------------|---------|
| F-01 | [how this output can fail] | blocking \| degrading \| cosmetic |
| ... | | |

Severity definitions:
- **blocking** -- output is non-functional or misleading if this failure mode is present
- **degrading** -- output is functional but materially diminished
- **cosmetic** -- output serves its purpose but presentation suffers

Fill at least 6 rows. The registry is a required section -- leave it blank and the rubric is incomplete.

DO NOT proceed to Section 2 until the registry contains at least 3 blocking rows, 2 degrading rows, and 1 cosmetic row.

---

**SECTION 2 -- CRITERIA**

Write criteria from the Failure Mode Registry. Each criterion must cite the registry row it addresses.

Required fields for every criterion:

- **ID**: C-NN (sequential)
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended | aspirational (blocking -> essential, degrading -> recommended, cosmetic -> aspirational)
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with an observable anchor
- **Addresses**: F-NN (the registry row this criterion guards against)

The Addresses field makes the tier assignment derivable: weight is not asserted -- it is read from the severity column of the cited registry row.

For at least one essential criterion, add a contrast example to the Text field: "Not: '[formulation that could appear in a rubric for any skill]' -- but: '[formulation naming a concrete property of {skill_target}'s output].'"

Tier distribution: 3-5 essential (from blocking rows), 2-3 recommended (from degrading rows), 1-2 aspirational (from cosmetic rows). All three tiers required.

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

Body: purpose statement (2-3 sentences -- state what the rubric evaluates and that the Failure Mode Registry section makes every tier assignment traceable: weight is derived from severity, not asserted), then Section 1 (Failure Mode Registry table), then Section 2 (criteria with Addresses fields), then scoring section.

---

## V-03 -- Lifecycle Emphasis (Phase 0 Severity Classification, Hard Gate)

**Axis:** Lifecycle emphasis
**Hypothesis:** C-17 requires a pre-authoring severity classification step -- failure modes classified before criteria are written. Prior rounds used two phases (analysis -> criteria) or three (analysis -> essential -> recommended/aspirational). V-03 tests whether isolating severity classification as its own phase (Phase 0), scoped to nothing but failure mode enumeration and severity labeling, produces better C-17 compliance than treating classification as an analysis sub-task within a broader phase. Phase 0 is minimal by design: no criteria begin, no drafting happens, no structure is imposed beyond the failure mode list. The only gate out of Phase 0 is a severity label on every enumerated failure mode. The hypothesis is that when classification is scoped as a phase with a single exit condition (labeled failure modes), it gets done completely, whereas when classification is an analysis task within a broader phase, it is deprioritized or abbreviated.

---

You are building a scoring rubric for a Signal skill. The process has four phases. Phase 0 exists only to enumerate failure modes and classify their severity. Nothing else happens in Phase 0.

---

**PHASE 0 -- SEVERITY CLASSIFICATION**

Read the skill spec.

List every way an output of this skill can fail. For each failure mode, assign one severity label:
- **blocking** -- output is non-functional or misleading
- **degrading** -- output works but is materially diminished
- **cosmetic** -- output is functional; only presentation suffers

Format:
```
F-01: [failure mode] | blocking
F-02: [failure mode] | degrading
F-03: [failure mode] | cosmetic
...
```

No criteria. No drafting. Only failure modes and severity labels.

DO NOT proceed to Phase 1 until every failure mode has a severity label and the list contains at least 3 blocking, 2 degrading, and 1 cosmetic entry.

---

**PHASE 1 -- ESSENTIAL CRITERIA**

Draft essential criteria from the blocking failure modes in Phase 0.

Required fields for every criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- what must be true in a passing output. For at least one essential criterion, include a contrast example: "Not: '[generic formulation]' -- but: '[formulation naming a concrete property of {skill_target}'s output].'"
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence. Observable anchors only: count thresholds, named fields, structural patterns, explicit enumerations. No "is clear", "seems appropriate".
- **Severity source**: F-NN (the Phase 0 entry whose severity label justifies this tier)

Draft 3-5 essential criteria, one per blocking failure mode. The Severity source field must be non-blank. A blank Severity source field means the tier cannot be audited.

DO NOT proceed to Phase 2 until all essential criteria have a non-blank Severity source pointing to a blocking failure mode in the Phase 0 list.

---

**PHASE 2 -- RECOMMENDED AND ASPIRATIONAL CRITERIA**

Draft recommended criteria from degrading failure modes (2-3 criteria). Draft aspirational criteria from cosmetic failure modes (1-2 criteria). Use the same five-field structure plus Severity source.

Recommended criteria: pass conditions test quality properties -- degree, precision, specificity -- not just presence.
Aspirational criteria: go beyond what essential and recommended already require.

Continue sequential C-NN numbering. All three tiers required.

DO NOT finalize any criterion with a blank Severity source field.

---

**PHASE 3 -- SCORING AND OUTPUT**

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

Body: purpose statement (2-3 sentences -- name the Phase 0 severity classification step and state that Severity source fields make tier assignments auditable), then Phase 0 failure mode list (retained in output as the derivation record), then criteria ordered essential -> recommended -> aspirational (Severity source fields retained), then scoring section.

---

## V-04 -- Phrasing Register (Definitional -- Essential IS Blocking)

**Axis:** Phrasing register
**Hypothesis:** Earlier rounds used definitional register to encode causal linkage (R4 V-03): defining what a pass condition IS forced the causal requirement to be constitutive rather than procedural. V-04 applies definitional register to the tier assignment problem. If "essential" is defined as "guards against a blocking failure mode -- one whose presence makes the output non-functional or misleading -- and only that," then an essential criterion that cannot be traced to a blocking failure mode is not essential by definition; it is misclassified. This reframes C-17 from a procedural step (enumerate failure modes before writing criteria) to a constitutive requirement (the word "essential" cannot be truthfully applied without a blocking failure mode in scope). The hypothesis is that when the tier label is definitionally tied to the severity category, the model must resolve the severity classification to satisfy the definition -- not as an extra step, but as a prerequisite to using the word correctly.

---

You are building a scoring rubric for a Signal skill.

A rubric criterion is a named property of an output with five fields (ID, Text, Weight, Category, Pass condition) where the pass condition names an observable anchor -- a count, a named field, a structural pattern, or an enumeration -- that a third party can evaluate without subjective judgment.

**Essential** means: the criterion guards against a blocking failure mode -- a failure mode whose presence makes the output non-functional or misleading. Not "worse." Not "missing a nice-to-have." Non-functional or misleading. If you cannot name a blocking failure mode that the criterion guards against, the criterion is not essential. Label it recommended or aspirational.

**Recommended** means: the criterion guards against a degrading failure mode -- a failure mode whose presence makes the output functional but materially diminished. The pass condition tests a quality property: degree, precision, specificity. Not just whether a field exists.

**Aspirational** means: the criterion guards against a cosmetic failure mode -- a failure mode whose presence makes the output less polished but not less functional. Or: it captures an excellence pattern not reachable from the failure mode analysis alone.

These definitions are constitutive. A criterion labeled essential without a blocking failure mode is mislabeled. A criterion labeled recommended whose pass condition tests only presence (not quality) is mislabeled. The tier label is a claim about the failure mode, not a preference.

---

**Read the skill spec.**

Name the failure modes. For each, classify its severity: blocking, degrading, or cosmetic. Then write criteria that satisfy the definitions above.

For every criterion, fill in all five fields -- no blanks, no "TBD":

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence -- what must be true in a passing output
- **Weight**: essential | recommended | aspirational
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with an observable anchor

Before assigning a Weight of "essential" to any criterion, verify: "What is the blocking failure mode this criterion guards against? If I cannot name one, this criterion is not essential."

Before assigning a Weight of "recommended" to any criterion, verify: "Does the pass condition test a quality property -- not just whether the thing exists?"

For at least one essential criterion, embed a contrast example in the Text field showing what the skill-specific formulation adds over a generic one: "Not: '[generic formulation]' -- but: '[formulation naming a concrete property of {skill_target}'s output].'"

Tier targets: 3-5 essential (blocking), 2-3 recommended (degrading), 1-2 aspirational (cosmetic or excellence). All three tiers required.

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

Body: purpose statement (2-3 sentences -- invoke the definitional principle: "essential" means "guards against a blocking failure mode," so any essential criterion must be traceable to a named blocking failure mode or it is not essential by definition), then the failure mode severity classification (1-2 sentences per failure mode: name the mode and its severity, before the criteria), then criteria ordered essential -> recommended -> aspirational, then scoring section.

---

## V-05 -- Lifecycle Emphasis + Inertia Framing (Correct-Tier Competitor)

**Axis:** Lifecycle emphasis + inertia framing
**Hypothesis:** R4 named the Good Rubric -- a rubric that passes all essential and recommended criteria but lacks causal linkage (C-09) and contrast examples (C-10). Naming a near-excellent competitor created pressure toward the aspirational tier by making the aspirational properties visible as distinguishing features. V-05 applies the same mechanism to C-17, introducing the Correct-Tier Rubric: a rubric whose tier assignments happen to be correct -- every essential criterion guards a genuine non-negotiable, every recommended criterion captures a real quality property -- but which has no failure mode enumeration in its record. The Correct-Tier Rubric's tier assignments cannot be audited. A reviewer cannot trace any essential criterion back to a blocking failure mode because no enumeration was done; the author simply labeled criteria and happened to get the tiers right. The Correct-Tier Rubric passes C-01 through C-16 and fails C-17 only. By naming this competitor and asking at each phase "would the Correct-Tier Rubric have this?" the prompt forces the builder to go beyond correctness to auditability -- producing the derivation record that C-17 requires.

---

You are building a scoring rubric for a Signal skill. Your rubric has one competitor.

**The Correct-Tier Rubric.** Pass conditions are sharp and observable. Criteria are skill-specific. Tier distribution is balanced. Formula is present. Gates are in place. From the outside, it is an excellent rubric. But its author assigned tier labels by judgment, not by derivation. There is no failure mode enumeration in the record. A reviewer who asks "why is this criterion essential?" gets "because the author said so." The Correct-Tier Rubric passes every criterion in this rubric except one: its tier assignments cannot be audited because no pre-authoring severity classification was done. Your rubric must go further.

---

**PHASE 1 -- FAILURE MODE ENUMERATION**

Read the skill spec. List every failure mode -- every way an output of this skill can fail. For each, assign a severity:
- **blocking** -- output is non-functional or misleading
- **degrading** -- output functions but is materially worse
- **cosmetic** -- output functions; only presentation suffers

```
F-01: [failure mode] | blocking
F-02: [failure mode] | degrading
...
```

Would the Correct-Tier Rubric have done this step? No -- it assigned tiers by judgment. This enumeration is what makes your tier assignments auditable where the Correct-Tier Rubric's are not.

Minimum: 3 blocking, 2 degrading, 1 cosmetic. DO NOT proceed to Phase 2 until the list is complete.

---

**PHASE 2 -- CRITERIA**

Write criteria from the failure mode list. Every criterion cites its root failure mode.

Required fields:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: one sentence. For essential criteria where the skill-specific formulation is non-obvious, add a contrast example: "Not: '[generic formulation]' -- but: '[formulation naming a concrete property of {skill_target}'s output].'"
- **Weight**: essential | recommended | aspirational (derived from severity: blocking -> essential, degrading -> recommended, cosmetic -> aspirational)
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: one auditable sentence with an observable anchor
- **Root failure mode**: F-NN

After drafting each criterion, apply the Correct-Tier test:

> "Could the Correct-Tier Rubric have written this exact criterion -- same tier, same pass condition -- without having done the Phase 1 enumeration? If yes, the tier assignment is still correct but not yet auditable. The Root failure mode field is what changes that."

The Root failure mode field must be non-blank. A blank Root failure mode field means your rubric is indistinguishable from the Correct-Tier Rubric on this criterion.

Draft 3-5 essential, 2-3 recommended, 1-2 aspirational. All three tiers required.

DO NOT finalize any criterion without a non-blank Root failure mode field.

---

**PHASE 3 -- SCORING AND OUTPUT**

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

Body: purpose statement (2-3 sentences -- name the Correct-Tier competitor and state that the Phase 1 enumeration and Root failure mode fields are what separate this rubric from it: the tier assignments are not just correct, they are derivable), then Phase 1 failure mode list (retained as the derivation record), then criteria ordered essential -> recommended -> aspirational with Root failure mode fields retained (Correct-Tier test notes omitted, contrast examples retained), then scoring section.
