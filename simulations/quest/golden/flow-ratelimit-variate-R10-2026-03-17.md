---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 10
rubric_version: 10
---

# flow-ratelimit — Variate R10

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence — Verdict Claim (d) commits to UX completeness and
tier count, subject to bidirectional revision marking), V-02 (output format — Schema B declared
as a named structural schema in Format Contract with its own STRUCTURAL REJECTION CLAUSE, parallel
to Schema A), V-03 (lifecycle emphasis — six-item UX gate with (a)–(f) enumerated separately,
closing the tier-count and structure-compliance bypass paths).
Combination variations: V-04 (role sequence + output format — Claim (d) + Schema B in Format
Contract + Terminal Reconciler Schema B audit as check (d)), V-05 (all three axes — Claim (d) +
Schema B + six-item gate with tier-count against burst path audit + full Terminal Reconciler).

**R10 target criteria: C-27, C-28, C-29**

C-27 (V-02 signal): Schema B is a named structural schema in the Format Contract with its own
STRUCTURAL REJECTION CLAUSE, making missing UX fields detectable at scan time without reading
prose. The Terminal Reconciler includes an explicit Schema B audit as check (d), distinct from
the gate audit (check b).

C-28 (V-03 signal A): Claim (d) in the Verdict Block commits to UX template completeness and
tier count. A tier added mid-analysis lacking full four-field coverage triggers a REVISED marker
on Claim (d) at the gate boundary, not only at terminal reconciliation.

C-29 (V-03 signal B): The UX gate enumerates six explicitly named blocking conditions: (a)–(d)
one condition per FIELD, (e) tier-count verification against the burst path audit section (not
merely the two-tier minimum), (f) structure-compliance confirmation as a separately named
blocking condition. Items (e) and (f) must not be collapsed into a compound condition.

**R10 variation axes:**

| Axis | What changes | C-27 | C-28 | C-29 | Predicted composite |
|------|-------------|------|------|------|---------------------|
| V-01: Role sequence | Verdict gains Claim (d); Gate 6→7 revised-marks Claim (d) | — | PASS | — | 118/120 |
| V-02: Output format | Schema B in Format Contract with named STRUCTURAL REJECTION CLAUSE; Reconciler check (d) | PASS | — | — | 118/120 |
| V-03: Lifecycle emphasis | Six-item gate (a)–(f) with (e) tier-count-against-burst-path and (f) structure-compliance separately named | — | — | PASS | 118/120 |
| V-04: Role seq + Output fmt | Claim (d) + Schema B + Reconciler check (d) | PASS | PASS | — | 120/120 |
| V-05: All three axes | Claim (d) + Schema B + Six-item gate + Reconciler checks (b)+(d) | PASS | PASS | PASS | 120/120 |

---

## V-01

**Axis:** Role sequence — the Verdict Block gains Claim (d) committing to UX template
completeness and tier count before analysis begins, making UX coverage automatically subject to
C-18 bidirectional revision marking. Gate 6→7 inserts a REVISED marker on Claim (d) when tier
count changes mid-analysis.

**Hypothesis:** Elevating UX commitment to Verdict level — alongside binding constraint (a),
primary gap (b), and system status (c) — means any mid-analysis tier discovered after Role 6
begins triggers a REVISED marker on Claim (d) at that gate boundary, not only at terminal
reconciliation. A Verdict-only reader gains UX coverage visibility without proceeding to the UX
section. V-02 through V-04 showed that the four-field gate (C-26) and Schema B (C-27) are
necessary for scan-time enforcement; this variation closes the Verdict-layer gap (C-28) as a
distinct mechanism.

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
(d) **UX coverage commitment:** total number of throttle tiers that will be described in this
    document, with a statement that every tier uses the complete four-field template (FIELD-A
    through FIELD-D). Format: "N tiers described; all tiers use the four-field UX template."

Self-containment requirement: a reader who reads only this block knows the core finding and the
scope of UX coverage without proceeding to the evidence sections. Evidence sections must confirm
each claim (a)–(d) or insert an inline "REVISED — see Role N" marker for any claim that changes.

**Revision rule for Claim (d):** if analysis in Roles 2–8 reveals an additional throttle tier
not anticipated at Verdict-write time, insert "REVISED — see Role N" on Claim (d) at the gate
of the role where the new tier was discovered. Do not defer the REVISED marker to the terminal
reconciler.

**Gate 0→1:** Verdict Block written with all four claims, including Claim (d) with tier count
and four-field template commitment, before Role 1 begins.

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
the described load. Provide explicit reasoning: why this limit, not a higher-capacity one, is
the binding constraint.

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

Record the count of distinct burst paths identified. This count feeds Gate 6→7 item (e).

**Verdict currency check:** Confirm Verdict claim (b), or insert "REVISED — see Role 4".

**Gate 4→5:** At least one burst path with STRUCTURAL vs. INCIDENTAL classification; burst path
count recorded; Verdict claim (b) confirmed or marked REVISED. Do not begin Role 5 until this
gate is satisfied.

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

**Verdict currency check for Claim (d):** count the tiers described in this role. If the count
differs from the tier count stated in Verdict Claim (d), insert "REVISED — see Role 6" on Claim
(d) immediately. Do not defer to terminal reconciliation.

**GATE 6→7 [FIELD-LEVEL GATE]:**

Do not begin Role 7 until ALL of the following are confirmed individually:

- [ ] **(a)** FIELD-A (error code or platform signal) is present and substantively populated
      for EVERY tier described in this document — not only the minimum two tiers
- [ ] **(b)** FIELD-B (user-visible behavior) is present and substantively populated for
      EVERY tier
- [ ] **(c)** FIELD-C (visibility level) is present and explicitly labeled EXPLICIT or SILENT
      for EVERY tier
- [ ] **(d)** FIELD-D (recovery path) is present and substantively populated for EVERY tier
- [ ] **(e)** Tier count in this section matches the count stated in Verdict Claim (d); if a
      new tier was discovered during this role, Claim (d) is already marked REVISED
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

