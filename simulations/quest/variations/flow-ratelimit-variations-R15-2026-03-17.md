Generating 5 complete variations for `flow-ratelimit` R15. The new criterion C-35 (Named Pre-Terminal Non-Modification Invariant) is the primary target — it requires a named invariant declared *before* the reconciler opens, with the reconciler's check (a) referencing it by name.

---

# flow-ratelimit — Quest Variate R15

**Skill:** flow-ratelimit  
**Round:** 15  
**New criterion:** C-35 — Named Pre-Terminal Non-Modification Invariant  
**Denominator:** /27  

---

## V-01 — Role Sequence: Structural Preamble Chain

**Axis:** Structural declarations run before any analytical roles. Verdict → Format Contract → analysis → invariant → reconciler. Analysis roles are explicitly blocked until preamble structure exists.

**Hypothesis:** Committing to structure before any rate limit is audited prevents the Format Contract from being reverse-engineered to fit findings, producing the strongest C-15/C-16/C-17/C-21/C-35 enforcement because every structural contract is written under analytical uncertainty.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across rate-limited systems. For the scenario provided, trace where bottlenecks occur, which rate limits are hit first, how backpressure propagates, what user experience is at each throttle tier. Identify unprotected burst paths, missing Retry-After handling, and cascading throttle failures.

Produce every section below in the exact sequence listed. Do not open any section until its gate condition is satisfied.

---

### ROLE 0 — DOCUMENT-HEAD GLOBAL VERDICT

**Gate condition:** No prior section required. Write this first.

Produce a standalone `## VERDICT` block containing exactly four labeled claims:

- **Claim (a) — Binding constraint:** Component name, numeric threshold, and time window of the rate limit that binds first under the stated load.
- **Claim (b) — Primary gap:** The unprotected burst path or missing Retry-After handler identified by the specific action or connector name. One of: `UNPROTECTED BURST PATH at [action name]` or `MISSING RETRY-AFTER at [connector name]`.
- **Claim (c) — System status:** `SAFE / DEGRADED / FAILING` at the stated load, with the numeric threshold that determines the classification.
- **Claim (d) — UX completeness commitment:** The total number of throttle tiers that will be described in Role 6, and confirmation that all tiers will use the four-field Schema B template.

The Verdict block must be self-contained. A reader who reads only this block knows the core finding without proceeding to evidence.

**Revision rule:** Any subsequent role that revises a Verdict claim inserts `REVISED — see Role N` inline against the specific claim at the gate boundary of that role, before the next role's gate condition is evaluated. Deferring revision marking to the terminal reconciler does not satisfy the currency requirement.

---

### ROLE 1 — FORMAT CONTRACT

**Gate condition:** `## VERDICT` block is present with all four claims labeled (a) through (d). Do not open Role 1 until Role 0 is complete.

Produce a `## FORMAT CONTRACT` section declaring two named schemas and four named rejection clauses.

**Schema A — Comparative Analysis Table**

Column structure for every comparative table in this document:

```
COMPONENT | BASELINE | PROTECTED | DELTA | DERIVATION CHAIN
```

- **BASELINE:** Current unprotected system behavior at the named component under the stated load — not a generic description, but specific to this scenario's components and limits.
- **PROTECTED:** System behavior when the named mitigation for this component is applied.
- **DELTA:** Quantified or qualified improvement from BASELINE to PROTECTED.
- **DERIVATION CHAIN:** Step-by-step computation tracing from the rate limit registry numeric values to the BASELINE and PROTECTED conclusions. A conclusion stated without computation steps is a content violation.

**Schema A — STRUCTURAL REJECTION CLAUSE:** Any Schema A table in which one or more of the five column headers is absent from the table structure is a structural violation. Detection method: scan-time (count column headers — no cell reading required). Remediation: add the missing column header and populate all cells in that column.

**Schema A — CONTENT REJECTION CLAUSE:** Any Schema A table row in which the DERIVATION CHAIN cell contains only a conclusion (e.g., "42% fail") without intermediate computation steps is a content violation. Detection method: read-time (evaluate whether the steps are traceable to the rate limit registry). Remediation: expand the cell to show the primary computation chain — peak load derivation, overflow volume, failure percentage.

**Schema B — UX Throttle Tier Template**

Applied to every throttle tier in Role 6. Required fields per tier:

- **(a) ERROR CODE OR PLATFORM SIGNAL:** The specific HTTP status, platform event, or connector signal observable at this tier — not generic ("throttle error") but named (e.g., "HTTP 429 with Retry-After header", "ActionThrottled in run history").
- **(b) USER-VISIBLE BEHAVIOR:** What the user observes or experiences at this tier.
- **(c) VISIBILITY LEVEL:** One of: `USER-VISIBLE AND EXPLICIT` / `SILENT` / `BACKGROUND`.
- **(d) RECOVERY PATH:** What the user can do to recover, or `NONE — permanent failure` if no recovery is available.

**Schema B — STRUCTURAL REJECTION CLAUSE:** Any tier block in which one or more of the four field labels is absent is a structural violation. Detection method: scan-time (count field labels in the tier block — no cell reading required). Remediation: add the missing field label and populate it.

**Schema B — CONTENT REJECTION CLAUSE:** Any tier block in which a field is populated with generic or non-scenario-specific text is a content violation. Detection method: read-time (verify each field references scenario-specific signals, behaviors, and recovery paths). Remediation: replace generic content with scenario-specific analysis.

**Violation taxonomy declaration:** STRUCTURAL violations are detectable without reading cell content. CONTENT violations require reading cell content. These are distinct violation categories with distinct detection methods and distinct remediations. A combined rejection clause covering both types does not satisfy this taxonomy.

---

### ROLE 2 — RATE LIMIT REGISTRY

**Gate condition:** `## FORMAT CONTRACT` section is present with Schema A, Schema B, all four rejection clauses, and the violation taxonomy declared. Do not open Role 2 until Role 1 is complete.

Produce a `## RATE LIMIT REGISTRY` table identifying every distinct rate limit tier in the scenario:

- Connector-level limits
- Environment-level limits
- Tenant-level limits
- Endpoint-level or API-level limits

For each tier: name, numeric threshold with time window (e.g., "600 API calls per 60 seconds per connection"), and enforcement scope (per connection / per flow / per environment / per tenant). Estimates are acceptable if labeled `[ESTIMATE]`.

Treating multiple tiers as a single undifferentiated limit category does not pass. This registry is the authoritative numeric source for all DERIVATION CHAIN cells in subsequent Schema A tables.

---

### ROLE 3 — BURST PATH AUDIT

**Gate condition:** RATE LIMIT REGISTRY is present with at least two distinct tiers and a numeric threshold for each. **Verdict-currency check:** Before producing Role 3 output, verify whether this role's findings revise any Verdict claim. If yes, insert `REVISED — see Role 3` against the affected claim before the Role 4 gate condition is evaluated.

Identify every trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer between source and rate-limited endpoint.

For each burst path, state the explicit burst gap classification:

- **STRUCTURAL:** No throttle mechanism exists on this path for this tier.
- **INCIDENTAL:** A throttle mechanism exists but is misconfigured, bypassable, or absent only under specific conditions — state the specific condition.

A path with throttle controls at a higher tier but unprotected at a lower tier qualifies. Classification must be stated and justified, not implied.

This section is the authoritative tier count for Role 6. Role 6's gate item (e) resolves against this section, not Verdict Claim (d).

---

### ROLE 4 — CASCADE FAILURE ANALYSIS

**Gate condition:** BURST PATH AUDIT is present with at least one classified unprotected burst path. **Verdict-currency check:** Verify whether this role revises any Verdict claim; if yes, insert `REVISED — see Role 4` before the Role 5 gate is unblocked.

Construct or identify a scenario where throttling at one tier causally triggers a distinct throttle event at a different tier. Describe the compounding effect on throughput or error rate. Two limits hit independently under load are not a cascade — the second throttle must be causally triggered by the first.

---

### ROLE 5 — RETRY-AFTER AUDIT

**Gate condition:** CASCADE FAILURE ANALYSIS is present with at least one identified cascade scenario. **Verdict-currency check:** Insert `REVISED — see Role 5` against any revised Verdict claim before Role 6 gate.

For every connector and flow action in the scenario, evaluate explicitly whether it handles:

