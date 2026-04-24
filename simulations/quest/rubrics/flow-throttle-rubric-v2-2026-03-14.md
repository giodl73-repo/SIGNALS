Written. Here's what changed:

---

**v2 additions — three new aspirational criteria (C-11–C-13), 3 points each, max score 109:**

**C-11 — Two-Barrier Domain Validation** (R1 Signal 1)
Gates catch missing constructs; validation roles catch imprecise ones. An output passes only if it validates PA construct accuracy twice — once in context, once at a dedicated review step. A single domain-rule pass (V-01/V-02/V-03 pattern) does not pass this criterion.

**C-12 — Structured Tabular Analysis within Gated Phases** (R1 Signal 2)
Tables, not prose, for any criterion where ordering or comparison is required. At least two of: tier ordering, backpressure hops, burst paths, cascade sequence, risk register — each in a table whose columns enforce the hardest pass condition for that criterion.

**C-13 — Inertia-to-Cascade Causal Thread** (R1 Signal 3)
The bottleneck statement (C-01) must name the naive assumption that breaks, and the cascade section (C-08) must resolve that framing. C-01 and C-08 logically disconnected = fail, even if both pass their individual criteria.

**Scoring impact:**
- V-05 R1 equivalent stays at 100 on the original ten criteria
- A V-05-style output that also satisfies all three structure criteria scores 109
- Golden threshold stays at 80 — no existing pass/fail decisions are disturbed
 and so on -- producing a ranked sequence rather than a flat list of limits.
- **Pass condition**: Output presents at least two throttle tiers in explicit order (e.g., "connector-level at 600 req/min hits before tenant-level at 1200 req/min") and explains why that ordering holds for the scenario request volume. An unordered list of limits does not pass.

### C-03 -- Backpressure Propagation Trace
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The output traces how throttling at one tier propagates upstream or downstream -- showing the causal chain from the first throttled component to the caller or downstream consumer.
- **Pass condition**: Output describes at least one propagation step: what signal travels (error code, retry-after header, queue depth, etc.), which component receives it, and what that component does in response. Stating only that "backpressure occurs" without a causal chain does not pass.

### C-04 -- User Experience per Throttle Tier
- **Category**: coverage
- **Weight**: essential (12)
- **Text**: The output characterizes the user-facing experience at each identified throttle tier -- distinguishing between transparent retry, visible delay, error surfaced to user, and silent data loss.
- **Pass condition**: Output maps at least two distinct throttle tiers to distinct UX outcomes (not the same outcome for all tiers). Each mapping must state what the user sees or experiences, not just what the system does internally.

### C-05 -- Domain Grounding in Connectors / Power Automate
- **Category**: correctness
- **Weight**: essential (12)
- **Text**: The analysis uses terminology and limits specific to the Connectors / Power Automate throughput domain -- not generic API rate-limiting theory.
- **Pass condition**: Output references at least one Power Automate or connector-specific construct (e.g., Power Platform request entitlements, connector throttling policies, flow run concurrency limits, action call limits, premium vs. standard connector tiers, or Microsoft 365 service protection limits). Generic HTTP 429 descriptions without connector context do not pass.

---

## Recommended Criteria (weight: 30)

### C-06 -- Unprotected Burst Path Detection
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output identifies at least one path in the flow that can emit a burst of requests without a rate-limiting guard -- e.g., an Apply to Each loop with no concurrency cap, a parallel branch with unbounded fan-out, or a trigger with no debounce.
- **Pass condition**: Output names a specific flow construct or pattern that creates unprotected burst exposure and explains why it bypasses or overwhelms the rate limit. Must be specific to the scenario, not a generic warning.

### C-07 -- Missing Retry-After Handling
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output identifies gaps in retry-after handling -- cases where a 429 response is received but the retry-after header value is ignored, not read, or results in a fixed backoff that undershoots or overshoots the required wait.
- **Pass condition**: Output describes at least one specific location where retry-after handling is absent or incorrect, explains the consequence (hammering, premature retry, extended outage), and links it to a specific action or connector call in the scenario.

### C-08 -- Cascading Throttle Failure Analysis
- **Category**: depth
- **Weight**: recommended (10)
- **Text**: The output traces at least one scenario where throttling at one tier causes a second tier to also throttle -- a cascade -- rather than treating each limit as independent.
- **Pass condition**: Output names two components in a cascade sequence, explains the causal link (e.g., "retry storm from connector A increases call volume to service B, which then hits its own limit"), and characterizes the resulting failure mode (brownout, full stop, partial data).

---

## Aspirational Criteria -- Original (weight: 10)

### C-09 -- Quantified Throughput Model
- **Category**: depth
- **Weight**: aspirational (5)
- **Text**: The output provides a quantified throughput model -- actual numbers, formulas, or threshold comparisons that allow the reader to determine whether a given request volume is safe, marginal, or over-limit for the scenario.
- **Pass condition**: Output includes at least one numeric threshold (requests/minute, requests/day, concurrent runs) alongside the scenario projected volume, and states whether the scenario is safe or at risk. Qualitative-only analysis does not pass this criterion.

