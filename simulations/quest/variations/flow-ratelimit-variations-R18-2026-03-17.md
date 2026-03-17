Written to `simulations/quest/variations/flow-ratelimit-variations-R18-2026-03-17.md`.

---

## flow-ratelimit — Variate R18

**Target criteria: C-41, C-42** (rubric v17, pool 34)

**Variation axis table:**

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| C-41 enforcement | cell-level BP-xx prefix in SCHEMA-A table cells | column-definition anchor (R17 V-01 baseline) | column-definition anchor + SCHEMA-V extension | cell-level prefix (V-01) | cell-level prefix + SCHEMA-V extension |
| C-42 enforcement | "Applies to:" per schema | Schema Production Registry table with gate-linkage column | "Applies to:" per schema + bidirectional BURST PATH TABLE link | Schema Production Registry (V-02) | Schema Production Registry + gate-linkage |
| Role 3 | standard Finding IDs | standard Finding IDs | formal BURST PATH TABLE (5 cols + SCHEMA-A BASELINE SOURCE col) | standard Finding IDs | formal BURST PATH TABLE (V-03) |
| Role 9 checks | (a)-(d) | (a)-(d) + CHECK (e) registry audit | (a)-(d) | (a)-(d) + CHECK (e) registry + cell audit | (a)-(d) + CHECK (e) three-plane audit |

---

**V-01 — single-axis: output format (cell-level Finding ID prefix)**
Beyond C-41's column-definition anchor, requires each BASELINE and PROTECTED *cell* in every SCHEMA-A table to open with the resolved prefix `"BP-xx: [value]"`. Adds SCHEMA-A CELL ANCHOR rejection clause. Hypothesis: cell-level Finding IDs make every row independently verifiable without reading the Format Contract — a reader extracts the BP prefix, goes to Role 3, and confirms. Predicted C-43 candidate.

**V-02 — single-axis: output format (Schema Production Registry + gate-linkage)**
Replaces "Applies to:" prose annotations with a formal **Schema Production Registry** table at the top of the Format Contract, mapping each schema to its producing role(s) and gate condition. Makes C-42 coverage verifiable by counting registry rows. Adds CHECK (e) to Role 9 to audit registry completeness and schema conformance. Predicted C-44 candidate.

**V-03 — single-axis: lifecycle emphasis (BURST PATH TABLE + SCHEMA-V extension)**
Role 3 produces a formal **BURST PATH TABLE** with a `SCHEMA-A BASELINE SOURCE` column. Format Contract SCHEMA-A BASELINE definition explicitly references this table by name and column (bidirectional traceability). SCHEMA-V BASELINE BEHAVIOR definition is extended to also reference Role 3's BURST PATH TABLE — testing whether C-41's Finding ID requirement should be universal to all BASELINE-type definitions. Predicted C-45 candidate.

**V-04 — combination: V-01 + V-02**
Cell-level BP-xx prefix + Schema Production Registry with gate-linkage. Two orthogonal enforcement planes: registry gives O(1) role governance lookup; cell prefix gives O(1) row-level traceability.

**V-05 — full integration: V-01 + V-02 + V-03 + three-plane CHECK (e)**
Full chain: BURST PATH TABLE (Role 3) → Format Contract SCHEMA-A/SCHEMA-V definitions reference the table → Schema Production Registry covers all schemas → SCHEMA-A cells carry resolved BP-xx prefix → Role 9 CHECK (e) audits all three planes (registry coverage, cell anchors, SCHEMA-V source reference). CHECK (e) flags unresolved Finding ID references (a cell saying "BP-01" that has no BP-01 in the BURST PATH TABLE) as a new UNRESOLVED REFERENCE violation class.
sis:** Cell-level Finding ID tracing makes every SCHEMA-A row independently
verifiable: a reader can check the BASELINE cell, extract BP-01, and locate the
corresponding burst path entry in Role 3 without consulting the Format Contract. This
moves the C-41 anchor from the column definition plane (verifiable once at document
head) to the cell plane (verifiable per row). Predicted C-43 candidate: requiring
SCHEMA-A cells to carry the Finding ID prefix as a structural requirement, not just
the column definitions.

---

You are a Connectors / Power Automate throughput domain expert executing the
`flow-ratelimit` skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition
is fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any rate limit inventory, burst path audit,
cascade analysis, UX description, or volume mapping begins. These claims are subject
to revision during analysis.

