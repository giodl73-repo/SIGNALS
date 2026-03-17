---
agent: 'agent'
tools: ['codebase', 'web_search']
description: 'Competitive landscape analysis leading with inertia as primary competitor.'
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


Auto-detect domain from repo context. Do not prompt unless context absent. THE PRIMARY COMPETITOR: assess "none / status quo" first -- why do teams do nothing? Score threat always HIGH. Inertia is the primary competitor. Named competitors (5-8): feature overlap, positioning, technical moat, distribution, overall threat (HIGH/MEDIUM/LOW each). Use WebSearch to verify at least one claim per major competitor, cite source inline. FINDINGS as a brief: (1) The Primary Competitor -- why inertia is the real threat, (2) The Whitespace -- what no competitor owns, (3) The Table Stakes -- what any entrant must have, (4) The Competitive Matrix -- supporting evidence, (5) --mode risk -- cost of not acting, for exec audiences. AMEND: 3 specific adjustments each with what changes in the output.

Write artifact to: simulations/scout/competitors/{topic}-competitors-{date}.md
