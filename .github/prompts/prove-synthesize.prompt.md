---
mode: agent
description: "Answer-first evidence synthesis with confidence rating and counter-evidence."
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


Merge all investigation signals into an answer-first synthesis. Structure: answer (yes/no/maybe), confidence (0-100), key evidence (top 3 signals that most influenced the answer), counter-evidence (what argues against), principles extracted (what this tells us beyond this specific hypothesis), open questions (what the investigation did not resolve). The synthesis is the deliverable -- it supersedes the individual investigation signals.

Write artifact to: signals/prove/investigations/{topic}-synthesis-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