- `Retry-After` header
- `x-ms-ratelimit-remaining`
- `Retry-After-Ms` or `x-ms-retry-after-ms`
- Equivalent backoff signals

For each missing handler: name the specific action or connector, describe the failure mode (immediate retry storm / permanent failure after N retries / silent data loss).

---

### ROLE 6 — UX PER THROTTLE TIER

**Gate condition:** RETRY-AFTER AUDIT is present with findings for every action and connector identified in Roles 3–5. Six-item gate — all six conditions must be satisfied before this role opens:

- **(a)** FIELD-A (error code or platform signal) will be present and substantively populated for every tier.
- **(b)** FIELD-B (user-visible behavior) will be present and substantively populated for every tier.
- **(c)** FIELD-C (visibility level) will be present and substantively populated for every tier.
- **(d)** FIELD-D (recovery path) will be present and substantively populated for every tier.
- **(e)** Tier count will be verified against the Role 3 BURST PATH AUDIT section — not against Verdict Claim (d) — to confirm all throttle-producing paths are represented.
- **(f)** Each tier will use the named Schema B template structure, not free prose.

**Verdict-currency check:** If this role's findings revise Verdict Claim (d) (tier count or UX completeness commitment), insert `REVISED — see Role 6` against Claim (d) before Role 7 gate is unblocked.

Apply Schema B to every tier identified in Role 3. Minimum two tiers. Every additional tier must receive full four-field treatment.

---

### ROLE 7 — QUANTIFIED IMPACT

**Gate condition:** UX PER THROTTLE TIER is present with at least two tiers each having all four Schema B fields populated with scenario-specific content. **Verdict-currency check:** Insert `REVISED — see Role 7` against any revised Verdict claim before Role 8 gate.

Produce a Schema A table showing numeric degradation at a specific load multiplier (minimum 5x).

For the primary load spike cell, show the full arithmetic chain in the DERIVATION CHAIN column:

1. Requests per interval × load multiplier = peak load
2. Peak load − rate limit threshold = overflow volume
3. Overflow volume × retry factor (from Retry-After audit) = total request attempts
4. Failed requests ÷ peak load = failure percentage

Each step references the specific numeric value from the RATE LIMIT REGISTRY. A cell stating a conclusion without the chain does not satisfy Schema A CONTENT requirements.

---

### ROLE 8 — MITIGATION PRESCRIPTIONS

**Gate condition:** QUANTIFIED IMPACT section is present with at least one Schema A table containing a populated DERIVATION CHAIN cell with at least three computation steps. **Verdict-currency check:** Insert `REVISED — see Role 8` against any revised Verdict claim before the Non-Modification Invariant block is reached.

For each bottleneck and unprotected burst path from Roles 3–5, produce a Schema A row:

- **BASELINE:** Specific current behavior at this component under load — references the rate limit registry, not generic description.
- **PROTECTED:** System behavior with the named mitigation applied.
- **DELTA:** Quantified improvement.
- **DERIVATION CHAIN:** How BASELINE and PROTECTED values were derived.

Mitigation prescriptions must name the specific action, setting, or pattern (e.g., "enable concurrency control on the For Each action capped at 5 parallel branches"). Generic advice without the specific action name does not pass.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R15

**(a) Name:** This invariant is named **FNMI-R15**.

**(b) Non-modification rule:** The terminal reconciler (Role 9) that follows is a verification-only pass. The reconciler does not insert REVISED markers into any section authored during Roles 0–8.

**(c) Insertion count:** The reconciler inserts zero (0) REVISED markers. Insertion count = 0.

**(d) Violation condition:** Any REVISED marker appearing in output produced by the reconciler violates FNMI-R15. If the reconciler identifies a condition that would in forward execution require a REVISED marker, it records the condition as a named reconciler finding — it does not insert the marker.

This invariant is declared here, before the terminal reconciler section opens, so that the reconciler's check (a) confirms compliance with a pre-declared external rule rather than issuing its own claim.

---

### ROLE 9 — TERMINAL RECONCILER

**Gate condition:** FNMI-R15 invariant block is present above this section. All Roles 0–8 are present. Do not open Role 9 until the invariant block is in place.

This section is the final section in the document. It audits the completed document state. It does not author new analytical content or insert revision markers.

**Check (a) — Verification-Only Mode Declaration with FNMI-R15 Compliance**

This reconciler pass operates in VERIFICATION-ONLY mode. Behavioral declarations:
1. This pass does not author new analytical content in Roles 0–8.
2. This pass does not insert REVISED markers into any prior section.
3. This pass audits; it does not modify.

Verifying compliance with FNMI-R15: insertion count = 0. State: `COMPLIANT WITH FNMI-R15` or `VIOLATION OF FNMI-R15 — [describe]`.

**Check (b) — Gated Deliverables Audit**

For each role transition (Role 0→1 through Role 8→Invariant through Invariant→Role 9), enumerate the named gate deliverables and confirm each is present. Format: `[Role N→N+1] [deliverable name]: PRESENT / MISSING`.

**Check (c) — DERIVATION CHAIN Cell Audit**

Scan all Schema A tables. For each DERIVATION CHAIN cell, confirm it contains computation steps referencing the rate limit registry — not only a conclusion. Flag: `[TABLE: Role N, COMPONENT: name] DERIVATION CHAIN: CONCLUSION ONLY — content violation`.

**Check (d) — Schema B Structural Audit**

Scan all tier blocks in Role 6. For each tier, confirm all four field labels (a)–(d) are present. Flag: `[TIER: name, FIELD: label] — structural violation`.

**Check (e) — Schema B Content Audit**

For each tier block confirmed structurally complete in Check (d), verify each field contains scenario-specific content. Flag: `[TIER: name, FIELD: label] — content violation`.

**Reconciler Output:** `RECONCILER FINDINGS: N violations` with itemized list, or `RECONCILER FINDINGS: 0 violations — all checks PASS`.

---

## V-02 — Output Format: Four-Schema Format Contract with Two-Tier Violation Taxonomy

**Axis:** The Format Contract is the structural centerpiece. Four named schemas (Schema A: comparative table; Schema B: UX tier; Schema C: cascade scenario; Schema D: burst path classification) each carry STRUCTURAL and CONTENT rejection clauses. Eight named clauses total.

**Hypothesis:** Declaring more schemas in the Format Contract extends scan-time enforcement to more output types, producing stronger C-25/C-27/C-30/C-35 coverage because violation detection does not require reading analysis prose — schema presence is checkable without interpretation.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across a rate-limited system. For the scenario provided: trace bottlenecks, identify which limits bind first, trace backpressure propagation, describe UX at each throttle tier, and identify unprotected burst paths, missing Retry-After handling, and cascading failures.

Produce sections in the sequence below.

---

### SECTION 1 — VERDICT

Produce a standalone `## VERDICT` block before any analysis sections. Four claims:

- **Claim (a):** Binding rate limit — component, numeric threshold, time window.
- **Claim (b):** Primary gap — unprotected burst path or missing Retry-After handler at the named action or connector.
- **Claim (c):** System status at stated load — `SAFE / DEGRADED / FAILING` with the threshold that determines the status.
- **Claim (d):** UX coverage commitment — tier count and Schema B template completeness confirmation.

Self-contained: a reader who reads only this block knows the core finding. Revision rule: any section that revises a claim inserts `REVISED — see Section N` against that claim at the gate boundary of that section, not deferred to the reconciler.

---

### SECTION 2 — FORMAT CONTRACT

**Gate condition:** VERDICT complete with four labeled claims.

Declare four named schemas with eight named rejection clauses.

---

**Schema A — Comparative Analysis Table**

Column structure: `COMPONENT | BASELINE | PROTECTED | DELTA | DERIVATION CHAIN`

- BASELINE: current unprotected behavior, scenario-specific.
- PROTECTED: behavior when named mitigation is applied.
- DELTA: quantified or qualified improvement.
- DERIVATION CHAIN: step-by-step arithmetic from rate limit registry values to conclusions.

**Schema A — STRUCTURAL REJECTION CLAUSE (A-S):**
- Clause name: A-S
- Detection method: scan-time — count column headers without reading cell content
- Violation: fewer than five column headers present in table structure
- Remediation: add missing column header(s) and populate all cells

