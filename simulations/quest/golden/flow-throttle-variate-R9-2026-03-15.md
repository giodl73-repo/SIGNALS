# flow-throttle Variate — Round 9
**Date:** 2026-03-15
**Rubric:** v9 (C-01 through C-34, essential/recommended/aspirational)
**Baseline ceiling:** R8 V-05 (C-31+C-32 full-surface; v9 adds C-33 enumerated-block form and C-34 compound block)

---

## State Analysis: What R8 Established vs. What R9 Must Add

**R8 confirmed:**
- C-31: All three gates carry explicit negative invariants (not just the correction gate)
- C-32: The correction gate prescribes rewrite location as "immediately below the `[FAIL]` annotation"
- R8 V-03 and V-05 showed that the inline single-sentence negative form (C-31) generalizes
  to a separate enumerated-list block when multiple subsidiary criteria are present — this
  excellence pattern became C-33
- R8 V-05 showed that when a gate governs both item disposition AND spatial co-location, the
  not-cleared block must enumerate both predicates as a compound list — this became C-34

**C-33 failure mode in R8 V-01 / V-02 / V-04:**
GATE 1 and GATE 2 used the inline dash-append form: "cleared when [conditions] — no row may
be absent, no cell may be blank." When a gate's positive predicate already lists three or more
conditions, appending the negation inline conflates the positive and negative state
declarations. The inline form passes C-31 but fails C-33 because each failure state is not
independently scannable. Only the enumerated-list block form — "GATE N is not cleared when
any of the following failure states are present: [list]" — satisfies C-33.

**C-34 failure mode in R8 V-01 through V-04:**
The correction gate in R8 V-01 through V-04 satisfied C-31 (negative invariant present) and
C-32 (spatial prescription) but declared them separately: one sentence for undisposed items,
one sentence for spatial co-location. C-34 requires the compound list form: a single
"not-cleared when" block that enumerates BOTH the item-disposition failure predicate AND the
spatial co-location failure predicate as distinct list items. Scattering them across separate
declarations requires cross-reference to derive full gate state; only the compound block makes
gate state derivable by inspection of the block alone.

**R9 structural additions required:**
1. GATE 1 and GATE 2: replace inline negative append with enumerated-list not-cleared blocks
   (each subsidiary failure condition as a separate list item)
2. GATE 3 (cascade check): enumerated not-cleared block (also multiple conditions → C-33)
3. CORRECTION GATE: compound not-cleared block covering both item disposition (C-31) and
   spatial co-location (C-32) as a single enumerated list (C-34)

**R9 design hypothesis:** C-33 and C-34 evaluate structural form of gate declarations —
enumerated-list block vs. inline append — not content decisions (role, format, register,
emphasis, or inertia framing). All five content axes are predicted to be inert for C-33/C-34.
Any variation that uses enumerated blocks for GATE 1/2/3 and a compound block for the
CORRECTION GATE will satisfy both criteria regardless of what the phases contain.

---

## Round 9 Variation Map

| Variation | Axis | C-33 | C-34 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Role sequence: PA architect (Round 1) + connector engineer (Round 2) | PASS | PASS | v9 ceiling |
| V-02 | Output format: prose-primary, no tables in Phases 2–3 | PASS | PASS | v9 ceiling |
| V-03 | Lifecycle emphasis: cascade-first, Phase 2 compressed | PASS | PASS | v9 ceiling |
| V-04 | Phrasing register (conversational) + inertia framing | PASS | PASS | v9 ceiling |
| V-05 | Role sequence (single throughput analyst) + output format (lists) | PASS | PASS | v9 ceiling |

All five predicted at v9 ceiling. Expected confirmation: (1) enumerated-list gate blocks
(C-33) survive all five content axes — role persona, prose format, cascade emphasis,
conversational register, and list format do not disturb gate declaration structure.
(2) The compound CORRECTION GATE block (C-34) is equally axis-inert: whether Phase 4 is
preceded by a compressed or expanded Phase 2/3, the CORRECTION GATE block form depends only
on the gate's own declaration, not on upstream phase content.

---

## V-01 — Role Sequence: PA Architect (Round 1) + Connector Engineer (Round 2)

