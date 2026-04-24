# flow-throttle — Round 12 Variations (v12 Rubric, 178-point max)

## Variation Axes and Hypotheses

R11 confirmed that C-35 (Pre-Analysis Baseline Heading Subtitle) is inert across all four
scored variations — all pass. C-36 (Phase-4 Anchor Heading Evaluation-Type Subtitle) was the
sole discriminator: only V-04 introduced an evaluation-type subtitle on the Phase 4 heading
("Capacity Synthesis and PA Validation"), scoring 178; V-01 scored 175 (C-35 PASS, C-36 FAIL)
because its Phase 4 heading lacked an evaluation-type subtitle. V-02 and V-03 scored 172
(C-34 FAIL + C-36 FAIL).

Under v12, two new criteria are formalized:

**C-35** (3 pts, requires C-33): Phase 0/Step 0 heading carries a dash-separated (or otherwise
delimited) subtitle naming the baseline content class — not merely an ordinal or label. A heading
like `### PHASE 0 — Inertia Baseline` passes; `### PHASE 0` alone fails.

**C-36** (3 pts, no preconditions): Phase 4 heading carries a dash-separated subtitle naming the
output or synthesis class — an evaluation-type subtitle, not a generic operation description.
A heading like `### PHASE 4 — Capacity Synthesis and PA Validation` passes; `### PHASE 4 —
Synthesis and Validation` (operations listed, no named output class) fails.

**R12 design goals:**
1. Confirm C-36 is subtitle-text-inert for conforming evaluation-type subtitle forms — a Phase 4
   subtitle different from R11 V-04's "Capacity Synthesis and PA Validation" should still pass C-36
   if it names an output class.
2. Confirm C-36 fails when the Phase 4 heading carries an operation-description subtitle rather
   than an evaluation-type subtitle — establishing the failure boundary.
3. Confirm C-35 fails when the Phase 0 heading carries no content-type subtitle — establishing
   that the subtitle is structural, not decorative.
4. Confirm C-35 and C-36 are independent: a variation failing C-35 while passing C-36 should
   score identically to one failing C-36 while passing C-35.
5. Confirm both criteria are role-sequence-inert — persona assignment in Round 1/Round 2 does
   not interact with Phase 0 or Phase 4 heading structure.

Three single-axis tests (V-01, V-02, V-03), then two combination tests (V-04, V-05):

| Variation | Axis | C-35 | C-36 | Predicted score |
|-----------|------|------|------|-----------------|
| V-01 | Single: Phase 4 alternative evaluation-type subtitle text ("Remediation Registry and Throttle Budget Corrections") | PASS | PASS | 178/178 |
| V-02 | Single: Phase 4 operation-description subtitle ("Synthesis and Validation") — not an evaluation-type subtitle | PASS | FAIL | 175/178 |
| V-03 | Single: Phase 0 plain ordinal heading, no content-type subtitle | FAIL | PASS | 175/178 |
| V-04 | Combination: role sequence variation + Phase 0 new subtitle text ("Current-State Inventory") + Phase 4 new subtitle text ("Throttle Budget Corrections") | PASS | PASS | 178/178 |
| V-05 | Combination: Phase 0 plain heading (C-35 fail) + Phase 4 operation-description subtitle (C-36 fail) | FAIL | FAIL | 172/178 |

Score spread: 178 / 175 / 175 / 178 / 172.

V-01 and V-04 establish the 178 ceiling with distinct subtitle text forms. V-02 and V-03 each
score 175 via a single-criterion failure on opposite heading positions — their equal scores
confirm C-35 and C-36 are independent (failing either one costs exactly 3 points; failing the
other in a separate variation costs exactly 3 points). V-05 establishes the double-failure
floor at 172/178, confirming C-35 and C-36 together add exactly 6 points above the R11
C-35/C-36-absent baseline.

---

## V-01 — Phase 4 Alternative Evaluation-Type Subtitle Text

