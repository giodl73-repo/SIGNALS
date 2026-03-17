---
agent: 'agent'
tools: ['codebase']
description: 'System developer simulates the platform. Request tracing, state validation, contract testing, component trees, deployment impact, migration safety, and permission walk-through. Full default.
'
---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Hand-compile a request through service boundaries, APIs, and middleware. Step by step: entry point, authentication, routing, each service boundary crossed, storage access, response assembly, error paths. No boundary skipped. Identify: failure points at each boundary, latency sources, authorization gaps, batch operation edge cases. Stock roles: Dataverse / Commerce / Automate platform expert auto-selected from context.

Write artifact to: simulations/trace/request/{topic}-request-{date}.md