**Axis:** Role sequence — Round 1 is owned by a Power Automate flow architect who owns the
bottleneck topology and cascade model. Round 2 is owned by a connector support engineer who
owns exact construct naming and rate unit sources. The role switch is declared at the Round 1
opening and confirmed at the Round 2 role marker. Gate declarations and block structure are
unchanged by the role split.

**Hypothesis:** v9 ceiling. Role assignment affects expertise framing, not gate declaration
form. C-33 evaluates whether failure states appear as enumerated list items in a dedicated
block — role persona has no bearing on this. C-34 evaluates whether the CORRECTION GATE block
enumerates both item-disposition and spatial co-location predicates — the role executing the
gate does not change the block's list structure. Expected: v9 ceiling.

---

You are a Power Automate flow architect simulating throughput across a rate-limited Power
Automate system. For Round 2, you will adopt the role of a connector support engineer to apply
construct-precision verification.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: Power Automate flow architect.*

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic "API
limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type from the domain list, (b) a numeric limit with unit, and (c) a request
contribution estimate with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type rather than an exact PA term
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

Rows in any of the above failure states receive a `?` flag — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two
hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. UX
categories MUST differ across tiers. Each row must state what the user sees or experiences —
not what the system does internally.

**GATE 2** is cleared when and only when: TABLE 3 has >= 2 complete hops with a named
terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has a "why this
order holds" explanation for each row.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 complete hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share the same UX category
- TABLE 2 has any row without a "why this order holds" explanation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with unbounded
fan-out, high-frequency trigger with no debounce, nested loops, batch-size misconfigurations.
If none found, write explicit acknowledgment with guards currently in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.
If no gap, state why every consumer correctly honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism linking
them. A flat list of independent throttle risks without cascade relationships does not pass.

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all
required fields populated and distinct Tier A / Tier B constructs.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A equal to Tier B
- Any TABLE 7 row is missing a stated throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row, mark either `[PASS: confirmed]` (the name
is the exact documented PA term) or `[FAIL: corrected below]` (the name requires correction).
For any `[FAIL]` item, write the corrected construct name, limit source, and precision note
immediately below the `[FAIL]` annotation before proceeding.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

*Flow architect: confirm the exact documented term or flag for Round 2 connector engineer
correction. Generic terms must be flagged here. "Confirmed" requires the exact PA
documentation name — not paraphrase.*

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have a corrected construct name, limit source, and
  precision note immediately below its `[FAIL]` annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior. Internal
system behavior (queue depth increase, internal retry count) is not user experience. Correct
any row that conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation time
or headroom]."

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs. "Add retries" and "reduce load" do not
count. Each remediation must map to a specific finding from PHASES 2–3 by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition each
signal surfaces and when it would trigger.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State the
impact: does the entitlement change shift any TABLE 9 row from SAFE to OVER-LIMIT or vice
versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling. "Test in staging" without a
specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the flow architect's analysis is not evidence of
Round 2's connector-level precision. A thorough, coherent Round 1 output can still contain PA
construct names that are imprecise, rate units drawn from estimates rather than documentation,
or cascade load estimates using directional language where numeric precision is required. Round
2 operates independently of Round 1's output quality.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

*Role: Connector support engineer.*

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? Does it match the product-published limit source?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a derived
   estimate? State the source (PA documentation, connector certification, admin center
   observed value, or estimate with confidence level).

3. **Rate unit precision:** Is the unit per-minute, per-second, per-24-hours, per-user, or
   per-environment? Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact
   signal path and load calculation) or qualitative? Promote qualitative statements to
   structural ones using TABLE 9 arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a directional
   statement? If directional, compute the numeric projection from TABLE 9 data.

Write the Round 2 precision output:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-01 prompt body.*

---

## V-02 — Output Format: Prose-Primary Analysis

**Axis:** Output format — labeled prose paragraphs replace markdown tables for Phase 2 and
Phase 3 analysis sections. Phase 1 retains TABLE 1 (construct inventory requires structured
data). Phase 4 retains tables (precision audit, throttle budget, remediations). Sections
2.A–2.C and 3.A–3.C use labeled paragraph blocks with explicit field requirements stated
inline. Gate declarations are structurally unchanged: enumerated not-cleared blocks
(C-33) and the compound CORRECTION GATE block (C-34) appear exactly as in V-01.

