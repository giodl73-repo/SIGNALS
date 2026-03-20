# simlab

This is your Signal workspace. Run investigations here, keep artifacts here.

## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Namespaces**:
- discover: /discover-competitors, /discover-feasibility, /discover-inertia, /discover-hypothesis, /discover-risk, /discover-analysis, /discover-synthesize
- specify: /specify-spec, /specify-proposal, /specify-pitch, /specify-commitment, /specify-abstract
- validate: /validate-design, /validate-users, /validate-customers, /validate-code, /validate-adoption, /validate-feedback, /validate-support
- simulate: /simulate-lifecycle, /simulate-request, /simulate-state, /simulate-contract, /simulate-conversation, /simulate-argument
- rhythm: /rhythm-decide, /rhythm-status, /rhythm-story, /rhythm-qa, /rhythm-brief, /rhythm-rebuttal
- roles: /roles-scan, /roles-build, /roles-check, /roles-product-review, /roles-pull-request
- research: /research-pre-write, /research-post-write
- tools: /tools-coverage, /tools-preview, /tools-accept
- signal: /signal, /signal-health, /signal-setup

**Inertia rule**: The primary competitor is always inertia. Every investigation answers
why teams would do nothing instead.

**Context**: Read CONTEXT.md at the start of every skill run for workspace context,
active topics, and repo pointers.

**Topics**: Topic slugs live in CONTEXT.md ## Topics. When a skill run introduces a new
topic slug that is not already in that table, add it before writing any artifacts.
Status values: active / paused / decided.

**Artifacts**: signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
Topic slugs come from CONTEXT.md ## Topics table.
Use /tools-coverage <topic> to check coverage gaps.
Use /rhythm-status <topic> to see readiness.
Use /signal-health to check workspace health.
