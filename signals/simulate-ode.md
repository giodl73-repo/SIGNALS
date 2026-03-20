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

**Method**: Compute the Jacobian matrix J = ∂f/∂x evaluated at the fixed point. Find eigenvalues λ of J. Classify based on eigenvalue sign and type.

**Stability classification table:**

| FP-ID | Jacobian J at FP | Eigenvalues λ | Classification | Physical meaning |
|-------|-----------------|---------------|----------------|------------------|

**Classification rules:**

For 1D systems (single state variable):
- λ < 0: STABLE NODE (globally attracting if no other fixed points in domain)
- λ > 0: UNSTABLE NODE (repelling)
- λ = 0: NON-HYPERBOLIC (use higher-order analysis or numerical check)

For 2D systems:
- Both λ real, same sign negative: STABLE NODE
- Both λ real, same sign positive: UNSTABLE NODE
- λ real, opposite signs: SADDLE POINT
- λ complex with Re(λ) < 0: STABLE SPIRAL
- λ complex with Re(λ) > 0: UNSTABLE SPIRAL
- λ purely imaginary: CENTER (neutrally stable -- requires higher-order verification)

For n > 2: report all n eigenvalues; classify as STABLE if all Re(λ) < 0, UNSTABLE if any Re(λ) > 0, SADDLE if mixed signs on real parts.

**Stability verification** (for each FP):

```
FP-[NN] stability:
  Jacobian: [J matrix or scalar dF/dX for 1D]
  Eigenvalue(s): [λ = expression]
  Sign analysis: [is Re(λ) < 0, > 0, or 0?]
  Classification: [STABLE NODE / UNSTABLE NODE / SADDLE / STABLE SPIRAL / UNSTABLE SPIRAL / CENTER / NON-HYPERBOLIC]
  Oscillations possible? [YES (complex eigenvalues) / NO (real eigenvalues)]
```

---

## PHASE 4 -- BIFURCATION ANALYSIS

Identify parameters where the number or stability of fixed points changes.

**Method**: A bifurcation occurs when an eigenvalue crosses zero (for real eigenvalues) or the real part crosses zero (for complex eigenvalues). Find the parameter value(s) where this happens.

**Bifurcation scan** -- for each parameter P-ID:
- Fix all other parameters at estimated values
- Vary P-ID from 0 to its maximum plausible value
- Does the number of fixed points change? Does any eigenvalue cross zero?

**Bifurcation register:**

| B-ID | Parameter | Bifurcation value | Type | Effect |
|------|-----------|------------------|------|--------|

**Bifurcation types:**
- **SADDLE-NODE**: two fixed points collide and annihilate; system jumps to distant attractor
- **TRANSCRITICAL**: two fixed points exchange stability as they pass through each other
- **PITCHFORK (supercritical)**: one stable fixed point splits into two stable + one unstable
- **PITCHFORK (subcritical)**: one stable fixed point merges with two unstable, destabilizes
- **HOPF**: stable spiral becomes unstable spiral; limit cycle born
- **NONE IDENTIFIED**: if eigenvalues do not cross zero for any parameter in the physical range

If no bifurcation exists in the physical range: state this explicitly and explain why (e.g., "eigenvalue is always negative in physical parameter range").

---

## PHASE 5 -- PHASE PORTRAIT DESCRIPTION

Describe the geometry of state space without computing numerical trajectories.

**For each region of state space** (based on fixed points and their basins):

```
Region [name]:
  Boundaries: [what separates this region from adjacent regions]
  Attractor: [which fixed point or limit cycle trajectories converge to]
  Basin of attraction: [parameter conditions that place the system in this region]
  Separatrix: [the boundary curve between competing basins, if any]
```

**Limit cycles**: If a Hopf bifurcation was identified in Phase 4, describe the expected limit cycle: approximate period, amplitude relative to fixed point, and parameter regime where it exists.

**Phase portrait summary**: one paragraph describing the qualitative picture -- how many attractors, how many basins, whether transitions between basins are continuous or discontinuous (jumps).

---

## PHASE 6 -- BOUNDARY BEHAVIOR