**Hypothesis:** v9 ceiling. Output format controls how analysis is laid out. C-33 evaluates
gate declaration structure — whether the not-cleared conditions appear as an independent
enumerated-list block. Replacing phase tables with prose paragraphs does not affect the gate
declaration, which is a structural marker following each phase. C-34 evaluates the CORRECTION
GATE block in Phase 4.A, which retains its table structure across all format variations.
Expected: v9 ceiling.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic terms
do not pass.

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type from the domain list, (b) a numeric limit with unit, and (c) a request
contribution estimate with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type rather than an exact PA term
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

Rows in any of the above failure states receive a `?` flag — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write three labeled paragraphs:

**Bottleneck paragraph:** Identify the primary bottleneck by name. State the PA construct
type, the saturation rate under this scenario's volume, and the reason this ordering holds.
Explain in one sentence why limits are non-independent (cascade chain or shared principal
pool).

**Hit order paragraph:** Describe the throttle tier sequence in explicit order — first,
second, and any subsequent. For each tier, name the construct, its limit, and why it
saturates before the next at this aggregate volume. An unordered enumeration without ordering
rationale does not satisfy this section.

**Ordering validation paragraph:** State one sentence confirming that the bottleneck analysis
accounts for shared resource pools that make per-construct limits interdependent.

**Section 2.B — Backpressure Hop Chain**

Write the propagation trace as labeled hops. Minimum: two hops.

**Hop 1:** `[From component]` emits `[signal type]` signal `[exact value or code]`.
`[To component]` receives the signal and `[response behavior]`.

**Hop 2 (and further, if applicable):** Continue from the last receiving component using the
same format.

**Terminal state:** Name the terminal outcome — user-visible error, flow run failure, or
silent drop — and which component reaches it.

**Section 2.C — User Experience per Throttle Tier**

Write one labeled paragraph per UX tier. Minimum: two tiers with distinct UX categories.

**Tier [N] — [UX category]:** The user experiences `[specific observable state]` at this
throttle tier. The system action is `[internal behavior]`, which surfaces as `[what the user
sees or does not see]`. UX category: transparent-retry / visible-delay / error-surfaced /
silent-loss.

UX categories must differ across tiers.

**GATE 2** is cleared when and only when: Section 2.B has >= 2 labeled hops with a named
terminal state; Section 2.C has >= 2 tier paragraphs with distinct UX categories; Section
2.A includes a "why this order holds" explanation for each tier.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section 2.B has fewer than 2 labeled hops, or is missing a named terminal state
- Section 2.C has fewer than 2 tier paragraphs, or any two paragraphs share the same UX
  category
- Section 2.A is missing a "why this order holds" explanation for any tier

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

For each burst-exposed path, write a labeled prose entry:

**Burst path [N]:** Flow construct `[name]` at `[location]` uses PA construct type `[type]`.
Estimated peak rate: `[N req/unit]`. This path bypasses or overwhelms the tier-1 guard
because `[mechanism]`.

Check all patterns: Apply to Each with no concurrency cap, parallel branches with unbounded
fan-out, high-frequency trigger without debounce, nested loops, batch-size misconfigurations.
If none found, write an explicit acknowledgment naming the guards currently in place.

**Section 3.B — Retry-After Gaps**

For each gap, write a labeled prose entry:

**Gap [N]:** Consumer construct `[name]` receives a 429 at `[location]`. Retry-After header:
`[read / not read]`. Actual backoff: `[description]`. Failure mode: retry-storm /
fixed-misalign / silent-discard.

At least one gap required. If no gap, explain why every consumer correctly honors Retry-After
and name the PA mechanism enforcing it.

**Section 3.C — Cascade Risk Pairs**

For each cascade pair, write a labeled prose entry:

**Cascade [label]:** Tier A — `[construct]` throttled via `[mechanism]`. Load added to Tier
B: `[numeric or directional estimate]`. Tier B — `[construct]`. Failure mode: `[description]`.
Severity: critical / high / medium. Duration: `[estimated]`.

