# flow-throttle — Round 10 Variations (v10 Rubric, 166-point max)

## Variation Axes and Hypotheses

R9 confirmed that all five content axes are structurally inert for C-29 and C-30 (the
compound intersection criteria). Under v10, two new criteria are formalized from the R9
ceiling pattern:

**C-31** (3 pts): The named portion of the pre-barrier container header (outside the
boundary-event parenthetical) contains a mechanism-type term declaring assertive content
("ASSERTIONS," "DECLARATIONS," "PRECONDITIONS," "PREREQUISITES"). Requires C-21.

**C-32** (3 pts): The barrier heading carries both (a) a round/barrier ordinal AND
(b) a dash-separated evaluation-type subtitle naming the analysis class. Independent of
all container-layer criteria.

**R10 design goal:** Confirm that the five content axes — role sequence, output format,
lifecycle emphasis, phrasing register, inertia framing — are structurally inert for C-31
and C-32. This mirrors the R6 inertness finding for C-25/C-26 and the R9 inertness
finding for C-29/C-30.

Three single-axis tests (V-01, V-02, V-03), then two combination tests (V-04, V-05):

| Variation | Axis | C-31 | C-32 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Role sequence: Throughput Modeler (R1) + Platform Limits Auditor (R2) | PASS | PASS | 166/166 |
| V-02 | Output format: numbered findings blocks (no tables in Phases 2–3) | PASS | PASS | 166/166 |
| V-03 | Lifecycle emphasis: cascade-first (Phase 2 leads with cascade topology) | PASS | PASS | 166/166 |
| V-04 | Phrasing register (terse imperative) + inertia framing (Phase 0 baseline) | PASS | PASS | 166/166 |
| V-05 | Role sequence (single PA performance engineer) + output format (risk-scored findings) | PASS | PASS | 166/166 |

All five predicted at 166/166. Expected confirmation: (1) C-31 is content-axis-inert —
the ASSERTIONS mechanism-type term survives role changes, format changes, phase
reordering, phrasing shifts, and inertia framing additions. (2) C-32 is content-axis-inert
— a barrier heading with a dash-separated evaluation-type subtitle remains structurally
stable regardless of the content variation in phases below it.

---

## V-01 — Role Sequence: Throughput Modeler (R1) + Platform Limits Auditor (R2)

**Axis:** Role sequence — Round 1 is owned by a PA throughput modeler who constructs the
quantitative request-volume-vs-tier model. Round 2 is owned by a platform limits auditor
who verifies every numeric limit against Microsoft-published documentation. The role switch
occurs at the Round 2 barrier. This differs from R9-V01's (PA flow architect + connector
support engineer) by shifting Round 1's emphasis from topology mapping to quantitative
model construction, and Round 2's emphasis from construct-name precision to documentation-
source verification. The Round 2 subtitle is updated to "Platform Limits Audit" to name the
auditor's analysis class.

**Hypothesis:** Ceiling maintained (166/166). Role assignments affect expertise framing and
persona labels. C-31 evaluates whether the container header contains a mechanism-type term
("ASSERTIONS") — the term is in the header's named portion regardless of which expert persona
is declared. C-32 evaluates whether the barrier heading carries a dash-separated evaluation-
type subtitle — "Platform Limits Audit" names the analysis class as required; the subtitle
text content is not constrained beyond naming an analysis class. Expected: 166/166.

---

You are a Power Automate throughput modeler simulating request volume against rate limit
tiers. For Round 2, you will operate as a platform limits auditor to verify every numeric
limit against Microsoft-published documentation.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throughput Model and Tier Impact Analysis

*Role: PA throughput modeler.*

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

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing
fields receive a `?` flag — correct before proceeding.

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
misconfigurations. If none found, write explicit acknowledgment with guards currently in
place.

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

### PHASE 4 — Synthesis and Construct Staging for Round 2

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — Construct Model Confidence**

Review every construct in TABLE 1. For each row produce TABLE 8:

**TABLE 8 — Construct Staging**

