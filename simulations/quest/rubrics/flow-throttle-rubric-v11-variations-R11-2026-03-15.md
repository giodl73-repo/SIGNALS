# flow-throttle — Round 11 Variations (v11 Rubric, 172-point max)

## Variation Axes and Hypotheses

R10 confirmed that C-33 (Pre-Analysis Inertia Frame) discriminates V-04 from V-01–V-03:
only V-04 introduced a Phase 0 section before Phase 1. C-34 (Phase-Anchor Tabular Encoding)
was inert across all four scored R10 variations — all passed.

Under v11, two new criteria are formalized:

**C-33** (3 pts): A structurally distinct section labeled Phase 0, Step 0, Baseline Frame, or
equivalent appears before Phase 1 and establishes current-state baseline. No preconditions.

**C-34** (3 pts): Phase 1 contains at least one TABLE AND Phase 4 contains at least one TABLE,
regardless of format in Phases 2–3. No preconditions.

**R11 design goal:** (1) Confirm C-33 passes with an alternative label form beyond "Phase 0"
(the R10 V-04 label) — confirming C-33 is label-text-inert as long as the structural position
and section identity are correct. (2) Decompose C-34's two anchor requirements — Phase-1 TABLE
and Phase-4 TABLE — by removing each independently to confirm both are necessary. (3) Confirm
C-33 and C-34 are both role-sequence-inert. (4) Establish the double-failure floor at 166/172
by removing both Phase 0 and Phase-4 tables simultaneously.

Three single-axis tests (V-01, V-02, V-03), then two combination tests (V-04, V-05):

| Variation | Axis | C-33 | C-34 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Single: Phase 0 alternative label — "Step 0: Baseline Snapshot" | PASS | PASS | 172/172 |
| V-02 | Single: Phase 4 fully prose — all Phase 4 tables removed | PASS | FAIL | 169/172 |
| V-03 | Single: Phase 1 numbered-entry format — TABLE 1 replaced with numbered list | PASS | FAIL | 169/172 |
| V-04 | Combination: Role sequence (PA Capacity Planner R1 + Documentation Verifier R2) + Phase 0 | PASS | PASS | 172/172 |
| V-05 | Combination: No Phase 0 + Phase 4 fully prose (double failure) | FAIL | FAIL | 166/172 |

Score spread: 172 / 169 / 169 / 172 / 166.

V-02 and V-03 both score 169 but fail C-34 via different anchor positions: V-02 removes the
Phase-4 TABLE anchor; V-03 removes the Phase-1 TABLE anchor. Together they prove C-34's
semantics require both anchor phases independently — passing one anchor while failing the
other is not sufficient. V-05 establishes the double-failure floor at 166/172, confirming
C-33 and C-34 each contribute 3 points that cannot be recovered without their specific
structural conditions.

---

## V-01 — Phase 0 Alternative Label: "Step 0: Baseline Snapshot"

**Axis:** The pre-analysis baseline section uses the label "Step 0: Baseline Snapshot"
instead of "Phase 0: Inertia Baseline" (the R10 V-04 form). The C-33 pass condition
explicitly lists "Step 0" as an acceptable label alongside "Phase 0" and "Baseline Frame."
The section is structurally distinct (heading-level section, not a preamble within Phase 1),
appears before Phase 1, and establishes current-state context: construct stack, active limits,
and operational conditions. All Phase 4 tables (TABLE 8, TABLE 9, TABLE 10) are retained.

**Hypothesis:** 172/172. C-33 evaluates structural position and section identity — a heading-
labeled "Step 0: Baseline Snapshot" appearing before Phase 1 satisfies the pass condition.
Label-text variation ("Step 0" vs. "Phase 0") is C-33-inert as long as the section is
structurally distinct and pre-Phase-1. C-34 evaluates TABLE presence in Phase 1 and Phase 4
— both anchor phases retain tables, so C-34 passes. C-01 through C-32 are unaffected: the
label of the pre-analysis section does not touch the two-barrier structural chain (C-17–C-32)
or the content criteria (C-01–C-13).

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Establish the current-state baseline first — what the
system does today under load before any throttle-aware design — then identify where that
baseline fails at the scenario's request volume.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### STEP 0 — Baseline Snapshot

