---
name: signal-prove-intelligence
description: Internal source evidence search with file-path citations and relevance assessment.
allowed-tools: [Read, Write, Glob, Grep]
param_set: full
---
Search internal sources (repo files, design docs, scenarios, prior signals) for evidence. For each source: file path, relevant excerpt, relevance to hypothesis, strength of evidence. Internal evidence is often stronger than public evidence for product-specific hypotheses.

Write artifact to: simulations/prove/investigations/{topic}-intelligence-{date}.md