**Check (a) — Verdict audit:** Scan Verdict claims (a)–(d). For each claim revised during
analysis, confirm an inline "REVISED — see Role N" marker is present with a forward reference
to the revising role. List any revised claim lacking a marker as a violation. Explicitly confirm
Claim (d) (UX tier count and template completeness) matches the actual tier count and template
usage in Role 6.

**Check (b) — Gate audit:** Enumerate each role transition (Gates 0→1 through 10→11). For each
gate, confirm the named deliverables from the prior role are present.
- For Gate 6→7 specifically: confirm FIELD-A, FIELD-B, FIELD-C, and FIELD-D are all present
  for every throttle tier described in the document, not only the minimum two tiers.

**Check (c) — Derivation chain audit:** Scan all quantified tables. For each DERIVATION CHAIN
cell: does it contain computation steps, or only a conclusion? Flag each conclusion-only cell
as a CONTENT VIOLATION.

**Output:** `Reconciler Findings: N violation(s)` followed by an itemized list, or
`Reconciler Findings: 0 violations` if the audit finds no issues.

**Gate 11 (document close):** Reconciler produces a named finding record referencing checks
(a), (b), and (c). Document is complete.

---

## V-02

**Axis:** Output format — Schema B (the four-field UX template) is declared as a named
structural schema in the Format Contract, parallel to Schema A, with its own STRUCTURAL
REJECTION CLAUSE enabling scan-time detection of missing UX fields. The Terminal Reconciler
includes an explicit Schema B audit as check (d), distinct from the gate audit.

**Hypothesis:** When the Format Contract explicitly names the UX template as Schema B —
with column-level field names and a dedicated STRUCTURAL REJECTION CLAUSE — missing UX fields
become detectable at scan time by counting field labels, exactly as a missing DERIVATION CHAIN
column is detectable at scan time by counting table headers. This scan-time property means any
tool or reviewer performing a structural scan of the document can confirm UX completeness
without reading UX prose. V-01 locates four-field authority in the role gate; this variation
locates it in the Format Contract, making it a document-level structural commitment rather than
a role-level instruction — which is the C-27 mechanism.

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

**STRUCTURAL REJECTION CLAUSE — Schema A (scan-time):**
A required column (BASELINE, PROTECTED, DERIVATION CHAIN, or DELTA) is absent from a table's
column structure. Detection: scan-time — count headers without reading cells. Marker:
`[STRUCTURAL VIOLATION (Schema A) — missing column: {name}]`. Remediation: add the column.

**CONTENT REJECTION CLAUSE — Schema A (read-time):**
A required column is present but its cell contains only a conclusion without derivation steps.
Detection: read-time — requires reading the cell. Marker:
`[CONTENT VIOLATION (Schema A) — conclusion only: {column name}]`. Remediation: deepen
the cell with computation steps.

---

#### Schema B — UX Per-Tier Template

Every throttle tier in the UX analysis section (Section 5) uses ALL FOUR named fields in
structured template form. Schema B is a named structural schema, not a formatting suggestion.

| FIELD-A: Error code or platform signal | FIELD-B: User-visible behavior | FIELD-C: Visibility level | FIELD-D: Recovery path |

- **FIELD-A:** specific HTTP status, connector event, or Power Automate run history marker
  (e.g., "HTTP 429 with Retry-After header", "ActionThrottled in run history")
- **FIELD-B:** what the user observes or experiences at this tier — specific to this tier
- **FIELD-C:** EXPLICIT (user sees error/message/notification) or SILENT (background, user
  unaware) — the label itself must appear, not a description that implies the label
- **FIELD-D:** exact recovery path — manual retry / automatic exponential backoff with
  Retry-After parsed / permanent failure after N retries / no recovery path

A tier described in free prose without the Schema B column structure does not satisfy Section 5
even if all four topics are mentioned in the prose.

**STRUCTURAL REJECTION CLAUSE — Schema B (scan-time):**
A required field label (FIELD-A, FIELD-B, FIELD-C, or FIELD-D) is absent from a UX tier
entry in Section 5. Detection: scan-time — count field labels in the tier block without reading
field content. Marker: `[STRUCTURAL VIOLATION (Schema B) — missing field: FIELD-X]`.
Remediation: add the field label and populate it before proceeding.

**CONTENT REJECTION CLAUSE — Schema B (read-time):**
A required field label is present but the content is a tier name or generic placeholder without
field-specific information. Detection: read-time — requires reading the field content. Marker:
`[CONTENT VIOLATION (Schema B) — label only: FIELD-X]`. Remediation: deepen the field with
substantive content.

All four rejection clauses (Schema A structural, Schema A content, Schema B structural,
Schema B content) apply throughout this document. Violations are flagged inline and enumerated
in the Terminal Reconciler (Section 10).

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

**Gate:** Binding constraint identified with explicit reasoning; Verdict claim (a) confirmed
or marked REVISED.

---

### SECTION 3 — BURST PATH AUDIT

**[Gate: Binding constraint identified. Verdict current.]**

Identify at least one structurally unprotected burst path. For each path:
- The trigger or action generating concurrent requests
- The missing controls (no concurrency cap / no retry policy / no queue buffer)
- **Classification:** STRUCTURAL vs. INCIDENTAL — stated and justified

**Verdict currency check:** Confirm claim (b) or mark REVISED.

**Gate:** At least one burst path with STRUCTURAL/INCIDENTAL classification; Verdict claim
(b) confirmed or marked REVISED.

---

### SECTION 4 — RETRY-AFTER GAP CHECK

**[Gate: Burst path audit complete. Verdict current.]**

Evaluate Retry-After header handling (or equivalent: `x-ms-ratelimit-remaining`,
`Retry-After-Ms`) at every throttled endpoint from Sections 2–3. Flag each missing-handling
case with its failure mode.

**Verdict currency check:** Confirm claims (b) and (c) or mark REVISED.

**Gate:** Every throttled path evaluated; missing handling flagged with failure mode; Verdict
current.

---

### SECTION 5 — UX PER THROTTLE TIER [REQUIRED SECTION — Schema B governs this section]

