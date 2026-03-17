The variate file for Round 1 already exists on disk. Here is the complete output:

---

# flow-throttle Variate — Round 1
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-10, essential/recommended/aspirational)
**Baseline ceiling:** 0 (no prior rounds)

---

## Round 1 Variation Map

| Variation | Axis | Hypothesis | Predicted composite |
|-----------|------|------------|---------------------|
| V-01 | Role sequence — risk-first discovery ordering | Starting with burst path scan (C-05) before tier inventory grounds the search in the highest-impact gap; tier enumeration then closes the gap rather than opening it | ~78/100 |
| V-02 | Output format — scorecard with per-criterion running tally | Inline pass/fail after each section forces the model to self-check C-03 and C-04 before moving on; catches elision before it accumulates | ~84/100 |
| V-03 | Phrasing register — adversarial disproof framing | Asking the model to disprove "this system is safe at this volume" inverts the default posture; C-05 and C-07 emerge from attempted disproof rather than enumeration | ~72/100 |
| V-04 | Lifecycle emphasis — numbered checklist with completion gates | Explicit checkboxes per criterion make omissions structurally visible; "mark complete" language creates completion pressure that prose phases do not | ~80/100 |
| V-05 | Combined: inertia framing + role sequence (risk-first) | Inertia story names the production incident that inertia produces; risk-first role ordering ensures the burst path and retry-after gap are found before tier enumeration closes the narrative | ~87/100 |

**Primary questions this round asks:**

Q1: Does risk-first role ordering (V-01, V-05) surface C-05 and C-06 more reliably than inventory-first ordering, or does starting from burst paths without a tier baseline cause the model to anchor on incomplete coverage?

Q2: Does the per-criterion running scorecard (V-02) catch C-03 elision in real time, or does the model fill scores optimistically before completing the numeric inventory?

Q3: Does adversarial disproof framing (V-03) outperform enumeration on C-05 and C-07 at the cost of C-03 and C-04 precision?

---

## V-01 — Role Sequence: Risk-First Discovery Ordering

**Axis:** Role sequence — roles execute in reverse of what a cautious analyst would naturally produce. Burst path scan runs first, before the tier inventory is locked. Tier enumeration then serves to close the gap the burst scan opened, rather than to initialize the analysis. Retry-after assessment runs immediately after the first bottleneck is identified, before propagation is fully traced — because fixing retry-after is the single highest-leverage intervention at the earliest point of failure.

**Hypothesis:** Inventory-first ordering creates a risk that the model exhausts its attention on enumeration and gives abbreviated treatment to C-05 and C-06 — the criteria most likely to surface actionable production gaps. By leading with the burst path scan, the model is forced to reason about what escapes throttle controls before it knows all the controls that exist. This increases the specificity of C-05 by requiring the model to search without a pre-built inventory as a safety blanket. Risk: C-03 may regress if numeric limits are not yet established when the burst scan runs. The explicit "note each numeric limit as you find it" instruction in Role 1 is the compensating mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in the signal for the given request volume.

Execute the following roles in strict order. Each role builds on the output of the prior role. Do not merge roles. Do not skip roles.

---

**ROLE 1 — BURST PATH SCAN**

Before establishing a complete tier inventory, search for paths where burst traffic can enter the system without encountering a rate limit. For each path found:
- Entry component where burst traffic enters
- Route the burst takes through the system
- Specific reason this path bypasses throttle controls (absent connector policy, trigger type exempt from queuing, endpoint that skips the gateway layer, no concurrency cap on this path)
- As you identify each component along the path, note any numeric rate limit you observe at that component. Do not leave limits as vague labels — state the number and unit.

If no unprotected path exists at this stage, state that provisional conclusion and explain what controls appear to cover every entry point.

---

**ROLE 2 — RETRY-AFTER ASSESSMENT AT FIRST FAILURE**

Identify the rate limit that fires first at the given request volume. State:
- Tier name
- Numeric limit (number + unit) that the request volume exceeds
- Whether the throttled caller receives a Retry-After header or equivalent backoff signal
- If Retry-After is absent: the failure mode that results (immediate retry storm, missing exponential backoff, silent quota drain, infinite loop)
- If Retry-After is present: the header value and whether existing caller code respects it

