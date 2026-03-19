---
name: preview
description: Generate a mock artifact for a single namespace. Same annotation and category rules as mock-all. Use --skill to target a
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Generate a mock artifact for a single namespace. Same annotation and category rules as mock-all. Use --skill to target a specific skill within the namespace. Supports --tier 1|2|3.