**[Gate: Retry-After gap check complete. Verdict current. Schema B declared in Format Contract.]**

Apply Schema B to EVERY throttle tier reached in this scenario. Every tier must use the Schema
B four-field template structure. Free prose is not a substitute, even if all four topics are
addressed in prose.

For each tier, produce one Schema B block:

---
**[Tier Name / throttle level]**

- **FIELD-A — Error code or platform signal:** [specific signal per Schema B definition]
- **FIELD-B — User-visible behavior:** [per Schema B — tier-specific, not generic]
- **FIELD-C — Visibility level:** EXPLICIT or SILENT [label must appear]
- **FIELD-D — Recovery path:** [exact path per Schema B definition]

---

After each tier: run the Schema B structural check (count field labels; flag missing as
STRUCTURAL VIOLATION (Schema B)) and Schema B content check (confirm substantive content;
flag label-only as CONTENT VIOLATION (Schema B)).

**Verdict currency check:** Confirm claim (c) or mark REVISED.

**Gate 5→6:** At least two tiers described using Schema B template structure; all four field
labels present and substantively populated for every tier; Verdict current.

---

### SECTION 6 — CAUSAL CHAIN TO FAILURE MODE

**[Gate: UX section complete per Schema B for all tiers. Verdict current.]**

Trace the complete causal chain from trigger event through the rate-limited endpoint to the
resulting failure mode. Every link explicit. Implied causation does not pass.

**Verdict currency check:** Mark REVISED for any revised claim.

---

### SECTION 7 — CASCADING THROTTLE FAILURE

**[Gate: Causal chain complete. Verdict current.]**

Construct a specific scenario where throttling at one tier causally triggers a second distinct
throttle event at a different tier. State the mechanism of causation and the compounding effect.

**Verdict currency check:** Mark REVISED for any revised claim.

---

### SECTION 8 — VOLUME-TO-BEHAVIOR MAPPING

**[Gate: Cascade scenario complete. Verdict current.]**

Produce a comparative table using the Schema A structure (BASELINE | PROTECTED | DERIVATION
CHAIN | DELTA). For the load spike tier (5x nominal):

DERIVATION CHAIN must contain:
- Step 1: requests per interval × load multiplier = peak load [cite Role 2 numeric values]
- Step 2: peak load − rate limit = overflow volume
- Step 3: overflow × retry factor = failed request volume
- Step 4: failed / peak = failure percentage

Conclusion-only cell → CONTENT REJECTION CLAUSE (Schema A).

**Verdict currency check:** Confirm claim (c) or mark REVISED.

**Gate 8→9:** Schema A table with all four columns; load spike derivation chain with Steps 1–4;
Verdict claim (c) confirmed or marked REVISED.

---

### SECTION 9 — MITIGATIONS

**[Gate: Volume table with full derivation chain complete. Verdict current.]**

Per-bottleneck mitigations with specific named actions and before/after states referencing
Schema A BASELINE and PROTECTED columns.

**Verdict currency check:** Mark REVISED for any revised claim.

---

### SECTION 10 — TERMINAL RECONCILER

Audit the complete document state. Produce a named finding record.

**Check (a) — Verdict audit:** Scan claims (a)–(c). Confirm each revised claim has an inline
"REVISED — see Section N" marker. List any revised claim lacking a marker as a violation.

**Check (b) — Gate audit:** Enumerate each section transition. For each gate, confirm the
named deliverables from the prior section are present. For Gate 5→6 specifically: confirm
FIELD-A, FIELD-B, FIELD-C, and FIELD-D are present for every throttle tier.

**Check (c) — Derivation chain audit:** Scan all Schema A tables. Flag each DERIVATION CHAIN
cell containing only a conclusion (CONTENT VIOLATION, Schema A).

**Check (d) — Schema B audit [distinct from gate audit]:** Scan all Schema B tier blocks
in Section 5. For each tier: count the four field labels (FIELD-A, FIELD-B, FIELD-C, FIELD-D).
A missing field label is a STRUCTURAL VIOLATION (Schema B) regardless of whether Gate 5→6
flagged it. A field label present but containing only a tier name or placeholder is a CONTENT
VIOLATION (Schema B). The Schema B audit is performed as a document-level scan, separate from
the gate deliverable check in (b).

**Output:** `Reconciler Findings: N violation(s)` followed by itemized list, or
`Reconciler Findings: 0 violations`.

**Gate 10 (document close):** Reconciler produces a finding record referencing checks (a), (b),
(c), and (d). Document is complete.

---

## V-03

**Axis:** Lifecycle emphasis — the UX gate is renamed and restructured as a six-item gate with
(a)–(f) each explicitly named as a separately blocking condition: four FIELD conditions, (e)
tier-count verification against the burst path audit section (not the two-tier minimum), and
(f) structure-compliance confirmation as a separately named blocking condition.

**Hypothesis:** R9's Gate 6→7 already contains seven checklist items, but three are bundled
implicitly: "at least two tiers" (a tier-count floor, not a burst-path cross-check), "template
structure used" (present but not named as a separate blocking condition), and "Verdict updated"
(a currency check, not a structure condition). C-29 requires the gate to close two specific
bypass paths: undercounting tiers (fixed by (e) cross-checking against the burst path audit
section, not a static minimum) and prose-formatting compliant-field tiers (fixed by (f) as a
separately named blocking condition, not merged with the field conditions). This variation makes
those two conditions explicit at the gate level without touching the Format Contract structure.

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
- Numeric threshold and scope
- Enforcement point

At least one limit must carry a concrete numeric threshold. Estimates labeled.

**Verdict currency check:** Revise claim (a) or (c) if findings differ; insert marker.

**Gate 2→3:** At least one rate limit with numeric threshold; Verdict current.

---

### ROLE 3 — BINDING CONSTRAINT DETERMINATION

Identify the binding constraint with explicit reasoning.

**Verdict currency check:** Confirm claim (a) or mark REVISED.

**Gate 3→4:** Binding constraint with reasoning; Verdict claim (a) confirmed or REVISED.

---

### ROLE 4 — BURST PATH AUDIT