This role runs before full propagation is traced, because Retry-After handling at the first failure point determines whether the failure stays local or amplifies into the system.

---

**ROLE 3 — COMPLETE TIER INVENTORY**

Using everything observed in Roles 1 and 2, enumerate all throttle tiers in the system. For each tier:
- Component name
- Rate limit value (number + unit — no vague labels)
- Scope (per-user, per-connection, per-tenant, global)
- Whether this tier is reachable at the given request volume (Y / N / PARTIAL)
- Gap status: does this tier have unprotected paths (found in Role 1) or missing Retry-After handling (found in Role 2)?

Every tier must have a numeric limit. Any tier without a stated number must be marked `unresolvable` with a reason before this role is declared complete.

---

**ROLE 4 — BOTTLENECK SEQUENCING AND PROPAGATION TRACE**

Using the Role 3 tier inventory:

Part A — Identify the binding constraint: which single tier is hit first at the given request volume? State the tier name, the numeric limit exceeded, and the causal reason this tier binds before others (lower absolute cap, narrower scope, no burst headroom, shortest token window).

Part B — Trace backpressure propagation from the binding constraint outward. For each affected component:
- Component name (downstream or upstream)
- Propagation mechanism: queue fill, connection hold, retry amplification, dependency stall, or timeout cascade
- Observable effect at that component

Minimum two hops from the binding constraint.

---

**ROLE 5 — USER EXPERIENCE CATALOG**

For every tier from Role 3, state what a user or flow author observes when that tier is hit:
- HTTP status code or platform error code
- Whether failure appears in flow run history or is silently retried
- What happens if the caller ignores Retry-After and retries immediately

Every Role 3 tier must appear in this catalog. No tier may be omitted.

---

**ROLE 6 — RISK RANKING AND CASCADE SCENARIO**

Part A — Risk ranking: rank all Role 3 tiers by business risk (highest to lowest). For the top-ranked tier: blast radius (users or flows affected), failure visibility (silent vs. explicit), recovery time estimate.

Part B — Cascade scenario: trace one concrete scenario where the Role 4 binding constraint triggers failure at a second tier, which triggers failure at a third. Name each tier, the causal link at each step, and the compounded effect on throughput or error rate. Minimum three tiers. Generic cascade claims do not satisfy this section.

---

Produce output following the role order above. Do not skip roles. Do not merge roles.

---

## V-02 — Output Format: Scorecard with Per-Criterion Running Tally

**Axis:** Output format — a running scorecard is embedded in the prompt structure. After each analytical section, the model marks the rubric criteria that the section satisfies, stating pass condition and evidence. The score accumulates inline rather than appearing as a post-hoc summary.

**Hypothesis:** A running scorecard forces the model to self-evaluate coverage before moving to the next section. If a section would leave a criterion un-scored, the model must notice the gap and either backfill or explicitly defer. This catches C-03 elision (vague limits stated without numbers) immediately, at the point of production, before later sections compound the omission. The risk is that the model inflates scores optimistically — marking criteria as passed based on partial evidence. The "state the specific evidence" requirement after each mark is the compensating mechanism.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in the signal for the given request volume.

Produce the sections below in order. After each section, update the running scorecard by marking which criteria from the list below are satisfied. For each marked criterion, state the specific evidence from your output that satisfies it.

**Rubric criteria to track:**
- C-01: Bottleneck sequencing (first-hit tier named with causal reason)
- C-02: Backpressure propagation (2+ hops traced causally)
- C-03: Quantified limits (every tier has a number + unit)
- C-04: UX per tier (every tier has an observable consequence)
- C-05: Unprotected burst path (entry component + gap reason named)
- C-06: Retry-after handling (present/absent + consequence stated)
- C-07: Cascade failure scenario (3+ tiers, causal chain)
- C-08: Tier risk ranking (tiers prioritized with rationale)
- C-09: Mitigation prescriptions (specific settings/patterns per gap)
- C-10: Load shape sensitivity (uniform vs. burst at same volume)

---

**SECTION 1 — THROTTLE TIER INVENTORY**

