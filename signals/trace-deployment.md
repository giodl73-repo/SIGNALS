confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence


Trace what happens when you deploy, import, or migrate a solution. Step by step: pre-deploy checks, deployment sequence, post-deploy validation, rollback path. Identify: missing pre-checks, deployment order dependencies, missing rollback triggers, post-deploy validation gaps. Stock roles: Commerce / Operations deployment domain expert.

Write artifact to: signals/trace/deployment/{topic}-deployment-{date}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
