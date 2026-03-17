# flow-ratelimit — Round 11 Variations (V-01 through V-05)

---

## V-01 — Role Sequence Axis: Complete Gate Chain Closure

**Axis:** Role sequence — 11 explicitly numbered roles with a closed gate chain. Every section transition names the prior role's specific deliverables as blocking conditions. No ungated boundaries in the analysis body.

**Hypothesis:** Mechanically enforced gate conditions at every role transition — not just preambles — produce the strongest structural compliance because each role cannot be reached unless all prior deliverables are confirmed present, closing all selective-skip bypass paths.

---

You are a Connectors and Power Automate throughput domain expert. You have been given a rate-limited system scenario. Produce a complete throughput analysis following the 11-role sequence below. Every role transition is gated — do not begin any role until its gate condition is satisfied by the content produced in prior roles.

---

### ROLE 0 — FORMAT CONTRACT AND VERDICT BLOCK (Preamble)

Produce two mandatory preamble blocks before any analysis content. These are the first two named sections in the document.

**Format Contract:** Declare the column structure that applies to every comparative table in this document:

Schema A — Comparative Tables:
- Required columns: BASELINE | PROTECTED | DERIVATION CHAIN
- BASELINE: current system behavior at the stated load, specific to the named component
- PROTECTED: system behavior with the named mitigation applied
- DERIVATION CHAIN: step-by-step computation (not a conclusion alone)
- STRUCTURAL REJECTION CLAUSE: a table missing any of these three column headers is flagged INCOMPLETE at scan time — no reading of cell content required; remediation is to add the missing column
- CONTENT REJECTION CLAUSE: a table with all three column headers present but any DERIVATION CHAIN cell containing only a conclusion without computation steps is flagged INCOMPLETE at read time; remediation is to replace the conclusion with its arithmetic chain referencing the rate limit registry values from Role 1

Schema B — UX Tier Template:
- Required fields per tier block: (a) Error Code or Platform Signal, (b) User-Visible Behavior, (c) Visibility Level, (d) Recovery Path
- STRUCTURAL REJECTION CLAUSE: a tier block missing any of the four field labels is flagged INCOMPLETE at scan time — count field labels present; remediation is to add the missing field label
- CONTENT REJECTION CLAUSE: a tier block with all four field labels present but any field populated with conclusion-only, generic, or non-scenario-specific text is flagged INCOMPLETE at read time; remediation is to replace with scenario-specific content tied to the named tier's behavior

The Format Contract is binding. Any table or tier block that violates it is flagged before proceeding.

**Verdict Block:** State the following four claims before any rate limit inventory, burst path audit, or volume mapping:

- Claim (a): The binding constraint — name the specific component and numeric threshold that limits throughput first
- Claim (b): The primary gap — identify the unprotected burst path by its specific trigger or action name, or name the missing Retry-After handler at the specific connector
- Claim (c): Current system status at the stated load — choose one: SAFE / DEGRADED / FAILING — with a one-sentence justification
- Claim (d): UX completeness commitment — state the number of distinct throttle tiers present in this scenario and confirm that all tiers will be described using the four-field Schema B template

The Verdict block is self-contained: a reader who reads only it knows the core finding without proceeding to evidence. Evidence sections must confirm or explicitly revise each Verdict claim. A Verdict claim that no evidence section references does not pass.

**Gate to Role 1:** Do not begin Role 1 until the Format Contract contains Schema A with three named columns and two named rejection clauses (STRUCTURAL and CONTENT), Schema B with four named fields and two named rejection clauses, AND the Verdict block contains all four claims (a) through (d) as separately enumerable entries.

---

### ROLE 1 — RATE LIMIT REGISTRY

Enumerate every rate limit present in the stated scenario. For each:
- Component name (connector, action, platform, environment)
- Numeric threshold (requests per interval, concurrent runs, etc.) — use estimates labeled as such if exact figures are unavailable
- Interval unit (per second, per minute, per day)
- Scope (per user, per connection, per environment, per flow)

Produce this as a structured registry table. This table is the numeric basis for all arithmetic in Role 7.

**Gate to Role 2:** Do not begin Role 2 until the Rate Limit Registry table is complete with at least one numeric threshold entry and all four fields (component, threshold, interval, scope) populated for each entry.

---

### ROLE 2 — BURST PATH AUDIT

Identify every path in the scenario that can generate concurrent requests exceeding a rate limit without a concurrency cap, retry policy queue, or buffer between the source and the rate-limited endpoint.

For each unprotected burst path:
- Name the specific trigger or action that generates the burst
- Name the rate-limited endpoint it contacts
- Explain why no structural cap exists on this path (not merely that a higher-tier limit exists)
- Label it: STRUCTURAL (no mechanism exists on this path) or INCIDENTAL (mechanism exists but is misconfigured, bypassable, or absent only under specific conditions)

The count of distinct unprotected burst paths identified here is the authoritative tier-count source for Role 5 gate item (e). Do not reference the Verdict block to resolve tier count — reference this section directly.

**Gate to Role 3:** Do not begin Role 3 until the Burst Path Audit contains at least one explicitly labeled unprotected burst path with all four fields (trigger/action name, rate-limited endpoint, structural explanation, STRUCTURAL/INCIDENTAL classification) populated.

---

### ROLE 3 — VOLUME-TO-BEHAVIOR MAPPING

Produce a structured BASELINE | PROTECTED | DERIVATION CHAIN table mapping request volume ranges to throttle behavior. Each row:
- Volume range (e.g., 1–100 req/min, 101–600 req/min, 601+ req/min)
- BASELINE: what throttle behavior activates at this volume in the current unprotected state
- PROTECTED: what throttle behavior activates with mitigations from Role 8 applied
- DERIVATION CHAIN: the computation step showing how this volume range maps to the rate limit threshold from the Role 1 registry

Apply the Schema A Format Contract. Flag any cell violating the STRUCTURAL or CONTENT rejection clause inline.

**Gate to Role 4:** Do not begin Role 4 until the Volume-to-Behavior Mapping table is complete, uses the three declared columns, and contains at least three volume tier rows — AND the DERIVATION CHAIN cells reference specific numeric values from the Role 1 registry (not generic descriptions).

---

### ROLE 4 — CASCADING THROTTLE FAILURE SCENARIO

Construct or identify a specific scenario where throttling at one tier causally triggers a second distinct throttle event at a different tier. Requirements:
- Name both tiers and their specific rate limits from the Role 1 registry
- Explain the causal mechanism: what does Tier 1 throttling do that causes Tier 2 to be hit?
- Two independent limits both hit under load do NOT qualify — the second throttle must be caused by the first
- Describe the compounding effect on throughput or error rate

If no cascading scenario is possible in the stated system, state this explicitly with justification; do not fabricate a cascade.

**Gate to Role 5:** Do not begin Role 5 until the Cascading Throttle Failure Scenario either (a) names both throttle tiers with their specific numeric limits and explains the causal trigger mechanism, OR (b) explicitly states that no cascade is structurally possible and provides a one-sentence justification.

---

### ROLE 5 — UX PER-TIER TEMPLATE

**This is an explicitly numbered role in the role sequence.** Apply Schema B to every throttle tier present in the scenario. The tier count in this section must be verified against the Role 2 Burst Path Audit — not against Verdict Claim (d).

Gate conditions for this role (all six must be satisfied before proceeding to Role 6):

