---
name: generate
description: Generate a typed role registry for a domain. Analyzes product/codebase to determine what expert perspectives are needed.
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


Generate a typed role registry for a domain. Analyzes product/codebase to determine what expert perspectives are needed. Each role gets: orientation, lens (verify + simplify), expertise, scope, collaborates_with. Output is .craft/roles/{area}/ directory of markdown role files. Inertia-advocate always included. AMEND: add more roles, adjust level distribution.