**Axis:** Phase 4 heading carries an alternative evaluation-type subtitle — "Remediation
Registry and Throttle Budget Corrections" — rather than the R11 V-04 form "Capacity Synthesis
and PA Validation." The C-36 pass condition explicitly lists "Remediation Registry" and
"Throttle Budget Corrections" as conforming subtitle examples. If C-36 is subtitle-text-inert
(as C-32 was confirmed text-inert in R10), any conforming evaluation-type subtitle should pass.

**Secondary axis:** Phrasing register — the prompt uses a more directive register throughout,
with imperative section instructions ("Fill," "State," "Name") made consistent across all phases
rather than mixing directive and descriptive forms.

Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS — carries subtitle "Inertia
Baseline," naming the content class of the pre-analysis section).

Phase 4 heading: `### PHASE 4 — Remediation Registry and Throttle Budget Corrections`
(C-36 PASS — "Remediation Registry" names the output class; the subtitle is evaluation-type,
not a list of operations).

**Hypothesis:** 178/178. C-35 passes — Phase 0 heading carries "Inertia Baseline" subtitle,
exactly the form confirmed in R11 V-02/V-03/V-04. C-36 passes — the Phase 4 subtitle names
an output class in evaluation-type form. If C-36 is subtitle-text-inert (hypothesis to confirm),
this variation proves that the R11 V-04 specific text is not required — any conforming evaluation-
type subtitle satisfies C-36. C-01 through C-34 are unaffected: Phase 4 retains TABLE 8, TABLE 9,
TABLE 10 (C-34 PASS); Phase 0 retains the structurally distinct pre-Phase-1 section (C-33 PASS);
Phase 4 heading text does not interact with the two-barrier chain (C-17–C-32) or content criteria
(C-01–C-13). Round 2 barrier heading retains evaluation-type subtitle (C-32 PASS).

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Establish the inertia baseline first — what the system
does today under load before any throttle-aware design — then identify where that baseline
fails at the scenario's request volume.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0 — Inertia Baseline

*State what the system does today. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume
at the scenario load. State each construct's current configuration — default settings, no
explicit throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct named above, state the limit that applies
under the current configuration and license tier. This is the inertia profile — the ceiling
the system operates under whether the team is aware of it or not.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the inertia state first breaks at this volume.
Name the construct, the limit it hits, and the user-visible consequence when no mitigation
is present. This is the outcome a team accepts by doing nothing.

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

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds
> at this aggregate volume]. The naive assumption that limits are independent fails here
> because [one sentence linking to cascade chain or shared principal pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck? Reference
the baseline failure point identified in Phase 0.*

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
Categories MUST differ across tiers. Each row states what the user sees — not what the
system does internally.

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

Check: Apply to Each loop with no concurrency cap, parallel branches with unbounded fan-out,
high-frequency trigger with no debounce, nested loops, batch-size misconfigurations. If none
found, write explicit acknowledgment with guards currently in place.

*Anchor to baseline: are these burst paths present and unguarded in the Phase 0 inertia state?*

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

### PHASE 4 — Remediation Registry and Throttle Budget Corrections

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center observed),
LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2 audit. "Confirmed" requires
the exact PA documentation name — not a paraphrase.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct the UX category against PA runtime
behavior. Internal system behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row:
"[N items] x [M connector calls] = [total req], against [limit req/unit] → [saturation
or headroom]." Qualitative "this will hit the limit" without numeric projection does not pass.

*Anchor to baseline: which TABLE 9 rows confirm the Phase 0 failure point? Mark each row
that would be OVER-LIMIT in the inertia state.*

**Section 4.D — PA-Specific Remediations**

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two remediations using PA-native constructs. "Add retries" and "reduce load"
do not count. Each remediation must map to a specific finding from Phases 2–3 by section
label.

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

**Independence:** Round 1's Phase 0 baseline and Phase 1–4 simulation are not evidence of
Round 2's construct precision. A grounded inertia baseline and thorough simulation can still
contain PA construct names that are imprecise, rate units drawn from estimates rather than
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

## V-02 — Phase 4 Operation-Description Subtitle (Fail C-36)