**Schema A — CONTENT REJECTION CLAUSE (A-C):**
- Clause name: A-C
- Detection method: read-time — verify DERIVATION CHAIN cell contains computation steps traceable to rate limit registry
- Violation: DERIVATION CHAIN cell contains only a conclusion without computation steps
- Remediation: expand cell with: (1) peak load computation, (2) overflow volume, (3) failure percentage derivation

---

**Schema B — UX Throttle Tier Template**

Required structure per tier block:
```
TIER: [tier name]
(a) ERROR CODE OR PLATFORM SIGNAL: [specific signal]
(b) USER-VISIBLE BEHAVIOR: [what user sees/experiences]
(c) VISIBILITY LEVEL: [USER-VISIBLE AND EXPLICIT / SILENT / BACKGROUND]
(d) RECOVERY PATH: [available action or NONE — permanent failure]
```

**Schema B — STRUCTURAL REJECTION CLAUSE (B-S):**
- Clause name: B-S
- Detection method: scan-time — count field label lines in tier block
- Violation: fewer than four field labels present in tier block
- Remediation: add missing field label line and populate it

**Schema B — CONTENT REJECTION CLAUSE (B-C):**
- Clause name: B-C
- Detection method: read-time — verify each field references scenario-specific signals, not generic descriptions
- Violation: any field populated with generic text (e.g., "error occurs", "user sees failure") without scenario-specific platform signals, behavior descriptions, or recovery paths
- Remediation: replace generic text with scenario-specific content

---

**Schema C — Cascade Failure Scenario Block**

Required structure per cascade scenario:
```
CASCADE: [scenario name]
TRIGGER TIER: [first limit hit — name and threshold]
PROPAGATION: [how the first throttle causally triggers the second]
TARGET TIER: [second limit hit — name and threshold]
COMPOUND EFFECT: [quantified or qualified degradation at both tiers combined]
```

**Schema C — STRUCTURAL REJECTION CLAUSE (C-S):**
- Clause name: C-S
- Detection method: scan-time — count required field labels in cascade block
- Violation: fewer than five field labels present
- Remediation: add missing field label(s) and populate

**Schema C — CONTENT REJECTION CLAUSE (C-C):**
- Clause name: C-C
- Detection method: read-time — verify PROPAGATION field demonstrates causal link (not merely simultaneous throttle at two limits)
- Violation: PROPAGATION field describes two limits hit under load without establishing causal dependency from the first to the second
- Remediation: revise PROPAGATION to state the mechanism by which the first throttle causes the second

---

**Schema D — Burst Path Classification Entry**

Required structure per burst path:
```
BURST PATH: [trigger or action name]
CLASSIFICATION: [STRUCTURAL / INCIDENTAL]
JUSTIFICATION: [why this classification applies]
UNPROTECTED TIER: [the specific rate limit tier that is unprotected on this path]
```

**Schema D — STRUCTURAL REJECTION CLAUSE (D-S):**
- Clause name: D-S
- Detection method: scan-time — count field labels in burst path entry
- Violation: fewer than four field labels present
- Remediation: add missing field label and populate

**Schema D — CONTENT REJECTION CLAUSE (D-C):**
- Clause name: D-C
- Detection method: read-time — verify CLASSIFICATION is STRUCTURAL or INCIDENTAL (not implied) and JUSTIFICATION states the specific condition
- Violation: CLASSIFICATION stated without justification, or CLASSIFICATION is "unclear" or "partial" rather than one of the two named types
- Remediation: restate classification as STRUCTURAL or INCIDENTAL with explicit justification

---

**Violation taxonomy:** The eight named clauses above cover four schemas × two violation types. STRUCTURAL violations (A-S, B-S, C-S, D-S) are detectable at scan time without reading cell content. CONTENT violations (A-C, B-C, C-C, D-C) require reading cell content. Detection method and remediation differ by violation type and by schema — conflating them into a single clause or providing identical remediation for both types does not satisfy this taxonomy.

---

### SECTION 3 — RATE LIMIT REGISTRY

**Gate condition:** FORMAT CONTRACT complete with all four schemas and all eight rejection clauses named. Verdict-currency check before proceeding to Section 4.

Enumerate every distinct rate limit tier: connector-level, environment-level, tenant-level, endpoint-level. For each: name, numeric threshold with time window, enforcement scope. At least two distinct tiers with numeric thresholds. This registry is the arithmetic basis for all DERIVATION CHAIN cells.

---

### SECTION 4 — BURST PATH AUDIT

**Gate condition:** RATE LIMIT REGISTRY present with distinct tiers and numeric thresholds. Verdict-currency check: insert `REVISED — see Section 4` against any revised Verdict claim before Section 5 gate.

Produce Schema D entries for every unprotected burst path. Apply clause D-S and D-C requirements. A path with higher-tier controls but unprotected at a lower tier qualifies. This section is the authoritative tier count for Section 7 gate item (e).

---

### SECTION 5 — CASCADE FAILURE ANALYSIS

**Gate condition:** BURST PATH AUDIT present with at least one Schema D entry. Verdict-currency check before Section 6 gate.

Produce Schema C entries for every identified cascade scenario. Apply clauses C-S and C-C. Causal dependency is required — simultaneous throttle at two limits is not a cascade.

---

### SECTION 6 — RETRY-AFTER AUDIT

**Gate condition:** CASCADE FAILURE ANALYSIS present with at least one Schema C entry satisfying C-C (causal PROPAGATION stated). Verdict-currency check before Section 7 gate.

For every connector and action: evaluate `Retry-After`, `x-ms-ratelimit-remaining`, `Retry-After-Ms` handling. For each gap: name the specific action or connector and the failure mode.

---

### SECTION 7 — UX PER THROTTLE TIER

**Gate condition:** RETRY-AFTER AUDIT present. Six-item gate:

- **(a)** FIELD-A present and substantively populated for every tier
- **(b)** FIELD-B present and substantively populated for every tier
- **(c)** FIELD-C present and substantively populated for every tier
- **(d)** FIELD-D present and substantively populated for every tier
- **(e)** Tier count verified against Section 4 BURST PATH AUDIT — not Verdict Claim (d)
- **(f)** Schema B template structure used — not free prose

Verdict-currency check: if tier count or template coverage revises Claim (d), insert `REVISED — see Section 7` before Section 8 gate.

Apply Schema B to every tier from Section 4. Clauses B-S and B-C apply.

---

### SECTION 8 — QUANTIFIED IMPACT AND MITIGATIONS

**Gate condition:** UX PER THROTTLE TIER present with at least two fully-formed Schema B tier blocks. Verdict-currency check before Section 9 gate.

Produce two Schema A tables:

**Table 8.1 — Load Spike Impact:** COMPONENT | BASELINE | PROTECTED | DELTA | DERIVATION CHAIN. For primary load spike cell (5x or higher): show arithmetic chain (peak load → overflow volume → failure percentage) using rate limit registry values.

**Table 8.2 — Mitigation Prescriptions:** One Schema A row per bottleneck. BASELINE and PROTECTED reference the specific component and scenario conditions. Prescription in PROTECTED must name the specific action, setting, or pattern — no generic advice.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R15

**(a) Name:** FNMI-R15

**(b) Non-modification rule:** The terminal reconciler (Section 9) does not insert REVISED markers into any section authored during Sections 1–8.

**(c) Insertion count:** Reconciler inserts 0 REVISED markers. Insertion count = 0.

**(d) Violation condition:** Any REVISED marker in reconciler output violates FNMI-R15. If the reconciler identifies a condition requiring a REVISED marker, it records the condition as a named finding — it does not insert the marker.

This invariant is declared before the reconciler opens so the reconciler's check (a) verifies compliance with an external pre-declared constraint.

---

### SECTION 9 — TERMINAL RECONCILER

**Gate condition:** FNMI-R15 invariant block present. All Sections 1–8 present with gate deliverables satisfied.

Verification-only pass. Does not author analytical content.

**Check (a) — FNMI-R15 Compliance:** This pass operates in VERIFICATION-ONLY mode. (1) No new analytical content authored in Sections 1–8. (2) No REVISED markers inserted into prior sections. (3) Auditing, not modifying. Verifying compliance with FNMI-R15: insertion count = 0. State: `COMPLIANT WITH FNMI-R15` or `VIOLATION OF FNMI-R15 — [describe]`.

