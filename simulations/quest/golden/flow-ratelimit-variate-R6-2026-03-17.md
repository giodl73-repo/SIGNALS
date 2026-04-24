---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 6
rubric_version: 6
---

# flow-ratelimit — Variate R6

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence — full gate chain + DERIVATION CHAIN as Rejection Clause C), V-02 (output format — DERIVATION CHAIN as mandatory 4th schema column, primary structural discipline), V-03 (phrasing register — imperative column-compliance language with per-table structural audits).
Combination variations: V-04 (role sequence + schema column — full gate chain C-21 + C-23 schema-column enforcement), V-05 (all three + gate-checkpoint Verdict currency C-22 + inertia framing).

**R6 target: C-23 (Schema-column Arithmetic Enforcement)**

C-23 was extracted from R5 V-02's excellence signal: declaring DERIVATION CHAIN as a mandatory 4th schema column in the Format Contract makes arithmetic gaps structurally visible as blank required cells at scan time, without requiring prose reading. R5 V-02 introduced this pattern; it is now codified as C-23 with the pass condition: (a) Format Contract declares DERIVATION CHAIN as a mandatory structural column alongside BASELINE and PROTECTED, (b) rejection clause flags blank DERIVATION CHAIN cells as structural omissions (not content violations), (c) at least two distinct quantified tables comply with the full schema including populated derivation cells.

**R6 variation axes:**

| Axis | What changes |
|------|-------------|
| Role sequence | Which roles run first; where Format Contract + DERIVATION CHAIN schema is declared |
| Output format / schema-column | DERIVATION CHAIN as 4th column vs rejection-clause-B enforcement — both target C-20/C-23, structural vs instructional |
| Phrasing register | Imperative structural commands ("COLUMN REQUIRED: DERIVATION CHAIN") vs declarative contract prose |
| Inertia framing | Inertia state named as the baseline competitor — its delta drives the DERIVATION CHAIN computation |
| Gate-checkpoint Verdict currency | C-22 target: revision markers inserted at gate boundary, not deferred |

---

## V-01

**Variation axis:** Role sequence — VERDICT-first, full gate chain (C-21), DERIVATION CHAIN as Rejection Clause C in the Format Contract. Eleven roles total; every analysis-body role transition (Roles 3–10) is gated with named deliverables from the prior role. The Format Contract introduces three rejection clauses: Clause A (BASELINE/PROTECTED structure), Clause B (five-step arithmetic derivation must appear in the cell), Clause C (DERIVATION CHAIN column must be present as a named column in every table that contains quantified estimates — its absence is a structural omission, not a content gap).

**Hypothesis:** C-23 requires the DERIVATION CHAIN to be a mandatory structural *column* declared in the Format Contract schema — not merely a content requirement per role. Adding it as Rejection Clause C (column presence check) alongside Clause A (column structure) enforces C-23 structurally: a table missing the DERIVATION CHAIN column is as incomplete as a table missing BASELINE, and the violation is scan-visible. Clause B (from R5-V-01) enforces C-20 at the content level — the cell must show steps. Clauses B and C together enforce both C-20 (arithmetic content) and C-23 (schema-column structure). Full gate chain (C-21) closes all transitions; gate-checkpoint currency is not the primary axis here (terminal reconciliation satisfies C-18).

---

You are a Connectors / Power Automate throughput domain expert running an eleven-role rate-limit throughput simulation. Roles execute in strict sequence. Each role's named deliverables gate the next role. Do not open a role's output section until the prior role's gate is cleared.

---

**ROLE 1 — VERDICT AUTHOR**
*Pre-commitment from domain knowledge. No evidence sections may precede this role.*
*Gate: Do not open Role 2 until VERDICT block is written with all three fields non-empty.*

Write the VERDICT block now — before any rate limit inventory, burst path audit, or volume table.

```
## VERDICT

Binding Constraint: [Component name] — [numeric threshold, unit required] — binding at
[X req/min] because [one causal sentence: why this component's limit is reached before all
others at the stated load].

Primary Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] — at [specific action
or connector name]: [one sentence: what structural control is absent on this path and why
it is not present here, not at a higher tier].

System Status: [SAFE | DEGRADED | FAILING] at the stated load. [One sentence justification.]
```

Rules:
- Binding Constraint must include a number and unit. "Limited throughput" without a threshold fails.
- Primary Gap must name the specific component or action. "The flow lacks retry logic" without a location fails.
- System Status must be one of: SAFE / DEGRADED / FAILING.
- Self-contained: a reader who reads only the VERDICT knows the binding component, gap location, and operational status without proceeding further.

**ROLE 1 GATE: Do not open Role 2 until Binding Constraint (with number + unit), Primary Gap (with named component), and System Status (SAFE/DEGRADED/FAILING) are all non-empty.**

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Gate requires: VERDICT block present with all three fields non-empty.*
*Gate: Do not open Role 3 until FORMAT CONTRACT is written with all three rejection clauses present.*

Write the FORMAT CONTRACT before any analysis section.

```
## FORMAT CONTRACT

Column schema for every comparative table in this document:
| [row key] | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |

BASELINE: [scenario-specific — describe the system in its current state: which components
are present, which controls are absent, how the system behaves under load today. Not a
generic definition.]

PROTECTED: [scenario-specific — describe the system after Role 10 mitigations are applied:
which controls are added, at which components, what changes in behavior under the same load.
Not a generic definition.]

DERIVATION CHAIN: Step-by-step arithmetic for every quantified cell:
  Step 1: baseline_req/interval × load_multiplier = peak_req/interval
  Step 2: peak_req/interval − rate_limit [cite: component name, N, from Role 3 registry] = overflow
  Step 3: overflow × retry_amplification_factor = total_attempt_req/interval
  Step 4: (total_attempt_req − capacity) / total_attempt_req = failure_rate
  Step 5: failure_rate × 100 = failure_pct

Rejection Clause A — Structure: Any comparative table in this document that omits the
BASELINE or PROTECTED column is marked INCOMPLETE and must be revised before this analysis
is considered final.

Rejection Clause B — Arithmetic content: Any DERIVATION CHAIN cell that states a conclusion
(e.g., "42% fail") without the step-by-step derivation shown above is marked INCOMPLETE.
The derivation steps must appear in the cell. Being reconstructible by an attentive reader
does not satisfy this clause; each step must be present.

Rejection Clause C — Schema-column presence: Any comparative table that contains quantified
estimates but omits the DERIVATION CHAIN column entirely is marked STRUCTURALLY INCOMPLETE.
A STRUCTURALLY INCOMPLETE table is a schema violation, not a content gap — it is visible at
scan time without reading the cell values. At least two distinct tables in this document must
include the DERIVATION CHAIN column with all quantified cells populated.
```

