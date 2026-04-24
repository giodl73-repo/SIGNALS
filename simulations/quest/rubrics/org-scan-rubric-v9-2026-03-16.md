# Scoring Rubric: org-scan (v9)

## Changes from v8

Three new aspirational criteria added from R8 excellence signals. Aspirational band expands to 27 criteria.

**Scoring note**: With 27 aspirational criteria at 2 pts each the aspirational ceiling is 54 pts. Cap on aspirational contribution remains 10. A variation scoring all 27 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-33 | Named gate entry condition: the gate requires a named phase-completion statement to be written before checklist evaluation can begin, enforcing sequential constraint on gate entry itself rather than only within the gate checklist items |
| C-34 | Dual-register inertia dictionary: the Inertia pattern dictionary includes a Behavioral Signals column alongside structural code-pattern entries, adding human-observable behavioral tells so the dictionary is verifiable by both code inspection and team observation |
| C-35 | Hypothesis confirmation tracking column: the scan output schema includes a `Hypothesis Held` column (yes / no / partial vocabulary) that links each scan row to a prior Phase 1 prediction, and the gap table includes a "prediction not resolved" gap type, forming a complete machine-verifiable hypothesis-test-result loop |

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
**C-29** Schema violation label — the column-order constraint includes an explicit named violation label (e.g., "Inverting the order is a schema violation"), making constraint violations identifiable by output inspection rather than requiring prose interpretation of whether the constraint was breached  
**C-30** Universal schema governing statement — the output schema opens with a single governing statement asserting that Status applies to every column across all tables (e.g., "This schema governs every table in this skill. Status applies to every column."), establishing universal applicability structurally rather than relying on per-table annotations alone  
**C-31** Named phase boundary header — the gate is introduced with a named phase boundary label (e.g., "PHASE 1 / PHASE 2 BOUNDARY: GATE EVALUATION:") that makes the boundary a structurally identifiable named element, not just a hard sequencing transition, enabling the gate location to be found by structural scanning rather than prose reading  
**C-32** Sequential evaluation enforcement — the gate checklist includes an explicit instruction to evaluate items in order without skipping (e.g., "evaluate each item in order; do not skip"), making checklist execution sequential and verifiable as a stated constraint beyond merely being a numbered list  
**C-33** Named gate entry condition — the gate requires a named phase-completion statement to be written before checklist evaluation begins (e.g., a SCANNER COMPLETE declaration or equivalent), enforcing sequential constraint on gate entry itself rather than only within the checklist items, adding a pre-gate checkpoint that is structurally distinct from in-checklist sequential enforcement  
**C-34** Dual-register inertia dictionary — the Inertia pattern dictionary includes a Behavioral Signals column alongside structural code-pattern entries (e.g., team language, leadership framing, incident response patterns), adding human-observable behavioral tells so each pattern is verifiable by both code inspection and team observation rather than code evidence alone  
**C-35** Hypothesis confirmation tracking column — the scan output schema includes a `Hypothesis Held` column (constrained vocabulary: yes / no / partial) that links each scan row to a prior Phase 1 prediction, and the gap table includes a "prediction not resolved" gap type, forming a complete machine-verifiable hypothesis-test-result loop across prediction, evidence, and outcome

---

## Composite Score Formula

```
aspirational_pts = sum of passing aspirational criteria × 2
aspirational_contribution = min(aspirational_pts, 10)

score = essential_score + recommended_score + aspirational_contribution
```

**Essential ceiling**: 60 pts (5 criteria × 12 pts each)  
**Recommended ceiling**: 30 pts (3 criteria × 10 pts each)  
**Aspirational ceiling**: 10 pts (cap; 27 criteria × 2 pts = 54 raw, capped at 10)  
**Perfect score**: 100