**Axis:** Phase 4 heading carries a subtitle that describes the phase's operations rather
than naming an output or synthesis class. The heading becomes `### PHASE 4 — Synthesis and
Validation` — a description of what the phase does (it synthesizes and validates) rather
than an evaluation-type subtitle declaring what class of output the phase produces.

The C-36 pass condition requires a subtitle "naming the output or synthesis class" and
explicitly states "the subtitle must name an output class, not merely repeat the phase label."
An operation-description subtitle like "Synthesis and Validation" describes phase operations
without naming an analysis class or registry type. It fails the evaluation-type requirement
in the same way that `### Phase 0` without a content-type subtitle fails C-35 — the heading
is structurally present but carries no class declaration.

Phase 0 heading: `### PHASE 0 — Inertia Baseline` (C-35 PASS).
Phase 4 heading: `### PHASE 4 — Synthesis and Validation` (C-36 FAIL — operation list, not
evaluation-type subtitle).

**Hypothesis:** 175/178. C-35 passes — Phase 0 heading carries "Inertia Baseline," naming the
content class. C-36 fails — "Synthesis and Validation" lists operations performed rather than
naming an output class or synthesis registry. C-34 passes — Phase 1 retains TABLE 1 and
Phase 4 retains TABLE 8, TABLE 9, TABLE 10 (the tabular encoding requirement is independent
of the heading subtitle). C-01 through C-33 are unaffected: the Phase 0 section is present
(C-33 PASS); the Phase 4 heading text does not interact with any prior content or barrier
criteria. Expected: 175/178 — three points lost via C-36 failure.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Start from the inertia baseline — what the system does
today without throttle awareness — then identify where that baseline fails at the scenario's
request volume.

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
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic "API
limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 is blocked until every row satisfies all three conditions. Rows with missing
fields receive a `?` flag.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason]. The naive
> assumption that limits are independent fails here because [cascade chain or shared pool]."

*Anchor to baseline: how does the Phase 0 inertia state reach this bottleneck?*

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
two hops. Trace to terminal state.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers. State user-visible outcome, not internal system state.

*Anchor to baseline: which UX tier row represents the inertia state's outcome? Mark it.*

**GATE 2:** TABLE 3 >= 2 complete hops AND TABLE 4 >= 2 tiers with distinct UX categories
AND TABLE 2 "why this order holds" per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch-size misconfigurations. If none
found, write acknowledgment with guards in place.

*Anchor to baseline: are these burst paths present and unguarded in the Phase 0 inertia state?*

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

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center observed),
LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2.

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

Describe at least one concrete PA tooling test step with observable pass/fail result.

---

## ROUND 2 — Structural Precision Pass

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's Phase 0 baseline and Phase 1–4 simulation are not evidence of
Round 2's construct precision. A grounded inertia frame and complete synthesis can still
contain PA construct names that are imprecise, rate units drawn from estimates rather than
documentation, or cascade mechanisms described at a directional level where numeric precision
is required. Round 2 operates independently of Round 1's synthesis quality.

**Scope extension:** Construct populations introduced after Round 1's execution window had
closed — specifically corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries — are now in scope for Round 2 precision checking.

---

For each TABLE 8 row, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? State the documentation source.

2. **Numeric limit precision:** Documented platform limit or derived estimate? State source.
   "Generally known limit" does not pass.

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

*End of V-02 prompt body.*

---

## V-03 — Phase 0 Plain Ordinal Heading, No Content-Type Subtitle (Fail C-35)

**Axis:** Phase 0 heading carries only the ordinal label — `### PHASE 0` — with no
dash-separated content-type subtitle. The section is structurally present and establishes
current-state context (C-33 PASS). But the heading does not declare its content class: a
reader encountering `### PHASE 0` cannot determine from the heading alone whether the section
contains an inertia baseline, a system inventory, a load snapshot, or some other pre-analysis
content. C-35 requires the heading to carry a subtitle that names the baseline content class —
the structural analog of C-32's requirement on barrier headings. Without the subtitle, C-35
fails regardless of the section's content.

