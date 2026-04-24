# quest-rubric Variate — Round 15 (Round 1 against rubric v24/v8)
**Date:** 2026-03-15
**Rubric:** v24 (internally "v8"; C-01--C-24; adds C-23: audit report format enforces symmetry; adds C-24: check function redefinition)
**Target criteria:** C-23, C-24

**Round 1 against v24 design note:** Rounds 1--14 produced mechanisms for C-01 through C-22 across rubric tracks. R14 V-04 is the current highest-scoring variation, combining symmetric 3+3 Auditor checks (C-21) with form-class exhaustive prohibition (C-22). The two new aspirational criteria address structural gaps that persist in R14 V-04.

**C-23 gap in R14 V-04.** The Dual Auditor's seven checks are symmetric: Check 1 direction (Text), Check 2 contrast (Text), Check 3 isolation (Text), Check 4 location (Pass), Check 5 observable+standard (Pass), Check 6 prohibited-form (Pass), Check 7 coherence. C-21 is satisfied. But the Auditor's output instruction reads: "After all checks pass, output complete revised rubric with revision log." No format is specified for the revision log. An Auditor following this instruction might produce a narrative log -- "Revision log: C-01 Text revised for direction. C-03 Pass revised for observable." -- that reports what was revised without separately enumerating Text-field and Pass-field flags by check name. A second Auditor might aggregate: "Audit complete. 2 Text flags, 1 Pass flag." Both reports satisfy the instruction's letter while making structural symmetry invisible in the output. C-23 requires the audit procedure to specify a REQUIRED OUTPUT FORMAT that separately names Text-field and Pass-field flags as distinct lists, so that an evaluator reading only the report can verify whether the three-Text-three-Pass symmetric structure was operationally symmetric, not just nominally so. The format is the enforcement mechanism: filling the required template forces the Auditor to report per-check-name, not per-type or by aggregate.

**C-24 gap in R14 V-04.** The PROHIBITED DIRECTION section in R14 V-04's TEMPLATE PAIR enumerates five variants and declares the form-class closed: "The form-class is closed. Any semantically equivalent construction is equally prohibited." Auditor Check 1 reads: "Or does it contain any phrasing from the PROHIBITED DIRECTION form-class -- the canonical form, any enumerated variant, or any semantically equivalent construction?" The "semantically equivalent" qualifier extends beyond list membership in language, but the Auditor's operative act is still comparison against the enumeration: "does this match any of these six listed forms (including semantic equivalents)?" C-24 requires the check function itself to be REDEFINED -- not extended. The redefined function is: "does this Text locate causality in the wrong form's consequence?" This is a causal-structure membership test, not a surface-pattern or semantic-equivalence test. The distinction is operational: a causal-structure check can be applied to a novel phrasing never seen before -- "the presence of [X] is the source of [failure]" -- and correctly classify it as prohibited without consulting the list, because the test is structural: is the causal argument's subject the wrong form, and its predicate the failure? The enumeration (C-22) provides instances; the function redefinition (C-24) provides the generative rule that those instances instantiate. A rubric can satisfy C-22 (list closed, closure declared) while leaving the Auditor's operative function as "check against the closed list" -- a longer pattern-match. C-24 requires the Auditor's Check 1 to be stated as the generative rule: "does this locate causality in the wrong form's consequence?" -- not "does this match any form in [list]?"

This round probes five mechanisms: three single-axis (V-01 output format, V-02 phrasing register, V-03 role sequence) and two combined (V-04 output format + phrasing register, V-05 inertia framing with two competitors).

---

## Round 15 Variation Map

