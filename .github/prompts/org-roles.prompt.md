---
mode: agent
description: "Typed role registry generation for a domain with orientation, lens, and expertise."
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

Generate a typed role registry for a domain. Analyzes the product, codebase, or spec to determine what expert perspectives are needed. Each role gets: name, orientation (frame + serves), lens (verify questions + simplify rules), expertise (depth + relevance), scope, collaborates_with. Output is a .roles/{area}/ directory of markdown role files. Inertia check: include a devil-advocate role whose job is to challenge every proposal with why the status quo is sufficient. Stock structure: PM, Architect, Strategy, domain experts auto-selected from context.

Write artifact to: .roles/{domain}/
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
