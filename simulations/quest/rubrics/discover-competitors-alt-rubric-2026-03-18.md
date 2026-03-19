Rubric written to `simulations/quest/rubrics/discover-competitors-alt-rubric-2026-03-18.md`.

**Design summary:**

**Essential (5)** — what makes the unified approach work or fail:
- C-01: Inertia (C0) first — ordering correctness, not just presence
- C-02: Named competitors with threat levels — minimum viable competitive map
- C-03: Focus woven not appended — the core differentiator from parameterized; vacuous pass when no focus provided
- C-04: Whitespace identified — primary actionable output
- C-05: Auto-detect — zero-friction invocation

**Recommended (3)** — separates useful from great:
- C-06: Mechanism-level inertia reasoning (not just "high")
- C-07: Web-verified claim with inline citation
- C-08: AMEND block naming both input change and output effect

**Aspirational (2)** — validates the unified approach's synergy claim:
- C-09: Cross-dimensional whitespace (requires both competitive map + focus lens together)
- C-10: No free-floating findings (every finding traces to a named competitor row)
s at least 3 competitive alternatives including C0. Every named entry — including C0 — receives an explicit HIGH / MEDIUM / LOW threat rating. No competitor appears without a threat level. Generic category labels ("incumbent," "legacy tool") without a proper name do not count. |
| C-03 | Focus dimension woven, not appended | behavior | When a focus dimension (market sizing or positioning framework) is supplied, that content is distributed throughout competitor rows, findings, and narrative — not isolated in a trailing section. A standalone "Market Sizing" or "Positioning" appendix after the main analysis fails this criterion. If no focus is provided, this criterion passes by vacuous satisfaction. |
| C-04 | Whitespace identified | coverage | Output names an uncontested space or gap that no listed competitor owns. The gap is stated in its own labeled finding or clearly called out — not buried in a competitor row. A generic statement ("there is room to innovate") without naming the specific uncontested dimension does not pass. |
| C-05 | Auto-detect topic without prompting | behavior | Topic domain and relevant competitors are inferred from repo context (README, CLAUDE.md, package.json, or equivalent). Output does not ask the user to supply the domain, competitor names, or market category before proceeding. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Inertia stickiness reasoning | depth | The C0 inertia section names at least one concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — specific to the status quo's behavior or feature set. "Inertia is high" or a category label applied generically does not pass; the mechanism must be tied to something the current solution does or provides. |
| C-07 | Web-verified competitive claim | correctness | At least one named external competitor characterization is supported by an inline citation (URL or publication name) from a WebSearch result. The citation appears within the competitor entry or its immediately adjacent finding — not in a trailing footnote block. |
| C-08 | AMEND section present with actionable adjustments | format | Output includes an AMEND section listing at least 2 adjustments the user can make. Each adjustment names both the input change (shift focus dimension, adjust depth, narrow competitor set) and what changes in the output as a result. A list of options without specifying the output effect does not pass. |

---

## Aspirational Criteria (weight = 10 points total, 5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires both the competitive map and the focus lens together. A finding that merely cites both dimensions without demonstrating their intersection does not pass. |
| C-10 | Grounded findings (no free-floating claims) | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Findings that read as general domain knowledge without tying back to a specific competitor entry do not pass. |

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
