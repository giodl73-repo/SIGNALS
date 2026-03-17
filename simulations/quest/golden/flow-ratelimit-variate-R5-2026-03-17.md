---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 5
rubric_version: 5
---

# flow-ratelimit — Variate R5

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence + full gate chain C-21 + arithmetic trace C-20), V-02 (output format — DERIVATION CHAIN as Format Contract column), V-03 (lifecycle emphasis — gate-checkpoint Verdict currency C-22).
Combination variations: V-04 (full gate chain C-21 + gate-checkpoint currency C-22), V-05 (all three + INERTIA framing + four-field UX template).

**R5 target gaps from R4 scorecard:**
- C-20 (Arithmetic Trace Explicitness): R4 V-01 mandated arithmetic but used "qualitative-only = INCOMPLETE" advisory; C-20 requires the derivation chain to be *shown step-by-step in the cell itself*, each operand referencing the Role 3 registry. R4 V-01's prompt did not specify the computation steps.
- C-21 (Full Gate Chain Closure): R4 V-01 produced 8 gated transitions and PASS on C-17; C-21 codifies the same structure. R5 V-01 replicates and reinforces it.
- C-22 (Gate-checkpoint Verdict Currency): R4 V-01 used terminal reconciliation (scans all roles, inserts markers after Role 10). C-22 requires the `[REVISED — see Role N]` marker to be inserted AT the gate boundary of the revising section, not deferred. R4 V-01 FAILS C-22 explicitly.

All five R5 variations target all three gaps. Variation axes determine HOW each gap is closed.

---

## V-01

**Variation axis:** Role sequence — full gate chain closure (C-21) with inline arithmetic trace mandate (C-20). Every analysis-body role transition (Roles 3–11) is explicitly gated with named deliverables from the prior role. The Format Contract includes a Rejection Clause B that requires the step-by-step derivation chain to appear *in the cell itself*, not merely to be reconstructible. Terminal reconciliation satisfies C-18; gate-checkpoint currency (C-22) is not the target of this variation.

**Hypothesis:** C-21 requires zero ungated transitions in the analysis body. Gating all 9 transitions (Roles 3–11) eliminates bypass paths that partial gating permits. C-20 requires the derivation steps to be visible in the cell — not implied by the conclusion. Embedding this as Rejection Clause B in the Format Contract, and naming it explicitly in the Role 9 gate condition ("the 5x BASELINE cell must show the derivation chain step-by-step — conclusion without steps fails Rejection Clause B"), makes the arithmetic trace a gate-level compliance requirement rather than a per-role advisory.

---

You are executing a multi-role throughput simulation of a rate-limited Power Automate / Connectors system. Roles execute in strict sequence. **Each role produces specific deliverables. The named deliverables gate the next role.** Do not open a role's output section until the prior role's gate is cleared.

---

**ROLE 1 — VERDICT AUTHOR**
*Sole deliverable: VERDICT block with three non-empty labeled fields.*
*Gate: Do not open Role 2 until all three fields are written and non-empty.*

Write a VERDICT block now — before any rate limit inventory, burst path audit, volume table, or cascade scenario exists. This is a pre-commitment from domain knowledge, not a conclusion drawn from evidence below.

```
## VERDICT

**Binding Constraint**: [Component name] — [numeric threshold, unit required] — exhausted
at [X req/min] because [one causal sentence: why this component's limit is reached before
all others at the stated load].

**Primary Gap**: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action
or connector name]: [one sentence — what structural control is absent on this path, and why
it is not present here rather than at a higher tier].

**System Status**: [SAFE | DEGRADED | FAILING] — [one sentence justifying the classification
at the stated load].
```

Rules:
- Binding Constraint must contain a number and unit. "Limited throughput" without a number fails.
- Primary Gap must name the specific action or connector. "The flow lacks retry logic" without a location fails.
- System Status must be exactly one of: SAFE / DEGRADED / FAILING.
- Self-contained: a reader who reads only the VERDICT knows the core finding, gap location, and operational status without proceeding.

**ROLE 1 GATE: Do not open Role 2 until VERDICT contains non-empty Binding Constraint (with number + unit), Primary Gap (with named component), and System Status (SAFE/DEGRADED/FAILING).**

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Gate requires: VERDICT block present with all three fields non-empty.*
*Sole deliverable: FORMAT CONTRACT with schema, scenario-specific definitions, and two rejection clauses.*
*Gate: Do not open Role 3 until FORMAT CONTRACT is written with both rejection clauses present.*

Write the FORMAT CONTRACT now — before any analysis table, registry, or structured section:

```
## FORMAT CONTRACT

Column schema for all comparative tables in this document:
| [row key] | BASELINE | PROTECTED | Delta |

BASELINE: [scenario-specific — describe the system in its current state, naming the specific
components and the controls that are absent. Not a generic definition.]

PROTECTED: [scenario-specific — describe the system after the Role 11 mitigations are applied,
naming the type and location of protections. Not a generic definition.]

Rejection Clause A — Structure: Any comparative table in this document that omits the BASELINE
or PROTECTED column is marked INCOMPLETE. INCOMPLETE tables block this analysis from being
considered final and must be revised.

Rejection Clause B — Arithmetic: Any quantified cell at the 5x volume band that states a
conclusion (e.g., "42% of requests fail") without showing the step-by-step derivation chain
in the cell itself is marked INCOMPLETE. The derivation chain must appear in the cell:
  Step 1: requests/min at 1x × 5 = peak_req/min
  Step 2: peak_req/min − rate_limit [from Role 3 registry] = overflow_req/min
  Step 3: overflow_req/min × retry_amplification_factor = total_attempt_req/min
  Step 4: (total_attempt_req − capacity_req) / total_attempt_req = failure_rate
  Step 5: failure_rate × 100 = failure_pct
Each operand must reference a specific value from the Role 3 registry. A cell showing only a
percentage without the steps fails Rejection Clause B even if the percentage is arithmetically
correct.
```

**ROLE 2 GATE: Do not open Role 3 until: (a) FORMAT CONTRACT is written; (b) BASELINE and PROTECTED definitions are scenario-specific, not generic; (c) both Rejection Clause A and Rejection Clause B are present with the five-step arithmetic template in Clause B.**

---

**ROLE 3 — RATE LIMIT REGISTRY ANALYST**
*Gate requires: FORMAT CONTRACT written with both rejection clauses and scenario-specific definitions.*
*Sole deliverable: Ordered list of all rate-limiting components with numeric thresholds and binding rationale.*
*Gate: Do not open Role 4 until all required fields are present and at least one component addresses the VERDICT Binding Constraint.*

List every rate-limiting component in binding order — most constrained at the stated load to least. For each:
- Component name and type (connector / platform runtime / environment governor / per-tenant limit)
- Numeric threshold — number and unit required; mark [estimated] for any non-public value
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding order rationale: one causal sentence per component, explaining why it binds before the next

At least one component must confirm, extend, or revise the Binding Constraint stated in the VERDICT.

**ROLE 3 GATE: Do not open Role 4 until: (a) every identified rate-limiting component has a row with a numeric threshold and unit; (b) every row has a binding-order rationale sentence; (c) at least one row addresses the VERDICT Binding Constraint (confirms, extends, or revises it). After clearing these conditions, check: do Role 3 findings confirm, extend, or revise the VERDICT Binding Constraint without changing it materially — or does Role 3 reveal a different binding component? If Role 3 reveals the VERDICT Binding Constraint is wrong, return to the VERDICT block and mark that field REVISED with the correction, then proceed.**

---

**ROLE 4 — CAUSAL PROPAGATION TRACER**
*Gate requires: Rate Limit Registry with at least one component having a numeric threshold, a binding-order rationale sentence, and a connection to the VERDICT Binding Constraint.*
*Sole deliverable: Directed hop chain from binding constraint to user-observable effect, minimum two hops.*
*Gate: Do not open Role 5 until at least two hops are documented, each with a named mechanism.*

