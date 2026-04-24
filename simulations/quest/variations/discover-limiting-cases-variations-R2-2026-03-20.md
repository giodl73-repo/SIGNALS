Written to `simulations/quest/variations/discover-limiting-cases-variations-R2-2026-03-20.md`.

---

## Round 2 — discover-limiting-cases — 5 Variations

### Variation axes and hypotheses

| Variation | Axis | Key hypothesis |
|-----------|------|----------------|
| **V-01** | L-00 integration depth | A pre-filled UNSTATED block in Phase 3 teaches the format by example; C-11/C-13 without gates tests whether example-driven instruction substitutes for checklist enforcement |
| **V-02** | Prohibition density (maximal) | Prohibition text on every field saturates the model against verbal fill-in; C-12 intentionally absent as the controlled variable |
| **V-03** | Phrasing register (imperative minimal) | Ultra-terse imperatives with all 4 new criteria in compressed form tests whether brevity plus completeness outperforms verbose scaffolding |
| **V-04** | Lifecycle emphasis + L-00 (V-05 + V-03 best patterns) | Adding L-00 to the R1-V-05 gate structure is the minimum change to target all 6 aspirational criteria |
| **V-05** | Role sequence + full aspirational complement | Mathematician role (strongest C-09 enforcer) with C-11/C-12/C-13/C-14 embedded at the role that owns each criterion |

### Aspirational criterion coverage

| | C-09 | C-10 | C-11 | C-12 | C-13 | C-14 |
|-|------|------|------|------|------|------|
| V-01 | yes | yes | yes | **no** | partial | yes (deep) |
| V-02 | yes | yes | yes | **no (soft)** | yes (maximal) | yes |
| V-03 | yes | yes | yes | yes | yes | yes |
| V-04 | yes | yes | yes | yes | yes | yes (deep) |
| V-05 | yes | yes | yes | yes | yes | yes |

### Key structural choices

**V-01 vs V-02** — controlled absence of C-12 in two different forms: V-01 uses example-based instruction (pre-filled Phase 3 L-00 block as a model), V-02 uses prohibition saturation. Comparing them isolates whether the gate does independent work when the rest of the instruction is strong.

**V-03** — all 4 new criteria present in the shortest possible form. If it scores equal to V-04/V-05, prompt verbosity is waste.

**V-04** — the natural R1 successor: R1-V-05 + L-00. Only two additions to a proven structure: the L-00 row in Phase 2, its seed in Phase 4 register, and Gate 2 updated to require L-00 is present.

**V-05** — role-owned enforcement: each criterion is assigned to the role that executes the relevant work. The Extractor gate enforces C-08/C-14 before algebra begins. The Mathematician example pair + prohibition enforces C-09/C-11/C-13 at the point of algebraic work. The Auditor verdict prohibition enforces C-03/C-13 at verdict time.
-|------|------|------|------|
| **V-01** | yes | yes | yes | no | partial | yes (deep) |
| **V-02** | yes | yes | yes | no (soft) | yes (maximal) | yes |
| **V-03** | yes | yes | yes | yes | yes | yes |
| **V-04** | yes | yes | yes | yes | yes | yes (deep) |
| **V-05** | yes | yes | yes | yes | yes | yes |

### Key design decision

C-14 (L-00 anchor) is the only aspirational pattern that requires a pre-filled artifact
element rather than an instruction change. C-11/C-12/C-13 can be added to any existing phase
structure. C-14 adds a row that must propagate through Phase 2, Phase 4 register, and
frontmatter count. The R2 research question: is Phase 2 placement sufficient (surface), or
does a pre-filled L-00 verification block in Phase 3 (deep) materially improve C-06 quality by
showing what a complete UNSTATED block looks like before the model writes its own?

---

## V-01: L-00 Integration Depth

