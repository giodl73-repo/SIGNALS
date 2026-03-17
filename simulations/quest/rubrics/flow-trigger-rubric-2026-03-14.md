Rubric written to `simulations/quest/rubrics/flow-trigger-rubric-2026-03-14.md`.

**Structure:**
- **4 Essential (C-01–C-04):** trigger enumeration, firing order with sync/async, inputs/outputs per trigger, and explicit pathology detection (storm / missing / circular)
- **3 Recommended (C-05–C-07):** side effects, condition evaluation gates, scenario boundary declaration
- **2 Aspirational (C-08–C-09):** remediation recommendations per pathology, trigger storm quantification against Power Platform limits

**Scoring:** `(essential/4 * 60) + (recommended/3 * 30) + (aspirational/2 * 10)` — golden at all essential pass + composite >= 80.
 triggers that fire for the given change are present; no trigger that fires is omitted |
| C-02 | **Firing Order** — Triggers are listed in the sequence they fire, with synchronous vs. asynchronous execution distinguished | correctness | A clear numbered or ordered sequence is provided; sync/async distinction is explicit for each trigger |
| C-03 | **Inputs and Outputs** — For each trigger, the inputs consumed (triggering record, context data, conditions evaluated) and outputs produced (actions taken, records written, messages sent) are stated | depth | Each trigger entry includes at least one concrete input and one concrete output; generic placeholders like "does something" do not pass |
| C-04 | **Pathology Detection** — The output explicitly identifies or rules out: trigger storms (cascade of triggers from one change), missing triggers (expected automation absent), and circular triggers (A fires B fires A) | coverage | Each of the three pathology types is addressed -- either flagged with evidence or explicitly confirmed absent |

---

## Recommended Criteria (30% of composite score)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Side Effects** -- Downstream side effects beyond the direct output are called out (e.g., a trigger writes a field that itself fires another trigger, an email is sent, a queue message is produced) | depth | At least one side effect is identified per trigger that has one; triggers with no side effects are noted as clean |
| C-06 | **Condition Evaluation** -- Filter conditions, scope settings, and branch logic that determine whether a trigger fires or skips are shown for each trigger | correctness | For each trigger, the condition(s) that gate it are stated; a trigger listed as "always fires" must justify that claim |
| C-07 | **Scenario Boundary** -- The output states what change was simulated (field name, old value to new value, or event type) and which environment / solution context was assumed | format | The triggering change is unambiguous; assumed environment or solution layer is named |

---

## Aspirational Criteria (10% of composite score)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Remediation Recommendations** -- For each pathology found (storm, missing, circular), a concrete remediation is proposed (e.g., add a condition to break the loop, register the missing trigger, throttle the storm with a scope filter) | behavior | Every flagged pathology has at least one actionable remediation; remediations reference specific Power Automate / Copilot Studio constructs |
| C-09 | **Trigger Storm Quantification** -- If a trigger storm is present or at risk, the depth of the cascade is estimated (how many triggers fire in sequence, approximate execution budget consumed) | depth | Storm depth is expressed as a number or bounded range; budget impact is framed in terms of Power Platform request limits or run duration |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Output is trustworthy and production-useful |
| Silver | 60-79 or 1 essential miss | Useful but requires human verification |
| Bronze | 40-59 | Partial signal; major gaps present |
| Fail | < 40 or 2+ essential miss | Not usable; regenerate |