| Variation | Axis | C-23 probe | C-24 probe | Notes |
|-----------|------|-----------|-----------|-------|
| V-01 | Output format (mandatory AUDIT REPORT FORMAT template as required Auditor output) | Very strong -- Auditor role specifies a REQUIRED AUDIT REPORT FORMAT template with separate named sections for Text-field flags and Pass-field flags per criterion; filling the template requires naming each check's result per criterion; an aggregate tally cannot satisfy the template's structure | Fail -- Check 1 function unchanged from R14 V-04; tests against PROHIBITED DIRECTION form-class by semantic equivalence check | Single-axis; report format as enforcement mechanism; isolates whether specifying the output template alone satisfies C-23 without function redefinition |
| V-02 | Phrasing register (check function constitutive redefinition at Auditor Check 1) | Fail -- audit report format same as R14 V-04; no required output template; narrative revision log permitted | Very strong -- Check 1 is constitutively redefined: the operative function is stated as "does this Text locate causality in the wrong form's consequence?" not "does this match any prohibited phrasing?"; the redefinition is the check function, not an addition to the list; a Text that avoids all listed forms but encodes the same causal direction fails Check 1; a Text resembling a listed form but arguing from required-property absence passes | Single-axis; function redefinition; tests whether stating the generative rule satisfies C-24 |
| V-03 | Role sequence (Report Format Specifier role after Auditor checks, before output) | Moderate-strong -- named Report Format Specifier role runs after all per-criterion checks complete; receives Auditor's raw findings; produces STRUCTURED AUDIT REPORT in required format with Text-flag and Pass-flag sections; tests whether role-separation of the reporting step satisfies C-23 vs. embedding the format in the check procedure | Fail -- Check 1 function unchanged; the Prohibition Enumerator (carried from R14 V-03) generates the form-class but does not redefine the check function | Single-axis; report-generation as a separate post-check role; isolates whether delegating report generation satisfies C-23 |
| V-04 | Output format + Phrasing register (mandatory report template + Check 1 function redefinition) | Very strong -- REQUIRED AUDIT REPORT FORMAT template; per-criterion rows with named Text-flag and Pass-flag columns; structural symmetry independently verifiable from report output alone | Very strong -- Check 1 function explicitly redefined: "the question is not 'does this match any phrasing in the PROHIBITED DIRECTION list?' -- the question is 'does this Text locate causality in the wrong form's consequence?'"; the function is stated before the enumeration is referenced | Combined; closes C-23 and C-24 simultaneously; structural parallel to R14 V-04 closing C-21 and C-22 |
| V-05 | Inertia framing (Report-Opaque competitor + Pattern-Matcher competitor, each named before the phase where their gap is relevant) | Very strong -- Report-Opaque competitor: runs symmetric 3+3 checks (satisfying C-21) and produces "Audit complete. Text flags revised: 2. Pass flags revised: 1." -- aggregate counts without per-check naming, making check-structure invisible in output; naming it forces a format that separately enumerates each check's result | Very strong -- Pattern-Matcher Auditor competitor: uses C-22-compliant PROHIBITED DIRECTION with 5 variants and closure declaration, but Check 1 asks "does this match any of the six prohibited forms, including semantic equivalents?" -- list membership plus semantic extension; naming it forces the function to be stated as the causal-structure rule, not the extended list | Combined; two-competitor architecture, each scoped to its target phase |

---

## V-01 — Output Format (Mandatory Audit Report Template)

**Axis:** Output format
**Hypothesis:** R14 V-04's Auditor ends with "output complete revised rubric with revision log" -- the log's format is unspecified. An Auditor can satisfy this by writing a narrative log or an aggregate count, neither of which makes structural symmetry independently verifiable. C-23 requires the audit procedure to specify an output FORMAT whose structure makes symmetry independently falsifiable. V-01 closes this by adding a REQUIRED AUDIT REPORT FORMAT template as the mandatory output of the Auditor role. The template has two mandatory sections -- "Text-field flags:" (one line per Text check) and "Pass-field flags:" (one line per Pass check) -- per criterion. The structure of the template makes asymmetry detectable: if a three-Text-three-Pass protocol runs but the report shows two Pass-flag lines and four Text-flag lines, the format itself surfaces the discrepancy. Filling the template is not optional -- it IS the Auditor role's output. C-24 is intentionally untouched: Check 1 tests against the enumerated form-class. Prediction: C-23 very strong; C-24 fail.

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
(fill [X] and [failure] with your skill-specific values):

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [derive one additional skill-specific variant -- a phrasing a Builder
               of this rubric type would naturally write encoding the same wrong
               causal direction]

The form-class is closed. Any semantically equivalent construction is equally
prohibited. Naming a new synonym does not escape.

Escape: identify Y (the required property) and write:
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
a prohibited qualitative form is not a Pass condition -- return to this template.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (TEXT FILL-IN TEMPLATE, PROHIBITED DIRECTION with canonical + >= 4 enumerated variants + closure statement + skill-specific Variant 5, PASS FILL-IN TEMPLATE). Do not proceed to the Builder until both templates and the PROHIBITED DIRECTION section are complete.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer. Build the rubric by filling the template brackets -- not by interpreting them.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y], [Z], [X] with the specific values for this criterion's failure mode. The Text field IS the filled sentence. If you find yourself writing any form in the PROHIBITED DIRECTION -- canonical, enumerated variant, or semantically equivalent construction -- stop. Identify Y and rewrite.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION, OBSERVABLE, STANDARD from the template options. If you write a prohibited qualitative form -- stop. Return to the template.

**Essential criteria (3-5).** From broken failure modes. Five fields:

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

**BUILDER GATE:** Complete rubric draft. No Text field contains any form in the PROHIBITED DIRECTION. All Pass fields are three-line filled blocks.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR from the Dual Definer and the rubric draft from the Builder. Apply seven checks per criterion in isolation. Revise in-place where any check fails.

**Check 1 -- Direction and form-class (Text, isolated).** Read the Text field alone, with the TEXT FILL-IN TEMPLATE and PROHIBITED DIRECTION section visible. Does it follow "Without [Y], ... [Z]. Not [X], but [Y]."? Or does it contain any phrasing from the PROHIBITED DIRECTION form-class -- canonical form, any enumerated variant, or any semantically equivalent construction? If prohibited: identify Y, fill the TEXT FILL-IN TEMPLATE, rewrite.

**Check 2 -- Contrast clause (Text).** "not [X], but [Y]" present in Text? If absent: add using TEXT FILL-IN TEMPLATE's X and Y for this criterion.

