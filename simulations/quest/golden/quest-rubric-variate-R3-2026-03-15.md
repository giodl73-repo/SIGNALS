# quest-rubric Variate — Round 3
**Date:** 2026-03-15
**Rubric:** v3 (adds C-13: protocol hard gate at quality checkpoints; C-14: critical properties structurally enforced as required fields with format templates)
**Target criteria:** C-13 and C-14 (new aspirational criteria from v3, not tested in Rounds 1 or 2)

**Round 3 design note:** Round 2 probed C-11 (causal linkage) and C-12 (worked example in criterion text) through five mechanisms: three-link causal chains (V-01), a single hard gate before the contrast step (V-02), extended table columns (V-03), conversational causal interrogation (V-04), and an anti-generic contrast test (V-05). Round 2 found that V-02 demonstrated C-13 but not C-14 (gate present, no column constraint); V-03 demonstrated C-14 but not C-13 (column enforces presence, no blocking gate language). Round 3 probes whether either mechanism can be strengthened and whether combining them with new axes produces outputs that satisfy both C-13 and C-14 simultaneously.

**C-13 probe requirement:** The generated protocol must contain at least one statement matching "DO NOT proceed [to X] until [verifiable condition Y]" or equivalent blocking form. The gated condition must correspond to an essential or aspirational property.

**C-14 probe requirement:** The generated rubric format must include at least one dedicated required sub-field or column for a critical property (causal link, contrast example, or skill-specific formulation), with an explicit non-blank constraint and a format template specifying the *shape* of the required value (not just its presence).

---

## Round 3 Variation Map

| Variation | Axis | C-13 probe | C-14 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Lifecycle emphasis (systematic multi-gate) | Very strong — one hard gate per critical property, each requires a named gate artifact | Moderate — gate artifacts implicitly enforce structure but no column template | Single-axis; each gate tests a different property; risk: procedural overhead displaces analytical depth |
| V-02 | Output format (sub-field schema with format templates) | Moderate — no explicit blocking gate language, but template mismatch = format error | Very strong — every criterion is a structured block with labeled sub-fields specifying the *shape* of the required value | Single-axis; template enforcement at sub-field level, not just column presence; risk: template rigidity suppresses emergent criterion properties |
| V-03 | Phrasing register (contractual constraint-declaration) | Moderate — contract declarations carry implicit blocking force ("REQUIRED: non-blank") | Strong — contract form annotates each required property with format and constraint; missing field = syntax error | Single-axis; shifts mental model from advisory to contractual; risk: contract register displaces analytical reasoning needed for criterion quality |
| V-04 | Lifecycle emphasis + role sequence (verification phase as dedicated gate) | Very strong — explicit VERIFICATION phase with gate checklist; output-writing phase cannot begin until checklist clears | Moderate — checklist enforces presence; no format template for value shape | Combined; gate is a first-class phase, not inline instruction; strongest structural probe for C-13 |
| V-05 | Output format + inertia framing (anti-skip schema) | Strong — "discipline-dependent rubric" competitor motivates gate language; anti-skip test applied to each critical field | Strong — required sub-fields motivated by inertia test; format template required to survive anti-skip pressure | Combined; names the competitor whose properties are skippable, then requires both gates and templates to beat it; probes whether naming the failure mode produces the mechanism |

---

## V-01 — Lifecycle Emphasis (Systematic Multi-Gate)

**Axis:** Lifecycle emphasis
**Hypothesis:** Round 2 V-02 placed a single hard gate before the contrast example step. V-01 places a hard gate at each critical property checkpoint — after failure mode enumeration, after causal chain construction, after contrast example embedding — and requires each gate to produce a named gate artifact that proves the condition is satisfied before the next phase begins. Systematic gating across all critical properties is the direct probe for C-13 applied broadly. The gate artifacts (FAILOUT, CHAINOUT, CONTRASTOUT) also serve as reference material for criterion drafting, making the gates load-bearing rather than ceremonial. The risk is that three gate artifacts create overhead that displaces criterion quality; the hypothesis is that the forced artifacts produce better essential criteria because they are pre-computed from analysis rather than drafted in real time.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden — it must be complete, testable, and anchored to the specific failure modes of the target skill.

Three properties make a rubric excellent rather than merely passing: causal linkage (pass conditions name the observable whose absence IS the failure, not a symptom), specificity (criteria can only apply to this skill, not any document), and structural completeness (no field blank or TBD). Each of these properties has a hard gate below. A gate is a stopping condition with a verifiable test — not a reminder.

