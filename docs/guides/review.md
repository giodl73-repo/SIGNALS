# review — Design, Code, and Persona Review

## The short version

The review namespace routes an artifact through structured expert perspectives: six standard
disciplines, auto-selected domain experts, and 12 customer personas. Review skills require
something real to review. Pass the artifact as context, not a description of it.

---

## When to use this namespace

Use review after you have a written artifact worth reviewing. The review namespace is not
a replacement for human review -- it is a structured pre-review that catches the issues
a single-author read misses.

- You have a draft spec and want multi-discipline critique before sharing with the team.
- You have code you want reviewed against a spec for compliance.
- You want to know whether real users would find the design confusing before the design review meeting.
- You want to know how customers will actually react, not how you hope they will.

Review is most powerful in a chain: draft-spec produces the artifact, review-design consumes
it. The Grounded Review achievement is earned by running this chain correctly -- spec first,
then review with the spec artifact available as context.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `review-design` | 6-discipline review (architect, code-quality, documentation, testing, process, implementation) plus 3-5 auto-selected domain experts. P1/P2/P3 severity. Consensus analysis. | After draft-spec. The standard pre-commit design review. |
| `review-code` | Same 6-discipline structure applied to code files, PRs, or diffs. File:line annotations. Pass/fail per discipline. Can check spec compliance. | After implementation. Before merge on high-risk changes. |
| `review-users` | 5 persona advocates walk the design in first person, flag confusion/friction/fear/jargon. Aggregate usability score. | When the design has UX surface area. Before usability testing. |
| `review-customers` | 12 customer personas (C-01 through C-12) evaluate usefulness, clarity, and would-adopt (1-5). Weighted aggregate score. Adoption blocker identification. | Before shipping. Finds out which personas would not adopt and why. |

---

## Example workflow

You have a draft spec for "payment-reminders" and want review before the design meeting.

**Step 1: Run the design review.**

```
/review-design payment-reminders
```

The skill loads `payment-reminders-spec-2026-03-16.md` from context. Six disciplines
review it. The architect flags the email throttle constraint as under-designed (P1). The
documentation reviewer flags that the "unsubscribe" flow has no spec coverage (P2). The
process reviewer flags a missing error-recovery section (P2). Three findings from two or
more reviewers are marked as consensus.

**Step 2: Check whether the design works for real users.**

```
/review-users payment-reminders
```

Five personas walk the spec. The Operator persona scores 2/5 and flags: "I do not see
how to bulk-dismiss reminders." This persona conflict is surfaced in the synthesis:
what the Maker persona wants (individual control) conflicts with what the Operator
wants (batch control). You add a bulk-dismiss requirement.

**Step 3: Before shipping, check customer personas.**

```
/review-customers payment-reminders
```

C-03 (Enterprise Admin) scores would-adopt at 2/5. Finding: no enterprise policy controls.
This is an adoption blocker. You add it to the v1.1 backlog and note it in the release decision.

---

## What it produces

All review artifacts write to `simulations/review/`:

```
simulations/review/
  design/     payment-reminders-design-2026-03-16.md
  code/       payment-reminders-code-2026-03-16.md
  users/      payment-reminders-users-2026-03-16.md
  customers/  payment-reminders-customers-2026-03-16.md
```

Example frontmatter:

```yaml
---
skill: review-design
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Pass the artifact as context, not the topic name alone.** review-design is most effective
when it reads the actual spec artifact. Running it with only a topic name produces a review
of what you described, not a review of what you wrote. The Grounded Review pattern: run
draft-spec, then pass its output as context to review-design.

**AMEND is how you iterate, not re-run.** After review-design produces findings, use AMEND
to address them one by one and re-run specific reviewers on changed sections only. This is
faster than a full re-run and produces a finding-resolution log.

**review-customers weighted aggregate is the adoption signal.** Primary personas (your target
audience) are weighted 3x. Non-target personas are weighted 1x. A weighted aggregate below
4.0 means your primary audience has significant reservations. Below 3.0 means the feature
has an adoption problem before it ships.

---

## What's next

- **[flow](flow.md)** -- simulate runtime behavior of what review approved.
- **[listen](listen.md)** -- predict post-ship feedback and support burden.
- **[trace](trace.md)** -- verify the implementation matches what review signed off on.
- **[prove](prove.md)** -- if review surfaces a structural assumption, test it before building.
