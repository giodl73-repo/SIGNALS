---
mode: agent
description: "General-purpose research orchestrator for open-ended research questions."
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


General-purpose research orchestrator. Takes a research question, plans experiments (which prove skills + web searches + data analysis), runs them in sequence, feeds outputs forward, synthesizes findings. More flexible than prove-topic: not limited to a Signal topic, can run any combination of prove skills, web searches, and custom experiments. Use for open-ended research questions that may span multiple namespaces or require custom experiment sequences. Output: Qx.md style research document with hypothesis, experiments, findings, and principles.

Write artifact to: signals/prove/research/{topic}-research-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
