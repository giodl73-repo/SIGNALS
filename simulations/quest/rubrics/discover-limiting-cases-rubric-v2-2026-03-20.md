Done. The v2 rubric is at `simulations/quest/rubrics/discover-limiting-cases-rubric-v2-2026-03-20.md`.

**What changed from v1:**

| | v1 | v2 |
|--|--|--|
| Aspirational criteria | C-09, C-10 (2 total) | C-09 through C-14 (6 total) |
| Aspirational denominator | `/2` | `/6` |
| Max aspirational pts | 10 | 10 (same, redistributed) |

**Four new criteria:**

- **C-11** — Correct/wrong example pair: names the anti-pattern beside the positive instruction (V-01, V-05). Addresses the failure where a good positive example still gets verbal fill-in.
- **C-12** — Checklist gate: hard phase-transition exit converts criteria into pre-conditions (V-05). Insurance layer on top of field labels.
- **C-13** — Pre-printed label + explicit prohibition: each field with a known failure mode carries inline prohibition text (V-01, V-05). Closes the verbal-fill-in gap at field level.
- **C-14** — L-00 inertia anchor: pre-filled always-UNSTATED row replaces the abstract "reviewers will ask" with a concrete named attack (V-03). The only R1 pattern unique to one variation that demonstrably improved C-06 quality.

Golden threshold is unchanged (all 5 essential + composite >= 80). The scoring formula still allocates 10 pts to aspirational — now spread across 6 criteria instead of 2, making each harder to claim individually but the composite unchanged.
surance when the field labels alone are insufficient.
- **C-13** (new) pairs pre-printed field labels with explicit prohibition text — closes the gap where a blank label is filled verbally rather than structurally.
- **C-14** (new) replaces the generic "reviewers will ask about inertia" instruction with a named, pre-filled L-00 row — concrete beats abstract for severity quality.

---

## Essential Criteria (60 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | Inventory table with required columns | format | Phase 2 produces a table with columns: L-ID, Equation, Parameter/Variable, Limit direction, Expected behavior, Is expected behavior stated in paper? Every equation in the paper has at least one row. A table with fewer columns or no L-IDs fails. |
| C-02 | Verification blocks present | correctness | Phase 3 contains one structured block per L-ID with fields: Equation, At limit, Substituted form, Result, Expected, Verdict, and a conditional "If FAIL" or "If UNSTATED" note. A prose-only evaluation without structured blocks fails. |
| C-03 | PASS/FAIL/UNSTATED verdicts | correctness | Every L-ID receives exactly one of PASS, FAIL, or UNSTATED as its verdict. Qualitative phrases ("looks correct", "unclear") without one of the three canonical verdicts fail. Verdicts must match across the Phase 2 inventory and the Phase 4 register. |
| C-04 | Standard limit classes covered | coverage | At least one equilibrium/steady-state limit is tested (set time derivatives to zero, verify recovery of static formula). At least one additional class is tested: zero-input/boundary, saturation, or degenerate parameter. Artifacts that test only one limit class fail. |
| C-05 | Artifact frontmatter with required fields | format | Output file includes YAML frontmatter with all required fields: skill, topic, date, limits_checked, p1_failures, unstated_limits. Missing or incorrect field names fail. Numeric counts must match the body content. |

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
| C-11 | Correct/wrong example pair for substituted form | instruction-quality | The skill instruction for the "Substituted form" field names the anti-pattern beside the positive example — e.g., "write the algebra, not a description of what happens" immediately after showing the correct form. A positive example alone without naming the wrong form fails. |
| C-12 | Checklist gate as hard phase-transition exit | structure | At least one phase boundary (e.g., end of Phase 2 before Phase 3, or end of Phase 3 before Phase 4) includes a checklist of pass conditions the artifact must satisfy before advancing. The checklist converts rubric criteria into explicit pre-conditions. A phase transition with no gate fails. |
| C-13 | Pre-printed field label with explicit prohibition | instruction-quality | Each structured block field that has a known failure mode carries an explicit prohibition inline — e.g., a "Verdict" label followed by "PASS / FAIL / UNSTATED — no other phrasing". A pre-printed label without prohibition text, or a blank left for the user to fill in the label, fails. |
| C-14 | L-00 inertia anchor row | coverage | The Phase 2 inventory template includes a pre-filled L-00 row representing the always-UNSTATED inertia assumption (e.g., "no limits tested in original paper"). L-00 is fixed as UNSTATED and P2. This row serves as a named concrete attack on inertia and a model verdict for subsequent rows. Artifacts that lack L-00 or that mark L-00 as anything other than UNSTATED fail. |

---

## Scoring Formula

```
essential_score     = (essential_criteria_passed / 5) * 60
recommended_score   = (recommended_criteria_passed / 3) * 30
aspirational_score  = (aspirational_criteria_passed / 6) * 10

composite = essential_score + recommended_score + aspirational_score
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## R1 Excellence Patterns (source for C-11 through C-14)

These patterns were extracted from variations that scored 97.5-100 in Round 1.

| Pattern | Source variation | New criterion |
|---------|-----------------|---------------|
| Correct/wrong example pair names the anti-pattern beside the positive instruction | V-01, V-05 | C-11 |
| Checklist gate as hard phase-transition exit converts rubric criteria into pre-conditions | V-05 | C-12 |
| Pre-printed field label combined with explicit prohibition text closes verbal fill-in gap | V-01, V-05 | C-13 |
| L-00 pre-printed as always-UNSTATED inertia row replaces generic "reviewer will ask" with specific named attack | V-03 | C-14 |