- (a) Field-A — Error Code or Platform Signal — is present and scenario-specific (not generic) for every tier
- (b) Field-B — User-Visible Behavior — is present and describes what the user observes at this specific tier for every tier
- (c) Field-C — Visibility Level — is present and states whether the signal is user-visible and explicit, or silent/background, for every tier
- (d) Field-D — Recovery Path — is present and names a specific available recovery action (manual retry, automatic exponential backoff, permanent failure, etc.) for every tier
- (e) Tier count in this section verified against the Role 2 Burst Path Audit section directly — not against Verdict Claim (d). If Role 2 identified N unprotected burst paths, this section must describe behavior for each throttle tier those paths encounter. Discrepancies trigger a REVISED marker on Verdict Claim (d) at this boundary.
- (f) Structure compliance confirmed: each tier uses the named Schema B four-field template structure, not free prose. A tier described in paragraphs without the four field labels present does not pass, even if all four topics are addressed in the text.

Do not proceed to Role 6 until all six gate items are confirmed.

**Gate to Role 6:** Do not begin Role 6 until all six UX gate items (a) through (f) above are satisfied for every tier described.

---

### ROLE 6 — RETRY-AFTER GAP ANALYSIS

Evaluate whether the flow or connector handles Retry-After headers (or equivalent backoff signals: `x-ms-ratelimit-remaining`, `Retry-After-Ms`, `X-RateLimit-Reset`) from throttled endpoints.

For each rate-limited endpoint in the Role 1 registry:
- Does the current implementation handle the Retry-After signal? State YES / NO / PARTIAL
- If NO or PARTIAL: describe the failure mode (e.g., immediate retry storm, permanent failure after N retries, silent dropped requests)
- If PARTIAL: name the specific signal handled and the gap

Missing Retry-After handling must be flagged as a finding with the failure mode described.

**Gate to Role 7:** Do not begin Role 7 until Role 6 has evaluated Retry-After handling for every endpoint in the Role 1 registry, with a YES/NO/PARTIAL verdict and failure mode description for each non-YES entry.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Using the numeric rate limits from Role 1 as the arithmetic basis, produce a Schema A table showing quantified impact at a 5x load spike.

For the primary binding constraint identified in Verdict Claim (a), show step-by-step arithmetic:
1. Baseline request rate (from scenario context)
2. × 5x multiplier = peak load
3. Peak load − rate limit threshold = overflow volume per interval
4. Overflow volume × retry factor (if Retry-After is not handled) = failed request count
5. Failed request count ÷ peak load = failure percentage

Each computation step must appear in the DERIVATION CHAIN cell — not reconstructible by inference, but written out explicitly. A conclusion without its computation chain fails the Schema A CONTENT REJECTION CLAUSE and is flagged INCOMPLETE inline.

If any Verdict claim is revised by Role 7 findings, insert REVISED — see Role 7 marker in the Verdict block for the affected claim.

**Gate to Role 8:** Do not begin Role 8 until the Quantified Impact table contains the arithmetic chain in the DERIVATION CHAIN column with each of the five steps above explicitly shown, referencing Role 1 registry values by name.

---

### ROLE 8 — BASELINE-DELTA MITIGATIONS

For each bottleneck and unprotected burst path identified in Roles 2 and 6, propose a concrete remediation. Each mitigation must:
- Name the specific action, setting, or pattern (not "add retry logic" — name the Power Automate action, concurrency control setting, or HTTP action configuration)
- State the BEFORE state: what the system does at the bottleneck without this mitigation
- State the AFTER state: what the system does with the mitigation applied
- Appear in the PROTECTED column of the Role 3 Volume-to-Behavior Mapping table (update that table if needed)

Generic advice not tied to the specific component and baseline condition does not qualify.

If any Verdict claim is revised by Role 8 findings, insert REVISED — see Role 8 marker in the Verdict block for the affected claim.

**Gate to Role 9:** Do not begin Role 9 until every bottleneck and unprotected burst path from Roles 2 and 6 has a mitigation with explicit BEFORE and AFTER state, and the Role 3 PROTECTED column reflects the mitigated state.

---

### ROLE 9 — VERDICT CURRENCY CHECK

Before the terminal reconciler, perform an inline currency check:

1. Re-read the Verdict block claims (a) through (d)
2. For each claim, confirm whether the evidence sections (Roles 1–8) confirmed, revised, or left unchallenged the claim
3. For each revised claim, confirm that a REVISED — see Role N marker was inserted at the boundary of the revising role (not deferred to now)
4. For any marker not yet inserted: insert it now and note that it was deferred

This role does not produce new analysis. It reconciles Verdict currency before terminal close.

**Gate to Role 10:** Do not begin Role 10 until all four Verdict claims have been explicitly checked for currency and any missing revision markers have been inserted.

---

### ROLE 10 — TERMINAL RECONCILER

This is the last named section in the document. Perform three checks and produce a named finding record:

**Check (a) — Verdict Revision Marker Audit:** Scan the Verdict block. For each claim, confirm it carries a REVISED — see Role N marker if revised by any evidence section. List any claim revised by evidence but missing a marker as a violation.

**Check (b) — Gate Deliverable Audit:** Enumerate each role transition (Role 0→1, 1→2, ..., 8→9, 9→10) and confirm the specific named deliverables from the prior role are present. List any gate whose named deliverables are absent as a violation.

**Check (c) — Derivation Chain Completeness Audit:** Identify any DERIVATION CHAIN cell in any Schema A table that contains only a conclusion without computation steps. Flag each as INCOMPLETE with the table and row reference.

**Check (d) — Schema B Structural and Content Audit:** For every UX tier block, run two scans:
- Structural scan: confirm all four field labels (a)–(d) are present. Flag any missing label as a STRUCTURAL violation.
- Content scan: confirm each field contains scenario-specific content for this tier, not generic or conclusion-only text. Flag any field with generic content as a CONTENT violation.

**Reconciler Findings:** State the total violation count. If zero violations: "Reconciler Findings: 0 violations — document complete." If violations exist, list each with role reference, clause type, and remediation.

A reconciler section that performs scans without producing a named finding record does not close.

---

**Scenario:** [INSERT SCENARIO HERE — describe the Power Automate flow, connectors used, trigger type, expected request volume, and target endpoints]

---

## V-02 — Format Contract Axis: Four-Clause Schema Declaration

**Axis:** Output format — Format Contract preamble with two named schemas (Schema A: comparative tables; Schema B: UX tier template), each with a STRUCTURAL and CONTENT rejection clause, producing four named rejection clauses total. DERIVATION CHAIN as mandatory fourth structural column.

**Hypothesis:** Declaring both Schema A and Schema B in a single Format Contract preamble with four explicitly differentiated rejection clauses (two per schema) produces the strongest scan-time and read-time violation detection because violation type, detection method, and remediation path are named separately — structural violations are detectable without reading prose; content violations are detectable by reading the named field without interpreting surrounding text.

---

You are a Connectors and Power Automate throughput domain expert analyzing a rate-limited system scenario. Your output must be structured according to the Format Contract declared below. The Format Contract is section one of your output and must appear before any rate limit inventory, burst path analysis, or volume mapping.

---

### SECTION 1 — FORMAT CONTRACT

This section is a binding structural contract. All subsequent sections must comply.

#### Schema A — Comparative Analysis Tables

