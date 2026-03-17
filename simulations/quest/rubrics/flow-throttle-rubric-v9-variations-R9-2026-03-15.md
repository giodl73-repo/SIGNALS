# flow-throttle — Round 9 Variations (v9 Rubric, 160-point max)

## Variation Axes and Hypotheses

R8 confirmed that both temporal and imperative boundary-event phrase forms (C-27) reach the
154/154 v8 ceiling when paired with round-head immediacy (C-26). Under v9, both R8 V-03 and
V-04 retroactively score 160/160 via C-29 (C-26 ∩ C-27) and C-30 (C-27 ∩ C-28).

**C-29** (3 pts): C-26 (round-head immediacy) AND C-27 (round-name in boundary-event phrase)
from the same container — forming a closed navigational loop: the heading declares the barrier,
the phrase echoes the barrier label, and the container is structurally adjacent to both.

**C-30** (3 pts): C-27 (round-name phrase) AND C-28 (C-25 ∩ C-26, dual machine-verifiability)
from the same container — adding heading cross-reference as a third orthogonal verification
path to the dual-lock established by C-28.

**Dependency consequence (key R9 finding):** C-27 requires C-25 as a precondition. Therefore
satisfying C-29 (C-26 ∩ C-27) transitively satisfies C-25. Combined with C-26 already present,
C-28 (C-25 ∩ C-26) is also satisfied. And since C-30 requires C-27 AND C-28 — both of which
are now implied — C-29 → C-30. The rubric also states C-30 → C-29. Therefore **C-29 ↔ C-30**:
they are co-determined. No structural arrangement can pass C-29 while failing C-30 or vice
versa.

**R9 design consequence:** With C-29 and C-30 co-determined, R9 cannot isolate them as
independent failure modes the way R8 isolated C-27 and C-28. Instead, R9 confirms that the
five content axes — role sequence, output format, lifecycle emphasis, phrasing register, and
inertia framing — are all structurally inert for C-29 and C-30. This mirrors the R6 finding
that confirmed content-axis inertness for C-25 and C-26.

Three single-axis content tests (V-01, V-02, V-03), then two combination tests (V-04, V-05):

| Variation | Axis | C-25 | C-26 | C-27 | C-28 | C-29 | C-30 | Predicted score |
|-----------|------|------|------|------|------|------|------|-----------------|
| V-01 | Role sequence: PA architect + connector engineer | PASS | PASS | PASS | PASS | PASS | PASS | 160/160 |
| V-02 | Output format: prose-primary, no tables in Phases 2–3 | PASS | PASS | PASS | PASS | PASS | PASS | 160/160 |
| V-03 | Lifecycle emphasis: cascade-first, bottleneck compressed | PASS | PASS | PASS | PASS | PASS | PASS | 160/160 |
| V-04 | Phrasing register (conversational) + inertia framing | PASS | PASS | PASS | PASS | PASS | PASS | 160/160 |
| V-05 | Role sequence (throughput analyst) + output format (lists) | PASS | PASS | PASS | PASS | PASS | PASS | 160/160 |

All five predicted at 160/160. Expected confirmation: (1) C-29 and C-30 are always
co-satisfied — the co-determination finding is structurally necessary, not incidental.
(2) All five content axes are inert for C-29 and C-30. A variation passing C-27 and C-26 from
the same immediately-adjacent container will always earn both C-29 and C-30.

---

## V-01 — Role Sequence: PA Architect (Round 1) + Connector Engineer (Round 2)

**Axis:** Role sequence — two distinct expert roles lead the two rounds. Round 1 is owned by a
Power Automate flow architect who owns the bottleneck topology and cascade model. Round 2 is
owned by a connector support engineer who owns exact construct naming and rate unit sources.
The role switch happens at the Round 2 barrier — same document, different evaluator persona.

