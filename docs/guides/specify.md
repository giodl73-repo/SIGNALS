# specify — Specification and Commitment Authoring

## The short version

The specify namespace turns evidence into written artifacts. Five skills cover specs,
proposals, pitches, brainstorms, and commitment plans. Specify skills pull from discover
signals automatically when they exist. Write the spec after you have evidence, not before.

---

## When to use this namespace

Use specify when you are ready to commit something to writing. Specify is not the first
step in an investigation -- it is where the investigation becomes a document and where
intent becomes a plan.

- You have discover signals and are ready to write the spec.
- A stakeholder asked for a proposal with options and trade-offs.
- You need to pitch the feature to an exec, a developer audience, or a non-technical audience.
- You have a large option space and want to generate candidates before evaluating.
- You are planning a multi-skill investigation and want to stage it with explicit gates.

Specify also serves as a standalone starting point when you have no prior signals. But specs
written with prior discover context are stronger: the feasibility constraints are grounded,
the requirements are prioritized, and the inertia case has been answered.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `specify-spec` | Author a specification from intent: purpose, requirements, design, constraints, open questions. Pulls discover signals automatically. Self-reviews on completion -- flags open questions and gaps. | When you are ready to write the spec. After discover-feasibility and discover-hypothesis if possible. |
| `specify-proposal` | ADR-style proposal: 3+ options (including do-nothing), each with pros, cons, risk, effort. Recommendation with rationale. Pulls discover-feasibility. | When a decision has multiple viable paths and you need to document the trade-offs. |
| `specify-pitch` | Pitch narrative in exec, developer, and maker versions. Hook, what it does, why it matters, call to action, anti-positioning. Pulls scout-positioning. | Before a stakeholder presentation, launch announcement, or team all-hands. |
| `specify-brainstorm` | 20-40 idea candidates, grouped by category, top 5 flagged. Includes do-nothing as a candidate. AMEND: 3 adjustments to shift the pool. | When you have a large option space and want to generate before evaluating. |
| `specify-commitment` | Sequence skills into a staged program plan with gates. Generates program.yaml for the topic. Final stage is always echo (auto, no skills). | Before a multi-skill investigation. After governing the topic with govern-status. |

---

## Example workflow

You have completed discovery on "payment-reminders" and are ready to write the spec.

**Step 1: Write the spec.**

```
/specify-spec payment-reminders
```

The skill detects prior discover artifacts automatically. It pulls the feasibility constraint
(email throttle at 3/minute/org), the synthesized finding (timing of the first reminder
is the critical variable), and the MoSCoW requirements from discover-feasibility. The spec
is pre-populated with constraints and flags two open questions on completion.

**Step 2: Write a proposal for the notification channel decision.**

One open question was: email or in-app notification? You need to document the trade-offs.

```
/specify-proposal payment-reminders-notification-channel
```

Produces three options: email only (cheapest, throttle risk), in-app only (no throttle
risk, lower reach), dual-channel (most coverage, most complex). Each with pros, cons, risk
rating, effort estimate. Recommendation: in-app only for v1 with email in v2. Includes the
do-nothing option: "keep the spreadsheet workflow." The do-nothing option must be present.

**Step 3: Write a pitch for the exec review.**

```
/specify-pitch payment-reminders --for exec
```

Produces an exec version (ROI framing, outcome-first), a developer version (show the tool),
and a maker version (can I do this?). Anti-positioning section: "This is not a billing
tool." Pulls positioning from discover-competitors automatically.

**Step 4: Plan the full investigation.**

If this is a complex feature requiring 10+ signals across multiple team members:

```
/specify-commitment payment-reminders
```

Generates a staged program with gate conditions: Stage 1 (discovery, gate: feasibility
score >= 60), Stage 2 (design, gate: spec reviewed), Stage 3 (simulation, gate: no P1
gaps), Stage 4 (echo, auto). Writes program.yaml. Assigns ownership by role.

---

## What it produces

All specify artifacts write to `simulations/draft/` and `simulations/program/`:

```
simulations/draft/
  specs/       payment-reminders-spec-2026-03-16.md
  proposals/   payment-reminders-proposal-2026-03-16.md
  pitches/     payment-reminders-pitch-2026-03-16.md
  brainstorm/  payment-reminders-brainstorm-2026-03-16.md

simulations/program/
  plans/       payment-reminders-program-2026-03-16.md
```

Example frontmatter for a spec:

```yaml
---
skill: specify-spec
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Specify after discover, not before.** A spec written with discover-feasibility and
discover-synthesize in context will include constraints and evidence automatically. A spec
written cold invents them. Invented constraints are wrong more often than inferred ones.

**specify-brainstorm is an idea generator, not a decision tool.** Run it to expand the
option space before committing to a direction. Then use validate-design or specify-proposal
to evaluate the pool. The pattern "brainstorm then evaluate" is Signal's chain for design
decisions.

**The do-nothing candidate is required in every brainstorm and proposal.** If your
brainstorm does not include inertia as a candidate, you have pre-filtered the option space.
If your proposal does not include a "do nothing" option, the trade-off analysis is incomplete.
Include it to make the case against it explicit.

**specify-commitment is most valuable for shared investigations.** Solo investigations rarely
need a formal plan -- you can run skills as needed and check govern-status for coverage.
Where specify-commitment earns its place is in team investigations where multiple contributors
need to know what they own, what order matters, and what gates control progress.

---

## What's next

- **[validate](validate.md)** -- review the spec. Grounded Review: pass the specify-spec
  artifact as context.
- **[simulate](simulate.md)** -- simulate how the spec's described system behaves at runtime.
- **[discover](discover.md)** -- if specify raises new questions, run discover skills before
  committing to the design.
- **[govern](govern.md)** -- track investigation coverage across namespaces.