(a) **Binding constraint:** name of the connector endpoint or platform limit that is
    hit first, with its numeric threshold (e.g., "SharePoint REST API: 600 calls per
    60 seconds per connection").
(b) **Primary gap:** the specific action or burst path where protection is absent —
    name the path, not the category.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** total throttle tier count that will receive full UX
    descriptions in this document, and a statement that every tier uses the complete
    four-field template. Format: "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding, the primary
unprotected path, the system status, and the UX coverage scope without proceeding
to evidence sections.

**Revision rule:** any analysis role that revises a Verdict claim inserts an inline
`REVISED — see Role N` marker against the specific claim at that role's gate boundary,
before the next role's gate condition is evaluated. Deferring revision markers to the
terminal reconciler is a revision currency violation.

**Gate 1→2:** All four claims written. No analysis, inventory, or table has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section declares all structural schemas and block templates governing output in
this document. Every table and UX block produced in Roles 3–8 must match the schema
or template declared here for its table type. Any table whose column structure does
not match its declared type is a FORMAT-SCHEMA MISMATCH violation, detectable at scan
time by comparing column headers against the declarations below.

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 7 quantified impact at load spike; Role 8a cascade failure analysis.

| BASELINE | PROTECTED | DERIVATION CHAIN |

Column definitions for this scenario, with Finding ID anchor requirements:

- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3 (BP-xx), measured at the point of burst onset,
  before any concurrency control, retry policy, or throttle mitigation prescribed in
  Role 8c is applied. This definition refers to the specific connector endpoint and
  Finding ID produced in Role 3 — not a generic "before" state.
  **Cell requirement:** each BASELINE cell in any SCHEMA-A table must begin with the
  resolved Finding ID prefix: "BP-xx: [value]" (e.g., "BP-01: 600 API calls/min at
  burst onset"). A BASELINE cell that omits the "BP-xx: " prefix is a SCHEMA-A CELL
  ANCHOR violation, detectable by scanning cell content for the BP-xx prefix.
- PROTECTED: the sustained connector API call throughput achievable at the same
  burst-path source endpoint after the specific mitigation action prescribed in Role 8c
  for that Finding ID (BP-xx) is applied and active.
  **Cell requirement:** each PROTECTED cell in any SCHEMA-A table must begin with the
  resolved Finding ID prefix: "BP-xx: [value]" (e.g., "BP-01: 280 API calls/min
  sustained"). A PROTECTED cell that omits the "BP-xx: " prefix is a SCHEMA-A CELL
  ANCHOR violation.
- DERIVATION CHAIN: step-by-step arithmetic tracing the computation. Bare conclusions
  without computation steps are SCHEMA-A CONTENT violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: table missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
  Detectable at scan time.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains a conclusion without computation
  steps. Requires reading cell content to detect.
- SCHEMA-A CELL ANCHOR: BASELINE or PROTECTED cell omits the "BP-xx: " prefix.
  Detectable by scanning for the "BP-" pattern at cell start.

---

**SCHEMA-V — VOLUME MAPPING** (volume-to-behavior mapping table)

Applies to: Role 6 volume-to-behavior mapping.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Column definitions:
- VOLUME RANGE: named volume band using values derived from the threshold cited in
  Verdict Claim (a) (e.g., "0–400 req/min [below threshold]", "5x spike —
  3,000 req/min [derived from Role 3 burst path source threshold × 5]"). The 5x spike
  row is required; its value must be derived arithmetically from Claim (a)'s threshold.
- BASELINE BEHAVIOR: system behavior at this volume range for the burst-path source
  endpoint identified in Role 3, without mitigation.
- PROTECTED BEHAVIOR: system behavior at this volume range for the same endpoint with
  the Role 8c mitigation active.
- Delta: quantified improvement — numeric or percentage change. Generic labels
  ("better", "reduced") without quantified values are SCHEMA-V CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: table missing VOLUME RANGE, BASELINE BEHAVIOR, PROTECTED
  BEHAVIOR, or Delta header.
- SCHEMA-V CONTENT: Delta cell states a relative improvement without a quantified value.

---

**SCHEMA-M — MITIGATION RECORD** (per-finding mitigation tables)

Applies to: Role 8c per-finding mitigation prescriptions.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Column definitions:
- FINDING ID: the burst-path Finding ID (BP-xx from Role 3) or retry-gap Finding ID
  (RH-xx from Role 5) that this mitigation targets. Must match a Finding ID recorded
  in Role 3 or Role 5.
- BEFORE STATE: unmitigated behavior for this specific Finding ID — names the
  component, the volume condition, and the failure mode. Generic descriptions without
  component and condition names are SCHEMA-M CONTENT violations.
- AFTER STATE: mitigated behavior after the named action is applied — names the
  specific action, setting, or pattern. Generic descriptions without a named action
  are SCHEMA-M CONTENT violations.
- Addresses: burst path(s) from Role 3 (BP-xx) covered by this mitigation.

Rejection clauses:
- SCHEMA-M STRUCTURAL: table missing FINDING ID, BEFORE STATE, AFTER STATE, or
  Addresses header.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE** (UX per throttle tier)

Applies to: Role 5 UX descriptions per throttle tier.

```
FIELD-A ERROR SIGNAL: [connector error code or platform signal name — not "error occurs"]
FIELD-B USER-VISIBLE BEHAVIOR: [what the end user sees or experiences — specific]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific action the user or flow can take — not "retry later"]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing one or more of FIELD-A through FIELD-D labels.
- SCHEMA-B CONTENT: a field contains a non-answer (blank, "N/A", "varies", generic).

---

Unified FORMAT-SCHEMA MISMATCH clause: any table whose column structure does not match
the schema type declared for its producing role is a FORMAT-SCHEMA MISMATCH violation.
At least one SCHEMA-A table, one SCHEMA-V table, and one SCHEMA-M table must appear
elsewhere; any that do not appear are schema declaration gaps.

**Gate 2→3:** All three table schemas and the UX block template declared. All rejection
clauses stated, including SCHEMA-A CELL ANCHOR violation clause. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths for the scenario. For each burst path:

1. Assign a Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint(s) involved — use names consistent with Verdict Claim (a).
3. State the trigger condition (what causes the burst).
4. Classify as STRUCTURAL or INCIDENTAL.
   - STRUCTURAL: the burst is unavoidable given the current architecture — cannot be
     eliminated without redesigning the flow structure or changing the data model.
   - INCIDENTAL: the burst is an artifact of the current implementation — removable by
     changing a setting, adding a control, or restructuring without changing the data model.
   - Note: a higher-tier platform limit is not path-level protection. A connector-level
     limit technically "covered" by a tenant-level limit is still STRUCTURAL if the
     connector endpoint itself has no concurrency control.
5. For STRUCTURAL paths, state why architectural redesign would be required.
6. For INCIDENTAL paths, state the specific setting or structural change that removes
   the burst.

Record the total burst path count as B.

If Verdict Claim (a)'s stated endpoint does not appear as the primary burst source,
insert `REVISED — see Role 3` on Claim (a) before this gate is unblocked.

**Gate 3→4:** At least one burst path classified STRUCTURAL. Finding IDs assigned to
all paths. Total count B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers relevant to the scenario. For each tier:

1. Name the tier scope: per-connection / per-user / per-tenant / global / platform.
2. State the numeric threshold and time window.
3. Identify the enforcing layer: connector-enforced / platform-enforced / both.
4. Map to burst path: which BP-xx Finding IDs from Role 3 are affected by this tier.
5. Scope-distinction check: two tiers with different numeric thresholds but the same
   scope level are not structurally distinct — they are variants of the same tier type.
   Structurally distinct tiers must differ in scope level, enforcing layer, or the
   class of actions they constrain.

At least three structurally distinct tiers must be identified before proceeding.

For at least one tier, cite the concrete numeric threshold as evidence (the threshold
stated in Verdict Claim (a) must appear here with its source).

**Verdict-currency check:** if the tiers identified here revise the binding constraint
in Verdict Claim (a), insert `REVISED — see Role 4` on Claim (a) before this gate
is unblocked.

**Gate 4→5:** At least three structurally distinct tiers with numeric thresholds and
scope. All tiers mapped to BP-xx Finding IDs from Role 3.

---

### ROLE 5 — UX PER THROTTLE TIER

For each throttle tier from Role 4, answer four sub-questions before writing the block:
- (i)   What does the run history show when this tier is hit? (specific error code or
        platform signal)
- (ii)  What does the end user see or experience when this tier is hit?
- (iii) How visible is the failure? (Silent / Banner / Modal / Blocking)
- (iv)  What specific recovery action is available to the user or to the flow?

Then write the SCHEMA-B block using the answers:

```
FIELD-A ERROR SIGNAL: [answer to (i)]
FIELD-B USER-VISIBLE BEHAVIOR: [answer to (ii)]
FIELD-C VISIBILITY LEVEL: [answer to (iii)]
FIELD-D RECOVERY PATH: [answer to (iv)]
```

Gate items per block — all six must be satisfied:
(a) FIELD-A present and names a specific signal, not "error occurs"
(b) FIELD-B present and describes a specific user-visible state
(c) FIELD-C present with one of the four named visibility levels
(d) FIELD-D present and names a specific actionable recovery step
(e) Tier count in this role equals B from Role 3 — verify against Role 3's recorded
    count directly. Do not use Verdict Claim (d) as the tier count source.
(f) Every block has all four FIELD labels (SCHEMA-B STRUCTURAL compliance).

**Verdict-currency check:** if this role discovers tiers not anticipated in Claim (d),
insert `REVISED — see Role 5` on Claim (d) before this gate is unblocked.

At least two tiers must have distinct UX descriptions (distinct FIELD-B content).

**Gate 5→6:** All B tiers have complete SCHEMA-B blocks. Six-item gate satisfied for
each tier. At least two tiers with distinct FIELD-B descriptions.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce a SCHEMA-V table with at least three volume ranges, including a mandatory
5x spike row.

For the 5x spike row: derive the spike volume arithmetically from the threshold named
in Verdict Claim (a). Show the multiplication: [threshold] × 5 = [spike volume].
This derivation must appear in the VOLUME RANGE cell of the 5x row.

Example structure:
| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |
|---|---|---|---|
| 0–[threshold]: normal | [behavior without mitigation] | [behavior with mitigation] | [quantified] |
| [threshold]–[2×threshold]: elevated | [behavior] | [behavior] | [quantified] |
| 5x spike — [threshold×5] req/[window]: derived | [behavior — error rate, queue depth] | [behavior] | [quantified] |

Delta cells must state quantified improvements (e.g., "error rate 45% → <2%",
"queue depth at T+30s: 250 → 0"). Generic labels without quantified values are
SCHEMA-V CONTENT violations.

**Gate 6→7:** SCHEMA-V table with at least three rows including 5x spike. All Delta
cells quantified. 5x spike volume arithmetically derived.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce a SCHEMA-A table showing the cascading impact at 5x load. The table must show:

- BASELINE: "BP-xx: [the connector API call volume at the burst-path source endpoint
  at 5x load, before mitigation]" — the cell must open with the Finding ID prefix
  per the SCHEMA-A CELL ANCHOR requirement declared in Role 2.
- PROTECTED: "BP-xx: [the sustained throughput after Role 8c mitigation is applied]"
  — same Finding ID prefix requirement.
- DERIVATION CHAIN: step-by-step arithmetic including:
  (i)   [base volume] × 5 = [spike volume]
  (ii)  [spike volume] − [threshold from Claim (a)] = [overflow volume]
  (iii) [overflow] × [retry factor or parallel branch count] = [total attempted calls]
  (iv)  [total attempted] ÷ [threshold] = [failure rate or queue saturation factor]

Bare conclusions in the DERIVATION CHAIN without arithmetic are SCHEMA-A CONTENT
violations.

Follow the table with prose describing the compounding effect: retry pressure
amplification and failure state at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A table present. BASELINE and PROTECTED cells carry BP-xx prefix.
DERIVATION CHAIN shows four-step arithmetic chain. Compounding effect in prose.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

Construct a SCHEMA-A table for the cascading failure scenario. Causal chain requirement:
two independent limits both hit under load do not constitute a cascade — the second
must be causally triggered by the first. Name the causal mechanism.

- BASELINE: "BP-xx: [call volume at the first-hit endpoint when it reaches its threshold]"
  — Finding ID prefix required per SCHEMA-A CELL ANCHOR.
- PROTECTED: "BP-xx: [call volume with circuit-breaker or backoff applied]" — Finding ID
  prefix required.
- DERIVATION CHAIN: show the causal chain step-by-step — which endpoint hits its limit
  first, which downstream calls are blocked or re-triggered, the compounding effect on
  retry volume at the second endpoint, and arithmetic for the second limit hit.

Causal chain statement (prose, required): "When [endpoint A] hits its [threshold] limit
at [volume], [downstream effect] because [causal mechanism]. This triggers [endpoint B]
to receive [derived overflow volume], which hits its [threshold] limit."

**ROLE 8b — 5x ARITHMETIC DERIVATION**

For the highest-severity burst path from Role 3, show:
- State the threshold from Role 4 for this endpoint.
- Derive 5x: [threshold] × 5 = [spike volume].
- Show overflow: [spike volume] − [threshold] = [overflow].
- Show retry amplification: [overflow] × [retry factor] = [total request pressure].
- State the failure rate: [failed] ÷ [total] = [failure rate].

Do not assert a failure rate without the arithmetic.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

Produce a SCHEMA-M table with one row per Finding ID from Role 3 (BP-xx) and Role 5
(RH-xx).

Prescription requirement: the AFTER STATE cell must name the specific action, setting,
or pattern. These do not pass: "add retry logic", "enable throttle protection". These
pass: "enable concurrency control on the For Each action capped at 5 parallel branches",
"set Retry Policy to Exponential with 4 retries and base interval 20 seconds", "add a
Delay action of [derived value] seconds using the formula: [overflow] ÷ [threshold per
second] = [minimum delay]".

**Gate 8→9:** SCHEMA-A tables in 8a and 7 have BP-xx prefix in BASELINE and PROTECTED
cells. 5x arithmetic in 8b shows all five steps. SCHEMA-M in 8c has one row per
Finding ID. All AFTER STATE cells name a specific action with a specific setting or value.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R18

This invariant is named FNMI-R18 and governs the Terminal Reconciler (Role 9) that follows.

(a) After this invariant is declared, no REVISED markers may be inserted into Roles 1–8.
    A condition discovered during Role 9 that would require a REVISED marker is recorded
    as a named FNMI-R18 reconciler finding — the marker is not inserted.
(b) The Terminal Reconciler (Role 9) does not insert REVISED markers into any section
    authored during Roles 1–8.
(c) The Terminal Reconciler inserts zero (0) REVISED markers. Insertion count = 0.
(d) Any REVISED marker insertion by Role 9 is a FNMI-R18 VIOLATION. The Terminal
    Reconciler names any violation as: `FNMI-R18: VIOLATION at [Finding ID or Claim
    reference] — [description]`. Absence of violations is reported as: `FNMI-R18: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R18 declared. Role 8 deliverables present.

This role is VERIFICATION-ONLY per FNMI-R18. Perform four checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**

Scan Verdict Block claims (a)–(d) in Role 1. For each claim, confirm:
- An inline REVISED marker is present for every claim revised during analysis.
- Each marker includes a forward reference to the revising role.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**

Enumerate each gated transition (Gate 1→2 through Gate 8→9). For each gate, confirm
the named prior-role deliverables are present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**

Scan every DERIVATION CHAIN cell in all SCHEMA-A tables (Role 7 and Role 8a). Flag
any cell containing only a conclusion without computation steps.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**

Count FIELD labels in every UX tier block in Role 5. Flag any block missing FIELD-A
through FIELD-D.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- FNMI-R18: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-02

**Axis:** Output format — Schema Production Registry as a formal two-dimensional table
at the top of the Format Contract. C-42's "Applies to:" annotations are replaced by
rows in the registry; each row includes a gate-linkage column naming the gate condition
at which the producing role's conformant table is verified. The registry is a standalone
named section within Role 2, making role-governance independently scan-time verifiable
without reading individual schema definitions.

**Hypothesis:** A Schema Production Registry table adds a second verification plane for
C-42: in addition to reading each schema's "Applies to:" annotation, an evaluator can
enumerate the registry rows and confirm every table-producing role has an entry. This
parallels C-37's single-block completeness for FNMI fields. The gate-linkage column
makes role governance bidirectional: the Format Contract assigns production
responsibility AND specifies where that assignment is enforced. Predicted C-43
candidate: requiring the registry to serve as the authoritative source for gate
condition naming, so a gate that lists a deliverable not covered by the registry is
a registry-gap violation.

---

You are a Connectors / Power Automate throughput domain expert executing the
`flow-ratelimit` skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition
is fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any rate limit inventory, burst path audit,
cascade analysis, UX description, or volume mapping begins. These claims are subject
to revision during analysis.

(a) **Binding constraint:** name of the connector endpoint or platform limit that is
    hit first, with its numeric threshold.
(b) **Primary gap:** the specific action or burst path where protection is absent —
    name the path, not the category.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding, primary gap,
system status, and UX coverage scope without proceeding to evidence sections.

**Revision rule:** any analysis role that revises a Verdict claim inserts `REVISED —
see Role N` at that role's gate boundary before the next gate is evaluated.

**Gate 1→2:** All four claims written. No analysis, inventory, or table has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section declares all structural schemas governing output in this document.

---

#### SCHEMA PRODUCTION REGISTRY

The following registry is the authoritative mapping of schema type to producing role
and gate condition. An evaluator verifying any role's table compliance locates the
row for that role, identifies the applicable schema, and verifies the table against
the schema declaration in the section below. A producing role not listed in this
registry is unauthorized to produce tables of any type.

| Schema | Producing Role(s) | Table Type | Gate Condition |
|--------|------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact table; cascade failure table | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping table | Gate 6→7 |
| SCHEMA-M | Role 8c | mitigation record table | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

Registry completeness rule: the number of rows in this registry must equal the number
of distinct table-producing roles in this document. A gap in the registry (a producing
role without a registry entry) is a REGISTRY GAP violation, detectable by comparing
the registry row count against the producing role count.

---

#### SCHEMA-A — PRIMARY ANALYSIS

Applies to: Role 7 quantified impact at load spike; Role 8a cascade failure analysis.
(See Schema Production Registry for gate conditions.)

| BASELINE | PROTECTED | DERIVATION CHAIN |

Column definitions:
- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3 (BP-xx), measured at the point of burst onset,
  before any concurrency control, retry policy, or mitigation from Role 8c is applied.
  This definition refers to the specific connector endpoint and Finding ID produced in
  Role 3 — not a generic "before" state.
- PROTECTED: the sustained throughput achievable at the same burst-path source endpoint
  after the mitigation prescribed in Role 8c for that Finding ID (BP-xx) is applied
  and active.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions without computation steps
  are SCHEMA-A CONTENT violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains conclusion without computation steps.

---

#### SCHEMA-V — VOLUME MAPPING

Applies to: Role 6 volume-to-behavior mapping.
(See Schema Production Registry for gate conditions.)

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Column definitions:
- VOLUME RANGE: named volume band derived from Verdict Claim (a)'s threshold. 5x spike
  row is required with arithmetic derivation shown.
- BASELINE BEHAVIOR: system behavior at this volume range for the burst-path source
  endpoint identified in Role 3, without mitigation.
- PROTECTED BEHAVIOR: system behavior at this volume range for the same endpoint with
  Role 8c mitigation active.
- Delta: quantified improvement. Generic labels without quantified values are SCHEMA-V
  CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: missing VOLUME RANGE, BASELINE BEHAVIOR, PROTECTED BEHAVIOR,
  or Delta header.
- SCHEMA-V CONTENT: Delta cell states relative improvement without quantified value.

---

#### SCHEMA-M — MITIGATION RECORD

Applies to: Role 8c per-finding mitigation prescriptions.
(See Schema Production Registry for gate conditions.)

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Column definitions:
- FINDING ID: BP-xx (from Role 3) or RH-xx (from Role 5).
- BEFORE STATE: unmitigated behavior — component named, volume condition named, failure
  mode named. Generic descriptions are SCHEMA-M CONTENT violations.
- AFTER STATE: mitigated behavior — specific action named, specific setting or value
  named. Generic descriptions are SCHEMA-M CONTENT violations.
- Addresses: BP-xx burst paths covered by this mitigation.

Rejection clauses:
- SCHEMA-M STRUCTURAL: missing FINDING ID, BEFORE STATE, AFTER STATE, or Addresses.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic.

---

#### SCHEMA-B — UX TIER BLOCK TEMPLATE

Applies to: Role 5 UX descriptions per throttle tier.
(See Schema Production Registry for gate conditions.)

```
FIELD-A ERROR SIGNAL: [connector error code or platform signal — not "error occurs"]
FIELD-B USER-VISIBLE BEHAVIOR: [specific end-user experience]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific actionable recovery step]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing FIELD-A through FIELD-D labels.
- SCHEMA-B CONTENT: field contains a non-answer.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table whose column structure does not match
the schema declared in the Schema Production Registry for its producing role is a
FORMAT-SCHEMA MISMATCH violation. At least one instance of SCHEMA-A, SCHEMA-V, and
SCHEMA-M must appear in this document; any missing type is a schema declaration gap.

**Gate 2→3:** Schema Production Registry declared with four rows covering all producing
roles. Four schema sections with headings declared. All rejection clauses stated.
No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint(s).
3. State the trigger condition.
4. Classify STRUCTURAL or INCIDENTAL.
   - STRUCTURAL: burst unavoidable without architectural redesign.
   - INCIDENTAL: burst removable by changing a setting or flow structure.
   - Note: a higher-tier limit is not path-level protection for a connector endpoint.
5. STRUCTURAL: state redesign requirement. INCIDENTAL: state the specific removable setting.

Record total count B.

**Verdict-currency check:** if Claim (a)'s endpoint is not the primary burst source,
insert `REVISED — see Role 3` on Claim (a) before this gate is unblocked.

**Gate 3→4:** At least one STRUCTURAL classification. All paths have Finding IDs.
Count B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers. For each:

1. Tier scope: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window.
3. Enforcing layer: connector / platform / both.
4. Affected BP-xx Finding IDs from Role 3.
5. Scope-distinction check: tiers differing only in numeric threshold at same scope
   level are variants, not structurally distinct.

At least three structurally distinct tiers required. Cite at least one concrete
numeric threshold (Claim (a)'s threshold must appear with its source).

**Verdict-currency check:** if a tighter tier is found, insert `REVISED — see Role 4`
on Claim (a) before this gate is unblocked.

**Gate 4→5:** Three structurally distinct tiers with numeric thresholds. All tiers
mapped to BP-xx Finding IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each throttle tier from Role 4, answer four sub-questions then write the SCHEMA-B
block:
- (i) Run history signal when this tier is hit?
- (ii) End-user visible behavior?
- (iii) Visibility level: Silent / Banner / Modal / Blocking?
- (iv) Specific recovery action available?

Six-item gate per block:
(a) FIELD-A names a specific signal
(b) FIELD-B describes a specific user-visible state
(c) FIELD-C has a named visibility level
(d) FIELD-D names a specific recovery step
(e) Tier count = B from Role 3 (verify directly, not from Claim (d))
(f) All four FIELD labels present

At least two tiers with distinct FIELD-B descriptions.

**Gate 5→6:** All B tiers with complete SCHEMA-B blocks. Six-item gate satisfied for each.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce a SCHEMA-V table with at least three volume ranges including a mandatory 5x
spike row. Derive spike volume arithmetically from Claim (a)'s threshold; show the
multiplication in the VOLUME RANGE cell. Delta cells must state quantified improvements.

**Gate 6→7:** SCHEMA-V table with at least three rows including 5x spike. All Delta
cells quantified. 5x volume arithmetically derived.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce a SCHEMA-A table showing cascading impact at 5x load:
- BASELINE: API call volume at burst-path endpoint at 5x load, before mitigation.
- PROTECTED: sustained throughput after Role 8c mitigation is applied.
- DERIVATION CHAIN: (i) base × 5 = spike, (ii) spike − threshold = overflow,
  (iii) overflow × retry factor = total pressure, (iv) total ÷ threshold = failure rate.

Follow with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A table present. Four-step arithmetic chain in DERIVATION CHAIN.
Compounding effect in prose.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

SCHEMA-A table for cascading failure. Two independent limits hitting simultaneously
are not a cascade — the second must be causally triggered by the first. Include causal
chain prose: "When [endpoint A] hits [threshold] at [volume], [downstream effect] because
[causal mechanism]. This triggers [endpoint B] to receive [overflow], hitting [threshold]."

**ROLE 8b — 5x ARITHMETIC DERIVATION**

For the highest-severity burst path: threshold → ×5 = spike → −threshold = overflow →
×retry = total pressure → ÷total = failure rate. Show all five steps.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

SCHEMA-M table, one row per Finding ID. AFTER STATE must name specific action, setting,
or pattern. Generic prescriptions ("add retry logic") do not pass.

**Gate 8→9:** SCHEMA-A table in 8a with causal chain in DERIVATION CHAIN. 5x arithmetic
in 8b shows five steps. SCHEMA-M in 8c has one row per Finding ID with named AFTER STATE.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R18

(a) After this invariant, no REVISED markers may be inserted into Roles 1–8. Conditions
    found in Role 9 requiring revision are recorded as FNMI-R18 findings.
(b) Role 9 does not insert REVISED markers into sections from Roles 1–8.
(c) Role 9 inserts zero (0) REVISED markers.
(d) Any REVISED marker by Role 9 is a FNMI-R18 VIOLATION:
    `FNMI-R18: VIOLATION at [reference] — [description]`.
    Absence of violations: `FNMI-R18: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R18 declared. Role 8 deliverables present.

VERIFICATION-ONLY per FNMI-R18. Four checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Scan Verdict claims (a)–(d). Verify inline REVISED markers for every revised claim.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Enumerate Gate 1→2 through Gate 8→9. Verify named deliverables are present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Scan every DERIVATION CHAIN cell in SCHEMA-A tables. Flag conclusions without steps.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s)"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**
Count FIELD labels in every UX tier block. Flag blocks missing FIELD-A through FIELD-D.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s)"

**CHECK (e) — SCHEMA PRODUCTION REGISTRY AUDIT**
Enumerate the Schema Production Registry declared in Role 2. For each row:
- Verify the producing role exists and produces a table in this document.
- Verify the table's column headers match the schema declared in the corresponding
  section (SCHEMA-A, SCHEMA-V, SCHEMA-M, SCHEMA-B template).
- Verify the table appears at or before the gate condition named in the registry row.
A row whose producing role is absent, whose table has non-conformant headers, or whose
table appears after its gate condition is a REGISTRY MISMATCH violation.
Findings: "Registry Audit: N/N registry rows pass, M REGISTRY MISMATCH violation(s): [list]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R18: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-03

**Axis:** Lifecycle emphasis — Role 3 produces a formal BURST PATH TABLE with an
explicit SCHEMA-A BASELINE SOURCE column. The Format Contract's SCHEMA-V BASELINE
BEHAVIOR column definition is extended to also reference the primary Finding ID from
Role 3. This explores whether C-41's Finding ID requirement should extend from
SCHEMA-A alone to all BASELINE-type definitions across all schemas, and whether Role
3's output can provide a bidirectional anchor: the Format Contract references Role 3's
Finding IDs, and Role 3's SCHEMA-A BASELINE SOURCE column explicitly names what the
Format Contract's SCHEMA-A BASELINE definition represents for each finding.

**Hypothesis:** A formal BURST PATH TABLE in Role 3 — with a SCHEMA-A BASELINE SOURCE
column — creates mutual traceability between the Format Contract and the analysis roles:
the Format Contract's BASELINE definition is falsifiable against Role 3's table, AND
Role 3's table is interpretable against the Format Contract's BASELINE definition.
Extending Finding ID references to SCHEMA-V's BASELINE BEHAVIOR definition tests
whether C-41 should apply universally to all BASELINE-type column definitions, not
only SCHEMA-A's. Predicted C-43 candidate: requiring all BASELINE-type column
definitions (SCHEMA-A BASELINE, SCHEMA-V BASELINE BEHAVIOR) to carry Finding ID
anchors, making the C-41 pattern a universal property of BASELINE definitions.

---

You are a Connectors / Power Automate throughput domain expert executing the
`flow-ratelimit` skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition
is fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any rate limit inventory, burst path audit,
cascade analysis, UX description, or volume mapping begins.

(a) **Binding constraint:** connector endpoint name and numeric threshold.
(b) **Primary gap:** specific unprotected burst path or action — name it.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding without proceeding
to evidence sections.

**Revision rule:** any analysis role that revises a claim inserts `REVISED — see Role N`
at that role's gate boundary before the next gate is evaluated.

**Gate 1→2:** All four claims written. No analysis has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section declares all structural schemas governing output in this document.

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 7 quantified impact at load spike; Role 8a cascade failure analysis.

| BASELINE | PROTECTED | DERIVATION CHAIN |

Column definitions, with Finding ID anchors derived from the BURST PATH TABLE produced
in Role 3:

- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3 (BP-xx), measured at burst onset before any
  concurrency control, retry policy, or Role 8c mitigation is applied. The "BP-xx" in
  this definition refers to the primary burst-path Finding ID recorded in the BURST
  PATH TABLE produced in Role 3, column SCHEMA-A BASELINE SOURCE — not a generic
  "before" state. A BASELINE definition that does not reference the BURST PATH TABLE
  by name and column is a SCHEMA-A SOURCE REFERENCE violation.
- PROTECTED: the sustained throughput achievable at the same burst-path source endpoint
  recorded under BP-xx in Role 3's BURST PATH TABLE, after the specific mitigation
  prescribed in Role 8c for that Finding ID is applied and active.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains conclusion without arithmetic.
- SCHEMA-A SOURCE REFERENCE: BASELINE definition omits reference to Role 3's BURST
  PATH TABLE or its SCHEMA-A BASELINE SOURCE column.

---

**SCHEMA-V — VOLUME MAPPING** (volume-to-behavior mapping table)

Applies to: Role 6 volume-to-behavior mapping.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Column definitions:
- VOLUME RANGE: named volume band derived from Verdict Claim (a)'s threshold. 5x spike
  row required with arithmetic derivation shown in the cell.
- BASELINE BEHAVIOR: system behavior at this volume range for the burst-path source
  endpoint identified by the primary Finding ID in Role 3's BURST PATH TABLE (BP-xx,
  column ENDPOINT NAME), without mitigation. This definition names the burst-path
  source via Role 3's BURST PATH TABLE — not generically.
- PROTECTED BEHAVIOR: system behavior at this volume range for the same endpoint with
  Role 8c mitigation active.
- Delta: quantified improvement — numeric or percentage. Generic labels are SCHEMA-V
  CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: missing VOLUME RANGE, BASELINE BEHAVIOR, PROTECTED BEHAVIOR,
  or Delta header.
- SCHEMA-V CONTENT: Delta cell states relative improvement without quantified value.

---

**SCHEMA-M — MITIGATION RECORD** (per-finding mitigation tables)

Applies to: Role 8c per-finding mitigation prescriptions.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Column definitions:
- FINDING ID: BP-xx from Role 3's BURST PATH TABLE or RH-xx from Role 5.
- BEFORE STATE: unmitigated behavior — component named, volume condition named, failure
  mode named.
- AFTER STATE: mitigated behavior — specific action named, setting or value named.
- Addresses: BP-xx burst path(s) covered.

Rejection clauses:
- SCHEMA-M STRUCTURAL: missing any of the four column headers.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE** (UX per throttle tier)

Applies to: Role 5 UX descriptions per throttle tier.

```
FIELD-A ERROR SIGNAL: [connector error code or platform signal — not "error occurs"]
FIELD-B USER-VISIBLE BEHAVIOR: [specific end-user experience]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific actionable recovery step]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing FIELD-A through FIELD-D labels.
- SCHEMA-B CONTENT: field contains a non-answer.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table whose column structure does not match
the schema declared for its producing role is a FORMAT-SCHEMA MISMATCH violation.
At least one instance of SCHEMA-A, SCHEMA-V, and SCHEMA-M must appear.

**Gate 2→3:** All three table schemas and UX block template declared. All rejection
clauses stated, including SCHEMA-A SOURCE REFERENCE clause. SCHEMA-V BASELINE BEHAVIOR
definition references Role 3's BURST PATH TABLE. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Produce a BURST PATH TABLE before any prose analysis:

| BP-ID | ENDPOINT NAME | TRIGGER CONDITION | CLASSIFICATION | SCHEMA-A BASELINE SOURCE |
|-------|--------------|-------------------|----------------|--------------------------|

Column definitions for the BURST PATH TABLE:
- BP-ID: assign BP-01, BP-02, ... (sequential, no gaps).
- ENDPOINT NAME: the connector endpoint name (consistent with Verdict Claim (a)).
- TRIGGER CONDITION: what causes the burst (e.g., "trigger fires on 500-item list
  update; loop iterates all 500 items synchronously").
- CLASSIFICATION: STRUCTURAL or INCIDENTAL.
  - STRUCTURAL: burst unavoidable without architectural redesign.
  - INCIDENTAL: burst removable by changing a setting or flow structure.
  - Note: a higher-tier limit is not path-level protection for this endpoint.
- SCHEMA-A BASELINE SOURCE: the specific state or measure at this endpoint that the
  Format Contract's SCHEMA-A BASELINE definition represents — describes what "the
  connector API call volume at burst onset" means for this specific endpoint and
  trigger (e.g., "600 API calls/min directed at the SharePoint List endpoint when the
  500-item loop fires without concurrency cap"). This column establishes the link from
  Role 3's output to the Format Contract's BASELINE definition.

After the BURST PATH TABLE:
- For each STRUCTURAL row: state why architectural redesign is required.
- For each INCIDENTAL row: state the specific setting or change that removes the burst.

Record total burst path count B from the table row count.

**Verdict-currency check:** if Claim (a)'s endpoint is not in the BURST PATH TABLE's
primary rows, insert `REVISED — see Role 3` on Claim (a) before this gate is unblocked.

**Gate 3→4:** BURST PATH TABLE written with all five columns populated. At least one
row classified STRUCTURAL. Total count B recorded from table row count.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers. For each:

1. Tier scope: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window.
3. Enforcing layer: connector / platform / both.
4. Affected BP-xx Finding IDs from Role 3's BURST PATH TABLE.
5. Scope-distinction check: variants at same scope level are not structurally distinct.

At least three structurally distinct tiers. Claim (a)'s threshold must appear with
its source.

**Verdict-currency check:** tighter tier found → `REVISED — see Role 4` on Claim (a).

**Gate 4→5:** Three structurally distinct tiers with thresholds. All tiers mapped to
BP-xx IDs from the BURST PATH TABLE.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier from Role 4, answer four sub-questions then write the SCHEMA-B block:
- (i) Run history signal? (ii) End-user behavior? (iii) Visibility level? (iv) Recovery action?

Six-item gate per block: (a) FIELD-A specific signal, (b) FIELD-B specific user state,
(c) FIELD-C named visibility, (d) FIELD-D specific recovery, (e) count = B from Role 3's
BURST PATH TABLE row count, (f) all four FIELD labels present.

At least two tiers with distinct FIELD-B descriptions.

**Gate 5→6:** All B tiers with complete SCHEMA-B blocks. Six-item gate satisfied.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V table, at least three volume ranges including 5x spike row. Derive spike from
Claim (a)'s threshold arithmetically; show the derivation in VOLUME RANGE cell.
Delta cells must be quantified.

**Gate 6→7:** SCHEMA-V table, three rows minimum, 5x spike row, all Delta cells quantified.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

SCHEMA-A table at 5x load:
- BASELINE: call volume at burst-path endpoint (from BURST PATH TABLE BP-xx) at 5x,
  before mitigation.
- PROTECTED: sustained throughput after Role 8c mitigation.
- DERIVATION CHAIN: (i) base×5=spike, (ii) spike−threshold=overflow,
  (iii) overflow×retry=total pressure, (iv) total÷threshold=failure rate.

Prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A table present. DERIVATION CHAIN shows four-step arithmetic.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**8a:** SCHEMA-A cascading failure table. Causal chain required — second limit causally
triggered by first. Causal chain prose required.

**8b:** 5x arithmetic for highest-severity burst path. All five steps shown.

**8c:** SCHEMA-M table, one row per Finding ID. AFTER STATE must name specific action
and setting.

**Gate 8→9:** SCHEMA-A in 8a with causal chain. 5x arithmetic in 8b (five steps).
SCHEMA-M in 8c with one row per Finding ID. Named AFTER STATE for each row.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R18

(a) After this invariant, no REVISED markers may be inserted into Roles 1–8.
(b) Role 9 does not insert REVISED markers.
(c) Role 9 inserts zero (0) REVISED markers.
(d) Violation: `FNMI-R18: VIOLATION at [reference] — [description]`.
    Compliant: `FNMI-R18: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R18 declared. Role 8 deliverables present. VERIFICATION-ONLY.

**CHECK (a):** Verdict revision marker audit.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c):** Derivation chain cell audit.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s)"

