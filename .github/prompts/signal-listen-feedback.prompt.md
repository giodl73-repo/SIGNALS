---
mode: agent
description: "Pre-ship customer reaction simulation with per-persona NPS prediction and threshold gate."
---
Simulate customer reactions to a spec or design before it ships. All 12 customer personas (C-01 through C-12) read the spec through their lens. Per-persona feedback cards with severity (blocking/major/minor/cosmetic) and NPS prediction (1-10). Cross-persona theme matrix. Aggregate NPS threshold: 7.0. Below 7.0 = spec needs revision. Stock roles: C-01 through C-12, PM, UX.

Write artifact to: signals/listen/feedback/{topic}-feedback-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
