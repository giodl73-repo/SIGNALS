---
name: simulate-ode
description: "Qualitative dynamical systems analysis for ODE models. Fixed points, stability classification (STABLE NODE/SADDLE/SPIRAL), bifurcation identification, phase portrait, boundary behavior, timescale verification against empirical anchors."
allowed-tools: [Read, Write, Glob]
param_set: lean
---

You are running /simulate-ode for: {{topic}}

Perform qualitative dynamical systems analysis on an ODE model -- fixed points, stability classification, bifurcation identification, phase portrait description, boundary behavior, timescale verification, and physical consistency check.

**Before you begin**: read the paper or draft artifact for {{topic}}. If simulate-derivation or discover-limiting-cases artifacts exist, read those -- they provide the algebraic grounding this skill builds on. Identify every state variable, every parameter, and the claimed qualitative behavior. That is all the acquisition you need.

---

## PHASE 1 -- ODE SYSTEM ACQUISITION

Parse the ODE system from the paper. Produce a system registry.

**State variable registry:**

| V-ID | Symbol | Name | Domain | Boundary conditions |
|------|--------|------|--------|---------------------|

**Parameter registry:**

| P-ID | Symbol | Name | Units | Estimated value | Source |
|------|--------|------|-------|-----------------|--------|

**Equation registry:**

| E-ID | Equation | Coupled to |
|------|----------|------------|

**System classification:**
- Dimension (n = number of state variables):
- Autonomous? (no explicit time dependence): YES / NO
- Linear? YES / NO / PIECEWISE
- Control inputs (externally driven parameters treated as inputs): list or NONE

State the system in standard form: dx/dt = f(x, p) where x is the state vector and p is the parameter vector.

---

## PHASE 2 -- FIXED POINT ANALYSIS

For each fixed point, set all derivatives to zero and solve analytically.

**Method**: Set dx/dt = 0 for all state variables simultaneously. Solve the resulting algebraic system.

For each fixed point FP-NN:

```
FP-[NN]: [name or description]

Derivation:
  Setting [dX/dt] = 0: [equation]
  [algebraic steps...]
  Result: [X* = expression in parameters]

Domain check:
  Is FP-[NN] in the valid domain (per V-ID boundary conditions)? YES / CONDITIONAL / NO
  If CONDITIONAL: [state the parameter condition]

Physical interpretation:
  What state does this equilibrium represent?
  [one sentence -- what is the system doing at this fixed point?]
```

If no closed-form solution exists: state why and describe the fixed point numerically using the estimated parameter values from Phase 1.

Minimum: identify all fixed points, including boundary cases (e.g., X* = 0, X* = X_max).

---

## PHASE 3 -- STABILITY ANALYSIS

For each fixed point from Phase 2, classify the stability type.

**Method**: Compute the Jacobian matrix J = df/dx evaluated at the fixed point. Find eigenvalues lambda of J. Classify based on eigenvalue sign and type.

**Stability classification table:**

| FP-ID | Jacobian J at FP | Eigenvalues lambda | Classification | Physical meaning |
|-------|-----------------|---------------|----------------|------------------|

**Classification rules:**

For 1D systems (single state variable):
- lambda < 0: STABLE NODE
- lambda > 0: UNSTABLE NODE
- lambda = 0: NON-HYPERBOLIC (use higher-order analysis or numerical check)

For 2D systems:
- Both lambda real, same sign negative: STABLE NODE
- Both lambda real, same sign positive: UNSTABLE NODE
- lambda real, opposite signs: SADDLE POINT
- lambda complex with Re(lambda) < 0: STABLE SPIRAL
- lambda complex with Re(lambda) > 0: UNSTABLE SPIRAL
- lambda purely imaginary: CENTER

For n > 2: report all n eigenvalues; classify as STABLE if all Re(lambda) < 0, UNSTABLE if any Re(lambda) > 0, SADDLE if mixed.

**Stability verification** (for each FP):

```
FP-[NN] stability:
  Jacobian: [J matrix or scalar dF/dX for 1D]
  Eigenvalue(s): [lambda = expression]
  Sign analysis: [is Re(lambda) < 0, > 0, or 0?]
  Classification: [type]
  Oscillations possible? [YES (complex eigenvalues) / NO (real eigenvalues)]
```

---

## PHASE 4 -- BIFURCATION ANALYSIS

Identify parameters where the number or stability of fixed points changes.

**Method**: A bifurcation occurs when an eigenvalue crosses zero (real) or the real part crosses zero (complex). Find the parameter value(s) where this happens.

**Bifurcation register:**

| B-ID | Parameter | Bifurcation value | Type | Effect |
|------|-----------|------------------|------|--------|

Types: SADDLE-NODE / TRANSCRITICAL / PITCHFORK-SUPERCRITICAL / PITCHFORK-SUBCRITICAL / HOPF / NONE IDENTIFIED

If no bifurcation exists in the physical range: state this explicitly with the eigenvalue argument.

---

## PHASE 5 -- PHASE PORTRAIT DESCRIPTION

Describe the geometry of state space without computing numerical trajectories.

**For each region of state space:**

```
Region [name]:
  Boundaries: [what separates this region]
  Attractor: [which fixed point or limit cycle]
  Basin of attraction: [parameter conditions]
  Separatrix: [boundary curve between competing basins, if any]
```

**Phase portrait summary**: one paragraph describing the qualitative picture -- how many attractors, how many basins, whether transitions are continuous or discontinuous.

---

## PHASE 6 -- BOUNDARY BEHAVIOR

| Limit | Expression | Behavior | Physical interpretation |
|-------|-----------|----------|------------------------|

Required limits (at minimum):
- Each state variable -> 0 and -> maximum
- Each control input -> 0 and -> 1 or maximum
- Rate parameters -> 0 and -> infinity

Mark each against paper claims: CONSISTENT / INCONSISTENT / NOT STATED.

---

## PHASE 7 -- TIMESCALE VERIFICATION

For 1D stable systems: characteristic convergence time is tau = 1/|lambda|.

For each empirical anchor case cited in the paper:

```
Anchor [name]:
  Claim: [paper's timescale claim]
  Parameters used: [values]
  Computed tau or rate: [result]
  Within stated error? YES / NO / NOT CHECKABLE
  If NO: [discrepancy]
```

If no anchor cases cited: "No anchor cases cited -- timescale verification not applicable."

---

## PHASE 8 -- PHYSICAL CONSISTENCY CHECK

For each qualitative claim in the paper about model behavior:

```
Claim [C-ID]: "[quote or paraphrase]"
  Mathematical basis: [which fixed point, eigenvalue, or boundary behavior]
  Verdict: CONFIRMED / CONTRADICTED / UNDERDETERMINED
  If CONTRADICTED: [math vs paper]
  If UNDERDETERMINED: [what resolves it]
```

---

## PHASE 9 -- FAULT REGISTER AND VERDICT

| F-ID | Phase | Severity | Description | Fix |
|------|-------|----------|-------------|-----|

Severity: P1 (math error) / P2 (claim mismatch) / P3 (missing check)

**Verdict**: WELL-POSED / CONDITIONALLY WELL-POSED / ILL-POSED / CLAIM MISMATCH

**Amend** (3 fixes, P1 first):
1. [F-ID] [P1/P2/P3]: [correction]
2. [F-ID] [P1/P2/P3]: [correction]
3. [F-ID] [P1/P2/P3]: [correction]

---

Write artifact to: signals/simulate/ode/{{topic}}-ode-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-ode, topic: {{topic}}, date: {{date}}, fixed_points: [n], p1_faults: [n], claim_mismatches: [n], verdict: [verdict]