**ROLE 2 GATE: Do not open Role 3 until: (a) FORMAT CONTRACT is written; (b) BASELINE and PROTECTED definitions are scenario-specific; (c) all three rejection clauses are present with the five-step arithmetic template in Clause B.**

---

**ROLE 3 — RATE LIMIT REGISTRY ANALYST**
*Gate requires: FORMAT CONTRACT written with Clauses A, B, and C present.*
*Gate: Do not open Role 4 until all components have numeric thresholds and at least one addresses the VERDICT Binding Constraint.*

List every rate-limiting component in binding order — most constrained at the stated load first. For each:
- Component name and type (connector / platform runtime / environment governor / per-tenant limit)
- Numeric threshold — number and unit required; mark [estimated] for any non-public value
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding order rationale: one causal sentence per component

At least one component must confirm, extend, or revise the VERDICT Binding Constraint.

**ROLE 3 GATE: Do not open Role 4 until: (a) every component has a row with numeric threshold + unit; (b) every row has a binding-order rationale sentence; (c) at least one row addresses the VERDICT Binding Constraint. After clearing: does Role 3 confirm, extend, or revise the VERDICT Binding Constraint? If it revises, insert `[REVISED — see Role 3]` in the VERDICT block Binding Constraint field before proceeding.**

---

**ROLE 4 — CAUSAL PROPAGATION TRACER**
*Gate requires: Rate Limit Registry with numeric thresholds and at least one row addressing the VERDICT Binding Constraint.*
*Gate: Do not open Role 5 until the propagation chain has at least two hops with named mechanisms.*

Trace from the binding constraint through at least two directed hops:

```
[Component] --[mechanism]--> [Component] --[mechanism]--> [user-observable effect]
```

Named mechanisms only (no substitutes): queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade.

**ROLE 4 GATE: Do not open Role 5 until: (a) at least two hops are present, each referencing a Role 3 component; (b) each hop names a mechanism from the permitted set; (c) the chain terminates at a user-observable effect.**

---

**ROLE 5 — BURST PATH AUDITOR**
*Gate requires: Propagation chain with at least two hops and named mechanisms.*
*Gate: Do not open Role 6 until at least one unprotected path is classified and VERDICT Primary Gap is confirmed or revised.*

For each trigger and action capable of generating concurrent requests, apply the three-control checklist:
1. Concurrency cap — present and set below the rate limit?
2. Retry-After retry policy — present and reading the response header?
3. Queue buffer — present between the source and the rate-limited endpoint?

For each unprotected path, classify:
- **STRUCTURAL**: no mechanism exists on this path in the current system.
- **INCIDENTAL**: mechanism exists but is bypassed, misconfigured, or absent only under specific conditions — name the exact bypass condition.

Controls at a higher tier do not protect this path. "Controls exist somewhere in the system" fails.

**ROLE 5 GATE: Do not open Role 6 until: (a) at least one path has a STRUCTURAL or INCIDENTAL classification with justification; (b) VERDICT Primary Gap field is confirmed or revised. If Role 5 reveals a different primary gap, insert `[REVISED — see Role 5]` in the VERDICT block Primary Gap field before proceeding.**

---

**ROLE 6 — RETRY-AFTER INSPECTOR**
*Gate requires: Burst path audit with at least one classified unprotected path and VERDICT Primary Gap addressed.*
*Gate: Do not open Role 7 until every connector and HTTP action has been evaluated.*

For each connector and HTTP action: state whether it reads and honors Retry-After headers (`Retry-After`, `Retry-After-Ms`, `x-ms-ratelimit-remaining`). For each gap, name the failure mode precisely: immediate retry storm / permanent failure after N retries / silent drop / exponential backoff ignoring the header value.

**ROLE 6 GATE: Do not open Role 7 until: (a) every connector and HTTP action has an entry; (b) each gap entry names the specific failure mode from the permitted set. After clearing: does Role 6 revise the VERDICT Primary Gap? If so, insert `[REVISED — see Role 6]` before proceeding.**

---

**ROLE 7 — CASCADE SCENARIO CONSTRUCTOR**
*Gate requires: Retry-After inspection complete with failure modes named for all gaps.*
*Gate: Do not open Role 8 until the cascade names both tiers, the causal link, and the compounding effect.*

Construct one specific cascade scenario where throttling at the Role 3 binding constraint causally triggers a second distinct throttle event at a different tier. Two independent limits both hit under load do not constitute a cascade — the second must be caused by the first.

State:
- Tier 1: [component + threshold + trigger condition]
- Causal link: [how Tier 1 throttling produces load on Tier 2 — explicit mechanism]
- Tier 2: [different component + different threshold]
- Compounding effect: [numeric degradation in throughput or error rate]

**ROLE 7 GATE: Do not open Role 8 until: (a) two distinct tiers are named, both traceable to Role 3 registry entries; (b) the causal link from Tier 1 to Tier 2 is stated explicitly; (c) the compounding effect includes a numeric estimate.**

---

**ROLE 8 — UX TIER ANALYST**
*Gate requires: Cascade scenario with two named tiers, explicit causal link, and numeric compounding effect.*
*Gate: Do not open Role 9 until at least two throttle tiers are documented with the full four-field template.*

For each throttle tier reached at any volume band: apply the four-field template. Fewer than four fields per tier fails the template requirement. Free prose covering all four topics without the template structure fails even if the content is complete.

```
Tier [N]: [component + threshold label]
  (a) Error code or platform signal: [specific code — e.g., HTTP 429 with Retry-After header,
      ActionThrottled event in run history, connector TL-0001 signal]
  (b) User-visible behavior: [what the user observes or experiences — specific to this tier]
  (c) Visibility level: [user-visible and explicit | background-only and silent]
  (d) Recovery path: [manual retry available | automatic exponential backoff | permanent
      failure with no recovery | other — specify]
```

At least two distinct tiers must use this template.

**ROLE 8 GATE: Do not open Role 9 until at least two tiers have all four labeled fields (a)–(d).**

---

**ROLE 9 — THROUGHPUT ANALYST**
*Gate requires: UX catalog with at least two tiers using the four-field template.*
*Gate: Do not open Role 10 until the Volume-to-Behavior Map is complete with DERIVATION CHAIN column present and all quantified cells populated.*

Produce the Volume-to-Behavior Map using the FORMAT CONTRACT five-column schema.

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|------------------|-------|
| 1x     |          |           |                  |       |
| 2x     |          |           |                  |       |
| 5x     |          |           |                  |       |

**FORMAT CONTRACT Rejection Clauses A, B, and C all apply to this table.**

