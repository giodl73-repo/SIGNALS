Rubric v2 written to `simulations/quest/rubrics/prove-analysis-rubric-v2-2026-03-14.md`.

---

**Three new aspirational criteria added (C-11, C-12, C-13):**

| ID | Name | Extracted from |
|----|------|----------------|
| C-11 | Per-source structured format | "table columns eliminate criteria bleeding -- visible blank cell stronger than instruction" |
| C-12 | Null or falsification framing | "null hypothesis column makes disconfirmation structurally unavoidable" |
| C-13 | Vocabulary precision | "fixed three-option C-04 vocabulary eliminates hedged non-answers" |

**Scoring changes:**
- Aspirational tier: 10 pts (2 criteria) → 25 pts (5 criteria, 5 pts each)
- Grand total: 100 → 115

**One new failure mode added:**
- **Criteria bleeding** -- two obligations satisfied in one sentence without separation; relevant when scoring C-11

**What was NOT promoted to essential/recommended:** These remain aspirational because they are structural properties of excellent outputs, not minimum correctness bars. An output can score 90/115 with solid essentials and recommended criteria while missing all three new aspirational criteria -- which is fine. The aspirational tier rewards outputs that eliminate the structural ambiguities that instruction-based prompts cannot close.
sified hedged relationship claims).
- **Scoring table updated**: aspirational tier expands from 10 pts (2 criteria) to 25 pts (5 criteria, 5 pts each). Grand total moves from 100 to 115.
- Failure modes section adds **criteria bleeding** (from Round 1 finding that named columns are stronger than prose-embedded satisfaction of multiple obligations).

---

## Essential Criteria (60 pts total)

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-01 | **Source named** -- The output names each data source analyzed by its specific identifier: a file, table, dataset, log stream, API endpoint, or system -- not just "the data" or "existing telemetry". | correctness | Each data source cited has a specific name or identifier -- not a generic reference. |
| C-02 | **Pattern stated** -- For each data source analyzed, the output explicitly states what pattern was found (or that no pattern was found). | correctness | At least one pattern claim is present in the form: "X was found to correlate/associate/predict/follow Y" or equivalent. Absence of pattern is acceptable if stated explicitly. |
| C-03 | **Hypothesis connection** -- The output connects each pattern back to the hypothesis under investigation, explaining how the pattern bears on it. | correctness | Each pattern has an explicit sentence or clause tying it to the hypothesis -- not left implicit. |
| C-04 | **Correlation vs. causation labeled** -- The output explicitly distinguishes whether each relationship is correlational or causal, using those terms or equivalents ("we cannot infer causation", "this establishes a directional cause", etc.). | behavior | The word "correlation", "causal", "cause", "association", or a direct equivalent appears in the analysis with correct usage -- not just as decoration. |
| C-05 | **Strength assessed** -- The output provides an assessment of the statistical or logical strength of each pattern (e.g., sample size, effect size, confidence level, logical necessity, prevalence rate, or a reasoned qualitative tier: weak/moderate/strong). | depth | At least one strength indicator per pattern -- a number, a rate, a tier label with justification, or a logical argument for why the pattern is or is not compelling. |

---

## Recommended Criteria (30 pts total)

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-06 | **Multiple data sources** -- The output analyzes more than one distinct data source, broadening the evidentiary base. | coverage | At least two named, distinct data sources appear in the analysis. |
| C-07 | **Counter-patterns or disconfirming data** -- The output notes data that does not fit the pattern, contradicts it, or limits its generalizability. | depth | At least one sentence addresses data that weakens, limits, or contradicts the main pattern -- not only confirmatory evidence is reported. |
| C-08 | **Quantified claims** -- Patterns are described with numbers, rates, counts, or percentages rather than vague qualifiers alone ("most", "often", "sometimes"). | correctness | At least one pattern claim includes a numeric value (e.g., "73% of scenarios", "14 of 16 cases", "p < 0.05", "effect size 0.4"). |