*Establish what the system does today. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume
at the scenario load. State each construct's current configuration (default settings; no
explicit throttle handling, backpressure controls, or concurrency caps applied).

**Active limits in effect:** For each construct named above, state the limit that applies
under the current configuration and license tier. This is the inertia profile — the ceiling
the system is operating under whether the team is aware of it or not.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context (per-user plan, per-flow plan, or environment-level). These conditions
drive all downstream analysis.

**Baseline failure point:** Identify where the inertia state first breaks at this volume.
Name the construct, the limit it hits, and the user-visible consequence when no mitigation is
present. This is the status quo outcome a team accepts by doing nothing.

*Step 0 produces no gate. Proceed to Phase 1.*

---

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

*Anchor to baseline: how does the Step 0 inertia state reach this bottleneck? Reference the
baseline failure point identified in Step 0.*

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

*Anchor to baseline: which UX tier row represents the inertia state's outcome? Mark it.*

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write explicit acknowledgment with guards currently in
place.

*Anchor to baseline: are these burst paths present and unguarded in the Step 0 inertia state?*

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
linking them.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (all fields filled, Tier A != Tier B,
mechanism stated, severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Produce TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence levels: HIGH (limit sourced from Microsoft documentation), MEDIUM (limit from
community source or observed admin center value), LOW (estimated from runtime behavior).
Flag MEDIUM or LOW rows for Round 2 audit. "Confirmed" requires the exact PA documentation
name — not paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category against PA runtime
behavior. Internal system behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation or
headroom]." Qualitative "this will hit the limit" without numeric projection does not pass.

*Anchor to baseline: which TABLE 9 rows confirm the Step 0 failure point? Mark each row
that would be OVER-LIMIT in the inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs. "Add retries" and "reduce load" do
not count. Each remediation must map to a specific finding from Phases 2–3 by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal: flow run history throttle status, connector call
telemetry in Power Platform admin center, request usage dashboard. State the condition each
signal surfaces and when it would trigger. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State
the impact on this scenario's volume: does the entitlement change shift any TABLE 9 row from
SAFE to OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling. "Test in staging" without a
specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's Step 0 baseline and Phase 1–4 simulation are not evidence of
Round 2's construct precision. A grounded baseline and thorough simulation can still contain
PA construct names that are imprecise, rate units drawn from estimates rather than
documentation, or cascade mechanisms described at a directional level where numeric precision
is required. Round 2 operates independently of Round 1's baseline framing and analysis quality.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

For each TABLE 8 row, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? State the documentation source.

2. **Numeric limit precision:** Is the limit the documented platform limit or a derived
   estimate? State the specific source for each row. "Generally known limit" does not pass.

3. **Rate unit precision:** Confirm the unit (per-minute / per-second / per-24-hours /
   per-user / per-environment) matches the construct's documented enforcement granularity.
   A correct number with wrong units is a documentation error.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (exact signal path
   and load calculation) or qualitative? Promote qualitative statements using TABLE 9
   arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a directional
   estimate? If directional, compute the numeric projection from TABLE 9 data.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-01 prompt body.*

---

## V-02 — Phase 4 Fully Prose (No Tables in Phase 4)

**Axis:** Output format — Phase 4 sections (4.A through 4.G) switch entirely to prose and
bulleted-list format. TABLE 8 (PA Construct Precision Pass), TABLE 9 (Throttle Budget), and
TABLE 10 (Remediations) are all removed and replaced with structured prose. Phase 4 content
requirements remain identical: construct validation, UX validation, quantified risk register
(with arithmetic), PA-native remediations, monitoring signals, entitlement boundary, test
approach. Only the encoding medium changes. Phase 1 retains TABLE 1 (Throttle Tier Map).
Phase 0 is present ("Phase 0 — Inertia Baseline"). Round 2 retains TABLE 11.