**PHASE 1 — ENUMERATE FAILURE MODES**

Read the skill spec. For each lifecycle phase of the skill, name what breaks if the phase produces wrong output. Write a failure mode list:

```
FAIL-01: [what is missing or wrong in the output] — [why this makes the output non-functional or misleading]
FAIL-02: ...
FAIL-03: ...
```

Minimum 3 failure modes. Each must be concrete and skill-specific — name the artifact property or structural element that is absent or malformed, not a generic quality observation.

**GATE 1:** Write the FAILOUT artifact:
```
FAILOUT:
  failure_count: [N]
  all_specific: [yes/no — do all failure modes name a concrete property of this skill's output?]
  generic_failures_removed: [yes/no — are observations like "output is low quality" excluded?]
```

DO NOT proceed to Phase 2 unless `failure_count >= 3` and `all_specific: yes`.

---

**PHASE 2 — CONSTRUCT CAUSAL CHAINS**

For each failure mode in FAILOUT, write a three-link causal chain:

```
CHAIN-NN:
  (1) Failure: [from FAIL-NN — verbatim or tightened]
  (2) Mechanism: [why that absence breaks downstream use — name the specific downstream operation that fails]
  (3) Observable: [the specific thing a third party can check whose absence directly instantiates (1) — not a symptom]
```

The observable in link (3) is the thing whose absence IS the failure mode — not a correlate, not a symptom, but the condition that, if present, would have prevented the failure. A pass condition derived from link (3) tests the observable that matters, not a proxy for it.

**GATE 2:** Write the CHAINOUT artifact:
```
CHAINOUT:
  chain_count: [N]
  all_causal: [yes/no — does every observable in link (3) directly instantiate the failure in link (1)?]
  proxy_observables_removed: [yes/no — are observables that merely correlate with the failure excluded?]
```

DO NOT proceed to Phase 3 unless `chain_count >= 3` and `all_causal: yes` and `proxy_observables_removed: yes`.

---

**PHASE 3 — DRAFT ESSENTIAL CRITERIA WITH CONTRAST EXAMPLES**

For each causal chain from CHAINOUT, write one essential criterion. The pass condition is link (3) from the chain — verbatim or tightened, not weakened.

For each essential criterion, embed a contrast example in the criterion Text field:

> "Not: '[generic formulation that could apply to any document]' — but: '[skill-specific formulation naming a concrete property of {skill_target}'s output].'"

The generic formulation must be one that the vague rubric would use. The skill-specific formulation must be derivable only from this skill's output structure.

Each criterion requires all five fields:

- **ID**: C-01, C-02, ... (sequential)
- **Text**: one sentence + embedded contrast example
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: the observable from CHAINOUT link (3), stated as one auditable sentence

**GATE 3:** Write the CONTRASTOUT artifact:
```
CONTRASTOUT:
  criteria_count: [N]
  all_fields_complete: [yes/no — do all criteria have all five fields with no blanks?]
  contrast_examples_embedded: [yes/no — does every essential criterion's Text field contain a contrast example?]
  skill_specific_formulations: [yes/no — does every skill-specific formulation name a property derivable only from this skill?]
```

DO NOT proceed to Phase 4 unless `all_fields_complete: yes` and `contrast_examples_embedded: yes` and `skill_specific_formulations: yes`.

---

**PHASE 4 — RECOMMENDED AND ASPIRATIONAL CRITERIA**

Recommended (2-3): What separates a passing output from a good one? Each pass condition tests a quality property — precision, degree, specificity — not pure presence/absence. Continue sequential C-NN numbering.

Aspirational (1-2): What separates a good output from an excellent one? Must go beyond what essential and recommended require. An aspirational criterion that restates an essential in different words fails this tier.

All three tiers required. Verify before proceeding.

---

**PHASE 5 — SCORING AND OUTPUT**

Write the composite formula:

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

Body: purpose statement (2-3 sentences stating what the rubric evaluates and why gate-enforced analysis matters), then criteria ordered essential → recommended → aspirational (gate artifacts omitted from final output, contrast examples retained in Text fields), then scoring section.

---

## V-02 — Output Format (Sub-field Schema with Format Templates)

