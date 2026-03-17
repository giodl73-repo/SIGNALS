---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 3
rubric_version: 3
---

# flow-ratelimit — Variate R3

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence), V-02 (output format), V-03 (lifecycle emphasis).
Combination variations: V-04 (phrasing register + commit-first imperative), V-05 (inertia framing + dual-state contract).

**R3 target gaps from R2 scorecard:**
- C-10 (Quantified Impact): V-01 PARTIAL, V-02 FAIL — no arithmetic mandate in prompt
- C-12 (Dual-state Volume): V-01 FAIL — no BASELINE/PROTECTED split in volume table
- C-13 (Verdict-before-Evidence): V-01 PARTIAL, V-02 PARTIAL — verdict mid-document in both
- C-15 (Document-head Global Verdict): NEW — would fail both R2 variations
- C-16 (Format Contract Preamble): NEW — V-02 had the concept but no formal rejection clause or 2-table requirement

All five R3 variations target all four gaps. Variation axes determine HOW each gap is closed.

---

## V-01

**Variation axis:** Role sequence — Bottleneck Auditor runs as a gating Role 1 whose sole deliverable is the Verdict block; a Format Contract Writer runs as Role 2; all analysis roles are blocked until both preamble roles complete.
**Hypothesis:** Sequential role gating at document head enforces C-15 structurally — no analysis role can begin until Role 1 (Verdict) and Role 2 (Format Contract) are written. This avoids the mid-document verdict placement that caused PARTIAL on C-13 in both R2 variations, because the model cannot "start the structural audit" (Role 3) without having completed the Verdict role first. C-10 arithmetic is mandated inside Role 5 (Throughput Analyst), which already has the numeric thresholds from Role 3 in scope.

---

You are executing a multi-role throughput simulation of a rate-limited Power Automate / Connectors system. Roles execute in strict sequence. **Each role's output section must appear in the document before the next role begins.** Do not write Role 2 output until Role 1 is complete.

---

**ROLE 1 — BOTTLENECK AUDITOR**
*Sole deliverable: VERDICT block. Do not produce any table, list, or analysis section until this block is written and all three fields are non-empty.*

Write a VERDICT block with exactly these three labeled fields:

```
## VERDICT

**Binding Constraint**: [Component Name] — [N req/min or req/sec per scope] — exhausted at [X req/min] nominal load because [one causal sentence naming why this component's limit is reached before all others].

**Primary Gap**: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] — [specific action or connector name]: [one sentence on the structural control absent on this path — not at a higher tier, absent here].

**System Status at Stated Load**: [SAFE | DEGRADED | FAILING] — [one sentence justifying the classification].
```

Rules:
- Binding Constraint must contain a number and unit. "Limited throughput" in the limit field fails.
- Primary Gap must name the specific action or connector. "The flow lacks retry logic" without a location fails.
- System Status must be exactly one of: SAFE / DEGRADED / FAILING.
- This block must be self-contained: a reader who reads only the VERDICT must know the core finding without reading any subsequent section.

**Do not begin Role 2 until all three labeled fields are written.**

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Sole deliverable: Format Contract section. No comparative tables may appear before this section. Only the VERDICT block precedes it.*

Write a FORMAT CONTRACT section with:

```
## FORMAT CONTRACT

Column schema for all comparative tables in this document:
| [row key] | BASELINE | PROTECTED | Delta |

BASELINE: [specific meaning for this scenario — describe the system as presented in the scenario with no additional protections, naming the specific components in their current state]
PROTECTED: [specific meaning for this scenario — describe the system with the mitigations proposed in Role 9 applied, naming the type of protections]

Rejection rule: Any table in this document that omits the BASELINE or PROTECTED column is marked INCOMPLETE. INCOMPLETE tables must be revised before this analysis is considered final.
```

---

**ROLE 3 — RATE LIMIT REGISTRY ANALYST**

List every rate-limiting component in binding order — most likely to bind first at the stated load to least likely. For each:
- Component name and type (connector / platform runtime / environment governor / per-tenant limit)
- Numeric threshold — number and unit required; mark [estimated] for any threshold not in public docs
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Ordering rationale: one causal sentence naming why this limit binds before the next one

