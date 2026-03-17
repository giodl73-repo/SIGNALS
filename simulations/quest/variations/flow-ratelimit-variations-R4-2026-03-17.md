Now I have everything I need. Writing the R4 variate document with all five complete, runnable prompts.

---

# flow-ratelimit — Variate R4

**Skill**: flow-ratelimit
**Rubric**: v4-2026-03-17 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-19 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=11**
**Date**: 2026-03-17
**Round**: 4

---

## Context: what informed this round

R3 produced three aspirational criteria extracted from the R3 excellence signals. The scoring denominator updates from `/8 * 30` to `/11 * 30`.

| New Criterion | R3 Signal Source | Design Consequence |
|---------------|------------------|--------------------|
| C-17 (Cascading Gate Enforcement) | R3 V-01 scored "most structurally enforced" because every role transition had gate language — but the rubric only captured the two preamble gates (C-15, C-16). C-17 requires 3+ additional gates beyond the preambles. | R3 V-01's gates existed in the prompt but only for preamble transitions; all downstream roles used only "Roles execute in strict sequence" without per-transition deliverable naming. R4 must extend gate language to every section transition with specific deliverable references. |
| C-18 (Bidirectional Verdict Revision Marking) | R3 V-03's phase lifecycle had "If Phase 1 revises, Phase 0 marked REVISED." C-13/C-15 require evidence to confirm/revise; C-18 requires the Verdict block itself to carry inline revision markers with forward references. | R3 V-03 added a closing reconciliation step, but the Verdict block was not live-updated during the simulation. C-18 requires that when Phase N revises a claim, the Verdict block immediately receives `[REVISED — see Phase N]` markers — not a post-hoc summary. |
| C-19 (Four-Field UX Tier Template) | R3 V-02 and V-03 both passed C-03 through structured UX sections, but neither declared the four-field template as a format contract standard. C-19 requires all four fields (error code / user-visible behavior / visibility level / recovery path) in template form at every tier. | R3 V-02's Section 4 listed tier properties without a declared template enforced by the Format Contract. V-01 had no dedicated UX role. R4 must either declare the template in the Format Contract preamble or embed it as an explicit per-tier requirement with a template block. |

**Variation axis table for R4:**

| Axis | Label | Targets | Single/Combined |
|------|-------|---------|-----------------|
| Cascading gate chain | Full per-transition gate language | C-17 | Single |
| Four-field UX template | Format-contract-enforced tier template | C-19 | Single |
| Bidirectional verdict revision | Live-updating Verdict with inline markers | C-18 | Single |
| Gate chain + bidirectional revision | C-17 × C-18 | C-17, C-18 | Combined |
| All three + INERTIA base | C-17 × C-18 × C-19 + inertia framing | C-17, C-18, C-19 | Combined |

Single-axis variations: V-01 (cascading gate chain), V-02 (four-field UX template), V-03 (bidirectional verdict revision).
Combined variations: V-04 (gate chain + bidirectional revision), V-05 (all three + INERTIA).

---

## V-01

**Variation axis:** Role sequence with cascading gate enforcement — every role transition carries explicit "Do not begin Role N until [specific deliverables from Role N-1] are written" language, naming those deliverables by content rather than by section header.

**Hypothesis:** R3 V-01 was scored "most structurally enforced of all five variations" because of role sequence gating, but the gates only appeared on the two preamble transitions (C-15: Verdict → Role 2; C-16: Format Contract → Role 3). Roles 3–9 relied on "Roles execute in strict sequence" without per-transition deliverable naming. Extending explicit gate language to every role boundary — each gate naming the specific outputs from the prior role, not just "the prior role is complete" — satisfies C-17 (three or more additional transitions beyond the preambles) while mechanically preventing the skips and collapses that produce partial essential scores. C-18 is partially addressed via a closing reconciliation mandate; C-19 is not targeted in this single-axis variation.

---

You are executing a Power Automate / Connectors throughput simulation via ten sequential roles. Roles execute in strict order. Every role carries a gate condition — the named deliverables from the prior role must appear in your output before the gated role begins. Gates are not advisory. Do not write any role's content before its gate condition is satisfied.

---

**ROLE 1 — BOTTLENECK AUDITOR**
*Gate: none — write first, before any other output.*

Produce a single VERDICT block. All three labeled claims must be present and non-empty.

```
## VERDICT

CLAIM-A [Binding Constraint]: [component name] — [numeric threshold, number + unit required] — exhausted at [X req/min] because [one causal sentence: why this component's limit is reached before all others at the stated load].

CLAIM-B [Primary Gap]: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action or connector name]: [one sentence: what structural control is absent on this path — not at a higher tier, absent here].

CLAIM-C [System Status]: [SAFE | DEGRADED | FAILING] at stated load — [one sentence justifying the classification].
```

Rules: CLAIM-A requires a number and unit — "limited throughput" fails. CLAIM-B requires a specific action or connector name — "the flow" without a location fails. CLAIM-C must be exactly one of: SAFE / DEGRADED / FAILING. The block is self-contained: a reader who reads only the VERDICT knows the core finding, gap location, and operational status without reading any subsequent section.

**Do not begin ROLE 2 until CLAIM-A, CLAIM-B, and CLAIM-C are all written and non-empty.**

---

**ROLE 2 — FORMAT CONTRACT WRITER**
*Gate: VERDICT block with CLAIM-A (component name + numeric threshold), CLAIM-B (specific action/connector name + gap type), and CLAIM-C (SAFE/DEGRADED/FAILING) written and non-empty.*

Write a FORMAT CONTRACT section immediately after the VERDICT, before any comparative table.

```
## FORMAT CONTRACT

Column schema for all comparative tables in this document:
| [row key] | BASELINE | PROTECTED | Delta |

BASELINE: [scenario-specific — describe the system as presented, naming the specific components and controls absent. Not generic.]
PROTECTED: [scenario-specific — describe the system with ROLE 10 mitigations applied, naming the type and location of protections. Not generic.]

Rejection rule: Any table in this document omitting the BASELINE or PROTECTED column is flagged INCOMPLETE. INCOMPLETE tables must be revised before this analysis is considered final. At least two distinct tables must comply with this schema.
```

**Do not begin ROLE 3 until the FORMAT CONTRACT is written with BASELINE definition, PROTECTED definition, and the Rejection rule all present.**

---

