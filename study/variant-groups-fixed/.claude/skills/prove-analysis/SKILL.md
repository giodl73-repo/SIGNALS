---
name: prove-analysis
description: Data pattern analysis distinguishing correlation from causation with source attribution.
allowed-tools: [Read, Write, Glob, Grep]
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


Analyze existing data, telemetry, schemas, or scenarios for patterns that bear on the hypothesis. For each data source: what was analyzed, what pattern was found, what is the statistical or logical strength of the pattern. Distinguish correlation from causation explicitly.

Write artifact to: simulations/prove/investigations/{topic}-analysis-{date}.md
