---
name: build
description: "Read a confirmed org.yaml and generate the full org. Outputs: (1) org-chart.md with ASCII box diagram, headcount by grou"
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


Read a confirmed org.yaml and generate the full org. Outputs: (1) org-chart.md with ASCII box diagram, headcount by group/area, level distribution; (2) .craft/roles/{area}/{role}.md typed files for every role -- standard roles per team, specialized roles per team, shared group roles, exec office roles. Supports arbitrary group nesting: Division > Team > Sub-group. Inertia-advocate always included in every team. AMEND: regenerate specific area, adjust level vocabulary, change group structure.