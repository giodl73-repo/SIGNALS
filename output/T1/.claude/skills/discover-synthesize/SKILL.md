---
name: discover-synthesize
description: "Merge all investigation signals into an answer-first synthesis. Structure: answer (yes/no/maybe), confidence (0-100), ke"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Merge all investigation signals into an answer-first synthesis. Structure: answer (yes/no/maybe), confidence (0-100), key evidence (top 3 signals that most influenced the answer), counter-evidence (what argues against), principles extracted (what this tells us beyond this specific hypothesis), open questions (what the investigation did not resolve). The synthesis is the deliverable -- it supersedes the individual investigation signals.