At least one entry must confirm, extend, or contradict the Binding Constraint stated in the VERDICT.

---

**ROLE 4 — CAUSAL PROPAGATION TRACER**

Starting from the binding constraint identified in Role 3: trace how throttling propagates to at least one upstream or downstream component. Minimum two directed hops. Each hop must use a named mechanism from this set: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. The chain must terminate at a user-observable effect.

"Component B is also throttled" without a named mechanism fails. "Component A's queue fills → Component B receives delayed events → Component B's own timeout fires" passes.

---

**ROLE 5 — THROUGHPUT ANALYST**

Produce the Volume-to-Behavior Map using the FORMAT CONTRACT schema. Three volume bands minimum: 1x nominal, 2x nominal, 5x nominal. For each band, fill BASELINE and PROTECTED columns.

In the 5x PROTECTED row, include numeric estimates: using the numeric threshold from Role 3 and the 5x request rate, compute the percentage of requests expected to queue beyond 30 seconds and the percentage expected to fail after retries exhaust. Show the arithmetic step-by-step. Rows at any volume band that describe behavior only in qualitative terms ("most requests fail") without a number are INCOMPLETE under the FORMAT CONTRACT.

---

**ROLE 6 — BURST PATH AUDITOR**

For each trigger and action that can generate concurrent requests: verify the three-control checklist:
1. Concurrency cap present and set below the rate limit
2. Retry-After retry policy present and reading the response header
3. Queue buffer between the source and the rate-limited endpoint

For each path missing all three controls: classify as **STRUCTURAL** (no mechanism exists on this path) or **INCIDENTAL** (mechanism exists but is bypassed, misconfigured, or absent only under specific conditions — name the specific condition). A path that has controls at a higher tier but not on this path does not qualify as protected.

This section must confirm or explicitly revise the Primary Gap stated in the VERDICT.

---

**ROLE 7 — RETRY-AFTER INSPECTOR**

For each connector and HTTP action in the flow: state whether it reads and honors Retry-After headers. Check equivalents: `Retry-After-Ms`, `x-ms-ratelimit-remaining`. For each gap: name the failure mode — immediate retry storm / permanent failure after N retries / silent drop / exponential backoff that ignores the header value.

---

**ROLE 8 — CASCADE SCENARIO CONSTRUCTOR**

Construct one specific scenario where throttling at the binding constraint (Role 3) causally triggers a second distinct throttle event at a different tier — and describe the compounding effect on throughput or error rate. Two independent limits both hit under load do not constitute a cascade. The second throttle event must be causally triggered by the first. State the causal link explicitly.

---

**ROLE 9 — MITIGATION ARCHITECT**

For each bottleneck (Role 3) and unprotected burst path (Role 6): produce one table row per finding using the FORMAT CONTRACT schema. BASELINE column: the specific system behavior at this bottleneck before any mitigation, tied to this component and load condition. PROTECTED column: the system behavior after the specific mitigation is applied, naming the exact action, connector setting, or flow pattern changed. Delta column: the measurable change in throughput, error rate, or queue depth.

Generic advice ("add retry logic") without naming the specific control and location fails.

---

Evidence in Roles 3–9 must confirm or explicitly revise each claim in the VERDICT. A VERDICT claim with no confirming or revising evidence in any Role section fails.

---

## V-02

**Variation axis:** Output format — Verdict block and Format Contract appear as an explicit numbered twin preamble (in that order) before any analysis section, with a formal rejection clause and arithmetic mandate inside the volume table.
**Hypothesis:** Naming both preamble sections as "PREAMBLE A" and "PREAMBLE B" with explicit ordering instructions ("before you write any numbered section") enforces C-15 and C-16 without the multi-role framing of V-01. The preamble label removes ambiguity about whether the Verdict is an introduction or a section — it is PREAMBLE A, the first thing in the document. C-10 is closed by an arithmetic mandate in Section 5 that explicitly calls out qualitative-only rows as incomplete under the FORMAT CONTRACT.

