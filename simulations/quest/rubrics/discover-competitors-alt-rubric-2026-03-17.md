Rubric written. Here's a summary of the design decisions:

**Essential (5)** — the non-negotiables that define whether the unified approach actually works:
- C-01/C-03: Inertia-first + threat levels — correctness of the competitive model
- C-02: Focus woven not appended — the core differentiator from parameterized
- C-04: Whitespace — the primary actionable output
- C-05: Auto-detect — zero-friction invocation

**Recommended (3)** — what separates a useful output from a great one:
- C-06: Mechanism-level inertia reasoning (not just label)
- C-07: Web verification (claim quality)
- C-08: Actionable AMEND block (amendability is the unified skill's other claim)

**Aspirational (2)** — raise the bar once essentials are stable:
- C-09: Cross-dimensional whitespace (proves the unified approach is synergistic, not just additive)
- C-10: Grounded findings (no free-floating claims)

Golden threshold is all essential + composite >= 80 per the standard formula.
l. |
| C-02 | Focus woven, not appended | behavior | When a focus dimension (market sizing or positioning framework) is provided, that content is distributed throughout competitor rows, findings, and narrative — not isolated in a trailing section. If no focus is provided, this criterion passes by vacuous satisfaction. |
| C-03 | Threat level per competitor | correctness | Every named competitor and inertia receive an explicit HIGH / MEDIUM / LOW threat rating. No competitor appears without a threat level. |
| C-04 | Whitespace identified | coverage | Output names an uncontested space or gap that no listed competitor owns — stated in its own finding or clearly labeled. |
| C-05 | Auto-detect without prompting | behavior | Topic domain is inferred from repo context (README, CLAUDE.md, package.json, etc.). Output does not ask the user to supply the domain or competitor names. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | Inertia section names at least one concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — not just "inertia is high." |
| C-07 | Web-verified competitive claim | correctness | At least one named competitor characterization is supported by an inline citation (URL or publication) from a WebSearch result. |
| C-08 | AMEND section with 3 actionable adjustments | format | AMEND lists exactly 3 adjustments. Each names both what the user changes and what changes in the output as a result. |

---

## Aspirational Criteria (weight = 10 points total, 5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires the competitive map and the focus dimension together. |
| C-10 | Table-stakes grounding per finding | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-10 | 5 | 10 |
| **Max composite** | | | **100** |

**Composite formula:**
```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 2 * 10)
```

**Golden threshold:** All 5 essential pass AND composite >= 80

**Grade bands:**

| Score | Grade |
|-------|-------|
| 95 -- 100 | Exceptional |
| 85 -- 94 | Strong |
| 80 -- 84 | Passing |
| < 80 | Below bar |