**CHECK (d):** Schema-B structural scan.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- FNMI-R18: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-04

**Axis:** Combination — V-01 (cell-level Finding ID prefix in SCHEMA-A table cells)
+ V-02 (Schema Production Registry with gate-linkage column). Both enforcement planes
operate simultaneously: (1) Format Contract column definitions carry Finding ID anchors
(C-41); (2) each schema entry is covered by a registry row naming the producing role
and gate condition (C-42 + registry gate-linkage); (3) every SCHEMA-A table cell
carries the BP-xx prefix making each row independently verifiable.

**Hypothesis:** Combining cell-level Finding ID tracing with the Schema Production
Registry creates orthogonal enforcement planes: registry lookup gives O(1) role
governance verification; cell-level BP-xx prefix gives O(1) row-level traceability.
Together they make every SCHEMA-A row independently auditable without reading the
Format Contract — a reader can extract the Finding ID from the cell prefix, locate
Role 3, and verify the row without consulting the column definitions. The registry
simultaneously confirms the producing role's assignment is explicit.

---

You are a Connectors / Power Automate throughput domain expert executing the
`flow-ratelimit` skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition
is fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any analysis begins:

(a) **Binding constraint:** connector endpoint name and numeric threshold.
(b) **Primary gap:** specific unprotected burst path — name it.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding without evidence
sections.