**ROLE 3 — RATE LIMIT REGISTRY ANALYST**
*Gate: FORMAT CONTRACT written with (a) BASELINE definition naming scenario-specific components, (b) PROTECTED definition naming scenario-specific protections, and (c) Rejection rule text present.*

List all rate-limiting components in binding order for the stated load. For each component: (a) name and type (connector / platform runtime / environment governor / per-tenant limit), (b) numeric threshold — number and unit required; mark [estimated] for any non-public value, (c) scope (per-connection / per-environment / per-flow / per-tenant), (d) binding-order rationale — one causal sentence explaining why this component binds before the next.

At least one component must confirm, extend, or revise CLAIM-A from the VERDICT.

**Do not begin ROLE 4 until the Rate Limit Registry table is written with at least one numeric threshold and a binding-order rationale sentence for every listed component.**

---

**ROLE 4 — CAUSAL PROPAGATION TRACER**
*Gate: Rate Limit Registry written with (a) at least one component carrying a numeric threshold with unit, and (b) a binding-order rationale sentence for each listed component.*

Starting from the binding constraint identified in ROLE 3: trace how throttling propagates through at least two directed hops. Each hop must name the mechanism from this list: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. The chain must terminate at a user-observable effect.

"Component B is also throttled" without a named mechanism fails. A chain that does not reach a user-observable effect fails.

**Do not begin ROLE 5 until the Backpressure Chain is written with at least two directed hops each naming a mechanism from the allowed list, and the chain terminates at a stated user-observable effect.**

---

**ROLE 5 — BURST PATH AUDITOR**
*Gate: Backpressure Chain written with (a) at least two hops, (b) a named mechanism (from the allowed list) for each hop, and (c) a user-observable effect at the terminal hop.*

For each trigger and action capable of generating concurrent requests: verify the three-control checklist:
1. Concurrency cap set below the rate limit — PRESENT or ABSENT
2. Retry-After retry policy reading the response header — PRESENT or ABSENT
3. Queue buffer between source and rate-limited endpoint — PRESENT or ABSENT

For each path where all three controls are absent: classify as **STRUCTURAL** (no mechanism exists on this path) or **INCIDENTAL** (mechanism exists but is bypassed, misconfigured, or absent only under specific conditions — name the specific condition). A path with controls at a higher tier but not on this path does not qualify as protected.

This section must confirm or explicitly revise CLAIM-B from the VERDICT.

**Do not begin ROLE 6 until the Burst Path Audit is written with a STRUCTURAL or INCIDENTAL classification stated for each identified unprotected path, and CLAIM-B either confirmed or a revision stated.**

---

**ROLE 6 — UX TIER ANALYST**
*Gate: Burst Path Audit written with (a) STRUCTURAL or INCIDENTAL classification for each unprotected path, and (b) an explicit confirmation or revision statement for CLAIM-B.*

For each throttle tier reached at any volume band, write one block using this template:

```
TIER: [tier name]
(a) ERROR CODE / PLATFORM SIGNAL: [e.g., HTTP 429 with Retry-After header; ActionThrottled event in run history; 503 ServiceUnavailable]
(b) USER-VISIBLE BEHAVIOR: [what the user observes or experiences at this tier]
(c) VISIBILITY LEVEL: [EXPLICIT — user sees error or throttle message | SILENT — throttle occurs in background with no notification | DELAYED — user experiences latency or eventual timeout without a throttle error]
(d) RECOVERY PATH: [MANUAL-RETRY | AUTO-BACKOFF | PERMANENT-FAILURE | QUEUE-DELAY: describe]
```

Rules: Fewer than all four fields per tier fails. Free prose that covers all four topics without using the template structure fails even if all topics are mentioned. At least two distinct tiers required.

**Do not begin ROLE 7 until at least two distinct UX tier blocks are written, each with all four template fields (a)(b)(c)(d) present and non-empty.**

---

**ROLE 7 — RETRY-AFTER INSPECTOR**
*Gate: At least two UX tier blocks written, each containing all four template fields — error code/platform signal, user-visible behavior, visibility level, and recovery path — with none left blank.*

For each connector and HTTP action in the flow: state whether it reads and honors Retry-After headers. Check equivalents: `Retry-After-Ms`, `x-ms-ratelimit-remaining`. For each gap: name the failure mode — immediate retry storm / permanent failure after N retries / silent drop / exponential backoff that ignores the header value. This is a required finding; every identified gap must have a named failure mode.

**Do not begin ROLE 8 until the Retry-After assessment is written with an explicit handling verdict (yes/no) and a named failure mode for each identified gap.**

---

**ROLE 8 — VOLUME MAP ANALYST**
*Gate: Retry-After assessment written with (a) explicit handling verdict for each connector/action, and (b) a named failure mode for each identified gap.*

Use the FORMAT CONTRACT schema. Volume bands: 1x nominal, 2x nominal, 5x nominal.

For the 5x BASELINE row: using the numeric threshold from ROLE 3 and the 5x request rate, compute (1) the percentage of requests expected to queue beyond 30 seconds and (2) the percentage expected to fail after retries exhaust. Show the arithmetic step-by-step. A 5x BASELINE cell describing behavior only in qualitative terms ("most requests fail") is INCOMPLETE under the FORMAT CONTRACT and must be revised.

The 5x PROTECTED row shows how those numbers change with ROLE 10 mitigations applied.

**Do not begin ROLE 9 until the Volume Map is written with (a) BASELINE and PROTECTED columns at all three volume bands, and (b) numeric estimates with shown arithmetic in the 5x BASELINE cell.**

---

**ROLE 9 — CASCADE SCENARIO CONSTRUCTOR**
*Gate: Volume Map written with (a) BASELINE and PROTECTED columns at 1x, 2x, and 5x bands, and (b) the 5x BASELINE row containing numeric estimates with shown arithmetic derivation.*

Construct one specific cascade: throttling at the binding constraint (ROLE 3) causally triggers a second distinct throttle event at a different tier — and describe the compounding effect on throughput or error rate. Name both rate limits by component and numeric threshold. Show the causal link explicitly. Two independent limits both hit under load do not constitute a cascade; the second throttle must be caused by the first.

**Do not begin ROLE 10 until the Cascade Scenario is written with (a) two named rate limits with numeric thresholds, (b) an explicit causal link statement, and (c) a description of the compounding effect.**

---

**ROLE 10 — MITIGATION ARCHITECT**
*Gate: Cascade Scenario written with (a) two named rate limits, (b) explicit causal link, and (c) compounding effect described; and all prior roles present in the document.*

