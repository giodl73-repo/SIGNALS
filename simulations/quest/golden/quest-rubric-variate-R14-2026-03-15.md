# quest-rubric Variate — Round 14 (Round 1 against rubric v22)
**Date:** 2026-03-15
**Rubric:** v22 (C-01--C-22; adds C-21: audit symmetry — the post-draft audit mirrors the generation gate's two-field structure with individually named, independently operative checks for Text and Pass fields as parallel tracks of equal granularity; adds C-22: form-class prohibition exhaustiveness — the direction prohibition explicitly enumerates variant phrasings and declares the form-class closed, not merely asserts "in any phrasing")
**Target criteria:** C-21, C-22

**Round 1 against v22 design note:** Rounds 1--13 produced mechanisms for C-01 through C-20 across rubric tracks v1--v8/v21. Against rubric v22 specifically, the two new aspirational criteria address structural gaps that persist in R13 V-04 — currently the highest-scoring variation, achieving C-19 and C-20 via a Dual Definer with slot-fillable templates.

**C-21 gap in R13 V-04.** The Dual Auditor runs three individually named checks for Text (Check 1 direction, Check 2 contrast, Check 3 isolation) and one named check for Pass (Check 4), which contains four sub-bullets: LOCATION, OBSERVABLE, STANDARD, prohibited-forms. Sub-bullets under a single check number are structurally subordinate — they constitute one audit event. An auditor reports "Check 4 passed" or "Check 4 failed" for the entire Pass field; they cannot report "Check 4 failed but Check 5 passed" because the location and observable concerns share a check number. C-21 requires the audit phase to be structurally symmetric: the number of individually named, independently reportable checks for the Pass field must equal those for the Text field. Three Text checks demands three Pass checks: one for location, one for observable and standard, one for prohibited-form. Each must be separately numbered, separately operative, and separately reported.

**C-22 gap in R13 V-04.** The TEMPLATE PAIR says "A Text beginning '[X] causes [failure]' -- in any phrasing -- is in the prohibited direction." The "in any phrasing" claim is present but the form-class is not enumerated. Auditor Check 1 tests whether the Text argues "[X] causes [failure]" -- a function that detects the canonical form and direction. A Builder who writes "[X] leads to [failure]" or "the artifact breaks when [X] is present" passes Check 1 because neither matches the canonical example. C-22 requires the prohibition to be operationally form-class exhaustive: the TEMPLATE PAIR must enumerate 4+ variant phrasings covering all synonymous constructions of the wrong-direction argument, declare the form-class closed, and Auditor Check 1 must test against the full enumerated form-class, not just the canonical example.

This round probes three single-axis mechanisms and two combined: (1) V-01 targets C-21 by splitting Auditor Check 4 into three separately numbered Pass checks; (2) V-02 targets C-22 by extending the TEMPLATE PAIR to enumerate 4+ variant phrasings with an explicit form-class closure statement; (3) V-03 targets C-22 via role sequence by inserting a named Prohibition Enumerator step between Definer and Builder; (4) V-04 combines V-01 and V-02 to close both criteria simultaneously; (5) V-05 names two competitors — Asymmetric-Audit Protocol (passes C-17, fails C-21) and Example-Bounded Protocol (passes C-15, fails C-22) — to make each gap concrete before the protocol is specified.

---

## Round 14 Variation Map

| Variation | Axis | C-21 probe | C-22 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Lifecycle emphasis (symmetric 3+3 Auditor checks) | Very strong — Auditor has 3 named Pass checks (Check 4 location, Check 5 observable+standard, Check 6 prohibited-form) matching the 3 Text checks (Check 1 direction, Check 2 contrast, Check 3 isolation); each independently numbered and reportable; audit report separates Text and Pass flag tallies | Fail — TEMPLATE PAIR prohibition unchanged from R13 V-04; "in any phrasing" present but no variant phrasings enumerated; Auditor Check 1 tests only canonical form | Single-axis; audit granularity restructure; isolates whether symmetric check count alone satisfies C-21 |
| V-02 | Phrasing register (form-class prohibition with enumerated variants) | Fail — Auditor structure unchanged from R13 V-04 baseline; 3 Text checks + 1 Pass check (sub-bullets); Pass audit not elevated to equal granularity | Very strong — TEMPLATE PAIR includes PROHIBITED DIRECTION section with 5 enumerated variant phrasings and explicit form-class closure; Auditor Check 1 references full form-class; form-class declared operationally closed | Single-axis; form-class enumeration; isolates whether named variants + Auditor reference closes C-22 without audit restructure |
| V-03 | Role sequence (Prohibition Enumerator sub-role between Definer and Builder) | Fail — Auditor structure unchanged; Pass audit remains single named check with sub-bullets | Moderate-strong — named Prohibition Enumerator step generates PROHIBITED FORM-CLASS before Builder runs; form-class is a distinct pre-construction output; tests whether role-isolated enumeration satisfies C-22 vs inline template enumeration | Single-axis; role-boundary form-class generation; tests whether structural separation of the enumeration step affects C-22 compliance |
| V-04 | Lifecycle emphasis + Phrasing register (symmetric 3+3 checks + form-class prohibition) | Very strong — 3 individually named Pass checks (Check 4 location, Check 5 observable+standard, Check 6 prohibited-form) + same 3 Text checks; symmetric and independently operative; report distinguishes Text and Pass flag counts | Very strong — PROHIBITED DIRECTION section enumerates 5 variant phrasings with form-class closure; Auditor Check 1 tests the full form-class not the canonical example | Combined; closes C-21 and C-22 simultaneously; baseline for future rounds |
| V-05 | Inertia framing (Asymmetric-Audit + Example-Bounded competitors, both named at the phase where their gap is relevant) | Very strong — Asymmetric-Audit competitor concretizes the C-21 failure: 3 Text checks + 1 Pass check with sub-bullets; naming it forces 3 independently numbered Pass checks to surpass it | Very strong — Example-Bounded competitor concretizes the C-22 failure: "in any phrasing" claim without enumeration; naming it forces explicit variant listing and form-class closure in the PROHIBITED DIRECTION section | Combined; two-competitor architecture, each scoped to its target criterion |

---

## V-01 — Lifecycle emphasis (Symmetric 3+3 Auditor checks)

**Axis:** Lifecycle emphasis
**Hypothesis:** C-21 requires the post-draft audit to have equal granularity for Text and Pass checks — individually named, individually operative, separately reportable. R13 V-04's Auditor has 3 named Text checks and 1 named Pass check with 4 sub-bullets. V-01 fixes this by splitting Check 4 into three separately numbered Pass checks: Check 4 (Pass location — does LOCATION name a specific artifact section from the template options?), Check 5 (Pass observable and standard — does OBSERVABLE name a confirmable fact and STANDARD state a verifiable condition?), Check 6 (Pass prohibited-form — does any Pass line contain qualitative-only language?). What was Check 5 (coherence) becomes Check 7. This produces a 3+3 symmetric structure with a separate coherence check. The audit report explicitly tallies Text flags and Pass flags separately. C-22 is intentionally untouched: the TEMPLATE PAIR says "in any phrasing" without enumeration; Auditor Check 1 tests only the canonical form. Prediction: C-21 very strong; C-22 fail.

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. The TEMPLATE PAIR contains two fill-in templates in the exact phrasing register of the final criterion fields. The Builder fills the brackets to produce criteria — there is no interpretation step between your output and theirs. Do not draft criteria. Do not draft scoring.

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
  [Y] = [the specific required-property type for this skill -- the category of thing
         this skill's criteria will require; derive from skill spec and failure log;
         name the specific artifact element or output property, not an abstraction]
  [Z] = [the specific failure-consequence type when Y is absent -- what breaks in the
         artifact; name the damage; derive from failure log]
  [X] = [the specific rejected-form type -- the wrong-direction argument a Builder is
         tempted to write for this skill's domain; name the class of mistake]

Do not write "A criterion Text is..." or "The required form is:" before this template.
The sentence above IS the template. Fill the brackets and the result IS the Text field.
A Text beginning "[X] causes [failure]" -- in any phrasing -- is in the prohibited
direction and must be rewritten by filling this template.

PASS FILL-IN TEMPLATE (fill brackets to produce a criterion Pass field):
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name], fill the brackets as follows:
  LOCATION options (2-3 specific sections or fields in this skill's output type --
    the structural elements where criterion observables are found):
    - [location 1]
    - [location 2]
    - [location 3 if applicable]
  OBSERVABLE options (2-3 specific confirmable facts for this skill):
    - [observable 1]
    - [observable 2]
    - [observable 3 if applicable]
  Prohibited qualitative-only forms (1-2 forms tempting for this skill's domain):
    - [prohibited form 1]
    - [prohibited form 2 if applicable]

A criterion Pass IS these three lines with the brackets filled. Do not write
"the required form is:" before them. A Pass containing a prohibited form is not
a Pass condition -- return to this template and fill the brackets.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (both fill-in templates complete, skill-specific values filled in, bare fill-in form -- no "the structure is:" or "the required form is:" wrapper). Do not proceed to the Builder until both templates are present in bare fill-in form.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer. Build the rubric by filling the template brackets -- not by interpreting them.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y] with the specific required property for this criterion's failure mode. Replace [Z] with the failure consequence. Replace [X] with the rejected form. The Text field IS the filled sentence.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION from LOCATION options. Fill OBSERVABLE from OBSERVABLE options. State STANDARD. The Pass field IS the three filled lines. If you find yourself writing a prohibited form -- stop. Return to the PASS FILL-IN TEMPLATE and fill the brackets.

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

Read the TEMPLATE PAIR from the Dual Definer and the rubric draft from the Builder. Apply seven checks per criterion in isolation. Revise in-place where any check fails. Report each revision: criterion ID, check number, original content, revised content.

**Check 1 -- Direction (Text, isolated).** Read the Text field alone, with only the TEXT FILL-IN TEMPLATE visible. Does it follow "Without [Y filled], ... [Z filled]. Not [X filled], but [Y filled]."? Or does it argue "[X filled] causes [failure]" in any phrasing? If wrong direction: identify Y for this criterion from the failure log. Fill the TEXT FILL-IN TEMPLATE. Rewrite.

**Check 2 -- Contrast clause (Text).** Does the Text contain "not [X for this criterion], but [Y for this criterion]"? If absent: add the contrast clause using the TEXT FILL-IN TEMPLATE's X and Y scoped to this criterion.

**Check 3 -- Text isolation.** Does the Text pass Check 1 when the reader has ONLY the bare TEXT FILL-IN TEMPLATE sentence as context (no bracket guidance, no other criteria, no preamble)? A Text requiring surrounding context to be intelligible fails. Rewrite until the filled sentence is self-contained.

**Check 4 -- Pass location (Pass, isolated).** Read the Pass field's LOCATION line alone. Does it name a specific artifact section or field from the LOCATION options in the PASS FILL-IN TEMPLATE? General descriptions ("in the rubric," "in a criterion"), qualitative-only location claims, and absent LOCATION lines all fail this check. If insufficient: select a specific location from the Definer's LOCATION options and fill the LOCATION line.

**Check 5 -- Pass observable and standard (Pass, isolated).** Read the Pass field's OBSERVABLE and STANDARD lines alone. Does OBSERVABLE name a specific confirmable fact from the OBSERVABLE options -- a token, count, keyword, or pattern verifiable by reading the artifact without judgment? Does STANDARD state a verifiable condition (present | count >= N | matches pattern | absent)? Vague confirmables ("well-specified," "clearly present"), absent OBSERVABLE lines, and absent STANDARD lines all fail. If insufficient: fill from the OBSERVABLE options and state STANDARD explicitly.

**Check 6 -- Pass prohibited-form (Pass, isolated).** Read every line of the Pass field independently of Checks 4 and 5. Does any line contain a prohibited qualitative-only form from the PASS FILL-IN TEMPLATE list? A Pass field fails this check even if Check 4 and Check 5 pass -- a prohibited qualitative form embedded in a modifier or sub-clause fails independently. If present: remove the prohibited form and restate using the PASS FILL-IN TEMPLATE.

**Check 7 -- Pass-Text coherence.** Is the OBSERVABLE in Pass the logical conclusion of the Text argument? Does Pass name an observable not established in Text? If so: add grounding to Text or remove the ungrounded claim from Pass.

After all seven checks pass for every criterion, output the complete revised rubric. Prepend the revision log. Report totals: "Audit complete. Text flags: [direction N, contrast N, isolation N]. Pass flags: [location N, observable+standard N, prohibited-form N]. Coherence flags: [N]."

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the symmetric-audit principle: the Dual Definer produces both fill-in templates as a unified TEMPLATE PAIR; the Builder fills brackets from both templates without paraphrase; the Dual Auditor applies three individually named checks to Text fields and three individually named checks to Pass fields as parallel, independently operative audit tracks with separately reported flag tallies), then criteria ordered essential -> recommended -> aspirational (reference anchors retained; Dual Definer output and audit log omitted), then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 — Phrasing register (Form-class prohibition with enumerated variants)