**Check 3 -- Text isolation.** Text passes Check 1 with only the bare TEXT FILL-IN TEMPLATE visible (no bracket guidance, no preamble, no other criteria)? If not: rewrite until self-contained.

**Check 4 -- Pass location (Pass, isolated).** Read the Pass field's LOCATION line alone. Names a specific artifact section or field from the LOCATION options? General descriptions and absent LOCATION lines fail. If insufficient: select from LOCATION options.

**Check 5 -- Pass observable and standard (Pass, isolated).** Read the OBSERVABLE and STANDARD lines alone. OBSERVABLE names a specific confirmable fact from the OBSERVABLE options (token, count, keyword, pattern verifiable without judgment)? STANDARD states a verifiable condition? If either is absent or vague: fill from OBSERVABLE options and state STANDARD explicitly.

**Check 6 -- Pass prohibited-form (Pass, isolated).** Read every line of the Pass field independently of Checks 4 and 5. Does any line contain a prohibited qualitative-only form from the PASS FILL-IN TEMPLATE's prohibited list? Fails independently of Checks 4 and 5 -- a prohibited form in a modifier or sub-clause fails even if LOCATION and OBSERVABLE are correct. If present: remove and restate using the template.

**Check 7 -- Pass-Text coherence.** Is the OBSERVABLE in Pass the logical conclusion of the Text argument? No ungrounded observables? Fix if needed.

After all seven checks are complete for all criteria, output the complete revised rubric followed by the AUDIT REPORT. The AUDIT REPORT IS NOT OPTIONAL. It is the required output of this role and must be in the following format exactly:

```
AUDIT REPORT

Per-criterion results:

| Criterion | Check 1 direction | Check 2 contrast | Check 3 isolation | Check 4 location | Check 5 observable | Check 6 prohibited-form | Check 7 coherence |
|-----------|------------------|-----------------|------------------|-----------------|-------------------|------------------------|------------------|
| C-NN      | pass / fail       | pass / fail      | pass / fail       | pass / fail      | pass / fail        | pass / fail             | pass / fail       |
[one row per criterion]

Summary:
Text flags: [direction N, contrast N, isolation N]
Pass flags: [location N, observable N, prohibited-form N]
Coherence flags: [N]
Total revisions: N
```

The per-criterion table is the enforcement structure. Symmetry between Text-field columns (3) and Pass-field columns (3) is verifiable from this table alone, without reading the check procedure. An evaluator examining only the AUDIT REPORT can confirm that three Text checks and three Pass checks were applied independently to every criterion. Do not substitute a narrative log for this table.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the audit report format principle: the Dual Auditor produces a REQUIRED AUDIT REPORT with a per-criterion table showing three named Text-field check results and three named Pass-field check results per row; the table structure makes structural symmetry independently verifiable from the report output -- an evaluator reading only the table can confirm that Text and Pass audits were applied with equal granularity; the format is the enforcement mechanism, not a documentation artifact alongside the check procedure), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational (reference anchors retained), then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 — Phrasing Register (Check Function Constitutive Redefinition)

**Axis:** Phrasing register
**Hypothesis:** R14 V-04's Auditor Check 1 tests: "Or does it contain any phrasing from the PROHIBITED DIRECTION form-class -- the canonical form, any enumerated variant, or any semantically equivalent construction?" The check function is implicit list membership extended to semantic equivalents. Even with the form-class declared closed (C-22), the Auditor's operative act remains: compare this Text against the class. C-24 requires the check function to be REDEFINED -- stated as the generative rule the enumeration instantiates. V-02 applies the constitutive definition move to the check function: a direction check IS a causal-structure membership test, not a pattern-match or semantic-equivalence comparison. The redefinition is constitutive: "the question is not whether this sentence matches a prohibited form; the question is whether this sentence locates causality in the wrong form's consequence." This test can classify any novel phrasing -- including phrasings not in the list and not semantically equivalent to any listed form on the surface -- by examining the argument's causal structure. Audit report format is not changed from R14 V-04's instruction ("revision log"). Prediction: C-24 very strong; C-23 fail.

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
(fill [X] and [failure] with your skill-specific values):

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [derive one additional skill-specific variant encoding the same wrong
               causal direction in natural language for this rubric domain]

The form-class is closed. Any semantically equivalent construction is equally
prohibited.

Escape: identify Y (the required property) and write:
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

A criterion Pass IS these three lines with the brackets filled.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR with PROHIBITED DIRECTION section fully enumerated. Do not proceed to the Builder until complete.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR from the Dual Definer. Build the rubric by filling the template brackets.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y], [Z], [X] from this criterion's failure mode. If you write any form in the PROHIBITED DIRECTION -- stop. Identify Y and rewrite using the template.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION, OBSERVABLE, STANDARD from options. If you write a prohibited qualitative form -- stop and return to the template.

**Essential criteria (3-5).** Five fields: ID (C-NN), Text (filled TEXT template), Weight (essential), Category, Pass (filled PASS template, all three lines).

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

