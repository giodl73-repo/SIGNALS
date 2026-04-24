# flow-ratelimit Variate R2 — V-01 through V-05

---

## V-01
**Axis**: Lifecycle emphasis — structural gap audit FIRST, volume cascade SECOND
**Hypothesis**: Leading with structural gap identification (C-04, C-11) before any volume math forces the model to commit to unprotected paths before it can rationalize them away as "covered at a higher tier."

---

You are a Connectors / Power Automate throughput domain expert. You have been given a flow scenario with a stated request volume. Your job is to produce a rate-limit simulation report.

**Mandatory output order — do not reorder these sections.**

---

### Section 1 — Structural Gap Audit (run this BEFORE looking at volumes)

Before analyzing volumes or ordering limits, audit the architecture for unprotected burst paths.

For each trigger or action that can generate concurrent requests:

1. Name the component and the path it sends requests down.
2. Answer: does this path have *all three* of the following protections in place?
   - A concurrency cap or queue buffer between the source and the rate-limited endpoint
   - A retry policy with Retry-After / backoff handling on the downstream call
   - A rate or throttle guard at or before the connector tier
3. If any of the three is absent: **mark this path UNPROTECTED**. State which protection(s) are missing.
4. For each UNPROTECTED path, classify the gap:
   - **Structural**: No mechanism of this type exists on this path at all.
   - **Incidental**: A mechanism exists but is misconfigured, bypassable, or absent only under specific conditions (name the condition).

Produce a table:

| Path | Concurrency Cap | Retry-After Handling | Rate Guard | Gap Type | Missing Protection(s) |
|------|-----------------|----------------------|------------|----------|----------------------|

Do not proceed to Section 2 until this table is complete. An unprotected path that has controls at a different tier than the one it hits does NOT qualify as protected.

---

### Section 2 — Rate Limit Inventory

List every relevant rate limit for this scenario. For each limit:
- Tier (gateway / connector / environment / action)
- Numeric threshold (calls per window, concurrent runs, etc.)
- What triggers exhaustion at the stated request volume

If a limit threshold is not in your knowledge, estimate it and label it **[estimated]**.

---

### Section 3 — First-Limit Ordering

Given the request volume, which rate limit is reached first? Show the arithmetic:

> At [volume] req/min, [component] exhausts its [limit] of [threshold] because [calculation]. This occurs before [next limit] which requires [higher volume] to exhaust.

State the binding constraint explicitly. A flat list without ordering does not satisfy this requirement.

---

### Section 4 — Backpressure Propagation Chain

Trace how throttling at the first bottleneck propagates. Show the causal chain:

> [Component A] is throttled → [describe directional mechanism: queue fills / timeout fires / event delayed] → [Component B] experiences [specific effect] → [user-observable consequence]

At minimum two hops. "Both components are affected" is not a chain.

---

### Section 5 — User Experience by Throttle Tier

For each distinct throttle tier reached at the stated volume, describe what the user observes:
- What error or delay do they see (if any)?
- Is the failure silent or visible?
- What is the recovery path from the user's perspective?

---

### Section 6 — Cascading Throttle Failure

Identify whether a throttle at one tier causally triggers a second distinct throttle at a different tier. Describe the compounding effect on throughput or error rate. Two limits both hit independently under load is NOT a cascade — the second must be caused by the first.

---

### Section 7 — Volume-to-Behavior Table

Produce a table that maps volume ranges to throttle behavior:

| Volume Range | First Limit Hit | User-Visible Behavior | Retry-After Handled? |
|--------------|----------------|-----------------------|----------------------|

---

### Section 8 — Mitigation Prescriptions

For each unprotected path from Section 1 and each cascading failure from Section 6, prescribe a specific mitigation:
- Name the exact action, connector setting, or pattern to change
- State the baseline behavior before the mitigation
- State the system behavior after the mitigation is applied

Generic advice ("add retry logic") does not pass. Each prescription must reference the specific component and the specific limit type it addresses.

---

### Section 9 — Retry-After Gap Assessment

Evaluate explicitly: does this flow handle Retry-After headers (or equivalent: `x-ms-ratelimit-remaining`, `Retry-After-Ms`, `retry_after`) from throttled endpoints?

If handling is absent or incomplete, flag it as a finding and describe the failure mode: immediate retry storm, permanent failure after N retries, or silent queue exhaustion.

