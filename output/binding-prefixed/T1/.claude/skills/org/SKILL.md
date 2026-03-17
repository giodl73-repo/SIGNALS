---
name: org
description: "Org namespace -- 4 skills for organizational simulation.

/org-roles      -> typed role registry with orientation, lens, and expertise
/org-chart      -> org structure with areas, committees, and operating rhythms
/org-review     -> full org review running artifact through all relevant roles
/org-committee  -> committee meeting simulation for ROB, shiproom, or architecture board

Run any sub-skill directly, or describe your organizational need and the most relevant skill will run.
"
allowed-tools: [Read, Write, Glob]
param_set: standard
---
Generate a typed role registry for a domain. Analyzes the product, codebase, or spec to determine what expert perspectives are needed. Each role gets: name, orientation (frame + serves), lens (verify questions + simplify rules), expertise (depth + relevance), scope, collaborates_with. Output is a .craft/roles/{area}/ directory of markdown role files. Inertia check: include a devil-advocate role whose job is to challenge every proposal with why the status quo is sufficient. Stock structure: PM, Architect, Strategy, domain experts auto-selected from context.

Write artifact to: .craft/roles/{domain}/
