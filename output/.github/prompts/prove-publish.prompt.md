---
agent: 'agent'
tools: ['codebase']
description: 'Investigation write-up as paper with abstract, method, findings, and limitations.'
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


Write up an investigation as a paper or report for institutional memory. Simplified panel review using custom expert roles. Structure: abstract, hypothesis, method, evidence, findings, principles, limitations, future work. The published paper is the endgame of a prove investigation -- it is what the next team finds when they search for prior work on this topic.

Write artifact to: simulations/prove/publications/{topic}-paper-{date}.md