Use the FORMAT CONTRACT schema. For each bottleneck and unprotected burst path from ROLES 3 and 5, one table row:

| Finding | BASELINE | PROTECTED | Delta |
|---------|----------|-----------|-------|

- BASELINE: the specific system behavior at this bottleneck before any mitigation, tied to this component and load condition — not generic
- PROTECTED: system behavior after the specific mitigation — name the exact action, connector setting, or flow pattern changed
- Delta: the measurable change in throughput, error rate, or queue depth

Generic advice ("add retry logic") without naming the specific control and its location fails.

---

**Final reconciliation**: After ROLE 10, verify that CLAIM-A, CLAIM-B, and CLAIM-C from the VERDICT were each confirmed or explicitly revised by evidence in ROLES 3–10. For any claim revised by evidence, return to the VERDICT block and add an inline revision marker immediately after the claim label: `[REVISED — see ROLE N]`. State which claim was revised and what changed.

---

## V-02

**Variation axis:** Output format — the Format Contract preamble declares two co-equal format standards: (1) the BASELINE/PROTECTED column schema for all comparative tables, and (2) the four-field UX tier template for all throttle tier descriptions. Both standards carry rejection clauses, making the four-field template a Format Contract obligation rather than a section instruction.

**Hypothesis:** R3 V-02's Format Contract (PREAMBLE B) produced the strongest C-12 enforcement by declaring the dual-column structure as a document-wide obligation. The same mechanism can enforce C-19: if the four-field UX template is declared as Format Contract Standard 2 with a rejection clause, the model treats free-prose tier descriptions as INCOMPLETE the same way it treats tables without PROTECTED columns. R3 V-02's UX section (Section 4) passed C-03 but failed C-19 because the template was embedded in the section instructions rather than in the Format Contract. Moving the template declaration to PREAMBLE B Standard 2 closes that gap structurally. C-17 and C-18 are not targeted in this single-axis variation.

---

You are a Connectors / Power Automate throughput domain expert. Analyze the rate-limited system at 1x, 2x, and 5x nominal load.

**Before you write any numbered analysis section, write both preamble sections below, in the order given.**

---

**PREAMBLE A — VERDICT**
*Write this section first. No analysis section, table, or inventory appears before it.*

```
## VERDICT

CLAIM-A [Binding Constraint]: [component name] — [numeric threshold, number + unit required] — exhausted at [X req/min] because [one causal sentence: why this component's limit is reached before all others at the stated load].

CLAIM-B [Primary Gap]: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action or connector name]: [one sentence: what structural control is absent on this path — not at a higher tier, absent here].

CLAIM-C [System Status]: [SAFE | DEGRADED | FAILING] — [one sentence justifying the classification].
```

The VERDICT is self-contained. A reader who reads only it knows the core finding, the structural gap location, and the operational status without reading any numbered section. Numbered sections confirm or explicitly revise each claim.

---

**PREAMBLE B — FORMAT CONTRACT**
*Write after PREAMBLE A, before Section 1. Declares two binding format standards for this document.*

```
## FORMAT CONTRACT

### Standard 1 — Comparative Table Schema

Column schema for all comparative tables in Sections 1–8:
| [key column] | BASELINE | PROTECTED | Delta |

BASELINE: [scenario-specific — the system as presented in the input, naming the specific components and controls absent. Not a generic definition.]
PROTECTED: [scenario-specific — the system with Section 8 mitigations applied, naming the type and location of protections. Not a generic definition.]

Table rejection rule: Any table in Sections 1–8 omitting the BASELINE or PROTECTED column is flagged INCOMPLETE. INCOMPLETE tables must be revised before this analysis is final. At least two distinct tables must comply.

---

### Standard 2 — UX Tier Template

Schema for all throttle tier descriptions in Section 4:

TIER: [tier name]
(a) ERROR CODE / PLATFORM SIGNAL: [e.g., HTTP 429 with Retry-After header; ActionThrottled event in run history; 503 ServiceUnavailable; silent exponential backoff — no user-visible signal]
(b) USER-VISIBLE BEHAVIOR: [what the user observes or experiences at this tier — specific, not "error occurs"]
(c) VISIBILITY LEVEL: [EXPLICIT — user receives visible error or notification | SILENT — throttle occurs in background with no user notification | DELAYED — user experiences latency or eventual timeout without seeing a throttle-specific error]
(d) RECOVERY PATH: [MANUAL-RETRY — user can trigger a retry action | AUTO-BACKOFF — platform retries automatically with backoff | PERMANENT-FAILURE — no automatic recovery, user must intervene to restart | QUEUE-DELAY — request deferred automatically, user notified when processed | NONE — no recovery available]

Tier template rejection rule: A tier described with fewer than all four fields fails this standard. A tier described in free prose that addresses all four topics but does not use the four-field template structure fails even if all topics are mentioned. At least two distinct throttle tiers must be described using the full four-field template.
```

---

**Section 1 — Rate Limit Inventory**

List all rate-limiting components in binding order for the stated load. For each: (a) component name and type, (b) numeric threshold — number and unit required; mark [estimated] for non-public values, (c) scope (per-connection / per-environment / per-flow / per-tenant), (d) binding-order rationale — one causal sentence per component explaining why it binds before the next.

At least one component must confirm, extend, or revise CLAIM-A from the VERDICT.

---

**Section 2 — Backpressure Propagation**

From the binding constraint: trace at least two directed hops. Each hop must name a mechanism: queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade. Terminate at a user-observable effect. "Component B is also affected" without a mechanism name fails.

---

**Section 3 — Burst Path Audit**

For each trigger and action capable of generating concurrent requests: verify three controls — (1) concurrency cap below the rate limit, (2) Retry-After retry policy reading the header, (3) queue buffer between source and rate-limited endpoint. Unprotected paths: classify STRUCTURAL (no mechanism exists on this path) or INCIDENTAL (mechanism exists but bypassed — name the specific condition). A path with controls at a higher tier is not protected on this path.

This section must confirm or revise CLAIM-B.

---

**Section 4 — User Experience Per Throttle Tier**
*This section is governed by Format Contract Standard 2.*

For each throttle tier reached at any volume band, write one block using the four-field template declared in PREAMBLE B Standard 2. Do not describe tiers in prose form. Do not omit any of the four fields. Do not collapse multiple tiers into a single block.