**Axis:** Output format
**Hypothesis:** Round 2 V-03 added "Causal link" and "Contrast example" as table columns — enforcing presence but not the *shape* of the value. A blank cell is a format error; a poorly-formed cell is not. V-02 goes further: each criterion is a structured block with labeled sub-fields that include a format template specifying what a valid value looks like. A sub-field that doesn't match its template is a format error regardless of content quality. This encodes C-14's "blank cell = format error" at the shape level: not just "write something here" but "write something in this form." The risk is that template rigidity produces syntactically correct but semantically shallow values — operators satisfy the template pattern without satisfying the underlying analytical requirement.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden.

**Inputs:** skill spec (required), sample outputs (optional).

**Analysis**

Read the skill spec. Identify:
- What the skill produces: artifact shape, required fields, content structure.
- Lifecycle phases: what each phase delivers.
- Failure modes: what makes an output of this skill non-functional? Minimum 3.

**Criteria format**

Each criterion is a structured block. All sub-fields are required for every criterion. A sub-field that is blank, "N/A", or does not match its format template is a format error.

```
### C-NN — [Name]

ID: C-NN
Text: [one sentence — what must be true in a passing output]
Weight: essential | recommended | aspirational
Category: correctness | depth | format | coverage | behavior
Pass condition: [one auditable sentence — count threshold, named field, structural pattern, or enumeration. No "is clear", "seems appropriate", "adequately covers".]
Causal link: [REQUIRED for essential and recommended. Format: "If [observable in pass condition] is absent, then [specific downstream operation] fails because [mechanism]."]
Contrast example: [REQUIRED for essential criteria only. Format: "(generic: '[formulation applicable to any document]'; skill-specific: '[formulation naming a concrete property of {skill_target}'s output]')"]
```

Sub-field constraints:

- **Causal link**: Must follow the template exactly. "If [X] is absent, then [Y] fails because [Z]." X is the observable from the pass condition. Y is a named downstream operation. Z is the causal mechanism. A causal link that does not name a specific downstream operation fails the template.
- **Contrast example**: Must follow the template exactly. "(generic: '...'; skill-specific: '...')" The skill-specific formulation must name a property that is specific to {skill_target}'s output — not a generic quality attribute that applies to any rubric.
- **Pass condition**: Must use observable anchors (count thresholds, named fields, structural patterns, enumerations). Purely qualitative language with no anchor fails this sub-field.

Tier rules:
- Essential (3-5): absence makes the output non-functional. All six sub-fields required. Causal link and contrast example must satisfy their templates.
- Recommended (2-3): pass condition tests quality property, not just presence. Five sub-fields required (no contrast example). Causal link required.
- Aspirational (1-2): goes beyond essential and recommended. Five sub-fields required except causal link is optional. Must not restate an essential criterion.

**Scoring section**

After all criteria blocks, write:

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

Body: purpose statement (2-3 sentences — state what the rubric evaluates and name the template-enforcement principle: "a sub-field that doesn't match its template is a format error, not a compliance failure"), then criteria blocks (essential → recommended → aspirational), then scoring section.

---

## V-03 — Phrasing Register (Contractual Constraint-Declaration)

**Axis:** Phrasing register
**Hypothesis:** Rounds 1–2 used instructional register ("write this", "use this format") and conversational register ("what breaks?", "what matters?"). V-03 uses contractual register: the rubric output specification is presented as a formal contract where each required property is declared with a non-blank constraint annotation. The contract form shifts the mental model from "I should include X" to "X must be non-blank or this output is invalid." This directly maps to C-14's "format-enforced rather than discipline-enforced" language — a contract that says REQUIRED: non-blank is functionally a structural constraint, even without a table column. The implied blocking force of "REQUIRED" also probes C-13: the contract treats missing required fields as stopping conditions, even without explicit "DO NOT proceed" language. The risk is that contract language is bureaucratic and suppresses the analytical reasoning needed to surface good criterion content; the hypothesis is that the constraint-declaration form compensates by making missing fields syntactically obvious.

---

You are building a scoring rubric for a Signal skill. This document specifies the contract your output must satisfy. Read it as a contract: every REQUIRED field must be non-blank, and every FORMAT constraint defines what a valid value looks like. A missing REQUIRED field or a value that violates its FORMAT is a contract breach — not a style preference.

**CONTRACT: INPUT**

```
REQUIRED: skill spec
  FORMAT: a methodology document describing what the skill does, its lifecycle phases, and what a complete correct output contains
OPTIONAL: sample outputs
  PURPOSE: calibrate pass condition thresholds
```