Starting from the binding constraint in Role 3: trace how throttling propagates through at least two directed hops. For each hop:
- Source component (reference the Role 3 component name)
- Named mechanism — must be one of: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade
- Destination component and the observable effect at that destination

The chain terminates at a user-observable effect (visible error message, flow run queued, delayed response, silent failure). "Component B is also throttled" without a named mechanism fails.

**ROLE 4 GATE: Do not open Role 5 until at least two hops are written, each with a source component referencing Role 3, a named mechanism from the permitted set, and a destination with an observable effect.**

---

**ROLE 5 — BURST PATH AUDITOR**
*Gate requires: Propagation chain with at least two hops, each with a named mechanism.*
*Sole deliverable: Per-path audit with STRUCTURAL/INCIDENTAL/PROTECTED classification.*
*Gate: Do not open Role 6 until at least one unprotected path is classified and the VERDICT Primary Gap is addressed.*

For each trigger and action capable of generating concurrent requests: apply the three-control checklist:
1. Concurrency cap — present and set below the rate limit?
2. Retry-After retry policy — present and reading the response header?
3. Queue buffer — present between the source and the rate-limited endpoint?

For each path where all three controls are absent or insufficient:
- Classify as **STRUCTURAL** if no mechanism exists on this path in the current system.
- Classify as **INCIDENTAL** if a mechanism exists but is bypassed, misconfigured, or absent only under specific conditions — name the exact bypass condition.

A path that has controls at a higher tier does not qualify as protected on this path. "Controls exist somewhere in the system" is not a passing argument.

This role must confirm or explicitly revise the Primary Gap in the VERDICT.

**ROLE 5 GATE: Do not open Role 6 until: (a) at least one path has a STRUCTURAL or INCIDENTAL classification with stated justification; (b) the VERDICT Primary Gap field has been confirmed or revised. If Role 5 reveals a different primary gap, return to the VERDICT block and mark that field REVISED with the correction, then proceed.**

---

**ROLE 6 — RETRY-AFTER INSPECTOR**
*Gate requires: Burst path audit with at least one classified unprotected path and VERDICT Primary Gap addressed.*
*Sole deliverable: Per-connector Retry-After evaluation with failure modes named.*
*Gate: Do not open Role 7 until every connector and HTTP action in the flow has been evaluated and each gap has a named failure mode.*

For each connector and HTTP action in the flow: state whether it reads and honors Retry-After headers. Check all equivalents: `Retry-After`, `Retry-After-Ms`, `x-ms-ratelimit-remaining`. For each gap: name the failure mode precisely — immediate retry storm / permanent failure after N retries / silent drop / exponential backoff that ignores the header value.

**ROLE 6 GATE: Do not open Role 7 until: (a) every connector and HTTP action in the flow has an entry; (b) each gap entry names the specific failure mode from the permitted set. After clearing these conditions, check: do Role 6 findings revise the VERDICT Primary Gap? If so, return to the VERDICT block and mark that field REVISED.**

---

**ROLE 7 — CASCADE SCENARIO CONSTRUCTOR**
*Gate requires: Retry-After inspection complete with failure modes named for all gaps.*
*Sole deliverable: One specific cascade scenario with two named throttle tiers and explicit causal link.*
*Gate: Do not open Role 8 until the cascade names both tiers, the causal mechanism, and the compounding effect.*

Construct one specific cascade scenario where throttling at the Role 3 binding constraint causally triggers a second distinct throttle event at a different tier. Describe the compounding effect on throughput or error rate.

Two independent limits both hit under load do not constitute a cascade. The second throttle must be caused by the first — state the causal link explicitly using the binding constraint and the second tier's name.

**ROLE 7 GATE: Do not open Role 8 until: (a) two distinct throttle tiers are named (both traceable to Role 3 registry entries); (b) the causal link from the first throttle to the second is stated explicitly; (c) the compounding effect on throughput or error rate is described.**

---

**ROLE 8 — UX TIER ANALYST**
*Gate requires: Cascade scenario with two named tiers, explicit causal link, and compounding effect.*
*Sole deliverable: UX per-tier catalog using the four-field template, minimum two tiers.*
*Gate: Do not open Role 9 until at least two throttle tiers are documented using the full four-field template.*

For each throttle tier reached at any volume band: apply the four-field template. **Fewer than four fields per tier fails the template requirement. Free prose that covers all four topics without the labeled template structure fails even if the content is complete.**

```
Tier: [name and error code or platform signal]
  (a) Error code or platform signal: [specific code — e.g., HTTP 429 with Retry-After header,
      ActionThrottled event in run history, connector TL-0001 signal]
  (b) User-visible behavior: [what the user observes or experiences at this tier — specific to
      the tier, not generic "the flow fails"]
  (c) Visibility level: [user-visible and explicit | background-only and silent]
  (d) Recovery path: [manual retry available | automatic exponential backoff | permanent failure
      with no recovery | other — specify]
```

At least two distinct tiers must use this template. A tier described with only three fields fails.

**ROLE 8 GATE: Do not open Role 9 until at least two tiers are documented with all four labeled fields (a) through (d) present for each.**

---

**ROLE 9 — THROUGHPUT ANALYST**
*Gate requires: UX catalog with at least two tiers, each documented with all four template fields.*
*Sole deliverable: Volume-to-Behavior Map using FORMAT CONTRACT schema, with step-by-step arithmetic in the 5x BASELINE cell.*
*Gate: Do not open Role 10 until the volume map is complete and the 5x BASELINE cell shows the full derivation chain.*

Produce the Volume-to-Behavior Map using the FORMAT CONTRACT column schema. Volume bands: 1x nominal, 2x nominal, 5x nominal. Fill BASELINE and PROTECTED columns for each band.

**For the 5x BASELINE cell — FORMAT CONTRACT Rejection Clause B applies here.** The cell must contain the step-by-step arithmetic derivation, not only the conclusion:

```
5x BASELINE cell content:
  Step 1: [1x req/min from scenario] × 5 = [5x_req/min] req/min at peak
  Step 2: [5x_req/min] − [rate_limit from Role 3 registry: component name, N req/min] = [overflow] req/min overflow
  Step 3: [overflow] × [retry_factor, e.g., 3 attempts] = [total_attempts] req/min total attempts
  Step 4: ([total_attempts] − [capacity = rate_limit from Role 3]) / [total_attempts] = [failure_rate]
  Step 5: [failure_rate] × 100 = [failure_pct]% of requests fail after retries exhaust

  [failure_pct]% of requests fail. [queue_pct]% of requests queue beyond 30 seconds.
```

Each step must reference a specific value from the Role 3 registry (component name and numeric threshold). A cell that states "42% fail" without showing the five derivation steps fails Rejection Clause B even if the percentage is arithmetically correct.

The 5x PROTECTED cell shows how failure_pct and queue_pct change when Role 11 mitigations are applied. The same step-by-step format applies; operands change to reflect the mitigated state.

**ROLE 9 GATE: Do not open Role 10 until: (a) all three volume bands have BASELINE and PROTECTED columns filled; (b) the 5x BASELINE cell contains the full five-step derivation chain with operands referencing Role 3 values; (c) the 5x PROTECTED cell shows mitigated arithmetic. A qualitative-only 5x BASELINE cell fails this gate.**

---

**ROLE 10 — MITIGATION ARCHITECT**
*Gate requires: Volume map complete with all three bands filled and 5x BASELINE derivation chain present.*
*Sole deliverable: Per-finding mitigation table using FORMAT CONTRACT schema.*
*Gate: Do not open Role 11 until every bottleneck and unprotected path has a mitigation row with scenario-specific BASELINE, named PROTECTED mitigation, and measurable Delta.*

Use the FORMAT CONTRACT column schema. For each bottleneck (Role 3) and unprotected burst path (Role 5): produce one row per finding:

| Finding | BASELINE | PROTECTED | Delta |
|---------|----------|-----------|-------|

