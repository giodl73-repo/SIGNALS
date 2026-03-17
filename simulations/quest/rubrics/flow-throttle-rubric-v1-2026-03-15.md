---
skill: quest-rubric
skill_target: flow-throttle
date: 2026-03-15
version: 1
---

# Rubric: flow-throttle

Evaluates simulated throughput analysis across rate-limited systems. A passing output
traces bottleneck location, rate-limit hit order, backpressure propagation, user-visible
impact at each tier, and identifies structural gaps (burst paths, retry-after, cascades).

---

## Criteria

### Essential (weight: 60 pts total -- all must pass)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-01 | **Bottleneck localization** -- For the given request volume, the output identifies *which specific component or tier* hits its rate limit first, and in what order subsequent tiers are impacted. | correctness | Names at least one concrete bottleneck component (connector, gateway, API endpoint, queue) and asserts a hit-order sequence among tiers. Vague "it gets throttled" without location fails. |
| C-02 | **Backpressure propagation trace** -- The output traces how throttle pressure propagates upstream (caller receives signal, retries, queues, or drops) rather than stopping at the first hit. | correctness | Describes at least two hops in the propagation chain: the throttled component AND the behavior of its caller in response. A single-hop description fails. |
| C-03 | **Rate-limit tier enumeration** -- The output identifies the applicable rate limits for the scenario (e.g., per-connection, per-user, tenant, platform) and correctly matches each to the system component that enforces it. | coverage | At least two distinct rate-limit tiers are named with their enforcing component. Generic "API limits apply" without tier distinction fails. |
| C-04 | **User experience at each throttle tier** -- For each throttle tier identified, the output describes the observable user experience (latency spike, error code, silent drop, queue delay, degraded mode). | depth | Every named tier from C-03 has a corresponding UX description. A tier named without UX consequence fails this criterion. |
| C-05 | **Unprotected burst path identification** -- The output explicitly calls out at least one path or scenario where burst traffic can bypass or overwhelm throttle controls. | correctness | A concrete burst scenario is named (e.g., parallel branch fan-out, retry storm, initial cold-start surge). Output that only describes steady-state throttle without any burst analysis fails. |

---

### Recommended (weight: 30 pts total -- output improves with these)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-06 | **Retry-after handling gaps** -- The output checks whether callers correctly consume and honor `Retry-After` (or equivalent) signals, and flags any caller that ignores them and contributes to retry storms. | behavior | At least one caller is evaluated for retry-after compliance, with a pass/fail verdict and consequence described. Omitting retry-after analysis entirely fails. |
| C-07 | **Cascading throttle failure scenario** -- The output describes at least one scenario where throttling at one tier causes a second downstream tier to also throttle, compounding the impact beyond the initial bottleneck. | depth | A two-tier cascade is named: Tier A throttles -> Tier B receives delayed/batched traffic -> Tier B throttles. Single-tier analysis only fails. |
| C-08 | **Quantified throughput thresholds** -- The output provides numeric context: requests-per-second, burst ceiling, queue depth, or timeout window for at least the primary bottleneck tier identified in C-01. | correctness | At least one threshold is stated as a number (even if approximate or from documentation). Purely qualitative descriptions ("it gets slow") fail. |

---

### Aspirational (weight: 10 pts total -- raise the bar)

| ID | Text | Category | Pass Condition |
|----|------|----------|----------------|
| C-09 | **Mitigation recommendations with tradeoffs** -- For each structural gap found (burst path, missing retry-after, cascade), the output proposes a concrete mitigation and states the tradeoff (e.g., adding a queue reduces burst but adds latency). | depth | At least two mitigations with explicit tradeoffs. Mitigations without tradeoffs, or tradeoffs without mitigations, score partial credit only (counts as fail for binary scoring). |
| C-10 | **Comparative severity ranking** -- The output ranks the identified throttle risks by user-visible severity (high/medium/low or ordered list) and justifies the ranking with reference to impact frequency or blast radius. | behavior | A ranked list of at least three risks with justification. Unranked lists or rankings without justification fail. |

---

## Scoring

```
Composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: All 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Ready for golden artifact |
| Silver | >= 60, all essential pass | Useful, missing depth |
| Bronze | >= 40, some essential pass | Partial signal, not reliable |
| Fail | Any essential fails | Output not usable |

---

## Evaluation Notes

- C-01 and C-02 are the core of the skill -- a throttle simulation that cannot locate the
  bottleneck or trace propagation is not a simulation, it is speculation.
- C-05 (burst path) is the most commonly missed criterion in initial outputs; models tend
  to describe steady-state throttle only.
- C-08 (quantified thresholds) should be drawn from Power Automate / Connector
  documentation rates where applicable; invented numbers fail this criterion.
- The stock role for this skill is Connectors / Power Automate throughput domain expert;
  the rubric assumes that framing when evaluating domain accuracy.
