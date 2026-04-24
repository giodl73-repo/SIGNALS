Reading the scorecard carefully, I see two new excellence signals to codify as C-16 and C-17. Here is the complete v4 rubric:

---

# validate-referee — Evaluation Rubric v4

**Version**: 4.0
**Date**: 2026-03-19
**Skill**: `validate-referee`
**Change from v3**: Added C-16, C-17 — two aspirational criteria extracted from Round 3 excellence signals.

---

## Scoring Summary

| Tier | Criteria | Points |
|------|----------|--------|
| Essential | C-01 through C-05 | 60 |
| Recommended | C-06 through C-08 | 30 |
| Aspirational (v1) | C-09, C-10 | 10 |
| Aspirational (v2) | C-11, C-12, C-13 | 15 |
| Aspirational (v3) | C-14, C-15 | 10 |
| Aspirational (v4 new) | C-16, C-17 | 10 |
| **Max** | | **135** |

Scores above 100 are possible. 100/100 = full v1 compliance. 135/135 = mastery-level simulation with generation-time enforcement.

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
- **C-16** (aspirational v4): Self-verification instruction embedded in the prompt — V-05 R3 revealed that inserting "if X still makes full sense without Y, rewrite X" turns a review-time compliance check into a generation-time check; V-04 R3's verbatim-anchor requirement was checkable only after output was produced; V-05 R3's SEED/EXPAND with the removal test lets the model detect non-compliance *while writing*; the difference is between "did the output comply?" and "could the model detect non-compliance during generation?"; any structural dependency criterion that lacks a self-verification test is enforced less reliably
- **C-17** (aspirational v4): Anti-pattern vaccination with a plausible-looking FORBIDDEN example — V-02 R3 showed that labeling a fluent-but-wrong form FORBIDDEN is more effective than labeling an obviously wrong one; if the FORBIDDEN example looks bad, it does not vaccinate against the actual failure mode; the failure mode is the default generation path, which is always fluent; V-04 and V-05 R3 confirmed this generalizes — FORBIDDEN/REQUIRED templates consistently closed the gap between partial and full compliance on both C-14 and C-15; the mechanism is removing the lower-friction path, not describing the higher-friction one

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
| C-11 | Diverger identity committed before reports are written | behavior | 5 | Phase 2 (or equivalent pre-writing step) explicitly names which referee will diverge and in which direction — not inferred retrospectively from the reports |
| C-12 | Issue Registry uses verifiable "Done when" criteria | coverage | 5 | Each fix in Phase 5 includes a testable completion condition ("Done when Table 2 reports Cohen's d with 95% CI"), not a vague directive ("add effect sizes") |
| C-13 | Archetype grounded in concrete experiential detail | depth | 5 | Each referee persona includes at least one concrete career or reviewing experience that explains their disposition — not just a label ("statistician") but a sketch ("trained as a biostatistician; spent five years reviewing clinical trials where underpowered studies caused harm") |

---

## Aspirational Criteria — v3 (10 points total)

*Extracted from Round 2 excellence signals. These address the mechanism by which persona grounding is enforced across phases.*

| ID | Criterion | Category | Points | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-14 | Experiential sketch structurally seeds the character brief | behavior | 5 | The Phase 2 experiential sketch is explicitly designated as the source of the Phase 4 character brief — brief must open with or derive from the sketch verbatim; a brief that is consistent with the sketch but not causally derived from it does not pass |
| C-15 | Strongest-referee rationale is grounded in character brief content | depth | 5 | The Phase 5 "strongest referee" designation cites a specific fact from that referee's character brief or reviewing history — not generic journal policy; a rationale that could have been written without the character briefs existing does not satisfy this criterion |

---

## Aspirational Criteria — v4 (10 points total)

*Extracted from Round 3 excellence signals. These address generation-time enforcement: prompts that make compliance checkable while the model is writing, not only after output is produced.*

| ID | Criterion | Category | Points | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-16 | Structural dependency enforced by embedded self-verification test | enforcement | 5 | Any structural dependency between phases (e.g., brief derived from sketch, rationale derived from brief) is accompanied by a generation-time removal test of the form "if X still makes full sense without Y, rewrite X so that it depends on Y" — the test must be embedded in the prompt instruction, not noted as a post-hoc review criterion |
| C-17 | Anti-pattern vaccination uses a plausible-looking FORBIDDEN example | enforcement | 5 | Where a default generation path produces fluent-but-wrong output (e.g., policy-form rationale, sketch-independent brief), the prompt shows that exact plausible form labeled FORBIDDEN alongside the correct form labeled REQUIRED; a FORBIDDEN example that looks obviously wrong does not vaccinate against the actual failure mode |