Enumerate every throttle tier in the system. For each tier:
- Component name
- Rate limit value (number + unit — no vague labels; enter the number or mark the tier `unresolvable` and state why)
- Scope (per-user, per-connection, per-tenant, global)
- Whether this tier is reachable at the given request volume

*Scorecard update after Section 1:*
Mark any criteria from the list above that this section satisfies. For each marked criterion, quote the specific output element that provides the evidence. If C-03 is not yet fully satisfied (any tier lacks a numeric limit), note which tiers are incomplete before continuing.

---

**SECTION 2 — BOTTLENECK SEQUENCING**

Using the Section 1 inventory and the given request volume, identify the binding constraint:
- Tier name (from Section 1)
- Numeric limit exceeded
- Causal reason this tier binds before all others

*Scorecard update after Section 2:*
Mark any newly satisfied criteria. State the evidence. Note any criteria that require later sections to satisfy.

---

**SECTION 3 — BACKPRESSURE PROPAGATION**

From the Section 2 binding constraint, trace propagation outward:
- Affected component (downstream or upstream)
- Propagation mechanism: queue fill, connection hold, retry amplification, dependency stall, timeout cascade
- Observable effect at that component

Minimum two hops from the binding constraint.

*Scorecard update after Section 3:*
Mark newly satisfied criteria. State evidence. Identify any criteria still open.

---

**SECTION 4 — USER EXPERIENCE CATALOG**

For every tier from Section 1:
- Error code or platform signal the user sees
- Retry-After header: present or absent; if present, what it contains
- Whether failure appears in flow run history or is silently retried
- Effect if caller ignores Retry-After and retries immediately

No Section 1 tier may be omitted.

*Scorecard update after Section 4:*
Mark newly satisfied criteria. State evidence. C-04 requires every tier to be present here — flag any tier that appears in Section 1 but not Section 4.

---

**SECTION 5 — BURST PATH SCAN**

Scan for paths where burst traffic enters without encountering a rate limit. For each unprotected path:
- Entry component
- Route through the system
- Specific gap reason (missing connector policy, exempt trigger type, gateway bypass, no concurrency cap)

If no unprotected path exists, state the conclusion and cite the controls that cover every entry point.

*Scorecard update after Section 5:*
Mark newly satisfied criteria. State evidence.

---

**SECTION 6 — RISK RANKING, CASCADE, AND ADVANCED ANALYSIS**

Part A — Tier risk ranking: rank Section 1 tiers by business risk (highest to lowest). For the top-ranked tier: blast radius, failure visibility (silent vs. explicit), recovery time estimate.

Part B — Cascade scenario: trace one concrete scenario where the Section 2 binding constraint triggers failure at a second tier, then a third. Name each tier, the causal link, and the compounded throughput or error-rate effect. Minimum three tiers.

Part C — Mitigation prescriptions: for each gap identified (unprotected burst paths, absent Retry-After handling, cascade risk): provide a specific remediation — setting name, API parameter, or implementation pattern. Generic advice does not satisfy this section.

Part D — Load shape sensitivity: show that the same total request count produces different throttle outcomes when requests arrive uniformly vs. in bursts. Include at least one numeric comparison (e.g., "100 requests spread over 10 minutes stays under the 12 req/min cap; the same 100 requests in a 30-second burst exceeds it threefold").

*Final scorecard:*
List all ten criteria. Mark each PASS or FAIL. State the evidence for each PASS. State the gap for each FAIL.

```
C-01: [ ] Evidence:
C-02: [ ] Evidence:
C-03: [ ] Evidence:
C-04: [ ] Evidence:
C-05: [ ] Evidence:
C-06: [ ] Evidence:
C-07: [ ] Evidence:
C-08: [ ] Evidence:
C-09: [ ] Evidence:
C-10: [ ] Evidence:
```

---

## V-03 — Phrasing Register: Adversarial Disproof Framing

**Axis:** Phrasing register — the entire prompt is framed as an adversarial safety case. The model is asked to disprove the claim "this system handles the given request volume without throttle failure." Every section is a disproof attempt. The analysis succeeds when it either finds a counterexample or exhausts all possible counterexamples and must reluctantly confirm the claim.