**Hypothesis:** 169/172. C-33 passes — Phase 0 is present and structurally distinct before
Phase 1. C-34 fails — Phase 4 contains no TABLE at all; the Phase-4 TABLE anchor required
by C-34 is absent. Phase 1 TABLE 1 is present, but C-34 requires BOTH Phase 1 AND Phase 4
to contain a TABLE; satisfying only one anchor is insufficient. C-01 through C-32 are all
format-inert for content criteria (C-01–C-13) and for structural barrier criteria (C-17–C-32)
which operate at the Round 1/Round 2 boundary, not at the Phase 4 encoding layer. Expected:
169/172 — three points lost via C-34 Phase-4 anchor failure.

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

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** Each PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call limits,
premium vs. standard connector tiers, Microsoft 365 service protection limits. "API limit"
or "service limit" does not pass. Use the exact PA documentation term.

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

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck?*

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
Categories MUST differ across tiers. Each row states user-visible outcome, not internal state.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" explanation for each row. Block:
PHASE 3 is blocked until GATE 2 passes.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check patterns: Apply to Each loop with no concurrency cap, parallel branches with
unbounded fan-out, high-frequency trigger with no debounce, nested loops, batch-size
misconfigurations. If none found, write acknowledgment with guards in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs (Tier A != Tier B, mechanism stated,
severity assessed). Block: PHASE 4 is blocked until GATE 3 passes.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

For each construct row in TABLE 1, write one validation entry in the following format:

**[Construct name]:** PA construct term — [confirmed / corrected to: exact term]. [If
corrected: state why the TABLE 1 term was imprecise.] Confidence: HIGH / MEDIUM / LOW.
[Source: state the documentation source for HIGH; state observation source for MEDIUM/LOW.]
Flag rows with MEDIUM or LOW confidence for Round 2 documentation audit.

**Section 4.B — UX Validation**

For each tier in TABLE 4, write one validation sentence: confirm or correct the UX category
against PA runtime behavior. Internal system state (queue depth increase, internal retry
counter) is not user experience. Correct any row that conflates system state with user-visible
outcome.

**Section 4.C — Quantified Risk Register**

For each construct from TABLE 1, write one risk assessment entry:

**[Construct name]:** Limit — [N req/unit]. Projected volume at scenario load — [M req/unit
with arithmetic showing [X items] x [Y calls] = [total]]. Status: SAFE / MARGINAL /
OVER-LIMIT. Headroom: [+N req/unit] or Deficit: [-N req/unit]. At least one entry must show
the arithmetic inline. Qualitative "this will hit the limit" without numeric projection does
not pass.

*Anchor to baseline: identify which entries would be OVER-LIMIT in the Phase 0 inertia state.*

**Section 4.D — PA-Specific Remediations**

For each remediation, write one entry:

**Remediation [N] — [Finding addressed from Phase 2 or 3 by section label]:** PA feature —
[exact name]. Configuration — [what to set and to what value]. Effect — [how this changes
the finding's status]. "Add retries" and "reduce load" without a specific PA construct do
not count. Minimum: two PA-native remediations.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal. State: (a) what the signal is, (b) the condition it
surfaces, (c) when it would trigger in this scenario. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary where the throttle limit materially differs. State the
impact on this scenario: does the entitlement shift change any Section 4.C entry from SAFE
to OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Describe at least one concrete test step using PA tooling. State: what to run, what to
observe, and what a pass/fail result looks like. "Test in staging" without a specific method
does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's Phase 0 baseline and prose synthesis are not evidence of Round 2's
construct precision. A thorough inertia frame and complete risk narrative can still contain PA
construct names that are imprecise, rate units drawn from estimates rather than documentation,
or cascade mechanisms stated qualitatively where numeric precision is required. Round 2
operates independently of Round 1's prose quality and synthesis depth.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names declared in Section 4.A (PA Construct
Validation) that replaced imprecise TABLE 1 entries — are now in scope for Round 2 precision
checking. These were excluded from Round 1's evaluation window because Round 1 closed before
Section 4.A corrections were finalized.

---

For each Section 4.A entry, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? State the documentation source.

2. **Numeric limit precision:** Is the limit the documented platform limit or a derived
   estimate? "Community-sourced" and "observed behavior" are not documentation.

