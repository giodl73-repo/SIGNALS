Rubric written to `simulations/quest/rubrics/flow-resilience-rubric-2026-03-14.md`.

**Structure:**

- **5 essential** (60%): scenario coverage (3 classes), four-field structure per scenario, gap identification (3 types), distributed systems accuracy, commerce domain grounding
- **3 recommended** (30%): severity + blast-radius classification, recovery path specificity with actor labels, conflict resolution strategy for eventual consistency
- **2 aspirational** (10%): chaos engineering test cases (injectable, observable, pass/fail), observability hooks tied to named gaps

**Design decisions:**
- C-02 is the spine — the four-field structure (state / capability / data-at-risk / recovery) is literally what the skill spec defines, so it's essential and per-scenario, not just overall
- C-03 catches the skill's three named output targets (offline gaps, consistency violations, missing recovery flows) — all three must appear, not just one
- Fast-paths catch the most common failure modes: pure prose output, domain-agnostic analysis, and trivial recovery paths that add no signal
apability — what the user can still do; (3) data
  at risk — what data may be lost, stale, or inconsistent; (4) recovery path — how the system
  returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with
  non-trivial content (not placeholder or "N/A"). A scenario missing any field fails this
  criterion.

### C-03 — Gap Identification
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct findings.
- **Pass condition**: All three finding types appear, each labeled and actionable (not just
  implied). Generic statements like "offline support may be limited" without specificity fail.

### C-04 — Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals: CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly where referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated
  error codes, invented protocols, or impossible consistency guarantees fail this criterion.

### C-05 — Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows (e.g., checkout, inventory reservation, payment
  processing, order fulfillment) rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation.
  Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality — 30% of score)

### C-06 — Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded / impaired /
  down) and a blast radius (what percentage or which segment of users is affected). This helps
  triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a blast-radius
  estimate or qualifier (e.g., "affects all users in offline mode", "affects <1% under
  split-brain").

### C-07 — Recovery Path Specificity
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors (e.g., "client retries with
  exponential back-off up to 5 attempts, then surfaces manual reconcile UI"), not just outcomes
  (e.g., "system recovers"). Steps should include who/what initiates each action: client, server,
  operator, or user.
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that only
  describe the end state (system is back online) without mechanism fail.

### C-08 — Conflict Resolution Strategy
- **Weight**: recommended
- **Category**: coverage
- **Text**: For eventual-consistency scenarios, the output specifies what conflict resolution
  strategy is assumed (last-write-wins, merge, manual reconcile, reject-stale) and flags whether
  the strategy is adequate for the data type involved.
- **Pass condition**: At least one eventual-consistency scenario names a conflict-resolution
  strategy and includes a brief adequacy judgment. Scenarios that describe lag without resolution
  strategy fail.

---

## Aspirational Criteria (raise the bar — 10% of score)

### C-09 — Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that could
  be executed in a test harness: what to inject (network partition, latency spike, service kill),
  expected observable behavior, and pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements
  (injection, expected behavior, pass/fail signal). Vague suggestions to "test resilience" fail.

### C-10 — Observability Hooks
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals (metrics, logs, traces, alerts)
  that would surface each identified gap in production. Each recommendation is tied to a specific
  gap or scenario from the analysis.
- **Pass condition**: At least two observability recommendations are present, each linked to a
  named gap or scenario with a rationale for why that signal would detect the failure.

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

- Output contains no explicit failure scenarios (no structure, just prose advice)
- Output is domain-agnostic (no commerce or distributed systems grounding)
- Recovery paths are all identical or all trivially "restart the service"