**Axis:** L-00 integration depth -- L-00 appears as a pre-filled row in Phase 2, as a
complete pre-filled model verification block in Phase 3 (showing what UNSTATED looks like
before the model writes any blocks of its own), and as a seed row in Phase 4. The Phase 3
model block demonstrates the correct/wrong pair for "Substituted form" (C-11) and carries
prohibition text on Verdict and Substituted form (C-13). No checklist gates (C-12 absent --
controlled omission). Tests whether example-driven instruction substitutes for gate enforcement.

**Hypothesis:** A complete pre-filled UNSTATED block in Phase 3 does two things: it seeds the
UNSTATED format for L-00 correctly, and it shows the model what every UNSTATED block should
look like. Combined with prohibition text on the key failure fields (C-13), this should produce
C-09 compliance (algebra, not prose) and C-06 quality (specific justification, not generic)
without requiring gates. Expected gap: without a hard gate, later rows may drift on C-08.

```
You are running /discover-limiting-cases for: {{topic}}

Test whether every equation in the paper behaves correctly at its natural limits. These checks
are rarely done explicitly but always checked by hostile reviewers. Complete every labeled
field. A blank field is a failed criterion.

The primary inertia is: the author assumed the limits were fine and did not check them.
L-00 is pre-printed as the always-UNSTATED inertia assumption.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read: discover-hypothesis, specify-spec, simulate-argument if available.

Extract and list below:
- Every equation that models a dynamic or static relationship (label each EQ-01, EQ-02, ...)
- The paper's stated parameter space and variable ranges
- Any explicit claims the paper makes about behavior at limits

Equations found: [list each with label]
Parameter space: [state domain for each free variable, or "unstated" if not given]
Limit claims in paper: [quote or summarize each explicit limit claim, or write "None found"]

---

## PHASE 2 -- LIMIT INVENTORY

L-00 is pre-printed and always UNSTATED. No paper says "we verified all limits behave
correctly." Add rows for every equation found in Phase 1.

Required coverage: at least one equilibrium row (set time derivatives to zero) AND at least
one of: zero-input, saturation, or degenerate-parameter row.

Fill every cell. "Is expected behavior stated in paper?" requires YES or NO only.
Blank, "unknown", or "unclear" are not valid answers.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-00 | (all equations) | (all variables) | (all limits) | All limits behave correctly | NO -- this is never stated |
| L-01 | [equation] | [variable] | [→ value] | [what it should give] | YES / NO |
| L-02 | [equation] | [variable] | [→ value] | [what it should give] | YES / NO |
[Add rows until every equation has at least one limit row and required coverage is met.]

---

## PHASE 3 -- LIMIT VERIFICATION

L-00 does not require algebraic substitution -- it represents the absence of verification
across all equations, not a single substitution. The pre-filled block below shows the correct
format for an UNSTATED block. Read it before writing any blocks of your own.

---
L-00 [MODEL BLOCK -- read this, then replicate the format for L-01 onward]:
Equation: (all equations -- no single equation to substitute)
At limit (all variables → all boundaries):
  Substituted form: N/A -- L-00 represents the absence of verification, not a single substitution
  Result: Unknown -- the paper does not check
  Expected: All equations behave correctly at all natural limits
  Verdict: UNSTATED -- no other verdict is valid for L-00
  If UNSTATED: The paper implicitly assumes every equation behaves correctly at all boundaries.
               Reviewer attack: "Did you verify your model behaves sensibly at the limits?"
               The paper has no answer. This is what L-00 represents.
---

For each L-ID from L-01 onward, complete this block exactly. Every field is required.

"Substituted form" must show the equation with the limit value substituted in.
  Correct: "dR/dt = alpha*O*(1-tau) - beta*tau^2, setting dR/dt=0 gives alpha*O*(1-tau) = beta*tau^2"
  Wrong: "the derivative vanishes at steady state"

---
L-[NN]: [one-line description of this limit]
Equation: [exact symbolic form]
At limit ([variable] → [value]):
  Substituted form: [equation with limit value substituted -- algebra required, not description]
  Result: [what the substituted form evaluates to or simplifies to]
  Expected: [paper's explicit claim OR mathematical/physical requirement if unstated]
  Verdict: PASS / FAIL / UNSTATED -- no other phrasing
  If FAIL: [exact discrepancy -- which term is wrong, what sign is off, what is missing]
  If FAIL -- error type: mathematical error / unstated approximation / model design choice
  If UNSTATED: [what the paper implicitly assumes by not stating this limit]
  If UNSTATED: [the one sentence the paper should add to preempt this reviewer attack]
---

Repeat for every row in Phase 2 except L-00.

---

## PHASE 4 -- LIMIT REGISTER

L-00 is pre-seeded as always UNSTATED/P2. Add one row per L-ID from Phase 3.

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
| L-00 | UNSTATED | P2 | No limits verified; reviewer will ask: "Did you test model behavior at boundaries?" | Add limit-verification section or per-equation boundary note |
| [L-ID] | PASS/FAIL/UNSTATED | P1/P2/P3/-- | [one sentence -- name the specific discrepancy or question, not "reviewer may ask"] | [equation + section + change, or -- for PASS] |

Severity scale:
- P1: formula gives wrong or nonsensical result at a natural limit
- P2: limit not tested or stated -- reviewer will ask; one sentence in the paper fixes it
- P3: behavior is correct but surprising -- worth a note to preempt confusion
- --: PASS, no action needed

Justification must name the specific question or discrepancy. "Reviewer may ask" alone fails.

---

## PHASE 5 -- AMEND

List one concrete fix per severity class present in the register.

If P1 exists:
  P1 fix: Equation: [name it] / Section: [name it] / Change: [what the correction is]

If P2 exists:
  P2 fix: Equation: [name it] / Section: [name it] / Sentence to add: [write the sentence]

If P3 exists:
  P3 fix: Behavior: [name it] / Note to add: [write the note]

Generic advice ("review the model") is not a fix. Name the equation. Name the section.

---

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter required:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n -- rows in Phase 2 excluding L-00]
  p1_failures: [n -- P1 rows in Phase 4 excluding L-00]
  unstated_limits: [n -- UNSTATED verdicts in Phase 4 including L-00]
```

