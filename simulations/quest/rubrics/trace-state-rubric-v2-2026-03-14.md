Here is the complete updated rubric:

---

# trace-state Rubric v2
**Updated**: 2026-03-14
**Change**: Added C-11, C-12, C-13 from R1 excellence signals (V-04 sweep table, Op ID cross-referencing, Entry Condition column).

---

## Design Rationale

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
- C-11: sweep table with mandatory row-level verdicts per anomaly type (R1 excellence signal)
- C-12: Op ID cross-referencing between declaration and trace (R1 excellence signal)
- C-13: Entry Condition column in state machine table (R1 excellence signal)

---

## Essential Criteria

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Before/after state per operation** -- Every operation in the trace shows the full entity state immediately before and immediately after execution. No operation is described with only a narrative summary. | correctness | Every operation has a documented before-state and after-state. At least three operations are traced. Narrative-only descriptions do not pass. |
| C-02 | **Preconditions and postconditions** -- For each operation, the trace states what must be true before the operation executes (preconditions) and what is guaranteed to be true after (postconditions). | correctness | Every operation has at least one precondition and one postcondition. Vague statements like "data is valid" do not count -- they must be state-specific. |
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
| C-11 | **Sweep table with mandatory row-level verdicts** -- All four anomaly types appear as pre-printed rows in a sweep table, each requiring an explicit "found / none" verdict with the triggering operation and affected state. The model cannot omit a type without leaving a blank cell. | coverage | A sweep table with all four anomaly type rows is present. Each row has an explicit verdict, not a blank. A fully-negative table (all four "none") does not pass -- at least one row must be "found". |
| C-12 | **Op ID cross-referencing** -- Operations are declared with unique identifiers (e.g., OP-01, OP-02) in the transitions table, and every reference in the trace body uses that identifier. Any operation used but not declared is flagged as an anomaly finding. | correctness | All operations have declared Op IDs. Every trace step and anomaly entry references operations by Op ID. Undeclared operation use is surfaced as a finding. |
| C-13 | **Entry Condition column in state machine table** -- The state machine table includes an "Entry Condition" column declaring what must be true to be in each state at declaration time, not just at operation initiation. Enables anomaly detection at two levels: entry to a state and initiation of an operation. | correctness | Entry Condition column present with at least one non-trivial, state-specific entry per state. At least one anomaly finding references a violated entry condition. |

---

## Scoring Summary

| Tier | Criteria | Weight |
|------|----------|--------|
| Essential | C-01, C-02, C-03, C-04, C-05 | 60% |
| Recommended | C-06, C-07, C-08 | 30% |
| Aspirational | C-09, C-10, C-11, C-12, C-13 | 10% |

**Pass**: All essential criteria pass AND composite score >= 80.

**Aspirational scoring note**: C-09 through C-13 share the 10% aspirational weight at 2 points each. C-11 supersedes C-09 -- a trace that passes C-11 automatically passes C-09. Score both independently; no double-penalty for failing C-09 when C-11 is attempted but fails.

---

Three things to note about the new criteria:

**C-11 vs C-09**: C-11 is a structural upgrade, not a separate concern. The sweep table enforces what C-09 only requests. Scoring both preserves the ability to distinguish "had four prose sections that all said None found" (C-09 fail, C-11 fail) from "had four prose sections with at least one finding" (C-09 pass, C-11 fail — sweep table absent) from "had sweep table with one affirmative row" (C-09 pass, C-11 pass).

**C-12 linkage**: The Op ID pattern directly strengthens C-04 and C-06 — anomalies reference specific declared operations, which sharpens "generic statements do not pass" from a prose check to a mechanical one.

**C-13 linkage**: Entry Condition complements C-02 (per-operation preconditions) by catching the case where a state itself has an invalid entry — a missing-precondition-check anomaly that per-operation tracing alone would miss.
