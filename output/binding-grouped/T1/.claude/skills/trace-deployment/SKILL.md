---
name: trace-deployment
description: Deployment sequence tracing with pre-checks, validation, and rollback path.
allowed-tools: [Read, Write, Glob]
param_set: analysis
---
Trace what happens when you deploy, import, or migrate a solution. Step by step: pre-deploy checks, deployment sequence, post-deploy validation, rollback path. Identify: missing pre-checks, deployment order dependencies, missing rollback triggers, post-deploy validation gaps. Stock roles: Commerce / Operations deployment domain expert.

Write artifact to: simulations/trace/deployment/{topic}-deployment-{date}.md