---

## V-02: Prohibition Density (Maximal)

**Axis:** Prohibition density -- every field in every phase carries explicit inline prohibition
text immediately after its label. Not selective: every field. Tests whether maximal prohibition
saturation eliminates all verbal fill-in and format drift without requiring checklist gates.
Includes L-00 (C-14) and a correct/wrong example pair for "Substituted form" (C-11). Checklist
gate is advisory only (C-12 intentionally absent as the controlled variable). Tests whether
prohibition density alone substitutes for gate enforcement.

**Hypothesis:** If every field is annotated with "not X", no valid path to the failure mode
exists for any field. The gate should be unnecessary when prohibitions are total. Expected to
score strongly on C-09/C-10/C-11/C-13/C-14. Expected gap: without a hard gate, C-08 compliance
may degrade in later rows as the model drifts from the dense instruction.

```
You are running /discover-limiting-cases for: {{topic}}

Test whether every equation in the paper behaves correctly at its natural limits. Hostile
reviewers check limits before reading conclusions. The most common failure is assuming the
limits are fine without checking. L-00 captures that assumption -- it is always UNSTATED.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read: paper or draft artifact for {{topic}}, and any of: discover-hypothesis, specify-spec,
simulate-argument.

Equations found: [list -- not "see paper", not blank; one line per equation with label EQ-NN]
Parameter space: [domain per variable -- not "various", not blank; write "unstated" if not given]
Limit claims in paper: [quotes or "None found" -- not "unclear", not blank]

---

## PHASE 2 -- LIMIT INVENTORY

L-00 is pre-printed. For every equation found in Phase 1, add rows. Required: at least one
equilibrium row and at least one of: zero-input, saturation, degenerate-parameter.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-00 | (all equations) | (all) | (all) | All limits are correct | NO -- not stated in any paper |

For rows L-01 onward, field-by-field requirements:
- L-ID: L-NN format -- not a description, not "L1" or bare "1"
- Equation: exact symbolic form -- not a word description, not an equation number alone
- Parameter / Variable: one variable name or parameter symbol -- not a phrase
- Limit direction: → [value] format -- not "goes to" or "approaches" or a word description
- Expected behavior: one sentence stating what the equation gives -- not "see the paper"
- Is expected behavior stated in paper?: YES or NO -- no other answer, not blank, not "unclear"

| L-01 | [exact equation] | [symbol] | → [value] | [one sentence] | YES / NO |
[Add rows until all equations covered and required coverage met.]

Advisory check before Phase 3: every cell filled? Every "Stated in paper?" cell is YES or NO?
If not, fill before proceeding -- a blank cell is a failed criterion.

---

## PHASE 3 -- LIMIT VERIFICATION

One block per L-ID from Phase 2 (skip L-00 -- it represents all unchecked limits, not one
substitution). Every labeled field in every block is required.

---
L-[NN]: [one-line description -- not blank]
Equation: [exact symbolic form -- not a word description]
At limit ([variable symbol] → [value]):
  Substituted form: [write the algebra -- e.g., "dR/dt=0 gives alpha*O*(1-tau) = beta*tau^2"]
                    [NOT "the derivative vanishes" -- NOT "the equation simplifies"]
  Result: [what it evaluates to -- not "as expected", not "the correct value"]
  Expected: [paper's explicit claim or physical requirement -- not "it should work"]
  Verdict: PASS / FAIL / UNSTATED -- no other phrasing, not "looks correct", not "unclear"
  If FAIL: [exact discrepancy -- which term, which sign, what is missing -- not "something is wrong"]
  If FAIL -- error type: mathematical error / unstated approximation / model design choice
             -- one of these three, no other classification
  If UNSTATED: [paper's implicit assumption -- not "the paper doesn't say", not blank]
  If UNSTATED: [one sentence the paper should add -- name the equation, not generic advice]
---

---

## PHASE 4 -- LIMIT REGISTER

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
| L-00 | UNSTATED | P2 | Reviewer attack: "Did you verify limit behaviors?" No answer in paper | Add limit-verification note per equation |

For rows L-01 onward, field-by-field requirements:
- Verdict: PASS / FAIL / UNSTATED -- must match Phase 3 block; no other phrasing
- Impact: P1 / P2 / P3 / -- -- one of these four only; not blank for non-PASS
  - P1: wrong or nonsensical result at a natural limit
  - P2: limit not tested or stated -- reviewer will ask
  - P3: correct but surprising -- worth a note
  - --: PASS, no action
- Justification: [one sentence naming specific discrepancy or question]
                 -- not "reviewer may ask" alone, not blank for non-PASS
- What needs to change: [equation name + section name + change]
                        -- not "review the model", not blank for non-PASS

---

## PHASE 5 -- AMEND

For each severity class present in the register:

P1 fix (if any P1 exists):
  Equation: [name it -- not "the main equation"]
  Section: [name it -- not "the methods section"]
  Change: [what the correction is -- write the corrected form or statement]

P2 fix (if any P2 exists):
  Equation: [name it -- not "the dynamic equation"]
  Section: [name it -- not "the results section"]
  Sentence to add: [write the exact sentence -- not "add a sentence about this"]

P3 fix (if any P3 exists):
  Behavior: [name the limit and equation -- not "the surprising one"]
  Note to add: [write the exact note]

---

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter required:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n -- rows in Phase 2 excluding L-00; count them]
  p1_failures: [n -- P1 rows in Phase 4; count them]
  unstated_limits: [n -- UNSTATED verdicts in Phase 4 including L-00; count them]
```