Check behavior at every boundary of the state and parameter space.

For each state variable and each parameter, check the limit as the quantity approaches its minimum and maximum value.

| Limit | Expression | Behavior | Physical interpretation |
|-------|-----------|----------|------------------------|

**Required limits** (at minimum, check these):
- Each state variable → 0
- Each state variable → maximum (X_max or domain boundary)
- Each control input → 0 (pure off case)
- Each control input → 1 or maximum (pure on case)
- Rate parameters α, β → 0 (frozen dynamics)
- Rate parameters α, β → ∞ (infinitely fast dynamics)

**Consistency check**: Do the boundary limits match the paper's qualitative claims about limiting regimes (e.g., "pure cooperation leads to R*=R_max")? Mark each: CONSISTENT / INCONSISTENT / NOT STATED.

---

## PHASE 7 -- TIMESCALE VERIFICATION

Verify that the estimated parameter values reproduce the empirical anchor cases cited in the paper.

**Timescale formula**: For a 1D stable system near a fixed point, the characteristic convergence time is τ = 1/|λ| where λ is the eigenvalue at the fixed point.

For each empirical anchor case cited in the paper:

```
Anchor [name]:
  Claim: [paper's claim about timescale or convergence rate]
  Parameters used: [values substituted]
  Computed τ or rate: [result]
  Within stated error? YES / NO / NOT CHECKABLE
  If NO: [discrepancy -- computed vs claimed]
```

If no empirical anchor cases are cited: state "No anchor cases cited -- timescale verification not applicable."

---

## PHASE 8 -- PHYSICAL CONSISTENCY CHECK

Verify that the mathematical structure matches the paper's qualitative claims.

For each qualitative claim in the paper about the model's behavior:

```
Claim [C-ID]: "[exact quote or paraphrase]"
  Mathematical basis: [which fixed point, eigenvalue, or boundary behavior supports or contradicts this]
  Verdict: CONFIRMED / CONTRADICTED / UNDERDETERMINED
  If CONTRADICTED: [what the math actually implies vs what the paper claims]
  If UNDERDETERMINED: [what additional analysis would resolve it]
```

**Required checks** (at minimum):
- Does the paper claim the system has a unique equilibrium? Check Phase 2.
- Does the paper claim monotone convergence (no oscillations)? Check Phase 3 eigenvalue type.
- Does the paper claim a phase transition at some threshold? Check Phase 4.
- Does the paper describe qualitatively different regimes? Check Phase 5 basin structure.

---

## PHASE 9 -- FAULT REGISTER AND VERDICT

**Fault register:**

| F-ID | Phase | Severity | Description | Fix |
|------|-------|----------|-------------|-----|

Severity:
- **P1** -- mathematical error (wrong fixed point, wrong stability classification, wrong bifurcation type)
- **P2** -- claim inconsistency (paper asserts behavior that contradicts the math)
- **P3** -- missing check (analysis incomplete, not necessarily wrong)

**Dynamical Systems Verdict:**

| Verdict | Meaning |
|---------|---------|
| WELL-POSED | Fixed points found, stability classified, no P1 or P2 faults |
| CONDITIONALLY WELL-POSED | System is well-posed under stated parameter constraints |
| ILL-POSED | P1 fault: fixed point algebra wrong, stability misclassified, or bifurcation type incorrect |
| CLAIM MISMATCH | P2 fault: math contradicts paper's qualitative claims |

State the verdict and cite supporting findings.

**Amend** -- exactly three targeted fixes ordered by severity (P1 first, then P2, then P3):

1. [F-ID] [P1/P2/P3]: [specific correction]
2. [F-ID] [P1/P2/P3]: [specific correction]
3. [F-ID] [P1/P2/P3]: [specific correction]

If fewer than three faults exist, use remaining slots for P3 clarity improvements.

---

Write artifact to: signals/simulate/ode/{{topic}}-ode-{{date}}.md
If --output <path> provided: write flat into <path>/
Frontmatter: skill: simulate-ode, topic: {{topic}}, date: {{date}}, fixed_points: [n], p1_faults: [n], claim_mismatches: [n], verdict: [verdict]
