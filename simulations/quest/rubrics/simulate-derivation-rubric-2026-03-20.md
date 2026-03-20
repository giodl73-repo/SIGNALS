Rubric written to `simulations/quest/rubrics/simulate-derivation-rubric-2026-03-20.md`.

**Structure:**
- **5 essential** (60 pts): derivation map completeness, per-step verification blocks, APPROX flagging, fault register with P1/P2/P3 severity, artifact frontmatter
- **3 recommended** (30 pts): global soundness verdict, amend-to-fault alignment, step type classification
- **2 aspirational** (10 pts): catches faults the paper misses, expands compressed steps with interpolated intermediates

The essential criteria enforce the core contract of the skill — if the derivation map, verification blocks, or fault register are missing or incomplete, the output isn't useful regardless of everything else. C-03 (APPROX flagging) is the distinctive check that separates this skill from `simulate-argument`.
 applied, resulting expression, justification, and type (EXACT / APPROX /
  DEFINITION / PHYSICAL). Every non-trivial derivation step in the source artifact has a
  corresponding row. At least 3 rows present (or all steps if fewer than 3 exist).

---

### C-02 | Step-by-step verification block for each step
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: Each S-ID in the derivation map has a corresponding verification block
  containing: algebraic correctness verdict (YES / NO / CONDITIONAL), dimensional
  consistency check (YES / NO / NOT APPLICABLE), sign check (YES / NO), and a final
  verdict (SOUND / WEAK / BROKEN). No S-ID is skipped.

---

### C-03 | Every APPROX step is explicitly flagged
- **Category**: correctness
- **Weight**: essential
- **Pass condition**: For every step typed APPROX in the derivation map, the verification
  block states: (a) what quantity or relationship is being approximated, (b) the validity
  condition under which the approximation holds, and (c) whether the source paper states
  this approximation. If the paper has zero APPROX steps, this criterion auto-passes with
  a note confirming that fact.

---

### C-04 | Derivation Fault Register present and actionable
- **Category**: coverage
- **Weight**: essential
- **Pass condition**: A fault register table exists with columns F-ID, S-ID, verdict, type,
  description, and fix. Every step with verdict WEAK or BROKEN appears in the fault
  register. Each fault has a severity label (P1 / P2 / P3) consistent with the definitions:
  P1 = algebraically wrong, P2 = unstated approximation, P3 = notational/clarity issue.
  If no faults are found, the register explicitly states "No faults found" with a brief
  justification.

---

### C-05 | Artifact written with required frontmatter
- **Category**: format
- **Weight**: essential
- **Pass condition**: The artifact is written to `signals/simulate/derivation/` (or the
  `--output` path if provided). Frontmatter contains exactly the required fields: `skill:
  simulate-derivation`, `topic`, `date`, `steps_traced` (integer), `p1_errors` (integer),
  `unstated_approx` (integer). Values for `steps_traced`, `p1_errors`, and
  `unstated_approx` are consistent with the derivation map and fault register.

---

## Recommended Criteria (30 pts total)

### C-06 | Overall derivation soundness verdict is explicit
- **Category**: depth
- **Weight**: recommended
- **Pass condition**: The artifact states whether the derivation is globally sound — i.e.,
  whether the stated endpoint follows from the stated starting point given the steps traced.
  The verdict is one of: SOUND (all steps verified), CONDITIONALLY SOUND (all steps
  verified under stated approximations), or BROKEN (at least one P1 error blocks the
  conclusion). The verdict appears in a summary section, not buried in a step block.

---

### C-07 | Amend section maps to actual faults found
- **Category**: behavior
- **Weight**: recommended
- **Pass condition**: The AMEND section provides exactly three targeted fixes. Each fix
  references a specific F-ID from the fault register. If P1 faults exist, at least one
  fix addresses a P1. If P2 faults exist, at least one fix addresses a P2. Fixes are
  specific enough to act on (not generic advice like "check the algebra").

---

### C-08 | Step types are correctly classified
- **Category**: correctness
- **Weight**: recommended
- **Pass condition**: EXACT steps cite or sketch the algebraic identity that makes them
  exact (e.g., "product rule," "distributivity," "substitution of Eq. 3"). PHYSICAL steps
  state the physical assumption being encoded (e.g., "at equilibrium, dR/dt = 0").
  Spot-check: at least 2 randomly selected EXACT or PHYSICAL steps have traceable
  justifications; none are labeled EXACT when they contain an unexplained jump.

---

## Aspirational Criteria (10 pts total)

### C-09 | Catches at least one fault not acknowledged by the paper
- **Category**: depth
- **Weight**: aspirational
- **Pass condition**: At least one fault in the fault register identifies an error,
  unstated approximation, or dimensional inconsistency that is not already flagged or
  caveated in the source paper itself. The fault register entry notes "not acknowledged
  by paper" or equivalent.

---

### C-10 | Expands compressed steps with intermediate lines
- **Category**: depth
- **Weight**: aspirational
- **Pass condition**: At least one step in the derivation map where the paper skips an
  intermediate algebraic step is expanded — the intermediate expression is supplied
  inline or as a sub-step (S-03a, S-03b pattern), closing the logical gap between the
  paper's consecutive expressions. Each expansion is marked as "(interpolated)" to
  distinguish it from the paper's own steps.

---

## Quick Reference

| ID   | Criterion                                | Weight        | Category    |
|------|------------------------------------------|---------------|-------------|
| C-01 | Derivation map present and complete      | essential     | correctness |
| C-02 | Verification block for each step         | essential     | correctness |
| C-03 | Every APPROX step explicitly flagged     | essential     | correctness |
| C-04 | Fault register present and actionable    | essential     | coverage    |
| C-05 | Artifact with required frontmatter       | essential     | format      |
| C-06 | Overall soundness verdict explicit       | recommended   | depth       |
| C-07 | Amend maps to actual faults              | recommended   | behavior    |
| C-08 | Step types correctly classified          | recommended   | correctness |
| C-09 | Catches fault not in paper               | aspirational  | depth       |
| C-10 | Expands compressed steps                 | aspirational  | depth       |
