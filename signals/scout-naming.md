for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Generate and evaluate candidate names using multi-persona scoring. Supports --validate <name> to pin an existing name at row 1 and produce a validation summary alongside alternatives. Generate 10-15 candidates. Score across PM (memorability), Design (visual weight), UX (speakability), GTM (searchability), Strategy (positioning fit). Collision check against package registries and domains. Stock roles: PM, Design, UX, GTM, Strategy.

Write artifact to: signals/scout/naming/{topic}-naming-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
