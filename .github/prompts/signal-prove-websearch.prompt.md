---
mode: agent
description: "Web evidence gathering with direct quotes, URLs, and strength-of-evidence rating per source."
---
Search the public web for evidence supporting or refuting the hypothesis. For each search: query used, sources found, evidence extracted (direct quotes with URLs), relevance to hypothesis, strength of evidence (strong/weak/mixed). Cite sources. Do not paraphrase without attribution. Do not use training data as evidence -- every claim must have a URL.

Write artifact to: signals/prove/investigations/{topic}-websearch-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