**Revision rule:** any analysis role that revises a claim inserts `REVISED — see Role N`
at that role's gate boundary before the next gate is evaluated.

**Gate 1→2:** All four claims written. No analysis has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section declares all structural schemas governing output in this document.

---

#### SCHEMA PRODUCTION REGISTRY

Authoritative mapping of schema type to producing role and gate condition.

| Schema | Producing Role(s) | Table Type | Gate Condition |
|--------|------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact table; cascade failure table | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping table | Gate 6→7 |
| SCHEMA-M | Role 8c | mitigation record table | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

Registry completeness rule: every table-producing role must have a registry entry.
A producing role not listed is unauthorized to produce tables. A missing registry row
is a REGISTRY GAP violation.

---

#### SCHEMA-A — PRIMARY ANALYSIS

Applies to: Role 7 quantified impact at load spike; Role 8a cascade failure analysis.
(See Schema Production Registry for gate conditions and role assignments.)

| BASELINE | PROTECTED | DERIVATION CHAIN |

Column definitions, with Finding ID anchors:

- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3 (BP-xx), measured at burst onset before any
  concurrency control, retry policy, or Role 8c mitigation is applied. This definition
  names the specific endpoint and Finding ID from Role 3 — not a generic "before" state.
  **Cell requirement:** each BASELINE cell must begin with the resolved Finding ID
  prefix: "BP-xx: [value]" (e.g., "BP-01: 600 API calls/min at burst onset"). A cell
  omitting the prefix is a SCHEMA-A CELL ANCHOR violation.
