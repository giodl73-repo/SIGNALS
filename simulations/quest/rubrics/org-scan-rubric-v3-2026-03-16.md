Looking at the R2 scorecard, I need to find patterns that pushed variations beyond current criteria — things scoring distinctions revealed but v2 doesn't yet capture as criteria.

**New patterns from R2:**

| Source | Pattern | Distinction |
|---|---|---|
| V-04 C-12 (PASS) | STOP gate + numbered checklist + required confirmation sentence | C-12 only requires a "hard gate" — V-04 adds checklist + forced confirmation |
| V-02 C-10 (PASS) | GROUP A: CURRENT STATE / GROUP B: RECOMMENDED STATE structural labels | C-10 only requires "clearly separated" — V-02 adds labeled structural groups |
| V-02 C-09 (PASS) | 5-path floor stated as a gate condition blocking next phase | C-09 only requires paths to be cited — V-02 enforces it as a proceed-or-stop gate |

---

# Scoring Rubric: org-scan (v3)

## Changes from v2

Three new aspirational criteria added from R2 excellence signals. Aspirational band expands to 8 criteria — weight per criterion adjusts to maintain 10% total (now ~1.25 pts each; scoring simplification: treat each as 1 pt + pool rounding, or keep 2 pts and cap at 10).

**Scoring note**: With 8 aspirational criteria at 2 pts each the aspirational ceiling is 16 pts. Cap the aspirational contribution at 10 in the composite formula — a variation scoring all 8 still earns 10, not 16.

| New Criterion | Source Signal |
|---|---|
| C-14 | Verification checklist at the sequencing gate: numbered items + required confirmation sentence before synthesis begins |
| C-15 | Structural group labels for phase separation: GROUP A: CURRENT STATE / GROUP B: RECOMMENDED STATE (or equivalent labeled groups), not just section headings |
| C-16 | File path floor enforced as a gate condition: 5-path requirement stated as a precondition that blocks proceeding, not just an output expectation |

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

**C-14** (new): C-12 requires a hard gate; C-14 requires that gate to include a verification checklist and a mandatory confirmation sentence. V-04 shows this pattern: a STOP checkpoint with 5 enumerated conditions the agent must confirm before synthesis begins. This is the difference between a rule and a protocol.

**C-15** (new): C-10 requires current/recommended to be separated; C-15 requires that separation to be expressed as labeled structural groups (GROUP A / GROUP B). V-02 shows this pattern: named group headers that make the structural boundary explicit and machine-readable, not just prose-level.

**C-16** (new): C-09 requires 5+ paths to appear in output; C-16 requires the 5-path floor to be stated as a proceed-or-stop gate — a condition the agent checks before moving forward. V-02 shows this as "A-1 gate condition." The distinction: C-09 measures presence, C-16 measures enforcement posture.
