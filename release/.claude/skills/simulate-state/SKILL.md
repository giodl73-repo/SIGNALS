---
name: simulate-state
description: "Hand-compile state transitions: starting state, operations applied, expected outcome at each step. For each operation: p"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Keep total output under 2000 words. If --compact: under 800 words.

Hand-compile state transitions: starting state, operations applied, expected outcome at each step. For each operation: preconditions, state changes, postconditions, invariants that must hold. Identify: invalid state transitions, missing precondition checks, invariant violations, race conditions. Stock roles: Sales / Customer Service / Finance state domain expert.
Write artifact to: signals/simulate/state/{{topic}}-state-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-state-{date}.md). No namespace subdirectory.
Include frontmatter: skill: simulate-state, topic: {{topic}}, date: {{date}}