**CONTRACT: ANALYSIS (not written to output)**

Before writing any criteria, complete the following analysis. This analysis is not part of the output artifact, but it is REQUIRED to produce the output.

```
REQUIRED: failure_modes
  FORMAT: list of 3+ items, each naming a concrete property of {skill_target}'s output that is absent or malformed, and why that makes the output non-functional
  CONSTRAINT: generic observations ("output is low quality") are not valid failure modes

REQUIRED: causal_observables
  FORMAT: one observable per failure mode, following the form "absence of [X] directly instantiates [failure mode]" — not a symptom, not a correlate
  CONSTRAINT: observables must be auditable by a third party without subjective judgment
```

**CONTRACT: OUTPUT — CRITERIA**

Each criterion must satisfy this contract. Every field is REQUIRED. Every FORMAT constraint applies.

```
REQUIRED: id
  FORMAT: C-NN where NN is a two-digit sequential integer starting at 01

REQUIRED: name
  FORMAT: 2–5 word noun phrase identifying the property being evaluated

REQUIRED: text
  FORMAT: one sentence stating what must be true in a passing output
  ADDITIONAL CONSTRAINT for essential criteria: text must include an embedded contrast example
    FORMAT: "Not: '[generic formulation]' — but: '[skill-specific formulation naming a concrete property of {skill_target}'s output].'"
    CONSTRAINT: generic formulation must be applicable to any document; skill-specific formulation must be derivable only from {skill_target}'s output structure

REQUIRED: weight
  FORMAT: one of — essential | recommended | aspirational
  CONSTRAINT: 3–5 essential, 2–3 recommended, 1–2 aspirational; all three tiers present

REQUIRED: category
  FORMAT: one of — correctness | depth | format | coverage | behavior

REQUIRED: pass_condition
  FORMAT: one auditable sentence using observable anchors (count threshold, named field, structural pattern, explicit enumeration)
  CONSTRAINT: the following phrases are contract violations and must not appear — "is clear", "seems appropriate", "adequately covers", "looks good"

REQUIRED for essential and recommended: causal_link
  FORMAT: "If [observable from pass_condition] is absent, then [named downstream operation] fails because [mechanism]."
  CONSTRAINT: [observable] must be the observable named in pass_condition; [downstream operation] must be named specifically, not described generically; [mechanism] must explain causality, not restate correlation
```

**CONTRACT: OUTPUT — SCORING**

```
REQUIRED: composite_formula
  FORMAT: composite = (essential_pass / N_essential * 60) + (recommended_pass / N_recommended * 30) + (aspirational_pass / N_aspirational * 10)
  CONSTRAINT: N_essential, N_recommended, N_aspirational must match the count of criteria at each tier

REQUIRED: golden_threshold
  FORMAT: "Golden threshold: all essential criteria pass AND composite >= 80."
```

**CONTRACT: OUTPUT — ARTIFACT**

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

```
REQUIRED: frontmatter
  FORMAT:
    skill: quest-rubric
    skill_target: {the skill being evaluated}
    date: {today's date in ISO-8601 format}
    version: 1

REQUIRED: purpose_statement
  FORMAT: 2–3 sentences stating what the rubric evaluates and naming the contract-enforcement principle (that required fields with format templates are structurally enforced, not discipline-dependent)

REQUIRED: criteria_blocks
  FORMAT: essential first (C-01 through C-NN), then recommended, then aspirational; each criterion as a section with all fields labeled

REQUIRED: scoring_section
  FORMAT: composite formula and golden threshold, verbatim from the CONTRACT: OUTPUT — SCORING section above
```

---

## V-04 — Lifecycle Emphasis + Role Sequence (Verification Phase as Dedicated Gate)

**Axis:** Lifecycle emphasis + role sequence
**Hypothesis:** Round 2 V-02 used inline DO NOT gates — blocking language embedded within a phase. V-04 goes further: the gate is a first-class VERIFICATION phase that sits between criterion drafting and output writing. The verification phase has an explicit checklist; no output is written until all checklist items are ticked. This differs from V-01's gate artifacts in that the gate is a named role/phase in the sequence (a "verifier" operating after the "analyst"), not an inline stopping condition. The verifier role has a fixed scope: for each essential criterion, verify causal linkage, verify contrast example embedded, verify skill-specific formulation. The hypothesis is that making gate-satisfaction a phase boundary — rather than an inline check — is the strongest structural probe for C-13, because the phase boundary is visible in the document structure rather than buried in phase text. The risk is that a separate verification phase produces redundant overhead for operators who already satisfied the properties in Phase 2; the hypothesis is that the redundancy is worth it because the verification produces an explicit signed checklist that cannot be satisfied by approximate compliance.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden — it must be complete, testable, and anchored to the actual failure modes of the target skill.