**Hypothesis:** Most throttle analyses default to a descriptive posture — enumerate what exists, describe what happens. Adversarial disproof inverts this: the model is trying to break the system. First, it raises the stakes of C-05 (unprotected burst path) and C-07 (cascade scenario) — these are the tools the adversary uses to disprove safety. Second, it creates natural specificity pressure on C-03, because "the system is rate-limited" does not disprove the safety claim — only a specific number that the request volume exceeds can constitute evidence. Risk: C-04 (UX per tier) may regress because adversarial framing focuses on finding failures, not cataloging what users observe. The explicit "what does the user see when your attack succeeds" question compensates.

---

You are a Connectors / Power Automate throughput domain expert. Your task is to attempt to disprove the following safety claim:

> **"This system handles [REQUEST VOLUME FROM SIGNAL] requests without throttle failure, service degradation, or cascading error at any tier."**

You are the adversary. The claim is wrong until you cannot find a counterexample.

---

**ATTEMPT 1 — FIND THE BINDING RATE LIMIT**

To disprove the claim, find a rate limit that the given request volume exceeds. Enumerate all throttle tiers. For each tier that could be a counterexample, you need:
- The specific rate limit (number + unit — "limited" is not evidence; a number is)
- The scope (per-user, per-connection, per-tenant, global)
- Whether the given request volume exceeds this limit at that scope

If the request volume exceeds any limit, the safety claim fails at this tier. State which tier is the binding counterexample and why the others are not — why does this tier fail first when others do not?

---

**ATTEMPT 2 — TRACE THE FAILURE FORWARD**

If a binding rate limit exists (Attempt 1 succeeded), trace what happens after that tier throttles. For each component the throttle reaches:
- Component name (downstream or upstream)
- How the throttle reaches it: queue fill, connection hold, retry amplification, dependency stall, timeout cascade
- The observable state of that component under throttle

Trace at least two hops. Each hop is an additional element of the safety claim failure — the throttle is not contained at one tier but propagates.

If no propagation occurs (the throttle is fully contained), explain why — this strengthens the safety claim partially.

---

**ATTEMPT 3 — FIND THE UNPROTECTED PATH**

Is there a path through the system where burst traffic can arrive and not hit any rate limit? This is the strongest disproof: a failure mode the system has no defense against.

For each unprotected path found:
- Entry component (where burst traffic enters unimpeded)
- Route the burst takes (the path that bypasses throttle controls)
- The specific reason no throttle applies (no connector policy, trigger type exempt from queuing, endpoint that bypasses the gateway layer, no concurrency cap on this route)
- What happens to the system when this path receives burst traffic

If no unprotected path exists, state what controls cover every entry point. This is not a concession — it is the evidence that defeats this disproof attempt.

---

**ATTEMPT 4 — TRIGGER A CASCADE**

Is there a scenario where throttling at the Attempt 1 binding tier triggers throttling at a second tier, which triggers throttling at a third? A cascade makes the safety claim fail in a compounding way. Trace the scenario:
- Tier 1 (the binding constraint from Attempt 1): what it throttles and when
- Causal link to Tier 2: why throttling at Tier 1 triggers a failure at Tier 2
- Causal link to Tier 3: why the Tier 2 failure triggers a failure at Tier 3
- Compounded effect on throughput or error rate

Minimum three tiers in the cascade. Generic cascade claims ("it could cascade") are not evidence and do not constitute a disproof.

---

**ATTEMPT 5 — EXPLOIT THE RETRY-AFTER GAP**

Does the throttled caller at the Attempt 1 binding tier handle Retry-After correctly? If Retry-After is absent or ignored, a second disproof is available: the caller's retry behavior amplifies the original throttle failure into a sustained storm that consumes quota across the tenant or connection.

State:
- Whether Retry-After is present at the binding tier
- If absent: the failure mode the caller produces (immediate retry storm, missing exponential backoff, silent infinite loop)
- If present: whether caller code respects it, and what happens if it does not

What does the user or flow author see when this failure mode fires? What error code, what delay, what visibility in run history?

---

**VERDICT**

Based on the five disproof attempts, state the verdict:

*Claim fails* if any of the following hold:
- A binding rate limit was found that the request volume exceeds (Attempt 1)
- An unprotected burst path exists with no throttle defense (Attempt 3)
- A cascade scenario of 3+ tiers was traced (Attempt 4)