Every table containing quantified throughput analysis uses three mandatory columns:

| BASELINE | PROTECTED | DERIVATION CHAIN |
|----------|-----------|-----------------|
| Current system behavior at stated load — specific to the named component, not generic | System behavior with named mitigation applied — references the mitigation from Section 7 by name | Step-by-step arithmetic — each computation step shown, referencing the rate limit registry values from Section 2 by name |

**BASELINE** means: what the system does today at the stated volume, at the specific component named in this row. A BASELINE cell describing what could happen generically rather than what this specific component does at this load does not satisfy this definition.

**PROTECTED** means: what the system does with the specific named mitigation from Section 7 applied. A PROTECTED cell describing what mitigations generally do rather than what this specific mitigation does to this specific component does not satisfy this definition.

**DERIVATION CHAIN** means: the explicit arithmetic connecting the stated volume to the threshold to the overflow to the outcome. Each step must be written out — not reconstructible by inference.

**Schema A — STRUCTURAL REJECTION CLAUSE:**
- Clause type: STRUCTURAL
- Detection method: scan-time — examine column headers; no reading of cell content required
- Violation condition: any required column header (BASELINE, PROTECTED, or DERIVATION CHAIN) is absent from the table
- Detection action: flag the table as INCOMPLETE immediately upon scanning the header row
- Remediation: add the missing column header and populate all rows

**Schema A — CONTENT REJECTION CLAUSE:**
- Clause type: CONTENT
- Detection method: read-time — examine cell content for each row after confirming header structure is intact
- Violation condition: DERIVATION CHAIN cell contains only a conclusion (e.g., "42% failure rate") without the computation steps that produce it, OR BASELINE cell contains generic system behavior not specific to this component and load, OR PROTECTED cell describes a generic mitigation outcome not tied to the specific named mitigation
- Detection action: flag the specific cell as INCOMPLETE with the clause type: CONTENT
- Remediation: replace the cell content with the required computation chain or component-specific description; do not alter the column structure

#### Schema B — UX Tier Template

Every throttle tier described in Section 6 uses a four-field block structure:

```
Tier [N] — [Tier Name]
(a) Error Code or Platform Signal: [HTTP status code, connector error name, or platform event exactly as it appears in the UI or run history]
(b) User-Visible Behavior: [what the user observes — connector error message shown, flow run queued in history, silent failure with no indicator]
(c) Visibility Level: [USER-VISIBLE EXPLICIT | USER-VISIBLE IMPLICIT | SILENT-BACKGROUND]
(d) Recovery Path: [specific action available to the user or system — manual retry, automatic exponential backoff with stated delay, permanent failure with no recovery, queue drain with stated SLA]
```

All four fields are required for every tier. Fields must be populated with scenario-specific content tied to this tier's behavior — not generic descriptions that could apply to any throttled system.

**Schema B — STRUCTURAL REJECTION CLAUSE:**
- Clause type: STRUCTURAL
- Detection method: scan-time — count field labels (a), (b), (c), (d) present in the tier block; no reading of field content required
- Violation condition: any of the four field labels is absent from the tier block
- Detection action: flag the tier block as INCOMPLETE (STRUCTURAL) immediately upon counting field labels
- Remediation: add the missing field label(s) and populate with scenario-specific content

**Schema B — CONTENT REJECTION CLAUSE:**
- Clause type: CONTENT
- Detection method: read-time — examine each field's content after confirming all four labels are present
- Violation condition: any field is populated with (i) a generic description not specific to this tier (e.g., "user sees an error" without naming the error), or (ii) conclusion-only text (e.g., "flow fails") without the mechanism that produces that outcome, or (iii) a copy of content from another tier's field without explaining why this tier produces the same behavior
- Detection action: flag the specific field as INCOMPLETE (CONTENT) with the field label and tier name
- Remediation: replace with scenario-specific content naming the exact error code, platform event, or user-visible signal at this tier

**Four Total Rejection Clauses Declared:** Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT. Each clause has been given a distinct name, detection method, and remediation. A violation of one clause does not imply violation of another — they are checked independently.

**Gate to Section 2:** Do not begin Section 2 until this Format Contract contains all four rejection clauses with named clause type, detection method (scan-time vs. read-time), and remediation for each.

---

### SECTION 2 — VERDICT BLOCK

State the following before any rate limit inventory or analysis:

**Claim (a) — Binding Constraint:** [Component name] at [numeric threshold] per [interval] is the binding constraint — it is the first rate limit reached as load increases.

**Claim (b) — Primary Gap:** [Specific trigger or action name] is an unprotected burst path: it can generate concurrent requests exceeding [Claim (a) threshold] with no concurrency cap, queue buffer, or Retry-After handler between it and the rate-limited endpoint.

**Claim (c) — System Status:** At [stated load], this system is [SAFE / DEGRADED / FAILING] because [one sentence tying the load volume to the binding constraint threshold].

**Claim (d) — UX Completeness:** This analysis will describe [N] distinct throttle tiers. All [N] tiers will be documented using Schema B's four-field template. This claim will be marked REVISED if new tiers are discovered mid-analysis or if any tier cannot be fully populated using Schema B.

**Revision Rule:** Any evidence section (Sections 3–7) that revises a Claim must insert the marker REVISED — see Section [N] immediately after the affected Claim text. The revision must be inserted at the boundary of the revising section — deferral to terminal reconciliation does not satisfy currency.

**Gate to Section 3:** Do not begin Section 3 until all four Verdict Claims are present and Claim (d) names a specific tier count commitment.

---

### SECTION 3 — RATE LIMIT REGISTRY

Enumerate every rate limit in the scenario. For each:
- Component: specific name (connector, action, environment tier, platform service)
- Threshold: numeric value per interval (label as estimate if not published)
- Interval: per second / per minute / per day
- Scope: per user / per connection / per environment / per flow

This registry is the sole numeric source for DERIVATION CHAIN cells throughout the document. Any Schema A DERIVATION CHAIN cell must cite registry entries by component name — not use round numbers or estimates independent of this registry.

If any registry entry revises Verdict Claim (a) (binding constraint), insert REVISED — see Section 3 in the Verdict block at this point.

**Gate to Section 4:** Do not begin Section 4 until the Rate Limit Registry contains at least one entry with all four fields (component, threshold, interval, scope) populated and at least one numeric threshold.

---

### SECTION 4 — BURST PATH AUDIT TABLE

Produce a Schema A table with columns: BURST PATH | BASELINE | PROTECTED | DERIVATION CHAIN.

For each burst path:
- BURST PATH: name the specific trigger or action and its target rate-limited endpoint
- BASELINE: describe how many concurrent requests this path generates versus the endpoint's threshold — specific to the component and volume
- PROTECTED: describe the concurrency behavior with the named mitigation applied (reference Section 7 mitigation name)
- DERIVATION CHAIN: compute requests generated ÷ rate limit threshold = saturation ratio at baseline volume; show the step

Classify each burst path as STRUCTURAL or INCIDENTAL (a mechanism exists but is bypassed/misconfigured under specific conditions).

The burst path count established here is the authoritative tier count source for Section 6, Gate Item (e). This section — not the Verdict block — resolves tier count for the UX gate.

If any entry revises Verdict Claim (b), insert REVISED — see Section 4 in the Verdict block.

**Gate to Section 5:** Do not begin Section 5 until the Burst Path Audit table has at least one row satisfying the Schema A column structure with all three cells substantively populated.

---

### SECTION 5 — VOLUME-TO-BEHAVIOR MAPPING

Produce a Schema A table mapping volume ranges to throttle behavior:

| Volume Range | BASELINE | PROTECTED | DERIVATION CHAIN |
|---|---|---|---|

Each row: a distinct volume tier. DERIVATION CHAIN: show the computation from volume to threshold saturation using registry values. At least three volume tiers. Update PROTECTED cells after completing Section 7 mitigations.

Apply the Schema A Format Contract. Inline flag any cell violating STRUCTURAL or CONTENT rejection clauses.

**Gate to Section 6:** Do not begin Section 6 until the Volume-to-Behavior Mapping table contains at least three rows and all DERIVATION CHAIN cells contain computation steps (not conclusions alone).

---

### SECTION 6 — UX PER-TIER ANALYSIS

Apply Schema B to every throttle tier in the scenario.

**UX Role Gate Conditions** (all six must pass before proceeding to Section 7):
- (a) Field (a) — Error Code or Platform Signal — present and scenario-specific for every tier
- (b) Field (b) — User-Visible Behavior — present with the specific observable outcome for every tier
- (c) Field (c) — Visibility Level — present using one of the three named levels for every tier
- (d) Field (d) — Recovery Path — present naming the specific available action for every tier
- (e) Tier count verified against Section 4 Burst Path Audit — count the burst paths identified there; this section must describe UX behavior for each throttle tier those paths encounter. Tier count must match Section 4's count, not Verdict Claim (d). A mismatch triggers REVISED — see Section 6 on Verdict Claim (d) at this boundary.
- (f) Structure compliance: each tier uses the four-field labeled block structure, not free prose

Apply Schema B rejection clauses inline. Flag any tier block with STRUCTURAL violations (missing field labels) or CONTENT violations (generic/non-specific field content) before proceeding.

**Gate to Section 7:** Do not begin Section 7 until all six gate items (a)–(f) are satisfied.

---

### SECTION 7 — MITIGATION PRESCRIPTIONS WITH BASELINE-DELTA

For each bottleneck and burst path from Sections 4 and 5:

- Mitigation Name: a specific, named configuration, action, or pattern (not generic advice)
- BEFORE state: the specific baseline behavior at this component without mitigation
- AFTER state: the specific system behavior with this mitigation applied
- Update the PROTECTED column in Sections 4 and 5 to reflect this mitigation by name

After completing all mitigations, check Verdict Claims (a)–(d) for currency. If any claim is revised by these mitigations, insert REVISED — see Section 7 at the boundary.

**Gate to Section 8:** Do not begin Section 8 until every burst path and bottleneck has a named mitigation with explicit BEFORE and AFTER states.

---

### SECTION 8 — QUANTIFIED IMPACT

Schema A table with the binding constraint row showing 5x load spike arithmetic:

DERIVATION CHAIN cell must show:
1. Baseline request rate (from scenario context)
2. × 5 = peak load
3. Peak load − [registry threshold] = overflow volume
4. Overflow × retry factor = failed requests
5. Failed ÷ peak = failure percentage

Each step shows the specific numeric values from the Section 3 registry. A conclusion cell without these steps fails Schema A CONTENT REJECTION CLAUSE and is flagged INCOMPLETE inline.

**Gate to Section 9:** Do not begin Section 9 until the Quantified Impact table contains the five-step arithmetic chain in the DERIVATION CHAIN cell.

---

### SECTION 9 — TERMINAL RECONCILER

Last named section. Produce a finding record.

**Check (a) — Verdict Revision Markers:** For each Verdict Claim (a)–(d), confirm revision markers were inserted at the boundary of the revising section (not deferred). List any claim revised by evidence but missing a marker as a violation.

**Check (b) — Gate Deliverable Confirmation:** Enumerate Sections 1–8 gate conditions. Confirm each gate's named deliverables are present. List any missing deliverable as a violation.

**Check (c) — Schema A Derivation Chain Audit:** Identify any DERIVATION CHAIN cell containing only a conclusion. Flag as INCOMPLETE (CONTENT) with section and row reference.

**Check (d) — Schema B Dual Audit:**
- Structural scan: for each UX tier block, count field labels (a)–(d). Flag any missing label as STRUCTURAL violation.
- Content scan: for each UX tier block with all four labels present, flag any field with generic or non-scenario-specific content as CONTENT violation.

**Reconciler Findings:** State total violation count. "Reconciler Findings: 0 violations — document complete." or itemize each violation with section reference, clause type, and remediation.

---

**Scenario:** [INSERT SCENARIO HERE]

---

## V-03 — Verdict-First Axis: Document-Head Verdict with Bidirectional Revision and Claim (d)

**Axis:** Lifecycle emphasis — the Verdict block appears before any analysis content, contains four explicitly named claims including Claim (d) committing to UX tier count and template completeness, and every evidence section that revises a claim inserts an inline revision marker at that section's boundary (not deferred to terminal reconciliation).

**Hypothesis:** Forcing an analytical position at document head — before evidence — creates accountability that narration-toward-a-conclusion avoids. Bidirectional revision marking (Verdict block updated at the boundary of the revising section) makes Verdict staleness detectable at any point in the document, not only after full reading. Claim (d) subjects UX coverage to the same revision discipline as analytical claims.

---

You are a Connectors and Power Automate throughput domain expert. Analyze the rate-limited system scenario below. Your document must open with a standalone Verdict block — before any rate limit inventory, burst path table, volume mapping, or UX section. The Verdict commits to analytical positions before evidence. Evidence sections confirm or revise each claim.

---

### DOCUMENT OPENING — VERDICT BLOCK

This block appears first. A reader who reads only this block knows the core finding without reading further.

**Claim (a) — Binding Constraint:**
State: the component name, its numeric rate limit threshold, and the interval. This is the first limit reached as load increases. Commit before reading forward.

**Claim (b) — Primary Gap:**
State: the specific trigger or action name that constitutes the unprotected burst path, and why no structural cap exists between it and the rate-limited endpoint. Commit before reading forward.

**Claim (c) — System Status:**
State: SAFE / DEGRADED / FAILING at the stated load volume. One sentence tying the load to the threshold. Commit before reading forward.

**Claim (d) — UX Coverage Commitment:**
State: the number of distinct throttle tiers this scenario contains and the commitment that all tiers will be documented using a four-field template (Error Code, User-Visible Behavior, Visibility Level, Recovery Path). This claim must be marked REVISED if a tier is discovered or removed during analysis, or if any tier cannot be fully populated.

**Revision Protocol:** When any section (Sections 1–8 below) produces evidence that revises a Claim, that section must:
1. Insert the marker: `REVISED — see Section [N]` immediately after the affected Claim text in this Verdict block
2. Insert the marker at the boundary of the revising section — the section heading or its first line — not at document close
3. State what changed: which Claim, what the prior position was, what the evidence showed

A Verdict claim revised by evidence but not marked is a staleness error. A Verdict claim marked REVISED but with no corresponding revision in the named section is a phantom revision error. The Terminal Reconciler (Section 9) audits for both.

---

### FORMAT CONTRACT

Declare before Section 1:

Schema A — every comparative table uses BASELINE | PROTECTED | DERIVATION CHAIN columns. STRUCTURAL REJECTION CLAUSE: missing column header = INCOMPLETE at scan time. CONTENT REJECTION CLAUSE: present column header with conclusion-only cell content = INCOMPLETE at read time.