---

You are a Connectors / Power Automate throughput domain expert. Analyze the rate-limited system at 1x, 2x, and 5x nominal load.

**Before you write any numbered analysis section, write the two preamble sections below, in order.**

---

**PREAMBLE A — VERDICT**

This section opens the document. It states the binding constraint and primary gap before any supporting evidence exists. Write it now.

```
## VERDICT

**Binding Constraint**: [Component] — [numeric threshold, unit required] — binding at [N req/min] because [one causal sentence: why this limit is reached before all others at the stated load].
**Primary Gap**: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action or connector name]. [One sentence: what structural control is absent on this path and why it is not present here, not at a higher tier.]
**System Status**: [SAFE | DEGRADED | FAILING] at stated load. [One sentence.]
```

The VERDICT is self-contained. A reader who reads only it must know the core finding, the primary structural gap, and the current operational status. Numbered analysis sections must confirm or explicitly revise each claim.

---

**PREAMBLE B — FORMAT CONTRACT**

This section defines the column schema for every comparative table in this document. Write it after the VERDICT, before Section 1.

```
## FORMAT CONTRACT

Column schema for all comparative tables:
| [key column] | BASELINE | PROTECTED | Delta |

In this scenario:
- **BASELINE** = [specific description of the system in its current state — name the components present and the controls absent]
- **PROTECTED** = [specific description of the system with mitigations applied — name the type and location of protections assumed]

Compliance rule: Any table in this document that omits the BASELINE or PROTECTED column is marked INCOMPLETE. INCOMPLETE tables must be revised. Two or more distinct tables must comply with this schema.
```

---

**Section 1 — Rate Limit Inventory**

List every rate-limiting component in binding order. For each:
- Component name and type
- Numeric threshold — number and unit required; [estimated] for any non-public threshold
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding rank rationale: one causal sentence per component explaining why it binds before the next

At least one component must confirm, extend, or revise the Binding Constraint from the VERDICT.

---

**Section 2 — Backpressure Propagation**

Trace from the binding constraint to at least one downstream or upstream component. Show at least two directed hops:

```
[Component A] → [mechanism] → [Component B] → [mechanism] → [Component C: user-observable effect]
```

Mechanism must be named from: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. Generic terms ("blocked", "slowed") without a mechanism name fail.

---

**Section 3 — Burst Path Audit**

For each trigger and action capable of generating concurrent requests: verify three controls (concurrency cap | Retry-After retry policy | queue buffer between source and rate-limited endpoint). For unprotected paths: classify STRUCTURAL (no mechanism exists on this path) or INCIDENTAL (mechanism exists but bypassed — name the specific condition). A path with controls at a higher tier does not qualify as protected on this path.

This section must confirm or revise the Primary Gap from the VERDICT.

---

**Section 4 — User Experience Per Tier**

For each throttle tier reached at any volume band: state the error code or platform signal, user-visible behavior, whether the throttle is visible to the user, and the user's available recovery path. At least two distinct tiers.

---

**Section 5 — Volume-to-Behavior Map**

Use the FORMAT CONTRACT schema. Volume bands: 1x, 2x, 5x nominal. Each row must have BASELINE and PROTECTED columns filled.

At the 5x band: in the BASELINE column, include numeric estimates derived from the threshold in Section 1 and the 5x request rate — compute the percentage of requests expected to queue beyond 30 seconds and the percentage expected to fail after retries exhaust. Show the arithmetic. Qualitative-only cells at the 5x BASELINE row are INCOMPLETE under the FORMAT CONTRACT. The PROTECTED column at 5x shows how those numbers change with mitigations from Section 8 applied.

---

**Section 6 — Retry-After Handling**

For each connector and HTTP action: evaluate whether Retry-After headers are read and honored (including `Retry-After-Ms`, `x-ms-ratelimit-remaining`). For each gap: name the failure mode — immediate retry storm / permanent failure after N retries / silent drop / backoff that ignores the header value.

