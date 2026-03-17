Now I have the full context. Writing the Round 4 variations now.

---

# quest-rubric Variate — Round 4
**Date:** 2026-03-16
**Rubric:** v4 (adds C-15: specificity mechanism must produce a scoreable criterion; C-16: required field declarations must have a structural home)
**Target criteria:** C-15 and C-16 (new aspirational criteria in v4, untested in prior rounds)

**Round 4 design note:** Round 3 probed C-13 (protocol hard gate) and C-14 (critical properties structurally enforced as required fields with format templates). Round 3 V-04 and V-05 demonstrated both C-13 and C-14 simultaneously; V-05 achieved 79.3 — the highest composite to date, one miss (C-10). Round 4 targets two new v4 criteria. C-15 captures the pattern where a prompt-level specificity mechanism (a prohibition, an input-analysis gate) stops short of generating a scoreable criterion in the output rubric. C-16 captures the pattern where required fields are stated as obligations in instructions but have no structural home in the output schema — making them undiscoverable by inspection. The universal miss (C-10: scoring formula includes partial credit) is probed in V-05.

**C-15 probe requirement:** The variation prompt must produce an output rubric that contains at least one criterion testing whether the output rubric is specific to the target skill. That criterion must be a testable property of the output (pass/fail evaluable from the artifact), not a prohibition ("avoid generic criteria") or an input-analysis step ("check if the spec defines X"). The probe succeeds if the variation causes the builder to convert a specificity mechanism into a scoreable criterion.

**C-16 probe requirement:** Every field declared REQUIRED in the variation prompt must be mapped to a named structural location in the output schema (frontmatter, criterion block, scoring section, purpose statement). A REQUIRED field with no structural home in the output template fails C-16. The probe succeeds if the variation's output template anchors all required fields to locatable sections.

---

## Round 4 Variation Map

| Variation | Axis | C-15 probe | C-16 probe | C-10 probe | Notes |
|-----------|------|-----------|-----------|-----------|-------|
| V-01 | Output format (schema-first declaration block) | None — schema-first doesn't change how specificity criteria are generated | Very strong — SCHEMA BLOCK maps every required field to a structural location before drafting begins; unanchored declarations are structurally impossible | None | Single-axis; risk: builder declares required fields correctly in SCHEMA but still produces prohibitions instead of criteria for specificity |
| V-02 | Lifecycle emphasis (specificity-conversion phase) | Very strong — dedicated CONVERT step requires each specificity element to become a named criterion with a testable pass condition; prohibitions fail the conversion test | Moderate — phase ordering enforces presence but no explicit structural-home declaration | None | Single-axis; risk: conversion step produces criteria anchored to specificity but does not prevent other required fields from being unanchored |
| V-03 | Phrasing register (criteria-forward interrogation) | Strong — criteria-forward phrasing requires every specificity mechanism to answer "what would a third-party evaluator check?" — prohibitions don't survive this question | Strong — criteria-forward phrasing requires every obligation to answer "at what structural location?" — unanchored obligations don't survive this question | None | Single-axis; criteria-forward phrasing addresses both C-15 and C-16 through the same mechanism; risk: phrasing discipline alone is not a structural gate |
| V-04 | Output format + Lifecycle emphasis (schema-first + specificity-conversion) | Very strong — CONVERT phase from V-02 ensures specificity elements produce criteria | Very strong — SCHEMA BLOCK from V-01 ensures all required fields are anchored | None | Combined; targets C-15 and C-16 simultaneously; risk: two declaration phases create overhead; hypothesis is that they address distinct failure modes with no interaction |
| V-05 | Role sequence + Output format + Lifecycle emphasis (Schema-miner → Builder → Auditor + redundancy check) | Very strong — Auditor Part 2 verifies specificity elements from SPECIFICITY-INVENTORY map to output-testing criteria (not prohibitions) | Very strong — Schema-miner produces SCHEMA-DECLARATION before Builder begins; Auditor Part 1 verifies schema compliance | Strong — Auditor Part 3 REDUNDANCY-TABLE checks every criterion pair for distinct observables; direct probe for C-10 | Combined; extends Round 3 V-05 three-role pattern; Schema-miner role decouples structural/specificity analysis from criterion drafting |