---

## V-03: Phrasing Register (Imperative Minimal)

**Axis:** Phrasing register -- ultra-terse imperative commands only. No explanatory framing
prose, no motivation, no "hostile reviewers" context-setting. Every instruction is the shortest
imperative that conveys the requirement. All 4 new criteria present in minimal form. Tests
whether brevity plus completeness outperforms verbose scaffolding.

**Hypothesis:** Minimal instructional noise produces equal or better compliance because the
model navigates fewer words to the required action. All 6 aspirational criteria are present
in compressed form: C-14 (L-00 pre-filled), C-11 (inline NOT annotation on Substituted form),
C-12 (two hard gates), C-13 (inline prohibitions on Verdict and Substituted form). Expected
gap: without "hostile reviewer" framing, UNSTATED justifications (C-06) may be less specific
because the reviewer-attack motivation is absent.

```
You are running /discover-limiting-cases for: {{topic}}

---

## PHASE 1

Read: paper or draft for {{topic}}, plus discover-hypothesis, specify-spec, simulate-argument
if present.

List: every equation (label EQ-01, EQ-02, ...). Record each variable's domain. Note every
explicit limit claim, or write "none found."

---

## PHASE 2

Build the limit inventory. L-00 is pre-filled and always UNSTATED.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Stated in paper? |
|------|----------|---------------------|----------------|-------------------|-----------------|
| L-00 | (all equations) | (all) | (all limits) | All limits behave correctly | NO |
| L-01 | [equation] | [variable] | [→ value] | [expected behavior] | YES / NO |

Cover: at least one equilibrium row. At least one of: zero-input, saturation, degenerate-parameter.
"Stated in paper?": YES or NO. No other answer. No blanks.

GATE: every cell filled? Every "Stated in paper?" cell is YES or NO?
Do not begin Phase 3 until both are true. Fill blanks before continuing.

---

## PHASE 3

One block per L-ID (skip L-00). Fill every field.

---
L-[NN]: [description]
Equation: [exact form]
At limit ([var] → [val]):
  Substituted form: [algebra -- e.g., "dR/dt=0 gives alpha*O*(1-tau) = beta*tau^2"]
                    [NOT "the derivative vanishes" -- NOT a description of what happens]
  Result: [what it evaluates to]
  Expected: [paper's claim or physical requirement]
  Verdict: PASS / FAIL / UNSTATED -- no other phrasing
  If FAIL: [exact discrepancy]
  If FAIL -- error type: mathematical error / unstated approximation / model design choice
  If UNSTATED: [paper's implicit assumption] / [sentence the paper should add]
---

GATE: every "Substituted form" shows algebra? Every verdict is PASS/FAIL/UNSTATED?
Do not begin Phase 4 until both are true. Rewrite any descriptions as algebra before continuing.

---

## PHASE 4

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
| L-00 | UNSTATED | P2 | No limit verification in paper | Add limit-check section |
| [L-ID] | [verdict] | P1/P2/P3/-- | [one sentence -- name specific question] | [equation + section + change, or --] |

Severity: P1 = wrong result. P2 = unstated. P3 = surprising. -- = PASS.
Justification: one sentence naming the specific issue. "Reviewer may ask" alone fails.

Amendments. One fix per severity class present:

P1 fix (if any): Equation: [name] / Section: [name] / Change: [correction]
P2 fix (if any): Equation: [name] / Section: [name] / Sentence: [write it]
P3 fix (if any): Behavior: [name] / Note: [write it]

---

Write: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path>: write flat into <path>/

Frontmatter:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n -- Phase 2 rows excluding L-00]
  p1_failures: [n -- P1 rows in Phase 4]
  unstated_limits: [n -- UNSTATED verdicts in Phase 4 including L-00]
```

