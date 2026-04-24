Written to `simulations/quest/variations/discover-limiting-cases-variations-R1-2026-03-20.md`.

---

## Round 1 — discover-limiting-cases — 5 Variations

### Variation axes chosen

**Single-axis (V-01 through V-03):**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| **V-01** | Output format | Pre-printed tables + labeled block fields make C-01/C-02/C-09 structural. The model can't omit "Substituted form" without leaving a visible blank. |
| **V-02** | Phrasing register | Question-driven conversational prose. Tests whether interrogation-without-templates produces the same rubric compliance. Expected gap: C-09 (algebra stays verbal) and C-08 (YES/NO column needs a column to force it). |
| **V-03** | Inertia framing | L-00 is pre-printed as always-UNSTATED: the paper assumes limits are fine. Every UNSTATED verdict carries the specific reviewer attack it preempts. |

**Combination axes (V-04 through V-05):**

| Variation | Axes | Hypothesis |
|-----------|------|------------|
| **V-04** | Role sequence + output format | Extractor → Mathematician → Auditor. Mathematician writes algebra *before* verdict; Auditor reads it to assign PASS/FAIL/UNSTATED. This makes C-09 a sequential dependency, not a recommendation. |
| **V-05** | Lifecycle emphasis + inertia framing | Four phases with checklist gates. Gate 2 blocks Phase 3 until every "stated in paper" cell is YES/NO. Gate 3 blocks Phase 4 until every substituted form is algebraic. Gates make C-08 and C-09 hard exits. |

### Key research question for R2

C-09 (algebraic substitution) is the highest-value gap in the baseline skill: the field exists in the verification block but the label "Substituted form" doesn't prevent verbal fill-in. V-01 adds a named field, V-04 makes it a role-dependency, V-05 makes it a gate. If all three improve on baseline, the gate is likely doing the work. If only V-04/V-05 improve, the role boundary and gate matter more than the field label alone.
ty justification). The role boundary between Mathematician
and Auditor enforces C-09: the algebra must appear before the verdict can be written.

**V-05: Lifecycle Emphasis + Inertia Framing** -- Four explicit phases with checklist gates.
PHASE 2 gate: every row has YES or NO in the "stated in paper" column before Phase 3 begins --
makes C-08 a hard exit condition, not a recommendation. PHASE 3 gate: "Substituted form" is
algebraic (equation shown, not described) before verdict is written -- makes C-09 a gate, not
aspirational. Inertia interrogated as a peer: every UNSTATED verdict carries the sentence
"A hostile reviewer will ask this; the paper's current implicit answer is [X]."

### Key design decision

C-09 (substituted form written algebraically) is the rubric's highest-value aspirational
criterion because it distinguishes checking the math from describing the math. In V-01 and
V-04, it is made structural by naming it as a required labeled field; the model cannot write
"the derivative vanishes" without something before it in the named slot. The open research
question for R2: does a named field reliably produce algebra, or does the model fill the slot
with prose anyway? If so, V-04's role boundary (Mathematician writes form BEFORE verdict)
may be the stronger gate.

---

## V-01: Output Format (Fully Templated)

**Axis:** Output format -- Phase 2 table and Phase 3 verification blocks have all required
fields pre-printed as fixed structure. Missing a field means leaving a visible blank, not
omitting a section.

**Hypothesis:** Pre-printed field labels prevent the most common failure modes: incomplete
Phase 2 tables (missing the "stated in paper" column), prose-only Phase 3 evaluations, and
algebraic substitution replaced by a verbal description. Each label is a micro-gate.