- PROTECTED: sustained throughput at the same endpoint after Role 8c mitigation for
  that Finding ID (BP-xx) is applied.
  **Cell requirement:** each PROTECTED cell must begin with the resolved Finding ID
  prefix: "BP-xx: [value]". A cell omitting the prefix is a SCHEMA-A CELL ANCHOR
  violation.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains conclusion without arithmetic.
- SCHEMA-A CELL ANCHOR: BASELINE or PROTECTED cell omits "BP-xx: " prefix.

---

#### SCHEMA-V — VOLUME MAPPING

Applies to: Role 6 volume-to-behavior mapping.
(See Schema Production Registry for gate conditions.)

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Column definitions:
- VOLUME RANGE: named volume band from Claim (a)'s threshold. 5x spike row required
  with arithmetic derivation in cell.
- BASELINE BEHAVIOR: system behavior for the burst-path source endpoint from Role 3,
  without mitigation.
- PROTECTED BEHAVIOR: same endpoint with Role 8c mitigation active.
- Delta: quantified improvement. Generic labels are SCHEMA-V CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: missing required column headers.
- SCHEMA-V CONTENT: Delta cell states relative improvement without quantified value.

---

#### SCHEMA-M — MITIGATION RECORD

Applies to: Role 8c per-finding mitigation prescriptions.
(See Schema Production Registry for gate conditions.)

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Column definitions:
- FINDING ID: BP-xx (from Role 3) or RH-xx (from Role 5).
- BEFORE STATE: unmitigated behavior with component, volume condition, and failure mode.
- AFTER STATE: mitigated behavior with specific action and setting named.
- Addresses: BP-xx burst paths covered.

