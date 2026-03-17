---
skill: quest-rubric
skill_target: campaign-brief
date: 2026-03-16
version: 1
---

# Rubric: campaign-brief

`campaign-brief` runs the full topic narrative campaign, orchestrating four sub-skills in sequence — topic-new (register), topic-roadmap/plan (plan signals), topic-status (current coverage), topic-story (narrative synthesis) — and delivering a complete topic dashboard. It is designed to bookend signal-gathering sessions: run at the start to orient, run at the end to assess readiness.

---

## Scoring Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 total, ~12 each)

Must all pass. Without these, the output is not useful.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Orchestration completeness** | correctness | Output demonstrates all four sub-skills were invoked in order: topic-new/register, topic-plan/roadmap, topic-status, topic-story. Each stage's output is present or explicitly summarized in the dashboard. Skipping any stage is a fail. |
| C-02 | **Signal inventory** | coverage | Output enumerates existing signals for the topic, attributed by namespace (e.g., scout/competitors, flow/trigger). Generic "signals exist" with no enumeration is a fail. At least one artifact name or namespace hit must be cited. |
| C-03 | **Gap identification** | coverage | Output explicitly lists signals that are planned but absent — the missing evidence needed before commit. A coverage table showing zero gaps on an incomplete topic is a fail. Must name at least one missing signal type when gaps exist. |
| C-04 | **Narrative arc** | depth | Output includes a topic-story synthesis: a coherent narrative connecting existing signals toward a decision. A flat list of artifacts with no synthesis is a fail. The narrative must state what the signals say *together*, not just enumerate them. |
| C-05 | **Topic registration** | correctness | The topic is named, described, and anchored in the session — either confirming an existing TOPICS.md entry or registering a new one. Output without topic identity (name, start date, intent) is a fail. |

---

## Recommended Criteria (weight: 30 total, 10 each)

Output is better with these. Missing one lowers the score but does not block golden.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-06 | **Readiness verdict** | behavior | Output includes an explicit readiness signal: ready / not ready / conditional, with a one-sentence rationale. A dashboard that reports coverage without a commit recommendation is a partial fail on this criterion. |
| C-07 | **Prioritized gap list** | depth | Missing signals are ordered by priority (e.g., blocking vs. optional, earlier stage vs. later stage). An unordered gap list fails this criterion. At minimum, "blocking gaps" must be distinguished from "nice-to-have signals". |
| C-08 | **Scannable dashboard format** | format | The output is structured for at-a-glance reading: uses headers or sections for each sub-skill output, a coverage table or status block, and a summary verdict. Prose-only output with no visual hierarchy fails this criterion. |

---

## Aspirational Criteria (weight: 10 total, 5 each)

Raise the bar once essential and recommended are stable.

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-09 | **Session delta awareness** | behavior | When invoked at the end of a session (signals exist), output shows what changed relative to an implicit or explicit baseline: signals added this session, coverage delta, how the story evolved. A first-run invocation may skip this without penalty; an end-of-session invocation that omits delta fails. |
| C-10 | **Narrative confidence level** | depth | The topic-story synthesis includes an explicit confidence rating on the overall narrative arc (e.g., low / medium / high, or a numeric scale) with a brief rationale. A narrative that synthesizes without calibrating its own certainty fails this criterion. |

---

## Criterion Summary Table

| ID | Text (short) | Weight | Category |
|----|--------------|--------|----------|
| C-01 | All four sub-skills invoked in sequence | essential | correctness |
| C-02 | Existing signals enumerated by namespace | essential | coverage |
| C-03 | Missing signals explicitly listed | essential | coverage |
| C-04 | Narrative arc synthesizes signals together | essential | depth |
| C-05 | Topic registered with name, date, intent | essential | correctness |
| C-06 | Explicit readiness verdict with rationale | recommended | behavior |
| C-07 | Gap list prioritized (blocking vs. optional) | recommended | depth |
| C-08 | Scannable dashboard with visual hierarchy | recommended | format |
| C-09 | Session delta shown when signals exist | aspirational | behavior |
| C-10 | Narrative confidence level with rationale | aspirational | depth |

---

## Scoring Example

All 5 essential pass, 2 of 3 recommended pass, 0 of 2 aspirational pass:

```
composite = (5/5 * 60) + (2/3 * 30) + (0/2 * 10)
          = 60 + 20 + 0
          = 80
```

Result: golden threshold met (all essential pass, composite = 80).

---

## Notes for Rubric Evolution

- C-02 and C-03 are the core diagnostic pair — a dashboard that can't tell you what you have AND what you're missing isn't a dashboard.
- C-04 is what distinguishes campaign-brief from a plain `topic-status` run — if narrative is absent, the orchestration value is not realized.
- C-09 becomes more important as campaign-brief is tested on end-of-session invocations. Promote to recommended when the skill is used in session-pair mode consistently.
- C-10 can be merged with C-04 if confidence becomes standard narrative output.