3. **Rate unit precision:** Confirm the unit (per-minute / per-second / per-24-hours /
   per-user / per-environment) matches the construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (exact signal path
   and load calculation) or qualitative? Promote qualitative using Section 4.C arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" numeric or directional? If directional,
   compute the numeric projection using Section 4.C data.

**TABLE 11 — Round 2 Precision Audit**

| Item (Section 4.A entry or TABLE 7 pair) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-02 prompt body.*

---

## V-03 — Phase 1 Numbered-Entry Format (TABLE 1 Replaced)

**Axis:** Output format — Phase 1's construct inventory switches from a markdown table
(TABLE 1) to a numbered-entry format. Each throttle-relevant construct is expressed as a
labeled block with the same four required fields (construct name, PA construct type, numeric
limit with unit, request contribution with arithmetic, Retry-After status) stated inline rather
than as table columns. The domain rule and GATE 1 field requirements remain identical. Phase 4
retains TABLE 8, TABLE 9, and TABLE 10. Phase 0 is present ("Phase 0 — Inertia Baseline").

**Hypothesis:** 169/172. C-33 passes — Phase 0 is structurally distinct and appears before
Phase 1. C-34 fails — Phase 1 contains no TABLE; the Phase-1 TABLE anchor required by C-34
is absent. Phase 4 retains TABLE 8, 9, 10 — the Phase-4 anchor is present — but C-34 requires
BOTH anchors simultaneously; satisfying Phase 4 alone is insufficient. C-01 and C-02 (construct
inventory content criteria) are format-inert — numbered entries carry the same inventory content
as TABLE rows. C-17 through C-32 (structural barrier chain) are unaffected — Phase 1's
encoding medium does not interact with the Round 2 barrier heading or pre-barrier container.
Expected: 169/172 — three points lost via C-34 Phase-1 anchor failure.

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

Identify every throttle-relevant construct in the flow. For each construct, write a numbered
entry with the following required fields:

**Construct [N]: [Construct name]**
- PA construct type: [exact term from PA documentation domain list]
- Numeric limit: [N req/unit — include rate unit]
- Request contribution at scenario volume: [arithmetic estimate — show calculation]
- Retry-After read: yes / no / N/A

**Domain rule:** PA construct type must be drawn from: Power Platform request entitlements,
connector throttling policies, flow run concurrency limits, action call limits, premium vs.
standard connector tiers, Microsoft 365 service protection limits. Generic "API limit" or
"service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All construct entries have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution with arithmetic shown. Block:
PHASE 2 is blocked until every entry satisfies all three conditions. Entries with missing
fields receive a `?` flag — correct before proceeding.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason]. The naive
> assumption that limits are independent fails here because [cascade chain or shared pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck?*

**TABLE 2 — Hit Order**

| Hit order | Construct (from Phase 1 inventory) | Limit | Why this order holds at scenario volume |
|-----------|-------------------------------------|-------|-----------------------------------------|
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
Categories MUST differ across tiers.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has a "why this order holds" for each row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check patterns: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch-size misconfigurations. If none
found, write acknowledgment with guards currently in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, mechanism stated,
severity assessed.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct entry in Phase 1. Produce TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from Phase 1 inventory) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|------------------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation source), MEDIUM (community or admin center
observed), LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2. "Confirmed"
requires the exact PA documentation name.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

*Anchor to baseline: which TABLE 9 rows are OVER-LIMIT in the inertia state?*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to Phase 2–3 findings by section label.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition and trigger.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material throttle impact on this scenario.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's Phase 0 inertia baseline and numbered Phase 1 inventory are not
evidence of Round 2's construct precision. An inventory presented as numbered entries rather
than a table carries the same precision risk as a tabular inventory: PA construct names may
be imprecise, limits may be estimated rather than documented, units may be mismatched to
enforcement granularity. The encoding format of Phase 1 does not affect Round 2's precision
mandate. Round 2 operates independently of Phase 1's output format.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise Phase 1 entries — are now in scope for Round 2 precision checking. These were
excluded from Round 1's evaluation window because Round 1 closed before TABLE 8 corrections
were finalized.

---

For each TABLE 8 row, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? State the documentation source.

2. **Numeric limit precision:** Documented platform limit or derived estimate? State source.

