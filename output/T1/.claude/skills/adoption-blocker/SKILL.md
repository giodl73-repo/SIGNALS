---
name: adoption-blocker
description: Validate the adoption case by stress-testing the inertia scenario. Why would users NOT adopt this feature even if it wor
allowed-tools: [Read, Write]
param_set: standard
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


Validate the adoption case by stress-testing the inertia scenario. Why would users NOT adopt this feature even if it works perfectly? Maps: current workaround satisfaction, switching cost per persona, habit lock-in, social proof requirements, learning curve. Produces per-persona inertia score and overall adoption inertia risk. AMEND: focus on specific persona, quantify switching cost, identify the one barrier that would kill adoption.