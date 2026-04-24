# flow-throttle Variate — Round 14
**Date:** 2026-03-15
**Rubric:** v13 (C-01 through C-46, denominator /38)
**Baseline ceiling:** R13 V-05 confirmed triple-axis (TABLE 0 + mandate overlay + single-analyst)
with C-42–C-45; C-46 formalized from R13 universal GATE 3 failure (TABLE 7 named alone in both
predicate blocks; TABLE 5 and TABLE 6 absent from every variation).

---

## State Analysis: What R13 Established vs. What R14 Must Add

**R13 confirmed (v12 criteria plus C-46 formalized as v13):**
- C-42: Gate-arrival acknowledgment positional anchor (immediately after `---`, before `##`
  heading) is register-inert (V-01) and format-inert (V-02, V-04).
- C-43: Positional qualifier "at the end of this phase" in non-sub statements is
  format-inert (V-02, V-04): holds in blockquote form and numbered checklist form.
- C-44: Monitoring continuity clause (`TABLE 0 monitoring carries into Phase N`) is
  footprint-inert (V-03): holds under compressed Phase 1.
- C-45: Five-element phase-transition sequence is inertia-framing-inert (V-05): holds when
  a Current State preamble precedes Phase 1 TABLE 0.
- **R13 universal failure (C-46)**: All five R13 variations' GATE 3 predicate blocks
  referenced TABLE 7 only. Both the cleared and not-cleared predicate blocks omitted TABLE 5
  and TABLE 6 in every variation. Evidence: "GATE 3 references TABLE 7 only; TABLE 5 and
  TABLE 6 absent from both cleared and not-cleared predicates in all five variations."
  C-46 closes this gap — both GATE 3 predicate blocks must name TABLE 5, TABLE 6, and
  TABLE 7 explicitly by token.

**What R13 did NOT test under v13:**
- **C-46 plain baseline** (single-analyst, no overlay, no TABLE 0, formal register): Whether
  the GATE 3 three-table fix holds in the simplest axis configuration. Risk: absent a
  specific template enforcement, the model reverts to the R13 failure pattern (TABLE 7 only).
- **C-46 register-inertia**: Whether GATE 3 three-table naming survives when the instructional
  prose uses conversational/imperative register. Risk: conversational register leads the model
  to write "check that all three tables are filled" without naming TABLE 5, TABLE 6, TABLE 7
  as distinct tokens.
- **C-46 format-inertia (checklist)**: Whether GATE 3 three-table naming holds when Phase 3
  has a numbered checklist whose item 1 enumerates "TABLE 5 — Burst Path Register; TABLE 6 —
  Retry-After Gaps; TABLE 7 — Cascade Risk Register." Risk: model treats the checklist
  enumeration as satisfying gate predicate coverage and abbreviates the GATE 3 predicate to
  "TABLE 7 complete."
- **C-46 + TABLE 0 (V-03/V-04 axis)**: Whether GATE 3 three-table naming holds under TABLE 0
  + monitoring continuity (C-37, C-39, C-44). Risk: continuity acknowledgment at the Phase 3
  boundary may crowd the gate predicate block.
- **C-46 + triple-axis (V-05 style)**: Whether GATE 3 three-table naming holds within the
  five-element phase-transition sequence when mandate overlay + TABLE 0 + single-analyst are
  all active. Risk: PHASE 3 MANDATE block enumerates TABLE 5, TABLE 6, TABLE 7 as "Produces"
  — model may treat that as satisfying the gate predicate scope and write GATE 3 predicates
  referencing TABLE 7 only.

**R14 design hypothesis:** C-46 is predicate-content-specific, not format-specific or
axis-specific. The fix requires both GATE 3 predicate blocks to contain "TABLE 5", "TABLE 6",
and "TABLE 7" as distinct named tokens. This is independent of: whether surrounding
instructions are formal or conversational; whether Phase 3 has a checklist mandate; whether
TABLE 0 monitoring continuity is active; whether a mandate block enumerates the same tables
under "Produces." Expected: all five variations pass C-46 after the fix, across all N/A
adjustments.

**R13 retroactive C-46 scoring:**

| Variation | GATE 3 cleared names | Not-cleared names | C-46 |
|-----------|---------------------|-------------------|------|
| V-01 (conversational) | TABLE 7 only | TABLE 7 only | FAIL |
| V-02 (checklist) | TABLE 7 only | TABLE 7 only | FAIL |
| V-03 (TABLE 0 compressed) | TABLE 7 only | TABLE 7 only | FAIL |
| V-04 (format + register) | TABLE 7 only | TABLE 7 only | FAIL |
| V-05 (triple-axis) | TABLE 7 only | TABLE 7 only | FAIL |

---

## Round 14 Variation Map

| Variation | Axis | New criteria targeted | C-46 | Predicted score |
|-----------|------|-----------------------|------|----------------|
| V-01 | Single: C-46 baseline (formal, no overlay, no TABLE 0) | C-46 base | PASS | v13 ceiling |
| V-02 | Single: C-46 + phrasing register (conversational) | C-46 register-inertia | PASS | v13 ceiling |
| V-03 | Single: C-46 + output format (checklist mandate) | C-46 format-inertia | PASS | v13 ceiling |
| V-04 | Combined: C-46 + TABLE 0 + lifecycle emphasis | C-46 + C-44 co-inertia | PASS | v13 ceiling |
| V-05 | Combined: C-46 + triple-axis (TABLE 0 + mandate overlay + single-analyst) | C-46 + C-45 | PASS | v13 ceiling |

**Risk vectors for R14:**
- V-01: Absent a specific enforcement prompt, the model may revert to the R13 failure
  pattern and write GATE 3 as "TABLE 7 has >= 2 cascade pairs" only. Prompt mitigates by
  providing the complete GATE 3 predicate templates as required forms labeled with the C-46
  requirement before Phase 3.
- V-02: Conversational register may cause GATE 3 to be phrased as "check that all three
  tables have what they need" without naming each table. Prompt mitigates by providing
  explicit gate predicate block templates labeled "exact form required" and declaring that
  paraphrasing without named tables fails.
- V-03: Phase 3 checklist item 1 enumerates TABLE 5, TABLE 6, TABLE 7 — model may treat
  this as satisfying gate predicate coverage. Prompt mitigates by declaring the GATE 3
  predicate independent of the checklist enumeration and requiring named tables in both
  predicate blocks explicitly.
- V-04: Monitoring continuity acknowledgment at the Phase 3 boundary may reduce attention
  to GATE 3 predicate content. Prompt mitigates by providing the GATE 3 predicate template
  above the Phase 3 section with the three-table enumeration stated as a numbered rule.
- V-05: PHASE 3 MANDATE block enumerates "Produces: TABLE 5 — Burst Path Register;
  TABLE 6 — Retry-After Gaps; TABLE 7 — Cascade Risk Register" — model may rely on this
  and write a shorter GATE 3 predicate referencing TABLE 7 only. Prompt mitigates by
  declaring that the mandate block enumeration does not substitute for the GATE 3 predicate
  enumeration, and providing the GATE 3 predicate template with all three table names at
  both positions.

---

## V-01 — Single-Axis: C-46 Baseline (Formal Register, No Overlay, No TABLE 0)

**Axis:** C-46 baseline. Simplest single-analyst configuration: formal technical register,
no mandate overlay, no TABLE 0. All structural forms from the established flow-throttle
pattern preserved. GATE 3 carries the C-46 fix: both cleared and not-cleared predicate
blocks name TABLE 5, TABLE 6, and TABLE 7 explicitly by token. This is the minimum
necessary test of C-46 — does the three-table naming hold without any axis complexity?

**Hypothesis:** v13 ceiling. C-46 fires because both GATE 3 predicate blocks are provided
as required templates naming TABLE 5, TABLE 6, and TABLE 7 before Phase 3. C-39 fires
(single-analyst gate-arrival acknowledgments). C-42 fires (acknowledgments immediately after
`---`, before `##` heading). C-35, C-36, C-37, C-38, C-40, C-41, C-43, C-44, C-45 are N/A
(no overlay, no TABLE 0, no multi-role). N/A adjustment: aspirational denominator reduces
to /38 - 7 = /31 applicable. Risk vector: without a mandate overlay to "activate" C-35/C-38
enforcement, the model may treat GATE 3 as a simple "TABLE 7 complete" predicate. Prompt
mitigates by stating the C-46 three-table requirement explicitly before Phase 3 and providing
both predicate block templates verbatim.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
a rate-limited Power Automate system: trace where bottlenecks occur, which rate limits are
hit first, how backpressure propagates, and what the user experiences at each throttle tier.

**Gate-arrival acknowledgment (required — read before starting):**
Each phase after Phase 1 must open with a standalone acknowledgment line immediately after
the `---` separator and before any `##` heading, analytical content, or table:
- Before Phase 2: `*(GATE 1 cleared — proceed to Phase 2.)*`
- Before Phase 3: `*(GATE 2 cleared — proceed to Phase 3.)*`
- Before Phase 4: `*(GATE 3 cleared — proceed to Phase 4.)*`

This line is standalone. It does not appear inside a heading, after a heading, or as part
of an introductory paragraph. It is the first content token after `---`.

**GATE 3 predicate requirement — three tables required (read before starting):**
GATE 3 governs Phase 3, which produces three tables: TABLE 5 (burst-path enumeration),
TABLE 6 (Retry-After gaps), and TABLE 7 (cascade pairs). Both the cleared predicate block
and the not-cleared predicate block of GATE 3 must name TABLE 5, TABLE 6, and TABLE 7
explicitly by name as distinct tokens. A GATE 3 predicate block that says "all Phase 3
tables are complete" without naming each table fails this requirement. A GATE 3 predicate
that names TABLE 7 but does not name TABLE 5 or TABLE 6 in the same predicate block also
fails. Use the exact forms provided below for both predicate blocks.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 1 — Construct Inventory

Identify every throttle-relevant construct in this Power Automate flow. For each, fill a
row in TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain constraint:** PA construct type must be drawn from the following accepted terms:
Power Platform request entitlements, connector throttling policies, flow run concurrency
limits, action call limits, premium vs. standard connector tiers, Microsoft 365 service
protection limits. Generic labels such as "API limit" or "service limit" fail.

**Numeric limit column:** state the limit with its unit (requests/minute, runs/day, etc.).
"Varies" or a blank fails.

**Request contribution column:** calculate how many requests this construct contributes at
the scenario volume. Show the arithmetic.

**GATE 1** is cleared when and only when every TABLE 1 row carries (a) an exact PA construct
type from the accepted list, (b) a numeric limit with unit, and (c) a request contribution
estimate with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

Flag any failing row with `?` — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

*(GATE 1 cleared — proceed to Phase 2.)*

## PHASE 2 — Bottleneck, Propagation, and UX Analysis

### Section 2.A — Rate Limit Hit Ordering

Write the bottleneck statement using this template:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck. It
> saturates at [N req/unit-time] under this scenario because [reason the ordering holds at
> this volume]. The naive assumption that limits are independent fails here because [cascade
> chain or shared pool that makes them interact]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

For each row: explain why this construct hits before the next one at the scenario volume.
Showing the comparison numbers is required — "it's lower" without a numeric comparison fails.

### Section 2.B — Backpressure Hop Chain

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Trace at
least two hops. Continue until a terminal state: user-visible error, flow run failure, or
silent drop. Stopping before a terminal state fails.

### Section 2.C — User Experience per Throttle Tier

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Different
tiers must map to different categories. The user-visible experience column describes what
the user sees, not what the system does internally.

**GATE 2** is cleared when and only when: TABLE 3 has at least 2 complete hops with a
named terminal state; TABLE 4 has at least 2 tiers with distinct UX categories; TABLE 2
has a "why this order holds at scenario volume" explanation for each row.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 complete hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share the same UX category
- TABLE 2 has any row without a "why this order holds" explanation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

*(GATE 2 cleared — proceed to Phase 3.)*

## PHASE 3 — Exposure Analysis

### Section 3.A — Unprotected Burst Paths

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check each of the following burst-path patterns — if any apply, add a row to TABLE 5:
1. Apply to Each loop with no concurrency cap
2. Parallel branches with unbounded fan-out
3. High-frequency trigger with no debounce
4. Nested loops that multiply request volume
5. Batch-size misconfiguration that bursts at trigger

If none apply, write a one-sentence acknowledgment explaining why and name the guards
currently in place.

### Section 3.B — Retry-After Gap Analysis

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. Each mode must be described
distinctly. At least one gap is required. If every consumer honors Retry-After correctly,
state explicitly why with evidence.

### Section 3.C — Cascade Risk Pairs

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Find at least two cascade pairs. For each: name the mechanism that links Tier A to Tier B.
Tier A and Tier B must be different constructs. "Tier B is also throttled" without a
mechanism fails.

**GATE 3** is cleared when and only when: TABLE 5 has enumerated all applicable burst-path
patterns (or confirmed none with active guards listed); TABLE 6 has identified all
Retry-After gaps across applicable consumers (or explicitly confirmed all consumers honor
Retry-After with explanation); and TABLE 7 has at least 2 complete cascade pairs with all
required fields populated, named throttle mechanisms, and distinct Tier A / Tier B
constructs.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 5 is absent or omits an applicable burst-path pattern without acknowledgment
- TABLE 6 is absent or has any consumer row with unexamined Retry-After behavior
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A equal to Tier B
- Any TABLE 7 row is missing a stated throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

*(GATE 3 cleared — proceed to Phase 4.)*

## PHASE 4 — Synthesis and PA Validation

### Section 4.A — PA Construct Validation

