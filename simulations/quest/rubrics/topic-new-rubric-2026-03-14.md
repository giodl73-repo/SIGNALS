Rubric written to `simulations/quest/rubrics/topic-new-rubric-2026-03-14.md`.

**Summary of criteria:**

- **5 Essential (C-01–C-05):** TOPICS.md entry exists, strategy at correct path, all 5 signal fields present, valid priority vocabulary, at least one essential signal
- **3 Recommended (C-06–C-08):** Multi-namespace coverage, narrative rationale, differentiated owner roles
- **2 Aspirational (C-09–C-10):** Explicit commit gate defined, item names match artifact convention

The hardest failure mode to catch is C-04 — models tend to substitute "high/medium/low" for the canonical essential/recommended/optional vocabulary. C-05 catches the degenerate case where everything is optional and there's no actual commit gate implied.
 correctness | Every signal row includes all five required fields: namespace, skill, item name, owner role, priority |
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
| C-09 | Strategy defines a commit gate | depth | Strategy explicitly states the minimal signal set required before design commit (e.g., "all essential signals + at least 2 recommended") rather than leaving the gate implicit |
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

## Failure Modes (common disqualifiers)

- TOPICS.md not updated -> C-01 fails -> automatic fail regardless of composite
- Strategy file at wrong path (e.g., `simulations/strategy.md` instead of `simulations/{topic}/strategy.md`) -> C-02 fails
- Signal rows missing fields (e.g., no owner role column) -> C-03 fails
- Priority field contains "high/medium/low" or other non-canonical values -> C-04 fails
- All signals marked recommended/optional with no essential -> C-05 fails
