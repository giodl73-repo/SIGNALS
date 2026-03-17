---
name: listen
description: "Listen namespace -- 3 skills for post-ship signal simulation.

/listen-feedback  -> pre-ship customer reaction with per-persona NPS prediction
/listen-support   -> top support ticket prediction for first 90 days
/listen-adoption  -> adoption curve simulation across Rogers archetypes with chasm analysis

Run any sub-skill directly, or describe your feature and the most relevant listen skill will run.
"
allowed-tools: [Read, Write, Glob]
param_set: full
---
Simulate customer reactions to a spec or design before it ships. All 12 customer personas (C-01 through C-12) read the spec through their lens. Per-persona feedback cards with severity (blocking/major/minor/cosmetic) and NPS prediction (1-10). Cross-persona theme matrix. Aggregate NPS threshold: 7.0. Below 7.0 = spec needs revision. Stock roles: C-01 through C-12, PM, UX.

Write artifact to: simulations/listen/feedback/{topic}-feedback-{date}.md
