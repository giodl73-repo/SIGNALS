# flow-ratelimit Variate — Round 9 (v9 Rubric)
**Date:** 2026-03-17
**Rubric:** v9 (C-01 through C-26, N_essential=5, N_recommended=3, N_aspirational=18)
**Scoring:** composite = (essential_pass/5 * 60) + (recommended_pass/3 * 30) + (aspirational_pass/18 * 30)
**Golden threshold:** all 5 essential pass AND composite >= 95

---

## Context: What R8 Found and What R9 Must Add

**R8 gap analysis recap:**
- V-01 achieves 16/17 aspirational (118.24 composite) — only C-19 fails.
- C-19 FAIL evidence: *"implied ROLE 10 may cover UX but four-field template structure is not enforced"*
- V-01 passes C-21 (full gate chain closure) and C-24 (terminal reconciler), but the UX role is
  implicit in the role sequence and the four-field constraint is never named as a gate deliverable.
- V-02, V-03 FAILs map to existing criteria; no new patterns.

**R8 new signal (C-26):** Gate chain closure does not automatically propagate to UX template completeness
unless the four required fields are explicitly named as gate deliverables for an explicitly numbered UX
role. C-26 closes the gap: the UX-per-tier section must be an explicitly numbered role whose gate
condition names all four fields — (a) error code or platform signal, (b) user-visible behavior,
(c) visibility level, (d) recovery path — individually, so that C-24's reconciler check (b) can
enumerate and confirm UX completeness at document close without a separate UX-specific audit.

**Aspirational pool:** v9 grows from 17 → 18 (adds C-26).

---

## Round 9 Variation Map

| Variation | Single/Combined Axis | C-26 Mechanism | C-19 | C-21 | C-24 | Predicted composite |
|-----------|---------------------|----------------|------|------|------|---------------------|
| V-01 | Single: Explicit UX role in numbered sequence | Role 6 named, gate enumerates all four fields | PASS | PASS | PASS | 120/120 |
| V-02 | Single: Format Contract schema declares UX template | Schema B in Format Contract with UX-specific STRUCTURAL clause | PASS | PASS | PASS | 120/120 |
| V-03 | Single: Phase lifecycle with field-level UX gate | Phase 4 gate enumerates all four fields as blocking checklist | PASS | PASS | PASS | 120/120 |
| V-04 | Combined: V-01 + V-02 (role sequence + schema declaration) | Role 6 gate + Schema B in Format Contract + two-tier taxonomy | PASS | PASS | PASS | 120/120 |
| V-05 | Combined: V-01 + V-02 + V-03 (full structural synthesis) | All four mechanisms: role gate + schema + phase gate + reconciler audit | PASS | PASS | PASS | 120/120 |

---

## V-01

**Axis:** Role sequence — UX Per Tier is an explicitly numbered role (Role 6) with a gate condition
that enumerates all four required fields by name, blocking Role 7 until each field is confirmed
present for every tier.

**Hypothesis:** Elevating UX from an implied responsibility buried in a multi-purpose role to a
dedicated, explicitly numbered role with field-level gate conditions satisfies C-26 and allows
C-24's reconciler check (b) — which enumerates gated deliverables — to automatically audit UX
completeness at document close without a separate UX-specific check. V-01 R8 passed C-21 (zero
ungated boundaries) but failed C-19 because its UX role was implied. This variation makes the
role explicit and its gate field-level.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is fully
satisfied. Gate violations block the next role; they do not terminate the document.

---

### ROLE 0 — VERDICT BLOCK

State before any rate limit inventory, burst path audit, or UX analysis:

(a) **Binding constraint:** component name + numeric threshold
(b) **Primary gap:** specific action or path where the unprotected burst or Retry-After failure
    occurs
(c) **System status at stated load:** SAFE / DEGRADED / FAILING

Self-containment requirement: a reader who reads only this block knows the core finding without
proceeding to the evidence sections. Evidence sections must confirm each claim (a)–(c) or insert
an inline "REVISED — see Role N" marker for any claim that changes.

**Gate 0→1:** Verdict Block written with all three claims before Role 1 begins.

---

### ROLE 1 — FORMAT CONTRACT

Declare the structural contract governing this entire document:

**(a) Table schema:** every comparative table containing quantified estimates uses:

| BASELINE | PROTECTED | DERIVATION CHAIN | DELTA |

- **BASELINE:** current / unprotected system behavior at this volume tier
- **PROTECTED:** system behavior with stated mitigations applied
- **DERIVATION CHAIN:** full arithmetic computation chain — not a conclusion alone
- **DELTA:** net change from BASELINE to PROTECTED

**(b) Rejection clauses:**

- **STRUCTURAL REJECTION CLAUSE (scan-time detection):** A required column is absent from a
  table's structure. Detectable at scan time by counting column headers without reading cell
  content. Violation marker: `[STRUCTURAL VIOLATION — missing: {column name}]`. Remediation:
  add the missing column header before proceeding.

- **CONTENT REJECTION CLAUSE (read-time detection):** A required column is present but its cell
  contains only a qualitative conclusion without the mandated derivation steps. Detectable only
  by reading the cell. Violation marker: `[CONTENT VIOLATION — conclusion only: {column name}]`.
  Remediation: deepen the cell with computation steps.

Both clauses apply throughout. Violations are flagged inline and enumerated by the Role 11
terminal reconciler.

**Gate 1→2:** Format Contract written with table schema, both named rejection clause types, and
detection method stated for each clause before Role 2 begins.

---

### ROLE 2 — RATE LIMIT REGISTRY

Enumerate all rate limits relevant to this scenario. For each:

- Component name
- Numeric threshold and scope (e.g., "600 API calls per 60 seconds per connection")
- Enforcement point (connector tier / environment tier / action tier)

At least one limit must carry a concrete numeric threshold. Estimates are acceptable if labeled
as such.

**Verdict currency check:** Do any findings here revise claim (a) or (c) in the Verdict Block?
If yes: insert "REVISED — see Role 2" inline in the Verdict Block for the revised claim.

**Gate 2→3:** At least one rate limit with numeric threshold registered; Verdict updated if
revised. Do not begin Role 3 until this gate is satisfied.

---

### ROLE 3 — BINDING CONSTRAINT DETERMINATION

Identify which rate limit is the binding constraint — the one hit first or most severely under
the described load. Provide explicit reasoning: why this limit, not a higher-capacity one,
is the binding constraint.

**Verdict currency check:** Confirm Verdict claim (a), or insert "REVISED — see Role 3" if the
binding constraint differs from the initial commitment.

**Gate 3→4:** Binding constraint identified with explicit reasoning; Verdict claim (a) confirmed
or marked REVISED. Do not begin Role 4 until this gate is satisfied.

---

### ROLE 4 — BURST PATH AUDIT

Identify at least one structurally unprotected burst path — a trigger or action that generates
concurrent requests exceeding a rate limit with no concurrency cap, no retry policy, and no
queue buffer between the source and the rate-limited endpoint.

For each path:
- The trigger or action generating concurrent requests
- The missing controls (no concurrency cap / no retry policy / no queue buffer)
- **Classification:** STRUCTURAL (no mechanism exists on this path) vs. INCIDENTAL (mechanism
  exists but is misconfigured, bypassable, or absent only under specific conditions) — stated
  and justified, not implied by framing

**Verdict currency check:** Confirm Verdict claim (b), or insert "REVISED — see Role 4".

**Gate 4→5:** At least one burst path with STRUCTURAL vs. INCIDENTAL classification; Verdict
claim (b) confirmed or marked REVISED. Do not begin Role 5 until this gate is satisfied.

---

### ROLE 5 — RETRY-AFTER GAP CHECK

Evaluate whether flows or connectors handle Retry-After headers (or equivalent backoff signals:
`x-ms-ratelimit-remaining`, `Retry-After-Ms`) from every throttled endpoint identified in
Roles 3–4. Flag each missing-handling case as a finding with the failure mode it causes
(immediate retry storm, permanent failure after N retries, silent drop, etc.).