---

## V-01 — Output Format (Schema-First Declaration Block)

**Axis:** Output format
**Hypothesis:** C-16 fails when a prompt declares required fields as obligations in the instructions ("the frontmatter must include a version field") but the output template shows no structural location for them. A builder following such instructions knows the field must exist but not where to put it — or produces an output where the field appears in a different structural location each time. V-01 requires the output to open with a SCHEMA BLOCK that explicitly maps every required field to its structural location (frontmatter block, purpose statement, criterion block, scoring section) before any criteria are written. The SCHEMA BLOCK is not documentation — it is the output skeleton. A field mentioned as required in any instruction but absent from the SCHEMA BLOCK is an unanchored obligation: a structural error detectable by inspection. The schema-first constraint forces explicit declaration of WHERE before content is written. The risk is that the SCHEMA BLOCK adds overhead without improving criterion quality; the hypothesis is that it prevents unanchored fields by making their absence visible at the point of first declaration rather than at audit time.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden — it must be complete, testable, and structurally anchored: every required field must be declared in the output schema with a named structural home before any criterion is written.

**PHASE 1 — SCHEMA DECLARATION**

Before reading the skill spec, declare the output schema. The schema maps every required field in the output rubric to its structural location. Write the schema block exactly as it will appear in the output — this is not a planning step, it is the first section of the artifact:

```
SCHEMA:
  frontmatter_block:
    required: skill, skill_target, date, version
    format: yaml block delimited by ---
  purpose_statement:
    required: 2–3 sentences
    location: first paragraph of body, before any criteria
  criterion_block:
    required: id, text, weight, category, pass_condition
    location: one block per criterion; essential section first, then recommended, then aspirational
  scoring_section:
    required: composite_formula, golden_threshold
    location: final section of body
```

A field that will appear in the final output must have an entry in SCHEMA before you begin Phase 2. Do not add fields during drafting that are not in SCHEMA. Do not reference a required field in any instruction that has no SCHEMA entry.

**PHASE 2 — READ THE SKILL SPEC**

Read the skill spec. Extract:

1. What the skill produces: artifact type, required output fields, structural shape of a complete correct output.
2. Lifecycle phases: what each phase delivers and what a non-functional phase output looks like.
3. Failure modes (minimum 3): what makes an output of this skill non-functional? For each, name the specific property of the output that is absent or malformed — not a generic quality observation.

Write the failure mode list:

```
FAIL-01: [specific property absent or malformed] — [why this makes the output non-functional]
FAIL-02: ...
FAIL-03: ...
```

**PHASE 3 — DRAFT CRITERIA**

For each failure mode, draft one essential criterion. Use the fields declared in SCHEMA (criterion_block). A field not in the SCHEMA criterion_block entry cannot appear in the criterion.

Pass condition rules: use observable anchors only — count thresholds, named fields, structural patterns, explicit enumerations. The following phrases are not observable anchors and must not appear in any pass condition: "is clear," "seems appropriate," "adequately covers," "is comprehensive."

Tier structure:
- Essential (3–5): absence makes the output non-functional.
- Recommended (2–3): pass conditions test quality properties, not just presence.
- Aspirational (1–2): go beyond what essential and recommended require; must not restate an essential criterion.

All three tiers required. Sequential C-NN numbering throughout.

**PHASE 4 — SCORING AND OUTPUT**

