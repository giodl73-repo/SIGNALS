---
skill: quest-rubric
skill_target: flow-ratelimit
date: 2026-03-17
version: 1
---

# Rubric: flow-ratelimit

Evaluate simulated throughput analysis across rate-limited systems. The output must identify which rate limits are hit first for a given request volume, trace backpressure propagation, describe user-visible behavior at each throttle tier, flag unprotected burst paths, and check for missing Retry-After handling. Stock domain: Connectors / Power Automate throughput.

---

## Criteria

### Essential (60 points total — must all pass)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **First-limit Ordering** | correctness | essential | Output identifies which rate limit is reached first for the stated request volume, and explains why that limit is the binding constraint before others are reached (e.g., connector-tier call limit exhausted at 450 req/min before gateway limit of 1000 req/min). A flat list of limits without ordering or reasoning does not pass. |
| C-02 | **Backpressure Propagation Chain** | correctness | essential | Output traces how throttling at the first bottleneck propagates causally to at least one upstream or downstream component — showing the directional mechanism, not just a list of affected components. "Component B is also throttled" does not pass; "Component A's queue fills → Component B receives delayed events → Component B's own timeout fires" does pass. |
| C-03 | **User Experience at Each Throttle Tier** | coverage | essential | Output describes observable user-facing behavior at each distinct throttle tier reached (e.g., 429 with Retry-After shown in connector error, flow run queued and delayed, flow run failed with ActionThrottled, silent exponential backoff invisible to user). At least two distinct tiers described if the scenario spans multiple tiers. |
| C-04 | **Unprotected Burst Path Identification** | correctness | essential | Output identifies at least one structurally unprotected burst path — a trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between the source and the rate-limited endpoint. A path that has throttle controls but at a higher tier does not qualify. |
| C-05 | **Retry-After Handling Gap Check** | coverage | essential | Output explicitly evaluates whether the flow or connector handles Retry-After headers (or equivalent backoff signals such as `x-ms-ratelimit-remaining`, `Retry-After-Ms`) from throttled endpoints. Missing handling must be flagged as a finding with a description of the failure mode it causes (e.g., immediate retry storm, permanent failure after N retries). |

---

### Recommended (30 points total — output is better with these)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-06 | **Cascading Throttle Failure Scenario** | depth | recommended | Output constructs or identifies a specific scenario where throttling at one tier triggers a second distinct throttle event at a different tier — and describes the compounding effect on throughput or error rate. Two independent limits both hit under load do not constitute a cascade; the second throttle must be causally triggered by the first. |
| C-07 | **Numeric Rate Limit Specificity** | depth | recommended | At least one rate limit is cited with a concrete numeric threshold (e.g., "600 API calls per 60 seconds per connection", "5 concurrent runs per environment per flow") rather than described only in abstract or relative terms. Estimates are acceptable if labeled as such. |
| C-08 | **Volume-to-Behavior Mapping** | format | recommended | Output includes a structured mapping — table, tiered list, or equivalent — that shows which throttle behavior activates at which request volume range, enabling a reader to determine expected system behavior for a given load without re-reading the full analysis. |

---

### Aspirational (10 points total — raise the bar once essential/recommended are stable)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-09 | **Per-bottleneck Mitigation Prescriptions** | depth | aspirational | For each identified bottleneck or unprotected burst path, output proposes a concrete remediation specific to the component and limit type (e.g., "enable concurrency control on the For Each action capped at 5 parallel branches", "add exponential backoff with Retry-After header parsing to the HTTP action", "split batch trigger into N sequential calls with 1s delay"). Generic advice ("add retry logic") does not pass — the prescription must name the specific action, setting, or pattern. |
| C-10 | **Quantified Impact at Load Spike** | depth | aspirational | Output provides numeric estimates of degradation at a specific load multiplier (e.g., "at 5× normal volume with a 600 req/min limit, 42% of requests are queued beyond 30s, 11% fail after exhausting 3 retry attempts") using the rate limits cited in C-07 as the arithmetic basis. The estimate must be derivable from the stated limits — not asserted as a generic percentage. |

---

## Scoring

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass **AND** composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Ready for golden file |
| Silver | >= 65, all essential pass | Usable, missing depth |
| Bronze | >= 50, >= 4 essential pass | Partial — gap in core coverage |
| Fail | < 50 or any essential fail | Not useful — regenerate |

---

## Evaluator Notes

- **C-01 vs C-07**: C-01 requires ordering reasoning; C-07 requires a numeric threshold. An output can pass C-01 with relative ordering ("connector limit is lower than gateway limit") without passing C-07 (no number stated). Both are needed for a Silver score.
- **C-02 causal chain**: A flat list of "also throttled" components does not pass. Look for explicit causal connectors: "because", "causes", "triggers", "fills the queue", "delays downstream". A chain of two or more causal steps is required.
- **C-04 unprotected path**: The path must be structurally unprotected — no cap, no retry policy, no queue. A path with a high-tier limit that is not yet hit at the stated volume does not qualify. The criterion tests for missing protection, not for limits not yet reached.
- **C-05 Retry-After**: The evaluation must be explicit — not inferred. An output that describes retry behavior without specifically checking for Retry-After header parsing does not pass. The finding must name the failure mode caused by missing handling.
- **C-06 cascading**: The cascade is directional: first throttle causes second throttle. Two limits independently saturated by the same load spike is not a cascade — that is coincident throttling.
- **C-08 structure**: Any structured form passes — a table, a numbered tier list, a bullet list with volume ranges. Prose paragraphs describing behavior at different load levels do not pass unless they are formatted as discrete volume-range sections.
- **C-09 vs C-04**: C-04 identifies unprotected burst paths as findings. C-09 requires that each finding receives a specific prescription. An output that identifies three paths (C-04 passes) but prescribes mitigation for only one does not pass C-09.
- **C-10 vs C-07**: C-07 passes with any single numeric threshold. C-10 requires that the quantified impact section traces its arithmetic back to the limits cited in C-07 — the degradation estimate must be grounded, not asserted. Generic percentages without a derivation path fail C-10 even when C-07 is satisfied.