```
You are running /discover-limiting-cases for: {{topic}}

Test whether every equation in the paper behaves correctly at its natural limits. These checks
are rarely done explicitly but always checked by hostile reviewers. Complete every labeled
field. A blank field is a failed criterion.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read: discover-hypothesis, specify-spec, simulate-argument if available.

Extract and list below:
- Every equation that models a dynamic or static relationship
- The paper's stated parameter space and variable ranges
- Any explicit claims the paper makes about behavior at limits

Equations found: [List each equation by label]
Parameter space: [State the domain for each free variable]
Limit claims in paper: [Quote or summarize each explicit limit claim, or write "None found"]

---

## PHASE 2 -- LIMIT INVENTORY

For every equation found in Phase 1, create at least one row. Standard limits to include:
- Equilibrium / steady state: set all time derivatives to zero
- Zero input / boundary: set driving variable to zero
- Saturation: set driving variable to its maximum (1 for probabilities, stated max otherwise)
- Degenerate parameters: set each free parameter to zero

Fill every cell. Do not leave the "Is expected behavior stated in paper?" column blank.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-01 | [equation] | [variable] | [→ value] | [what it should give] | YES / NO |
| L-02 | [equation] | [variable] | [→ value] | [what it should give] | YES / NO |
| L-03 | [equation] | [variable] | [→ value] | [what it should give] | YES / NO |
[Add rows until every equation has at least one limit tested and at least one equilibrium row
and at least one row from: zero-input, saturation, or degenerate parameter.]

---

## PHASE 3 -- LIMIT VERIFICATION

For each L-ID in the Phase 2 table, complete this block exactly. Fill every labeled field.
"Substituted form" must show the equation with the limit value substituted in -- write the
algebra, not a description of what happens.

---
L-[NN]: [limit description]
Equation: [exact equation form]
At limit ([variable] → [value]):
  Substituted form: [equation with limit value substituted -- show the algebra]
  Result: [what the substituted form evaluates to]
  Expected: [what the paper claims OR what physical/mathematical intuition requires]
  Verdict: PASS / FAIL / UNSTATED
  If FAIL: [exact discrepancy -- which term is wrong, what sign is off, what is missing]
  If FAIL -- error type: mathematical error / unstated approximation / model design choice
  If UNSTATED: [what the paper should say about this limit]
---

Repeat this block for every row in Phase 2. Do not combine rows.

---

## PHASE 4 -- LIMIT REGISTER

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
| [L-ID] | PASS/FAIL/UNSTATED | P1/P2/P3/-- | [one sentence -- why this severity] | [specific fix or --] |

Severity scale:
- P1: formula gives a wrong or nonsensical result -- likely a sign error or missing term
- P2: limit not tested or stated -- reviewer will ask; needs one sentence in the paper
- P3: behavior is technically correct but surprising -- worth a note to preempt confusion
- --: PASS, no action needed

Every non-PASS verdict requires a severity label AND a one-line justification. Do not write
"reviewer may ask" as the justification -- name what specific question the reviewer will ask.

---

## PHASE 5 -- AMEND

List one concrete fix per severity class present in the body.

If P1 exists:
  P1 fix: [name the equation and section -- state what the correction is]

If P2 exists:
  P2 fix: [name the equation and section -- state the sentence to add]

If P3 exists:
  P3 fix: [name the behavior -- state the clarifying sentence to add]

Generic advice ("review the model", "add more explanation") is not a fix. Name the equation.
Name the section. State the change.

---

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter required:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n -- must match row count in Phase 2]
  p1_failures: [n -- must match P1 count in Phase 4]
  unstated_limits: [n -- must match UNSTATED count in Phase 4]
```

---

## V-02: Phrasing Register (Conversational / Question-Driven)

**Axis:** Phrasing register -- the skill is entirely question-driven prose. No pre-printed
tables or labeled blocks. The model answers a sequence of questions rather than filling
templates. Tests whether guided interrogation produces rubric-compliant outputs without
structural enforcement.

**Hypothesis:** Strong questions about specific mathematical behaviors will surface the same
limit failures as structured blocks, because the questions force the same reasoning. Expected
to score well on C-01/C-02/C-03/C-04, weakly on C-09 (algebraic substitution tends to stay
verbal without a labeled field demanding algebra) and C-08 (the "stated in paper" question
may not get a YES/NO answer without a column forcing it).

