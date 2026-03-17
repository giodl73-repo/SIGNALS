---
agent: 'agent'
tools: ['codebase']
description: 'Regulatory and policy constraint scan before design begins.'
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


Identify regulatory and policy constraints before design begins. Infer applicable frameworks from domain and data type signals. Always distinguish between compliance obligations on the product vs. on the host platform (e.g., SR 11-7 applies to the AI model, not to a structured prompt methodology). Git-native, no-server designs are compliance-favorable -- surface this when applicable. Stock roles: Compliance (framework catalog), Architect (technical constraints), PM (timeline impact), Strategy (market access vs. cost).

Write artifact to: simulations/scout/compliance/{topic}-compliance-{date}.md
