---
agent: 'agent'
tools: ['codebase']
description: 'Hypothesis framing with claim, falsification condition, confidence, and experiment list.'
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


State what you believe and what would change your mind. Entry point to a prove investigation. A hypothesis has: a claim (what you believe), a falsification condition (what evidence would prove it wrong), a confidence level (0-100), and a list of experiments that will test it. The hypothesis is a commitment -- you cannot move the goalposts after seeing results.

Write artifact to: simulations/prove/investigations/{topic}-hypothesis-{date}.md