Identify at least one structurally unprotected burst path. For each path:
- Trigger or action generating concurrent requests
- Missing controls
- **Classification:** STRUCTURAL vs. INCIDENTAL — stated and justified

**Record the exact count of distinct throttle tiers implied by burst paths identified here.**
This count is used in Gate 6→7 item (e).

**Verdict currency check:** Confirm claim (b) or mark REVISED.

**Gate 4→5:** At least one burst path with STRUCTURAL/INCIDENTAL classification; tier count
implied by burst path audit recorded; Verdict claim (b) confirmed or REVISED.

---

### ROLE 5 — RETRY-AFTER GAP CHECK

Evaluate Retry-After handling at every throttled endpoint from Roles 3–4. Flag each missing
case with failure mode.

**Verdict currency check:** Confirm claims (b) and (c) or mark REVISED.

**Gate 5→6:** Every throttled path evaluated; missing handling flagged with failure mode;
Verdict current.

---

### ROLE 6 — UX PER THROTTLE TIER [REQUIRED ROLE — DO NOT SKIP OR MERGE]

Apply the four-field UX template to EVERY throttle tier reached in this scenario. For each tier,
all four fields are mandatory.

**Template format for each tier:**

---
**[Tier Name / throttle level]**

- **FIELD-A — Error code or platform signal:** [specific HTTP status, connector event, or Power
  Automate run history marker]
- **FIELD-B — User-visible behavior:** [what the user observes at this tier — tier-specific]
- **FIELD-C — Visibility level:** EXPLICIT or SILENT
- **FIELD-D — Recovery path:** [exact path: manual retry / automatic backoff with Retry-After /
  permanent failure after N retries / no recovery]

---

**GATE 6→7 — SIX-ITEM UX GATE [ALL SIX CONDITIONS ARE SEPARATELY BLOCKING]:**

Do not begin Role 7 until ALL of the following conditions are individually satisfied. Each
condition is a separate blocking gate item. Combining or collapsing any two conditions into a
compound check does not satisfy both individually.

- [ ] **(a) FIELD-A completeness:** FIELD-A (error code or platform signal) is present and
      substantively populated for EVERY tier described in this document. A tier with FIELD-A
      absent or containing only a tier label fails this condition regardless of other fields.

- [ ] **(b) FIELD-B completeness:** FIELD-B (user-visible behavior) is present and
      substantively populated for EVERY tier. Tier-specific content required — generic
      descriptions do not satisfy this condition.

- [ ] **(c) FIELD-C completeness:** FIELD-C (visibility level) is present and explicitly
      labeled EXPLICIT or SILENT for EVERY tier. The label itself must appear; a description
      that implies the label does not satisfy this condition.

- [ ] **(d) FIELD-D completeness:** FIELD-D (recovery path) is present and substantively
      populated for EVERY tier. A label-only entry ("recovery path available") does not
      satisfy this condition.

- [ ] **(e) Tier-count verification:** The count of tiers described in this section matches
      the count of distinct throttle tiers identified in the Role 4 burst path audit. The
      two-tier minimum is a floor, not the verification target; verification is against the
      burst path audit count. If the burst path audit identified N tiers and this section
      describes fewer than N, this condition fails.

- [ ] **(f) Structure-compliance:** Every tier in this section uses the template structure
      (four named FIELD labels). A tier that discusses all four topics in free prose without
      the FIELD-A through FIELD-D label structure fails this condition. This is a separately
      named blocking condition; it does not merge with conditions (a)–(d).

---

### ROLE 7 — CAUSAL CHAIN TO FAILURE MODE

Trace the complete causal chain from trigger event through rate-limited endpoint to failure
mode. Every link explicit. Implied causation does not pass.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 7→8:** Complete causal chain with every link explicit; Verdict current.

---

### ROLE 8 — CASCADING THROTTLE FAILURE

Construct a specific scenario where throttling at one tier causally triggers a second distinct
throttle event at a different tier. State the mechanism and compounding effect.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 8→9:** Cascade with causal linkage named and compounding effect described; Verdict
current.

---

### ROLE 9 — VOLUME-TO-BEHAVIOR MAPPING

Produce a Schema A comparative table (BASELINE | PROTECTED | DERIVATION CHAIN | DELTA).

For the load spike tier:
- Step 1: requests per interval × load multiplier = peak load [cite Role 2 numerics]
- Step 2: peak load − rate limit = overflow volume
- Step 3: overflow × retry factor = failed request volume
- Step 4: failed / peak = failure percentage

Conclusion-only cell → CONTENT REJECTION CLAUSE.

**Verdict currency check:** Confirm claim (c) or mark REVISED.

**Gate 9→10:** Schema A table with all four columns; load spike derivation chain Steps 1–4;
Verdict claim (c) confirmed or REVISED.

---

### ROLE 10 — MITIGATIONS

Per-bottleneck mitigations with specific named actions and before/after states.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 10→11:** Specific mitigations; Verdict current.

---

### ROLE 11 — TERMINAL RECONCILER

Audit the complete document state. Produce a named finding record.

**Check (a) — Verdict audit:** Scan claims (a)–(c). Confirm each revised claim has an inline
"REVISED — see Role N" marker. List any revised claim lacking a marker as a violation.

**Check (b) — Gate audit:** Enumerate each role transition (Gates 0→1 through 10→11). For each
gate, confirm the named deliverables from the prior role are present.
- For Gate 6→7 specifically: confirm all six conditions (a)–(f) were satisfied. Confirm
  FIELD-A, FIELD-B, FIELD-C, FIELD-D present for every tier; tier count matches burst path
  audit count; template structure (not prose) used for every tier.

**Check (c) — Derivation chain audit:** Scan all Schema A tables. Flag each DERIVATION CHAIN
cell containing only a conclusion.

**Output:** `Reconciler Findings: N violation(s)` with itemized list, or
`Reconciler Findings: 0 violations`.

**Gate 11 (document close):** Reconciler finding record referencing checks (a), (b), (c).

---

## V-04