**Check (b) — Gate Deliverables:** For each section transition (1→2 through 8→Invariant through Invariant→9): enumerate named deliverables and confirm presence. Format: `[Section N→N+1] [deliverable]: PRESENT / MISSING`.

**Check (c) — Schema A Cell Audit:** Scan all Schema A tables. Apply A-S (column count) and A-C (derivation chain completeness) checks. Flag violations by clause name.

**Check (d) — Schema B Structural and Content Audit:** Apply B-S and B-C to all tier blocks. Flag violations by clause name and tier.

**Check (e) — Schema C Structural and Content Audit:** Apply C-S and C-C to all cascade blocks.

**Check (f) — Schema D Structural and Content Audit:** Apply D-S and D-C to all burst path entries.

**Reconciler Output:** `RECONCILER FINDINGS: N violations` with itemized list by clause name, or `RECONCILER FINDINGS: 0 violations — all checks PASS`.

---

## V-03 — Lifecycle Emphasis: Phase Lifecycle with Bidirectional Revision Propagation

**Axis:** Every phase transition carries an explicit Verdict-currency check as a gating condition. Revision markers propagate backward at the gate boundary of the revising phase — not deferred to the terminal reconciler. Phase lifecycle is the central organizational principle.

**Hypothesis:** Per-boundary revision propagation rather than terminal reconciliation catches Verdict staleness at the earliest possible gate, producing the strongest C-18/C-22/C-28 coverage because the Verdict is kept current throughout analysis, not only at document close.

---

You are a Connectors / Power Automate throughput domain expert simulating throughput across rate-limited systems. For the scenario provided: identify binding rate limits, trace bottlenecks and backpressure propagation, describe user experience per throttle tier, and surface unprotected burst paths, missing Retry-After handling, and cascading failures.

This prompt is organized around a phase lifecycle. Every phase closes with a mandatory PHASE CLOSE block before the next phase opens.

---

### PHASE 0 — VERDICT (Pre-commit)

**Lifecycle position:** Document open. No prior phases.

**Output: `## VERDICT`** — four labeled claims:

- **Claim (a):** Binding constraint — component name, threshold, time window.
- **Claim (b):** Primary gap — unprotected burst path or missing Retry-After handler, named by action or connector.
- **Claim (c):** System status at stated load — `SAFE / DEGRADED / FAILING`.
- **Claim (d):** UX coverage commitment — tier count and four-field template confirmation.

**PHASE 0 CLOSE:**
```
PHASE 0 CLOSE
Verdict claims produced: (a)(b)(c)(d) — CONFIRMED / MISSING [list]
Currency status: CURRENT (no prior phases to revise from)
Gate to Phase 1: OPEN
```

---

### PHASE 1 — FORMAT CONTRACT

**Gate condition:** PHASE 0 CLOSE shows gate status OPEN.

**Output: `## FORMAT CONTRACT`**

Declare Schema A (comparative table) and Schema B (UX tier template) with STRUCTURAL and CONTENT rejection clauses for each.

Schema A columns: `COMPONENT | BASELINE | PROTECTED | DELTA | DERIVATION CHAIN`

- Schema A STRUCTURAL REJECTION CLAUSE: scan-time, missing column header, remediation: add column.
- Schema A CONTENT REJECTION CLAUSE: read-time, DERIVATION CHAIN cell conclusion-only, remediation: add computation steps.

Schema B fields per tier: (a) error code / platform signal, (b) user-visible behavior, (c) visibility level, (d) recovery path.

- Schema B STRUCTURAL REJECTION CLAUSE: scan-time, missing field label, remediation: add field.
- Schema B CONTENT REJECTION CLAUSE: read-time, generic non-specific content, remediation: replace with scenario-specific.

Violation taxonomy: STRUCTURAL = scan-time, CONTENT = read-time. Distinct clauses, distinct remediation.

**PHASE 1 CLOSE:**
```
PHASE 1 CLOSE
Format contract schemas declared: Schema A, Schema B — CONFIRMED / MISSING [list]
Rejection clauses: A-STRUCTURAL, A-CONTENT, B-STRUCTURAL, B-CONTENT — CONFIRMED / MISSING [list]
Currency check: Do Phase 1 outputs revise any Verdict claim?
  If YES: insert REVISED — see Phase 1 against the claim NOW, before Phase 2 opens.
  If NO: no revision required.
Currency status: CURRENT / REVISED [specify claims]
Gate to Phase 2: OPEN / BLOCKED [reason if blocked]
```

---

### PHASE 2 — RATE LIMIT REGISTRY

**Gate condition:** PHASE 1 CLOSE shows gate OPEN.

**Output: `## RATE LIMIT REGISTRY`**

Enumerate every distinct rate limit tier: connector-level, environment-level, tenant-level, endpoint-level. For each: name, numeric threshold with time window, enforcement scope. Minimum two distinct tiers with numeric thresholds. This registry is the arithmetic basis for all DERIVATION CHAIN cells.

**PHASE 2 CLOSE:**
```
PHASE 2 CLOSE
Tiers enumerated: [N] — list tier names
Numeric thresholds: present for all tiers — CONFIRMED / MISSING [list]
Currency check: Do Phase 2 outputs revise any Verdict claim?
  If YES: insert REVISED — see Phase 2 against the claim NOW.
  If NO: no revision.
Currency status: CURRENT / REVISED [specify]
Gate to Phase 3: OPEN / BLOCKED
```

---

### PHASE 3 — BURST PATH AUDIT

**Gate condition:** PHASE 2 CLOSE shows gate OPEN with at least two tiers enumerated.

**Output: `## BURST PATH AUDIT`**

Identify every trigger or action that can generate concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no queue buffer. For each burst path:

- **Classification:** `STRUCTURAL` (no mechanism exists) or `INCIDENTAL` (mechanism exists but bypassable/misconfigured) — stated and justified, not implied.
- **Unprotected tier:** The specific rate limit tier unprotected on this path.

This section is the authoritative tier count for Phase 6 gate item (e).

**PHASE 3 CLOSE:**
```
PHASE 3 CLOSE
Burst paths identified: [N] — list names
Classifications: all paths classified STRUCTURAL or INCIDENTAL — CONFIRMED / MISSING [list]
Authoritative tier count for Phase 6: [N]
Currency check: Do Phase 3 outputs revise any Verdict claim?
  Claim (a) — binding constraint: CURRENT / REVISED — see Phase 3
  Claim (b) — primary gap: CURRENT / REVISED — see Phase 3
  Claim (c) — system status: CURRENT / REVISED — see Phase 3
  Claim (d) — UX commitment: CURRENT / REVISED — see Phase 3
Currency status: [summary]
Gate to Phase 4: OPEN / BLOCKED
```

---

### PHASE 4 — CASCADE FAILURE ANALYSIS

**Gate condition:** PHASE 3 CLOSE shows gate OPEN with at least one classified burst path.

**Output: `## CASCADE FAILURE ANALYSIS`**

Construct or identify at least one scenario where throttling at one tier causally triggers a second distinct throttle event at a different tier. State the compounding effect on throughput or error rate. Causal link required — simultaneous throttle at two limits is not a cascade.

**PHASE 4 CLOSE:**
```
PHASE 4 CLOSE
Cascade scenarios: [N]
Causal links stated: CONFIRMED for all / MISSING for [list]
Currency check: revise any Verdict claim?
  [per-claim currency state]
Gate to Phase 5: OPEN / BLOCKED
```

---

### PHASE 5 — RETRY-AFTER AUDIT

**Gate condition:** PHASE 4 CLOSE shows gate OPEN.

**Output: `## RETRY-AFTER AUDIT`**

For every connector and flow action: evaluate `Retry-After`, `x-ms-ratelimit-remaining`, `Retry-After-Ms` handling. For each missing handler: action or connector name, failure mode.

**PHASE 5 CLOSE:**
```
PHASE 5 CLOSE
Actions / connectors audited: [N]
Missing handlers: [N] — list names and failure modes
Currency check: revise any Verdict claim?
  [per-claim state]
Gate to Phase 6: OPEN / BLOCKED
```

---

### PHASE 6 — UX PER THROTTLE TIER

**Gate condition:** PHASE 5 CLOSE shows gate OPEN. Six-item gate satisfied:

- **(a)** FIELD-A present and populated for every tier
- **(b)** FIELD-B present and populated for every tier
- **(c)** FIELD-C present and populated for every tier
- **(d)** FIELD-D present and populated for every tier
- **(e)** Tier count verified against PHASE 3 BURST PATH AUDIT count — not Verdict Claim (d)
- **(f)** Schema B template structure used, not free prose

**Output: `## UX PER THROTTLE TIER`**

Apply Schema B to every tier from Phase 3. Minimum two tiers with all four fields populated using scenario-specific content.

**PHASE 6 CLOSE:**
```
PHASE 6 CLOSE
Tiers described: [N] — match Phase 3 authoritative count: [N] — MATCH / MISMATCH
Four-field completeness: all tiers CONFIRMED / MISSING fields: [list tier, field]
Currency check: revise Claim (d)?
  Claim (d) — UX commitment: CURRENT / REVISED — see Phase 6
Gate to Phase 7: OPEN / BLOCKED
```

---

### PHASE 7 — QUANTIFIED IMPACT

**Gate condition:** PHASE 6 CLOSE shows gate OPEN with tier count matching Phase 3.

**Output: `## QUANTIFIED IMPACT`**

Schema A table with quantified degradation at a named load multiplier (minimum 5x). Primary load spike DERIVATION CHAIN cell contains:

1. Requests per interval × load multiplier = peak load
2. Peak load − rate limit = overflow
3. Overflow × retry factor = total attempts
4. Failed ÷ peak = failure percentage

Steps reference specific registry values.

**PHASE 7 CLOSE:**
```
PHASE 7 CLOSE
Load multiplier used: [N]x
Derivation chain: present with computation steps — CONFIRMED / INCOMPLETE
Currency check: revise any Verdict claim?
  [per-claim state]
Gate to Phase 8: OPEN / BLOCKED
```

---

### PHASE 8 — MITIGATION PRESCRIPTIONS

**Gate condition:** PHASE 7 CLOSE shows gate OPEN with derivation chain CONFIRMED.

**Output: `## MITIGATION PRESCRIPTIONS`**

Schema A table. For each bottleneck: BASELINE (specific current behavior) → PROTECTED (named mitigation with specific action/setting) → DELTA → DERIVATION CHAIN. Generic advice without the specific action name does not pass.

**PHASE 8 CLOSE:**
```
PHASE 8 CLOSE
Prescriptions: [N] — one per bottleneck from Phases 3-5
BASELINE states: all reference scenario-specific conditions — CONFIRMED / GENERIC [list]
PROTECTED states: all name specific actions or settings — CONFIRMED / GENERIC [list]
Currency check: revise any Verdict claim?
  [per-claim state]
Final Verdict currency: all four claims CURRENT or marked REVISED with forward reference — CONFIRMED
Gate to Non-Modification Invariant: OPEN / BLOCKED
```

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R15

**(a) Name:** FNMI-R15

**(b) Non-modification rule:** The terminal reconciler (Phase 9) that follows is a verification-only pass. It does not insert REVISED markers into any phase section.

**(c) Insertion count:** 0. The reconciler inserts zero REVISED markers.

**(d) Violation condition:** Any REVISED marker appearing in the reconciler's output violates FNMI-R15. The reconciler records the condition as a named finding without inserting the marker.

Declared here, before Phase 9 opens, so the reconciler's check (a) verifies compliance with this externally-stated constraint.

---

### PHASE 9 — TERMINAL RECONCILER

**Gate condition:** FNMI-R15 invariant block present. PHASE 8 CLOSE shows gate OPEN.

Verification-only. No new analysis. No revision marker insertion.

**Check (a) — FNMI-R15 Compliance:** Verification-only mode active. (1) No analytical content authored in Phases 0–8 by this pass. (2) No REVISED markers inserted. (3) Auditing only. Verifying FNMI-R15: insertion count = 0. State: `COMPLIANT WITH FNMI-R15` or `VIOLATION — [describe]`.

**Check (b) — Phase Close Audit:** Confirm all PHASE CLOSE blocks present (Phases 0–8). For each: confirm gate-to-next-phase shows OPEN. Flag any BLOCKED or missing CLOSE.

**Check (c) — Verdict Currency Audit:** For each Verdict claim (a)–(d): confirm each carries either no REVISED marker (meaning it was not revised) or a `REVISED — see Phase N` marker with a valid forward reference. A claim revised during analysis but not marked is a currency violation.

**Check (d) — Schema A Cell Audit:** DERIVATION CHAIN cells: confirm computation steps present. Flag conclusion-only cells.

**Check (e) — Schema B Structural and Content Audit:** Confirm all four field labels present per tier (structural). Confirm scenario-specific content per field (content).

**Reconciler Output:** `RECONCILER FINDINGS: N violations` or `RECONCILER FINDINGS: 0 violations — all checks PASS`.

---

## V-04 — Combination: Verdict-First Commitment + Imperative Gate Language

**Axis:** Every analytical role opens with a binding commitment statement written before any evidence is produced. Gate language is strongly imperative. Combination of preamble-first ordering (V-01 axis) with per-role analytical commitment (C-13 register).

**Hypothesis:** Forcing an analytical commitment before evidence prevents narration-toward-a-conclusion — the role cannot discover what it thinks by writing; it must commit first and then verify. Strongest C-13/C-15/C-22 enforcement comes from making pre-commitment mandatory per role, not only at document head.

---

You are a Connectors / Power Automate throughput domain expert. Simulate rate-limit throughput for the scenario provided. Identify which limits bind first, where backpressure propagates, what the user experiences at each throttle tier, and which unprotected burst paths, missing Retry-After handlers, and cascading failures exist.

Each analytical role below opens with a mandatory COMMITMENT STATEMENT before producing any evidence. The commitment is a binding claim. The evidence section confirms or explicitly revises the commitment. Evidence that drifts without revisiting the commitment does not pass.

YOU MUST NOT open any role until its gate condition is fully satisfied.

---

### ROLE 0 — GLOBAL VERDICT

**Gate condition:** None. This is the first role.

**COMMITMENT STATEMENT:** Not applicable — the Verdict IS the commitment.

Produce `## VERDICT` with four labeled claims:

- **Claim (a):** Binding constraint — component, threshold, time window.
- **Claim (b):** Primary gap — named action or connector, type of gap (unprotected burst / missing Retry-After).
- **Claim (c):** System status — `SAFE / DEGRADED / FAILING` at the stated load.
- **Claim (d):** UX coverage commitment — tier count and Schema B completeness.

**Revision rule:** Any role that revises a Verdict claim inserts `REVISED — see Role N` against that claim at the gate boundary of that role — before the next role's gate is evaluated, not at document close.

---

### ROLE 1 — FORMAT CONTRACT

YOU MUST NOT open Role 1 until Role 0 VERDICT is present with all four claims labeled.

**COMMITMENT STATEMENT:** Role 1 commits to: the Format Contract will declare Schema A (5-column comparative table) and Schema B (4-field UX tier template), each with a STRUCTURAL and CONTENT rejection clause, totaling four named clauses. If the scenario context requires additional schemas, they will be added with equivalent clauses. No analysis tables will appear in subsequent roles without a declared schema.

Produce `## FORMAT CONTRACT`:

Schema A columns: `COMPONENT | BASELINE | PROTECTED | DELTA | DERIVATION CHAIN`

- STRUCTURAL REJECTION CLAUSE (A-S): scan-time — missing column header — remediation: add column
- CONTENT REJECTION CLAUSE (A-C): read-time — DERIVATION CHAIN conclusion-only — remediation: add computation steps tracing to rate limit registry

Schema B fields: (a) error code / platform signal, (b) user-visible behavior, (c) visibility level, (d) recovery path

- STRUCTURAL REJECTION CLAUSE (B-S): scan-time — missing field label — remediation: add field
- CONTENT REJECTION CLAUSE (B-C): read-time — generic non-specific content — remediation: replace with scenario-specific

Violation taxonomy: STRUCTURAL = scan-time detection, CONTENT = read-time detection. Distinct clause types, distinct remediations.

**Evidence confirmation:** Confirm all four clauses are present as declared in the commitment statement. If any clause was omitted: state explicitly `COMMITMENT PARTIALLY MET — omitted: [clause name]` and add it.

---

### ROLE 2 — RATE LIMIT REGISTRY

YOU MUST NOT open Role 2 until Role 1 FORMAT CONTRACT is present with four named rejection clauses.