**Axis:** Phrasing register
**Hypothesis:** C-22 requires the direction prohibition to be operationally form-class exhaustive -- not just "in any phrasing" as a claim but as an enforced constraint with enumerated variants. R13 V-04 says "in any phrasing" but names only one canonical form; Auditor Check 1 tests only that canonical form. A Builder who writes "[X] leads to [failure]" or "the artifact fails when [X] is present" escapes detection. V-02 fixes this by (a) replacing the single-example prohibition in the TEMPLATE PAIR with a PROHIBITED DIRECTION section that enumerates five variant phrasings and declares the form-class closed with "any semantically equivalent construction is equally prohibited," and (b) updating Auditor Check 1 to reference the full enumerated form-class. The audit structure is otherwise unchanged from R13 V-04 (3 Text checks + 1 sub-bullet Pass check), so C-21 remains unaddressed. Prediction: C-22 very strong; C-21 fail.

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. The TEMPLATE PAIR contains two fill-in templates in the exact phrasing register of the final criterion fields, plus a PROHIBITED DIRECTION section that closes the wrong-direction form-class. Do not draft criteria. Do not draft scoring.

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
  [Y] = [the specific required-property type for this skill -- derive from skill spec
         and failure log; name the specific artifact element or output property]
  [Z] = [the specific failure-consequence type when Y is absent -- name the damage;
         derive from failure log]
  [X] = [the specific rejected-form type -- the wrong-direction argument a Builder is
         tempted to write for this skill's domain; name the class of mistake]

The sentence above IS the template. Fill the brackets; the result IS the Text field.
Do not write "A criterion Text is..." or "The required form is:" before this template.

PROHIBITED DIRECTION -- form-class exhaustive. A criterion Text is in the prohibited
direction if it locates the causal chain in the wrong form's consequence rather than
the required property's absence. For this skill, all of the following are prohibited
(fill [X] and [failure] with your skill-specific values from the [X] and [Z] entries):

  Canonical:    "[X] causes [failure]"
  Variant 1:    "[X] leads to [failure]"
  Variant 2:    "the artifact [fails] when [X] is present"
  Variant 3:    "the rubric [breaks] because [X] occurs"
  Variant 4:    "presence of [X] produces [bad outcome]"
  Variant 5:    [derive one additional skill-specific variant -- a phrasing a Builder
                 of this rubric type would naturally write that encodes the same
                 wrong causal direction: wrong form as subject, failure as predicate]

These phrasings share the same causal structure. The form-class is closed: any
semantically equivalent construction is equally prohibited. Naming a new synonym does
not escape the prohibition. The check is not "does this match the canonical example?"
The check is "does this locate causality in the wrong form's consequence?"

Escape: identify Y (the required property for this criterion) and write:
"Without [Y], the artifact [fails] because [Z]."

PASS FILL-IN TEMPLATE (fill brackets to produce a criterion Pass field):
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name], fill the brackets as follows:
  LOCATION options (2-3 specific sections or fields in this skill's output type):
    - [location 1]
    - [location 2]
    - [location 3 if applicable]
  OBSERVABLE options (2-3 specific confirmable facts for this skill):
    - [observable 1]
    - [observable 2]
    - [observable 3 if applicable]
  Prohibited qualitative-only forms (1-2 forms tempting for this skill's domain):
    - [prohibited form 1]
    - [prohibited form 2 if applicable]

A criterion Pass IS these three lines with the brackets filled. A Pass containing
a prohibited form is not a Pass condition -- return to this template and fill.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (TEXT FILL-IN TEMPLATE in bare fill-in form; PROHIBITED DIRECTION section with canonical form + >= 4 enumerated variants + form-class closure statement + skill-specific Variant 5; PASS FILL-IN TEMPLATE in bare fill-in form with LOCATION, OBSERVABLE, and prohibited-forms instantiated). Do not proceed to the Builder until the PROHIBITED DIRECTION section is fully enumerated.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer. Build the rubric by filling the template brackets -- not by interpreting them.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y], [Z], [X] with the specific values for this criterion's failure mode. The Text field IS the filled sentence. If you find yourself writing any form in the PROHIBITED DIRECTION -- including the canonical form, any enumerated variant, or any semantically equivalent construction -- stop. Identify Y and rewrite by filling the TEXT FILL-IN TEMPLATE.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION from LOCATION options. Fill OBSERVABLE from OBSERVABLE options. State STANDARD. If you find yourself writing a prohibited qualitative-only form -- stop. Return to the PASS FILL-IN TEMPLATE and fill the brackets.

**Essential criteria (3-5).** From broken failure modes. Five fields per criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: filled TEXT FILL-IN TEMPLATE
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: filled PASS FILL-IN TEMPLATE (all three lines: LOCATION, OBSERVABLE, STANDARD)

**Recommended criteria (2-3).** Pass tests degree, precision, or specificity. Annotate: **Property tested:** [degree | precision | specificity].

**Aspirational criteria (1-2).** Reference anchor per criterion:

```
Reference: [specific prior rubric or class passing C-01--C-08]
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

**BUILDER GATE:** Complete rubric draft. No Text field contains any form in the PROHIBITED DIRECTION, including enumerated variants. All Pass fields are three-line filled blocks.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR from the Dual Definer and the rubric draft from the Builder. Apply five checks per criterion in isolation. Revise in-place where any check fails.

**Check 1 -- Direction and form-class (Text, isolated).** Read the Text field alone, with only the TEXT FILL-IN TEMPLATE and PROHIBITED DIRECTION section visible. Does it follow "Without [Y filled], ... [Z filled]. Not [X filled], but [Y filled]."? Or does it contain any phrasing from the PROHIBITED DIRECTION form-class -- the canonical form, any enumerated variant, or any semantically equivalent construction? The check function is not "does this match the canonical example?" -- it is "does this locate causality in the wrong form's consequence, in any phrasing?" If any prohibited form is present: identify Y, fill the TEXT FILL-IN TEMPLATE, rewrite.

**Check 2 -- Contrast clause (Text).** "not [X for this criterion], but [Y for this criterion]" present? If absent: add.

**Check 3 -- Text isolation.** Text passes Check 1 with only the bare TEXT FILL-IN TEMPLATE visible (no bracket guidance, no preamble, no other criteria)? If not: rewrite until self-contained.

**Check 4 -- Pass verifiability (Pass, isolated).** Read the Pass field with only the PASS FILL-IN TEMPLATE visible. Apply:
- *LOCATION line:* specific section or field from LOCATION options? If not: fill.
- *OBSERVABLE line:* specific confirmable fact from OBSERVABLE options? If not: fill.
- *STANDARD line:* verifiable condition stated? If not: add.
- *Prohibited forms:* any prohibited qualitative-only form present? If yes: replace.

**Check 5 -- Pass-Text coherence.** OBSERVABLE is logical conclusion of Text argument? No ungrounded observables in Pass? Fix if needed.

After all checks pass, output complete revised rubric with revision log.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the form-class exhaustive principle: the Dual Definer's TEMPLATE PAIR includes a PROHIBITED DIRECTION section enumerating the canonical form plus 5 skill-specific variants with an explicit form-class closure statement; the prohibition is not example-bounded -- any semantically equivalent construction is equally prohibited regardless of surface phrasing; the Dual Auditor's Check 1 tests every Text field against the full enumerated form-class, not just the canonical example), then TEMPLATE PAIR (retained in artifact with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational, then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 — Role sequence (Prohibition Enumerator sub-role)

**Axis:** Role sequence
**Hypothesis:** C-22's form-class exhaustiveness requirement could be satisfied by making the enumeration a structurally separate role step rather than embedding it in the TEMPLATE PAIR. A named Prohibition Enumerator runs between the Dual Definer and the Builder. It receives the TEMPLATE PAIR (specifically [X], the rejected form type) and produces a PROHIBITED FORM-CLASS: a bounded list of 4+ variant phrasings plus an explicit closure statement and escape instruction. The Builder and Auditor receive both the TEMPLATE PAIR and the PROHIBITED FORM-CLASS as distinct inputs. The key test: does role-isolated generation of the form-class satisfy C-22's "form-class exhaustive" requirement, or is embedding enumeration in the TEMPLATE PAIR itself required? The hypothesis is that role isolation is sufficient -- the form-class is generated before construction, explicitly instantiated for this skill, and provided as binding Auditor input -- but the evidence may show that a separate role step is a weaker mechanism than a prohibition embedded directly in the template. Audit structure is unchanged from R13 V-04 (3 Text + 1 Pass check), so C-21 is untouched. Prediction: C-22 moderate-strong; C-21 fail.

---

You are a four-role rubric construction system. Roles run in strict sequence: Dual Definer -> Prohibition Enumerator -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. The TEMPLATE PAIR contains two fill-in templates in the exact phrasing register of the final criterion fields. Do not draft criteria. Do not draft scoring.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

**TEMPLATE PAIR.** Write both templates as bare fill-in forms.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE (fill brackets to produce a criterion Text field):
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name], fill the brackets as follows:
  [Y] = [the specific required-property type -- derive from skill spec and failure log]
  [Z] = [the specific failure-consequence type when Y is absent -- name the damage]
  [X] = [the specific rejected-form type -- the wrong-direction argument for this domain]

The sentence above IS the template. Fill the brackets; the result IS the Text field.
Do not write "A criterion Text is..." or "The required form is:" before this template.

PASS FILL-IN TEMPLATE (fill brackets to produce a criterion Pass field):
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name], fill the brackets as follows:
  LOCATION options: [2-3 specific sections or fields in this skill's output]
  OBSERVABLE options: [2-3 specific confirmable facts for this skill]
  Prohibited qualitative-only forms: [1-2 tempting but unverifiable forms]

A criterion Pass IS these three lines with the brackets filled.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and TEMPLATE PAIR (both templates in bare fill-in form). Do not proceed to the Prohibition Enumerator until both templates are present.

---

### PROHIBITION ENUMERATOR ROLE

Read the TEMPLATE PAIR from the Dual Definer. Your sole input is the TEMPLATE PAIR. Your sole output is a PROHIBITED FORM-CLASS. Do not draft criteria.

The TEMPLATE PAIR specifies [X] -- the type of rejected form a Builder would write for this skill's domain. Your task: generate the PROHIBITED FORM-CLASS covering all variant phrasings of the wrong-direction argument for this specific skill.

**Step E-1 -- Canonical form.** State the canonical prohibited phrasing, filled with skill-specific X and failure terms from the TEMPLATE PAIR:

```
Canonical: "[X -- skill-specific] causes [failure -- skill-specific]"
```

**Step E-2 -- Variant phrasings.** Generate 4+ variant phrasings encoding the same causal direction (wrong form as subject, failure as predicate), filled with skill-specific terms:

```
Variant 1: "[X] leads to [failure]"
Variant 2: "the artifact [fails] when [X] is present"
Variant 3: "the rubric [breaks] because [X] occurs"
Variant 4: "presence of [X] produces [bad outcome]"
Variant 5: [skill-specific variant -- a phrasing a Builder of this rubric type would
            naturally write; derive from the failure log's structural gap language]
```

**Step E-3 -- Form-class closure.** Write the PROHIBITED FORM-CLASS:

```
PROHIBITED FORM-CLASS for [skill name]:

  Canonical:  [filled canonical form]
  Variant 1:  [filled variant 1]
  Variant 2:  [filled variant 2]
  Variant 3:  [filled variant 3]
  Variant 4:  [filled variant 4]
  Variant 5:  [filled skill-specific variant]

Form-class definition: a criterion Text is in the prohibited direction if it locates
the causal chain in the wrong form's consequence rather than the required property's
absence. All phrasings above share this structure. The form-class is closed -- any
semantically equivalent construction is equally prohibited. Naming a new synonym
does not escape.

Escape: identify Y (the required property) and write:
"Without [Y], the artifact [fails] because [Z]."
```

**PROHIBITION ENUMERATOR GATE:** Output is the PROHIBITED FORM-CLASS (canonical form + >= 4 skill-specific variants + closure statement + escape instruction). Do not proceed to the Builder until the PROHIBITED FORM-CLASS is written.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer, and the PROHIBITED FORM-CLASS from the Prohibition Enumerator. Build the rubric by filling the template brackets.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Fill [Y], [Z], [X] from this criterion's failure mode. The Text IS the filled sentence. If you find yourself writing any phrasing in the PROHIBITED FORM-CLASS -- canonical form, enumerated variants, or any semantically equivalent construction -- stop. Identify Y and rewrite.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION, OBSERVABLE, STANDARD from the template options. If you find yourself writing a prohibited qualitative form -- stop. Return to the template.

**Essential criteria (3-5).** Five fields: ID (C-NN), Text (filled TEXT template), Weight (essential), Category, Pass (filled PASS template).

**Recommended criteria (2-3).** Pass tests degree, precision, or specificity. **Property tested:** [degree | precision | specificity].

**Aspirational criteria (1-2).** Reference anchor per criterion.

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE:** Complete draft. No Text field contains any form in the PROHIBITED FORM-CLASS.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR from the Dual Definer, the PROHIBITED FORM-CLASS from the Prohibition Enumerator, and the rubric draft from the Builder. Apply five checks per criterion in isolation.

**Check 1 -- Direction and form-class (Text, isolated).** Read the Text field alone. Does it follow "Without [Y], ... [Z]. Not [X], but [Y]."? Or does it contain any phrasing from the PROHIBITED FORM-CLASS -- canonical form, any of the five variants, or any semantically equivalent construction? A Text that avoids the canonical form but uses an enumerated variant fails. If prohibited: identify Y, fill the TEXT FILL-IN TEMPLATE, rewrite.

**Check 2 -- Contrast clause (Text).** "not [X], but [Y]" present? If absent: add.

**Check 3 -- Text isolation.** Text intelligible with only the bare TEXT FILL-IN TEMPLATE visible? If not: rewrite.

**Check 4 -- Pass verifiability (Pass, isolated).** Read Pass with only the PASS FILL-IN TEMPLATE visible:
- *LOCATION:* specific location from LOCATION options? If not: fill.
- *OBSERVABLE:* specific confirmable fact from OBSERVABLE options? If not: fill.
- *STANDARD:* verifiable condition stated? If not: add.
- *Prohibited forms:* qualitative-only form present? If yes: replace.

**Check 5 -- Pass-Text coherence.** OBSERVABLE is logical conclusion of Text argument? No ungrounded observables? Fix if needed.

After all checks pass, output complete revised rubric with revision log.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the role-sequenced form-class principle: the Dual Definer produces the TEMPLATE PAIR naming the rejected form type [X]; the Prohibition Enumerator generates a PROHIBITED FORM-CLASS before the Builder runs, producing the canonical form plus 5 skill-specific variant phrasings with an explicit closure statement; the Dual Auditor tests every Text field against the full PROHIBITED FORM-CLASS, not just the canonical form), then PROHIBITED FORM-CLASS (retained in artifact), then criteria ordered essential -> recommended -> aspirational, then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 — Lifecycle emphasis + Phrasing register (Symmetric 3+3 checks + form-class prohibition)

**Axes:** Lifecycle emphasis + phrasing register
**Hypothesis:** V-01 achieves C-21 by splitting the Auditor's Pass check into 3 separately numbered checks (location, observable+standard, prohibited-form) matching the 3 Text checks. V-02 achieves C-22 by embedding a PROHIBITED DIRECTION section with 5 enumerated variants and a form-class closure statement in the TEMPLATE PAIR, and updating Auditor Check 1 to reference the full form-class. V-04 combines both. The Dual Definer's TEMPLATE PAIR contains the form-class exhaustive PROHIBITED DIRECTION section. The Dual Auditor runs seven checks: Check 1 (direction+form-class / Text), Check 2 (contrast / Text), Check 3 (isolation / Text), Check 4 (location / Pass), Check 5 (observable+standard / Pass), Check 6 (prohibited-form / Pass), Check 7 (coherence). The audit report explicitly tallies Text flags and Pass flags separately. Prediction: C-21 very strong (symmetric 3+3 check counts, each independently named and reportable); C-22 very strong (enumerated form-class, form-class declared closed, Auditor Check 1 tests the full class).

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. The TEMPLATE PAIR contains two fill-in templates in the exact phrasing register of the final criterion fields, plus a PROHIBITED DIRECTION section that closes the wrong-direction form-class. The Builder fills the brackets to produce criteria -- there is no interpretation step between your output and theirs. Do not draft criteria. Do not draft scoring.

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
  [Y] = [the specific required-property type for this skill -- derive from skill spec
         and failure log; name the specific artifact element or output property]
  [Z] = [the specific failure-consequence type when Y is absent -- name the damage;
         derive from failure log]
  [X] = [the specific rejected-form type -- the wrong-direction argument a Builder is
         tempted to write for this skill's domain; name the class of mistake]

The sentence above IS the template. Fill the brackets; the result IS the Text field.
Do not write "A criterion Text is..." or "The required form is:" before this template.

PROHIBITED DIRECTION -- form-class exhaustive. A criterion Text is in the prohibited
direction if it locates the causal chain in the wrong form's consequence rather than
the required property's absence. For this skill, all of the following are prohibited
(fill [X] and [failure] with your skill-specific values from the entries above):

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [derive one additional skill-specific variant -- a phrasing natural to
               this rubric domain that encodes the same wrong causal direction]

The form-class is closed. Any semantically equivalent construction is equally
prohibited. Naming a new synonym does not escape. The check is not "does this
match the canonical example?" -- it is "does this locate causality in the wrong
form's consequence, in any phrasing?"

Escape: identify Y (the required property) and write:
"Without [Y], the artifact [fails] because [Z]."

PASS FILL-IN TEMPLATE (fill brackets to produce a criterion Pass field):
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name], fill the brackets as follows:
  LOCATION options (2-3 specific sections or fields in this skill's output type --
    structural elements where criterion observables are found):
    - [location 1]
    - [location 2]
    - [location 3 if applicable]
  OBSERVABLE options (2-3 specific confirmable facts for this skill):
    - [observable 1]
    - [observable 2]
    - [observable 3 if applicable]
  Prohibited qualitative-only forms (1-2 forms tempting for this skill's domain):
    - [prohibited form 1]
    - [prohibited form 2 if applicable]

A criterion Pass IS these three lines with the brackets filled. A Pass containing
a prohibited qualitative form is not a Pass condition -- return to this template.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (TEXT FILL-IN TEMPLATE in bare fill-in form; PROHIBITED DIRECTION section with canonical form + >= 4 enumerated variants + form-class closure statement + skill-specific Variant 5 instantiated; PASS FILL-IN TEMPLATE in bare fill-in form with all options and prohibited forms instantiated). Do not proceed to the Builder until all elements are present.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer. Build the rubric by filling the template brackets -- not by interpreting them.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y], [Z], [X] with this criterion's specific values. The Text IS the filled sentence. If you find yourself writing any form in the PROHIBITED DIRECTION -- canonical form, any enumerated variant, or any semantically equivalent construction -- stop. Identify Y and rewrite.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION, OBSERVABLE, STANDARD from the template options. If you find yourself writing a prohibited qualitative form -- stop. Return to the template.

**Essential criteria (3-5).** Five fields per criterion:

- **ID**: C-NN (sequential, starting at C-01)
- **Text**: filled TEXT FILL-IN TEMPLATE
- **Weight**: essential
- **Category**: correctness | depth | format | coverage | behavior
- **Pass**: filled PASS FILL-IN TEMPLATE (all three lines)

**Recommended criteria (2-3).** Pass tests degree, precision, or specificity. **Property tested:** [degree | precision | specificity].

**Aspirational criteria (1-2).** Reference anchor per criterion.

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE:** Complete draft. No Text field contains any PROHIBITED DIRECTION form. All Pass fields are three-line filled blocks.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR from the Dual Definer and the rubric draft from the Builder. Apply seven checks per criterion in isolation. Revise in-place where any check fails. Report each revision: criterion ID, check number, original content, revised content.

**Check 1 -- Direction and form-class (Text, isolated).** Read the Text field alone, with only the TEXT FILL-IN TEMPLATE and PROHIBITED DIRECTION section visible. Does it follow "Without [Y filled], ... [Z filled]. Not [X filled], but [Y filled]."? Or does it contain any phrasing from the PROHIBITED DIRECTION form-class -- the canonical form, any enumerated variant, or any semantically equivalent construction? The check function is "does this locate causality in the wrong form's consequence, in any phrasing?" -- not "does this match the canonical example." If any prohibited form is present: identify Y, fill the TEXT FILL-IN TEMPLATE, rewrite.

**Check 2 -- Contrast clause (Text).** "not [X for this criterion], but [Y for this criterion]" present in Text? If absent: add.

**Check 3 -- Text isolation.** Text passes Check 1 with only the bare TEXT FILL-IN TEMPLATE sentence visible (no bracket guidance, no preamble, no other criteria)? If not: rewrite until self-contained.

**Check 4 -- Pass location (Pass, isolated).** Read the LOCATION line alone. Specific artifact section or field from the LOCATION options? General descriptions, absent LOCATION lines, and qualitative-only location claims fail. If insufficient: select a specific location from the LOCATION options. Fill.

**Check 5 -- Pass observable and standard (Pass, isolated).** Read the OBSERVABLE and STANDARD lines alone. OBSERVABLE: specific confirmable fact from OBSERVABLE options, verifiable without judgment? STANDARD: verifiable condition (present | count >= N | matches pattern | absent)? Vague confirmables, absent OBSERVABLE, absent STANDARD all fail. If insufficient: fill from OBSERVABLE options; state STANDARD.

**Check 6 -- Pass prohibited-form (Pass, isolated).** Read every Pass line independently of Checks 4 and 5. Any prohibited qualitative-only form from the PASS FILL-IN TEMPLATE list present -- including in modifiers or sub-clauses? A Pass that passes Checks 4 and 5 can still fail Check 6. If present: remove and restate using the PASS FILL-IN TEMPLATE.

**Check 7 -- Pass-Text coherence.** OBSERVABLE is logical conclusion of Text argument? No ungrounded observables in Pass? Fix if needed.

After all seven checks pass, output complete revised rubric. Prepend revision log. Report totals: "Audit complete. Text flags: [direction+form-class N, contrast N, isolation N]. Pass flags: [location N, observable+standard N, prohibited-form N]. Coherence flags: [N]."

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the symmetric-audit + form-class-exhaustive principle: the Dual Definer's TEMPLATE PAIR includes a PROHIBITED DIRECTION section enumerating the wrong-direction form-class with 5 variant phrasings and an explicit form-class closure statement; the Dual Auditor applies three individually named checks to the Text field and three individually named checks to the Pass field as parallel, independently operative audit tracks; the audit report distinguishes Text and Pass flag counts, making the parallel structure structurally visible in the output), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational, then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 — Inertia framing (Asymmetric-Audit + Example-Bounded competitors)

**Axes:** Inertia framing + lifecycle emphasis + phrasing register
**Hypothesis:** R11 V-05 demonstrated that naming a near-passing competitor at the exact phase where its gap is relevant makes the gap non-abstract. V-05 applies the two-competitor architecture to C-21 and C-22. Competitor 1 (Asymmetric-Audit Protocol) passes C-16 and C-17 but fails C-21: 3 Text checks + 1 Pass check with sub-bullets -- sub-bullet granularity is structurally subordinate to named-check granularity. Named before the Auditor section, this forces the protocol to specify 3 independently numbered Pass checks. Competitor 2 (Example-Bounded Protocol) passes C-15 but fails C-22: "in any phrasing" claim without enumeration, Auditor Check 1 tests canonical form only. Named before the TEMPLATE PAIR is specified, this forces the protocol to enumerate variants and close the form-class. The competitors are not generic warnings -- each is placed at the exact phase where its failure mode would otherwise be produced. Prediction: C-21 very strong (Competitor 1 makes the granularity asymmetry concrete; the protocol specifies 3 named Pass checks to surpass it); C-22 very strong (Competitor 2 makes the example-bounded gap concrete; the protocol enumerates variants to surpass it).

---

You are building a scoring rubric for a Signal skill. The rubric is the objective function for quest-golden. Your protocol has two direct competitors. Each satisfies C-01 through C-20. Each fails exactly one of the two new target criteria.

---

**Competitor 1: The Asymmetric-Audit Protocol**

The Asymmetric-Audit Protocol runs three individually named Text checks and one named Pass check per criterion. Text checks: Check 1 (direction), Check 2 (contrast), Check 3 (isolation). Pass check: Check 4 (verifiability), which contains four sub-bullets: LOCATION present, OBSERVABLE present, STANDARD present, no prohibited forms.

The Asymmetric-Audit Protocol satisfies C-16 (two-phase direction and contrast enforcement), C-17 (two-phase testability enforcement), and all of C-01 through C-20.

The Asymmetric-Audit Protocol fails C-21 because its post-draft audit runs three individually operative, separately reportable checks against the Text field and one check (with sub-bullets) against the Pass field. The sub-bullets address four distinct Pass concerns but they share one check number, making them structurally subordinate in granularity to the Text checks. An evaluator reports "Check 4 passed" or "Check 4 failed" for the entire Pass field; they cannot report "Check 4 (location) failed but Check 5 (observable) passed" because those concerns are sub-bullets, not separate checks. C-21 requires Pass audit granularity to match Text audit granularity: three individually numbered Pass checks, each with its own pass/fail determination.

**Your protocol must go further than the Asymmetric-Audit Protocol.** The post-draft audit must run three individually numbered Pass checks -- one for location (is LOCATION a specific artifact section from the template options?), one for observable and standard (is OBSERVABLE a specific confirmable fact? is STANDARD a verifiable condition?), one for prohibited-form (does any line contain a prohibited qualitative form?) -- each independently reportable, matching the three Text checks in count and structural status.

---

**Competitor 2: The Example-Bounded Protocol**

The Example-Bounded Protocol includes a direction prohibition in its TEMPLATE PAIR: "A Text beginning '[X] causes [failure]' -- in any phrasing -- is in the prohibited direction." Auditor Check 1 is direction-aware and references this prohibition. The protocol satisfies C-15 (correct direction identified, required direction specified) and all of C-01 through C-20.

The Example-Bounded Protocol fails C-22 because although it claims "in any phrasing," it names only the canonical form. Auditor Check 1 detects "[X] causes [failure]" and its exact negations. A Builder who writes "[X] leads to [failure]" or "the artifact fails when [X] is present" passes Check 1 because neither matches the named example. The "in any phrasing" claim is aspirational but not operationally enforced: no variant phrasings are enumerated, the form-class boundary is not stated, and the Auditor has no mechanism to catch semantically equivalent constructions. C-22 requires the prohibition to be operationally exhaustive: the TEMPLATE PAIR must enumerate 4+ variant phrasings, declare the form-class closed, and Auditor Check 1 must test against the full enumerated class.

**Your protocol must go further than the Example-Bounded Protocol.** The TEMPLATE PAIR's PROHIBITED DIRECTION section must name the canonical form and at least four variant phrasings -- filled with skill-specific X and failure terms -- state that any semantically equivalent construction is equally prohibited, and declare the form-class closed. Auditor Check 1 must test against the full enumerated form-class, not the canonical example.

---

**Read the skill spec and sample outputs.**

**STEP 1 -- FAILURE MODES**

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

Minimum: 3 broken, 2 suboptimal. Do not proceed until >= 5 entries.

---

**STEP 2 -- DUAL DEFINER**

Beyond the Example-Bounded Protocol, the PROHIBITED DIRECTION section enumerates 4+ variant phrasings and explicitly closes the form-class. Write the TEMPLATE PAIR now.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE (fill brackets to produce a criterion Text field):
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name]:
  [Y] = [specific required-property type; derive from failure log and skill spec]
  [Z] = [specific failure-consequence when Y is absent; name the damage]
  [X] = [specific rejected-form type; the wrong-direction argument for this domain]

The sentence above IS the template. Fill the brackets; the result IS the Text field.
Do not write "A criterion Text is..." or "The required form is:" before this template.

PROHIBITED DIRECTION -- form-class exhaustive. Prohibited phrasings (fill with
skill-specific [X] and failure terms from your entries above):

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [skill-specific variant derived from this domain's natural wrong-direction
               phrasing; encode the same causal structure: wrong form as subject,
               failure as predicate]

Form-class is closed. Any semantically equivalent construction is equally prohibited.
The check is not "does this match the canonical example?" -- it is "does this locate
causality in the wrong form's consequence, in any phrasing?"

Escape: identify Y; write: "Without [Y], the artifact [fails] because [Z]."

PASS FILL-IN TEMPLATE (fill brackets to produce a criterion Pass field):
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name]:
  LOCATION options: [2-3 specific sections or fields in this skill's output type]
  OBSERVABLE options: [2-3 specific confirmable facts for this skill]
  Prohibited qualitative-only forms: [1-2 tempting but unverifiable forms]

A criterion Pass IS these three lines with the brackets filled.
```

**DEFINER GATE:** TEMPLATE PAIR present. PROHIBITED DIRECTION section includes canonical form + >= 4 enumerated variants (skill-specific) + form-class closure statement. Do not proceed to STEP 3 until gate clears.

---

**STEP 3 -- BUILDER**

Read failure log and TEMPLATE PAIR. Fill template brackets.

**Text field:** fill [Y], [Z], [X] from this criterion's failure mode. Filled sentence IS the Text. Any phrasing in the PROHIBITED DIRECTION form-class -- canonical, enumerated variants, or any semantically equivalent construction -- is prohibited. Identify Y and rewrite.

**Pass field:** fill LOCATION, OBSERVABLE, STANDARD from PASS FILL-IN TEMPLATE options. Three filled lines ARE the Pass field.

**Essential (3-5):** ID (C-NN), Text (filled), Weight (essential), Category, Pass (filled, all three lines).

**Recommended (2-3):** Pass tests degree, precision, or specificity. **Property tested:** [degree | precision | specificity].

**Aspirational (1-2):** Reference anchor per criterion.

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE:** Complete draft. No prohibited direction form in any Text. All Pass fields three-line blocks.

---

**STEP 4 -- DUAL AUDITOR**

Beyond the Asymmetric-Audit Protocol, the post-draft audit runs three individually named Pass checks matching the three Text checks. Apply seven checks per criterion in isolation.

**Check 1 -- Direction and form-class (Text, isolated).** Read the Text field alone with only the TEXT FILL-IN TEMPLATE and PROHIBITED DIRECTION section visible. Does it follow "Without [Y], ... [Z]. Not [X], but [Y]."? Or does it contain any phrasing from the PROHIBITED DIRECTION form-class -- canonical, any enumerated variant, or any semantically equivalent construction? The check is "does this locate causality in the wrong form's consequence?" -- not "does this match the canonical example." If prohibited: identify Y, fill TEXT FILL-IN TEMPLATE, rewrite.

**Check 2 -- Contrast clause (Text).** "not [X], but [Y]" present? If absent: add.

**Check 3 -- Text isolation.** Text passes Check 1 with only the bare TEXT FILL-IN TEMPLATE visible? If not: rewrite until self-contained.

**Check 4 -- Pass location (Pass, isolated).** LOCATION line names a specific artifact section from the LOCATION options? General descriptions and absent lines fail. If insufficient: fill from LOCATION options.

**Check 5 -- Pass observable and standard (Pass, isolated).** OBSERVABLE names a specific confirmable fact from OBSERVABLE options, verifiable without judgment? STANDARD states a verifiable condition? Vague confirmables, absent lines fail. If insufficient: fill from OBSERVABLE options; state STANDARD.

**Check 6 -- Pass prohibited-form (Pass, isolated).** Every Pass line free of prohibited qualitative-only forms from the PASS FILL-IN TEMPLATE list -- including in modifiers and sub-clauses? A Pass that passes Checks 4 and 5 can still fail Check 6. If present: remove and restate using the PASS FILL-IN TEMPLATE.

**Check 7 -- Pass-Text coherence.** OBSERVABLE is logical conclusion of Text argument? No ungrounded observables? Fix if needed.

Audit report: "Audit complete. Text flags: [direction+form-class N, contrast N, isolation N]. Pass flags: [location N, observable+standard N, prohibited-form N]. Coherence flags: [N]."

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state that this protocol surpasses both competitors: the Asymmetric-Audit Protocol fails C-21 via sub-bullet Pass audit, surpassed here by three individually named Pass checks with separate flag reporting; the Example-Bounded Protocol fails C-22 via un-enumerated form-class, surpassed here by a PROHIBITED DIRECTION section enumerating 5 skill-specific variant phrasings with an explicit form-class closure declaring the check function as "does this locate causality in the wrong form's consequence, in any phrasing?"), then TEMPLATE PAIR with PROHIBITED DIRECTION section (retained in artifact as construction standard), then criteria ordered essential -> recommended -> aspirational, then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
