# scout — Market and Technical Intelligence

## The short version

The scout namespace answers "why would teams do nothing?" before you write a spec. Eight
skills cover competitors, feasibility, naming, compliance, market size, stakeholders, positioning,
and requirements. Inertia is always the primary competitor. Scout first.

---

## When to use this namespace

Use scout whenever you have a feature idea and want to understand the landscape before
committing to a design. The scout namespace is pre-spec evidence: it tells you whether the
feature is worth building and what constraints to design within.

- You have a feature idea and want to check if it is feasible before speccing it.
- You need to understand who the real competitors are (usually inertia).
- You are about to write a spec and want to ground it in requirements and constraints.
- A stakeholder asked "did you check if we need compliance sign-off on this?"
- You need to write a pitch and want positioning that is grounded in actual market reality.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `scout-competitors` | Assesses "none / status quo" first, then 5-8 named competitors with threat scoring. Inertia is always PRIMARY. | First. Always. Before anything else for any feature. |
| `scout-feasibility` | Traffic-light rating per component, overall feasibility score 0-100, team size and timeline inferred from repo. | Before drafting any spec. Catches blockers early. |
| `scout-requirements` | MoSCoW prioritization, dependency graph, ambiguity flags, suspicious silences. | Before draft-spec. Gives the spec its requirements grounding. |
| `scout-market` | TAM/SAM/SOM, segment ranking by fit, beachhead recommendation. | When you need to size the opportunity or pick a first target. |
| `scout-stakeholders` | Power/interest grid, veto risks, champion identification, communication strategy. | When a decision involves multiple teams or approvers. |
| `scout-positioning` | Per-audience positioning statements, competitive differentiation matrix, anti-positioning. Loads scout-competitors if available. | Before a pitch, a launch, or any external communication. |
| `scout-naming` | 10-15 name candidates, multi-persona scoring, registry collision check. Supports --validate to score an existing name. | When naming a feature, product, or API. |
| `scout-compliance` | Regulatory and policy constraints, framework identification, compliance timeline impact. | For any feature touching data, auth, payments, or regulated domains. |

---

## Example workflow

You have an idea for a feature called "payment-reminders" -- automated reminders for overdue
invoices.

**Step 1: Scout the inertia case.**

```
/scout-competitors payment-reminders
```

Output opens with "The Primary Competitor: why teams do nothing." You learn that the current
workaround is a Slack channel with a manual weekly spreadsheet review. Teams have been doing
it for two years and it works well enough. Threat: HIGH. You now have the inertia case.

**Step 2: Check feasibility.**

```
/scout-feasibility payment-reminders
```

Scans your repo for stack signals. Finds you are on a platform that throttles email sends to
3 per minute per org. Flags this as YELLOW: doable but requires backpressure design. The spec
will need to address this.

**Step 3: Extract requirements.**

```
/scout-requirements payment-reminders
```

Produces a MoSCoW list with 14 requirements. Flags one suspicious silence: no requirement
around "unsubscribe" -- which is almost certainly a compliance need. You add it.

**Step 4: Check your topic status.**

```
/topic-status payment-reminders
```

Scout namespace: 3 of 8 skills covered. Readiness for spec: enough to proceed.

---

## What it produces

All scout artifacts write to `simulations/scout/{skill-name}/`:

```
simulations/scout/
  competitors/    payment-reminders-competitors-2026-03-16.md
  feasibility/    payment-reminders-feasibility-2026-03-16.md
  requirements/   payment-reminders-requirements-2026-03-16.md
  market/         payment-reminders-market-2026-03-16.md
  stakeholders/   payment-reminders-stakeholders-2026-03-16.md
  positioning/    payment-reminders-positioning-2026-03-16.md
  naming/         payment-reminders-naming-2026-03-16.md
  compliance/     payment-reminders-compliance-2026-03-16.md
```

Every artifact opens with standard frontmatter:

```yaml
---
skill: scout-competitors
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Run scout-competitors before everything else.** The inertia case is the most important
signal Signal produces. If you cannot explain why inertia loses, you are not ready to build.
scout-competitors answers that question in 10 minutes.

**scout-positioning degrades silently without scout-competitors context.** The skill will
warn you and run a lightweight competitor pass inline, but the positioning will be weaker.
Run them in order.

**scout-requirements and scout-feasibility together form the minimum pre-spec kit.** A
draft-spec written with both artifacts available as context produces stronger specs than
one written cold. Chain these before reaching for draft-spec.

---

## What's next

- **[draft](draft.md)** -- write the spec. Use scout-requirements and scout-feasibility as context.
- **[review](review.md)** -- review the spec against real user and customer personas.
- **[prove](prove.md)** -- test the core assumption. Especially: is the inertia case actually beatable?
- **[listen](listen.md)** -- simulate adoption before ship. Addresses the "teams will just keep their spreadsheet" risk.
