---
skill: quest-rubric
skill_target: trace-state
date: 2026-03-15
version: 1
---

# Rubric: trace-state

Hand-compile state transitions for a domain object. For each operation: starting state, preconditions, state changes, postconditions, invariants. Identify invalid transitions, missing precondition checks, invariant violations, race conditions.

## Scoring

Composite = (essential_pass/N × 60) + (recommended_pass/N × 30) + (aspirational_pass/N × 10)

**Golden threshold**: all essential criteria pass AND composite ≥ 80

---

## Essential Criteria (60 pts total — must all pass)

### C-01 · Explicit state transitions
- **Weight**: essential
- **Category**: correctness
- **Text**: Every operation is expressed as a triple: `starting_state → operation → ending_state`. The before and after state are named, not inferred from prose.
- **Pass condition**: Every operation in the trace has a named starting state and a named ending state. No operation is described only narratively without identifying the state change.

---

### C-02 · Preconditions per operation
- **Weight**: essential
- **Category**: correctness
- **Text**: Each operation documents the preconditions that must hold before the operation executes. Preconditions are stated as checkable conditions, not vague descriptions.
- **Pass condition**: Every operation has at least one explicit precondition. At least one precondition is expressed as a testable assertion (e.g., "status == Open", "balance > 0", "owner is assigned").

---

### C-03 · Invariants identified and checked
- **Weight**: essential
- **Category**: correctness
- **Text**: The trace names at least two domain invariants (conditions that must hold throughout the object's lifecycle) and explicitly checks them after each state change.
- **Pass condition**: Two or more invariants are named. At least one is verified after each operation — the output notes whether the invariant holds or is violated at each step.

---

### C-04 · Domain-grounded state vocabulary
- **Weight**: essential
- **Category**: coverage
- **Text**: States use domain terminology from the assigned role (Sales, Customer Service, or Finance). Generic placeholders ("State A", "State 1") are not acceptable.
- **Pass condition**: All state names come from a real domain lifecycle. Sales examples: Lead → Qualified → Proposal → Closed-Won/Lost. CS examples: New → Open → Pending → Resolved → Closed. Finance examples: Draft → Submitted → Approved → Posted → Paid.

---

## Recommended Criteria (30 pts total)

### C-05 · Invalid transitions identified
- **Weight**: recommended
- **Category**: depth
- **Text**: The trace explicitly calls out at least one invalid transition — an operation that cannot legally execute from the current state — and explains why it is invalid (which precondition or invariant blocks it).
- **Pass condition**: At least one invalid transition is named, the attempted operation is identified, and the blocking condition is stated.

---

### C-06 · Postconditions per operation
- **Weight**: recommended
- **Category**: correctness
- **Text**: Each operation documents postconditions — conditions that must be true after the operation completes. Postconditions complement preconditions and together bound the operation's contract.
- **Pass condition**: Every operation has at least one explicit postcondition. Postconditions are distinct from the ending state name (they assert something about the state's properties, not just the label).

---

### C-07 · Race conditions or concurrency risks flagged
- **Weight**: recommended
- **Category**: depth
- **Text**: Where two or more operations could execute concurrently on the same object, the trace flags the race condition, identifies the conflicting operations, and describes the unsafe interleaving.
- **Pass condition**: At least one concurrency risk is identified, OR the trace explicitly states that no concurrent access is possible and gives the reason (e.g., single-owner lock, sequential pipeline).

---

## Aspirational Criteria (10 pts total)

### C-08 · Structured transition table or state diagram
- **Weight**: aspirational
- **Category**: format
- **Text**: Transitions are presented in a table (columns: From State | Operation | Preconditions | To State | Postconditions | Invariants) or an equivalent structured layout, not only as free prose.
- **Pass condition**: A Markdown table or ASCII state diagram is present that captures all transitions. The table is complete — no transition appears only in prose.

---

### C-09 · Boundary and terminal state coverage
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The trace addresses edge cases: the initial state (object just created), terminal states (no further transitions possible), and re-entry attempts (trying to transition out of a terminal state).
- **Pass condition**: Initial state is explicitly labeled. At least one terminal state is identified. An attempt to leave the terminal state is traced and shown to be invalid.

---

## Quick Reference

| ID | Criterion | Weight | Category |
|----|-----------|--------|----------|
| C-01 | Explicit state transitions (triple form) | essential | correctness |
| C-02 | Preconditions per operation | essential | correctness |
| C-03 | Invariants identified and checked | essential | correctness |
| C-04 | Domain-grounded state vocabulary | essential | coverage |
| C-05 | Invalid transitions identified | recommended | depth |
| C-06 | Postconditions per operation | recommended | correctness |
| C-07 | Race conditions or concurrency risks flagged | recommended | depth |
| C-08 | Structured transition table or state diagram | aspirational | format |
| C-09 | Boundary and terminal state coverage | aspirational | coverage |

## Score Examples

| Scenario | Essential | Recommended | Aspirational | Composite | Golden? |
|----------|-----------|-------------|--------------|-----------|---------|
| All pass | 4/4 | 3/3 | 2/2 | 100 | Yes |
| Essential only | 4/4 | 0/3 | 0/2 | 60 | No (< 80) |
| Essential + 2 rec | 4/4 | 2/3 | 0/2 | 80 | Yes |
| Miss 1 essential | 3/4 | 3/3 | 2/2 | 85 | No (not all essential) |
| Essential + 1 rec + 1 asp | 4/4 | 1/3 | 1/2 | 75 | No (< 80) |