### C-10 -- Actionable Remediation with Connector Specifics
- **Category**: behavior
- **Weight**: aspirational (5)
- **Text**: The output concludes with specific, implementable mitigations -- not generic advice -- that reference Power Automate or connector controls available to the developer (e.g., concurrency control settings, chunking strategies, premium entitlement upgrades, scheduled trigger spreading, or service principal pooling).
- **Pass condition**: Output provides at least two distinct remediations, each naming a specific Power Automate feature or setting (not "add retries" or "reduce load"), and explains which identified problem each remediation addresses.

---

## Aspirational Criteria -- R1 Patterns (weight: 9)

These criteria capture prompt-structural excellence signals identified in Round 1. They reward outputs whose internal organization reflects the two-barrier, pre-printed-table, and inertia-seeding patterns that distinguish V-05 from all other variations.

### C-11 -- Two-Barrier Domain Validation
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R1 Signal 1 -- two-barrier essential enforcement
- **Text**: The output demonstrates PA domain accuracy through two independent checks -- not just presence of PA terminology but contextual precision. This is evidenced when the output both (a) names exact PA constructs and (b) explicitly validates or corrects earlier construct usage at a dedicated review step.
- **Pass condition**: Output contains at least two distinct moments of PA domain validation: one where PA constructs are named in context (the gate pass) and one where the accuracy of those construct names is confirmed or corrected against actual PA behavior (the validation-role pass). An output that lists PA terms once without self-verification does not pass. Applies primarily when the output is structured enough to have distinguishable analysis and review phases.

### C-12 -- Structured Tabular Analysis within Gated Phases
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R1 Signal 2 -- pre-printed tables within gated phases
- **Text**: The output organizes ordered, comparative, or enumerated analysis in tables -- not prose lists -- for criteria where both prose shortcuts and section omission are plausible failure modes. This combines format discipline (table columns prevent compression) with coverage discipline (all required rows present).
- **Pass condition**: Output presents at least two of the following in table form rather than prose: throttle tier ordering, backpressure hop chain, burst path enumeration, cascade sequence, or quantified risk register. Each table must have columns that structurally enforce the criterion's hardest requirement (e.g., a "Hit order" column for C-02, a "Load added" column for C-08, a "Status" column for C-09). Prose descriptions with inline numbers do not pass even if the numbers are correct.

### C-13 -- Inertia-to-Cascade Causal Thread
- **Category**: structure
- **Weight**: aspirational (3)
- **Source**: R1 Signal 3 -- inertia framing as cross-phase cascade catalyst
- **Text**: The bottleneck statement explicitly names the naive assumption that the scenario invalidates, and this framing carries forward into the cascade analysis -- creating a continuous causal thread rather than treating bottleneck identification and cascade analysis as isolated observations.
- **Pass condition**: Output bottleneck statement (C-01) contains language that names an assumption about limit independence or additive behavior that fails under the scenario (e.g., "the assumption that tier limits are independent fails here because..."). The cascade section (C-08) then resolves or extends that framing -- the cascade is presented as the consequence of the broken assumption, not a new independent finding. An output where C-01 and C-08 are logically disconnected does not pass even if both individually meet their own pass conditions.

---

## Criterion Summary

| ID   | Category    | Weight       | Points | Short Title                        |
|------|-------------|--------------|--------|------------------------------------|
| C-01 | correctness | essential    | 12     | Bottleneck localization            |
| C-02 | correctness | essential    | 12     | Rate limit hit ordering            |
| C-03 | correctness | essential    | 12     | Backpressure propagation trace     |
| C-04 | coverage    | essential    | 12     | UX per throttle tier               |
| C-05 | correctness | essential    | 12     | Domain grounding (Connectors/PA)   |
| C-06 | depth       | recommended  | 10     | Unprotected burst path detection   |
| C-07 | depth       | recommended  | 10     | Missing retry-after handling       |
| C-08 | depth       | recommended  | 10     | Cascading throttle failure         |
| C-09 | depth       | aspirational | 5      | Quantified throughput model        |
| C-10 | behavior    | aspirational | 5      | Actionable PA-specific remediation |
| C-11 | structure   | aspirational | 3      | Two-barrier domain validation      |
| C-12 | structure   | aspirational | 3      | Structured tabular analysis        |
| C-13 | structure   | aspirational | 3      | Inertia-to-cascade causal thread   |

---

## Scoring Examples

**Below threshold**
- All 5 essential pass, 0 recommended, 0 aspirational
- Score = 60 + 0 + 0 = 60 -- does NOT meet >= 80

**Minimal pass (golden threshold)**
- All 5 essential pass, 2/3 recommended pass, 0 aspirational
- Score = 60 + 20 + 0 = 80 -- exactly meets threshold

**Strong output**
- All 5 essential, all 3 recommended, 1 original aspirational
- Score = 60 + 30 + 5 = 95

**Full original sweep (V-05 R1 equivalent)**
- All 5 essential, all 3 recommended, both original aspirational
- Score = 60 + 30 + 10 = 100

**R1 pattern bonus**
- All 5 essential, all 3 recommended, both original aspirational, all 3 R1 patterns
- Score = 60 + 30 + 10 + 9 = 109 (max possible)

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| v1 | 2026-03-14 | Initial rubric -- 10 criteria (C-01-C-10) |
| v2 | 2026-03-14 | Added C-11-C-13 from Round 1 excellence signals; expanded max score to 109; golden threshold unchanged at 80 |