Phase 0 heading: `### PHASE 0` (C-33 PASS — structurally distinct pre-Phase-1 section;
C-35 FAIL — no content-type subtitle on the heading).
Phase 4 heading: `### PHASE 4 — Capacity Synthesis and PA Validation` (C-36 PASS — same
evaluation-type subtitle as R11 V-04).

**Hypothesis:** 175/178. C-33 passes — Phase 0 section is structurally distinct and appears
before Phase 1, establishing current-state context. C-35 fails — `### PHASE 0` carries no
subtitle; the heading is a structural placeholder, not a self-documenting content-type
declaration. C-36 passes — Phase 4 heading carries "Capacity Synthesis and PA Validation,"
the R11 V-04 confirmed evaluation-type subtitle. C-34 passes — Phase 1 retains TABLE 1 and
Phase 4 retains TABLE 8, TABLE 9, TABLE 10. This variation confirms C-35 and C-36 are
independent: failing C-35 while passing C-36 scores identically (175/178) to failing C-36
while passing C-35 (V-02: 175/178). Expected: 175/178 — three points lost via C-35 failure.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Identify the current-state baseline before any
throttle-aware design, then trace where bottlenecks occur, how backpressure propagates, and
what the user experience is at each throttle tier.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0

*State what the system does today. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume
at the scenario load. State each construct's current configuration — default settings, no
explicit throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct named above, state the limit that applies
under the current configuration and license tier.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context (per-user plan, per-flow plan, or environment-level).

**Baseline failure point:** Identify where the current state first breaks at this volume.
Name the construct, the limit it hits, and the user-visible consequence when no mitigation
is present.

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
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic "API
limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 blocked until all rows pass. Missing fields receive a `?` flag.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason the ordering holds].
> The naive assumption that limits are independent fails here because [cascade chain or
> shared principal pool]."

*Anchor to baseline: how does the Phase 0 current state reach this bottleneck?*

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
two hops. Trace to terminal state (user-visible error, flow run failure, or silent drop).

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers.

**GATE 2:** TABLE 3 >= 2 complete hops AND TABLE 4 >= 2 tiers with distinct UX categories
AND TABLE 2 ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch-size misconfigurations. If none
found, write acknowledgment with guards in place.

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

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Capacity Synthesis and PA Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center observed),
LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
behavior is not user experience.

**Section 4.C — Quantified Risk Register**

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

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

**Independence:** Round 1's Phase 0 pre-analysis section and Phase 1–4 simulation are not
evidence of Round 2's construct precision. A structurally complete analysis can still contain
PA construct names that are imprecise, rate units drawn from estimates rather than
documentation, or cascade mechanisms described qualitatively where numeric precision is
required. Round 2 operates independently of Round 1's structural completeness.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are now in scope for Round 2 precision checking.

---

For each TABLE 8 row, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? State the documentation source.

2. **Numeric limit precision:** Documented platform limit or derived estimate? State source.

3. **Rate unit precision:** Confirm unit matches documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural or qualitative? Promote qualitative using
   TABLE 9 arithmetic.

2. **Load-added precision:** Numeric or directional? If directional, compute from TABLE 9.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-03 prompt body.*

---

## V-04 — Combination: Role Sequence + Phase 0 "Current-State Inventory" + Phase 4 "Throttle Budget Corrections"

**Axes:** (1) Role sequence — Round 1 is owned by a PA throttle scenario analyst whose
primary mandate is to project aggregate request volume against the tier stack and identify
where the principal budget exhausts first. The analyst's Phase 0 is an operational inventory
of the current-state system, not a narrative baseline. Round 2 is owned by a platform
entitlement verifier whose mandate is to confirm every numeric limit against the documented
entitlement tier applicable to the scenario's license class. (2) Phase 0 heading: `### PHASE 0
— Current-State Inventory` (new subtitle text — "Current-State Inventory" names the content
class of the pre-analysis section; different from "Inertia Baseline" to confirm C-35 is
subtitle-text-inert). (3) Phase 4 heading: `### PHASE 4 — Throttle Budget Corrections` (from
the C-36 explicit example list — different from "Capacity Synthesis and PA Validation" to
confirm C-36 is subtitle-text-inert for additional conforming forms).

