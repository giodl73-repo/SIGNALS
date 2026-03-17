Reading the scorecard closely, I see two excellence patterns that drove perfect scores in V-01 and V-05 that aren't yet captured as criteria:

1. **Named rule + invocation pairing** — V-05 declares rules (FALSIFICATION RULE, CALIBRATION RULE, ATTRIBUTION RULE) at a preamble block, then explicitly invokes them by name at the point of use. V-01 has inline notes but no named rule system. The pattern of *declare once, invoke by name* is structurally stronger than prose warnings embedded in steps.

2. **Hypothesis reordering rationale stated** — Both V-01 and V-05 passed C-10 by reordering stages. But V-05 also explains *why*: "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." V-01 makes it structural without stating the principle. Encoding the rationale makes the decision auditable and transferable.

These become C-13 and C-14. Aspirational pool goes from 5 to 7, so the formula denominator updates accordingly.

---

```markdown
---
skill: quest-rubric
skill_target: campaign-evidence
date: 2026-03-16
version: 3
---

# Rubric: campaign-evidence

Evaluates whether the skill ran the full evidence campaign and produced a complete evidence brief with confidence levels and falsification status.

---

## Essential Criteria (60 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **All five prove skills executed** | behavior | Output shows evidence from all five stages: prove-hypothesis, prove-websearch, prove-intelligence, prove-analysis, prove-synthesize — each contributes a named section or labeled artifact block. Missing any one stage fails. |
| C-02 | **Confidence level assigned per finding** | correctness | Every significant finding carries an explicit confidence level (e.g., High / Medium / Low or numeric) — not a single summary rating but per-claim labels. At least 3 distinct findings must carry individual confidence ratings. |
| C-03 | **Falsification status declared** | correctness | The brief includes a falsification section or per-hypothesis status — at minimum "supported", "refuted", or "indeterminate" for each hypothesis. A brief with no falsification status at all fails. |
| C-04 | **Evidence brief is self-contained** | format | The output is a single coherent document (not a collection of raw dumps). It has a title, topic context, and synthesized narrative — a reader unfamiliar with the run can understand what was investigated and what was found. |

## Recommended Criteria (30 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Source attribution per claim** | depth | Claims are linked to their source stage (e.g., "per web search", "per intelligence review"). At least 70% of material claims carry stage attribution. |
| C-06 | **Synthesis section distinguishes consensus from conflict** | depth | The synthesize stage output explicitly identifies where prove-websearch and prove-intelligence agree vs. diverge, not just lists findings side-by-side. |
| C-07 | **Confidence levels are calibrated, not uniform** | correctness | Confidence ratings vary across findings — a brief where every finding is "Medium" fails this criterion. Distribution must show at least two distinct levels used meaningfully. |

## Aspirational Criteria (10 pts)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Gaps and open questions surfaced** | coverage | The brief closes with an explicit list of what remains unknown or under-evidenced after the full campaign, enabling a follow-up investigation to pick up cleanly. |
| C-09 | **Decision readiness signal included** | behavior | The brief includes a final verdict on whether the evidence is sufficient to proceed (e.g., "Ready to commit", "Needs more investigation on X") — not just findings but an actionable posture statement. |
| C-10 | **Hypotheses declared post-evidence** | correctness | Hypotheses are finalized or formally stated *after* the web search and intelligence stages complete — not pre-committed before evidence gathering. Falsification decisions grounded in actual findings rather than confirmed against pre-anchored assumptions. A campaign that states hypotheses only in prove-hypothesis *before* any evidence gathering fails this criterion. |
| C-11 | **Explicit calibration anti-pattern guard** | correctness | The brief or its process includes an explicit check against uniform confidence ratings — e.g., a stated rule or reviewer note that "if all findings carry the same confidence level, calibration is insufficient." A bare scale definition without an anti-uniformity guard does not pass. |
| C-12 | **Decision readiness compressed to a single verdict sentence** | behavior | The decision readiness signal (C-09) is expressed as one actionable sentence that names a posture and, if not ready, names the specific gap — e.g., "Ready to proceed" or "Needs more investigation on regulatory approval timeline before committing." Multi-paragraph readiness discussions do not pass; the compression itself is the signal. |
| C-13 | **Named rules declared at preamble and invoked at point of use** | correctness | The brief's governing rules (falsification, attribution, calibration) are declared as named identifiers in a preamble or header block and then explicitly invoked by name at the step where they apply — not only embedded as inline prose warnings. A brief with unnamed in-place notes but no declared rule identifiers does not pass. |
| C-14 | **Hypothesis reordering rationale stated** | correctness | When the campaign places hypothesis declaration after evidence gathering (C-10), the brief explicitly states *why* — a rationale sentence such as "A hypothesis anchored before evidence gathering is a bias, not a hypothesis." Passing C-10 by reordering stages without encoding the underlying principle does not pass this criterion. |

---

## Scoring

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/7 * 10)
```

**Golden threshold**: all 4 essential pass AND composite ≥ 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | ≥ 80, all essential | Ship-ready output |
| Silver | ≥ 60, all essential | Usable with gaps |
| Bronze | all essential pass | Minimum viable brief |
| Fail | any essential miss | Not useful |
```

---

Two criteria added, one formula change:

- **C-13** captures the V-05 structural pattern: rules named at preamble level and invoked by identifier at point of use. The distinction from C-11 is about *naming discipline* — C-11 requires a guard exists, C-13 requires the guard be part of a declared rule system that can be referenced.
- **C-14** captures why V-05 earns the design rationale credit that V-01 does not: reordering stages is necessary (C-10) but articulating the principle behind the reorder makes the decision legible to anyone reading the brief cold.
- Formula denominator: `5 → 7` for the aspirational tier.