---

**Section 7 — Cascade Scenario**

Describe one specific cascade: throttling at the binding constraint (Section 1) causally triggers a second throttle event at a different tier. Show the compounding effect on throughput or error rate. Two independent limits both hit under load do not qualify — the second must be caused by the first.

---

**Section 8 — Mitigation Prescriptions**

Use the FORMAT CONTRACT schema. For each bottleneck and unprotected burst path from Sections 1 and 3, one table row. BASELINE column: specific system behavior at this bottleneck before any fix, tied to this component and condition. PROTECTED column: system behavior after the specific mitigation — name the exact action, connector, or setting changed. Delta column: the measurable change.

Generic advice without naming the specific control location fails.

---

After Section 8: verify that each VERDICT claim has been confirmed, extended, or explicitly revised by evidence in Sections 1–8. Note any revisions.

---

## V-03

**Variation axis:** Lifecycle emphasis — the analysis lifecycle is defined as numbered phases (Phase 0 through Phase 8), with Phase 0 (Verdict) and Phase 0.5 (Format Contract) receiving disproportionate instruction space and explicit gate language ("do not begin Phase 1 until Phase 0 is closed").
**Hypothesis:** When Phase 0 receives the most detailed instructions in the prompt and has an explicit gate-close requirement before Phase 1, the model treats the Verdict as a primary analytical deliverable rather than a summary drawn from evidence. Heavier instruction weight on Phase 0 than on any single analysis phase signals that the Verdict is the most important phase — distinct from V-01's role structure and V-02's preamble label. C-10 arithmetic is enforced inside Phase 5 by explicitly calling qualitative-only Phase 5 rows INCOMPLETE under the Phase 0.5 FORMAT CONTRACT.

---

You are a Connectors / Power Automate throughput domain expert running a multi-phase throughput simulation. The simulation has nine phases. **Phases 0 and 0.5 run before any evidence is collected.** Phases 1–8 gather and analyze evidence. Each phase's output must appear in the document before the next phase begins.

---

**PHASE 0 — GLOBAL VERDICT** *(required first — no evidence sections may precede it)*

Phase 0 is not a conclusion drawn from evidence. It is a pre-commitment: your analytical position before the evidence phases run. The evidence phases confirm, extend, or revise it. Write it now.

This pre-commitment discipline is load-bearing. If you describe inventory before committing to a binding constraint, the inventory shapes the constraint. Phase 0 forces the binding constraint to come from your domain knowledge, not from the evidence you are about to present. If Phase 1 reveals a different binding component, return and update Phase 0 — mark it REVISED and state what changed.

Phase 0 output is a single self-contained block:

```
## PHASE 0 — VERDICT

Binding Constraint: [Component name] — [numeric threshold with unit, required] — exhausted at [X req/min] because [one causal sentence: why this component's limit is reached before all others at the stated load].

Primary Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] — Location: [specific action or connector name] — Absence: [one sentence: what structural control is missing on this path and why it is not present here, not at a higher tier].

System Status: [SAFE | DEGRADED | FAILING] — Basis: [one sentence stating what evidence would confirm or refute this status classification].
```

The block must be self-contained. A reader who reads only Phase 0 must know the core finding, the critical gap location, and the operational status.

**Do not begin Phase 0.5 until all three fields are written and non-empty.**

---

**PHASE 0.5 — FORMAT CONTRACT** *(runs after Phase 0, before Phase 1)*

Before any tables are generated, declare the column schema that all comparative tables in this document must follow.

```
## PHASE 0.5 — FORMAT CONTRACT

Comparative table schema for all tables in Phases 1–8:
| [row key] | BASELINE | PROTECTED | Delta |

BASELINE: [specific meaning for this scenario — describe the system in its current state, naming the specific components and the controls that are absent. This is the system as presented in the input.]
PROTECTED: [specific meaning for this scenario — describe the system after the mitigations in Phase 8 are applied, naming the type of protections and where they attach.]

Rejection rule: Any table in Phases 1–8 that omits the BASELINE or PROTECTED column is flagged INCOMPLETE. INCOMPLETE tables must be revised before this simulation is considered final. At least two distinct Phase tables must comply with this schema.
```

