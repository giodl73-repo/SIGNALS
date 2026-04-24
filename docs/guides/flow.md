# flow — Runtime Behavior Simulation

## The short version

The flow namespace simulates how a system actually behaves at runtime -- before it is built.
Seven skills cover lifecycle, conversation, triggers, data movement, integrations, throttling,
and failure conditions. A spec describes what you are building. Flow finds out whether it
will work the way you described it.

---

## When to use this namespace

Use flow after you have a spec and before you build the implementation. The flow namespace
is developer-facing: it assumes you know what the system should do and asks whether it will
actually do that under real operating conditions.

- You have a spec and want to verify the state machine does not have missing transitions.
- You are designing a multi-turn agent conversation and want to walk every dialog path.
- You need to know what happens when three automations fire on the same record change.
- Your system makes cross-platform API calls and you want to trace authentication and rate limits.
- You want to know what happens at 10x expected volume before you build the throttle handling.
- You want to know what happens when the external system is unavailable.

Flow skills do not write code -- they simulate behavior from the spec. The simulation finds
the gaps before the implementation encodes them.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `flow-lifecycle` | Walks every step of a multi-step business process: entry conditions, state transitions, decision points, parallel paths, exception flows, terminal states. | When your feature involves a multi-step process with state. |
| `flow-conversation` | Simulates a multi-turn agent conversation through the topic graph: intents, responses, topic transitions, fallbacks, session state. | For Copilot Studio or any agent conversation design. |
| `flow-trigger` | Traces what automations fire for each record change, in what order, with what side effects. Identifies trigger storms and missing triggers. | For any feature involving Power Automate or event-driven automation. |
| `flow-dataflow` | Traces data through ETL, sync, CDX, or dual-write patterns: source, transformations, destination, latency, error handling at each boundary. | For any feature involving data movement or synchronization. |
| `flow-integration` | Traces cross-system calls through connectors and APIs: request format, auth, rate limits, response handling, retry logic, error propagation. | For any feature making external API calls or using platform connectors. |
| `flow-throttle` | Simulates throughput at scale: where bottlenecks occur, which rate limits are hit first, how backpressure propagates, UX at each throttle tier. | Before building any high-volume path. Catches unprotected burst paths. |
| `flow-resilience` | Simulates degraded conditions: offline, partial failure, eventual consistency. What can the user do, what data is at risk, what is the recovery path. | For any feature with availability requirements or eventual-consistency data. |

---

## Example workflow

You are building "payment-reminders" -- automated email reminders. You have a spec. Now you
want to simulate the system before building it.

**Step 1: Walk the lifecycle.**

```
/flow-lifecycle payment-reminders
```

Traces the reminder lifecycle: reminder scheduled → notification queued → delivery attempted →
success or failure → retry logic → escalation after N failures → terminal state (delivered /
abandoned / unsubscribed). Finds a missing transition: what happens if the invoice is paid
between scheduling and delivery? No terminal state defined. You add it to the spec.

**Step 2: Simulate the throttle scenario.**

```
/flow-throttle payment-reminders
```

Your platform throttles email at 3/minute/org. At 50 overdue invoices, the queue takes
17 minutes to drain. At 500, it takes 2.8 hours. Backpressure: the queue grows faster than
it drains at 500+. Finding: you need a batching strategy and a user-visible queue position
indicator. Neither is in the spec.

**Step 3: Simulate the failure condition.**

```
/flow-resilience payment-reminders
```

Email service unavailable scenario: the queue builds up, but there is no dead-letter
handling in the spec. Invoices due in the next 10 minutes will miss their reminder window.
Recovery path is undefined. You add dead-letter handling to the spec.

---

## What it produces

All flow artifacts write to `simulations/flow/`:

```
simulations/flow/
  lifecycle/    payment-reminders-lifecycle-2026-03-16.md
  conversation/ payment-reminders-conversation-2026-03-16.md
  trigger/      payment-reminders-trigger-2026-03-16.md
  dataflow/     payment-reminders-dataflow-2026-03-16.md
  integration/  payment-reminders-integration-2026-03-16.md
  throttle/     payment-reminders-throttle-2026-03-16.md
  resilience/   payment-reminders-resilience-2026-03-16.md
```

Example frontmatter:

```yaml
---
skill: flow-lifecycle
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Run flow-lifecycle first.** It gives you the state machine skeleton. The other flow skills
build on the lifecycle understanding: throttle assumes you know the nominal path, resilience
assumes you know the recovery path, trigger assumes you know which state transitions matter.

**flow-throttle catches the most common unexamined risk.** Most features are specced and built
for nominal volume and break at scale because nobody ran the throttle simulation. The throttle
numbers are easy to calculate from your platform documentation -- and flow-throttle does that
calculation for you before you discover it in production.

**Simulation-Before-Build is a chain achievement for a reason.** flow-lifecycle before
any trace skill on the same topic earns Simulation-Before-Build. The reason: trace finds
what was implemented. Flow found what should have been. Run flow first so trace has a target.

---

## What's next

- **[trace](trace.md)** -- after building, verify the implementation matches the flow simulation.
- **[review](review.md)** -- if flow surfaces spec gaps, revise the spec and re-run review.
- **[listen](listen.md)** -- flow-resilience findings often predict support tickets. Check listen-support.
- **[draft](draft.md)** -- flow findings frequently require spec updates. Go back and amend.