**Hypothesis:** Ceiling maintained (160/160). Role assignment affects expertise framing but not
the structural placement or phrase content of the Round 2 pre-barrier container. C-26
(heading-to-container adjacency), C-27 (phrase names "Round 2"), C-28 (C-25 ∩ C-26), C-29
(C-26 ∩ C-27), and C-30 (C-27 ∩ C-28) all evaluate structure and phrase text, not which
expert persona is declared. Role persona is content; barrier placement is structure.
Expected: 160/160.

---

You are a Power Automate flow architect simulating throughput across a rate-limited Power
Automate system. For Round 2, you will adopt the role of a connector support engineer to
apply construct-precision verification.

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

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list, (b) a
numeric limit with unit, (c) a request contribution estimate with arithmetic shown. Block:
PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing fields
receive a `?` flag — correct before proceeding.

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

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Rule: UX categories MUST differ across tiers. Each row must state what the user sees or
experiences — not what the system does internally.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write explicit acknowledgment with guards currently in place.

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

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them. A flat list of independent throttle risks without cascade relationships does
not pass.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Flow architect: either confirm the exact documented term or flag for Round 2 connector
engineer correction. Generic terms must be flagged here. "Confirmed" requires the exact PA
documentation name — not paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior. Internal
system behavior (e.g., queue depth increase, internal retry count) is not user experience.
Correct any row that conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation time
or headroom]." A qualitative "this will hit the limit" without numeric projection does not pass.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs (e.g., concurrency control settings,
flow run queuing, Delay action with Retry-After value, request batching via Data Operations,
premium connector entitlement upgrade). "Add retries" and "reduce load" do not count. Each
remediation must map to a specific finding from PHASES 2–3 by label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition each
signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs (e.g.,
Office 365 E3 vs. Power Apps per-user plan request entitlements). State the impact on this
scenario's volume: does the entitlement change shift any TABLE 9 row from SAFE to OVER-LIMIT
or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling: run flow with synthetic volume in
dev environment, inject throttle error via mock connector, observe run history for 429
patterns, use Power Platform admin center to monitor request consumption during test. "Test
in staging" without a specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the flow architect's analysis is not evidence of
Round 2's connector-level precision. A thorough, coherent Round 1 output can still contain PA
construct names that are imprecise, rate units drawn from estimates rather than documentation,
or cascade labels that use directional language where numeric precision is required. Round 2
operates independently of Round 1's output quality.

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
   per-environment? PA limits vary by unit type — confirm the unit matches the construct's
   documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (names the exact
   signal path and load calculation) or qualitative ("will cause increased load")? Promote
   qualitative statements to structural ones using TABLE 9 arithmetic.

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

**Axis:** Output format — labeled prose paragraphs replace markdown tables for the primary
analysis sections (Phases 2 and 3). Phase 1 retains TABLE 1 (construct inventory requires
structured data). Phase 4 retains tables (precision audit, throttle budget, and remediations
are tabular by nature). Sections 2.A–2.C and 3.A–3.C use labeled paragraph blocks with
explicit field requirements stated in prose.

**Hypothesis:** Ceiling maintained (160/160). Output format controls how analysis is laid out
on the page. C-26 measures whether any content intervenes between `## ROUND 2` and the
pre-barrier section header — that relationship is format-independent. The pre-barrier container
header `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)` is a
structural heading, not a content block, and its adjacency to `## ROUND 2` is unaffected by
whether Phase 2 and Phase 3 use tables or prose. Expected: 160/160.

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
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic "API
limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list, (b) a
numeric limit with unit, (c) a request contribution estimate with arithmetic shown. Block:
PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing fields
receive a `?` flag — correct before proceeding.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write three prose paragraphs:

**Bottleneck paragraph:** Identify the primary bottleneck. Name the specific PA construct
component and construct type. State the rate at which it saturates under the scenario's
request volume. Explain in one sentence why this ordering holds at this aggregate volume. Name
the cascade chain or shared principal pool that makes limits non-independent.

**Hit order paragraph:** Describe the throttle tier sequence in explicit order — first, second,
and any subsequent. For each tier, name the construct, the limit, and why this construct
saturates before the next at the scenario's volume. An unordered enumeration of limits without
ordering rationale does not satisfy this section.