---

## V-04: Lifecycle Emphasis + L-00 Integration (Gates + Inertia)

**Axis:** Lifecycle emphasis (V-05 gate structure from R1) combined with L-00 deep integration
(V-03 inertia anchor from R1). Takes R1-V-05 as the base and adds: L-00 pre-filled in Phase 2
(C-14), a pre-filled L-00 seed row in Phase 4, and Gate 2 updated to require L-00 is present
before proceeding. C-11/C-12/C-13 all carried from V-05. This is the minimum-change path from
the best R1 variation to a variation targeting all 6 aspirational criteria.

**Hypothesis:** V-05's gate structure is the most reliable compliance mechanism for C-08/C-09.
Adding L-00 fills the only aspirational gap V-05 had in R1. The combination should produce all
6 aspirational criteria with the smallest change from a known strong variation. Gates remain
the primary enforcement; L-00 anchors inertia framing. Expected to score at or above R1-V-05
on all criteria.

```
You are running /discover-limiting-cases for: {{topic}}

Four phases with hard gates. Do not begin a phase until its gate condition is met.
The most common failure is skipping the algebra and going straight to a verdict.
The gate between Phase 3 and Phase 4 exists specifically to prevent this.
The second most common failure is assuming the limits are fine. L-00 captures that assumption.

---

## PHASE 1 -- ACQUIRE

Read the paper or draft artifact for {{topic}}.
Also read: discover-hypothesis, specify-spec, simulate-argument if available.

List:
- Every equation in the paper (label EQ-01, EQ-02, ...)
- The domain of each variable and parameter (stated range, or "unstated")
- Every explicit limit claim in the paper (quote or "None found")

GATE 1:
[ ] All equations labeled (EQ-NN format)?
[ ] All variable domains recorded (value or "unstated")?
Do not begin Phase 2 until both boxes are checked.

---

## PHASE 2 -- INVENTORY

L-00 is pre-printed. It is always UNSTATED -- no paper says "we verified all limits."
For every equation found in Phase 1, add rows starting at L-01.

Required coverage:
- At least one equilibrium row (set time derivatives to zero, verify recovery of static formula)
- At least one of: zero-input row, saturation row, or degenerate-parameter row

Fill every cell. "Is expected behavior stated in paper?" requires YES or NO only.
Blank cells, "unknown", or "unclear" are not valid answers.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-00 | (all equations) | (all variables) | (all limits) | All limits behave correctly | NO -- the paper does not state this |
| L-01 | [equation] | [variable] | [→ value] | [expected behavior] | YES / NO |
[Add rows until all equations covered and required coverage met.]

GATE 2:
[ ] L-00 row is present and marked NO in "Is expected behavior stated in paper?" column?
[ ] Every row L-01 onward has YES or NO in "Is expected behavior stated in paper?" column?
[ ] At least one equilibrium row present?
[ ] At least one additional class row present (zero-input, saturation, or degenerate)?
Do not begin Phase 3 until all four boxes are checked.
If any cell is blank: fill it before proceeding. If the paper does not state the expected
behavior, that is NO -- the paper's implicit assumption is that the limit is fine.

---

## PHASE 3 -- VERIFY

For each L-ID starting at L-01, complete the verification block. Skip L-00 (it represents all
unchecked limits, not a single equation -- no algebraic substitution exists for it).

The "Substituted form" field must show the equation with the limit value substituted in.
Write the algebra, not a description:
  Correct: "dR/dt = alpha*O*(1-tau) - beta*tau^2, setting dR/dt=0 gives alpha*O*(1-tau) = beta*tau^2"
  Wrong: "the derivative vanishes at steady state"

---
L-[NN]: [one-line limit description]
Equation: [exact symbolic form]
At limit ([variable] → [value]):
  Substituted form: [equation with limit value substituted -- algebra required, not description]
  Result: [what it evaluates to or simplifies to]
  Expected: [paper's claim OR physical/mathematical requirement]
  Verdict: PASS / FAIL / UNSTATED -- no other phrasing
  If FAIL: [exact discrepancy -- which term, which sign, what is missing]
  If FAIL -- error type: mathematical error / unstated approximation / model design choice
  If UNSTATED: [what the paper implicitly assumes by not stating this limit]
  If UNSTATED: [the sentence the paper should add to preempt this reviewer attack]
---

GATE 3:
[ ] One verification block exists for every L-ID in Phase 2 except L-00?
[ ] Every "Substituted form" field shows an equation or algebraic expression, not a description?
[ ] Every verdict is exactly one of: PASS / FAIL / UNSTATED?
Do not begin Phase 4 until all three boxes are checked.
If any "Substituted form" is a description: rewrite it as algebra before proceeding.
If any verdict is qualitative ("looks correct", "unclear"): assign PASS/FAIL/UNSTATED.

---

## PHASE 4 -- REGISTER AND AMEND

Build the limit register from Phase 3 verdicts. L-00 is pre-seeded as always UNSTATED/P2.

Register:

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
| L-00 | UNSTATED | P2 | No limit verification in paper; reviewer will ask: "Did you test model behavior at boundaries?" | Add limit-check section or per-equation boundary notes |
| [L-ID] | PASS/FAIL/UNSTATED | P1/P2/P3/-- | [one sentence -- name specific issue, not "reviewer may ask"] | [equation + section + change, or -- for PASS] |

Severity scale:
- P1: formula gives wrong or nonsensical result at a natural limit
- P2: limit not tested or stated -- reviewer will ask; one sentence in the paper fixes it
- P3: behavior is correct but surprising -- worth one sentence to preempt confusion
- --: PASS, no action

Amendments. One concrete fix per severity class present:

P1 fix (if any P1 exists):
  Target equation: [name]
  Target section: [name]
  Fix: [exact correction -- what changes in the formula or claim]

P2 fix (if any P2 exists):
  Target equation: [name]
  Target section: [name]
  Fix: [exact sentence to add -- write the sentence]

P3 fix (if any P3 exists):
  Target behavior: [name]
  Fix: [exact note to add -- write the note]

GATE 4:
[ ] limits_checked = number of L-ID rows in Phase 2 excluding L-00?
[ ] p1_failures = number of P1 rows in Phase 4 excluding L-00?
[ ] unstated_limits = number of UNSTATED verdicts in Phase 4 including L-00?

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

## V-05: Role Sequence + Full Aspirational Complement

**Axis:** Role sequence combined with all 4 new aspirational criteria embedded at the role
level that owns each criterion. Takes R1-V-04's three-role pipeline and adds: Extractor
produces L-00 as the first row and includes a gate before handoff (C-12, C-14); Mathematician
receives the correct/wrong example pair and prohibition text on Substituted form (C-11, C-13);
Auditor receives prohibition-heavy verdict block (C-13 on Verdict) and inherits L-00 as seed
row in register (C-14). C-09/C-10 are enforced by the Mathematician role boundary.

**Hypothesis:** The Mathematician role is the strongest C-09 enforcer because its entire job
is to write algebra before any verdict is possible. Embedding C-11 (example pair) in the
Mathematician's instructions and C-13 (prohibition) on the Substituted form field creates a
three-layer defense: role framing, example pair, and prohibition. C-14 (L-00) propagates from
Extractor through Auditor naturally. The gate at the Extractor→Mathematician boundary (C-12)
enforces C-08 before the algebra phase begins. Expected to produce all 6 aspirational criteria.

```
You are running /discover-limiting-cases for: {{topic}}