The protocol has four phases. Phase 3 (VERIFICATION) cannot begin until Phase 2 is complete. Phase 4 (OUTPUT) cannot begin until Phase 3 is complete. These are phase boundaries, not suggestions.

**PHASE 1 — ANALYSIS**

Read the skill spec. Extract:

1. What the skill promises to produce: the artifact type, required fields, structural shape of a complete correct output.
2. The lifecycle phases: what each phase delivers.
3. Failure modes (minimum 3): what makes an output of this skill non-functional or misleading? Name the specific property of the output that is absent or malformed — not a generic quality observation.

For each failure mode, write the observable: the specific thing whose absence IS the failure, not a symptom or correlate of it.

Write the failure mode list before proceeding to Phase 2:
```
FAIL-01: [property absent or malformed] — [why non-functional] — [observable: absence of X is the failure]
FAIL-02: ...
FAIL-03: ...
```

**PHASE 2 — CRITERION DRAFTING**

For each failure mode, draft one essential criterion. The pass condition is the observable from FAIL-NN — verbatim or tightened.

For each essential criterion, embed a contrast example in the Text field:

> "Not: '[generic formulation]' — but: '[skill-specific formulation naming a concrete property of {skill_target}'s output].'"

Each criterion requires all five fields: ID (C-NN sequential), Text (with embedded contrast example for essential criteria), Weight (essential), Category (correctness | depth | format | coverage | behavior), Pass condition (auditable sentence using observable anchors — no "is clear", "seems appropriate", "adequately covers").

After essential criteria (3-5), draft recommended criteria (2-3) and aspirational criteria (1-2) using the same five-field structure. Recommended pass conditions test quality properties, not presence. Aspirational criteria go beyond essential and recommended.

**PHASE 3 — VERIFICATION**

DO NOT proceed to Phase 4 until this checklist is complete.

For each essential criterion (C-01 through C-NN where Weight = essential), verify:

```
[ ] C-NN causal linkage: Does the pass condition name the observable whose absence IS the failure mode — not a symptom?
    Test: "If this observable were present, would it have prevented the failure mode entirely?"
    If no: return to Phase 2 and revise the pass condition.

[ ] C-NN contrast example: Does the Text field contain a "Not: '...' — but: '...'" contrast example?
    Test: "Could the Text field be copied unchanged into a rubric for a different skill?"
    If yes: the skill-specific formulation is not specific enough — return to Phase 2 and revise.

[ ] C-NN skill-specific formulation: Does the skill-specific half of the contrast example name a property derivable only from {skill_target}'s output?
    Test: "Would this formulation pass for a rubric about any other skill if only the skill name were changed?"
    If yes: return to Phase 2 and name a more specific property.
```

After completing the checklist for all essential criteria, write the VERIFICATION SUMMARY:

```
VERIFICATION SUMMARY:
  essential_criteria_verified: [N]
  causal_linkage_passed: [N of N]
  contrast_examples_embedded: [N of N]
  skill_specific_formulations_verified: [N of N]
  status: PASS | FAIL
```

DO NOT proceed to Phase 4 unless `status: PASS`.

**PHASE 4 — OUTPUT**

Write the composite formula:

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

Body: purpose statement (2-3 sentences — state what the rubric evaluates and name the verification-phase principle: "the verifier's checklist is the gate; Phase 4 cannot begin until Phase 3 status is PASS"), then criteria ordered essential → recommended → aspirational (VERIFICATION SUMMARY omitted from final output, contrast examples retained in Text fields), then scoring section.

---

## V-05 — Output Format + Inertia Framing (Anti-skip Schema)

