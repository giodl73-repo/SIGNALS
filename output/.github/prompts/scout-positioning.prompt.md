---
agent: 'agent'
tools: ['codebase']
description: 'Per-audience positioning statements with competitive differentiation.'
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


Define how a product should be positioned per audience. If a prior scout-competitors run exists, load it -- positioning built without competitor context degrades silently. If no prior run found: note the degradation, run competitor identification inline, flag "run scout-competitors for richer positioning." Per-audience positioning statements, competitive differentiation matrix, messaging hierarchy, anti-positioning. Stock roles: Strategy (framework), GTM (per-audience value props), PM (reality check), Design (narrative coherence).

Write artifact to: simulations/scout/positioning/{topic}-positioning-{date}.md