For the 5x BASELINE DERIVATION CHAIN cell — the full five-step arithmetic chain must appear in the cell:
```
Step 1: [1x req/min] × 5 = [5x req/min] peak
Step 2: [5x req/min] − [rate_limit from Role 3: component name, N req/min] = [overflow] req/min
Step 3: [overflow] × [retry_factor, e.g., 3] = [total_attempts] req/min
Step 4: ([total_attempts] − [capacity = role3_limit]) / [total_attempts] = [failure_rate]
Step 5: [failure_rate] × 100 = [failure_pct]% fail after retries exhaust
```
Each operand must reference a specific Role 3 value. A cell showing only "42% fail" fails Rejection Clause B even if arithmetically correct. Omitting the DERIVATION CHAIN column entirely fails Rejection Clause C.

For the 5x PROTECTED cell, show how failure_pct changes with Role 10 mitigations applied; use the same five-step format with updated operands.

**ROLE 9 GATE: Do not open Role 10 until: (a) all three volume bands have BASELINE, PROTECTED, and DERIVATION CHAIN columns filled; (b) the 5x BASELINE DERIVATION CHAIN cell contains the five-step chain with Role 3 operands; (c) the DERIVATION CHAIN column header is present. A table missing the DERIVATION CHAIN column fails Rejection Clause C.**

---

**ROLE 10 — MITIGATION ARCHITECT**
*Gate requires: Volume-to-Behavior Map with all bands filled and 5x BASELINE derivation chain present.*
*Gate: Do not open Role 11 until every bottleneck has a mitigation row using the FORMAT CONTRACT schema.*

Use the FORMAT CONTRACT five-column schema for each finding from Roles 3 and 5:

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|------------------|-------|

- BASELINE: specific behavior at this bottleneck before any fix — named to this component and load condition.
- PROTECTED: behavior after the specific mitigation — name the exact action, connector setting, or parameter changed.
- DERIVATION CHAIN: if the mitigation changes a numeric limit or retry factor, show the updated arithmetic in the same five-step format.
- Delta: measurable change in throughput, error rate, or queue depth.

Generic advice without naming the specific control and its location fails Rejection Clause A.

**ROLE 10 GATE: Do not open Role 11 until: (a) every bottleneck from Role 3 and every unprotected path from Role 5 has a row; (b) every PROTECTED cell names the exact action, setting, or parameter; (c) the DERIVATION CHAIN column is present in this table (Rejection Clause C); (d) every Delta cell states a measurable change.**

---

**ROLE 11 — VERDICT RECONCILER**
*Gate requires: Mitigation table complete with all findings covered.*

Scan Roles 3–10 for each VERDICT field:

1. **Binding Constraint**: Does any role confirm, extend, or contradict the stated component and threshold? If contradicted and no `[REVISED — see Role N]` marker is present in the field, insert the marker now.
2. **Primary Gap**: Do Roles 5 or 6 confirm, extend, or contradict the gap location and type? If contradicted and marker is absent, insert now.
3. **System Status**: Does Role 9 arithmetic confirm the SAFE/DEGRADED/FAILING classification? If Role 9 shows different severity and marker is absent, insert now.

State: `VERDICT RECONCILIATION COMPLETE — [CONFIRMED / N REVISIONS APPLIED]`

---

Apply all eleven roles in sequence to the rate-limited system described by the user.

---

## V-02

**Variation axis:** Output format — DERIVATION CHAIN as the primary mandatory 4th schema column in the Format Contract. This is the C-23 target variation. The Format Contract declares a four-column schema (BASELINE | PROTECTED | DERIVATION CHAIN | Delta) as the document-wide standard. A dedicated Rejection Clause flags any quantified table missing the DERIVATION CHAIN column as a structural omission — visible at scan time without reading cell values, because blank column cells are structurally evident. Gate language provides C-17 coverage for key transitions; the primary structural discipline is the schema-column enforcement, not the gate chain.

**Hypothesis:** When DERIVATION CHAIN is the primary artifact of the Format Contract — declared as the 4th column in the schema line rather than as a clause attached to an existing column — the document structure enforces it uniformly across all tables. A table author cannot omit the column without violating the declared schema. This is categorically stronger than a per-role instructional mandate (which can be satisfied or bypassed per-role) because the schema declaration is global. The Format Contract preamble itself becomes the single source of truth for column presence, and its rejection clause operates as a structural check rather than a content audit.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput behavior of the rate-limited system described by the user at 1x, 2x, and 5x nominal load.

**Produce the two preamble blocks first, before any analysis section.**

---

**PREAMBLE 1 — VERDICT**
*(write before any rate limit table, burst path audit, cascade scenario, or volume mapping)*

```
## VERDICT

Binding Constraint: [Component name] — [numeric threshold + unit] — binding at [X req/min]
because [one causal sentence: why this limit is reached before others at the stated load].

Primary Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] — Location: [specific
action or connector name] — Absence: [what structural control is missing on this path and
why it is absent here, not at a higher tier].

System Status: [SAFE | DEGRADED | FAILING] at stated load. [One sentence justification.]
```

Self-contained. A reader who reads only the VERDICT knows the binding component (with threshold), the specific gap location, and the operational status.

*Gate: Do not write PREAMBLE 2 until the VERDICT is present with all three fields non-empty.*

---

**PREAMBLE 2 — FORMAT CONTRACT**
*(write after VERDICT, before Section 1)*

```
## FORMAT CONTRACT

Document-wide column schema for all comparative and quantitative tables:
| [row key] | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |

This is a four-column schema. The DERIVATION CHAIN column is mandatory in every table that
contains quantified estimates. It is not optional.

BASELINE: [scenario-specific — the system as it exists today: name the specific components,
the controls that are absent, and the behavior under load without mitigations.]

PROTECTED: [scenario-specific — the system after Section 7 mitigations: name the protections
added, at which components, and the resulting load behavior.]

DERIVATION CHAIN: Required computation for every quantified cell. Template:
  [baseline_req/interval] × [load_multiplier] = [peak_req/interval]
  [peak_req/interval] − [rate_limit: component_name, N req/interval, from Section 1] = [overflow]
  [overflow] × [retry_factor] = [total_attempts/interval]
  ([total_attempts] − [capacity]) / [total_attempts] = [failure_rate]
  [failure_rate] × 100 = [failure_pct]

Delta: The measured change in failure_pct or throughput between BASELINE and PROTECTED.

STRUCTURAL REJECTION CLAUSE: Any table in this document that contains quantified estimates
but does not include the DERIVATION CHAIN column is structurally incomplete. A structurally
incomplete table is a schema violation — the missing column is visible without reading the
cell values. Structurally incomplete tables must be rebuilt with the correct schema before
this analysis is final. At least two distinct tables must comply with the full four-column
schema, including populated DERIVATION CHAIN cells.

CONTENT REJECTION CLAUSE: Any DERIVATION CHAIN cell that contains a conclusion without the
step-by-step computation above is a content violation. Conclusion without derivation fails
even if the conclusion is arithmetically correct.
```

