---
agent: 'agent'
tools: ['codebase']
description: 'Pitch deck narrative in exec, developer, and maker versions.'
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


Author a pitch deck narrative in exec, developer, and maker versions. Pulls from scout-positioning if available. Each version: hook, what it does, why it matters, call to action. Anti-positioning section (what we are NOT). Exec version: outcome-first, ROI framing. Dev version: show the tool, not the business case. Maker version: jargon-free, "can I do this?" framing. Stock roles: PM, Strategy.

Write artifact to: simulations/draft/pitches/{topic}-pitch-{date}.md
