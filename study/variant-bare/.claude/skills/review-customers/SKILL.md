---
name: review-customers
description: Twelve customer personas evaluate feature for usefulness, clarity, and would-adopt.
allowed-tools: [Read, Write, Glob]
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


12 customer personas (C-01 through C-12) evaluate a feature for usefulness, clarity, and would-adopt (all 1-5). Primary audience weighted 3x, secondary 2x, non-target 1x. Identify adoption blockers (primary persona would-adopt < 3), positioning leaks (non-target confused about who this is for), delight signals (score 5). Weighted aggregate score. Amend: address blockers and leaks first. Stock: C-01 Maria Chen (Maker) through C-12 Frank Hoffmann (Regulator).

Write artifact to: simulations/review/customers/{topic}-customers-{date}.md