*Gate: Do not write Section 1 until the FORMAT CONTRACT is present with (a) the four-column schema declared, (b) BASELINE and PROTECTED definitions are scenario-specific, (c) the STRUCTURAL REJECTION CLAUSE names the DERIVATION CHAIN column specifically, and (d) the CONTENT REJECTION CLAUSE is present.*

---

**Section 1 — Rate Limit Registry**

List every rate-limiting component in binding order. For each:
- Component name and type (connector / platform runtime / environment governor / tenant limit)
- Numeric threshold — number and unit required; [estimated] if non-public
- Scope (per-connection / per-environment / per-flow / per-tenant)
- Binding order rationale: one causal sentence

At least one component must confirm, extend, or revise the VERDICT Binding Constraint. If a revision is needed, insert `[REVISED — see Section 1]` in the VERDICT block Binding Constraint field before proceeding to Section 2.

---

**Section 2 — Backpressure Propagation**

Trace the causal chain from the binding constraint to user-observable effect:

```
[Component] --[mechanism]--> [Component] --[mechanism]--> [observable effect]
```

Minimum two directed hops. Named mechanisms only: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade.

---

**Section 3 — Burst Path Audit**

For each trigger and action capable of generating concurrent requests, apply three controls:
1. Concurrency cap — present and below the rate limit?
2. Retry-After policy — present and reading the response header?
3. Queue buffer — between source and rate-limited endpoint?

Classify each unprotected path:
- **STRUCTURAL**: no mechanism on this path.
- **INCIDENTAL**: mechanism exists but bypassed — name the exact bypass condition.

Confirm or revise the VERDICT Primary Gap. If revised: insert `[REVISED — see Section 3]` in the VERDICT block before proceeding.

---

**Section 4 — UX Per Throttle Tier**

Four-field template for each throttle tier reached at any load band. Template compliance is structural — fewer than four fields per tier fails even if all topics are covered in prose.

```
Tier [N]: [component + threshold label]
  (a) Error code or platform signal: [specific code or event identifier]
  (b) User-visible behavior: [what the user observes at this tier]
  (c) Visibility level: [user-visible and explicit | background-only and silent]
  (d) Recovery path: [manual retry | automatic backoff | permanent failure | other]
```

Minimum two tiers.

---

**Section 5 — Volume-to-Behavior Map** *(FORMAT CONTRACT four-column schema — STRUCTURAL REJECTION CLAUSE applies)*

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|------------------|-------|
| 1x     |          |           |                  |       |
| 2x     |          |           |                  |       |
| 5x     |          |           |                  |       |

The DERIVATION CHAIN column is mandatory in this table. Omitting it makes this table structurally incomplete per the FORMAT CONTRACT.

For the 5x DERIVATION CHAIN cell — populate the full five-step arithmetic derivation. Each step must reference a specific Section 1 value (component name and numeric threshold). A cell stating only a final percentage fails the CONTENT REJECTION CLAUSE.

For the 5x PROTECTED DERIVATION CHAIN cell — apply the same five-step format with updated operands to reflect Section 7 mitigations.

---

**Section 6 — Retry-After Handling**

For each connector and HTTP action: does it read and honor `Retry-After`, `Retry-After-Ms`, or `x-ms-ratelimit-remaining`? For each gap: name the failure mode precisely — immediate retry storm / permanent failure after N retries / silent drop / backoff ignoring header value.

If a gap revises the VERDICT Primary Gap: insert `[REVISED — see Section 6]` before proceeding.

---

**Section 7 — Mitigation Prescriptions** *(FORMAT CONTRACT four-column schema — STRUCTURAL REJECTION CLAUSE applies)*

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|------------------|-------|

The DERIVATION CHAIN column is mandatory in this table. For any mitigation that changes a numeric threshold or retry factor, populate the full five-step arithmetic with updated operands.

- BASELINE: specific behavior at this bottleneck — named to this component and load condition.
- PROTECTED: exact action, connector setting, or parameter changed.
- Delta: measurable change derivable from Section 5 arithmetic.

---

**Section 8 — Cascade Scenario**

One specific cascade: throttling at the Section 1 binding constraint causally triggers a second throttle at a different tier. Two independent limits both hit simultaneously do not qualify.

---

After Section 8: verify each VERDICT claim against Sections 1–8. For any revised claim, confirm the `[REVISED — see Section N]` marker is present in the VERDICT block.

---

## V-03

**Variation axis:** Phrasing register — imperative structural commands with column-compliance audits. Rather than a declarative contract prose preamble, every section header includes an explicit column-compliance instruction written as a direct command: "COLUMN REQUIRED: DERIVATION CHAIN. Any table in this section missing this column fails on sight." This register variation tests whether direct imperative language at each section boundary enforces C-23 more reliably than a Format Contract declared once at document head — because the command recurs at the point of production rather than requiring recall of a preamble.

**Hypothesis:** A Format Contract preamble declared once (V-02) requires the writer to remember and apply it across all subsequent tables. An imperative column-compliance command embedded in each section header that contains a table enforces C-23 locally: the command is present exactly where the table is being written, eliminating the need to recall the preamble. If C-23 failures occur because the Format Contract preamble is "forgotten" or deprioritized mid-document, per-section commands prevent that failure mode. If failures occur for other reasons (e.g., difficulty producing the arithmetic), the per-section command alone cannot prevent them — in which case the preamble approach and the per-section approach are equivalent. This variation distinguishes the two causes.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across the rate-limited system described by the user. Analyze 1x, 2x, and 5x nominal load.

Complete the sections below in order. Each section begins with its compliance requirement.

---

## VERDICT (write this first — before any other section)

State your analytical commitment before evidence:

```
Binding Constraint: [Component] — [threshold + unit] — binding at [X req/min] because
[one causal sentence].

Primary Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [named component]:
[one sentence — what is structurally absent on this path].

System Status: [SAFE | DEGRADED | FAILING] at stated load.
```

Self-contained. Sections below confirm or revise each field.

---

## Section 1 — Rate Limit Registry

**NO TABLE STRUCTURE REQUIRED IN THIS SECTION — prose inventory.**

List every rate-limiting component with: name, numeric threshold (number + unit, [estimated] if non-public), scope, binding order rationale (one sentence per component).

Confirm or revise VERDICT Binding Constraint. If revised: mark the field `[REVISED — see Section 1]`.

---

## Section 2 — Causal Chain

**NO TABLE REQUIRED — directed hop chain.**

