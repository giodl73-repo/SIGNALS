---
mode: agent
description: "System developer simulates the platform. Request tracing, state validation, contract testing, component trees, deployment impact, migration safety, an"
---
confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Hand-compile a request through service boundaries, APIs, and middleware. Step by step: entry point, authentication, routing, each service boundary crossed, storage access, response assembly, error paths. No boundary skipped. Identify: failure points at each boundary, latency sources, authorization gaps, batch operation edge cases. Stock roles: Dataverse / Commerce / Automate platform expert auto-selected from context.

Write artifact to: signals/trace/request/{topic}-request-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