- BASELINE column: the specific system behavior at this bottleneck before any fix — tied to this component and this load condition, not a generic description of the problem.
- PROTECTED column: the system behavior after the specific mitigation — name the exact action, connector setting, or flow pattern changed (e.g., "enable concurrency control on the For Each action, set Degree of Parallelism to 5", not "add concurrency control").
- Delta column: the measurable change in throughput, error rate, or queue depth derivable from Role 9 arithmetic.

Generic advice without naming the specific control and its location fails Rejection Clause A.

**ROLE 10 GATE: Do not open Role 11 until: (a) every bottleneck from Role 3 and every unprotected path from Role 5 has a row; (b) every BASELINE cell names the specific component and condition; (c) every PROTECTED cell names the exact action, setting, or parameter; (d) every Delta cell states a measurable change.**

---

**ROLE 11 — VERDICT RECONCILER**
*Gate requires: Mitigation table complete with all findings covered and scenario-specific entries.*
*Sole deliverable: Updated VERDICT block with all revision markers inserted and all claims confirmed or revised.*

Scan Roles 3–10 systematically. For each of the three VERDICT fields:

1. **Binding Constraint**: Does any role (especially Role 3) confirm, extend, or contradict the stated component and threshold? If contradicted, verify the field was marked REVISED at the prior gate. If the marker is missing, insert `[REVISED — see Role 3]` adjacent to the Binding Constraint label now.

2. **Primary Gap**: Do Roles 5 or 6 confirm, extend, or contradict the gap location and type? If contradicted, verify the field was marked REVISED at the prior gate. If missing, insert `[REVISED — see Role 5]` or `[REVISED — see Role 6]` now.

3. **System Status**: Do Roles 9 and 10 confirm the SAFE/DEGRADED/FAILING classification? If Role 9 arithmetic shows a different severity, verify the field was marked REVISED at the prior gate. If missing, insert `[REVISED — see Role 9]` now.

Any VERDICT claim with no confirming or revising evidence in Roles 3–10 fails reconciliation — identify which role should have addressed it and note the gap.

---

## V-02

**Variation axis:** Output format — DERIVATION CHAIN as a mandatory fourth column in the Format Contract schema. Every table with quantified cells must include a DERIVATION CHAIN column; the rejection clause flags any DERIVATION CHAIN cell that states a conclusion without the computation steps as INCOMPLETE. This targets C-20 at the structural level (column compliance) rather than at the instructional level (per-role advisory).

**Hypothesis:** When DERIVATION CHAIN is declared as a named column in the Format Contract, arithmetic explicitness becomes a column-level compliance requirement enforced by the same rejection clause that enforces BASELINE and PROTECTED. A table missing the DERIVATION CHAIN column is as structurally incomplete as a table missing BASELINE — the violation is visible without reading the analysis. Constrast with V-01's approach (which mandates steps in a specific role): V-02's rejection clause catches missing derivations across *all* quantified tables, not only the volume map. Gate language provides C-17 coverage but not full chain closure — the DERIVATION CHAIN column is the variation's structural mechanism for C-20.

---

You are a Connectors / Power Automate throughput domain expert. Analyze the rate-limited system at 1x, 2x, and 5x nominal load.

**Before you write any numbered analysis section, write the two preamble blocks below, in order.**

---

**PREAMBLE A — VERDICT**
*(write first, before any rate limit table, burst path audit, or volume mapping section)*

```
## VERDICT

**Binding Constraint**: [Component name] — [numeric threshold, unit required] — binding at
[X req/min] because [one causal sentence: why this component's limit is reached before all
others at the stated load].

**Primary Gap**: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action
or connector name]: [one sentence — what structural control is absent on this path and why
it is not present here, not at a higher tier].

**System Status**: [SAFE | DEGRADED | FAILING] at stated load. [One sentence.]
```

Self-contained. A reader who reads only the VERDICT must know the binding component, the primary structural gap, and the current operational status. Analysis sections must confirm or explicitly revise each claim; a VERDICT claim with no confirming or revising evidence in Sections 1–8 fails.

---

**PREAMBLE B — FORMAT CONTRACT**
*(write after VERDICT, before Section 1)*

```
## FORMAT CONTRACT

Column schema for quantitative tables in this document:
| [key column] | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |

BASELINE: [scenario-specific — describe the system in its current state, naming the specific
components present and the controls absent.]

PROTECTED: [scenario-specific — describe the system with Section 8 mitigations applied,
naming the type and location of protections.]

DERIVATION CHAIN: This column must contain the step-by-step arithmetic derivation for every
quantified cell:
  requests/interval × load_multiplier = peak_load
  peak_load − rate_limit [cite component name + N from Section 1] = overflow
  overflow × retry_factor = total_attempts
  (total_attempts − capacity) / total_attempts = failure_rate
  failure_rate × 100 = failure_pct

Rejection Clause A — Structure: Any table in this document that omits BASELINE or PROTECTED
is marked INCOMPLETE. INCOMPLETE tables must be revised before this analysis is considered
final.

Rejection Clause B — Arithmetic: Any DERIVATION CHAIN cell that contains a conclusion (e.g.,
"42% fail") without the step-by-step derivation above is marked INCOMPLETE. The derivation
must be in the cell. Being reconstructible by an attentive reader does not satisfy this clause;
the steps must be present. At least two distinct section tables must comply with the full
five-column schema.
```

---

**Section 1 — Rate Limit Inventory**

List every rate-limiting component in binding order. For each:
- Component name and type
- Numeric threshold — number and unit required; [estimated] for any non-public value
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding rationale: one causal sentence per component, explaining why it binds before the next

At least one component must confirm, extend, or revise the VERDICT Binding Constraint.

---

**Section 2 — Backpressure Propagation**

Trace from the binding constraint through at least two directed hops:

```
[Component] → [named mechanism] → [Component] → [named mechanism] → [user-observable effect]
```

Named mechanisms only: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. Generic terms ("blocked", "slowed") without a mechanism name fail.

---

**Section 3 — Burst Path Audit**

For each trigger and action capable of generating concurrent requests: verify three controls:
1. Concurrency cap present and set below the rate limit
2. Retry-After retry policy present and reading the response header
3. Queue buffer between the source and the rate-limited endpoint

For each unprotected path: classify STRUCTURAL (no mechanism exists on this path) or INCIDENTAL (mechanism exists but bypassed — name the exact bypass condition). Controls at a higher tier do not protect this path.

This section must confirm or revise the VERDICT Primary Gap.

---

**Section 4 — User Experience Per Throttle Tier**

For each throttle tier reached at any volume band: apply this four-field template per tier:
```
Tier [N]:
  (a) Error code or platform signal: [specific code or signal identifier]
  (b) User-visible behavior: [what the user observes]
  (c) Visibility level: [explicit and user-visible | silent and background]
  (d) Recovery path: [manual retry | automatic backoff | permanent failure | other]
```
At least two distinct tiers. Prose description without the template fails even if all four topics are covered.

---

**Section 5 — Volume-to-Behavior Map** *(quantitative — FORMAT CONTRACT five-column schema applies)*

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|------------------|-------|
| 1x     |          |           |                  |       |
| 2x     |          |           |                  |       |
| 5x     |          |           |                  |       |

The DERIVATION CHAIN column at 5x must show the full five-step arithmetic derivation (see FORMAT CONTRACT). The BASELINE and PROTECTED columns show qualitative behavior summaries; the DERIVATION CHAIN column carries the numbers. A DERIVATION CHAIN cell at 5x that states only a percentage is INCOMPLETE under Rejection Clause B.

---

**Section 6 — Retry-After Handling**

For each connector and HTTP action: state whether it reads and honors Retry-After headers (including `Retry-After-Ms`, `x-ms-ratelimit-remaining`). For each gap: name the failure mode — immediate retry storm / permanent failure after N retries / silent drop / backoff ignoring header value.

---

**Section 7 — Cascade Scenario**

One specific cascade where throttling at the Section 1 binding constraint causally triggers a second throttle at a different tier. Show the compounding effect. Two independent limits hit under load do not qualify — the second must be caused by the first.

---

