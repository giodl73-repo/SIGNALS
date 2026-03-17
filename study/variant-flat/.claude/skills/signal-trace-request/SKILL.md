---
name: signal-trace-request
description: Request hand-compilation through service boundaries with no boundary skipped.
allowed-tools: [Read, Write, Glob, Grep]
param_set: analysis
---
Hand-compile a request through service boundaries, APIs, and middleware. Step by step: entry point, authentication, routing, each service boundary crossed, storage access, response assembly, error paths. No boundary skipped. Identify: failure points at each boundary, latency sources, authorization gaps, batch operation edge cases. Stock roles: Dataverse / Commerce / Automate platform expert auto-selected from context.

Write artifact to: simulations/trace/request/{topic}-request-{date}.md
