Rubric written to `simulations/quest/rubrics/trace-state-rubric-2026-03-14.md`.

**Design rationale:**

**Essential (60%)** — the five things that make a trace-state output useful at all:
- C-01: before/after state for every operation (the whole point of the skill)
- C-02: preconditions + postconditions per operation (not just "what happened" but "why it was allowed")
- C-03: invariants named (the thing a state machine analysis is really hunting for)
- C-04: at least one anomaly identified (the deliverable — no finding = no signal)
- C-05: domain grounding (Sales/CS/Finance vocabulary — otherwise it's a toy example)

**Recommended (30%)** — what separates a useful trace from a great one:
- C-06: negative path (attempted invalid transition + why it's rejected)
- C-07: numbered step-by-step format (reader can replay the trace mechanically)
- C-08: race condition scenario (the hardest anomaly type, worth its own criterion)

**Aspirational (10%)** — raises the bar once the basics are stable:
- C-09: all four anomaly types covered (complete signal, not just the easy ones)
- C-10: structured notation / transition table (enables mechanical verification, not just prose review)
 executes (preconditions) and what is guaranteed to be true after (postconditions). | correctness | Every operation has at least one precondition and one postcondition. Vague statements like "data is valid" do not count -- they must be state-specific. |
| C-03 | **Invariant declaration** -- At least one invariant is identified that must hold across all states or across a named subset of states (e.g., "balance never goes negative", "closed ticket cannot be reopened without manager approval"). | correctness | At least one invariant is named, stated precisely, and scoped to specific states or the whole lifecycle. |
| C-04 | **Anomaly identification** -- At least one concrete anomaly is identified from the set: invalid state transition, missing precondition check, invariant violation, or race condition. Each anomaly includes the specific operation and state where it occurs. | coverage | At least one anomaly is called out by name, with the triggering operation and affected state identified. Generic statements ("errors can occur") do not pass. |
| C-05 | **Domain grounding** -- The trace uses vocabulary, entity names, and scenarios from one of the three stock domains (Sales, Customer Service, or Finance). States and operations are recognizable as real domain events, not generic placeholders. | behavior | Entity names, state labels, and operation names match domain conventions. A domain expert in Sales, CS, or Finance would recognize the scenario as realistic. |

---

## Recommended Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Negative path coverage** -- At least one invalid or rejected transition is traced: an operation attempted from a state where it is not allowed, with the expected rejection behavior documented. | coverage | One or more "attempted but rejected" transitions appear in the trace, with the reason for rejection (which precondition fails or which invariant would be violated). |
| C-07 | **Step-by-step trace format** -- The trace is presented as a numbered sequence of discrete steps, each showing the full state snapshot before and after the operation, not just a high-level summary. | format | Steps are numbered. Each step shows before-state, operation, after-state. Reader can follow entity state at every moment without inference. |
| C-08 | **Race condition analysis** -- At least one concurrent scenario is explored: two operations that could interleave, the resulting state conflict, and which one should win or how the conflict should be detected. | depth | A race condition scenario is described with at least two concurrent operations, the problematic interleaving, and the expected resolution or detection mechanism. |

---

## Aspirational Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Full anomaly type coverage** -- All four anomaly types are represented: invalid transition, missing precondition check, invariant violation, and race condition -- each with a concrete example from the trace. | coverage | One concrete example per anomaly type, each tied to a specific operation and state in the trace. |
| C-10 | **Structured notation** -- The state machine is expressed in a formal or semi-formal notation: a state table, transition matrix, or named-state diagram description -- not just prose. Enables mechanical verification. | format | A table, matrix, or structured list captures all states, all valid transitions, and all operations. Prose narrative may accompany but does not substitute for the structured artifact. |

---

## Scoring Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60% |
| Recommended | C-06, C-07, C-08 | 30% |
| Aspirational | C-09, C-10 | 10% |

**Pass**: All essential criteria pass AND composite score >= 80.