**Do not begin Phase 1 until the FORMAT CONTRACT is written.**

---

**PHASE 1 — RATE LIMIT REGISTRY**

List all rate-limiting components in binding order for the stated load. For each:
- Component name and type
- Numeric threshold — number and unit required; [estimated] for any non-public value
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding order rationale: one causal sentence per component

At least one component must confirm, extend, or revise the Binding Constraint from Phase 0. If Phase 1 reveals a different binding component, return to Phase 0 and mark it REVISED.

---

**PHASE 2 — CAUSAL BACKPRESSURE CHAIN**

Starting from the binding constraint: trace propagation through at least two directed hops. Each hop must name the mechanism: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. Terminate at a user-observable effect. Listing components without a named mechanism fails.

---

**PHASE 3 — BURST PATH AUDIT**

Use the FORMAT CONTRACT schema for the audit table. For each trigger or action capable of generating concurrent requests: verify three controls (concurrency cap | Retry-After retry policy | queue buffer). For unprotected paths: classify STRUCTURAL or INCIDENTAL (name the bypass condition for Incidental). A path with controls at a higher tier is not protected on this path.

This phase must confirm or revise the Primary Gap from Phase 0.

---

**PHASE 4 — UX PER THROTTLE TIER**

For each tier reached at any volume band: error code or platform signal, user-visible behavior, visibility to user, and user recovery path. At least two distinct tiers.

---

**PHASE 5 — VOLUME-TO-BEHAVIOR MAP**

Use the FORMAT CONTRACT schema. Volume bands: 1x, 2x, 5x nominal. BASELINE and PROTECTED columns required for each band.

For the 5x BASELINE row: include numeric estimates. Using the threshold from Phase 1 and the 5x request rate, compute the percentage of requests queuing beyond 30 seconds and the percentage failing after retries exhaust. Show the arithmetic. A 5x BASELINE cell that describes behavior only in qualitative terms is INCOMPLETE under the Phase 0.5 FORMAT CONTRACT and must be revised. The 5x PROTECTED row shows how those numbers change with Phase 8 mitigations applied.

---

**PHASE 6 — RETRY-AFTER EVALUATION**

For each connector and HTTP action: state whether Retry-After is read and honored (including `Retry-After-Ms`, `x-ms-ratelimit-remaining`). For each gap: name the failure mode — retry storm / permanent failure / silent drop / backoff that ignores the header value.

---

**PHASE 7 — CASCADE SCENARIO**

Construct one specific cascade where throttling at the Phase 1 binding constraint causally triggers a second throttle at a different tier. Describe the compounding effect. Two limits independently hit under load do not qualify — the second must be caused by the first.

---

**PHASE 8 — MITIGATION PRESCRIPTIONS**

Use the FORMAT CONTRACT schema. For each bottleneck and burst path from Phases 1 and 3, one row. BASELINE column: system behavior at this bottleneck before any fix, specific to this component and load condition. PROTECTED column: system behavior after the specific mitigation — name the exact action, connector, or setting. Delta column: the measurable change in throughput, error rate, or queue depth. Generic advice without specifics is INCOMPLETE under the Phase 0.5 FORMAT CONTRACT.

---

**Phase 0 reconciliation**: After Phase 8, verify that each Phase 0 claim has been confirmed, extended, or explicitly revised by evidence in Phases 1–8. Note any revisions and mark the Phase 0 block REVISED where applicable.

---

## V-04

**Variation axis:** Phrasing register — conversational, imperative, commit-first second-person commands throughout. "Write your verdict first. Now. Before your first table." No formal phase numbering or role framing; the register itself enforces structural ordering through direct command pressure.
**Hypothesis:** Imperative second-person commands ("before you write a single analysis sentence", "now, before your first table") create a different kind of structural enforcement than role gating or phase labels. The register makes the ordering feel like a constraint on the model's immediate action rather than a document structure requirement. This may be more effective at preventing mid-document verdict drift because the commands are time-indexed to the generation sequence, not to the output structure. C-10 arithmetic is enforced with "do the math — show the calculation — qualitative-only rows fail."

