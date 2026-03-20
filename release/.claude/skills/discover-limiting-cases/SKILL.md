---
name: discover-limiting-cases
description: "Test whether model equations behave correctly at known limits. Does dR/dt=0 recover the static formula? Does the model degenerate correctly at zero input? Identifies FAIL, PASS, and UNSTATED limits with P1/P2/P3 severity."
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /discover-limiting-cases for: {{topic}}

Test whether a model's equations behave correctly at known limits and boundary conditions. For the RMM program: does dR/dt → 0 at equilibrium? Does the dynamic formula reduce to the static formula at steady state? Does the model degenerate correctly when parameters go to zero? These checks are rarely done explicitly but always checked by hostile reviewers.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read: discover-hypothesis, specify-spec, simulate-argument if available.

Extract: every equation that models a dynamic or static relationship, the paper's stated parameter space, and any claims about behavior at limits.

---

## PHASE 2 -- LIMIT INVENTORY

For each equation or model in the paper, identify the limits to test:

| L-ID | Equation | Parameter / Variable | Limit direction | Expected behavior | Is expected behavior stated in paper? |
|------|----------|---------------------|----------------|-------------------|--------------------------------------|
| L-01 | dR/dt = α·O·(1−τ) − β·τ² | dR/dt | → 0 (equilibrium) | reduces to static τ = O×(1−R) | YES / NO |
| L-02 | dR/dt = ... | α parameter | → 0 | degenerate: no adaptation | YES / NO |
| L-03 | τ(O, R) | O | → 0 | τ → 0 (no opportunity, no influence) | YES / NO |
| L-04 | τ(O, R) | R | → 1 | τ → 0 (full resistance, no influence) | YES / NO |

Standard limits to always check (adapt to this paper's variables):
- **Equilibrium / steady state**: set all time derivatives to zero — does it recover the static formula?
- **Zero input / boundary**: set the driving variable to zero — does the output go to zero or a sensible baseline?
- **Saturation**: set the driving variable to its maximum (1 for probabilities) — does the output saturate correctly?
- **Degenerate parameters**: set each free parameter to zero or infinity — does the model degenerate gracefully?
- **Additivity / superposition** (if claimed): do two independent inputs sum linearly?

---

## PHASE 3 -- LIMIT VERIFICATION

For each limit in Phase 2, evaluate:

```
L-[NN]: [limit description]
Equation: [exact form]
At limit [variable → value]:
  Substituted form: [what the equation becomes]
  Result: [what it gives]
  Expected: [what the paper claims or what physical intuition requires]
  Verdict: PASS / FAIL / UNSTATED (limit not addressed in paper)
  If FAIL: [exact discrepancy]
  If UNSTATED: [what the paper should say about this limit]
```

For limits that FAIL: is the failure a mathematical error, an unstated approximation, or a model design choice that needs to be made explicit?

---

## PHASE 4 -- LIMIT REGISTER

| L-ID | Verdict | Impact | What needs to change |
|------|---------|--------|---------------------|
| L-01 | PASS | — | — |
| L-02 | FAIL | P1 — the model doesn't degenerate correctly; reviewer will catch this | Add explicit statement of behavior at α=0, or fix the formula |
| L-03 | UNSTATED | P2 — reviewer will ask; should be stated | Add "When O=0, τ=0 by construction" to §2 |

Severity:
- P1: The formula gives a wrong or nonsensical result at a natural limit — likely a sign error or missing term
- P2: The limit isn't tested or stated — reviewer will ask; needs one sentence in the paper
- P3: The behavior is technically correct but surprising — worth noting to preempt confusion

---

## PHASE 5 -- AMEND

Three targeted fixes:
1. [P1 fix: the limit that produces a wrong result — fix the equation or the paper's claims]
2. [P2 fix: the most important unstated limit — add the statement]
3. [P3 fix: the surprising-but-correct behavior that needs a sentence of explanation]

Write artifact to: signals/discover/limiting-cases/{{topic}}-limiting-cases-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: discover-limiting-cases, topic: {{topic}}, date: {{date}}, limits_checked: [n], p1_failures: [n], unstated_limits: [n]