Write the scoring section using the fields declared in SCHEMA (scoring_section):

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter (from SCHEMA: frontmatter_block):
```yaml
skill: {skill}
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2–3 sentences — state what the rubric evaluates and the schema-first principle: "every required field is declared in the output schema before content is written; a required field with no structural home in SCHEMA is a structural error, not a content gap"), then criteria ordered essential → recommended → aspirational (each criterion as a labeled block matching the SCHEMA criterion_block fields), then scoring section.

---

## V-02 — Lifecycle Emphasis (Specificity-Conversion Phase)

**Axis:** Lifecycle emphasis
**Hypothesis:** C-15 fails when a prompt includes a "check specificity" mechanism — a gate, a prohibition, or an input-analysis step — that identifies whether criteria are generic, but does not require the builder to convert that identification into a scoreable criterion. A prohibition ("do not write generic criteria") identifies the failure mode but produces no criterion. An input-analysis gate ("verify that pass conditions are skill-specific before proceeding") tests a process property, not an output property. V-02 adds a SPECIFICITY-CONVERSION phase positioned after failure mode enumeration and before criterion drafting. The phase has a single purpose: for each specificity element identified in the skill spec, convert it into a named criterion whose pass condition is a testable property of the output rubric — not a prohibition, not an input-analysis check. The phase name signals the required action: convert. The risk is that conversion produces criteria that are syntactically specific but semantically shallow; the hypothesis is that the explicit conversion step produces at least one criterion per specificity element that tests a named structural property of the output, which is the direct observable that C-15 requires.

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden — it must be complete, testable, and specific: every specificity-controlling element in the skill spec must produce a scoreable criterion in the output rubric, not a prohibition or an input-analysis gate.

**PHASE 1 — FAILURE MODE ENUMERATION**

Read the skill spec. For each lifecycle phase, identify what breaks if the phase produces wrong output. Write the failure mode list:

```
FAIL-01: [specific property absent or malformed] — [why non-functional] — [observable: what a third party can check]
FAIL-02: ...
FAIL-03: ...
```

Minimum 3 failure modes. Each must name a concrete property of the skill's output — not a generic quality observation.

**PHASE 2 — SPECIFICITY-CONVERSION**

Specificity-controlling elements are properties of the skill spec that determine how targeted the output must be to its specific input. They are distinct from generic quality properties (completeness, format, length). Identify them:

```
SPEC-INVENTORY:
  spec-01: [element name] — [what it makes specific: what would be different in the output if this element were ignored?]
  spec-02: ...
```

For each element in SPEC-INVENTORY, convert it into a criterion. The conversion rule:

> **A prohibition is not a criterion.** "The rubric must not contain generic criteria" — this is a prohibition. It cannot be evaluated pass/fail from the output artifact alone.
>
> **An input-analysis step is not a criterion.** "Verify that each criterion is specific to this skill" — this is a process check. It evaluates the process of building, not a property of the output.
>
> **A scoreable criterion** names a testable property of the output: "The rubric contains at least one criterion whose pass condition names a structural element specific to {skill_target}'s output — not a property that would apply to any rubric."

Write the CONVERSION MAP:

```
CONVERSION-MAP:
  spec-01 → [criterion candidate]:
    pass_condition_draft: [one sentence naming a testable property of the output rubric]
    is_prohibition: [yes/no — does the pass condition tell the builder what to avoid?]
    is_input_analysis: [yes/no — does the pass condition evaluate a build step rather than the artifact?]
    conversion_complete: [yes/no — is the pass condition a testable property of the output artifact?]
  spec-02 → ...
