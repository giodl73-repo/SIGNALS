---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 1
---

# Rubric: flow-lifecycle

Scoring rubric for the `flow-lifecycle` skill. This skill simulates a multi-step business
document lifecycle (L2O, P2P, period close, case lifecycle): walks every step with entry
conditions, state transitions, decision points, parallel paths, exception flows, and terminal
states. Surfaces bottlenecks, missing steps, and unhandled edge cases. Domain roles are
auto-selected from process context.

## Composite Score Formula

```
score = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

Where `_pass` counts full passes as 1.0. N = count of criteria in each tier.

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria

> All must pass. Without these the output is not useful.

### C-01 -- State Transition Coverage
- **Weight**: essential
- **Category**: correctness
- **Text**: Every lifecycle step is traced with (a) a named state, (b) the condition required
  to enter it, and (c) the event or action that advances to the next state. No step is implied
  or left in prose without a named state and explicit trigger.
- **Pass condition**: At least 6 distinct named states appear for the chosen lifecycle. Each
  state has an explicit entry trigger and an explicit exit trigger. No transition reads "then X
  happens" without naming the cause.

### C-02 -- Exception Flow Traces
- **Weight**: essential
- **Category**: coverage
- **Text**: The output does not stop at the happy path. At least one exception or failure branch
  per major lifecycle phase is traced -- with the trigger condition, the divergence point from
  the main sequence, and the outcome (recovery state or terminal failure).
- **Pass condition**: At least 3 exception flows are present. Each names: (1) the triggering
  condition, (2) the phase and step where it fires, (3) the recovery action or terminal failure
  state reached. A note that "errors can occur" is not an exception flow.

### C-03 -- Terminal State Completeness
- **Weight**: essential
- **Category**: correctness
- **Text**: All terminal states -- both success outcomes and failure/cancel endpoints -- are
  explicitly named and labeled. No traced path leads to an unnamed dead end.
- **Pass condition**: At least 2 terminal states present: one labeled success (e.g., "Invoice
  Paid," "Order Fulfilled") and one labeled failure or cancel (e.g., "Rejected -- No Resubmit,"
  "Voided"). Every traced path reaches a named terminal.

### C-04 -- Bottleneck and Gap Identification
- **Weight**: essential
- **Category**: depth
- **Text**: The output explicitly identifies states or transitions where work stalls, approvals
  queue, or handoffs fail. Each bottleneck names the step, the cause (manual gate, role
  dependency, external system), and the process impact. At least one process gap -- a step the
  lifecycle design omits but real-world execution requires -- is also identified.
- **Pass condition**: At least 2 bottlenecks named with cause and impact. At least 1 process
  gap identified with the missing step named and the consequence stated.

### C-05 -- Domain Role Assignment
- **Weight**: essential
- **Category**: correctness
- **Text**: Each major step or decision point is owned by a domain-specific role drawn from the
  lifecycle context. Generic placeholders ("User," "Admin," "System") do not qualify.
- **Pass condition**: At least 3 distinct named domain roles appear (e.g., Account Executive,
  AP Clerk, Controller, Support Agent). Each role assignment is tied to a specific step or
  decision gate. No decision gate is left unowned.

---

## Recommended Criteria

> Output is meaningfully better with these.

### C-06 -- Parallel Path Modeling
- **Weight**: recommended
- **Category**: depth
- **Text**: Concurrent activities within the lifecycle (e.g., credit check + inventory
  reservation in L2O; goods receipt + invoice matching in P2P) are shown as parallel lanes
  with an explicit join condition -- what must be true before the lifecycle resumes the main
  sequence.
- **Pass condition**: At least 1 parallel path identified with a named join condition. If the
  lifecycle type has no natural parallel (e.g., a simple case lifecycle), the output explicitly
  notes the absence and states why.

### C-07 -- Decision Point Explicitness
- **Weight**: recommended
- **Category**: format
- **Text**: Every fork in the lifecycle (approval/rejection, threshold check, routing rule) is
  named as a decision point with: the question being decided, the role that decides, and the
  downstream path for each outcome.
- **Pass condition**: At least 3 named decision points. Each includes condition, owner role,
  and all outcome branches. A decision point described only as "approved or rejected" without
  stating who decides and what triggers each path is a partial fail.

### C-08 -- Edge Case Enumeration
- **Weight**: recommended
- **Category**: coverage
- **Text**: The output names edge cases the lifecycle design does not handle -- scenarios
  logically reachable but absent from the trace (e.g., partial shipment re-entry, duplicate
  submission collision, retroactive approval after payment).
- **Pass condition**: At least 2 edge cases distinct from the C-02 exception flows. Each
  includes: the scenario, why the current lifecycle has no step for it, and the risk or
  consequence if the gap is unaddressed.

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable.

### C-09 -- Cross-Lifecycle Dependencies
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least one point where the simulated lifecycle interacts with a different business
  process is identified with direction: which lifecycle sends the artifact, which receives it,
  and at what state the handoff occurs (e.g., L2O generating a sales order that triggers P2P
  replenishment; period close blocking AR posting until all open L2O flows resolve).
- **Pass condition**: 1 cross-lifecycle dependency named with direction, the partner lifecycle
  identified, and the coupling state or artifact specified.

### C-10 -- SLA and Timing Annotation
- **Weight**: aspirational
- **Category**: depth
- **Text**: At least 3 states or transitions are annotated with a timing expectation (SLA
  target or typical duration) and a flag indicating whether the C-04 bottlenecks place that
  SLA at risk.
- **Pass condition**: 3 or more states carry a timing annotation (e.g., "target: 2 business
  days"). At least 1 is flagged AT-RISK with a causal reference to a specific bottleneck from
  C-04.

---

## Scoring Table

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | State Transition Coverage | essential | correctness |
| C-02 | Exception Flow Traces | essential | coverage |
| C-03 | Terminal State Completeness | essential | correctness |
| C-04 | Bottleneck and Gap Identification | essential | depth |
| C-05 | Domain Role Assignment | essential | correctness |
| C-06 | Parallel Path Modeling | recommended | depth |
| C-07 | Decision Point Explicitness | recommended | format |
| C-08 | Edge Case Enumeration | recommended | coverage |
| C-09 | Cross-Lifecycle Dependencies | aspirational | depth |
| C-10 | SLA and Timing Annotation | aspirational | depth |

## Example Score Calculations

**All essential pass, all recommended pass, no aspirational**:
(5/5 * 60) + (3/3 * 30) + (0/2 * 10) = 60 + 30 + 0 = **90** -- golden

**All essential pass, 2/3 recommended pass, no aspirational**:
(5/5 * 60) + (2/3 * 30) + (0/2 * 10) = 60 + 20 + 0 = **80** -- golden (threshold met)

**4/5 essential pass, all recommended pass, all aspirational pass**:
(4/5 * 60) + (3/3 * 30) + (2/2 * 10) = 48 + 30 + 10 = **88** -- not golden (essential incomplete)

**All essential pass, 1/3 recommended, all aspirational**:
(5/5 * 60) + (1/3 * 30) + (2/2 * 10) = 60 + 10 + 10 = **80** -- golden (all essential pass, threshold met)