| Construct (from TABLE 1) | PA construct (confirmed / flagged) | Flag reason | Model confidence |
|--------------------------|-----------------------------------|-------------|-----------------|

Confidence levels: HIGH (limit sourced from Microsoft documentation), MEDIUM (limit from
community source or observed admin center value), LOW (estimated from runtime behavior).
Flag any MEDIUM or LOW confidence row for Round 2 audit. "Confirmed" requires the exact PA
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
or headroom]." A qualitative "this will hit the limit" without numeric projection does not
pass.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs (e.g., concurrency control settings,
flow run queuing, Delay action with Retry-After value, request batching via Data Operations,
premium connector entitlement upgrade). "Add retries" and "reduce load" do not count. Each
remediation must map to a specific finding from PHASES 2–3 by section label.

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

## ROUND 2 — Platform Limits Audit

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's model confidence ratings (HIGH / MEDIUM / LOW in TABLE 8) are
not evidence of documentation accuracy. A HIGH-confidence rating assigned by the throughput
modeler reflects the model's internal arithmetic consistency — it does not confirm that the
numeric limit matches the Microsoft-published documented value for the scenario's license
tier. Round 2 operates independently of Round 1's confidence assignments.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically constructs flagged in TABLE 8 (Section 4.A) where the throughput model
assigned MEDIUM or LOW confidence — are now in scope for Round 2 documentation verification.
These were excluded from Round 1's evaluation window because Round 1 closed before platform
documentation lookup was performed.

---

*Role: Platform limits auditor.*

For each row in TABLE 8, apply documentation-source verification:

1. **Documentation source:** Is the numeric limit sourced from Microsoft Power Platform
   documentation, connector certification pages, or admin center observed values? State the
   specific source for each row. "Generally known limit" and "standard PA limit" do not pass.

2. **License-tier match:** PA limits vary by licensing tier. Confirm the limit applies to the
   scenario's tier (per-user plan / per-flow plan / Office 365 included / premium). A limit
   from a mismatched tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Confirm the unit (per-minute / per-second / per-24-hours / per-user /
   per-environment) matches the construct's documented enforcement granularity. A correct
   number with wrong units is a documentation error.

For each cascade pair in TABLE 7, apply precision checks:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or
   inferred behavior? Inferred cascade mechanisms require explicit flagging and a verification
   path.

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential between Tier A and Tier B? A "HIGH" severity on a cascade where Tier B has
   10x the headroom requires justification.

Write the Round 2 audit output:

**TABLE 11 — Round 2 Platform Limits Audit**

| Item (TABLE ref + row) | Documentation source | Source-match finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|----------------------------------------------------------|---------------------|

---

*End of V-01 prompt body.*

---

## V-02 — Output Format: Numbered Findings Blocks (no tables in Phases 2–3)

**Axis:** Output format — Phases 2 and 3 switch from markdown tables to numbered findings
blocks with inline field requirements. Phase 1 retains TABLE 1 (construct inventory is
inherently tabular). Phase 4 retains TABLE 8, TABLE 9, TABLE 10 (precision artifacts and
quantified risk require column alignment). Round 2 retains TABLE 11 (audit output). In
Phases 2 and 3, each finding is a numbered labeled entry with required fields stated inline;
no markdown table columns are used.

**Hypothesis:** Ceiling maintained (166/166). Output format governs how analysis content
is presented on the page. C-31 evaluates the mechanism-type term ("ASSERTIONS") in the
container header's named portion — the header text is independent of whether Phase 2 and
Phase 3 used tables or numbered blocks. C-32 evaluates the barrier heading subtitle
("Structural Precision Pass") — the subtitle appears in the `## ROUND 2` heading, above
all Phase content; its presence is unaffected by format choices in the phases below.
Expected: 166/166.

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

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type, (b) a numeric limit with
unit, (c) a request contribution estimate with arithmetic shown. Block: PHASE 2 is blocked
until every row satisfies all three conditions. Rows with missing fields receive a `?` flag.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason]. The naive
> assumption that limits are independent fails here because [cascade chain or shared pool]."

For each throttle tier that saturates after the bottleneck, write a numbered entry:

**Hit [N]:** Construct `[name]` (PA type: `[exact term]`) saturates at `[limit]`. This
construct saturates after the bottleneck at this volume because `[ordering rationale]`.

Minimum: two numbered entries (bottleneck statement + at least one subsequent tier).

**Section 2.B — Backpressure Hop Chain**

For each propagation hop, write a numbered entry:

**Hop [N]:** `[From component]` emits a `[signal type: error code / retry-after header /
queue depth increase / other]` signal (`[exact value or code]`). `[To component]` receives
the signal and `[response behavior: retries / queues / fails / drops]`.

Minimum: two hops. End the chain with a terminal state entry:

**Terminal:** `[Component]` reaches terminal state — `[user-visible error / flow run failure /
silent drop]` — because `[mechanism]`.

**Section 2.C — User Experience per Throttle Tier**

For each UX tier, write a numbered entry:

**Tier [N] — [UX category]:** The user experiences `[specific observable state]`. System
action: `[internal behavior]`. User-visible outcome: `[what the user sees or fails to see]`.
UX category: transparent-retry / visible-delay / error-surfaced / silent-loss.

Rule: UX categories MUST differ across tiers. Each entry must state the user-visible outcome
— not only the internal system action.

**GATE 2:** Section 2.B has >= 2 hop entries with a terminal state entry AND Section 2.C has
>= 2 tier entries with distinct UX categories AND Section 2.A has at least a bottleneck
statement plus one subsequent tier. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

For each burst-exposed path, write a numbered entry:

**Burst path [N]:** Flow construct `[name]` at `[location in flow]` (PA type: `[exact term]`).
Estimated peak request rate: `[N req/unit]`. Bypass mechanism: `[why it overwhelms or
bypasses the tier-1 guard — e.g., no concurrency cap, unbounded fan-out, no debounce]`.

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If no burst paths found, write an explicit acknowledgment naming the
guards currently in place.

**Section 3.B — Retry-After Gaps**

For each gap, write a numbered entry:

**Gap [N]:** Consumer construct `[name]` receives a 429 at `[location]`. Retry-After header
read: `[yes / no]`. Actual backoff behavior: `[description]`. Failure mode: retry-storm /
fixed-misalign / silent-discard.

At least one gap required. If no gap exists, state why every consumer correctly honors
Retry-After and name the PA mechanism enforcing compliant backoff.

**Section 3.C — Cascade Risk Pairs**

For each cascade pair, write a numbered entry:

**Cascade [label]:** Tier A — construct `[name]` throttled via `[mechanism]`. Load added to
Tier B: `[numeric or directional estimate]`. Tier B — construct `[name]`. Failure mode:
`[description]`. Severity: critical / high / medium. Duration: `[estimate]`.

Minimum: two cascade pair entries with distinct Tier A / Tier B constructs and the mechanism
linking them.

**GATE 3:** Section 3.C has >= 2 cascade pair entries (Tier A != Tier B, mechanism stated,
severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

"Confirmed" requires the exact PA documentation name — not paraphrase. Generic terms must
be corrected here.

**Section 4.B — UX Validation**

For each tier entry in Section 2.C, write one validation sentence: confirm or correct the
UX category against PA runtime behavior. Internal system behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings from Phases 2–3.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with the condition it surfaces and its trigger.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material throttle impact on this scenario.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's confidence in the analysis is not evidence of Round 2's
structural precision. A thorough Round 1 output — whether expressed as numbered findings
blocks or as tables — can still contain PA construct names that are imprecise, rate units
drawn from estimates rather than documentation, or cascade descriptions using directional
language where numeric precision is required. Round 2 operates independently of Round 1's
output quality and format choices.

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

3. **Rate unit precision:** Confirm the unit (per-minute / per-second / per-24-hours /
   per-user / per-environment) matches the construct's documented enforcement granularity.

For each cascade pair entry in Section 3.C, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (exact signal path
   and load calculation) or qualitative? Promote qualitative statements using TABLE 9
   arithmetic.

2. **Load-added precision:** Is the load estimate numeric or directional? If directional,
   compute a numeric projection from TABLE 9 data.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref or Section 3.C entry) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|---------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Lifecycle Emphasis: Cascade-First (Phase 2 leads with cascade topology)

