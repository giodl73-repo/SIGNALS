# quest-rubric Variate — Round 9 against rubric v9 (C-25, C-26, C-27)

**Date:** 2026-03-15
**Rubric:** v9 (C-01--C-27; adds C-25: independent-mechanism pairing; C-26: constraint-as-output-requirement; C-27: competitor-as-gap-specification)
**Target criteria:** C-25, C-26, C-27

**Round 9 design note:** Round 15 (against rubric v24/v8) produced R15 V-04 — the current highest-scoring variation, combining the mandatory AUDIT REPORT FORMAT table (C-23) with the CHECK 1 OPERATIVE FUNCTION redefinition (C-24). R15 V-05 additionally names the Pattern-Matcher Auditor competitor before the direction-check operating principle, approaching C-27. Three new aspirational criteria were added in rubric v9.

**C-25 gap in R15 V-04.** R15 V-04 introduces four mechanisms and closes four criteria (C-21: symmetric-checks, C-22: form-class-exhaustive, C-23: format-as-output, C-24: function-redefinition). The mechanisms are architecturally independent in practice, but the protocol never states the one-to-one assignment principle explicitly. A builder following R15 V-04 could introduce a unified enforcement step that attempts to close two criteria simultaneously with one structural move, satisfying neither cleanly because the mechanism cannot be isolated for independent evaluation. C-25 requires the protocol to assign one mechanism per criterion gap and verify each mechanism is independently removable before writing criteria.

**C-26 gap in R15 V-03.** R15 V-03 delegates report production to a separate Report Format Specifier role; the Auditor's own exit condition is satisfied before the format is produced. R15 V-04 already closes C-26 implicitly through "Do not substitute a narrative log for this table" in the Auditor's own output instruction. A dedicated V-03 variation strengthens this by defining output ownership constitutively — naming delegation as structural non-ownership — rather than merely demonstrating it through prohibition.

**C-27 gap in R15 V-04.** R15 V-04's OPERATING PRINCIPLE 1 correctly states the check function positively: "does this Text locate causality in the wrong form's consequence?" A reader learns the correct function from the positive definition. C-27 requires the competitor to precede the positive definition such that the gap is derivable from the competitor's failure mode alone, before the correct function is stated. R15 V-05 names the Pattern-Matcher Auditor alongside the definition — the competitor provides motivation but the gap specification still depends on the positive definition that follows. C-27 requires the competitor description to BE the gap specification, independently.

This round probes three single-axis variations and two combined variations.

---

## Round 9 Variation Map

| Variation | Axis | C-25 probe | C-26 probe | C-27 probe | Notes |
|-----------|------|-----------|-----------|-----------|-------|
| V-01 | Inertia framing (Pattern-Matcher Auditor as constitutive gap specification) | Weak — no Mechanism Map; one-to-one assignment not stated | Carry-forward — table embedded in Auditor instruction per R15 V-04 | Very strong — competitor block precedes OPERATING PRINCIPLE 1; competitor's failure mode IS the gap specification; correct function derivable from foil alone before positive definition is read | Single-axis; extends R15 V-05 by restructuring competitor block so the failure mode is the constitutive specification, not motivation accompanying the definition |
| V-02 | Output format (Mechanism Map before aspirational tier) | Very strong — MECHANISM MAP table required before aspirational criteria; one row per gap; independent-removal column; multi-assignment is a format error | Carry-forward — table embedded in Auditor instruction per R15 V-04 | Weak — no competitor precedes positive definition; function redefinition carried forward from R15 V-04 | Single-axis; Mechanism Map makes one-to-one gap-mechanism assignment a format requirement rather than a design assertion |
| V-03 | Phrasing register (Output Ownership constitutive definition) | Moderate — ownership principle mentions that coupling defeats independent evaluation, but no Mechanism Map | Very strong — OUTPUT OWNERSHIP defined constitutively with three numbered conditions; delegation named as structural non-ownership; Format-Delegating Protocol named as foil | Weak — function redefinition carried forward; no competitor precedes it | Single-axis; strengthens C-26 by making delegation structurally visible as non-ownership via constitutive definition rather than implicit demonstration |
| V-04 | Role sequence + inertia framing (Mechanism Definer + Pattern-Matcher competitor) | Very strong — dedicated MECHANISM DEFINER role precedes aspirational criteria; produces MECHANISM MAP as exit condition; Builder cites map row per criterion | Carry-forward — table embedded in Auditor instruction per R15 V-04 | Very strong — Pattern-Matcher block IS the constitutive gap specification; OPERATING PRINCIPLE 1 follows; correct function derivable from foil alone | Combined; two independent mechanisms, one per target criterion; V-04 demonstrates C-25 by its own design — removing Mechanism Definer fails C-25 only; removing Pattern-Matcher fails C-27 only |
| V-05 | Role sequence + phrasing register + inertia framing (Mechanism Map + Output Ownership + Pattern-Matcher) | Very strong | Very strong | Very strong | Combined; three independent mechanisms, one per criterion; demonstrates C-25 by construction — each mechanism removable without affecting the other two |

---

## V-01 -- Inertia Framing (Pattern-Matcher Auditor as Constitutive Gap Specification)

