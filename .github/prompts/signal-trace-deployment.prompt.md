---
mode: agent
description: "Deployment sequence tracing with pre-checks, validation, and rollback path."
---
Trace what happens when you deploy, import, or migrate a solution. Step by step: pre-deploy checks, deployment sequence, post-deploy validation, rollback path. Identify: missing pre-checks, deployment order dependencies, missing rollback triggers, post-deploy validation gaps. Stock roles: Commerce / Operations deployment domain expert.

Write artifact to: signals/trace/deployment/{topic}-deployment-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