**Axis:** Lifecycle emphasis — the ordering of Phase 2's sub-sections is inverted to
cascade-first. Standard ordering presents bottleneck identification first, then backpressure
propagation, then UX. V-03 presents cascade topology first (the structural dependency graph
between throttle tiers), then derives the binding bottleneck from the cascade model as the
tier that initiates the dominant cascade, then traces UX impact as the downstream consequence
of cascade propagation. Phase 3 reorganizes burst paths and retry-after gaps as named failure
modes within the cascade framework rather than independent exposure categories. More analysis
space is allocated to cascade relationship structure; the bottleneck statement is a derived
conclusion ("The binding tier is the cascade initiator at this volume") rather than the
opening frame.

**Hypothesis:** Ceiling maintained (166/166). Phase ordering is a lifecycle emphasis choice
that affects which findings appear first within Round 1. The Round 2 barrier — `## ROUND 2`
heading immediately followed by `### PRE-EVALUATION ASSERTIONS (before any Round 2 construct
evaluation begins)` — occurs after all phases, at the Round 1 / Round 2 boundary. C-31
(mechanism-type "ASSERTIONS" in container header) and C-32 (evaluation-type subtitle in
barrier heading) both evaluate the barrier/container pair, not the ordering of phases within
Round 1. Phase reordering is content-inert for the structural boundary. Expected: 166/166.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system. This simulation uses a cascade-first analysis approach:
cascade topology is established before bottleneck identification; the binding bottleneck is
derived as the tier that initiates the dominant cascade chain at the scenario's volume.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Cascade Topology Mapping and Throttle Impact Analysis

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic "API
limit" or "service limit" does not pass.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type, (b) a numeric limit with
unit, (c) a request contribution estimate with arithmetic shown. Block: PHASE 2 is blocked
until every row satisfies all three conditions.

---

### PHASE 2 — Cascade Topology, Bottleneck Derivation, and UX Impact

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Cascade Topology**

Map the structural dependency graph between throttle tiers. Fill TABLE 2:

**TABLE 2 — Cascade Dependency Graph**

| Source tier | Construct (from TABLE 1) | Dependency type | Target tier | Construct (from TABLE 1) | Coupling mechanism |
|-------------|--------------------------|----------------|-------------|--------------------------|-------------------|