---

Here is what you are doing: analyzing a rate-limited Power Automate / Connectors system to find where it breaks, how fast, and what the user experiences at each failure tier.

Before you write a single analysis sentence, answer these three questions and write the answers at the very top of your document:

```
## VERDICT

What breaks first? [Component name] hits [numeric threshold — number and unit required] at [X req/min] because [one causal sentence: why this limit is reached before all others].
What is structurally unprotected? [Specific action or connector name]: [one sentence on what control is absent on this path — not at a higher tier, absent here].
Is the system safe at the stated load? [SAFE | DEGRADED | FAILING] — [one sentence].
```

That is your opening section. It comes before anything else. A reader who reads only the VERDICT should know the core finding, the critical structural gap, and the current operational status. You will prove these claims in the steps below. If the evidence contradicts a claim, return and update the VERDICT — mark it REVISED.

Now, before your first comparative table, declare what your tables mean:

```
## FORMAT CONTRACT

All comparison tables in this document use this column schema:
| [key] | BASELINE | PROTECTED | Delta |

BASELINE = [what this column means in this specific scenario — describe the system as given, naming the specific components in their current state, no additional protections]
PROTECTED = [what this column means in this specific scenario — describe the system after the Step 8 mitigations are applied, naming the type of protections]

Any table in this document missing a BASELINE or PROTECTED column is incomplete. Flag it and fix it before treating this analysis as final.
```

Now do the analysis in order:

---

**Step 1 — Rate Limit Inventory**

List every rate-limiting component. Order them: which one binds first at the stated load, which second, and so on. For each, give a number and unit — not "limited throughput," a number. If you are estimating, say [est]. For each component, write one causal sentence explaining why it binds before the next one.

At least one component must speak to the binding constraint you wrote in the VERDICT.

---

**Step 2 — Backpressure Chain**

Starting from whatever binds first: trace how the throttle spreads. Give at least two hops. For each hop, name the mechanism — queue-fill, connection-hold, retry-amplification, dependency-stall, timeout-cascade — and where it lands. "Component B is also affected" without a mechanism name fails. End at something the user can see.

---

**Step 3 — Burst Path Check**

For each action or trigger that can fire concurrent requests, check three things:
1. Is there a concurrency cap set below the rate limit?
2. Is there a Retry-After retry policy reading the response header?
3. Is there a queue buffer between the source and the rate-limited endpoint?

If all three are absent: STRUCTURAL gap — no mechanism exists on this path. If one is present but bypassed or misconfigured: INCIDENTAL gap — name the exact bypass condition. "Controls exist at a higher tier" does not count as protected on this path.

This check must speak to the primary gap you wrote in the VERDICT.

---

**Step 4 — What the User Sees**

For each throttle tier that gets hit: what does the user actually experience? Give the error code or platform signal, whether it is visible to them, and how they would find out. At least two distinct tiers.

---

**Step 5 — Volume-to-Behavior Map**

Use the FORMAT CONTRACT column schema. Three rows: 1x load, 2x load, 5x load. Fill in BASELINE and PROTECTED for each.

At 5x, do the math. Using the numeric threshold from Step 1 and the 5x request rate: compute how many requests queue beyond 30 seconds and how many fail after retries run out. Show the calculation. "Most requests fail" without a number fails the FORMAT CONTRACT — the cell is incomplete. In the PROTECTED column at 5x: show how those numbers change with Step 8 mitigations applied.

---

**Step 6 — Retry-After Audit**

Go through each connector and HTTP action. Does it read Retry-After? Does it act on the value? Check equivalents: `Retry-After-Ms`, `x-ms-ratelimit-remaining`. For each gap: name the failure mode — retry storm, permanent failure after N attempts, silent drop, or backoff that ignores the header value.

---

**Step 7 — Cascade Scenario**