Minimum: two cascade pairs with distinct Tier A / Tier B constructs. A flat enumeration of
independent throttle risks without cascade relationships does not satisfy this section.

**GATE 3** is cleared when and only when Section 3.C has >= 2 complete cascade pair entries
with distinct Tier A / Tier B constructs, a stated throttle mechanism, and severity assessed.

**GATE 3 is not cleared when any of the following failure states are present:**
- Section 3.C has fewer than 2 cascade pair entries
- Any cascade entry has Tier A equal to Tier B
- Any cascade entry is missing a stated throttle mechanism
- Any cascade entry is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row, mark either `[PASS: confirmed]` or
`[FAIL: corrected below]`. For any `[FAIL]` item, write the corrected construct name, limit
source, and precision note immediately below the `[FAIL]` annotation.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have a corrected construct name, limit source, and
  precision note immediately below its `[FAIL]` annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

**Section 4.B — UX Validation**

Review each tier paragraph from Section 2.C. Write one validation sentence per tier.
Correct any paragraph that conflates internal system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings from PHASES 2–3 by label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal and the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 status row.

**Section 4.G — Test Approach**

At least one concrete PA tooling test step. "Test in staging" without a specific method does
not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 2's
structural precision. A thorough, coherent Round 1 output — whether expressed in prose or
table form — can still contain PA construct names drawn from paraphrase rather than
documentation, rate units from estimates rather than documented platform values, or cascade
descriptions using directional language where numeric precision is required. Round 2 operates
independently of Round 1's output quality and format choices.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation?

2. **Numeric limit precision:** Is the limit value documented or estimated? State the source.

3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement
   granularity (per-minute, per-24-hours, per-user, per-environment).

For each cascade pair entry in Section 3.C, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism structural (exact signal path and load
   calculation) or qualitative? Promote qualitative statements using TABLE 9 arithmetic.

2. **Load-added precision:** Is the load estimate numeric? If directional, compute the
   projection from TABLE 9 data.

Write the Round 2 precision output:

**TABLE 11 — Round 2 Precision Audit**

| Item (section + label) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Lifecycle Emphasis: Cascade-First, Phase 2 Compressed

**Axis:** Lifecycle emphasis — Phase 3 (cascade and exposure analysis) is elevated to primary
analytical emphasis with expanded cascade coverage including priority ranking. Phase 2
(bottleneck and UX) is compressed to a mandatory minimum: a single bottleneck statement, a
two-tier hit-order entry, a one-sentence terminal propagation path, and two named UX outcomes.
Gate declarations maintain C-33/C-34 structure; GATE 2's conditions match the compressed
Phase 2 minimum.

**Hypothesis:** v9 ceiling. Lifecycle emphasis controls relative analytical volume per phase
and does not affect gate declaration form. The enumerated not-cleared blocks (C-33) and the
compound CORRECTION GATE block (C-34) are structural markers at phase boundaries — their
content is phase-allocation-independent. Compressing Phase 2 to a minimum does not reduce the
gate declaration to a simpler form; the block structure is maintained regardless of how much
analytical content precedes it. Expected: v9 ceiling.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across a
rate-limited Power Automate system. This analysis emphasizes cascade risk: the most dangerous
throttle failures occur not at first saturation but when Tier A saturation triggers Tier B
overload before any recovery path is available.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Cascade Risk Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types must be exact documented terms: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits.

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type from the domain list, (b) a numeric limit with unit, and (c) a request
contribution estimate with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type rather than an exact PA term
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck Identification (Compressed)

*(GATE 1 must pass before this phase executes.)*

**Bottleneck statement (required):**

> "[Specific component] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] under this scenario because [reason]. Limits are non-independent because
> [one sentence on cascade chain or shared principal pool]."

**TABLE 2 — Hit Order (minimum two tiers)**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Terminal propagation path (minimum):** Name the signal path from the bottleneck to the
terminal state in one sentence: "[bottleneck construct] emits [signal type] → [next
component] → [terminal state: user-visible error / flow run failure / silent drop]."

**UX minimum:** Name two throttle tiers with distinct UX categories (transparent-retry /
visible-delay / error-surfaced / silent-loss). One sentence each.

