---
name: simulate-permissions
description: "Trace who can do what through RBAC, security roles, teams, and field-level security. For each operation: which roles can"
allowed-tools: [Read, Write, Glob]
param_set: lean
---
depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure


Keep total output under 2000 words. If --compact: under 800 words.

Trace who can do what through RBAC, security roles, teams, and field-level security. For each operation: which roles can perform it, which fields are visible, which records are accessible. Identify: privilege escalation paths, missing field-level security, team membership gaps, sharing rule conflicts. Stock roles: Customer Service / Dataverse security expert.
Write artifact to: signals/simulate/permissions/{{topic}}-permissions-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-permissions-{date}.md). No namespace subdirectory.
Include frontmatter: skill: simulate-permissions, topic: {{topic}}, date: {{date}}
