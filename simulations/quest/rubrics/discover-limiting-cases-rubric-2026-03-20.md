Written to `simulations/quest/rubrics/discover-limiting-cases-rubric-2026-03-20.md`.

**Structure:**

- **5 essential** — inventory table (C-01), verification blocks (C-02), canonical verdicts (C-03), standard limit classes covered (C-04), frontmatter fields (C-05)
- **3 recommended** — P1/P2/P3 severity with justification (C-06), amendment fixes per severity class (C-07), "stated in paper" column populated (C-08)
- **2 aspirational** — algebraic substitution written out (C-09), FAIL error-type classification (C-10)

**Key design decisions:**

- C-03 enforces the three-way vocabulary (PASS/FAIL/UNSTATED) and requires consistency between Phase 2 and Phase 4 — the most common failure mode is calling something "unclear" instead of picking a verdict
- C-04 requires equilibrium as a mandatory class since it's the most reviewer-hostile gap, plus one additional class — prevents single-limit artifacts
- C-09 aspirational distinguishes "describes what happens" from "shows the algebra" — this is where reviewers actually check the math
e 2 produces a table with columns: L-ID, Equation, Parameter/Variable, Limit direction, Expected behavior, Is expected behavior stated in paper? Every equation in the paper has at least one row. A table with fewer columns or no L-IDs fails. |
| C-02 | Verification blocks present | correctness | Phase 3 contains one structured block per L-ID with fields: Equation, At limit, Substituted form, Result, Expected, Verdict, and a conditional "If FAIL" or "If UNSTATED" note. A prose-only evaluation without structured blocks fails. |
| C-03 | PASS/FAIL/UNSTATED verdicts | correctness | Every L-ID receives exactly one of PASS, FAIL, or UNSTATED as its verdict. Qualitative phrases ("looks correct", "unclear") without one of the three canonical verdicts fail. Verdicts must match across the Phase 2 inventory and the Phase 4 register. |
| C-04 | Standard limit classes covered | coverage | At least one equilibrium/steady-state limit is tested (set time derivatives to zero, verify recovery of static formula). At least one additional class is tested: zero-input/boundary, saturation, or degenerate parameter. Artifacts that test only one limit class fail. |
| C-05 | Artifact frontmatter with required fields | format | Output file includes YAML frontmatter with all four required fields: skill, topic, date, limits_checked, p1_failures, unstated_limits. Missing or incorrect field names fail. Numeric counts must match the body content. |

## Recommended Criteria (30 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Severity classification in limit register | depth | Phase 4 register column "Impact" uses the P1/P2/P3 severity scale: P1 = formula gives wrong/nonsensical result; P2 = limit untested or unstated; P3 = correct but surprising. Every non-PASS verdict carries a severity label with a one-line justification. Severity assigned without justification fails. |
| C-07 | Amendment section with targeted fixes | behavior | Phase 5 lists at least one concrete fix per severity class present in the body (P1 fix if any P1 exists, P2 fix if any P2 exists). Fixes name the specific equation or section to modify and state what the change is. Generic advice ("review the model") without a specific target fails. |
| C-08 | "Stated in paper" column populated | coverage | Every row in the Phase 2 inventory answers YES or NO in the "Is expected behavior stated in paper?" column. Blank, "unknown", or omitted cells fail. |

## Aspirational Criteria (10 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Substituted form written out algebraically | depth | For each verification block, the "Substituted form" field shows the equation with the limit value substituted in — e.g., "dR/dt = alpha*O*(1-tau) - beta*tau^2 with dR/dt=0 gives alpha*O*(1-tau) = beta*tau^2". A description of what happens ("the derivative vanishes") without the algebraic substitution fails. |
| C-10 | FAIL error-type classification | depth | For every FAIL verdict, the artifact classifies the failure as one of: mathematical error (sign, term), unstated approximation (valid under conditions not disclosed), or model design choice (intentional but not explicit). A FAIL block that identifies what went wrong without classifying why fails. |

---

## Scoring Formula

```
essential_score     = (essential_criteria_passed / 5) * 60
recommended_score   = (recommended_criteria_passed / 3) * 30
aspirational_score  = (aspirational_criteria_passed / 2) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.
