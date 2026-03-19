---
name: quest-variate
description: Generate N distinct prompt variations of a skill body. Each variation is a complete, runnable skill body -- not a diff.
allowed-tools: [Read, Write]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Generate N distinct prompt variations of a skill body. Each variation is a complete, runnable skill body -- not a diff. Variation axes: role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity. Single-axis variation isolates the effect of each choice. Combinations come after single-axis passes. Default N=5. Each variation labeled V-01 through V-0N with its axis and hypothesis.