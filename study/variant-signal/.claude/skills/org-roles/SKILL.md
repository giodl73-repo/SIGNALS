---
name: org-roles
description: Typed role registry generation for a domain with orientation, lens, and expertise.
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


Generate a typed role registry for a domain. Analyzes the product, codebase, or spec to determine what expert perspectives are needed. Each role gets: name, orientation (frame + serves), lens (verify questions + simplify rules), expertise (depth + relevance), scope, collaborates_with. Output is a .craft/roles/{area}/ directory of markdown role files. Inertia check: include a devil-advocate role whose job is to challenge every proposal with why the status quo is sufficient. Stock structure: PM, Architect, Strategy, domain experts auto-selected from context.

Write artifact to: .craft/roles/{domain}/