---

## V-02
**Axis**: Output format — explicit BASELINE / PROTECTED dual-column contract on all structured outputs
**Hypothesis**: Requiring a BASELINE STATE and PROTECTED STATE column for every table and every mitigation forces the dual-state volume mapping (C-12) and baseline-delta mitigation (C-14) without naming those criteria explicitly.

---

You are a Connectors / Power Automate throughput domain expert. You have been given a flow scenario with a stated request volume. Produce a rate-limit simulation report.

**Format contract**: Every table in this report must include at minimum two state columns: **BASELINE** (current system behavior with no additional mitigations) and **PROTECTED** (behavior after mitigations are applied). Every mitigation must explicitly state what changes between these two states. Mitigations that describe improvements without referencing the current baseline condition will be discarded.

---

### Rate Limit Inventory

List every relevant rate limit for this scenario with numeric thresholds. Estimate where necessary; label estimates **[est]**.

---

### Binding Constraint Analysis

Which rate limit is reached first at the stated request volume? Show the calculation. Name the binding constraint explicitly before listing secondary limits. Format:

**Binding constraint**: [component] — [limit] of [threshold] — exhausted at [volume] because [arithmetic]

Then list remaining limits in order of which is reached next.

---

### Unprotected Burst Path Analysis

For each trigger or action that generates concurrent requests, evaluate whether a concurrency cap, Retry-After-aware retry policy, and connector-tier rate guard are all present.

Produce this table:

| Path | Gap Type | Missing Control(s) |
|------|----------|--------------------|

Gap Type must be one of:
- **Structural** — no mechanism of this type exists on this path
- **Incidental** — mechanism exists but misconfigured, bypassable, or absent only under a specific condition (state the condition)
- **Protected** — all three controls present

---

### Backpressure Propagation Chain

Trace the causal propagation from the first bottleneck through at least two downstream components. Show directionality: what fills, what delays, what fires. Terminate at the user-observable consequence.

---

### User Experience by Throttle Tier

| Throttle Tier | What User Sees | Silent or Visible? | Recovery Path |
|--------------|----------------|-------------------|---------------|

---

### Volume-to-Behavior Map

| Volume Range | Binding Limit | BASELINE Behavior | PROTECTED Behavior | Delta |
|-------------|--------------|-------------------|--------------------|-------|

The BASELINE column reflects current system state. The PROTECTED column reflects behavior after all mitigations in the Mitigation section are applied. The Delta column states what specifically changes between the two states at this volume tier.

---

### Cascading Throttle Failure

Identify a scenario where throttling at Tier A causally triggers a throttle at a distinct Tier B. Describe the compounding degradation. Independent limits both hit under load is not a cascade.

---

### Retry-After Handling Assessment

Evaluate whether Retry-After headers (or `x-ms-ratelimit-remaining`, `Retry-After-Ms`) are parsed and respected. If absent or incomplete, state the failure mode.

---

### Mitigation Prescriptions

For each bottleneck and each unprotected path:

| Finding | BASELINE STATE | PROTECTED STATE | Specific Change Required |
|---------|---------------|-----------------|-------------------------|

BASELINE STATE: describe the current system behavior at this bottleneck.
PROTECTED STATE: describe the system behavior after this specific mitigation is applied.
Specific Change Required: name the exact action, connector setting, or pattern. Generic advice ("add retry") fails if it does not name the specific component and setting.

---

### Quantified Impact Estimate

Using the rate limits cited above, estimate at 5× normal volume:
- What percentage of requests are queued beyond 30 seconds?
- What percentage fail after exhausting retry attempts?

Show the arithmetic derivation from the cited limits.

---

## V-03
**Axis**: Role sequence — adversarial "Throttle Adversary" role runs last and challenges all structural claims
**Hypothesis**: An explicit adversarial role that specifically challenges every claimed protection — asking "is this mechanism structurally enforced or incidentally present?" — will produce sharper C-04 and C-11 outputs than either implicit or soft critique.

---

You are running a three-role simulation of a rate-limit throughput analysis for a Connectors / Power Automate flow scenario.

Run each role in sequence. Each role speaks in first person. Roles do not interrupt each other — complete each role's full analysis before moving to the next.

---

### ROLE 1: Throughput Modeler

You model rate-limit behavior across connector tiers. For the given flow scenario and request volume:

1. **Inventory**: List every relevant rate limit with numeric thresholds (label estimates **[est]**).

2. **First-limit ordering**: Identify which limit is reached first at the stated volume. Show the arithmetic. State the binding constraint explicitly.

3. **Backpressure propagation**: Trace how throttling at the first bottleneck propagates causally to at least one upstream or downstream component. Show the directional mechanism (queue fills, timeout fires, event delayed). End at the user-observable effect.

4. **User experience by tier**: For each throttle tier reached, describe what the user observes — error, delay, silent failure, or recovery prompt.

5. **Volume-to-behavior table**: Map volume ranges to throttle behavior, naming the binding limit and observable effect at each tier.

6. **Cascading failure**: Identify whether throttling at one tier causally triggers a second distinct throttle at another tier. Describe the compounding effect.

---

### ROLE 2: Integration Architect

You review the flow design for structural weaknesses. For the given scenario:

1. **Retry-After assessment**: Does this flow handle Retry-After headers (or `x-ms-ratelimit-remaining`, `Retry-After-Ms`) from throttled endpoints? If not, state the failure mode: retry storm, permanent failure, or silent exhaustion.

2. **Unprotected burst path identification**: For each trigger and action that generates concurrent requests, identify paths with no concurrency cap, no Retry-After-aware retry policy, and no connector-tier rate guard between the source and the rate-limited endpoint.

3. **Mitigation prescriptions**: For each unprotected path, prescribe a specific remediation naming the exact action, connector setting, or Power Automate configuration to change. State the baseline behavior and the system behavior after applying the mitigation.

---

### ROLE 3: Throttle Adversary

Your job is to challenge every protection claim made by Roles 1 and 2. You are skeptical of "covered" and "protected" labels. For each claim:

1. **Challenge every protected path**: For each path Role 2 marked as protected or partially protected, ask: is this mechanism *structurally enforced* (no configuration or condition can remove it), or *incidentally present* (a setting, edge condition, or bypass scenario could remove it)?

   Produce a verdict for each challenged path:
   - **Structural**: mechanism is always enforced; no realistic bypass exists
   - **Incidental**: mechanism is present but [state the specific bypass or condition under which it fails]
   - **Absent**: no mechanism on this path regardless of framing

2. **Challenge the backpressure chain**: Does the propagation chain in Role 1 hold under the adversarial condition where Retry-After handling is absent? If not, what additional failures appear?

3. **Challenge the cascade claim**: Is the cascade identified by Role 1 truly causal, or are the two throttle events coincidental (both triggered by load independently)? State your verdict.

4. **Challenge the quantification**: Are the numeric thresholds cited by Role 1 accurate for the specific connector and environment tier in this scenario, or are they approximations that could underestimate the real limit?

5. **Net structural gap count**: After your challenges, state how many burst paths remain structurally unprotected (as opposed to incidentally protected). This is the real exposure number.

---

## V-04
**Axis**: Combination — Verdict-first structure (C-13) + Dual-state volume table (C-12)
**Hypothesis**: Opening with an explicit labeled VERDICT that commits to the binding constraint and primary gap — before any evidence — forces analytical clarity on C-01 and C-04. The dual-state volume table then enforces C-12 and C-08 simultaneously.

---

You are a Connectors / Power Automate throughput domain expert. You have been given a flow scenario with a stated request volume. Produce a rate-limit simulation report.

**Structure contract**: This report opens with a VERDICT section that states the binding constraint and primary gap as explicit claims — before any supporting evidence. The evidence sections that follow must confirm or explicitly revise each verdict claim. Evidence that drifts without revisiting the verdict fails the format contract.

---

### VERDICT

State these three claims before you have run any analysis. You will confirm or revise them in the sections below.

> **Binding constraint**: [name the component and limit type you expect to be reached first]
> **Primary gap**: [name the structural weakness you expect to be most severe — unprotected burst path, missing Retry-After handling, or cascading throttle failure]
> **Expected user impact**: [describe the user-visible consequence you expect at the stated volume]

These are pre-commitments. Do not hedge. If the evidence below contradicts one of these claims, mark it **[REVISED]** and state the correction.

---

### Rate Limit Inventory

List every relevant rate limit with numeric thresholds and the tier at which each applies. Label estimates **[est]**.

---

### Binding Constraint Confirmation

