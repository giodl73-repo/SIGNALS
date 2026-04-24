# quest-rubric Variate — Round 13 (Round 6 against rubric v6/v21)
**Date:** 2026-03-15
**Rubric:** v6/v21 (C-01--C-20; adds C-19: dual-template Definer — single Definer role produces both Text-direction and Pass-observability templates as a unified paired output, satisfying C-17 and C-18 through the same structural mechanism; C-20: template composability — Definer output in exact slot-fillable phrasing register of the final criterion fields, eliminating the Builder's on-the-fly interpretation step)
**Target criteria:** C-19, C-20

**Round 6 design note:** Rounds 1--12 produced mechanisms for C-01 through C-18 across rubric tracks v1--v8. Against rubric v6/v21 specifically, the two new aspirational criteria address a structural asymmetry exposed by Round 11 scoring. C-19 closes the gap R11 V-03 left open: that variation satisfies C-17 (Pass generation gate via Step A-5, a phase-level inline step) and C-18 PARTIAL (definitional step within Phase A, not a role boundary), leaving direction and testability on separate enforcement paths — the direction gate uses one mechanism (Phase A direction step), testability gate uses another (Phase A verifiability step). C-19 requires unification: a single named Definer role produces both the Text-direction template (Y/Z/X) and the Pass-observability template (location/observable/standard) as a paired output, so the Builder receives both simultaneously from the same structural source and C-17 and C-18 are satisfied by a single architectural element rather than independently. R11 V-04 achieves this — its Pre-Instantiation Definer generates both templates — making C-19 a confirmable property of that architecture. C-20 addresses what R11 V-04 does not fully resolve: even when a Definer role produces both templates, the templates are expressed as structural descriptions ("a criterion Text is an absence-consequence chain; the structure is: 'Without [Y], the artifact [fails] because [Z]...'") rather than as bare fill-in forms. The Builder must still read "The structure is: '...'" and unwrap the description into criterion field language — a thin but real translation step that produces wrong-form-consequence errors under construction pressure. C-20 requires the Definer's output to BE the fill-in template: "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]." and "LOCATION: [field]. OBSERVABLE: [token]. STANDARD: [count]." — so the Builder instantiates criteria by filling brackets directly, not by interpreting structure descriptions. This round probes three single-axis mechanisms: (1) V-01 establishes the C-19 baseline via a Dual Definer role with a TEMPLATE PAIR block in propositional form — predicting C-19 very strong, C-20 fail; (2) V-02 isolates C-20 via slot-fillable Phase A inline templates without a Definer role — predicting C-20 very strong, C-19 fail; (3) V-03 tests whether a named TEMPLATE FOUNDATION section (same Phase A, both templates co-located under one heading, STOP gate covers both) satisfies C-19's "same mechanism" requirement without a role boundary — predicting C-19 moderate, C-20 fail. Combined: V-04 pairs the Dual Definer role with slot-fillable templates to close both criteria simultaneously; V-05 names two specific competitors (Split-Path Protocol and Propositional-Pair Protocol) that fail C-19 and C-20 respectively, making both gaps concrete before the Definer's output format is specified.

---

## Round 13 Variation Map

| Variation | Axis | C-19 probe | C-20 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Role sequence (Dual Definer, propositional templates) | Very strong -- named Dual Definer role produces explicit TEMPLATE PAIR block; both templates in single role output; C-17 and C-18 share one architectural source; Builder receives both simultaneously | Fail -- templates in propositional form: "the required form is: 'Without Y...'" framing; Builder must unwrap the description before filling the criterion field; interpretation step present | Single-axis; role boundary for C-19; exposes C-20 gap by using propositional form intentionally |
| V-02 | Phrasing register (slot-fillable templates, Phase A inline steps) | Fail -- templates produced as two sequential Phase A steps (A-3 for direction, A-5 for Pass); no Definer role boundary; C-17 and C-18 gated by separate Phase A steps -- different mechanisms | Very strong -- both templates in exact bare fill-in form: "Without [Y], ... [Z]. Not [X], but [Y]." and "LOCATION: []. OBSERVABLE: []. STANDARD: []." Builder fills brackets verbatim with zero interpretation | Single-axis; slot-fillable register for C-20; isolates whether register alone achieves C-20 without a role boundary |
| V-03 | Lifecycle emphasis (Symmetric TEMPLATE FOUNDATION section) | Moderate -- both templates produced within a single named TEMPLATE FOUNDATION section under one STOP gate; tests whether "same section" satisfies "same mechanism" without a role boundary | Fail -- templates within the section are in propositional form | Single-axis; tests the boundary: is a named lifecycle section equivalent to a role boundary for C-19 purposes? |
| V-04 | Role sequence + Phrasing register (Dual Definer with slot-fillable templates) | Very strong -- single Dual Definer role produces unified TEMPLATE PAIR block; C-17 and C-18 share one architectural source | Very strong -- both templates in exact slot-fillable field-register form; Builder fills brackets directly with no interpretation step | Combined; closes C-19 and C-20 simultaneously via unified role + slot-fillable register |
| V-05 | Inertia framing + Role sequence (Split-Path + Propositional-Pair competitors) | Very strong -- Split-Path competitor concretizes the asymmetric-mechanism failure (Definer gates direction; Phase A step gates testability -- different structures); naming this failure forces unified Definer output | Very strong -- Propositional-Pair competitor concretizes the interpretation-gap failure (Definer produces both templates in propositional form; C-19 satisfied but Builder still translates); naming this failure forces slot-fillable register | Combined; two-competitor architecture, each scoped to its target criterion; each competitor named at the phase where its failure becomes relevant |

---

## V-01 -- Role sequence (Dual Definer, propositional templates)

**Axis:** Role sequence
**Hypothesis:** C-19 requires that a single Definer role produce both the Text-direction template and the Pass-observability template as a unified paired output -- so that the Builder receives both simultaneously and C-17 and C-18 are satisfied through the same structural mechanism. R11 V-04 achieved this structure targeting C-17 and C-18; V-01 makes C-19 the explicit axis by naming a "Dual Definer" role whose sole output is a TEMPLATE PAIR block containing both templates. The templates are expressed in propositional form -- the Definer describes the required structure using "the required form is: '...'" framing rather than presenting bare fill-in sentences -- which should leave the Builder with a thin translation step. Prediction: C-19 very strong (single role, explicit TEMPLATE PAIR output, same source for both templates); C-20 fail (propositional "the required form is:" wrapper means Builder must interpret the structure description before filling the criterion field -- the translation step that C-20 requires be eliminated).

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output from this role is exactly two things: a failure log and a TEMPLATE PAIR. Do not draft criteria. Do not draft scoring. Produce only what is listed below.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap: what the skill failed to require | broken / suboptimal
```

**TEMPLATE PAIR.** Write the following two templates completely before proceeding. Both templates are binding for the Builder. The Builder may not draft a single criterion until both are present.

```
TEMPLATE PAIR:

Text direction template for [skill name]:
  A criterion Text for this skill is an absence-consequence argument. It establishes why
  the required property matters before the Pass condition names it as testable.
  The required form for this skill:
    "Without [Y], the artifact [fails] because [Z]. [Y] means [definition].
     Not [X], but [Y]."
  For this skill, Y (required property) is typically: [derive from failure log and skill
    spec; name the category of property that this skill's criteria will most often require]
  For this skill, Z (failure consequence) is typically: [what breaks in the rubric artifact
    when Y is absent; derive from the failure log -- name the class of downstream failure]
  For this skill, X (rejected form) is typically: [describe the wrong-form-consequence
    structure that a Builder of this skill's rubric would be tempted to write; name the
    class of mistake, not a hypothetical example]
  Prohibited form: "X causes failure" -- this names what the wrong form does, not what the
    absence of the required property costs. Any criterion Text arguing in the prohibited
    direction fails the direction check in the Dual Auditor role.

Pass observability template for [skill name]:
  A criterion Pass condition for this skill is an artifact-anchored observable: a fact
  that can be confirmed by reading the rubric artifact without judgment. It names where
  in the artifact to look and what to confirm there.
  The required form for this skill:
    "In [artifact location], [specific observable] is [present | count >= N | matches
     pattern | absent]."
  For this skill, artifact locations (2-3 specific sections or fields): [derive from the
    skill spec -- name the structural elements of this skill's output type where criteria
    observables are found]
  For this skill, typical observables (2-3 specific confirmable facts): [derive from what
    the skill produces -- name facts that can be verified without judgment]
  Prohibited qualitative-only forms (1-2 specific to this domain): [name the specific
    tempting but unverifiable forms a Builder would write for this skill's rubric type]
  Any Pass field containing a prohibited qualitative-only form fails the observability
  check in the Dual Auditor role.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (both templates complete, with skill-specific values filled in). Do not proceed to the Builder role until both are written.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer. Build the rubric using both templates as construction standards.

For every **Text field**: write an absence-consequence argument in the required form from the direction template. If you find yourself beginning with "[something] causes [failure]," stop. Identify the required property Y whose absence produces the failure. Rewrite: "Without Y, the artifact [fails] because Z."

For every **Pass field**: name an artifact location and observable from the observability template. If you find yourself writing a prohibited qualitative-only form, stop. Replace it with the location and observable the qualitative phrase is gesturing at.

**Essential criteria (3-5).** From broken failure modes. Five fields per criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: absence-consequence chain per direction template
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass condition**: artifact-anchored observable per observability template

**Recommended criteria (2-3).** From suboptimal failure modes. Pass conditions test degree, precision, or specificity -- not whether an element is present. Annotate: **Property tested:** [degree | precision | specificity].

**Aspirational criteria (1-2).** Reference anchor per criterion:

```
Reference: [prior rubric or class that passes C-01--C-08]
Passes: [essential and recommended explicitly]
Fails: [exact dimension where it falls short]
```

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE:** Output is the complete rubric draft. All criteria present with required fields. Do not proceed to the Dual Auditor role without the full draft.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR from the Dual Definer and the rubric draft from the Builder. Apply five checks per criterion in isolation. Revise in-place where any check fails. Report each revision: criterion ID, check number, what changed.

**Check 1 -- Direction (Text, isolated).** Read the Text field alone, without the TEMPLATE PAIR and without other criteria. Does it argue from the absence of the required property to artifact failure ("without Y, Z fails")? Or does it argue from the presence of the rejected form ("[X] causes F")? If the prohibited form is present: apply the direction template -- identify Y, name consequence Z, build the absence-consequence chain.

**Check 2 -- Contrast clause (Text).** Does the Text contain "not [rejected form X], but [required form Y]"? If not, add the contrast clause using the direction template's X and Y scoped to this criterion.

**Check 3 -- Text isolation.** Does the Text field establish the required property, absence consequence, and contrast clause entirely within the Text cell -- without depending on the TEMPLATE PAIR for intelligibility? A Text that passes Check 1 only because the reader has the direction template visible fails Check 3. Rewrite until self-contained.

**Check 4 -- Pass verifiability (Pass, isolated).** Read the Pass field alone. Apply the observability template:
- *Location check:* does Pass name a specific artifact location from the template? If not, add the location.
- *Observable check:* does Pass name a specific confirmable fact? If not, replace the qualitative phrase with the location and observable it is gesturing at.
- *Prohibited-form check:* does Pass contain any prohibited qualitative-only form? If yes, replace.

**Check 5 -- Pass-Text coherence.** Is the Pass condition the logical conclusion of the Text argument? Does Pass name an observable not established in Text? If so, add grounding to Text or remove the ungrounded claim from Pass.

After all five checks pass for every criterion, output the complete revised rubric. The revision log appears before the rubric body.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the Dual Definer principle: a single role produces both the Text-direction template and the Pass-observability template as a unified paired output before the Builder runs; the paired output ensures direction and testability are gated by the same architectural mechanism; the Dual Auditor applies both templates in isolation to every criterion post-draft), then criteria ordered essential -> recommended -> aspirational (reference anchors retained; role headers and revision log omitted from final artifact), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 -- Phrasing register (Fill-in-the-slot templates, Phase A inline steps)

**Axis:** Phrasing register
**Hypothesis:** C-20 requires that the Definer's templates be in the exact phrasing register of the final criterion fields -- verbatim slot-fillable, not propositional descriptions of what to produce. V-02 tests whether slot-fillable register can be achieved without a Definer role by placing both templates as Phase A inline steps where the templates are written in bare fill-in form. Phase A Step A-3 produces the direction template as the exact fill-in sentence: "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]." Phase A Step A-5 produces the Pass template as the exact fill-in structure: "LOCATION: [field]. OBSERVABLE: [token]. STANDARD: [count]." Both templates are in the register the Builder fills -- not descriptions of the register. The C-19 asymmetry is preserved intentionally: templates are produced by separate Phase A steps (A-3 and A-5), not a unified Definer role. C-17 is gated by Step A-5 (a lifecycle step) and C-18 would be gated by A-3 (another lifecycle step) -- different mechanisms. Prediction: C-20 very strong (templates in exact field-register, Builder fills brackets verbatim); C-19 fail (separate Phase A mechanisms, not a unified Definer role).

---

You are building a scoring rubric for a Signal skill. Construction runs in two phases. **Do not begin Phase B until Phase A output is written and the STOP gate is cleared.**

---

### PHASE A -- STRUCTURAL GATE

Phase A produces all construction standards before any criterion is drafted. Each step must be completed in order.

**Step A-1: Read the skill spec and sample outputs.** Write one sentence: what does this skill produce?

**Step A-2: Extract failure modes.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

**Step A-3: Write the TEXT FILL-IN TEMPLATE.**

This is not a rule to follow -- it is the template the Builder fills to produce every criterion's Text field. Write the bare fill-in sentence, then specify what to put in each bracket for this specific skill:

```
TEXT FILL-IN TEMPLATE:
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For this rubric, fill the brackets as follows:
  [Y] = [name the type of required property this skill's criteria will assert --
         derive from the skill spec; name the category, not a hypothetical example]
  [Z] = [name the type of failure consequence when Y is absent -- derive from the
         failure log; what specifically breaks when Y is missing]
  [X] = [name the rejected form specific to this skill's domain -- the wrong-direction
         argument a Builder would write for this skill's output type]
```

The Builder fills these brackets per-criterion by substituting the specific Y, Z, and X for that criterion's failure mode. A Text field is the filled sentence -- not a paraphrase. A criterion Text that argues "[X] causes [failure]" -- in any phrasing -- is in the prohibited direction and must be rewritten by filling the template.

**Step A-4: Establish the contrast and isolation requirements.**

> "Each criterion Text must contain: not [X per this criterion], but [Y per this criterion]. Both elements must appear in the Text cell. Each criterion Text must be self-contained: a reader with no access to preamble, other criteria, or Phase A output must be able to identify the required property, the consequence of its absence, and what satisfies it."

**Step A-5: Write the PASS FILL-IN TEMPLATE.**

This is the template the Builder fills to produce every criterion's Pass field. Write the bare fill-in structure, then specify the options for this specific skill:

```
PASS FILL-IN TEMPLATE:
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern X | absent]

For this rubric, fill the brackets as follows:
  LOCATION options (2-3 specific sections or fields in this skill's output):
    [derive from the skill spec; name the structural elements where observables live]
  OBSERVABLE options (2-3 specific confirmable facts for this skill):
    [derive from what the skill produces; name facts confirmable without judgment]
  Prohibited qualitative-only forms for this domain (1-2):
    [name specific tempting but unverifiable forms for this skill's rubric type]
```

The Builder fills these brackets per-criterion by selecting a LOCATION from the options, naming the OBSERVABLE, and stating the STANDARD. A Pass field is the three filled lines -- not a description of them. A Pass field containing a prohibited qualitative-only form must be replaced with the filled template.

**STOP GATE A:** Do not proceed to Phase B until all steps are present:

- Failure log >= 5 entries
- TEXT FILL-IN TEMPLATE (Step A-3) in bare fill-in form, with bracket guidance for this skill
- Contrast and isolation requirements (Step A-4)
- PASS FILL-IN TEMPLATE (Step A-5) in bare fill-in form, with LOCATION options, OBSERVABLE options, and prohibited forms for this skill

Write: "Phase A complete. TEXT template: [one-line summary of Y/Z/X for this skill]. PASS template: [one-line summary of LOCATION options, OBSERVABLE options, prohibited forms]. Both templates in slot-fillable form -- no 'the structure is:' wrapper present."

---

### PHASE B -- CRITERION DRAFTING AND SYMMETRIC AUDIT

**Step B-1: Draft criteria** by filling the template brackets.

- Every **Text field**: copy the TEXT FILL-IN TEMPLATE. Fill [Y] with the specific required property for this criterion. Fill [Z] with the failure consequence. Fill [X] with the rejected form. The Text field IS the filled sentence.
- Every **Pass field**: copy the PASS FILL-IN TEMPLATE. Fill LOCATION from the options list. Fill OBSERVABLE from the options list. State STANDARD. The Pass field IS the three filled lines.

**Essential criteria (3-5).** From broken failure modes. Five fields: ID (C-NN starting C-01), Text (filled TEXT template), Weight (essential), Category, Pass (filled PASS template).

**Recommended criteria (2-3).** From suboptimal failure modes. Pass tests degree, precision, or specificity. Annotate: **Property tested:** [degree | precision | specificity]. All Pass fields: filled PASS FILL-IN TEMPLATE.

**Aspirational criteria (1-2).** Reference anchor per criterion. All Pass fields: filled PASS FILL-IN TEMPLATE.

**Step B-2: Symmetric isolation audit.** Re-read each criterion with Phase A templates NOT visible. Apply:

*Direction (Text):* Argues "without Y, Z fails" per TEXT FILL-IN TEMPLATE structure? Or "[X] causes [failure]"? Flag and refill if wrong direction.

*Contrast (Text):* "not [X], but [Y]" present? Flag and add if absent.

*Isolation (Text):* Intelligible with no context outside the Text cell? Flag and rewrite if context-dependent.

*Pass verifiability (Pass):* All three lines present? LOCATION from the Step A-5 options? OBSERVABLE a specific confirmable fact? STANDARD stated? No prohibited form? Flag and refill if any check fails.

Report: "B-2 audit complete. Direction flags: [N]. Contrast flags: [N]. Isolation flags: [N]. Pass flags: [N by check type]."

**Step B-3: Scoring.**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the fill-in-template principle: the TEXT FILL-IN TEMPLATE and PASS FILL-IN TEMPLATE are in the exact phrasing register of the final criterion fields; the Builder fills brackets directly from the Phase A templates; a criterion field is the filled template, not a paraphrase of it), then criteria ordered essential -> recommended -> aspirational (reference anchors retained; Phase A templates and audit report omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 -- Lifecycle emphasis (Symmetric TEMPLATE FOUNDATION section)

**Axis:** Lifecycle emphasis
**Hypothesis:** C-19's "same structural mechanism" requirement could be satisfied by a named section that groups both templates together before criteria are drafted, rather than by a role boundary. V-03 tests this by placing both templates inside a single named TEMPLATE FOUNDATION section in Phase A, with a single STOP gate that requires both templates to be complete before the section is exited. The section makes the co-location of both templates visible as a structural artifact in the output -- both appear under the same heading, with a note that neither is optional and that the section is incomplete without both. The key test: does "same named section under a shared STOP gate" constitute "same structural mechanism" for C-19, or is a role boundary required? The hypothesis is that it does not -- a section is a grouping device, not an architectural boundary; the direction template and Pass template remain produced by sequential steps within the section, not by a single unified output -- so C-19 should be moderate rather than very strong. Templates are in propositional form, producing C-20 fail. This variation isolates the section-vs-role distinction for C-19.

---

You are building a scoring rubric for a Signal skill. Construction runs in two phases. **Do not begin Phase B until Phase A output is written and the STOP gate is cleared.**

---

### PHASE A -- STRUCTURAL GATE

**Step A-1: Read the skill spec and sample outputs.** Write one sentence: what does this skill produce?

**Step A-2: Extract failure modes.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

---

**TEMPLATE FOUNDATION**

*Both templates in this section must be written completely and in order before the Phase A STOP gate can be cleared. The STOP gate covers the entire TEMPLATE FOUNDATION as a unit. A TEMPLATE FOUNDATION with only one template is incomplete -- it creates an asymmetric enforcement structure where one field type is defined and the other is not.*

**Template 1 -- Text direction.** Write the direction requirement for this specific skill:

> "For this rubric, a criterion Text argues from the absence of the required property to artifact failure. The required form for [this skill] is: 'Without [required property Y], the artifact [fails] because [Z]. [Y] means [definition]. Not [rejected form X], but [required form Y].'
>
> For this skill, Y is typically: [derive from failure log -- name the category of required property]
> For this skill, Z is typically: [derive from failure log -- name the class of downstream failure when Y is absent]
> For this skill, X is typically: [name the wrong-direction argument a Builder would write for this skill's domain]
> Prohibited direction: 'X causes failure.' A criterion Text carrying this argument fails the Phase B audit."

**Template 2 -- Pass verifiability.** Written within the same TEMPLATE FOUNDATION section, after Template 1. Write the verifiability requirement for this specific skill:

> "For this rubric, a criterion Pass condition is verifiable if and only if it names: (1) a specific artifact location in this skill's output; (2) a specific observable that a reader can confirm without judgment; (3) no prohibited qualitative-only language.
>
> For this skill, artifact locations: [list 2-3 specific sections or fields -- derive from the skill spec]
> For this skill, typical observables: [list 2-3 specific confirmable facts -- derive from what the skill produces]
> Prohibited qualitative-only forms for this domain: [list 1-2 tempting but unverifiable forms]
> A Pass condition containing a prohibited form must be rewritten as a location + observable + standard."

*Both templates constitute the TEMPLATE FOUNDATION. The direction template (Template 1) defines what the Text field IS for this skill. The Pass verifiability template (Template 2) defines what the Pass field IS for this skill. Neither is subordinate to the other. A TEMPLATE FOUNDATION missing either template cannot gate criterion construction symmetrically.*

---

**Step A-4: Contrast and isolation requirements.**

> "Each criterion Text must contain: not [X for this criterion], but [Y for this criterion]. Each Text must be self-contained: a reader who has not seen the TEMPLATE FOUNDATION must be able to identify the required property, the causal consequence, and what satisfies it."

**STOP GATE A:** Phase A complete when all four outputs are present:

- Failure log >= 5 entries
- TEMPLATE FOUNDATION: Template 1 AND Template 2 both written with skill-specific values
- Contrast and isolation requirements

Write: "Phase A complete. TEMPLATE FOUNDATION present: Template 1 [summary of Y/Z/X] and Template 2 [summary of locations, observables, prohibited forms]. Section is complete -- no asymmetry. STOP gate cleared."

---

### PHASE B -- CRITERION DRAFTING AND SYMMETRIC AUDIT

**Step B-1: Draft criteria** using the Phase A failure log, TEMPLATE FOUNDATION, and contrast and isolation requirements.

Every **Text field**: apply Template 1's required form: "Without [Y], the artifact [fails] because [Z]. Not [X], but [Y]." Prohibited direction: "[X] causes [failure]."

Every **Pass field**: apply Template 2's required form. Names a specific location (from Template 2), a specific observable (from Template 2), no prohibited qualitative form.

**Essential criteria (3-5).** From broken failure modes. Five fields: ID (C-NN starting C-01), Text, Weight (essential), Category, Pass condition.

**Recommended criteria (2-3).** From suboptimal failure modes. Pass tests degree, precision, or specificity. Annotate: **Property tested:** [degree | precision | specificity].

**Aspirational criteria (1-2).** Reference anchor per criterion.

**Step B-2: Symmetric isolation audit.** Re-read each criterion with TEMPLATE FOUNDATION not visible. Apply:

*Direction (Text):* "Without Y, Z fails" per Template 1? Flag and rewrite if prohibited direction present.

*Contrast (Text):* "not X, but Y" present? Flag and add if absent.

*Isolation (Text):* Intelligible without TEMPLATE FOUNDATION context? Flag and rewrite if not.

*Pass verifiability (Pass):* Location from Template 2? Specific confirmable observable? No prohibited form? Flag and rewrite if any check fails.

Report: "B-2 audit complete. Direction flags: [N]. Contrast flags: [N]. Isolation flags: [N]. Pass flags: [N by check]."

**Step B-3: Scoring.**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the TEMPLATE FOUNDATION principle: both the direction template and the Pass verifiability template are produced together in a named section before any criterion is drafted; a TEMPLATE FOUNDATION missing either template is structurally incomplete because it creates an asymmetric generation gate; the single STOP gate covering the entire section enforces symmetric generation-phase coverage of direction and testability before criterion construction begins), then criteria ordered essential -> recommended -> aspirational (reference anchors retained; TEMPLATE FOUNDATION and audit report omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 -- Role sequence + Phrasing register (Dual Definer with slot-fillable templates)

**Axes:** Role sequence + phrasing register
**Hypothesis:** V-01 establishes C-19 via a Dual Definer role with a TEMPLATE PAIR block, but leaves C-20 open by using propositional templates (the Builder must unwrap "the required form is:" before filling the criterion field). V-02 establishes C-20 via slot-fillable fill-in forms, but leaves C-19 open by producing templates in separate Phase A steps rather than from a unified Definer role. V-04 combines both: the Dual Definer role from V-01 and the slot-fillable register from V-02. The Definer's TEMPLATE PAIR block contains both templates as bare fill-in sentences -- the TEXT FILL-IN TEMPLATE and PASS FILL-IN TEMPLATE in the exact phrasing of the final criterion fields. The Builder fills the brackets directly; the Dual Auditor verifies the brackets are correctly filled. There is no structural description layer between Definer output and Builder input: the Definer's output IS the criterion field structure. Prediction: C-19 very strong (single Definer role, unified paired output, same source for both templates); C-20 very strong (bare slot-fillable register, no "the structure is:" wrapper, no interpretation step between Definer output and criterion construction).

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. The TEMPLATE PAIR contains two fill-in templates in the exact phrasing register of the final criterion fields. The Builder fills the brackets to produce criteria -- there is no interpretation step between your output and theirs. Do not draft criteria. Do not draft scoring.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

**TEMPLATE PAIR.** Write both templates as bare fill-in forms, instantiated for this specific skill.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE (fill brackets to produce a criterion Text field):
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name], fill the brackets as follows:
  [Y] = [write the specific required-property type for this skill -- the category of
         thing this skill's criteria will require; derive from skill spec and failure
         log; e.g., for a rubric-building skill: "the stated scoring formula and
         denominator" -- name the specific artifact element, not an abstraction]
  [Z] = [write the specific failure-consequence type when Y is absent -- what breaks
         in the artifact; e.g., for a rubric-building skill: "composite scores cannot
         be reproduced by a third party" -- name the damage, not the category]
  [X] = [write the specific rejected-form type -- the wrong-direction argument a
         Builder is tempted to write; e.g., "naming what the bad output does ('a
         rubric without a formula makes scoring subjective') rather than what the
         good property's absence costs"]

A criterion Text IS this sentence with the brackets filled. Do not write "the structure is:"
or "the required form is:" before it. Do not paraphrase it. Fill the brackets and the
result is the Text field. A Text beginning "[X] causes [failure]" -- in any phrasing --
is in the prohibited direction and must be rewritten by filling this template.

PASS FILL-IN TEMPLATE (fill brackets to produce a criterion Pass field):
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name], fill the brackets as follows:
  LOCATION options (name 2-3 specific sections or fields in this skill's output type --
    derive from the skill spec; these are the structural elements where criterion
    observables will be found; name them as a reader would navigate to them in the
    artifact):
    - [location 1]
    - [location 2]
    - [location 3 if applicable]
  OBSERVABLE options (name 2-3 specific confirmable facts for this skill -- things
    that can be verified by reading the artifact without judgment; e.g., "scoring
    formula denominator stated as an integer N" or "F-NN entry count >= 5"):
    - [observable 1]
    - [observable 2]
    - [observable 3 if applicable]
  Prohibited qualitative-only forms (1-2 specific forms tempting for this skill's
    domain that are not verifiable without judgment):
    - [prohibited form 1]
    - [prohibited form 2 if applicable]

A criterion Pass IS these three lines with the brackets filled. Do not write "the required
form is:" before them. Fill LOCATION from the options above. Fill OBSERVABLE from the
options above. State STANDARD as a verifiable condition. A Pass field containing a
prohibited form is not a Pass condition -- return to this template and fill the brackets.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (both fill-in templates complete, with skill-specific instantiation guidance filled in, in bare fill-in form -- no "the structure is:" or "the required form is:" wrapper around either template). Do not proceed to the Builder role until both templates are present in bare fill-in form.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer. Build the rubric by filling the template brackets -- not by interpreting them.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y] with the specific required property for this criterion's failure mode. Replace [Z] with the failure consequence. Replace [X] with the rejected form. The Text field IS the filled sentence.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION with a specific location from the Definer's LOCATION options. Fill OBSERVABLE with a specific confirmable fact from the OBSERVABLE options. State STANDARD. The Pass field IS the three filled lines. If you find yourself writing a prohibited form -- stop. Return to the PASS FILL-IN TEMPLATE and fill the brackets.

**Essential criteria (3-5).** From broken failure modes. Five fields per criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: filled TEXT FILL-IN TEMPLATE
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: filled PASS FILL-IN TEMPLATE (all three lines: LOCATION, OBSERVABLE, STANDARD)

**Recommended criteria (2-3).** From suboptimal failure modes. Pass tests degree, precision, or specificity -- not presence. Annotate: **Property tested:** [degree | precision | specificity]. All Pass fields: filled PASS FILL-IN TEMPLATE.

**Aspirational criteria (1-2).** Reference anchor per criterion:

```
Reference: [specific prior rubric or class that passes C-01--C-08]
Passes: [essential and recommended explicitly]
Fails: [exact dimension where it falls short]
```

All Pass fields: filled PASS FILL-IN TEMPLATE.

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE:** Complete rubric draft. All Text fields are filled TEXT FILL-IN TEMPLATE sentences. All Pass fields are filled PASS FILL-IN TEMPLATE three-line blocks.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR from the Dual Definer and the rubric draft from the Builder. The TEMPLATE PAIR is the audit standard. Apply five checks per criterion in isolation.

**Check 1 -- Direction (Text, isolated).** Strip the Text field. Read it alone with only the TEXT FILL-IN TEMPLATE visible (not the full Definer output or preamble). Does it follow the TEXT FILL-IN TEMPLATE structure ("Without [Y filled], ... [Z filled]. Not [X filled], but [Y filled].")? Or does it argue "[X filled] causes [failure]"? If wrong direction: identify Y for this criterion from the failure log. Fill the TEXT FILL-IN TEMPLATE. Rewrite.

**Check 2 -- Contrast clause (Text).** Does the Text contain "not [X for this criterion], but [Y for this criterion]"? If absent, add using the TEXT FILL-IN TEMPLATE's X and Y scoped to this criterion.

**Check 3 -- Text isolation.** Does the Text pass Check 1 when the reader has ONLY the TEXT FILL-IN TEMPLATE as context (not the bracket guidance, not other criteria, not preamble)? If the Text requires the bracket guidance to be intelligible, it fails isolation. Rewrite until the filled sentence is self-contained.

**Check 4 -- Pass verifiability (Pass, isolated).** Strip the Pass field. Read it with only the PASS FILL-IN TEMPLATE visible. Apply:
- *LOCATION line:* is a specific section or field from the Definer's LOCATION options on the LOCATION line? If not: fill from the options.
- *OBSERVABLE line:* is a specific confirmable fact from the OBSERVABLE options on the OBSERVABLE line? If not: fill from the options.
- *STANDARD line:* is a verifiable condition stated? If not: add.
- *Prohibited forms:* does any line contain a prohibited qualitative-only form from the Definer's list? If yes: replace with the filled PASS FILL-IN TEMPLATE.

**Check 5 -- Pass-Text coherence.** Is the OBSERVABLE in the Pass the logical conclusion of the absence-consequence argument in the Text? Does Pass name an observable not grounded in Text? If so: add grounding to Text or remove the ungrounded line from Pass.

After all checks pass for every criterion, output the complete revised rubric. Prepend the revision log: criterion ID, check number, original content, revised content.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the dual-template composability principle: the Dual Definer produces both the TEXT FILL-IN TEMPLATE and PASS FILL-IN TEMPLATE in the exact phrasing register of the final criterion fields; the Builder fills brackets without paraphrase -- a criterion field IS the filled template; the Dual Auditor verifies each field is correctly filled by applying the bare templates in isolation), then TEMPLATE PAIR (retained in artifact as the construction standard, in its bare fill-in form), then criteria ordered essential -> recommended -> aspirational (all fields retained; reference anchors retained; role headers and revision log omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 -- Inertia framing + Role sequence (Split-Path + Propositional-Pair competitors)

**Axes:** Inertia framing + role sequence
**Hypothesis:** Prior rounds established that naming a specific near-failing competitor at the right phase makes the gap concrete. R11 V-05 named the PARTIAL-17 Rubric (passes C-16, fails C-17 via asymmetric enforcement) and produced very strong C-17 compliance by making the enforcement gap non-abstract before Phase A was specified. V-05 for this round applies the same two-competitor architecture to C-19 and C-20. Competitor 1 (Split-Path Protocol) achieves C-18 but fails C-19 by using two different mechanisms -- a Definer role for direction, a Phase A inline step for testability; C-17 and C-18 are satisfied independently. Competitor 2 (Propositional-Pair Protocol) achieves C-19 (single Definer role, both templates as paired output) but fails C-20 because the templates are expressed as structural descriptions ("the structure is: 'Without [Y]...'"), forcing a thin translation step on the Builder. Each competitor is named at the phase where its failure becomes relevant: Competitor 1 before the Definer role is specified (motivating unified source for both templates), Competitor 2 inside the Definer role specification (motivating bare fill-in register). The protocol must surpass both by using a unified Definer role with slot-fillable fill-in templates. Prediction: C-19 very strong (Competitor 1 makes the asymmetric-mechanism failure concrete; protocol corrects via unified role output); C-20 very strong (Competitor 2 makes the propositional-vs-slot distinction concrete at the exact moment of template specification; protocol corrects via bare fill-in form).

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your protocol has two direct competitors. Each satisfies C-01 through C-18. Each fails exactly one of the two new target criteria.

---

**Competitor 1: The Split-Path Protocol**

The Split-Path Protocol uses a dedicated Definer role before the Builder runs. The Definer produces the direction template: a constitutive definition naming the required property Y, failure consequence Z, and rejected form X for this specific skill. The Builder receives this direction template as binding input before constructing any criterion. A separate Phase A inline step (between the Definer role output and the Builder) produces the Pass verifiability template -- the artifact locations, typical observables, and prohibited forms for this skill's Pass fields.

The Split-Path Protocol satisfies C-18 (direction is role-isolated: a named Definer role produces the direction template before the Builder runs) and C-17 (two-phase testability: the Pass template exists before construction, a post-draft auditor checks Pass fields).

The Split-Path Protocol fails C-19 because: the direction template and the Pass observability template are produced by different structural mechanisms -- one by a named Definer role, one by a Phase A inline step. C-17 and C-18 are satisfied through separate architectural sources. The Builder conceptually receives direction from "the Definer role" and testability from "Phase A." An evaluator reviewing the protocol can point to two different structural elements as the enforcement mechanism for these two properties. C-19 requires that both templates come from a single structural source -- that there is one Definer role whose sole output is a TEMPLATE PAIR containing both.

**Your protocol must go further than the Split-Path Protocol.** Both the direction template and the Pass observability template must come from the same structural source: a single named Definer role whose output is a unified TEMPLATE PAIR.

---

**Competitor 2: The Propositional-Pair Protocol**

The Propositional-Pair Protocol uses a single Definer role that produces both templates as a unified TEMPLATE PAIR block -- one role, one output, both templates present. This satisfies C-19: both C-17 and C-18 are satisfied through the same structural mechanism.

The Propositional-Pair Protocol fails C-20 because: the templates in the TEMPLATE PAIR are expressed in propositional form. The direction template reads:

> "A criterion Text for [skill name] is an absence-consequence chain. The required form is: 'Without [Y], the artifact [fails] because [Z]. [Y] means [definition]. Not [X], but [Y].'"

The Pass template reads:

> "A criterion Pass for [skill name] is an artifact-anchored observable. The required form is: 'In [artifact location], [specific observable] is [present|count|pattern].' Prohibited forms: [list]."

The Builder reading these templates must process "A criterion Text is..." and "The required form is:" before reaching the fill-in sentence. Even though the fill-in sentence is present (inside the quotation), it is wrapped in a structural description that requires interpretation. Under construction pressure, this interpretation step -- reading the wrapper, extracting the quoted sentence, applying it to the criterion -- is the translation step that produces wrong-form-consequence errors. The propositional wrapper creates an abstraction layer between Definer output and criterion field.

**Your protocol must go further than the Propositional-Pair Protocol.** The TEMPLATE PAIR must contain bare fill-in forms -- the TEXT FILL-IN TEMPLATE and PASS FILL-IN TEMPLATE with no "A criterion X is..." or "The required form is:" wrapper. The Builder reads the bare template and fills the brackets. The filled brackets ARE the criterion field.

---

**Read the skill spec and sample outputs.**

**STEP 1 -- FAILURE MODES**

Name failure modes. Assign severity:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

Minimum: 3 broken, 2 suboptimal. Do not draft criteria until >= 5 entries.

---

**STEP 2 -- DUAL DEFINER**

Beyond the Split-Path Protocol, both templates come from a single Dual Definer role. Beyond the Propositional-Pair Protocol, both templates are in bare fill-in form. Write the TEMPLATE PAIR now, as the Dual Definer's output.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE (fill brackets to produce a criterion Text field):
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name]:
  [Y] = [the specific required-property type -- name the artifact element or output
         property this skill's criteria will require; derive from failure log; must
         be specific enough that a Builder filling this bracket produces a criterion
         Text about this skill, not a generic rubric skill]
  [Z] = [the specific failure consequence -- what breaks in the artifact when Y is
         absent; name the damage; derive from failure log]
  [X] = [the specific rejected form -- the wrong-direction argument the Builder would
         write for this skill's domain; name the class of mistake]

Do not write "A criterion Text is..." or "The required form is:" before this template.
The sentence above IS the template. Fill the brackets and the result IS the Text field.

PASS FILL-IN TEMPLATE (fill brackets to produce a criterion Pass field):
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name]:
  LOCATION options: [list 2-3 specific sections or fields in this skill's output --
    the structural elements where criteria observables are found]
  OBSERVABLE options: [list 2-3 specific confirmable facts -- things verifiable by
    reading the artifact without judgment]
  Prohibited forms: [list 1-2 specific qualitative-only forms tempting for this domain]

Do not write "A criterion Pass is..." or "The required form is:" before this template.
The three lines above ARE the template. Fill the brackets and the result IS the Pass field.
```

**STEP 2 GATE:** TEMPLATE PAIR is complete with both templates in bare fill-in form, no propositional wrapper, and skill-specific instantiation guidance. The Split-Path Protocol's asymmetry is absent (both templates from the same Dual Definer output). The Propositional-Pair Protocol's propositional wrapper is absent (both templates are bare fill-in forms).

---

**STEP 3 -- CONTRAST AND ISOLATION REQUIREMENTS**

Write both requirements for Phase B:

> "Each criterion Text must contain: not [X for this criterion], but [Y for this criterion]. Each Text must be self-contained: a reader with only the TEMPLATE PAIR (not bracket guidance) must be able to identify the required property, the consequence of its absence, and what satisfies it."

---

**STEP 4 -- ESSENTIAL CRITERIA (3-5)**

From broken failure modes. Five fields per criterion: ID (C-NN starting C-01), Text (fill TEXT FILL-IN TEMPLATE), Weight (essential), Category, Pass (fill PASS FILL-IN TEMPLATE).

For each essential criterion before writing the next: "Does my Text argue 'without Y, Z fails' or 'X causes failure'? Does my Pass have a LOCATION from the options, an OBSERVABLE from the options, and a STANDARD?" If not, return to the TEMPLATE PAIR and fill the brackets.

---

**STEP 5 -- RECOMMENDED CRITERIA (2-3)**

From suboptimal failure modes. Pass tests degree, precision, or specificity. Annotate: **Property tested:** [degree | precision | specificity]. All Pass fields: filled PASS FILL-IN TEMPLATE.

---

**STEP 6 -- ASPIRATIONAL CRITERIA (1-2)**

Reference anchor per criterion. The Propositional-Pair Protocol may serve as a reference (passes C-01--C-18 including C-19, fails C-20):

```
Reference: [name the competitor or prior rubric]
Passes: [tiers and criteria it satisfies]
Fails: [exact dimension where it falls short -- the delta this criterion measures]
```

All Pass fields: filled PASS FILL-IN TEMPLATE.

---

**STEP 7 -- POST-DRAFT AUDIT**

Re-read each criterion in isolation with only the TEMPLATE PAIR visible (not the bracket guidance, not other criteria, not preamble). Apply:

*Direction (Text):* Follows TEXT FILL-IN TEMPLATE structure? Or "[X] causes [failure]"? Flag and refill if wrong direction.

*Contrast (Text):* "not [X], but [Y]" present? Flag and add if absent.

*Isolation (Text):* Intelligible with only the bare TEXT FILL-IN TEMPLATE (brackets filled) as context? Flag and rewrite if it depends on bracket guidance or preamble.

*Pass verifiability (Pass):* All three lines present? LOCATION from options? OBSERVABLE a specific confirmable fact? STANDARD stated? No prohibited form? Flag and refill if any check fails.

Report: "Step 7 complete. Direction flags: [N]. Contrast flags: [N]. Isolation flags: [N]. Pass flags: [N by check]. Split-Path asymmetry not present: both templates from Dual Definer TEMPLATE PAIR. Propositional-Pair wrapper not present: both templates in bare fill-in form."

---

**STEP 8 -- SCORING**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- name both competitors and state what each adds: where the Split-Path Protocol uses two separate structural mechanisms for direction and testability, this protocol unifies both under a single Dual Definer role output; where the Propositional-Pair Protocol wraps the fill-in sentences in structural descriptions, this protocol presents bare fill-in templates directly; unified source and bare register together close the architectural asymmetry and eliminate the interpretation gap), then TEMPLATE PAIR (retained in artifact in bare fill-in form), then criteria ordered essential -> recommended -> aspirational (reference anchors and Fills gap fields retained; competitor descriptions and step notes omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
