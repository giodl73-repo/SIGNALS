---
skill: quest-rubric
skill_target: flow-dataflow
date: 2026-03-15
version: 1
---

# flow-dataflow Rubric — v1

## Purpose

Score a `flow-dataflow` skill output: a data lineage trace covering source, transformation stages, and destination for a Finance, Operations, or Commerce pipeline scenario.

---

## Scoring Formula

```
composite = (essential_pass/N_essential * 60)
          + (recommended_pass/N_recommended * 30)
          + (aspirational_pass/N_aspirational * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria (weight: 60 pts total — must all pass)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-01 | **Data lineage chain** | correctness | Every in-scope data item has an unbroken source => stage(s) => destination chain. No item appears at a destination without an identified origin. |
| C-02 | **Boundary error handling** | correctness | Each inter-stage boundary is annotated: either the error-handling mechanism (retry, dead-letter queue, rollback, compensating transaction) or an explicit "no handling — risk accepted" flag. Silence fails. |
| C-03 | **Data loss point identification** | coverage | At least one concrete, named data loss point per pipeline stage. Generic "errors may occur" does not qualify; a named failure mode does. |
| C-04 | **Schema state at each stage** | correctness | The schema at each stage entry/exit is described or diffed. A stage that alters field names, types, or cardinality with no schema annotation fails. |

---

## Recommended Criteria (weight: 30 pts total)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-05 | **Latency characterization** | depth | Every stage carries a latency annotation: value, range, or characterization (real-time / micro-batch / hourly / daily). A stage with no timing information fails. |
| C-06 | **Stale data windows** | depth | At least one stale window quantified. Failure-mode staleness addressed separately from normal-operation staleness. |
| C-07 | **Domain framing** | format | Domain-specific entity names (Invoice, PurchaseOrder, SKU, LedgerEntry, etc.) appear in the lineage chain. A trace using only "data" or "records" throughout fails. |

---

## Aspirational Criteria (weight: 10 pts total — 5 pts each)

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Recovery prescriptions** | depth | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion naming the mechanism and boundary. Generic advice does not qualify. |
| C-09 | **Pattern trade-off analysis** | behavior | A named alternative pattern (e.g., event sourcing vs. dual-write, CDC vs. polling) with ≥2 explicitly stated trade-off dimensions, at least one quantified in domain terms. |

---

Saved to `simulations/quest/rubrics/flow-dataflow-rubric-2026-03-15.md`.
LedgerEntry, FulfillmentEvent) appear in the lineage chain. A trace that uses only "data" or "records" throughout without naming domain entities fails. |

---

## Aspirational Criteria (weight: 10 pts total)

Weight per criterion: 10 / 2 = **5 pts**. PARTIAL = 50% of criterion weight (2.5 pts).

| ID | Criterion | Category | Pass Condition |
|----|-----------|----------|----------------|
| C-08 | **Recovery prescriptions** | depth | Every "no handling" annotation from C-02 and every loss point from C-03 has a paired, specific recovery suggestion. Generic advice ("add retry logic") does not qualify; the prescription must name the mechanism and at what boundary it applies. |
| C-09 | **Pattern trade-off analysis** | behavior | A named alternative pattern is presented (e.g., event sourcing vs. dual-write, CDC vs. polling sync) with at least two explicitly stated trade-off dimensions comparing it to the chosen approach. At least one dimension must be quantified or qualified in terms of the scenario's domain. |
