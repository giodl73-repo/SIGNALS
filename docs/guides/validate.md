# validate — Design Review and Adoption Prediction

## The short version

The validate namespace routes an artifact through structured expert perspectives and
predicts what happens after you ship. Seven skills: four discipline-and-persona reviews,
three post-ship prediction skills. Review skills require something real to review. Adoption
skills require a realistic spec or design. Pass the artifact as context, not a description.

---

## When to use this namespace

Use validate after you have a written artifact worth reviewing and before you commit to
building or shipping it. The validate namespace is the closest Signal comes to simulated
user testing -- it does not replace real user research, but it catches the predictable
problems before they are discovered the expensive way.

- You have a draft spec and want multi-discipline critique before sharing with the team.
- You want to know whether real users would find the design confusing before the design meeting.
- You want to know how customers will actually react, not how you hope they will.
- You are about to ship and want to predict the first support tickets and adoption curve.
- A feature has been live a month and adoption is flat. You want to understand why.

Validate is most powerful in a chain: specify-spec produces the artifact, validate-design
consumes it. The Grounded Review achievement requires this chain -- spec first, then review
with the spec artifact available as context.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `validate-design` | 6-discipline review (architect, code-quality, documentation, testing, process, implementation) plus 3-5 auto-selected domain experts. P1/P2/P3 severity. Consensus analysis (2+ reviewers flag same issue). AMEND: address findings one by one. | After specify-spec. The standard pre-commit design review. |
| `validate-code` | Same 6-discipline structure applied to code files, PRs, or diffs. File:line annotations. Pass/fail per discipline. Can check spec compliance. | After implementation. Before merge on high-risk changes. |
| `validate-users` | 5 persona advocates walk the design in first person, flag confusion/friction/fear/jargon. Aggregate usability score. Cross-persona synthesis: universal friction, role-specific friction, persona conflicts. | When the design has UX surface area. Before usability testing. |
| `validate-customers` | 12 customer personas (C-01 through C-12) evaluate usefulness, clarity, and would-adopt (all 1-5). Primary audience weighted 3x. Adoption blocker identification. Positioning leak detection. | Before shipping. Finds which personas would not adopt and why. |
| `validate-feedback` | All 12 customer personas read the spec through their lens. Per-persona feedback cards with severity and NPS prediction (1-10). Aggregate NPS threshold: 7.0. Below 7.0 = spec needs revision. | Before shipping. The pre-ship NPS signal. |
| `validate-support` | Predicts top support tickets filed in the first 90 days: title, category, persona, predicted volume, severity, sample ticket in the persona's voice. Gap analysis: doc gaps, design gaps, operational gaps. | Before shipping. Tells your support team what is coming. |
| `validate-adoption` | Simulates the adoption curve across Rogers archetypes (innovator/early-adopter/early-majority/late-majority/laggard). Month-by-month simulation. Chasm analysis. Champion network, churn risks, interventions. | Before shipping. Finds the chasm before you fall in it. |

---

## Example workflow

You have a draft spec for "payment-reminders" and want to review it before the design meeting,
then predict the post-ship signal before shipping.

**Step 1: Run the design review.**

```
/validate-design payment-reminders
```

Six disciplines review the spec. The architect flags the email throttle constraint as
under-designed (P1). The documentation reviewer flags "unsubscribe" has no spec coverage
(P2). The process reviewer flags a missing error-recovery section (P2). Three findings from
two or more reviewers are marked as consensus.

**Step 2: Check whether the design works for real users.**

```
/validate-users payment-reminders
```

Five personas walk the spec. The Operator persona scores 2/5: "I do not see how to
bulk-dismiss reminders." Persona conflict surfaced: Maker wants individual control, Operator
wants batch control. You add a bulk-dismiss requirement.

**Step 3: Before shipping, simulate customer feedback.**

```
/validate-feedback payment-reminders
```

C-03 (Enterprise Admin) scores NPS at 4 -- blocking. Finding: no org-wide reminder policies.
C-07 (Finance Controller) scores NPS at 3 -- blocking. Finding: no audit log of sent reminders.
Aggregate NPS: 6.2. Below 7.0 threshold. The spec needs two additions.

**Step 4: Predict the support queue.**

```
/validate-support payment-reminders
```

Top predicted tickets: "How do I turn off reminders for a specific customer?" (HIGH volume,
no docs exist). "Can't see which reminders were sent" (MEDIUM volume, same audit log gap).
The audit log gap is now confirmed by two independent validate signals.

**Step 5: Simulate the adoption curve.**

```
/validate-adoption payment-reminders
```

Month 1: Innovators (Finance team pioneers) try it. Month 3: chasm appears -- early majority
requires seeing a peer succeed. Champion identified: Finance team lead. Churn risk: if the
first 90-day support experience is poor, early adopters abandon and the chasm widens.

---

## What it produces

All validate artifacts write to `simulations/review/` and `simulations/listen/`:

```
simulations/review/
  design/     payment-reminders-design-2026-03-16.md
  code/       payment-reminders-code-2026-03-16.md
  users/      payment-reminders-users-2026-03-16.md
  customers/  payment-reminders-customers-2026-03-16.md

simulations/listen/
  feedback/   payment-reminders-feedback-2026-03-16.md
  support/    payment-reminders-support-2026-03-16.md
  adoption/   payment-reminders-adoption-2026-03-16.md
```

Example frontmatter:

```yaml
---
skill: validate-design
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Pass the artifact as context, not the topic name alone.** validate-design is most effective
when it reads the actual spec artifact. Running it with only a topic name produces a review
of what you described, not a review of what you wrote.

**AMEND is how you iterate, not re-run.** After validate-design produces findings, use AMEND
to address them one by one and re-run specific reviewers on changed sections only. This is
faster than a full re-run and produces a finding-resolution log.

**Aggregate NPS below 7.0 is a stop signal.** validate-feedback uses 7.0 as the revision
threshold. A weighted aggregate below 7.0 means your primary personas have blocking objections.
Address the blocking findings before shipping.

**validate-support predictions cluster around the same gaps that other skills found.** If
validate-design flagged a spec gap, validate-feedback found an NPS blocker on the same
feature, and validate-support predicts a high-volume ticket on the same topic -- that
convergence is a signal to address it before ship, not after.

**The chasm is predictable.** validate-adoption's chasm analysis follows Rogers' diffusion
curve with persona-specific crossing conditions. The crossing condition is almost always:
"I need to see a peer succeed before I try." Signal this to your launch plan: identify the
champion, make their success visible.

---

## What's next

- **[simulate](simulate.md)** -- simulate runtime behavior of what validate approved.
- **[discover](discover.md)** -- if validate surfaces a structural assumption, test it
  before building.
- **[govern](govern.md)** -- track investigation coverage and synthesize signals into decisions.
- **[specify](specify.md)** -- validate findings frequently require spec updates.
