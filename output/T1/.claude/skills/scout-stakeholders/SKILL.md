---
name: scout-stakeholders
description: Stakeholder mapping with power/interest grid and veto risk ranking.
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


Map the stakeholder landscape for a product decision. If CODEOWNERS is absent, extract org context from the invocation string. If invocation context is also insufficient, ask one question: "What org or team is this decision for?" Never silently infer an org structure. Power/interest grid, veto risks ranked by probability, champion identification, communication strategy per quadrant. Stock roles: PM (power/interest mapping), Strategy (conflicts), UX (journeys).

Write artifact to: simulations/scout/stakeholders/{topic}-stakeholders-{date}.md