**GATE 2** is cleared when and only when: the bottleneck statement is present with ordering
rationale; TABLE 2 has >= 2 rows each with a "why this order holds" explanation; a terminal
propagation path is stated; two UX outcomes with distinct categories are named.

**GATE 2 is not cleared when any of the following failure states are present:**
- The bottleneck statement is absent or missing its ordering rationale
- TABLE 2 has fewer than 2 rows, or any row is missing a "why this order holds" explanation
- The terminal propagation path is absent or does not name a terminal state
- Fewer than 2 UX outcomes are named, or any two share the same UX category

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Cascade Risk Analysis (Primary)

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Path Register**

**TABLE 3 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Guard in place (or NONE) | Why bypass occurs |
|----------------|------------------|-----------------|--------------------|--------------------------|--------------------|

Check all patterns: Apply to Each with no concurrency cap, parallel branches with unbounded
fan-out, high-frequency trigger without debounce, nested loops, batch-size misconfigurations.

**Section 3.B — Retry-After Gap Analysis**

**TABLE 4 — Retry-After Gaps**

| Consumer construct | 429 location | Header read? | Backoff behavior | Failure mode |
|-------------------|-------------|--------------|------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register (Primary)**

For each cascade pair, provide the full causal chain: what state change at Tier A generates
what additional load at Tier B, with numeric estimate where possible.

**TABLE 5 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle trigger | Load added to Tier B | Tier B construct | Tier B limit | Headroom after load | Failure mode | Severity | Recovery window |
|---------------|-----------------|-----------------|----------------------|-----------------|-------------|---------------------|--------------|----------|----------------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, numeric Tier B load
estimate, and severity and recovery window assessed. At least one pair where Tier B belongs to
a different PA construct type than Tier A.

**Section 3.D — Cascade Priority Ranking**

Rank the TABLE 5 cascade pairs by severity × estimated exposure window. Write one sentence
per pair justifying its rank.

**GATE 3** is cleared when and only when TABLE 5 has >= 2 complete cascade pairs with all
columns filled, distinct Tier A / Tier B constructs, numeric load estimates, and severity
assessed; and Section 3.D has a prioritized ranking with one justification sentence per pair.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 5 has fewer than 2 cascade pairs
- Any TABLE 5 row has Tier A equal to Tier B
- Any TABLE 5 row is missing a numeric load estimate for Tier B
- Any TABLE 5 row is missing a severity or recovery window assessment
- Section 3.D is absent or missing a justification sentence for any cascade pair

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Mark each `[PASS: confirmed]` or `[FAIL: corrected below]`.
For any `[FAIL]` item, write the corrected construct name, limit source, and precision note
immediately below the `[FAIL]` annotation.

**TABLE 6 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

**CORRECTION GATE** is cleared when and only when every TABLE 6 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 6 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 6 `[FAIL]` row does not have a corrected construct name, limit source, and
  precision note immediately below its `[FAIL]` annotation

*Sections 4.B through 4.F are blocked until the CORRECTION GATE is cleared.*

**Section 4.B — Quantified Risk Register**

**TABLE 7 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.C — PA-Specific Remediations**

**TABLE 8 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations, each mapped to a specific cascade finding from TABLE 5
by cascade label.

**Section 4.D — Monitoring Signals**

Name at least one PA-observable signal. State the condition it surfaces and when it triggers.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 7 status row.

**Section 4.F — Test Approach**

At least one concrete PA tooling test step targeting cascade behavior specifically.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the cascade risk analysis is not evidence of Round
2's structural precision. A thorough cascade analysis with well-prioritized severity rankings
and numeric load estimates can still contain PA construct names drawn from paraphrase rather
than documentation, load estimates unsupported by TABLE 7 arithmetic, or recovery window
claims without mechanism basis. Round 2 operates independently of Round 1's analytical depth
and cascade coverage.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 6 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 6 corrections
were finalized.

---

For each row in TABLE 6, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation?

2. **Numeric limit precision:** Is the limit value documented or estimated? State the source.

3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair in TABLE 5, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism structural (exact signal path and load
   calculation) or qualitative? Promote qualitative statements using TABLE 7 arithmetic.

