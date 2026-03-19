---
name: state
description: "Hand-compile state transitions: starting state, operations applied, expected outcome at each step. For each operation: p"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Hand-compile state transitions: starting state, operations applied, expected outcome at each step. For each operation: preconditions, state changes, postconditions, invariants that must hold. Identify: invalid state transitions, missing precondition checks, invariant violations, race conditions. Stock roles: Sales / Customer Service / Finance state domain expert.