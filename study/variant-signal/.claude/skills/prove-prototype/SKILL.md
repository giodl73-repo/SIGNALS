---
name: prove-prototype
description: Smallest-possible prototype with defined measure and predicted vs actual results.
allowed-tools: [Read, Write, Bash, Glob]
param_set: full
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


Build something small and measure it. A prototype is the smallest possible thing that tests the hypothesis. Define: what to build, what to measure, what result confirms vs. refutes the hypothesis. Build it. Measure it. Report what actually happened vs. what was predicted.

Write artifact to: simulations/prove/investigations/{topic}-prototype-{date}.md
