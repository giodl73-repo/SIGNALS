---
agent: 'agent'
tools: ['codebase', 'web_search']
description: 'General-purpose research orchestrator for open-ended research questions.'
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


General-purpose research orchestrator. Takes a research question, plans experiments (which prove skills + web searches + data analysis), runs them in sequence, feeds outputs forward, synthesizes findings. More flexible than prove-topic: not limited to a Signal topic, can run any combination of prove skills, web searches, and custom experiments. Use for open-ended research questions that may span multiple namespaces or require custom experiment sequences. Output: Qx.md style research document with hypothesis, experiments, findings, and principles.

Write artifact to: simulations/prove/research/{topic}-research-{date}.md