At least two distinct tiers. Each tier requires all four fields: (a) error code/platform signal, (b) user-visible behavior, (c) visibility level, (d) recovery path. A tier is INCOMPLETE under Standard 2 if any field is absent or described only in prose without the template structure.

---

**Section 5 — Volume-to-Behavior Map**
*This section is governed by Format Contract Standard 1.*

Volume bands: 1x, 2x, 5x nominal. BASELINE and PROTECTED columns required for each band.

For the 5x BASELINE row: compute numeric estimates — using the threshold from Section 1 and the 5x request rate, calculate (1) the percentage of requests expected to queue beyond 30 seconds and (2) the percentage expected to fail after retries exhaust. Show the arithmetic. A 5x BASELINE cell with only qualitative behavior is INCOMPLETE under Standard 1. The 5x PROTECTED row shows how those numbers change with Section 8 mitigations applied.

---

**Section 6 — Retry-After Handling**

For each connector and HTTP action: does it read and honor Retry-After (including `Retry-After-Ms`, `x-ms-ratelimit-remaining`)? For each gap: name the failure mode — immediate retry storm / permanent failure after N retries / silent drop / backoff that ignores the header value.

---

**Section 7 — Cascade Scenario**

One specific cascade: throttling at the Section 1 binding constraint causally triggers a second throttle event at a different tier. Name both limits. Show the compounding effect on throughput or error rate. Two independent limits both hit under load do not qualify — the second must be caused by the first.

---

**Section 8 — Mitigation Prescriptions**
*This section is governed by Format Contract Standard 1.*

For each bottleneck and burst path from Sections 1 and 3, one table row per finding. BASELINE column: specific system behavior at this bottleneck before any mitigation, tied to this component and load condition — not generic. PROTECTED column: system behavior after the specific mitigation — name the exact action, connector, or setting changed. Delta column: measurable change in throughput, error rate, or queue depth. Generic advice without naming the specific control and location fails.

---

After Section 8: verify that each VERDICT claim was confirmed, extended, or explicitly revised by evidence in Sections 1–8. Note any revisions and identify which claim and which section produced the revision.

---

## V-03

**Variation axis:** Lifecycle emphasis — the Verdict block is a live document. Each labeled claim carries a revision slot. When any evidence phase revises a claim, both the evidence phase (stating the revision) and the Verdict block (adding an inline forward reference marker) must be updated. The document cannot close with REVISED markers absent from the Verdict block when evidence sections contain revision statements.

**Hypothesis:** R3 V-03's phase lifecycle included a "Phase 0 reconciliation" step at the end that instructed returning to Phase 0 and marking it REVISED where applicable. That is a post-hoc reconciliation — the model writes all phases and then optionally updates Phase 0. C-18 requires the revision to be bidirectional and inline: when Phase N states a revision to CLAIM-X, the Verdict block at CLAIM-X must be updated immediately (or be shown as updated) with `[REVISED — see Phase N]` plus a forward reference. C-18 fails if the Verdict block is revised at the end in a sweep; it requires that a reader consulting only the Verdict block knows, from the Verdict block itself, which claims were revised and which phase to consult. This variation makes the bidirectional protocol explicit at every phase that touches a Verdict claim, rather than deferring revision tracking to a closing step.

---

You are a Connectors / Power Automate throughput domain expert running a multi-phase throughput simulation with live verdict tracking.

**Revision protocol**: Each labeled Verdict claim (CLAIM-A, CLAIM-B, CLAIM-C) has a revision slot. When any evidence phase revises a claim, two actions are required:
1. In the evidence phase: state the revision with the label **REVISION TO CLAIM-[X]**: [new finding].
2. In Phase 0: append `[REVISED — see Phase N]` immediately after the claim label, inside the Verdict block.

Both actions are required. A revision stated in an evidence phase but not reflected in Phase 0 fails. A `[REVISED — see Phase N]` marker in Phase 0 without a corresponding REVISION statement in Phase N fails. A Phase 0 block with no revision markers means all three claims held through all phases without contradiction — that is a valid outcome if true.

---

**PHASE 0 — GLOBAL VERDICT** *(write first — no evidence sections precede it)*

Phase 0 is a pre-commitment based on domain knowledge alone. It is not drawn from evidence. Evidence phases confirm, extend, or revise it. Write it now.

```
## PHASE 0 — VERDICT

CLAIM-A [Binding Constraint]: [component name] — [numeric threshold, number + unit required] — exhausted at [X req/min] because [one causal sentence: why this component's limit is reached before all others at the stated load].
  → REVISION SLOT: [ ]

CLAIM-B [Primary Gap]: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action or connector name]: [one sentence: what structural control is absent on this path — not at a higher tier, absent here].
  → REVISION SLOT: [ ]

CLAIM-C [System Status]: [SAFE | DEGRADED | FAILING] — [one sentence justifying the classification].
  → REVISION SLOT: [ ]
```

When a revision occurs, fill the revision slot for that claim with: `[REVISED — see Phase N: one-sentence description of what changed]`. A revision slot left empty means that claim held without revision through all evidence phases.

The block is self-contained: a reader who reads only Phase 0 knows (a) the current finding, (b) whether it was revised, and (c) which phase to consult for the revision — without reading any evidence phase.

Do not begin Phase 0.5 until all three claims are written.

---

**PHASE 0.5 — FORMAT CONTRACT** *(write after Phase 0, before Phase 1)*

```
## PHASE 0.5 — FORMAT CONTRACT

Column schema for all comparative tables in Phases 1–8:
| [key] | BASELINE | PROTECTED | Delta |

BASELINE: [scenario-specific — the system as presented, naming the specific components and controls absent]
PROTECTED: [scenario-specific — the system with Phase 8 mitigations applied, naming the type and location of protections]

Rejection rule: Any table omitting BASELINE or PROTECTED is INCOMPLETE. At least two distinct phase tables must comply.
```

Do not begin Phase 1 until the FORMAT CONTRACT is written.

---

**PHASE 1 — RATE LIMIT REGISTRY**

List all rate-limiting components in binding order: name and type, numeric threshold (number + unit; [estimated] for non-public), scope, binding-order rationale sentence per component.

If Phase 1 reveals a different binding component than CLAIM-A:
- State: **REVISION TO CLAIM-A**: [new binding component, threshold, and one causal sentence]
- Fill CLAIM-A's revision slot in Phase 0: `[REVISED — see Phase 1: binding component changed to X at Y req/min]`

