---
name: signal-org
description: "Org namespace: role registry (/signal-org-roles), org chart (/signal-org-chart), org review (/signal-org-review), committee simulation (/signal-org-committee).
"
allowed-tools: [Read, Write, Glob]
param_set: standard
---
Generate a typed role registry for a domain. Analyzes the product, codebase, or spec to determine what expert perspectives are needed. Each role gets: name, orientation (frame + serves), lens (verify questions + simplify rules), expertise (depth + relevance), scope, collaborates_with. Output is a .craft/roles/{area}/ directory of markdown role files. Inertia check: include a devil-advocate role whose job is to challenge every proposal with why the status quo is sufficient. Stock structure: PM, Architect, Strategy, domain experts auto-selected from context.

Write artifact to: .craft/roles/{domain}/
