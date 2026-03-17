---
name: topic-report
description: Shareable status document with progress table and readiness statement.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Write a shareable status document for a topic. Same information as topic-status but as a file. --format teams produces a compact ASCII card suitable for paste into Teams or a standup doc. Progress table, open signals with owners, readiness statement, recommended next step.

Write artifact to: simulations/{topic}/status-{date}.md