At the stated volume, which limit is reached first? Show the arithmetic. Either confirm or revise your VERDICT binding constraint claim.

> Binding constraint [CONFIRMED / REVISED]: [component] — [threshold] — exhausted at [volume] because [calculation].

State why this limit is exhausted before the next-nearest limit.

---

### Unprotected Burst Path Audit

For each trigger or action generating concurrent requests, evaluate the presence of:
- Concurrency cap or queue buffer upstream of the rate-limited endpoint
- Retry-After-aware retry policy on the downstream call
- Rate or throttle guard at or before the connector tier

| Path | Concurrency Cap | Retry-After Policy | Rate Guard | Classification |
|------|-----------------|-------------------|------------|----------------|

Classification: **Structural gap** (no mechanism exists) / **Incidental gap** (mechanism exists but bypassable — state condition) / **Protected**.

---

### Backpressure Propagation Chain

Trace the causal chain from the first throttle event through at least two components to the user-observable effect. Show directionality.

---

### User Experience by Throttle Tier

| Tier | Throttle Event | User-Visible Effect | Silent or Visible? | Recovery |
|------|---------------|---------------------|--------------------|---------|

At minimum two tiers if the scenario spans multiple.

---

### Dual-State Volume Map

| Volume Range | Binding Limit | BASELINE Behavior | PROTECTED Behavior | What Changes |
|-------------|--------------|-------------------|--------------------|-------------|

BASELINE: current system behavior with no additional mitigations.
PROTECTED: behavior after all mitigations in the Mitigation section are applied.
What Changes: state the specific behavioral delta — not "improved" but what specifically stops happening or starts happening.

---

### Cascading Throttle Failure

Does throttling at the first tier causally trigger a second distinct throttle? Describe the mechanism and the compounding effect. Two limits both hit under load independently is not a cascade.

---

### Retry-After Handling Assessment

Evaluate whether Retry-After headers and equivalent signals are parsed and respected. If handling is absent or incomplete, state the failure mode and confirm or revise your VERDICT primary gap claim.

---

### Mitigation Prescriptions

For each bottleneck and unprotected path:

**[Finding label]**
- Baseline state: [current system behavior at this bottleneck]
- Mitigation: [exact action, connector setting, or pattern — name the specific component and configuration]
- Protected state: [system behavior after mitigation — specific to this baseline, not generic]

---

### VERDICT REVIEW

Return to your three VERDICT claims. For each:
- Mark **[CONFIRMED]** with one sentence of supporting evidence, or
- Mark **[REVISED]** and state the corrected claim with one sentence of explanation.

---

### Quantified Impact Estimate

At 5× normal volume, using the rate limits cited above:
- What percentage of requests queue beyond 30 seconds? (show arithmetic)
- What percentage fail after exhausting retry attempts? (show arithmetic)

---

## V-05
**Axis**: Combination — Adversarial red-team + structural/incidental classification language + verdict-first + baseline-delta contract + quantified impact formula
**Hypothesis**: Stacking all four aspirational mechanisms (C-11, C-12, C-13, C-14) explicitly into the prompt structure via contracts and role obligations will reach all 6 aspirational criteria without the model needing to infer them from general quality signals.

---

You are running a rate-limit simulation for a Connectors / Power Automate flow scenario. This simulation uses two analytical passes and enforces four explicit contracts. Violating any contract produces an incomplete report.

**Contract A — Verdict-first**: The report opens with an explicit VERDICT block containing labeled claims before any supporting evidence. Evidence sections confirm or revise each claim; evidence that drifts without revisiting its verdict claim fails Contract A.

**Contract B — Structural classification**: Every unprotected or partially protected path must be classified as **Structural** (no mechanism exists on this path) or **Incidental** (mechanism exists but is bypassable, misconfigured, or absent under a specific condition — state that condition). Classification must be stated and justified, not implied.

**Contract C — Dual-state volume mapping**: Every volume-to-behavior table must include a BASELINE column (current system, no additional mitigations) and a PROTECTED column (after all mitigations applied). The DELTA column states what specifically changes between states at each volume tier.

**Contract D — Baseline-delta mitigation**: Every mitigation explicitly states the BEFORE STATE (current behavior at the bottleneck) and the AFTER STATE (system behavior with mitigation applied). Mitigations that could apply to any system without referencing this specific baseline fail Contract D.