Review every construct in TABLE 1. For each row, write one of:
- `[PASS: confirmed]` — the name is the exact documented PA term
- `[FAIL: corrected below]` — the name requires correction

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL]` row: write the corrected construct name, the source, and the correction
reason immediately below the `[FAIL]` annotation, before the next row.

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have corrected construct name, correction reason, and
  precision note immediately below its `[FAIL]` annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

### Section 4.B — UX Category Validation

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior. Internal
system behavior is not user experience — correct any row that describes a system action
rather than a user-visible outcome.

### Section 4.C — Quantified Risk Register

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Status must be derived arithmetically from
the limit and projected volume. Show arithmetic for at least one row.

### Section 4.D — PA-Specific Remediations

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations, each cross-referenced to a finding from Phases 2–3
by section label (e.g., 3.B, 3.C). Generic remediations without PA feature names or
finding cross-reference fail.

### Section 4.E — Monitoring Signals

Name at least one PA-observable signal. State the condition it surfaces and when it fires.
Name the specific PA tooling surface: flow run history, connector call telemetry in Power
Platform admin center, request usage dashboard, or equivalent. "Set up alerting" without
naming the tool fails.

### Section 4.F — License and Entitlement Boundary

Name at least one entitlement boundary where the throttle limit materially differs. State
whether crossing it shifts any TABLE 9 row from SAFE to OVER-LIMIT or vice versa.

### Section 4.G — Test Approach

Describe at least one concrete test step using a named PA tool and method. "Test in staging"
without naming the tool or method fails.

---

*End of V-01 prompt body.*

---

## V-02 — Single-Axis: C-46 + Phrasing Register (Conversational/Imperative) — C-46 Register-Inertia

**Axis:** Phrasing register variation. The prompt uses conversational, imperative register
throughout the analytical instructions: direct commands and plain-language explanations
rather than formal technical declaratives. Examples: "Find everything in this flow with a
rate cap" rather than "Identify every throttle-relevant construct"; "Show why this one
hits first — use the numbers" rather than "include a rationale column with ordering
explanation"; "Trace until the user feels it" rather than "trace until terminal state."
Gate names, table column headers, gate-predicate language, section labels, and structural
requirement forms are preserved exactly, including the C-46 GATE 3 template naming TABLE 5,
TABLE 6, and TABLE 7 in both predicate blocks. Single analyst; no overlay; no TABLE 0.

**Hypothesis:** v13 ceiling. C-46 fires because the GATE 3 predicate structure is preserved
in the template regardless of conversational register in the analytical prose surrounding
it. The table names TABLE 5, TABLE 6, TABLE 7 appear as tokens in the gate predicate block
regardless of how the instructions phrase the analytical tasks. C-39 fires (gate-arrival
acknowledgments). C-42 fires (acknowledgments immediately after `---`). C-35, C-36, C-37,
C-38, C-40, C-41, C-43, C-44, C-45 are N/A (no overlay, no TABLE 0). Risk vector:
conversational register in Phase 3 section headers ("Find the burst paths", "Where 429s
aren't being handled") may induce an equally conversational GATE 3 predicate ("check that
all three tables have what they need") without the named table tokens. Prompt mitigates
by providing the exact GATE 3 predicate blocks as labeled templates ("GATE 3 predicate —
exact form required") and stating that paraphrasing the table names fails.

---

You are a Connectors / Power Automate throughput expert. Your job: trace the throttle risk
in a Power Automate flow — find where it breaks first, how far the damage spreads, and what
the user actually experiences.

**Gate-arrival acknowledgment (read this before you start):**
After each gate clears, the next phase starts with a standalone acknowledgment line — the
very first thing after the `---` separator, before any heading, before any content.

Required forms:
- Before Phase 2: `*(GATE 1 cleared — proceed to Phase 2.)*`
- Before Phase 3: `*(GATE 2 cleared — proceed to Phase 3.)*`
- Before Phase 4: `*(GATE 3 cleared — proceed to Phase 4.)*`

Don't put this inside a heading ("## Phase 2 (GATE 1 cleared)"). Don't put it after a
heading. First line, standalone, before anything else.

**GATE 3 predicate — exact form required (read before you start):**
GATE 3 covers all three tables from Phase 3: TABLE 5 (burst paths), TABLE 6 (Retry-After
gaps), TABLE 7 (cascade pairs). The gate predicate blocks below are the required form — use
the exact table names. Do not paraphrase with "all three Phase 3 tables" or "everything from
Phase 3." TABLE 5, TABLE 6, and TABLE 7 must appear as distinct named tokens in both the
cleared and not-cleared predicate blocks.

Cleared form (use exactly):
> GATE 3 is cleared when and only when: TABLE 5 has enumerated all applicable burst-path
> patterns (or confirmed none with active guards listed); TABLE 6 has identified all
> Retry-After gaps across applicable consumers (or confirmed all consumers honor Retry-After
> with explicit explanation); and TABLE 7 has >= 2 complete cascade pairs with all required
> fields populated, named throttle mechanisms, and distinct Tier A / Tier B constructs.

Not-cleared form (use exactly):
> GATE 3 is not cleared when any of the following failure states are present:
> - TABLE 5 is absent or omits an applicable burst-path pattern without acknowledgment
> - TABLE 6 is absent or has any consumer row with unexamined Retry-After behavior
> - TABLE 7 has fewer than 2 cascade pairs
> - Any TABLE 7 row has Tier A equal to Tier B
> - Any TABLE 7 row is missing a named throttle mechanism
> - Any TABLE 7 row is missing a severity or duration assessment

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 1 — Find Everything That Has a Rate Cap

Your first job: find every construct in this flow that has a rate limit, a concurrency cap,
or a throttle policy. Don't generalize — name each one precisely.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

For **PA construct type**: use the exact term from PA docs. Accepted terms only: Power
Platform request entitlements, connector throttling policies, flow run concurrency limits,
action call limits, premium vs. standard connector tiers, Microsoft 365 service protection
limits. Writing "API limit" or "rate limit" fails.

For **numeric limit**: give the actual limit with the unit — requests per minute, runs per
day, etc. "Varies" fails.

For **request contribution**: calculate how many requests this construct adds at the scenario
volume. Show the math.

**GATE 1** is cleared when and only when every TABLE 1 row has (a) an exact PA construct
type, (b) a numeric limit with unit, and (c) a request contribution with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution with arithmetic shown

Flag any failing row with `?` — fix it before moving on.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

*(GATE 1 cleared — proceed to Phase 2.)*

## PHASE 2 — Figure Out Which One Breaks First and Trace the Damage

### Section 2.A — Which Limit Hits First

Write the bottleneck statement using this template:

> "[Component] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] because [one reason the ordering holds at this volume]. The naive
> assumption that limits are independent fails here because [the cascade or shared pool
> that links them]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

For the "why" column: explain why this construct hits before the next one. Show the numbers.

### Section 2.B — How the Pressure Travels

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Trace at
least two hops. Keep going until something the user or flow actually sees: user-visible
error, flow failure, silent drop. Don't stop in the middle of the chain.

### Section 2.C — What Does the User See

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss. Different
tiers must use different categories. Describe what the user sees, not what the system does.

**GATE 2** is cleared when and only when: TABLE 3 has at least 2 hops with a named terminal
state; TABLE 4 has at least 2 tiers with distinct UX categories; TABLE 2 has a "why this
order holds" explanation for each row.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or two tiers share a UX category
- TABLE 2 has any row without a "why this order holds" explanation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

*(GATE 2 cleared — proceed to Phase 3.)*

## PHASE 3 — Find the Exposure Points

### Section 3.A — Unprotected Burst Paths

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check each of these patterns — if any apply, add a row:
1. Apply to Each loop with no concurrency cap
2. Parallel branches with unbounded fan-out
3. High-frequency trigger with no debounce
4. Nested loops that multiply request volume
5. Batch-size misconfiguration that bursts at trigger

If none apply, explain why in one sentence and name the guards currently in place.

### Section 3.B — Where 429s Aren't Being Handled

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. You need at least one gap.
If every consumer handles 429s correctly, explain why explicitly.

### Section 3.C — Pairs That Can Take Each Other Down

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Find at least two cascade pairs. Name the mechanism linking Tier A to Tier B. Tier A and
Tier B must be different constructs.

**GATE 3** is cleared when and only when: TABLE 5 has enumerated all applicable burst-path
patterns (or confirmed none with active guards listed); TABLE 6 has identified all
Retry-After gaps across applicable consumers (or explicitly confirmed all consumers honor
Retry-After with explanation); and TABLE 7 has >= 2 complete cascade pairs with all
required fields populated, named throttle mechanisms, and distinct Tier A / Tier B
constructs.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 5 is absent or omits an applicable burst-path pattern without acknowledgment
- TABLE 6 is absent or has any consumer row with unexamined Retry-After behavior
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A equal to Tier B
- Any TABLE 7 row is missing a named throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

*(GATE 3 cleared — proceed to Phase 4.)*

## PHASE 4 — Validate, Quantify, and Fix

### Section 4.A — Check Every Construct Name

Go through every row in TABLE 1. For each one, write:
- `[PASS: confirmed]` — exact documented PA term
- `[FAIL: corrected below]` — needs correction

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

For any `[FAIL]`: write the corrected name, the source, and why the original was wrong
immediately below the `[FAIL]` annotation — before the next row.

**CORRECTION GATE** is cleared when and only when every TABLE 8 row has a disposition and
every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row is missing corrected content immediately below its annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

### Section 4.B — Check the UX Categories

Review TABLE 4. Confirm or correct each UX category. Internal system behavior is not user
experience — fix anything that describes a system action rather than what the user sees.

### Section 4.C — Throttle Budget

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status: SAFE / MARGINAL / OVER-LIMIT. Show the math for at least one row.

### Section 4.D — PA Fixes

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

At least two PA-native fixes. Each maps to a finding from Phases 2–3 by section label.
Generic fixes without PA feature names fail.

### Section 4.E — Monitoring Signals

At least one PA-observable signal. Name the trigger condition and the PA tooling surface.
"Set up alerting" without naming the tool fails.

### Section 4.F — License and Entitlement Boundary

Name at least one entitlement boundary. State whether crossing it shifts a TABLE 9 row
status from SAFE to OVER-LIMIT or vice versa.

### Section 4.G — Test Approach

One concrete test step with a named PA tool and method.

---

*End of V-02 prompt body.*

---

## V-03 — Single-Axis: C-46 + Output Format (Checklist Mandate) — C-46 Format-Inertia

**Axis:** Output format variation. Phase mandate blocks are expressed as numbered checklists
rather than blockquote headers. Each phase opens with a **Phase N Checklist** containing:
(1) what this phase produces, (2) which gate closes it, (3) "Completing this checklist does
NOT substitute for the [GATE N] declaration at the end of this phase." Phase 3 checklist
item 1 enumerates "TABLE 5 — Burst Path Register; TABLE 6 — Retry-After Gaps;
TABLE 7 — Cascade Risk Register." GATE 3 independently names all three tables in both
predicate blocks (C-46). Single analyst; checklist overlay present (C-35, C-38, C-43);
no TABLE 0.

**Hypothesis:** v13 ceiling. C-46 fires because the GATE 3 predicate template is declared
independently of the Phase 3 checklist — the checklist item 1 enumeration does not satisfy
the gate predicate requirement. Both predicate blocks carry TABLE 5, TABLE 6, and TABLE 7
as named tokens. C-43 fires (positional qualifier "at the end of this phase" in checklist
item 3 and standalone parenthetical at both positions). C-38 fires (dual-placement). C-39
fires (gate-arrival acknowledgments). C-42 fires (acknowledgments immediately after `---`
and before checklist). C-37, C-40, C-44, C-45 are N/A (no TABLE 0). Risk vector: Phase 3
checklist item 1 already enumerates TABLE 5, TABLE 6, TABLE 7 — model may abbreviate GATE 3
predicate to "TABLE 7 complete" because the other tables appear in the checklist. Prompt
mitigates by explicitly declaring the gate predicate is independent of the checklist
enumeration and requiring all three table names as distinct tokens in both predicate blocks.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system.

**Output format — Phase checklists:** Each phase opens with a numbered phase checklist
before the analytical content. The checklist states what this phase must produce, which
gate closes it, and a non-substitution declaration.

**Checklist item 3 form (required in every phase checklist):**
Item 3 must read: "Non-substitution: Completing this checklist does NOT substitute for
the [GATE N] declaration at the end of this phase."
The phrase **at the end of this phase** is required. Dropping it or replacing it with
"below" fails the gate positional qualifier requirement for that phase.

**Pre-gate parenthetical form (required immediately before every gate declaration):**
A standalone italicized line immediately before each gate declaration:
`*(This phase checklist does NOT substitute for the [GATE N] declaration at the end of this phase.)*`
The phrase **at the end of this phase** is required here as well.

**Phase-arrival acknowledgment form (required):** Each phase after Phase 1 opens with the
gate-arrival acknowledgment as the first standalone line after `---` — before the phase
checklist and before any `##` section heading:
- Phase 2 opens with: `*(GATE 1 cleared — proceed to Phase 2.)*`
- Phase 3 opens with: `*(GATE 2 cleared — proceed to Phase 3.)*`
- Phase 4 opens with: `*(GATE 3 cleared — proceed to Phase 4.)*`