Schema B — every UX tier block uses four fields: (a) Error Code or Platform Signal, (b) User-Visible Behavior, (c) Visibility Level, (d) Recovery Path. STRUCTURAL REJECTION CLAUSE: missing field label = INCOMPLETE at scan time. CONTENT REJECTION CLAUSE: present field label with generic non-scenario-specific content = INCOMPLETE at read time.

Both schemas carry two rejection clauses each: STRUCTURAL (scan-time, remediation: add missing structure) and CONTENT (read-time, remediation: replace generic content with scenario-specific analysis).

---

### SECTION 1 — RATE LIMIT REGISTRY

Enumerate every rate limit: component, numeric threshold, interval, scope. This registry is the numeric basis for all DERIVATION CHAIN cells.

**Verdict Check at Section 1 close:** Does the registry confirm, extend, or revise Claim (a)? If the binding constraint identified in Claim (a) does not appear in the registry with its stated threshold, or if a lower threshold appears for a different component, insert REVISED — see Section 1 in the Verdict block at this boundary.

---

### SECTION 2 — BURST PATH AUDIT

Identify every unprotected burst path: trigger/action name, target endpoint, structural explanation, STRUCTURAL vs. INCIDENTAL classification. Produce a Schema A burst path table.

This section's burst path count is the authoritative tier count source for the Section 6 UX gate, Item (e). Resolution of tier count for gate purposes must reference this section, not Verdict Claim (d).

**Verdict Check at Section 2 close:** Does the burst path audit confirm, extend, or revise Claim (b) or Claim (d)?
- If the primary gap identified in Claim (b) is not found, or a different path is structurally unprotected: insert REVISED — see Section 2 on Claim (b)
- If the tier count implied by burst paths differs from Claim (d)'s stated tier count: insert REVISED — see Section 2 on Claim (d)

---

### SECTION 3 — RETRY-AFTER GAP EVALUATION

For each endpoint in the Section 1 registry, evaluate Retry-After handling (or equivalent: `x-ms-ratelimit-remaining`, `Retry-After-Ms`): YES / NO / PARTIAL. For NO and PARTIAL, describe the failure mode (retry storm, permanent failure after N retries, silent drop).

**Verdict Check at Section 3 close:** Do the Retry-After gaps confirm or revise Claims (a), (b), or (c)? If missing Retry-After handling changes the system status assessment, insert REVISED — see Section 3 on Claim (c).

---

### SECTION 4 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table with at least three volume tiers. DERIVATION CHAIN cells must show: volume ÷ rate limit threshold = saturation ratio, with specific registry values cited. BASELINE and PROTECTED cells must be component-specific, not generic.

**Verdict Check at Section 4 close:** Does the volume mapping confirm or revise Claim (c) system status? Insert revision markers at this boundary if needed.

---

### SECTION 5 — CASCADING THROTTLE FAILURE ANALYSIS

Identify or construct a scenario where throttling at one tier causally triggers throttling at a second tier. Name both tiers, their rate limits from Section 1, and the causal mechanism. If no cascade is possible, state this explicitly.

**Verdict Check at Section 5 close:** Does the cascade analysis revise any Verdict claim? Insert markers at this boundary.

---

### SECTION 6 — UX PER-TIER ANALYSIS (Explicitly Numbered Role)

Apply Schema B to every throttle tier. Use the four-field block for each tier:

```
Tier [N] — [Name]
(a) Error Code or Platform Signal: [scenario-specific]
(b) User-Visible Behavior: [scenario-specific]
(c) Visibility Level: [USER-VISIBLE EXPLICIT | USER-VISIBLE IMPLICIT | SILENT-BACKGROUND]
(d) Recovery Path: [scenario-specific named action]
```

**Six-Item Gate (all six must pass before Section 7):**
- (a) Field (a) present and scenario-specific for every tier
- (b) Field (b) present and scenario-specific for every tier
- (c) Field (c) present using one of the three named levels for every tier
- (d) Field (d) present naming a specific recovery action for every tier
- (e) Tier count verified against Section 2 Burst Path Audit — reference the section directly, not Verdict Claim (d). If tier counts disagree: insert REVISED — see Section 6 on Claim (d) at this gate boundary before proceeding
- (f) Structure compliance: all tiers use the four-field labeled template, not free prose

**Verdict Check at Section 6 close:** Verify Claim (d) currency using Section 2's tier count (per gate item (e) above). Insert REVISED — see Section 6 if Claim (d)'s stated tier count has changed.

---

### SECTION 7 — MITIGATION PRESCRIPTIONS

For each bottleneck and burst path: named mitigation (specific action/setting/pattern), BEFORE state (baseline behavior at this component), AFTER state (system behavior with mitigation). Update Section 4's PROTECTED column by mitigation name.

**Verdict Check at Section 7 close:** Do mitigations revise any claim? Insert markers at this boundary.

---

### SECTION 8 — QUANTIFIED IMPACT

Schema A table. Primary binding constraint row at 5x load spike. DERIVATION CHAIN cell must show five steps:
1. Baseline rate × 5 = peak
2. Peak − threshold = overflow
3. Overflow × retry factor = failed requests
4. Failed ÷ peak = failure %
5. Each step cites Section 1 registry values by name

Inline flag any DERIVATION CHAIN cell failing the CONTENT REJECTION CLAUSE.

**Verdict Check at Section 8 close:** Does the arithmetic revise Claim (c)? Insert marker if yes.

---

### SECTION 9 — TERMINAL RECONCILER

Last section. Four checks, named finding record.

**Check (a):** Scan Verdict Claims (a)–(d). For each, confirm that any revision occurring in Sections 1–8 has an inline REVISED — see Section [N] marker inserted at the boundary of the revising section. List staleness violations (revised but unmarked) and phantom violations (marked but no revision in cited section).

**Check (b):** Enumerate each section's gate conditions. Confirm named deliverables are present. List missing deliverables.

**Check (c):** Identify Schema A DERIVATION CHAIN cells with conclusions only. Flag as INCOMPLETE (CONTENT).

**Check (d) — Schema B Dual Audit:**
- Structural scan: count field labels per tier. Flag missing labels as STRUCTURAL violation.
- Content scan: flag generic or non-scenario-specific field content as CONTENT violation.

**Reconciler Findings:** State total count. "0 violations — document complete." or itemized list.

---

**Scenario:** [INSERT SCENARIO HERE]

---

## V-04 — UX Gate Independence Axis: Six-Item Gate with Analytical Independence from Verdict

**Axis:** Role sequence variant — a nine-section document where the UX analysis section carries a fully explicit six-item gate, with gate item (e) analytically independent from the Verdict block: tier-count verification references the burst path audit section by name, not Verdict Claim (d). Schema B carries both STRUCTURAL and CONTENT rejection clauses. Item (e) resolution path cannot cite the Verdict as source even alongside an analysis-section reference.

**Hypothesis:** When gate item (e) names the specific analysis section as its resolution path (not the Verdict), the gate cannot silently pass on a stale Verdict — the verifier must examine the analytical content directly. This eliminates the circular dependency where a stale Verdict satisfies a gate that is supposed to check the Verdict's accuracy. Analytical independence of item (e) is the minimal change required to close the C-31 bypass path.

---

