---
name: mock
description: "Mock namespace -- 3 skills for synthetic signal generation.

/mock-all     -> synthetic signal artifacts for all 9 namespaces with coverage picture
/mock-ns      -> mock artifact for a single namespace with category annotation
/mock-review  -> coverage review writing MOCK-ACCEPTED or REAL-REQUIRED per namespace

Run any sub-skill directly, or describe your coverage need and the most relevant mock skill will run.
"
allowed-tools: [Read, Write, Edit, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure
