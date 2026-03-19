Generate a typed role registry for a domain. Analyzes the product, codebase, or spec to determine what expert perspectives are needed. Each role gets: name, orientation (frame + serves), lens (verify questions + simplify rules), expertise (depth + relevance), scope, collaborates_with. Output is a .craft/roles/{area}/ directory of markdown role files. Inertia check: include a devil-advocate role whose job is to challenge every proposal with why the status quo is sufficient. Stock structure: PM, Architect, Strategy, domain experts auto-selected from context.

Write artifact to: .craft/roles/{domain}/
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
