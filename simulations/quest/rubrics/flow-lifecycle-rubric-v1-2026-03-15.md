---
skill: quest-rubric
skill_target: flow-lifecycle
date: 2026-03-15
version: 1
---

# Rubric: flow-lifecycle

Scoring rubric for the `flow-lifecycle` skill. This skill simulates a multi-step business document lifecycle (L2O, P2P, period close, case lifecycle), walking every step with entry conditions, state transitions, decision points, parallel paths, exception flows, and terminal states.

## Composite Score Formula

```
score = (essential_pass/N * 60) + (recommended_pass/N * 30) + (aspirational_pass/N * 10)
```

**Golden threshold**: all essential criteria pass AND composite >= 80.

---

## Essential Criteria

> All must pass. Without these the output is not useful.

### C-01 -- State Enumeration
- **Weight**: essential
- **Category**: correctness
- **Text**: The output names every major state in the lifecycle, from initial entry to all terminal states. No state that a document or process instance can occupy is left implicit.
- **Pass condition**: At least 6 distinct named states are present for any single lifecycle path. Every named state appears in both the state list and the transition table (no orphan states, no phantom transitions).

### C-02 -- Transition Triggers
- **Weight**: essential
- **Category**: correctness
- **Text**: Each state transition is annotated with the condition or event that fires it. Transitions are not described as arrows alone -- each carries a guard (what must be true) or an event (what must happen).
- **Pass condition**: Every transition has an explicit trigger (event name, condition expression, or time-based rule). Zero transitions may read "next state" without a named cause.

### C-03 -- Entry and Exit Conditions
- **Weight**: essential
- **Category**: coverage
- **Text**: Each state carries at least one entry condition (what must hold to enter) and one exit condition (what ends the stay). Conditions are specific to the business domain, not generic placeholders.
- **Pass condition**: At least 80% of named states have both an entry condition and an exit condition expressed in domain terms (e.g., "PO approved by level-2 authority", not "ready flag is set").

### C-04 -- Exception Flows
- **Weight**: essential
- **Category**: coverage
- **Text**: At least one exception or failure path is traced per major lifecycle phase. Exception paths name the recovery action or the terminal failure state reached.
- **Pass condition**: The output traces at least one exception per lifecycle phase (e.g., approval rejection, timeout, data validation failure). Each exception path reaches either a named recovery state or a named terminal failure state.

### C-05 -- Terminal States
- **Weight**: essential
- **Category**: correctness
- **Text**: All terminal states (happy-path completion and all failure/cancel endpoints) are explicitly labeled. The output makes clear which terminal states represent success and which represent failure.
- **Pass condition**: At least two terminal states are named. At least one is a success terminal (e.g., "Invoice Paid", "Order Fulfilled") and at least one is a failure/cancel terminal (e.g., "Rejected -- No Resubmit", "Voided"). No transition leads to an unnamed dead end.

---

## Recommended Criteria

> Output is meaningfully better with these.

### C-06 -- Parallel Paths and Join Conditions
- **Weight**: recommended
- **Category**: depth
- **Text**: Concurrent activities within the lifecycle are identified (e.g., parallel approval tracks, simultaneous inventory reservation and credit check). Join conditions -- what must be true before the parallel paths merge -- are stated.
- **Pass condition**: At least one parallel activity is identified if the lifecycle type warrants it (L2O credit + availability check, P2P three-way match legs). The join condition for each parallel fork is explicit.

### C-07 -- Bottleneck and Delay Identification
- **Weight**: recommended
- **Category**: depth
- **Text**: The output identifies at least one state or transition that is a known bottleneck or source of delay in real-world execution. The diagnosis names why (manual step, approval chain depth, external system dependency) and is grounded in the simulated process context.
- **Pass condition**: At least one bottleneck is flagged with a cause (not just "this step is slow"). The diagnosis is domain-plausible for the lifecycle type selected.

### C-08 -- Role Assignment
- **Weight**: recommended
- **Category**: behavior
- **Text**: Each step or state is assigned to a named role drawn from the domain (Sales Rep, AP Clerk, Controller, Support Agent, etc.). Roles are specific and appropriate -- not "user" or "system actor".
- **Pass condition**: Every state or step is owned by at least one named role. Roles are drawn from the domain context of the lifecycle type (e.g., Finance roles for P2P, Sales roles for L2O). Generic role names ("user", "admin", "system") are not used without qualification.

---

## Aspirational Criteria

> Raise the bar once essential and recommended are stable.

### C-09 -- Unhandled Edge Cases
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output surfaces at least two edge cases that standard process documentation omits -- states or transitions that are logically reachable but rarely accounted for in design (e.g., partial shipment re-entry, retroactive approval after payment, lifecycle state collision from duplicate submission).
- **Pass condition**: At least two edge cases are named and described with the condition that triggers them and the gap they expose. Each edge case must be distinct from the exception flows in C-04.

### C-10 -- Cross-Lifecycle Dependencies
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output notes at least one point where the simulated lifecycle depends on or affects a different business process (e.g., L2O triggering P2P replenishment, period close blocking AR posting, case resolution creating a service credit memo). The dependency is directional and specific.
- **Pass condition**: At least one cross-lifecycle dependency is named with direction (this lifecycle sends / receives / blocks another), the partner lifecycle is identified, and the coupling point (state or event) is specified.

---

## Scoring Table

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | State Enumeration | essential | correctness |
| C-02 | Transition Triggers | essential | correctness |
| C-03 | Entry and Exit Conditions | essential | coverage |
| C-04 | Exception Flows | essential | coverage |
| C-05 | Terminal States | essential | correctness |
| C-06 | Parallel Paths and Join Conditions | recommended | depth |
| C-07 | Bottleneck and Delay Identification | recommended | depth |
| C-08 | Role Assignment | recommended | behavior |
| C-09 | Unhandled Edge Cases | aspirational | depth |
| C-10 | Cross-Lifecycle Dependencies | aspirational | coverage |

## Example Score Calculations

**All essential pass, all recommended pass, no aspirational**:
(5/5 * 60) + (3/3 * 30) + (0/2 * 10) = 60 + 30 + 0 = 90 -- golden

**All essential pass, 2/3 recommended pass, no aspirational**:
(5/5 * 60) + (2/3 * 30) + (0/2 * 10) = 60 + 20 + 0 = 80 -- golden (threshold met)

**4/5 essential pass, all recommended pass, all aspirational pass**:
(4/5 * 60) + (3/3 * 30) + (2/2 * 10) = 48 + 30 + 10 = 88 -- not golden (essential incomplete)

**All essential pass, 1/3 recommended, all aspirational**:
(5/5 * 60) + (1/3 * 30) + (2/2 * 10) = 60 + 10 + 10 = 80 -- golden (threshold met, all essential pass)
