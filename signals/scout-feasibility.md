for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership


If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

Assess whether a product idea is technically feasible given current constraints. Scan repo for stack signals (package.json, tsconfig.json, Cargo.toml). Always surface inferred team size and timeline explicitly -- never silently infer. Traffic-light rating per component (green/yellow/red). Overall feasibility score 0-100. Stock roles: Architect (complexity scoring), PM (timeline overlay), Strategy (build-vs-buy per component).

Write artifact to: signals/scout/feasibility/{topic}-feasibility-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
