```markdown
---
skill: quest-rubric
skill_target: campaign-evidence
date: 2026-03-16
version: 2
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

---

## Scoring

```
composite = (essential_pass/4 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/5 * 10)
```

**Golden threshold**: all 4 essential pass AND composite ≥ 80.

| Band | Score | Meaning |
|------|-------|---------|
| Gold | ≥ 80, all essential | Ship-ready output |
| Silver | ≥ 60, all essential | Usable with gaps |
| Bronze | all essential pass | Minimum viable brief |
| Fail | any essential miss | Not useful |
```
