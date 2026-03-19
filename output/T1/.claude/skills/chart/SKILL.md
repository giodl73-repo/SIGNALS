---
name: chart
description: "Generate org structure for a product or domain: areas, divisions, committees, operating rhythms. Reads existing .craft/r"
allowed-tools: [Read, Write, Glob]
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


Generate org structure for a product or domain: areas, divisions, committees, operating rhythms. Reads existing .craft/roles/ to build from real roles. Output: org-chart.md with ASCII org box, headcount by area, committee charters, operating rhythm table. AMEND: adjust headcount, reorganize teams.