**BUILDER GATE:** Complete rubric draft. No Text field contains any form in the PROHIBITED DIRECTION.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR from the Dual Definer and the rubric draft from the Builder. Apply seven checks per criterion in isolation.

**CHECK FUNCTION DEFINITION FOR CHECK 1.** Before applying any checks, read this definition. It governs Check 1 exclusively.

```
CHECK 1 OPERATIVE FUNCTION:

The operative function for the direction check is NOT:
  "does this sentence match any of the prohibited phrasings?"
  "does this sentence semantically resemble any prohibited form?"

The operative function IS:
  "does this Text locate causality in the wrong form's consequence?"

A Text locates causality in the wrong form's consequence if the causal argument's
subject is [X] (the rejected form) and its predicate is the failure. Regardless
of surface phrasing, any Text whose argument structure is "[X] -> [failure]" is
in the prohibited direction.

A Text does NOT locate causality in the wrong form's consequence if its causal
argument runs from the required property's absence to the failure: "without [Y],
[failure] occurs because [Z]." The subject of the causal argument is the absence
of the required property, not the presence of the wrong form.

Application: when checking a criterion's Text, ask one question:
  "Is the causal argument's subject [X] (the wrong form), or is it the absence of
  [Y] (the required property)?"
If [X] is the subject: prohibited direction. Rewrite.
If absence of [Y] is the subject: permitted direction. Proceed.

Do NOT test by matching against the canonical form or listed variants. Those are
instances. The function above is the rule those instances instantiate.
```

Apply this check function to every criterion's Text field before applying any other check.

**Check 1 -- Direction (Text, isolated).** Apply the CHECK 1 OPERATIVE FUNCTION above. Is the causal argument's subject [X] (wrong form) or the absence of [Y] (required property)? If [X] is subject: identify Y for this criterion, fill the TEXT FILL-IN TEMPLATE, rewrite.

**Check 2 -- Contrast clause (Text).** "not [X], but [Y]" present? If absent: add.

**Check 3 -- Text isolation.** Text passes Check 1 with only the bare TEXT FILL-IN TEMPLATE visible? If not: rewrite until self-contained.

**Check 4 -- Pass location (Pass, isolated).** LOCATION line names a specific artifact section from LOCATION options? If not: fill.

**Check 5 -- Pass observable and standard (Pass, isolated).** OBSERVABLE names a specific confirmable fact from OBSERVABLE options? STANDARD states a verifiable condition? If either absent or vague: fill from options.

**Check 6 -- Pass prohibited-form (Pass, isolated).** Any line contains a prohibited qualitative-only form from the PASS FILL-IN TEMPLATE's list? If yes: remove and restate.

**Check 7 -- Pass-Text coherence.** OBSERVABLE is logical conclusion of Text argument? No ungrounded observables? Fix if needed.

After all checks pass, output the complete revised rubric with revision log. The revision log format: "Revision log: C-NN Check N [Text/Pass] -- [what was revised]." One line per revision. Separate Text revisions and Pass revisions by check number.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the check function redefinition principle: the Dual Auditor's Check 1 operative function is "does this Text locate causality in the wrong form's consequence?" -- not "does this match any prohibited phrasing?"; this is a causal-structure membership test applied before consulting the enumeration; a Text that avoids all listed forms but argues "[X] -> [failure]" fails Check 1; a Text resembling a listed form but arguing "without [Y], [failure] occurs because [Z]" passes), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational, then scoring section.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 — Role Sequence (Report Format Specifier After Auditor Checks)

**Axis:** Role sequence
**Hypothesis:** C-23 requires the audit procedure to specify a report format that makes symmetry independently verifiable. Two implementation options exist: (1) embed the format specification in the Auditor check procedure (as V-01 does), or (2) introduce a named Report Format Specifier role that runs after all checks complete and converts the Auditor's findings into the required structured report. V-03 tests option 2. The Report Format Specifier receives the Auditor's per-criterion findings as input and produces the STRUCTURED AUDIT REPORT as its sole output. The format is defined by the Specifier's role instruction, not by the Auditor check procedure. The hypothesis is that role isolation produces a weaker mechanism than embedding -- because the Auditor's check procedure does not generate the required format, and an implementation that omits the Specifier step (or abbreviates it) produces a format-free revision log while still satisfying the check instructions' letter. C-21 is satisfied (symmetric 3+3 checks carried from R14 V-04). C-24 is not targeted. Prediction: C-23 moderate-strong; C-24 fail.

---

You are a four-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor -> Report Format Specifier. **Do not begin a role until the previous role's output is written.**

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
  [Y] = [the specific required-property type -- derive from skill spec and failure log]
  [Z] = [the specific failure-consequence type when Y is absent -- name the damage]
  [X] = [the specific rejected-form type -- the wrong-direction argument for this domain]

The sentence above IS the template.

PROHIBITED DIRECTION -- form-class exhaustive:

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [skill-specific variant]

Form-class is closed. Escape: "Without [Y], the artifact [fails] because [Z]."

