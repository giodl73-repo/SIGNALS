Reading the R4 scorecard to extract the new excellence patterns before writing v5.

Three patterns emerge:

**Pattern A (V-01 C-17 PASS vs V-02 C-17 PARTIAL):** V-01 wins C-17 by forcing `DOMAIN-TERMS: [term-1], [term-2]` as a separate committed output artifact before token construction. V-02 only instructs the model to use domain terms — no intermediate commitment. The operative gap: *structural extraction step vs. instructional guidance*.

**Pattern B (V-03 C-15):** V-03 escalates C-15 by requiring TOKEN as the literal first output line — before focus detection, before auto-detect, before any conditional logic. C-15 only requires token before C0 prose. V-03's "first output line" contract closes every remaining execution-order gap.

**Pattern C (V-03 AMEND):** V-03 names all four AMEND components as an explicit numbered schema — "1. Input change. 2. Output effect. 3. STABILITY. 4. EVIDENCE." C-16 requires verdict+evidence per entry; this pattern requires the schema itself to enumerate all four parts by name, making omission structurally visible.

New criteria: **C-18** (DOMAIN-TERMS as intermediate artifact), **C-19** (TOKEN as absolute first output), **C-20** (AMEND schema enumerates all four components by name).

Aspirational tier: 9 → 12 criteria, 1.11 → 0.833 pts each.

---

```markdown
# discover-competitors-alt Rubric — v5

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

## Aspirational Criteria (weight = 10 points total, 0.833 points each)

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
| C-18 | DOMAIN-TERMS committed as extraction artifact before token construction | depth | The output contains an explicit DOMAIN-TERMS (or equivalent vocabulary commitment) artifact as a separate step prior to the TOKEN declaration — e.g., `DOMAIN-TERMS: [term-1], [term-2]` written and closed before the token name is chosen. Instruction-only guidance that tells the model to use domain terms without forcing an intermediate output commitment does not pass. The vocabulary step must be its own output artifact: embedded vocabulary selection inside the token declaration line does not satisfy this criterion. This criterion requires C-17 to pass; if C-17 fails, C-18 is scored 0. |
| C-19 | TOKEN declared before any conditional or procedural logic executes | depth | The TOKEN declaration is the literal first output — no focus detection, auto-detect, section headers, or conditional branching appears before it. C-15 requires only that the token precede C0 mechanism prose; this criterion closes the remaining execution-order gap by requiring the token to precede all other operations, including focus resolution. A token that appears after focus detection or within a section block does not pass even if it precedes C0 mechanism prose. This criterion requires C-15 to pass; if C-15 fails, C-19 is scored 0. |
| C-20 | AMEND entry schema enumerates all required components by name | depth | The AMEND section instruction or template explicitly enumerates all required per-entry components — input change, output effect, stability verdict, and evidence — as a named, numbered (or equivalent structured) schema. An AMEND instruction that names some components and implies others, or that specifies format without enumerating all four components by name, does not pass. The operative test: a reader consulting only the schema can identify all four required elements without reading examples. This criterion requires C-16 to pass; if C-16 fails, C-20 is scored 0. |

---

## Scoring Summary

| Tier | Criteria | Points each | Subtotal |
|------|----------|-------------|---------|
| Essential | C-01 -- C-05 | 12 | 60 |
| Recommended | C-06 -- C-08 | 10 | 30 |
| Aspirational | C-09 -- C-20 | 0.833 | 10 |
| **Max composite** | | | **100** |

**Composite formula:**
```
composite = (essential_pass / 5 * 60) + (recommended_pass / 3 * 30) + (aspirational_pass / 12 * 10)
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
```

---

**Summary of additions:**

| New ID | Derived from | Operative gap closed |
|--------|-------------|----------------------|
| C-18 | V-01 C-17 PASS vs V-02 C-17 PARTIAL | Instruction-only domain guidance leaves model free to skip vocabulary commitment; a separate DOMAIN-TERMS artifact makes C-17 structurally impossible to fail by drift |
| C-19 | V-03 C-15 "first output line" | C-15 only requires token before C0 prose; focus detection and auto-detect remain unguarded execution steps that can precede the token and introduce conditional branching before commitment |
| C-20 | V-03 four-part AMEND schema | C-16 requires verdict+evidence per entry but does not require the schema to enumerate all four components; an unenumerated schema allows a model to satisfy C-16 while leaving components discoverable only through examples |
