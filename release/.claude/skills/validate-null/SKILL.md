---
name: validate-null
description: "Check whether an empirical result (regression coefficient, exponential fit, ODE parameter) is distinguishable from a specified null distribution. Includes pre-registration completeness check: every researcher degree of freedom must be committed in writing before analysis runs."
allowed-tools: [Read, Write, Glob]
param_set: lean
---

You are running /validate-null for: {{topic}}

Check whether an empirical result is distinguishable from a specified null distribution, and verify that every researcher degree of freedom in the analysis design is committed to in writing before data analysis runs.

**Before you begin**: read the paper or draft artifact for {{topic}}. Read any prior signals: simulate-derivation (for fitted ODE parameters), discover-causal (for theoretical mechanism), validate-consistency (for value cross-checks). Identify the primary empirical claim -- the number, coefficient, or fit that the paper is staking a result on. That is the target of this skill.

---

## PHASE 1 -- EMPIRICAL CLAIM ACQUISITION

Extract the primary empirical claim(s) and their statistical context.

**Claim registry:**

| CL-ID | Claim | Value | Method | Location in paper |
|-------|-------|-------|--------|------------------|

**Analysis context** (for each CL-ID):

```
CL-[NN]: [exact claim]
  Fitted quantity: [what was estimated -- coefficient, rate, R^2, etc.]
  Data source: [dataset, sample size, time period]
  Method: [regression / exponential fit / ODE parameter estimation / time series / other]
  Primary reviewer who will challenge this: [name the reviewer most likely to raise a null challenge]
```

---

## PHASE 2 -- NULL MODEL STATEMENT

State the null explicitly in the same mathematical form as the empirical claim.

For each CL-ID:

```
CL-[NN] null:
  Null hypothesis H0: [formal statement]
  Null generative process: [the process that produces the data if H0 is true]
  What a null result looks like: [what value would the fitted quantity take under H0?]
  Why this null is the correct baseline: [one sentence]
```

Do not accept vague nulls ("no effect"). Every null must be stateable as a generative process that a computer could simulate.

---

## PHASE 3 -- NULL DISTRIBUTION PROCEDURE

Describe the procedure that generates the null distribution with enough precision that an analyst could implement it without consulting the paper.

For each CL-ID:

```
CL-[NN] null distribution:
  Procedure type: PERMUTATION / BOOTSTRAP / ANALYTIC / PRIOR / OTHER

  Step-by-step procedure:
    1. [first step]
    2. [second step]
    ...
    N. Report P(statistic >= observed) across all iterations

  Number of iterations: [N -- typically 1,000 exploration, 10,000 publication]
  Software: [function or package -- e.g., scipy.stats.permutation_test]
  Key assumption: [exchangeability / stationarity / etc.]
  Assumption check: verified in paper? YES / NO / PARTIALLY
```

---

## PHASE 4 -- RESULT CLASSIFICATION

Classify the empirical result against the null distribution.

For each CL-ID:

```
CL-[NN] classification:

  If null distribution values available:
    P-value: [value]
    Observed vs null 95th percentile: [observed] vs [null 95th]
    Classification: SIGNAL / BORDERLINE / PATTERN-IN-NOISE

  If null distribution not computed:
    Expected null value: [theoretical expectation]
    Distance from null: [qualitative assessment]
    Classification: SIGNAL-LIKELY / BORDERLINE-LIKELY / CANNOT-CLASSIFY
    Required action: [what computation would resolve this]
```

Definitions:
- **SIGNAL**: result in tail of null (p < 0.05); finding is robust
- **BORDERLINE**: near threshold (0.05 <= p < 0.15); depends on specification choices
- **PATTERN-IN-NOISE**: consistent with null; finding not robust as stated

---

## PHASE 5 -- SPECIFICATION SENSITIVITY

Identify every researcher degree of freedom that could change the result classification.

**Degree-of-freedom registry:**

| DOF-ID | Description | Current choice | Alternative choices | Effect on result |
|--------|-------------|----------------|---------------------|-----------------|

For each DOF marked BORDERLINE or UNSPECIFIED:

```
DOF-[NN] sensitivity:
  Choice: [the specific decision the analyst made]
  Alternative: [most defensible alternative]
  Effect on primary result: ROBUST / SENSITIVE / UNKNOWN
  If SENSITIVE: [how the result changes]
```

Required degrees of freedom to check (at minimum):
- Outcome variable operationalization
- Sample inclusion/exclusion criteria
- Control variable set
- Time period or sample period
- Model specification (linear vs nonlinear)
- Outlier handling
- For exponential fits / ODE fitting: event list, anchor case selection

---

## PHASE 6 -- PRE-REGISTRATION COMPLETENESS

**Pre-registration register:**

| DOF-ID | Description | Status | Evidence |
|--------|-------------|--------|---------|

Status: COMMITTED / IMPLICIT / UNCOMMITTED / UNKNOWN

For each UNCOMMITTED or UNKNOWN DOF:

```
DOF-[NN] commitment gap:
  What must be written: [exact statement that would commit this choice]
  Where to write it: [plan.md / methods section / pre-registration document]
  Risk if uncommitted: [what a skeptical reviewer (name) would say]
```

---

## PHASE 7 -- VERDICT

| Verdict | Meaning |
|---------|---------|
| PUBLISHABLE-AS-IS | All claims SIGNAL; all DOFs committed; no P1 or P2 faults |
| NEEDS-SENSITIVITY-ANALYSIS | BORDERLINE claim exists; sensitivity across DOFs must be reported |
| NEEDS-PREREGISTRATION | UNCOMMITTED DOFs exist; choices must be locked in writing |
| PARTIALLY-ROBUST | Mix of SIGNAL and BORDERLINE claims |
| FALSIFIED-BY-NULL | PATTERN-IN-NOISE: result consistent with null |

State the verdict and which claims and DOFs drive it.

**Amend** (3 fixes, P1 first):

Severity: P1 (falsified by null or DOF changes core claim) / P2 (uncommitted DOF a named reviewer will flag) / P3 (presentation gap, result likely robust)

1. [DOF/CL-ID] [P1/P2/P3]: [specific action]
2. [DOF/CL-ID] [P1/P2/P3]: [specific action]
3. [DOF/CL-ID] [P1/P2/P3]: [specific action]

---

Write artifact to: signals/validate/null/{{topic}}-null-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: validate-null, topic: {{topic}}, date: {{date}}, claims: [n], uncommitted_dofs: [n], verdict: [verdict]