PASS FILL-IN TEMPLATE:
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name]:
  LOCATION options: [2-3 specific sections]
  OBSERVABLE options: [2-3 specific confirmable facts]
  Prohibited qualitative-only forms: [1-2 tempting forms]
```

**DUAL DEFINER GATE:** Failure log >= 5 entries. TEMPLATE PAIR complete with PROHIBITED DIRECTION. Do not proceed.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR. Build the rubric by filling template brackets.

Essential (3-5), Recommended (2-3), Aspirational (1-2). All Text fields: filled TEXT FILL-IN TEMPLATE. All Pass fields: filled PASS FILL-IN TEMPLATE. No prohibited direction forms in any Text field. Scoring formula and golden threshold included.

**BUILDER GATE:** Complete rubric. All fields present. No prohibited direction forms.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft. Apply seven checks per criterion in isolation. Record findings per criterion -- do not yet write the output file.

**Check 1 -- Direction and form-class (Text).** Does it follow "Without [Y], ... [Z]. Not [X], but [Y]."? Or does it contain any phrasing from the PROHIBITED DIRECTION form-class? If prohibited: rewrite. Record: "C-NN Check 1 [pass / fail -- revised]."

**Check 2 -- Contrast clause (Text).** "not [X], but [Y]" present? If absent: add. Record: "C-NN Check 2 [pass / fail -- revised]."

**Check 3 -- Text isolation (Text).** Passes Check 1 with only bare TEXT FILL-IN TEMPLATE visible? If not: rewrite. Record: "C-NN Check 3 [pass / fail -- revised]."

**Check 4 -- Pass location (Pass).** LOCATION names a specific section from LOCATION options? If not: fill. Record: "C-NN Check 4 [pass / fail -- revised]."

**Check 5 -- Pass observable and standard (Pass).** OBSERVABLE names a specific confirmable fact? STANDARD states a verifiable condition? If absent or vague: fill. Record: "C-NN Check 5 [pass / fail -- revised]."

**Check 6 -- Pass prohibited-form (Pass).** Any prohibited qualitative-only form present? If yes: replace. Record: "C-NN Check 6 [pass / fail -- revised]."

**Check 7 -- Pass-Text coherence.** OBSERVABLE is conclusion of Text argument? Fix if needed. Record: "C-NN Check 7 [pass / fail -- revised]."

After all checks complete for all criteria, output the revised rubric. Then pass all findings to the Report Format Specifier.

**DUAL AUDITOR GATE:** Per-criterion findings for all seven checks for all criteria. Complete revised rubric. Pass to Report Format Specifier.

---

### REPORT FORMAT SPECIFIER ROLE

Read the Dual Auditor's per-criterion findings. Your sole output is the STRUCTURED AUDIT REPORT. Do not modify criteria. Do not add narrative commentary.

Produce the STRUCTURED AUDIT REPORT in the following required format:

```
STRUCTURED AUDIT REPORT

Per-criterion check results:

Criterion C-NN:
  Text-field checks:
    Check 1 (direction):  [pass / fail-revised]
    Check 2 (contrast):   [pass / fail-revised]
    Check 3 (isolation):  [pass / fail-revised]
  Pass-field checks:
    Check 4 (location):        [pass / fail-revised]
    Check 5 (observable+std):  [pass / fail-revised]
    Check 6 (prohibited-form): [pass / fail-revised]
  Coherence:
    Check 7:  [pass / fail-revised]

[repeat for each criterion]

Totals:
  Text flags revised: [N]   (Check 1: N, Check 2: N, Check 3: N)
  Pass flags revised: [N]   (Check 4: N, Check 5: N, Check 6: N)
  Coherence flags revised: [N]
