Scanning each PASS+ signal in the scorecard against all existing v6 criteria to find what isn't yet captured:

**V-01 C-22 PASS+** — "These two statements name the same contract from both sides. Both must hold." — C-22 requires bidirectional expression; the PASS+ adds a *contract declaration sentence* that names the bilateral nature explicitly. Not captured.

**V-02 C-19 PASS+** — "Pattern identification precedes citation" via column ordering. C-19 requires the column exists; this requires it to be positioned *before* File Path Evidence. Not captured.

**V-02 C-23 PASS+** — Dictionary includes "Free text is structurally invalid — unconstrained values make pattern comparison across runs unverifiable." C-23 requires enumerated labels; the PASS+ adds a named *invalidity statement* embedded in the constraint. Not captured.

**V-03 C-21 PASS+** — Full OUTPUT SCHEMA with Status column (REQUIRED / optional) for *every* column, not just evidence columns. C-21 requires evidence columns be declared required; this annotates the complete schema. Not captured.

Four new criteria → C-25 through C-28.

---

# Scoring Rubric: org-scan (v7)

## Changes from v6

Four new aspirational criteria added from R6 excellence signals. Aspirational band expands to 20 criteria.

**Scoring note**: With 20 aspirational criteria at 2 pts each the aspirational ceiling is 40 pts. Cap on aspirational contribution remains 10. A variation scoring all 20 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-25 | Inertia Match column-order enforcement: the Inertia Match column is positioned *before* File Path Evidence in the scan output schema, enforcing that pattern identification precedes evidence citation as a structural column-order constraint rather than a layout preference |
| C-26 | Dictionary invalidity statement: the Inertia pattern dictionary includes an explicit named invalidity statement (e.g., "Free text is structurally invalid — unconstrained values make pattern comparison across runs unverifiable"), embedding the consequence of non-compliance as rationale within the constraint definition |
| C-27 | Full-schema status annotation: the output schema includes a Status annotation (REQUIRED / optional) for *every* column in the schema, not just evidence columns, making compliance expectations structurally visible across the full schema rather than only at designated evidence-column declarations |
| C-28 | Bilateral contract declaration sentence: after the Phase 1 postcondition and Phase 2 precondition blocks, an explicit declaration sentence states that both blocks name the same contract from both sides and both must hold — making the contract self-documenting about its bilateral nature beyond mere bidirectional expression |

---

## Essential (60%)

**C-01** Areas named and traceable to scan evidence, not invented  
**C-02** Multi-source scan — 3+ of 7 source types cited  
**C-03** Headcount estimated as a range with supporting rationale  
**C-04** Cross-cutting concerns named with boundary note  
**C-05** Raw analysis only — no org chart, no reporting lines

## Recommended (30%)

**C-06** Team boundary candidates with seam rationale  
**C-07** Org shape named and justified from findings  
**C-08** Evidence gaps and ambiguities flagged explicitly

## Aspirational (10% cap, 2 pts each, max 10)

**C-09** 5+ specific file paths cited as auditable evidence  
**C-10** Current state vs recommended state clearly separated  
**C-11** Anti-fabrication language embedded per evidence-dependent section  
**C-12** Hard sequencing gate: scan must complete before synthesis begins  
**C-13** Critical constraint (C-05) stated twice — preamble + output format  
**C-14** Verification checklist at sequencing gate — numbered items + required confirmation sentence before synthesis proceeds  
**C-15** Structural group labels for phase separation — phases labeled as discrete named groups (e.g., GROUP A / GROUP B), not just section headings within a single flow  
**C-16** File path floor enforced as a gate condition — 5-path requirement stated as a precondition that blocks proceeding to the next phase, not just an output expectation  
**C-17** Gate confirmation token — the confirmation sentence follows a named-token format (e.g., "Gate clear — [brief summary]"), making gate passage machine-parseable rather than requiring prose interpretation  
**C-18** Gate failure output — the gate condition includes an explicit named failure-state string (e.g., "write 'Path floor not met'") that the agent outputs when the condition is unmet, making gate failures verifiable without prose inspection  
**C-19** Inertia Match column — scan output includes a per-row Inertia Match column that anchors each finding to an organizational inertia pattern, making scan evidence structured and pattern-linked rather than descriptive prose  
**C-20** Bidirectional gate token protocol block — a named `GATE TOKEN PROTOCOL` block in the preamble defines both the pass token and fail token as named constants before Phase 1 begins, making the gate protocol self-contained and referenceable throughout the skill rather than defined only at the point of use  
**C-21** Required table column enforcement — evidence columns (Inertia Match, file paths) are declared as *required* table columns in the output schema, making omissions structurally visible as empty cells rather than silently absent from prose narrative  
**C-22** Formal phase contract — the gate is expressed bidirectionally as the postcondition of Phase 1 *and* the precondition of Phase 2, naming both sides of the contract explicitly so the phase boundary is verifiable in either direction, not just a unidirectional sequencing rule  
**C-23** Inertia pattern dictionary — the Inertia Match column is constrained by a named pattern dictionary (enumerated valid values with labels) embedded in the skill before Phase 1 begins, preventing free-text entry that would make pattern-linkage structurally unverifiable  
**C-24** Self-documenting pass token — the pass token includes explicit acknowledgment of the key conditions verified (e.g., source count, path floor status, dominant pattern name), making the token self-reporting about what it asserts rather than a bare named signal of passage  
**C-25** Inertia Match column-order enforcement — the Inertia Match column is positioned *before* File Path Evidence in the scan output schema, enforcing that pattern identification precedes evidence citation as a structural column-order constraint rather than a layout preference  
**C-26** Dictionary invalidity statement — the Inertia pattern dictionary includes an explicit named invalidity statement (e.g., "Free text is structurally invalid — unconstrained values make pattern comparison across runs unverifiable"), embedding the consequence of non-compliance as rationale within the constraint definition itself  
**C-27** Full-schema status annotation — the output schema includes a Status annotation (REQUIRED / optional) for *every* column in the schema, not just evidence columns, making compliance expectations structurally visible across the full schema rather than only at designated evidence-column declarations  
**C-28** Bilateral contract declaration sentence — after the Phase 1 postcondition and Phase 2 precondition blocks, an explicit declaration sentence states that both blocks name the same contract from both sides and both must hold, making the contract self-documenting about its bilateral nature beyond mere bidirectional expression

---

## Composite Score Formula

```
aspirational_pts = sum of passing aspirational criteria × 2
aspirational_contribution = min(aspirational_pts, 10)

composite = (essential_pass / 5 × 60)
          + (recommended_pass / 3 × 30)
          + (aspirational_contribution)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.