*Claim holds* only if all five attempts found no valid counterexample. State this explicitly if so.

Then rank the identified failures by blast radius — which failure mode is most impactful, most likely to surface in production, and hardest to recover from once it fires?

---

## V-04 — Lifecycle Emphasis: Numbered Checklist with Completion Gates

**Axis:** Lifecycle emphasis — the prompt is structured as an explicit checklist of criteria-mapped tasks. Each task has a checkbox placeholder, a completion condition, and a gate before the next task opens. The model must mark each item complete (with evidence) before proceeding. The checklist is criterion-aware: each item names the rubric criterion it satisfies.

**Hypothesis:** Phase-gated prompts create structure but do not create criterion awareness — the model knows the phases but not which rubric criteria each phase satisfies. Making the criterion mapping explicit (each checklist item says "this satisfies C-03") creates a different kind of completeness pressure: the model can see which criteria will remain unmarked if it skips a task. Completion pressure from checkbox framing may reduce the rate at which the model silently elides items under token pressure. Risk: the model may mark items complete based on partial completion if the evidence standard is not stated.

---

You are a Connectors / Power Automate throughput domain expert. Complete the checklist below. Mark each item `[DONE]` when its completion condition is satisfied. State the evidence for each `[DONE]` mark. Do not mark an item done if the condition is not fully met — defer it and note what is missing.

---

**CHECKLIST — flow-throttle analysis**

---

`[ ]` **TASK 1 — Throttle tier inventory** *(satisfies C-03)*

Enumerate every throttle tier in the system. For each tier:
- Component name
- Rate limit value (number + unit — required; mark tier `unresolvable` if the number cannot be stated, and give the reason)
- Scope (per-user, per-connection, per-tenant, global)
- Whether this tier is reachable at the given request volume

**Completion condition:** Every tier has a numeric rate limit OR is marked `unresolvable` with a stated reason. No tier has a vague label ("limited", "throttled") in place of a number.

Mark `[DONE]` and state evidence before proceeding to Task 2.

---

`[ ]` **TASK 2 — Binding constraint identification** *(satisfies C-01)*

Using the Task 1 inventory and the given request volume, identify which single tier is hit first:
- Tier name (from Task 1)
- Numeric limit exceeded
- Causal reason this tier binds before others (lower absolute cap, narrower scope, no burst headroom, shortest window)

**Completion condition:** A single tier is named as the binding constraint with a causal reason grounded in the Task 1 data.

Mark `[DONE]` and state evidence before proceeding to Task 3.

---

`[ ]` **TASK 3 — Backpressure propagation trace** *(satisfies C-02)*

From the Task 2 binding constraint, trace propagation outward. For each hop:
- Affected component (downstream or upstream)
- Propagation mechanism: queue fill, connection hold, retry amplification, dependency stall, timeout cascade
- Observable effect at that component

**Completion condition:** At least two hops are traced from the binding constraint, each with a named mechanism and an observable effect.

Mark `[DONE]` and state evidence before proceeding to Task 4.

---

`[ ]` **TASK 4 — User experience catalog** *(satisfies C-04 and C-06)*

For every tier from Task 1:
- Error code or platform signal the user sees
- Retry-After header: present or absent; if present, the header value
- Whether failure appears in flow run history or is silently retried
- Effect if caller ignores Retry-After and retries immediately

**Completion condition (C-04):** Every Task 1 tier has a row in this catalog. No tier may be omitted. If a tier produces no user-visible signal, state that explicitly.

**Completion condition (C-06):** The binding constraint tier from Task 2 has an explicit Retry-After assessment: present/absent, and the consequence of absence or mishandling stated.

Mark `[DONE]` for each satisfied criterion and state evidence before proceeding to Task 5.

---

`[ ]` **TASK 5 — Unprotected burst path scan** *(satisfies C-05)*

Scan for paths where burst traffic enters the system without encountering a rate limit. For each unprotected path found:
- Entry component
- Route through the system
- Specific gap reason (missing connector policy, exempt trigger type, gateway bypass, no concurrency cap)