**Axis:** Combined — role sequence + output format. Verdict Block gains Claim (d) (C-28) AND
Format Contract gains Schema B as a named structural schema with its own STRUCTURAL REJECTION
CLAUSE (C-27) AND Terminal Reconciler gains check (d) as a Schema B audit distinct from the
gate audit (C-27 terminal requirement).

**Hypothesis:** C-27 and C-28 are complementary enforcement layers: C-28 makes UX commitment
visible at Verdict level (reader-facing, revision-tracked), while C-27 makes UX structure
enforceable at Format Contract level (scanner-facing, scan-time-detectable). Neither alone
closes both gaps. V-01 adds C-28 without C-27; V-02 adds C-27 without C-28. V-04 combines
both: a Verdict reader knows the tier count committed to (C-28), and any structural scan of
the document detects missing UX fields without reading prose (C-27). The Terminal Reconciler
check (d) runs the Schema B scan after all analysis is complete, distinct from the gate audit
that checked deliverables at section transitions.

---

You are a Connectors / Power Automate throughput domain expert. Simulate throughput across
rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is fully
satisfied.

---

### ROLE 0 — VERDICT BLOCK

State before any rate limit inventory, burst path audit, or UX analysis:

(a) **Binding constraint:** component name + numeric threshold
(b) **Primary gap:** specific action or path where burst or Retry-After failure occurs
(c) **System status at stated load:** SAFE / DEGRADED / FAILING
(d) **UX coverage commitment:** the total number of throttle tiers that will be described using
    the four-field Schema B template in this document. Format: "N tiers; all use Schema B
    (FIELD-A through FIELD-D)." A tier added mid-analysis that is not reflected in this claim
    requires a "REVISED — see Role N" marker on Claim (d) at the gate of the role where
    the new tier was identified.

Self-containment: a reader who reads only this block knows the core finding and the committed
UX tier count. Evidence sections confirm or mark REVISED for any changed claim.

**Revision rule for Claim (d):** insert the REVISED marker at the gate of the role where
the tier count diverges — not at terminal reconciliation.

**Gate 0→1:** All four Verdict claims written including Claim (d) with tier count.

---

### ROLE 1 — FORMAT CONTRACT

Declare the structural contract governing this entire document.

#### Schema A — Comparative Analysis Tables

Every table with quantified estimates:

| BASELINE | PROTECTED | DERIVATION CHAIN | DELTA |

**STRUCTURAL REJECTION CLAUSE — Schema A (scan-time):**
Required column absent. Detection: count column headers without reading cells.
Marker: `[STRUCTURAL VIOLATION (Schema A) — missing column: {name}]`.

**CONTENT REJECTION CLAUSE — Schema A (read-time):**
Column present, cell contains conclusion only. Detection: read cell content.
Marker: `[CONTENT VIOLATION (Schema A) — conclusion only: {column name}]`.

#### Schema B — UX Per-Tier Template

Schema B is a named structural schema. Every throttle tier in Role 6 uses ALL FOUR named fields
in structured template form:

| FIELD-A: Error code or platform signal | FIELD-B: User-visible behavior | FIELD-C: Visibility level | FIELD-D: Recovery path |

- **FIELD-A:** specific HTTP status, connector event, or run history marker
- **FIELD-B:** what the user observes at this tier — tier-specific content
- **FIELD-C:** EXPLICIT or SILENT — the label itself must appear
- **FIELD-D:** exact recovery path (manual retry / automatic backoff / permanent failure
  after N retries / no recovery)

Free prose in Role 6 that addresses all four topics without the Schema B field structure does
not satisfy Schema B, even if all topics are present in the prose.

**STRUCTURAL REJECTION CLAUSE — Schema B (scan-time):**
Required field label (FIELD-A, FIELD-B, FIELD-C, or FIELD-D) absent from a tier entry in
Role 6. Detection: count field labels without reading field content.
Marker: `[STRUCTURAL VIOLATION (Schema B) — missing field: FIELD-X]`.
Remediation: add the field label and populate it.

**CONTENT REJECTION CLAUSE — Schema B (read-time):**
Field label present, content is tier name or placeholder without field-specific information.
Detection: read field content.
Marker: `[CONTENT VIOLATION (Schema B) — label only: FIELD-X]`.

All four rejection clauses apply throughout. Violations flagged inline and enumerated in
the Terminal Reconciler Role 11 checks (c) and (d).

**Gate 1→2:** Format Contract with Schema A and Schema B — both named, both with STRUCTURAL
REJECTION CLAUSE named and detection method stated — complete before Role 2 begins.

---

### ROLE 2 — RATE LIMIT REGISTRY

Enumerate rate limits with numeric thresholds, scope, and enforcement points. At least one
concrete numeric threshold required.

**Verdict currency check:** Revise claims (a) or (c) if findings differ; insert marker.

**Gate 2→3:** At least one numeric threshold; Verdict current.

---

### ROLE 3 — BINDING CONSTRAINT DETERMINATION

Identify the binding constraint with explicit reasoning.

**Verdict currency check:** Confirm claim (a) or mark REVISED.

**Gate 3→4:** Binding constraint with reasoning; Verdict claim (a) current.

---

### ROLE 4 — BURST PATH AUDIT

Identify at least one unprotected burst path. For each:
- Trigger or action
- Missing controls
- **Classification:** STRUCTURAL vs. INCIDENTAL — stated and justified

**Verdict currency check:** Confirm claim (b) or mark REVISED.

**Gate 4→5:** At least one burst path classified; Verdict claim (b) current.

---

### ROLE 5 — RETRY-AFTER GAP CHECK

Evaluate Retry-After handling at every throttled endpoint. Flag missing handling with
failure mode.

**Verdict currency check:** Confirm claims (b) and (c) or mark REVISED.

**Gate 5→6:** Every throttled path evaluated; missing handling flagged; Verdict current.

---

### ROLE 6 — UX PER THROTTLE TIER [REQUIRED — Schema B governs all tier entries]

Apply Schema B to EVERY throttle tier in this scenario.

For each tier:

---
**[Tier Name / throttle level]**