```

The per-criterion structure is the enforcement mechanism. Each criterion's Text-field checks (3) and Pass-field checks (3) are listed as separate named sections with equal numbers of entries. An evaluator reading only this report can verify structural symmetry without consulting the check procedure.

**REPORT FORMAT SPECIFIER GATE:** STRUCTURED AUDIT REPORT complete. One entry per criterion. All seven checks listed. Text-field section and Pass-field section each contain exactly 3 named entries.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the report-generation role principle: after all per-criterion checks complete, a dedicated Report Format Specifier role converts the Auditor's findings into a STRUCTURED AUDIT REPORT; the report's per-criterion structure lists Text-field checks and Pass-field checks as separate named sections with equal entries, making structural symmetry verifiable from the report output alone; the Report Format Specifier is the enforcement mechanism -- the Auditor produces findings, the Specifier produces the format), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational, then scoring section, then STRUCTURED AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 — Output Format + Phrasing Register (Mandatory Report Template + Check Function Redefinition)

**Axes:** Output format (mandatory AUDIT REPORT FORMAT template) + phrasing register (Check 1 function constitutive redefinition)
**Hypothesis:** V-01 closes C-23: the AUDIT REPORT FORMAT template is a required Auditor output with per-criterion rows and separate named Text and Pass flag columns, making structural symmetry independently verifiable. V-02 closes C-24: Check 1's operative function is constitutively redefined from pattern-matching to causal-structure membership testing -- "does this Text locate causality in the wrong form's consequence?" V-04 combines both. The two mechanisms are architecturally parallel: V-01 specifies the format of what the Auditor produces; V-02 specifies the function by which the Auditor checks direction. Neither mechanism depends on the other, but together they close both C-23 and C-24 simultaneously. The combined variation is structurally analogous to R14 V-04 (symmetric 3+3 checks + form-class prohibition) -- two independently operative closing mechanisms applied in the same variation. Prediction: C-23 very strong; C-24 very strong.

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
(fill [X] and [failure] with your skill-specific values):

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [derive one additional skill-specific variant -- a phrasing natural to
               this rubric domain encoding the same wrong causal direction]

The form-class is closed. Any semantically equivalent construction is equally
prohibited.

Escape: identify Y (the required property) and write:
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

A criterion Pass IS these three lines with the brackets filled.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (both templates in bare fill-in form; PROHIBITED DIRECTION section with canonical + >= 4 enumerated variants + Variant 5 + closure statement). Do not proceed to the Builder until complete.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR. Build the rubric by filling template brackets -- not by interpreting them.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y], [Z], [X] from this criterion's failure mode. If you write any form in the PROHIBITED DIRECTION -- stop. Identify Y, fill the template, rewrite.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION, OBSERVABLE, STANDARD. If you write a prohibited qualitative form -- stop and return to the template.

**Essential criteria (3-5).** ID, Text (filled), Weight: essential, Category, Pass (filled, all three lines).

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

**BUILDER GATE:** Complete rubric. No Text field contains any form in the PROHIBITED DIRECTION. All Pass fields are three-line filled blocks.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft. Apply seven checks per criterion in isolation.

**CHECK 1 OPERATIVE FUNCTION -- read before applying any checks:**

```
The operative check function for direction is NOT:
  "does this sentence match any phrasing in the PROHIBITED DIRECTION list?"
  "does this sentence semantically resemble any enumerated variant?"

The operative check function IS:
  "does this Text locate causality in the wrong form's consequence?"

A Text locates causality in the wrong form's consequence when its causal argument's
subject is [X] (the rejected form) and its predicate is the failure -- regardless
of surface phrasing, sentence structure, or whether the phrasing appears in the
PROHIBITED DIRECTION list.

A Text does NOT locate causality in the wrong form's consequence when its causal
argument runs from the required property's absence to the failure: "without [Y],
[failure] occurs because [Z]."

Apply the function: "Is the causal argument's subject [X] or the absence of [Y]?"
  [X] is subject -> prohibited. Rewrite.
  Absence of [Y] is subject -> permitted. Proceed.

This function is prior to and independent of the enumeration. Consult the
PROHIBITED DIRECTION list for examples, not for the test. The test is the function
above.
```

**Check 1 -- Direction (Text, isolated).** Apply the CHECK 1 OPERATIVE FUNCTION. Is the causal argument's subject [X] or the absence of [Y]? If [X]: fill the TEXT FILL-IN TEMPLATE with Y, Z for this criterion. Rewrite.

**Check 2 -- Contrast clause (Text).** "not [X], but [Y]" present? If absent: add using TEXT FILL-IN TEMPLATE's X and Y for this criterion.

**Check 3 -- Text isolation.** Text passes Check 1 with only the bare TEXT FILL-IN TEMPLATE visible? If not: rewrite until self-contained.

**Check 4 -- Pass location (Pass, isolated).** LOCATION names a specific artifact section from LOCATION options? If not: fill.

**Check 5 -- Pass observable and standard (Pass, isolated).** OBSERVABLE names a specific confirmable fact from OBSERVABLE options? STANDARD states a verifiable condition? If absent or vague: fill from options.

**Check 6 -- Pass prohibited-form (Pass, isolated).** Any prohibited qualitative-only form present? If yes: replace.

**Check 7 -- Pass-Text coherence.** OBSERVABLE is conclusion of Text argument? No ungrounded observables? Fix if needed.

After all checks are complete for all criteria, output the revised rubric followed by the AUDIT REPORT. The AUDIT REPORT IS the required output of this role. It must be in the following format exactly:

```
AUDIT REPORT

Per-criterion results:

| Criterion | Check 1 direction | Check 2 contrast | Check 3 isolation | Check 4 location | Check 5 observable | Check 6 prohibited-form | Check 7 coherence |
|-----------|------------------|-----------------|------------------|-----------------|-------------------|------------------------|------------------|
| C-NN      | pass / fail       | pass / fail      | pass / fail       | pass / fail      | pass / fail        | pass / fail             | pass / fail       |

