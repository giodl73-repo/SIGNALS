---
name: signal-prove-synthesize
description: Answer-first evidence synthesis with confidence rating and counter-evidence.
allowed-tools: [Read, Write, Glob]
param_set: full
---
Merge all investigation signals into an answer-first synthesis. Structure: answer (yes/no/maybe), confidence (0-100), key evidence (top 3 signals that most influenced the answer), counter-evidence (what argues against), principles extracted (what this tells us beyond this specific hypothesis), open questions (what the investigation did not resolve). The synthesis is the deliverable -- it supersedes the individual investigation signals.

Write artifact to: simulations/prove/investigations/{topic}-synthesis-{date}.md