- **FIELD-A — Error code or platform signal:** [per Schema B]
- **FIELD-B — User-visible behavior:** [per Schema B — tier-specific]
- **FIELD-C — Visibility level:** EXPLICIT or SILENT
- **FIELD-D — Recovery path:** [per Schema B]

---

After each tier: check Schema B structural compliance (count field labels; flag absent as
STRUCTURAL VIOLATION (Schema B)) and Schema B content compliance (flag label-only as
CONTENT VIOLATION (Schema B)).

**Verdict currency check for Claim (d):** if tier count differs from Claim (d), insert
"REVISED — see Role 6" on Claim (d) immediately at Gate 6→7.

**GATE 6→7 [FIELD-LEVEL GATE]:**

Do not begin Role 7 until ALL confirmed:

- [ ] **(a)** FIELD-A present and substantively populated for EVERY tier
- [ ] **(b)** FIELD-B present and substantively populated for EVERY tier
- [ ] **(c)** FIELD-C present and explicitly labeled EXPLICIT or SILENT for EVERY tier
- [ ] **(d)** FIELD-D present and substantively populated for EVERY tier
- [ ] **(e)** Tier count in this section matches Verdict Claim (d); if count changed, Claim (d)
      already marked REVISED
- [ ] Schema B template structure (not free prose) used for every tier
- [ ] Verdict updated for any revised claims

---

### ROLE 7 — CAUSAL CHAIN TO FAILURE MODE

Trace complete causal chain; every link explicit.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 7→8:** Complete chain; Verdict current.

---

### ROLE 8 — CASCADING THROTTLE FAILURE

Specific cascade: throttling at one tier causally triggers a second distinct throttle event.
Mechanism and compounding effect stated.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 8→9:** Cascade with causal linkage; Verdict current.

---

### ROLE 9 — VOLUME-TO-BEHAVIOR MAPPING

Schema A table (BASELINE | PROTECTED | DERIVATION CHAIN | DELTA).

Load spike DERIVATION CHAIN:
- Step 1: requests × multiplier = peak load [cite Role 2 numerics]
- Step 2: peak − limit = overflow
- Step 3: overflow × retry = failed
- Step 4: failed / peak = failure rate

**Verdict currency check:** Confirm claim (c) or mark REVISED.

**Gate 9→10:** Schema A table; Steps 1–4 present; Verdict claim (c) current.

---

### ROLE 10 — MITIGATIONS

Specific named mitigations per bottleneck with before/after states referencing Schema A columns.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 10→11:** Specific mitigations; Verdict current.

---

### ROLE 11 — TERMINAL RECONCILER

Audit complete document state. Produce a named finding record.

**Check (a) — Verdict audit:** Scan claims (a)–(d). Confirm each revised claim has an inline
"REVISED — see Role N" marker. Confirm Claim (d) (tier count and Schema B template commitment)
matches actual Role 6 content — count tiers in Role 6 and compare to Claim (d). List any
mismatch or missing marker as a violation.

**Check (b) — Gate audit:** Enumerate each role transition (Gates 0→1 through 10→11). Confirm
named deliverables present. For Gate 6→7: confirm FIELD-A, FIELD-B, FIELD-C, FIELD-D present
for every tier; tier count consistent with Claim (d); template structure confirmed.

**Check (c) — Schema A derivation chain audit:** Scan all Schema A tables. Flag DERIVATION
CHAIN cells containing only conclusions as CONTENT VIOLATION (Schema A).

**Check (d) — Schema B structural audit [distinct from gate audit in (b)]:** Scan all Schema
B tier entries in Role 6 as a document-level structural pass. For each tier:
- Count field labels: if fewer than four, flag each missing label as STRUCTURAL VIOLATION
  (Schema B). This check is independent of whether Gate 6→7 flagged the tier.
- Read field content: if any field contains only a tier name or placeholder, flag as CONTENT
  VIOLATION (Schema B).
The Schema B audit is a terminal document-level scan, not a repeat of the gate check.

**Output:** `Reconciler Findings: N violation(s)` with itemized list, or
`Reconciler Findings: 0 violations`.

**Gate 11 (document close):** Finding record referencing checks (a), (b), (c), and (d).

---

## V-05

**Axis:** Combined — all three axes. Verdict Block gains Claim (d) (C-28) + Format Contract
gains Schema B with STRUCTURAL REJECTION CLAUSE (C-27) + UX gate becomes six explicitly named
items (a)–(f) with (e) tier-count-against-burst-path-audit and (f) structure-compliance as
separately named blocking conditions (C-29) + Terminal Reconciler checks (b) audits six gate
conditions and check (d) runs the independent Schema B scan.

**Hypothesis:** C-27, C-28, and C-29 address three distinct bypass paths that each survive
when the other two are present but the third is absent. C-28 alone: a Verdict reader knows tier
count but cannot detect missing fields without reading prose. C-27 alone: a scanner detects
missing fields but a Verdict reader has no tier-count visibility. C-29 alone: the gate enumerates
conditions but the Format Contract carries no structural authority and the Verdict carries no
UX commitment. All three together create a closed loop: Verdict commits (C-28), Format Contract
enforces structure (C-27), gate verifies tier count against burst path audit and structure
compliance as separate named conditions (C-29), and Terminal Reconciler independently audits
Schema B as a document-level scan (C-27 terminal requirement) and confirms Claim (d) currency
(C-28 terminal requirement).

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
(b) **Primary gap:** specific action or path where burst or Retry-After failure occurs
(c) **System status at stated load:** SAFE / DEGRADED / FAILING
(d) **UX coverage commitment:** total number of throttle tiers that will be described using
    Schema B (FIELD-A through FIELD-D) in Role 6. Format: "N tiers; all use Schema B
    four-field template." A tier discovered during analysis that was not anticipated here
    requires a "REVISED — see Role N" marker on Claim (d) at the gate boundary of the role
    where the discovery occurred — not deferred to terminal reconciliation.

Self-containment: a reader who reads only this block knows the core finding and the committed
UX tier count and coverage type. Evidence sections confirm each claim or insert REVISED markers.