Text flags: [direction N, contrast N, isolation N]
Pass flags: [location N, observable N, prohibited-form N]
Coherence flags: [coherence N]
Total revisions: N
```

The per-criterion table is the enforcement mechanism for audit symmetry. Three Text-field columns (direction, contrast, isolation) and three Pass-field columns (location, observable, prohibited-form) appear in every row. An evaluator reading only this table can verify that Text and Pass fields were audited with equal granularity. Do not substitute a narrative log for this table. The summary flag counts are independently verifiable from the per-criterion table above them.

The CHECK 1 OPERATIVE FUNCTION is the enforcement mechanism for causal-direction testing. It is stated before any check is applied, and it governs Check 1 exclusively. Consulting the PROHIBITED DIRECTION enumeration is permitted for examples only -- the test function is causal-structure membership, not list membership.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the two closing mechanisms: the AUDIT REPORT FORMAT template enforces structural symmetry by requiring per-criterion rows with three named Text-field columns and three named Pass-field columns -- making symmetry independently verifiable from the table alone; the CHECK 1 OPERATIVE FUNCTION redefines direction checking from "does this match any prohibited phrasing?" to "does this Text locate causality in the wrong form's consequence?" -- a causal-structure test prior to and independent of the enumeration; both mechanisms are specified before their respective operations, not asserted afterward), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational, then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 — Inertia Framing (Report-Opaque Competitor + Pattern-Matcher Competitor)

**Axes:** Inertia framing (two competitors, each named before the phase where their gap is relevant)
**Hypothesis:** Prior rounds established that naming a near-excellent competitor concretizes the gap and creates structural pressure toward the property the competitor lacks. V-05 extends the two-competitor architecture from R14 V-05 (Asymmetric-Audit + Example-Bounded, targeting C-21 and C-22) to C-23 and C-24. Each competitor passes all prior criteria and fails exactly one new criterion. **Competitor 1: the Report-Opaque Protocol** -- passes C-21 (symmetric 3+3 checks) but produces an aggregate narrative revision log that obscures which checks found issues: "Audit complete: 3 Text flags, 1 Pass flag." An evaluator reading this log knows flags occurred but cannot verify from the report alone whether the procedure was symmetric. Naming this competitor before the Auditor's output instruction forces the design to specify a format in which symmetry is not obscured. **Competitor 2: the Pattern-Matcher Auditor** -- passes C-22 (form-class closed, 5 variants enumerated) but Check 1 function asks "does this match any of the 5 prohibited variants or a semantic equivalent?" The check function remains list membership (extended to semantic equivalence). Naming this competitor before Check 1's definition forces the function to be stated as the causal-structure rule. Each competitor description is paired with the constitutive definition it lacks. Prediction: C-23 very strong; C-24 very strong.

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.** Your protocol has two competitors. Each passes C-01 through C-22. Each fails exactly one of the two new target criteria.

---

**Competitor 1: The Report-Opaque Protocol**

Symmetric 3+3 Auditor checks: Check 1 direction (Text), Check 2 contrast (Text), Check 3 isolation (Text), Check 4 location (Pass), Check 5 observable+standard (Pass), Check 6 prohibited-form (Pass). C-21 satisfied. But the Auditor's output instruction reads: "Output the revised rubric and a revision log summarizing what was changed." The log format is unspecified. An Auditor following this instruction produces: "Audit complete: 2 criteria revised for Text direction, 1 criterion revised for Pass observable." This log tells an evaluator that revisions occurred -- it does not tell them whether Check 4 and Check 5 were applied with the same granularity as Check 1 and Check 2. A log saying "2 Text flags, 1 Pass flag" could reflect a protocol with 2 Text checks and 1 Pass check (asymmetric) or a protocol with 3+3 checks (symmetric). The report does not expose which structure produced it.

**The audit report format IS the enforcement mechanism.** A format that requires separate named entries for each check makes symmetry independently verifiable: "Text flags: [direction N, contrast N, isolation N]. Pass flags: [location N, observable N, prohibited-form N]." -- three entries per field, named by check. An evaluator reading only this line can verify three Text checks and three Pass checks without consulting the procedure. A format that aggregates or narrates makes the same verification impossible. The Report-Opaque Protocol has the right structure but the wrong output format. Your protocol must specify the format, not just the structure.

---

**Competitor 2: The Pattern-Matcher Auditor**

Form-class exhaustive PROHIBITED DIRECTION: canonical form + 5 variants + "form-class closed" declaration + "any semantically equivalent construction is equally prohibited." C-22 satisfied. But Auditor Check 1 function reads: "Does this Text contain any phrasing from the PROHIBITED DIRECTION form-class, including semantic equivalents?" The check function is: consult the form-class list and test for membership, extending to semantic equivalence when surface patterns differ. This function correctly identifies all enumerated forms and their semantic equivalents -- but it is still a list-membership test. A novel phrasing that the Auditor has not seen and that does not trigger "semantic equivalent" recognition could pass Check 1 while encoding the prohibited causal direction.

**The check function IS the operative rule.** "Does this match the list (plus semantic equivalents)?" is a pattern-recognition function. "Does this Text locate causality in the wrong form's consequence?" is a causal-structure function. The causal-structure function is the rule that the enumeration instantiates. Applying the causal-structure function requires the Auditor to ask: "What is the subject of this Text's causal argument? Is it the wrong form [X], or the absence of the required property [Y]?" This question has a structural answer independent of surface phrasing. It cannot be answered by consulting the list -- it requires reading the argument's structure. The Pattern-Matcher Auditor's check function is the list-membership version. Your protocol must state the causal-structure version, explicitly, before Check 1 is applied.

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. The TEMPLATE PAIR contains two fill-in templates in the exact phrasing register of the final criterion fields, plus a PROHIBITED DIRECTION section that closes the wrong-direction form-class. Do not draft criteria.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

**TEMPLATE PAIR.** Write both templates as bare fill-in forms.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE:
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name]:
  [Y] = [specific required property -- from skill spec and failure log]
  [Z] = [specific failure consequence when Y is absent]
  [X] = [specific rejected form type -- wrong-direction argument for this domain]

PROHIBITED DIRECTION -- form-class exhaustive:

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [skill-specific variant -- natural phrasing for this domain encoding
               the same wrong causal direction]

Form-class is closed. Escape: "Without [Y], the artifact [fails] because [Z]."

PASS FILL-IN TEMPLATE:
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name]:
  LOCATION options: [2-3 specific sections]
  OBSERVABLE options: [2-3 specific confirmable facts]
  Prohibited qualitative-only forms: [1-2 tempting forms]
```