**Axis:** Inertia framing
**Hypothesis:** R15 V-05 named the Pattern-Matcher Auditor as motivation — the competitor is described and then the positive definition follows as the answer. The competitor supports the definition; it does not constitute it. C-27 requires the competitor's failure mode to be the constitutive gap specification: reading the competitor alone, before the positive definition, a reader must be able to derive what the correct implementation must not do. V-01 restructures the competitor block: the competitor comes first; the block ends with an explicit statement that the competitor IS the gap specification; the positive definition (OPERATING PRINCIPLE 1) follows and confirms the gap rather than creating it. The test: cover OPERATING PRINCIPLE 1 and ask whether the gap is still visible from the competitor block alone. If yes: C-27 satisfied. C-25 and C-26 carry forward from R15 V-04.

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. Do not draft criteria.

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
  [Z] = [the specific failure-consequence type when Y is absent -- name the damage]
  [X] = [the specific rejected-form type -- the wrong-direction argument a Builder is
         tempted to write for this skill's domain]

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

A criterion Pass IS these three lines with the brackets filled.
```

**DUAL DEFINER GATE:** Output is the failure log (>= 5 entries) and the TEMPLATE PAIR (both templates in bare fill-in form; PROHIBITED DIRECTION section with canonical + >= 4 enumerated variants + Variant 5 + closure statement). Do not proceed to Builder until complete.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR. Build the rubric by filling template brackets -- not by interpreting them.

**For every Text field:** copy the TEXT FILL-IN TEMPLATE. Replace [Y], [Z], [X] from this criterion's failure mode. If you write any form in the PROHIBITED DIRECTION -- stop. Identify Y, fill the template, rewrite.

**For every Pass field:** copy the PASS FILL-IN TEMPLATE. Fill LOCATION, OBSERVABLE, STANDARD from the LOCATION options and OBSERVABLE options. If you write a prohibited qualitative form -- stop and return to the template.

**Essential criteria (3-5):** ID (C-NN sequential), Text (filled), Weight: essential, Category (correctness | depth | format | coverage | behavior), Pass (filled, all three lines).

**Recommended criteria (2-3):** Pass tests degree, precision, or specificity -- not just whether a field exists. Annotate: **Property tested:** [degree | precision | specificity].

**Aspirational criteria (1-2):** State the aspirational reference anchor before each criterion: name a rubric that passes C-01--C-08, then name the exact dimension in which it falls short of the aspirational bar.

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories across the full rubric.

**BUILDER GATE:** Complete rubric. No Text field contains any form in the PROHIBITED DIRECTION. All Pass fields are three-line filled blocks.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft. Before applying any checks, read the following competitor block. The competitor block is the gap specification for OPERATING PRINCIPLE 1.

---

**COMPETITOR: The Pattern-Matcher Auditor**

The Pattern-Matcher Auditor satisfies C-01 through C-22. It holds the PROHIBITED DIRECTION form-class: canonical form, four enumerated variants, one skill-specific variant, closure declaration, "any semantically equivalent construction is equally prohibited." Check 1 reads: "Does this Text contain any phrasing from the PROHIBITED DIRECTION form-class, including semantic equivalents?"

The Pattern-Matcher Auditor's check function is: consult the form-class and test for membership, extending to semantic equivalents when surface patterns differ. It correctly identifies all six enumerated forms and their direct semantic equivalents. But its operative act at Check 1 is comparison against a list. A novel phrasing that the Auditor has not categorized -- "the presence of [X] is the source of [the rubric's failure]" -- may not trigger "semantic equivalent" recognition even though it locates causality in the wrong form's consequence. The Pattern-Matcher Auditor runs a test that is bounded by the list it holds and its ability to recognize equivalence.

**This competitor block IS the gap specification for Check 1.** From the description above -- before reading OPERATING PRINCIPLE 1 below -- derive: the correct check function must test something other than list membership and semantic equivalence. What must it test? Answer from the competitor's failure alone: it must test whether the causal argument's subject is the wrong form, regardless of whether that subject has been enumerated or categorized.

---

**OPERATING PRINCIPLE 1 -- Check 1 function (the gap the Pattern-Matcher Auditor fails to close):**

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

Apply the function: "Is the causal argument's subject [X] or the absence of [Y]?"
  [X] is subject -> prohibited. Rewrite using the TEXT FILL-IN TEMPLATE.
  Absence of [Y] is subject -> permitted. Proceed.

The PROHIBITED DIRECTION list provides instances of this function's application.
The function is prior to the list. Consult the list for examples; apply the function
for every Text, including phrasings not on the list.
```

**OPERATING PRINCIPLE 2 -- Audit report format:**

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
```

Apply seven checks per criterion in isolation:

**Check 1 -- Direction (Text, isolated).** Apply OPERATING PRINCIPLE 1. Is the causal argument's subject [X] or the absence of [Y]? If [X]: fill the TEXT FILL-IN TEMPLATE.

**Check 2 -- Contrast clause (Text).** "not [X], but [Y]" present? If absent: add.

**Check 3 -- Text isolation.** Text passes Check 1 with only the bare TEXT FILL-IN TEMPLATE visible? If not: rewrite until self-contained.

**Check 4 -- Pass location (Pass, isolated).** LOCATION names a specific artifact section from LOCATION options? If not: fill.

**Check 5 -- Pass observable and standard (Pass, isolated).** OBSERVABLE names a specific confirmable fact? STANDARD states a verifiable condition? If absent: fill.

**Check 6 -- Pass prohibited-form (Pass, isolated).** Any prohibited qualitative-only form present? If yes: replace.

**Check 7 -- Pass-Text coherence.** OBSERVABLE is the conclusion of the Text argument? Fix if not.

After all checks, output the revised rubric followed by the AUDIT REPORT in the format specified in OPERATING PRINCIPLE 2. **Do not substitute a narrative log for this table.** The table is this role's required output; its three Text-field columns and three Pass-field columns make structural symmetry independently verifiable from the table alone.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- name the Pattern-Matcher Auditor competitor and state what OPERATING PRINCIPLE 1 adds: where the competitor's check function asks "does this match the list or a semantic equivalent?", the operative function asks "is [X] the causal subject?" -- a structural test that requires no list and applies to novel phrasings; the competitor IS the gap specification because the required function is derivable from the competitor's failure mode alone, before the positive definition is read), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION section), then criteria ordered essential -> recommended -> aspirational, then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-02 -- Output Format (Mechanism Map Before Aspirational Tier)

**Axis:** Output format
**Hypothesis:** C-25 requires the protocol to assign one mechanism per criterion gap and verify independent removability. Prior rounds achieved independent mechanisms in practice -- R15 V-04's format-table and function-redefinition mechanisms are independently removable -- but never required the builder to produce an artifact demonstrating this. A builder who reads "introduce mechanisms for new criteria" and introduces a unified mechanism that addresses two gaps simultaneously satisfies the criteria letter while creating coupling invisible to an evaluator. V-02 introduces the MECHANISM MAP: before aspirational criteria are written, the Builder produces a table with one row per intended mechanism, one column asserting that removing this mechanism affects exactly one criterion. Multi-assignment -- one mechanism responsible for two gaps -- is a format error caught by the table's structure, not a judgment call. The Mechanism Map is the enforcement artifact: filling it correctly is equivalent to demonstrating one-to-one assignment. C-26 and C-27 are carried forward from R15 V-04 (audit table embedded in Auditor output instruction; function redefinition present but no competitor precedes it).

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. Do not draft criteria.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

**TEMPLATE PAIR.** Write both templates as bare fill-in forms, instantiated for this specific skill.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE:
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name]:
  [Y] = [specific required property from skill spec and failure log]
  [Z] = [specific failure consequence when Y is absent]
  [X] = [specific rejected form -- wrong-direction argument for this domain]

PROHIBITED DIRECTION -- form-class exhaustive:

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [skill-specific variant -- natural phrasing encoding the same wrong direction]

Form-class is closed. Any semantically equivalent construction is equally prohibited.
Escape: "Without [Y], the artifact [fails] because [Z]."

PASS FILL-IN TEMPLATE:
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name]:
  LOCATION options: [2-3 specific sections or fields]
  OBSERVABLE options: [2-3 specific confirmable facts]
  Prohibited qualitative-only forms: [1-2 tempting forms for this domain]
```

**DUAL DEFINER GATE:** Failure log >= 5 entries. TEMPLATE PAIR complete with PROHIBITED DIRECTION closure. Do not proceed to Builder.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR. Build the rubric by filling template brackets.

**For every Text field:** copy TEXT FILL-IN TEMPLATE. Fill [Y], [Z], [X]. Check for prohibited direction; rewrite if present.

**For every Pass field:** copy PASS FILL-IN TEMPLATE. Fill LOCATION, OBSERVABLE, STANDARD from options. No prohibited qualitative forms.

**Essential criteria (3-5):** C-NN, Text (filled), Weight: essential, Category, Pass (three-line block).

**Recommended criteria (2-3):** Pass tests degree, precision, or specificity. Annotate: **Property tested:** [degree | precision | specificity].

**Before writing aspirational criteria -- produce the MECHANISM MAP:**

For each new aspirational criterion you intend to add beyond the rubric's essential and recommended floor, assign exactly one mechanism. A mechanism is a structural element you introduce into the protocol that enforces the criterion's requirement. Produce the following table:

```
MECHANISM MAP

| New criterion gap | Mechanism name | What this mechanism enforces | Can removing this mechanism alone cause this criterion to fail, without affecting any other criterion? |
|---|---|---|---|
| [criterion C-NN: gap description] | [mechanism name] | [one sentence: what structural element this mechanism adds and what it prevents the builder from doing] | Yes -- removing [mechanism name] would affect [criterion C-NN] only. No other criterion depends on this mechanism. |
```

Rules for the MECHANISM MAP:
- One row per mechanism. One mechanism per criterion gap.
- If removing Mechanism A would cause both criterion C-NN and criterion C-MM to fail: A is coupling two gaps. Split into two independent mechanisms before writing criteria.
- If criterion C-NN has two rows in the map (two mechanisms assigned): one is redundant or they are testing different properties of the same gap -- verify before proceeding.
- The final column must read "Yes -- removing [mechanism name] would affect [criterion C-NN] only." If any row cannot honestly say "Yes": revise the mechanism assignment before proceeding.

**MECHANISM MAP GATE:** Map complete. Every row answers "Yes" in the last column. Each mechanism traces to exactly one criterion gap. Do not write aspirational criteria until the map is complete and verified.

**Aspirational criteria (1-2):** Write one criterion per row in the MECHANISM MAP. Each criterion's mechanism must be the mechanism named in its map row. State the aspirational reference anchor before each criterion.

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE:** Complete rubric. MECHANISM MAP complete and verified. No prohibited direction forms. All Pass fields three-line blocks.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft.

**OPERATING PRINCIPLE 1 -- Check 1 function:**

```
The operative check function for direction is NOT:
  "does this sentence match any phrasing in the PROHIBITED DIRECTION list?"

The operative check function IS:
  "does this Text locate causality in the wrong form's consequence?"

Apply: "Is the causal argument's subject [X] or the absence of [Y]?"
  [X] is subject -> prohibited. Rewrite.
  Absence of [Y] is subject -> permitted. Proceed.
```

**OPERATING PRINCIPLE 2 -- Audit report format:**

```
AUDIT REPORT (required output; do not substitute a narrative log)

| Criterion | Check 1 direction | Check 2 contrast | Check 3 isolation | Check 4 location | Check 5 observable | Check 6 prohibited-form | Check 7 coherence |
|-----------|------------------|-----------------|------------------|-----------------|-------------------|------------------------|------------------|
| C-NN      | pass / fail       | pass / fail      | pass / fail       | pass / fail      | pass / fail        | pass / fail             | pass / fail       |

Text flags:      [direction N, contrast N, isolation N]
Pass flags:      [location N, observable N, prohibited-form N]
Coherence flags: [coherence N]
```

Apply seven checks per criterion in isolation:

**Check 1 -- Direction.** Apply OPERATING PRINCIPLE 1. If [X] is causal subject: rewrite.
**Check 2 -- Contrast.** "not [X], but [Y]" present? If absent: add.
**Check 3 -- Isolation.** Text passes Check 1 standalone? If not: rewrite.
**Check 4 -- Location.** LOCATION names specific artifact section? If not: fill.
**Check 5 -- Observable and standard.** Both specific and verifiable? If not: fill.
**Check 6 -- Prohibited-form.** No qualitative-only language? If yes: replace.
**Check 7 -- Coherence.** OBSERVABLE follows from Text argument? Fix if not.

Output revised rubric then AUDIT REPORT (OPERATING PRINCIPLE 2 format). Do not substitute a narrative log.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the Mechanism Map principle: before aspirational criteria are written, the MECHANISM MAP assigns exactly one mechanism per criterion gap and verifies that removing any mechanism affects exactly one criterion; a mechanism responsible for two criteria cannot be evaluated independently for either, making one-to-one assignment a structural requirement rather than a design preference; the map makes coupling visible as a format error before criteria are written), then MECHANISM MAP (retained as the architectural assignment record), then TEMPLATE PAIR, then criteria ordered essential -> recommended -> aspirational, then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-03 -- Phrasing Register (Output Ownership Constitutive Definition)

