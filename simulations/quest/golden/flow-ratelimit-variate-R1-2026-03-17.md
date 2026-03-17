---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 1
rubric_version: 1
---

# flow-ratelimit — Variate R1

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (output format), V-02 (role sequence), V-03 (phrasing register).
Combination variations: V-04 (lifecycle emphasis + output format), V-05 (role sequence + inertia framing + output format).

---

## V-01

**Variation axis:** Output format — table-dominant
**Hypothesis:** Enforcing a named table schema for every section forces numeric specificity (C-07) and structured volume-to-behavior mapping (C-08). Each column acts as a type constraint; the model cannot fill a `Limit (req/min)` cell with "limited throughput" the way it can in prose.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in the input. Treat the stated request volume as 1x nominal. Also analyze at 2x and 5x.

Produce the following six tables in order. Every cell SHALL be filled. Do not skip a table.

---

**TABLE 1 — THROTTLE TIER REGISTRY**

Identify every rate-limiting component in the system. For each:

| Tier-ID | Component | Limit (req/min or req/sec — number required) | Scope | Status at 1x | Status at 2x | Status at 5x | Failure mode at saturation |
|---------|-----------|---------------------------------------------|-------|--------------|--------------|--------------|---------------------------|
| T-01 | | | | | | | |
| T-02 | | | | | | | |
| (add rows as needed) | | | | | | | |

Rules:
- `Limit` must contain a number and unit (e.g., "600 req/min"). A vague label ("limited", "throttled") fails.
- `Status` must be one of: SAFE / APPROACHING / HIT / EXCEEDED.
- `Failure mode` must be one of: 429-with-Retry-After / 429-silent / queue-delay / run-cancel / timeout / drop.
- At least two distinct `Failure mode` values must appear across all T-01..T-N rows.

---

**TABLE 2 — BINDING ORDER**

State which tier is hit first for each volume band, and explain causally why it binds before the others.

| Volume band | Binding tier (T-ID) | Limit that binds (copy from TABLE 1) | Why this tier binds first — causal reason | What the next tier to bind would be |
|-------------|--------------------|------------------------------------|------------------------------------------|-------------------------------------|
| 1x | | | | |
| 2x | | | | |
| 5x | | | | |

A row that states "T-01 binds" without a causal reason fails. The causal reason must name why this tier's limit is lower or reached sooner than the alternatives.

---

**TABLE 3 — BACKPRESSURE PROPAGATION**

Trace how throttling at the binding tier propagates causally through the system. Minimum 2 hops.

| Hop | From component | Mechanism | To component | Observable effect |
|-----|---------------|-----------|-------------|------------------|
| 1 | | | | |
| 2 | | | | |
| (add rows for each additional hop) | | | | |

`Mechanism` must be named from this set: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. Generic terms ("blocked", "slowed") fail.

---

**TABLE 4 — USER EXPERIENCE PER THROTTLE TIER**

For each tier that is hit (STATUS = HIT or EXCEEDED at any volume), describe what the user sees.

| Tier-ID | Error code or platform signal | User-visible behavior at tier saturation | Is the throttle visible to the user? (Y/N) | How the user discovers the problem |
|---------|------------------------------|------------------------------------------|------------------------------------------|------------------------------------|
| | | | | |

`Error code or platform signal` must be a specific identifier (e.g., "HTTP 429", "ActionThrottled", "TL-0001"). "Request fails" fails. At least 2 distinct tiers must be represented.

---

**TABLE 5 — UNPROTECTED BURST PATHS AND RETRY-AFTER GAPS**

Section A — Unprotected burst paths.

| Path-ID | Entry point (trigger or action) | Request generation mechanism | Why it is structurally unprotected (no cap / no retry policy / no queue buffer) | Risk at 5x |
|---------|---------------------------------|------------------------------|--------------------------------------------------------------------------------|------------|
| P-01 | | | | |

A path with a high-tier limit not yet hit at stated volume does NOT qualify — the path must lack structural protection, not merely have headroom.

Section B — Retry-After handling gaps.

| Caller | Throttled endpoint | Retry-After header consumed? (Y/N) | Equivalent signal checked (x-ms-ratelimit-remaining, Retry-After-Ms)? (Y/N) | Finding | Failure mode if gap present |
|--------|-------------------|-----------------------------------|----------------------------------------------------------------------------|---------|----------------------------|
| | | | | | |

