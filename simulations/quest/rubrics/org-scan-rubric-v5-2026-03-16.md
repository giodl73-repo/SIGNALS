Scanning the R4 scorecard for patterns beyond v4 criteria:

1. **V-03 structural note** (explicitly flagged): "Inertia Match column is a new per-row evidence discipline not captured in any current criterion." Per-row column anchoring each scan finding to an organizational inertia pattern — not just citation, but pattern-linkage.

2. **V-04 axis**: `GATE TOKEN PROTOCOL` named block in the preamble defines **both** pass and fail tokens as named constants *before Phase 1 begins* — a step beyond C-17/C-18 (which require the tokens to exist at the gate) toward a formal protocol block that makes both tokens referenceable throughout the skill from the start.

These become C-19 and C-20.

---

# Scoring Rubric: org-scan (v5)

## Changes from v4

Two new aspirational criteria added from R4 excellence signals. Aspirational band expands to 12 criteria.

**Scoring note**: With 12 aspirational criteria at 2 pts each the aspirational ceiling is 24 pts. Cap the aspirational contribution at 10 in the composite formula — a variation scoring all 12 still earns 10, not 24.

| New Criterion | Source Signal |
|---|---|
| C-19 | Inertia Match column: scan output includes a per-row Inertia Match column anchoring each finding to an organizational inertia pattern, making scan evidence pattern-linked rather than descriptive prose |
| C-20 | Bidirectional gate token protocol block: a named `GATE TOKEN PROTOCOL` block in the preamble defines both pass token and fail token as named constants before Phase 1 begins, making the gate protocol self-contained and referenceable throughout the skill |

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

**C-17** (from v4): C-14 requires a confirmation sentence; C-17 requires that sentence to follow a named-token format ("Gate clear — ..."). V-01/R3 shows this: the sentence isn't natural-language prose but a parseable token with a fixed prefix. The distinction: C-14 measures existence of a confirmation, C-17 measures whether that confirmation is machine-readable.

**C-18** (from v4): C-16 requires a gate condition; C-18 requires that condition to produce a named failure-state string when unmet. V-03/R3 shows this: "write 'Path floor not met'" — an exact string the agent outputs, not a prose description of failure. The distinction: C-16 measures whether the floor is enforced, C-18 measures whether failure is machine-verifiable.

**C-19** (new): Beyond citing file paths (C-09) or separating phases (C-10), C-19 requires each scan row to carry an Inertia Match column linking the finding to an organizational inertia pattern. V-03/R4 shows this as a structural discipline: evidence is not just cited, it is pattern-anchored at the row level, making the scan output directly useful for org design reasoning.

**C-20** (new): C-17 and C-18 require the pass and fail tokens to exist; C-20 requires both to be defined together in a named protocol block in the preamble, before Phase 1. V-04/R4 shows this as `GATE TOKEN PROTOCOL`: both constants declared upfront so every subsequent reference is to a pre-defined term, not an inline string. The distinction: C-17/C-18 measure token existence at the gate, C-20 measures whether the token contract is established before the skill begins.
