---
name: signal-scout-feasibility
description: Technical feasibility assessment with traffic-light ratings and budget chain.
allowed-tools: [Read, Write, Glob, Grep]
param_set: standard
---
Assess whether a product idea is technically feasible given current constraints. Scan repo for stack signals (package.json, tsconfig.json, Cargo.toml). Always surface inferred team size and timeline explicitly -- never silently infer. Traffic-light rating per component (green/yellow/red). Overall feasibility score 0-100. Stock roles: Architect (complexity scoring), PM (timeline overlay), Strategy (build-vs-buy per component).

Write artifact to: simulations/scout/feasibility/{topic}-feasibility-{date}.md
