---
name: feasibility-alt
description: UNIFIED VERSION (A/B test against discover-feasibility). Single prompt handles base feasibility AND optional focus dimen
allowed-tools: [Read, Write, Glob, Grep]
param_set: standard
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


UNIFIED VERSION (A/B test against discover-feasibility). Single prompt handles base feasibility AND optional focus dimensions woven together, not appended. Produces a richer, more coherent output when focus is active. Test whether unified > parameterized. AMEND: shift focus, adjust confidence thresholds.