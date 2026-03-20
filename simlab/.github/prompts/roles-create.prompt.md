---
mode: agent
description: "Create a new role or sub-role in .craft/roles/. Three modes: (1) name only -- /roles-create backend:healthcare generates"
---
You are running /roles-create for: {{topic}}

Create a new Signal-compatible role file in .craft/roles/. Three modes:
- Name only: `/roles-create backend:healthcare` -- generates a healthcare-specialist backend role
- With description: `/roles-create "fintech compliance reviewer"` -- infers domain from description
- With context: `/roles-create security --for api-gateway` -- tailors lens.verify to the specific artifact type

---

## PHASE 1 -- ROLE IDENTIFICATION

Determine from the invocation:
- Role slug (e.g., `healthcare-backend`, `fintech-compliance`)
- Domain directory (e.g., `.craft/roles/backend/`, `.craft/roles/compliance/`)
- Primary artifact types this role will review
- Who will use this role's findings (PM / engineer / exec / security)

If .craft/roles/ does not exist: note it will be created.

---

## PHASE 2 -- GENERATE ROLE FILE

Write a complete Signal role with all required fields:

```yaml
---
name: {role-slug}
version: "1.0"
archetype: craft

orientation:
  frame: "[What this role focuses on -- specific domain concern, not generic. Must name the failure modes this role catches that generic roles miss.]"
  serves: "[Who benefits from this role's findings -- name the specific team or decision-maker and what question this role answers for them.]"

lens:
  verify:
    - "[Specific check 1 -- names an exact thing to look for]"
    - "[Specific check 2]"
    - "[Specific check 3]"
    - "[Specific check 4]"
    - "[Specific check 5]"
    - "[Specific check 6]"
  simplify:
    - "[Simplification principle 1 -- what this role deprioritizes so signal stays clean]"
    - "[Simplification principle 2]"
    - "[Simplification principle 3]"

expertise:
  depth: "[Specific domain knowledge this role applies]"
  relevance: "[When this role fires -- specific artifact types or topic domains that activate it]"

collaborates_with:
  - [role-slug-1]
  - [role-slug-2]
---
```

Minimum 6 lens.verify items. Each must name a specific, checkable condition -- not a category name.

---

## PHASE 3 -- AMEND

Three targeted improvements to the generated role:
1. [Sharpen lens.verify item that is most generic -- make it name a specific mechanism]
2. [Add a lens.verify item that catches the most common failure mode for this domain]
3. [Tighten orientation.frame -- ensure it names what generic roles miss]

Write role to: .craft/roles/{domain}/{role-slug}.md
Write artifact to: signals/roles/create/{{topic}}-roles-create-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-roles-create-{date}.md). No namespace subdirectory.
Include frontmatter: skill: roles-create, topic: {{topic}}, date: {{date}}, role_created: {role-slug}, domain: {domain}