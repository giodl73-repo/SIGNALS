---
mode: agent
description: "Per-audience positioning statements with competitive differentiation."
---
for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Define how a product should be positioned per audience. If a prior scout-competitors run exists, load it -- positioning built without competitor context degrades silently. If no prior run found: note the degradation, run competitor identification inline, flag "run scout-competitors for richer positioning." Per-audience positioning statements, competitive differentiation matrix, messaging hierarchy, anti-positioning. Stock roles: Strategy (framework), GTM (per-audience value props), PM (reality check), Design (narrative coherence).

Write artifact to: signals/scout/positioning/{topic}-positioning-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