**Hypothesis:** 178/178. C-35 passes — "Current-State Inventory" names the content class of
the Phase 0 section; the subtitle form satisfies C-35's requirement for a content-type
declaration on the heading. This confirms C-35 subtitle-text inertness: any subtitle naming
a baseline content class (not just "Inertia Baseline") satisfies C-35. C-36 passes — "Throttle
Budget Corrections" names an output class explicitly listed in the C-36 pass examples. This
confirms C-36 subtitle-text inertness: "Capacity Synthesis and PA Validation" is not the only
passing form. C-33 passes — Phase 0 is structurally distinct before Phase 1. C-34 passes —
Phase 1 retains TABLE 1 and Phase 4 retains TABLE 8, TABLE 9, TABLE 10. Both criteria are
role-sequence-inert: the analyst/verifier persona assignment does not interact with Phase 0 or
Phase 4 heading structure. Round 2 heading carries "Entitlement Verification" (C-32 PASS —
evaluation-type subtitle, role-matched to the verifier persona).

---

You are a PA throttle scenario analyst simulating aggregate request volume across a rate-
limited Power Automate system. For Round 2, you will operate as a platform entitlement
verifier to confirm every numeric limit against the documented entitlement tier for the
scenario's license class.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

*Role: PA throttle scenario analyst.*

### PHASE 0 — Current-State Inventory

*Inventory the system's current state. No throttle mitigations assumed.*

**Construct inventory:** Name every PA construct in the flow that carries request volume at
the scenario load. For each construct, state the current configuration — default settings,
no explicit throttle handling applied.

**Active limit profile:** For each construct, state the enforced limit under the current
license tier and configuration. This is the operational ceiling the system runs against
whether or not the team has measured it.

**Scenario parameters:** State the request volume, trigger frequency, and principal context
(per-user plan, per-flow plan, or environment-level). These parameters drive all downstream
volume projections.

**First-break point:** Identify which construct in the current inventory breaks first at the
scenario volume. State the limit it hits and the operational consequence with no mitigation
in place. This is the current-state failure the analyst is modeling against.

*Phase 0 produces no gate. Proceed to Phase 1.*

---

### PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain rule:** PA construct types from: Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits. Generic "API limit" fails. Use
exact PA documentation terms.

**Analyst focus:** The request contribution column is the primary analyst output. Show
arithmetic for every row. These projections drive TABLE 9's budget model — rows without
arithmetic cannot be budgeted.

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

*Anchor to baseline: which Phase 0 first-break point does this bottleneck confirm?*

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

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers. State user-visible outcome, not internal system action.

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
name guards currently in place.

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

### PHASE 4 — Throttle Budget Corrections

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center), LOW
(runtime estimate). Flag MEDIUM or LOW for Round 2 entitlement verification. "Confirmed"
requires the exact PA documentation name.

**Section 4.B — UX Validation**

Review TABLE 4. One sentence per tier: confirm or correct UX category. Internal system
state is not user experience.

**Section 4.C — Capacity Budget**

Fill TABLE 9:

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row. The analyst
must demonstrate arithmetic for the binding bottleneck row at minimum.

*Anchor to baseline: which TABLE 9 rows confirm the Phase 0 first-break point?*

**Section 4.D — PA-Specific Remediations**

Fill TABLE 10:

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to specific findings from Phases 2–3 by section
label. Generic "add retries" fails.

**Section 4.E — Monitoring Signals**

Name at least one PA-observable signal with condition, trigger, and when it fires in this
scenario.

**Section 4.F — License and Entitlement Boundary**

Name at least one entitlement boundary with material capacity impact. State which TABLE 9
row shifts status if the entitlement tier changes.

**Section 4.G — Test Approach**

Describe at least one concrete PA tooling test step with observable pass/fail result.

---

