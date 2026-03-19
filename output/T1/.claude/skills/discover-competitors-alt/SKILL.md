---
name: discover-competitors-alt
description: UNIFIED VERSION (A/B test against discover-competitors). Single prompt handles base competitive analysis AND optional fo
allowed-tools: [Read, Write, Glob, Grep, WebSearch]
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


UNIFIED VERSION (A/B test against discover-competitors). Single prompt handles base competitive analysis AND optional focus dimensions (market sizing, positioning framework) in one coherent output. The focus is not appended -- it is woven into the analysis. Goal: test whether unified > parameterized for depth and coherence. The inertia competitor is always assessed first. AMEND: shift focus dimension, adjust depth.