2. **Load-added precision:** Is the Tier B load estimate numeric? If directional, compute
   from TABLE 7.

3. **Recovery window precision:** Is the recovery window derived from a PA retry or queue
   mechanism, or estimated? State the basis.

Write the Round 2 precision output:

**TABLE 9 — Round 2 Precision Audit**

| Item (TABLE ref + label) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Phrasing Register (Conversational) + Inertia Framing

**Axis:** Phrasing register (conversational and descriptive — "your job is to," "consider
how," "when you see") combined with inertia framing (each phase opens by describing the
current-state barrier — what is typically absent or broken in production — before stating the
analytical task). Phrasing applies throughout ROUND 1. Inertia preambles appear at the start
of each phase and each major section. Gate declarations use the same enumerated-block
structure; only the surrounding prose register changes.

**Hypothesis:** v9 ceiling. Conversational register affects sentence structure and frame.
Inertia preambles add current-state context before analytical tasks. Neither changes the form
of gate declarations. C-33 tests whether the not-cleared conditions appear as an independent
enumerated list — this is a structural property of the gate block, not affected by the phrasing
of the phase instructions that precede it. C-34 tests the CORRECTION GATE block structure
in Phase 4.A, which is insulated from register choices made in Phases 1–3. Expected: v9
ceiling.

---

You are a Connectors / Power Automate throughput domain expert. Your job is to simulate what
actually happens when a rate-limited Power Automate flow is pushed to its operational volume —
tracing where it breaks, how fast, and what the user experiences.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

**Current-state barrier:** Most PA flows are deployed without a map of which throttle tiers
are present or which will be hit first under load. The result is reactive firefighting when
the first 429 surfaces in production — often weeks after the flow went live.

Your job: map every throttle-relevant construct in the flow to its exact PA construct type,
numeric limit, and request contribution at the scenario's volume. Populate TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** When you name a PA construct type, use the exact documented term — Power
Platform request entitlements, connector throttling policies, flow run concurrency limits,
action call limits, premium vs. standard connector tiers, or Microsoft 365 service protection
limits. Generic terms like "API limit" or "service limit" are not acceptable.

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type from the domain list, (b) a numeric limit with unit, and (c) a request
contribution estimate with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type rather than an exact PA term
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

Rows in any of the above failure states get a `?` flag — resolve before moving to PHASE 2.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Current-state barrier:** Most PA flows hit throttle limits without anyone identifying the
binding constraint or understanding why it saturates first. When 429s appear, the first guess
is usually wrong because limits share principal pools or accumulate across nested constructs.

**Section 2.A — Rate Limit Hit Ordering**

Think through which tier will saturate first at this volume and why. Write the bottleneck
statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Section 2.B — Backpressure Hop Chain**

**Current-state barrier:** When a 429 is issued, the signal rarely travels cleanly to the
surface. Intermediate constructs absorb, drop, or transform it — which is why the user
experience often doesn't match what the logs show.

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two
hops. Trace to terminal state.

**Section 2.C — User Experience per Throttle Tier**

**Current-state barrier:** The internal system response to throttling is not what the user
sees. Queue depth increases and retry counts are frequently reported as user experience, which
produces UX claims that don't match PA runtime behavior.

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Consider
what the user actually sees — not what the system is doing internally. UX categories must
differ across tiers.

**GATE 2** is cleared when and only when: TABLE 3 has >= 2 complete hops with a named
terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has a "why this
order holds" explanation for each row.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 complete hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share the same UX category
- TABLE 2 has any row without a "why this order holds" explanation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Current-state barrier:** PA flows routinely include constructs that generate burst loads
with no guard — uncapped Apply to Each loops, unbounded parallel branches. These are treated
as default behavior until they cause an outage. Consider what would happen at the first
unexpected batch event or concurrent submission storm.

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each loop with no concurrency cap, parallel branches with unbounded fan-out,
high-frequency trigger with no debounce, nested loops, batch-size misconfigurations.

**Section 3.B — Retry-After Gaps**