3. **Rate unit precision:** Confirm unit (per-minute / per-second / per-24-hours / per-user
   / per-environment) matches documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural (exact signal path and load calculation) or
   qualitative? Promote qualitative using TABLE 9 arithmetic.

2. **Load-added precision:** Numeric or directional? If directional, compute from TABLE 9.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Role Sequence: PA Capacity Planner (R1) + Documentation Verifier (R2) + Phase 0

**Axes:** (1) Role sequence — Round 1 is owned by a PA throughput capacity planner whose
primary focus is projecting total request budget consumption across the tier stack: every
construct's contribution is quantified against its entitlement ceiling, and the output is a
capacity model, not just a failure trace. Round 2 is owned by a platform documentation
verifier whose mandate is to confirm every numeric limit and PA construct name against
published documentation, independent of the capacity model's internal arithmetic. The Round 2
subtitle is updated to "Platform Documentation Verification" to name the verifier's analysis
class. (2) Phase 0 is retained from V-04 R10, labeled "Phase 0 — Inertia Baseline."
All Phase 4 tables are retained.

**Hypothesis:** 172/172. C-33 passes — Phase 0 is present and structurally distinct before
Phase 1. C-34 passes — Phase 1 retains TABLE 1 and Phase 4 retains TABLE 8, TABLE 9,
TABLE 10. C-33 is role-sequence-inert: the pre-Phase-1 baseline section is independent of
which expert persona runs Round 1. C-34 is role-sequence-inert: the anchor-phase TABLE
requirement is independent of which roles are assigned to each round. C-32 (evaluation-type
subtitle) passes with "Platform Documentation Verification" — the form (ordinal + dash-
separated evaluation-type subtitle) is satisfied; C-32 is subtitle-text-inert, as confirmed
in R10-V01. Expected: 172/172.

---

You are a PA throughput capacity planner simulating total request budget consumption across
a rate-limited Power Automate system. For Round 2, you will operate as a platform
documentation verifier to confirm every numeric limit against Microsoft-published sources.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Capacity Model and Throttle Tier Analysis

*Role: PA throughput capacity planner.*

### PHASE 0 — Inertia Baseline

*State what the system does today. No mitigations assumed.*

**Current state:** Describe the flow's current behavior at the scenario's request volume
under default PA settings. Name the constructs involved, the volume they carry, and the
absence of explicit throttle handling. This is the status quo the team accepts by doing
nothing.

**Baseline failure point:** Identify where the inertia state first breaks. Name the
construct, the limit it hits, and the user-visible consequence when no mitigation is present.

**Why inertia persists:** State the structural reason teams leave this state unaddressed.
This establishes the obstacle the capacity model is designed to overcome.

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types from: Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. "API limit" fails. Use exact PA
documentation terms.

**Capacity planner focus:** The request contribution column is the capacity planner's primary
output. Show arithmetic for every row. The column drives TABLE 9's budget projection — rows
without arithmetic cannot be budgeted.

**GATE 1:** Every TABLE 1 row has (a) exact PA construct type, (b) numeric limit with unit,
(c) request contribution with arithmetic shown. Block: PHASE 2 blocked until all rows pass.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[PA construct component] at [PA construct type] is the binding bottleneck. It saturates
> at [N req/unit-time] under this scenario because [reason the ordering holds at aggregate
> volume]. The naive assumption that limits are independent fails here because [cascade chain
> or shared principal pool]."

*Anchor to baseline: which Phase 0 baseline failure does this bottleneck confirm?*

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
two hops. Terminal state: user-visible error, flow run failure, or silent drop.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Categories
MUST differ across tiers. State user-visible outcome, not internal system action.

**GATE 2:** TABLE 3 >= 2 hops AND TABLE 4 >= 2 tiers with distinct UX categories AND TABLE 2
ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location | Estimated peak rate | Bypass mechanism |
|----------------|------------------|----------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch misconfigurations. If none:
name guards in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After read? | Backoff behavior | Failure mode |
|-------------------|-------------|------------------|-----------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two pairs. Tier A != Tier B. Mechanism stated. Severity assessed.

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center), LOW
(runtime estimate). Flag MEDIUM or LOW for Round 2 documentation audit. "Confirmed" requires
the exact PA documentation term.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
behavior is not user experience.