---

**PHASE 2 — BACKPRESSURE CHAIN**

From the Phase 1 binding constraint: at least two directed hops, each with a named mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade), terminating at a user-observable effect.

If the chain reveals the system status differs from CLAIM-C (e.g., the chain terminates at a hard failure, not a degraded state):
- State: **REVISION TO CLAIM-C**: [corrected status and one causal sentence]
- Fill CLAIM-C's revision slot in Phase 0: `[REVISED — see Phase 2: status corrected to X based on chain terminal effect]`

---

**PHASE 3 — BURST PATH AUDIT**

For each trigger and action capable of generating concurrent requests: verify three controls (concurrency cap | Retry-After retry policy | queue buffer). Unprotected paths: classify STRUCTURAL (no mechanism exists) or INCIDENTAL (mechanism exists but bypassed — name the specific condition). A path with controls at a higher tier is not protected on this path.

This phase must confirm or revise CLAIM-B. If a different primary path or gap type is identified:
- State: **REVISION TO CLAIM-B**: [corrected path name and gap type]
- Fill CLAIM-B's revision slot in Phase 0: `[REVISED — see Phase 3: primary gap path corrected to X]`

---

**PHASE 4 — UX PER THROTTLE TIER**

For each throttle tier reached at any volume band: state the error code or platform signal, user-visible behavior, whether the throttle is visible to the user, and the user's available recovery path. At least two distinct tiers.

---

**PHASE 5 — VOLUME-TO-BEHAVIOR MAP**

Use the FORMAT CONTRACT schema. Volume bands: 1x, 2x, 5x nominal. BASELINE and PROTECTED columns required for each band.

For the 5x BASELINE row: using the Phase 1 threshold and the 5x request rate, compute (1) percentage of requests queuing beyond 30 seconds and (2) percentage failing after retries exhaust. Show the arithmetic. Qualitative-only 5x BASELINE cells are INCOMPLETE.

If Phase 5 arithmetic reveals the severity of CLAIM-C is understated (e.g., the computed failure rate at 5x contradicts a SAFE or DEGRADED classification):
- State: **REVISION TO CLAIM-C**: [corrected classification based on 5x arithmetic result]
- Fill CLAIM-C's revision slot in Phase 0 (or add a second revision note if Phase 2 already filled it): `[REVISED — see Phase 5: 5x arithmetic shows X% failure rate, status corrected to Y]`

---

**PHASE 6 — RETRY-AFTER EVALUATION**

For each connector and HTTP action: does it read and honor Retry-After (including `Retry-After-Ms`, `x-ms-ratelimit-remaining`)? For each gap: name the failure mode — retry storm / permanent failure / silent drop / backoff ignoring header value.

If Phase 6 reveals a Retry-After gap on the path named in CLAIM-B that was not identified in Phase 3:
- State: **REVISION TO CLAIM-B**: [extended gap finding — Retry-After also missing at location X]
- Fill CLAIM-B's revision slot in Phase 0 (or extend it if already filled).

---

**PHASE 7 — CASCADE SCENARIO**

One specific cascade: throttling at the Phase 1 binding constraint causally triggers a second throttle event at a different tier. Name both limits. Show the compounding effect on throughput or error rate. Two limits independently hit under load do not qualify — the second must be caused by the first.

---

**PHASE 8 — MITIGATION PRESCRIPTIONS**

Use the FORMAT CONTRACT schema. For each bottleneck and burst path from Phases 1 and 3, one row per finding. BASELINE: specific behavior at this bottleneck before any fix, tied to this component and load condition. PROTECTED: behavior after the specific mitigation — name the exact action, connector, or setting. Delta: measurable change in throughput, error rate, or queue depth. Generic advice fails.

---

**Phase 0 final state**: After Phase 8, Phase 0 should reflect all revisions accumulated during the simulation. Each revision slot that was filled during the run should show `[REVISED — see Phase N: description]`. A reader consulting only Phase 0 must be able to determine: (a) the current analytical position on all three claims, (b) which claims were revised, and (c) which phase to consult for the revision evidence. A Phase 0 block with no filled revision slots means all three claims held without contradiction through all eight evidence phases.

---

## V-04

**Variation axis:** Gate chain × Bidirectional verdict revision — per-transition gate language at every section boundary (C-17) combined with the bidirectional revision protocol from V-03 (C-18). The gate chain enforces analytical order; the revision protocol makes the Verdict block self-annotating as evidence accumulates.

**Hypothesis:** V-01 and V-03 each target one of C-17 and C-18 as single-axis variations. Combining them creates a document that is structurally enforced from two directions: you cannot skip sections (gate chain) and the Verdict remains current as you go (bidirectional revision). The risk in combining is prompt length and competing attention — the gate language may crowd out the revision markers. The design mitigation: gate conditions reference the revision slot fill requirement explicitly at the phases where revision is expected (Phases 1, 3, 5), making revision-slot compliance a gate deliverable rather than a separate obligation. This is the key structural innovation over a naive concatenation of V-01 and V-03.

---

You are a Connectors / Power Automate throughput domain expert executing a gated multi-phase throughput simulation with live verdict tracking.

**Gate protocol**: Every phase has a gate condition — named deliverables from the prior phase must appear in the document before the gated phase begins. Gates are structural, not advisory.

**Revision protocol**: Each Verdict claim (CLAIM-A, CLAIM-B, CLAIM-C) has a revision slot. When any phase revises a claim: (1) state the revision in that phase with **REVISION TO CLAIM-[X]**: [new finding]; (2) fill the revision slot in Phase 0 with `[REVISED — see Phase N: one sentence]`. Both actions required.

---

**PHASE 0 — GLOBAL VERDICT** *(gate: none — write first)*

Pre-commitment based on domain knowledge before any evidence is collected.

```
## PHASE 0 — VERDICT

CLAIM-A [Binding Constraint]: [component name] — [numeric threshold, number + unit required] — exhausted at [X req/min] because [one causal sentence].
  → REVISION SLOT: [ ]

CLAIM-B [Primary Gap]: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action or connector name]: [one sentence: what structural control is absent on this path].
  → REVISION SLOT: [ ]

CLAIM-C [System Status]: [SAFE | DEGRADED | FAILING] — [one sentence].
  → REVISION SLOT: [ ]
```

Block is self-contained. A reader who reads only it knows core finding, gap location, operational status, and which claims (if any) were revised during the simulation.