**Ordering validation paragraph:** State one sentence confirming that the bottleneck analysis
accounts for shared resource pools (e.g., tenant-level entitlement shared across flows) that
make per-construct limits interdependent at the scenario volume.

**Section 2.B — Backpressure Hop Chain**

Write the propagation trace as a labeled hop chain. Minimum: two hops.

**Hop 1:** `[From component]` emits `[signal type: error code / retry-after header / queue
depth increase / other]` signal `[exact signal value or code]`. `[To component]` receives the
signal and `[response behavior]`.

**Hop 2 (if applicable):** Continue from the last receiving component using the same format.

**Terminal state:** Name the terminal outcome — user-visible error, flow run failure, or
silent drop — and which component reaches it.

**Section 2.C — User Experience per Throttle Tier**

Write one labeled paragraph per UX tier. Minimum: two tiers with distinct UX categories.

**Tier [N] — [UX category]:** The user experiences `[specific observable state]` at this
throttle tier. The system action is `[internal behavior]`, which surfaces as `[what the user
sees or does not see]`. UX category: transparent-retry / visible-delay / error-surfaced /
silent-loss.

Rule: UX categories MUST differ across tiers. Each paragraph must state what the user sees —
not what the system does internally.

**GATE 2:** Section 2.B has >= 2 labeled hops with a named terminal state AND Section 2.C has
>= 2 tier paragraphs with distinct UX categories AND Section 2.A has a "why this order holds"
explanation for each tier. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

For each burst-exposed path found, write a labeled prose entry:

**Burst path [N]:** Flow construct `[name]` at `[location in flow]` uses PA construct type
`[type]`. Estimated peak request rate: `[N req/unit]`. This path bypasses or overwhelms the
tier-1 guard because `[mechanism — e.g., no concurrency cap on Apply to Each, unbounded
parallel branch fan-out]`.

Check all patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger without debounce, nested loops, batch-size
misconfigurations. If none found, write an explicit acknowledgment naming the guards currently
in place.

**Section 3.B — Retry-After Gaps**

For each gap found, write a labeled prose entry:

**Gap [N]:** Consumer construct `[name]` receives a 429 at `[location]`. Retry-After header:
`[read / not read]`. Actual backoff behavior: `[description]`. Failure mode: retry-storm /
fixed-misalign / silent-discard.

At least one gap required. If no gap exists, state why every consumer correctly honors
Retry-After and name the PA mechanism enforcing it.

**Section 3.C — Cascade Risk Pairs**

For each cascade pair found, write a labeled prose entry:

**Cascade [label]:** Tier A — `[construct]` throttled via `[mechanism]`. Load added to Tier B:
`[numeric or directional estimate]`. Tier B — `[construct]`. Failure mode: `[description]`.
Severity: critical / high / medium. Duration: `[estimated]`.

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them. A flat enumeration of independent throttle risks without cascade relationships
does not satisfy this section.

