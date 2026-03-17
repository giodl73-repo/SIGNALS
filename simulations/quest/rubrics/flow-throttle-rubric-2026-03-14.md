Rubric written to `simulations/quest/rubrics/flow-throttle-rubric-2026-03-14.md`.

**Summary:**

- **5 essential** (C-01–C-05): bottleneck localization, rate limit hit ordering, backpressure propagation trace, UX per tier, domain grounding in Connectors/PA. All must pass — a generic HTTP 429 walkthrough with no PA-specific constructs fails C-05 outright.
- **3 recommended** (C-06–C-08): unprotected burst path detection, missing retry-after handling, cascading throttle failure analysis. Two of three needed to hit the 80 threshold alongside all essentials.
- **2 aspirational** (C-09–C-10): quantified throughput model (actual numbers vs. limits), actionable PA-specific remediations (named features, not generic advice).

Golden threshold requires all essentials + composite >= 80. With all 5 essential + 2/3 recommended you land exactly at 80.
ondition**: Output names a specific system component (not a generic "the API") as the bottleneck and states the request volume or rate at which it saturates. Vague statements like "the system slows down" do not pass.

### C-02 — Rate Limit Hit Ordering
- **Category**: correctness
- **Weight**: essential
- **Text**: The output establishes which rate limits are hit first, second, and so on — producing a ranked sequence rather than a flat list of limits.
- **Pass condition**: Output presents at least two throttle tiers in explicit order (e.g., "connector-level at 600 req/min hits before tenant-level at 1200 req/min") and explains why that ordering holds for the scenario's request volume. An unordered list of limits does not pass.

### C-03 — Backpressure Propagation Trace
- **Category**: correctness
- **Weight**: essential
- **Text**: The output traces how throttling at one tier propagates upstream or downstream — showing the causal chain from the first throttled component to the caller or downstream consumer.
- **Pass condition**: Output describes at least one propagation step: what signal travels (error code, retry-after header, queue depth, etc.), which component receives it, and what that component does in response. Stating only that "backpressure occurs" without a causal chain does not pass.

### C-04 — User Experience per Throttle Tier
- **Category**: coverage
- **Weight**: essential
- **Text**: The output characterizes the user-facing experience at each identified throttle tier — distinguishing between transparent retry, visible delay, error surfaced to user, and silent data loss.
- **Pass condition**: Output maps at least two distinct throttle tiers to distinct UX outcomes (not the same outcome for all tiers). Each mapping must state what the user sees or experiences, not just what the system does internally.

### C-05 — Domain Grounding in Connectors / Power Automate
- **Category**: correctness
- **Weight**: essential
- **Text**: The analysis uses terminology and limits specific to the Connectors / Power Automate throughput domain — not generic API rate-limiting theory.
- **Pass condition**: Output references at least one Power Automate or connector-specific construct (e.g., Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, or Microsoft 365 service protection limits). Generic HTTP 429 descriptions without connector context do not pass.

---

## Recommended Criteria (weight: 30)

### C-06 — Unprotected Burst Path Detection
- **Category**: depth
- **Weight**: recommended
- **Text**: The output identifies at least one path in the flow that can emit a burst of requests without a rate-limiting guard — e.g., an Apply to Each loop with no concurrency cap, a parallel branch with unbounded fan-out, or a trigger with no debounce.
- **Pass condition**: Output names a specific flow construct or pattern that creates unprotected burst exposure and explains why it bypasses or overwhelms the rate limit. Must be specific to the scenario, not a generic warning.

### C-07 — Missing Retry-After Handling
- **Category**: depth
- **Weight**: recommended
- **Text**: The output identifies gaps in retry-after handling — cases where a 429 response is received but the retry-after header value is ignored, not read, or results in a fixed backoff that undershoots or overshoots the required wait.
- **Pass condition**: Output describes at least one specific location where retry-after handling is absent or incorrect, explains the consequence (hammering, premature retry, extended outage), and links it to a specific action or connector call in the scenario.

### C-08 — Cascading Throttle Failure Analysis
- **Category**: depth
- **Weight**: recommended
- **Text**: The output traces at least one scenario where throttling at one tier causes a second tier to also throttle — a cascade — rather than treating each limit as independent.
- **Pass condition**: Output names two components in a cascade sequence, explains the causal link (e.g., "retry storm from connector A increases call volume to service B, which then hits its own limit"), and characterizes the resulting failure mode (brownout, full stop, partial data).

---

## Aspirational Criteria (weight: 10)

### C-09 — Quantified Throughput Model
- **Category**: depth
- **Weight**: aspirational
- **Text**: The output provides a quantified throughput model — actual numbers, formulas, or threshold comparisons that allow the reader to determine whether a given request volume is safe, marginal, or over-limit for the scenario.
- **Pass condition**: Output includes at least one numeric threshold (requests/minute, requests/day, concurrent runs) alongside the scenario's projected volume, and states whether the scenario is safe or at risk. Qualitative-only analysis does not pass this criterion.

### C-10 — Actionable Remediation with Connector Specifics
- **Category**: behavior
- **Weight**: aspirational
- **Text**: The output concludes with specific, implementable mitigations — not generic advice — that reference Power Automate or connector controls available to the developer (e.g., concurrency control settings, chunking strategies, premium entitlement upgrades, scheduled trigger spreading, or service principal pooling).
- **Pass condition**: Output provides at least two distinct remediations, each naming a specific Power Automate feature or setting (not "add retries" or "reduce load"), and explains which identified problem each remediation addresses.

---

## Criterion Summary

| ID   | Category    | Weight        | Short Title                        |
|------|-------------|---------------|------------------------------------|
| C-01 | correctness | essential     | Bottleneck localization            |
| C-02 | correctness | essential     | Rate limit hit ordering            |
| C-03 | correctness | essential     | Backpressure propagation trace     |
| C-04 | coverage    | essential     | UX per throttle tier               |
| C-05 | correctness | essential     | Domain grounding (Connectors/PA)   |
| C-06 | depth       | recommended   | Unprotected burst path detection   |
| C-07 | depth       | recommended   | Missing retry-after handling       |
| C-08 | depth       | recommended   | Cascading throttle failure         |
| C-09 | depth       | aspirational  | Quantified throughput model        |
| C-10 | behavior    | aspirational  | Actionable PA-specific remediation |

---

## Scoring Examples

**Minimal pass (golden threshold)**
- All 5 essential pass, 0 recommended, 0 aspirational
- Score = (5/5 * 60) + (0/3 * 30) + (0/2 * 10) = 60 -- does NOT meet >= 80

**Solid pass**
- All 5 essential pass, 2/3 recommended pass, 0 aspirational
- Score = 60 + (2/3 * 30) + 0 = 60 + 20 = 80 -- exactly meets threshold

**Strong output**
- All 5 essential, all 3 recommended, 1 aspirational
- Score = 60 + 30 + (1/2 * 10) = 95
