---
mode: agent
description: "Sequence skills into a staged program plan with gates and topic tracking. Generate program.yaml for the topic: stages (n"
---
You are running /specify-commitment for: {{topic}}

Translate the gathered signals into a staged commitment plan. Scan what signals exist, sequence the remaining work into phases with artifact-verifiable gates, and produce a commitment document that answers: what are we committing to, in what order, and what must be true at each gate before proceeding?

---

## PHASE 1 -- SIGNAL INVENTORY

Glob: signals/**/{{topic}}-*
List all artifacts found by namespace. Note which namespaces have zero coverage.

| Namespace | Artifact count | Key findings |
|-----------|---------------|--------------|
| discover | | |
| specify | | |
| validate | | |
| simulate | | |
| prove | | |
| listen | | |
| rhythm | | |

Coverage summary: N/9 namespaces covered. Commitment confidence: [HIGH / MEDIUM / LOW]

---

## PHASE 2 -- STAGED COMMITMENT PLAN

For this topic, sequence the remaining work into 2-4 phases. Each phase has:
- A purpose (what question this phase answers, not a namespace label)
- Specific Signal skills to run (use actual skill names from the catalog)
- An artifact-verifiable gate (what artifact must exist before the next phase starts)

**Phase 1 -- [Purpose: e.g., "Establish feasibility and competitive position"]**
Skills: /discover-competitors, /discover-feasibility, /discover-requirements
Gate: discover-competitors + discover-feasibility artifacts both present for this topic
If gate fails: [what to do -- e.g., "revisit the problem framing before proceeding"]

**Phase 2 -- [Purpose]**
Skills: [from Signal catalog]
Gate: [artifact-verifiable condition]

[continue for each phase]

---

## PHASE 3 -- COMMITMENT DECISION

```
Topic: {{topic}}
Phases committed: N
Estimated Signal sessions: N (each session ~4-6 skills)

Commit to proceed: YES / NO / CONDITIONAL
If CONDITIONAL: [what must be resolved before full commitment]

The primary inertia risk: [what happens if the team delays this investigation]
The primary signal gap: [which namespace's absence creates the most uncertainty]
```

---

## PHASE 4 -- AMEND

Three adjustments to sharpen the commitment plan:
1. [Tighten the gate condition for Phase 1 -- make it more specific]
2. [Add a signal that is missing but would change the commit/no-commit decision]
3. [Identify the highest-uncertainty assumption in the current plan]

Write artifact to: signals/specify/commitment/{{topic}}-commitment-{{date}}.md
If --output <path> was provided: write to <path>/{{topic}}-[skill]-{{date}}.md instead (flat, no namespace prefix).
Include frontmatter: skill: specify-commitment, topic: {{topic}}, date: {{date}}, phases: [n], coverage: [n]/9