---
name: qa
description: "Run the full design validation campaign. Orchestrates: review-design, review-users, review-customers, listen-feedback, l"
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


Run the full design validation campaign. Orchestrates: review-design, review-users, review-customers, listen-feedback, listen-adoption in sequence. Output: validation brief with findings ranked by adoption impact. Use to validate a design before committing to spec.