**GATE 3:** Section 3.C has >= 2 complete cascade pair entries (Tier A != Tier B, mechanism
stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. For each row:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

PA expert: either confirm the exact documented term or provide the corrected name. Generic
terms must be corrected here. "Confirmed" requires the exact PA documentation name — not
paraphrase.

**Section 4.B — UX Validation**

Review each tier paragraph from Section 2.C. Write one validation sentence per tier: confirm
or correct the UX category against PA runtime behavior. Internal system behavior (e.g., queue
depth increase, internal retry count) is not user experience. Correct any paragraph that
conflates system state with user-visible outcome.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations. "Add retries" and "reduce load" do not count. Each
remediation must map to a specific finding from PHASES 2–3 by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition each
signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State
the impact on this scenario's volume: does the entitlement change shift any TABLE 9 row?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling. "Test in staging" without a
specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 2's structural
precision. A thorough, coherent Round 1 output — whether expressed in prose or table form —
can still contain PA construct names that are imprecise, rate units drawn from estimates rather
than documentation, or cascade descriptions using directional language where numeric precision
is required. Round 2 operates independently of Round 1's output quality and format choices.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? Does it match the product-published limit source?

2. **Numeric limit precision:** Is the limit value the documented platform limit or a derived
   estimate? State the source (PA documentation, connector certification, admin center
   observed value, or estimate with confidence level).

3. **Rate unit precision:** Is the unit per-minute, per-second, per-24-hours, per-user, or
   per-environment? Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair entry in Section 3.C, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (exact signal path
   and load calculation) or qualitative? Promote qualitative statements using TABLE 9
   arithmetic.

2. **Load-added precision:** Is the load-added estimate numeric or directional? If
   directional, compute the numeric projection from TABLE 9 data.

Write the Round 2 precision output:

**TABLE 11 — Round 2 Precision Audit**

| Item (section + label) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Lifecycle Emphasis: Cascade Risk as Primary Analytical Emphasis

**Axis:** Lifecycle emphasis — Phase 3 (cascade and exposure analysis) is elevated to primary
analytical emphasis. Phase 2 (bottleneck and UX) is compressed to a mandatory minimum: a
single bottleneck statement, a two-tier hit-order entry, a one-sentence terminal propagation
path, and two named UX outcomes. Phase 3 expands to include a cascade priority ranking as a
required subsection. Advisory sections maintain standard depth.

**Hypothesis:** Ceiling maintained (160/160). Lifecycle emphasis controls the relative volume
of analysis in each phase, not the structural placement of the Round 2 pre-barrier container.
Expanding Phase 3 and compressing Phase 2 does not move where `## ROUND 2` appears or whether
the pre-barrier container is immediately adjacent. C-29 and C-30 evaluate only heading
adjacency and phrase content, both of which are phase-allocation-independent.
Expected: 160/160.

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
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic terms
do not pass.

**GATE 1:** All rows have (a) exact PA construct type, (b) numeric limit with unit, (c)
request contribution with arithmetic. Missing fields: `?` flag — fix before PHASE 2.

---

### PHASE 2 — Bottleneck Identification (Compressed)

*(GATE 1 must pass before this phase executes.)*

**Bottleneck statement (required):**

> "[Specific component] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] under this scenario because [reason]. Limits are non-independent because
> [one sentence on cascade chain or shared principal pool]."

**TABLE 2 — Hit Order (minimum two tiers)**

| Hit order | Construct | Limit | Why this order holds at scenario volume |
|-----------|-----------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

**Backpressure (minimum):** Name the terminal signal path from the bottleneck to the
user-facing outcome in one sentence: "[bottleneck construct] emits [signal type] → [next
component] → [terminal state: user-visible error / flow run failure / silent drop]."

**UX (minimum):** Name two throttle tiers with distinct UX categories
(transparent-retry / visible-delay / error-surfaced / silent-loss). One sentence each.

**GATE 2:** Bottleneck statement complete, TABLE 2 has >= 2 rows with "why this order holds,"
terminal propagation path stated, two UX outcomes with distinct categories named. Block:
PHASE 3 is blocked until GATE 2 passes.

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

For each consumer in TABLE 1, assess Retry-After handling.

**TABLE 4 — Retry-After Gaps**

| Consumer construct | 429 location | Header read? | Backoff behavior | Failure mode |
|-------------------|-------------|--------------|------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Register (Primary)**

For each cascade pair, provide the full causal chain: what state change at Tier A generates
what additional load at Tier B, with numeric estimate.

**TABLE 5 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle trigger | Load increase at Tier B | Tier B construct | Tier B limit | Headroom after load | Failure mode | Severity | Recovery window |
|---------------|-----------------|-----------------|------------------------|-----------------|-------------|---------------------|--------------|----------|----------------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, numeric Tier B load
estimate, and severity and recovery window assessed. Include at least one pair where Tier B
belongs to a different PA construct type than Tier A.

**Section 3.D — Cascade Priority Ranking**

