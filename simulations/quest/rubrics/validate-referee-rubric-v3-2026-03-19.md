Reading the scorecard carefully, I see two new excellence signals to codify as C-14 and C-15. Here is the complete v3 rubric:

---

# validate-referee — Evaluation Rubric v3

**Version**: 3.0
**Date**: 2026-03-19
**Skill**: `validate-referee`
**Change from v2**: Added C-14, C-15 — two aspirational criteria extracted from Round 2 excellence signals.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational (v1) | C-09, C-10 | 10 |
| Aspirational (v2) | C-11, C-12, C-13 | 15 |
| Aspirational (v3 new) | C-14, C-15 | 10 |
| **Max** | | **125** |

Scores above 100 are possible. 100/100 = full v1 compliance. 125/125 = mastery-level simulation.

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
- **C-14** (aspirational v3): Experiential sketch structurally seeds the character brief — V-05 R2 revealed that writing the diverger's experiential sketch once in Phase 2 and then building the character brief from it in Phase 4 creates a structural dependency that prevents persona collapse; C-11 and C-13 treated as parallel requirements (V-04) produce partial grounding; treating the sketch as the seed of the brief (V-05) produces full grounding. The linkage is the mechanism.
- **C-15** (aspirational v3): Brief-grounded strongest-referee rationale — V-05 R2 connected the Phase 5 "strongest referee" designation to the character brief's reviewing history, anchoring editorial dynamics in a concrete persona rather than abstract journal policy; variations that passed C-09 without character briefs cited policy ("PNAS editors desk-reject on power analysis grounds") rather than persona ("this reviewer's history of statistical objections at journals of this tier"); the latter is harder to hedge and more stable across topics

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
| C-13 | All three referee archetypes grounded in concrete experiential detail | depth | 5 | Each referee receives a 2–3 sentence character brief before their report; briefs must pass the swap test — if two briefs could be exchanged without changing any concerns, they are not distinct enough. Applying only to the diverger scores partial (2/5). |

---

## Aspirational Criteria — v3 (10 points total)

*Extracted from Round 2 excellence signals. These distinguish structurally integrated simulation from correctly-executed-but-parallel simulation.*

| ID | Criterion | Category | Points | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-14 | Diverger's experiential sketch in Phase 2 structurally seeds their Phase 4 character brief | behavior | 5 | The diverger's experiential sketch (written when committing to the structural minority view, satisfying C-11) is explicitly referenced as the source when constructing the character brief (satisfying C-13). C-11 and C-13 are treated as a causal chain, not parallel requirements. A skill that writes C-11 and C-13 independently — without the sketch seeding the brief — scores FAIL. |
| C-15 | Strongest-referee rationale is grounded in the character brief's reviewing history, not abstract journal policy | depth | 5 | The C-09 rationale cites a fact from the referee's character brief (e.g., "this reviewer's history of statistical objections at journals of this tier") rather than generic editorial policy (e.g., "PNAS editors desk-reject on power analysis grounds"). Requires C-13 to be satisfied first; if no character briefs exist, C-15 is automatically FAIL. |

---
