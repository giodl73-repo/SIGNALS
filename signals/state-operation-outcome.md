# /state-operation-outcome — State Machine Verification

> Installed from sim/techniques/02 + signal:trace-state skill.
> For: pacts S03 (halt semantics), S04 (compile gate)

## Usage

```
/state-operation-outcome <topic> <spec>
```

## Protocol

Hand-compile state transitions: starting state, operations applied, expected outcome
at each step. For each operation: preconditions, state changes, postconditions,
invariants that must hold.

### Phase 1 — State Enumeration

From the cited spec, enumerate ALL valid states and transitions:

| # | State | Entry Condition | Valid Transitions | Spec Clause |
|---|-------|-----------------|-------------------|-------------|

### Phase 2 — Operation Sequence

Define the operation sequence to test. For each operation:

| Step | Operation | Precondition | Starting State | Expected State | Postcondition | Invariants |
|------|-----------|-------------|----------------|----------------|---------------|------------|

### Phase 3 — Execute and Verify

For each step, check:
- Does the actual implementation match the expected state?
- Do all invariants hold?
- Are all preconditions checked (or silently assumed)?

### Phase 4 — Classification

| Step | Operation | Expected State | Actual State | Result | Severity | Spec Clause |
|------|-----------|----------------|-------------|--------|----------|-------------|

Severity: `breaking` (wrong state), `degraded` (right state, missing check), `cosmetic`.

### Phase 5 — Findings

For each mismatch: identify the specific mechanism that caused divergence.
For missing precondition checks: identify what goes wrong when the precondition is violated.

## Output

Write to the scenario directory:
- `SCENARIO.md` — full state-operation-outcome trace
- `TRACE.md` — classification table summary

## Identify

- Invalid state transitions (operation from wrong state)
- Missing precondition checks
- Invariant violations
- Race conditions (concurrent operations on same state)
- Unspecified states (actual behavior not in spec)