**Axis:** Output format + inertia framing
**Hypothesis:** Round 1 V-05 used the vague rubric as a status-quo competitor to sharpen pass conditions. Round 2 V-05 extended this to the anti-generic test. Round 3 V-05 names a third competitor: the discipline-dependent rubric — one whose critical properties (causal link, contrast example, skill-specific formulation) are present only when the operator remembered to include them, not because the format required it. The discipline-dependent rubric satisfies the essential criteria on its best day; it fails them on a bad day. The prompt uses this competitor to motivate both C-13 (gates prevent skipping under pressure) and C-14 (required sub-fields make skipping a format error regardless of attention). The output schema combines the sub-field template approach from V-02 with an explicit "anti-skip test" applied to each critical sub-field, asking: "could an inattentive operator produce a valid output without filling this field?" If yes, the field must be made structurally required. The hypothesis is that naming the discipline-dependent rubric as a failure mode — rather than just poor practice — produces both the schema enforcement and the gate language that C-13 and C-14 require.

---

You are building the objective function for a Signal skill. Your rubric has three competitors to beat.

**Competitor 1: The Vague Rubric.** Pass conditions that say "the output is clear and well-organized." Cannot be evaluated by a third party. Fails C-03 (testable pass conditions).

**Competitor 2: The Generic Rubric.** Specific pass conditions that apply to any document. "Contains at least 5 criteria with all five fields" passes for a rubric about any skill. Fails C-05 (criteria targeted to skill).

**Competitor 3: The Discipline-Dependent Rubric.** It has specific, skill-targeted criteria on its best day — but causal linkage is present only if the operator remembered to write it, contrast examples only if they had time, skill-specific formulations only if they were careful. On a bad day, these properties are absent and the rubric still passes structural checks because nothing in the format requires them. The discipline-dependent rubric cannot be distinguished from an excellent rubric by format inspection alone.

Your rubric must make all three competitors fail. That means: pass conditions sharp enough that Competitor 1 fails, criteria specific enough that Competitor 2 fails, and a schema strict enough that Competitor 3 fails even on a bad day.

**Read the skill spec.**

What does this skill promise? What does a complete correct output contain? For each lifecycle phase, what does passing look like?

**PHASE 1 — ENUMERATE FAILURE MODES**

Name at least 3 failure modes — what makes this skill's output non-functional? For each, apply the observable test: what is the specific thing whose absence IS this failure? Not a symptom. The thing that, if present, prevents the failure.

Write explicitly before proceeding:
```
FAIL-01: [what breaks] — [observable: absence of X is the failure]
FAIL-02: ...
FAIL-03: ...
```

**PHASE 2 — DRAFT ESSENTIAL CRITERIA**

Convert each failure mode into an essential criterion with all five fields. The pass condition is the observable from Phase 1.

After drafting each essential criterion, apply three tests before finalizing:

**Inertia test (anti-vague):** Could Competitor 1's rubric ("the output is clear and comprehensive") still pass this condition? If yes, sharpen the anchor.

**Generic test (anti-generic):** Could Competitor 2's rubric pass this criterion for a different skill by swapping only the skill name? If yes, embed a contrast example in the Text field:
> "Not: '[generic formulation]' — but: '[skill-specific formulation naming a concrete property of {skill_target}'s output].'"

**Anti-skip test (anti-discipline-dependent):** Could Competitor 3's rubric produce a syntactically valid criterion without the causal link or contrast example? If yes, make these sub-fields structurally required by encoding them in the output schema with explicit format templates.

For essential criteria, the required sub-field schema is:

```
Text: [one sentence + embedded contrast example — "Not: '...' — but: '...'"]
Pass condition: [auditable sentence with observable anchor]
Causal link: [REQUIRED — "If [observable] is absent, then [named operation] fails because [mechanism]."]
```

A criterion block that omits the Causal link sub-field, or writes it in a form that does not follow the template, fails the anti-skip test and must be revised before finalization.

DO NOT finalize an essential criterion until all three tests pass.

**PHASE 3 — RECOMMENDED AND ASPIRATIONAL CRITERIA**

Recommended (2-3): Apply the inertia test to each recommended criterion's pass condition. A presence-only pass condition fails the inertia test. Causal link sub-field required.

Aspirational (1-2): Must go beyond essential and recommended. Must not restate an essential criterion.

Continue sequential C-NN numbering. All three tiers required.

**PHASE 4 — SCORING AND OUTPUT**

Write the composite formula:

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

Body: purpose statement (2-3 sentences — name all three competitors and state that the anti-skip schema is what defeats Competitor 3), then criteria ordered essential → recommended → aspirational (with sub-fields rendered as labeled lines within each criterion block, contrast examples embedded in Text fields, causal links as labeled sub-fields), then scoring section.