---

## Aspirational Criteria (25 pts total)

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-09 | **Causal mechanism proposed** -- Even when labeling a relationship as correlational, the output proposes a plausible causal mechanism or rules one out with reasoning. | depth | A mechanism sentence is present: "A plausible cause is...", "This could be explained by...", or "No causal mechanism is apparent because...". |
| C-10 | **Scope and validity conditions stated** -- The output specifies the conditions under which the pattern holds and where it may not generalize (population, time window, platform, configuration, etc.). | coverage | At least one explicit boundary condition or scope limitation is stated for the primary pattern. |
| C-11 | **Per-source structured format** -- The output presents each data source in a discrete structural unit (table row, numbered block, or labeled section) with each analytical obligation -- pattern, correlation/causation label, strength, hypothesis connection -- appearing as a visually distinct element rather than merged in undifferentiated prose. | behavior | At least one data source is analyzed using a format where the five essential obligations each occupy a named, structurally separate position. A table with labeled columns or a numbered block with labeled fields qualifies. A single prose paragraph covering all obligations does not. |
| C-12 | **Null or falsification framing** -- For at least one major pattern, the output explicitly states what the disconfirming or null condition would look like and whether it was or was not observed in the data. | depth | At least one pattern has an explicit falsification sentence: "If this pattern did not hold, we would expect to see X; instead we observed Y" -- or equivalent null-met / null-not-met reporting. Absence of disconfirming data is acceptable if the null condition is named and its absence noted. |
| C-13 | **Vocabulary precision** -- The output uses only category-precise relationship vocabulary throughout. Every relationship claim specifies its type -- "correlation", "association", "causal (basis: ...)", or a formal equivalent -- without leaving hedged terms ("appears related", "suggests a link", "may indicate", "is associated with") unclassified. | behavior | No unclassified relationship claim appears. Every claim either uses type-precise vocabulary or immediately follows with an explicit label from the permitted set (correlation / association / causal). A single unclassified hedged term that stands alone as the relationship characterization is a FAIL. |

---

## Scoring Table

| Tier | Criteria | Count | Max Points |
|------|----------|-------|------------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 |
| Recommended | C-06, C-07, C-08 | 3 | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13 | 5 | 25 |
| **Total** | | **13** | **115** |

---

## Failure Modes

These patterns indicate an output that cannot pass essential criteria regardless of other quality:

- **Phantom data** -- cites data sources that do not exist or are not accessible in the context
- **Hypothesis orphan** -- pattern is interesting but never connected to the hypothesis
- **Causation overclaim** -- labels a correlational finding as causal without justification
- **Causation underclaim** -- refuses to name causation even when logical necessity is established
- **Strength vacuum** -- all strength claims are qualitative ("significant", "notable") with no backing
- **Criteria bleeding** -- satisfies two analytical obligations in a single sentence without structural separation, making individual criterion evaluation ambiguous; relevant when scoring C-11

---

## v2 Change Log

| Change | Source |
|--------|--------|
| C-11 added (per-source structured format) | R1 excellence signal: "table columns eliminate criteria bleeding -- visible blank cell is a stronger failure signal than any instruction-based prompt" |
| C-12 added (null or falsification framing) | R1 excellence signal: "null hypothesis column makes disconfirmation structurally unavoidable -- Null met rows are counter-patterns by definition" |
| C-13 added (vocabulary precision) | R1 excellence signal: "fixed three-option C-04 vocabulary eliminates hedged non-answers -- the model must pick one; it cannot write 'relationship' or leave the type implicit" |
| Aspirational tier: 10 pts (2 criteria) -> 25 pts (5 criteria, 5 pts each) | Tier expansion to accommodate new criteria |
| Grand total: 100 -> 115 | Follows from aspirational tier expansion |
| Failure modes: added criteria bleeding | R1 finding that structural separation is a stronger guarantee than prose instruction |
