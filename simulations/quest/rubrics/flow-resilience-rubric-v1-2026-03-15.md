---
skill: quest-rubric
skill_target: flow-resilience
date: 2026-03-15
version: 1
---

# Rubric — flow-resilience

Evaluate outputs from the `flow-resilience` skill, which simulates degraded conditions
(offline, partial failure, eventual consistency) and produces per-scenario analysis with
four mandatory fields: system state, user capability, data at risk, and recovery path.
Stock role: Commerce / distributed systems domain expert.

---

## Essential Criteria (all must pass — 60% of score)

### C-01 — Failure Scenario Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three degradation classes defined by the skill: (1) offline /
  network-partition conditions, (2) partial service failure (one or more dependencies down,
  system partially operational), and (3) eventual-consistency lag or split-brain states. Each
  class must be represented by at least one named scenario.
- **Pass condition**: At least one scenario exists per degradation class, each clearly labeled
  or attributable to its class. An output covering only one or two classes fails.

### C-02 — Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: format
- **Text**: Every failure scenario in the output includes all four mandatory analysis fields:
  (1) system state — what degraded condition the system is in; (2) user capability — what the
  user can still do; (3) data at risk — what data may be lost, stale, or inconsistent; (4)
  recovery path — how the system returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with
  non-trivial content (not placeholder, "N/A", or a single word). A scenario missing any
  field fails this criterion entirely.

### C-03 — Gap Identification (Three Types)
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct named findings.
  These are the three explicit output targets the skill defines.
- **Pass condition**: All three finding types appear, each labeled and actionable — not merely
  implied or bundled. Generic statements like "offline support may be limited" without
  specificity fail.

### C-04 — Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals. CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly wherever referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated
  error codes, invented protocols, or impossible consistency guarantees (e.g., strong
  consistency with no latency cost across a partition) fail this criterion.

### C-05 — Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows — checkout, inventory reservation, payment
  processing, order fulfillment, cart state — rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation
  by name. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality — 30% of score)

### C-06 — Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded /
  impaired / down) and a blast radius describing what fraction or segment of users is
  affected. These labels enable triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a
  blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects
  <1% under split-brain"). Scenarios with severity but no blast radius, or vice versa, do
  not satisfy this criterion.

### C-07 — Recovery Path Specificity with Actor Labels
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors — not just outcomes.
  Each step names who or what initiates the action: client, server, operator, or user.
  Example: "Client retries with exponential back-off up to 5 attempts; on exhaustion,
  server surfaces a manual reconcile UI to the user."
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that
  describe only the end state ("system recovers", "data is synchronized") without
  mechanism fail.

### C-08 — Conflict Resolution Strategy for Eventual Consistency
- **Weight**: recommended
- **Category**: coverage
- **Text**: For eventual-consistency scenarios, the output specifies what conflict resolution
  strategy is assumed (last-write-wins, merge, manual reconcile, reject-stale) and flags
  whether that strategy is adequate for the data type involved (e.g., LWW is inadequate for
  inventory counts).
- **Pass condition**: At least one eventual-consistency scenario names a conflict-resolution
  strategy and includes a brief adequacy judgment. Scenarios that describe lag or divergence
  without naming a resolution strategy fail.

---

## Aspirational Criteria (raise the bar — 10% of score)

### C-09 — Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that
  could be scheduled in a test harness. Each scenario specifies: (1) what to inject (network
  partition, latency spike, service kill, packet loss), (2) expected observable behavior, and
  (3) a binary pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements.
  Vague suggestions to "test resilience" or "add chaos testing" without specifics fail.

### C-10 — Observability Hooks Tied to Named Gaps
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals — metrics, logs, traces, or
  alerts — that would surface each identified gap in production. Each recommendation is tied
  to a specific named gap or scenario from the analysis with a rationale.
- **Pass condition**: At least two observability recommendations are present, each linked to a
  named gap or scenario with a rationale for why that signal would detect the failure early.
  Generic "add monitoring" suggestions without specifics fail.

---

## Scoring Formula

| Tier | Weight | Criteria |
|------|--------|----------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 |
| Recommended | 30% | C-06, C-07, C-08 |
| Aspirational | 10% | C-09, C-10 |

```
composite = (essential_pass/5 * 60)
          + (recommended_pass/3 * 30)
          + (aspirational_pass/2 * 10)
```

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

---

## Failure Fast-Paths

The following conditions automatically fail scoring regardless of composite score:

- Output contains no explicit failure scenarios (pure prose advice with no scenario structure)
- Output is domain-agnostic (no commerce or distributed systems grounding anywhere)
- Recovery paths are all identical or all trivially "restart the service" / "wait for recovery"
- Fewer than three degradation classes are represented (offline, partial failure, eventual consistency)
