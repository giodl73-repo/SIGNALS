---
name: coverage
description: Generate synthetic signal artifacts for all 9 namespaces in a single pass. Each mock follows the structural requirements
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Generate synthetic signal artifacts for all 9 namespaces in a single pass. Each mock follows the structural requirements of its golden rubric. Automatic pre-flagging: EVIDENCE-HEAVY namespaces get REAL-REQUIRED, compliance namespaces flagged at all tiers. Coverage summary table at end. Supports --tier 1|2|3 and --compliance flags.