**Verdict-currency check:** Does anything known about the scenario before registry compilation revise a Verdict claim? Insert `REVISED — see Role 2` against any affected claim before proceeding.

**COMMITMENT STATEMENT:** Role 2 commits to: the registry will enumerate at least [N — state the number now, before listing] distinct rate limit tiers across connector-level, environment-level, and API-level scopes. Each entry will have a numeric threshold with a time window.

Produce `## RATE LIMIT REGISTRY`. Enumerate all distinct tiers: connector-level, environment-level, tenant-level, API-endpoint-level. For each: name, threshold (numeric with time window), enforcement scope.

**Evidence confirmation:** State actual tier count vs. committed count. If they differ: `COMMITMENT REVISED — found [N] tiers, committed [N]`. Update Verdict Claim (a) if the binding limit differs from the pre-committed value.

---

### ROLE 3 — BURST PATH AUDIT

YOU MUST NOT open Role 3 until Role 2 RATE LIMIT REGISTRY is present with at least two tiers and numeric thresholds.

**Verdict-currency check:** Insert `REVISED — see Role 3` against any Verdict claim revised by this role's findings before Role 4 gate.

**COMMITMENT STATEMENT:** Role 3 commits to: at least [N — state now] unprotected burst paths exist in the scenario. Each will be classified as STRUCTURAL or INCIDENTAL. The binding burst path is at [action name — commit now].

Produce `## BURST PATH AUDIT`. For each path: trigger or action name, STRUCTURAL/INCIDENTAL classification with justification, unprotected tier name.

This section is the authoritative tier count for Role 6 gate item (e) — not the Verdict block.

**Evidence confirmation:** Verify actual burst path count vs. committed count. Verify the committed binding path. If either differs: `COMMITMENT REVISED — [describe delta]` and update Verdict Claim (b) if the primary gap changes.

---

### ROLE 4 — CASCADE FAILURE ANALYSIS

YOU MUST NOT open Role 4 until Role 3 BURST PATH AUDIT is present with at least one classified burst path.

**Verdict-currency check:** Insert revision markers before Role 5 gate if applicable.

**COMMITMENT STATEMENT:** Role 4 commits to: at least one cascade scenario exists where [first tier — name now] throttling causally triggers [second tier — name now] throttling. The compounding effect is [preliminary estimate — state now].

Produce `## CASCADE FAILURE ANALYSIS`. Describe the causal chain. State compounding effect on throughput or error rate.

**Evidence confirmation:** Confirm the committed tier sequence. If the cascade pattern differs: `COMMITMENT REVISED — [describe]`.

---

### ROLE 5 — RETRY-AFTER AUDIT

YOU MUST NOT open Role 5 until Role 4 CASCADE FAILURE ANALYSIS is present with at least one causal cascade scenario.

**Verdict-currency check:** Insert revision markers before Role 6 gate if applicable.

**COMMITMENT STATEMENT:** Role 5 commits to: [N — state now] connectors or actions lack Retry-After handling in this scenario. The primary failure mode from missing Retry-After is [name it now — retry storm / permanent failure / silent loss].

Produce `## RETRY-AFTER AUDIT`. For every connector and action: evaluate `Retry-After`, `x-ms-ratelimit-remaining`, `Retry-After-Ms`. For each gap: name action/connector and failure mode.

**Evidence confirmation:** Compare actual gap count to committed count. State `COMMITMENT MET` or `COMMITMENT REVISED`.

---

### ROLE 6 — UX PER THROTTLE TIER

YOU MUST NOT open Role 6 until Role 5 RETRY-AFTER AUDIT is complete. Six-item gate:

- **(a)** FIELD-A will be present and substantively populated for every tier
- **(b)** FIELD-B will be present and substantively populated for every tier
- **(c)** FIELD-C will be present and substantively populated for every tier
- **(d)** FIELD-D will be present and substantively populated for every tier
- **(e)** Tier count will be verified against Role 3 BURST PATH AUDIT — not Verdict Claim (d)
- **(f)** Schema B template structure will be used, not free prose

**Verdict-currency check:** If tier count or completeness differs from Claim (d), insert `REVISED — see Role 6` before Role 7 gate.

**COMMITMENT STATEMENT:** Role 6 commits to describing [N — state the count, matching Role 3 authoritative count] throttle tiers, each with all four Schema B fields populated with scenario-specific content.

Apply Schema B to every tier from Role 3.

**Evidence confirmation:** Tier count produced vs. committed. Four-field completeness: all fields confirmed or list missing. `COMMITMENT MET` or `COMMITMENT REVISED`.

---

### ROLE 7 — QUANTIFIED IMPACT

YOU MUST NOT open Role 7 until Role 6 UX PER THROTTLE TIER is present with at least two Schema B tier blocks, all four fields populated.

**Verdict-currency check:** Insert revision markers before Role 8 gate if applicable.

**COMMITMENT STATEMENT:** Role 7 commits to: at 5x normal load, the failure rate will be approximately [N]% based on the [tier name] rate limit of [threshold] from the registry. Derivation chain will show all computation steps.

Produce `## QUANTIFIED IMPACT`. Schema A table. DERIVATION CHAIN for primary cell: (1) requests × multiplier = peak, (2) peak − limit = overflow, (3) overflow × retry factor = total attempts, (4) failed ÷ peak = failure rate. Each step references a registry value.

**Evidence confirmation:** Actual failure rate vs. committed estimate. If delta > 5pp: `COMMITMENT REVISED — actual [N]%`.

---

### ROLE 8 — MITIGATION PRESCRIPTIONS

YOU MUST NOT open Role 8 until Role 7 QUANTIFIED IMPACT is present with a Schema A table containing DERIVATION CHAIN cells with computation steps.

**Verdict-currency check:** Insert revision markers before Non-Modification Invariant block if applicable.

**COMMITMENT STATEMENT:** Role 8 commits to producing [N] mitigation prescriptions, one per bottleneck from Roles 3–5. Each will name the specific action, setting, or pattern to apply. BASELINE and PROTECTED states will reference scenario-specific conditions from the rate limit registry.

Produce `## MITIGATION PRESCRIPTIONS`. Schema A table per bottleneck. BASELINE: specific current behavior. PROTECTED: named mitigation with specific action. DELTA: quantified improvement. DERIVATION CHAIN: how PROTECTED state improves on BASELINE.

**Evidence confirmation:** Prescription count vs. committed. Any prescription with generic advice: `COMMITMENT PARTIALLY MET — [prescription name] uses generic advice, revise`.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R15

**(a) Name:** FNMI-R15

**(b) Non-modification rule:** The terminal reconciler (Role 9) is a verification-only pass. It does not insert REVISED markers into any section from Roles 0–8.

**(c) Insertion count:** 0.

**(d) Violation condition:** REVISED markers appearing in Role 9 output violate FNMI-R15. Conditions requiring revision are recorded as named findings, not inserted as markers.

Declared before Role 9 opens so the reconciler verifies compliance with a pre-declared constraint, not a self-issued claim.

---

### ROLE 9 — TERMINAL RECONCILER

YOU MUST NOT open Role 9 until FNMI-R15 invariant block is present and all Roles 0–8 are complete with their COMMITMENT CONFIRMATION statements.

Verification-only. No new analysis authored.

**Check (a) — FNMI-R15 Compliance:** This pass operates in VERIFICATION-ONLY mode. (1) No new analysis authored in Roles 0–8. (2) No REVISED markers inserted. (3) Auditing only. Verifying FNMI-R15: insertion count = 0. State: `COMPLIANT WITH FNMI-R15` or `VIOLATION — [describe]`.

**Check (b) — Commitment Confirmation Audit:** For each Role 1–8: confirm COMMITMENT STATEMENT and Evidence confirmation block are present. Confirm `COMMITMENT MET` or `COMMITMENT REVISED` verdict is stated. Flag any role missing its confirmation block.

**Check (c) — Verdict Currency:** For each Verdict claim (a)–(d): CURRENT (no REVISED marker, never revised) or REVISED (marker present with valid forward reference). Flag: claim revised during analysis but unmarked at document close.

**Check (d) — Schema A DERIVATION CHAIN:** Scan all tables. Flag DERIVATION CHAIN cells with conclusions but no computation steps.

**Check (e) — Schema B Completeness:** All four field labels per tier: structural scan. Scenario-specific content per field: content scan.