**Gate 0→1:** All four claims including Claim (d) with tier count and Schema B commitment.

---

### ROLE 1 — FORMAT CONTRACT

Declare the structural contract governing this entire document.

#### Schema A — Comparative Analysis Tables

Every comparative table with quantified estimates:

| BASELINE | PROTECTED | DERIVATION CHAIN | DELTA |

- BASELINE: current / unprotected behavior
- PROTECTED: behavior with mitigations applied
- DERIVATION CHAIN: full arithmetic chain — not a conclusion alone
- DELTA: net change

**STRUCTURAL REJECTION CLAUSE — Schema A (scan-time):**
Required column absent. Detection: scan-time — count column headers without reading cells.
Marker: `[STRUCTURAL VIOLATION (Schema A) — missing column: {name}]`.

**CONTENT REJECTION CLAUSE — Schema A (read-time):**
Column present, conclusion-only cell. Detection: read-time — read cell content.
Marker: `[CONTENT VIOLATION (Schema A) — conclusion only: {name}]`.

#### Schema B — UX Per-Tier Template

Schema B is a named structural schema, parallel in authority to Schema A. Every throttle tier
in Role 6 must use ALL FOUR named fields in the structured template below. Schema B is a
Format Contract commitment — it is not a role-level formatting suggestion.

For each tier in Role 6, produce one Schema B block:

```
[Tier Name / throttle level]
- FIELD-A — Error code or platform signal: [specific HTTP status, connector event, or run history marker]
- FIELD-B — User-visible behavior: [tier-specific — what the user sees or experiences]
- FIELD-C — Visibility level: EXPLICIT or SILENT [label must appear]
- FIELD-D — Recovery path: [exact: manual retry / automatic backoff with Retry-After / permanent failure after N / no recovery]
```

Free prose in Role 6 that addresses all four topics without the FIELD-A through FIELD-D label
structure does not satisfy Schema B, even when all topics appear in the prose.

**STRUCTURAL REJECTION CLAUSE — Schema B (scan-time):**
Required field label (FIELD-A, FIELD-B, FIELD-C, or FIELD-D) absent from a tier entry in
Role 6. Detection: scan-time — count field labels without reading field content.
Marker: `[STRUCTURAL VIOLATION (Schema B) — missing field: FIELD-X]`.
Remediation: add the field label and populate it before proceeding.

**CONTENT REJECTION CLAUSE — Schema B (read-time):**
Field label present, content is tier name or placeholder without field-specific information.
Detection: read-time — read field content.
Marker: `[CONTENT VIOLATION (Schema B) — label only: FIELD-X]`.

All four rejection clauses (Schema A structural, Schema A content, Schema B structural,
Schema B content) apply throughout this document. Violations are flagged inline and enumerated
in Terminal Reconciler checks (c) and (d).

**Gate 1→2:** Format Contract complete with Schema A and Schema B, each with its own named
STRUCTURAL REJECTION CLAUSE, detection method stated for each clause.

---

### ROLE 2 — RATE LIMIT REGISTRY

Enumerate rate limits with numeric thresholds, scope, and enforcement points. At least one
concrete numeric threshold required. Estimates labeled.

**Verdict currency check:** Revise claims (a) or (c) if findings differ; insert marker.

**Gate 2→3:** At least one numeric threshold; Verdict current.

---

### ROLE 3 — BINDING CONSTRAINT DETERMINATION

Identify the binding constraint with explicit reasoning: why this limit — not a higher-capacity
one — is hit first or most severely under the described load.

**Verdict currency check:** Confirm claim (a) or insert "REVISED — see Role 3".

**Gate 3→4:** Binding constraint with reasoning; Verdict claim (a) current.

---

### ROLE 4 — BURST PATH AUDIT

Identify at least one structurally unprotected burst path. For each path:
- Trigger or action generating concurrent requests
- Missing controls (no concurrency cap / no retry policy / no queue buffer)
- **Classification:** STRUCTURAL (no mechanism exists on this path) vs. INCIDENTAL (mechanism
  exists but misconfigured, bypassable, or condition-specific) — stated and justified

**Record the exact count of distinct throttle tiers implied by the burst paths and throttled
components identified in this role.** This count is the verification target for Gate 6→7
item (e) — not the two-tier minimum.

**Verdict currency check:** Confirm claim (b) or insert "REVISED — see Role 4".

**Gate 4→5:** At least one burst path with STRUCTURAL/INCIDENTAL classification; tier count
from burst path audit recorded; Verdict claim (b) current.

---

### ROLE 5 — RETRY-AFTER GAP CHECK

Evaluate whether flows or connectors handle Retry-After headers (or equivalent backoff signals:
`x-ms-ratelimit-remaining`, `Retry-After-Ms`) from every throttled endpoint identified in
Roles 3–4. Flag each missing-handling case with its failure mode (immediate retry storm /
permanent failure after N retries / silent drop / etc.).

**Verdict currency check:** Confirm claims (b) and (c) or mark REVISED.

**Gate 5→6:** Every throttled path evaluated; missing handling flagged with failure mode;
Verdict current.

---

### ROLE 6 — UX PER THROTTLE TIER [REQUIRED ROLE — Schema B governs all tier entries]

Apply Schema B to EVERY throttle tier reached in this scenario. Every tier must use the Schema
B four-field template structure declared in Role 1. Free prose does not substitute for
Schema B, even if all four topics are addressed in the prose.

For each tier, produce one Schema B block as declared in Role 1's Format Contract.

After each tier: run both Schema B rejection clause checks:
- Structural check: count field labels — flag any missing as STRUCTURAL VIOLATION (Schema B)
- Content check: read field content — flag any label-only entry as CONTENT VIOLATION (Schema B)

**Verdict currency check for Claim (d):** count the tiers in this role. If the count differs
from the tier count stated in Verdict Claim (d), insert "REVISED — see Role 6" on Claim (d)
immediately at Gate 6→7. Do not defer.

**GATE 6→7 — SIX-ITEM UX GATE:**

