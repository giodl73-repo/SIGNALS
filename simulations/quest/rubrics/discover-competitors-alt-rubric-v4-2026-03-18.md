Reading the R3 scorecard patterns, then writing v4.

The three new criteria:

- **C-15** — Token pre-declared before C0 description begins (Pattern 1)
- **C-16** — Stability verdict accompanied by evidence in every AMEND entry (Pattern 2)
- **C-17** — Token identifier encodes domain context (Pattern 3)

Aspirational tier: 6 → 9 criteria, 1.67 pts each → 1.11 pts each. Composite denominator: 6 → 9.

---

```markdown
# discover-competitors-alt Rubric — v4

## Essential Criteria (weight = 60 points total, 12 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | C0 named before competitors | structure | The current solution (C0) is introduced and described before any external competitor is named. If C0 appears first in a dedicated section or as row 0 before any competitor rows, this passes. A rubric that opens with competitor rows and places C0 afterward fails. |
| C-02 | 3+ named competitors with threat levels | coverage | Output names at least 3 external competitors by product or company name, each with an explicit threat level (HIGH / MEDIUM / LOW or equivalent). Unnamed categories ("various startups") do not count toward the minimum. |
| C-03 | C0 at row 0 in competitive map | structure | The competitive comparison table or map places C0 as the first row (row 0). If no table is present and comparison is prose-only, this criterion fails. If the focus input is INACTIVE, this criterion passes by vacuous satisfaction. |
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

## Aspirational Criteria (weight = 10 points total, 1.11 points each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | Cross-dimensional whitespace finding | depth | The whitespace finding names a gap uncontested across both the competitive dimension and the focus dimension simultaneously. The finding cannot be produced by dropping the focus input — it requires both the competitive map and the focus lens together. A finding that merely cites both dimensions without demonstrating their intersection does not pass. |
| C-10 | Grounded findings (no free-floating claims) | depth | Each item in the findings section references at least one named competitor row or map entry by label. No finding is free-floating prose that does not require the competitive analysis to support it. Findings that read as general domain knowledge without tying back to a specific competitor entry do not pass. |
| C-11 | Inertia reference propagates downstream | depth | The inertia mechanism named in the C0 section is referenced by name or label in at least one downstream finding or competitor comparison — not only in the C0 entry. The mechanism must demonstrably shape the competitive analysis after its introduction: it appears in a finding, a competitor threat framing, or a gap rationale. A mechanism described once in C0 and then abandoned does not pass. |
| C-12 | AMEND evaluates inertia stability | depth | For at least one entry in the AMEND section, the output states whether the proposed input adjustment would alter the inertia reference or leave it stable. An AMEND that only specifies output format or content changes without addressing whether the inertia anchor shifts does not pass. This criterion requires C-08 to pass; if C-08 fails, C-12 is scored 0. |
| C-13 | Inertia mechanism assigned a portable token | depth | The inertia mechanism in C0 is assigned an explicit short token or label (e.g., MECH, INERTIA-REF, a product-specific abbreviation) that stands as a standalone identifier. A role description ("the **inertia mechanism**," "the C0 stickiness factor," "the current workflow's lock-in") does not pass. The label must be a copyable token — one that can appear verbatim in a downstream column header, finding slot, or AMEND entry without additional context to interpret it. Register is irrelevant: conversational label, template block, and architectural ROOT declaration all satisfy this criterion equally; the operative element is the token, not the syntax around it. |
| C-14 | Inertia stability addressed in every AMEND entry | depth | Every entry in the AMEND section — not just one — explicitly addresses whether the proposed adjustment would alter the inertia reference or leave it stable. An AMEND with a stability question on some entries but silent on others does not pass. Minimum viable enforcement is one explicit stability question per entry, in any register (column, inline phrase, or conversational imperative). This criterion requires C-08 to pass and imposes a stricter scope than C-12 (which requires only one entry); if C-08 fails, C-14 is scored 0. |
| C-15 | Token pre-declared before C0 description begins | depth | The token identifier is committed before the first sentence of C0 mechanism prose — not embedded in it or introduced after. Pre-declaration makes the name structurally prior to any description, eliminating the drift path where a role description hardens into a nominal label mid-paragraph. A token that appears for the first time inside the C0 mechanism description does not pass, even if it reads as a clean token at that point. This criterion requires C-13 to pass; if C-13 fails, C-15 is scored 0. |
| C-16 | Stability verdict accompanied by evidence in every AMEND entry | depth | Each stability assessment in the AMEND section includes both a verdict (stable / unstable or equivalent) and supporting reasoning or evidence. A verdict tag or column without an evidence column or explanation does not pass — the operative failure mode is a model writing "Stable" on every entry without reasoning. Minimum viable form: one verdict plus one supporting rationale per AMEND entry. This criterion requires C-14 to pass; if C-14 fails, C-16 is scored 0. |
| C-17 | Token identifier encodes domain context | depth | The portable token includes at least one domain-specific term drawn from the product or repo context — not a generic placeholder such as MECH, LOCK, or INERTIA-REF alone. A domain-adaptive token (e.g., SIGNAL-LOCK, WORKFLOW-ANCHOR, DATA-GRIP) makes generic stability reasoning structurally wrong because the token name itself frames every downstream reference. Pass requires at least one domain-specific term visible in the token identifier. A two-part token where one part is a generic category and one part is domain-specific satisfies this criterion. This criterion requires C-13 to pass; if C-13 fails, C-17 is scored 0. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-17 | 1.11 | 10 |
| **Max composite** | | | **100** |

**Composite formula:**
```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 9 * 10)
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
| v4 | 2026-03-18 | Added C-15 (token pre-declared before C0 description begins), C-16 (stability verdict accompanied by evidence in every AMEND entry), and C-17 (token identifier encodes domain context) from R3 excellence signals. C-15 captures Pattern 1: pre-declaration makes the token name structurally prior to any mechanism description, eliminating role-description drift at the source. C-16 captures Pattern 2: a verdict-only stability field is empty-form compliance -- the two-column contract (verdict + evidence) closes the failure mode where "Stable" appears on every row without reasoning. C-17 captures Pattern 3: domain-adaptive token naming encodes product context in the identifier itself, making generic stability reasoning structurally wrong. C-15 and C-17 depend on C-13; C-16 depends on C-14. Aspirational tier: 6 to 9 criteria, 1.67 pts each to 1.11 pts each. Composite denominator changes from 6 to 9. Max composite and golden threshold unchanged at 100 and >=80. |
```