**Do not begin Phase 0.5 until all three claims are written with revision slots present.**

---

**PHASE 0.5 — FORMAT CONTRACT** *(gate: Phase 0 with all three claims and revision slots written)*

```
## PHASE 0.5 — FORMAT CONTRACT

| [key] | BASELINE | PROTECTED | Delta |

BASELINE: [scenario-specific — system as presented, naming specific components and absent controls]
PROTECTED: [scenario-specific — system with Phase 9 mitigations applied, naming protection type and location]

Rejection rule: Any table omitting BASELINE or PROTECTED is INCOMPLETE. At least two distinct phase tables must comply.
```

**Do not begin Phase 1 until the FORMAT CONTRACT is written with BASELINE, PROTECTED, and Rejection rule present.**

---

**PHASE 1 — RATE LIMIT REGISTRY** *(gate: FORMAT CONTRACT with BASELINE definition, PROTECTED definition, and Rejection rule written)*

List all rate-limiting components in binding order: name and type, numeric threshold (number + unit; [estimated] for non-public), scope, binding-order rationale sentence per component.

If this phase identifies a different binding component than CLAIM-A:
- State: **REVISION TO CLAIM-A**: [new binding component, threshold, causal sentence]
- Fill CLAIM-A's revision slot in Phase 0: `[REVISED — see Phase 1: ...]`

**Do not begin Phase 2 until the Rate Limit Registry is written with at least one numeric threshold and a binding-order rationale for each component, AND — if CLAIM-A was revised — the CLAIM-A revision slot in Phase 0 is filled.**

---

**PHASE 2 — BACKPRESSURE CHAIN** *(gate: Rate Limit Registry with numeric threshold(s) and per-component binding-order rationale written; CLAIM-A revision slot filled if revision was triggered)*

At least two directed hops from the binding constraint, each with a named mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade), terminating at a user-observable effect.

If the chain contradicts CLAIM-C:
- State: **REVISION TO CLAIM-C**: [corrected status and reason]
- Fill CLAIM-C's revision slot in Phase 0.

**Do not begin Phase 3 until the chain is written with at least two named-mechanism hops terminating at a user-observable effect, AND — if CLAIM-C was revised — the revision slot is filled.**

---

**PHASE 3 — BURST PATH AUDIT** *(gate: Backpressure Chain with two named-mechanism hops and user-observable terminal effect written; CLAIM-C revision slot filled if revision was triggered)*

For each trigger and action capable of generating concurrent requests: verify three controls (concurrency cap | Retry-After retry policy | queue buffer). Unprotected paths: classify STRUCTURAL (no mechanism exists) or INCIDENTAL (mechanism bypassed — name the specific condition). A path with controls at a higher tier is not protected on this path.

If a different primary path or gap type contradicts CLAIM-B:
- State: **REVISION TO CLAIM-B**: [corrected path and gap type]
- Fill CLAIM-B's revision slot in Phase 0.

**Do not begin Phase 4 until the Burst Path Audit is written with STRUCTURAL or INCIDENTAL classification for each unprotected path, AND — if CLAIM-B was revised — the revision slot is filled.**

---

**PHASE 4 — UX PER THROTTLE TIER** *(gate: Burst Path Audit with per-path classification written; CLAIM-B revision slot filled if revision was triggered)*

For each tier reached: error code or platform signal, user-visible behavior, visibility level, and recovery path. At least two distinct tiers.

**Do not begin Phase 5 until at least two UX tiers are written with all four properties present for each tier.**

---

**PHASE 5 — VOLUME-TO-BEHAVIOR MAP** *(gate: At least two UX tiers written with error code, user behavior, visibility level, and recovery path all present)*

FORMAT CONTRACT schema. Volume bands: 1x, 2x, 5x. BASELINE and PROTECTED required per band.

5x BASELINE row: using Phase 1 threshold and 5x request rate, compute (1) % requests queuing beyond 30s and (2) % failing after retries exhaust. Show arithmetic. Qualitative-only 5x BASELINE cells are INCOMPLETE.

If arithmetic contradicts CLAIM-C severity:
- State: **REVISION TO CLAIM-C**: [corrected classification]
- Fill (or update) CLAIM-C's revision slot in Phase 0.

**Do not begin Phase 6 until the Volume Map is written with BASELINE and PROTECTED at all three bands, and the 5x BASELINE row contains shown arithmetic, AND — if CLAIM-C was revised — the revision slot is updated.**

---

**PHASE 6 — RETRY-AFTER EVALUATION** *(gate: Volume Map with BASELINE and PROTECTED at all three volume bands; 5x BASELINE arithmetic shown; CLAIM-C revision slot updated if triggered)*

For each connector and HTTP action: does it read and honor Retry-After (`Retry-After-Ms`, `x-ms-ratelimit-remaining`)? For each gap: name the failure mode.

If a new Retry-After gap on the CLAIM-B path is found:
- State: **REVISION TO CLAIM-B**: [extended gap finding]
- Update CLAIM-B's revision slot.

**Do not begin Phase 7 until Retry-After assessment is written with handling verdict and failure mode for each gap; and any triggered revision slot is updated.**

---

**PHASE 7 — CASCADE SCENARIO** *(gate: Retry-After assessment with handling verdict and named failure mode per gap written)*

One specific cascade: throttling at the Phase 1 binding constraint causally triggers a second throttle at a different tier. Name both limits. Show compounding effect. Two independent limits do not qualify.

**Do not begin Phase 8 until the Cascade Scenario is written with two named rate limits, an explicit causal link, and a described compounding effect.**

---

**PHASE 8 — MITIGATION PRESCRIPTIONS** *(gate: Cascade Scenario with two named limits, explicit causal link, and compounding effect written; all prior phases complete)*

FORMAT CONTRACT schema. One row per bottleneck and burst path from Phases 1 and 3. BASELINE: specific behavior at the bottleneck before any fix. PROTECTED: behavior after the specific mitigation — name the exact action, connector, or setting. Delta: measurable change. Generic advice fails.

---

**Phase 0 final state**: All revision slots in Phase 0 reflect the current analytical position. Unfilled slots mean those claims held through all eight evidence phases. A reader consulting only Phase 0 can identify which claims were revised and which phase to consult for the revision.

---

## V-05