Dependency types: shared-principal-pool / backpressure-amplification / retry-load-transfer /
entitlement-shared. Coupling mechanism: name the PA resource that links source and target
(e.g., "tenant-level Power Platform request entitlement pool," "connector call shared per
flow owner principal").

Minimum: two dependency edges. An enumeration of tiers without dependency relationships does
not satisfy this section.

**Section 2.B — Bottleneck Derivation**

Using the cascade topology from Section 2.A, derive the binding bottleneck:

> "The binding bottleneck is [specific PA construct component] at [PA construct type]. It is
> the cascade initiator at this scenario volume because [it is the first tier in the dominant
> cascade chain to saturate — state why it reaches its limit before downstream tiers at the
> aggregate volume]. Downstream tiers [name them] are load-amplified by this tier's saturation
> via [coupling mechanism from TABLE 2]."

**TABLE 3 — Throttle Hit Order (derived from cascade model)**

| Hit order | Construct | Limit | Cascade role (initiator / amplified / terminal) | Why this order holds |
|-----------|-----------|-------|------------------------------------------------|---------------------|

**Section 2.C — UX Impact as Cascade Downstream**

For each cascade propagation path in TABLE 2, trace the user-visible outcome at the terminal
node. Fill TABLE 4:

**TABLE 4 — UX Impact Map**

| Cascade path (source → target) | Terminal component | System action (internal) | User-visible experience | UX category |
|-------------------------------|-------------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Rule: UX categories MUST differ across paths. Each row states what the user sees — not what
the system does internally.

**GATE 2:** TABLE 2 has >= 2 dependency edges (dependency type + coupling mechanism filled)
AND TABLE 3 has >= 2 rows (cascade role assigned) AND TABLE 4 has >= 2 paths with distinct
UX categories. Block: PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Cascade Failure Mode Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Burst-Triggered Cascade Initiation**

Identify flow constructs that can initiate cascade through unprotected bursts. For each:

**TABLE 5 — Burst-Triggered Cascade Initiators**

| Flow construct | PA construct type | Location | Estimated peak burst rate | Cascade path triggered (from TABLE 2) | Guard missing |
|----------------|------------------|----------|--------------------------|--------------------------------------|---------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops. If no burst
initiators found, write explicit acknowledgment with guards currently in place.

**Section 3.B — Retry-After Failures as Cascade Amplifiers**

Identify consumer constructs that amplify cascade load by failing to honor Retry-After:

**TABLE 6 — Retry-After Cascade Amplifiers**

| Consumer construct | 429 source tier | Retry-After read? | Amplification behavior | Load increase on source tier | Failure mode |
|-------------------|----------------|------------------|------------------------|------------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one entry required.
If no retry-after failures exist, state why every consumer honors Retry-After and name the
PA mechanism enforcing compliant backoff.

**Section 3.C — Cascade Risk Summary**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, mechanism stated,
severity assessed. Each entry must link to a dependency edge in TABLE 2.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (Tier A != Tier B, mechanism stated,
severity assessed, TABLE 2 link present). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

**Section 4.B — UX Validation**

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior. Internal
system behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific cascade risk findings from Phase 3.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition and trigger.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material cascade impact on this scenario.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step targeting cascade behavior.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's cascade topology model is not evidence of Round 2's construct
precision. A coherent cascade model with well-formed dependency edges can still contain PA
construct names that are imprecise, rate units drawn from estimates, or cascade mechanisms
described at a directional level where numeric precision is required. Round 2 operates
independently of Round 1's cascade model quality.

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
   granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (exact signal path
   and load calculation) or qualitative? Promote qualitative statements using TABLE 9
   arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a directional
   statement? If directional, compute the numeric projection from TABLE 9 data.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Phrasing Register (Terse Imperative) + Inertia Framing (Phase 0 Baseline)

**Axes:** (1) Phrasing register — all instructions use terse imperative sentences. No
explanatory padding before directives. No "ensure that," "you should," or "consider." Each
phase opens with a directive; gate conditions are stated as blocking rules without
elaboration. (2) Inertia framing — a Phase 0 (Inertia Baseline) precedes the construct
inventory. Phase 0 establishes what the system does today under load without throttle-aware
mitigations. All subsequent phase analysis is anchored to deviation from this baseline. The
status quo is the primary reference frame: throttle findings are findings relative to what
the inertia state would have done.

**Hypothesis:** Ceiling maintained (166/166). Phrasing register affects sentence-level
vocabulary. Inertia framing adds a Phase 0 block inside Round 1. Neither change touches the
Round 2 barrier: C-31 evaluates the container header mechanism-type term; C-32 evaluates the
barrier heading subtitle. Both structural elements sit at the Round 1 / Round 2 boundary,
unaffected by a Phase 0 addition inside Round 1 or by terse vs. explanatory prose in the
phases below. Expected: 166/166.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Start from the inertia baseline — what the system does
today without throttle awareness — then identify where that baseline fails.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Inertia Baseline

*State what the system does today. No mitigations assumed.*

**Current state:** Describe the flow's current behavior at the scenario's request volume
under default PA settings. Name the constructs involved, the volume they carry, and the
absence of explicit throttle handling. This is the status quo competitor — the state a team
accepts when it does nothing.

**Baseline failure point:** Identify where the inertia state first breaks. Name the
construct, the limit it hits, and the user-visible consequence when no mitigation is present.

**Why inertia persists:** State the structural reason teams leave this state unaddressed
(e.g., throttle failures appear as transient errors, retry logic is implicit in the
connector, monitoring gaps mask 429 patterns). This is the primary obstacle to change.

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Map every throttle-relevant construct. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types from: Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. "API limit" fails. Use the exact
PA documentation term.

**GATE 1:** Every row: (a) exact PA construct type, (b) numeric limit with unit, (c)
arithmetic request contribution. Block: PHASE 2 blocked until all rows pass. Flag `?`.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[PA construct component] at [PA construct type] binds at [N req/unit-time] because
> [ordering rationale at aggregate volume]. Limits are not independent: [cascade chain or
> shared principal pool]."

Fill TABLE 2:

**TABLE 2 — Hit Order**

| Hit order | Construct | Limit | Why this order holds |
|-----------|-----------|-------|---------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

*Anchor to baseline: how does the inertia state reach this bottleneck? Reference Phase 0.*

**Section 2.B — Backpressure Hop Chain**

Fill TABLE 3:

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum: two
hops. End at terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

Fill TABLE 4:

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories
must differ across tiers. State user-visible outcome — not internal system action.

*Anchor to baseline: which UX outcome does the inertia state deliver? Mark that row.*

**GATE 2:** TABLE 3 >= 2 hops AND TABLE 4 >= 2 tiers with distinct UX categories AND TABLE 2
ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass.)*

