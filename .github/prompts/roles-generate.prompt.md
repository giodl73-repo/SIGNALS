---
mode: agent
description: "Generate a typed role registry for a domain. Analyzes product/codebase to determine what expert perspectives are needed. Roles hold tensions, not single lenses."
---
for: {value}
# pm       -> adoption, user value, competitive positioning
# engineer -> implementation, edge cases, technical debt
# exec     -> risk, cost, strategic alignment
# team     -> shared understanding, action items, ownership

If --for pm: frame findings for product managers (adoption, user value, positioning).
If --for engineer: frame findings for engineers (implementation, edge cases, technical depth).
If --for exec: frame findings for executives (risk, cost, strategic alignment, ROI).
If --for team: frame findings for team discussions (shared understanding, action items).

---

## PHASE 1 — DOMAIN SCAN

Scan the product/codebase to identify what expert perspectives are needed.

Sources to check:
- Repository structure, languages, frameworks
- Existing .craft/roles/ (avoid duplicating installed roles)
- Recent signal artifacts (what domains have been reviewed)
- README, CLAUDE.md, or equivalent project docs

Identify 4-8 domain areas that need reviewer coverage.

---

## PHASE 2 — ROLE CANDIDATES

For each domain area, propose a role. Every role MUST hold a tension — two concerns that
pull against each other. A single-domain-focus role is incomplete.

| # | Role slug | Tension (concern A vs concern B) | Audience ({value}) |
|---|-----------|----------------------------------|-------------------|
| 1 | | | |
| 2 | | | |
| ... | | | |

**Inertia-advocate is always included** — it holds "status quo safety" vs "opportunity cost
of not changing" in tension.

### Tension validation

For each candidate, verify:
- The two concerns are genuinely distinct (not two words for the same thing)
- The tension is productive (reviewing from either side alone would miss something)
- The role's findings will differ from adjacent roles

Flag any role that fails validation. Rewrite or merge before proceeding.

---

## PHASE 3 — GENERATE ROLES

For each validated candidate, generate a full role file using the roles-build structure:
orientation (frame with tension), lens (verify + simplify), expertise, collaborates_with.

Write each role to: `.craft/roles/{area}/{role-slug}.md`

---

## PHASE 4 — REGISTRY REVIEW

| Role | Tension | Overlap with existing? | Coverage gap? |
|------|---------|----------------------|---------------|
| | | | |

If two generated roles cover the same tension from the same angle: merge them.
If a gap exists that no role covers: add a role.

---

Write artifact to: signals/roles/generate/{topic}-roles-generate-{date}.md

Frontmatter:
```
skill: roles-generate
topic: {topic}
date: {date}
roles_generated: {N}
audience: {value}
```

AMEND: add more roles, adjust level distribution, sharpen tensions.