Each of the following six conditions is a separately named blocking gate condition. Combining
any two into a compound condition does not satisfy both. Do not begin Role 7 until ALL SIX
are individually confirmed:

- [ ] **(a) FIELD-A completeness:** FIELD-A present and substantively populated for EVERY tier
      in this document — not only the minimum two tiers. A tier with FIELD-A absent or containing
      only a tier label fails condition (a) regardless of other fields.

- [ ] **(b) FIELD-B completeness:** FIELD-B present and substantively populated for EVERY tier.
      Tier-specific content required. A generic behavioral description not specific to this tier
      fails condition (b).

- [ ] **(c) FIELD-C completeness:** FIELD-C present and explicitly labeled EXPLICIT or SILENT
      for EVERY tier. The label itself must appear in the field. A description implying the
      label without stating it fails condition (c).

- [ ] **(d) FIELD-D completeness:** FIELD-D present and substantively populated for EVERY tier.
      A label-only entry or generic placeholder fails condition (d).

- [ ] **(e) Tier-count verification:** The count of tiers described in this role matches the
      count of distinct throttle tiers identified in the Role 4 burst path audit. The two-tier
      minimum is a floor, not the verification target. If the Role 4 burst path audit identified
      N tiers and this role describes fewer than N, condition (e) fails. If Claim (d) was revised
      to reflect the updated count, that revision must already be marked.

- [ ] **(f) Structure-compliance:** Every tier uses Schema B template structure — the four
      named FIELD labels in structured form. A tier that discusses all four topics in free prose
      without the FIELD-A through FIELD-D label structure fails condition (f). This is a
      separately named blocking condition; it does not merge with conditions (a)–(d).

---

### ROLE 7 — CAUSAL CHAIN TO FAILURE MODE

Trace the complete causal chain from trigger event through the rate-limited endpoint to the
resulting failure mode. Every link in the chain must be stated explicitly. Implied causation
does not pass.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 7→8:** Complete causal chain with every link explicit; Verdict current.

---

### ROLE 8 — CASCADING THROTTLE FAILURE

Construct a specific scenario where throttling at one tier causally triggers a second distinct
throttle event at a different tier. State the mechanism of causation and the compounding effect
on throughput or error rate. Two independent limits both hit under load without causal linkage
do not constitute a cascade.

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 8→9:** Cascade with causal linkage named and compounding effect described; Verdict
current.

---

### ROLE 9 — VOLUME-TO-BEHAVIOR MAPPING

Produce a Schema A comparative table (BASELINE | PROTECTED | DERIVATION CHAIN | DELTA).

For the load spike tier (5x nominal or scenario-equivalent highest load), the DERIVATION CHAIN
cell must contain ALL of:
- Step 1: requests per interval × load multiplier = peak load [cite Role 2 numerics]
- Step 2: peak load − rate limit = overflow volume
- Step 3: overflow × retry factor = failed request volume
- Step 4: failed / peak = failure percentage

A conclusion-only cell triggers CONTENT REJECTION CLAUSE (Schema A).

**Verdict currency check:** Confirm claim (c) or insert "REVISED — see Role 9".

**Gate 9→10:** Schema A table with all four columns; Steps 1–4 for load spike tier; Verdict
claim (c) current.

---

### ROLE 10 — MITIGATIONS

For each bottleneck and unprotected burst path from Roles 3–5: specific named mitigation
identifying the action, setting, or pattern. Generic advice without naming the specific action
does not pass.

For each mitigation:
- **Before-state:** baseline behavior at this bottleneck — references a specific component and
  corresponds to a BASELINE-column entry in Role 9
- **After-state:** system behavior with mitigation applied — populates PROTECTED column in
  Role 9

**Verdict currency check:** Mark REVISED for any revised claim.

**Gate 10→11:** Specific mitigations with before/after states; Verdict current.

---

### ROLE 11 — TERMINAL RECONCILER

Audit the complete document state. This is the last section. Produce a named finding record.

**Check (a) — Verdict audit:** Scan claims (a)–(d). For each claim revised during analysis,
confirm an inline "REVISED — see Role N" marker is present. Confirm Claim (d) matches the
actual tier count in Role 6 — count Role 6 tiers and compare to Claim (d). A count mismatch
without a REVISED marker is a violation. List all violations.

**Check (b) — Gate audit:** Enumerate each role transition (Gates 0→1 through 10→11). Confirm
named deliverables from each prior role are present. For Gate 6→7 specifically: audit all six
conditions (a)–(f) independently.
- Condition (a): FIELD-A present for every tier
- Condition (b): FIELD-B present for every tier
- Condition (c): FIELD-C explicitly labeled EXPLICIT or SILENT for every tier
- Condition (d): FIELD-D present for every tier
- Condition (e): tier count in Role 6 matches burst path audit count from Role 4
- Condition (f): template structure (not prose) used for every tier — checked independently
  of conditions (a)–(d)

**Check (c) — Schema A derivation chain audit:** Scan all Schema A tables. For each DERIVATION
CHAIN cell: does it contain computation steps, or only a conclusion? Flag each conclusion-only
cell as CONTENT VIOLATION (Schema A).

**Check (d) — Schema B structural audit [independent document-level scan, distinct from gate
audit in check (b)]:** Perform a fresh structural scan of all Schema B tier entries in Role 6:
- Count field labels in each tier entry; flag any tier with fewer than four labels as containing
  at least one STRUCTURAL VIOLATION (Schema B), identifying the missing label(s). This scan is
  independent of what Gate 6→7 found — Schema B violations are reported here regardless of
  whether they were caught at the gate.
- Read field content in each tier entry; flag any field whose content is a tier name, generic
  placeholder, or label-only as CONTENT VIOLATION (Schema B).
The Schema B audit is a terminal document-level enforcement of the Format Contract, not a
repetition of the gate check.

**Output:** `Reconciler Findings: N violation(s)` followed by an itemized list keyed to the
check that found each violation, or `Reconciler Findings: 0 violations` if all checks pass.

**Gate 11 (document close):** Reconciler produces a named finding record explicitly referencing
checks (a), (b), (c), and (d). Document is complete.
