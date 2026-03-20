---
mode: agent
description: "Run the full decision intelligence suite for a topic. Combines scout + prove into a"
---
Run the full pre-commitment intelligence suite for: {{topic}}

This domain skill runs the complete decision evidence campaign before feature commitment.
Execute these skills in sequence, feeding each output to the next:

1. **scout-competitors** — identify the competitive landscape and why inertia is the primary threat
2. **scout-feasibility** — assess whether the feature is buildable given current constraints  
3. **scout-market** — size the market and identify the target segment
4. **prove-hypothesis** — frame the core product hypothesis and its falsification conditions
5. **prove-websearch** — gather external evidence for the hypothesis
6. **prove-synthesize** — synthesize all evidence into a decision brief

For each skill: run it, capture the output as a signal artifact, then proceed.
Final output: a decision brief at signals/{{topic}}/decide-{{date}}.md summarizing
the evidence and stating a clear recommendation: COMMIT / PAUSE / PIVOT / ABANDON.
