---
name: validate-consistency
description: "Check that every numbered equation, quantitative claim, and result in a paper is mutually consistent. Catches value mismatches (7.4% vs 11.3%), equation disagreements, and violated boundary conditions."
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /validate-consistency for: {{topic}}

Check that every numbered equation, claim, and quantitative result in a paper is mutually consistent. Catches the class of error where the same quantity appears with different values in different places, or where two equations that must agree (e.g. a static limit and a dynamic equation at equilibrium) do not.

---

## PHASE 1 -- SIGNAL ACQUISITION

Read the paper or draft artifact for {{topic}}.
Also read any prior signals: specify-spec, simulate-contract, simulate-argument.

---

## PHASE 2 -- QUANTITY REGISTRY

Extract every named quantity, equation, and quantitative result into a registry.

| Q-ID | Name | Value / Form | Location (section, equation number, table, abstract) |
|------|------|-------------|-----------------------------------------------------|
| Q-01 | [quantity name] | [value or symbolic form] | §2, Eq. 3 |
| Q-02 | [same quantity] | [possibly different value] | §4, Table 1 |

Flag any quantity that appears in more than one location for cross-checking in Phase 3.

Also register:
- All equations with explicit left-hand and right-hand sides
- All numerical values stated in text, tables, and abstract
- All inequalities or boundary conditions that constrain quantities
- All claims of the form "reduces to X in the limit Y"

---

## PHASE 3 -- CONSISTENCY CHECKS

### 3A — Value Consistency
For every quantity that appears in more than one location: do the values agree?

| C-ID | Quantity | Location A | Value A | Location B | Value B | Consistent? |
|------|----------|-----------|---------|-----------|---------|-------------|
| C-01 | MAPE | §3 Table 1 | 7.4% | Abstract | 11.3% | FAIL |

### 3B — Equation Consistency
For every pair of equations that describe the same quantity or relationship: are they algebraically equivalent?

| C-ID | Eq A | Eq B | Relationship | Consistent? | If FAIL: what diverges |
|------|------|------|-------------|-------------|------------------------|
| C-02 | Eq. 3 static formula | Eq. 7 at dR/dt=0 | Eq 7 should reduce to Eq 3 at equilibrium | PASS/FAIL | |

### 3C — Boundary / Limit Consistency
For every equation with stated boundary conditions or limiting cases: do they hold?

| C-ID | Equation | Boundary condition | Holds? | If FAIL: what the equation actually gives |
|------|----------|-------------------|--------|------------------------------------------|

### 3D — Sign and Direction Consistency
For any quantity with a stated sign (positive feedback, negative correlation, etc.): is the sign consistent across all uses?

---

## PHASE 4 -- INCONSISTENCY REGISTER

| I-ID | Type | What conflicts | Severity | Fix required |
|------|------|---------------|---------|-------------|
| I-01 | Value | MAPE 7.4% vs 11.3% | P1 — reject condition | Correct one value and verify which is right |

Severity:
- P1: Different values for the same quantity, or two equations that provably disagree — reject condition at any journal
- P2: Ambiguous notation used for different quantities — confuses reviewers but doesn't falsify the result
- P3: Minor inconsistency in framing or rounding that doesn't affect the argument

---

## PHASE 5 -- AMEND

Three targeted fixes ordered by severity:
1. [P1 fix: the inconsistency most likely to trigger rejection]
2. [P2 fix: ambiguous notation or framing that needs disambiguation]
3. [P3 fix: rounding or presentation consistency]

Write artifact to: signals/validate/consistency/{{topic}}-consistency-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: validate-consistency, topic: {{topic}}, date: {{date}}, p1_count: [n], p2_count: [n], quantities_checked: [n]
