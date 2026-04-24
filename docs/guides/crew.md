# crew — Org Review Without Configuration

## The short version

The crew namespace runs artifacts through your org's expert perspectives. Two skills:
crew-roles generates the role registry for a domain, crew-review runs any artifact through
relevant roles. Zero config required -- stock roles activate by default when no .roles/
directory exists.

---

## When to use this namespace

Use crew when you want org-level review without setting up a full corp configuration. Crew
is the lightweight path to multi-perspective review: it does not require org.yaml, does not
require a pre-built role registry, and produces useful output on the first run.

- You want a spec reviewed by multiple expert perspectives before the design meeting.
- You do not have .roles/ configured but want expert review now.
- You have roles configured and want to run an artifact through all of them.
- You want to generate a role registry for a new domain before setting up corp.

Crew and corp are complementary, not alternatives. Crew is the first step: run crew-review
on any artifact with no setup. Corp is the scaled version: configure org.yaml, build the
full role tree, run ROB stages and PR reviews. Teams typically start with crew and graduate
to corp as their org configuration matures.

---

## The virtual company model (crew edition)

When `.roles/` does not exist, crew uses a set of stock roles that cover the most
common expert perspectives for software feature review:

- Architect: system design, scalability, dependencies
- PM: user value, scope, feasibility
- Engineer: implementation complexity, testing, maintenance
- UX Designer: usability, accessibility, user flow
- Security Architect: auth, access control, data exposure
- Compliance: regulatory, policy, data handling
- Inertia Advocate: status quo defense, switching cost, adoption risk

The Inertia Advocate is always included. Their job is to make the case that the current
workaround is sufficient. If the feature cannot answer the Inertia Advocate's objections,
it is not ready.

When `.roles/` exists, crew reads it and selects relevant roles based on the artifact
type and content signals. A spec mentioning RBAC gets the Security Architect. A spec mentioning
data migration gets the Compliance role. Stock roles fill in where specific roles are not found.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `crew-roles` | Generates a typed role registry for a domain. Analyzes product/codebase to determine expert perspectives needed. Each role gets orientation, lens, expertise, scope, collaborates_with. Inertia-advocate always included. Outputs .roles/{area}/ directory. | Before switching from crew to corp. When you want to customize the role definitions. |
| `crew-review` | Runs any artifact through the full org (or stock roles if no .roles/ exists). Per-role findings with severity. Review matrix: role, findings, severity, recommendation. --depth deep runs all roles; standard runs relevant roles only. | Anytime you have an artifact worth reviewing. No config required. |

---

## Example workflow

You have a draft spec and want expert review before sharing with the team.

**Step 1: Run crew-review with no setup.**

```
/crew-review payment-reminders-spec-2026-03-16.md
```

No .roles/ detected. Stock roles activate. Seven roles review the spec.

The Security Architect flags: no mention of who can access the unsubscribe list (P1).
The Inertia Advocate flags: the current spreadsheet process has 100% team adoption and
requires no training -- what is the explicit adoption plan for this feature? (P2).
The UX Designer flags: the reminder preview flow is described but no mockup or wireframe
referenced (P3).

Review matrix produced. Three P1/P2/P3 findings with role attribution.

**Step 2: Generate domain-specific roles.**

After a few crew-review runs, you want sharper reviews calibrated to your specific domain.

```
/crew-roles payment-reminders
```

Analyzes the repo and the existing spec. Generates `.roles/billing/` with:
- Billing Architect: invoicing platform, payment flows, reconciliation
- Finance Domain Expert: accounting controls, audit requirements, period-end
- Inertia Advocate: the spreadsheet workflow defense

Next crew-review run uses these roles instead of stock roles. Reviews are more specific.

**Step 3: Run with depth deep for final review.**

```
/crew-review payment-reminders-spec-2026-03-16.md --depth deep
```

All roles in .roles/ review the artifact, not just the auto-selected relevant ones.
More findings, but complete coverage. Use --depth deep before a major commit or release.

---

## What it produces

crew-review writes to `simulations/crew/`:

```
simulations/crew/
  payment-reminders-review-2026-03-16.md
```

crew-roles writes to `.roles/`:

```
.roles/
  billing/
    billing-architect.md
    finance-domain-expert.md
    inertia-advocate.md
```

Example frontmatter for crew-review output:

```yaml
---
skill: crew-review
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Start with crew, graduate to corp.** Crew's stock roles are designed to be useful
immediately. As your domain understanding deepens and your role definitions become more
specific, run crew-roles to generate domain roles, then configure org.yaml to move to corp.
You do not have to make this transition -- crew is fully functional indefinitely. But corp
unlocks ROB stages, PR review automation, and committee simulation.

**The Inertia Advocate finding is always worth reading first.** Every crew-review includes
an Inertia Advocate finding. Read this one before the others. If the Inertia Advocate's
objection is not answerable by the spec, that is a signal to run scout-competitors again
and strengthen the inertia case.

**crew-review on any artifact, not just specs.** Crew-review works on specs, proposals,
pitch documents, architecture decisions, investigation summaries, and program plans. Any
written artifact benefits from multi-perspective review. The stock roles are calibrated
to be useful across all artifact types.

---

## What's next

- **[corp](corp.md)** -- the scaled version of crew. Configure org.yaml, build the full role tree, run ROB stages.
- **[review](review.md)** -- crew-review and review-design are complementary. review-design uses discipline-based roles; crew-review uses your org's roles.
- **[ACHIEVEMENTS](../ACHIEVEMENTS.md)** -- First Review is earned by running crew-review for the first time.
