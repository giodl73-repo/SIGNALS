---
agent: 'agent'
tools: ['codebase', 'web_search']
description: 'Name generation and evaluation with multi-persona scoring.'
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


Generate and evaluate candidate names using multi-persona scoring. Supports --validate <name> to pin an existing name at row 1 and produce a validation summary alongside alternatives. Generate 10-15 candidates. Score across PM (memorability), Design (visual weight), UX (speakability), GTM (searchability), Strategy (positioning fit). Collision check against package registries and domains. Stock roles: PM, Design, UX, GTM, Strategy.

Write artifact to: simulations/scout/naming/{topic}-naming-{date}.md
