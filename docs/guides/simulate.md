# simulate — Runtime Behavior and Implementation Verification

## The short version

The simulate namespace finds out whether the system will work the way you described it --
before you build it, and whether it was built correctly -- after you do. Seven skills span
lifecycle simulation, conversation flow, stress testing, and implementation verification.
A spec describes what you are building. Simulate finds whether it will actually work.

---

## When to use this namespace

Use simulate after you have a spec and before or after implementation. The simulate namespace
is developer-facing: it assumes you know what the system should do and asks whether it will
actually do that under real operating conditions.

Before building:
- You have a spec and want to verify the state machine does not have missing transitions.
- You are designing a multi-turn agent conversation and want to walk every dialog path.
- You need to know what happens when three automations fire on the same record change.
- You want to know what happens at 10x expected volume before you build the throttle handling.
- You want to know what happens when the external system is unavailable.

After building:
- You want to verify the request path through service boundaries matches the spec.
- A spec says "check permissions before accessing the record" and you want to verify that
  actually happens at each boundary.
- You are about to deploy a solution and want to trace the deployment sequence.
- A migration is planned and you want to find data loss paths before running it.

Simulate skills do not write code -- they hand-compile behavior from the spec and verify
implementation from the artifact. The gap between what the spec says and what the code does
is found by simulate, not by testing.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `simulate-lifecycle` | Full business process lifecycle: entry conditions, state transitions, decision points, parallel paths, exception flows, terminal states. --focus trigger, --focus dataflow, --focus integration, --focus ratelimit for targeted dimensions. | When your feature involves a multi-step process with state. First simulate skill to run. |
| `simulate-conversation` | Multi-turn agent conversation through the topic graph: intents, responses, topic transitions, fallbacks, session state. Finds dead ends, infinite loops, intent collisions. | For Copilot Studio or any agent conversation design. |
| `simulate-stress` | Degraded conditions: offline, partial failure, eventual consistency. What can the user do, what data is at risk, what is the recovery path. | For any feature with availability requirements or eventual-consistency data. |
| `simulate-request` | Hand-compile a request through service boundaries, APIs, and middleware: entry point, auth, routing, service boundaries, storage access, response assembly, error paths. No boundary skipped. | Whenever you want to know what actually happens when a user does something. |
| `simulate-state` | Hand-compile state transitions: starting state, operation, expected outcome, preconditions, postconditions, invariants. Finds invalid transitions, missing precondition checks, race conditions. | For features with explicit state machines or complex conditional logic. |
| `simulate-contract` | Verify implementation against spec contract. --type component (UI tree), --type deployment (infrastructure compliance), --type migration (schema invariants), --type inspect (skill trace). Default: full 7-gate manifest. | When you want to verify the implementation against a specific spec section. |
| `simulate-permissions` | Trace who can do what through RBAC, security roles, teams, and field-level security. Finds privilege escalation paths, FLS gaps, sharing rule conflicts. | For any feature with access control requirements. |

---

## Example workflow

You are building "payment-reminders." You have a spec. Now simulate it before and after building.

**Before building -- Step 1: Walk the lifecycle.**

```
/simulate-lifecycle payment-reminders
```

Traces the reminder lifecycle: reminder scheduled → notification queued → delivery attempted
→ success or failure → retry logic → escalation after N failures → terminal state. Finds a
missing transition: what happens if the invoice is paid between scheduling and delivery? No
terminal state defined. You add it to the spec.

**Before building -- Step 2: Simulate the throttle scenario.**

```
/simulate-lifecycle payment-reminders --focus ratelimit
```

Your platform throttles email at 3/minute/org. At 50 overdue invoices the queue takes 17
minutes to drain. At 500 it takes 2.8 hours. Backpressure: the queue grows faster than it
drains at 500+. Finding: you need a batching strategy and a queue-position indicator. Neither
is in the spec.

**Before building -- Step 3: Simulate the failure condition.**

```
/simulate-stress payment-reminders
```

Email service unavailable scenario: the queue builds up, but there is no dead-letter handling
in the spec. Invoices due in the next 10 minutes will miss their reminder window. Recovery
path undefined. You add dead-letter handling to the spec.

**After building -- Step 4: Verify the request path.**

```
/simulate-request payment-reminders
```

Traces: user clicks "send reminder" → auth check → record access → invoice data fetched →
notification queued → email service called → response logged. At the notification queue
boundary, no retry logging. The spec says retry attempts should be logged. Finding: P2
deviation.

**After building -- Step 5: Verify permissions.**

```
/simulate-permissions payment-reminders
```

Three roles can access reminder configuration. Finance Admin can see the unsubscribe list --
a list of customers who opted out. The spec did not restrict this field. Finding: FLS gap
on a sensitive field. P1.

**After building -- Step 6: Verify the contract.**

```
/simulate-contract payment-reminders
```

Expected from spec: "API returns 202 Accepted with reminder ID and estimated delivery
timestamp." Actual: 200 OK with no reminder ID. Two deviations: missing field (breaking),
wrong status code (degraded). 7-gate manifest: FAIL.

---

## What it produces

All simulate artifacts write to `simulations/flow/` and `simulations/trace/`:

```
simulations/flow/
  lifecycle/    payment-reminders-lifecycle-2026-03-16.md
  conversation/ payment-reminders-conversation-2026-03-16.md
  resilience/   payment-reminders-resilience-2026-03-16.md

simulations/trace/
  request/      payment-reminders-request-2026-03-16.md
  state/         payment-reminders-state-2026-03-16.md
  contract/     payment-reminders-contract-2026-03-16.md
  permissions/  payment-reminders-permissions-2026-03-16.md
```

Example frontmatter:

```yaml
---
skill: simulate-lifecycle
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**Run simulate-lifecycle first.** It gives you the state machine skeleton. The other simulate
skills build on the lifecycle understanding: throttle (via --focus ratelimit) assumes you
know the nominal path, simulate-stress assumes you know the recovery path, simulate-request
assumes you know which service boundaries matter.

**simulate-lifecycle --focus ratelimit catches the most common unexamined risk.** Most
features are specced and built for nominal volume and break at scale because nobody ran the
throttle simulation. The throttle numbers are easy to calculate from platform documentation
-- simulate-lifecycle does that calculation before you discover it in production.

**simulate-contract is the spec compliance test.** The expected output is the contract: any
deviation is a finding. Write the expected output before checking the actual. This is the
three-directory pattern (10-input / 20-expected / 30-actual) applied to Signal skill outputs.

**simulate-permissions finds what code review misses.** Security reviewers check that
permission checks exist. simulate-permissions walks every role through every operation and
finds the gaps: operations nobody checked, fields visible when they should not be. The P1
findings in permissions traces are usually invisible to code review.

**Hand-compile before building for complex features.** Running simulate-request on a spec
before implementation -- not after -- turns simulate into a design verification tool. The
act of hand-compiling every step forces you to discover under-specified boundaries before
they are built in.

---

## What's next

- **[validate](validate.md)** -- if simulate surfaces spec gaps, revise the spec and
  re-run validate-design.
- **[specify](specify.md)** -- simulate findings frequently require spec updates.
- **[govern](govern.md)** -- track simulate coverage and synthesize findings into decisions.