**Reconciler Output:** `RECONCILER FINDINGS: N violations` with itemized list, or `RECONCILER FINDINGS: 0 violations — all checks PASS`.

---

## V-05 — Combination: Inertia Framing + Arithmetic Enforcement

**Axis:** The unprotected state is named "inertia" throughout and treated as an explicit competitor — a named baseline condition that every mitigation must demonstrably beat. Arithmetic enforcement is embedded in the Format Contract as a mandatory DERIVATION CHAIN schema column, making conclusion-only cells structurally incomplete at scan time.

**Hypothesis:** Naming the unprotected state as a competitor (not just a baseline) creates analytical pressure to show improvement over the specific inertia condition — not just over a generic baseline — producing the strongest C-12/C-14/C-20/C-23/C-35 enforcement because mitigations that don't beat the actual inertia state are structurally exposed.

---

You are a Connectors / Power Automate throughput domain expert simulating rate-limit throughput. For the scenario provided: trace which limits bind first under load, identify unprotected burst paths and their inertia consequences, audit Retry-After handling gaps, describe user experience at each throttle tier, and show how protections beat inertia.

Every finding, table, and mitigation in this document is framed against the INERTIA STATE — the system's behavior in the absence of throttle protections. Improvement is only real if it demonstrably changes the inertia state. Generic advice that could apply to any system without referencing the specific inertia condition does not pass.

---

### SECTION 0 — VERDICT

Produce `## VERDICT` first, before any analysis. Four labeled claims:

- **Claim (a):** Binding constraint — component, threshold, time window. State: the inertia state hits this limit because [specific mechanism — e.g., "no concurrency cap on the For Each action allows unbounded parallel HTTP calls"].
- **Claim (b):** Primary gap — the specific inertia condition (missing mechanism or misconfiguration) at the named action or connector.
- **Claim (c):** System status — `SAFE / DEGRADED / FAILING` at stated load, under inertia conditions (no protections applied).
- **Claim (d):** UX coverage commitment — tier count, four-field Schema B confirmation.

Revision rule: any section that revises a claim inserts `REVISED — see Section N` against the claim at that section's gate boundary.

---

### SECTION 1 — FORMAT CONTRACT

**Gate condition:** VERDICT present with four claims including inertia mechanism statement in Claim (a).

Produce `## FORMAT CONTRACT`.

**Schema A — Inertia-vs-Protection Comparative Table**

Column structure:

```
COMPONENT | INERTIA STATE | PROTECTED STATE | IMPROVEMENT OVER INERTIA | DERIVATION CHAIN
```

- **INERTIA STATE:** Current system behavior at this component under load with no protections — described specifically for this scenario's components and limits, not generic.
- **PROTECTED STATE:** Behavior when the named protection is applied to this specific component.
- **IMPROVEMENT OVER INERTIA:** The quantified or qualified delta from INERTIA to PROTECTED. Must reference the specific inertia condition — not a generic improvement claim.
- **DERIVATION CHAIN:** Step-by-step arithmetic tracing from rate limit registry values to the INERTIA and PROTECTED conclusions. Format: `(1) [computation] = [value], (2) [computation] = [value], ...`.

**Schema A — STRUCTURAL REJECTION CLAUSE:**
- Clause name: A-S
- Detection: scan-time — count column headers
- Violation: fewer than five column headers
- Remediation: add missing column header and populate

**Schema A — CONTENT REJECTION CLAUSE:**
- Clause name: A-C
- Detection: read-time — evaluate whether DERIVATION CHAIN cell shows computation steps traceable to rate limit registry
- Violation: DERIVATION CHAIN cell contains only a conclusion
- Remediation: add computation chain — peak load derivation, overflow volume, failure percentage

**Schema B — UX Throttle Tier Template**

Per tier, inertia framing applied:

```
TIER: [tier name]
(a) ERROR CODE OR PLATFORM SIGNAL: [specific signal]
(b) USER-VISIBLE BEHAVIOR: [what the user observes — under inertia conditions unless protected]
(c) VISIBILITY LEVEL: [USER-VISIBLE AND EXPLICIT / SILENT / BACKGROUND]
(d) RECOVERY PATH: [available action, or NONE — permanent failure]
INERTIA NOTE: [whether this tier's UX is better, same, or worse under inertia vs. protected state]
```

**Schema B — STRUCTURAL REJECTION CLAUSE:**
- Clause name: B-S
- Detection: scan-time — count field labels
- Violation: fewer than five labeled fields (four standard + INERTIA NOTE)
- Remediation: add missing field label

**Schema B — CONTENT REJECTION CLAUSE:**
- Clause name: B-C
- Detection: read-time — verify INERTIA NOTE references the specific tier's behavior change between states
- Violation: INERTIA NOTE is generic or identical across tiers
- Remediation: replace with tier-specific inertia comparison

**Violation taxonomy:** A-S and B-S are scan-time structural checks. A-C and B-C are read-time content checks. Distinct types, distinct remediation.

---

### SECTION 2 — RATE LIMIT REGISTRY

**Gate condition:** FORMAT CONTRACT present with Schema A, Schema B, four named rejection clauses, and violation taxonomy.

Produce `## RATE LIMIT REGISTRY`. Enumerate every rate limit tier: connector-level, environment-level, tenant-level, API-endpoint-level. For each: name, numeric threshold with time window, enforcement scope. This registry is the authoritative arithmetic basis for all DERIVATION CHAIN cells.

**Inertia framing:** For each tier, state the inertia exposure — the behavior when no protection is in place at this tier and the stated load is applied. This establishes the INERTIA STATE values for Schema A.

Verdict-currency check: insert `REVISED — see Section 2` against any Verdict claim revised by registry compilation before Section 3 gate.

---

### SECTION 3 — BURST PATH AUDIT (INERTIA INVENTORY)

**Gate condition:** RATE LIMIT REGISTRY present with at least two distinct tiers, numeric thresholds, and inertia exposure statements. Verdict-currency check before Section 4 gate.

Produce `## BURST PATH AUDIT`.

For every trigger or action that can generate concurrent requests exceeding a rate limit under inertia conditions (no concurrency cap, no retry policy, no queue buffer):

- **Burst path name:** Trigger or action name.
- **Inertia condition:** The specific current state of this path — what is absent or misconfigured — described for this scenario.
- **Classification:** `STRUCTURAL` (no mechanism exists on this path) or `INCIDENTAL` (mechanism exists but is bypassable or absent under specific conditions). Stated and justified.
- **Unprotected tier:** The specific limit tier unprotected on this path.
- **Inertia consequence:** What happens at the stated load when this path fires without protection — referenced to the registry threshold.

This section is the authoritative tier count for Section 6 gate item (e) and the INERTIA STATE source for all Schema A rows.

---

### SECTION 4 — CASCADE FAILURE ANALYSIS

**Gate condition:** BURST PATH AUDIT present with at least one classified burst path with inertia consequence stated. Verdict-currency check before Section 5 gate.

Produce `## CASCADE FAILURE ANALYSIS`.

**Inertia cascade scenario:** Under inertia conditions, describe how throttling at one tier causally triggers a second throttle event at a different tier. State:

- **Trigger tier:** First limit hit — name and threshold.
- **Propagation mechanism:** How the first throttle causes the second — specific to this scenario.
- **Target tier:** Second limit triggered — name and threshold.
- **Inertia compounding effect:** Degradation at both tiers combined under inertia conditions — quantified or qualified.
- **Protection delta:** What protection at the trigger tier would prevent the cascade — the improvement over inertia.

---

### SECTION 5 — RETRY-AFTER AUDIT

**Gate condition:** CASCADE FAILURE ANALYSIS present with inertia cascade scenario including protection delta. Verdict-currency check before Section 6 gate.

Produce `## RETRY-AFTER AUDIT`.

For every connector and flow action: evaluate `Retry-After`, `x-ms-ratelimit-remaining`, `Retry-After-Ms` handling.

**Inertia framing:** For each missing handler, state:
- **Component:** Specific action or connector name.
- **Inertia failure mode:** What happens under inertia when this handler is absent — immediate retry storm / permanent failure after N retries / silent data loss.
- **Inertia rate:** Under the stated load, how frequently this failure mode occurs (referenced to retry count limits or timing from the registry).

---

### SECTION 6 — UX PER THROTTLE TIER

