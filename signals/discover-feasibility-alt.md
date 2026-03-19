You are running /discover-feasibility-alt for: {{topic}}

Unified feasibility analysis with optional focus dimension woven throughout. Covers technical, resource, and timeline feasibility in a single coherent assessment.

--focus options: technical | resource | timeline | compliance | integration
Default: balanced (all three dimensions weighted equally).

---

## PHASE 1 -- INERTIA FEASIBILITY CHECK

Before assessing build feasibility, assess the feasibility of doing nothing:
- Is the status quo workaround sustainable? (Y/N + reason)
- At what scale does the workaround break down?
- Cost of the workaround continuing 12 months: [quantified]

If the workaround is sustainable and cheap: flag "Inertia is feasible -- build case must clear this bar."

---

## PHASE 2 -- FEASIBILITY ASSESSMENT

**Technical feasibility**
- Hardest technical problem to solve
- Known unknowns / research required
- Dependencies on external systems or teams
- Risk: HIGH / MEDIUM / LOW + rationale
If --focus technical: proof-of-concept path, build vs buy per hard component, estimated eng-weeks.

**Resource feasibility**
- Team skills required vs available
- Estimated scope (days / weeks / months / quarters)
- Key constraint: [the single resource that most limits this]
- Risk: HIGH / MEDIUM / LOW + rationale
If --focus resource: skill gap analysis, hiring vs upskilling tradeoff.

**Timeline feasibility**
- Earliest realistic ship date
- What must be true to hit that date
- Key dependency on critical path
- Risk: HIGH / MEDIUM / LOW + rationale
If --focus timeline: phase breakdown, gates that can vs cannot slip, risk-adjusted timeline.

If --focus compliance: add regulatory, legal, and policy constraints.
If --focus integration: add API, data, and system integration requirements.

---

## PHASE 3 -- VERDICT

Technical:  [HIGH/MEDIUM/LOW risk] -- [rationale]
Resource:   [HIGH/MEDIUM/LOW risk] -- [rationale]
Timeline:   [HIGH/MEDIUM/LOW risk] -- [rationale]

Overall: PROCEED / PROCEED-WITH-GATES / INVESTIGATE-FIRST / BLOCK

Blocking condition (if BLOCK or INVESTIGATE-FIRST): [what must be resolved]

---

## PHASE 4 -- AMEND

Three adjustments:
1. [Shift focus dimension to expose a different risk angle]
2. [Tighten the hardest technical problem -- be more specific]
3. [Adjust timeline estimate based on resource constraint]

Write artifact to: signals/discover/feasibility-alt/{{topic}}-feasibility-alt-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-feasibility-alt-{date}.md). No namespace subdirectory.
Include frontmatter: skill: discover-feasibility-alt, topic: {{topic}}, date: {{date}}, focus: [dimension or balanced], verdict: [verdict]