**Section 4.C — Capacity Budget**

Fill TABLE 9:

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row. The capacity
planner must demonstrate arithmetic for the binding bottleneck row at minimum.

*Anchor to baseline: which TABLE 9 rows confirm the Phase 0 failure point?*

**Section 4.D — PA-Specific Remediations**

Fill TABLE 10:

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations. Each must map to a specific finding from Phases 2–3
by section label. Generic "add retries" fails.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition and trigger.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material capacity impact. State the TABLE 9
shift if entitlement changes.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step.

---

## ROUND 2 — Platform Documentation Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's capacity model — however arithmetically grounded — is not
evidence of documentation accuracy. The capacity planner's TABLE 1 numeric limits may be
sourced from community data, admin center observations, or estimated from runtime behavior.
The capacity planner's internal arithmetic consistency does not confirm that any limit matches
the Microsoft-published documented value for the scenario's license tier. Round 2's verifier
mandate operates independently of Round 1's capacity model: every numeric limit and PA
construct name is evaluated against published documentation regardless of the model's
confidence assignments.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 documentation verification. These
were excluded from Round 1's evaluation window because Round 1 closed before TABLE 8
corrections were finalized.

---

*Role: Platform documentation verifier.*

For each TABLE 8 row, apply documentation verification:

1. **Documentation source:** Is the numeric limit sourced from Microsoft Power Platform
   documentation, connector certification pages, or admin center observed values? State the
   specific source. "Generally known limit" and "standard PA limit" do not pass.

2. **License-tier match:** PA limits vary by licensing tier. Confirm the limit applies to the
   scenario's tier (per-user plan / per-flow plan / Office 365 included / premium). A limit
   from a mismatched tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Confirm the unit (per-minute / per-second / per-24-hours / per-user
   / per-environment) matches the construct's documented enforcement granularity.

For each cascade pair in TABLE 7, apply documentation checks:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or
   inferred? Inferred cascade mechanisms require explicit flagging and a verification path.

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential? A HIGH severity on a cascade where Tier B has 10x headroom requires
   justification.

**TABLE 11 — Round 2 Documentation Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — No Phase 0 + Phase 4 Fully Prose (Double Failure)

**Axes:** (1) No Phase 0 — no pre-analysis baseline section appears before Phase 1.
The analysis begins directly at Phase 1 without establishing current-state context first.
C-33 fails. (2) Phase 4 fully prose — Phase 4 sections (4.A through 4.G) use prose and
bulleted-list format exclusively. TABLE 8 (PA Construct Precision Pass), TABLE 9 (Throttle
Budget), and TABLE 10 (Remediations) are removed and replaced with structured prose. C-34
fails — the Phase-4 TABLE anchor is absent. Phase 1 retains TABLE 1 (construct inventory).

**Hypothesis:** 166/172. C-33 fails — no Phase 0 section. C-34 fails — Phase 4 has no TABLE;
Phase 1 TABLE alone does not satisfy C-34's conjunctive requirement. C-01 through C-32 all
pass: Phase 4 prose carries the same content as tables (format-inert for C-01–C-13);
the two-barrier structural chain (C-17–C-32) operates at the Round 1/Round 2 boundary, not
at the Phase 4 encoding or Phase 0 presence layer. Expected: 166/172 — six points lost, one
from C-33 and one from C-34.

This is the floor for Round 11. V-05 scores identically to the R10 ceiling (166/172) — it
confirms that C-33 and C-34 together add exactly 6 points above the R10 ceiling, and
failing both returns to the prior ceiling exactly.

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
Categories MUST differ across tiers. Each row states user-visible outcome, not internal state.

**GATE 2:** TABLE 3 has >= 2 complete hops AND TABLE 4 has >= 2 tiers with distinct UX
categories AND TABLE 2 has ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch-size misconfigurations. If none
found, write acknowledgment with guards currently in place.

**Section 3.B — Retry-After Gap Table**

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

**Section 3.C — Cascade Risk Pairs**

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs, mechanism stated,
severity assessed.