```

DO NOT proceed to Phase 3 unless every entry in CONVERSION-MAP has `conversion_complete: yes`.

**PHASE 3 — CRITERION DRAFTING**

Draft essential criteria from failure modes (Phase 1). Draft converted specificity criteria from CONVERSION-MAP (Phase 2). Assign them to tiers:

- Essential (3–5): absence makes the output non-functional. Pass condition uses observable anchors.
- Recommended (2–3): pass conditions test quality properties, not just presence. At least one converted specificity criterion belongs here or in Essential.
- Aspirational (1–2): go beyond essential and recommended. Must not restate an essential criterion.

All three tiers required. Sequential C-NN numbering throughout.

After all criteria, write the CONVERSION TRACE:

```
CONVERSION-TRACE:
  spec-01 → C-NN: [how the criterion's pass condition tests the specificity element]
  spec-02 → C-NN: [...]
  unmapped: [must be empty]
```

DO NOT proceed to Phase 4 unless `unmapped` is empty.

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
skill: {skill}
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2–3 sentences — state what the rubric evaluates and the conversion principle: "each specificity-controlling element in the skill spec produces a scoreable criterion in the output rubric; a specificity element that produces only a prohibition or process check is unconverted and must be revised"), then criteria ordered essential → recommended → aspirational (CONVERSION-MAP and CONVERSION-TRACE omitted from final output), then scoring section.

---

## V-03 — Phrasing Register (Criteria-Forward Interrogation)

**Axis:** Phrasing register
**Hypothesis:** Both C-15 and C-16 share a failure mode rooted in instruction phrasing. C-16 fails when instructions say "this field is required" — an obligation from the builder's perspective — rather than "the evaluator must find this field at [location]" — a testable claim from the evaluator's perspective. C-15 fails when instructions say "ensure the rubric is specific to this skill" — a directive to the builder — rather than "the criterion passes if the evaluator can verify specificity without consulting the instructions" — a scoreable assertion. V-03 reframes all definitional instructions as criteria-forward interrogations: every obligation is stated as an evaluator's question ("what must the evaluator be able to verify?") and every specificity mechanism is stated as a criterion candidate ("what property of the output would the evaluator check?"). This phrasing shift makes unanchored field declarations (C-16) syntactically awkward — a declaration without a structural location doesn't answer "where does the evaluator look?" — and makes mechanism-as-prohibition (C-15) structurally disfavored — a prohibition doesn't answer "what would the evaluator check in the artifact?" The risk is that phrasing discipline alone is not a structural gate and motivated builders can satisfy the phrasing while producing shallow criteria; the hypothesis is that the interrogative form consistently elicits output-grounded responses because the question form requires an artifact reference, not an instruction reference.

---

You are building a scoring rubric for a Signal skill. You are writing for a third-party evaluator who has access only to the output artifact and the rubric — not to the instructions that produced it. Every criterion you write must be checkable by that evaluator through inspection of the artifact alone.

**PHASE 1 — EVALUATOR INSPECTION MAP**

Before writing criteria, map what the evaluator can inspect. For each section of the output artifact, list what fields are present and how the evaluator would confirm their presence:

```
INSPECTION-MAP:
  section-01: frontmatter block
    fields: [field-1, field-2, ...]
    how_evaluator_checks: [e.g., "scan lines 1–N for YAML block; confirm each field name and non-blank value"]
  section-02: purpose statement
    fields: [...]
    how_evaluator_checks: [...]
  section-03: criterion blocks
    fields: [id, text, weight, category, pass_condition for each criterion]
    how_evaluator_checks: [...]
  section-04: scoring section
    fields: [composite_formula, golden_threshold]
    how_evaluator_checks: [...]
```

A field declared required anywhere in these instructions must appear in the `fields` list for exactly one section in INSPECTION-MAP. If the evaluator cannot find a field by inspecting a named section, the field has no structural home — it is evaluator-invisible.

**PHASE 2 — FAILURE MODES AS EVALUATOR-VISIBLE DEFECTS**

From the evaluator's position: what does a failing artifact look like when inspected? Write failure modes as evaluator-visible defects:

```
FAIL-01: [The evaluator opens the artifact and finds: {specific missing or malformed property}] — [consequence: {what scoring operation fails}]
FAIL-02: ...
FAIL-03: ...
```

Minimum 3 failure modes. Each must be detectable through inspection of the output artifact — not through re-reading the instructions.

**PHASE 3 — CRITERION DRAFTING (EVALUATOR-CHECKABLE)**

For each failure mode, draft one criterion. Each criterion's pass condition must cite a specific inspectable section from INSPECTION-MAP. Evaluator-invisible pass conditions fail this phase.

Prohibited language (not evaluator-checkable): "is clear," "seems appropriate," "adequately covers," "is well-organized." These do not tell the evaluator where to look or what to count.

**Specificity interrogation:** For the output rubric to be specific to its target skill, the evaluator must be able to check — from the artifact alone, without re-reading the skill spec — whether the criteria are skill-targeted or generic. Draft at least one criterion that answers the evaluator's question: "What property of this artifact would tell me that its criteria cannot apply to a different skill?" The pass condition must name that property in the artifact, not invoke the builder's intent.

Tier structure:
- Essential (3–5): absence makes the output non-functional.
- Recommended (2–3): pass conditions test quality properties, not just presence.
- Aspirational (1–2): go beyond essential and recommended; must not restate an essential criterion.

All three tiers required. Sequential C-NN numbering throughout.

**PHASE 4 — SCORING AND OUTPUT**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter (structural home: frontmatter block, section-01 of INSPECTION-MAP):
```yaml
skill: {skill}
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2–3 sentences — state what the rubric evaluates and the evaluator-perspective principle: "every criterion is written from the evaluator's position; a criterion whose pass condition requires consulting the instructions rather than inspecting the artifact is not evaluator-checkable"), then criteria ordered essential → recommended → aspirational (each criterion as a labeled block; INSPECTION-MAP omitted from final output), then scoring section.

