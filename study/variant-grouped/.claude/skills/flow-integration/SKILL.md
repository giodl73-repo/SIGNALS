---
name: flow-integration
description: Cross-system integration tracing through connectors and APIs with gap analysis.
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Trace cross-system interaction through connectors, APIs, and MCP. For each cross-system call: request format, authentication, rate limits, response handling, retry logic, error propagation. Identify: authentication gaps, rate limit exposure, error swallowing, missing idempotency. Stock roles: Connectors / backend integration domain expert.

Write artifact to: simulations/flow/integration/{topic}-integration-{date}.md