**Section 3.A — Unprotected Burst Paths**

Fill TABLE 5:

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location | Estimated peak rate | Bypass mechanism |
|----------------|------------------|----------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out), high-
frequency trigger (no debounce), nested loops, batch-size misconfigurations. If none: name
guards in place.

*Anchor to baseline: are these burst paths present in the inertia state?*

**Section 3.B — Retry-After Gap Table**

Fill TABLE 6:

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After read? | Backoff behavior | Failure mode |
|-------------------|-------------|------------------|-----------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap. If none:
state why every consumer honors Retry-After.

**Section 3.C — Cascade Risk Pairs**

Fill TABLE 7:

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two pairs. Tier A != Tier B. Mechanism stated. Severity assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass.)*

**Section 4.A — PA Construct Validation**

Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confirm exact documented term or correct. "Confirmed" = exact PA documentation name.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
behavior is not user experience.

**Section 4.C — Quantified Risk Register**

Fill TABLE 9:

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Arithmetic for at least one row.

*Anchor to baseline: which TABLE 9 rows are OVER-LIMIT in the inertia state?*

**Section 4.D — PA-Specific Remediations**

Fill TABLE 10:

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Two PA-native remediations minimum. Map each to a Phase 2–3 finding. "Add retries" fails.

**Section 4.E — Monitoring Signals**

Name one PA-observable signal. State condition and trigger.

**Section 4.F — License and Entitlement Boundary**

Name one entitlement boundary with material limit impact. State TABLE 9 shift if any.

**Section 4.G — Test Approach**

One concrete PA tooling test step. "Test in staging" without a specific method fails.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's inertia baseline and scenario analysis are not evidence of
Round 2's construct precision. A thorough Phase 0 baseline and well-grounded cascade model
can still contain PA construct names that are imprecise, rate units from estimates rather
than documentation, or cascade mechanisms stated at directional rather than numeric precision.
Round 2 operates independently of Round 1's inertia framing and analysis quality.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

For each TABLE 8 row, apply precision checks:

1. **PA construct name precision:** Exact PA documentation term?

2. **Numeric limit precision:** Documented platform limit or derived estimate? State source.

3. **Rate unit precision:** Unit matches documented enforcement granularity?

For each TABLE 7 cascade pair, apply precision checks:

1. **Causal mechanism precision:** Structural (exact signal path + load calculation) or
   qualitative? Promote qualitative using TABLE 9 arithmetic.

2. **Load-added precision:** Numeric or directional? Compute numeric from TABLE 9 if
   directional.

Fill TABLE 11:

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — Role Sequence (Single PA Performance Engineer) + Output Format (Risk-Scored Findings)

