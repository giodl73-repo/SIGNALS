---
name: validate-customers
description: 12 customer personas (C-01 through C-12) evaluate a feature for usefulness, clarity, and would-adopt (all 1-5). Primary
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


12 customer personas (C-01 through C-12) evaluate a feature for usefulness, clarity, and would-adopt (all 1-5). Primary audience weighted 3x, secondary 2x, non-target 1x. Identify adoption blockers (primary persona would-adopt < 3), positioning leaks (non-target confused about who this is for), delight signals (score 5). Weighted aggregate score. Amend: address blockers and leaks first. Stock: C-01 Maria Chen (Maker) through C-12 Frank Hoffmann (Regulator).