Each row must carry a `Finding` (PASS or FAIL-[reason]) and, for FAIL rows, the failure mode it causes (e.g., "immediate retry storm", "permanent failure after N retries with no backoff").

---

**TABLE 6 — VOLUME-TO-BEHAVIOR SUMMARY**

One-stop reference: what does the system do at each load level?

| Volume | Which tier binds | User experience | Cascading effect? (Y/N + description) | Recovery path |
|--------|-----------------|-----------------|---------------------------------------|---------------|
| 1x | | | | |
| 2x | | | | |
| 5x | | | | |

`Cascading effect` requires naming the second tier triggered *by* the first throttle — not two tiers independently hit by load.

---

After TABLE 6, write a **MITIGATION SECTION**: for each unprotected burst path in TABLE 5 Section A and each FAIL row in TABLE 5 Section B, prescribe a specific remediation. Name the exact action, connector setting, or API parameter (e.g., "set `maxConcurrentCalls: 5` on the For Each action", "add exponential backoff reading `Retry-After` header in HTTP action error branch"). Generic advice ("add retry logic") does not pass.

---

## V-02

**Variation axis:** Role sequence — three named analysts with explicit handoffs
**Hypothesis:** Separating the throttle-inventory analyst, the UX analyst, and the gap analyst into distinct named roles prevents early-role findings from crowding out later-role findings. Each role owns exactly one rubric concern; handoffs force completion before the next role activates.

---

You are executing the flow-ratelimit skill as a three-role analyst chain. Each role activates in sequence. A role SHALL NOT activate until its predecessor's handoff is declared.

Stock domain: Connectors / Power Automate throughput. Treat the input's request volume as 1x nominal; also analyze at 2x and 5x.

---

**ROLE A — THROTTLE INVENTORY ANALYST**

Responsibility: Identify every rate-limiting tier in the system, assign numeric limits, determine binding order.

Produce:

1. **Tier inventory** — list each component with its numeric limit (number + unit required), scope, and status at 1x / 2x / 5x.

2. **Binding order statement** — for each volume band, state which tier binds first. Explain causally why that tier's limit is reached before the others. A statement of "T-01 binds first" without a causal reason does not close this section.

3. **Load-shape classification** — for each tier, state whether its limit applies identically to uniform and burst traffic (SHAPE-NEUTRAL) or whether burst traffic reaches it faster than uniform traffic of the same total volume (SHAPE-SENSITIVE — name the differential).

When these three items are complete, record: **ROLE A COMPLETE — HANDOFF TO ROLE B**.

Do not proceed to Role B until this handoff is declared.

---

**ROLE B — UX AND BACKPRESSURE ANALYST**

Activation condition: ROLE A COMPLETE declared.

Responsibility: Trace backpressure propagation and describe user experience per tier.

Produce:

1. **Backpressure chain** — starting from the binding tier identified by Role A, trace how throttle pressure propagates. Minimum 2 hops. For each hop: name the source component, the mechanism (from: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade), the destination component, and the observable effect. Generic terms ("blocked") fail.

2. **UX per throttle tier** — for each tier that reaches HIT or EXCEEDED status: describe the observable user-facing behavior. State the specific error code or platform signal (e.g., "HTTP 429", "ActionThrottled"). Describe whether the throttle is visible to the user or silent. At least 2 distinct tiers must be described.

3. **Cascade scenario** — describe one scenario where throttling at the first tier causally triggers throttling at a second distinct tier. The second throttle must be caused by the first — two tiers independently saturated by load is not a cascade.

When these three items are complete, record: **ROLE B COMPLETE — HANDOFF TO ROLE C**.

---

**ROLE C — GAP ANALYST**

Activation condition: ROLE B COMPLETE declared.

Responsibility: Identify structural protection gaps and evaluate Retry-After handling.

Produce:

1. **Unprotected burst paths** — identify at least one trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between the source and the rate-limited endpoint. State explicitly what protection is absent. A path with a high-tier limit not yet hit at stated volume does NOT qualify.