If no unprotected path exists: state the conclusion and cite the specific controls at every entry point.

**Completion condition:** At least one specific path is named and analyzed, OR a conclusion that no path exists is supported by named controls at every entry point.

Mark `[DONE]` and state evidence before proceeding to Task 6.

---

`[ ]` **TASK 6 — Risk ranking** *(satisfies C-08)*

Rank all Task 1 tiers by business risk, highest to lowest. For the top-ranked tier: blast radius (users or flows affected), failure visibility (silent vs. explicit), recovery time estimate. One sentence of rationale per remaining tier.

**Completion condition:** All Task 1 tiers appear in the ranking with stated rationale.

Mark `[DONE]` and state evidence before proceeding to Task 7.

---

`[ ]` **TASK 7 — Cascade scenario** *(satisfies C-07)*

Trace one concrete scenario where the Task 2 binding constraint triggers failure at a second tier, which triggers failure at a third. For each step: tier name, causal link, compounded effect on throughput or error rate.

**Completion condition:** Three or more tiers appear in the cascade, with explicit causal links at each step. Generic claims ("could cascade") do not satisfy this task.

Mark `[DONE]` and state evidence.

---

**COMPLETION SUMMARY**

After all tasks are marked:

```
TASK 1 (C-03): [ ] Evidence:
TASK 2 (C-01): [ ] Evidence:
TASK 3 (C-02): [ ] Evidence:
TASK 4 (C-04): [ ] Evidence:
TASK 4 (C-06): [ ] Evidence:
TASK 5 (C-05): [ ] Evidence:
TASK 6 (C-08): [ ] Evidence:
TASK 7 (C-07): [ ] Evidence:
```

If any task was deferred or incomplete, state what is missing and why it was not satisfiable from the signal.

---

## V-05 — Combined: Inertia Framing + Risk-First Role Sequence

**Axis:** Inertia framing (the specific production incident that inertia produces is named upfront) combined with risk-first role ordering (burst path and Retry-After gap are discovered before the tier inventory is finalized, motivated by the named incident).

**Hypothesis:** V-01 tested risk-first ordering without motivational context; V-05 adds the inertia story as a frame that makes the risk-first search feel urgent rather than arbitrary. Teams that skip throttle analysis reason from "it worked in staging" — and the most dangerous gaps they leave behind are exactly what risk-first ordering prioritizes: the unprotected burst path that staging never triggered, and the missing Retry-After handler that staged load never stressed. Naming these specific gaps in the inertia story before the analysis begins should increase specificity in C-05 and C-06 (the model is searching for the exact failure the story named) while the risk-first structure prevents the model from burying those criteria under a large tier inventory.

The combination tests whether inertia framing amplifies the C-05/C-06 gains of risk-first ordering beyond what either achieves alone.

---

**THE PRODUCTION INCIDENT THAT INERTIA PRODUCES**

Here is the most common throttle failure path in production systems:

> A team validates their flow at development volumes. Everything works. They ship to production. At 3x staging volume, a connector fires its per-connection rate limit. The caller has no Retry-After handler — it retries immediately, exhausting the connection quota within 90 seconds. The platform silently drops subsequent calls. The flow appears to succeed in run history. Users see stale data or missing records. Three dependent flows stall waiting for the connection to recover. The team discovers the failure during an incident review, not from monitoring.

Two gaps made this incident possible:
1. An unprotected burst path that staging volumes never stressed — it looked fine until production volume arrived.
2. A missing Retry-After handler that turned a temporary throttle into sustained quota exhaustion and silent data loss.

The analysis below finds these gaps before production does.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described in the signal for the given request volume.

The inertia story above names two specific gaps: the unprotected burst path and the missing Retry-After handler. Start by looking for those gaps. Then build the full inventory that closes the picture.

Execute the following roles in order. Do not merge roles.

---

**ROLE 1 — BURST PATH SEARCH**

*(Find the unprotected path that staging never triggered.)*

Before the full tier inventory is built, search for paths where burst traffic can enter the system without encountering a rate limit. For each path found:
- Entry component (where burst arrives unimpeded)
- Route through the system (the path that bypasses throttle controls)
- Specific gap reason: missing connector policy, trigger type exempt from queuing, endpoint that bypasses the gateway, no concurrency cap on this path
- As you identify each component on this path, note any numeric rate limit you observe. Do not leave limits as vague labels.