Describe one specific case where hitting the first limit causes a second distinct limit at a different tier to be hit. Not two limits hit independently — the second one happens because the first was hit. Show the causal link explicitly and describe how the combined failure is worse than either alone.

---

**Step 8 — Fixes**

For each gap found in Steps 1–6: use the FORMAT CONTRACT column schema. BASELINE column: what the system does at this point today, specific to this component and load condition. PROTECTED column: what it does after your fix — name the specific action, connector, or setting changed. Delta column: the measurable improvement in throughput, error rate, or queue depth. "Add retry logic" without naming the specific control and location fails.

---

After Step 8: check your VERDICT. Did the evidence confirm each claim, or did you find something different? Update and mark REVISED where the evidence overrules the opening commitment.

---

## V-05

**Variation axis:** Inertia framing — the entire analysis is organized around a named two-state comparison: INERTIA (the current system, no additional protections — the status-quo competitor) vs PROTECTED (the system with mitigations applied). Every table, every mitigation row, every volume estimate compares these two states. The Format Contract names INERTIA explicitly as the baseline state.
**Hypothesis:** Making INERTIA the named first-class competitor state throughout the document drives C-12 and C-14 by structural necessity — every table already has INERTIA and PROTECTED columns because that is the organizing frame, not an add-on. C-15 falls naturally: the Verdict is an INERTIA status report written before the evidence that proves it. C-16 falls naturally: the Format Contract declares INERTIA vs PROTECTED as the document schema before any tables exist. C-10 arithmetic is the INERTIA column obligation at 5x — if the INERTIA state is failing at 5x, the column must say by how much.

---

You are a Connectors / Power Automate throughput domain expert. Your analysis compares two named states throughout:

- **INERTIA** — the system as it currently exists, with no additional protections applied. This is the status-quo competitor. Every failure this analysis finds is an INERTIA failure.
- **PROTECTED** — the system with the mitigations your analysis proposes. Every improvement is a move away from INERTIA.

Every table, every mitigation row, every volume estimate shows what changes between INERTIA and PROTECTED. Never describe a finding without stating what the INERTIA behavior is and what the PROTECTED behavior would be.

---

**Opening — VERDICT (write first, before any inventory or table)**

This is your INERTIA status report. Write it before any rate limit inventory, burst path audit, or volume mapping section exists.

```
## VERDICT

Binding Constraint (INERTIA): [Component name] — [numeric threshold, unit required] — exhausted at [X req/min] in the INERTIA state because [one causal sentence: why this component's limit is reached before all others].

Primary INERTIA Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action or connector name]: [one sentence: what structural control is absent in the INERTIA state and why it is not present on this path, not at a higher tier].

INERTIA System Status at Stated Load: [SAFE | DEGRADED | FAILING] — [one sentence].
```

Self-contained. A reader who reads only the VERDICT must know the core INERTIA failure mode, the gap location, and the operational status without reading any subsequent section.

---

**Format Contract — INERTIA vs PROTECTED (write after VERDICT, before Section 1)**

Declare the column schema before any table is generated.

```
## FORMAT CONTRACT

All comparative tables in this document use:
| [key] | INERTIA | PROTECTED | Delta |

INERTIA: [specific meaning for this scenario — the system as described in the input, naming the specific components in their current state, no additional protections applied. This is the competitor state.]
PROTECTED: [specific meaning for this scenario — the system with the mitigations from Section 7 applied, naming the type and location of protections.]

Rejection rule: Any table in Sections 1–7 that omits the INERTIA or PROTECTED column is marked INCOMPLETE. INCOMPLETE tables must be revised before this analysis is final. At least two distinct section tables must comply with this schema.
```

---

**Section 1 — Rate Limit Registry (INERTIA Analysis)**

List all rate-limiting components in binding order for the INERTIA state. For each:
- Component name and type
- Numeric threshold — number and unit required; [estimated] for non-public thresholds
- Scope (per-connection / per-environment / per-flow / per-tenant)
- INERTIA binding order rationale: one causal sentence per component

