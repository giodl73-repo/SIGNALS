---
agent: 'agent'
tools: ['codebase']
description: 'Answer-first evidence synthesis with confidence rating and counter-evidence.'
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


Merge all investigation signals into an answer-first synthesis. Structure: answer (yes/no/maybe), confidence (0-100), key evidence (top 3 signals that most influenced the answer), counter-evidence (what argues against), principles extracted (what this tells us beyond this specific hypothesis), open questions (what the investigation did not resolve). The synthesis is the deliverable -- it supersedes the individual investigation signals.

Write artifact to: simulations/prove/investigations/{topic}-synthesis-{date}.md
