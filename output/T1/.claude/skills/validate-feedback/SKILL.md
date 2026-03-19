---
name: validate-feedback
description: Simulate customer reactions to a spec or design before it ships. All 12 customer personas (C-01 through C-12) read the s
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Simulate customer reactions to a spec or design before it ships. All 12 customer personas (C-01 through C-12) read the spec through their lens. Per-persona feedback cards with severity (blocking/major/minor/cosmetic) and NPS prediction (1-10). Cross-persona theme matrix. Aggregate NPS threshold: 7.0. Below 7.0 = spec needs revision. Stock roles: C-01 through C-12, PM, UX.