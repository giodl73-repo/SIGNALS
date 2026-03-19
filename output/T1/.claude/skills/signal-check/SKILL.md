---
name: signal-check
description: "Self-check your signals before committing. Analyzes all signal artifacts for a topic across 4 dimensions: SEQUENCE (did"
allowed-tools: [Read, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Self-check your signals before committing. Analyzes all signal artifacts for a topic across 4 dimensions: SEQUENCE (did you discover before specifying?), COHERENCE (do your signals agree with each other?), STALENESS (are signals recent enough to trust?), CAUSAL GAP (do you have evidence for the mechanism linking feature to outcome?). Not punitive -- coaching. Surfaces what looks inconsistent so you can decide whether to address it before committing. Run before /specify-commitment or any major decision.