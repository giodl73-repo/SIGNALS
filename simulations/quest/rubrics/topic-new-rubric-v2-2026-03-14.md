Here is the complete updated rubric:

---

# Rubric: topic-new — v2

**Skill**: `topic:new`
**Version**: v2
**Date**: 2026-03-14
**Promoted from**: v1 + R1 excellence signals

**Summary of criteria:**

- **5 Essential (C-01–C-05):** TOPICS.md entry exists, strategy at correct path, all 5 signal fields present, valid priority vocabulary, at least one essential signal
- **3 Recommended (C-06–C-08):** Multi-namespace coverage, narrative rationale, differentiated owner roles
- **5 Aspirational (C-09–C-13):** Explicit commit gate defined, item names match artifact convention, checkbox-gate self-verification before phase transition, operational-consequence framing for invalid vocabulary, dedicated section per aspirational criterion

The hardest failure mode to catch is C-04 — models tend to substitute "high/medium/low" for the canonical essential/recommended/optional vocabulary. C-05 catches the degenerate case where everything is optional and there's no actual commit gate implied. **C-11–C-13 are structural excellence signals**: they do not change whether a strategy is valid, but they predict whether the prompt will reliably produce valid strategies across diverse inputs.

---

## Essential Criteria (60% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | TOPICS.md entry exists | artifact | `simulations/TOPICS.md` contains a row for the new topic with at least: topic name, status, and strategy path |
| C-02 | Strategy file at correct path | artifact | Strategy written to `simulations/{topic}/strategy.md` -- not to a flat path, not inline in TOPICS.md |
| C-03 | All five signal fields present | correctness | Every signal row includes all five required fields: namespace, skill, item name, owner role, priority |
| C-04 | Priority values are valid | correctness | Every signal priority is one of: essential / recommended / optional -- no other values present |
| C-05 | At least one essential signal planned | coverage | Strategy contains at least one signal marked essential -- a topic with no essential signals has no defined commit gate |

---

## Recommended Criteria (30% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | Signal set spans multiple namespaces | coverage | Planned signals reference at least 2 distinct namespaces from: scout, draft, review, flow, trace, prove, listen, program, topic |
| C-07 | Strategy includes a narrative rationale | depth | Strategy file contains a prose section (>= 2 sentences) explaining why this topic needs investigation and what decision it informs |
| C-08 | Owner roles are differentiated | depth | At least 2 distinct owner roles appear across the planned signals (e.g., PM, engineer, designer, researcher) -- signals should not all default to a single generic role |

---

## Aspirational Criteria (10% of composite)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | Strategy defines a commit gate | depth | Strategy explicitly states the minimal signal set required before design commit rather than leaving the gate implicit |
| C-10 | Signal item names follow artifact naming convention | format | All item names follow the `{topic}-{signal}-{date}.md` pattern or are expressed as parameterized templates matching that convention |
| C-11 | Prompt includes checkbox-gate before phase transition | structure | Prompt contains a pre-transition checklist that forces coverage self-verification before the model proceeds to the next phase -- eliminates silent criterion omissions |
| C-12 | Invalid vocabulary framed as operational consequence | framing | Prompt states the harm of invalid priority values in terms of downstream failure ("strategy cannot be used as a commit gate") rather than as a style preference or generic warning |
| C-13 | Each aspirational criterion has a dedicated section | structure | C-09 and C-10 each appear as their own named section or heading in the prompt template -- not as inline reminders or parenthetical notes |

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 5 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

---

## Three changes from v1

1. **C-11, C-12, C-13 added** — extracted from the three new_patterns in the R1 scorecard. These are prompt-structure criteria, not output criteria: they assess whether the variation was engineered to prevent failure, not just whether the output happened to pass.

2. **Aspirational denominator bumped from 2 to 5** — the 10% weight is now spread across five criteria. A variation that only satisfies C-09 and C-10 scores 4 points on aspirational instead of 10. The full 10 now requires all three structural patterns.

3. **Excellence Signals section added** — records the R1 observations that motivated each new criterion, so future rubric authors know which evidence they're building on.
C-13:

| Pattern | Criterion | Observation |
|---------|-----------|-------------|
| Checkbox-gate before phase transition | C-11 | Forces coverage self-verification; variations with pre-transition checklists had zero silent criterion omissions across all five signal fields |
| Operational-consequence framing | C-12 | Tying invalid vocabulary to "strategy cannot be used as a commit gate" was more reliable than generic WARNING labels; consequence framing persisted across varied inputs |
| Dedicated section per aspirational criterion | C-13 | C-09 and C-10 treated as inline reminders were skipped on sparse inputs; each as its own section heading eliminated skipping entirely |
