You are running /simulate-derivation for: {{topic}}

Trace a mathematical derivation step by step — not the logical argument, but the algebraic manipulation. Every line of the derivation is a claim that the left side equals the right side after some operation. This skill catches sign errors, missing terms, unjustified approximations, and dimensional inconsistencies that simulate-argument misses.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read: simulate-argument, discover-limiting-cases if available.
Extract: the derivation to trace, the stated starting point, the stated endpoint, and any approximations the paper acknowledges.

---

## PHASE 2 -- DERIVATION MAP

Extract each step of the derivation as a row:

| S-ID | Starting expression | Operation applied | Resulting expression | Justification | Type |
|------|-------------------|------------------|---------------------|---------------|------|
| S-01 | [exact LHS] | [e.g. "expand product"] | [exact RHS] | [algebraic identity, substitution, approximation, definition] | EXACT / APPROX / DEFINITION |

Types:
- **EXACT**: the step is an exact algebraic identity — can be verified mechanically
- **APPROX**: an approximation is made (Taylor expansion, small-angle, mean-field, etc.) — must be explicitly stated with its validity conditions
- **DEFINITION**: a symbol is introduced or substituted — must be consistent with all prior uses
- **PHYSICAL**: a physical assumption is encoded algebraically (e.g. "at equilibrium, dR/dt = 0") — must be stated as an assumption

Flag every APPROX step: what is being approximated, under what conditions is it valid, and does the paper state this?

---

## PHASE 3 -- STEP-BY-STEP VERIFICATION

For each step S-ID, verify:

```
S-[NN]: [description]
From: [expression A]
Operation: [what is done]
To: [expression B]
Verification:
  - Algebraically correct? YES / NO / CONDITIONAL (state condition)
  - If APPROX: is the approximation stated? YES / NO; is its validity condition stated? YES / NO
  - Dimensional consistency: units LHS = units RHS? YES / NO / NOT APPLICABLE
  - Sign check: does the sign of each term make physical/mathematical sense? YES / NO
Verdict: SOUND / WEAK / BROKEN
If WEAK or BROKEN: [exact description]
```

---

## PHASE 4 -- DERIVATION FAULT REGISTER

| F-ID | S-ID | Verdict | Type | Description | Fix |
|------|------|---------|------|-------------|-----|
| F-01 | S-03 | BROKEN | Sign error | RHS should be −β·τ² not +β·τ² — the damping term must oppose growth | Change sign and verify it recovers the correct equilibrium |
| F-02 | S-07 | WEAK | Unstated approx | Mean-field approximation taken without stating validity conditions | Add "assuming weak spatial correlations" or cite the mean-field condition |

Severity:
- P1: The derivation is algebraically wrong — the stated result does not follow from the stated starting point
- P2: An approximation is made but not stated — the result is only valid under conditions the paper doesn't mention
- P3: A step is correct but could be clearer — notational ambiguity or missing intermediate step

---

## PHASE 5 -- AMEND

Three targeted fixes:
1. [P1 fix: the algebraic error — exact correction]
2. [P2 fix: the unstated approximation — what to add to the paper]
3. [P3 fix: the step that needs a clarifying sentence or intermediate line]

Write artifact to: signals/simulate/derivation/{{topic}}-derivation-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: simulate-derivation, topic: {{topic}}, date: {{date}}, steps_traced: [n], p1_errors: [n], unstated_approx: [n]