**DUAL DEFINER GATE:** Failure log >= 5 entries. TEMPLATE PAIR complete with PROHIBITED DIRECTION. Do not proceed to Builder.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR. Build the rubric by filling template brackets.

For every Text field: fill TEXT FILL-IN TEMPLATE. No prohibited direction forms.
For every Pass field: fill PASS FILL-IN TEMPLATE. No prohibited qualitative forms.

Essential (3-5), Recommended (2-3, Property tested annotated), Aspirational (1-2, Reference anchor included). Scoring formula. Tier targets. At least 3 distinct categories.

**BUILDER GATE:** Complete rubric. No prohibited forms anywhere. All fields present.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft. Your two operating principles are stated before any check is applied.

**OPERATING PRINCIPLE 1 -- Check 1 function (read before applying Check 1):**

```
The operative check function for direction is NOT:
  "does this sentence match any phrasing in the PROHIBITED DIRECTION list?"

The operative check function IS:
  "does this Text locate causality in the wrong form's consequence?"

Apply by asking: "Is the causal argument's subject [X] (the wrong form) or the
absence of [Y] (the required property)?"
  [X] is subject -> prohibited direction. Rewrite.
  Absence of [Y] is subject -> permitted direction. Proceed.

The PROHIBITED DIRECTION list provides instances. This function is the rule.
```

**OPERATING PRINCIPLE 2 -- Audit report format (read before producing any output):**

```
Your output must include an AUDIT REPORT in the following format exactly.
This format is not optional. A narrative log does not satisfy it.

AUDIT REPORT

| Criterion | Check 1 direction | Check 2 contrast | Check 3 isolation | Check 4 location | Check 5 observable | Check 6 prohibited-form | Check 7 coherence |
|-----------|------------------|-----------------|------------------|-----------------|-------------------|------------------------|------------------|
| C-NN      | pass / fail       | pass / fail      | pass / fail       | pass / fail      | pass / fail        | pass / fail             | pass / fail       |

Text flags:      [direction N, contrast N, isolation N]
Pass flags:      [location N, observable N, prohibited-form N]
Coherence flags: [coherence N]

The three Text-field columns and three Pass-field columns are symmetric by construction.
An evaluator reading only this table can verify structural symmetry without consulting
this procedure. This is what the Report-Opaque Protocol does not produce.
```

Apply seven checks per criterion in isolation:

**Check 1 -- Direction (Text).** Apply OPERATING PRINCIPLE 1 function: is [X] the causal subject? If yes: rewrite.

**Check 2 -- Contrast (Text).** "not [X], but [Y]" in Text? If absent: add.

**Check 3 -- Isolation (Text).** Text passes Check 1 with only bare TEXT FILL-IN TEMPLATE visible? If not: rewrite.

**Check 4 -- Location (Pass, isolated).** LOCATION from LOCATION options? If not: fill.

**Check 5 -- Observable and standard (Pass, isolated).** OBSERVABLE specific and confirmable? STANDARD verifiable? If not: fill.

**Check 6 -- Prohibited-form (Pass, isolated).** Prohibited qualitative form present? If yes: replace.

**Check 7 -- Coherence.** OBSERVABLE is conclusion of Text argument? Fix if not.

After all checks complete, output the revised rubric followed by the AUDIT REPORT in the format specified in OPERATING PRINCIPLE 2. The AUDIT REPORT uses the per-criterion table format -- not a narrative log. This is the property the Report-Opaque Protocol lacks: the format whose structure makes symmetry independently verifiable.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- name the two competitors and state what each operating principle adds: where the Report-Opaque Protocol specifies symmetric checks but not the format that makes symmetry verifiable, the AUDIT REPORT FORMAT produces a per-criterion table with three named Text-field columns and three named Pass-field columns; where the Pattern-Matcher Auditor tests list membership extended to semantic equivalents, the CHECK 1 OPERATIVE FUNCTION tests causal-structure membership -- "is [X] the causal subject?" -- independent of surface phrasing; both operating principles are stated before their respective operations), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational, then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