Rank the TABLE 5 cascade pairs by severity × probability. Write one sentence per pair
justifying its rank.

**GATE 3:** TABLE 5 has >= 2 complete cascade pairs (all columns filled, Tier A != Tier B,
numeric load estimate, severity assessed). Section 3.D has a prioritized ranking with one
justification sentence per pair. Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

**TABLE 6 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

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

Name at least one PA-observable signal. State the condition it surfaces and when it would
trigger.

**Section 4.E — License and Entitlement Boundary**

Name at least one entitlement boundary that materially shifts a TABLE 7 status row.

**Section 4.F — Test Approach**

At least one concrete PA tooling test step targeting cascade behavior specifically (e.g.,
trigger the cascade via synthetic volume and observe Tier B status in flow run history).

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the cascade risk analysis is not evidence of Round 2's
structural precision. A thorough cascade analysis with well-prioritized severity rankings can
still contain PA construct names drawn from paraphrase rather than documentation, numeric load
estimates unsupported by TABLE 7 arithmetic, or recovery window claims without mechanism basis.
Round 2 operates independently of Round 1's analytical depth and cascade coverage.

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
   granularity (per-minute, per-24-hours, per-user, per-environment).

For each cascade pair in TABLE 5, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism structural (exact signal path and load
   calculation) or qualitative? Promote qualitative statements using TABLE 7 arithmetic.

2. **Load-added precision:** Is the Tier B load estimate numeric? If not, compute from
   TABLE 7.

3. **Recovery window precision:** Is the recovery window derived from a PA retry or queue
   mechanism, or estimated? State the basis.

Write the Round 2 precision output:

**TABLE 9 — Round 2 Precision Audit**

| Item (TABLE ref + label) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|--------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Combined: Phrasing Register (Conversational) + Inertia Framing

**Axis:** Phrasing register (conversational and descriptive — "your job is to," "consider how,"
"when you see") combined with inertia framing (each phase opens by describing the current-state
barrier — what is typically absent or broken — before stating the analytical task). The
phrasing shift applies throughout ROUND 1. The inertia preambles appear at the start of each
phase and each major section.

**Hypothesis:** Ceiling maintained (160/160). Conversational register affects sentence
structure and frame; inertia preambles add current-state context before analytical tasks.
Neither changes the structural placement of the Round 2 pre-barrier container (C-26) or the
content of the boundary-event phrase (C-27). The `## ROUND 2` heading and its immediately
adjacent `### PRE-EVALUATION ASSERTIONS` container are structural markers immune to register
or framing decisions made within ROUND 1. Expected: 160/160.

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

**Domain rule:** When you name a PA construct type, use the exact documented term —
Power Platform request entitlements, connector throttling policies, flow run concurrency
limits, action call limits, premium vs. standard connector tiers, or Microsoft 365 service
protection limits. Generic terms like "API limit" or "service limit" are insufficient.

**GATE 1:** Every TABLE 1 row must have (a) an exact PA construct type, (b) a numeric limit
with unit, and (c) a request contribution estimate with arithmetic. Rows missing any field
get a `?` flag — resolve before proceeding to PHASE 2.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Current-state barrier:** Most PA flows hit throttle limits without anyone identifying the
binding constraint or understanding why it saturates first. When 429s appear, the first guess
is usually wrong because limits share principal pools or accumulate across nested constructs.

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

**Current-state barrier:** When a 429 is issued, the signal rarely travels cleanly to the
surface. Intermediate constructs absorb, drop, or transform it — which is why the user
experience often doesn't match what the logs show.

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state.

**Section 2.C — User Experience per Throttle Tier**

**Current-state barrier:** The internal system response to throttling (queue depth increase,
retry count decrement) is not what the user sees. These are frequently conflated, producing
UX claims that don't match PA runtime behavior.

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. UX
categories must differ across tiers. Each row must state what the user sees — not what the
system does internally.

