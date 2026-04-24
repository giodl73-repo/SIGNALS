---
skill: quest-rubric
skill_target: topic-open
date: 2026-03-17
version: 1
---

# Rubric: topic-open (v1)

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Outputs**: entry in `TOPICS.md` + `simulations/{topic}/strategy.md`

---

## Essential Criteria (60% of composite)

Must all pass. Without these the output is not useful.

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | TOPICS.md entry exists | correctness | `simulations/TOPICS.md` contains a row for the new topic with at least: topic slug, short description, and start date |
| C-02 | Strategy file at correct path | correctness | Strategy written to `simulations/{topic}/strategy.md` — not to a flat path, not inline in TOPICS.md |
| C-03 | All five signal fields present | correctness | Every signal row contains all five required fields: namespace, skill, item name, owner role, priority — no field omitted or collapsed |
| C-04 | Priority vocabulary is valid | correctness | Every signal priority value is exactly one of: `essential` / `recommended` / `optional` — no substitutions (high/medium/low or other) |
| C-05 | At least one essential signal declared | coverage | Strategy contains at least one signal marked `essential` — a topic with no essential signals has no defined commit gate |

---

## Recommended Criteria (30% of composite)

Output is better with these.

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Signal set spans multiple namespaces | coverage | Planned signals reference at least 2 distinct namespaces from: scout, draft, review, flow, trace, prove, listen, program, topic |
| C-07 | Strategy includes a prose rationale | depth | Strategy file contains a prose section (>= 2 sentences) explaining why this topic needs investigation and what decision the signals are meant to inform |
| C-08 | Owner roles are differentiated | depth | At least 2 distinct owner roles appear across the planned signals — signals must not all default to a single generic role |

---

## Aspirational Criteria (10% of composite)

Raise the bar once essential and recommended are stable.

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines an explicit commit gate | depth | Strategy contains a named COMMIT GATE section listing the exact minimal signal set (by item name) that must exist before design commit — gate is not left implicit |
| C-10 | Signal item names follow artifact naming convention | format | All item names follow the `{topic}-{signal}-{date}.md` pattern or are expressed as parameterized templates matching that convention |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Criterion Notes

- **C-04** is the most common failure mode: models substitute `high/medium/low` for the canonical
  `essential/recommended/optional` vocabulary, making the strategy unusable as a commit gate.
- **C-05** catches the degenerate case where every signal is `optional` — no essential signal means
  no commit gate and the strategy provides no design readiness signal.
- **C-07** distinguishes a useful strategy from a pure mechanical table — the rationale is what
  connects the signal plan to an actual decision that needs to be made.
- **C-09** makes the implied gate explicit: a strategy that lists essential signals but never names
  the gate condition forces the consumer to infer it.
- **C-10** makes artifacts discoverable by `topic-scanner`; item names that don't follow the
  convention break glob-based coverage computation downstream.