2. **Retry-After assessment** — for each caller interacting with a throttled tier: state whether the Retry-After header (or equivalent: `x-ms-ratelimit-remaining`, `Retry-After-Ms`) is consumed and honored. Verdict: PASS or FAIL. For FAIL: name the failure mode caused by missing handling (e.g., "immediate retry storm", "permanent failure after N retries with no backoff").

3. **Quantified load-spike impact** — using the numeric limits from Role A, estimate degradation at 5x volume. Show the arithmetic: how many requests per minute exceed the binding tier's limit, what fraction are queued or dropped, and over what time window. The estimate must be derivable from the limits stated in the tier inventory.

4. **Per-gap mitigation** — for each unprotected burst path and each FAIL Retry-After row: prescribe a specific remediation naming the exact action, connector property, or API parameter. Generic advice fails.

When all four items are complete, record: **ROLE C COMPLETE — ANALYSIS CLOSED**.

---

## V-03

**Variation axis:** Phrasing register — conversational imperative
**Hypothesis:** Shorter, direct commands with minimal scaffolding reduce model distraction. When the prompt stops explaining itself and just tells the model what to do, the model spends more tokens on analysis. This may improve causal reasoning quality in C-01 and C-02 at the cost of some structural guarantees.

---

You're a Power Automate throughput expert. A system is hitting rate limits under load. Walk through it.

**1. Map the limits.**
List every rate-limiting layer in the system. For each one: the component name, the numeric limit (number + unit — not "limited", not "throttled"), and what happens when that limit is hit. Use the request volume from the input as 1x. Note status at 1x, 2x, and 5x.

**2. Find the first bottleneck.**
Which limit is hit first? Explain *why* — not just that it's lower, but why requests reach it before any other limit. This is the binding constraint.

**3. Follow the pressure.**
Once the binding tier throttles, where does that pressure go? Trace it hop by hop through the system. At each hop: name the mechanism (queue-fill, connection-hold, retry-amplification, dependency-stall, or timeout-cascade — pick one) and what the user or system sees. Trace at least 2 hops from the binding tier.

**4. Describe what users see.**
For each throttle tier that gets hit: what does the user experience? Give the specific error code or signal (HTTP 429, ActionThrottled, etc. — not just "an error"). Is the throttle visible to them or does it happen silently? Describe at least 2 tiers.

**5. Find the unprotected paths.**
Find at least one path where requests can burst without hitting any cap — no concurrency limit, no retry policy, no buffer between the request source and the rate-limited endpoint. Explain what's missing. Don't list paths that have high limits but aren't hit yet — find paths that have no protection at all.

**6. Check Retry-After.**
For each caller hitting a throttled endpoint: is the Retry-After header (or `x-ms-ratelimit-remaining`, `Retry-After-Ms`) being read and honored? If not, say so and describe what goes wrong — retry storm, silent failure, run cancellation, something specific.

**7. Build a load table.**
Make a simple table: at 1x, 2x, and 5x load — which tier binds, what does the user see, does anything cascade. One row per volume level.

**8. Name the cascade.**
Describe one scenario where the first throttle event causes a second throttle event at a different tier. The second throttle has to be a consequence of the first, not just both hitting limits at the same time.

**9. Fix it.**
For each unprotected burst path and each missing Retry-After handler: prescribe the specific fix. Name the action, the connector setting, or the API parameter. Not "add retry logic" — the actual parameter (`connector.retryPolicy`, `maxConcurrentCalls: 5`, etc.).

**10. Quantify one spike.**
Pick the binding tier from step 2. At 5x load, show the math: how many requests per minute exceed the limit, how many queue or fail, over what time window.

---

## V-04

**Variation axis:** Lifecycle emphasis — finding-first (inverted structure)
**Hypothesis:** Leading with the findings verdict forces the model to commit to a risk stance early. The evidence sections then validate or contradict the verdict. This inverted structure produces cleaner C-01 ordering reasoning (the binding constraint must be named upfront) and more explicit C-04/C-05 gap identification (gaps must be declared before evidence is assembled).

---

You are a Connectors / Power Automate throughput domain expert. Analyze the rate-limited system in the input using an answer-first structure: state findings first, then provide supporting evidence for each finding.

Treat the input's request volume as 1x nominal; analyze at 2x and 5x where relevant.

---

**SECTION 1 — VERDICT BLOCK** (complete this first, before any analysis)

State the following without evidence — you will support each with evidence in Section 2:

1.1 **Binding constraint at 1x**: Which component's rate limit is the first constraint reached? One sentence.

1.2 **Binding constraint at 5x**: Which component's rate limit dominates at high load? Same or different from 1x?

1.3 **Worst user experience**: At 5x load, what is the worst user-observable behavior? Name the specific error signal.

1.4 **Most critical gap**: Is it an unprotected burst path, a missing Retry-After handler, or a cascading failure? Name one.

1.5 **System recovers without intervention?**: Y / N and one-sentence reason.

---

**SECTION 2 — EVIDENCE** (support each verdict item with specific evidence)

**2.1 — Tier inventory and binding order evidence**

List every rate-limiting tier. For each: component name, numeric limit (number + unit required), scope, and status at 1x / 2x / 5x. Then explain causally why the tier named in VERDICT 1.1 binds first: why does request volume exhaust this tier's limit before any other tier's limit?

Include: load-shape note — does burst traffic hit this tier faster than uniform traffic of the same total volume?

**2.2 — Backpressure propagation evidence**

Trace how throttling at the binding tier propagates. Minimum 2 hops. For each hop: source component → mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade) → destination component → observable effect at 1x saturation and at 5x saturation. This evidence supports VERDICT 1.3.

**2.3 — User experience evidence per tier**

For each tier that reaches saturation (any volume): name the specific error code or platform signal (HTTP 429, ActionThrottled, etc. — not "an error"), whether the throttle is user-visible, and what the user observes. At least 2 tiers. This evidence supports VERDICT 1.3.

**2.4 — Unprotected burst path evidence**

Identify at least one trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between source and rate-limited endpoint. State each missing protection type explicitly. This evidence supports VERDICT 1.4 if the critical gap is a burst path.

**2.5 — Retry-After gap evidence**

For each caller interacting with a throttled tier: does it consume and honor the Retry-After header (or `x-ms-ratelimit-remaining`, `Retry-After-Ms`)? Verdict per caller: PASS or FAIL. For each FAIL: name the failure mode (retry storm, permanent failure after N retries, etc.). This evidence supports VERDICT 1.4 if the critical gap is a missing Retry-After handler.

**2.6 — Cascade scenario evidence**

Describe the specific cascade: Tier A throttles → [mechanism] → Tier B receives amplified or delayed traffic → Tier B throttles. Name at least three tiers in the chain. Confirm or revise VERDICT 1.5 based on whether cascade recovery is possible without intervention.

---

**SECTION 3 — VOLUME-TO-BEHAVIOR TABLE**

| Volume | Binding tier | Error signal | User experience | Cascade? | Recovers? |
|--------|-------------|--------------|-----------------|----------|-----------|
| 1x | | | | | |
| 2x | | | | | |
| 5x | | | | | |

---

**SECTION 4 — MITIGATION TABLE**

| Gap-ID | Source (tier or path) | Gap type | Specific mitigation | Exact setting or parameter | Tradeoff |
|--------|----------------------|----------|---------------------|---------------------------|----------|
| | | | | | |

`Specific mitigation` must name an action (not a category). `Exact setting or parameter` must be a named property or API attribute — "add retry logic" fails.

---

**SECTION 5 — QUANTIFIED SPIKE**

Using the numeric limits from Section 2.1: at 5x load, show the arithmetic for the binding tier. How many requests per minute arrive? How many exceed the limit? What fraction queue or fail? Over what time window does the backlog clear? Show the calculation steps — do not assert a percentage without derivation.

---

## V-05

