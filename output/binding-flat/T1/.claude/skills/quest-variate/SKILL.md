---
name: quest-variate
description: "Generate N prompt variations of a skill body for comparison. Given a skill description and variation axes (role sequence, output format, lifecycle emphasis, stock role selection, phrasing), produce N distinct prompt formulations of the same skill. Each variation is a complete, runnable skill body -- not a diff. Variation axes are independent; combinations are intentional. Default N=5.
"
allowed-tools: [Read, Write]
param_set: lean
---
Generate N distinct prompt variations of a skill body. Each variation is a complete, runnable skill body -- not a diff. Variation axes: role sequence, output format, lifecycle emphasis, stock role selection, phrasing register, scoring granularity. Single-axis variation isolates the effect of each choice. Combinations come after single-axis passes. Default N=5. Each variation labeled V-01 through V-0N with its axis and hypothesis.

Write artifact to: simulations/quest/variations/{skill}-variations-{date}.md
