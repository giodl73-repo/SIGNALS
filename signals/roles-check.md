You are running /roles-check for: {{topic}}

Run any artifact through the full installed role set. Reads .roles/ and selects relevant reviewers based on the artifact type and topic domain. Each role reviews from its perspective.

---

## PHASE 1 -- ARTIFACT IDENTIFICATION

Read the artifact provided (or glob signals/**/{topic}-* to find the most recent artifact).

Identify:
- Artifact type (spec / design / code / proposal / adoption analysis / other)
- Domain signals present (security / data / compliance / platform / UX / ...)

---

## PHASE 2 -- ROLE SELECTION

Glob .roles/**/*.md to find all installed roles.
If .roles/ does not exist or is empty: use stock roles (architect, security, PM, engineer, UX, process).

Select relevant roles based on artifact type and domain signals detected. List selected roles and why each was selected.

---

## PHASE 3 -- REVIEW

For each selected role, run its lens.verify checks against the artifact.

Per-role output:

| # | Finding | Severity | Section | Recommendation |
|---|---------|----------|---------|----------------|
| 1 | [finding from this role's lens] | P1/P2/P3 | [reference] | [fix] |

P1 = blocks ship, P2 = must fix, P3 = should fix.
Minimum: quick=2 findings/role, standard=3, deep=5.

---

## PHASE 4 -- SYNTHESIS

```
Roles reviewed: N
P1 blockers: N  |  P2 issues: N  |  P3 notes: N

Verdict: APPROVED / APPROVED-WITH-CONDITIONS / NEEDS-WORK

Top finding: [single most important finding across all roles]
Cross-role consensus: [if 2+ roles flagged the same issue, name it]
```

---

## PHASE 5 -- AMEND

Three amendments based on highest-severity findings:
1. [What to fix, where, and why]
2. [What to fix, where, and why]
3. [What to fix, where, and why]

Write artifact to: signals/roles/check/{{topic}}-roles-check-{{date}}.md
If --output <path> provided: write the artifact flat into <path>/ using the same filename as the default (e.g., {topic}-roles-check-{date}.md). No namespace subdirectory.
Include frontmatter: skill: roles-check, topic: {{topic}}, date: {{date}}, roles_used: [n], p1_count: [n], verdict: [verdict]