**Sequence within each post-Phase-1 phase:**
1. Gate-arrival acknowledgment (immediately after `---`, before checklist)
2. Phase checklist (items 1–3, item 3 includes the positional qualifier)
3. Analytical content and tables
4. Pre-gate parenthetical (standalone, includes positional qualifier)
5. Gate declaration

**GATE 3 predicate — independent of Phase 3 checklist (read before writing Phase 3):**
Phase 3 checklist item 1 enumerates TABLE 5, TABLE 6, and TABLE 7 under "Produces." The
GATE 3 gate predicate must independently name TABLE 5, TABLE 6, and TABLE 7 in both its
cleared and not-cleared predicate blocks. The checklist enumeration does not substitute for
the gate predicate enumeration. A GATE 3 predicate that references only TABLE 7 fails even
if TABLE 5 and TABLE 6 appear in the Phase 3 checklist item 1.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 1 — Construct Inventory

**Phase 1 Checklist:**
1. Produces: TABLE 1 — Throttle Tier Map
2. Gate that closes this phase: GATE 1
3. Non-substitution: Completing this checklist does NOT substitute for the GATE 1
   declaration at the end of this phase.

Identify every throttle-relevant construct in the flow. Fill TABLE 1.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

**Domain constraint:** PA construct type must be drawn from: Power Platform request
entitlements, connector throttling policies, flow run concurrency limits, action call
limits, premium vs. standard connector tiers, Microsoft 365 service protection limits.
Generic labels fail.

*(This phase checklist does NOT substitute for the GATE 1 declaration at the end of this phase.)*

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type from the domain list, (b) a numeric limit with unit, and (c) a request
contribution estimate with arithmetic shown.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a generic or undocumented construct type
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

Flag any failing row with `?` — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

*(GATE 1 cleared — proceed to Phase 2.)*

## PHASE 2 — Bottleneck, Propagation, and UX Analysis

**Phase 2 Checklist:**
1. Produces: TABLE 2 — Hit Order; TABLE 3 — Backpressure Propagation; TABLE 4 — UX Map
2. Gate that closes this phase: GATE 2
3. Non-substitution: Completing this checklist does NOT substitute for the GATE 2
   declaration at the end of this phase.

