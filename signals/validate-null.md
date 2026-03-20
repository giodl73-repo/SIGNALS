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
  Fitted quantity: [what was estimated -- coefficient, rate, R², etc.]
  Data source: [what dataset, sample size, time period]
  Method: [regression / exponential fit / ODE parameter estimation / time series / other]
  Primary reviewer who will challenge this: [name the reviewer most likely to raise a null challenge]
```

Read enough of the paper to answer: what is the paper betting on? One number, one coefficient, one effect size -- that is CL-01. Additional claims are CL-02 onward.

---

## PHASE 2 -- NULL MODEL STATEMENT

State the null explicitly in the same mathematical form as the empirical claim.

For each CL-ID:

```
CL-[NN] null:
  Null hypothesis H0: [formal statement -- e.g., "λ = 0 in the population" or
    "β_MFQ = 0 after ideology controls" or "interval timing is drawn from Uniform[t_min, t_max]"]
  Null generative process: [the process that would produce the data if H0 is true]
  What a null result looks like: [what value would the fitted quantity take under H0?]
  Why this null is the correct baseline: [one sentence -- why is this the right comparison?]
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

  Number of iterations required: [N -- typically 1,000 for exploration, 10,000 for publication]

  Software implementation: [what function or package would compute this?
    e.g., "scipy.stats.permutation_test", "boot::boot in R", "manual loop with numpy.random.permutation"]

  Key assumption: [the one distributional assumption the procedure depends on --
    e.g., "exchangeability of residuals" or "stationarity of intervals"]

  Assumption check: is this assumption verified in the paper? YES / NO / PARTIALLY
```

---

## PHASE 4 -- RESULT CLASSIFICATION

Classify the empirical result against the null distribution.

For each CL-ID:

```
CL-[NN] classification:

  If null distribution values are available from prior analysis or the paper:
    P-value or tail probability: [value or range]
    Observed vs null 95th percentile: [observed value] vs [null 95th pct]
    Classification: SIGNAL / BORDERLINE / PATTERN-IN-NOISE

  If null distribution has not been computed:
    Expected null value: [theoretical null expectation if known]
    Distance from null: [is the empirical result far from the expected null value?]
    Classification: SIGNAL-LIKELY / BORDERLINE-LIKELY / CANNOT-CLASSIFY
    Required action: [what computation or analysis would resolve the classification]
```

**Classification definitions:**
- **SIGNAL**: result is in the tail of the null distribution (p < 0.05 or equivalent); finding is robust
- **BORDERLINE**: result is near the threshold (0.05 ≤ p < 0.15); classification depends on specification choices
- **PATTERN-IN-NOISE**: result is consistent with null; finding is not robust as stated
- **SIGNAL-LIKELY / BORDERLINE-LIKELY / CANNOT-CLASSIFY**: used when null distribution is unavailable

---

## PHASE 5 -- SPECIFICATION SENSITIVITY

Identify every researcher degree of freedom that could change the result classification.

**Degree-of-freedom registry:**

| DOF-ID | Description | Current choice | Alternative choices | Effect on result |
|--------|-------------|----------------|---------------------|-----------------|

For each DOF-ID marked BORDERLINE or UNSPECIFIED, run a sensitivity check:

```
DOF-[NN] sensitivity:
  Choice: [the specific decision the analyst made]
  Alternative: [the most defensible alternative choice]
  Effect on primary result: [ROBUST -- result classification unchanged / SENSITIVE -- classification changes / UNKNOWN]
  If SENSITIVE: [how would the result change? larger / smaller / sign flip / loses significance?]
```

**Required degrees of freedom to check** (at minimum):
- Outcome variable operationalization (how is the dependent variable measured?)
- Sample inclusion/exclusion criteria (who is in the dataset?)
- Control variable set (what is held constant?)
- Time period or sample period
- Model specification (linear vs nonlinear, additive vs multiplicative)
- Outlier handling (are any cases excluded or capped?)
- For exponential fits / ODE fitting: event list composition, anchor case selection

---

## PHASE 6 -- PRE-REGISTRATION COMPLETENESS

List every researcher degree of freedom from Phase 5 and its commitment status.

**Pre-registration register:**

| DOF-ID | Description | Status | Evidence |
|--------|-------------|--------|---------|

Status values:
- **COMMITTED**: written down in a pre-registration document, plan.md, or methods section before analysis
- **IMPLICIT**: effectively committed by the paper's method section, even if not formally pre-registered
- **UNCOMMITTED**: choice was made during or after analysis; not yet locked in writing
- **UNKNOWN**: cannot determine whether choice was made before or after seeing the data

**Commitment check** (for each UNCOMMITTED or UNKNOWN DOF):

```
DOF-[NN] commitment gap:
  What must be written: [the exact statement that would commit this choice]
  Where to write it: [plan.md / methods section / pre-registration document]
  Risk if left uncommitted: [what a skeptical reviewer (cite by name) would say]
```

---

## PHASE 7 -- VERDICT

**Null robustness verdict:**

| Verdict | Meaning |
|---------|---------|
| PUBLISHABLE-AS-IS | All claims are SIGNAL; all DOFs committed; no P1 or P2 faults |
| NEEDS-SENSITIVITY-ANALYSIS | BORDERLINE claim exists; sensitivity across DOFs must be reported |
| NEEDS-PREREGISTRATION | UNCOMMITTED DOFs exist; analysis choices must be locked in writing before results are reported |
| PARTIALLY-ROBUST | Mix of SIGNAL and BORDERLINE claims; some results solid, others need sensitivity analysis |
| FALSIFIED-BY-NULL | PATTERN-IN-NOISE: result is consistent with null; claim as stated is not supported |

State the verdict and which claims and DOFs drive it.

**Amend** -- exactly three targeted fixes ordered by severity:

Severity:
- **P1** -- falsified by null or DOF so consequential it changes the core claim
- **P2** -- uncommitted DOF that a named reviewer will flag; or borderline result needing sensitivity analysis
- **P3** -- presentation gap (null not described, procedure underspecified, but result likely robust)

1. [DOF/CL-ID] [P1/P2/P3]: [specific action -- what to write, compute, or commit]
2. [DOF/CL-ID] [P1/P2/P3]: [specific action]
3. [DOF/CL-ID] [P1/P2/P3]: [specific action]

---

Write artifact to: signals/validate/null/{{topic}}-null-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: validate-null, topic: {{topic}}, date: {{date}}, claims: [n], uncommitted_dofs: [n], verdict: [verdict]