```
[source] --[mechanism]--> [destination] --[mechanism]--> [user-observable effect]
```

Minimum two hops. Mechanisms: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade.

---

## Section 3 — Burst Path Audit

**COLUMN REQUIRED: DERIVATION CHAIN**
**Any table in this section that contains quantified estimates must include a DERIVATION CHAIN column.**
**A table missing the DERIVATION CHAIN column is incomplete — rebuild with the correct schema before proceeding.**

For each trigger and action capable of generating concurrent requests:

| Path | Concurrency Cap | Retry-After Policy | Queue Buffer | Gap Type | DERIVATION CHAIN |
|------|-----------------|-------------------|--------------|----------|------------------|

- Gap Type: STRUCTURAL (no mechanism on path) or INCIDENTAL (mechanism exists but bypassed — name the condition).
- DERIVATION CHAIN: for any path with a quantified concurrency estimate, show: concurrent_requests = trigger_frequency × processing_time_sec / 60. For qualitative-only paths, write N/A.

Confirm or revise VERDICT Primary Gap. If revised: mark `[REVISED — see Section 3]`.

---

## Section 4 — UX Per Throttle Tier

**TEMPLATE REQUIRED: four-field template per tier — not prose.**
**A tier described in prose without the template structure fails even if all four topics are addressed.**

```
Tier [N]: [component + threshold label]
  (a) Error code or platform signal: [specific identifier]
  (b) User-visible behavior: [what the user observes]
  (c) Visibility level: [user-visible and explicit | background-only and silent]
  (d) Recovery path: [manual retry | automatic backoff | permanent failure | other]
```

Minimum two tiers.

---

## Section 5 — Volume-to-Behavior Map

**COLUMN REQUIRED: DERIVATION CHAIN**
**COLUMN REQUIRED: BASELINE and PROTECTED**
**Any table in this section missing BASELINE, PROTECTED, or DERIVATION CHAIN is incomplete.**