You are a Connectors and Power Automate throughput domain expert analyzing a rate-limited system scenario. Produce a structured throughput analysis. The UX analysis section uses a six-item gate where item (e) — tier count verification — is resolved by reference to the burst path audit section directly, not by reference to any claim in the Verdict block.

---

### SECTION 1 — FORMAT CONTRACT AND VERDICT BLOCK

**Format Contract:**

Schema A — Comparative Tables: columns BASELINE | PROTECTED | DERIVATION CHAIN.
- STRUCTURAL REJECTION CLAUSE: absent column = INCOMPLETE (scan-time). Remediation: add column.
- CONTENT REJECTION CLAUSE: column present, conclusion-only cell = INCOMPLETE (read-time). Remediation: replace with computation chain.

Schema B — UX Tier Template: four field labels per tier block — (a) Error Code or Platform Signal, (b) User-Visible Behavior, (c) Visibility Level, (d) Recovery Path.
- STRUCTURAL REJECTION CLAUSE: absent field label = INCOMPLETE (scan-time). Remediation: add field label.
- CONTENT REJECTION CLAUSE: field label present, generic or non-scenario-specific content = INCOMPLETE (read-time). Remediation: replace with scenario-specific content for this tier.

Four rejection clauses declared: Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT.

**Verdict Block:**

**Claim (a):** [Binding constraint — component name and numeric threshold]

**Claim (b):** [Primary gap — unprotected burst path at named trigger/action]

**Claim (c):** [System status: SAFE / DEGRADED / FAILING at stated load — one sentence]

**Claim (d):** [UX coverage — N distinct throttle tiers; all N will use Schema B four-field template. Mark REVISED if tier count changes or any tier cannot be fully populated.]

Revision protocol: any section that revises a Claim inserts REVISED — see Section [N] at the Claim at the revising section's boundary.

---

### SECTION 2 — RATE LIMIT REGISTRY

Registry table: component | threshold | interval | scope. Minimum one numeric threshold. This registry supplies all DERIVATION CHAIN arithmetic.

---

### SECTION 3 — BURST PATH AUDIT

**This section is the authoritative tier count source for Section 6 Gate Item (e).** Gate item (e) resolution references this section by name and number — not Verdict Claim (d).

For each unprotected burst path:
- Trigger or action name
- Target rate-limited endpoint
- Why no structural cap exists (not merely "a higher-tier limit exists")
- Classification: STRUCTURAL or INCIDENTAL

The total number of burst paths identified here determines how many tiers Section 6 must cover.

---

### SECTION 4 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table, three+ volume tiers. DERIVATION CHAIN cells: volume / threshold = saturation ratio, citing registry values. Apply Schema A rejection clauses inline.

---

### SECTION 5 — RETRY-AFTER GAP ANALYSIS

Evaluate each registry endpoint for Retry-After handling: YES / NO / PARTIAL. Describe failure mode for non-YES entries.

---

### SECTION 6 — UX PER-TIER ANALYSIS

Apply Schema B to every throttle tier. Block structure:

```
Tier [N] — [Name from Section 3]
(a) Error Code or Platform Signal: [specific to this tier — not generic]
(b) User-Visible Behavior: [what the user observes at this specific tier — not generic]
(c) Visibility Level: [USER-VISIBLE EXPLICIT | USER-VISIBLE IMPLICIT | SILENT-BACKGROUND]
(d) Recovery Path: [specific available action — manual retry, exponential backoff, permanent failure]
```

Apply Schema B rejection clauses inline: flag STRUCTURAL violations (missing field labels) and CONTENT violations (generic text) immediately.

**SIX-ITEM GATE — all six conditions must be satisfied before Section 7:**

**(a) FIELD-A Completeness:** Field label (a) Error Code or Platform Signal is present **and** populated with the specific HTTP status code, connector error name, or platform event name for this tier — not a generic description. Verify for every tier described.

**(b) FIELD-B Completeness:** Field label (b) User-Visible Behavior is present **and** describes what the user observes specifically at this tier — naming the interface element, message, or flow state that changes. Not "user sees an error." Verify for every tier.

**(c) FIELD-C Completeness:** Field label (c) Visibility Level is present **and** states one of the three named levels (USER-VISIBLE EXPLICIT / USER-VISIBLE IMPLICIT / SILENT-BACKGROUND) for every tier.

**(d) FIELD-D Completeness:** Field label (d) Recovery Path is present **and** names a specific recovery action available at this tier — not "retry" but the specific mechanism (e.g., "automatic exponential backoff using Power Automate's built-in retry policy, up to 8 retries with base delay of 20s"). Verify for every tier.

**(e) Tier Count Independence — ANALYTICAL INDEPENDENCE REQUIRED:**
Verify the tier count in this section against **Section 3 (Burst Path Audit)** — count the burst paths enumerated there and confirm this section describes throttle behavior for each tier those paths encounter. **This item must be resolved by examining Section 3 directly.** Citing Verdict Claim (d) as the tier count source — even alongside a Section 3 reference — does not satisfy this gate item. If the tier count derived from Section 3 differs from the count in this section: insert REVISED — see Section 6 on Verdict Claim (d) at this gate boundary before proceeding to Section 7.

**(f) Structure Compliance:** Each tier uses the named Schema B four-field template with explicit field labels (a)–(d), not free prose. A tier that addresses all four topics in paragraph form without the field label structure does not pass this item. Verify for every tier.

Items (e) and (f) are separately named blocking conditions. They cannot be combined into a single compound check.

**Do not begin Section 7 until all six gate items (a)–(f) are confirmed for every tier.**

---

### SECTION 7 — MITIGATION PRESCRIPTIONS

For each burst path and bottleneck: named mitigation, BEFORE state (specific baseline behavior), AFTER state (specific behavior with mitigation). Update Section 4 PROTECTED column by mitigation name.

---

### SECTION 8 — QUANTIFIED IMPACT

Schema A table. 5x load spike on binding constraint. DERIVATION CHAIN: five-step arithmetic chain using Section 2 registry values. Inline flag any DERIVATION CHAIN cell failing CONTENT REJECTION CLAUSE.

---

### SECTION 9 — TERMINAL RECONCILER

Checks (a)–(d). Named finding record.

**(a) Verdict Revision Marker Audit:** Confirm REVISED markers present at revising section boundaries for any revised Claim (a)–(d).

**(b) Gate Deliverable Audit:** Enumerate each section's gate conditions. Confirm named deliverables present.

**(c) Schema A DERIVATION CHAIN Audit:** Flag conclusion-only cells.

**(d) Schema B Dual Audit:**
- Structural scan: count field labels per tier. Flag missing labels (STRUCTURAL).
- Content scan: flag generic/non-specific field content (CONTENT).
- **Confirm that Section 6 Gate Item (e) cited Section 3 as resolution source** — not Verdict Claim (d). If Verdict Claim (d) was the stated resolution path for gate item (e), flag as a gate independence violation.

**Reconciler Findings:** Total violation count and itemized list if non-zero.

---

**Scenario:** [INSERT SCENARIO HERE]

---

## V-05 — Combined Axis: Complete Gate Chain + Four-Clause Format Contract + Document-Head Verdict + Six-Item UX Gate Independence

