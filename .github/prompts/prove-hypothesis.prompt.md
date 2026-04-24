---
mode: agent
description: "Hypothesis framing with claim, falsification condition, confidence, and experiment list."
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


State what you believe and what would change your mind. Entry point to a prove investigation. A hypothesis has: a claim (what you believe), a falsification condition (what evidence would prove it wrong), a confidence level (0-100), and a list of experiments that will test it. The hypothesis is a commitment -- you cannot move the goalposts after seeing results.

Write artifact to: signals/prove/investigations/{topic}-hypothesis-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
