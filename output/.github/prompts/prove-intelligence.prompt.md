---
agent: 'agent'
tools: ['codebase']
description: 'Internal source evidence search with file-path citations and relevance assessment.'
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


Search internal sources (repo files, design docs, scenarios, prior signals) for evidence. For each source: file path, relevant excerpt, relevance to hypothesis, strength of evidence. Internal evidence is often stronger than public evidence for product-specific hypotheses.

Write artifact to: simulations/prove/investigations/{topic}-intelligence-{date}.md
