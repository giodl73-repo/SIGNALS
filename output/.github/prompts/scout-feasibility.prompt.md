---
agent: 'agent'
tools: ['codebase']
description: 'Technical feasibility assessment with traffic-light ratings and budget chain.'
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


Assess whether a product idea is technically feasible given current constraints. Scan repo for stack signals (package.json, tsconfig.json, Cargo.toml). Always surface inferred team size and timeline explicitly -- never silently infer. Traffic-light rating per component (green/yellow/red). Overall feasibility score 0-100. Stock roles: Architect (complexity scoring), PM (timeline overlay), Strategy (build-vs-buy per component).

Write artifact to: simulations/scout/feasibility/{topic}-feasibility-{date}.md