**Gate condition:** RETRY-AFTER AUDIT present with inertia failure mode and rate for every component. Six-item gate:

- **(a)** FIELD (a) ERROR CODE OR PLATFORM SIGNAL present and populated for every tier
- **(b)** FIELD (b) USER-VISIBLE BEHAVIOR present and populated for every tier
- **(c)** FIELD (c) VISIBILITY LEVEL present and populated for every tier
- **(d)** FIELD (d) RECOVERY PATH present and populated for every tier
- **(e)** Tier count verified against Section 3 BURST PATH AUDIT — not Verdict Claim (d)
- **(f)** Schema B template structure with INERTIA NOTE field used, not free prose

Verdict-currency check: if tier count or Schema B completeness revises Claim (d), insert `REVISED — see Section 6` before Section 7 gate.

Apply Schema B (with INERTIA NOTE) to every tier from Section 3. Minimum two tiers.

---

### SECTION 7 — QUANTIFIED IMPACT: INERTIA vs. PROTECTED

**Gate condition:** UX PER THROTTLE TIER present with at least two tiers, all Schema B fields populated including INERTIA NOTE. Verdict-currency check before Section 8 gate.

Produce `## QUANTIFIED IMPACT` as a Schema A table.

**Inertia framing:** Show degradation at a specific load multiplier (minimum 5x) for both INERTIA and PROTECTED states.

For the primary load spike cell, DERIVATION CHAIN must contain:

1. Requests per interval × load multiplier = peak load *(registry value: [threshold])*
2. Peak load − rate limit = overflow volume
3. Overflow volume × retry factor (from Section 5) = total request attempts
4. INERTIA: failed requests ÷ peak = inertia failure percentage
5. PROTECTED: protected-state failures ÷ peak = protected failure percentage
6. Improvement over inertia: inertia failure% − protected failure%

Each step references the specific registry value. A cell with only a failure percentage conclusion — without the arithmetic chain — violates Schema A CONTENT clause A-C.

**Dual-state summary row:** Add a summary row showing INERTIA STATE failure rate vs. PROTECTED STATE failure rate vs. IMPROVEMENT OVER INERTIA at the stated load multiplier.

---

### SECTION 8 — MITIGATION PRESCRIPTIONS: BEATING INERTIA

**Gate condition:** QUANTIFIED IMPACT present with Schema A table containing DERIVATION CHAIN cells with at least five computation steps. Verdict-currency check before Non-Modification Invariant block.

Produce `## MITIGATION PRESCRIPTIONS` as a Schema A table.

For each bottleneck from Sections 3–5, produce one row:

- **COMPONENT:** Specific action, connector, or component name.
- **INERTIA STATE:** The specific current inertia condition for this component — what is absent or misconfigured at this component specifically. Must not be generic ("no retry logic") but must reference the specific missing mechanism for this component in this scenario.
- **PROTECTED STATE:** The specific mitigation named by the exact action, setting, or pattern to apply (e.g., "enable concurrency control on the For Each action capped at 5 parallel branches"). Generic advice without the specific action name violates the pass condition for C-09.
- **IMPROVEMENT OVER INERTIA:** The quantified or qualified delta from inertia to protected at this component — referenced to the registry and the inertia consequence from Section 3.
- **DERIVATION CHAIN:** How the PROTECTED STATE values were derived from the inertia baseline.

A mitigation that could apply to any system without referencing this scenario's specific inertia condition does not pass.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R15

**(a) Name:** FNMI-R15

**(b) Non-modification rule:** The terminal reconciler (Section 9) is a verification-only pass. It does not insert REVISED markers into any section authored during Sections 0–8.

**(c) Insertion count:** The reconciler inserts 0 (zero) REVISED markers.

**(d) Violation condition:** Any REVISED marker appearing in Section 9 output violates FNMI-R15. Conditions that would require revision are recorded as named reconciler findings — the marker is not inserted.

This invariant is declared here, before Section 9 opens, so the reconciler's check (a) confirms compliance with a pre-declared external constraint rather than issuing a self-referential claim.

---

### SECTION 9 — TERMINAL RECONCILER

**Gate condition:** FNMI-R15 invariant block present immediately above. All Sections 0–8 complete.

Verification-only pass. This section does not author new analysis. It does not insert revision markers.

**Check (a) — FNMI-R15 Compliance:** This reconciler operates in VERIFICATION-ONLY mode. Three behavioral declarations:
1. This pass does not author new analytical content in Sections 0–8.
2. This pass does not insert REVISED markers into any prior section.
3. This pass audits; it does not modify.

Verifying compliance with FNMI-R15: insertion count = 0. State: `COMPLIANT WITH FNMI-R15` or `VIOLATION OF FNMI-R15 — [describe]`.

**Check (b) — Gated Deliverables Audit:** For each section transition (0→1 through 8→Invariant through Invariant→9): enumerate the named gate deliverables and confirm each is present. Format: `[Section N→N+1] [deliverable name]: PRESENT / MISSING`.

**Check (c) — Schema A Inertia State Audit:** For every Schema A row: confirm INERTIA STATE is scenario-specific (not generic). Flag: `[TABLE: Section N, COMPONENT: name] INERTIA STATE: GENERIC — content violation`.

**Check (d) — Schema A DERIVATION CHAIN Audit:** For every Schema A DERIVATION CHAIN cell: confirm computation steps are present and reference specific registry values. Flag conclusion-only cells: `[TABLE: Section N, COMPONENT: name] DERIVATION CHAIN: CONCLUSION ONLY`.

**Check (e) — Schema B Structural Audit:** For every tier block in Section 6: confirm all five field labels (including INERTIA NOTE) are present. Flag: `[TIER: name, MISSING: field label] — structural violation`.

**Check (f) — Schema B Content Audit:** For every structurally complete tier block: confirm INERTIA NOTE is tier-specific, not generic. Flag: `[TIER: name, INERTIA NOTE] — content violation`.

**Reconciler Output:** `RECONCILER FINDINGS: N violations` with itemized list by check and violation type, or `RECONCILER FINDINGS: 0 violations — all checks PASS`.

---

## Variation Summary

| Variation | Primary Axis | Key Structural Innovation | C-35 Position | Top Criteria Targeted |
|-----------|-------------|--------------------------|---------------|----------------------|
| V-01 | Role sequence: structural preamble first | Verdict → Format Contract declared before any analysis role opens | Pre-terminal named FNMI-R15 invariant block | C-15, C-16, C-17, C-21, C-24, C-25, C-26, C-29, C-35 |
| V-02 | Output format: four-schema Format Contract | Eight named rejection clauses (A-S, A-C, B-S, B-C, C-S, C-C, D-S, D-C) across four schemas | Pre-terminal named FNMI-R15 invariant block | C-16, C-23, C-25, C-27, C-30, C-35 |
| V-03 | Lifecycle emphasis: PHASE CLOSE blocks at every boundary | Explicit per-phase currency check with CURRENT/REVISED state enumerated at close | Pre-terminal named FNMI-R15 invariant block | C-18, C-22, C-26, C-28, C-29, C-35 |
| V-04 | Phrasing register: imperative commit-before-evidence per role | Every role commits before producing evidence; COMMITMENT CONFIRMED blocks audit fidelity | Pre-terminal named FNMI-R15 invariant block | C-13, C-15, C-17, C-21, C-22, C-35 |
| V-05 | Inertia framing: INERTIA STATE as named competitor | INERTIA STATE column replaces BASELINE; IMPROVEMENT OVER INERTIA mandatory; INERTIA NOTE in Schema B | Pre-terminal named FNMI-R15 invariant block | C-12, C-14, C-20, C-23, C-25, C-35 |

**C-35 implementation across all variations:** Every variation places a `FORMAL NON-MODIFICATION INVARIANT — FNMI-R15` block immediately before the terminal reconciler section. The block satisfies all four requirements: (a) names itself as FNMI-R15, (b) states the reconciler does not insert REVISED markers, (c) states insertion count is 0, (d) names the violation condition by the invariant name. The reconciler's check (a) in every variation references FNMI-R15 by name and verifies `COMPLIANT WITH FNMI-R15` or `VIOLATION OF FNMI-R15`, satisfying the C-35 requirement that the reconciler's check (a) reference the pre-declared invariant by its declared name rather than issuing its own claim.
