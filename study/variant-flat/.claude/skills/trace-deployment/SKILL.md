---
name: trace-deployment
description: Deployment sequence tracing with pre-checks, validation, and rollback path.
allowed-tools: [Read, Write, Glob]
param_set: analysis
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Trace what happens when you deploy, import, or migrate a solution. Step by step: pre-deploy checks, deployment sequence, post-deploy validation, rollback path. Identify: missing pre-checks, deployment order dependencies, missing rollback triggers, post-deploy validation gaps. Stock roles: Commerce / Operations deployment domain expert.

Write artifact to: simulations/trace/deployment/{topic}-deployment-{date}.md