```
You are running /discover-limiting-cases for: {{topic}}

A hostile reviewer will check your limits before anything else. They will pick one equation,
substitute a boundary value, and see if the result makes sense. Do this first, before they do.

---

Start by reading the paper or draft artifact for {{topic}}.
Also check: discover-hypothesis, specify-spec, simulate-argument if available.

**What equations does the paper present?**
List every equation that models a dynamic or static relationship. Give each a label (L-01,
L-02, ...). For each one, write one sentence explaining what it computes.

**What is the natural equilibrium of the model?**
Pick the central dynamic equation. Set all time derivatives to zero. Write out what the
equation becomes. Does that simplified form match the static formula in the paper? If the
paper has no static formula, what does the equilibrium form say must be true at steady state?
Is that stated anywhere in the paper?

**What happens when the driving input goes to zero?**
For each equation with a driving input (an external signal, an opportunity, a forcing term),
set that input to zero. Write what the equation gives. Is that result physically sensible --
does the output go to zero, stay at a baseline, or do something else? Does the paper say what
should happen in this case?

**What happens when the driving input hits its maximum?**
For probabilities, that is 1. For bounded variables, use the stated maximum. Does the output
saturate correctly? Does the paper claim or imply it should?

**What happens when each free parameter goes to zero?**
A model with a free parameter should degenerate gracefully when that parameter is removed.
For each free parameter (growth rate, decay constant, scaling factor), write what the equation
becomes when the parameter is zero. Does the model reduce to something simpler and sensible?

**Which of these limits does the paper actually verify or state?**
For each limit you tested, answer: does the paper explicitly state what should happen at this
limit? YES or NO. If NO, what is the implicit assumption the paper is making by not stating it?

**Which limits failed?**
For each limit where the result did not match what was expected: describe the discrepancy
precisely. Is this a mathematical error (wrong sign, missing term), an unstated approximation
(the formula is only valid when X is small and the paper does not say so), or a model design
choice that needs to be made explicit?

**What is the priority order for fixing these?**
Rate each non-PASS limit as P1 (formula gives the wrong answer), P2 (correct but unstated,
reviewer will ask), or P3 (correct but surprising, worth a note). For each P1 and P2, state
exactly what sentence or equation change would resolve it.

---

Write a summary artifact to:
  signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/

The artifact must include:
- A table with one row per limit tested (L-ID, equation, variable, direction, verdict)
- A structured block per L-ID with: equation, substitution, result, verdict
- A register table with severity and fix for each non-PASS verdict
- YAML frontmatter: skill, topic, date, limits_checked, p1_failures, unstated_limits
```

---

## V-03: Inertia Framing (Status-Quo as Named Competitor)

**Axis:** Inertia framing -- the status-quo (skip the limit checks) is L-00, pre-printed as
the first row of Phase 2. L-00 is always UNSTATED by construction: no paper says "we verified
all limits are correct." The skill frames each UNSTATED verdict as a preemptive response to a
named reviewer attack.

**Hypothesis:** Making the skip-cost visible (L-00 as a pre-printed UNSTATED row) and framing
every UNSTATED as a specific reviewer attack will raise the quality and completeness of the
unstated-limit identification and justification. Expected to improve C-06 (severity
justification) and C-08 (stated-in-paper column) by replacing the generic "reviewer will ask"
with a specific attack the artifact is defending against.

