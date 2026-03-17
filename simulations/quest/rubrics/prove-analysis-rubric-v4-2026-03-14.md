Written to `simulations/quest/rubrics/prove-analysis-rubric-v4-2026-03-14.md`.

---

**Two new aspirational criteria extracted from R3:**

| ID | Name | Source Signal | Upgrades |
|----|------|---------------|---------|
| C-17 | Falsification chain traceability | V-05: `"Source null verdict (C-16): Copy from Falsification Chain. Do not rewrite."` — table cell constrained to copy, not re-derive | C-16: null condition committed -> verdict locked against post-hoc softening via structural copy constraint |
| C-18 | Pre-write verdict audit (write-gate) | V-05 + V-03 (independent): `"VERDICT (pre-audit before writing)"` framing — audit fires before verdict is composed | C-15: audit covers narrative sections -> audit fires as a write-gate before verdict language is committed |

**Scoring changes:**
- Aspirational tier: 8 criteria, 40 pts → 10 criteria, 50 pts (5 pts each)
- Grand total: 130 → 140

The upgrade lineage is consistent across all four rounds: every new aspirational criterion closes a loophole left open by the one it upgrades. C-16 required per-source null conditions but didn't prevent post-hoc verdict softening in the table — C-17 closes that. C-15 required a vocabulary audit before the final verdict but allowed post-hoc correction — C-18 promotes it to a write-gate that fires before the verdict section is entered.
it sentence or clause tying it to the hypothesis -- not left implicit. |
| C-04 | **Correlation vs. causation labeled** -- The output explicitly distinguishes whether each relationship is correlational or causal, using those terms or equivalents ("we cannot infer causation", "this establishes a directional cause", etc.). | behavior | The word "correlation", "causal", "cause", "association", or a direct equivalent appears in the analysis with correct usage -- not just as decoration. |
| C-05 | **Strength assessed** -- The output provides an assessment of the statistical or logical strength of each pattern (e.g., sample size, effect size, confidence level, logical necessity, prevalence rate, or a reasoned qualitative tier: weak/moderate/strong). | depth | At least one strength indicator per pattern -- a number, a rate, a tier label with justification, or a logical argument for why the pattern is or is not compelling. |

Essential points: 12 pts each.

---

## Recommended Criteria (30 pts total)

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-06 | **Multiple data sources** -- The output analyzes more than one distinct data source, broadening the evidentiary base. | coverage | At least two named, distinct data sources appear in the analysis. |
| C-07 | **Counter-patterns or disconfirming data** -- The output notes data that does not fit the pattern, contradicts it, or limits its generalizability. | depth | At least one sentence addresses data that weakens, limits, or contradicts the main pattern -- not only confirmatory evidence is reported. |
| C-08 | **Quantified claims** -- Patterns are described with numbers, rates, counts, or percentages rather than vague qualifiers alone ("most", "often", "sometimes"). | correctness | At least one pattern claim includes a numeric value (e.g., "73% of scenarios", "14 of 16 cases", "p < 0.05", "effect size 0.4"). |

Recommended points: 10 pts each.

---

## Aspirational Criteria (50 pts total)