### Section 2.A — Rate Limit Hit Ordering

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason]. The naive
> assumption that limits are independent fails here because [cascade chain or shared pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

### Section 2.B — Backpressure Hop Chain

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace to terminal state (user-visible error, flow run failure, or silent drop).

### Section 2.C — User Experience per Throttle Tier

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers. Describe the user-visible experience, not the
internal system action.

*(This phase checklist does NOT substitute for the GATE 2 declaration at the end of this phase.)*

**GATE 2** is cleared when and only when: TABLE 3 has >= 2 complete hops with a named
terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has a "why
this order holds" explanation for each row.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 complete hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share the same UX category
- TABLE 2 has any row without a "why this order holds" explanation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

*(GATE 2 cleared — proceed to Phase 3.)*

## PHASE 3 — Exposure Analysis

**Phase 3 Checklist:**
1. Produces: TABLE 5 — Burst Path Register; TABLE 6 — Retry-After Gaps;
   TABLE 7 — Cascade Risk Register
2. Gate that closes this phase: GATE 3
3. Non-substitution: Completing this checklist does NOT substitute for the GATE 3
   declaration at the end of this phase.

### Section 3.A — Unprotected Burst Paths

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out,
high-frequency trigger with no debounce, nested loops, batch-size misconfigurations.
If none found, write explicit acknowledgment with guards in place.

### Section 3.B — Retry-After Gap Analysis

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.
If every consumer honors Retry-After, state explicitly why.

### Section 3.C — Cascade Risk Pairs

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them.

*(This phase checklist does NOT substitute for the GATE 3 declaration at the end of this phase.)*

**GATE 3** is cleared when and only when: TABLE 5 has enumerated all applicable burst-path
patterns (or confirmed none with active guards listed); TABLE 6 has identified all
Retry-After gaps across applicable consumers (or explicitly confirmed all consumers honor
Retry-After with explanation); and TABLE 7 has >= 2 complete cascade pairs with all
required fields populated, named throttle mechanisms, and distinct Tier A / Tier B
constructs.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 5 is absent or omits an applicable burst-path pattern without acknowledgment
- TABLE 6 is absent or has any consumer row with unexamined Retry-After behavior
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A equal to Tier B
- Any TABLE 7 row is missing a stated throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

*(GATE 3 cleared — proceed to Phase 4.)*

## PHASE 4 — Synthesis and PA Validation

**Phase 4 Checklist:**
1. Produces: TABLE 8 — PA Construct Precision Pass; TABLE 9 — Throttle Budget;
   TABLE 10 — Remediations; Sections 4.B through 4.G
2. Gate that closes this phase: CORRECTION GATE
3. Non-substitution: Completing this checklist does NOT substitute for the CORRECTION
   GATE declaration at the end of Section 4.A.

### Section 4.A — PA Construct Validation

Review every construct in TABLE 1. Mark either `[PASS: confirmed]` or
`[FAIL: corrected below]`. For any `[FAIL]`, write corrected construct name, limit source,
and precision note immediately below the annotation.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

*(This phase checklist does NOT substitute for the CORRECTION GATE declaration at the end of Section 4.A.)*

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have corrected content immediately below its annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

### Section 4.B — UX Validation

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior. Internal
system behavior is not user experience.

### Section 4.C — Quantified Risk Register

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

### Section 4.D — PA-Specific Remediations

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to findings by section label.

### Section 4.E — Monitoring Signals

Name at least one PA-observable signal with trigger condition and PA tooling surface.

### Section 4.F — License and Entitlement Boundary

Name at least one entitlement boundary with SAFE ↔ OVER-LIMIT shift statement.

### Section 4.G — Test Approach

One concrete PA-tooling test step with named tool and method.

---

*End of V-03 prompt body.*

---

## V-04 — Combined: C-46 + TABLE 0 + Lifecycle Emphasis — C-46 + C-44 Co-Inertia

**Axis:** Two-axis combination. (1) C-46 fix in GATE 3 (both predicate blocks name TABLE 5,
TABLE 6, TABLE 7). (2) Lifecycle emphasis: TABLE 0 present in Phase 1 (C-37 trigger); single-
analyst gate-arrival acknowledgments carry monitoring continuity clause (C-44). No mandate
overlay (C-38, C-43 N/A). Tests whether C-46 holds when TABLE 0 monitoring scope adds a
continuity obligation to the Phase 3 boundary and GATE 1 scope isolation is active.

**Hypothesis:** v13 ceiling. C-46 fires because GATE 3 names TABLE 5, TABLE 6, and TABLE 7
in both predicate blocks, independent of the monitoring continuity clause. C-44 fires
(gate-arrival acknowledgments carry TABLE 0 continuity clause). C-37 fires (GATE 1 scope
isolation sentence). C-39 fires (single-analyst acknowledgments). C-42 fires (acknowledgments
immediately after `---`). C-40 fires (TABLE 11 three-value vocabulary in Section 4.E).
C-35, C-36, C-38, C-41, C-43, C-45 are N/A (no overlay, no multi-role). Risk vector: the
monitoring continuity acknowledgment at the Phase 3 boundary (`GATE 2 cleared — TABLE 0
monitoring carries into Phase 3`) may reduce the model's attention to GATE 3 predicate
content, reverting to TABLE 7 only. Prompt mitigates by providing the GATE 3 predicate
template above Phase 3 with the three-table enumeration declared as a numbered requirement
separate from the continuity acknowledgment.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system. This analysis is observability-anchored: declare the
monitoring signals active or available before mapping throttle constructs.

**Monitoring continuity acknowledgment form (required — read before starting):**
Because TABLE 0 monitoring scope established in Phase 1 carries forward through all phases,
each gate-arrival acknowledgment must confirm continuity. Use this form at each phase
opening, immediately after `---` and before any `##` heading:
- Phase 2 opens with: `*(GATE 1 cleared — TABLE 0 monitoring carries into Phase 2.)*`
- Phase 3 opens with: `*(GATE 2 cleared — TABLE 0 monitoring carries into Phase 3.)*`
- Phase 4 opens with: `*(GATE 3 cleared — TABLE 0 monitoring carries into Phase 4.)*`

This acknowledgment is the first standalone line after `---`, before any `##` heading. It
applies regardless of Phase 1 instruction depth or Phase 3 predicate content.

**Monitoring signal classification vocabulary (required in Section 4.E, minimum three
signals):**
- `active` — signal is present and operational in TABLE 0
- `inactive but available` — signal is in TABLE 0 but not currently running
- `newly recommended` — signal is not in TABLE 0; requires new instrumentation

**GATE 3 predicate — three-table enumeration required (read before starting):**
GATE 3 governs Phase 3, which produces TABLE 5 (burst-path enumeration), TABLE 6
(Retry-After gaps), and TABLE 7 (cascade pairs). Both predicate blocks of GATE 3 must name
TABLE 5, TABLE 6, and TABLE 7 explicitly as distinct tokens. Paraphrasing ("all Phase 3
tables" or "all three tables") fails. The monitoring continuity acknowledgment at the Phase
3 boundary does not affect this requirement — the gate predicate is independent of the
acknowledgment.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 1 — Construct and Observability Inventory

### Section 1.0 — Monitoring Baseline

**TABLE 0 — Active and Available Signals**

| Signal name | PA tooling surface | What it measures | TABLE 0 status (active / inactive / unknown) |
|-------------|-------------------|-----------------|----------------------------------------------|

Include: flow run throttle/failure status (flow run history), connector call telemetry
(Power Platform admin center), request usage dashboard. List inactive or unknown signals;
do not omit them.

### Section 1.1 — Throttle Construct Inventory

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

Use the exact documented PA construct type. Include unit in numeric limit. Show arithmetic
in request contribution. Accepted types: Power Platform request entitlements, connector
throttling policies, flow run concurrency limits, action call limits, premium vs. standard
connector tiers, Microsoft 365 service protection limits.

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type, (b) a numeric limit with unit, and (c) a request contribution with
arithmetic shown. GATE 1 governs TABLE 1 only; TABLE 0 requirements are governed by the
Section 1.0 entry condition above.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a construct type not on the accepted list
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution with arithmetic shown

*PHASE 2 is blocked until GATE 1 is cleared.*

---

*(GATE 1 cleared — TABLE 0 monitoring carries into Phase 2.)*

## PHASE 2 — Bottleneck, Propagation, and UX Analysis

### Section 2.A — Rate Limit Hit Ordering

Write the bottleneck statement:

> "[Component] at [PA construct type] is the binding bottleneck. It saturates at
> [N req/unit-time] under this scenario because [reason]. The naive assumption that limits
> are independent fails here because [cascade or shared pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

### Section 2.B — Backpressure Hop Chain

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum
two hops. Trace to terminal state.

### Section 2.C — User Experience per Throttle Tier

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers.

**GATE 2** is cleared when and only when: TABLE 3 has >= 2 complete hops with a named
terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has a "why
this order holds" explanation for each row.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share a UX category
- TABLE 2 has any row without a "why this order holds" explanation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

*(GATE 2 cleared — TABLE 0 monitoring carries into Phase 3.)*

## PHASE 3 — Exposure Analysis

### Section 3.A — Unprotected Burst Paths

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out,
high-frequency trigger with no debounce, nested loops, batch-size misconfigurations.
If none found, write explicit acknowledgment with guards in place.

### Section 3.B — Retry-After Gap Analysis

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

### Section 3.C — Cascade Risk Pairs

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them.

**GATE 3** is cleared when and only when: TABLE 5 has enumerated all applicable burst-path
patterns (or confirmed none with active guards listed); TABLE 6 has identified all
Retry-After gaps across applicable consumers (or explicitly confirmed all consumers honor
Retry-After with explanation); and TABLE 7 has >= 2 complete cascade pairs with all
required fields populated, named throttle mechanisms, and distinct Tier A / Tier B
constructs.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 5 is absent or omits an applicable burst-path pattern without acknowledgment
- TABLE 6 is absent or has any consumer row with unexamined Retry-After behavior
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A equal to Tier B
- Any TABLE 7 row is missing a stated throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

*(GATE 3 cleared — TABLE 0 monitoring carries into Phase 4.)*

## PHASE 4 — Synthesis and PA Validation

### Section 4.A — PA Construct Validation

Review every construct in TABLE 1. Mark `[PASS: confirmed]` or `[FAIL: corrected below]`.
For any `[FAIL]`, write corrected construct name, limit source, and precision note
immediately below the annotation.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have corrected content immediately below its annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

### Section 4.B — UX Validation

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior.

### Section 4.C — Quantified Risk Register

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

### Section 4.D — PA-Specific Remediations

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to findings from PHASES 2–3 by section label.

### Section 4.E — Monitoring Signals (Extended — TABLE 0 cross-reference required, minimum three signals)

Classify at least three monitoring signals by TABLE 0 status:

**TABLE 11 — Monitoring Signal Classification**

| Signal name | TABLE 0 status | PA tooling surface | Trigger condition | Missed-signal gap? |
|-------------|---------------|-------------------|------------------|--------------------|

For each signal:
- **TABLE 0 status** (required): `active` / `inactive but available` / `newly recommended`
- **PA tooling surface** (required): name the exact surface — flow run history, connector
  call telemetry in Power Platform admin center, request usage dashboard, or equivalent.
  Generic "set up alerting" fails.
- **Trigger condition** (required): state what value or event causes the signal to fire.
- **Missed-signal gap**: for any `inactive but available` signal — state whether it would
  have detected the Phase 2 bottleneck. If yes, flag with the TABLE 0 row name.

At least one TABLE 0 entry (active or inactive) must be referenced. At least one
`newly recommended` signal must be present.

### Section 4.F — License and Entitlement Boundary

Name at least one entitlement boundary with an explicit SAFE ↔ OVER-LIMIT shift statement.

### Section 4.G — Test Approach

Describe at least one concrete PA-tooling test step naming the tool and method.

---

*End of V-04 prompt body.*

---

## V-05 — Combined: C-46 + Triple-Axis (TABLE 0 + Mandate Overlay + Single-Analyst) — C-46 + C-45 Sequence Integrity

**Axis:** Full triple-axis combination from R13 V-05 with C-46 fix applied. (1) TABLE 0
present (C-37, C-44 trigger). (2) Mandate overlay (blockquote form) at each phase (C-35,
C-38, C-43). (3) Single-analyst gate-arrival acknowledgments (C-39, C-42). C-46 fix: GATE 3
names TABLE 5, TABLE 6, TABLE 7 in both predicate blocks within the five-element
phase-transition sequence. Tests whether C-45 sequence integrity is preserved when GATE 3
must also enumerate three tables in both predicates.

**Hypothesis:** v13 ceiling. C-46 fires because the GATE 3 predicate template is declared
independently of the PHASE 3 MANDATE block — the mandate block's "Produces" enumeration
does not satisfy the gate predicate requirement. C-45 fires because the five-element
sequence (TABLE 0 ref → mandate → standalone non-sub parenthetical → gate declaration
→ continuity acknowledgment after `---`) is preserved with the C-46 fix at each boundary.
C-44 fires (continuity clause). C-42 fires (acknowledgments after `---`). C-43 fires
(positional qualifier at both positions). C-38 fires (dual-placement). C-37 fires (GATE 1
scope isolation). C-40 fires (TABLE 11 three-value vocabulary). Risk vector: PHASE 3
MANDATE block produces "TABLE 5 — Burst Path Register; TABLE 6 — Retry-After Gaps;
TABLE 7 — Cascade Risk Register" — model may treat that enumeration as satisfying GATE 3
table coverage and write the gate predicate as "TABLE 7 complete" only. Prompt mitigates by
explicitly declaring that the mandate "Produces" list does not substitute for the gate
predicate enumeration and providing the GATE 3 predicate template verbatim with all three
table names at both predicate block positions.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across
a rate-limited Power Automate system.

**Phase-transition sequence rule (governs every phase boundary):**

At each phase boundary, the structural elements must appear in this exact order:

**Sending-phase side (end of Phase N):**
1. TABLE 0 inventory reference or scope note (in Phase 1 this is TABLE 0 itself; in
   Phases 2–3 this is the mandate block's TABLE 0 scope reference)
2. PHASE MANDATE block — contains the internal non-substitution statement:
   "Completing this mandate block does NOT substitute for the [GATE N] declaration
   at the end of this phase."
3. Standalone non-substitution parenthetical immediately before the gate:
   "*(The PHASE N MANDATE block above does NOT substitute for the gate declaration
   at the end of this phase.)*"
4. Gate declaration (last element before `---`)

**Receiving-phase side (start of Phase N+1, after `---`):**
5. Gate-cleared acknowledgment with TABLE 0 monitoring continuity clause — first
   standalone content line after `---`, before any `##` heading or mandate block

Any inversion of this order fails C-45 for that phase boundary.

**Non-substitution form (required at both positions per phase):**
- Position 1 (inside PHASE MANDATE block): "Completing this mandate block does NOT
  substitute for the [GATE N] declaration at the end of this phase."
- Position 2 (standalone parenthetical before gate): "*(The PHASE N MANDATE block above
  does NOT substitute for the gate declaration at the end of this phase.)*"
The phrase **at the end of this phase** is required at both positions.

**Gate-cleared acknowledgment form with continuity clause (required):**
- Phase 2 opens with: `*(GATE 1 cleared — TABLE 0 monitoring carries into Phase 2.)*`
- Phase 3 opens with: `*(GATE 2 cleared — TABLE 0 monitoring carries into Phase 3.)*`
- Phase 4 opens with: `*(GATE 3 cleared — TABLE 0 monitoring carries into Phase 4.)*`

**Monitoring signal classification vocabulary (required in Section 4.E, minimum three
signals):**
- `active` — present and operational in TABLE 0
- `inactive but available` — listed in TABLE 0, not currently running
- `newly recommended` — not in TABLE 0; new instrumentation required

**GATE 3 predicate — three-table enumeration required, independent of PHASE 3 MANDATE
(read before writing Phase 3):**
The PHASE 3 MANDATE block lists "Produces: TABLE 5 — Burst Path Register; TABLE 6 —
Retry-After Gaps; TABLE 7 — Cascade Risk Register." This mandate enumeration does NOT
satisfy the GATE 3 predicate requirement. The GATE 3 gate predicate must independently
name TABLE 5, TABLE 6, and TABLE 7 in both its cleared and not-cleared predicate blocks.
A GATE 3 predicate that names only TABLE 7, or that defers to "all tables produced in
Phase 3," fails even if TABLE 5 and TABLE 6 appear in the PHASE 3 MANDATE block.

**Inputs:** Topic: `{{topic}}` | Signal: `{{signal}}`

**Artifact output path:** `simulations/flow/throttle/{{topic}}-throttle-{{date}}.md`

---

## PHASE 1 — Construct and Observability Inventory

### Section 1.0 — Observability Baseline (entry condition: complete before TABLE 1)

Declare the monitoring signals currently active or available for this flow. Include inactive
or unknown signals.

**TABLE 0 — Active and Available Signals**

| Signal name | PA tooling surface | What it measures | TABLE 0 status (active / inactive / unknown) |
|-------------|-------------------|-----------------|----------------------------------------------|

Required entries: flow run throttle/failure status (flow run history), connector call
telemetry (Power Platform admin center), request usage dashboard. Section 4.E must classify
every recommended signal relative to this TABLE 0 inventory.

> **PHASE 1 MANDATE**
> - Produces: TABLE 1 — Throttle Tier Map
> - Gate that closes this phase: GATE 1
> - TABLE 0 scope: TABLE 0 monitoring baseline established in Section 1.0 carries forward
>   through all phases; each phase boundary carries an explicit continuity acknowledgment.
> - Obligation: every TABLE 1 row must carry an exact PA construct type from the accepted
>   list, a numeric limit with unit, and a request contribution estimate with arithmetic.
> - Non-substitution: Completing this mandate block does NOT substitute for the GATE 1
>   declaration at the end of this phase.

### Section 1.1 — Throttle Construct Inventory

Fill TABLE 1. PA construct type must be an exact documented term.

**TABLE 1 — Throttle Tier Map**

| Construct | PA construct type | Numeric limit | Request contribution at scenario volume | Retry-After read? (yes / no / N/A) |
|-----------|------------------|---------------|----------------------------------------|------------------------------------|
| (fill) | (exact PA term) | (N req/unit) | (estimate with arithmetic) | |

Accepted PA construct types: Power Platform request entitlements, connector throttling
policies, flow run concurrency limits, action call limits, premium vs. standard connector
tiers, Microsoft 365 service protection limits. Generic labels fail.

*(The PHASE 1 MANDATE block above does NOT substitute for the gate declaration at the end of this phase.)*

**GATE 1** is cleared when and only when every TABLE 1 row satisfies (a) an exact PA
construct type from the accepted list, (b) a numeric limit with unit, and (c) a request
contribution estimate with arithmetic shown. GATE 1 governs TABLE 1 only; TABLE 0
requirements are governed by the Section 1.0 entry condition above.

**GATE 1 is not cleared when any of the following failure states are present:**
- Any TABLE 1 row uses a construct type not on the accepted list
- Any TABLE 1 row is missing a numeric limit with unit
- Any TABLE 1 row is missing a request contribution estimate with arithmetic shown

Rows in any of the above failure states receive a `?` flag — correct before proceeding.
*PHASE 2 is blocked until GATE 1 is cleared.*

---

*(GATE 1 cleared — TABLE 0 monitoring carries into Phase 2.)*

> **PHASE 2 MANDATE**
> - Produces: TABLE 2 — Hit Order; TABLE 3 — Backpressure Propagation; TABLE 4 — UX Map
> - Gate that closes this phase: GATE 2
> - TABLE 0 scope: Section 1.0 TABLE 0 remains the active monitoring baseline; no new
>   entries at this boundary.
> - Obligations: TABLE 3 must have >= 2 hops with a named terminal state; TABLE 4 must
>   have >= 2 tiers with distinct UX categories; TABLE 2 must have ordering rationale
>   per row.
> - Non-substitution: Completing this mandate block does NOT substitute for the GATE 2
>   declaration at the end of this phase.

## PHASE 2 — Bottleneck, Propagation, and UX Analysis

### Section 2.A — Rate Limit Hit Ordering

Write the bottleneck statement:

> "[Specific PA construct component] at [PA construct type] is the binding bottleneck.
> It saturates at [N req/unit-time] under this scenario because [reason]. The naive
> assumption that limits are independent fails here because [cascade chain or shared pool]."

**TABLE 2 — Hit Order**

| Hit order | Construct (from TABLE 1) | Limit | Why this order holds at scenario volume |
|-----------|--------------------------|-------|-----------------------------------------|
| 1 (bottleneck) | | | |
| 2 | | | |

### Section 2.B — Backpressure Hop Chain

**TABLE 3 — Backpressure Propagation**

| From component | Signal emitted | Signal type | To component | Response behavior |
|----------------|---------------|-------------|--------------|-------------------|

Signal types: error code / retry-after header / queue depth increase / other. Minimum:
two hops. Trace until terminal state.

### Section 2.C — User Experience per Throttle Tier

**TABLE 4 — UX Map**

| Throttle tier | System action (internal) | User-visible experience | UX category |
|---------------|--------------------------|------------------------|-------------|

UX categories: transparent-retry / visible-delay / error-surfaced / silent-loss.
Categories MUST differ across tiers.

*(The PHASE 2 MANDATE block above does NOT substitute for the gate declaration at the end of this phase.)*

**GATE 2** is cleared when and only when: TABLE 3 has >= 2 complete hops with a named
terminal state; TABLE 4 has >= 2 tiers with distinct UX categories; TABLE 2 has a "why
this order holds" explanation for each row.

**GATE 2 is not cleared when any of the following failure states are present:**
- TABLE 3 has fewer than 2 complete hops, or is missing a named terminal state
- TABLE 4 has fewer than 2 tiers, or any two tiers share the same UX category
- TABLE 2 has any row without a "why this order holds" explanation

*PHASE 3 is blocked until GATE 2 is cleared.*

---

*(GATE 2 cleared — TABLE 0 monitoring carries into Phase 3.)*

> **PHASE 3 MANDATE**
> - Produces: TABLE 5 — Burst Path Register; TABLE 6 — Retry-After Gaps;
>   TABLE 7 — Cascade Risk Register
> - Gate that closes this phase: GATE 3
> - TABLE 0 scope: Section 1.0 TABLE 0 remains the active monitoring baseline; no new
>   entries at this boundary.
> - Obligations: TABLE 7 must have >= 2 cascade pairs with distinct Tier A / Tier B
>   constructs, each carrying a mechanism, severity, and duration.
> - Non-substitution: Completing this mandate block does NOT substitute for the GATE 3
>   declaration at the end of this phase.

## PHASE 3 — Exposure Analysis

### Section 3.A — Unprotected Burst Paths

**TABLE 5 — Burst Path Register**

| Flow construct | PA construct type | Location in flow | Estimated peak rate | Why it bypasses or overwhelms tier-1 guard |
|----------------|------------------|-----------------|--------------------|--------------------------------------------|

Check: Apply to Each with no concurrency cap, parallel branches with unbounded fan-out,
high-frequency trigger with no debounce, nested loops, batch-size misconfigurations.
If none found, write explicit acknowledgment with active guards listed.

### Section 3.B — Retry-After Gap Analysis

**TABLE 6 — Retry-After Gaps**

| Consumer construct | 429 location | Retry-After header read? | Actual backoff behavior | Failure mode |
|-------------------|-------------|-------------------------|------------------------|-------------|

Failure modes: retry-storm / fixed-misalign / silent-discard. At least one gap required.

### Section 3.C — Cascade Risk Pairs

**TABLE 7 — Cascade Risk Register**

| Cascade label | Tier A construct | Throttle mechanism | Load added to Tier B | Tier B construct | Failure mode | Severity | Duration |
|---------------|-----------------|-------------------|---------------------|-----------------|--------------|----------|---------|

Minimum: two cascade pairs with distinct Tier A / Tier B constructs and the mechanism
linking them.

*(The PHASE 3 MANDATE block above does NOT substitute for the gate declaration at the end of this phase.)*

**GATE 3** is cleared when and only when: TABLE 5 has enumerated all applicable burst-path
patterns (or confirmed none with active guards listed); TABLE 6 has identified all
Retry-After gaps across applicable consumers (or explicitly confirmed all consumers honor
Retry-After with explanation); and TABLE 7 has >= 2 complete cascade pairs with all
required fields populated, named throttle mechanisms, and distinct Tier A / Tier B
constructs.

**GATE 3 is not cleared when any of the following failure states are present:**
- TABLE 5 is absent or omits an applicable burst-path pattern without acknowledgment
- TABLE 6 is absent or has any consumer row with unexamined Retry-After behavior
- TABLE 7 has fewer than 2 cascade pairs
- Any TABLE 7 row has Tier A equal to Tier B
- Any TABLE 7 row is missing a stated throttle mechanism
- Any TABLE 7 row is missing a severity or duration assessment

*PHASE 4 is blocked until GATE 3 is cleared.*

---

*(GATE 3 cleared — TABLE 0 monitoring carries into Phase 4.)*

> **PHASE 4 MANDATE**
> - Produces: TABLE 8 — PA Construct Precision Pass; TABLE 9 — Throttle Budget;
>   TABLE 10 — Remediations; TABLE 11 — Monitoring Signal Classification;
>   Sections 4.B through 4.G
> - Gate that closes this phase: CORRECTION GATE
> - TABLE 0 scope: Section 4.E TABLE 11 must classify every recommended signal relative
>   to the Section 1.0 TABLE 0 inventory; missed-signal gaps must be flagged.
> - Obligations: every TABLE 8 row must carry an explicit disposition; every `[FAIL]` row
>   must have correction content immediately below its annotation.
> - Non-substitution: Completing this mandate block does NOT substitute for the CORRECTION
>   GATE declaration at the end of Section 4.A.

## PHASE 4 — Synthesis and PA Validation

### Section 4.A — PA Construct Validation

Review every construct in TABLE 1. Mark either `[PASS: confirmed]` or `[FAIL: corrected
below]`. For any `[FAIL]`, write corrected construct name, limit source, and precision note
immediately below the annotation before proceeding.

**TABLE 8 — PA Construct Precision Pass**

| Construct (from TABLE 1) | PA construct (confirmed / corrected) | Disposition | Correction reason | Precision note |
|--------------------------|-------------------------------------|-------------|------------------|----------------|

*(The PHASE 4 MANDATE block above does NOT substitute for the CORRECTION GATE declaration at the end of Section 4.A.)*

**CORRECTION GATE** is cleared when and only when every TABLE 8 row carries an explicit
disposition and every `[FAIL]` row has corrected content immediately below its annotation.

**CORRECTION GATE is not cleared when any of the following failure states are present:**
- Any TABLE 8 row lacks a `[PASS: confirmed]` or `[FAIL: corrected below]` disposition
- Any TABLE 8 `[FAIL]` row does not have a corrected construct name, limit source, and
  precision note immediately below its `[FAIL]` annotation

*Sections 4.B through 4.G are blocked until the CORRECTION GATE is cleared.*

### Section 4.B — UX Validation

Review TABLE 4. Confirm or correct each UX category against PA runtime behavior. Internal
system behavior is not user experience.

### Section 4.C — Quantified Risk Register

**TABLE 9 — Throttle Budget**

| Construct | Limit | Projected volume at scenario load | Status | Headroom / Deficit |
|-----------|-------|----------------------------------|--------|--------------------|

Status values: SAFE / MARGINAL / OVER-LIMIT. Show arithmetic for at least one row.

### Section 4.D — PA-Specific Remediations

**TABLE 10 — Remediations**

| Finding addressed | PA feature (exact name) | Configuration (what + value) | Effect on finding |
|------------------|------------------------|-----------------------------|--------------------|

Minimum: two PA-native remediations mapped to findings from PHASES 2–3 by section label.

### Section 4.E — Monitoring Signals (Extended — TABLE 0 cross-reference required, minimum three signals)

Classify at least three monitoring signals. For each, state its trigger condition, PA
tooling surface, and TABLE 0 status:

**TABLE 11 — Monitoring Signal Classification**

| Signal name | TABLE 0 status | PA tooling surface | Trigger condition | Missed-signal gap? |
|-------------|---------------|-------------------|------------------|--------------------|

TABLE 0 status values (required per signal): `active` / `inactive but available` /
`newly recommended`.

PA tooling surface (required): name the exact surface — flow run history, connector call
telemetry in Power Platform admin center, request usage dashboard, or equivalent documented
PA surface. Generic "set up alerting" fails.

Missed-signal gap (required for `inactive but available` signals): state whether the
signal would have detected the Phase 2 bottleneck or any Phase 3 finding. If yes, name
the TABLE 0 row and the finding it would have surfaced.

At least one TABLE 0 entry (active or inactive) must be referenced. At least one
`newly recommended` signal must be present.

### Section 4.F — License and Entitlement Boundary

Name at least one entitlement boundary with an explicit SAFE ↔ OVER-LIMIT shift statement
referencing a specific TABLE 9 row by construct name.

### Section 4.G — Test Approach

Describe at least one concrete test step using a named PA tool and method.

---

*End of V-05 prompt body.*
