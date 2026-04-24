---
skill: quest-rubric
skill_target: flow-trigger
date: 2026-03-15
version: 1
---

# Rubric: flow-trigger

Evaluates simulated output for the `flow-trigger` skill — which automations fire when a record changes, in what order, with what inputs/outputs and side effects, and whether trigger anomalies (storms, gaps, cycles) are correctly identified.

---

## Scoring Formula

```
composite = (essential_pass / N_essential * 60)
          + (recommended_pass / N_recommended * 30)
          + (aspirational_pass / N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 points total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Trigger enumeration is complete** -- for each field/event change in the scenario, every automation that fires is listed by name. No trigger is silently omitted. | correctness | All triggers for the stated change are present; no expected trigger is missing from the output. |
| C-02 | **Firing order is stated** -- triggers are sequenced (1, 2, 3... or "simultaneous") and the ordering rationale is traceable (e.g., synchronous before async, priority rules, platform execution model). | correctness | Output shows an explicit ordered list or sequence annotation; "fires in parallel" is acceptable if correct for the platform. |
| C-03 | **Each trigger has inputs and outputs documented** -- for every trigger listed, the input record/payload and the output action or record mutation are identified. | depth | Every trigger entry includes at least one input field and one output or side-effect. Entries with neither fail this criterion. |
| C-04 | **Trigger anomalies are assessed** -- the output explicitly addresses all three anomaly classes: trigger storms (excessive fires per change), missing triggers (expected automation absent), circular triggers (A fires B fires A). Each class is either confirmed present or confirmed absent for the scenario. | coverage | All three anomaly classes appear in the output with a finding (detected or not detected). Silence on any class fails. |

---

## Recommended Criteria (weight: 30 points total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-05 | **Side effects are enumerated per trigger** -- notifications sent, records created/updated elsewhere, external API calls, queue messages, or UI state changes are called out explicitly rather than implied. | depth | At least one trigger in the output carries a side-effect annotation beyond the primary output. Outputs with zero side-effect annotations fail this criterion. |
| C-06 | **Trigger conditions and filters are stated** -- for each trigger, the condition(s) that caused it to fire (field value threshold, record state, role/context filter) are documented so a reader can predict when the trigger would NOT fire. | correctness | Each trigger entry includes at least one "fires when X" or "does not fire when Y" clause. Generic "fires on change" with no condition detail fails. |
| C-07 | **Platform role is grounded** -- the output applies Power Automate / Copilot Studio domain knowledge (e.g., instant vs scheduled vs automated flows, connector triggers, Dataverse plugin steps vs Power Automate, expression-based conditions) to explain behavior rather than treating triggers as abstract events. | behavior | At least two platform-specific terms or constraints appear and are used correctly in context. |

---

## Aspirational Criteria (weight: 10 points total)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-08 | **Anomalies carry remediation guidance** -- for each detected anomaly (storm, gap, cycle), the output proposes a concrete fix: debounce strategy, missing trigger registration, cycle-break condition, or re-sequencing. | depth | Every detected anomaly has at least one actionable remediation step. Outputs with detected anomalies and no guidance fail this criterion. |
| C-09 | **Trigger map is provided** -- the output includes a structured summary table or diagram mapping change event to trigger name to order to output to anomaly flag, enabling at-a-glance review of the full automation surface. | format | A table or structured list covers all triggers with at minimum: trigger name, order/position, and anomaly flag (none / storm / cycle / missing). |

---

## Criterion Summary

| ID | Weight Class | Category | Short Name |
|----|-------------|----------|------------|
| C-01 | essential | correctness | Complete trigger enumeration |
| C-02 | essential | correctness | Firing order stated |
| C-03 | essential | depth | Inputs and outputs per trigger |
| C-04 | essential | coverage | All three anomaly classes assessed |
| C-05 | recommended | depth | Side effects enumerated |
| C-06 | recommended | correctness | Trigger conditions stated |
| C-07 | recommended | behavior | Platform grounding |
| C-08 | aspirational | depth | Anomaly remediation guidance |
| C-09 | aspirational | format | Trigger map provided |

---

## Scoring Examples

**Minimal pass (score = 80)**
All 4 essential pass (60 pts) + 2 of 3 recommended pass (20 pts) + 0 aspirational (0 pts) = 80.

**Strong output (score = 90)**
All 4 essential (60) + all 3 recommended (30) + 0 aspirational (0) = 90.

**Full score (score = 100)**
All 4 essential (60) + all 3 recommended (30) + both aspirational (10) = 100.

**Failing output**
Any essential criterion fails -> output does not meet golden threshold regardless of composite score.
