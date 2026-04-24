Written to `simulations/quest/rubrics/discover-competitors-alt-rubric-v2-2026-03-18.md`.

---

**Two new aspirational criteria extracted from R1:**

**C-11 — Inertia reference propagates downstream** (`depth`)
The R1 signal: V-03 got PARTIAL on C-06 because "the mechanism has no named reference handle — re-referencing it in later findings relies on model memory." V-04 scored PASS by naming it `INERTIA-REF` and propagating that label into column headers and findings templates. The pass condition requires the mechanism to appear in at least one downstream finding or competitor comparison after its introduction in C0 — not just to be stated once and dropped.

**C-12 — AMEND evaluates inertia stability** (`depth`)
The R1 signal: V-04 was the only variation to add a third AMEND column ("INERTIA-REF stable?") asking whether a proposed adjustment would shift the inertia anchor or leave it intact. The pass condition requires at least one AMEND entry to address this question. C-12 depends on C-08 passing — no AMEND section means C-12 scores 0.

**Scoring adjustment:** Aspirational tier stays at 10 points total; per-criterion weight drops from 5 to 2.5 to accommodate 4 criteria. Composite formula denominator changes from 2 to 4. Max composite and golden threshold (>=80) unchanged.
. Every named entry — including C0 — receives an explicit HIGH / MEDIUM / LOW threat rating. No competitor appears without a threat level. Generic category labels ("incumbent," "legacy tool") without a proper name do not count. |
| C-03 | Focus dimension woven, not appended | behavior | When a focus dimension (market sizing or positioning framework) is supplied, that content is distributed throughout competitor rows, findings, and narrative — not isolated in a trailing section. A standalone "Market Sizing" or "Positioning" appendix after the main analysis fails this criterion. If no focus is provided, this criterion passes by vacuous satisfaction. |
| C-04 | Whitespace identified | coverage | Output names an uncontested space or gap that no listed competitor owns. The gap is stated in its own labeled finding or clearly called out — not buried in a competitor row. A generic statement ("there is room to innovate") without naming the specific uncontested dimension does not pass. |
| C-05 | Auto-detect topic without prompting | behavior | Topic domain and relevant competitors are inferred from repo context (README, CLAUDE.md, package.json, or equivalent). Output does not ask the user to supply the domain, competitor names, or market category before proceeding. |

---

## Recommended Criteria (weight = 30 points total, 10 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | Mechanism-level inertia reasoning | depth | The C0 inertia section names at least one concrete mechanism — switching cost, habit lock-in, or workaround satisfaction — specific to the status quo's behavior or feature set. "Inertia is high" or a category label applied generically does not pass; the mechanism must be tied to something the current solution does or provides. |
| C-07 | Web-verified competitive claim with inline citation | correctness | At least one named external competitor characterization is supported by an inline citation (URL or publication name) from a WebSearch result. The citation appears within the competitor entry or its immediately adjacent finding — not in a trailing footnote block. |
| C-08 | AMEND section with input-to-output pairs | format | Output includes an AMEND section listing at least 2 adjustments the user can make. Each adjustment names both the input change (shift focus dimension, adjust depth, narrow competitor set) and what changes in the output as a result. A list of options without specifying the output effect does not pass. |

---

## Aspirational Criteria (weight = 10 points total, 2.5 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires both the competitive map and the focus lens together. A finding that merely cites both dimensions without demonstrating their intersection does not pass. |
| C-10 | Grounded findings (no free-floating claims) | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Findings that read as general domain knowledge without tying back to a specific competitor entry do not pass. |
| C-11 | Inertia reference propagates downstream | depth | The inertia mechanism named in the C0 section is referenced by name or label in at least one downstream finding or competitor comparison — not only in the C0 entry. The mechanism must demonstrably shape the competitive analysis after its introduction: it appears in a finding, a competitor threat framing, or a gap rationale. A mechanism described once in C0 and then abandoned does not pass. |
| C-12 | AMEND evaluates inertia stability | depth | For at least one entry in the AMEND section, the output states whether the proposed input adjustment would alter the inertia reference or leave it stable. An AMEND that only specifies output format or content changes without addressing whether the inertia anchor shifts does not pass. This criterion requires C-08 to pass; if C-08 fails, C-12 is scored 0. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-12 | 2.5 | 10 |
| **Max composite** | | | **100** |

**Composite formula:**
```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 4 * 10)
```

PARTIAL counts as 0.5 toward the numerator of each tier.

**Golden threshold:** All 5 essential pass AND composite >= 80

**Grade bands:**

| Score | Grade |
|-------|-------|
| 95 -- 100 | Exceptional |
| 85 -- 94 | Strong |
| 80 -- 84 | Passing |
| < 80 | Below bar |

---

## Rubric Change Log

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-18 | Initial rubric -- 5 essential, 3 recommended, 2 aspirational |
| v2 | 2026-03-18 | Added C-11 (inertia reference propagates downstream) and C-12 (AMEND evaluates inertia stability) from R1 excellence signals. Aspirational tier: 2 to 4 criteria, 5 pts each to 2.5 pts each. Scale unchanged at 100. |