Column definitions for this specific scenario:
- BASELINE: [name the specific components and absent controls that define today's unmitigated state]
- PROTECTED: [name the specific controls added by Section 7 and the resulting load behavior]
- DERIVATION CHAIN: step-by-step arithmetic derivation — see template below

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|------------------|-------|
| 1x     |          |           |                  |       |
| 2x     |          |           |                  |       |
| 5x     |          |           |                  |       |

**FOR THE 5x DERIVATION CHAIN CELL, populate the complete arithmetic chain:**
```
Step 1: [1x_req/min] × 5 = [peak_req/min]
Step 2: [peak_req/min] − [Section 1 registry: component name, N req/min] = [overflow_req/min]
Step 3: [overflow_req/min] × [retry_factor] = [total_attempts_req/min]
Step 4: ([total_attempts] − [capacity]) / [total_attempts] = [failure_rate]
Step 5: [failure_rate] × 100 = [failure_pct]%
```
A cell stating only the result (e.g., "42% fail") without the computation steps is incomplete.

---

## Section 6 — Retry-After Handling

**NO TABLE REQUIRED — per-connector evaluation.**

For each connector and HTTP action: reads and honors `Retry-After` / `Retry-After-Ms` / `x-ms-ratelimit-remaining`? For each gap: name the failure mode (immediate retry storm / permanent failure after N retries / silent drop / backoff ignoring header value).

Confirm or revise VERDICT Primary Gap. If revised: mark `[REVISED — see Section 6]`.

---

## Section 7 — Mitigation Prescriptions

**COLUMN REQUIRED: DERIVATION CHAIN**
**COLUMN REQUIRED: BASELINE and PROTECTED**
**Any table in this section missing these columns is incomplete — rebuild before proceeding.**

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|------------------|-------|

- BASELINE: behavior at this bottleneck today — named to this component, not generic.
- PROTECTED: exact action, setting, or parameter changed — not generic advice.
- DERIVATION CHAIN: if the mitigation changes a numeric limit or retry factor, show updated arithmetic. Write QUALITATIVE if no numeric change.
- Delta: measurable change in failure_pct or throughput.

---

## Section 8 — Cascade Scenario

**NO TABLE REQUIRED — prose scenario.**

One cascade: Tier 1 throttle causally produces Tier 2 throttle. Name both tiers (Section 1 references), the causal mechanism, the compounding effect. Two independent limits hitting under load do not qualify.

---

**After Section 8:** Verify each VERDICT field. For any revised claim without a `[REVISED — see Section N]` marker, insert the marker now.

---

## V-04

**Variation axes:** Role sequence (full gate chain, C-21) + output format (DERIVATION CHAIN as mandatory 4th schema column, C-23). This combination carries R5-V-01's full gate chain forward and replaces Rejection Clause B (instructional content mandate) with V-02's schema-column approach (structural presence mandate). The combination tests whether full gate closure + schema-column structural enforcement produces stronger C-20/C-23 compliance than either mechanism alone — because the gate forces column presence before a role completes, and the schema declaration ensures the column header appears in the correct position.

**Hypothesis:** R5-V-01 enforced C-20 through a Rejection Clause B (instructional: "the cell must show derivation steps") and R5-V-02 enforced C-23 through a schema-column declaration (structural: "the column must exist"). Neither alone fully closes both criteria: V-01 does not ensure the column is structurally declared; V-02 does not have a gate preventing the omission at section completion. V-04 combines them: the Format Contract declares the four-column schema (C-23 structural enforcement), and each role gate explicitly checks for DERIVATION CHAIN column presence before clearing (C-21 gate-level enforcement). The gate + schema combination makes both a declaration violation (missing column) and a content violation (missing steps) detectable at different enforcement layers.

---

You are a Connectors / Power Automate throughput domain expert. Execute the following ten-role throughput simulation in strict role order. **Each role gate must be satisfied before the next role opens.**

---

**ROLE 1 — VERDICT AUTHOR**
*Pre-commitment. No evidence sections precede this role.*

```
## VERDICT

Binding Constraint: [Component] — [numeric threshold + unit] — binding at [X req/min]
because [one causal sentence].

Primary Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [named action or
connector]: [what structural control is absent on this path, not at a higher tier].

System Status: [SAFE | DEGRADED | FAILING].
```

GATE: All three fields non-empty. Binding Constraint has number + unit. Primary Gap names component. Proceed to Role 2.

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Gate requires: VERDICT block complete.*

```
## FORMAT CONTRACT

Four-column schema for all comparative tables in this document:
| [row key] | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |

BASELINE: [scenario-specific — the system today: components present, controls absent,
load behavior without mitigations.]

PROTECTED: [scenario-specific — the system after Role 9 mitigations: protections added,
components changed, load behavior with mitigations.]

DERIVATION CHAIN: This column is mandatory in every table containing quantified estimates.
A table that omits this column is structurally incomplete (schema violation — visible without
reading cell values). Template computation for each quantified cell:
  [req/interval] × [multiplier] = [peak_req/interval]
  [peak_req/interval] − [component N req/interval, from Role 3] = [overflow]
  [overflow] × [retry_factor] = [total_attempts]
  ([total_attempts] − [capacity]) / [total_attempts] = [failure_rate]
  [failure_rate] × 100 = [failure_pct]

Rejection Clause — Schema: Any table omitting BASELINE, PROTECTED, or DERIVATION CHAIN is
STRUCTURALLY INCOMPLETE. Structural incompleteness is not a content gap; it is visible at
table-header scan time without reading any cell.

Rejection Clause — Content: Any DERIVATION CHAIN cell stating only a conclusion without the
step-by-step derivation is a CONTENT VIOLATION. At least two distinct tables must include the
DERIVATION CHAIN column with fully populated step-by-step derivation cells.
```

GATE: FORMAT CONTRACT present. Both rejection clauses written. DERIVATION CHAIN column named as mandatory in schema line. BASELINE and PROTECTED scenario-specific. Proceed to Role 3.

---

**ROLE 3 — RATE LIMIT REGISTRY**
*Gate requires: FORMAT CONTRACT with DERIVATION CHAIN as mandatory schema column.*

Enumerate rate-limiting components in binding order: name, type, numeric threshold + unit ([estimated] if non-public), scope, binding order rationale (one sentence each).

At least one component addresses VERDICT Binding Constraint.

GATE: All components have numeric thresholds + units. All rows have binding-order rationale. At least one row addresses VERDICT Binding Constraint. Verdict-currency check: does Role 3 revise the Binding Constraint? If yes, insert `[REVISED — see Role 3]` in VERDICT before proceeding to Role 4.

---

**ROLE 4 — CAUSAL PROPAGATION TRACER**
*Gate requires: Role 3 registry complete; at least one component addresses VERDICT Binding Constraint.*

Directed hop chain from binding constraint to user-observable effect, minimum two hops:
```
[Component] --[mechanism]--> [Component] --[mechanism]--> [observable effect]
```
Mechanisms: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade.

GATE: At least two hops. Each hop names a mechanism. Chain terminates at user-observable effect. Proceed to Role 5.

---

**ROLE 5 — BURST PATH AUDITOR**
*Gate requires: Propagation chain with at least two hops and named mechanisms.*

Three-control checklist per trigger/action capable of concurrent requests:
1. Concurrency cap below the rate limit?
2. Retry-After policy reading the header?
3. Queue buffer between source and endpoint?

STRUCTURAL = no mechanism. INCIDENTAL = mechanism bypassed (name exact bypass condition).

GATE: At least one path with STRUCTURAL or INCIDENTAL classification and justification. VERDICT Primary Gap confirmed or revised. If revised: insert `[REVISED — see Role 5]` in VERDICT before proceeding to Role 6.

---

**ROLE 6 — RETRY-AFTER INSPECTOR**
*Gate requires: Burst path audit with at least one classified unprotected path; VERDICT Primary Gap addressed.*

Per-connector and per-HTTP-action: reads and honors `Retry-After` / `Retry-After-Ms` / `x-ms-ratelimit-remaining`? For each gap: failure mode (immediate retry storm / permanent failure after N retries / silent drop / backoff ignoring header value).

GATE: Every connector and HTTP action has an entry. Each gap names a failure mode. Verdict-currency check: does Role 6 revise VERDICT Primary Gap? If yes: insert `[REVISED — see Role 6]` before proceeding to Role 7.

---

**ROLE 7 — CASCADE CONSTRUCTOR**
*Gate requires: Retry-After inspection complete with all gaps and failure modes named.*

One cascade: Tier 1 throttle causally triggers Tier 2 at a different component. Two independent limits hit simultaneously do not qualify. Name: Tier 1 component + threshold, causal mechanism, Tier 2 component + threshold, compounding effect (numeric estimate).

GATE: Two distinct tiers named and traceable to Role 3. Causal link stated explicitly. Compounding effect has numeric estimate. Proceed to Role 8.

---

**ROLE 8 — UX TIER ANALYST**
*Gate requires: Cascade with two tiers, causal link, and numeric compounding effect.*

Four-field template per throttle tier. Minimum two tiers. Prose without template fails.

```
Tier [N]: [component + threshold]
  (a) Error code or platform signal: [specific identifier]
  (b) User-visible behavior: [specific to this tier]
  (c) Visibility level: [user-visible and explicit | background-only and silent]
  (d) Recovery path: [manual retry | automatic backoff | permanent failure | other]
```

GATE: At least two tiers with all four fields (a)–(d) present. Proceed to Role 9.

---

**ROLE 9 — THROUGHPUT ANALYST**
*Gate requires: UX catalog with at least two four-field template tiers.*

Volume-to-Behavior Map using the FORMAT CONTRACT four-column schema:

| Volume | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|--------|----------|-----------|------------------|-------|
| 1x     |          |           |                  |       |
| 2x     |          |           |                  |       |
| 5x     |          |           |                  |       |

**FORMAT CONTRACT applies. DERIVATION CHAIN column is mandatory in this table.**

The 5x BASELINE DERIVATION CHAIN cell must contain the five-step computation chain with Role 3 operands. A cell stating only "42% fail" without the steps is a CONTENT VIOLATION even if correct. The table missing the DERIVATION CHAIN column header is a SCHEMA VIOLATION.

The 5x PROTECTED cell uses the same five-step format with Role 10 mitigations applied.

GATE: All three bands filled. DERIVATION CHAIN column present (no schema violation). 5x BASELINE has five-step derivation chain. 5x PROTECTED shows mitigated arithmetic. Verdict-currency check: does Role 9 arithmetic revise VERDICT System Status? If yes: insert `[REVISED — see Role 9]` before proceeding to Role 10.

---

**ROLE 10 — MITIGATION ARCHITECT**
*Gate requires: Volume map complete with DERIVATION CHAIN column present; 5x arithmetic chains present.*

Mitigation table using FORMAT CONTRACT four-column schema. Every bottleneck (Role 3) and unprotected path (Role 5) gets a row.

| Finding | BASELINE | PROTECTED | DERIVATION CHAIN | Delta |
|---------|----------|-----------|------------------|-------|

**DERIVATION CHAIN column is mandatory (schema violation if absent).** For mitigations changing a numeric limit or retry factor: five-step arithmetic. For non-numeric mitigations: write STRUCTURAL-CHANGE (describe behavioral change without quantification).

GATE: Every bottleneck and path has a row. DERIVATION CHAIN column present (no schema violation). Every PROTECTED cell names exact action/setting/parameter. Every Delta states measurable change. Proceed to Role 11 reconciliation.

---

**ROLE 11 — VERDICT RECONCILER**

Scan Roles 3–10 for each VERDICT field. For any revision without a marker, insert now. State: `VERDICT RECONCILIATION COMPLETE — [CONFIRMED | N REVISIONS APPLIED]`. Count: [N schema violations found / N content violations found].

---

## V-05

**Variation axes:** All five — role sequence (full gate chain C-21) + output format (DERIVATION CHAIN as mandatory 4th schema column C-23) + phrasing register (imperative per-section column-compliance commands) + inertia framing (unmitigated state named as INERTIA in all columns) + gate-checkpoint Verdict currency (C-22, revision markers inserted at gate boundary, not deferred to terminal reconciliation). This is the full-integration variation.

**Hypothesis:** The R5 champion variations (V-01 through V-04) each address C-20/C-21/C-22/C-23 through a single primary axis. None simultaneously enforces all five axes. V-05 tests whether the combined constraints create compound reinforcement — where each structural mechanism independently enforces its target criterion, so that the failure of any single mechanism does not cascade into criterion failures, and where the combination produces qualitatively stronger output than any single axis because each axis blocks a different failure mode: gate chain blocks section skipping, schema column blocks table omission, per-section commands block local forgetting, inertia framing blocks generic mitigations, and currency checks block stale Verdicts.

---

You are a Connectors / Power Automate throughput domain expert. Execute this ten-role simulation in strict role order. Every role gate must clear before the next role opens. Every gate includes a Verdict-currency check — if the current role revises a VERDICT claim, insert the revision marker in the VERDICT block **before** the gate condition is cleared. Do not defer revision marking to a terminal role.

---

**ROLE 1 — VERDICT AUTHOR**
*No evidence sections may precede this role.*

```
## VERDICT

Binding Constraint: [Component] — [numeric threshold + unit] — binding at [X req/min]
because [one causal sentence].

Primary Gap: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [named component]:
[one sentence: what structural control is absent, not at a higher tier].

System Status: [SAFE | DEGRADED | FAILING].
```

GATE: All three fields non-empty. Binding Constraint has number + unit. Verdict-currency check: no prior roles — no check needed. Proceed to Role 2.

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Gate requires: VERDICT block complete.*

**IMPERATIVE: This Format Contract governs ALL tables in Roles 3–10. Read it before producing any table.**

```
## FORMAT CONTRACT

Four-column schema — mandatory for all comparative and quantitative tables:
| [row key] | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |

INERTIA: The system in its current unmitigated state — named to specific components,
absent controls, and load behavior today. INERTIA is the status-quo competitor. Every
mitigation in Role 9 must explicitly beat the INERTIA state; a mitigation that does not
change the INERTIA condition at this bottleneck does not qualify.

PROTECTED: The system after Role 9 mitigations. Name the specific protections added and
the resulting behavior under the same load.

DERIVATION CHAIN: MANDATORY COLUMN in every table with quantified estimates. Omitting
this column is a schema violation visible at scan time. Template:
  [req/interval] × [multiplier] = [peak]
  [peak] − [Role 3 registry: component name, N req/interval] = [overflow]
  [overflow] × [retry_factor] = [total_attempts]
  ([total_attempts] − [capacity]) / [total_attempts] = [failure_rate]
  [failure_rate] × 100 = [failure_pct]

INERTIA-delta rule: Every DERIVATION CHAIN cell in the mitigation table must show the
delta from the INERTIA arithmetic — not merely the protected state in isolation. The delta
proves the mitigation beats the INERTIA competitor.

SCHEMA REJECTION CLAUSE: A table containing quantified estimates but missing the
DERIVATION CHAIN column is STRUCTURALLY INCOMPLETE. This is a schema violation — visible
without reading cell values. At least two distinct quantified tables must comply with the
full four-column schema including populated DERIVATION CHAIN cells.

CONTENT REJECTION CLAUSE: A DERIVATION CHAIN cell containing only a conclusion without
step-by-step computation is a CONTENT VIOLATION.
```

GATE: FORMAT CONTRACT present. Four-column schema with INERTIA declared as named competitor column. DERIVATION CHAIN declared mandatory in schema. Both rejection clauses present. Verdict-currency check: does the Format Contract definition of INERTIA revise the VERDICT System Status framing? If the INERTIA state implies a different severity, insert `[REVISED — see Role 2]` in VERDICT before proceeding to Role 3.

---

**ROLE 3 — RATE LIMIT REGISTRY**
*Gate requires: FORMAT CONTRACT with four-column schema and DERIVATION CHAIN mandatory.*

**COLUMN COMPLIANCE: This role's output contains an ordered list, not a comparative table — DERIVATION CHAIN column not required here. Binding-order rationale serves as the derivation narrative.**

Enumerate rate-limiting components in binding order: name, type, numeric threshold + unit ([estimated] if non-public), scope, binding-order rationale (one sentence — why this component binds before the next).

At least one component must address VERDICT Binding Constraint.

GATE: All components have numeric thresholds + units. All rows have binding-order rationale. At least one row addresses VERDICT Binding Constraint. Verdict-currency check: does Role 3 revise the VERDICT Binding Constraint? If yes: insert `[REVISED — see Role 3]` in VERDICT block **now**, before proceeding to Role 4.

---

**ROLE 4 — CAUSAL PROPAGATION TRACER**
*Gate requires: Rate limit registry complete with VERDICT Binding Constraint addressed.*

**COLUMN COMPLIANCE: Directed hop chain — no table. DERIVATION CHAIN not required in this role.**

```
[Component] --[mechanism]--> [Component] --[mechanism]--> [user-observable effect]
```

Minimum two hops. Mechanisms: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade.

GATE: Two hops. Named mechanisms. User-observable effect at terminus. Verdict-currency check: does Role 4 reveal the VERDICT Primary Gap is at a different link in the chain than stated? If yes: insert `[REVISED — see Role 4]` in VERDICT Primary Gap field now, before proceeding to Role 5.

---

**ROLE 5 — BURST PATH AUDITOR**
*Gate requires: Propagation chain with two hops and named mechanisms.*

**COLUMN REQUIRED: DERIVATION CHAIN (for quantified concurrent-request estimates)**
**Any burst path table in this role containing quantified estimates must include the DERIVATION CHAIN column. Omitting it is a schema violation.**

| Path | Concurrency Estimate | INERTIA Control State | Gap Type | DERIVATION CHAIN | PROTECTED Control State |
|------|---------------------|-----------------------|----------|------------------|-------------------------|

- Gap Type: STRUCTURAL (no mechanism) / INCIDENTAL (bypassed — name condition)
- DERIVATION CHAIN: for quantified concurrency estimates, show computation; for qualitative paths, N/A
- INERTIA Control State: the current absence of control — named specifically
- PROTECTED Control State: the control added by Role 9 mitigation

GATE: At least one STRUCTURAL or INCIDENTAL path with justification. DERIVATION CHAIN column present (no schema violation). VERDICT Primary Gap confirmed or revised. If revised: insert `[REVISED — see Role 5]` now, before proceeding to Role 6.

---

**ROLE 6 — RETRY-AFTER INSPECTOR**
*Gate requires: Burst path audit complete with VERDICT Primary Gap addressed.*

**COLUMN COMPLIANCE: Per-connector evaluation — no comparative table. DERIVATION CHAIN not required here.**

Per-connector and per-HTTP-action: reads and honors `Retry-After` / `Retry-After-Ms` / `x-ms-ratelimit-remaining`? For each gap: failure mode (immediate retry storm / permanent failure after N retries / silent drop / backoff ignoring header value).

GATE: Every connector and HTTP action has an entry. Each gap names a failure mode. Verdict-currency check: does Role 6 reveal that the VERDICT Primary Gap is missing Retry-After handling, not the burst path stated? If yes: insert `[REVISED — see Role 6]` in VERDICT Primary Gap now, before proceeding to Role 7.

---

**ROLE 7 — CASCADE CONSTRUCTOR**
*Gate requires: Retry-After inspection complete with all connectors evaluated.*

**COLUMN COMPLIANCE: Prose cascade scenario — no comparative table. DERIVATION CHAIN not required here.**

One cascade: Tier 1 throttle causally triggers Tier 2. Name both tiers (Role 3 references), causal mechanism, compounding effect (numeric). Two independent limits do not qualify.

GATE: Two distinct tiers. Causal link explicit. Numeric compounding effect. Verdict-currency check: does Role 7 cascade reveal a secondary gap not in the VERDICT? If the cascade reveals a gap that changes the PRIMARY GAP assessment: insert `[REVISED — see Role 7]` now, before proceeding to Role 8.

---

**ROLE 8 — UX TIER ANALYST**
*Gate requires: Cascade complete with two tiers, causal link, numeric effect.*

**COLUMN COMPLIANCE: Four-field template per tier — not a table. DERIVATION CHAIN not required here. Template structure is mandatory.**

```
Tier [N]: [component + threshold]
  (a) Error code or platform signal: [specific identifier]
  (b) User-visible behavior: [what the user observes]
  (c) Visibility level: [user-visible and explicit | background-only and silent]
  (d) Recovery path: [manual retry | automatic backoff | permanent failure | other]
```

Minimum two tiers. Prose without template fails.

GATE: At least two tiers with all four fields. Verdict-currency check: does any tier show SILENT behavior when the VERDICT implies EXPLICIT visibility? If yes: insert `[REVISED — see Role 8]` in VERDICT System Status now, before proceeding to Role 9.

---

**ROLE 9 — THROUGHPUT ANALYST**
*Gate requires: UX catalog with at least two four-field tiers.*

**COLUMN REQUIRED: INERTIA, PROTECTED, DERIVATION CHAIN, Delta**
**Any table missing the DERIVATION CHAIN column is a schema violation. INERTIA replaces generic BASELINE in this variation.**

| Volume | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |
|--------|---------|-----------|------------------|-------|
| 1x     |         |           |                  |       |
| 2x     |         |           |                  |       |
| 5x     |         |           |                  |       |

INERTIA is the status-quo competitor. PROTECTED shows what changes when mitigations apply.

**5x INERTIA DERIVATION CHAIN cell — mandatory:**
```
Step 1: [1x_req/min] × 5 = [peak_req/min]
Step 2: [peak_req/min] − [Role 3: component, N req/min] = [overflow_req/min]
Step 3: [overflow_req/min] × [retry_factor] = [total_attempts_req/min]
Step 4: ([total_attempts] − [capacity]) / [total_attempts] = [failure_rate]
Step 5: [failure_rate] × 100 = [failure_pct]% — INERTIA failure rate
```

**5x PROTECTED DERIVATION CHAIN cell — mandatory:**
Show same five steps with Role 9 mitigations applied. The Delta cell shows [INERTIA failure_pct] − [PROTECTED failure_pct] = [improvement]. This is the INERTIA-delta: proof the mitigation beats the status-quo competitor.

GATE: All three bands filled. DERIVATION CHAIN column present (schema violation if absent). 5x INERTIA has five-step derivation with Role 3 operands. 5x PROTECTED has five-step derivation with mitigated operands. Delta column shows INERTIA-delta for 5x. Verdict-currency check: does Role 9 arithmetic change VERDICT System Status? If yes: insert `[REVISED — see Role 9]` now, before proceeding to Role 10.

---

**ROLE 10 — MITIGATION ARCHITECT**
*Gate requires: Volume map with DERIVATION CHAIN column present; 5x arithmetic chains present.*

**COLUMN REQUIRED: INERTIA, PROTECTED, DERIVATION CHAIN, Delta**
**INERTIA-delta rule applies: each DERIVATION CHAIN cell must show the delta from INERTIA, not merely the protected state.**

| Finding | INERTIA | PROTECTED | DERIVATION CHAIN | Delta |
|---------|---------|-----------|------------------|-------|

For each bottleneck (Role 3) and unprotected path (Role 5):
- INERTIA: specific behavior at this bottleneck in the unmitigated state — named to this component.
- PROTECTED: exact action, setting, or parameter changed (name it explicitly).
- DERIVATION CHAIN: if mitigation changes a numeric limit or retry factor, show updated arithmetic using Role 9's five-step template; show INERTIA-vs-PROTECTED comparison. Write STRUCTURAL-CHANGE with behavioral description if non-numeric.
- Delta: [INERTIA failure_pct or queue_pct] − [PROTECTED failure_pct or queue_pct] = [improvement].

GATE: Every bottleneck and path has a row. DERIVATION CHAIN column present (no schema violation). Every PROTECTED cell names exact action/setting/parameter. Every DERIVATION CHAIN quantified cell shows INERTIA-delta. Every Delta states measurable improvement. Verdict-currency check: does Role 10 mitigation set change VERDICT System Status from FAILING/DEGRADED to a different classification under protection? If yes: insert `[REVISED — see Role 10]` in VERDICT System Status now.

---

**After Role 10:** VERDICT RECONCILIATION — scan all `[REVISED — see Role N]` markers in the VERDICT block. Verify each marker references a role whose output confirms the revision. State: `RECONCILIATION COMPLETE — [N revisions total, each confirmed by named role evidence]`. Count schema violations and content violations observed during execution.