Three roles execute in sequence. Each role reads the prior role's output. Do not skip ahead.
The inertia assumption -- that limits were never checked -- is captured as L-00 in every role.

---

## ROLE 1: EXTRACTOR

Your job: read the paper, identify every equation and its natural limits, produce the Phase 2
Limit Inventory table. L-00 is pre-printed as the first row.

Read the paper or draft artifact for {{topic}}.
Also check: discover-hypothesis, specify-spec, simulate-argument if available.

Extract every equation. For each equation, identify limits to test. Include at minimum:
- One equilibrium / steady-state row (set time derivatives to zero)
- At least one additional row: zero-input, saturation, or degenerate-parameter

"Is expected behavior stated in paper?" requires YES or NO only. No other answer.

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-00 | (all equations) | (all) | (all limits) | All limits behave correctly | NO -- no paper states this |
| L-01 | [equation] | [variable] | [→ value] | [expected behavior] | YES / NO |
[Add rows until all equations covered and required coverage met.]

EXTRACTOR GATE before handing off to MATHEMATICIAN:
[ ] L-00 row present and marked NO in "Is expected behavior stated in paper?"?
[ ] Every row L-01 onward has YES or NO in "Is expected behavior stated in paper?"?
[ ] At least one equilibrium row present?
[ ] At least one additional class row present (zero-input, saturation, or degenerate)?
Do not hand off until all four boxes are checked.