| ID   | Text | Category | Pass Condition |
|------|------|----------|----------------|
| C-09 | **Causal mechanism proposed** -- Even when labeling a relationship as correlational, the output proposes a plausible causal mechanism or rules one out with reasoning. | depth | A mechanism sentence is present: "A plausible cause is...", "This could be explained by...", or "No causal mechanism is apparent because...". |
| C-10 | **Scope and validity conditions stated** -- The output specifies the conditions under which the pattern holds and where it may not generalize (population, time window, platform, configuration, etc.). | coverage | At least one explicit boundary condition or scope limitation is stated for the primary pattern. |
| C-11 | **Per-source structured format** -- The output presents each data source in a discrete structural unit (table row, numbered block, or labeled section) with each analytical obligation -- pattern, correlation/causation label, strength, hypothesis connection -- appearing as a visually distinct element rather than merged in undifferentiated prose. | behavior | At least one data source is analyzed using a format where the five essential obligations each occupy a named, structurally separate position. A table with labeled columns or a numbered block with labeled fields qualifies. A single prose paragraph covering all obligations does not. |
| C-12 | **Null or falsification framing** -- For at least one major pattern, the output explicitly states what the disconfirming or null condition would look like and whether it was or was not observed in the data. | depth | At least one pattern has an explicit falsification sentence: "If this pattern did not hold, we would expect to see X; instead we observed Y" -- or equivalent null-met / null-not-met reporting. Absence of disconfirming data is acceptable if the null condition is named and its absence noted. |
| C-13 | **Vocabulary precision** -- The output uses only category-precise relationship vocabulary throughout. Every relationship claim specifies its type -- "correlation", "association", "causal (basis: ...)", or a formal equivalent -- without leaving hedged terms ("appears related", "suggests a link", "may indicate", "is associated with") unclassified. | behavior | No unclassified relationship claim appears. Every claim either uses type-precise vocabulary or immediately follows with an explicit label from the permitted set (correlation / association / causal). A single unclassified hedged term that stands alone as the relationship characterization is a FAIL. |
| C-14 | **Pre-registered mechanism** -- The mechanism is stated as an explicit prediction before any data source is analyzed. Each source then adjudicates whether the data confirms or disconfirms the pre-stated mechanism. A synthesis section renders a final mechanism verdict (confirmed / partially confirmed / disconfirmed) rather than proposing a mechanism after the evidence is assembled. | depth | A mechanism prediction appears before the first per-source analysis. At least one per-source block explicitly references the pre-stated mechanism and reports a confirmation verdict. A synthesis section renders a final mechanism verdict using a permitted verdict term. Post-hoc mechanism sentences that appear only in the conclusion do not qualify. |
| C-15 | **Document-wide vocabulary audit** -- The output includes an explicit vocabulary contract listing forbidden hedged terms with their required category-precise replacements, and a compliance check that audits all relationship claims across all sections of the output -- including narrative synthesis text, not only structured table fields -- before the final verdict. | behavior | A vocabulary contract (or equivalent labeled section) is present with at least one forbidden-term / replacement pair. A compliance check section is present and explicitly covers relationship claims outside the analysis table (e.g., synthesis narrative, mechanism section, verdict text). A compliance check that covers only the table column does not qualify. |
| C-16 | **Per-source falsification** -- For each data source analyzed, the output states the source-specific null condition: what this particular source would show if the hypothesis were false. It then reports whether that condition was or was not observed in that source. | depth | At least two data sources each carry an explicit source-specific falsification sentence of the form: "If the hypothesis were false, this source would show X; [we observed / we did not observe] X." A single shared null expectation applied uniformly to all sources does not qualify. |
| C-17 | **Falsification chain traceability** -- Per-source null verdict cells in the analysis table are explicitly constrained to copy from the preamble falsification chain rather than being independently re-derived. The copy instruction appears at the table cell level as a structural constraint, preventing post-hoc drift where the model softens a null verdict after observing the pattern data. | behavior | At least one analysis table cell containing a falsification verdict carries an explicit copy-from-chain instruction (e.g., "Copy from Falsification Chain. Do not rewrite." or equivalent). Independent re-derivation of the null verdict inside the table cell does not qualify. General guidance to "be consistent" does not qualify -- the constraint must be structural, not advisory. |
| C-18 | **Pre-write verdict audit (write-gate)** -- Before the VERDICT section is written, an explicit vocabulary audit is conducted on the planned verdict language as a gate step between the final analysis section and the verdict. The audit fires as a write-gate -- not as a post-hoc correction appended after the verdict is already composed. | behavior | An explicit audit step labeled or structured as occurring before the VERDICT is written appears between the last analysis section and the VERDICT section (e.g., "VERDICT (pre-audit before writing)" framing, or a labeled gate section with explicit pre-write framing). The audit must reference planned verdict language. A compliance check appended after the completed verdict does not qualify. |

Aspirational points: 5 pts each.

---

## Scoring Table

| Tier | Criteria | Count | Max Points |
|------|----------|-------|------------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 5 | 60 |
| Recommended | C-06, C-07, C-08 | 3 | 30 |
| Aspirational | C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18 | 10 | 50 |
| **Total** | | **18** | **140** |

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

## Version History

| Version | Change | Source |
|---------|--------|--------|
| v1 | Initial rubric: 10 criteria, 100 pts | -- |
| v2 | Added C-11, C-12, C-13 from R1 excellence signals; aspirational 10 -> 25 pts; total 100 -> 115; added criteria bleeding failure mode | R1 scorecard |
| v3 | Added C-14 (pre-registered mechanism), C-15 (document-wide vocabulary audit), C-16 (per-source falsification) from R2 excellence signals; aspirational 25 -> 40 pts; total 115 -> 130 | R2 scorecard |
| v4 | Added C-17 (falsification chain traceability), C-18 (pre-write verdict audit) from R3 excellence signals; aspirational 40 -> 50 pts; total 130 -> 140 | R3 scorecard |

### v4 Change Detail

| New Criterion | Source Signal | Upgrades |
|---------------|---------------|---------|
| C-17 (falsification chain traceability) | V-05 R3: "Source null verdict (C-16): Copy from Falsification Chain. Do not rewrite." -- prevents post-hoc drift; model cannot soften a null verdict after observing the pattern because the table cell is constrained to copy, not re-derive | C-16: per-source null condition committed -> per-source verdict locked against post-hoc softening via explicit copy constraint |
| C-18 (pre-write verdict audit / write-gate) | V-05 R3: "VERDICT (pre-audit before writing)" framing -- audits planned verdict language before the verdict section is composed; pattern appears independently in both V-03 and V-05, confirming structural stability | C-15: vocabulary audit covers narrative sections -> audit fires as a write-gate before verdict language is committed, stronger than post-hoc correction |

The pattern holds from R1 through R3: each new aspirational criterion is a structural enforcement upgrade over an existing one (C-17 > C-16, C-18 > C-15). The essential and recommended tiers are unchanged -- these remain correctness and coverage floors, not structural excellence bars.
