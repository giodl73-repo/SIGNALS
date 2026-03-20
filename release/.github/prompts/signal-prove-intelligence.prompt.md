---
mode: agent
description: "Internal source evidence search with file-path citations and relevance assessment."
---
Search internal sources (repo files, design docs, scenarios, prior signals) for evidence. For each source: file path, relevant excerpt, relevance to hypothesis, strength of evidence. Internal evidence is often stronger than public evidence for product-specific hypotheses.

Write artifact to: signals/prove/investigations/{topic}-intelligence-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