## ROUND 2 — Entitlement Verification

### PRE-EVALUATION ASSERTIONS (before any Round 2 construct evaluation begins)

**Independence:** Round 1's throttle scenario model — however arithmetically grounded — is
not evidence of entitlement accuracy. The scenario analyst's TABLE 1 numeric limits may be
sourced from community data, admin center observations, or estimated from runtime behavior.
The analyst's internal arithmetic consistency does not confirm that any limit matches the
Microsoft-published documented value for the scenario's license tier. Round 2's verifier
mandate operates independently of Round 1's model: every numeric limit and PA construct name
is evaluated against published entitlement documentation regardless of the analyst's
confidence assignments.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are now in scope for Round 2 entitlement verification.

---

*Role: Platform entitlement verifier.*

For each TABLE 8 row, apply entitlement verification:

1. **Documentation source:** Is the numeric limit sourced from Microsoft Power Platform
   documentation, connector certification pages, or admin center observed values? State the
   specific source. "Generally known limit" does not pass.

2. **License-tier match:** Confirm the limit applies to the scenario's entitlement tier
   (per-user plan / per-flow plan / Office 365 included / premium). A limit from a mismatched
   tier is a documentation error regardless of numeric value.

3. **Rate unit source:** Confirm the unit matches the construct's documented enforcement
   granularity (per-minute / per-second / per-24-hours / per-user / per-environment).

For each cascade pair in TABLE 7, apply documentation checks:

1. **Mechanism documentation:** Is the cascade mechanism documented platform behavior or
   inferred? Inferred mechanisms require explicit flagging and a verification path.

2. **Severity calibration:** Is the severity rating consistent with the documented limit
   differential? Justify HIGH severity where Tier B has significant headroom.

**TABLE 11 — Round 2 Entitlement Verification**

| Item (TABLE ref + row) | Documentation source | Verification finding (confirmed / mismatch / undocumented) | Correction if needed |
|------------------------|---------------------|-----------------------------------------------------------|---------------------|

---

*End of V-04 prompt body.*

---

## V-05 — Combination: Phase 0 Plain Heading (Fail C-35) + Phase 4 Operation-Description Subtitle (Fail C-36)

**Axes:** (1) Phase 0 heading carries only the ordinal label — `### PHASE 0` — with no
content-type subtitle (C-35 FAIL). (2) Phase 4 heading carries an operation-description
subtitle — `### PHASE 4 — Synthesis and Validation` — that lists the phase's operations
rather than naming an output class (C-36 FAIL). Phase 0 section content is present and
structurally distinct (C-33 PASS). Phase 1 retains TABLE 1 and Phase 4 retains TABLE 8,
TABLE 9, TABLE 10 (C-34 PASS). All other criteria are unaffected.

**Hypothesis:** 172/178. C-35 fails — `### PHASE 0` carries no content-type subtitle; the
heading is a structural placeholder. C-36 fails — `### PHASE 4 — Synthesis and Validation`
describes operations, not an output class. C-33 passes — Phase 0 section is present and
pre-Phase-1. C-34 passes — anchor-phase tabular encoding is present. C-01 through C-32 all
pass — the two-barrier chain, content criteria, and all prior aspirationals are unaffected
by Phase 0 and Phase 4 heading text.

This is the double-failure floor for Round 12. V-05 confirms that C-35 and C-36 together
add exactly 6 points above the R11 ceiling baseline (172/178 = 172 + 0), and that failing
both simultaneously returns to the R11 full-pass score of 172. The floor confirms each of
C-35 and C-36 contributes 3 points independently: failing one (V-02 or V-03) costs 3 points
to 175; failing both (V-05) costs 6 points to 172.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system. Establish the current-state baseline before any
throttle-aware design, then identify where bottlenecks occur, how backpressure propagates,
and what the user experience is at each throttle tier.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## ROUND 1 — Throttle Tier Mapping and Impact Analysis

### PHASE 0

*State what the system does today. No throttle mitigations assumed.*