---

## V-04 — Output Format + Lifecycle Emphasis (Schema-First + Specificity-Conversion)

**Axis:** Output format + Lifecycle emphasis
**Hypothesis:** V-01 addresses C-16 (unanchored field declarations) through schema-first declaration; V-02 addresses C-15 (specificity mechanism → scoreable criterion) through the specificity-conversion phase. V-04 combines both mechanisms. The combination hypothesis: the two mechanisms target orthogonal failure modes with no interaction — schema-first ensures structural completeness of required fields regardless of what specificity criteria are generated; specificity-conversion ensures specificity elements produce testable criteria regardless of how fields are anchored. Together they close both C-15 and C-16 in a single-pass prompt. The risk is that two declaration phases (SCHEMA BLOCK in Phase 1, SPEC-INVENTORY in Phase 2) create overhead that displaces criterion quality; the hypothesis is that both phases are narrow enough in scope — one declares locations, the other converts elements — that they do not compete for the same cognitive resources as criterion drafting in Phase 3.

---

You are building a scoring rubric for a Signal skill. Two properties govern this rubric before a single criterion is written: structural completeness (every required field has a declared home in the output schema) and specificity coverage (every specificity-controlling element in the skill spec produces a scoreable criterion, not a prohibition or process check).

**PHASE 1 — DUAL DECLARATION**

Before reading the skill spec for failure modes, produce two declaration artifacts.

**Declaration A — SCHEMA BLOCK** (structural completeness)

Declare every required field in the output schema and its structural location:

```
SCHEMA:
  frontmatter_block:
    fields: skill, skill_target, date, version
  purpose_statement:
    location: first paragraph of body, before criteria
    length: 2–3 sentences
  criterion_block:
    fields: id, text, weight, category, pass_condition
    location: one block per criterion; tier order: essential → recommended → aspirational
  scoring_section:
    fields: composite_formula, golden_threshold
    location: final section
```

A required field mentioned in any subsequent instruction that has no entry in SCHEMA is a structural error. Do not reference a required field that is absent from SCHEMA.

**Declaration B — SPEC-INVENTORY** (specificity coverage)

Read the skill spec. Identify specificity-controlling elements — properties that distinguish this skill's output from a generic rubric for any skill:

```
SPEC-INVENTORY:
  spec-01: [element] — [what it controls: how does its absence make the output generic?]
  spec-02: ...
```

For each spec-NN, confirm the conversion commitment:

```
CONVERSION-COMMITMENT:
  spec-01: [the criterion that will test this element will test {named property of the output artifact} — not a prohibition and not a process check]
  spec-02: ...
```

**GATE 1 — DECLARATION GATE:**

```
DECLARATION-GATE:
  schema_complete: [yes/no — all required fields from instructions appear in SCHEMA with structural homes?]
  inventory_populated: [yes/no — at least one spec-NN per identifiable specificity element?]
  conversions_committed: [yes/no — every spec-NN has a conversion commitment that names an output property?]
```