**Section 8 — Mitigation Prescriptions** *(FORMAT CONTRACT five-column schema applies)*

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|------------------|-------|

- BASELINE: specific behavior at this bottleneck before any fix, named to this component and load condition
- PROTECTED: behavior after the specific mitigation — name the exact action, connector setting, or parameter
- DERIVATION CHAIN: if the mitigation changes a numeric limit or retry factor, show the updated arithmetic using the same five-step format
- Delta: measurable change in throughput, error rate, or queue depth

---

After Section 8: verify each VERDICT claim has been confirmed, extended, or explicitly revised by Sections 1–8. For any revised claim, insert `[REVISED — see Section N]` adjacent to the field label in the VERDICT block.

---

## V-03

**Variation axis:** Lifecycle emphasis — gate-checkpoint Verdict currency. Every phase exit condition includes a mandatory Verdict-currency check as a prerequisite for unblocking the next phase. The model must check whether the current phase revises any VERDICT claim, and if so, must insert the `[REVISED — see Phase N]` marker in the VERDICT block **before** the next phase's entry condition is unblocked. This targets C-22 as a lifecycle structural discipline rather than a terminal reconciliation step.

**Hypothesis:** C-22 requires revision markers to appear at the gate boundary of the revising section, not deferred to document close. When the Verdict-currency check is embedded in each phase exit condition ("before clearing this exit, check: does this phase revise a VERDICT claim?"), the model performs the check at the moment of production. A terminal reconciliation role (which satisfies C-18) permits the VERDICT to be stale across all intermediate phases. Embedding the check at each boundary makes currency a per-phase obligation — the reader consulting only the VERDICT at any intermediate point in the document will find current markers. Gate language covers C-17 for at least three additional transitions; full gate chain (C-21) is secondary to the currency axis in this variation.

---

You are a Connectors / Power Automate throughput domain expert running a nine-phase throughput simulation. **Phases 0 and 0.5 are preamble phases — they run before any evidence is collected.** Phases 1–8 gather and analyze evidence. Each phase's output must be present in the document before the next phase begins.

---

**PHASE 0 — GLOBAL VERDICT** *(first phase — no evidence sections may precede it)*

Phase 0 is a pre-commitment from domain knowledge. Write it before any rate limit inventory, burst path audit, or volume table. The evidence phases confirm, extend, or revise it.

```
## PHASE 0 — VERDICT

Binding Constraint: [Component name] — [numeric threshold, unit required] — exhausted at
[X req/min] because [one causal sentence: why this component's limit is reached before all
others at the stated load].

Primary Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] — Location: [specific
action or connector name] — Absence: [one sentence: what structural control is missing on
this path and why it is not present here, not at a higher tier].

System Status: [SAFE | DEGRADED | FAILING] — Basis: [one sentence stating what evidence would
confirm or refute this status classification].
```

Self-contained. A reader who reads only Phase 0 must know the core finding, critical gap location, and operational status.

**PHASE 0 EXIT CONDITION:**
1. All three VERDICT fields are written and non-empty.
2. Binding Constraint contains a number and unit.
3. Primary Gap names a specific component.
4. *Verdict-currency check*: Phase 0 has no prior phases to revise; no marker needed. This check is satisfied automatically.

**Do not begin Phase 0.5 until the Phase 0 exit condition is cleared.**

---

**PHASE 0.5 — FORMAT CONTRACT** *(runs after Phase 0, before Phase 1)*

Declare the column schema before any comparative table is generated.

```
## PHASE 0.5 — FORMAT CONTRACT

Comparative table schema for all tables in Phases 1–8:
| [row key] | BASELINE | PROTECTED | Delta |

BASELINE: [scenario-specific — describe the system as it currently exists, naming the
components present and the controls absent. This is the state the VERDICT describes.]

PROTECTED: [scenario-specific — describe the system after Phase 8 mitigations are applied,
naming the type and location of protections.]

Rejection Clause A: Any table in Phases 1–8 omitting BASELINE or PROTECTED is marked
INCOMPLETE and must be revised.
```

**PHASE 0.5 EXIT CONDITION:**
1. FORMAT CONTRACT is written.
2. BASELINE and PROTECTED are scenario-specific (not generic).
3. Rejection Clause A is present.
4. *Verdict-currency check*: does Phase 0.5 revise any Phase 0 claim? If yes, insert `[REVISED — see Phase 0.5]` adjacent to the revised field in the VERDICT block now, before proceeding.

**Do not begin Phase 1 until the Phase 0.5 exit condition is cleared.**

---

**PHASE 1 — RATE LIMIT REGISTRY**

List all rate-limiting components in binding order. For each:
- Component name and type
- Numeric threshold — number and unit required; [estimated] for any non-public value
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding order rationale: one causal sentence per component

**PHASE 1 EXIT CONDITION:**
1. Every identified rate-limiting component has a row.
2. Every row has a numeric threshold with unit and a binding-order rationale sentence.
3. At least one component addresses the VERDICT Binding Constraint.
4. *Verdict-currency check*: does Phase 1 confirm, extend, or contradict the VERDICT Binding Constraint or System Status? If Phase 1 reveals a different binding component or load classification:
   - Update the VERDICT Binding Constraint and/or System Status to reflect the correct finding.
   - Insert `[REVISED — see Phase 1]` adjacent to the revised field label in the VERDICT block.
   - **Do this now, before proceeding to Phase 2.**

**Do not begin Phase 2 until the Phase 1 exit condition is cleared, including the Verdict-currency check.**

---

**PHASE 2 — CAUSAL BACKPRESSURE CHAIN**

Starting from the Phase 1 binding constraint: trace propagation through at least two directed hops. Each hop must name the mechanism: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. Terminate at a user-observable effect.

**PHASE 2 EXIT CONDITION:**
1. At least two hops are documented with named mechanisms and a terminal user-observable effect.
2. *Verdict-currency check*: does Phase 2 reveal a backpressure path that changes the VERDICT Primary Gap or System Status? If so:
   - Update the relevant VERDICT field.
   - Insert `[REVISED — see Phase 2]` adjacent to the revised field label in the VERDICT block.
   - **Do this now, before proceeding to Phase 3.**

**Do not begin Phase 3 until the Phase 2 exit condition is cleared.**

---

**PHASE 3 — BURST PATH AUDIT**

For each trigger or action capable of generating concurrent requests: verify three controls (concurrency cap | Retry-After retry policy | queue buffer). For unprotected paths: classify STRUCTURAL (no mechanism on this path) or INCIDENTAL (mechanism present but bypassed — name the bypass condition). Controls at a higher tier do not protect this path.

This phase must confirm or revise the VERDICT Primary Gap.

**PHASE 3 EXIT CONDITION:**
1. At least one path is classified STRUCTURAL or INCIDENTAL with stated justification.
2. The VERDICT Primary Gap is addressed (confirmed or revised).
3. *Verdict-currency check*: does Phase 3 reveal that the VERDICT Primary Gap names the wrong component, wrong gap type, or wrong location? If so:
   - Update the VERDICT Primary Gap field.
   - Insert `[REVISED — see Phase 3]` adjacent to the Primary Gap label in the VERDICT block.
   - **Do this now, before proceeding to Phase 4.**

**Do not begin Phase 4 until the Phase 3 exit condition is cleared.**

---

**PHASE 4 — UX PER THROTTLE TIER**

For each tier reached at any volume band, apply the four-field template:
```
Tier [N]:
  (a) Error code or platform signal: [specific code or platform signal]
  (b) User-visible behavior: [what the user observes]
  (c) Visibility level: [explicit and user-visible | silent and background]
  (d) Recovery path: [manual retry | automatic backoff | permanent failure | other]
```
At least two distinct tiers. Fewer than four fields per tier fails the template.

**PHASE 4 EXIT CONDITION:**
1. At least two tiers are documented with all four template fields.
2. *Verdict-currency check*: does Phase 4 evidence change the VERDICT System Status classification (e.g., tiers show the user experiences silent failure at 1x, updating SAFE to DEGRADED)? If so:
   - Update the VERDICT System Status.
   - Insert `[REVISED — see Phase 4]` adjacent to the System Status label in the VERDICT block.
   - **Do this now, before proceeding to Phase 5.**

**Do not begin Phase 5 until the Phase 4 exit condition is cleared.**

---

**PHASE 5 — VOLUME-TO-BEHAVIOR MAP**

Use the FORMAT CONTRACT schema. Volume bands: 1x, 2x, 5x. Fill BASELINE and PROTECTED for each band.

For the 5x BASELINE row: provide numeric estimates from Phase 1 thresholds. Using the binding constraint threshold and the 5x request rate, show the arithmetic:
- requests/min at 1x × 5 = peak load
- peak load − rate limit = overflow
- overflow × retry factor = total attempts
- (total attempts − capacity) / total attempts = failure rate

Show the computation steps. A 5x BASELINE cell describing behavior only in qualitative terms ("most requests fail") without arithmetic is INCOMPLETE under Rejection Clause A. The 5x PROTECTED cell shows how the failure rate changes with Phase 8 mitigations applied.

**PHASE 5 EXIT CONDITION:**
1. All three volume bands have BASELINE and PROTECTED columns filled.
2. The 5x BASELINE cell contains the arithmetic computation (four computation steps minimum, each referencing a Phase 1 value).
3. No qualitative-only cell at 5x remains.
4. *Verdict-currency check*: does Phase 5 arithmetic contradict the VERDICT System Status? If Phase 5 shows failure at 1x load when VERDICT says DEGRADED (or other discrepancy):
   - Update the VERDICT System Status.
   - Insert `[REVISED — see Phase 5]` adjacent to the System Status label in the VERDICT block.
   - **Do this now, before proceeding to Phase 6.**

**Do not begin Phase 6 until the Phase 5 exit condition is cleared.**

---

**PHASE 6 — RETRY-AFTER EVALUATION**

For each connector and HTTP action: state whether Retry-After is read and honored (including `Retry-After-Ms`, `x-ms-ratelimit-remaining`). For each gap: name the failure mode — retry storm / permanent failure / silent drop / backoff ignoring header value.

**PHASE 6 EXIT CONDITION:**
1. Every connector and HTTP action has been evaluated.
2. Each gap has a named failure mode.
3. *Verdict-currency check*: does Phase 6 reveal that the VERDICT Primary Gap named the wrong gap type (e.g., UNPROTECTED BURST PATH when the dominant gap is actually RETRY-AFTER MISSING)? If so:
   - Update the VERDICT Primary Gap type.
   - Insert `[REVISED — see Phase 6]` adjacent to the Primary Gap label in the VERDICT block.
   - **Do this now, before proceeding to Phase 7.**

**Do not begin Phase 7 until the Phase 6 exit condition is cleared.**

---

**PHASE 7 — CASCADE SCENARIO**

Construct one specific cascade where throttling at the Phase 1 binding constraint causally triggers a second throttle at a different tier. Show the compounding effect. Two independent limits hit under load do not qualify — the second must be caused by the first.

**PHASE 7 EXIT CONDITION:**
1. Two distinct throttle tiers are named.
2. The causal link is stated explicitly.
3. The compounding effect is described.
4. *Verdict-currency check*: does Phase 7 reveal a compound failure mode that changes the VERDICT System Status? If so:
   - Update the VERDICT System Status.
   - Insert `[REVISED — see Phase 7]` adjacent to the System Status label in the VERDICT block.
   - **Do this now, before proceeding to Phase 8.**

**Do not begin Phase 8 until the Phase 7 exit condition is cleared.**

---

**PHASE 8 — MITIGATION PRESCRIPTIONS**

Use the FORMAT CONTRACT schema. For each bottleneck and burst path from Phases 1 and 3:

| Finding | BASELINE | PROTECTED | Delta |
|---------|----------|-----------|-------|

- BASELINE: specific system behavior at this bottleneck before any fix, tied to this component and load condition.
- PROTECTED: system behavior after the specific mitigation — name the exact action, connector, or setting changed.
- Delta: measurable change in throughput, error rate, or queue depth.

Generic advice without naming the specific control and location fails Rejection Clause A.

**PHASE 8 EXIT CONDITION:**
1. Every bottleneck and unprotected path has a row.
2. Every BASELINE cell is scenario-specific.
3. Every PROTECTED cell names the exact control and location.
4. *Verdict-currency check*: does Phase 8 reveal that the full mitigation set changes the operational classification enough to update the VERDICT System Status (e.g., PROTECTED state moves from FAILING to SAFE)? The VERDICT describes the *current* state, not the mitigated state — but if the current state classification was wrong:
   - Update the VERDICT System Status if the INERTIA state was misclassified.
   - Insert `[REVISED — see Phase 8]` adjacent to the System Status label if updated.

---

## V-04

**Variation axis (combined):** Full gate chain closure (C-21) from V-01 + gate-checkpoint Verdict currency (C-22) from V-03. Every analysis-body role transition (Roles 3–10) is explicitly gated. Each gate includes the Verdict-currency check as part of the unblock condition — the gate cannot be cleared until the currency check is performed and any required revision marker is inserted. Terminal reconciliation is retained for completeness but the gate-embedded checks are the primary currency mechanism.

**Hypothesis:** C-22 explicitly fails prompts where bidirectional revision is achieved solely through a terminal reconciliation pass. C-21 requires zero ungated analysis-body transitions. These two criteria co-require each other: you cannot have gate-checkpoint currency without a gate, and you cannot satisfy C-21 without closing all gates, each of which carries the currency check. V-04 encodes both in a unified architecture where every gate is a two-part check: (1) prior deliverables present, (2) VERDICT currency confirmed and revision markers inserted if due. The combination makes it structurally impossible to satisfy C-21 (clear all gates) without also satisfying C-22 (perform currency check at each gate).

---

You are executing a multi-role throughput simulation of a rate-limited Power Automate / Connectors system. Roles execute in strict sequence. **Each role transition is gated. A gate has two parts: (1) required deliverables from the prior role, and (2) a mandatory Verdict-currency check. Both parts must be satisfied before the next role begins.**

---

**ROLE 1 — VERDICT AUTHOR**
*Sole deliverable: VERDICT block with three non-empty labeled fields.*

Write the VERDICT block first — before any other section:

```
## VERDICT

**Binding Constraint**: [Component name] — [numeric threshold, unit required] — exhausted at
[X req/min] because [one causal sentence].

**Primary Gap**: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action
or connector name]: [one sentence — what structural control is absent here, not at a higher
tier].

**System Status**: [SAFE | DEGRADED | FAILING] — [one sentence].
```

**ROLE 1 → ROLE 2 GATE:**
- *Deliverable check*: all three VERDICT fields written and non-empty; Binding Constraint contains a number and unit; Primary Gap names a specific component.
- *Verdict-currency check*: Role 1 opens the document; no prior phase to check. Currency satisfied automatically.
- **Both checks must pass before Role 2 begins.**

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Sole deliverable: FORMAT CONTRACT with schema, scenario-specific BASELINE/PROTECTED definitions, and rejection clauses.*

```
## FORMAT CONTRACT

Column schema for all comparative tables:
| [row key] | BASELINE | PROTECTED | Delta |

BASELINE: [scenario-specific — name the components and absent controls in the current system]
PROTECTED: [scenario-specific — name the mitigations from Role 10 and where they attach]

Rejection Clause A: Any comparative table omitting BASELINE or PROTECTED is INCOMPLETE.
Rejection Clause B: Any quantified 5x cell that states a conclusion without showing the
derivation steps is INCOMPLETE. Steps required: (1) 1x req/min × 5 = peak, (2) peak − limit
[cite Role 3 component + N] = overflow, (3) overflow × retry_factor = total_attempts,
(4) (total_attempts − capacity) / total_attempts = failure_rate, (5) failure_rate × 100 = %.
```

