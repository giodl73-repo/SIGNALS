# draft — Specification and Proposal Authoring

## The short version

The draft namespace turns intent into written artifacts. Four skills cover specs, proposals,
pitches, and brainstorms. Draft skills pull from scout signals automatically when they exist.
Write the spec after you have evidence, not before.

---

## When to use this namespace

Use draft when you are ready to commit something to writing. The draft namespace is not the
first step in an investigation -- it is where the investigation becomes a document.

- You have scout signals and are ready to write the spec.
- A stakeholder asked for a proposal with options and trade-offs.
- You need to pitch the feature to an exec, a developer audience, or a non-technical audience.
- You have a large option space and want to generate candidates before evaluating.

The draft namespace also serves as a standalone starting point when you have no prior signals.
The skills are self-contained. But specs written with prior scout context are stronger than
specs written cold: the feasibility constraints are grounded, the requirements are prioritized,
and the inertia case has been answered.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `draft-spec` | Spec with guided section structure: purpose, requirements, design, constraints, open questions. Pulls scout context automatically. Self-reviews on completion. | When you are ready to write the spec. After scout-requirements and scout-feasibility if possible. |
| `draft-proposal` | ADR-style proposal: 3+ options (including do-nothing), each with pros, cons, risk, effort. Recommendation with rationale. Pulls scout-feasibility. | When a decision has multiple viable paths and you need to document the trade-offs. |
| `draft-pitch` | Pitch narrative in exec, developer, and maker versions. Hook, what it does, why it matters, call to action, anti-positioning. Pulls scout-positioning. | Before a stakeholder presentation, launch announcement, or team all-hands. |
| `draft-brainstorm` | 20-40 idea candidates, grouped by category, top 5 flagged. Includes do-nothing as a candidate. AMEND: 3 adjustments to shift the pool. | When you have a large option space and want to generate before evaluating. |

---

## Example workflow

You have completed scout on "payment-reminders" and are ready to write the spec.

**Step 1: Run the spec.**

```
/draft-spec payment-reminders
```

The skill detects your prior scout artifacts automatically. It pulls requirements from
`payment-reminders-requirements-2026-03-16.md` and feasibility constraints from
`payment-reminders-feasibility-2026-03-16.md`. The spec is pre-populated with the
MoSCoW requirements and flags the email throttle constraint in the design section.
On completion, it self-reviews and flags two open questions.

**Step 2: Write a proposal for the notification channel decision.**

One open question was: email or in-app notification? You need a proposal.

```
/draft-proposal payment-reminders-notification-channel
```

Produces three options: email only (cheapest, throttle risk), in-app only (no throttle
risk, lower reach), dual-channel (most coverage, most complex). Each with pros, cons,
risk rating, effort estimate. Recommendation: in-app only for v1 with email in v2.

**Step 3: Write a pitch for the exec review.**

```
/draft-pitch payment-reminders --for exec
```

Pulls positioning from `payment-reminders-positioning-2026-03-16.md`. Produces an
exec version (ROI framing, outcome-first), a developer version (show the tool), and a
maker version (can I do this?). Anti-positioning section: "This is not a billing tool."

---

## What it produces

All draft artifacts write to `simulations/draft/`:

```
simulations/draft/
  specs/       payment-reminders-spec-2026-03-16.md
  proposals/   payment-reminders-proposal-2026-03-16.md
  pitches/     payment-reminders-pitch-2026-03-16.md
  brainstorm/  payment-reminders-brainstorm-2026-03-16.md
```

Example frontmatter for a spec:

```yaml
---
skill: draft-spec
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Draft after scout, not before.** A spec written with scout-feasibility and scout-requirements
in context will include the constraints and requirements automatically. A spec written cold
will invent them. Invented constraints are wrong more often than inferred ones.

**draft-brainstorm is an idea generator, not a decision tool.** Run it to expand the option
space before committing to a direction. Then use review-design or a proposal to evaluate the
pool. The pattern "brainstorm then evaluate" is the Signal chain for design decisions.

**The do-nothing candidate is required in every brainstorm.** If your brainstorm does not
include inertia as a candidate, you have pre-filtered the option space. The point of including
it is to make the case against it explicit, not to recommend it.

---

## What's next

- **[review](review.md)** -- review the spec. Grounded Review: pass the draft artifact as context.
- **[flow](flow.md)** -- simulate how the spec's described system actually behaves at runtime.
- **[trace](trace.md)** -- verify the implementation against the spec after building.
- **[prove](prove.md)** -- test the core assumption before committing. Run before draft-spec if possible.