**Axes:** (1) Role sequence — a single PA performance engineer role persists across both
rounds. There is no persona switch at the Round 2 barrier. The barrier separates Round 1
(throughput simulation) from Round 2 (precision verification) by mandate, not by evaluator
persona. The pre-barrier assertions explicitly address the single-role continuation: the
engineer's Round 1 simulation confidence is not carried into Round 2's precision mandate.
(2) Output format — each Phase 3 finding in TABLE 5, TABLE 6, and TABLE 7 carries an
inline risk score (1 = negligible to 5 = critical) with a one-sentence rationale. TABLE 3
and TABLE 7 gain a Risk column. TABLE 11 gains a "Score revision" column reflecting whether
Round 2 precision corrections change any risk score.

**Hypothesis:** Ceiling maintained (166/166). The absence of a persona switch at the Round 2
barrier is a role sequence choice — the barrier heading and pre-barrier container exist
structurally regardless of whether the same or a different persona crosses them. C-31
evaluates "ASSERTIONS" in the container header — the header text is independent of whether
one or two personas are declared. C-32 evaluates the evaluation-type subtitle in the barrier
heading — the subtitle names the Round 2 analysis class regardless of who performs it.
Adding a Risk column to tables is a format choice that adds columns but not headings between
`## ROUND 2` and `### PRE-EVALUATION ASSERTIONS`. Expected: 166/166.

---

You are a PA performance engineer simulating throughput across a rate-limited Power Automate
system and then verifying construct precision. You hold this role through both rounds. The
Round 2 barrier changes your mandate — from simulation to precision verification — but not
your identity.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: PA performance engineer (simulation mandate).*

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types from: Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. Use exact PA documentation terms.

**GATE 1:** Every row: (a) exact PA construct type, (b) numeric limit with unit,
(c) arithmetic request contribution. Block: PHASE 2 blocked until all rows pass.

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

| From component | Signal emitted | Signal type | To component | Response behavior | Risk (1–5) | Risk rationale |
|----------------|---------------|-------------|--------------|-------------------|-----------|----------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state. Risk score 1 = negligible, 5 = critical. One sentence
rationale per row.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories
MUST differ across tiers.

**GATE 2:** TABLE 3 >= 2 hops AND TABLE 4 >= 2 tiers with distinct UX categories AND
TABLE 2 ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location | Estimated peak rate | Bypass mechanism | Risk (1–5) | Risk rationale |
|----------------|------------------|----------|--------------------|--------------------|-----------|----------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch misconfigurations. If none found,
write explicit acknowledgment with guards in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After read? | Backoff behavior | Failure mode | Risk (1–5) | Risk rationale |
|-------------------|-------------|------------------|-----------------|-------------|-----------|----------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration | Risk (1–5) | Risk rationale |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|-----------|----------------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, mechanism stated,
severity assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific Phase 2–3 findings.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition and trigger.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material throttle impact.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** The absence of a role change at the Round 2 boundary is not evidence
that Round 2 evaluates the same claims as Round 1. Continuity of persona does not imply
continuity of evaluation mandate. The simulation mandate that governed Round 1 — modeling
request volume against tier limits — is suspended at this boundary. Round 2 operates under
a precision mandate: every construct name, numeric limit, and rate unit is evaluated against
documented sources. Round 1's throughput model, however coherent, is not evidence of
documentation accuracy. Round 2 findings supersede Round 1's claims wherever they conflict.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

*Role: PA performance engineer (precision mandate).*

For each row in TABLE 8, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation?

2. **Numeric limit precision:** Documented platform limit or derived estimate? State source.

3. **Rate unit precision:** Confirm the unit matches the construct's documented enforcement
   granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural (exact signal path and load calculation) or
   qualitative? Promote qualitative statements using TABLE 9 arithmetic.

2. **Load-added precision:** Numeric or directional? If directional, compute numeric from
   TABLE 9.

3. **Risk score revision:** Does the precision correction change the risk score from TABLE 7?
   If corrected limit is higher than modeled (more headroom), score may decrease. If lower
   (less headroom), score may increase. State rationale.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed | Score revision (TABLE 7 Risk col) |
|------------------------|------------------------|------------------------------------------|---------------------|----------------------------------|

---

*End of V-05 prompt body.*