**Current-state barrier:** The most common retry implementation in PA is a fixed-interval
loop — which ignores the Retry-After header and causes retry storms at the exact moment the
tier is already saturated.

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism linking
them. Think through what happens at Tier B after Tier A saturates — the failure at Tier B is
often the more destructive one.

**GATE 3** is cleared when and only when TABLE 7 has >= 2 complete cascade pairs with all
required fields populated and distinct Tier A / Tier B constructs.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A equal to Tier B
- Any TABLE 7 row is missing a stated throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Consider each entry in TABLE 1. When you confirm a construct name, you're asserting it matches
the exact term in PA documentation. When you correct it, explain why the original was a
paraphrase or category name. Mark each row `[PASS: confirmed]` or `[FAIL: corrected below]`.
For any `[FAIL]` item, write the corrected name, limit source, and precision note immediately
below the `[FAIL]` annotation.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have a corrected construct name, limit source, and
  precision note immediately below its `[FAIL]` annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

**Section 4.B — UX Validation**

Review each row in TABLE 4. Ask: does this UX category describe what the user sees, or what
the system does? Correct any row that conflates internal state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

Think through what PA-native configurations directly address the findings in PHASES 2–3.
Generic advice doesn't pass.

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations, each mapped to a specific finding by section label.

**Section 4.E — Monitoring Signals**

What PA-observable signal would surface the throttle condition before it becomes a
user-visible failure? Name the signal and the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

Consider how the entitlement tier changes what limits apply. Name one boundary that
materially shifts a TABLE 9 status row.

**Section 4.G — Test Approach**

How would you validate this throttle analysis before production? Describe at least one
concrete step using PA tooling.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 2's structural
precision. A well-framed, coherent Round 1 output — with thorough inertia framing and clear
current-state narratives — can still contain PA construct names drawn from paraphrase rather
than documentation, numeric limits based on estimates rather than documented platform values,
or cascade load estimates that are directional where numeric precision is required. Round 2
operates independently of Round 1's output quality and framing depth.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation?

2. **Numeric limit precision:** Is the limit value documented or estimated? State the source.

3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism structural (exact signal path and load
   calculation) or qualitative? Promote qualitative statements using TABLE 9 arithmetic.

2. **Load-added precision:** Is the load estimate numeric? If directional, compute from
   TABLE 9.

Write the Round 2 precision output:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — Combined: Single Throughput Analyst + List-Based Output (Phases 2–3)

**Axis:** Role sequence (single Connectors / Power Automate throughput analyst throughout,
no role switch at Round 2 — Round 2 applies a precision filter from the same analytical
perspective rather than adopting a second distinct role) combined with output format (bulleted
list entries replace tables in Phases 2 and 3; Phase 1 TABLE 1 and Phase 4 tables are
retained as structured data). Gate declarations are unchanged: enumerated not-cleared blocks
(C-33) and compound CORRECTION GATE block (C-34) appear as in V-01 through V-04.

**Hypothesis:** v9 ceiling. Role sequence affects framing of the Round 2 independence
declaration — a single-role format requires the independence claim to be formulated without
reference to a separate evaluator persona. Output format for Phases 2–3 affects how analytical
findings are expressed. Neither changes gate declaration form. C-33/C-34 survive the
single-role and list-format axes because the enumerated blocks and compound block are
structural markers that follow each phase regardless of what output format the phase uses.
Expected: v9 ceiling.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system. This analysis runs in two rounds: Round 1 builds the
throttle tier model and exposure analysis; Round 2 applies a precision filter to confirm every
construct name and numeric claim against documented platform sources.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic terms
do not pass.

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type from the domain list, (b) a numeric limit with unit, and (c) a request
contribution estimate with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type rather than an exact PA term
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

*PHASE 2 is blocked until GATE 1 is cleared.*

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason]. Limits are
> non-independent because [cascade chain or shared principal pool]."

List the hit order. Minimum: two entries. For each:

- **Hit [N]:** `[construct]` — limit: `[N req/unit]` — why this order holds: `[reason]`

**Section 2.B — Backpressure Hop Chain**

List the propagation hops. Minimum: two hops, then terminal state.

- **Hop 1:** `[from component]` emits `[signal type: error code / retry-after header /
  queue depth increase / other]` → `[to component]` responds with `[behavior]`