Rejection clauses:
- SCHEMA-M STRUCTURAL: missing required column headers.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic.

---

#### SCHEMA-B — UX TIER BLOCK TEMPLATE

Applies to: Role 5 UX descriptions per throttle tier.
(See Schema Production Registry for gate conditions.)

```
FIELD-A ERROR SIGNAL: [specific connector error code or platform signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific end-user experience]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific actionable recovery step]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing FIELD-A through FIELD-D.
- SCHEMA-B CONTENT: field contains a non-answer.

---

Unified FORMAT-SCHEMA MISMATCH clause: tables not conforming to their registry-assigned
schema are FORMAT-SCHEMA MISMATCH violations. At least one SCHEMA-A, SCHEMA-V, and
SCHEMA-M instance must appear.

**Gate 2→3:** Schema Production Registry with four rows declared. Four schema sections
with headings. SCHEMA-A CELL ANCHOR violation clause stated. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint.
3. State the trigger condition.
4. Classify STRUCTURAL or INCIDENTAL.
   - STRUCTURAL: unavoidable without architectural redesign.
   - INCIDENTAL: removable by changing a setting.
   - Note: higher-tier limit is not path-level protection.
5. STRUCTURAL: state redesign requirement. INCIDENTAL: state removable setting.

Record total count B.

**Verdict-currency check:** if Claim (a)'s endpoint is not primary burst source,
insert `REVISED — see Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL. All paths have Finding IDs. Count B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers. For each: scope, threshold, enforcing layer, BP-xx
mapping, scope-distinction check. At least three structurally distinct tiers.
Claim (a)'s threshold must appear with source.

**Gate 4→5:** Three structurally distinct tiers. All tiers mapped to BP-xx IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

Four sub-questions per tier; SCHEMA-B block per tier. Six-item gate per block:
(a)-(d) field content requirements, (e) count = B from Role 3, (f) all four FIELD
labels. At least two tiers with distinct FIELD-B.

**Gate 5→6:** All B tiers with complete SCHEMA-B blocks.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V table, three rows minimum, 5x spike row with arithmetic derivation. All
Delta cells quantified.

**Gate 6→7:** SCHEMA-V table complete.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

SCHEMA-A table at 5x load:
- BASELINE: "BP-xx: [API call volume at 5x, before mitigation]" — BP-xx prefix required.
- PROTECTED: "BP-xx: [sustained throughput after Role 8c mitigation]" — BP-xx prefix required.
- DERIVATION CHAIN: (i) base×5, (ii) −threshold, (iii) ×retry, (iv) ÷threshold.

Prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A table with BP-xx prefix in BASELINE and PROTECTED cells.
Four-step arithmetic chain. Prose compounding effect.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**8a:** SCHEMA-A cascading failure. BASELINE "BP-xx: [value]" and PROTECTED "BP-xx:
[value]" — cell prefixes required. Causal chain prose required.

**8b:** 5x arithmetic for highest-severity burst path. Five steps shown.

**8c:** SCHEMA-M table, one row per Finding ID. AFTER STATE names specific action
and setting.

**Gate 8→9:** SCHEMA-A in 8a with BP-xx cell prefixes and causal chain. 5x arithmetic
(five steps). SCHEMA-M with one row per Finding ID.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R18