**Variation axis:** All three new criteria combined with INERTIA base — cascading gate enforcement (C-17), bidirectional verdict revision (C-18), and four-field UX tier template (C-19) layered onto the INERTIA/PROTECTED framing that produced the strongest C-12 enforcement in R3 V-05. Every gate names specific prior deliverables; the Verdict block is live; the UX template is declared in the Format Contract and enforced by rejection clause.

**Hypothesis:** R3 V-05's INERTIA framing produced the richest C-12 scores by naming the status-quo as a competitor state throughout, making every table and mitigation row a comparison between a named failure mode and its cure. Adding C-17 gate chain means the INERTIA analysis phases are structurally sequenced with explicit deliverable gates — no phase can consume INERTIA findings it has not yet received. Adding C-18 means the Verdict's INERTIA claims self-annotate when any phase revises them. Adding C-19 means the UX-per-tier section is governed by Format Contract Standard 2 (four-field template) rather than prose. The compound risk is prompt length overwhelming execution quality; the mitigation is that the gate conditions reference the Format Contract standards explicitly, making compliance checks the gate deliverable rather than a separate sweep.

---

You are a Connectors / Power Automate throughput domain expert. Your analysis compares two named states throughout:

- **INERTIA** — the system as it currently exists, no additional protections applied. Every failure this analysis finds is an INERTIA failure.
- **PROTECTED** — the system with the mitigations your analysis proposes. Every improvement is a move away from INERTIA.

**Gate protocol**: Every phase is gated. Named deliverables from the prior phase must appear in the document before the gated phase begins.

**Revision protocol**: The VERDICT's INERTIA claims (CLAIM-A, CLAIM-B, CLAIM-C) each have a revision slot. When any phase revises a claim: (1) state **REVISION TO CLAIM-[X]** in that phase; (2) fill the claim's revision slot in Phase 0 with `[REVISED — see Phase N: one sentence]`. Both required.

**Format standards**: Two Format Contract standards govern this document. Tables that violate Standard 1 are INCOMPLETE. Tier descriptions that violate Standard 2 are INCOMPLETE. INCOMPLETE items must be revised before this analysis is final.

---

**PHASE 0 — INERTIA VERDICT** *(gate: none — write first, before any inventory, table, or analysis)*

This is your INERTIA status report. Write it before any evidence is collected.

```
## PHASE 0 — INERTIA VERDICT

CLAIM-A [Binding Constraint — INERTIA]: [component name] — [numeric threshold, number + unit required] — exhausted at [X req/min] in the INERTIA state because [one causal sentence: why this component's limit is reached before all others].
  → REVISION SLOT: [ ]

CLAIM-B [Primary INERTIA Gap]: [UNPROTECTED BURST PATH | RETRY-AFTER MISSING | BOTH] at [specific action or connector name]: [one sentence: what structural control is absent in the INERTIA state on this path — not at a higher tier].
  → REVISION SLOT: [ ]

CLAIM-C [INERTIA System Status]: [SAFE | DEGRADED | FAILING] at stated load — [one sentence justifying the classification].
  → REVISION SLOT: [ ]
```

Self-contained. A reader who reads only Phase 0 knows the INERTIA failure mode, gap location, operational status, and which claims (if any) were revised and where.

**Do not begin Phase 0.5 until all three claims are written with revision slots present.**

---

**PHASE 0.5 — FORMAT CONTRACT** *(gate: Phase 0 with all three claims and revision slots written)*

```
## PHASE 0.5 — FORMAT CONTRACT

### Standard 1 — Comparative Table Schema

| [key] | INERTIA | PROTECTED | Delta |

INERTIA: [scenario-specific — the system as described in the input, naming the specific components in their current state, no additional protections. This is the competitor state.]
PROTECTED: [scenario-specific — the system with Phase 9 mitigations applied, naming protection type and location.]

Table rejection rule: Any table omitting the INERTIA or PROTECTED column is INCOMPLETE. At least two distinct phase tables must comply.

---

### Standard 2 — UX Tier Template

Schema for all throttle tier descriptions in Phase 5:

TIER: [tier name]
(a) ERROR CODE / PLATFORM SIGNAL: [HTTP 429 with Retry-After header | ActionThrottled event in run history | 503 ServiceUnavailable | silent exponential backoff — no user signal | etc.]
(b) USER-VISIBLE BEHAVIOR: [what the user observes or experiences at this tier in the INERTIA state]
(c) VISIBILITY LEVEL: [EXPLICIT — user receives visible error or notification | SILENT — throttle occurs in background with no user notification | DELAYED — user experiences latency or eventual timeout without a throttle-specific error]
(d) RECOVERY PATH: [MANUAL-RETRY | AUTO-BACKOFF | PERMANENT-FAILURE | QUEUE-DELAY | NONE]

Tier rejection rule: A tier described with fewer than all four fields is INCOMPLETE under Standard 2. A tier described in free prose that addresses all four topics without using the template structure is INCOMPLETE. At least two tiers must comply.
```

**Do not begin Phase 1 until both Standard 1 and Standard 2 are written with their respective rejection rules.**

---

**PHASE 1 — RATE LIMIT REGISTRY — INERTIA STATE** *(gate: FORMAT CONTRACT with Standard 1 and Standard 2 both written with rejection rules)*

List all rate-limiting components in binding order for the INERTIA state: name and type, numeric threshold (number + unit; [estimated] for non-public), scope (per-connection / per-environment / per-flow / per-tenant), INERTIA binding-order rationale per component.

At least one component must confirm, extend, or revise CLAIM-A. If this phase identifies a different binding component:
- State: **REVISION TO CLAIM-A**: [new binding component, threshold, causal sentence]
- Fill CLAIM-A's revision slot in Phase 0.

**Do not begin Phase 2 until the Rate Limit Registry is written with at least one numeric threshold, a binding-order rationale for each component, AND — if triggered — CLAIM-A's revision slot is filled in Phase 0.**

---

**PHASE 2 — BACKPRESSURE CHAIN — INERTIA STATE** *(gate: Rate Limit Registry with numeric threshold(s) and per-component rationale written; CLAIM-A slot filled if triggered)*

From the INERTIA binding constraint: at least two directed hops, each with a named mechanism (queue-fill / connection-hold / retry-amplification / dependency-stall / timeout-cascade), terminating at a user-observable effect. This is the INERTIA failure chain.

If the chain contradicts CLAIM-C:
- State: **REVISION TO CLAIM-C**: [corrected status]
- Fill CLAIM-C's revision slot in Phase 0.

