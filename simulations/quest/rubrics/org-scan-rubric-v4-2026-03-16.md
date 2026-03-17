Looking at the R3 scorecard, I can extract two new patterns from what V-01 and V-03 demonstrate beyond v3 criteria:

- **V-01 C-14 evidence**: confirmation sentence uses a named-token format `"Gate clear — ..."` — not just any sentence, but a templated string making gate passage machine-parseable
- **V-03 C-16 evidence**: gate includes explicit failure output `"write 'Path floor not met'"` — a named string the agent writes when the condition is unmet, making gate failures verifiable without prose inspection

These are C-17 and C-18. Here is the complete v4 rubric:

---

# Scoring Rubric: org-scan (v4)

## Changes from v3

Two new aspirational criteria added from R3 excellence signals. Aspirational band expands to 10 criteria.

**Scoring note**: With 10 aspirational criteria at 2 pts each the aspirational ceiling is 20 pts. Cap the aspirational contribution at 10 in the composite formula — a variation scoring all 10 still earns 10, not 20.

| New Criterion | Source Signal |
|---|---|
| C-17 | Gate confirmation token: the confirmation sentence follows a named-token format (e.g., "Gate clear — [brief summary]"), making gate passage machine-parseable, not just natural-language confirmation |
| C-18 | Gate failure output: the gate condition includes an explicit named failure-state string the agent writes when the condition is unmet (e.g., "write 'Path floor not met'"), making gate failures verifiable without prose inspection |

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

**C-14** (from v3): C-12 requires a hard gate; C-14 requires that gate to include a verification checklist and a mandatory confirmation sentence. V-04 shows this pattern: a STOP checkpoint with 5 enumerated conditions the agent must confirm before synthesis begins. This is the difference between a rule and a protocol.

**C-15** (from v3): C-10 requires current/recommended to be separated; C-15 requires that separation to be expressed as labeled structural groups (GROUP A / GROUP B). V-02 shows this pattern: named group headers that make the structural boundary explicit and machine-readable, not just prose-level.

**C-16** (from v3): C-09 requires 5+ paths to appear in output; C-16 requires the 5-path floor to be stated as a proceed-or-stop gate — a condition the agent checks before moving forward. V-02 shows this as "A-1 gate condition." The distinction: C-09 measures presence, C-16 measures enforcement posture.

**C-17** (new): C-14 requires a confirmation sentence; C-17 requires that sentence to follow a named-token format ("Gate clear — ..."). V-01 shows this: the sentence isn't natural-language prose but a parseable token with a fixed prefix. The distinction: C-14 measures existence of a confirmation, C-17 measures whether that confirmation is machine-readable.

**C-18** (new): C-16 requires a proceed-or-stop gate; C-18 requires the gate to include an explicit named output for the failure path. V-03 shows this: "write 'Path floor not met'" — a string the agent emits when the condition is unmet. The distinction: C-16 measures whether the gate blocks, C-18 measures whether the gate's failure state is named and verifiable.