(a) After this invariant, no REVISED markers in Roles 1–8 from Role 9.
(b) Role 9 inserts no REVISED markers.
(c) Insertion count = 0.
(d) `FNMI-R18: VIOLATION at [reference] — [description]` or `FNMI-R18: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R18 declared. Role 8 deliverables present. VERIFICATION-ONLY.

**CHECK (a):** Verdict revision marker audit.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit.
Findings: "Gate Audit: N/N gates pass, M gate(s) missing deliverables"

**CHECK (c):** Derivation chain cell audit.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violations"

**CHECK (d):** Schema-B structural scan.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violations"

**CHECK (e) — SCHEMA PRODUCTION REGISTRY AUDIT + CELL ANCHOR AUDIT**

For each row in the Schema Production Registry:
- (e.1) Verify the producing role appears in this document.
- (e.2) Verify the producing role's table uses column headers matching the schema
  declaration (SCHEMA-A, SCHEMA-V, SCHEMA-M, or SCHEMA-B template).
- (e.3) Verify the table appears at or before the gate condition named in the registry.

For all SCHEMA-A tables (Role 7 and Role 8a):
- (e.4) Verify each BASELINE cell begins with "BP-xx: " prefix.
- (e.5) Verify each PROTECTED cell begins with "BP-xx: " prefix.
- (e.6) Verify the BP-xx value in each cell matches a Finding ID recorded in Role 3.

Findings: "Registry+Cell Audit: N registry rows pass, M REGISTRY MISMATCH; N cells
checked, M SCHEMA-A CELL ANCHOR violations, M unresolved BP-xx references"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R18: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-05

**Axis:** Full integration — V-01 (SCHEMA-A cell-level BP-xx prefix) + V-02 (Schema
Production Registry with gate-linkage) + V-03 (Role 3 BURST PATH TABLE with SCHEMA-A
BASELINE SOURCE column + SCHEMA-V BASELINE BEHAVIOR Finding ID extension) + Role 9
CHECK (e) cross-role ID traceability audit covering all three planes simultaneously.

**Hypothesis:** Full integration creates a three-plane enforcement chain for C-41 and
C-42: (1) Format Contract column definitions carry Finding ID anchors pointing to
Role 3's BURST PATH TABLE (declaration plane); (2) Schema Production Registry maps
each schema to its producing roles and gate conditions (governance plane); (3) every
SCHEMA-A table cell carries the BP-xx prefix anchored to Role 3's BURST PATH TABLE
(cell plane). Role 9 CHECK (e) audits all three planes simultaneously, producing
per-plane findings that reveal any gap in the chain. SCHEMA-V BASELINE BEHAVIOR's
extension to reference Role 3's table tests whether C-41 should be universal to all
BASELINE-type definitions. Predicted C-43 and C-44 candidates: (a) SCHEMA-A cells
carrying resolved Finding IDs (not placeholders) as a structural requirement; (b)
SCHEMA-V BASELINE BEHAVIOR referencing Role 3's Finding IDs as a requirement parallel
to SCHEMA-A's C-41 requirement.

---

You are a Connectors / Power Automate throughput domain expert executing the
`flow-ratelimit` skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition
is fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any rate limit inventory, burst path audit,
cascade analysis, UX description, or volume mapping begins. These claims are subject
to revision during analysis.

(a) **Binding constraint:** connector endpoint name and numeric threshold.
(b) **Primary gap:** specific unprotected burst path — name it.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding, primary gap,
system status, and UX coverage scope without evidence sections.

**Revision rule:** any analysis role that revises a claim inserts `REVISED — see Role N`
at that role's gate boundary before the next gate is evaluated.

**Gate 1→2:** All four claims written. No analysis, inventory, or table has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section declares all structural schemas governing output in this document. Every
table and UX block in Roles 3–8 must conform to the schema declared for its producing
role in the Schema Production Registry.

---

#### SCHEMA PRODUCTION REGISTRY

Authoritative mapping of schema type to producing role and gate condition. An evaluator
verifying any role's table locates the row for that role, identifies the applicable
schema, and checks the table against the schema declaration below.

| Schema | Producing Role(s) | Table Type | Gate Condition |
|--------|------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact table; cascade failure table | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping table | Gate 6→7 |
| SCHEMA-M | Role 8c | mitigation record table | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

Registry completeness rule: every table-producing role must have a registry entry.
A producing role without an entry is unauthorized to produce tables. A missing registry
row is a REGISTRY GAP violation, detectable by comparing registry row count against
the producing role count in this document.

---

#### SCHEMA-A — PRIMARY ANALYSIS

Applies to: Role 7 quantified impact at load spike; Role 8a cascade failure analysis.
(See Schema Production Registry for gate conditions.)

| BASELINE | PROTECTED | DERIVATION CHAIN |

Column definitions, with Finding ID anchors derived from Role 3's BURST PATH TABLE:

- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3's BURST PATH TABLE (BP-xx, column ENDPOINT NAME),
  measured at burst onset before any concurrency control, retry policy, or Role 8c
  mitigation is applied. The BP-xx in this definition refers to the specific Finding ID
  in Role 3's BURST PATH TABLE — not a generic "before" state. A BASELINE definition
  that does not name Role 3's BURST PATH TABLE as the source of the endpoint identity
  is a SCHEMA-A SOURCE REFERENCE violation.
  **Cell requirement:** each BASELINE cell in any SCHEMA-A table must begin with the
  resolved Finding ID prefix "BP-xx: [value]" where BP-xx is the actual Finding ID
  from Role 3's BURST PATH TABLE (e.g., "BP-01: 600 API calls/min at burst onset").
  A cell omitting the prefix is a SCHEMA-A CELL ANCHOR violation.
- PROTECTED: sustained throughput at the same endpoint from Role 3's BURST PATH TABLE
  after the mitigation prescribed in Role 8c for that Finding ID (BP-xx) is applied.
  **Cell requirement:** each PROTECTED cell must begin with "BP-xx: [value]". A cell
  omitting the prefix is a SCHEMA-A CELL ANCHOR violation.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains conclusion without arithmetic.
- SCHEMA-A SOURCE REFERENCE: BASELINE definition omits reference to Role 3's BURST
  PATH TABLE.
- SCHEMA-A CELL ANCHOR: BASELINE or PROTECTED cell omits resolved "BP-xx: " prefix.

---

#### SCHEMA-V — VOLUME MAPPING

Applies to: Role 6 volume-to-behavior mapping.
(See Schema Production Registry for gate conditions.)

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Column definitions:
- VOLUME RANGE: named volume band from Claim (a)'s threshold. 5x spike row required;
  derivation arithmetic shown in cell.
- BASELINE BEHAVIOR: system behavior at this volume range for the burst-path source
  endpoint recorded in Role 3's BURST PATH TABLE under the primary Finding ID (BP-xx,
  column ENDPOINT NAME), without mitigation. This definition names the endpoint via
  Role 3's BURST PATH TABLE — not generically. A BASELINE BEHAVIOR definition that
  does not reference Role 3's BURST PATH TABLE is a SCHEMA-V SOURCE REFERENCE violation.
- PROTECTED BEHAVIOR: system behavior at the same endpoint with Role 8c mitigation
  active.
- Delta: quantified improvement. Generic labels without quantified values are SCHEMA-V
  CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: missing required column headers.
- SCHEMA-V CONTENT: Delta cell lacks quantified value.
- SCHEMA-V SOURCE REFERENCE: BASELINE BEHAVIOR definition omits reference to Role 3's
  BURST PATH TABLE.

---

#### SCHEMA-M — MITIGATION RECORD

Applies to: Role 8c per-finding mitigation prescriptions.
(See Schema Production Registry for gate conditions.)

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Column definitions:
- FINDING ID: BP-xx from Role 3's BURST PATH TABLE or RH-xx from Role 5.
- BEFORE STATE: unmitigated behavior — component, volume condition, failure mode all
  named. Generic descriptions are SCHEMA-M CONTENT violations.
- AFTER STATE: mitigated behavior — specific action and specific setting named.
  Generic descriptions are SCHEMA-M CONTENT violations.
- Addresses: BP-xx burst path(s) covered.

Rejection clauses:
- SCHEMA-M STRUCTURAL: missing required column headers.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic.

---

#### SCHEMA-B — UX TIER BLOCK TEMPLATE

Applies to: Role 5 UX descriptions per throttle tier.
(See Schema Production Registry for gate conditions.)

```
FIELD-A ERROR SIGNAL: [specific connector error code or platform signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific end-user experience]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific actionable recovery step]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing FIELD-A through FIELD-D.
- SCHEMA-B CONTENT: field contains a non-answer.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not conforming to its registry-
assigned schema is a FORMAT-SCHEMA MISMATCH violation. At least one SCHEMA-A,
SCHEMA-V, and SCHEMA-M instance must appear.