**GATE 2:** TABLE 3 has >= 2 hops with named terminal state AND TABLE 4 has >= 2 tiers with
distinct UX categories AND TABLE 2 has "why this order holds" for each row. Block: PHASE 3 is
blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Current-state barrier:** PA flows routinely include constructs that generate burst loads
with no guard — uncapped Apply to Each loops, unbounded parallel branches. These are
treated as default behavior until they cause an outage.

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

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (Tier A != Tier B, mechanism stated,
severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Consider each entry in TABLE 1. When you confirm a construct name, you're asserting it matches
the exact term in PA documentation. When you correct it, explain why the original was a
paraphrase or category name.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

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

Minimum: two PA-native remediations, each mapped to a specific finding.

**Section 4.E — Monitoring Signals**

What PA-observable signal would surface the throttle condition before it becomes a
user-visible failure? Name the signal and the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

Consider how the entitlement tier changes what limits apply. Name one boundary that
materially shifts a TABLE 9 status row.

**Section 4.G — Test Approach**

How would you validate this throttle analysis before production? Describe at least one
concrete step using PA tooling that specifically exercises the cascade or burst path findings.

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

2. **Numeric limit precision:** Is the limit value the documented platform limit or a derived
   estimate? State the source.

3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement
   granularity (per-minute, per-24-hours, per-user, per-environment).

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism structural (exact signal path and load
   calculation) or qualitative? Promote qualitative statements using TABLE 9 arithmetic.

2. **Load-added precision:** Is the Tier B load estimate numeric or directional? If
   directional, compute the projection from TABLE 9 data.

Write the Round 2 precision output:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — Combined: Role Sequence (Throughput Analyst) + Output Format (Numbered Lists)

**Axis:** Role sequence — a single "PA throughput analyst" role replaces the domain expert
framing throughout; there is no role switch at Round 2. Output format — numbered and bulleted
lists replace markdown tables for Phase 2 and Phase 3 analysis sections (Phases 1 and 4 retain
tables for structured data collection).

**Hypothesis:** Ceiling maintained (160/160). The analyst role and list format do not affect
the `## ROUND 2` heading or the immediately adjacent `### PRE-EVALUATION ASSERTIONS (before
any Round 2 construct evaluation begins)` container. Neither the role label nor the formatting
choice inside ROUND 1 creates or removes any content between the heading and its first
structural child. Expected: 160/160.

---

You are a PA throughput analyst. You trace rate-limited Power Automate flows from first
throttle hit through cascade failure, producing a structured analysis that a PA administrator
can act on immediately.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? |
|-----------|------------------|---------------|----------------------------------------|-------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | yes / no / N/A |

PA construct types must be exact documented terms: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs.
standard connector tiers, Microsoft 365 service protection limits.

**GATE 1:** All rows have (a) exact PA construct type, (b) numeric limit with unit, (c)
request contribution with arithmetic. Missing fields: `?` flag — fix before continuing.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass.)*

**Section 2.A — Rate Limit Hit Ordering**

1. **Bottleneck statement:**
   - Component: `[specific PA construct component]`
   - Construct type: `[exact PA term]`
   - Saturation point: `[N req/unit-time]`
   - Why this order holds: `[reason at this aggregate volume]`
   - Why limits are non-independent: `[cascade chain or shared principal pool, one sentence]`

2. **Hit order (minimum two tiers):**
   - Hit 1: `[construct]` at `[limit]` — why it saturates first: `[reason]`
   - Hit 2: `[construct]` at `[limit]` — why it saturates second: `[reason]`

**Section 2.B — Backpressure Hop Chain**

Trace from first throttled component to terminal state. Minimum: two hops.

1. **Hop 1:** `[From component]` → emits `[signal type: error code / retry-after header /
   queue depth increase / other]` → `[To component]` responds with `[behavior]`.
2. **Hop 2:** `[From component]` → emits `[signal]` → `[To component]` responds with
   `[behavior]`.
- **Terminal state:** `[user-visible error / flow run failure / silent drop]` at
  `[component]`.

**Section 2.C — User Experience per Throttle Tier**

