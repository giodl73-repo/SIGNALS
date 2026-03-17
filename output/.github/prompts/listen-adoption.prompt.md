---
agent: 'agent'
tools: ['codebase']
description: 'Adoption curve simulation across Rogers archetypes with chasm analysis.'
---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


Simulate the adoption curve across team archetypes. Map personas to Rogers archetypes (innovator/early-adopter/early-majority/late-majority/laggard). Month-by-month simulation: who tries first, what spreads, what bridges the chasm. Chasm analysis: the gap between early adopters and early majority. Champion network, churn risks, intervention recommendations ranked by adoption delta. Stock roles: PM, UX, C-01 through C-12, Support, SRE.

Write artifact to: simulations/listen/adoption/{topic}-adoption-{date}.md
