---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 17
rubric_version: 16
---

# flow-ratelimit — Variate R17

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (role sequence — burst-path-first with C-39/C-40 inline prose
Format Contract), V-02 (output format — per-schema subsection headers in Format Contract),
V-03 (lifecycle emphasis — Format Contract expanded with role-to-schema mapping table and
component-name slot placeholders).
Combination variations: V-04 (role sequence + output format — burst-path-first + schema
subsection headers), V-05 (full integration — all three axes + schema-type compliance audit
in Terminal Reconciler as CHECK (e)).

**R17 target criteria: C-39, C-40**

C-39 (Format Contract Scenario-Anchored Column Definitions): BASELINE and PROTECTED in the
Format Contract are defined using the scenario's actual component names and states at the
point of declaration. Definitions must be self-contained — no deferral to wherever the
scenario is introduced. A reader of the Format Contract section alone knows which component
BASELINE refers to.

C-40 (Format Contract Per-Table-Type Schema Decomposition): The Format Contract declares
three distinct schemas — primary analysis, volume mapping, mitigation record — each with
its own column structure and rejection clause. A single universal schema applied to all
table types does not satisfy C-40, even if it is compliant with C-16.

**R17 variation axes:**

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Role sequence | burst-path-first | burst-path-first | burst-path-first | burst-path-first | burst-path-first |
| C-39 (scenario-anchored defs) | inline prose, component names | inline prose, component names | component-name slot placeholders | inline prose | inline prose |
| C-40 (per-table-type schemas) | three schemas, inline prose | three schemas, subsection headers | three schemas with role-mapping table | three schemas, subsection headers | three schemas + reconciler audit |
| Format Contract style | declarative prose + rejection clauses | named subsection headers per schema | expanded with role-schema mapping | subsection headers | comprehensive with CHECK (e) |
| Predicted C-39 | PASS | PASS | PASS | PASS | PASS |
| Predicted C-40 | PASS | PASS | PASS | PASS | PASS |

---

## V-01

**Axis:** Role sequence — burst-path-first ordering (Role 3 = Burst Path Audit before Role 4
= Tier Inventory) combined with a Format Contract that declares three distinct table schemas
(C-40) with scenario-anchored BASELINE/PROTECTED definitions (C-39) as inline prose.

**Hypothesis:** The burst-path-first ordering forces Structural/Incidental classification
before tier evidence is available, closing the alibi escape hatch. The Format Contract's
scenario-anchored BASELINE/PROTECTED definitions — naming the connector endpoint and the
burst-path Finding ID from Role 3 — make the Format Contract self-interpreting: a reader
does not need to find the scenario introduction to know what BASELINE refers to. The three
per-table-type schemas (SCHEMA-A, SCHEMA-V, SCHEMA-M) eliminate ambiguity about which column
structure governs which table type throughout the document.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any rate limit inventory, burst path audit, cascade
analysis, UX description, or volume mapping begins. These claims are subject to revision
during analysis.