At least one component must confirm, extend, or revise the Binding Constraint in the VERDICT. If this section reveals a different binding component, return to the VERDICT, update it, and mark it REVISED.

---

**Section 2 — Backpressure Chain (INERTIA State)**

Trace how throttling at the INERTIA binding constraint propagates. At least two directed hops, each with a named mechanism: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. Terminate at a user-observable effect. This is the INERTIA failure chain. "Component B is also throttled" without a mechanism name fails.

---

**Section 3 — Burst Path Audit (INERTIA vs PROTECTED)**

Use the FORMAT CONTRACT schema. For each trigger or action capable of generating concurrent requests:

| Path | INERTIA Controls | INERTIA Gap Type | PROTECTED Controls | Delta |
|------|------------------|------------------|-------------------|-------|

- INERTIA Controls: mark each of the three checks as PRESENT or ABSENT in the INERTIA state — (1) concurrency cap below the rate limit, (2) Retry-After retry policy reading the header, (3) queue buffer between source and rate-limited endpoint
- INERTIA Gap Type: STRUCTURAL (no mechanism exists on this path in the INERTIA state) or INCIDENTAL (mechanism exists but bypassed — name the specific condition) or PROTECTED (all three controls present — this path is safe in INERTIA)
- PROTECTED Controls: what the PROTECTED state adds to make an INERTIA-unprotected path safe

This section must confirm or revise the Primary INERTIA Gap from the VERDICT.

---

**Section 4 — UX Per Throttle Tier (INERTIA State)**

For each tier hit in the INERTIA state: error code or platform signal, user-visible behavior, whether the throttle is visible to the user, and the user's available recovery path. At least two distinct tiers. This section documents the observable cost of the INERTIA state.

---

**Section 5 — Volume-to-Behavior Map (INERTIA vs PROTECTED)**

Use the FORMAT CONTRACT schema. Volume bands: 1x, 2x, 5x nominal.

| Volume | INERTIA Behavior | PROTECTED Behavior | Delta |
|--------|-----------------|-------------------|-------|

For each band: observable behavior in both states.

For the 5x band INERTIA column: compute numeric estimates — using the threshold from Section 1 and the 5x request rate, calculate the percentage of requests queuing beyond 30 seconds and the percentage failing after retries exhaust. Show the arithmetic. A 5x INERTIA cell describing behavior only in qualitative terms is INCOMPLETE under the FORMAT CONTRACT. The 5x PROTECTED column shows how those numbers change when Section 7 mitigations are applied.

---

**Section 6 — Retry-After Handling (INERTIA State)**

For each connector and HTTP action: does the INERTIA state read and honor Retry-After (including `Retry-After-Ms`, `x-ms-ratelimit-remaining`)? For each gap: name the INERTIA failure mode — immediate retry storm / permanent failure after N retries / silent drop / backoff that ignores the header value. The PROTECTED state fixes are in Section 7.

---

**Section 6.5 — Cascade Scenario (INERTIA State)**

In the INERTIA state: construct one specific cascade where throttling at the binding constraint causally triggers a second throttle event at a different tier. Show the compounding effect on throughput or error rate. Two independent limits hit under load do not constitute a cascade — the second must be caused by the first.

---

**Section 7 — Mitigation Prescriptions (INERTIA to PROTECTED)**

Use the FORMAT CONTRACT schema. For each bottleneck and burst path from Sections 1 and 3, one row per finding:

| Finding | INERTIA Behavior | PROTECTED Behavior | Delta |
|---------|-----------------|-------------------|-------|

- INERTIA Behavior: what the system does at this bottleneck in the INERTIA state, specific to this component and load condition — not generic, tied to this scenario
- PROTECTED Behavior: what the system does after the specific mitigation — name the exact action, connector, or setting changed
- Delta: measurable improvement in throughput, error rate, or queue depth

Generic advice ("add retry logic") without naming the specific control and its location fails.

---

**Closing**: Review the VERDICT. Did Sections 1–7 confirm each INERTIA status claim? If evidence revised any claim, update the VERDICT block and mark it REVISED.
