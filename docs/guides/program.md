# program — Investigation Planning and Orchestration

## The short version

The program namespace turns a pile of signals into a staged plan. One skill: program-plan.
It sequences skills into gates-based stages and generates a program.yaml for the topic.
The program is a plan, not an executor -- every skill still runs standalone.

---

## When to use this namespace

Use program when you are about to start a multi-skill investigation and want to plan it
before running it. The program namespace is for leads and PMs who want to manage an
investigation as a tracked artifact, not just a series of ad-hoc runs.

- You have a complex feature that will require 10+ signals and you want a staged plan.
- A team is running a shared investigation and you want to assign skill ownership by role.
- You want to define explicit gates between stages: "do not proceed to flow simulation until
  scout and draft are complete."
- You want a written artifact that shows the planned investigation for stakeholder review.

program-plan is optional. Every skill runs standalone without it. The program is an editorial
plan -- it describes which namespaces to cover, in what order, who owns each signal, and what
gates must pass before advancing. It does not run the skills for you.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `program-plan` | Sequences skills into staged investigation plan with gates. Generates program.yaml. Final stage is always echo (auto, no skills). Reads topic strategy if available. | Before a multi-skill investigation. After topic-new. |

---

## Example workflow

You have registered a new topic for a major feature: "multi-currency-billing." It will
require coverage across all nine namespaces and involves two teams. You want a plan.

**Step 1: Open the topic.**

```
/topic-new multi-currency-billing
```

Registers in TOPICS.md. Creates strategy.md. The strategy is the starting point for program-plan.

**Step 2: Generate the program.**

```
/program-plan multi-currency-billing
```

Reads strategy.md. Generates a staged program:

```
Stage 1 -- Discovery
  skills: scout-competitors, scout-feasibility, scout-compliance, scout-requirements
  gate: all 4 complete, feasibility score >= 60
  owner: PM + Architect

Stage 2 -- Design
  skills: draft-spec, draft-proposal
  gate: spec reviewed by at least one review skill
  owner: PM

Stage 3 -- Review
  skills: review-design, review-users
  gate: no P1 findings unresolved
  owner: PM + UX

Stage 4 -- Simulation
  skills: flow-lifecycle, flow-dataflow, flow-resilience
  gate: no unaddressed state machine gaps
  owner: Architect + Dev

Stage 5 -- Evidence
  skills: prove-hypothesis, prove-websearch, prove-synthesize
  gate: synthesis answer is not INCONCLUSIVE
  owner: PM + Researcher

Stage 6 -- Listen
  skills: listen-feedback, listen-adoption
  gate: NPS >= 7.0
  owner: PM

Stage 7 -- Echo (auto)
  No skills. Synthesize unexpected findings.
```

Writes `simulations/program/plans/multi-currency-billing-program-2026-03-16.md` and
`program.yaml` for tracking.

---

## What it produces

program artifacts write to `simulations/program/plans/`:

```
simulations/program/
  plans/  multi-currency-billing-program-2026-03-16.md
```

Plus a `program.yaml` in the topic directory for structured tracking:

```yaml
topic: multi-currency-billing
date: 2026-03-16
stages:
  - name: Discovery
    skills: [scout-competitors, scout-feasibility, scout-compliance, scout-requirements]
    gate: feasibility_score >= 60
    status: pending
```

Example frontmatter:

```yaml
---
skill: program-plan
topic: multi-currency-billing
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**The final stage is always echo.** program-plan always ends with an echo stage -- no skills,
auto-generated from the gathered signals. This is Signal's mechanism for capturing unexpected
findings after all essential signals are in. You cannot skip it by design.

**Gates are commitments, not recommendations.** A program gate says: do not proceed to the
next stage until this condition is met. This is not enforced automatically -- Signal is a
planning tool, not an executor. But the gate is a documented commitment. If your team advances
past a gate without meeting the condition, that decision should be recorded, not ignored.

**program-plan is most valuable for shared investigations.** Solo investigations rarely need
a formal plan -- you can run skills as needed and check topic-status for coverage. Where
program-plan earns its place is in team investigations where multiple contributors need to
know what they own, what order matters, and what gates control progress.

---

## What's next

- **[topic](topic.md)** -- topic-status and topic-report show progress against the program plan.
- **[scout](scout.md)** -- Stage 1 in almost every program. Start here.
- **[corp](corp.md)** -- for features requiring ROB sign-off, corp-rob can be added as a program gate.