(a) **Binding constraint:** name of the connector endpoint or platform limit that is hit
    first, with its numeric threshold (e.g., "SharePoint REST API: 600 calls per 60 seconds
    per connection").
(b) **Primary gap:** the specific action or burst path where protection is absent —
    name the path, not the category.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** total throttle tier count that will receive full UX
    descriptions in this document, and a statement that every tier uses the complete
    four-field template. Format: "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding, the primary unprotected
path, the system status, and the UX coverage scope without proceeding to evidence sections.

**Revision rule:** any analysis role that revises a Verdict claim inserts an inline
`REVISED — see Role N` marker against the specific claim at that role's gate boundary,
before the next role's gate condition is evaluated. Deferring revision markers to the
terminal reconciler is a revision currency violation.

**Gate 1→2:** All four claims written. No analysis, inventory, or table has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section declares all structural schemas and block templates governing output in this
document. Every table and UX block produced in Roles 3–8 must match the schema or template
declared here for its table type. Any table whose column structure does not match its
declared type is a FORMAT-SCHEMA MISMATCH violation, detectable at scan time by comparing
column headers against the declarations below.

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 8a cascade failure analysis; Role 7 quantified impact at load spike.

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3 (BP-xx), measured at the point of burst onset, before
  any concurrency control, retry policy, or throttle mitigation prescribed in Role 8c
  is applied. This definition refers to the specific connector endpoint and Finding ID
  produced in Role 3 — not a generic "before" state.
- PROTECTED: the sustained connector API call throughput achievable at the same burst-path
  source endpoint after the specific mitigation action prescribed in Role 8c for that
  Finding ID (BP-xx) is applied and active.
- DERIVATION CHAIN: step-by-step arithmetic tracing the computation. Bare conclusions
  without computation steps are SCHEMA-A CONTENT violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: table missing one or more of BASELINE, PROTECTED, DERIVATION CHAIN
  column headers. Detectable at scan time.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains a conclusion without computation steps
  (e.g., "exceeds limit" without arithmetic). Requires reading cell content to detect.

---

**SCHEMA-V — VOLUME MAPPING** (volume-to-behavior mapping table)

Applies to: Role 6 volume-to-behavior mapping.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- VOLUME RANGE: named volume band using values derived from the threshold cited in
  Verdict Claim (a) (e.g., "0–400 req/min [below threshold]", "5x spike —
  3,000 req/min [derived from Role 3 burst path source threshold × 5]"). The 5x spike
  row is required; its value must be derived arithmetically.
- BASELINE BEHAVIOR: system behavior at this volume range for the burst-path source
  endpoint identified in Role 3, without mitigation.
- PROTECTED BEHAVIOR: system behavior at this volume range for the same endpoint,
  with the Role 8c mitigation active.
- Delta: quantified improvement — numeric or percentage change. Generic labels
  ("better", "reduced") without quantified values are SCHEMA-V CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: table missing one or more of VOLUME RANGE, BASELINE BEHAVIOR,
  PROTECTED BEHAVIOR, Delta column headers. Detectable at scan time.
- SCHEMA-V CONTENT: Delta cell states a relative improvement without a quantified value.

---

**SCHEMA-M — MITIGATION RECORD** (per-finding mitigation tables)

Applies to: Role 8c per-finding mitigation prescriptions.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- FINDING ID: the burst-path Finding ID (BP-xx from Role 3) or retry-gap Finding ID
  (RH-xx from Role 5) that this mitigation targets. Must match a Finding ID recorded
  in Role 3 or Role 5.
- BEFORE STATE: the unmitigated behavior for this specific Finding ID — names the
  component, the volume condition, and the failure mode. Generic descriptions
  ("throttling occurs") without component and condition names are SCHEMA-M CONTENT
  violations.
- AFTER STATE: the mitigated behavior after the named action is applied — names the
  specific action, setting, or pattern. Generic descriptions ("throttling reduced")
  without a named action are SCHEMA-M CONTENT violations.
- Addresses: burst path(s) from Role 3 (BP-xx) covered by this mitigation.

Rejection clauses:
- SCHEMA-M STRUCTURAL: table missing one or more of FINDING ID, BEFORE STATE, AFTER
  STATE, Addresses column headers. Detectable at scan time.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic — no component named,
  no action named, or a non-answer present.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE** (UX per throttle tier)

Applies to: Role 4 UX descriptions per throttle tier.

```
FIELD-A ERROR SIGNAL: [connector error code or platform signal name — not "error occurs"]
FIELD-B USER-VISIBLE BEHAVIOR: [what the end user sees or experiences — specific]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific action the user or flow can take — not "retry later"]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing one or more of FIELD-A through FIELD-D labels.
  Detectable at scan time.
- SCHEMA-B CONTENT: a field contains a non-answer (blank, "N/A", "varies", "see above",
  a generic instruction without specifics). Requires reading field content to detect.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table in this document whose column structure
does not match the schema type declared for its producing role is a FORMAT-SCHEMA MISMATCH
violation. This violation is detectable at scan time by comparing column headers against
the declarations in this role. At least one SCHEMA-A table, one SCHEMA-V table, and one
SCHEMA-M table must appear elsewhere in this document; any that do not appear are schema
declaration gaps.

**Gate 2→3:** All three table schemas and the UX block template declared. All rejection
clauses stated. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths for the scenario. For each burst path:

1. Assign a Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint(s) involved — use names consistent with Verdict Claim (a).
3. State the trigger condition (what causes the burst: e.g., "trigger fires on 500-item
   SharePoint list update; loop iterates all 500 items synchronously").
4. Classify as STRUCTURAL or INCIDENTAL.
   - STRUCTURAL: the burst is unavoidable given the current architecture — it cannot be
     eliminated without redesigning the flow structure or changing the data model.
   - INCIDENTAL: the burst is an artifact of the current implementation — removable by
     changing a setting, adding a control, or restructuring without changing the data model.
   - Note: a higher-tier platform limit is not path-level protection. A connector-level
     limit that is technically "covered" by a tenant-level limit is still STRUCTURAL if
     the connector endpoint itself has no concurrency control.
5. For STRUCTURAL paths, state why architectural redesign would be required.
6. For INCIDENTAL paths, state the specific setting or structural change that would remove
   the burst.

Record the total burst path count as B. This count is the authoritative source for the
tier count verification in Role 4 gate item (e).

If Verdict Claim (a)'s stated endpoint does not appear as the primary burst source among
the identified paths, insert `REVISED — see Role 3` on Claim (a) before this role's gate
is unblocked.

**Gate 3→4:** At least one burst path classified STRUCTURAL. Finding IDs assigned to all
paths. Total count B recorded. This gate does not open until at least one STRUCTURAL
classification is committed — a document where all burst paths are INCIDENTAL proceeds
no further until the architecture is re-examined and a STRUCTURAL path is identified or
the STRUCTURAL gate condition is explicitly contested.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers relevant to the scenario. For each tier:

1. Name the tier scope: per-connection / per-user / per-tenant / global / platform.
2. State the numeric threshold and time window (e.g., "600 API calls per 60 seconds per
   connection").
3. Identify the enforcing layer: connector-enforced / platform-enforced / both.
4. Map to burst path: which BP-xx Finding IDs from Role 3 are affected by this tier.
5. Scope-distinction check: two tiers with different numeric thresholds but the same scope
   level (e.g., two per-connection limits with different call counts) are not structurally
   distinct tiers — they are variants of the same tier type. Structurally distinct tiers
   must differ in scope level, enforcing layer, or the class of actions they constrain.

At least three structurally distinct tiers must be identified before proceeding.

For at least one tier, cite the concrete numeric threshold as evidence (the threshold stated
in Verdict Claim (a) must appear here with its source).

**Verdict-currency check:** if the tiers identified here revise the binding constraint named
in Verdict Claim (a) — for example, a tighter tier is found than originally stated —
insert `REVISED — see Role 4` on Claim (a) before this role's gate is unblocked.

**Gate 4→5:** At least three structurally distinct tiers identified with numeric thresholds
and scope. All tiers mapped to BP-xx Finding IDs from Role 3.

---

### ROLE 5 — UX PER THROTTLE TIER

For each throttle tier identified in Role 4, produce a SCHEMA-B UX block.

For each tier, answer four sub-questions before writing the block:
- (i) What does the run history show when this tier is hit? (specific error code or
      platform signal)
- (ii) What does the end user see or experience when this tier is hit?
- (iii) How visible is the failure? (Silent: only admins see it / Banner: visible to
        user but non-blocking / Modal: blocks user action / Blocking: flow terminates)
- (iv) What specific recovery action is available to the user or to the flow?

Then write the SCHEMA-B block using the answers:

```
FIELD-A ERROR SIGNAL: [answer to (i)]
FIELD-B USER-VISIBLE BEHAVIOR: [answer to (ii)]
FIELD-C VISIBILITY LEVEL: [answer to (iii): Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [answer to (iv)]
```

Gate items per block — all six must be satisfied:
(a) FIELD-A present and names a specific signal, not a generic "error occurs"
(b) FIELD-B present and describes a specific user-visible state
(c) FIELD-C present with one of the four named visibility levels
(d) FIELD-D present and names a specific actionable recovery step
(e) Tier count in this role equals B from Role 3 — verify against Role 3's recorded count
    directly. Do not use Verdict Claim (d) as the tier count source.
(f) Every block has all four FIELD labels (SCHEMA-B STRUCTURAL compliance).

**Verdict-currency check:** if this role discovers tiers not anticipated in Verdict Claim (d),
insert `REVISED — see Role 5` on Claim (d) before this role's gate is unblocked.

At least two tiers must have distinct UX descriptions — identical FIELD-B descriptions
across all tiers is a UX collapse failure.

**Gate 5→6:** All B tiers have complete SCHEMA-B blocks. Six-item gate satisfied for each
tier. At least two tiers with distinct UX descriptions.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce a SCHEMA-V table with at least three volume ranges, including a mandatory 5x spike
row.

For the 5x spike row: derive the spike volume arithmetically from the threshold named in
Verdict Claim (a). Show the multiplication: [threshold] × 5 = [spike volume]. This
derivation must appear in the VOLUME RANGE cell of the 5x row.

Example structure:
| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |
|---|---|---|---|
| 0–[threshold]: normal load | [behavior without mitigation] | [behavior with mitigation] | [quantified improvement] |
| [threshold]–[2× threshold]: elevated | [behavior] | [behavior] | [quantified] |
| 5x spike — [threshold × 5] req/[window]: derived | [behavior — including error rate, queue depth at T+30s if applicable] | [behavior] | [quantified] |

Delta cells must state quantified improvements (e.g., "error rate 45% → <2%", "queue depth
at T+30s: 250 → 0"). Generic labels ("better", "significantly reduced") without quantified
values are SCHEMA-V CONTENT violations.

**Gate 6→7:** SCHEMA-V table with at least three rows including 5x spike. All Delta cells
quantified. 5x spike volume arithmetically derived.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce a SCHEMA-A table showing the cascading impact at 5x load. The table must show:

- BASELINE: the connector API call volume at the burst-path source endpoint (BP-01 or
  highest-impact burst path from Role 3) at 5x load, before mitigation.
- PROTECTED: the sustained throughput after Role 8c mitigation is applied.
- DERIVATION CHAIN: step-by-step arithmetic. The chain must include:
  (i)   [base volume] × 5 = [spike volume]
  (ii)  [spike volume] − [threshold from Claim (a)] = [overflow volume]
  (iii) [overflow] × [retry factor or parallel branch count] = [total attempted calls]
  (iv)  [total attempted] ÷ [threshold] = [failure rate or queue saturation factor]

Bare conclusions in the DERIVATION CHAIN ("exceeds limit", "throttling occurs") without
arithmetic are SCHEMA-A CONTENT violations.

Follow the table with prose: describe the compounding effect — how does the overflow volume
amplify retry pressure, and what is the failure state at T+30s and T+60s?

**Gate 7→8:** SCHEMA-A table present. DERIVATION CHAIN shows four-step arithmetic chain.
Compounding effect described in prose.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

Construct a SCHEMA-A table for the cascading failure scenario. Causal chain requirement:
two independent limits both hit under load do not constitute a cascade — the second must
be causally triggered by the first. Name the causal mechanism.

- BASELINE: call volume at the first-hit endpoint when it reaches its threshold.
- PROTECTED: call volume with circuit-breaker or backoff applied at the first endpoint.
- DERIVATION CHAIN: show the causal chain step-by-step — which endpoint hits its limit
  first, which downstream calls are blocked or re-triggered as a result, the compounding
  effect on retry volume at the second endpoint, and the arithmetic for the second limit hit.

Causal chain statement (prose, required): "When [endpoint A] hits its [threshold] limit at
[volume], [downstream effect] because [causal mechanism]. This triggers [endpoint B] to
receive [derived overflow volume], which hits its [threshold] limit."

**ROLE 8b — 5x ARITHMETIC DERIVATION**

For the highest-severity burst path from Role 3, show the derivation from the stated
threshold at 5x load. Required arithmetic:

- State the threshold from Role 4 for this endpoint.
- Derive 5x: [threshold] × 5 = [spike volume].
- Show overflow: [spike volume] − [threshold] = [overflow].
- Show retry amplification: [overflow] × [retry factor] = [total request pressure].
- State the percentage of requests that fail: [failed] ÷ [total] = [failure rate].

Do not assert a failure rate without showing the arithmetic that produces it.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

Produce a SCHEMA-M table with one row per Finding ID from Role 3 (BP-xx) and Role 5 (RH-xx).

Prescription requirement: the AFTER STATE cell must name the specific action, setting, or
pattern. These do not pass: "add retry logic", "enable throttle protection", "reduce call
volume". These pass: "enable concurrency control on the For Each action capped at 5 parallel
branches", "set Retry Policy to Exponential with 4 retries and base interval 20 seconds",
"add a Delay action of [derived value] seconds between batches using the formula:
[overflow] ÷ [threshold per second] = [minimum delay]".

For each row, state:
- FINDING ID: BP-xx or RH-xx.
- BEFORE STATE: the unmitigated behavior — name the component, the volume condition, and
  the failure mode that occurs.
- AFTER STATE: the mitigated behavior — name the specific action applied, the setting or
  value used, and the resulting behavior.
- Addresses: the BP-xx burst paths from Role 3 that this mitigation covers.

**Gate 8→9:** SCHEMA-A table in 8a with causal chain in DERIVATION CHAIN. 5x arithmetic
derivation in 8b shows all five steps. SCHEMA-M table in 8c has one row per Finding ID.
All AFTER STATE cells name a specific action with a specific setting or value.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R17

This invariant is named FNMI-R17 and governs the Terminal Reconciler (Role 9) that follows.

(a) After this invariant is declared, no REVISED markers may be inserted into Roles 1–8.
    A condition discovered during Role 9 that would in forward execution require a REVISED
    marker is recorded as a named FNMI-R17 reconciler finding — the marker is not inserted.
(b) The Terminal Reconciler (Role 9) does not insert REVISED markers into any section
    authored during Roles 1–8.
(c) The Terminal Reconciler inserts zero (0) REVISED markers. Insertion count = 0. Any
    REVISED marker appearing in output produced by Role 9 violates FNMI-R17.
(d) Any REVISED marker insertion by Role 9 is a FNMI-R17 VIOLATION. The Terminal Reconciler
    names any such violation in its findings output as:
    `FNMI-R17: VIOLATION at [Finding ID or Claim reference] — [description]`.
    Absence of violations is reported as: `FNMI-R17: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R17 declared. Role 8 deliverables (SCHEMA-A in 8a, 5x arithmetic in 8b,
SCHEMA-M in 8c) present.

This role is VERIFICATION-ONLY per FNMI-R17. Perform four checks. Each check produces its
own named findings output.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**

Scan Verdict Block claims (a)–(d) in Role 1. For each claim, confirm:
- An inline REVISED marker is present for every claim revised during analysis.
- Each marker includes a forward reference to the revising role.
This check is pure verification — FNMI-R17 prohibits inserting markers here.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**

Enumerate each gated transition (Gate 1→2 through Gate 8→9). For each gate, confirm the
named prior-role deliverables are present in the document.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**

Scan every DERIVATION CHAIN cell in all SCHEMA-A tables (Role 7 and Role 8a). Flag any
cell containing only a conclusion without computation steps as a SCHEMA-A CONTENT violation.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**

Count FIELD labels in every UX tier block in Role 5. Flag any block missing one or more of
FIELD-A through FIELD-D as a SCHEMA-B STRUCTURAL violation.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- FNMI-R17: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-02

**Axis:** Output format — the Format Contract presents each schema as a named subsection
with a heading marker (### SCHEMA 1, ### SCHEMA 2, ### SCHEMA 3), making the three-schema
decomposition detectable at scan time as distinct document sections rather than as prose
blocks within a single role. BASELINE/PROTECTED definitions remain scenario-anchored (C-39).
Role sequence is identical to V-01 (burst-path-first).

**Hypothesis:** Structuring the three schemas as separately headed subsections rather than
inline prose declarations makes C-40's per-table-type decomposition independently scan-time
verifiable. An evaluator can locate each schema declaration without reading the full Format
Contract body — the presence of three distinct schema headings confirms the three-schema
structure at structural scan time, parallel to how a standalone FNMI heading confirms C-36.
The scenario-anchored definitions remain within each schema's subsection, satisfying C-39.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any analysis begins:

(a) **Binding constraint:** connector endpoint name and numeric threshold.
(b) **Primary gap:** specific unprotected burst path or action — name it.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** N tiers described; all tiers use the four-field UX template.

Self-containment: a reader of only this block knows the core finding without proceeding
to evidence sections.

**Revision rule:** any analysis role that revises a claim inserts `REVISED — see Role N`
at that role's gate boundary. Deferring to the terminal reconciler is a revision currency
violation.

**Gate 1→2:** All four claims written. No analysis yet.

---

### ROLE 2 — FORMAT CONTRACT

The following sections declare the structural schemas for this document. Every table in
Roles 3–8 must match the schema type declared for its producing role.

---

#### SCHEMA 1 — PRIMARY ANALYSIS

**Applies to:** Role 8a cascade failure table; Role 7 quantified impact table.

| BASELINE | PROTECTED | DERIVATION CHAIN |

**Column definitions for this scenario:**

- **BASELINE:** connector API call volume at the burst-path source endpoint identified by
  Finding ID in Role 3 (BP-xx), measured at burst onset, before concurrency controls,
  retry policies, or mitigations from Role 8c are applied. This definition names the
  burst-path source endpoint from Role 3 — not a generic prior state.
- **PROTECTED:** sustained throughput achievable at the same burst-path source endpoint
  after the specific mitigation action prescribed in Role 8c for that Finding ID is applied.
- **DERIVATION CHAIN:** step-by-step arithmetic. Conclusions without computation steps
  are SCHEMA 1 CONTENT violations.

Rejection clauses:
- **SCHEMA 1 STRUCTURAL:** missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- **SCHEMA 1 CONTENT:** DERIVATION CHAIN cell has conclusion without computation steps.

---

#### SCHEMA 2 — VOLUME MAPPING

**Applies to:** Role 6 volume-to-behavior mapping table.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

**Column definitions for this scenario:**

- **VOLUME RANGE:** named volume band derived from the threshold in Verdict Claim (a).
  The 5x spike row is required and must show the derivation arithmetic.
- **BASELINE BEHAVIOR:** system behavior at this volume for the burst-path source endpoint
  from Role 3, without mitigation.
- **PROTECTED BEHAVIOR:** system behavior at this volume for the same endpoint, with Role 8c
  mitigation active.
- **Delta:** quantified improvement — numeric or percentage. Generic labels without
  quantified values are SCHEMA 2 CONTENT violations.

Rejection clauses:
- **SCHEMA 2 STRUCTURAL:** missing VOLUME RANGE, BASELINE BEHAVIOR, PROTECTED BEHAVIOR,
  or Delta header.
- **SCHEMA 2 CONTENT:** Delta cell states relative improvement without quantified value.

---

#### SCHEMA 3 — MITIGATION RECORD

**Applies to:** Role 8c per-finding mitigation table.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

**Column definitions for this scenario:**

- **FINDING ID:** BP-xx (from Role 3) or RH-xx (from Role 5) that this mitigation targets.
- **BEFORE STATE:** unmitigated behavior for this Finding ID — names the component, volume
  condition, and failure mode. Generic descriptions without component names are SCHEMA 3
  CONTENT violations.
- **AFTER STATE:** mitigated behavior after the named action is applied — names the specific
  action, setting, or value. Generic descriptions without named action are SCHEMA 3 CONTENT
  violations.
- **Addresses:** BP-xx burst path(s) this mitigation covers.

Rejection clauses:
- **SCHEMA 3 STRUCTURAL:** missing FINDING ID, BEFORE STATE, AFTER STATE, or Addresses
  header.
- **SCHEMA 3 CONTENT:** BEFORE STATE or AFTER STATE cell is generic — no component named,
  no action named.

---

**UX TIER BLOCK TEMPLATE** (not a table schema — applies to Role 4 UX blocks):

```
FIELD-A ERROR SIGNAL: [specific connector error code or platform signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific end-user experience]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific actionable recovery step]
```

UX TEMPLATE rejection clauses:
- **STRUCTURAL:** block missing one or more FIELD labels (scan-time detection).
- **CONTENT:** field contains non-answer (blank, "N/A", "varies") requiring read-time
  detection.

---

Unified schema-mismatch clause: any table whose column headers do not match the schema
type declared for its producing role is a FORMAT-SCHEMA MISMATCH violation. At least one
instance of each of SCHEMA 1, SCHEMA 2, and SCHEMA 3 must appear in this document.

**Gate 2→3:** Three schema sections with heading markers present. UX block template declared.
All rejection clauses stated.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ...
2. Name the connector endpoint(s) involved.
3. Describe the trigger condition.
4. Classify STRUCTURAL or INCIDENTAL.
   - STRUCTURAL: burst unavoidable without architectural redesign or data model change.
   - INCIDENTAL: burst removable by changing a setting or flow structure.
   - Note: a higher-tier platform limit is not path-level protection for a connector endpoint.
5. State the redesign requirement (STRUCTURAL) or the specific removable setting (INCIDENTAL).

Record total count B. Burst-path-first ordering: this audit precedes the tier inventory so
that Structural/Incidental classification is committed before tier evidence is available.

**Verdict-currency check:** if the endpoint in Verdict Claim (a) is not the primary burst
source, insert `REVISED — see Role 3` on Claim (a) before this gate is unblocked.

**Gate 3→4:** At least one burst path classified STRUCTURAL. All paths have Finding IDs.
Count B recorded. This gate does not open without at least one STRUCTURAL classification.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers. For each tier:

1. Tier scope: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window.
3. Enforcing layer: connector / platform / both.
4. Affected BP-xx Finding IDs from Role 3.
5. Scope-distinction check: tiers differing only in numeric threshold at the same scope
   level are variants, not structurally distinct tiers.

At least three structurally distinct tiers required.

**Verdict-currency check:** if a tighter tier is found than Claim (a) states, insert
`REVISED — see Role 4` on Claim (a) before this gate is unblocked.

**Gate 4→5:** Three structurally distinct tiers with numeric thresholds. All tiers mapped
to BP-xx Finding IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each throttle tier from Role 4, answer four sub-questions then produce the UX tier block:
- (i) Run history signal when this tier is hit?
- (ii) End-user visible behavior?
- (iii) Visibility level: Silent / Banner / Modal / Blocking?
- (iv) Specific recovery action available?

Write the UX TEMPLATE block per tier. Six-item gate per block:
(a) FIELD-A present and names a specific signal
(b) FIELD-B present and describes a specific user-visible state
(c) FIELD-C present with named visibility level
(d) FIELD-D present with specific actionable recovery step
(e) Tier count equals B from Role 3 — verify against Role 3 directly, not Claim (d)
(f) All four FIELD labels present (STRUCTURAL compliance)

At least two tiers must have distinct FIELD-B descriptions.

**Verdict-currency check:** if new tiers are discovered here, insert `REVISED — see Role 5`
on Claim (d) before this gate is unblocked.

**Gate 5→6:** All B tiers with complete UX blocks. Six-item gate satisfied for each tier.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce a SCHEMA 2 table with at least three volume ranges, including a mandatory 5x spike
row. 5x spike VOLUME RANGE cell must show: "[threshold from Claim (a)] × 5 = [spike volume]
req/[window]". Delta cells must be quantified (numbers, not labels).

**Gate 6→7:** SCHEMA 2 table with three rows including 5x spike. All Delta cells quantified.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce a SCHEMA 1 table. DERIVATION CHAIN must show:
(i) [base] × 5 = [spike]
(ii) [spike] − [threshold] = [overflow]
(iii) [overflow] × [retry factor] = [total pressure]
(iv) [failed] ÷ [total] = [failure rate]

Follow with prose on the compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA 1 table present. DERIVATION CHAIN shows four arithmetic steps.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**8a — CASCADE FAILURE SCENARIO**

SCHEMA 1 table showing: which endpoint hits limit first (BASELINE), what volume is achievable
with circuit-breaker (PROTECTED), causal chain step-by-step in DERIVATION CHAIN. Causal
chain prose: "When [A] hits [threshold] at [volume], [downstream effect] because [mechanism].
This triggers [B] to receive [overflow], hitting its [threshold] limit."

**8b — 5x ARITHMETIC DERIVATION**

For highest-severity burst path: state threshold → derive 5x → derive overflow → derive retry
amplification → derive failure rate. All five steps required.

**8c — PER-FINDING-ID MITIGATIONS**

SCHEMA 3 table with one row per Finding ID (BP-xx and RH-xx). AFTER STATE must name a
specific action with a specific setting or value. Generic prescriptions do not pass.

**Gate 8→9:** SCHEMA 1 in 8a with causal chain. 5x arithmetic in 8b with all five steps.
SCHEMA 3 in 8c with one row per Finding ID, all AFTER STATE cells specific.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R17

(a) After this invariant, no REVISED markers may be inserted into Roles 1–8. Conditions
    discovered in Role 9 that would require REVISED markers are recorded as FNMI-R17
    reconciler findings, not inserted.
(b) Role 9 (Terminal Reconciler) does not insert REVISED markers into any prior role.
(c) Role 9 inserts zero (0) REVISED markers. Insertion count = 0.
(d) Any REVISED marker inserted by Role 9 is a FNMI-R17 VIOLATION, reported as:
    `FNMI-R17: VIOLATION at [reference] — [description]`.
    Absence of violations: `FNMI-R17: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R17 declared. Role 8 deliverables present.
VERIFICATION-ONLY per FNMI-R17.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Scan claims (a)–(d) in Role 1. Confirm inline REVISED markers present for all revised claims,
each with a forward reference to the revising role. Pure verification — no insertion.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Enumerate gated transitions Gate 1→2 through Gate 8→9. Confirm named deliverables present.
Findings: "Gate Audit: N/N gates pass, M gate(s) missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Scan all DERIVATION CHAIN cells in all SCHEMA 1 tables. Flag conclusions without arithmetic.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA 1 CONTENT violation(s)"

**CHECK (d) — UX TEMPLATE STRUCTURAL SCAN**
Scan all UX tier blocks in Role 5 for FIELD-A through FIELD-D. Flag missing labels.
Findings: "UX Template Scan: N tier(s) checked, M STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings]
- Check (b): [findings]
- Check (c): [findings]
- Check (d): [findings]
- FNMI-R17: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-03

**Axis:** Lifecycle emphasis — the Format Contract occupies proportionally more document
space through an explicit role-to-schema assignment table and component-name slot placeholders
in BASELINE/PROTECTED definitions. The slot language ("BASELINE = [connector endpoint
identified as BP-xx primary burst source in Role 3]") guides the executing model toward
scenario-specific naming rather than relying on post-hoc interpretation. Role sequence is
burst-path-first (same as V-01/V-02).

**Hypothesis:** The role-to-schema mapping table makes C-40's per-table-type decomposition
explicitly verifiable: an evaluator can check that each analysis role is assigned a specific
schema type and then verify the role's actual tables match. The slot placeholders in
BASELINE/PROTECTED definitions provide a stronger signal of C-39 compliance than inline prose
because the slot syntax forces the executing model to substitute scenario component names at
declaration time, not defer them.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

Before any analysis:

(a) **Binding constraint:** [connector endpoint name]: [numeric threshold] per [time window].
(b) **Primary gap:** [burst path name or action] — unprotected because [specific reason].
(c) **System status:** SAFE / DEGRADED / FAILING.
(d) **UX commitment:** [N] tiers; all tiers use the complete four-field UX template.

Revision rule: any role that revises a claim inserts `REVISED — see Role N` at its gate
boundary. Terminal reconciler deferral is a revision currency failure.

**Gate 1→2:** Four claims written. No tables or analysis present.

---

### ROLE 2 — FORMAT CONTRACT

This role is the architectural specification for all structured output in this document.
Section (i) assigns each analysis role to a schema type. Section (ii) declares the column
structure and scenario-specific definitions for each schema. Section (iii) declares rejection
clauses and the unified mismatch clause.

---

**(i) Role-to-Schema Assignment**

| Analysis Role | Schema Type | Table(s) Produced |
|---|---|---|
| Role 6 — Volume-to-Behavior Mapping | SCHEMA-V | One volume-to-behavior table |
| Role 7 — Quantified Impact | SCHEMA-A | One impact table at 5x load |
| Role 8a — Cascade Failure | SCHEMA-A | One cascade failure table |
| Role 8c — Mitigations | SCHEMA-M | One mitigation record table |

A table produced by a role that does not match its declared schema type is a
FORMAT-SCHEMA MISMATCH violation, detectable by comparing column headers against the
declarations in section (ii) below.

---

**(ii) Schema Declarations**

**SCHEMA-A — PRIMARY ANALYSIS**

| BASELINE | PROTECTED | DERIVATION CHAIN |

Scenario-specific column definitions:

- **BASELINE:** [the connector endpoint identified as the BP-xx primary burst source in
  Role 3 — its name will be substituted here when Role 3 is executed] call volume,
  measured at burst onset, before any concurrency control, retry policy, or mitigation
  prescribed for that BP-xx in Role 8c is applied. At the time Role 3 produces BP-xx
  Finding IDs, the executing model must substitute the actual connector endpoint name
  into this definition so that BASELINE names the scenario component, not a generic state.
- **PROTECTED:** call volume at the same connector endpoint after the specific mitigation
  named in Role 8c for BP-xx is applied and active. The mitigation name will be substituted
  when Role 8c is executed.
- **DERIVATION CHAIN:** step-by-step arithmetic. Conclusions without computation steps
  are SCHEMA-A CONTENT violations regardless of the correctness of the conclusion.

**SCHEMA-V — VOLUME MAPPING**

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Scenario-specific column definitions:

- **VOLUME RANGE:** a named volume band anchored to the threshold in Verdict Claim (a).
  The band names must be derived from the Claim (a) threshold and expressed as multiples
  or fractions of it. The 5x spike row is required; its volume value must be arithmetically
  derived as [Claim (a) threshold] × 5.
- **BASELINE BEHAVIOR:** system behavior at this volume range for the connector endpoint
  named in Verdict Claim (a), without any throttle mitigation.
- **PROTECTED BEHAVIOR:** system behavior for the same endpoint at this volume, with the
  Role 8c mitigation for BP-01 (or highest-severity burst path) active.
- **Delta:** quantified improvement. At minimum: state the error rate change or queue depth
  change as a percentage or absolute number. "Better" without numbers is a SCHEMA-V CONTENT
  violation.

**SCHEMA-M — MITIGATION RECORD**

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Scenario-specific column definitions:

- **FINDING ID:** the exact Finding ID produced in Role 3 (BP-xx) or Role 5 (RH-xx).
  No Finding ID may appear in this table that was not assigned in Role 3 or Role 5.
- **BEFORE STATE:** behavior for this specific Finding ID — names the connector endpoint
  or action, states the volume condition at which failure occurs, and states the failure
  mode. A cell that says "throttling occurs" without naming the component or condition is
  a SCHEMA-M CONTENT violation.
- **AFTER STATE:** behavior after the specific mitigation is applied — names the Power
  Automate action or connector setting that is changed, the value or parameter used, and
  the resulting behavior. A cell that says "throttling reduced" without naming the action
  is a SCHEMA-M CONTENT violation.
- **Addresses:** BP-xx Finding IDs from Role 3 that are mitigated by this row.

---

**(iii) Rejection Clauses and Unified Mismatch Clause**

| Schema | Violation Type | Detection Method | Rejection Condition |
|---|---|---|---|
| SCHEMA-A | STRUCTURAL | Scan-time (count column headers) | Missing BASELINE, PROTECTED, or DERIVATION CHAIN |
| SCHEMA-A | CONTENT | Read-time (read DERIVATION CHAIN cell) | Conclusion without arithmetic |
| SCHEMA-V | STRUCTURAL | Scan-time | Missing VOLUME RANGE, BASELINE BEHAVIOR, PROTECTED BEHAVIOR, or Delta |
| SCHEMA-V | CONTENT | Read-time (read Delta cell) | Delta cell lacks quantified value |
| SCHEMA-M | STRUCTURAL | Scan-time | Missing FINDING ID, BEFORE STATE, AFTER STATE, or Addresses |
| SCHEMA-M | CONTENT | Read-time (read BEFORE STATE / AFTER STATE) | Generic cell without component or action name |
| UX TEMPLATE | STRUCTURAL | Scan-time (count field labels) | Missing FIELD-A, FIELD-B, FIELD-C, or FIELD-D |
| UX TEMPLATE | CONTENT | Read-time (read field values) | Non-answer: blank, "N/A", "varies", generic instruction |
| Any table | FORMAT-SCHEMA MISMATCH | Scan-time (compare headers to role assignment table) | Headers do not match the schema type assigned in section (i) |

**Gate 2→3:** Role-to-schema assignment table present. All three table schemas declared with
scenario-anchored column definitions. Rejection clause table present.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Finding ID: BP-01, BP-02, ... (complete the component name substitution for SCHEMA-A's
   BASELINE definition — identify the actual connector endpoint name that anchors BASELINE).
2. Connector endpoint(s) involved.
3. Trigger condition.
4. STRUCTURAL or INCIDENTAL classification with justification.
   - STRUCTURAL: unavoidable without redesign. Higher-tier limits are not path-level
     protection.
   - INCIDENTAL: removable by changing a specific setting or flow structure.
5. For STRUCTURAL: state the architectural requirement that makes it unavoidable.
6. For INCIDENTAL: state the specific setting or change that eliminates the burst.

Count B = total burst paths identified.

**Verdict-currency check:** if Claim (a)'s endpoint is not the primary burst source, insert
`REVISED — see Role 3` on Claim (a) before this gate is unblocked.

**Gate 3→4:** At least one STRUCTURAL classification produced. All Finding IDs assigned.
Count B recorded. Connector endpoint name available for substitution into SCHEMA-A BASELINE
definition.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers. For each:

1. Scope level: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window (must match or supersede Claim (a)'s threshold).
3. Enforcing layer: connector / platform / both.
4. Affected BP-xx Finding IDs.
5. Scope-distinction check: tiers with different numbers but the same scope and enforcing
   layer are variants, not structurally distinct tiers.

Minimum: three structurally distinct tiers.

**Verdict-currency check:** if a tighter tier is found, insert `REVISED — see Role 4` on
Claim (a).

**Gate 4→5:** Three structurally distinct tiers identified with numeric thresholds.
All mapped to BP-xx Finding IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier from Role 4, answer:
(i) Run history signal? (ii) End-user behavior? (iii) Visibility: Silent / Banner / Modal /
Blocking? (iv) Recovery action?

Write UX TEMPLATE block per tier. Six-item gate:
(a) FIELD-A specific signal
(b) FIELD-B specific user-visible state
(c) FIELD-C named visibility level
(d) FIELD-D specific recovery step
(e) Tier count = B from Role 3 (not from Claim (d))
(f) All four FIELD labels present

At least two tiers with distinct FIELD-B descriptions.

**Verdict-currency check:** if new tiers discovered, insert `REVISED — see Role 5` on
Claim (d).

**Gate 5→6:** All B tiers with complete UX blocks. Six-item gate satisfied for each tier.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING (SCHEMA-V)

Produce a SCHEMA-V table (assigned in Role 2, section (i)). At least three rows including
mandatory 5x spike row. 5x spike VOLUME RANGE cell must show: "[threshold] × 5 = [value]
req/[window]". Delta cells must be quantified.

**Gate 6→7:** SCHEMA-V table present with three rows. 5x spike row present with derived
value. All Delta cells quantified.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE (SCHEMA-A)

Produce a SCHEMA-A table (assigned in Role 2, section (i)). DERIVATION CHAIN must show:
(i) base × 5 = spike; (ii) spike − threshold = overflow; (iii) overflow × retry factor =
total pressure; (iv) failed ÷ total = failure rate. Follow with compounding prose at T+30s
and T+60s.

**Gate 7→8:** SCHEMA-A table present. DERIVATION CHAIN shows four arithmetic steps. Prose
present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**8a — CASCADE FAILURE (SCHEMA-A):** table showing which endpoint hits limit first,
downstream causal chain in DERIVATION CHAIN, and volume achievable with circuit-breaker
(PROTECTED). Causal chain prose required: names endpoint A, threshold, triggered downstream
effect, endpoint B overflow volume.

**8b — 5x ARITHMETIC DERIVATION:** threshold → ×5 = spike → overflow → ×retry = pressure
→ ÷total = failure rate. Five steps required; no assertion without derivation.

**8c — MITIGATIONS (SCHEMA-M, as assigned in Role 2, section (i)):** one row per Finding ID
(BP-xx and RH-xx). AFTER STATE must name specific Power Automate action, setting, and value.
"Add retry logic" does not pass. "Set Retry Policy to Exponential, 4 retries, base interval
20 seconds" passes.

**Gate 8→9:** SCHEMA-A in 8a with causal chain. Five-step arithmetic in 8b. SCHEMA-M in 8c
with one row per Finding ID, all AFTER STATE cells specific.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R17

(a) After this invariant: no REVISED markers inserted into Roles 1–8. Conditions requiring
    markers are FNMI-R17 reconciler findings, not insertions.
(b) Role 9 does not insert REVISED markers into any prior role.
(c) Role 9 REVISED marker insertion count = 0.
(d) Any Role 9 REVISED marker insertion = FNMI-R17 VIOLATION.
    Report: `FNMI-R17: VIOLATION at [reference] — [description]`.
    No violations: `FNMI-R17: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R17 declared. All Role 8 schema-assigned tables present.
VERIFICATION-ONLY per FNMI-R17.

**CHECK (a):** Verdict revision marker audit — scan claims (a)–(d), confirm REVISED markers
for all revisions, each with forward reference. No insertion.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit — enumerate Gate 1→2 through Gate 8→9, confirm
named deliverables present.
Findings: "Gate Audit: N/N gates pass, M missing: [list]"

**CHECK (c):** Derivation chain audit — scan all DERIVATION CHAIN cells in SCHEMA-A tables
(Roles 7 and 8a), flag conclusions without arithmetic.
Findings: "Derivation Chain Audit: N cells checked, M CONTENT violation(s)"

**CHECK (d):** UX template structural scan — scan all UX tier blocks in Role 5, flag missing
FIELD labels.
Findings: "UX Template Scan: N tiers checked, M STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings]
- Check (b): [findings]
- Check (c): [findings]
- Check (d): [findings]
- FNMI-R17: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-04

**Axis:** Role sequence + output format (combination of V-01 and V-02) — burst-path-first
role ordering combined with the named subsection heading structure for the three-schema
Format Contract. Each schema is a headed subsection (### SCHEMA 1, ### SCHEMA 2,
### SCHEMA 3) AND the role sequence uses burst-path-first ordering with the Structural-gap
prerequisite gate.

**Hypothesis:** The burst-path-first ordering ensures Structural/Incidental classification
is committed before tier evidence is available (closing the alibi escape), while the
subsection-headed schema presentation makes C-40's three-schema decomposition both
scan-time verifiable (heading detection) and content-verifiable (column structure per
heading). These two structural properties are independent — either alone satisfies its
respective criterion, but their combination produces a document where classification
integrity and schema compliance are both auditable at the structural level without
requiring full content reads.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

Before any analysis:

(a) **Binding constraint:** connector endpoint name and numeric threshold.
(b) **Primary gap:** specific burst path or action — name it, not the category.
(c) **System status:** SAFE / DEGRADED / FAILING.
(d) **UX commitment:** N tiers; all tiers use the complete four-field UX template.

Self-containment: reader of only this block knows core finding and UX scope.

Revision rule: revising roles insert `REVISED — see Role N` at their gate boundary.

**Gate 1→2:** Four claims written. No analysis yet.

---

### ROLE 2 — FORMAT CONTRACT

Three table schemas and one block template govern all structured output. Each schema is
declared as a separate headed section. Every analysis role's tables must match the schema
type declared below for that role's table type.

---

#### SCHEMA 1 — PRIMARY ANALYSIS

*Applies to: Role 7 quantified impact table; Role 8a cascade failure table.*

| BASELINE | PROTECTED | DERIVATION CHAIN |

- **BASELINE:** connector API call volume at the burst-path source endpoint identified by
  Finding ID in Role 3 (BP-xx), at burst onset, before concurrency controls or mitigations
  from Role 8c are applied. This names the Role 3 burst-path source — not a generic state.
- **PROTECTED:** sustained throughput at the same endpoint after the specific mitigation
  for that BP-xx Finding ID (from Role 8c) is applied.
- **DERIVATION CHAIN:** step-by-step arithmetic. Conclusions without computation steps are
  SCHEMA 1 CONTENT violations.

Rejection clauses:
- **SCHEMA 1 STRUCTURAL:** missing BASELINE, PROTECTED, or DERIVATION CHAIN. Scan-time.
- **SCHEMA 1 CONTENT:** DERIVATION CHAIN cell has conclusion without arithmetic. Read-time.

---

#### SCHEMA 2 — VOLUME MAPPING

*Applies to: Role 6 volume-to-behavior mapping table.*

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- **VOLUME RANGE:** named band derived from threshold in Verdict Claim (a). 5x spike row
  required; must show "[threshold] × 5 = [spike volume]" derivation.
- **BASELINE BEHAVIOR:** system behavior at this volume for the burst-path source endpoint
  identified in Role 3, without mitigation.
- **PROTECTED BEHAVIOR:** system behavior at this volume for the same endpoint, with Role 8c
  mitigation active.
- **Delta:** quantified improvement — numbers required. Generic labels are SCHEMA 2 CONTENT
  violations.

Rejection clauses:
- **SCHEMA 2 STRUCTURAL:** missing VOLUME RANGE, BASELINE BEHAVIOR, PROTECTED BEHAVIOR, or
  Delta. Scan-time.
- **SCHEMA 2 CONTENT:** Delta cell lacks quantified value. Read-time.

---

#### SCHEMA 3 — MITIGATION RECORD

*Applies to: Role 8c per-finding mitigation table.*

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- **FINDING ID:** BP-xx (Role 3) or RH-xx (Role 5) — must match an assigned Finding ID.
- **BEFORE STATE:** unmitigated behavior for this Finding ID — names the component, volume
  condition, and failure mode. Generic descriptions are SCHEMA 3 CONTENT violations.
- **AFTER STATE:** mitigated behavior after the named action — names the specific Power
  Automate action, setting, and value. Generic descriptions are SCHEMA 3 CONTENT violations.
- **Addresses:** BP-xx burst paths this mitigation covers.

Rejection clauses:
- **SCHEMA 3 STRUCTURAL:** missing FINDING ID, BEFORE STATE, AFTER STATE, or Addresses.
  Scan-time.
- **SCHEMA 3 CONTENT:** BEFORE STATE or AFTER STATE generic (no component, no action).
  Read-time.

---

**UX TIER BLOCK TEMPLATE** *(applies to Role 5 UX blocks — block format, not a table)*:

```
FIELD-A ERROR SIGNAL: [specific connector error code or platform signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific end-user experience description]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific actionable recovery step]
```

UX TEMPLATE rejection clauses:
- **STRUCTURAL:** missing FIELD-A through FIELD-D labels. Scan-time.
- **CONTENT:** non-answer in any field (blank, "N/A", "varies"). Read-time.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching the schema type declared for
its producing role (as specified in the Applies-to line above each schema section) is a
FORMAT-SCHEMA MISMATCH violation, detectable by comparing column headers against the section
headings above. At least one instance of each schema must appear in the document.

**Gate 2→3:** Three schema sections with heading markers. UX block template. All rejection
clauses stated. No analysis yet.

---

### ROLE 3 — BURST PATH AUDIT

For each burst path:
1. Finding ID: BP-01, BP-02, ...
2. Connector endpoint(s) involved.
3. Trigger condition that causes the burst.
4. STRUCTURAL or INCIDENTAL classification.
   - STRUCTURAL: unavoidable without architectural redesign. Higher-tier platform limits
     are not path-level protection for the connector endpoint.
   - INCIDENTAL: removable by changing a specific setting or flow structure.
5. Justification for classification.

Total count = B.

Burst-path-first ordering: classification committed before Role 4's tier inventory opens.

**Verdict-currency check:** if Claim (a)'s endpoint is not the primary burst source, insert
`REVISED — see Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL classification committed. All Finding IDs assigned.
Count B recorded. This gate does not open without at least one STRUCTURAL burst path.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

For each tier:
1. Scope: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window.
3. Enforcing layer: connector / platform / both.
4. Affected BP-xx Finding IDs from Role 3.
5. Scope-distinction: different thresholds at the same scope level are variants.

Minimum three structurally distinct tiers.

**Verdict-currency check:** if a tighter tier found, insert `REVISED — see Role 4` on
Claim (a).

**Gate 4→5:** Three structurally distinct tiers with numeric thresholds, all mapped to
BP-xx Finding IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier from Role 4, four sub-questions:
(i) Run history signal? (ii) End-user behavior? (iii) Visibility level? (iv) Recovery action?

Write UX TEMPLATE block per tier. Six-item gate:
(a) FIELD-A specific signal
(b) FIELD-B specific user-visible state
(c) FIELD-C named visibility level
(d) FIELD-D specific recovery step
(e) Tier count = B from Role 3 (not Claim (d))
(f) All four FIELD labels present

At least two tiers with distinct FIELD-B.

**Verdict-currency check:** if new tiers, insert `REVISED — see Role 5` on Claim (d).

**Gate 5→6:** All B tiers complete. Six-item gate satisfied for each tier.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING (SCHEMA 2)

SCHEMA 2 table. At least three rows. Mandatory 5x spike row with "[threshold] × 5 = [value]"
in VOLUME RANGE cell. All Delta cells quantified.

**Gate 6→7:** SCHEMA 2 present with three rows and 5x spike. All Delta cells quantified.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE (SCHEMA 1)

SCHEMA 1 table. DERIVATION CHAIN: base × 5 = spike; spike − threshold = overflow; overflow
× retry factor = total pressure; failed ÷ total = failure rate. Four steps required.
Compounding prose at T+30s and T+60s.

**Gate 7→8:** SCHEMA 1 present. Four-step DERIVATION CHAIN. Compounding prose.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**8a (SCHEMA 1):** cascade failure table — BASELINE at first-hit endpoint, PROTECTED with
circuit-breaker, DERIVATION CHAIN with step-by-step causal chain. Causal chain prose
required: names endpoint A, threshold, mechanism, triggered downstream effect, endpoint B
overflow.

**8b:** 5x arithmetic — state threshold, derive ×5, derive overflow, derive retry pressure,
derive failure rate. Five steps; no assertions without derivation.

**8c (SCHEMA 3):** mitigation record — one row per BP-xx and RH-xx Finding ID. AFTER STATE
must name specific action, setting, and value. Generic prescriptions do not pass.

**Gate 8→9:** SCHEMA 1 in 8a with causal chain. Five-step arithmetic in 8b. SCHEMA 3 in 8c
with one row per Finding ID, all AFTER STATE cells specific.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R17

(a) After this invariant: no REVISED markers may be inserted into Roles 1–8.
(b) Role 9 does not insert REVISED markers.
(c) Role 9 REVISED marker insertion count = 0.
(d) Any Role 9 insertion = FNMI-R17 VIOLATION.
    Report: `FNMI-R17: VIOLATION at [reference] — [description]` or `FNMI-R17: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R17 declared. All schema-assigned deliverables present.
VERIFICATION-ONLY per FNMI-R17.

**CHECK (a):** Verdict revision marker audit — scan claims (a)–(d), confirm REVISED markers
with forward references for all revisions. No insertion.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit — Gate 1→2 through Gate 8→9, confirm named deliverables.
Findings: "Gate Audit: N/N gates pass, M missing"

**CHECK (c):** Derivation chain audit — all DERIVATION CHAIN cells in SCHEMA 1 tables
(Roles 7 and 8a), flag conclusions without arithmetic.
Findings: "Derivation Chain Audit: N cells checked, M CONTENT violation(s)"

**CHECK (d):** UX template structural scan — all Role 5 UX blocks, flag missing FIELD labels.
Findings: "UX Template Scan: N tiers checked, M STRUCTURAL violation(s)"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings]
- Check (b): [findings]
- Check (c): [findings]
- Check (d): [findings]
- FNMI-R17: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-05

**Axis:** Full integration — combines all three axes (burst-path-first role sequence from
V-01, subsection-headed schema declarations from V-02, expanded role-to-schema mapping from
V-03) and adds a new CHECK (e) in the Terminal Reconciler: SCHEMA-TYPE COMPLIANCE AUDIT,
which verifies that each analysis role's tables use the schema type declared for that role
in the Format Contract's role-to-schema assignment. CHECK (e) is FNMI-R17 scoped —
verification only, no table modification.

**Hypothesis:** Full integration produces end-to-end Format Contract enforcement: C-40's
three-schema decomposition is declared (Format Contract), assigned per role (role-to-schema
table), enforced at each role's gate (schema-type reminder in gate condition), and audited
at document close (CHECK (e) in reconciler). C-39's scenario-anchored definitions propagate
from the Format Contract through each role's table production instructions. CHECK (e)
creates a closed compliance chain for C-40 analogous to how CHECK (a) creates a closed chain
for Verdict revision currency.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

Before any analysis:

(a) **Binding constraint:** connector endpoint name and numeric threshold.
(b) **Primary gap:** specific burst path or action — name the component, not the category.
(c) **System status:** SAFE / DEGRADED / FAILING.
(d) **UX commitment:** N tiers described; all use the four-field UX template (FIELD-A
    through FIELD-D).

Self-containment: reader of only this block knows core finding and UX coverage scope.

Revision rule: revising roles insert `REVISED — see Role N` at their gate boundary.
Deferral to terminal reconciler is a revision currency violation.

**Gate 1→2:** Four claims written. No analysis, tables, or lists have appeared.

---

### ROLE 2 — FORMAT CONTRACT

This role is the structural specification for all tables and blocks in this document.
It contains three sections: (i) role-to-schema assignment, (ii) per-schema declarations
with scenario-anchored column definitions, (iii) rejection clause index and unified
mismatch clause.

---

#### (i) Role-to-Schema Assignment

| Analysis Role | Schema Type | Table Produced |
|---|---|---|
| Role 6 — Volume-to-Behavior Mapping | SCHEMA 2 (VOLUME MAPPING) | Volume-to-behavior table |
| Role 7 — Quantified Impact | SCHEMA 1 (PRIMARY ANALYSIS) | Quantified impact table |
| Role 8a — Cascade Failure | SCHEMA 1 (PRIMARY ANALYSIS) | Cascade failure table |
| Role 8c — Mitigations | SCHEMA 3 (MITIGATION RECORD) | Mitigation record table |

CHECK (e) in the Terminal Reconciler (Role 9) will audit that each table in the rows above
uses the schema type assigned in this table. FORMAT-SCHEMA MISMATCH violations are
detectable at scan time by comparing column headers against the schema declarations below.

---

#### (ii) Per-Schema Declarations

---

#### SCHEMA 1 — PRIMARY ANALYSIS

*For: Role 7 quantified impact; Role 8a cascade failure.*

| BASELINE | PROTECTED | DERIVATION CHAIN |

Scenario-anchored definitions:

- **BASELINE:** connector API call volume at the burst-path source endpoint assigned
  Finding ID BP-xx in Role 3, measured at burst onset, before any concurrency control,
  retry policy, or mitigation prescribed in Role 8c for that BP-xx is applied.
  This definition names the Role 3 burst-path source endpoint — not a generic "before"
  state. When Role 3 produces BP-xx Finding IDs, substitute the actual endpoint name.
- **PROTECTED:** sustained call throughput at the same burst-path source endpoint after
  the specific mitigation action named in Role 8c for BP-xx is applied and active.
  Substitute the actual mitigation action name when Role 8c produces it.
- **DERIVATION CHAIN:** complete step-by-step arithmetic. Conclusions without computation
  steps are SCHEMA 1 CONTENT violations.

---

#### SCHEMA 2 — VOLUME MAPPING

*For: Role 6 volume-to-behavior mapping.*

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Scenario-anchored definitions:

- **VOLUME RANGE:** named band anchored to the threshold in Verdict Claim (a). Each band
  name must include a derivation from Claim (a)'s threshold (e.g., "0.5× threshold",
  "at threshold", "5× threshold"). 5x spike row is required.
- **BASELINE BEHAVIOR:** system behavior at this volume range for the connector endpoint
  named in Verdict Claim (a) and identified as the primary burst source in Role 3,
  without throttle mitigation.
- **PROTECTED BEHAVIOR:** system behavior at this volume range for the same endpoint, with
  the Role 8c mitigation for BP-01 (highest-severity burst path) active.
- **Delta:** quantified — numbers required. Generic labels without numbers are SCHEMA 2
  CONTENT violations.

---

#### SCHEMA 3 — MITIGATION RECORD

*For: Role 8c per-finding mitigations.*

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Scenario-anchored definitions:

- **FINDING ID:** the Finding ID assigned in Role 3 (BP-xx) or Role 5 (RH-xx). No
  Finding IDs may appear here that were not assigned in Role 3 or Role 5.
- **BEFORE STATE:** unmitigated behavior for this Finding ID — names the connector
  endpoint or action, the volume condition at which it fails, and the failure mode.
  Generic cells without component names are SCHEMA 3 CONTENT violations.
- **AFTER STATE:** mitigated behavior after the named action — names the Power Automate
  action or connector setting, the parameter value applied, and the resulting behavior.
  Generic cells without named action and value are SCHEMA 3 CONTENT violations.
- **Addresses:** BP-xx burst paths from Role 3 covered by this row.

---

#### (iii) Rejection Clause Index and Unified Mismatch Clause

| ID | Schema | Violation | Detection | Trigger |
|---|---|---|---|---|
| R1 | SCHEMA 1 | STRUCTURAL | Scan-time | Missing column header |
| R2 | SCHEMA 1 | CONTENT | Read-time | Bare conclusion in DERIVATION CHAIN |
| R3 | SCHEMA 2 | STRUCTURAL | Scan-time | Missing column header |
| R4 | SCHEMA 2 | CONTENT | Read-time | Delta without quantified value |
| R5 | SCHEMA 3 | STRUCTURAL | Scan-time | Missing column header |
| R6 | SCHEMA 3 | CONTENT | Read-time | Generic BEFORE/AFTER STATE |
| R7 | UX TEMPLATE | STRUCTURAL | Scan-time | Missing FIELD label |
| R8 | UX TEMPLATE | CONTENT | Read-time | Non-answer in field |
| R9 | Any table | FORMAT-SCHEMA MISMATCH | Scan-time | Column headers don't match role assignment |

Unified clause: any table not matching the schema type assigned in section (i) for its
producing role is a FORMAT-SCHEMA MISMATCH (violation R9). The Terminal Reconciler's
CHECK (e) audits all four assigned tables against section (i).

At least one instance of each of SCHEMA 1, SCHEMA 2, and SCHEMA 3 must appear in this
document. Missing schema instances are FORMAT-SCHEMA MISMATCH gaps in section (i)'s
coverage.

**Gate 2→3:** Role-to-schema assignment table present. Three schema sections with heading
markers and scenario-anchored definitions. Rejection clause index present. No analysis yet.

---

### ROLE 3 — BURST PATH AUDIT

For each burst path:
1. Finding ID: BP-01, BP-02, ... (note: these IDs anchor SCHEMA 1's BASELINE definition
   — the endpoint identified here becomes the scenario-specific BASELINE component).
2. Connector endpoint(s) involved.
3. Trigger condition.
4. STRUCTURAL or INCIDENTAL classification with justification.
   - STRUCTURAL: burst unavoidable without redesign or data model change. Higher-tier
     platform limits are not path-level protection for connector endpoints.
   - INCIDENTAL: burst removable by a specific setting change or flow restructure.
5. For STRUCTURAL: state the architectural constraint.
6. For INCIDENTAL: state the specific removable setting or structural change.

Total count B.

**Verdict-currency check:** if Claim (a)'s endpoint is not the primary burst source, insert
`REVISED — see Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL classification committed. All Finding IDs assigned.
Count B recorded. This gate does not open without at least one STRUCTURAL burst path.
Burst-path-first: this commitment precedes Role 4's tier evidence.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

For each tier:
1. Scope: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window.
3. Enforcing layer: connector / platform / both.
4. Affected BP-xx Finding IDs.
5. Scope-distinction check: same scope + same enforcer + different threshold = variants.

Minimum: three structurally distinct tiers.

**Verdict-currency check:** if a tighter tier found, insert `REVISED — see Role 4` on
Claim (a).

**Gate 4→5:** Three structurally distinct tiers. All mapped to BP-xx Finding IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier from Role 4:
Sub-questions: (i) run history signal? (ii) end-user behavior? (iii) visibility level?
(iv) recovery action?

UX TEMPLATE block per tier. Six-item gate:
(a) FIELD-A specific signal
(b) FIELD-B specific user-visible state
(c) FIELD-C named visibility level
(d) FIELD-D specific recovery step
(e) Tier count = B from Role 3 (not Claim (d))
(f) All four FIELD labels present (STRUCTURAL compliance)

At least two tiers with distinct FIELD-B.

**Verdict-currency check:** if new tiers, insert `REVISED — see Role 5` on Claim (d).

**Gate 5→6:** All B tiers complete. Six-item gate satisfied for each tier.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING (SCHEMA 2, per Role 2 section (i))

Produce a SCHEMA 2 table. At least three rows including mandatory 5x spike. 5x spike
VOLUME RANGE cell: "[threshold from Claim (a)] × 5 = [spike value] req/[window]". All
Delta cells quantified with numbers.

**Gate 6→7:** SCHEMA 2 table present. Three rows with 5x spike. All Delta cells quantified.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE (SCHEMA 1, per Role 2 section (i))

Produce a SCHEMA 1 table. DERIVATION CHAIN four steps:
(i) base × 5 = spike; (ii) spike − threshold = overflow;
(iii) overflow × retry factor = total pressure; (iv) failed ÷ total = failure rate.

Follow with compounding prose at T+30s and T+60s.

**Gate 7→8:** SCHEMA 1 table present. Four arithmetic steps in DERIVATION CHAIN. Prose
present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**8a — CASCADE FAILURE (SCHEMA 1, per Role 2 section (i)):**
SCHEMA 1 table. BASELINE at first-hit endpoint at threshold onset. PROTECTED with
circuit-breaker active. DERIVATION CHAIN shows step-by-step causal chain: endpoint A hits
threshold → downstream calls blocked or amplified → endpoint B receives overflow → endpoint B
threshold hit. Causal chain prose required naming all three: endpoint A, mechanism, endpoint B.

**8b — 5x ARITHMETIC DERIVATION:**
Five steps: threshold → ×5 → overflow → retry pressure → failure rate. Show each arithmetic
step. No assertions without derivation.

**8c — MITIGATIONS (SCHEMA 3, per Role 2 section (i)):**
SCHEMA 3 table. One row per BP-xx and RH-xx Finding ID. AFTER STATE must name: the specific
Power Automate action or connector setting, the parameter value, and the resulting behavior.
These do not pass: "add retry logic", "enable throttle protection". These pass: "set
Retry Policy to Exponential with 4 retries and 20-second base interval on the HTTP action
at BP-01's burst source; retry pressure at overflow = 500 × (1 + 4) = 2,500 max attempts,
reduced to 500 ÷ 4 = 125 per window with exponential spacing."

**Gate 8→9:** SCHEMA 1 in 8a with step-by-step causal chain. Five arithmetic steps in 8b.
SCHEMA 3 in 8c with one row per Finding ID, all AFTER STATE cells specific with named
action and value.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R17

(a) After this invariant: no REVISED markers may be inserted into Roles 1–8. Conditions
    requiring markers are recorded as FNMI-R17 reconciler findings, not inserted.
(b) Role 9 does not insert REVISED markers into any prior role.
(c) Role 9 REVISED marker insertion count = 0.
(d) Any REVISED marker inserted by Role 9 = FNMI-R17 VIOLATION.
    `FNMI-R17: VIOLATION at [reference] — [description]` or `FNMI-R17: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R17 declared. All four role-assigned schema tables present (per Role 2,
section (i)).
VERIFICATION-ONLY per FNMI-R17. Five checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Scan claims (a)–(d) in Role 1. For each claim, confirm inline REVISED markers present for
all revisions, each with forward reference to revising role. No insertion.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Enumerate Gate 1→2 through Gate 8→9. Confirm named deliverables present for each gate.
Findings: "Gate Audit: N/N gates pass, M missing: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Scan every DERIVATION CHAIN cell in all SCHEMA 1 tables (Roles 7 and 8a). Flag conclusions
without computation steps (violation R2).
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA 1 CONTENT violation(s)"

**CHECK (d) — UX TEMPLATE STRUCTURAL SCAN**
Scan all UX tier blocks in Role 5 for FIELD-A through FIELD-D labels (violation R7).
Findings: "UX Template Scan: N tiers checked, M STRUCTURAL violation(s)"

**CHECK (e) — SCHEMA-TYPE COMPLIANCE AUDIT**
For each row in Role 2's role-to-schema assignment table (section (i)), verify that the
producing role's actual table uses the column headers declared for the assigned schema type.

| Assigned Table | Expected Schema | Column Headers Expected | Compliant? |
|---|---|---|---|
| Role 6 volume-to-behavior | SCHEMA 2 | VOLUME RANGE, BASELINE BEHAVIOR, PROTECTED BEHAVIOR, Delta | [Y/N] |
| Role 7 quantified impact | SCHEMA 1 | BASELINE, PROTECTED, DERIVATION CHAIN | [Y/N] |
| Role 8a cascade failure | SCHEMA 1 | BASELINE, PROTECTED, DERIVATION CHAIN | [Y/N] |
| Role 8c mitigation record | SCHEMA 3 | FINDING ID, BEFORE STATE, AFTER STATE, Addresses | [Y/N] |

Any row with Compliant? = N is a FORMAT-SCHEMA MISMATCH (violation R9). This check is
VERIFICATION-ONLY — no tables are modified.
Findings: "Schema-Type Audit: N/4 tables compliant, M FORMAT-SCHEMA MISMATCH violation(s):
[list any non-compliant role and the column discrepancy]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings]
- Check (b): [findings]
- Check (c): [findings]
- Check (d): [findings]
- Check (e): [findings]
- FNMI-R17: COMPLIANT / VIOLATION at [reference] — [description]