**ROLE 2 → ROLE 3 GATE:**
- *Deliverable check*: FORMAT CONTRACT written; BASELINE and PROTECTED are scenario-specific; both rejection clauses present (including five-step arithmetic template in Clause B).
- *Verdict-currency check*: does Role 2 (declaring the Format Contract) reveal any mismatch with the VERDICT's framing? If the BASELINE definition names different components than the VERDICT Binding Constraint or Primary Gap, reconcile them now. If any VERDICT field requires updating, insert `[REVISED — see Role 2]` in the VERDICT block adjacent to the revised field. **Do this now, before Role 3 begins.**
- **Both checks must pass before Role 3 begins.**

---

**ROLE 3 — RATE LIMIT REGISTRY ANALYST**
*Sole deliverable: Ordered list of rate-limiting components with numeric thresholds and binding rationale.*

List every rate-limiting component in binding order. For each:
- Component name and type
- Numeric threshold — number and unit; [estimated] for non-public values
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding rationale: one causal sentence per component

**ROLE 3 → ROLE 4 GATE:**
- *Deliverable check*: every component has a numeric threshold with unit and a binding-order rationale sentence; at least one component addresses the VERDICT Binding Constraint.
- *Verdict-currency check*: does Role 3 confirm, extend, or contradict the VERDICT Binding Constraint? If the registry reveals a different binding component or a different threshold at the stated load:
  - Update the VERDICT Binding Constraint field.
  - Insert `[REVISED — see Role 3]` adjacent to the Binding Constraint label in the VERDICT block.
  - **Do this now, before Role 4 begins.**
- **Both checks must pass before Role 4 begins.**

---

**ROLE 4 — CAUSAL PROPAGATION TRACER**
*Sole deliverable: Directed hop chain from binding constraint to user-observable effect, minimum two hops.*

Starting from Role 3's binding constraint: trace throttle propagation through at least two directed hops. Each hop must name the mechanism — queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade — and the destination component. Chain terminates at a user-observable effect.

**ROLE 4 → ROLE 5 GATE:**
- *Deliverable check*: at least two hops documented, each with a source component, named mechanism, and destination with observable effect.
- *Verdict-currency check*: does Role 4 reveal a propagation chain that changes the VERDICT System Status classification? If Role 4 shows cascading failure reaching user-visible tiers at 1x load when VERDICT said DEGRADED:
  - Update the VERDICT System Status.
  - Insert `[REVISED — see Role 4]` adjacent to the System Status label in the VERDICT block.
  - **Do this now, before Role 5 begins.**
- **Both checks must pass before Role 5 begins.**

---

**ROLE 5 — BURST PATH AUDITOR**
*Sole deliverable: Per-path audit with STRUCTURAL/INCIDENTAL/PROTECTED classification; VERDICT Primary Gap addressed.*

For each trigger and action capable of generating concurrent requests: verify three controls (concurrency cap set below limit | Retry-After retry policy reading the header | queue buffer between source and rate-limited endpoint). Classify unprotected paths as STRUCTURAL or INCIDENTAL (name the bypass condition). Higher-tier controls do not protect this path.

**ROLE 5 → ROLE 6 GATE:**
- *Deliverable check*: at least one path classified STRUCTURAL or INCIDENTAL with justification; VERDICT Primary Gap confirmed or revised.
- *Verdict-currency check*: does Role 5 reveal that the VERDICT Primary Gap names the wrong component or wrong gap type?
  - Update the VERDICT Primary Gap.
  - Insert `[REVISED — see Role 5]` adjacent to the Primary Gap label.
  - **Do this now, before Role 6 begins.**
- **Both checks must pass before Role 6 begins.**

---

**ROLE 6 — UX TIER ANALYST**
*Sole deliverable: UX per-tier catalog using the four-field template, minimum two tiers.*

For each throttle tier reached at any volume band: apply this template per tier. **Fewer than four fields per tier fails the template. Prose that covers all four topics without the labeled structure fails.**

```
Tier [N — name and error code]:
  (a) Error code or platform signal: [specific HTTP status code or platform signal identifier]
  (b) User-visible behavior: [what the user observes or experiences]
  (c) Visibility level: [explicit and user-visible | silent and background]
  (d) Recovery path: [manual retry | automatic exponential backoff | permanent failure | other]
```

**ROLE 6 → ROLE 7 GATE:**
- *Deliverable check*: at least two tiers documented with all four template fields (a)–(d).
- *Verdict-currency check*: does Role 6 show the user experiences a silent permanent failure at 1x load when VERDICT classifies the system as DEGRADED? If UX evidence changes the VERDICT System Status:
  - Update the VERDICT System Status.
  - Insert `[REVISED — see Role 6]` adjacent to the System Status label.
  - **Do this now, before Role 7 begins.**
- **Both checks must pass before Role 7 begins.**

---

**ROLE 7 — RETRY-AFTER INSPECTOR**
*Sole deliverable: Per-connector Retry-After evaluation with failure modes named.*

For each connector and HTTP action: state whether it reads and honors Retry-After headers (`Retry-After`, `Retry-After-Ms`, `x-ms-ratelimit-remaining`). For each gap: name the failure mode — immediate retry storm / permanent failure after N retries / silent drop / exponential backoff ignoring header value.

**ROLE 7 → ROLE 8 GATE:**
- *Deliverable check*: every connector and HTTP action evaluated; each gap has a named failure mode.
- *Verdict-currency check*: does Role 7 reveal that the dominant gap is RETRY-AFTER MISSING when VERDICT Primary Gap says UNPROTECTED BURST PATH (or vice versa)?
  - Update the VERDICT Primary Gap type if wrong.
  - Insert `[REVISED — see Role 7]` adjacent to the Primary Gap label.
  - **Do this now, before Role 8 begins.**
- **Both checks must pass before Role 8 begins.**

---

**ROLE 8 — CASCADE SCENARIO CONSTRUCTOR**
*Sole deliverable: One specific cascade with two named tiers, explicit causal link, and compounding effect.*

Construct one cascade where throttling at the Role 3 binding constraint causally triggers a second throttle at a different tier. Two independent limits hit under load do not qualify. State the causal link explicitly.

**ROLE 8 → ROLE 9 GATE:**
- *Deliverable check*: two distinct tiers named; causal link stated explicitly; compounding effect described.
- *Verdict-currency check*: does the cascade scenario change the VERDICT System Status? A cascade reaching a third tier at 1x load may indicate the system is FAILING, not DEGRADED.
  - Update the VERDICT System Status if warranted.
  - Insert `[REVISED — see Role 8]` adjacent to the System Status label.
  - **Do this now, before Role 9 begins.**
- **Both checks must pass before Role 9 begins.**

---

**ROLE 9 — THROUGHPUT ANALYST**
*Sole deliverable: Volume-to-Behavior Map using FORMAT CONTRACT schema, with step-by-step arithmetic in the 5x BASELINE cell.*

Use the FORMAT CONTRACT column schema. Volume bands: 1x, 2x, 5x. Fill BASELINE and PROTECTED for each band.

**For the 5x BASELINE cell — Rejection Clause B applies. Show the five-step derivation chain:**
```
  (1) [1x req/min from scenario] × 5 = [peak] req/min
  (2) [peak] − [limit: Role 3 component name, N req/min] = [overflow] req/min
  (3) [overflow] × [retry_factor] = [total_attempts] req/min
  (4) ([total_attempts] − [capacity = limit]) / [total_attempts] = [failure_rate]
  (5) [failure_rate] × 100 = [failure_pct]%
Conclusion: [failure_pct]% fail after retries; [queue_pct]% queue beyond 30s.
```
A conclusion without steps fails Rejection Clause B. The 5x PROTECTED cell shows the updated arithmetic with Role 10 mitigations.

**ROLE 9 → ROLE 10 GATE:**
- *Deliverable check*: all three volume bands have BASELINE and PROTECTED filled; 5x BASELINE shows the five-step derivation chain with operands referencing Role 3; no qualitative-only cell at 5x.
- *Verdict-currency check*: does Role 9 arithmetic show failure at 1x load when VERDICT said DEGRADED, or safety at 5x when VERDICT said FAILING?
  - Update the VERDICT System Status to match the arithmetic finding.
  - Insert `[REVISED — see Role 9]` adjacent to the System Status label.
  - **Do this now, before Role 10 begins.**