**Axis:** All four axes combined — (1) complete gate chain closure with 10 analysis sections each carrying explicit gate conditions naming prior deliverables; (2) Format Contract preamble declaring Schema A and Schema B each with STRUCTURAL and CONTENT rejection clauses (four total); (3) document-head Verdict block with Claim (d) and bidirectional revision marking at every gate boundary; (4) six-item UX gate with item (e) analytically independent from Verdict.

**Hypothesis:** The four structural axes are mutually reinforcing rather than redundant: Format Contract violations are detectable at scan time and read time; gate conditions block section entry without prior deliverables; Verdict revision marking catches analysis drift at each boundary; UX gate independence prevents circular Verdict dependency. Together they create three independent detection mechanisms (schema enforcement, gate enforcement, Verdict currency) operating across three event types (scan, gate, revision) that no single axis achieves alone.

---

You are a Connectors and Power Automate throughput domain expert. Analyze the rate-limited system scenario below. Your output follows the 10-section structure. Every section transition is gated. The Verdict block is first. The Format Contract is second. No analysis section begins without its gate satisfied.

---

### PREAMBLE A — VERDICT BLOCK

First named element. Standalone. A reader who reads only this block knows the core finding.

**Claim (a) — Binding Constraint:** [Component] at [N] per [interval] — first limit reached as load increases.

**Claim (b) — Primary Gap:** [Trigger/action name] is an unprotected burst path — no concurrency cap, no queue buffer, no Retry-After handler between it and [endpoint]. Classification: STRUCTURAL or INCIDENTAL.

**Claim (c) — System Status:** [SAFE / DEGRADED / FAILING] at [stated load]. [One sentence tying load to threshold.]

**Claim (d) — UX Coverage:** [N] distinct throttle tiers; all [N] will be documented using Schema B four-field template. Mark REVISED if tier count changes or any tier lacks complete four-field coverage.

**Revision Protocol:**
- Any section that revises a Claim inserts REVISED — see Section [N] immediately after the Claim text at the revising section's boundary
- Revision must be inserted at the boundary of the revising section — not deferred to terminal reconciliation
- Terminal Reconciler (Section 10) audits for staleness (revised but unmarked) and phantom (marked but no revision in cited section)

**Gate to Preamble B:** Preamble A must contain all four Claims as separately enumerable entries before Preamble B begins.

---

### PREAMBLE B — FORMAT CONTRACT

Second named element. Before any analysis section.

**Schema A — Comparative Analysis Tables**

Every table containing quantified data uses three mandatory columns:

| BASELINE | PROTECTED | DERIVATION CHAIN |
|---|---|---|
| Current system behavior at stated load, specific to named component | System behavior with named mitigation applied, specific to named mitigation | Step-by-step computation referencing Section 1 registry values by name |

**Schema A — STRUCTURAL REJECTION CLAUSE:**
Clause type: STRUCTURAL | Detection: scan-time (examine column headers) | Violation: required column header absent | Action: flag table INCOMPLETE | Remediation: add missing column

**Schema A — CONTENT REJECTION CLAUSE:**
Clause type: CONTENT | Detection: read-time (examine cell content row by row) | Violation: DERIVATION CHAIN cell contains conclusion only, or BASELINE/PROTECTED cell contains generic non-component-specific text | Action: flag cell INCOMPLETE (CONTENT) with table and row reference | Remediation: replace with computation chain or component-specific description

**Schema B — UX Tier Template**

Every throttle tier block uses four named fields:

```
Tier [N] — [Name]
(a) Error Code or Platform Signal: [exact error code, event name, or platform signal]
(b) User-Visible Behavior: [what the user observes — specific to this tier]
(c) Visibility Level: [USER-VISIBLE EXPLICIT | USER-VISIBLE IMPLICIT | SILENT-BACKGROUND]
(d) Recovery Path: [named specific mechanism available to user or system]
```

**Schema B — STRUCTURAL REJECTION CLAUSE:**
Clause type: STRUCTURAL | Detection: scan-time (count field labels a–d in tier block) | Violation: any field label absent | Action: flag tier block INCOMPLETE (STRUCTURAL) | Remediation: add missing field label(s)

**Schema B — CONTENT REJECTION CLAUSE:**
Clause type: CONTENT | Detection: read-time (examine field content after confirming all four labels present) | Violation: any field populated with (i) generic text not specific to this tier, (ii) conclusion-only text without mechanism, or (iii) copy of another tier's field without justification | Action: flag specific field INCOMPLETE (CONTENT) with tier and field label | Remediation: replace with scenario-specific content for this tier

**Four Named Rejection Clauses Total:** Schema A STRUCTURAL, Schema A CONTENT, Schema B STRUCTURAL, Schema B CONTENT. Each has: (a) distinct clause name, (b) detection method stated (scan-time vs. read-time), (c) remediation specific to that violation type. Violation of one clause is not a violation of the others — checked independently.

**Gate to Section 1:** Preamble B must contain all four rejection clauses with distinct names, detection methods, and remediations before Section 1 begins.

---

### SECTION 1 — RATE LIMIT REGISTRY

Enumerate every rate limit: component | threshold | interval | scope. Label estimates. This registry is the sole numeric source for all DERIVATION CHAIN cells.

**Verdict Currency Check:** If the binding constraint named in Claim (a) is absent from the registry with its stated threshold, or if a lower threshold exists for a different component, insert REVISED — see Section 1 on Claim (a) at this boundary before proceeding.

**Gate to Section 2:** Section 1 must contain at least one registry entry with all four fields (component, threshold, interval, scope) populated. Claim (a) binding constraint must appear in the registry or must be marked REVISED before Section 2 begins.

---

### SECTION 2 — BURST PATH AUDIT

**This section is the sole authoritative source for Section 6 Gate Item (e) tier count.**

Schema A burst path table: BURST PATH | BASELINE | PROTECTED | DERIVATION CHAIN.

For each unprotected burst path: name the trigger/action and target endpoint (BURST PATH column); show requests generated vs. threshold saturation at baseline (BASELINE); show behavior with named mitigation applied (PROTECTED — update after Section 8); show saturation computation (DERIVATION CHAIN). Classify STRUCTURAL or INCIDENTAL.

**Verdict Currency Check:** If burst path audit revises Claim (b) (different path is primary gap) or Claim (d) (tier count implied differs from stated), insert REVISED — see Section 2 on affected Claim(s) at this boundary.

**Gate to Section 3:** Section 2 must contain at least one burst path row satisfying all three Schema A columns with substantive (non-generic) content. Any Schema A violations must be flagged inline.

---

### SECTION 3 — RETRY-AFTER GAP EVALUATION

For each Section 1 endpoint: YES / NO / PARTIAL Retry-After handling. Failure mode for each non-YES entry.

**Verdict Currency Check:** If missing Retry-After handling changes system status, insert REVISED — see Section 3 on Claim (c) at this boundary.

**Gate to Section 4:** Every Section 1 endpoint has a YES/NO/PARTIAL verdict and, for non-YES, a failure mode description before Section 4 begins.

---

### SECTION 4 — CASCADING THROTTLE SCENARIO

Name both tiers (with Section 1 thresholds) and the causal mechanism by which Tier 1 throttling causes Tier 2 to be hit. Or state explicitly that no cascade is structurally possible with justification.

**Verdict Currency Check:** Check all four Claims for revision signals from the cascade analysis. Insert markers at this boundary if warranted.

**Gate to Section 5:** Cascading scenario either (a) names both tiers with numeric thresholds and a causal mechanism, or (b) explicitly states no cascade is possible with justification, before Section 5 begins.