DO NOT proceed to Phase 2 unless all three are `yes`.

**PHASE 2 — FAILURE MODE ENUMERATION**

Using SCHEMA and SPEC-INVENTORY as source material, identify failure modes:

```
FAIL-01: [specific property absent or malformed] — [why non-functional] — [source: SCHEMA field / spec-NN]
FAIL-02: ...
FAIL-03: ...
```

Minimum 3 failure modes. At least one failure mode per spec-NN in SPEC-INVENTORY.

**PHASE 3 — CRITERION DRAFTING**

For each failure mode, draft one criterion using fields declared in SCHEMA (criterion_block). Pass conditions use observable anchors only — count thresholds, named fields, structural patterns. No bare qualitative phrases.

For each spec-NN in SPEC-INVENTORY, draft a criterion whose pass condition tests the output property named in the CONVERSION-COMMITMENT — not a prohibition, not a process check.

After drafting, write the SPECIFICITY TRACE:

```
SPECIFICITY-TRACE:
  spec-01 → C-NN: [how this criterion's pass condition tests the specificity element as an output property]
  spec-02 → ...
  unmapped: [must be empty — if not, add criteria before proceeding]
```

Tier structure:
- Essential (3–5): absence makes the output non-functional.
- Recommended (2–3): pass conditions test quality properties, not just presence.
- Aspirational (1–2): go beyond essential and recommended; must not restate an essential criterion.

All three tiers required. Sequential C-NN numbering throughout.

**PHASE 4 — SCORING AND OUTPUT**

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter (SCHEMA: frontmatter_block):
```yaml
skill: {skill}
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2–3 sentences — state what the rubric evaluates and both governing principles: "structural completeness — every required field declared in the output schema before content is written" and "specificity coverage — every specificity-controlling element produces a scoreable criterion, not a prohibition"), then criteria ordered essential → recommended → aspirational (SCHEMA, SPEC-INVENTORY, SPECIFICITY-TRACE omitted from final output), then scoring section.

---

## V-05 — Role Sequence + Output Format + Lifecycle Emphasis (Schema-Miner → Builder → Auditor + Redundancy Check)

**Axis:** Role sequence + Output format + Lifecycle emphasis
**Hypothesis:** Round 3 V-05 (three-role Author/Auditor pattern) achieved 79.3 — the highest composite across all prior rounds, missing only C-10 (redundancy audit). V-05 extends the three-role pattern with two structural additions: (1) a Schema-miner role that precedes the Builder and whose sole output is the SCHEMA-DECLARATION (C-16) and SPECIFICITY-INVENTORY (C-15), and (2) an Auditor redundancy check (C-10 direct probe). The Schema-miner decouples structural and specificity analysis from criterion drafting — the Builder receives pre-declared artifacts rather than discovering structural requirements mid-draft. This separation is the mechanism for C-15 and C-16: the Schema-miner role cannot produce prohibitions because its scope is declaration and inventory, not instruction; and the declared SCHEMA prevents unanchored fields because the Builder cannot reference a field the Schema-miner didn't declare. The Auditor's three-part audit (schema compliance, specificity coverage, redundancy check) closes all three gaps — C-15, C-16, and C-10 — in a single terminal role. The hypothesis is that front-loading schema and specificity work into a dedicated role produces better compliance than embedding these checks inline in the Builder phase, because the Schema-miner is not competing for attention with criterion quality during drafting.

---

You are building a scoring rubric for a Signal skill. Three roles execute in sequence. Each role produces an artifact. The next role cannot begin until the prior role's artifact exists and is complete.

---

### SCHEMA-MINER PHASE

The Schema-miner reads the skill spec and produces two artifacts. The Builder cannot begin until both are complete.

**Artifact 1 — SCHEMA-DECLARATION**

Declare every field that will be required in the output rubric and its structural location in the artifact:

```
SCHEMA-DECLARATION:
  frontmatter_block:
    required: skill, skill_target, date, version
    format: yaml block delimited by ---; appears before body
  purpose_statement:
    required: 2–3 sentences
    location: first paragraph of body
  criterion_block:
    required_all_tiers: id, text, weight, category, pass_condition
    required_essential_only: causal_link, contrast_example
    required_recommended_only: causal_link
    location: one block per criterion; labeled section per tier
  scoring_section:
    required: composite_formula, golden_threshold
    location: final section of body
