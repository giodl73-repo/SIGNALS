# trace — Implementation Verification

## The short version

The trace namespace verifies that the implementation matches the spec by hand-compiling
execution paths. Seven skills cover requests, state transitions, contracts, UI components,
deployments, migrations, and permissions. Tracing finds what testing misses: the gap between
what the spec says and what the code does.

---

## When to use this namespace

Use trace after you have an implementation and want to verify it matches the design intent.
The trace namespace is developer-facing and post-commitment: it assumes the feature exists
and asks whether it was built correctly.

- You shipped a feature and want to verify the request path matches the spec.
- You are reviewing an implementation before sign-off and want more than a code read.
- A spec says "check permissions before accessing the record" and you want to verify that
  actually happens at each boundary.
- You are about to deploy a solution and want to trace the deployment sequence.
- A migration is planned and you want to find data loss paths before running it.

Trace is also pre-commitment useful as a design verification tool: hand-compiling a request
before building it finds design flaws before they are encoded in code. A skill that cannot
be hand-compiled cannot be implemented correctly.

---

## Skills

| Skill | What it does | When to run it |
|-------|-------------|----------------|
| `trace-request` | Hand-compiles a request step by step: entry point, auth, routing, each service boundary, storage access, response assembly, error paths. No boundary skipped. | Whenever you want to know what actually happens when a user does something. |
| `trace-state` | Hand-compiles state transitions: starting state, operation, expected outcome, preconditions, postconditions, invariants. | For features with explicit state machines or complex conditional logic. |
| `trace-contract` | Compares expected output (from spec) vs. actual output. Diffs expected vs. actual, severity-classified per mismatch. | When you want to verify the implementation against a specific spec section. |
| `trace-component` | Traces a user action through the UI component tree: event, component traversal, state updates, re-renders, side effects, final UI state. | For any feature with frontend surface area. |
| `trace-deployment` | Traces the deployment sequence: pre-deploy checks, deployment order, post-deploy validation, rollback path. | Before deploying to production or staging. |
| `trace-migration` | Traces before/after a schema change: what data exists before, what migration does to it, state after. Finds data loss paths. | Before any schema migration or version upgrade. |
| `trace-permissions` | Traces who can do what through RBAC, security roles, teams, and field-level security. Finds privilege escalation paths and FLS gaps. | For any feature with access control requirements. |

---

## Example workflow

"payment-reminders" has been built. You want to verify the implementation before the
sign-off review.

**Step 1: Trace the request path.**

```
/trace-request payment-reminders
```

Traces: user clicks "send reminder" → auth check → record access → invoice data fetched →
notification queued → email service called → response logged. At the notification queue
boundary, the trace finds no retry logging. The spec says retry attempts should be logged.
Finding: P2 deviation from spec.

**Step 2: Verify permissions.**

```
/trace-permissions payment-reminders
```

Three roles can access reminder configuration: Finance Admin, Billing Manager, System Admin.
The trace finds that Finance Admin can see the unsubscribe list -- a list of customers who
opted out. The spec did not restrict this field. Finding: field-level security gap on a
sensitive field. P1.

**Step 3: Verify the contract.**

```
/trace-contract payment-reminders
```

Writes the expected output from the spec: "API returns 202 Accepted with a reminder ID and
estimated delivery timestamp." Runs the actual API call. Actual output: 200 OK with no
reminder ID. Mismatch: missing field (breaking), wrong status code (degraded). Two deviations
from the contract.

---

## What it produces

All trace artifacts write to `simulations/trace/`:

```
simulations/trace/
  request/     payment-reminders-request-2026-03-16.md
  state/       payment-reminders-state-2026-03-16.md
  contract/    payment-reminders-contract-2026-03-16.md
  component/   payment-reminders-component-2026-03-16.md
  deployment/  payment-reminders-deployment-2026-03-16.md
  migration/   payment-reminders-migration-2026-03-16.md
  permissions/ payment-reminders-permissions-2026-03-16.md
```

Example frontmatter:

```yaml
---
skill: trace-contract
topic: payment-reminders
date: 2026-03-16
skill_version: 0.1.0
---
```

---

## Common patterns

**trace-contract is the spec compliance test.** The expected output is the contract: any
deviation is a finding. This discipline -- write the expected output before checking the
actual -- is the three-directory pattern (10-input / 20-expected / 30-actual) applied to
Signal skill outputs.

**trace-permissions finds what code review misses.** Security reviewers read the code and
check that permission checks exist. trace-permissions walks every role through every operation
and finds the gaps: operations that exist but nobody checked, fields that are visible when
they should not be. The P1 findings in permissions traces are usually invisible to code review.

**Hand-compile before building for complex features.** Running trace-request on a spec before
implementation -- not after -- turns trace into a design verification tool. The act of
hand-compiling every step forces you to discover under-specified boundaries before they are
built in. Use trace-skill for this: the hand-compilation tool for Signal's own skill design.

---

## What's next

- **[flow](flow.md)** -- if trace finds design-level gaps, flow can verify the corrected spec.
- **[review](review.md)** -- trace findings often surface spec gaps. Amend the spec and re-run review.
- **[topic](topic.md)** -- trace-complete topics should be updated in topic-status and documented in topic-story.
- **[crew](crew.md)** -- for P1 findings, run crew-review to get org-level perspective on the severity.
