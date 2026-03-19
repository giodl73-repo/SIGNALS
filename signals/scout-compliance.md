for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Identify regulatory and policy constraints before design begins. Infer applicable frameworks from domain and data type signals. Always distinguish between compliance obligations on the product vs. on the host platform (e.g., SR 11-7 applies to the AI model, not to a structured prompt methodology). Git-native, no-server designs are compliance-favorable -- surface this when applicable. Stock roles: Compliance (framework catalog), Architect (technical constraints), PM (timeline impact), Strategy (market access vs. cost).

Write artifact to: signals/scout/compliance/{topic}-compliance-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