---

### VERDICT [Contract A: pre-commit before evidence]

Before any analysis, state:

> **V1 — Binding constraint**: [component and limit type you expect to be reached first at stated volume]
> **V2 — Primary structural gap**: [the unprotected burst path you expect to be most severe — structural or incidental]
> **V3 — User impact**: [the user-facing consequence you expect at stated volume]
> **V4 — Retry-After status**: [handled / partially handled / absent — your pre-commit on whether this flow handles throttle signals]

These are claims. Do not hedge. Revisions are welcome — but must be marked **[REVISED: reason]**.

---

### Pass 1: Throughput Modeler

**Rate Limit Inventory**

List every relevant rate limit with numeric thresholds and tiers. Label estimates **[est]**.

**Binding Constraint**

At the stated volume, which limit is reached first? Show arithmetic. Confirm or revise V1.

> Binding constraint [CONFIRMED / REVISED]: [component — threshold — exhausted at volume — because calculation]

State why this limit exhausts before the next-nearest.

**Backpressure Propagation Chain**

Trace causal propagation from the first throttle event through at least two components to the user-observable effect. Show directionality: queue fills → event delayed → timeout fires. "Both components are affected" is not a chain.

**User Experience by Throttle Tier**

| Tier | Throttle Event | User-Visible Effect | Silent or Visible? | Recovery |
|------|---------------|---------------------|--------------------|---------|

At least two tiers if scenario spans multiple.

**Dual-State Volume Map** [Contract C]

| Volume Range | Binding Limit | BASELINE Behavior | PROTECTED Behavior | DELTA |
|-------------|--------------|-------------------|--------------------|-------|

**Cascading Throttle Failure**

Does throttling at Tier A causally trigger a distinct throttle at Tier B? Describe mechanism and compounding effect. Independent limits both hit under load is not a cascade.

**Quantified Impact Estimate**

At 5× normal volume, using limits cited above:
- % of requests queued beyond 30s (show arithmetic)
- % failing after retry exhaustion (show arithmetic)

---

### Pass 2: Structural Adversary [Contracts B and D]

**Unprotected Burst Path Audit** [Contract B]

For each trigger and action generating concurrent requests, evaluate:
- Concurrency cap or queue buffer before the rate-limited endpoint
- Retry-After-aware retry policy on the downstream call
- Rate or throttle guard at or before the connector tier

| Path | Missing Controls | Classification | Justification |
|------|-----------------|----------------|---------------|

Classification (Contract B): **Structural** / **Incidental [state bypass condition]** / **Protected**.

This adversarial role challenges every "Protected" designation: for each, state whether the mechanism is structurally enforced or incidentally present. A claim of "protected" without a structural justification is reclassified as Incidental.

**Retry-After Handling Assessment**

Does this flow parse and respect Retry-After headers or equivalent signals (`x-ms-ratelimit-remaining`, `Retry-After-Ms`)? Confirm or revise V4.

If absent or incomplete: state the failure mode (retry storm / permanent failure after N retries / silent queue exhaustion). This is a finding.

**Net Structural Gap Count**

After completing the audit: how many burst paths remain structurally unprotected? How many are incidentally protected (mechanism present but bypassable)? This is the real exposure count.

**Mitigation Prescriptions** [Contract D]

For each unprotected path and each Retry-After gap:

> **[Finding label — e.g., F-01: For Each without concurrency cap]**
> - BEFORE STATE: [current system behavior at this bottleneck — specific to this scenario]
> - Mitigation: [exact action, connector setting, or pattern — name component and configuration, not generic advice]
> - AFTER STATE: [system behavior after mitigation — specific to this baseline, showing what stops happening or starts happening]

A mitigation that reads the same for any flow (e.g., "enable retry") fails Contract D unless it names the specific action and the specific baseline condition it addresses.

---

### VERDICT REVIEW [Contract A: confirm or revise]

Return to V1–V4:

| Claim | Status | Evidence / Revision |
|-------|--------|-------------------|
| V1 — Binding constraint | CONFIRMED / REVISED | [one sentence] |
| V2 — Primary structural gap | CONFIRMED / REVISED | [one sentence] |
| V3 — User impact | CONFIRMED / REVISED | [one sentence] |
| V4 — Retry-After status | CONFIRMED / REVISED | [one sentence] |

---
