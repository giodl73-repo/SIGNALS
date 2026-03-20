# simlab

This is your Signal workspace. Run investigations here, keep artifacts here.

## Signal

Signal is installed in this workspace. Use Signal skills to gather evidence before
committing to a feature.

**Namespaces**:
- discover: competitors, feasibility, inertia, hypothesis, risk, analysis, synthesize
- specify: spec, proposal, pitch, commitment, abstract
- validate: design, users, customers, code, adoption, feedback, support
- simulate: lifecycle, request, state, contract, conversation, argument
- rhythm: decide, status, story, qa, brief, rebuttal
- roles: scan, build, check, product-review, pull-request
- research: pre-write, post-write
- tools: coverage, preview, accept
- signal: signal, health, setup

**Inertia rule**: The primary competitor is always inertia. Every investigation answers
why teams would do nothing instead.

**Context**: Read CONTEXT.md at the start of every skill run for workspace context,
active topics, and repo pointers.

**Topics**: Topic slugs live in CONTEXT.md ## Topics. When a skill run introduces a new
topic slug that is not already in that table, add it before writing any artifacts.
Status values: active / paused / decided.

**Artifacts**: signals/{namespace}/{skill}/{topic}-{skill}-{date}.md
Topic slugs come from CONTEXT.md ## Topics table.
Use the coverage prompt to check gaps.
Use the rhythm-status prompt to see readiness.