- **Both checks must pass before Role 10 begins.**

---

**ROLE 10 — MITIGATION ARCHITECT**
*Sole deliverable: Per-finding mitigation table using FORMAT CONTRACT schema.*

For each bottleneck (Role 3) and unprotected burst path (Role 5), one row:

| Finding | BASELINE | PROTECTED | Delta |
|---------|----------|-----------|-------|

- BASELINE: specific behavior at this bottleneck before any fix, tied to this component and load condition.
- PROTECTED: behavior after the specific mitigation — name the exact action, connector setting, or parameter.
- Delta: measurable change in throughput, error rate, or queue depth derivable from Role 9 arithmetic.

Generic advice ("add retry logic") without naming the specific control and location fails Rejection Clause A.

**ROLE 10 TERMINAL CHECK:**
- *Deliverable check*: every bottleneck and unprotected path has a row with scenario-specific BASELINE, named PROTECTED, and measurable Delta.
- *Verdict-currency check*: does Role 10 reveal any finding that was missed in Roles 3–9 and that would change a VERDICT claim?
  - Update the VERDICT field if warranted.
  - Insert `[REVISED — see Role 10]` adjacent to the revised field label.
- *Final verification*: scan the VERDICT block. Any field without a confirming or revising evidence note (confirmed by a Role N) fails reconciliation. Note the gap explicitly.

---

## V-05

**Variation axis (combined):** All three R4 excellence signals unified: full gate chain closure (C-21) + gate-checkpoint Verdict currency (C-22) + DERIVATION CHAIN as a mandatory Format Contract column (C-20) + four-field UX tier template (C-19) + INERTIA/PROTECTED framing throughout (C-12, C-14). INERTIA names the status-quo competitor state explicitly in the Format Contract, making the dual-state volume mapping and baseline-delta mitigation structural necessities rather than optional enhancements.

**Hypothesis:** Maximum composite across all 22 criteria requires C-20, C-21, and C-22 to be enforced simultaneously, each structurally rather than advisory. V-04 achieves C-21 + C-22. Adding the DERIVATION CHAIN column from V-02 achieves C-20 in the same structural register — a missing derivation chain is a column-level violation, not a per-role instruction. INERTIA framing drives C-12 (INERTIA vs. PROTECTED is the document schema, not an add-on), C-14 (every mitigation explicitly names the INERTIA behavior it replaces), and C-16 (the Format Contract declares INERTIA as the named baseline state). The four-field UX template (C-19) is double-anchored: declared in the Format Contract and enforced inline in the producing role. Every structural element serves multiple criteria simultaneously, making the prompt efficient without sacrificing coverage.

---

You are executing a multi-role throughput simulation of a rate-limited Power Automate / Connectors system. The simulation compares two named states throughout:

- **INERTIA** — the system as it currently exists, with no additional protections applied. Every failure this analysis finds is an INERTIA failure.
- **PROTECTED** — the system with the mitigations proposed in Role 10 applied. Every improvement is a move from INERTIA toward PROTECTED.

Every table, every mitigation row, and every quantified cell shows what changes between INERTIA and PROTECTED. **Each role transition is gated. A gate has two parts: (1) deliverable check, (2) Verdict-currency check. Both parts must pass before the next role begins.**

---

**ROLE 1 — VERDICT AUTHOR**
*Sole deliverable: VERDICT block with three INERTIA-state labeled fields.*

```
## VERDICT

**Binding Constraint (INERTIA)**: [Component name] — [numeric threshold, unit required] —
exhausted at [X req/min] in the INERTIA state because [one causal sentence].

**Primary INERTIA Gap**: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific
action or connector name]: [one sentence — what structural control is absent in the INERTIA
state on this path, not at a higher tier].

**INERTIA System Status**: [SAFE | DEGRADED | FAILING] at stated load. [One sentence.]
```

Self-contained: a reader who reads only the VERDICT knows the INERTIA failure mode, the gap location, and the operational status without proceeding.

**ROLE 1 → ROLE 2 GATE:**
- *Deliverable check*: all three VERDICT fields written; Binding Constraint contains number + unit; Primary Gap names a specific component; System Status is SAFE/DEGRADED/FAILING.
- *Verdict-currency check*: no prior roles; automatically satisfied.

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Sole deliverable: FORMAT CONTRACT declaring INERTIA/PROTECTED/DERIVATION CHAIN column schema, scenario-specific definitions, and two rejection clauses.*

```
## FORMAT CONTRACT

Column schema for all comparative tables in this document:
| [row key] | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |

INERTIA: [scenario-specific — describe the system in its current state, naming the specific
components and the absent controls. This is the state the VERDICT describes. Every failure
mode found in Roles 3–10 is an INERTIA failure.]

PROTECTED: [scenario-specific — describe the system after Role 10 mitigations are applied,
naming the type and location of protections that move the system from INERTIA toward safety.]

DERIVATION CHAIN: This column contains the step-by-step arithmetic for every quantified cell:
  Step 1: req/min at 1x × load_multiplier = peak_req/min
  Step 2: peak_req/min − rate_limit [cite Role 3 component name + N req/min] = overflow_req/min
  Step 3: overflow_req/min × retry_factor = total_attempts/min
  Step 4: (total_attempts − capacity) / total_attempts = failure_rate
  Step 5: failure_rate × 100 = failure_pct %
  [Conclusion: failure_pct% fail; queue_pct% queue >30s]

Rejection Clause A — Structure: Any comparative table omitting INERTIA or PROTECTED is marked
INCOMPLETE. INCOMPLETE tables must be revised before this analysis is final.

Rejection Clause B — Arithmetic: Any DERIVATION CHAIN cell at 5x that states a conclusion
without showing all five derivation steps is marked INCOMPLETE. Each step must reference a
specific value from the Role 3 registry. Being reconstructible by the reader does not satisfy
this clause; the steps must be present in the cell. At least two distinct tables must comply
with the full five-column schema.

UX Tier Template (applies to Role 6): The UX section applies this four-field structure to
each tier. A tier described with fewer than four fields fails the template:
  (a) Error code or platform signal: [specific code or signal identifier]
  (b) User-visible behavior: [what the user observes]
  (c) Visibility level: [explicit and user-visible | silent and background]
  (d) Recovery path: [manual retry | automatic backoff | permanent failure | other]
```

**ROLE 2 → ROLE 3 GATE:**
- *Deliverable check*: FORMAT CONTRACT written; INERTIA and PROTECTED definitions are scenario-specific; both Rejection Clauses present with five-step arithmetic template in Clause B; UX Tier Template declared.
- *Verdict-currency check*: does the INERTIA definition in the Format Contract conflict with the VERDICT Binding Constraint or Primary Gap framing? If the named components differ, reconcile now. Insert `[REVISED — see Role 2]` in VERDICT if any field updates. **Do this now.**

---

**ROLE 3 — INERTIA RATE LIMIT REGISTRY**
*Sole deliverable: Ordered list of rate-limiting components in the INERTIA state.*

List every rate-limiting component in binding order for the INERTIA state. For each:
- Component name and type
- Numeric threshold — number and unit; [estimated] for non-public values
- Scope (per-connection / per-environment / per-flow / per-tenant)
- INERTIA binding order rationale: one causal sentence per component

**ROLE 3 → ROLE 4 GATE:**
- *Deliverable check*: every component has numeric threshold + unit + binding rationale; at least one component addresses VERDICT Binding Constraint.
- *Verdict-currency check*: does Role 3 reveal a different INERTIA binding component than the VERDICT names? If so: update VERDICT Binding Constraint and insert `[REVISED — see Role 3]` in VERDICT now, before Role 4 begins.

---

**ROLE 4 — INERTIA BACKPRESSURE CHAIN**
*Sole deliverable: Directed hop chain from INERTIA binding constraint to user-observable effect.*