```
You are running /discover-limiting-cases for: {{topic}}

Hostile reviewers check limits before reading conclusions. They pick an equation, substitute
a boundary value, and look for nonsense. If they find it before you do, the paper fails.
This skill preempts that attack. The primary inertia is: the author assumed the limits were
fine and did not check them. L-00 is always present and always UNSTATED.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read: discover-hypothesis, specify-spec, simulate-argument if available.

Extract: every equation that models a dynamic or static relationship, the paper's stated
parameter space, and any explicit claims about behavior at limits.

---

## PHASE 2 -- LIMIT INVENTORY

L-00 is pre-printed. It is always UNSTATED -- no paper says "we verified all limits." Add
rows for every equation in the paper.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-00 | (all equations) | (all) | (all limits) | All limits behave correctly | NO -- this is the inertia assumption |
| L-01 | [equation] | [variable] | → 0 or steady state | [what it should give] | YES / NO |
| L-02 | [equation] | [variable] | [→ value] | [what it should give] | YES / NO |
[Add rows. Include at least one equilibrium row and one additional class: zero-input,
saturation, or degenerate parameter.]

For every row where the answer is NO: write one sentence naming the specific question a hostile
reviewer will ask. Example: "Reviewer will ask: what does τ give when O=0? The paper is silent."
This is the attack this artifact is defending against.

---

## PHASE 3 -- LIMIT VERIFICATION

For each L-ID (starting at L-01), evaluate the limit. L-00 does not need a verification block.

```
L-[NN]: [limit description]
Equation: [exact form]
At limit ([variable] → [value]):
  Substituted form: [equation with limit value substituted -- show the algebra]
  Result: [what the substituted form evaluates to]
  Expected: [paper's claim OR physical/mathematical requirement]
  Verdict: PASS / FAIL / UNSTATED
  Reviewer attack this defends against: [the specific question this verdict answers]
  If FAIL: [exact discrepancy]
  If FAIL -- error type: mathematical error / unstated approximation / model design choice
  If UNSTATED: [the sentence the paper should add to preempt this attack]
```

---

## PHASE 4 -- LIMIT REGISTER

| L-ID | Verdict | Impact | Reviewer attack | What the paper needs |
|------|---------|--------|-----------------|---------------------|
| L-00 | UNSTATED | P2 | "Did you check that your model behaves correctly at all limits?" | Add limit-verification section or note |
| [L-ID] | [verdict] | [P1/P2/P3/--] | [specific reviewer question] | [specific fix or --] |

For every non-PASS row: the "Reviewer attack" column must name the specific question (not
"reviewer may ask"), and the "What the paper needs" column must name the equation or section
and state the change. Generic advice fails.

---

## PHASE 5 -- AMEND

For each severity class present in the register:

P1 fix (if any P1 exists):
  Equation: [name it]
  Section: [name it]
  Change: [what the fix is -- correct the formula or the claim]
  Defends against: [the reviewer attack this fix closes]

P2 fix (if any P2 exists):
  Equation: [name it]
  Section: [name it]
  Change: [the sentence to add]
  Defends against: [the reviewer attack this fix closes]

P3 fix (if any P3 exists):
  Behavior: [name it]
  Change: [the clarifying sentence to add]

---

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter required:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n]
  p1_failures: [n]
  unstated_limits: [n]
```

---

## V-04: Role Sequence + Output Format (Three-Role Pipeline)

**Axis:** Role sequence combined with output format -- three sequential roles enforce a
strict dependency: the Extractor produces the Phase 2 table, the Mathematician performs
algebraic verification (substituted form BEFORE verdict), the Auditor builds the register and
amendments. The role boundary between Mathematician and Auditor makes C-09 structural: the
algebra is written before the verdict is locked, not inferred from the verdict.

**Hypothesis:** The Mathematician role -- whose only job is to write the substituted form and
result for each L-ID -- will reliably produce algebraic substitutions (C-09) because the role
description frames the work as mathematical derivation, not evaluation. The Auditor then reads
the Mathematician's output and assigns verdicts, which enforces consistency between Phase 3
and Phase 4 (C-03) because the Auditor cannot assign a verdict without the algebra to read.

```
You are running /discover-limiting-cases for: {{topic}}

Three roles execute in sequence. Each role reads the prior role's output. Do not skip ahead.

---

## ROLE 1: EXTRACTOR

Your job: read the paper, identify every equation and its natural limits.
Produce exactly one output: the Phase 2 Limit Inventory table.

Read the paper or draft artifact for {{topic}}.
Also check: discover-hypothesis, specify-spec, simulate-argument if available.

Extract every equation that models a dynamic or static relationship. For each equation,
identify the limits to test. Include at minimum:
- One equilibrium / steady-state row (set time derivatives to zero)
- At least one additional row: zero-input, saturation, or degenerate parameter

Fill every cell, including "Is expected behavior stated in paper?" -- answer YES or NO only.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-01 | [equation] | [variable] | [→ value] | [expected behavior] | YES / NO |
[Add rows until all equations are covered.]

EXTRACTOR OUTPUT COMPLETE. Hand off to MATHEMATICIAN.

---

## ROLE 2: MATHEMATICIAN

Your job: perform the algebraic verification for each L-ID in the Extractor's table.
Produce exactly one output block per L-ID. Write the algebra before writing the verdict.
Do not assign final verdicts -- write what the math gives; leave verdict assignment to Auditor.

For each row in the Extractor's table, complete this block:

---
L-[NN] MATH:
Equation: [exact form from Extractor's table]
Substitution: [state what you are substituting -- "[variable] → [value]"]
Substituted form: [write the equation with the value substituted in -- show every step]
  Example: "dR/dt = alpha*O*(1-tau) - beta*tau^2 with dR/dt=0 gives
            0 = alpha*O*(1-tau) - beta*tau^2
            therefore alpha*O*(1-tau) = beta*tau^2"
Result: [what the substituted form evaluates to or simplifies to]
Math check: [does this match Expected from Extractor's table? State: matches / does not match / cannot determine from paper]
If "does not match": [describe the discrepancy precisely -- wrong term, wrong sign, missing factor]
If "does not match": error type: mathematical error / unstated approximation / model design choice
---

Do not write PASS, FAIL, or UNSTATED. Those are Auditor's decisions. Write only what the math shows.

MATHEMATICIAN OUTPUT COMPLETE. Hand off to AUDITOR.

---

## ROLE 3: AUDITOR

Your job: read the Mathematician's blocks, assign official verdicts, build the register and
amendments. You may not change the Mathematician's algebraic work -- only interpret it.

Step 1 -- Assign verdicts. For each L-ID:
- Read the Mathematician's "Math check" field
- If "matches": verdict = PASS
- If "does not match": verdict = FAIL
- If "cannot determine from paper": verdict = UNSTATED
- Write a structured verdict block:

---
L-[NN] VERDICT:
Verdict: PASS / FAIL / UNSTATED
If FAIL: [quote the exact discrepancy from the Mathematician's block]
If FAIL: severity = P1 -- [one-line justification: what result does the formula give that is wrong?]
If UNSTATED: severity = P2 -- [one-line justification: what specific question will a reviewer ask?]
If PASS and surprising: severity = P3 -- [one-line note on why this is worth stating]
If PASS and expected: severity = --
---

Step 2 -- Build the Limit Register:

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
[One row per L-ID. Every non-PASS row requires both a justification and a specific fix.]

Step 3 -- Amendments. For each severity class present:

P1 fix (if any): Equation: [name] / Section: [name] / Change: [what the correction is]
P2 fix (if any): Equation: [name] / Section: [name] / Sentence to add: [exact text]
P3 fix (if any): Behavior: [name] / Note to add: [exact text]

---

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter required:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n -- count of L-IDs in Extractor table]
  p1_failures: [n -- count of P1 in Auditor register]
  unstated_limits: [n -- count of UNSTATED in Auditor register]
```

---

## V-05: Lifecycle Emphasis + Inertia Framing (Checklist Gates)

**Axis:** Lifecycle emphasis combined with inertia framing -- four explicit phases each with
a checklist gate that must pass before the next phase begins. The gates make C-08 (stated-in-
paper column) and C-09 (algebraic substitution) hard exit conditions rather than
recommendations. Inertia is interrogated at the gate: every UNSTATED verdict requires a one-
sentence answer to "what is the paper implicitly assuming by not stating this?"

**Hypothesis:** Checklist gates before phase transitions will produce higher C-08 and C-09
compliance than any non-gated format, because the model cannot advance to Phase 3 without
every Phase 2 row having a YES or NO answer, and cannot advance to Phase 4 without every
Phase 3 block having an algebraic substituted form. The gates are not advisory -- they are
the only instruction the model is given about those criteria.

```
You are running /discover-limiting-cases for: {{topic}}

Four phases with hard gates. Do not begin a phase until its gate condition is met.
The most common failure mode is skipping the algebra and going straight to a verdict.
The gate between Phase 3 and Phase 4 exists specifically to prevent this.

---

## PHASE 1 -- ACQUIRE

Read the paper or draft artifact for {{topic}}.
Also read: discover-hypothesis, specify-spec, simulate-argument if available.

List:
- Every equation in the paper with a label (EQ-01, EQ-02, ...)
- The domain of each variable and parameter (stated range, or "unstated")
- Every explicit limit claim in the paper (quote or "none found")

GATE 1: Every equation is labeled. Every variable has a stated domain or "unstated."
[ ] Check: all equations labeled? [ ] Check: all variable domains recorded?
Do not begin Phase 2 until both boxes are checked.

---

## PHASE 2 -- INVENTORY

For each equation, identify the limits to test. Assign L-IDs.

Required coverage:
- At least one equilibrium row (set time derivatives to zero, check recovery of static formula)
- At least one of: zero-input row, saturation row, or degenerate-parameter row

Fill every cell. The "Is expected behavior stated in paper?" column requires YES or NO.
Blank cells, "unknown", or "unclear" are not valid answers.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-01 | [eq] | [var] | [→ value] | [expected] | YES / NO |
[Add rows until all equations are covered and required coverage is met.]

GATE 2: Before proceeding to Phase 3:
[ ] Every row has YES or NO in the "Is expected behavior stated in paper?" column?
[ ] At least one equilibrium row present?
[ ] At least one additional class row present (zero-input, saturation, or degenerate)?
Do not begin Phase 3 until all three boxes are checked.
If any cell is blank: fill it before proceeding. If the paper does not state the expected
behavior, that is a NO -- the paper's implicit assumption is that the limit is fine.

---

## PHASE 3 -- VERIFY

For each L-ID, complete the verification block. The "Substituted form" field must show the
equation with the limit value substituted -- write the algebra, not a description.

Correct: "dR/dt = alpha*O*(1-tau) - beta*tau^2, setting dR/dt=0 gives alpha*O*(1-tau) = beta*tau^2"
Wrong: "the derivative vanishes at steady state"

---
L-[NN]: [limit description]
Equation: [exact form]
At limit ([variable] → [value]):
  Substituted form: [equation with limit value substituted -- algebra required]
  Result: [what it evaluates to]
  Expected: [paper's claim OR physical/mathematical requirement]
  Verdict: PASS / FAIL / UNSTATED
  If FAIL: [exact discrepancy]
  If FAIL -- error type: mathematical error / unstated approximation / model design choice
  If UNSTATED: [what the paper is implicitly assuming by not stating this limit]
  If UNSTATED: [the sentence the paper should add]
---

GATE 3: Before proceeding to Phase 4:
[ ] Every L-ID has a verification block?
[ ] Every "Substituted form" field shows an equation, not a description?
[ ] Every verdict is exactly one of: PASS / FAIL / UNSTATED (no "looks correct", no "unclear")?
Do not begin Phase 4 until all three boxes are checked.
If any "Substituted form" is a description: rewrite it as algebra. If any verdict is
qualitative: assign PASS, FAIL, or UNSTATED and move the qualitative language to the notes.

---

## PHASE 4 -- REGISTER AND AMEND

Build the limit register from Phase 3 verdicts. Then write targeted amendments.

Register:

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
[One row per L-ID. P1/P2/P3/-- severity. Every non-PASS row needs justification AND a specific fix.]

Severity scale:
- P1: formula gives a wrong or nonsensical result at a natural limit
- P2: limit not tested or stated -- reviewer will ask; a sentence in the paper fixes it
- P3: behavior is correct but surprising -- worth one sentence to preempt confusion
- --: PASS, no action

Amendments:

For each severity class present in the register, write one concrete fix:

P1 fix (if any P1 exists):
  Target equation: [name]
  Target section: [name]
  Fix: [exact correction -- what changes in the formula or in the claim]

P2 fix (if any P2 exists):
  Target equation: [name]
  Target section: [name]
  Fix: [exact sentence to add -- write the sentence]

P3 fix (if any P3 exists):
  Target behavior: [name]
  Fix: [exact note to add]

GATE 4: Verify frontmatter counts match body before writing:
[ ] limits_checked = number of L-ID rows in Phase 2 inventory?
[ ] p1_failures = number of P1 rows in Phase 4 register?
[ ] unstated_limits = number of UNSTATED verdicts in Phase 4 register?

---

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter required:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n]
  p1_failures: [n]
  unstated_limits: [n]
```
