---
name: rhythm-track
description: "Verify that dependency chains across papers in a research track are satisfied. P02 must use P01b's vector structure in the right places. Catches structural violations before submission of dependent papers."
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


You are running /rhythm-track for: {{topic}}

Verify that the dependency chain across papers in a research track is satisfied. Reads MODULE.md and the individual papers, then checks: does each paper correctly reference and use the structural results from the papers it depends on? P02 depending on P01b's vector/matrix structure should use that structure in the right places — this skill checks that it does.

---

## PHASE 1 -- MODULE SCAN

Read MODULE.md for this research program (or the track/module document specified as {{topic}}).

Extract:
- The paper dependency graph: which paper depends on which
- The structural results that propagate across papers (formulas, definitions, quantities that later papers are supposed to use)
- The quantification contracts per paper (what number each paper must deliver)

---

## PHASE 2 -- DEPENDENCY MAP

For each paper-to-paper dependency, extract what must transfer:

| D-ID | From paper | To paper | What transfers | Transfer type |
|------|-----------|---------|---------------|--------------|
| D-01 | P01 | P02 | τ = O×(1−R) formula | Definition — P02 must use this exact form |
| D-02 | P01b | P02 | Vector/matrix structure of (O, R) | Structural — P02's five states must live in this space |
| D-03 | P02 | P03 | Five equilibrium states | Initial conditions for the dynamic model |

Transfer types:
- **Definition**: P01 defines a term that all later papers must use consistently
- **Structural**: P01 establishes a mathematical framework that constrains later papers' formalism
- **Empirical**: P01 delivers a number that later papers treat as a known quantity
- **Causal**: P01 establishes a mechanism that later papers extend or apply

---

## PHASE 3 -- DEPENDENCY VERIFICATION

For each dependency in Phase 2, check the target paper:

```
D-[NN]: [From] → [To]: [what transfers]
In [target paper]:
  Is the transferred item cited? YES / NO / IMPLICITLY
  Is it used in the correct form? YES / NO / MODIFIED (describe modification)
  Is the modification justified? YES / NO / NOT ADDRESSED
  Verdict: SATISFIED / PARTIAL / VIOLATED
  If PARTIAL or VIOLATED: [exact description of the gap]
```

---

## PHASE 4 -- DEPENDENCY REGISTER

| D-ID | Verdict | Impact | What needs to change |
|------|---------|--------|---------------------|
| D-01 | SATISFIED | — | — |
| D-02 | PARTIAL | P2 — P02 uses the right variables but doesn't cite P01b explicitly | Add explicit citation "following the vector structure established in [P01b]" |
| D-03 | VIOLATED | P1 — P03's initial conditions don't match P02's five equilibrium states | Align P03 §2 to use the P02 state labels |

Severity:
- P1: A later paper contradicts or ignores a structural result from an earlier paper — breaks the track's causal chain
- P2: A dependency is used but not cited or not used in the stated form — reviewer will notice the inconsistency
- P3: A dependency is cited but could be more explicitly integrated

---

## PHASE 5 -- TRACK HEALTH

```
Track: {{topic}}
Papers checked: N
Dependencies mapped: N
P1 violations: N (must fix before submission of any dependent paper)
P2 gaps: N
Track integrity: SOUND / PARTIAL / BROKEN

Critical path to P[NN]:
  [List the dependencies that must be resolved before the next paper can be submitted]
```

---

## PHASE 6 -- AMEND

Three targeted fixes:
1. [P1 fix: the dependency violation that breaks the track — must be resolved first]
2. [P2 fix: the citation or integration gap that reviewers will notice]
3. [P3 fix: the dependency that could be more explicitly stated]

Write artifact to: signals/rhythm/track/{{topic}}-track-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/
Include frontmatter: skill: rhythm-track, topic: {{topic}}, date: {{date}}, papers_checked: [n], p1_violations: [n], track_integrity: SOUND|PARTIAL|BROKEN