**Variation axis:** Role sequence + inertia framing + output format (combination)
**Hypothesis:** Framing the status-quo ("accept throttling, do nothing") as the named inertia baseline before analysis begins primes the model to treat every finding as a gap from the baseline rather than a neutral observation. Combined with an explicit role chain and mixed table/narrative format, the inertia frame should produce sharper C-04 identification (burst paths are gaps from the baseline, not accidents) and crisper C-05 verdicts (Retry-After handling is a binary: you either improved from baseline or you didn't).

---

You are a Connectors / Power Automate throughput domain expert. Before analyzing the system, establish the inertia baseline.

**INERTIA BASELINE**

The primary competitor to rate-limit protection is: *do nothing*. A system with no throttle management, no Retry-After handling, no burst caps, and no concurrency controls is the inertia state. This is what teams ship when they haven't thought about throughput.

Describe the inertia system's behavior under the input's request volume:
- Which limits get hit first?
- What users see when those limits are hit?
- How quickly does failure cascade?
- Does the system recover, or does it stay failed?

Write 3–5 sentences. This is your baseline; every finding below measures deviation from it.

---

**ROLE 1 — THROTTLE ANALYST**

Identify every rate-limiting component. Produce TABLE A.

**TABLE A — THROTTLE TIER INVENTORY**

| Tier-ID | Component | Limit (req/min — number required) | Scope | Status at 1x | Status at 2x | Status at 5x | Failure mode |
|---------|-----------|----------------------------------|-------|--------------|--------------|--------------|--------------|
| T-01 | | | | | | | |
| T-02 | | | | | | | |

- `Limit` requires a number and unit. Vague labels fail.
- `Failure mode` must be specific: 429-with-Retry-After / 429-silent / queue-delay / run-cancel / timeout / drop.
- At least two distinct failure modes across TABLE A rows.

Then state: **Which tier binds first, and why?** Name the causal mechanism — not just that the limit is lower, but why requests exhaust this tier's limit before the others.

Declare: **ROLE 1 COMPLETE**.

---

**ROLE 2 — BACKPRESSURE AND UX ANALYST**

Activation: ROLE 1 COMPLETE.

**Part A — Backpressure chain**: Starting from the binding tier, trace propagation. Minimum 2 hops. For each hop: source → mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade) → destination → observable effect. Generic mechanism names fail.

**Part B — UX per tier**: For each tier at HIT or EXCEEDED status: error code or platform signal (specific — HTTP 429, ActionThrottled), whether user-visible, what the user observes. At least 2 tiers.

**Part C — Cascade scenario**: One scenario where the first throttle causally triggers a second throttle at a different tier. The second throttle must be a *consequence* of the first — two tiers independently hitting their limits under the same load is not a cascade.

Declare: **ROLE 2 COMPLETE**.

---

**ROLE 3 — GAP ANALYST**

Activation: ROLE 2 COMPLETE.

**Inertia gap framing**: For each finding below, state whether it is an expected consequence of the inertia baseline ("this is what the baseline system does") or a deviation from it ("this gap exists even though teams often assume baseline behavior prevents it").

**Gap 1 — Unprotected burst paths**: Identify at least one trigger or action with no concurrency cap, no retry policy, and no queue buffer between source and the rate-limited endpoint. State what structural protection is absent. A path with a high-tier limit not yet hit does NOT qualify — the path must lack structure, not just headroom. State: is this gap present in the inertia baseline, or does it require additional configuration to appear?

**Gap 2 — Retry-After handling**: For each caller hitting a throttled tier, evaluate whether Retry-After (or `x-ms-ratelimit-remaining`, `Retry-After-Ms`) is consumed and honored. Verdict: PASS or FAIL. For each FAIL: failure mode (retry storm / permanent failure after N retries / run cancellation). State: in the inertia baseline, does this caller handle Retry-After by default, or is handling always absent?

**Gap 3 — Quantified 5x impact**: Using TABLE A numeric limits, calculate: at 5x load, how many requests per minute arrive at the binding tier? How many exceed the limit? What fraction queue or fail in the first 60 seconds? Show the arithmetic. Describe how this differs from inertia-baseline behavior.

Declare: **ROLE 3 COMPLETE**.

---

**SYNTHESIS TABLE — VOLUME-TO-BEHAVIOR WITH INERTIA COMPARISON**

| Volume | Inertia behavior | Protected behavior (if gaps fixed) | Delta |
|--------|------------------|------------------------------------|-------|
| 1x | | | |
| 2x | | | |
| 5x | | | |

*`Delta` = what the user experiences differently if protections are in place versus the inertia baseline.*

---

**MITIGATION TABLE**

| Gap-ID | Source (tier or path) | Gap type | Specific fix | Exact parameter or setting | Improvement over inertia |
|--------|----------------------|----------|-------------|---------------------------|--------------------------|
| | | | | | |

`Exact parameter or setting` must be a named property or API attribute. Category descriptions fail. `Improvement over inertia` states the measurable or observable change relative to the inertia baseline.