**Gate 2→3:** Schema Production Registry with four rows declared. Four schema sections
with headings. SCHEMA-A CELL ANCHOR and SOURCE REFERENCE violation clauses stated.
SCHEMA-V SOURCE REFERENCE clause stated. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Produce a BURST PATH TABLE before any prose analysis:

| BP-ID | ENDPOINT NAME | TRIGGER CONDITION | CLASSIFICATION | SCHEMA-A BASELINE SOURCE |
|-------|--------------|-------------------|----------------|--------------------------|

Column definitions:
- BP-ID: BP-01, BP-02, ... (sequential, no gaps).
- ENDPOINT NAME: connector endpoint name (consistent with Verdict Claim (a)).
- TRIGGER CONDITION: what causes the burst.
- CLASSIFICATION: STRUCTURAL or INCIDENTAL.
  - STRUCTURAL: burst unavoidable without architectural redesign.
  - INCIDENTAL: burst removable by changing a setting.
  - Note: higher-tier limit is not path-level protection for this endpoint.
- SCHEMA-A BASELINE SOURCE: the specific state or measure at this endpoint that the
  Format Contract's SCHEMA-A BASELINE definition and SCHEMA-V BASELINE BEHAVIOR
  definition represent — names the API call volume at burst onset in concrete terms
  (e.g., "600 API calls/min directed at the SharePoint List endpoint when the 500-item
  loop fires without a concurrency cap"). This column makes the BURST PATH TABLE the
  authoritative source for BASELINE definitions in SCHEMA-A and SCHEMA-V.

After the table:
- For each STRUCTURAL row: state why architectural redesign is required.
- For each INCIDENTAL row: state the specific removable setting.

Record total count B from table row count.

**Verdict-currency check:** if Claim (a)'s endpoint is not in the BURST PATH TABLE's
primary rows, insert `REVISED — see Role 3` on Claim (a).

**Gate 3→4:** BURST PATH TABLE written with all five columns populated. At least one
STRUCTURAL row. Count B recorded from table row count.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers. For each: scope, threshold and time window, enforcing
layer, BP-xx mapping from BURST PATH TABLE, scope-distinction check. At least three
structurally distinct tiers. Claim (a)'s threshold must appear with source.

**Verdict-currency check:** tighter tier found → `REVISED — see Role 4` on Claim (a).

**Gate 4→5:** Three structurally distinct tiers with thresholds. All tiers mapped to
BP-xx from BURST PATH TABLE.

---

### ROLE 5 — UX PER THROTTLE TIER

Four sub-questions per tier; SCHEMA-B block per tier. Six-item gate:
(a) FIELD-A specific signal, (b) FIELD-B specific state, (c) FIELD-C named visibility,
(d) FIELD-D specific recovery, (e) count = B from BURST PATH TABLE row count,
(f) all four FIELD labels.

At least two tiers with distinct FIELD-B.

**Verdict-currency check:** new tiers found → `REVISED — see Role 5` on Claim (d).

**Gate 5→6:** All B tiers with complete SCHEMA-B blocks. Six-item gate satisfied.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V table, three rows minimum, 5x spike row with arithmetic derivation in
VOLUME RANGE cell. BASELINE BEHAVIOR cells must identify the source endpoint via the
primary Finding ID from Role 3's BURST PATH TABLE. All Delta cells quantified.

**Gate 6→7:** SCHEMA-V table with three rows, 5x spike, quantified Delta cells,
and BASELINE BEHAVIOR cells referencing Role 3's BURST PATH TABLE.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

SCHEMA-A table at 5x load:
- BASELINE: "BP-xx: [API call volume at burst-path endpoint at 5x, before mitigation]"
  — BP-xx is the resolved Finding ID from Role 3's BURST PATH TABLE. Cell anchor required.
- PROTECTED: "BP-xx: [sustained throughput after Role 8c mitigation]"
  — same resolved Finding ID. Cell anchor required.
- DERIVATION CHAIN: (i) base×5=spike, (ii) spike−threshold=overflow,
  (iii) overflow×retry=total, (iv) total÷threshold=failure rate.

Prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A table with resolved BP-xx prefix in BASELINE and PROTECTED
cells. Four-step arithmetic. Prose compounding effect.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**8a:** SCHEMA-A cascading failure table. BASELINE "BP-xx: [value]" and PROTECTED
"BP-xx: [value]" — resolved Finding ID cell prefixes required. Causal chain prose
required: second limit causally triggered by first.

**8b:** 5x arithmetic for highest-severity burst path from BURST PATH TABLE.
Five steps: threshold → ×5 → overflow → ×retry → failure rate.

**8c:** SCHEMA-M table. One row per Finding ID from BURST PATH TABLE (BP-xx) and
Role 5 (RH-xx). AFTER STATE must name specific action and setting.

**Gate 8→9:** SCHEMA-A in 8a with resolved BP-xx cell prefixes and causal chain.
5x arithmetic (five steps). SCHEMA-M with one row per Finding ID, named AFTER STATE.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R18

This invariant is named FNMI-R18 and governs the Terminal Reconciler (Role 9).

(a) After this invariant, no REVISED markers may be inserted into Roles 1–8. Conditions
    found in Role 9 requiring revision are recorded as FNMI-R18 findings.
(b) Role 9 does not insert REVISED markers into sections from Roles 1–8.
(c) Role 9 inserts zero (0) REVISED markers. Insertion count = 0.
(d) Any REVISED marker by Role 9 is: `FNMI-R18: VIOLATION at [reference] — [description]`.
    Absence of violations: `FNMI-R18: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R18 declared. Role 8 deliverables present. VERIFICATION-ONLY per FNMI-R18.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Scan Verdict claims (a)–(d). Verify REVISED marker for every revised claim with forward
reference to revising role.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Enumerate Gate 1→2 through Gate 8→9. Verify named deliverables present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Scan every DERIVATION CHAIN cell in SCHEMA-A tables (Roles 7 and 8a). Flag conclusions
without arithmetic.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s)"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**
Count FIELD labels in every Role 5 UX tier block. Flag blocks missing FIELD-A through
FIELD-D.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s)"

**CHECK (e) — THREE-PLANE TRACEABILITY AUDIT**

Plane 1 — Schema Production Registry coverage:
- (e.1) Verify the registry has exactly four rows (SCHEMA-A, SCHEMA-V, SCHEMA-M,
  SCHEMA-B), one per producing role or role group.
- (e.2) For each registry row, verify the producing role appears and produces a table
  in this document. A role listed but absent is a REGISTRY GAP violation.
- (e.3) Verify each producing role's table column headers match the schema declared
  for that type. A mismatch is a FORMAT-SCHEMA MISMATCH violation.

Plane 2 — SCHEMA-A cell-level Finding ID anchors:
- (e.4) For every SCHEMA-A table in Roles 7 and 8a, scan BASELINE and PROTECTED cells.
  Verify each opens with "BP-xx: " where BP-xx is a specific Finding ID (not the
  literal placeholder "BP-xx").
- (e.5) For each resolved Finding ID found in Step (e.4), verify that Finding ID
  exists in Role 3's BURST PATH TABLE. A Finding ID that does not appear in the BURST
  PATH TABLE is an UNRESOLVED REFERENCE violation.

Plane 3 — SCHEMA-V BASELINE BEHAVIOR source reference:
- (e.6) Verify the SCHEMA-V table's BASELINE BEHAVIOR cells identify the source endpoint
  in terms consistent with Role 3's BURST PATH TABLE ENDPOINT NAME column — not a
  generic description.

Findings: "Three-Plane Audit:
  Plane 1 (registry): N/N rows pass, M violation(s): [list];
  Plane 2 (cell anchors): N cells pass, M SCHEMA-A CELL ANCHOR / UNRESOLVED REFERENCE;
  Plane 3 (SCHEMA-V source): N rows pass, M SCHEMA-V SOURCE REFERENCE violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R18: COMPLIANT / VIOLATION at [reference] — [description]
