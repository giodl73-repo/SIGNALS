---
skill: quest-rubric
skill_target: topic-retro
date: 2026-03-16
version: 1
---

# Rubric: topic-retro

Post-commitment retrospective on a topic's signals. Evaluates whether the output correctly reconstructs the signal record, scores prediction accuracy, identifies coverage gaps, and surfaces the one unexpected learning (Echo).

---

## Essential Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Signal inventory is present and complete** | correctness | essential | Output lists every signal gathered for the topic (by namespace or artifact name). At minimum: signal count, namespace distribution. Fails if signals are omitted or invented. |
| C-02 | **Predicted vs actual outcome is stated for each signal type** | correctness | essential | For each signal (or signal category), output states what the signal predicted and what actually happened post-ship. Both sides must be explicit — not implied. |
| C-03 | **Gaps section identifies signals that were absent** | coverage | essential | Output names at least one signal type that was not gathered but, with hindsight, would have changed or refined the commit decision. May be "none" only if explicitly argued. |
| C-04 | **Echo section is present and names exactly one unexpected learning** | correctness | essential | Output contains a section titled Echo (or equivalent) with a single finding that was not predicted by any gathered signal. Must be post-ship observable, not a known unknown at commit time. |
| C-05 | **Accuracy verdict is rendered** | correctness | essential | Output provides an overall accuracy judgment — e.g., score, ratio, or qualitative rating — for the signal set as a whole. Must be grounded in the predicted vs actual comparisons in C-02. |

---

## Recommended Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Gap signals are actionable for future topics** | depth | recommended | Each gap in C-03 is accompanied by a concrete suggestion: which skill to run, what question to ask, or what threshold to set. Generic advice ("gather more signals") does not pass. |
| C-07 | **Signal accuracy is differentiated by namespace** | depth | recommended | Accuracy is broken down per namespace (scout, draft, flow, etc.) rather than averaged into a single number. Allows teams to identify which namespaces are consistently reliable vs noisy. |
| C-08 | **AMEND scope is respected when provided** | behavior | recommended | If an AMEND instruction limits scope (specific signal type or time window), the output honors that constraint throughout — inventory, accuracy, gaps, and Echo all stay within scope. |

---

## Aspirational Criteria

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Calibration trend is surfaced** | depth | aspirational | Output compares this topic's signal accuracy to a prior retro for the same team or namespace, identifying whether prediction quality is improving, degrading, or stable. Requires at least one prior retro as reference. |
| C-10 | **Echo feeds back into signal design** | depth | aspirational | The Echo finding is translated into a concrete change proposal: a new skill, a rubric amendment, or a threshold adjustment. Not just "we learned X" but "therefore we should do Y differently." |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Score | Meaning |
|------|-------|---------|
| Golden | 80-100, all essential pass | Retro is complete and trustworthy |
| Passing | 60-79 or 1 essential miss | Usable but has a notable gap |
| Failing | < 60 or 2+ essential miss | Retro is incomplete; do not use to improve signal design |

---

## Notes

- C-01 and C-02 are the load-bearing criteria: a retro without a full signal inventory or explicit predicted-vs-actual comparison cannot be scored or acted on.
- C-04 (Echo) is non-negotiable: it is the primary learning mechanism of the retro format. An output that omits Echo or lists multiple echoes fails this criterion.
- C-08 applies only when an AMEND instruction is present; if no AMEND is given, mark as pass by default.
- C-09 requires prior retro data; if this is the first retro for a topic, mark as not applicable (counts as pass for scoring).
