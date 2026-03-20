---
mode: agent
description: "Technical feasibility assessment with traffic-light ratings and budget chain."
---
Assess whether a product idea is technically feasible given current constraints. Scan repo for stack signals (package.json, tsconfig.json, Cargo.toml). Always surface inferred team size and timeline explicitly -- never silently infer. Traffic-light rating per component (green/yellow/red). Overall feasibility score 0-100. Stock roles: Architect (complexity scoring), PM (timeline overlay), Strategy (build-vs-buy per component).

Write artifact to: signals/scout/feasibility/{topic}-feasibility-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