---

### SECTION 5 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table, three+ volume tiers. DERIVATION CHAIN: compute volume / threshold = saturation ratio using Section 1 registry values. PROTECTED column updated after Section 8 mitigations. Apply Schema A rejection clauses inline.

**Verdict Currency Check:** If volume mapping revises Claim (c) system status, insert REVISED — see Section 5 on Claim (c) at this boundary.

**Gate to Section 6:** Section 5 must contain at least three volume tier rows with all three Schema A columns substantively populated. DERIVATION CHAIN cells must cite registry values by name, not use generic round numbers.

---

### SECTION 6 — UX PER-TIER ANALYSIS (Explicitly Numbered Role)

Apply Schema B to every throttle tier. Apply Schema B rejection clauses inline.

**SIX-ITEM GATE — all six required before Section 7:**

**(a) FIELD-A:** Field label (a) Error Code or Platform Signal present and populated with the exact code, event name, or connector error specific to this tier — not generic — for every tier.

**(b) FIELD-B:** Field label (b) User-Visible Behavior present and describes the specific observable outcome at this tier — names the UI state, message text, or flow run status — for every tier.

**(c) FIELD-C:** Field label (c) Visibility Level present and states USER-VISIBLE EXPLICIT, USER-VISIBLE IMPLICIT, or SILENT-BACKGROUND for every tier.

**(d) FIELD-D:** Field label (d) Recovery Path present and names the specific mechanism (named action, policy, or manual step) — not "retry" as a generic term — for every tier.

**(e) TIER COUNT INDEPENDENCE — resolve via Section 2 only:**
Count the unprotected burst paths enumerated in Section 2. Determine how many distinct throttle tiers those paths encounter. This section must document UX behavior for each of those tiers. **The resolution path for this item is Section 2 (Burst Path Audit) — not Verdict Claim (d) and not any other Verdict-block item.** A gate verifier resolves item (e) by reading Section 2's burst path table, not by reading the Verdict block. If this section's tier count differs from Section 2's burst path count: insert REVISED — see Section 6 on Verdict Claim (d) at this gate boundary — before proceeding.

A gate item (e) phrased as "consistent with Verdict Claim (d)" does not pass, even if Claim (d) is current. A gate item (e) that cites both Section 2 and Verdict Claim (d) as co-equal sources does not pass — Section 2 must be the stated resolution path.

**(f) STRUCTURE COMPLIANCE:** Each tier uses the Schema B four-field labeled template — field labels (a)–(d) present, content in the labeled fields. Free prose covering the same topics without the field labels does not pass.

Do not begin Section 7 until all six items (a)–(f) are confirmed. Items (e) and (f) are separately named blocking conditions — they cannot be collapsed.

**Verdict Currency Check at Section 6 close:** Having resolved gate item (e) against Section 2, check Claim (d) currency — if tier count has changed, confirm REVISED marker was inserted at the gate boundary. If the marker was not inserted during gate processing, insert it now and note that it was deferred.

---

### SECTION 7 — MITIGATION PRESCRIPTIONS

For each burst path and bottleneck from Sections 2 and 3: named mitigation (specific action/setting/pattern), BEFORE state (baseline behavior at component), AFTER state (behavior with mitigation). Update Section 2 and Section 5 PROTECTED columns by mitigation name.

**Verdict Currency Check:** If mitigations revise any Claim, insert markers at this boundary.

**Gate to Section 8:** Every burst path from Section 2 and every Retry-After gap from Section 3 has a named mitigation with BEFORE and AFTER states. Section 2 and Section 5 PROTECTED columns reflect the named mitigations.

---

### SECTION 8 — QUANTIFIED IMPACT

Schema A table. 5x load spike on binding constraint from Claim (a). DERIVATION CHAIN five-step chain:
1. Baseline rate × 5 = peak
2. Peak − [Section 1 threshold for Claim (a) component] = overflow
3. Overflow × retry factor = failed requests
4. Failed ÷ peak = failure %
5. Each step names the specific Section 1 registry values used

Inline flag any DERIVATION CHAIN cell failing Schema A CONTENT REJECTION CLAUSE.

**Verdict Currency Check:** If quantified impact revises Claim (c), insert REVISED — see Section 8 on Claim (c) at this boundary.

**Gate to Section 9:** Section 8 must contain the five-step arithmetic chain in the DERIVATION CHAIN column with each step showing specific numeric values from the Section 1 registry.

---

### SECTION 9 — VERDICT CURRENCY CHECK

Pre-terminal reconciliation pass. Review Claims (a)–(d):

1. For each Claim, state whether it was confirmed, revised, or left unchallenged by Sections 1–8
2. For each revised Claim: confirm the REVISED — see Section [N] marker appears at the boundary of the revising section
3. For any marker not inserted at the revising boundary: insert now, note it was deferred (this is a C-22 violation to be reported in Section 10)

This section produces analysis, not new findings. It prepares for terminal reconciliation.

**Gate to Section 10:** All four Claims have been explicitly reviewed for currency and any missing boundary-level markers have been inserted (with deferral noted).

---

### SECTION 10 — TERMINAL RECONCILER

Last named section. Four named checks. One named finding record.

**Check (a) — Verdict Revision Marker Audit:**
Scan Verdict Claims (a)–(d). For each Claim:
- Confirm that revision markers inserted at section boundaries are present for each revision event
- Identify staleness violations: Claim revised by evidence but no REVISED marker present
- Identify phantom violations: REVISED marker present but no revision in the cited section
- Identify deferral violations: marker present but Section 9 noted it was deferred from the revising boundary (C-22 target violation)

**Check (b) — Gate Deliverable Audit:**
Enumerate each gate condition: Preamble A→B, B→1, 1→2, 2→3, 3→4, 4→5, 5→6, 6→7, 7→8, 8→9, 9→10. For each gate, confirm the named prior-section deliverables are present. List any gate whose named deliverable is absent as a violation.

**Check (c) — Schema A DERIVATION CHAIN Audit:**
Identify any DERIVATION CHAIN cell in any Schema A table containing only a conclusion without computation steps. Flag each as INCOMPLETE (CONTENT) with table section, row, and column reference.

**Check (d) — Schema B Dual Audit:**
- Structural scan: count field labels (a)–(d) in each tier block. Flag any missing label as a STRUCTURAL violation with tier name and missing label.
- Content scan: for each tier block with all four labels present, assess whether each field contains scenario-specific content. Flag generic, non-scenario-specific content as a CONTENT violation with tier name and field label.
- Gate Item (e) Independence Audit: confirm that Section 6 Gate Item (e) cited Section 2 as its resolution source — not Verdict Claim (d). If Verdict Claim (d) appears as the resolution path, flag as a GATE INDEPENDENCE VIOLATION.

**Reconciler Findings:**
State the total violation count across all four checks. If zero: "Reconciler Findings: 0 violations — document complete and structurally closed." If violations exist, produce an itemized list: each violation with section reference, check letter, clause type, and remediation action required.

A reconciler section that performs scans without producing this named finding record does not close.

---

**Scenario:** [INSERT SCENARIO HERE — describe: the Power Automate flow structure, connectors invoked, trigger type and estimated event rate, target APIs and their rate limits if known, and the peak load volume to analyze]

---

*End of Round 11 Variations — V-01 through V-05*