**Verdict currency check:** Confirm Verdict claims (b) and (c), or mark REVISED.

**Gate 5→6:** Every throttled path evaluated for Retry-After handling; missing handling flagged
with failure mode; Verdict updated if revised. Do not begin Role 6 until this gate is satisfied.

---

### ROLE 6 — UX PER THROTTLE TIER [REQUIRED ROLE — DO NOT SKIP OR MERGE]

Apply the four-field UX template to EVERY throttle tier reached in this scenario. For each tier,
all four fields are mandatory. Free prose describing all four topics without the template
structure does not satisfy this role.

**Template format for each tier:**

---
**[Tier Name / throttle level]**

- **FIELD-A — Error code or platform signal:** [specific HTTP status, connector event, or Power
  Automate run history marker — e.g., "HTTP 429 with Retry-After header", "ActionThrottled
  event visible in run history", "ThrottlingException in connector error detail"]
- **FIELD-B — User-visible behavior:** [what the user observes or experiences at this tier —
  specific to this tier, not a generic description]
- **FIELD-C — Visibility level:** EXPLICIT (user sees an error, message, or notification) or
  SILENT (processing continues in background; user is unaware)
- **FIELD-D — Recovery path:** [exact path available: manual retry by user / automatic
  exponential backoff with Retry-After header parsed / permanent failure after N retries with
  no further retry / no recovery path available]

---

**Structural check:** after completing each tier entry, confirm all four field labels are
present. Missing label → `[STRUCTURAL VIOLATION — missing: FIELD-X]`.

**Content check:** after completing each tier entry, confirm each cell has substantive
field-specific content, not merely a tier label. Label-only cell → `[CONTENT VIOLATION —
conclusion only: FIELD-X]`.

**Verdict currency check:** Does any UX finding revise Verdict claim (c) or other claims?
If yes: insert "REVISED — see Role 6" for the revised claim.

**GATE 6→7 [FIELD-LEVEL GATE]:**

Do not begin Role 7 until ALL of the following are confirmed:

- [ ] **FIELD-A** (error code or platform signal) is present and substantively populated for
  **EVERY** tier described in this document — not only the minimum two tiers
- [ ] **FIELD-B** (user-visible behavior) is present and substantively populated for
  **EVERY** tier
- [ ] **FIELD-C** (visibility level) is present and explicitly labeled EXPLICIT or SILENT for
  **EVERY** tier
- [ ] **FIELD-D** (recovery path) is present and substantively populated for **EVERY** tier
- [ ] At least two tiers have been described
- [ ] Template structure (not free prose) used for every tier
- [ ] Verdict updated for any revised claims

A tier with three fields present and one absent does not pass this gate for that tier. A tier
described in free prose that mentions all four topics does not pass this gate for that tier.

---

### ROLE 7 — CAUSAL CHAIN TO FAILURE MODE

Trace the complete causal chain from trigger event through the rate-limited endpoint to the
resulting failure mode. Every link in the chain must be stated explicitly. Implied causation
does not pass.

**Verdict currency check:** Mark "REVISED — see Role 7" for any revised Verdict claim.

**Gate 7→8:** Complete causal chain with every link explicit; Verdict updated if revised.
Do not begin Role 8 until this gate is satisfied.

---

### ROLE 8 — CASCADING THROTTLE FAILURE

Construct a specific scenario where throttling at one tier causally triggers a second distinct
throttle event at a different tier. State the mechanism of causation. Describe the compounding
effect on throughput or error rate. Two independent limits both hit under load without causal
linkage do not constitute a cascade.

**Verdict currency check:** Mark "REVISED — see Role 8" for any revised Verdict claim.

**Gate 8→9:** Cascade scenario with causal linkage named and compounding effect described;
Verdict updated if revised. Do not begin Role 9 until this gate is satisfied.

---

### ROLE 9 — VOLUME-TO-BEHAVIOR MAPPING

Produce a comparative table using the BASELINE | PROTECTED | DERIVATION CHAIN | DELTA schema
declared in Role 1. For each request volume tier, show the throttle behavior at baseline and
the behavior with protections applied.

For the load spike tier (5x nominal, or the scenario-equivalent highest load):
- The DERIVATION CHAIN cell must contain ALL of the following computation steps:
  - Step 1: requests per interval × load multiplier = peak load `[cite numeric values from Role 2]`
  - Step 2: peak load − rate limit = overflow volume
  - Step 3: overflow × retry factor = failed request volume
  - Step 4: failed / peak = failure percentage
- A cell stating only the conclusion (e.g., "42% fail") without Steps 1–4 triggers the
  CONTENT REJECTION CLAUSE.

**Verdict currency check:** Confirm Verdict claim (c) or mark "REVISED — see Role 9".

**Gate 9→10:** Volume table with all four schema columns present; load spike tier with full
arithmetic derivation chain (Steps 1–4 shown); Verdict claim (c) confirmed or marked REVISED.
Do not begin Role 10 until this gate is satisfied.

---

### ROLE 10 — MITIGATIONS

For each bottleneck and unprotected burst path identified in Roles 3–5, prescribe a concrete
mitigation naming the specific action, setting, or pattern (e.g., "enable concurrency control
on the For Each loop capped at 5 parallel branches", "add exponential backoff with Retry-After
header parsing to the HTTP action"). Generic advice ("add retry logic") without naming the
specific action does not pass.

For each mitigation:
- **Before-state:** baseline behavior at this bottleneck (must reference a specific component
  and correspond to a BASELINE-column entry)
- **After-state:** system behavior with mitigation applied (populates PROTECTED column in
  Role 9 table)

**Verdict currency check:** Mark "REVISED — see Role 10" for any revised Verdict claim.

**Gate 10→11:** Per-bottleneck mitigations with specific named actions and before/after states;
Verdict updated if revised. Do not begin Role 11 until this gate is satisfied.

---

### ROLE 11 — TERMINAL RECONCILER

Audit the complete document state. This is the last section. Produce a named finding record.

**Check (a) — Verdict audit:** Scan Verdict claims (a)–(c). For each claim revised during
analysis, confirm an inline "REVISED — see Role N" marker is present with a forward reference
to the revising role. List any revised claim lacking a marker as a violation.

**Check (b) — Gate audit:** Enumerate each role transition (Gates 0→1 through 10→11). For each
gate, confirm the named deliverables from the prior role are present.
- For Gate 6→7 specifically: confirm **FIELD-A, FIELD-B, FIELD-C, and FIELD-D** are all
  present for **every throttle tier** described in the document, not only the minimum two tiers.

**Check (c) — Derivation chain audit:** Scan all quantified tables. For each DERIVATION CHAIN
cell: does it contain computation steps, or only a conclusion? Flag each conclusion-only cell
as a CONTENT VIOLATION.

**Output:** `Reconciler Findings: N violation(s)` followed by an itemized list, or
`Reconciler Findings: 0 violations` if the audit finds no issues.

**Gate 11 (document close):** Reconciler produces a named finding record referencing checks
(a), (b), and (c). Document is complete.

---

## V-02

**Axis:** Format Contract schema declares UX template — the four-field UX template is embedded
in the Format Contract as a named structural schema (Schema B), parallel to the table schema
(Schema A), with a dedicated UX STRUCTURAL REJECTION CLAUSE that creates scan-time detectability
for missing UX fields.

**Hypothesis:** Embedding the UX four-field template in the Format Contract as Schema B — not
just as a role instruction — creates the same scan-time detectability for UX field completeness
that the DERIVATION CHAIN column creates for arithmetic completeness. When the Format Contract
declares FIELD-A through FIELD-D as mandatory structural elements with a named STRUCTURAL
REJECTION CLAUSE, missing fields are visible at scan time without reading UX prose, parallel to
how a missing table column is detectable without reading cell content. V-02 differs from V-01
by locating the four-field authority in the Format Contract rather than the role gate — enabling
any section transition that references the Format Contract to enforce UX completeness without
repeating the field enumeration.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
rate-limited systems.

**SCENARIO:** {scenario}

---

### VERDICT BLOCK [Write before any analysis section]

State before any rate limit inventory, burst path audit, or UX analysis:

(a) **Binding constraint:** component name + numeric threshold
(b) **Primary gap:** named action or path where burst or Retry-After failure occurs
(c) **System status:** SAFE / DEGRADED / FAILING at stated load

Self-containment: a reader who reads only this block knows the core finding. Evidence sections
confirm or insert "REVISED — see Section N" for any revised claim.

---

### FORMAT CONTRACT [Write before any analysis section]

This contract governs the entire document. All tables, UX sections, and mitigation rows comply
with the schemas declared here.

#### Schema A — Comparative Analysis Tables

Every table containing quantified estimates uses:

| BASELINE | PROTECTED | DERIVATION CHAIN | DELTA |

- **BASELINE:** current / unprotected system behavior
- **PROTECTED:** system behavior with mitigations applied
- **DERIVATION CHAIN:** full arithmetic computation chain — not a conclusion alone
- **DELTA:** net change

#### Schema B — UX Per-Tier Template

Every throttle tier in the UX analysis section (Section 5) uses ALL FOUR named fields in
structured form:

| FIELD-A: Error code or platform signal | FIELD-B: User-visible behavior | FIELD-C: Visibility level | FIELD-D: Recovery path |

- **FIELD-A:** specific HTTP status, connector event, or Power Automate run history marker
  (e.g., "HTTP 429 with Retry-After header", "ActionThrottled in run history")
- **FIELD-B:** what the user observes or experiences at this tier — specific to this tier
- **FIELD-C:** EXPLICIT (user sees error/message/notification) or SILENT (background, user
  unaware)
- **FIELD-D:** exact recovery path available — manual retry / automatic exponential backoff /
  permanent failure after N retries / no recovery path

A tier described in free prose without the Schema B column structure does not satisfy Section 5
even if all four topics are mentioned in the prose.

#### Rejection Clauses

**STRUCTURAL REJECTION CLAUSE — Schema A (scan-time):**
A required column (BASELINE, PROTECTED, DERIVATION CHAIN, or DELTA) is absent from a table's
column structure. Detection: scan-time — count headers without reading cells. Marker:
`[STRUCTURAL VIOLATION (Schema A) — missing column: {name}]`. Remediation: add the column.

**STRUCTURAL REJECTION CLAUSE — Schema B (scan-time):**
A required field column (FIELD-A, FIELD-B, FIELD-C, or FIELD-D) is absent from a UX tier's
template structure in Section 5. Detection: scan-time — count field labels without reading
content. Marker: `[STRUCTURAL VIOLATION (Schema B) — missing field: FIELD-X]`. Remediation:
add the field label and populate it.

**CONTENT REJECTION CLAUSE (read-time):**
A required column or field is present in structure but its cell contains only a conclusion or
tier label without the mandated derivation steps or field-specific content. Detection:
read-time — requires reading the cell. Marker: `[CONTENT VIOLATION — conclusion only: {name}]`.
Remediation: deepen the cell.

All three rejection clauses apply throughout this document. Violations are flagged inline and
enumerated in the Terminal Reconciler (Section 10).

---

### SECTION 1 — RATE LIMIT REGISTRY

**[Gate: Verdict Block and Format Contract both written above before this section begins.]**

Enumerate rate limits with numeric thresholds, scope, and enforcement points. At least one
concrete numeric threshold required. Estimates labeled.

**Verdict currency check:** Do findings revise claim (a) or (c)? If yes: insert
"REVISED — see Section 1" in the Verdict Block.

---

### SECTION 2 — BINDING CONSTRAINT DETERMINATION

**[Gate: Rate limit registry with at least one numeric threshold complete. Verdict current.]**

Identify the binding constraint. Provide explicit reasoning: why this limit — not a
higher-capacity one — is hit first or most severely under the described load.

**Verdict currency check:** Confirm claim (a) or mark REVISED.

---

### SECTION 3 — BURST PATH AUDIT

**[Gate: Binding constraint identified with explicit reasoning. Verdict current.]**

Identify at least one structurally unprotected burst path. For each: trigger/action, missing
controls, and STRUCTURAL vs. INCIDENTAL classification (stated and justified, not implied).

**Verdict currency check:** Confirm claim (b) or mark REVISED.

---

### SECTION 4 — RETRY-AFTER GAP CHECK

**[Gate: At least one burst path with STRUCTURAL/INCIDENTAL classification. Verdict current.]**

Evaluate Retry-After handling (or equivalent: `x-ms-ratelimit-remaining`, `Retry-After-Ms`)
for every throttled path. Flag missing handling with failure mode.

**Verdict currency check:** Confirm claims (b) and (c) or mark REVISED.

---

### SECTION 5 — UX PER THROTTLE TIER [Schema B Required — See Format Contract]

**[Gate: All throttled paths evaluated for Retry-After handling. Verdict current.]**

Apply Schema B to every throttle tier reached in this scenario. Use the four-column template
declared in the Format Contract for each tier. Do not use free prose.

For each tier:

| Field | Content |
|-------|---------|
| FIELD-A — Error code or platform signal | [populate per Format Contract Schema B definition] |
| FIELD-B — User-visible behavior | [populate per Format Contract Schema B definition] |
| FIELD-C — Visibility level | EXPLICIT / SILENT |
| FIELD-D — Recovery path | [populate per Format Contract Schema B definition] |

**Structural check (Schema B):** after completing each tier, confirm all four field labels are
present. Missing label → apply Schema B STRUCTURAL REJECTION CLAUSE.

**Content check:** after completing each tier, confirm each cell has substantive field-specific
content. Label-only cell → apply CONTENT REJECTION CLAUSE.

**Verdict currency check:** Confirm claim (c) or mark REVISED.

**Gate 5→6:** ALL FOUR Schema B fields (FIELD-A, FIELD-B, FIELD-C, FIELD-D) present and
substantively populated for EVERY tier described in this document. At least two tiers described.
Schema B column structure (not free prose) used for every tier. Verdict current.

Do not begin Section 6 until Gate 5→6 is satisfied.

---

### SECTION 6 — CAUSAL CHAIN TO FAILURE MODE

**[Gate 5→6 satisfied: ALL FOUR Schema B fields present for every tier. Verdict current.]**

Trace: trigger event → rate-limited endpoint → failure mode. Every link stated explicitly.
Implied causation does not pass.

**Verdict currency check:** Mark REVISED for any revised claim.

---

### SECTION 7 — CASCADING THROTTLE FAILURE

**[Gate: Causal chain with every link explicit. Verdict current.]**

Construct a scenario where throttling at one tier causally triggers a second throttle event at
a different tier. Causal linkage required. Describe compounding effect on throughput or error
rate.

**Verdict currency check:** Mark REVISED for any revised claim.

---

### SECTION 8 — VOLUME-TO-BEHAVIOR MAPPING

**[Gate: Cascade scenario with causal linkage named. Verdict current.]**

Produce a comparative table using Schema A. For each volume tier: BASELINE behavior, PROTECTED
behavior, DERIVATION CHAIN, DELTA.

Load spike tier DERIVATION CHAIN cell must contain:
- Step 1: requests/interval × load multiplier = peak load `[cite Section 1 values]`
- Step 2: peak load − rate limit = overflow volume
- Step 3: overflow × retry factor = failed request volume
- Step 4: failed / peak = failure percentage

Conclusion-only cell → apply CONTENT REJECTION CLAUSE.

**Verdict currency check:** Confirm claim (c) or mark REVISED.

---

### SECTION 9 — MITIGATIONS

**[Gate: Schema A volume table with arithmetic derivation in load spike cell. Verdict current.]**

Per-bottleneck prescriptions naming specific action/setting/pattern. Before-state and
after-state for each. Generic advice without naming the specific action does not pass.

**Verdict currency check:** Mark REVISED for any revised claim.

---

### SECTION 10 — TERMINAL RECONCILER

**[Gate: Per-bottleneck mitigations with named actions and before/after states. Verdict current.]**

Audit the complete document. Produce named finding record.

**(a) Verdict audit:** For each claim (a)–(c): confirmed or marked REVISED with forward
reference? List any revised claim without a marker as a violation.

**(b) Gate audit:** Enumerate section transitions (Sections 1–9). Confirm named deliverables
from prior section present.
- For Gate 5→6 specifically: confirm FIELD-A, FIELD-B, FIELD-C, and FIELD-D are present for
  EVERY tier described in the document (not only the minimum two).

**(c) Schema A audit:** Scan all quantified tables. Flag each DERIVATION CHAIN cell containing
only a conclusion as a CONTENT VIOLATION.

**(d) Schema B audit:** Scan Section 5. For each tier, confirm the four-column Schema B
structure was used. Flag any tier using free prose as a STRUCTURAL VIOLATION (Schema B). Flag
any tier with a populated label but empty/conclusion-only cell as a CONTENT VIOLATION.

**Output:** `Reconciler Findings: N violation(s)` with itemized list, or
`Reconciler Findings: 0 violations`.

---

## V-03

**Axis:** Phase lifecycle — UX Per Tier is Phase 4, an explicitly numbered and named phase in
the lifecycle, whose gate condition enumerates all four required fields as individually named
blocking checklist items. Each phase gate includes an explicit Verdict-currency check that
embeds the "REVISED — see Phase N" marker at the gate boundary rather than deferring to
a terminal reconciler.

**Hypothesis:** A phase-driven structure where UX is Phase 4 with a field-level blocking gate
achieves C-26 through the lifecycle's natural phase-transition mechanism. Unlike a role sequence
(V-01) or a schema declaration (V-02), the phase structure makes each field a separately
enumerated gate condition — failing any single field blocks the entire phase transition,
making incompleteness structurally impossible to overlook. Per-gate Verdict currency checks
(C-22) satisfy C-18 at each phase boundary rather than deferring all revision marking to a
terminal reconciler.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
rate-limited systems.

**SCENARIO:** {scenario}

Proceed through the following phases in order. Each phase gate blocks the next phase. Do not
advance to the next phase until all gate conditions for the current phase are confirmed
satisfied.

---

### PHASE 0 — VERDICT

**[No prior gate. This phase must be completed before any other phase.]**

State and commit to before all analysis:

(a) **Binding constraint:** named component + numeric threshold
(b) **Primary gap:** named action or path where burst path or Retry-After failure occurs
(c) **System status:** SAFE / DEGRADED / FAILING at stated load
(d) **UX completeness commitment:** all four fields will be delivered for every throttle tier
    described in Phase 4 — (i) error code or platform signal, (ii) user-visible behavior,
    (iii) visibility level, (iv) recovery path. Any tier missing any field is a revision of
    this commitment.

Self-containment: a reader who reads only Phase 0 knows the core finding and the UX completeness
contract.

**Gate 0→1:**
- [ ] Claim (a) stated with component name and numeric threshold
- [ ] Claim (b) stated with named action or path
- [ ] Claim (c) stated as SAFE / DEGRADED / FAILING
- [ ] Claim (d) stated with all four field names enumerated

Phase 1 does not begin until all four gate items are checked.

---

### PHASE 1 — FORMAT CONTRACT

**[Gate 0→1 satisfied before Phase 1 begins.]**

Declare structural contracts:

**Table contract (Schema A):** every comparative table uses
BASELINE | PROTECTED | DERIVATION CHAIN | DELTA.
- BASELINE: current/unprotected state.
- PROTECTED: mitigated state.
- DERIVATION CHAIN: step-by-step arithmetic (not a conclusion alone).
- DELTA: net change.

**UX template contract (Schema B):** Phase 4 applies the four-field template to every tier:
- FIELD-A: error code or platform signal
- FIELD-B: user-visible behavior
- FIELD-C: visibility level (EXPLICIT / SILENT)
- FIELD-D: recovery path

This contract codifies Phase 0's Claim (d). Schema B is the structural enforcement of that
commitment.

**Rejection clauses:**
- **STRUCTURAL** (scan-time): required column or field label absent — detect by counting
  headers/labels — marker: `[STRUCTURAL VIOLATION]` — remediate: add structure.
- **CONTENT** (read-time): column/field present but cell has conclusion only — detect by
  reading — marker: `[CONTENT VIOLATION]` — remediate: deepen cell.

**Gate 1→2:**
- [ ] Schema A declared with all four columns named
- [ ] Schema B declared with all four field names (FIELD-A through FIELD-D)
- [ ] Both rejection clause types declared with detection method and remediation

Phase 2 does not begin until all three gate items are checked.

---

### PHASE 2 — RATE LIMIT ANALYSIS

**[Gate 1→2 satisfied before Phase 2 begins.]**

**Step 2a — Rate Limit Registry:** enumerate rate limits with numeric thresholds, scope,
enforcement points. At least one concrete numeric threshold. Estimates labeled.

**Step 2b — Binding Constraint:** identify the binding constraint with explicit reasoning.
Why this limit — not a higher-capacity one — is hit first.

**Step 2c — Burst Path Audit:** identify at least one unprotected burst path. Classify
STRUCTURAL vs. INCIDENTAL (stated and justified, not implied).

**Step 2d — Retry-After Gap Check:** evaluate Retry-After handling for every throttled path.
Flag missing handling with failure mode.

**Verdict currency check (per step):** after each step, check whether findings revise
Claims (a)–(d) from Phase 0. If any step revises a claim: insert "REVISED — see Phase 2,
Step [N]" inline in the Phase 0 Verdict block for that claim before continuing.

**Gate 2→3:**
- [ ] Rate limit registry with at least one numeric threshold (Step 2a)
- [ ] Binding constraint identified with explicit reasoning (Step 2b)
- [ ] At least one burst path with STRUCTURAL/INCIDENTAL classification (Step 2c)
- [ ] Every throttled path evaluated for Retry-After handling with failure mode (Step 2d)
- [ ] Verdict updated for any revised claims

Phase 3 does not begin until all five gate items are checked.

---

### PHASE 3 — FAILURE MODE CHAIN

**[Gate 2→3 satisfied before Phase 3 begins.]**

**Step 3a — Causal Chain:** trace trigger event → rate-limited endpoint → failure mode. Every
link explicit. Implied causation does not pass.

**Step 3b — Cascading Failure:** construct a scenario where throttling at one tier causally
triggers a second throttle event at a different tier. Causal linkage required. Describe
compounding effect.

**Verdict currency check:** after each step, check whether findings revise Claims (a)–(d).
Insert "REVISED — see Phase 3, Step [N]" for any revised claim before continuing.

**Gate 3→4:**
- [ ] Causal chain with every link explicit (Step 3a)
- [ ] Cascade scenario with causal linkage named and compounding effect described (Step 3b)
- [ ] Verdict updated for any revised claims

Phase 4 does not begin until all three gate items are checked.

---

### PHASE 4 — UX PER THROTTLE TIER [CRITICAL PHASE — GATE IS FIELD-LEVEL]

**[Gate 3→4 satisfied before Phase 4 begins.]**

Apply the Schema B four-field template from Phase 1 to EVERY throttle tier reached in this
scenario. This phase delivers on Phase 0's Claim (d) commitment.

For each tier, use the following structured format — do not use free prose:

---
**[Tier Name]**

- **FIELD-A — Error code or platform signal:**
  [specific HTTP status, connector event, or run history marker]
- **FIELD-B — User-visible behavior:**
  [what the user observes or experiences at this tier — specific, not generic]
- **FIELD-C — Visibility level:**
  EXPLICIT (user sees error/message) or SILENT (background, user unaware)
- **FIELD-D — Recovery path:**
  [manual retry / automatic exponential backoff with Retry-After parsed /
  permanent failure after N retries / no recovery path]

---

After completing each tier entry:
1. Confirm all four field labels are present → missing label: `[STRUCTURAL VIOLATION]`
2. Confirm each cell has substantive content → label-only: `[CONTENT VIOLATION]`

**Verdict currency check:** after completing all tiers, check whether any UX finding revises
Claims (a)–(d). If Claim (d) must be marked REVISED (because a tier is missing a field):
insert "REVISED — see Phase 4" in the Phase 0 Verdict block before proceeding to the gate.

**GATE 4→5 [FIELD-LEVEL BLOCKING GATE]:**

Evaluate each of the following independently — all must be satisfied:

- [ ] **FIELD-A present** for every tier described in this document (not only the minimum two)
- [ ] **FIELD-B present** for every tier described in this document
- [ ] **FIELD-C present** (and labeled EXPLICIT or SILENT) for every tier
- [ ] **FIELD-D present** for every tier described in this document
- [ ] At least two tiers described
- [ ] Schema B template structure (not free prose) used for every tier
- [ ] Claim (d) confirmed, or marked "REVISED — see Phase 4" with all four fields enumerated

A tier with three fields and one absent fails this gate for that tier. A tier described in
free prose mentioning all topics fails this gate for that tier. The gate cannot be unlocked
by completing some tiers; EVERY tier must satisfy all four field checks.

Phase 5 does not begin until every checklist item above is confirmed.

---

### PHASE 5 — VOLUME-TO-BEHAVIOR MAPPING

**[Gate 4→5 satisfied: all four Schema B fields confirmed for every tier. Verdict current.]**

Produce a table using Schema A (BASELINE | PROTECTED | DERIVATION CHAIN | DELTA). Show
behavior at each request volume tier in both states.

For the load spike tier (5x nominal or scenario-equivalent):
- DERIVATION CHAIN cell must show ALL steps:
  - Step 1: requests/interval × load multiplier = peak load `[cite Phase 2 values]`
  - Step 2: peak load − rate limit = overflow volume
  - Step 3: overflow × retry factor = failed request volume
  - Step 4: failed / peak = failure percentage
- Conclusion-only cell → `[CONTENT VIOLATION]`

**Verdict currency check:** Confirm Claim (c) or mark "REVISED — see Phase 5".

**Gate 5→6:**
- [ ] Schema A table with all four columns present
- [ ] Load spike tier with full arithmetic derivation (Steps 1–4)
- [ ] Claim (c) confirmed or marked REVISED

Phase 6 does not begin until all three gate items are checked.

---

### PHASE 6 — MITIGATIONS

**[Gate 5→6 satisfied before Phase 6 begins.]**

For each bottleneck and burst path: concrete mitigation naming specific action/setting/pattern.
Before-state and after-state for each. Generic advice without naming the specific action fails.

**Verdict currency check:** Mark "REVISED — see Phase 6" for any revised claim.

**Gate 6→7:**
- [ ] Per-bottleneck mitigations with named actions
- [ ] Before-state and after-state for each
- [ ] Verdict current

Phase 7 does not begin until all three gate items are checked.

---

### PHASE 7 — TERMINAL RECONCILER

**[Gate 6→7 satisfied before Phase 7 begins.]**

Audit the complete document. Produce named finding record.

**(a) Verdict audit (Claims (a)–(d)):**
- For each claim revised during analysis: confirm inline "REVISED — see Phase N, Step N"
  marker is present with correct forward reference.
- For Claim (d) specifically: confirm FIELD-A, FIELD-B, FIELD-C, and FIELD-D are all present
  for every throttle tier described in the document.

**(b) Phase gate audit:** enumerate gates 0→1 through 6→7. Confirm each checklist item
satisfied.
- Gate 4→5 audit: verify each of the four FIELD checks passed for every tier, not only the
  minimum two.

**(c) Derivation chain audit:** scan Schema A tables. Flag conclusion-only DERIVATION CHAIN
cells as CONTENT VIOLATIONS.

**(d) Schema B audit:** scan Phase 4. Flag any tier using free prose (STRUCTURAL VIOLATION)
or any tier with a populated label but empty/conclusion-only cell (CONTENT VIOLATION).

**Output:** `Reconciler Findings: N violation(s)` with itemized list, or
`Reconciler Findings: 0 violations`.

---

## V-04

**Axes (combined V-01 + V-02):** Explicit UX role in numbered sequence (V-01) combined with
Format Contract schema declaring the UX template (V-02). The role sequence provides the gate
with field-level blocking; the Format Contract provides schema authority that makes the
four-field names canonical across the entire document so every reference to UX completeness
points to the same authoritative definition.

**Hypothesis:** V-01 enforces C-26 through gate conditions that name the four fields in the
role's blocking gate. V-02 enforces C-26 through the Format Contract's Schema B declaration.
Combining both creates dual-authority enforcement: the four fields are defined canonically
in the Format Contract (making them referenceable by name in any section) AND enforced as
gate deliverables in the explicit UX role (making incompleteness structurally blocking). A
document with only one mechanism can satisfy C-26; a document with both mechanisms satisfies
C-26 more robustly because Format Contract violations are detectable at scan time (STRUCTURAL
REJECTION CLAUSE) and role gate violations are detectable at transition time. The two-tier
rejection clause taxonomy (C-25) is the natural structural consequence of combining both.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is fully
satisfied.

---

### ROLE 0 — VERDICT BLOCK

State before any analysis:

(a) **Binding constraint:** component name + numeric threshold
(b) **Primary gap:** named action or path where burst or Retry-After failure occurs
(c) **System status:** SAFE / DEGRADED / FAILING at stated load

Self-containment: a reader who reads only this block knows the core finding. Evidence sections
confirm or mark each claim REVISED with a forward reference.

**Gate 0→1:** Verdict Block with claims (a)–(c) written before Role 1 begins.

---

### ROLE 1 — FORMAT CONTRACT

**[Gate 0→1 satisfied before Role 1 begins.]**

Declare the structural contract governing this entire document.

#### Schema A — Comparative Tables

Every table with quantified estimates uses:

| BASELINE | PROTECTED | DERIVATION CHAIN | DELTA |

- **BASELINE:** current / unprotected system behavior
- **PROTECTED:** system behavior with mitigations applied
- **DERIVATION CHAIN:** full arithmetic computation steps — not a conclusion alone
- **DELTA:** net change from BASELINE to PROTECTED

#### Schema B — UX Per-Tier Template

Every throttle tier in Role 7 uses ALL FOUR of the following named fields in structured form:

- **FIELD-A:** Error code or platform signal (HTTP status, connector event, run history marker)
- **FIELD-B:** User-visible behavior (what user observes or experiences — tier-specific)
- **FIELD-C:** Visibility level — EXPLICIT (user sees error/message) or SILENT (background)
- **FIELD-D:** Recovery path (manual retry / automatic backoff / permanent failure / none)

Schema B is the canonical definition of the four-field UX requirement for this document.
All references to "UX completeness" in gate conditions and the terminal reconciler refer to
these four named fields.

#### Rejection Clauses

**STRUCTURAL REJECTION CLAUSE — Schema A (scan-time):**
Required column absent from a table's column structure.
Detection: scan-time (count column headers).
Marker: `[STRUCTURAL VIOLATION (Schema A) — missing: {column}]`.
Remediation: add the missing column.

**STRUCTURAL REJECTION CLAUSE — Schema B (scan-time):**
Required field (FIELD-A, FIELD-B, FIELD-C, or FIELD-D) absent from a UX tier's template
structure in Role 7.
Detection: scan-time (count field labels per tier).
Marker: `[STRUCTURAL VIOLATION (Schema B) — missing: FIELD-X for tier: {name}]`.
Remediation: add the missing field label and populate it.

**CONTENT REJECTION CLAUSE (read-time):**
Required column or field is present in structure but cell contains only a conclusion or label
without mandated derivation steps or field-specific content.
Detection: read-time (requires reading cell content).
Marker: `[CONTENT VIOLATION — conclusion only: {name}]`.
Remediation: deepen the cell.

All three clauses apply throughout. Violations flagged inline and enumerated in Role 12
terminal reconciler.

**Gate 1→2:** Format Contract written with Schema A, Schema B (four fields named), and all
three rejection clause types with detection method and remediation for each. Do not begin
Role 2 until this gate is satisfied.

---

### ROLE 2 — RATE LIMIT REGISTRY

**[Gate 1→2 satisfied before Role 2 begins.]**

Enumerate rate limits with numeric thresholds, scope, enforcement points. At least one concrete
numeric threshold. Estimates labeled.

**Verdict currency check:** Confirm claim (a) or (c) or mark "REVISED — see Role 2".

**Gate 2→3:** At least one numeric rate limit; Verdict current. Do not begin Role 3 until
this gate is satisfied.

---

### ROLE 3 — BINDING CONSTRAINT DETERMINATION

**[Gate 2→3 satisfied before Role 3 begins.]**

Identify the binding constraint with explicit reasoning: why this limit — not a higher-capacity
one — is hit first or most severely at the stated load.

**Verdict currency check:** Confirm claim (a) or mark "REVISED — see Role 3".

**Gate 3→4:** Binding constraint identified with explicit reasoning; Verdict claim (a)
confirmed or marked REVISED. Do not begin Role 4 until this gate is satisfied.

---

### ROLE 4 — BURST PATH AUDIT

**[Gate 3→4 satisfied before Role 4 begins.]**

Identify at least one unprotected burst path: trigger/action, missing controls, STRUCTURAL vs.
INCIDENTAL classification (stated and justified, not implied).

**Verdict currency check:** Confirm claim (b) or mark "REVISED — see Role 4".

**Gate 4→5:** At least one burst path with STRUCTURAL/INCIDENTAL classification; Verdict claim
(b) confirmed or marked REVISED. Do not begin Role 5 until this gate is satisfied.

---

### ROLE 5 — RETRY-AFTER GAP CHECK

**[Gate 4→5 satisfied before Role 5 begins.]**

Evaluate Retry-After handling for every throttled path. Flag missing handling with failure mode.

**Verdict currency check:** Confirm claims (b) and (c) or mark REVISED.

**Gate 5→6:** Every throttled path evaluated; Verdict current. Do not begin Role 6 until
this gate is satisfied.

---

### ROLE 6 — CAUSAL CHAIN AND CASCADE

**[Gate 5→6 satisfied before Role 6 begins.]**

**Step 6a — Causal Chain:** trace trigger event → rate-limited endpoint → failure mode. Every
link explicit.

**Step 6b — Cascading Failure:** construct scenario where throttling at one tier causally
triggers a second throttle at a different tier. Causal linkage required.

**Verdict currency check:** Mark "REVISED — see Role 6" for any revised claim.

**Gate 6→7:** Causal chain complete; cascade scenario with causal linkage; Verdict current.
Do not begin Role 7 until this gate is satisfied.

---

### ROLE 7 — UX PER THROTTLE TIER [REQUIRED ROLE — DO NOT SKIP OR MERGE]

**[Gate 6→7 satisfied before Role 7 begins.]**

Apply Schema B (declared in Role 1 Format Contract) to EVERY throttle tier reached in this
scenario. The Format Contract's Schema B definition is the authority for what each field
requires. Do not use free prose — use the four-field template structure.

For each tier:

---
**[Tier Name]**

| Field | Content |
|-------|---------|
| **FIELD-A** — Error code or platform signal | [per Schema B definition in Role 1] |
| **FIELD-B** — User-visible behavior | [per Schema B definition in Role 1] |
| **FIELD-C** — Visibility level | EXPLICIT / SILENT (per Schema B definition in Role 1) |
| **FIELD-D** — Recovery path | [per Schema B definition in Role 1] |

---

After each tier:
- Count field labels present → missing: apply Schema B STRUCTURAL REJECTION CLAUSE
- Read each cell for substantive content → conclusion-only: apply CONTENT REJECTION CLAUSE

**Verdict currency check:** Mark "REVISED — see Role 7" for any revised claim.

**GATE 7→8 [FIELD-LEVEL GATE — REFERENCES FORMAT CONTRACT SCHEMA B]:**

Do not begin Role 8 until ALL of the following are confirmed:

- [ ] **FIELD-A** (as defined in Format Contract Schema B) present for **every** tier
- [ ] **FIELD-B** (as defined in Format Contract Schema B) present for **every** tier
- [ ] **FIELD-C** (as defined in Format Contract Schema B) present for **every** tier
- [ ] **FIELD-D** (as defined in Format Contract Schema B) present for **every** tier
- [ ] At least two tiers described using Schema B template structure (not free prose)
- [ ] No Schema B STRUCTURAL VIOLATIONS remain unresolved
- [ ] Verdict current

---

### ROLE 8 — VOLUME-TO-BEHAVIOR MAPPING

**[Gate 7→8 satisfied: all four Schema B fields confirmed for every tier. Verdict current.]**

Produce comparative table using Schema A. For each volume tier: BASELINE and PROTECTED behavior,
DERIVATION CHAIN, DELTA.

Load spike tier DERIVATION CHAIN:
- Step 1: requests/interval × load multiplier = peak load `[cite Role 2 values]`
- Step 2: peak load − rate limit = overflow volume
- Step 3: overflow × retry factor = failed request volume
- Step 4: failed / peak = failure %

Conclusion-only cell → CONTENT REJECTION CLAUSE.

**Verdict currency check:** Confirm claim (c) or mark "REVISED — see Role 8".

**Gate 8→9:** Schema A table with all four columns; load spike derivation chain; Verdict
current. Do not begin Role 9 until this gate is satisfied.

---

### ROLE 9 — MITIGATIONS

**[Gate 8→9 satisfied before Role 9 begins.]**

Per-bottleneck prescriptions naming specific action/setting/pattern. Before-state and
after-state for each.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 9→10:** Per-bottleneck mitigations; Verdict current. Do not begin Role 10 until
this gate is satisfied.

---

### ROLE 10 — TERMINAL RECONCILER

**[Gate 9→10 satisfied before Role 10 begins.]**

Audit the complete document. Produce named finding record.

**(a) Verdict audit:** claims (a)–(c) confirmed or marked REVISED with forward references?
List any revised claim without a marker.

**(b) Gate audit:** enumerate role transitions 0→1 through 9→10. Confirm named deliverables
from prior role present.
- Gate 7→8 specifically: confirm FIELD-A (Schema B definition), FIELD-B, FIELD-C, and FIELD-D
  all present for EVERY tier described in the document. Cross-reference Role 1 Format Contract
  Schema B for the authoritative field definitions.

**(c) Schema A derivation chain audit:** flag conclusion-only DERIVATION CHAIN cells as
CONTENT VIOLATIONS.

**(d) Schema B UX audit:** confirm Schema B template structure (not free prose) used for every
tier in Role 7. Flag structural and content violations by type using the Format Contract
rejection clause taxonomy.

**Output:** `Reconciler Findings: N violation(s)` with itemized list, or
`Reconciler Findings: 0 violations`.

---

## V-05

**Axes (combined V-01 + V-02 + V-03):** Full structural synthesis — explicit UX role in
numbered sequence (V-01) + Format Contract Schema B with UX-specific STRUCTURAL clause (V-02) +
Phase-lifecycle field-level blocking gate (V-03) + two-tier rejection clause taxonomy (C-25) +
terminal reconciler auditing UX completeness via check (b) with field enumeration (C-24) +
per-gate Verdict currency checks (C-22).

**Hypothesis:** All three single-axis C-26 mechanisms are structurally orthogonal — they enforce
the four-field requirement through distinct channels that can each fail independently:
(1) Role gate can be satisfied by populating fields without them being schema-declared;
(2) Format Contract schema can be declared without appearing in a role gate;
(3) Phase blocking gate can be applied without a Format Contract authority.
Combining all three creates redundant, overlapping enforcement: a field missing from any tier
is simultaneously a schema violation (detectable at scan time via Schema B STRUCTURAL REJECTION
CLAUSE), a gate violation (blocking the next role at the field-level checklist), and a Verdict
revision (Claim (d) broken). Any single mechanism catching the gap ensures the reconciler
can enumerate it in check (b) and the Verdict block will carry the revision marker. No single
mechanism can be satisfied while bypassing C-26.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
rate-limited systems.

**SCENARIO:** {scenario}

**Structural enforcement architecture:**
Verdict-first commitment (Phase 0) → Format Contract schema authority (Phase 1) → Role sequence
with full gate chain → Per-gate Verdict currency checks → Terminal reconciler with field-level
audit. Every section transition is gated. No section is reachable without all prior sections'
named deliverables confirmed present.

---

### PHASE 0 / ROLE 0 — VERDICT BLOCK

State and commit before any analysis:

(a) **Binding constraint:** component name + numeric threshold
(b) **Primary gap:** named action or path where burst or Retry-After failure occurs
(c) **System status:** SAFE / DEGRADED / FAILING at stated load
(d) **UX completeness commitment:** all four fields will be delivered for every throttle tier
    in Role 7 — (i) error code or platform signal, (ii) user-visible behavior,
    (iii) visibility level, (iv) recovery path. Any tier missing any field is a revision of
    this commitment.

Self-containment: reader who reads only this block knows the core finding and UX contract.
Evidence sections confirm or insert "REVISED — see Role N" for any revised claim.

**Gate 0→1:**
- [ ] Claims (a)–(c) stated
- [ ] Claim (d) stated with all four field names individually enumerated

Do not begin Role 1 until both gate items are confirmed.

---

### ROLE 1 — FORMAT CONTRACT

**[Gate 0→1 satisfied before Role 1 begins.]**

Declare the structural contract governing this entire document.

#### Schema A — Comparative Tables

Every table with quantified estimates uses:

| BASELINE | PROTECTED | DERIVATION CHAIN | DELTA |

- **BASELINE:** current / unprotected system behavior
- **PROTECTED:** system behavior with mitigations applied
- **DERIVATION CHAIN:** full arithmetic computation chain — not a conclusion alone
- **DELTA:** net change from BASELINE to PROTECTED

#### Schema B — UX Per-Tier Template (canonical authority for Role 7 and Claim (d))

Every throttle tier in Role 7 uses ALL FOUR named fields in structured table form:

| FIELD-A: Error code / platform signal | FIELD-B: User-visible behavior | FIELD-C: Visibility level | FIELD-D: Recovery path |

- **FIELD-A:** specific HTTP status, connector event, or Power Automate run history marker
- **FIELD-B:** what the user observes or experiences — specific to this tier, not generic
- **FIELD-C:** EXPLICIT (user sees error/message/notification) or SILENT (background)
- **FIELD-D:** exact recovery path — manual retry / automatic exponential backoff with
  Retry-After parsed / permanent failure after N retries / no recovery path available

Schema B is the canonical definition of Claim (d). Any gate condition or reconciler check
referencing "UX completeness" uses these four field names as the enumerated deliverables.

#### Rejection Clause Taxonomy

**Type 1 — STRUCTURAL REJECTION CLAUSE (scan-time detection):**

*Schema A form:* Required column (BASELINE, PROTECTED, DERIVATION CHAIN, or DELTA) absent
from a table's column structure.
Detection method: scan-time — count column headers without reading cell content.
Violation marker: `[STRUCTURAL VIOLATION (Schema A) — missing column: {name}]`
Remediation: add the missing column header before proceeding.

*Schema B form:* Required field (FIELD-A, FIELD-B, FIELD-C, or FIELD-D) absent from a tier's
template structure in Role 7.
Detection method: scan-time — count field labels per tier without reading cell content.
Violation marker: `[STRUCTURAL VIOLATION (Schema B) — missing field: FIELD-X, tier: {name}]`
Remediation: add the missing field label and populate it.

**Type 2 — CONTENT REJECTION CLAUSE (read-time detection):**

Required column or field is present in structure but cell contains only a conclusion or label
without the mandated derivation steps or field-specific content.
Detection method: read-time — requires reading the cell to assess sufficiency.
Violation marker: `[CONTENT VIOLATION — conclusion only: {column or field name}]`
Remediation: deepen the cell with computation steps or field-specific content.

Both clause types apply throughout this document. Type 1 and Type 2 violations have distinct
detection methods and distinct remediations — a combined clause covering both would obscure
which remediation applies. Violations are flagged inline and enumerated in the Role 11
Terminal Reconciler by clause type.

**Gate 1→2:**
- [ ] Schema A declared with all four column names
- [ ] Schema B declared with all four field names (FIELD-A through FIELD-D) as the canonical
      definition of Claim (d)
- [ ] STRUCTURAL clause declared as Type 1 with scan-time detection method and remediation
- [ ] CONTENT clause declared as Type 2 with read-time detection method and remediation

Do not begin Role 2 until all four gate items are confirmed.

---

### ROLE 2 — RATE LIMIT REGISTRY

**[Gate 1→2 satisfied before Role 2 begins.]**

Enumerate rate limits with numeric thresholds, scope, enforcement points. At least one concrete
numeric threshold. Estimates labeled.

**Verdict currency check:** Do findings revise Claim (a) or (c)? If yes: insert
"REVISED — see Role 2" in the Verdict Block for the revised claim before continuing.

**Gate 2→3:**
- [ ] At least one rate limit with concrete numeric threshold
- [ ] Verdict current (updated if revised)

Do not begin Role 3 until both gate items are confirmed.

---

### ROLE 3 — BINDING CONSTRAINT DETERMINATION

**[Gate 2→3 satisfied before Role 3 begins.]**

Identify the binding constraint with explicit reasoning: why this limit — not a higher-capacity
one — is hit first or most severely at the stated load.

**Verdict currency check:** Confirm Claim (a) or insert "REVISED — see Role 3".

**Gate 3→4:**
- [ ] Binding constraint identified with explicit reasoning
- [ ] Claim (a) confirmed or marked REVISED

Do not begin Role 4 until both gate items are confirmed.

---

### ROLE 4 — BURST PATH AUDIT

**[Gate 3→4 satisfied before Role 4 begins.]**

Identify at least one structurally unprotected burst path: trigger/action, missing controls,
STRUCTURAL vs. INCIDENTAL classification (stated and justified, not implied).

**Verdict currency check:** Confirm Claim (b) or insert "REVISED — see Role 4".

**Gate 4→5:**
- [ ] At least one burst path with STRUCTURAL/INCIDENTAL classification
- [ ] Claim (b) confirmed or marked REVISED

Do not begin Role 5 until both gate items are confirmed.

---

### ROLE 5 — RETRY-AFTER GAP CHECK

**[Gate 4→5 satisfied before Role 5 begins.]**

Evaluate Retry-After handling (or equivalent: `x-ms-ratelimit-remaining`, `Retry-After-Ms`)
for every throttled path identified in Roles 3–4. Flag each missing-handling case with the
failure mode it causes.

**Verdict currency check:** Confirm Claims (b) and (c) or insert revision markers.

**Gate 5→6:**
- [ ] Every throttled path evaluated for Retry-After handling
- [ ] Missing handling flagged with failure mode
- [ ] Verdict current

Do not begin Role 6 until all three gate items are confirmed.

---

### ROLE 6 — CAUSAL CHAIN AND CASCADE

**[Gate 5→6 satisfied before Role 6 begins.]**

**Step 6a — Causal Chain:** trace trigger event → rate-limited endpoint → failure mode. Every
link stated explicitly. Implied causation does not pass.

**Step 6b — Cascading Failure:** construct a scenario where throttling at one tier causally
triggers a second throttle event at a different tier. Causal linkage required. Describe
compounding effect on throughput or error rate.

**Verdict currency check (per step):** insert "REVISED — see Role 6, Step [a/b]" for any
revised claim before continuing to the next step.

**Gate 6→7:**
- [ ] Causal chain complete with every link explicit (Step 6a)
- [ ] Cascade scenario with causal linkage and compounding effect described (Step 6b)
- [ ] Verdict current

Do not begin Role 7 until all three gate items are confirmed.

---

### ROLE 7 — UX PER THROTTLE TIER [REQUIRED ROLE — DO NOT SKIP OR MERGE]

**[Gate 6→7 satisfied before Role 7 begins.]**

Apply Schema B (Format Contract canonical definition) to EVERY throttle tier reached in this
scenario. This role delivers on Claim (d). Use the four-field table structure — do not use
free prose.

For each tier:

---
**[Tier Name]**

| Field | Content |
|-------|---------|
| **FIELD-A** — Error code or platform signal | [per Schema B: specific HTTP status, connector event, or run history marker] |
| **FIELD-B** — User-visible behavior | [per Schema B: what user observes or experiences — tier-specific] |
| **FIELD-C** — Visibility level | EXPLICIT / SILENT (per Schema B definition) |
| **FIELD-D** — Recovery path | [per Schema B: manual retry / automatic backoff / permanent failure / none] |

---

After each tier:
1. Count field labels → missing: `[STRUCTURAL VIOLATION (Schema B) — missing field: FIELD-X,
   tier: {name}]`
2. Read each cell → conclusion-only: `[CONTENT VIOLATION — conclusion only: FIELD-X]`

**Verdict currency check:** Does any UX finding revise Claim (d) or Claims (a)–(c)?
Insert "REVISED — see Role 7" for any revised claim before proceeding to the gate.

**GATE 7→8 [TRIPLE-ENFORCEMENT FIELD-LEVEL GATE]:**

Evaluate each of the following independently — all must be satisfied:

- [ ] **FIELD-A** (Schema B: error code or platform signal) present and substantively populated
      for **every** tier described in this document — not only the minimum two tiers
- [ ] **FIELD-B** (Schema B: user-visible behavior) present and substantively populated for
      **every** tier
- [ ] **FIELD-C** (Schema B: visibility level) present and labeled EXPLICIT or SILENT for
      **every** tier
- [ ] **FIELD-D** (Schema B: recovery path) present and substantively populated for **every**
      tier
- [ ] At least two tiers described using Schema B table structure (not free prose)
- [ ] No unresolved Schema B STRUCTURAL VIOLATIONS remain
- [ ] Claim (d) confirmed — or if any tier required a field to be added retroactively, Claim (d)
      is marked "REVISED — see Role 7" with the missing field(s) identified

A tier with three fields present and one absent does not pass this gate for that tier.
A tier described in free prose (even mentioning all four topics) does not pass this gate.
The gate cannot be unlocked by any tier; every tier must satisfy all four field checks.

Do not begin Role 8 until every checklist item is confirmed.

---

### ROLE 8 — VOLUME-TO-BEHAVIOR MAPPING

**[Gate 7→8 satisfied: all four Schema B fields confirmed for every tier. Verdict current.]**

Produce comparative table using Schema A (BASELINE | PROTECTED | DERIVATION CHAIN | DELTA).
Show behavior at each request volume tier.

Load spike tier DERIVATION CHAIN cell must contain ALL of:
- Step 1: requests/interval × load multiplier = peak load `[cite Role 2 numeric values]`
- Step 2: peak load − rate limit = overflow volume
- Step 3: overflow × retry factor = failed request volume
- Step 4: failed / peak = failure percentage

Conclusion-only cell → `[CONTENT VIOLATION — conclusion only: DERIVATION CHAIN]`.

**Verdict currency check:** Confirm Claim (c) or insert "REVISED — see Role 8".

**Gate 8→9:**
- [ ] Schema A table with all four columns (BASELINE, PROTECTED, DERIVATION CHAIN, DELTA)
- [ ] Load spike tier with full arithmetic derivation (Steps 1–4)
- [ ] Claim (c) confirmed or marked REVISED

Do not begin Role 9 until all three gate items are confirmed.

---

### ROLE 9 — MITIGATIONS

**[Gate 8→9 satisfied before Role 9 begins.]**

For each bottleneck and burst path: concrete mitigation naming specific action/setting/pattern
(e.g., "enable concurrency control on the For Each loop capped at 5 parallel branches",
"add exponential backoff with Retry-After header parsing to the HTTP action"). Generic advice
without naming the specific action/setting does not pass.

For each mitigation:
- **Before-state:** baseline behavior at this bottleneck (references a specific component and
  BASELINE-column entry)
- **After-state:** system behavior with mitigation applied (populates PROTECTED column in
  Role 8 table)

**Verdict currency check:** Mark "REVISED — see Role 9" for any revised claim.

**Gate 9→10:**
- [ ] Per-bottleneck mitigations with named actions
- [ ] Before-state and after-state for each mitigation
- [ ] Verdict current

Do not begin Role 10 until all three gate items are confirmed.

---

### ROLE 10 — TERMINAL RECONCILER

**[Gate 9→10 satisfied before Role 10 begins. This is the last role.]**

Audit the complete document. Produce a named finding record.

**Check (a) — Verdict audit (Claims (a)–(d)):**
For each claim revised during analysis: confirm inline "REVISED — see Role N" marker is present
with correct forward reference to the revising role.
- Claim (d) specifically: confirm FIELD-A, FIELD-B, FIELD-C, and FIELD-D (as defined in
  Format Contract Schema B) are all present for every throttle tier described in the document
  — not only the minimum two tiers.
List any revised claim without a marker as a violation. List Claim (d) as a violation if any
tier is missing any field even if no revision marker was required.

**Check (b) — Gate audit:**
Enumerate role transitions (Gates 0→1 through 9→10). For each gate, confirm the named
deliverables from the prior role are present.
- Gate 7→8 specifically: confirm all six checklist items satisfied, including FIELD-A, FIELD-B,
  FIELD-C, and FIELD-D confirmed for every tier.

**Check (c) — Schema A derivation chain audit:**
Scan all comparative tables. For each DERIVATION CHAIN cell: does it contain computation steps
(Steps 1–4), or only a conclusion? Flag each conclusion-only cell as:
`[CONTENT VIOLATION — conclusion only: DERIVATION CHAIN, table: {name}, tier: {name}]`

**Check (d) — Schema B UX audit:**
Scan Role 7. For each tier:
- Was Schema B table structure used (not free prose)?
  → No: `[STRUCTURAL VIOLATION (Schema B) — free prose used for tier: {name}]`
- Are all four field labels present?
  → Missing: `[STRUCTURAL VIOLATION (Schema B) — missing field: FIELD-X, tier: {name}]`
- Do all cells have substantive field-specific content?
  → Conclusion-only: `[CONTENT VIOLATION — conclusion only: FIELD-X, tier: {name}]`

Tag each violation with its clause type (Type 1 STRUCTURAL / Type 2 CONTENT) using the
Format Contract taxonomy declared in Role 1.

**Output:** `Reconciler Findings: N violation(s)` followed by itemized violation list
(each tagged by clause type), or `Reconciler Findings: 0 violations`.

Gate (document close): Reconciler produces a named finding record referencing all four checks.
Document is complete.
