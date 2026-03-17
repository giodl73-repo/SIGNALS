Rubric written to `simulations/quest/rubrics/prove-analysis-rubric-2026-03-14.md`.

**Design decisions:**

- **5 essential** rather than 3-4 because `prove-analysis` has five structurally distinct obligations: name the source, state the pattern, tie it to the hypothesis, label correlation/causation, and assess strength. Collapsing any two would let bad output through.
- **C-04 (correlation vs. causation)** is essential, not recommended — the skill description calls it out explicitly, and wrong labeling is the most common failure mode in LLM analysis.
- **C-07 (counter-patterns)** is recommended not essential — absence of disconfirming data isn't always a failure; sometimes there genuinely isn't any. But good analysis seeks it.
- **C-09 (mechanism)** is aspirational because proposing a causal mechanism requires reasoning beyond the data and should only be rewarded once the essentials are stable.
- Failure modes section captures the four ways a formally compliant output can still be misleading.
file, table, or system -- not just "the data" or "existing telemetry". |
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

## Aspirational Criteria (10 pts total)

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-09 | **Causal mechanism proposed** -- Even when labeling a relationship as correlational, the output proposes a plausible causal mechanism or rules one out with reasoning. | depth | A mechanism sentence is present: "A plausible cause is...", "This could be explained by...", or "No causal mechanism is apparent because...". |
| C-10 | **Scope and validity conditions stated** -- The output specifies the conditions under which the pattern holds and where it may not generalize (population, time window, platform, configuration, etc.). | coverage | At least one explicit boundary condition or scope limitation is stated for the primary pattern. |

---

## Scoring Table

| Tier | Criteria | Count | Max Points |
|------|----------|-------|------------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 |
| Recommended | C-06, C-07, C-08 | 3 | 30 |
| Aspirational | C-09, C-10 | 2 | 10 |
| **Total** | | **10** | **100** |

---

## Failure Modes

These patterns indicate an output that cannot pass essential criteria regardless of other quality:

- **Phantom data** -- cites data sources that do not exist or are not accessible in the context
- **Hypothesis orphan** -- pattern is interesting but never connected to the hypothesis
- **Causation overclaim** -- labels a correlational finding as causal without justification
- **Causation underclaim** -- refuses to name causation even when logical necessity is established
- **Strength vacuum** -- all strength claims are qualitative ("significant", "notable") with no backing