Trace INERTIA state propagation: at least two directed hops, each with a named mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade), terminating at a user-observable effect. This documents the INERTIA failure chain.

**ROLE 4 → ROLE 5 GATE:**
- *Deliverable check*: at least two hops documented with named mechanisms and terminal user-observable effect.
- *Verdict-currency check*: does Role 4 backpressure chain change the INERTIA System Status in the VERDICT? If cascading failure reaches user tiers at 1x load: update VERDICT System Status and insert `[REVISED — see Role 4]` now.

---

**ROLE 5 — INERTIA BURST PATH AUDIT** *(FORMAT CONTRACT five-column schema)*
*Sole deliverable: Per-path INERTIA audit table with STRUCTURAL/INCIDENTAL classification.*

Use the FORMAT CONTRACT schema. For each trigger or action capable of generating concurrent requests:

| Path | INERTIA Controls | INERTIA Gap Type | PROTECTED Controls | DERIVATION CHAIN | Delta |
|------|-----------------|-----------------|-------------------|-----------------|-------|

- INERTIA Controls: mark each of the three controls PRESENT or ABSENT in the INERTIA state (1. concurrency cap below rate limit, 2. Retry-After retry policy, 3. queue buffer)
- INERTIA Gap Type: STRUCTURAL (no mechanism on this path in INERTIA) or INCIDENTAL (mechanism exists but bypassed — name the condition) or PROTECTED (all three present in INERTIA)
- PROTECTED Controls: what the PROTECTED state adds to close the INERTIA gap
- DERIVATION CHAIN: if any mitigation changes a rate or retry factor, show the arithmetic delta
- Delta: measurable improvement

This role must confirm or revise the VERDICT Primary INERTIA Gap.

**ROLE 5 → ROLE 6 GATE:**
- *Deliverable check*: at least one path classified STRUCTURAL or INCIDENTAL; VERDICT Primary Gap addressed.
- *Verdict-currency check*: does Role 5 reveal a different primary gap location or type? Update VERDICT Primary Gap and insert `[REVISED — see Role 5]` now.

---

**ROLE 6 — UX TIER ANALYST (INERTIA STATE)**
*Sole deliverable: UX per-tier catalog using the Format Contract four-field template.*

For each tier reached in the INERTIA state at any volume band: apply the FORMAT CONTRACT UX Tier Template. **Fewer than four fields per tier fails the template. Free prose fails even if all four topics are mentioned.**

At least two distinct INERTIA tiers. This section documents the observable cost of the INERTIA state.

**ROLE 6 → ROLE 7 GATE:**
- *Deliverable check*: at least two tiers documented with all four template fields (a)–(d).
- *Verdict-currency check*: does Role 6 UX evidence change the INERTIA System Status classification? (e.g., tiers show silent permanent failure at 1x when VERDICT says DEGRADED) Update VERDICT System Status and insert `[REVISED — see Role 6]` now.

---

**ROLE 7 — RETRY-AFTER INSPECTOR (INERTIA STATE)**
*Sole deliverable: Per-connector Retry-After evaluation with INERTIA failure modes named.*

For each connector and HTTP action: does the INERTIA state read and honor Retry-After (`Retry-After`, `Retry-After-Ms`, `x-ms-ratelimit-remaining`)? For each INERTIA gap: name the failure mode — immediate retry storm / permanent failure after N retries / silent drop / backoff ignoring header value. PROTECTED state fixes belong in Role 10.

**ROLE 7 → ROLE 8 GATE:**
- *Deliverable check*: every connector and HTTP action evaluated; each gap has a named INERTIA failure mode.
- *Verdict-currency check*: does Role 7 reveal the dominant INERTIA gap is RETRY-AFTER MISSING when VERDICT Primary Gap says UNPROTECTED BURST PATH? Update VERDICT Primary INERTIA Gap type and insert `[REVISED — see Role 7]` now.

---

**ROLE 8 — CASCADE SCENARIO (INERTIA STATE)**
*Sole deliverable: One INERTIA cascade with two named tiers, explicit causal link, compounding effect.*

In the INERTIA state: construct one cascade where throttling at the Role 3 binding constraint causally triggers a second distinct throttle at a different tier. Show compounding effect. Two independent limits hit under load do not qualify.

**ROLE 8 → ROLE 9 GATE:**
- *Deliverable check*: two tiers named; causal link explicit; compounding effect described.
- *Verdict-currency check*: does the INERTIA cascade change the INERTIA System Status? Update VERDICT and insert `[REVISED — see Role 8]` now.

---

**ROLE 9 — THROUGHPUT ANALYST (INERTIA vs PROTECTED)** *(FORMAT CONTRACT five-column schema)*
*Sole deliverable: Volume-to-Behavior Map comparing INERTIA and PROTECTED states with arithmetic trace at 5x.*

Use the FORMAT CONTRACT column schema. Volume bands: 1x, 2x, 5x.

| Volume | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |
|--------|---------|-----------|-----------------|-------|

**For the 5x INERTIA/DERIVATION CHAIN cell — Rejection Clause B applies. Show all five steps:**
```
  Step 1: [1x_req/min] × 5 = [peak] req/min
  Step 2: [peak] − [Role 3 binding component: N req/min] = [overflow] req/min
  Step 3: [overflow] × [retry_factor] = [total_attempts] req/min
  Step 4: ([total_attempts] − [capacity]) / [total_attempts] = [failure_rate]
  Step 5: [failure_rate] × 100 = [failure_pct]%
  INERTIA conclusion: [failure_pct]% fail; [queue_pct]% queue >30s
```

The 5x PROTECTED DERIVATION CHAIN cell shows the same five steps with updated values reflecting Role 10 mitigations. A 5x cell stating only a percentage without the derivation steps fails Rejection Clause B.

**ROLE 9 → ROLE 10 GATE:**
- *Deliverable check*: all three bands filled; 5x INERTIA DERIVATION CHAIN shows five steps referencing Role 3 values; 5x PROTECTED DERIVATION CHAIN shows updated steps; no qualitative-only quantified cell at 5x.
- *Verdict-currency check*: does Role 9 arithmetic contradict the INERTIA System Status in the VERDICT? Update VERDICT System Status and insert `[REVISED — see Role 9]` now.

---

**ROLE 10 — MITIGATION ARCHITECT (INERTIA → PROTECTED)** *(FORMAT CONTRACT five-column schema)*
*Sole deliverable: Per-finding mitigation table showing INERTIA-to-PROTECTED transition.*

For each bottleneck (Role 3) and burst path (Role 5), one row:

| Finding | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |
|---------|---------|-----------|-----------------|-------|

- INERTIA: what the system does at this bottleneck in the INERTIA state, specific to this component and load condition — not generic.
- PROTECTED: what the system does after the specific mitigation — name the exact action, connector, or setting changed (e.g., "concurrency control on For Each action, Degree of Parallelism = 5", not "add concurrency control").
- DERIVATION CHAIN: if the mitigation changes a rate limit or retry factor, show the updated arithmetic using the five-step format from the Format Contract. If the change is structural (not arithmetic), note "structural change — arithmetic delta in Role 9 5x PROTECTED cell."
- Delta: measurable improvement in throughput, error rate, or queue depth, derivable from Role 9 arithmetic.

**ROLE 10 TERMINAL CHECK:**
- *Deliverable check*: every bottleneck and burst path has a row; every INERTIA cell names the component and condition; every PROTECTED cell names the exact control and location; every DERIVATION CHAIN cell at 5x shows steps or a valid structural-change note; every Delta is measurable.
- *Verdict-currency check*: does Role 10 reveal any finding that changes a VERDICT claim? Update VERDICT and insert `[REVISED — see Role 10]` now.
- *Final verification*: scan the VERDICT block. Every field must have either (a) confirming evidence from at least one Role or (b) a `[REVISED — see Role N]` marker pointing to the revising role. A VERDICT claim with no marker and no confirming Role note fails reconciliation.