**Axis:** Phrasing register
**Hypothesis:** C-26 is satisfied implicitly by R15 V-04: "Do not substitute a narrative log for this table" embeds the format requirement in the Auditor's own instruction, making the Auditor's exit condition contingent on the table's existence. But the implicit satisfaction depends on a reader recognizing that this prohibition constitutes ownership. A builder who reads the prohibition but structures the output instruction as a reference to a downstream specifier ("use the format in the appendix") satisfies the letter while failing the ownership principle. V-03 defines output ownership constitutively: a role owns its output when three conditions hold simultaneously. The constitutive definition makes delegation structurally visible as a form of non-ownership rather than a style choice. It also names the Format-Delegating Protocol as the foil -- the protocol that runs the Auditor's checks then passes findings to a Report Format Specifier -- and states why it fails C-26 in terms of the ownership conditions. C-25 is moderately addressed (the ownership principle notes that coupling defeats independent evaluation), and C-27 carries forward from R15 V-04 (function redefinition present but no competitor precedes it as constitutive gap specification).

---

You are a three-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. Do not draft criteria.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

**TEMPLATE PAIR.** Write both templates as bare fill-in forms, instantiated for this specific skill.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE:
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name]:
  [Y] = [specific required property]
  [Z] = [specific failure consequence when Y is absent]
  [X] = [specific rejected form -- wrong-direction argument for this domain]

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

