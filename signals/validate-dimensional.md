You are running /validate-dimensional for: {{topic}}

Check that every equation in a paper is dimensionally consistent — that the units on both sides match, that every term in a sum has the same units, and that every dimensionless quantity is truly dimensionless. Critical for physical substrate papers where EM fields, bioelectric potentials, or spectral quantities carry SI units that must be tracked.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Note: if the paper uses deliberately dimensionless variables (all quantities in [0,1]), flag this and do a dimensionlessness check instead of a units check.

---

## PHASE 2 -- DIMENSION INVENTORY

Assign dimensions to every quantity in the paper:

| Q-ID | Symbol | Quantity name | Dimensions | SI units | Source (definition, assumption, or derived) |
|------|--------|--------------|------------|----------|---------------------------------------------|
| Q-01 | E | electric field | [M·L·T⁻³·I⁻¹] | V/m | Maxwell's equations |
| Q-02 | τ | influence probability | dimensionless | — | defined in §1 as probability in [0,1] |
| Q-03 | α | adaptation rate | [T⁻¹] | s⁻¹ | from dR/dt = α·... (LHS has units [T⁻¹]) |

For dimensionless papers: verify every quantity is genuinely dimensionless and identify any hidden dimensional assumptions.

---

## PHASE 3 -- EQUATION CHECKS

For each equation, verify dimensional consistency:

```
Eq [N]: [equation]
LHS dimensions: [...]
RHS dimensions: [term 1: ..., term 2: ..., sum: ...]
Consistent? YES / NO / CONDITIONAL
If NO: [what the mismatch is and which term is wrong]
If CONDITIONAL: [what assumption is required to make it dimensionally consistent]
```

For sums (A + B + C): verify every term has the same dimensions.
For products: verify the product's dimensions match the stated quantity.
For ratios: verify the ratio is dimensionless if used as a dimensionless quantity.

Also check:
- **Exponential arguments**: the argument of e^x must be dimensionless
- **Logarithm arguments**: ln(x) requires dimensionless x
- **Trigonometric arguments**: sin(x), cos(x) require dimensionless x (or angle in radians)
- **Differential equations**: dX/dt has dimensions [X][T⁻¹] — verify α in dR/dt = α·... has units [T⁻¹]

---

## PHASE 4 -- DIMENSIONAL FAULT REGISTER

| D-ID | Equation | Fault type | Description | Severity | Fix |
|------|----------|-----------|-------------|---------|-----|
| D-01 | Eq. 3 | Unit mismatch | LHS has [V/m], RHS first term has [V/m] but second term has [V/m²] | P1 | Divide second term by characteristic length scale L |
| D-02 | Eq. 7 | Hidden dimension | α appears dimensionless but must be [T⁻¹] for dR/dt to balance | P2 | State explicitly "α has units of inverse time" |
| D-03 | Eq. 12 | Exponential argument | e^{E/k_B T}: E is in eV but k_B T is in J — inconsistent energy units | P1 | Convert both to SI joules |

Severity:
- P1: Dimensional inconsistency — the equation is physically wrong as written
- P2: Hidden dimensional assumption — the equation is correct under an unstated assumption about units
- P3: Notational ambiguity — the dimensions are consistent but the notation obscures this

---

## PHASE 5 -- AMEND

Three targeted fixes:
1. [P1 fix: the dimensional error — exact correction with units]
2. [P2 fix: the hidden assumption — what statement to add to the paper]
3. [P3 fix: notational clarification]

Write artifact to: signals/validate/dimensional/{{topic}}-dimensional-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-dimensional, topic: {{topic}}, date: {{date}}, equations_checked: [n], p1_errors: [n], dimensionless_paper: true|false
