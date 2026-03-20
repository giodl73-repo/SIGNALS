---
mode: agent
description: "Cross-system integration tracing through connectors and APIs with gap analysis."
---
Trace cross-system interaction through connectors, APIs, and MCP. For each cross-system call: request format, authentication, rate limits, response handling, retry logic, error propagation. Identify: authentication gaps, rate limit exposure, error swallowing, missing idempotency. Stock roles: Connectors / backend integration domain expert.

Write artifact to: signals/flow/integration/{topic}-integration-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
