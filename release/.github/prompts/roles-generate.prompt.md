---
mode: agent
description: "Generate a typed role registry for a domain. Analyzes product/codebase to determine what expert perspectives are needed."
---
for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Generate a typed role registry for a domain. Analyzes product/codebase to determine what expert perspectives are needed. Each role gets: orientation, lens (verify + simplify), expertise, scope, collaborates_with. Output is .craft/roles/{area}/ directory of markdown role files. Inertia-advocate always included. AMEND: add more roles, adjust level distribution.