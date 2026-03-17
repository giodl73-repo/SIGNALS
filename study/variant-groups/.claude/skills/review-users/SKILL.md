---
name: review-users
description: Five persona advocates walk through design with usability scores and cross-persona synthesis.
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


5 persona advocates walk through a design from their user perspective. Each persona narrates in first person, flags confusion/friction/fear/jargon with exact artifact quotes, gives usability score 1-5. Cross-persona synthesis: universal friction (3+ personas), role-specific friction, persona conflicts (what helps one hurts another). Aggregate usability score. Amend: iterate until no persona scores below 3/5. Stock: Maker, Developer, Compliance, Supervisor, Operator.

Write artifact to: simulations/review/users/{topic}-users-{date}.md
