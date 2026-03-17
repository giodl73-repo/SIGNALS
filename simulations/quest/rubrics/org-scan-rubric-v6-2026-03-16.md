Scanning the scorecard for excellence signals not captured in any v5 criterion:

1. **V-02 C-19 PASS+** (explicitly flagged stronger): "Table-enforced: empty cell is visible gap, not hidden prose." The Inertia Match column isn't just present — it's a *required table column*, so omissions surface as structural voids rather than silent prose gaps. That's a new enforcement posture beyond C-19 (which only requires the column exists).

2. **V-04 axis**: Gate expressed as *postcondition of Phase 1 = precondition of Phase 2* — a formal bidirectional phase contract, not just a sequencing rule. C-12 requires a hard gate; this requires the gate to be expressed in contract-theoretic terms (both sides named).

3. **V-03 C-19 PARTIAL risk**: The named pattern dictionary is what makes C-19 verifiable. Without it, the column is present but unconstrained — free text masquerading as structured data. The dictionary is a separate criterion from the column.

4. **V-02 pass token enhancement**: `SCAN GATE CLEAR — … path floor: met` — the token includes explicit acknowledgment of *what was verified*, not just a named signal of passage. C-17 requires a named token; this requires the token to be self-documenting about the conditions it asserts.

These become C-21 through C-24.

---

# Scoring Rubric: org-scan (v6)

## Changes from v5

Four new aspirational criteria added from R5 excellence signals. Aspirational band expands to 16 criteria.

**Scoring note**: With 16 aspirational criteria at 2 pts each the aspirational ceiling is 32 pts. Cap on aspirational contribution remains 10. A variation scoring all 16 still earns 10.

| New Criterion | Source Signal |
|---|---|
| C-21 | Required table column enforcement: evidence columns (Inertia Match, file paths) are declared as *required* table columns, making omissions structurally visible as empty cells rather than silently absent from prose |
| C-22 | Formal phase contract: the gate is expressed bidirectionally as the postcondition of Phase 1 *and* the precondition of Phase 2, making the phase boundary a verifiable contract rather than a prose sequencing instruction |
| C-23 | Inertia pattern dictionary: the Inertia Match column is constrained by a named pattern dictionary (enumerated valid values) embedded in the skill before Phase 1 begins, preventing free-text entry that would make pattern-linkage unverifiable |
| C-24 | Self-documenting pass token: the pass token includes explicit acknowledgment of the key conditions verified (e.g., source count, path count, dominant pattern), making the token self-reporting rather than a bare named signal of passage |

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

---

## Design Notes

**C-11/C-12/C-13** (from v2): These three explain the 15-point gap between V-01 (95) and a bare-essential pass. A skill with all three is structurally harder to violate than one without them.

**C-14** (from v3): C-12 requires a hard gate; C-14 requires that gate to include a verification checklist and a mandatory confirmation sentence. V-04/R3 shows this pattern: a STOP checkpoint with 5 enumerated conditions the agent must confirm before synthesis begins. This is the difference between a rule and a protocol.

**C-15** (from v3): C-10 requires current/recommended to be separated; C-15 requires that separation to be expressed as labeled structural groups (GROUP A / GROUP B). V-02/R3 shows this pattern: named group headers that make the structural boundary explicit and machine-readable, not just prose-level.

**C-16** (from v3): C-09 requires 5+ paths to appear in output; C-16 requires the 5-path floor to be stated as a proceed-or-stop gate — a condition the agent checks before moving forward. V-02/R3 shows this as "A-1 gate condition." The distinction: C-09 measures presence, C-16 measures enforcement posture.

**C-19/C-21/C-23** (from v5/v6): Three layered criteria on the Inertia Match pattern. C-19 requires the column exists. C-21 requires the column is declared *required* in the output schema so omissions are structurally visible. C-23 requires the column is constrained by an enumerated dictionary so entries are verifiable. A skill can satisfy C-19 without C-21 (column present but optional) or without C-23 (column present but free-text).

**C-17/C-24** (from v5/v6): Two layered criteria on the pass token. C-17 requires a named token format. C-24 requires the token to include explicit attestation of the conditions it verified. A skill can satisfy C-17 with a bare `SCAN GATE CLEAR` while failing C-24 if the token carries no embedded evidence summary.

**C-12/C-22** (from v5/v6): Two layered criteria on sequencing. C-12 requires a hard gate (unidirectional: scan before synthesis). C-22 requires the gate to be expressed as a formal contract naming both the Phase 1 postcondition and the Phase 2 precondition. The distinction: C-12 is a rule; C-22 is a contract.