EXTRACTOR OUTPUT COMPLETE. Hand off to MATHEMATICIAN.

---

## ROLE 2: MATHEMATICIAN

Your job: perform the algebraic verification for each L-ID in the Extractor's table. Skip
L-00 -- it represents unchecked limits across all equations, not a single substitution.
Write the algebra before writing any judgment. Do not assign PASS, FAIL, or UNSTATED -- those
are Auditor decisions.

For each L-ID from L-01 onward, complete this block:

---
L-[NN] MATH:
Equation: [exact form from Extractor's table]
Substitution: [state what you are substituting: "[variable] → [value]"]
Substituted form: [write the equation with the value substituted -- show every algebraic step]
  Correct: "dR/dt = alpha*O*(1-tau) - beta*tau^2, with dR/dt=0:
            0 = alpha*O*(1-tau) - beta*tau^2
            therefore alpha*O*(1-tau) = beta*tau^2"
  Wrong: "the derivative vanishes at steady state"
  Wrong: "the equation simplifies to the equilibrium form"
Result: [what the substituted form evaluates to or simplifies to]
Math check: matches / does not match / cannot determine from paper
  Basis: [what you are comparing against -- paper's claim or physical requirement]
If "does not match": [exact discrepancy -- which term, which sign, what is missing]
If "does not match": error type: mathematical error / unstated approximation / model design choice
---

Do not write PASS, FAIL, or UNSTATED. Do not skip the "Substituted form" field. Do not write
a description of what happens where algebra is required.

MATHEMATICIAN OUTPUT COMPLETE. Hand off to AUDITOR.

---

## ROLE 3: AUDITOR

Your job: read the Mathematician's blocks, assign official verdicts, build the register and
amendments. You may not change the Mathematician's algebraic work -- only interpret it.
L-00 is pre-seeded in the register as always UNSTATED/P2.

Step 1 -- Assign verdicts. For each L-ID from L-01 onward, write a verdict block:

---
L-[NN] VERDICT:
Verdict: PASS / FAIL / UNSTATED -- no other phrasing
Basis: [one sentence citing the Mathematician's math check field]
If FAIL: [quote the exact discrepancy from the Mathematician's "does not match" line]
If FAIL: severity = P1 -- [one-line justification: what wrong result does the formula give?]
If UNSTATED: severity = P2 -- [one-line justification: what specific reviewer question does this raise?]
If PASS and surprising: severity = P3 -- [one-line note: why is this worth stating?]
If PASS and expected: severity = --
---

Step 2 -- Build the Limit Register:

| L-ID | Verdict | Impact | Justification | What needs to change |
|------|---------|--------|---------------|---------------------|
| L-00 | UNSTATED | P2 | No limit verification in paper; reviewer will ask: "Did you test boundary behaviors?" | Add limit-check section or per-equation boundary note |
| [L-ID] | [verdict from Step 1] | [P1/P2/P3/--] | [one sentence -- specific issue, not "reviewer may ask"] | [equation + section + change, or -- for PASS] |

Step 3 -- Amendments. One concrete fix per severity class present in the register:

P1 fix (if any P1 exists):
  Equation: [name] / Section: [name] / Change: [exact correction -- write the corrected form]

P2 fix (if any P2 exists):
  Equation: [name] / Section: [name] / Sentence to add: [write the exact sentence]

P3 fix (if any P3 exists):
  Behavior: [name] / Note to add: [write the exact note]

---

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Frontmatter required:
  skill: discover-limiting-cases
  topic: {{topic}}
  date: {{date}}
  limits_checked: [n -- L-ID rows in Extractor table excluding L-00]
  p1_failures: [n -- P1 rows in Auditor register excluding L-00]
  unstated_limits: [n -- UNSTATED verdicts in Auditor register including L-00]
```