**DUAL DEFINER GATE:** Failure log >= 5 entries. TEMPLATE PAIR complete. Do not proceed to Builder.

---

### BUILDER ROLE

Read the failure log and TEMPLATE PAIR. Build the rubric by filling template brackets.

**Essential criteria (3-5):** C-NN, Text (filled, no prohibited direction), Weight: essential, Category, Pass (three-line block, no prohibited qualitative forms).

**Recommended criteria (2-3):** Pass tests degree, precision, or specificity. Annotate: **Property tested:** [degree | precision | specificity].

**Aspirational criteria (1-2):** State aspirational reference anchor before each criterion.

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30
Aspirational: (sum / N_a) x 10      max 10
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE:** Complete rubric. All fields filled. No prohibited forms.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft. Before applying any checks, read the OUTPUT OWNERSHIP PRINCIPLE and the OPERATING PRINCIPLES.

---

**OUTPUT OWNERSHIP PRINCIPLE (read before any check):**

A role in this protocol owns its output when all three conditions hold simultaneously:

```
CONDITION 1 -- In-block specification:
  The required artifact is named inside this role's instruction block.
  Not in a shared preamble. Not by reference to an appendix or downstream role.
  The artifact's format is specified here, in this block.

CONDITION 2 -- Existence exit condition:
  This role's exit condition is: "the required artifact exists and is complete."
  Not: "this role's actions are complete."
  Not: "findings have been passed to the next role."
  The role cannot declare itself done while the artifact does not exist.

CONDITION 3 -- Non-transferability:
  No downstream role can produce the same artifact while this role's exit
  condition remains satisfied.
  If a downstream role produces the artifact, this role has not satisfied
  Condition 2 -- its exit condition is contingent on existence, and the
  artifact does not yet exist.
```

**What this principle prohibits -- the Format-Delegating Protocol:**

The Format-Delegating Protocol runs the Auditor's seven checks per criterion, produces findings ("C-01: direction flag; C-03: observable flag"), then passes findings to a Report Format Specifier role that converts them into a structured table. The Auditor's exit condition reads: "After all checks are complete, pass findings to Report Format Specifier." The Auditor can satisfy this exit condition while the AUDIT REPORT does not yet exist. The Report Format Specifier owns the format; the Auditor does not.