```

Tier constraints for criterion_block:
- Essential: all five required fields plus causal_link and contrast_example. No field may be blank.
- Recommended: all five required fields plus causal_link. contrast_example omitted.
- Aspirational: all five required fields. causal_link optional.

A field mentioned as required in any Builder instruction but absent from SCHEMA-DECLARATION is an unanchored obligation — structural error.

**Artifact 2 — SPECIFICITY-INVENTORY**

Identify every specificity-controlling element in the skill spec — properties that determine how targeted the output must be to its specific input. Exclude generic quality properties (completeness, format).

```
SPECIFICITY-INVENTORY:
  spec-01: [element] — [what it controls: how does its absence make the rubric indistinguishable from a rubric for a different skill?]
  spec-02: ...
```

For each spec-NN: confirm the conversion mandate:

> The Builder must produce a criterion whose pass condition is a **testable property of the output artifact** — something the evaluator can check by inspecting the rubric, not by reading the instructions. A criterion whose pass condition says "avoids generic criteria" (prohibition) or "verify that the spec defines X" (process check) does not satisfy the conversion mandate.

DO NOT proceed to Builder phase until both SCHEMA-DECLARATION and SPECIFICITY-INVENTORY are complete and every spec-NN has a conversion mandate confirmed.

---

### BUILDER PHASE

The Builder reads SCHEMA-DECLARATION and SPECIFICITY-INVENTORY before writing any criteria.

**BUILDER ENTRY GATE:**

```
[ ] SCHEMA-DECLARATION is present — all required output fields declared with structural homes
[ ] SPECIFICITY-INVENTORY is present — all specificity-controlling elements listed with conversion mandates confirmed
```

DO NOT begin writing criteria until both boxes are checked.

For each essential criterion (3–5), execute four sub-steps in sequence:

**Sub-step 2a — Failure mode anchor:**
Name the specific property of the output that is absent or malformed and why that makes the output non-functional. One line. This failure mode becomes the source for the pass condition.

**Sub-step 2b — Inertia test:**
Draft the candidate pass condition. Apply the inertia test: "Could the vague rubric ('the output is clear and well-organized') still pass this condition?" If yes, add an observable anchor (count threshold, named field, structural pattern). Record:

```
INERTIA-RECORD:
  condition: [candidate pass condition]
  inertia_test: [yes=passes, no=fails — does vague rubric pass this condition?]
  skill_specific_element: [what property of {skill_target}'s output does this condition name?]
```

If `inertia_test: yes`, revise the condition before sub-step 2c.

**Sub-step 2c — Calibration pair (produce now):**
Write the contrast example immediately after sub-step 2b — not after all pass conditions are finalized:

> "(generic: '[formulation applicable to any rubric]'; skill-specific: '[formulation naming a concrete property of {skill_target}'s output]')"

If the skill-specific half does not name a property derivable from {skill_target}'s output structure, revise sub-step 2b first.

**Sub-step 2d — Record criterion block (forward-blocking gate):**
Record the criterion using SCHEMA-DECLARATION fields:

```
### C-NN — [Name]
id: C-NN
text: [one sentence including calibration pair from sub-step 2c]
weight: essential
category: correctness | depth | format | coverage | behavior
pass_condition: [auditable sentence from sub-step 2b]
causal_link: If [observable from pass_condition] is absent, then [named downstream operation] fails because [mechanism].
contrast_example: (from sub-step 2c)
```

**This is a forward-blocking gate.** Do not advance to the next criterion until INERTIA-RECORD shows `inertia_test: no` and both causal_link and contrast_example are present and match their template forms from SCHEMA-DECLARATION.

After essential criteria, draft Recommended (2–3) and Aspirational (1–2) using SCHEMA-DECLARATION fields for each tier. Recommended: causal_link required, contrast_example omitted. Aspirational: must not restate an essential criterion.

**SPECIFICITY TRACE** (after all criteria):

```
SPECIFICITY-TRACE:
  spec-01 → C-NN: [how this criterion's pass condition tests the spec-01 element as an inspectable property of the output artifact]
  spec-02 → ...
  unmapped: [must be empty — if not, add converted criteria before proceeding]
```

DO NOT proceed to the Structural Gate until SPECIFICITY-TRACE shows `unmapped: []`.

---

### STRUCTURAL GATE (between Builder and Auditor)

Before the Auditor phase begins, perform a heading-pattern scan of the Builder's output. Pattern match only — do not evaluate criterion quality.

```
[ ] Frontmatter block present (---yaml...---) with all four SCHEMA-DECLARATION frontmatter fields
[ ] Essential section heading present with 3–5 criterion blocks (### C-NN headings)
[ ] Recommended section heading present with 2–3 criterion blocks
[ ] Aspirational section heading present with 1–2 criterion blocks
[ ] Scoring section present with composite formula and golden threshold
```

If any heading is absent: write it now before proceeding. A missing heading after Builder phase completion indicates a forward-blocking gate was bypassed.

DO NOT proceed to Auditor phase until all structural gate boxes are checked.

---

### AUDITOR PHASE

The Auditor reads the complete Builder output and produces a three-part audit. The Auditor does not revise criteria — the Auditor identifies what must be revised and states the specific revision required.

**Audit Part 1 — Schema compliance:**
For each criterion, verify that all fields declared REQUIRED in SCHEMA-DECLARATION are present and non-blank. A blank causal_link in an essential criterion is a schema violation even if its other fields are complete.

Write per-criterion findings:
```
SCHEMA-AUDIT:
  C-NN: [compliant | violation — [field missing or blank]]
```

**Audit Part 2 — Specificity coverage:**
For each spec-NN in SPECIFICITY-INVENTORY, verify that the mapped criterion's pass condition tests a property of the output artifact — not a prohibition and not a process check.

Evaluator test: "Can this pass condition be evaluated by inspecting the output artifact alone, without re-reading the instructions or the skill spec?" If no, the criterion fails the conversion mandate.

Write findings:
```
SPECIFICITY-AUDIT:
  spec-01 → C-NN: [converted | unconverted — [reason]]
  spec-02 → ...
```

**Audit Part 3 — Redundancy check:**
For each pair of criteria in the Essential tier, verify that they do not test the same observable. Write:

```
REDUNDANCY-TABLE:
  (C-NN, C-MM): observable-NN=[...] | observable-MM=[...] | redundant=[yes/no]
  ...
```

If any pair is redundant: identify which criterion provides weaker coverage. Flag it for removal or replacement.

Write the AUDIT SUMMARY:

```
AUDIT-SUMMARY:
  schema_violations: [N — if > 0, list C-NN IDs]
  unconverted_elements: [N — if > 0, list spec-NN IDs]
  redundant_pairs: [N — if > 0, list pairs]
  revisions_required: [yes/no]
  revision_list: [C-NN IDs requiring revision, or "none"]
```

---

### OUTPUT

Incorporate all Auditor-required revisions. Write the final rubric.

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

Golden threshold: all essential criteria pass AND composite >= 80.

Write to: `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter (SCHEMA-DECLARATION: frontmatter_block):
```yaml
skill: {skill}
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2–3 sentences — state what the rubric evaluates and the three-role principle: "Schema-miner declares structure and specificity obligations before the Builder begins; Builder's forward-blocking gates prevent omission at write time; Auditor's redundancy check ensures no two essential criteria test the same observable"), then criteria ordered essential → recommended → aspirational (all Auditor-required revisions incorporated; SCHEMA-DECLARATION, SPECIFICITY-TRACE, and AUDIT-SUMMARY omitted from final output; calibration pairs and causal links retained as labeled fields), then scoring section.