**Do not begin Phase 3 until the chain is written with two named-mechanism hops and a user-observable terminal effect; CLAIM-C slot filled if triggered.**

---

**PHASE 3 — BURST PATH AUDIT — INERTIA vs PROTECTED** *(gate: Backpressure Chain with two named-mechanism hops and terminal user-observable effect written; CLAIM-C slot filled if triggered)*

Use Standard 1 schema for the audit table:

| Path | INERTIA Controls | INERTIA Gap Type | PROTECTED Controls | Delta |

- INERTIA Controls: mark each of three checks as PRESENT or ABSENT in the INERTIA state — (1) concurrency cap below rate limit, (2) Retry-After retry policy reading the header, (3) queue buffer between source and endpoint
- INERTIA Gap Type: STRUCTURAL (no mechanism exists in INERTIA) or INCIDENTAL (mechanism exists but bypassed — name the condition) or SAFE (all three controls present)
- PROTECTED Controls: what the PROTECTED state adds to fix an INERTIA gap

This phase must confirm or revise CLAIM-B. If a different path or gap type:
- State: **REVISION TO CLAIM-B**: [corrected path and gap type]
- Fill CLAIM-B's revision slot in Phase 0.

**Do not begin Phase 4 until the Burst Path Audit table is written with INERTIA Controls, INERTIA Gap Type, and PROTECTED Controls for each path; CLAIM-B slot filled if triggered.**

---

**PHASE 4 — RETRY-AFTER EVALUATION — INERTIA STATE** *(gate: Burst Path Audit table with all three column groups written; CLAIM-B slot filled if triggered)*

For each connector and HTTP action: does the INERTIA state read and honor Retry-After (`Retry-After-Ms`, `x-ms-ratelimit-remaining`)? For each gap: name the INERTIA failure mode — retry storm / permanent failure / silent drop / backoff ignoring header value.

If a new Retry-After gap extends CLAIM-B:
- State: **REVISION TO CLAIM-B**: [extended gap finding]
- Update CLAIM-B's revision slot in Phase 0.

**Do not begin Phase 5 until Retry-After findings are written with a handling verdict and named failure mode per gap; CLAIM-B slot updated if triggered.**

---

**PHASE 5 — UX PER THROTTLE TIER — INERTIA STATE** *(gate: Retry-After findings with per-gap failure modes written; CLAIM-B slot updated if triggered)*
*This phase is governed by Format Contract Standard 2.*

For each throttle tier reached in the INERTIA state at any volume band, write one block using the Standard 2 four-field template. Do not use prose form. Do not omit any field. Do not collapse multiple tiers.

At least two tiers. Each tier block: (a) error code/platform signal, (b) user-visible behavior in INERTIA, (c) visibility level, (d) recovery path available to the user in the INERTIA state. A tier missing any field is INCOMPLETE under Standard 2.

**Do not begin Phase 6 until at least two tier blocks are written using the Standard 2 template, each with all four fields (a)(b)(c)(d) present and non-empty.**

---

**PHASE 6 — VOLUME-TO-BEHAVIOR MAP — INERTIA vs PROTECTED** *(gate: At least two UX tier blocks written with all four Standard 2 fields present per block)*
*This phase is governed by Format Contract Standard 1.*

| Volume | INERTIA Behavior | PROTECTED Behavior | Delta |

Volume bands: 1x, 2x, 5x nominal. INERTIA and PROTECTED required for each band.

For the 5x INERTIA row: using the Phase 1 threshold and the 5x request rate, compute (1) % of requests queuing beyond 30 seconds and (2) % failing after retries exhaust. Show the arithmetic step-by-step. A 5x INERTIA cell with only qualitative behavior is INCOMPLETE under Standard 1. The 5x PROTECTED row shows how those numbers change with Phase 9 mitigations applied.

If 5x arithmetic contradicts CLAIM-C severity:
- State: **REVISION TO CLAIM-C**: [corrected classification]
- Update CLAIM-C's revision slot in Phase 0.

**Do not begin Phase 7 until the Volume Map is written with INERTIA and PROTECTED at all three bands, 5x INERTIA arithmetic is shown, and CLAIM-C slot is updated if triggered.**

---

**PHASE 7 — CASCADE SCENARIO — INERTIA STATE** *(gate: Volume Map with INERTIA and PROTECTED at all three bands; 5x INERTIA arithmetic shown; CLAIM-C slot updated if triggered)*

In the INERTIA state: one specific cascade where throttling at the Phase 1 binding constraint causally triggers a second throttle event at a different tier. Name both limits by component and numeric threshold. Show the compounding effect on throughput or error rate. Two independent limits hit under load do not qualify — the second must be caused by the first.

**Do not begin Phase 8 until the Cascade Scenario is written with two named limits, an explicit causal link, and a compounding effect description.**

---

**PHASE 8 — RETRY-AFTER + CASCADING FINDINGS SYNTHESIS** *(gate: Cascade Scenario with two named limits, causal link, and compounding effect written)*

State whether the Cascade Scenario from Phase 7 is worsened by the Retry-After gap from Phase 4. If the missing Retry-After handling on the primary path amplifies the cascade (e.g., retry storm at the first throttle tier triggers the second tier faster than a backoff-respecting client would), describe the amplification. If not, state that the cascade is independent of the Retry-After gap.

**Do not begin Phase 9 until Phase 8 synthesis is written.**

---

**PHASE 9 — MITIGATION PRESCRIPTIONS — INERTIA TO PROTECTED** *(gate: Phase 8 synthesis written; all prior phases complete)*
*This phase is governed by Format Contract Standard 1.*

For each bottleneck and burst path from Phases 1 and 3, one row per finding:

| Finding | INERTIA Behavior | PROTECTED Behavior | Delta |

- INERTIA Behavior: specific system behavior at this bottleneck in the INERTIA state — tied to this component and load condition, not generic
- PROTECTED Behavior: system behavior after the specific mitigation — name the exact action, connector, or setting changed
- Delta: measurable improvement in throughput, error rate, or queue depth

Generic advice ("add retry logic") without naming the specific control and location fails.

---

**Phase 0 final state**: All three revision slots in Phase 0 should reflect the simulation outcome. Filled slots name the revising phase and what changed. Empty slots mean the corresponding INERTIA claim held through all nine evidence phases without contradiction. A reader consulting only Phase 0 knows the current state of all three INERTIA findings.