- **Hop 2:** `[from component]` → `[to component]` → `[behavior]`
- **Terminal state:** `[user-visible error / flow run failure / silent drop]` reached at
  `[component]`

**Section 2.C — User Experience per Throttle Tier**

List the UX outcomes per tier. Minimum: two tiers with distinct UX categories.

- **Tier [N] ([UX category]):** User sees `[observable state]`. System action: `[internal
  behavior]`. UX category: transparent-retry / visible-delay / error-surfaced / silent-loss.

UX categories must differ across tiers. Each entry must state what the user sees — not what
the system does internally.

**GATE 2** is cleared when and only when: Section 2.B has >= 2 listed hops with a named
terminal state; Section 2.C has >= 2 tier entries with distinct UX categories; Section 2.A
has a "why this order holds" entry for each tier.

**GATE 2 is not cleared when any of the following failure states are present:**
- Section 2.B has fewer than 2 listed hops, or is missing a named terminal state
- Section 2.C has fewer than 2 tier entries, or any two entries share the same UX category
- Section 2.A is missing a "why this order holds" entry for any tier

*PHASE 3 is blocked until GATE 2 is cleared.*

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

List each burst-exposed path:

- **Burst path [N]:** `[flow construct]` at `[location]` — PA type: `[type]` — peak rate:
  `[N req/unit]` — bypass reason: `[mechanism]`

Check patterns: Apply to Each with no concurrency cap, parallel branches with unbounded
fan-out, high-frequency trigger without debounce, nested loops, batch-size misconfigurations.
If none found, write explicit acknowledgment with guards currently in place.

**Section 3.B — Retry-After Gaps**

List each gap:

- **Gap [N]:** `[consumer construct]` receives 429 at `[location]` — Retry-After read:
  `[yes / no]` — backoff: `[description]` — failure mode: retry-storm / fixed-misalign /
  silent-discard

At least one gap required.

**Section 3.C — Cascade Risk Pairs**

List each cascade pair:

- **Cascade [label]:** Tier A: `[construct]` throttled via `[mechanism]` — load added to
  Tier B: `[estimate]` — Tier B: `[construct]` — failure mode: `[description]` —
  severity: critical / high / medium — duration: `[estimated]`

Minimum: two cascade pairs with distinct Tier A / Tier B constructs.

**GATE 3** is cleared when and only when Section 3.C has >= 2 cascade pair entries with all
required fields, distinct Tier A / Tier B constructs, stated mechanism, and severity assessed.

**GATE 3 is not cleared when any of the following failure states are present:**
- Section 3.C has fewer than 2 cascade pair entries
- Any cascade entry has Tier A equal to Tier B
- Any cascade entry is missing a stated throttle mechanism
- Any cascade entry is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Mark each `[PASS: confirmed]` or `[FAIL: corrected below]`.
For any `[FAIL]` item, write the corrected construct name, limit source, and precision note
immediately below the `[FAIL]` annotation.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have a corrected construct name, limit source, and
  precision note immediately below its `[FAIL]` annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

**Section 4.B — UX Validation**

Review TABLE 1 UX categories. Confirm or correct each against PA runtime behavior. Correct
any entry that conflates internal system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings from PHASES 2–3.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal and the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 9 status row.

**Section 4.G — Test Approach**

At least one concrete PA tooling test step.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1 analytical output is not evidence of Round 2 precision. The same
analytical perspective that produced the throttle tier model and exposure analysis can still
contain construct names drawn from paraphrase rather than documentation, numeric limits based
on estimates rather than platform values, or cascade load entries using directional language
where numeric precision is required. Round 2 applies a precision filter independent of Round
1's analytical confidence.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a derived
   estimate? State the source.

3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement
   granularity (per-minute, per-24-hours, per-user, per-environment).

For each cascade pair entry in Section 3.C, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism structural (exact signal path and load
   calculation) or qualitative? Promote qualitative statements using TABLE 9 arithmetic.

2. **Load-added precision:** Is the load estimate numeric? If directional, compute from
   TABLE 9 data.

Write the Round 2 precision output:

**TABLE 11 — Round 2 Precision Audit**

| Item (section + entry) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*
