# listen — Adoption and Post-Ship Prediction

## The short version

The listen namespace predicts what happens after you ship: the feedback, the support tickets,
and the adoption curve. Three skills. Run them before you ship and you know what you are
about to hear. Run them after and you know what to fix first.

---

## When to use this namespace

Use listen when you want to understand how users will actually respond to the feature -- not
how you hope they will. The listen namespace simulates the post-ship signal before the ship.

- You are about to ship a feature and want to predict the first support tickets.
- You want to know which user persona will resist adoption and why.
- A feature has been live for a month and adoption is flat. You want to understand the adoption
  curve dynamics before making a change.
- A spec is written and you want to know whether the design will generate negative NPS.

The listen namespace is the closest Signal comes to simulated user testing. It does not replace
real user research -- nothing does. But it catches the predictable adoption blockers before
they are discovered the expensive way.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `listen-feedback` | All 12 customer personas read the spec and produce feedback cards with severity (blocking/major/minor/cosmetic) and NPS prediction. Aggregate NPS threshold: 7.0. Below 7.0 = spec needs revision. | Before shipping. Finds which personas have blocking objections. |
| `listen-support` | Predicts the top support tickets filed in the first 90 days: title, category (how-to/bug/feature/config/integration), persona, predicted volume, severity, sample ticket in the persona's voice. Gap analysis: doc gaps, design gaps, operational gaps. | Before shipping. Tells your support team what is coming. |
| `listen-adoption` | Simulates the adoption curve across Rogers archetypes (innovator/early-adopter/early-majority/late-majority/laggard). Month-by-month simulation. Chasm analysis. Champion network, churn risks, intervention recommendations. | Before shipping. Finds the chasm before you fall in it. |

---

## Example workflow

"payment-reminders" is approaching ship. You want to predict the post-ship signal.

**Step 1: Simulate customer feedback.**

```
/listen-feedback payment-reminders
```

All 12 personas read the spec. C-03 (Enterprise Admin) scores NPS at 4 -- blocking. Finding:
no way to set org-wide reminder policies. C-07 (Finance Controller) scores NPS at 3 -- blocking.
Finding: no audit log of sent reminders. Aggregate NPS: 6.2. Below 7.0 threshold. The spec
needs two additions before ship.

**Step 2: Predict the support queue.**

```
/listen-support payment-reminders
```

Top predicted tickets:
- "How do I turn off reminders for a specific customer?" (HIGH volume, how-to, no docs exist)
- "Reminder sent to wrong email" (MEDIUM volume, bug, configuration gap in the spec)
- "Can't see which reminders were sent" (MEDIUM volume, how-to, no audit log -- same gap as listen-feedback found)

Doc gaps: no how-to for configuring per-customer opt-out. Design gap: no audit log. The
audit log issue is now confirmed by two independent listen signals.

**Step 3: Simulate the adoption curve.**

```
/listen-adoption payment-reminders
```

Month 1: Innovators (Finance team pioneers) try it. They configure it for a small vendor set.
Month 2: Early adopters within Finance spread via word-of-mouth. The chasm appears at
Month 3: early majority requires seeing a peer use it successfully. Champion identification:
the Finance team lead is the champion. Churn risk: if the first 90-day support experience is
poor (see: the predicted ticket queue), early adopters abandon and the chasm widens.

---

## What it produces

All listen artifacts write to `simulations/listen/`:

```
simulations/listen/
  feedback/   payment-reminders-feedback-2026-03-16.md
  support/    payment-reminders-support-2026-03-16.md
  adoption/   payment-reminders-adoption-2026-03-16.md
```

Example frontmatter:

```yaml
---
skill: listen-adoption
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Aggregate NPS below 7.0 is a stop signal.** listen-feedback uses 7.0 as the revision
threshold. A weighted aggregate below 7.0 means your primary personas have blocking objections.
Address the blocking findings before shipping, not after.

**listen-support predictions cluster around the same gaps that review and flow found.**
The support tickets that listen-support predicts are usually traceable to: gaps in the spec
that review-design flagged, edge cases that flow-lifecycle found, and UX friction that
review-users identified. If those signals are consistent, the gap is real. If listen-support
finds something that review did not, that is worth noting.

**The chasm is predictable.** listen-adoption's chasm analysis follows Rogers' diffusion
curve with persona-specific crossing conditions. The chasm always falls between early adopters
and early majority. The crossing condition is almost always: "I need to see a peer succeed
before I try." Signal this to your launch plan: identify the champion, make their success
visible.

---

## What's next

- **[topic](topic.md)** -- use topic-story to synthesize all signals including listen findings.
- **[prove](prove.md)** -- if listen-adoption contradicts your adoption hypothesis, falsify it.
- **[scout](scout.md)** -- listen findings sometimes reveal that the inertia case is stronger than scout-competitors assessed.
- **[crew](crew.md)** -- for features with org-wide adoption goals, run crew-review after listen-adoption.