Minimum: two tiers with distinct UX categories (transparent-retry / visible-delay /
error-surfaced / silent-loss).

- **Tier 1 — [UX category]:** User sees: `[observable state]`. System does: `[internal
  action]`. Category: `[UX category]`.
- **Tier 2 — [UX category]:** User sees: `[observable state]`. System does: `[internal
  action]`. Category: `[UX category]`.

Rule: UX categories must differ across tiers.

**GATE 2:** Section 2.B has >= 2 hops with named terminal state AND Section 2.C has >= 2
tiers with distinct UX categories AND Section 2.A has "why it saturates" for each hit-order
entry. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass.)*

**Section 3.A — Unprotected Burst Paths**

For each burst-exposed path:

- **Burst path [N]:**
  - Construct: `[flow construct name]`
  - PA type: `[exact PA construct type]`
  - Location: `[position in flow]`
  - Peak rate: `[N req/unit]`
  - Guard: NONE / `[existing guard]`
  - Bypass mechanism: `[why it bypasses or overwhelms tier-1]`

Check: Apply to Each loop (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch-size misconfigurations.

**Section 3.B — Retry-After Gaps**

For each gap:

- **Gap [N]:**
  - Consumer: `[construct]`
  - 429 location: `[where in the flow]`
  - Retry-After read: yes / no
  - Backoff: `[fixed interval / exponential / other]`
  - Failure mode: retry-storm / fixed-misalign / silent-discard

At least one gap required.

**Section 3.C — Cascade Risk Pairs**

For each cascade pair:

- **Cascade [label]:**
  - Tier A: `[construct]` throttled via `[mechanism]`
  - Load added to Tier B: `[numeric or directional estimate]`
  - Tier B: `[construct]`
  - Failure mode: `[description]`
  - Severity: critical / high / medium
  - Duration: `[estimated]`

Minimum: two pairs with distinct Tier A / Tier B constructs.

**GATE 3:** Section 3.C has >= 2 complete cascade pairs (Tier A != Tier B, mechanism stated,
severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1.

**TABLE 2 — PA Construct Precision Pass**

| Construct | PA construct (confirmed / corrected) | Correction reason | Precision note |
|-----------|-------------------------------------|------------------|----------------|

**Section 4.B — UX Validation**

For each tier entry in Section 2.C, write one validation sentence: confirm the UX category
matches PA runtime behavior, or correct it with the accurate category.

**Section 4.C — Quantified Risk Register**

**TABLE 3 — Throttle Budget**

| Construct | Limit | Projected volume | Status | Headroom / Deficit |
|-----------|-------|-----------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

**TABLE 4 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations, each mapped to a specific finding from PHASES 2–3.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal and the condition it surfaces.

**Section 4.F — License and Entitlement Boundary**

Name one entitlement boundary that materially shifts a TABLE 3 status row.

**Section 4.G — Test Approach**

At least one concrete PA tooling test step. "Test in staging" without a specific method does
not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the throughput analysis is not evidence of Round 2's
structural precision. A complete Round 1 output — with numbered hop chains, bulleted cascade
pairs, and fully populated burst path lists — can still contain PA construct names drawn from
paraphrase rather than documentation, limit values derived from estimates rather than
platform-published sources, or cascade load estimates that are directional where numeric
verification is required. Round 2 operates independently of Round 1's list completeness and
structural coverage.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 2 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 2 corrections
were finalized.

---

For each row in TABLE 2, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term in Power
   Automate documentation? Match against the product-published limit source.

2. **Numeric limit precision:** Is the limit documented or estimated? State the source (PA
   documentation, connector certification, admin center observed value, or estimate with
   confidence level).

3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair entry in Section 3.C, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism structural (exact signal path and load
   calculation) or qualitative? Promote qualitative statements using TABLE 3 arithmetic.

2. **Load-added precision:** Is the Tier B load estimate numeric? If directional, compute
   the projection from TABLE 3 data.

Write the Round 2 precision output:

**TABLE 5 — Round 2 Precision Audit**

| Item (section + label) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*
