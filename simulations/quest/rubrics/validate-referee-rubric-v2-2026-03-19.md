Here is the complete updated rubric:

---

# validate-referee — Evaluation Rubric v2

**Version**: 2.0
**Date**: 2026-03-19
**Skill**: `validate-referee`
**Change from v1**: Added C-11, C-12, C-13 — three aspirational criteria extracted from Round 1 excellence signals.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational (v1) | C-09, C-10 | 10 |
| Aspirational (v2 new) | C-11, C-12, C-13 | 15 |
| **Max** | | **115** |

Scores above 100 are possible. 100/100 = full v1 compliance. 115/115 = mastery-level simulation.

---

## Design Decisions

- **C-01/C-03**: Structure completeness — the skill's value is entirely in the three-report + verdict format; partial output is not useful
- **C-02**: Archetype alignment is the core differentiator from generic review; a PNAS paper reviewed by phenomenologists is a correctness failure
- **C-04**: Specificity of concerns separates real simulation from vague hedging
- **C-05**: Artifact persistence is a first-class requirement
- **C-06/C-07/C-08** (recommended): Depth of journal fidelity and differentiation
- **C-09/C-10** (aspirational v1): Editorial dynamics knowledge and minority dissent
- **C-11** (aspirational v2): Pre-report divergence prediction — committing to which referee will diverge *before* writing forces structural minority view rather than emergent behavior; V-01 enforced this and hit 100/100; V-03 omitted it and C-10 scored 2/5
- **C-12** (aspirational v2): Issue Registry with verifiable "Done when" criteria — V-03's labeled registry was "strongest C-08 implementation across all variations"; turns a fix list into a checklist that survives revision
- **C-13** (aspirational v2): Archetype grounded in concrete experiential detail — V-04's coaching register made specificity "more natural and harder to hedge around"; abstract labels alone allow persona collapse

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Points | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | Three complete referee reports present | structure | 12 | Exactly three reports, each with: summary, major concerns (>=2), minor concerns (>=1), recommendation |
| C-02 | Referee archetypes match target journal | correctness | 12 | Personas drawn from journal-appropriate archetypes (PNAS: statistician + domain expert + methodologist; JCS: phenomenologist + cognitive scientist + philosopher of mind; NeurIPS: ML theorist + empiricist + reproducibility advocate) — not generic "Referee 1/2/3" |
| C-03 | Final verdict section contains all required fields | structure | 12 | Includes: editorial decision (ACCEPT / MINOR REVISION / MAJOR REVISION / REJECT), confidence level, P1 blockers, P2 conditions, strongest referee with stated reason |
| C-04 | Major concerns are specific and citable | depth | 12 | Every major concern names a concrete gap — not vague ("needs more rigor") but targeted ("Effect size d is not reported in Table 2; practical significance cannot be assessed") |
| C-05 | Artifact written with required frontmatter | format | 12 | File at signals/validate/referee/{topic}-referee-{date}.md; frontmatter includes skill, topic, date, journal, verdict |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Points | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | Journal-specific language enforced in at least one report | depth | 10 | At least one report uses vocabulary specific to the target journal (PNAS: effect sizes, p-values, N; JCS: phenomenological grounding, first/third-person distinction; NeurIPS: ablations, SOTA, reproducibility) |
| C-07 | Referee recommendations are differentiated | correctness | 10 | At least two distinct recommendation levels appear across the three reports |
| C-08 | Phase 5 fixes ordered by blocking severity and mapped to P1/P2 | coverage | 10 | Three fixes listed most-to-least blocking; Fix 1 = P1 blocker; Fix 2 = P2 consensus; Fix 3 = journal formatting or evidence standards |

---

## Aspirational Criteria — v1 (10 points total)

| ID | Criterion | Category | Points | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | Strongest referee rationale reflects journal editorial dynamics | depth | 5 | Designation cites a reason grounded in how that journal's editorial process actually weights concerns (e.g., "Referee 2's statistical objections carry most weight at PNAS because editors routinely desk-reject on power analysis grounds") |
| C-10 | At least one referee takes a contrarian position | behavior | 5 | One referee visibly diverges from the other two in valence or emphasis — genuine minority view, not three paraphrases of the same critique |

---

## Aspirational Criteria — v2 (15 points total)

*Extracted from Round 1 excellence signals. These distinguish mastery-level simulation from merely correct simulation.*

| ID | Criterion | Category | Points | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-11 | Divergence prediction committed before reports are written | behavior | 5 | Before reports begin, the skill explicitly names which referee archetype is predicted to diverge and why — a structural commitment, not emergent discovery. The prediction is falsifiable against the reports that follow. |
| C-12 | Fix plan uses a labeled registry with verifiable completion criteria | coverage | 5 | Fixes presented as a labeled registry (I-01, I-02, I-03) with severity tier (P1/P2/P3), fix description, and a "Done when" condition checkable against a revised manuscript — not merely a prioritized prose list |
| C-13 | At least one referee archetype is grounded in concrete experiential detail | depth | 5 | At least one referee persona includes a specific experiential qualifier shaping their lens (e.g., "has reviewed three failed replications in this area", "sits on the statistical methods board") rather than an abstract label alone |

---

## Scoring Guide

| Score | Interpretation |
|-------|----------------|
| 115/115 | Mastery — all three v2 excellence patterns present |
| 100–114 | Full v1 compliance; partial mastery-level signals |
| 90–99 | Strong — minor gaps in recommended or v1 aspirational tier |
| 75–89 | Adequate — essential structure present, meaningful depth gaps |
| 60–74 | Marginal — essential criteria met, recommended tier largely absent |
| < 60 | Fail — structural incompleteness; one or more essential criteria missed |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-19 | Initial — 5 essential, 3 recommended, 2 aspirational (100 pts max) |
| v2 | 2026-03-19 | Added C-11, C-12, C-13 from Round 1 scorecard signals (115 pts max) |

---

**Three new criteria added.** The evidence base for each:

- **C-11** (divergence prediction before writing): V-01 enforced this explicitly and hit 100/100 on C-10; V-03 had no such instruction and scored 2/5. The delta is causal — naming the predicted outlier in advance is what makes the minority view structural rather than accidental.
- **C-12** (labeled registry with "Done when"): V-03's Issue Registry was the only variation to label fixes with verifiable completion conditions; the scorecard called it "strongest C-08 implementation across all variations." The other variations produced prose lists that require interpretation to apply.
- **C-13** (experiential grounding for archetypes): V-04's coaching register phrasing — "sound like someone who reviewed three failed replications last month" — was credited with making specificity "more natural and harder to hedge around." Variations using abstract labels only (V-02, V-03) showed higher risk of persona collapse.
ntial criteria missed |

---

## Changelog

| Version | Date | Change |
|---------|------|--------|
| v1 | 2026-03-19 | Initial rubric — 5 essential, 3 recommended, 2 aspirational (100 pts max) |
| v2 | 2026-03-19 | Added C-11, C-12, C-13 from Round 1 scorecard signals (115 pts max) |
