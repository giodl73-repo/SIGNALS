---
mode: agent
description: "Smallest-possible prototype with defined measure and predicted vs actual results."
---
confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


iterations: 1  # run 1x independently, aggregate findings, mark new vs confirmed


Build something small and measure it. A prototype is the smallest possible thing that tests the hypothesis. Define: what to build, what to measure, what result confirms vs. refutes the hypothesis. Build it. Measure it. Report what actually happened vs. what was predicted.

Write artifact to: signals/prove/investigations/{topic}-prototype-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