If no unprotected path exists at this stage, state that provisional conclusion and what controls appear to cover every entry point.

---

**ROLE 2 — RETRY-AFTER HANDLER ASSESSMENT**

*(Find the missing handler that turns a temporary throttle into quota exhaustion.)*

Identify the rate limit that fires first at the given request volume. State:
- Tier name
- Numeric limit (number + unit) that the request volume exceeds
- Whether the throttled caller receives a Retry-After header or equivalent backoff signal
- If Retry-After is absent: the failure mode (immediate retry storm, missing exponential backoff, silent quota drain, infinite loop) and the first observable symptom when it fires
- If Retry-After is present: the header value and whether existing caller code respects it, and what happens if it does not

This is the gap that made the incident story possible. Confirm whether it exists here or explain why it does not.

---

**ROLE 3 — COMPLETE TIER INVENTORY**

*(Build the full inventory that closes the picture.)*

Using everything observed in Roles 1 and 2, enumerate all throttle tiers in the system. For each tier:
- Component name
- Rate limit value (number + unit — required; mark tier `unresolvable` if the number cannot be stated)
- Scope (per-user, per-connection, per-tenant, global)
- Whether this tier is reachable at the given request volume (Y / N / PARTIAL)
- Gap status: does this tier have unprotected paths (Role 1) or missing Retry-After handling (Role 2)?

Every tier must have a numeric limit or an explicit `unresolvable` designation.

---

**ROLE 4 — BOTTLENECK SEQUENCING AND BACKPRESSURE TRACE**

Using the Role 3 inventory:

Part A — Binding constraint: which single tier fires first at the given request volume? State the tier name, the numeric limit exceeded, and the causal reason this tier binds before others.

Part B — Propagation trace: from the binding constraint, trace backpressure outward. For each affected component:
- Component name (downstream or upstream)
- Propagation mechanism: queue fill, connection hold, retry amplification, dependency stall, timeout cascade
- Observable effect at that component

Minimum two hops from the binding constraint.

---

**ROLE 5 — USER EXPERIENCE CATALOG**

For every tier from Role 3:
- Error code or platform signal the user sees
- Whether failure is visible in flow run history or silently retried
- Effect if caller ignores Retry-After and retries immediately

Every Role 3 tier must appear here. No tier may be omitted.

---

**ROLE 6 — RISK RANKING, CASCADE, AND INERTIA EXPOSURE**

Part A — Tier risk ranking: rank all Role 3 tiers by business risk (highest to lowest). For the top-ranked tier: blast radius (users or flows affected), failure visibility (silent vs. explicit), recovery time estimate.

Part B — Cascade scenario: trace one concrete scenario where the Role 4 binding constraint triggers failure at a second tier, then a third. Name each tier, the causal link, and the compounded throughput or error-rate effect. Minimum three tiers.

Part C — Inertia exposure summary: name the specific gaps in this system that a team testing at staging volumes would not have discovered. For each gap, state:
- What the staging test did not exercise
- What production traffic exposes
- The first observable symptom when it fires

This section exists because the incident story above is the delivery mechanism for throttle failures in production — not an edge case, but the default failure path when analysis is skipped.

---

Produce output following the role order above. Do not skip roles. Do not merge roles.

---

**Written to:** `simulations/quest/golden/flow-throttle-variate-R1-2026-03-15.md`

**Summary of variation axes used:**
- **V-01**: Role sequence (risk-first — burst scan before tier inventory)
- **V-02**: Output format (inline running scorecard per section)
- **V-03**: Phrasing register (adversarial disproof — model as attacker)
- **V-04**: Lifecycle emphasis (numbered checklist with criterion-mapped completion gates)
- **V-05**: Combined — inertia framing + V-01 risk-first role sequence

**Predicted winner:** V-05 (~87) — inertia framing gives the risk-first search a motivational anchor. V-02 (~84) is the safer bet on C-03 compliance. V-03 (~72) is the experimental bet — likely loses on C-04 coverage but may dominate on C-05/C-07 specificity.