This fails Condition 2 (exit condition is "checks complete," not "report exists") and Condition 3 (a downstream role produces the report while the Auditor's exit condition is satisfied). The Format-Delegating Protocol has an Auditor and a structured report -- it has the surface form of output ownership without the operative conditions.

**Why ownership matters for independent evaluation:** Each mechanism in this protocol closes exactly one criterion. If the AUDIT REPORT is the Auditor's own output, the report-format mechanism can be evaluated independently: remove it, and the report fails -- only the format-enforcement criterion is affected. If the AUDIT REPORT is the Specifier's output, the "format enforcement" mechanism is the Specifier role, not the Auditor's instruction -- and the Auditor's instruction is a different mechanism targeting a different criterion. Coupling the format to the Auditor's instruction (Condition 1) is what makes the format mechanism independently evaluable.

---

**OPERATING PRINCIPLE 1 -- Check 1 function:**

```
The operative check function for direction is NOT:
  "does this sentence match any phrasing in the PROHIBITED DIRECTION list?"

The operative check function IS:
  "does this Text locate causality in the wrong form's consequence?"

Apply: "Is the causal argument's subject [X] or the absence of [Y]?"
  [X] is subject -> prohibited. Rewrite.
  Absence of [Y] is subject -> permitted. Proceed.
```

**OPERATING PRINCIPLE 2 -- Audit report format (this role's required output under the OUTPUT OWNERSHIP PRINCIPLE):**

The AUDIT REPORT is the required output of this role. Conditions 1, 2, and 3 of the OUTPUT OWNERSHIP PRINCIPLE apply:
- Condition 1: the format is specified in this block (below), not by reference to an appendix or downstream role.
- Condition 2: this role's exit condition is "AUDIT REPORT exists and contains a per-criterion row for every criterion."
- Condition 3: no downstream role produces this report.

```
AUDIT REPORT (required; do not substitute a narrative log; do not delegate production)

| Criterion | Check 1 direction | Check 2 contrast | Check 3 isolation | Check 4 location | Check 5 observable | Check 6 prohibited-form | Check 7 coherence |
|-----------|------------------|-----------------|------------------|-----------------|-------------------|------------------------|------------------|
| C-NN      | pass / fail       | pass / fail      | pass / fail       | pass / fail      | pass / fail        | pass / fail             | pass / fail       |

Text flags:      [direction N, contrast N, isolation N]
Pass flags:      [location N, observable N, prohibited-form N]
Coherence flags: [coherence N]
```

Apply seven checks per criterion in isolation:

**Check 1 -- Direction.** Apply OPERATING PRINCIPLE 1. Rewrite if [X] is causal subject.
**Check 2 -- Contrast.** "not [X], but [Y]" present? Add if absent.
**Check 3 -- Isolation.** Text passes Check 1 standalone? Rewrite if not.
**Check 4 -- Location.** LOCATION specific? Fill if not.
**Check 5 -- Observable and standard.** Both specific and verifiable? Fill if not.
**Check 6 -- Prohibited-form.** Qualitative-only language? Replace if yes.
**Check 7 -- Coherence.** OBSERVABLE follows from Text argument? Fix if not.

Exit condition: **AUDIT REPORT exists, is in the required format, and contains a per-criterion row for every criterion.** This exit condition is not satisfied by producing a narrative log, passing findings to another role, or writing "see revision log above." The AUDIT REPORT table IS this role's output.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state the OUTPUT OWNERSHIP PRINCIPLE: a role owns its output when the format is specified in-block, the exit condition is "artifact exists," and no downstream role can produce it; the Format-Delegating Protocol has the surface form of a structured audit but fails all three conditions -- the Auditor exits when checks are complete, not when the report exists; format embedded in the operative role's instruction makes the format mechanism independently evaluable: removing the format specification affects only the format-enforcement criterion, because the Auditor and the format are one mechanism, not two), then TEMPLATE PAIR, then criteria ordered essential -> recommended -> aspirational, then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-04 -- Role Sequence + Inertia Framing (Mechanism Definer + Pattern-Matcher Competitor)

**Axes:** Role sequence (dedicated MECHANISM DEFINER role) + inertia framing (Pattern-Matcher Auditor as constitutive gap specification)
**Hypothesis:** C-25 and C-27 are closed by two independent mechanisms, neither depending on the other. The MECHANISM DEFINER role runs before aspirational criteria are written and produces the MECHANISM MAP as its exit condition; the Builder cites the map row per criterion. The Pattern-Matcher Auditor competitor block precedes OPERATING PRINCIPLE 1 and constitutes the gap specification; OPERATING PRINCIPLE 1 follows and confirms. These two mechanisms are architecturally independent: removing the MECHANISM DEFINER role affects C-25 only (Pattern-Matcher competitor and OPERATING PRINCIPLE 1 remain unchanged). Removing the Pattern-Matcher competitor affects C-27 only (MECHANISM DEFINER and MECHANISM MAP remain unchanged). V-04 demonstrates C-25 by its own design: the two mechanisms are independently removable, each targeting exactly one criterion gap. C-26 carries forward from R15 V-04 (table embedded in Auditor output instruction, narrative log prohibited).

---

You are a four-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder (essential + recommended) -> Mechanism Definer -> Builder (aspirational) -> Dual Auditor. **Do not begin a role until the previous role's output is written.**

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. Do not draft criteria.

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
  [Y] = [specific required property]
  [Z] = [specific failure consequence when Y is absent]
  [X] = [specific rejected form]

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

**DUAL DEFINER GATE:** Failure log >= 5 entries. TEMPLATE PAIR complete. Do not proceed.

---

### BUILDER ROLE (essential and recommended criteria only)

Read the failure log and TEMPLATE PAIR. Draft essential criteria (3-5) from blocking failure modes and recommended criteria (2-3) from degrading failure modes.

**Essential criteria:** C-NN, Text (filled from TEXT FILL-IN TEMPLATE, no prohibited direction), Weight: essential, Category, Pass (three-line block).

**Recommended criteria:** Text (filled), Weight: recommended, Category, Pass (three-line block). Annotate: **Property tested:** [degree | precision | specificity].

**BUILDER GATE (phase 1):** Essential and recommended criteria complete. No prohibited direction forms. Do not write aspirational criteria until MECHANISM DEFINER role is complete.

---

### MECHANISM DEFINER ROLE

Read the essential and recommended criteria. Identify the gaps they leave uncovered. For each gap, assign exactly one independent mechanism.

**Step 1 -- Gap enumeration:**

```
Coverage record:
  Essential tier covers: [list what each essential criterion guards -- one line per criterion]
  Recommended tier covers: [list what each recommended criterion guards -- quality dimension]
  Gaps not covered: [name at least 1 property that a passing-but-not-excellent output
                     would lack; be specific -- not "could be better" but the precise
                     property whose absence makes the output non-excellent]
```

**Step 2 -- Mechanism assignment:**

For each gap, name exactly one mechanism:

```
MECHANISM MAP

| Gap | Criterion this gap will become | Mechanism name | What this mechanism enforces | Independent: removing this mechanism affects this criterion and no other |
|---|---|---|---|---|
| [gap description] | C-NN | [mechanism name -- a named structural element: a role, a table, an instruction block, a gate] | [what the mechanism prevents a Builder from doing] | Yes -- [mechanism name] closes [criterion C-NN] only. |
```

Verification: for each row, confirm:
- The mechanism is named (not described as "more careful attention" or "better instructions")
- The mechanism is a structural element that a builder either has or lacks -- not a degree of compliance
- Removing this mechanism while keeping all others would cause exactly one criterion to fail

If any row cannot say "Yes" to independence: split the mechanism or redesign before writing aspirational criteria.

**MECHANISM DEFINER GATE:** MECHANISM MAP complete. Every mechanism named, structural, and independent. Coverage record complete with at least 1 gap. Do not proceed to aspirational criteria.

---

### BUILDER ROLE (aspirational criteria)

Read the MECHANISM MAP. For each row, write one aspirational criterion whose mechanism matches the mechanism named in that row.

**Aspirational criteria (1-2):** Each criterion:
- Cites the MECHANISM MAP row it implements: **Implements mechanism:** [mechanism name from map]
- States the aspirational reference anchor: name a rubric passing C-01--C-08, name the dimension it falls short of
- Uses the TEXT FILL-IN TEMPLATE and PASS FILL-IN TEMPLATE from the TEMPLATE PAIR

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE (phase 2):** Aspirational criteria complete. Each implements exactly one mechanism from the MECHANISM MAP. No uncited map rows.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft. Before applying any checks, read the Pattern-Matcher competitor block. The competitor block is the constitutive gap specification for OPERATING PRINCIPLE 1.

---

**COMPETITOR: The Pattern-Matcher Auditor**

The Pattern-Matcher Auditor satisfies C-01 through C-22 and carries the PROHIBITED DIRECTION form-class with closure declaration. Its Check 1 function: "Does this Text contain any phrasing from the PROHIBITED DIRECTION form-class, including semantic equivalents?"

Its operative act is list membership extended to semantic equivalence. Given a Text whose surface phrasing is novel -- not in any enumerated variant, not a direct semantic equivalent the Auditor has categorized -- the Pattern-Matcher Auditor may pass the Text while it encodes the prohibited causal direction. The Auditor's test is bounded by what it can recognize as matching; causal structure testing is unbounded by recognition.

**The competitor's failure mode IS the gap specification.** A reader who covers OPERATING PRINCIPLE 1 below and asks: "from the competitor alone, what must the correct function test that the Pattern-Matcher Auditor does not?" has the answer: the correct function must test causal structure -- the identity of the causal argument's subject -- not list membership. This derivation requires only the competitor's description; it does not require the positive definition.

---

**OPERATING PRINCIPLE 1 -- Check 1 function (the gap the Pattern-Matcher Auditor fails to close):**

```
The operative check function for direction is NOT:
  "does this sentence match any phrasing in the PROHIBITED DIRECTION list?"
  "does this sentence semantically resemble any enumerated variant?"

The operative check function IS:
  "does this Text locate causality in the wrong form's consequence?"

Apply: "Is the causal argument's subject [X] or the absence of [Y]?"
  [X] is subject -> prohibited. Rewrite using TEXT FILL-IN TEMPLATE.
  Absence of [Y] is subject -> permitted. Proceed.

The PROHIBITED DIRECTION list provides instances. This function is the rule.
Consult the list for examples; apply the function for every Text.
```

**OPERATING PRINCIPLE 2 -- Audit report format:**

```
AUDIT REPORT (required output; do not substitute a narrative log)

| Criterion | Check 1 direction | Check 2 contrast | Check 3 isolation | Check 4 location | Check 5 observable | Check 6 prohibited-form | Check 7 coherence |
|-----------|------------------|-----------------|------------------|-----------------|-------------------|------------------------|------------------|
| C-NN      | pass / fail       | pass / fail      | pass / fail       | pass / fail      | pass / fail        | pass / fail             | pass / fail       |

Text flags:      [direction N, contrast N, isolation N]
Pass flags:      [location N, observable N, prohibited-form N]
Coherence flags: [coherence N]
```

Apply seven checks per criterion in isolation:

**Check 1 -- Direction.** Apply OPERATING PRINCIPLE 1. Rewrite if [X] is causal subject.
**Check 2 -- Contrast.** "not [X], but [Y]" present? Add if absent.
**Check 3 -- Isolation.** Text passes Check 1 standalone? Rewrite if not.
**Check 4 -- Location.** LOCATION specific artifact section? Fill if not.
**Check 5 -- Observable and standard.** Both specific and verifiable? Fill if not.
**Check 6 -- Prohibited-form.** Qualitative-only language? Replace if yes.
**Check 7 -- Coherence.** OBSERVABLE follows from Text? Fix if not.

Output revised rubric then AUDIT REPORT. **Do not substitute a narrative log for the table.**

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (2-3 sentences -- state both independent mechanisms: the MECHANISM DEFINER role assigns one mechanism per criterion gap before aspirational criteria are written, making one-to-one assignment a phase-gated requirement rather than a post-hoc assertion; the Pattern-Matcher Auditor competitor precedes OPERATING PRINCIPLE 1 and constitutes the gap specification -- from the competitor's failure mode alone, before reading the operative function, a builder can derive that the correct function must test causal structure; both mechanisms are independently removable: removing the Mechanism Definer affects only the assignment criterion, removing the Pattern-Matcher affects only the direction-function criterion), then MECHANISM MAP (retained as architectural record), then TEMPLATE PAIR, then criteria ordered essential -> recommended -> aspirational, then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}

---

## V-05 -- Combined Three-Axis (Mechanism Map + Output Ownership + Pattern-Matcher Competitor)

**Axes:** Role sequence (Mechanism Definer with MECHANISM MAP) + phrasing register (Output Ownership constitutive definition) + inertia framing (Pattern-Matcher Auditor as constitutive gap specification)
**Hypothesis:** Three independent mechanisms, one per target criterion. The MECHANISM DEFINER role and MECHANISM MAP close C-25: one-to-one gap-mechanism assignment is a phase-gated format requirement. The OUTPUT OWNERSHIP PRINCIPLE in the Auditor instruction closes C-26: the constitutive definition makes delegation structurally visible as non-ownership; the Auditor's exit condition is "AUDIT REPORT exists," not "checks complete." The Pattern-Matcher Auditor competitor block closes C-27: the competitor IS the gap specification; the correct function is derivable from the foil before OPERATING PRINCIPLE 1 is read. Independence: removing the Mechanism Definer (C-25 mechanism) leaves C-26 and C-27 unaffected. Removing the Output Ownership definition (C-26 mechanism) leaves C-25 and C-27 unaffected. Removing the Pattern-Matcher competitor (C-27 mechanism) leaves C-25 and C-26 unaffected. V-05 demonstrates C-25 by construction: it introduces exactly three mechanisms for exactly three gaps, each independently removable.

---

You are a four-role rubric construction system. Roles run in strict sequence: Dual Definer -> Builder (essential + recommended) -> Mechanism Definer -> Builder (aspirational) -> Dual Auditor. **Do not begin a role until the previous role's output is written.** Your protocol has three independent mechanisms, one per new aspirational criterion. Each mechanism is named, structural, and independently removable.

---

### DUAL DEFINER ROLE

Read the skill spec and sample outputs. Your output is exactly two things: a failure log and a TEMPLATE PAIR. Do not draft criteria.

**Failure log.** Minimum 5 entries:

```
F-NN | failure behavior | structural gap | broken / suboptimal
```

**TEMPLATE PAIR.** Write both templates as bare fill-in forms, instantiated for this specific skill.

```
TEMPLATE PAIR:

TEXT FILL-IN TEMPLATE:
Without [Y], the artifact [fails] because [Z]. Not [X], but [Y].

For [skill name]:
  [Y] = [specific required property]
  [Z] = [specific failure consequence when Y is absent]
  [X] = [specific rejected form]

PROHIBITED DIRECTION -- form-class exhaustive:

  Canonical:  "[X] causes [failure]"
  Variant 1:  "[X] leads to [failure]"
  Variant 2:  "the artifact [fails] when [X] is present"
  Variant 3:  "the rubric [breaks] because [X] occurs"
  Variant 4:  "presence of [X] produces [bad outcome]"
  Variant 5:  [skill-specific variant]

Form-class is closed. Any semantically equivalent construction equally prohibited.
Escape: "Without [Y], the artifact [fails] because [Z]."

PASS FILL-IN TEMPLATE:
LOCATION: [artifact section or field]
OBSERVABLE: [specific token, count, keyword, or pattern]
STANDARD: [present | count >= N | matches pattern | absent]

For [skill name]:
  LOCATION options: [2-3 specific sections]
  OBSERVABLE options: [2-3 specific confirmable facts]
  Prohibited qualitative-only forms: [1-2 tempting forms]
```

**DUAL DEFINER GATE:** Failure log >= 5 entries. TEMPLATE PAIR complete with PROHIBITED DIRECTION closure. Do not proceed.

---

### BUILDER ROLE (essential and recommended criteria only)

Draft essential criteria (3-5) from blocking failure modes and recommended criteria (2-3) from degrading failure modes.

**Essential criteria:** C-NN, Text (filled, no prohibited direction), Weight: essential, Category, Pass (three-line block, no prohibited qualitative forms).

**Recommended criteria:** Text (filled), Weight: recommended, Category, Pass (three-line block). Annotate: **Property tested:** [degree | precision | specificity].

**BUILDER GATE (phase 1):** Do not write aspirational criteria. Do not proceed to aspirational until the Mechanism Definer role is complete.

---

### MECHANISM DEFINER ROLE

Read the essential and recommended criteria. Identify gaps in their coverage. Assign one independent mechanism per gap.

**Coverage record:**

```
Essential tier covers: [one line per essential criterion -- what blocking failure it guards]
Recommended tier covers: [one line per recommended criterion -- what quality dimension it guards]

Gaps not yet covered (at least 1 required):
  [name the specific property that a passing-but-not-excellent output would lack;
   must not be reachable by tightening or combining existing criteria]
```

**MECHANISM MAP:**

```
| Gap | Intended criterion | Mechanism name | Mechanism type | What it structurally prevents | Independence verification |
|---|---|---|---|---|---|
| [gap] | C-NN | [name] | [role / table / instruction block / gate / constitutive definition] | [what a builder cannot do once this mechanism is present] | Removing [name] would cause C-NN to fail and would not affect any other criterion's mechanism. |
```

One row per gap. Mechanism type must be structural -- a named element that either exists or does not. "More careful authoring" is not a mechanism. Verify independence: for each row, confirm that the mechanism's removal does not affect any other row's criterion.

**MECHANISM DEFINER GATE:** MECHANISM MAP complete. Every mechanism named, typed as structural, and independently verified. Coverage record has at least 1 named gap. Do not write aspirational criteria until gate is satisfied.

---

### BUILDER ROLE (aspirational criteria)

For each MECHANISM MAP row, write one aspirational criterion that implements the assigned mechanism.

**Aspirational criteria (1 per map row):**
- **Implements:** [mechanism name from MECHANISM MAP]
- **Gap addressed:** [gap from MECHANISM MAP]
- **Reference anchor:** [name a rubric passing C-01--C-08; name the dimension it falls short of]
- ID: C-NN (continuing), Text (filled), Weight: aspirational, Category, Pass (three-line block)

**Scoring:**

```
Essential:    (sum) x (60 / N_e)    max 60
Recommended:  (sum / N_r) x 30      max 30  (partials = 0.5)
Aspirational: (sum / N_a) x 10      max 10  (partials = 0.5)
Composite = E + R + A               max 100
Golden threshold: >= 90
```

Tier targets: 3-5 essential, 2-3 recommended, 1-2 aspirational. At least 3 distinct categories.

**BUILDER GATE (phase 2):** Complete rubric. Aspirational criteria each cite one mechanism from MECHANISM MAP. No uncited map rows. No prohibited forms.

---

### DUAL AUDITOR ROLE

Read the TEMPLATE PAIR and rubric draft. Before applying any checks, read the following in order: the Pattern-Matcher competitor block, the OUTPUT OWNERSHIP PRINCIPLE, and both OPERATING PRINCIPLES.

---

**COMPETITOR: The Pattern-Matcher Auditor**

The Pattern-Matcher Auditor satisfies C-01 through C-22. It holds the PROHIBITED DIRECTION form-class with closure declaration: canonical form, five variants, "any semantically equivalent construction is equally prohibited." Its Check 1 function: "Does this Text contain any phrasing from the PROHIBITED DIRECTION form-class, including semantic equivalents?"

The operative act is: consult the list; test for membership; extend to semantic equivalence when surface patterns differ. This function is bounded by what the Auditor can categorize. A phrasing that encodes the prohibited causal direction through a novel syntactic structure -- "the rubric's inadequacy stems from [X]'s presence" -- may pass Check 1 because the Auditor's categorization procedure does not surface the causal structure.

**This competitor block IS the gap specification for OPERATING PRINCIPLE 1.** From the failure mode above -- before reading OPERATING PRINCIPLE 1 -- derive: the correct function must test the causal argument's subject identity, not list membership. The subject is either [X] (prohibited) or the absence of [Y] (permitted). This test requires no list. The competitor's failure is that it tests lists; the correct function tests structure.

---

**OUTPUT OWNERSHIP PRINCIPLE (applies to this role's AUDIT REPORT):**

A role in this protocol owns its output when all three conditions hold:

```
CONDITION 1 -- In-block specification:
  The required artifact's format is specified inside this role's instruction block.
  Not by reference to a shared appendix, a preamble, or a downstream role's output.

CONDITION 2 -- Existence exit condition:
  This role's exit condition is: "the required artifact exists and is complete."
  Not: "this role's actions are complete."
  Not: "findings have been passed to another role."

CONDITION 3 -- Non-transferability:
  No downstream role can produce the same artifact while this role's exit
  condition remains satisfied. If a downstream role would produce it, this
  role's Condition 2 is not yet satisfied.
```

**Why this principle is stated here:** The AUDIT REPORT table is this role's required output. Conditions 1, 2, and 3 apply to this role. Condition 1: the table format is specified in OPERATING PRINCIPLE 2 below, inside this instruction block. Condition 2: this role's exit condition is "AUDIT REPORT exists and contains a per-criterion row for every criterion." Condition 3: no downstream role produces the AUDIT REPORT. A variant of this protocol that delegates the report to a Report Format Specifier satisfies conditions on paper but fails Condition 2 for the Auditor -- the Auditor exits when checks are complete, not when the report exists; the report's existence is the Specifier's exit condition. Delegation is non-ownership.

**Why ownership matters for independent evaluation (C-25 note):** The format-enforcement mechanism targets exactly the format-enforcement criterion. If the format is embedded in the Auditor's own instruction (Condition 1), the mechanism is the Auditor's instruction block; removing it affects only the format criterion. If the format is delegated to a Specifier, the mechanism is the Specifier role; removing it affects the Specifier, not the Auditor's instruction. The mechanism's location determines which criterion it traces to. Condition 1 makes the assignment one-to-one by construction.

---

**OPERATING PRINCIPLE 1 -- Check 1 function (gap the Pattern-Matcher Auditor fails to close):**

```
The operative check function for direction is NOT:
  "does this sentence match any phrasing in the PROHIBITED DIRECTION list?"
  "does this semantically resemble any enumerated variant?"

The operative check function IS:
  "does this Text locate causality in the wrong form's consequence?"

Apply: "Is the causal argument's subject [X] or the absence of [Y]?"
  [X] is subject -> prohibited. Rewrite using TEXT FILL-IN TEMPLATE.
  Absence of [Y] is subject -> permitted. Proceed.

The PROHIBITED DIRECTION list provides instances. This function is the rule.
```

**OPERATING PRINCIPLE 2 -- Audit report format (this role's required output; OWNERSHIP CONDITIONS 1, 2, 3 apply):**

```
AUDIT REPORT

| Criterion | Check 1 direction | Check 2 contrast | Check 3 isolation | Check 4 location | Check 5 observable | Check 6 prohibited-form | Check 7 coherence |
|-----------|------------------|-----------------|------------------|-----------------|-------------------|------------------------|------------------|
| C-NN      | pass / fail       | pass / fail      | pass / fail       | pass / fail      | pass / fail        | pass / fail             | pass / fail       |

Text flags:      [direction N, contrast N, isolation N]
Pass flags:      [location N, observable N, prohibited-form N]
Coherence flags: [coherence N]
```

**Exit condition:** AUDIT REPORT exists, is in the format specified in OPERATING PRINCIPLE 2, and contains one row per criterion. This exit condition is not satisfied by passing findings to another role or producing a narrative log. Do not substitute a narrative log for this table.

Apply seven checks per criterion in isolation:

**Check 1 -- Direction.** Apply OPERATING PRINCIPLE 1. Is [X] the causal subject? If yes: rewrite.
**Check 2 -- Contrast.** "not [X], but [Y]" in Text? Add if absent.
**Check 3 -- Isolation.** Text passes Check 1 with only TEXT FILL-IN TEMPLATE visible? Rewrite if not.
**Check 4 -- Location.** LOCATION names specific artifact section? Fill if not.
**Check 5 -- Observable and standard.** Specific and verifiable? Fill if not.
**Check 6 -- Prohibited-form.** Qualitative-only language? Replace if yes.
**Check 7 -- Coherence.** OBSERVABLE is conclusion of Text argument? Fix if not.

Output revised rubric then AUDIT REPORT in OPERATING PRINCIPLE 2 format.

---

**Output:** Write to `simulations/quest/rubrics/{skill}-rubric-{date}.md`

Frontmatter:
```yaml
skill: quest-rubric
skill_target: {the skill being evaluated}
date: {today's date}
version: 1
```

Body: purpose statement (3 sentences -- one per independent mechanism: the MECHANISM DEFINER role assigns one mechanism per criterion gap before aspirational criteria are written, making one-to-one assignment a phase-gated structural requirement; the OUTPUT OWNERSHIP PRINCIPLE defines ownership constitutively -- the format is in-block, the exit condition is existence, no delegation -- making the format mechanism's trace to exactly one criterion a consequence of Condition 1; the Pattern-Matcher Auditor competitor IS the gap specification for OPERATING PRINCIPLE 1 -- the required function is derivable from the competitor's failure mode before the positive definition is read), then MECHANISM MAP (retained), then TEMPLATE PAIR (retained with PROHIBITED DIRECTION), then criteria ordered essential -> recommended -> aspirational, then scoring section, then AUDIT REPORT.

---

**Inputs:**

Skill spec:
{skill_spec}

Sample outputs:
{sample_outputs}