**Current construct stack:** Name every PA construct in the flow that carries request volume
at the scenario load. State each construct's current configuration — default settings, no
explicit throttle handling, no backpressure controls, no concurrency caps applied.

**Active limits in effect:** For each construct, state the limit that applies under the
current configuration and license tier.

**Baseline operational conditions:** State the scenario's request volume, trigger frequency,
and principal context.

**Baseline failure point:** Identify where the current state first breaks at this volume.
Name the construct, the limit it hits, and the user-visible consequence when no mitigation
is present.

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
premium vs. standard connector tiers, Microsoft 365 service protection limits. Generic "API
limit" or "service limit" does not pass. Use the exact PA documentation term.

**GATE 1:** All TABLE 1 rows have (a) an exact PA construct type from the domain list,
(b) a numeric limit with unit, (c) a request contribution estimate with arithmetic shown.
Block: PHASE 2 blocked until all rows pass. Missing fields receive a `?` flag.

---

### PHASE 2 — Bottleneck, Propagation, and UX Analysis

*(GATE 1 must pass before this phase executes.)*

**Section 2.A — Rate Limit Hit Ordering**

State the bottleneck:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason]. The naive
> assumption that limits are independent fails here because [cascade chain or shared pool]."

*Anchor to baseline: how does the Phase 0 current state reach this bottleneck?*

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
two hops. Trace to terminal state.

**Section 2.C — User Experience per Throttle Tier**

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers.

**GATE 2:** TABLE 3 >= 2 complete hops AND TABLE 4 >= 2 tiers with distinct UX categories
AND TABLE 2 ordering rationale per row. Block: PHASE 3 blocked.

---

### PHASE 3 — Exposure Analysis

*(GATE 2 must pass before this phase executes.)*

**Section 3.A — Unprotected Burst Paths**

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Bypass mechanism |
|----------------|------------------|-----------------|--------------------|--------------------|

Check: Apply to Each (no concurrency cap), parallel branches (unbounded fan-out),
high-frequency trigger (no debounce), nested loops, batch-size misconfigurations. If none
found, write acknowledgment with guards in place.

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

**GATE 3:** TABLE 7 >= 2 complete cascade pairs. Block: PHASE 4 blocked.

---

### PHASE 4 — Synthesis and Validation

*(GATE 3 must pass before this phase executes.)*

**Section 4.A — PA Construct Validation**

Review every construct in TABLE 1. Fill TABLE 8:

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Correction reason | Precision note |
|--------------------------|-------------------------------------|------------------|----------------|

Confidence: HIGH (Microsoft documentation), MEDIUM (community or admin center observed),
LOW (estimated from runtime). Flag MEDIUM or LOW for Round 2.

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

**Independence:** Round 1's Phase 0 pre-analysis and Phase 1–4 simulation are not evidence
of Round 2's construct precision. A structurally complete analysis can still contain PA
construct names that are imprecise, rate units drawn from estimates rather than documentation,
or cascade mechanisms described qualitatively where numeric precision is required. Round 2
operates independently of Round 1's structural completeness.

**Scope extension:** Corrected construct names from TABLE 8 (Section 4.A) that replaced
imprecise TABLE 1 entries are now in scope for Round 2 precision checking.

---

For each TABLE 8 row, apply precision checks:

1. **PA construct name precision:** Is the confirmed/corrected name the exact term used in
   Power Automate documentation? State the documentation source.

2. **Numeric limit precision:** Documented platform limit or derived estimate? State source.

3. **Rate unit precision:** Confirm unit matches documented enforcement granularity.

For each cascade pair in TABLE 7, apply precision checks:

1. **Causal mechanism precision:** Structural or qualitative? Promote qualitative using
   TABLE 9 arithmetic.

2. **Load-added precision:** Numeric or directional? If directional, compute from TABLE 9.

**TABLE 11 — Round 2 Precision Audit**

| Item (TABLE ref + row) | Precision check applied | Finding (precise / imprecise / corrected) | Correction if needed |
|------------------------|------------------------|------------------------------------------|---------------------|

---

*End of V-05 prompt body.*