**GATE 3:** TABLE 7 has >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

For each construct in TABLE 1, write one validation paragraph:

State whether the PA construct term is confirmed (exact match to PA documentation) or
corrected (specify the imprecise term, the corrected term, and why the correction was needed).
Assign confidence: HIGH if the limit was sourced from Microsoft documentation; MEDIUM if from
community source or admin center observation; LOW if estimated from runtime behavior. Flag any
MEDIUM or LOW confidence construct for Round 2 precision audit.

**Section 4.B — UX Validation**

For each tier in TABLE 4, write one sentence confirming or correcting the UX category against
PA runtime behavior. Internal system state (queue depth, internal retry counter) does not
constitute user experience. Note any row where the originally assigned UX category conflated
system state with user-visible outcome and correct it.

**Section 4.C — Quantified Risk Register**

For each construct in TABLE 1, write one risk paragraph:

State the construct name, its numeric limit, the projected request volume at scenario load
with arithmetic (show the calculation: [N items] x [M calls/item] = [total] against [limit]),
the status (SAFE / MARGINAL / OVER-LIMIT), and the resulting headroom or deficit. At least
one paragraph must show the full arithmetic inline. Qualitative "this will hit the limit"
without numeric projection does not pass.

**Section 4.D — PA-Specific Remediations**

For each remediation, write one paragraph identifying: the specific finding it addresses
(reference Phase 2 or Phase 3 section label), the exact PA feature name, the configuration
change (what to set and to what value), and the effect on the finding. Minimum: two
remediations using PA-native constructs. "Add retries" and "reduce load" without a specific
PA construct do not count.

**Section 4.E — Monitoring Signals**

Write a paragraph naming at least one PA-observable signal. State: what the signal is (flow
run history throttle status, connector call telemetry in Power Platform admin center, request
usage dashboard, or equivalent), the condition it surfaces, and when it would trigger given
this scenario's volume. Generic "set up alerting" does not pass.

**Section 4.F — License and Entitlement Boundary**

Write a paragraph naming at least one entitlement boundary where the throttle limit materially
differs (e.g., Office 365 E3 vs. Power Apps per-user plan). State the impact on this
scenario: does the entitlement difference shift any Section 4.C status from SAFE to
OVER-LIMIT or vice versa?

**Section 4.G — Test Approach**

Write a paragraph describing at least one concrete test step using PA tooling. State what
to run, what to observe, and how to interpret the result. "Test in staging" without a
specific method does not pass.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's simulation output — construct inventory, bottleneck analysis,
cascade register, and prose synthesis — is not evidence of Round 2's construct precision.
A thorough simulation with well-grounded TABLE 1 entries and detailed Phase 4 prose can
still contain PA construct names that are imprecise, rate units drawn from estimates rather
than documentation, or cascade mechanisms described qualitatively where numeric precision is
required. The prose format of Phase 4 does not affect Round 2's precision mandate. Round 2
operates independently of Round 1's encoding choices and analysis depth.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically any corrected construct names declared in Section 4.A (PA Construct
Validation) that replaced imprecise TABLE 1 entries — are now in scope for Round 2 precision
checking. These were excluded from Round 1's evaluation window because Round 1 closed before
Section 4.A corrections were finalized.

---

For each Section 4.A construct validation entry, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? State the specific documentation source for each construct.
   "Generally known limit" and "community-sourced" do not pass.

2. **Numeric limit precision:** Is the limit the documented platform limit for the scenario's
   license tier, or a derived estimate? State the source.

3. **Rate unit precision:** Confirm the unit (per-minute / per-second / per-24-hours /
   per-user / per-environment) matches the construct's documented enforcement granularity.
   A correct number with wrong units is a documentation error.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Is the mechanism statement structural (exact signal path
   and load calculation) or qualitative? Promote qualitative statements using the Section 4.C
   arithmetic.

2. **Load-added precision:** Is "Load added to Tier B" a numeric projection or a directional
   estimate? If directional, compute the numeric projection from Section 4.C data.

**TABLE 11 — Round 2 Precision Audit**

| Item (Section 4.A entry or TABLE 7 pair) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*
