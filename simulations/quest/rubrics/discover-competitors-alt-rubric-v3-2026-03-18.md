v3 written. Here's what changed:

**Two new aspirational criteria from R2 excellence patterns:**

**C-13 — Inertia mechanism assigned a portable token** (Pattern 1)
The operative insight from R2: MECH, INERTIA-REF, and ROOT all satisfied C-11 because the *label* is what enables propagation — not the format. A role description like "the **inertia mechanism**" doesn't pass because it can't be copied verbatim into a column header or finding slot. Pass requires an explicit short token.

**C-14 — Inertia stability addressed in every AMEND entry** (Pattern 2)
Stricter scope than C-12. C-12 requires at least one AMEND entry to address stability; C-14 requires every entry. Pattern 2 confirmed the minimum viable form is one explicit stability question per entry (any register) — column, inline phrase, or conversational imperative all work.

Pattern 3 (conversational register achieves perfect score via three ordered imperatives) is an insight about prompt design strategy, not a new evaluatable output behavior — it informs how to read C-13/C-14 rather than adding a third criterion.

**Scoring adjustment:** Aspirational tier stays at 10 points; per-criterion weight drops from 2.5 to 1.67 to accommodate 6 criteria. Composite formula denominator changes from 4 to 6. Max composite and golden threshold (>=80) unchanged.
ded, this criterion passes by vacuous satisfaction. |
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

## Aspirational Criteria (weight = 10 points total, 1.67 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires both the competitive map and the focus lens together. A finding that merely cites both dimensions without demonstrating their intersection does not pass. |
| C-10 | Grounded findings (no free-floating claims) | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Findings that read as general domain knowledge without tying back to a specific competitor entry do not pass. |
| C-11 | Inertia reference propagates downstream | depth | The inertia mechanism named in the C0 section is referenced by name or label in at least one downstream finding or competitor comparison — not only in the C0 entry. The mechanism must demonstrably shape the competitive analysis after its introduction: it appears in a finding, a competitor threat framing, or a gap rationale. A mechanism described once in C0 and then abandoned does not pass. |
| C-12 | AMEND evaluates inertia stability | depth | For at least one entry in the AMEND section, the output states whether the proposed input adjustment would alter the inertia reference or leave it stable. An AMEND that only specifies output format or content changes without addressing whether the inertia anchor shifts does not pass. This criterion requires C-08 to pass; if C-08 fails, C-12 is scored 0. |
| C-13 | Inertia mechanism assigned a portable token | depth | The inertia mechanism in C0 is assigned an explicit short token or label (e.g., MECH, INERTIA-REF, a product-specific abbreviation) that stands as a standalone identifier. A role description ("the **inertia mechanism**," "the C0 stickiness factor," "the current workflow's lock-in") does not pass. The label must be a copyable token — one that can appear verbatim in a downstream column header, finding slot, or AMEND entry without additional context to interpret it. Register is irrelevant: conversational label, template block, and architectural ROOT declaration all satisfy this criterion equally; the operative element is the token, not the syntax around it. |
| C-14 | Inertia stability addressed in every AMEND entry | depth | Every entry in the AMEND section — not just one — explicitly addresses whether the proposed adjustment would alter the inertia reference or leave it stable. An AMEND with a stability question on some entries but silent on others does not pass. Minimum viable enforcement is one explicit stability question per entry, in any register (column, inline phrase, or conversational imperative). This criterion requires C-08 to pass and imposes a stricter scope than C-12 (which requires only one entry); if C-08 fails, C-14 is scored 0. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-14 | 1.67 | 10 |
| **Max composite** | | | **100** |

**Composite formula:**
```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 6 * 10)
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
| v3 | 2026-03-18 | Added C-13 (inertia mechanism assigned a portable token) and C-14 (inertia stability addressed in every AMEND entry) from R2 excellence signals. C-13 captures Pattern 1: the label is the operative element, not the format -- conversational token, template block, and architectural ROOT declaration satisfy equally. C-14 captures Pattern 2: minimum viable enforcement is one explicit stability question per entry (stricter scope than C-12, which requires only one entry total). Aspirational tier: 4 to 6 criteria, 2.5 pts each to 1.67 pts each. Composite denominator changes from 4 to 6. Max composite and golden threshold unchanged at 100 and >=80. |
