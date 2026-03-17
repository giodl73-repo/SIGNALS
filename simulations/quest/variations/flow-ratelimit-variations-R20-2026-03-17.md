`simulations/quest/variations/flow-ratelimit-variations-R20-2026-03-17.md` written.

---

## flow-ratelimit — Variate R20 Summary

**Target criteria:** C-46, C-47, C-48

**Variation axes:**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-46 (merge prohibition) | seed: CHECK names "missing or invalid prefix" as prohibited merged form | none | none | Plane 2 of two-plane CHECK | Plane 3 e.5–e.6 |
| C-47 (orphaned schema) | none | seed: ORPHANED SCHEMA as symmetric independent class | none | Plane 1 of two-plane CHECK | Plane 1 e.1–e.3 |
| C-48 (named rejection clause) | none | none | seed: SCHEMA-A BASELINE SOURCE VIOLATION in Format Contract | none | SCHEMA-A rejection clauses |
| CHECK (e) structure | single-plane + merge prohibition | two-class registry | bidirectionality audit | two-plane | three-plane |
| Predicted C-46 | PASS | FAIL | FAIL | PASS | PASS |
| Predicted C-47 | FAIL | PASS | FAIL | PASS | PASS |
| Predicted C-48 | FAIL | FAIL | PASS | FAIL | PASS |

**What each variation introduces:**

- **V-01** — Single-axis C-46. Takes R19 V-01's CELL ANCHOR pattern (two violation classes already distinguished) and adds one sentence to CHECK (e) e.3: *"The prohibited merged form is 'missing or invalid prefix' — any findings report using this phrase in a single category does not satisfy the violation-class distinction requirement."* No registry. No BURST PATH TABLE.

- **V-02** — Single-axis C-47. Takes R19 V-02's Schema Production Registry with REGISTRY GAP. Extends CHECK (e) Plane 1 to make ORPHANED SCHEMA an explicitly named, logically independent symmetric class: *"REGISTRY GAP = undercounting (producing role without entry); ORPHANED SCHEMA = misalignment (body entry without entry). Both must appear under separate named labels."* No cell anchor. No BURST PATH TABLE.

- **V-03** — Single-axis C-48. Takes R19 V-03's BURST PATH TABLE. Adds SCHEMA-A BASELINE SOURCE VIOLATION as a labeled rejection clause in the Format Contract's SCHEMA-A entry — not just in CHECK — with the condition and the C-41-vs-C-45 distinction stated inline. No registry. No cell anchor.

- **V-04** — C-46 + C-47 combined. Registry + cell anchor. Two-plane CHECK (e): Plane 1 enforces REGISTRY GAP / ORPHANED SCHEMA independence (C-47), Plane 2 enforces CELL ANCHOR / UNRESOLVED REFERENCE separation with the merge prohibition named (C-46). No BURST PATH TABLE.

- **V-05** — Full integration. All three: registry + BURST PATH TABLE + cell anchor. Format Contract SCHEMA-A carries all five rejection clauses including SCHEMA-A BASELINE SOURCE VIOLATION (C-48). Three-plane CHECK (e): Plane 1 (C-47), Plane 2 (C-48), Plane 3 (C-46). Predicted score: 40/40 aspirational → 120/120.
itable obligation in the Format Contract itself: a non-compliant cell can be flagged
by violation class name without requiring knowledge of which round introduced the routing
requirement. Requires C-45.

**R20 variation axes:**

| | V-01 | V-02 | V-03 | V-04 | V-05 |
|---|---|---|---|---|---|
| C-46 (merge prohibition) | seed: CHECK names "missing or invalid prefix" as prohibited merged form | none | none | CHECK Plane 2 names prohibited merged form | Plane 3 e.5–e.6 with merge prohibition label |
| C-47 (orphaned schema) | none | seed: ORPHANED SCHEMA as symmetric class to REGISTRY GAP, logically independent, separately audited | none | CHECK Plane 1 names both classes as logically independent | Plane 1 e.1–e.3 with independent class audit |
| C-48 (named rejection clause) | none | none | seed: SCHEMA-A BASELINE SOURCE VIOLATION as named rejection clause in Format Contract | none | Format Contract SCHEMA-A carries named rejection clause |
| Role 9 CHECK (e) | single-plane cell audit + merge prohibition | two-class registry audit with orphaned schema | bidirectionality audit | two-plane: registry + cell anchor, each with new class | three-plane: registry + BURST PATH TABLE + cell anchor |
| Predicted C-46 | PASS | FAIL | FAIL | PASS | PASS |
| Predicted C-47 | FAIL | PASS | FAIL | PASS | PASS |
| Predicted C-48 | FAIL | FAIL | PASS | FAIL | PASS |

---

## V-01

**Axis:** Cell-plane violation merge prohibition — the CHECK (e) cell-anchor audit explicitly
names "missing or invalid prefix" as a prohibited merged violation label and declares it
non-compliant. C-43's two-class distinction (CELL ANCHOR = missing prefix, UNRESOLVED
REFERENCE = present but invalid prefix) is satisfied by enumerating both classes separately.
C-46 adds one more requirement: the CHECK instruction must name the merged form that conflates
them and state it does not satisfy the distinction requirement. This is the only new addition
over R19 V-01. No registry. No BURST PATH TABLE.

**Hypothesis:** A compliance check can enumerate CELL ANCHOR and UNRESOLVED REFERENCE
separately and still allow a summary line reading "N missing or invalid prefix violations
found." The merged phrase re-conflates at the summary level what the enumeration distinguished
at the detail level. Naming "missing or invalid prefix" as a labeled non-compliant form in
the CHECK instruction forecloses this pattern at both the detail and summary levels. The
enforcement is localized to a single sentence in CHECK (e) — making it the minimum viable
addition that closes the C-46 gap without restructuring any other role.

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
    descriptions in this document. Format: "N tiers described; all tiers use the four-field
    UX template (FIELD-A through FIELD-D)."

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
declared here for its table type.

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 8a cascade failure analysis; Role 7 quantified impact at load spike.
Producing role(s): Role 7 (Gate 7→8), Role 8a (Gate 8→9).

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3 (BP-xx), measured at the point of burst onset, before
  any mitigation prescribed in Role 8c is applied. This definition refers to the specific
  connector endpoint and Finding ID produced in Role 3 — not a generic "before" state.
- PROTECTED: the sustained connector API call throughput at the same burst-path source
  endpoint after the specific mitigation action prescribed in Role 8c for that Finding ID
  (BP-xx) is applied and active.
- DERIVATION CHAIN: step-by-step arithmetic tracing the computation. Bare conclusions
  without computation steps are SCHEMA-A CONTENT violations.

**SCHEMA-A CELL ANCHOR requirement:** every data cell in a SCHEMA-A-governed column must
open with a resolved Finding ID prefix in the form "BP-xx: [value]", where BP-xx is the
Finding ID from Role 3 whose output the cell's value was measured from. This requirement
applies to every BASELINE cell, PROTECTED cell, and DERIVATION CHAIN cell in SCHEMA-A tables.

Two violation classes — both must be explicitly distinguished in any compliance check:

- **CELL ANCHOR violation:** a cell is missing the "BP-xx:" prefix entirely. This is a
  format violation detectable at scan time by inspecting the cell's opening characters.
  Cause: the cell's value was written without anchoring it to a prior-role Finding ID.

- **UNRESOLVED REFERENCE violation:** a cell opens with a syntactically valid "BP-xx:"
  prefix, but the named BP-xx Finding ID does not exist in Role 3's output. This violation
  is format-compliant (the prefix is present) but semantically invalid. Detection requires
  cross-referencing the prefix against the Finding ID list in Role 3. A cell reading
  "BP-05: 1,200 req/min" is an UNRESOLVED REFERENCE if Role 3 produced only BP-01 through
  BP-03.

Rejection clauses:
- SCHEMA-A STRUCTURAL: table missing one or more of BASELINE, PROTECTED, DERIVATION CHAIN
  column headers.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains a conclusion without computation steps.
- SCHEMA-A CELL ANCHOR: a cell in any SCHEMA-A column is missing the "BP-xx:" prefix.
- SCHEMA-A UNRESOLVED REFERENCE: a cell's BP-xx prefix names a Finding ID that does not
  exist in Role 3.

---

**SCHEMA-V — VOLUME MAPPING** (volume-to-behavior mapping table)

Applies to: Role 6 volume-to-behavior mapping. Producing role: Role 6 (Gate 6→7).

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Rejection clauses:
- SCHEMA-V STRUCTURAL: table missing one or more declared column headers.
- SCHEMA-V CONTENT: Delta cell states a relative improvement without a quantified value.

---

**SCHEMA-M — MITIGATION RECORD** (per-finding mitigation tables)

Applies to: Role 8c per-finding mitigation prescriptions. Producing role: Role 8c (Gate 8→9).

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Rejection clauses:
- SCHEMA-M STRUCTURAL: table missing one or more declared column headers.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic — no component named,
  no action named, or a non-answer present.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE** (UX per throttle tier)

Applies to: Role 5 UX descriptions per throttle tier. Producing role: Role 5 (Gate 5→6).

```
FIELD-A ERROR SIGNAL: [connector error code or platform signal name — not "error occurs"]
FIELD-B USER-VISIBLE BEHAVIOR: [what the end user sees or experiences — specific]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific action the user or flow can take — not "retry later"]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing one or more of FIELD-A through FIELD-D labels.
- SCHEMA-B CONTENT: a field contains a non-answer.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table in this document whose column structure
does not match the schema type declared for its producing role is a FORMAT-SCHEMA MISMATCH
violation, detectable at scan time.

**Gate 2→3:** All four table schemas and the UX block template declared. All rejection
clauses stated. SCHEMA-A CELL ANCHOR requirement and both violation class definitions
present. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths for the scenario. For each burst path:

1. Assign a Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint(s) involved — use names consistent with Verdict Claim (a).
3. State the trigger condition (what causes the burst).
4. Classify as STRUCTURAL or INCIDENTAL.
   - STRUCTURAL: the burst is unavoidable given the current architecture.
   - INCIDENTAL: removable by changing a setting, adding a control, or restructuring.
   - A higher-tier platform limit is not path-level protection.
5. For STRUCTURAL paths, state why architectural redesign would be required.
6. For INCIDENTAL paths, state the specific setting or structural change that removes it.

Record the total burst path count as B.

If Verdict Claim (a)'s stated endpoint does not appear as the primary burst source among
the identified paths, insert `REVISED — see Role 3` on Claim (a) before this role's gate
is unblocked.

**Gate 3→4:** At least one burst path classified STRUCTURAL. Finding IDs assigned to all
paths. Total count B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Enumerate all rate limit tiers relevant to the scenario. For each tier:

1. Name the tier scope: per-connection / per-user / per-tenant / global / platform.
2. State the numeric threshold and time window.
3. Identify the enforcing layer: connector-enforced / platform-enforced / both.
4. Map to burst path: which BP-xx Finding IDs from Role 3 are affected by this tier.
5. Scope-distinction check: two tiers at the same scope level with different numeric
   thresholds are tier variants, not structurally distinct tiers. Structurally distinct
   tiers must differ in scope level, enforcing layer, or action class constrained.

At least three structurally distinct tiers must be identified. For at least one tier, cite
the concrete numeric threshold with its source. The threshold in Verdict Claim (a) must
appear here.

**Verdict-currency check:** if a tighter tier is found than originally stated, insert
`REVISED — see Role 4` on Claim (a) before this role's gate is unblocked.

**Gate 4→5:** At least three structurally distinct tiers with numeric thresholds and scope.
All tiers mapped to BP-xx Finding IDs from Role 3.

---

### ROLE 5 — UX PER THROTTLE TIER

For each throttle tier identified in Role 4, produce a SCHEMA-B UX block.

For each tier, answer four sub-questions before writing the block:
- (i)   What does the run history show when this tier is hit?
- (ii)  What does the end user see or experience when this tier is hit?
- (iii) How visible is the failure? (Silent / Banner / Modal / Blocking)
- (iv)  What specific recovery action is available to the user or the flow?

Then write the SCHEMA-B block:

```
FIELD-A ERROR SIGNAL: [answer to (i)]
FIELD-B USER-VISIBLE BEHAVIOR: [answer to (ii)]
FIELD-C VISIBILITY LEVEL: [answer to (iii)]
FIELD-D RECOVERY PATH: [answer to (iv)]
```

Gate items per block — all six must be satisfied:
(a) FIELD-A present and names a specific signal.
(b) FIELD-B present and describes a specific user-visible state.
(c) FIELD-C present with one of the four named visibility levels.
(d) FIELD-D present and names a specific actionable recovery step.
(e) Tier count in this role equals B from Role 3 — verify against Role 3 directly.
(f) Every block has all four FIELD labels (SCHEMA-B STRUCTURAL compliance).

At least two tiers must have distinct FIELD-B descriptions.

**Gate 5→6:** All B tiers have complete SCHEMA-B blocks. Six-item gate satisfied for each
tier. At least two tiers with distinct UX descriptions.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce a SCHEMA-V table with at least three volume ranges, including a mandatory 5x spike
row. Derive the spike volume arithmetically from the threshold in Verdict Claim (a). Show
the multiplication in the VOLUME RANGE cell of the 5x row.

Delta cells must state quantified improvements. Generic labels are SCHEMA-V CONTENT
violations.

**Gate 6→7:** SCHEMA-V table with at least three rows including 5x spike. All Delta cells
quantified. 5x spike volume arithmetically derived.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce a SCHEMA-A table showing cascading impact at 5x load.

SCHEMA-A CELL ANCHOR enforcement: every cell in BASELINE, PROTECTED, and DERIVATION CHAIN
columns must open with "BP-xx: [value]" where BP-xx is the Finding ID from Role 3 whose
measurement the cell's value is drawn from. Write the prefix before any numeric value.
Example: "BP-01: 3,000 req/min" not "3,000 req/min".

The table must show:
- BASELINE: "BP-xx: [connector API call volume at burst-path source endpoint at 5x load,
  before mitigation]"
- PROTECTED: "BP-xx: [sustained throughput after Role 8c mitigation applied]"
- DERIVATION CHAIN: "BP-xx: [step-by-step arithmetic: (i) threshold × 5 = spike,
  (ii) spike − threshold = overflow, (iii) overflow × retry factor = total pressure,
  (iv) total pressure ÷ threshold = failure rate]"

Follow with prose describing the compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A table present with BP-xx prefixes on all cells. DERIVATION CHAIN
shows four-step arithmetic. Compounding effect described in prose.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

Construct a SCHEMA-A table for the cascading failure scenario. The second throttle event
must be causally triggered by the first.

SCHEMA-A CELL ANCHOR enforcement: all BASELINE, PROTECTED, and DERIVATION CHAIN cells
must carry "BP-xx: [value]" prefixes. The DERIVATION CHAIN must show the causal chain
step-by-step.

Required causal chain statement (prose): "When [endpoint A] hits its [threshold] limit at
[volume], [downstream effect] because [causal mechanism]. This triggers [endpoint B] to
receive [derived overflow volume], which hits its [threshold] limit."

**ROLE 8b — 5x ARITHMETIC DERIVATION**

For the highest-severity burst path, show: threshold, 5x spike, overflow, retry
amplification, and failure rate. No bare assertions — every percentage has arithmetic.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

Produce a SCHEMA-M table with one row per Finding ID from Role 3 (BP-xx) and Role 5 (RH-xx).

AFTER STATE cell must name specific action, setting, or pattern. Generic descriptions do
not pass.

**Gate 8→9:** SCHEMA-A table in 8a with BP-xx prefixes and causal chain in DERIVATION CHAIN.
5x arithmetic in 8b shows all five steps. SCHEMA-M table in 8c has one row per Finding ID
with specific AFTER STATE descriptions.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R20

This invariant is named FNMI-R20 and governs the Terminal Reconciler (Role 9) that follows.

(a) After this invariant is declared, no REVISED markers may be inserted into Roles 1–8.
    A condition discovered during Role 9 that would in forward execution require a REVISED
    marker is recorded as a named FNMI-R20 reconciler finding — the marker is not inserted.
(b) The Terminal Reconciler (Role 9) does not insert REVISED markers into any section
    authored during Roles 1–8.
(c) The Terminal Reconciler inserts zero (0) REVISED markers. Insertion count = 0.
(d) Any REVISED marker insertion by Role 9 is a FNMI-R20 VIOLATION. Named as:
    `FNMI-R20: VIOLATION at [Finding ID or Claim reference] — [description]`.
    Absence of violations: `FNMI-R20: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R20 declared. Role 8 deliverables present.

This role is VERIFICATION-ONLY per FNMI-R20. Perform five checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**

Scan Verdict Block claims (a)–(d). Confirm inline REVISED markers are present for every
revised claim, each with a forward reference to the revising role.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**

Enumerate each gated transition (Gate 1→2 through Gate 8→9). Confirm named prior-role
deliverables are present.
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**

Scan every DERIVATION CHAIN cell in all SCHEMA-A tables. Flag bare conclusions without
computation steps as SCHEMA-A CONTENT violations.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**

Count FIELD labels in every UX tier block in Role 5. Flag any block missing FIELD-A
through FIELD-D as a SCHEMA-B STRUCTURAL violation.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — SCHEMA-A CELL ANCHOR AUDIT**

Scan every data cell in every SCHEMA-A table (Role 7 and Role 8a). For each cell:

- e.1: Does the cell open with a "BP-xx:" prefix? If not: CELL ANCHOR violation (scan-time
       detectable; report cell location and column).
- e.2: If a "BP-xx:" prefix is present, does the named Finding ID (e.g., BP-03) exist in
       Role 3's Finding ID list? If not: UNRESOLVED REFERENCE violation (cross-reference
       required; report cell location, prefix claimed, and the gap in Role 3).
- e.3: Report both violation classes with distinct labels. A cell failing e.1 is a CELL
       ANCHOR violation. A cell failing e.2 is an UNRESOLVED REFERENCE violation.
       **The prohibited merged form is "missing or invalid prefix" — any findings report
       that uses this phrase, or an equivalent combined label, to describe both violation
       classes in a single category does not satisfy the violation-class distinction
       requirement established by C-43/C-46.**

Findings: "Cell Anchor Audit: N cells checked, M CELL ANCHOR violation(s): [list],
P UNRESOLVED REFERENCE violation(s): [list]; violation classes reported separately: [Y/N]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R20: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-02

**Axis:** Registry orphaned-schema symmetric violation class — the Schema Production Registry
audit in CHECK (e) Plane 1 explicitly names ORPHANED SCHEMA as a violation class that is
logically independent of and symmetric to REGISTRY GAP. C-44's REGISTRY GAP detects
undercounting: a producing role has no registry entry, detectable by comparing row counts.
C-47 adds the symmetric class: ORPHANED SCHEMA detects misalignment: a schema body entry
has no registry row, detectable by scanning body entries against registry rows. The two
classes are logically independent — a registry can have REGISTRY GAP without ORPHANED SCHEMA
(a producing role missing from the registry, all body entries properly registered) or
ORPHANED SCHEMA without REGISTRY GAP (all producing roles registered, but one body entry
has no corresponding row). Both must be separately named, separately audited, and separately
reported. No cell anchor requirement. No BURST PATH TABLE.

**Hypothesis:** Declaring ORPHANED SCHEMA as a named symmetric counterpart in the CHECK
instruction pre-empts a common failure mode: an audit that checks row count (catching
REGISTRY GAP) but never checks body entries against the registry (missing ORPHANED SCHEMA).
Without the symmetric class, a Format Contract could contain a schema body entry for an
unreachable or misnamed schema, and the registry audit would pass because the row count
matches. The symmetric framing — "REGISTRY GAP catches what the registry is missing;
ORPHANED SCHEMA catches what the registry has that it shouldn't" — makes both directions
of the completeness contract auditable in the same pass.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State four claims before any analysis begins:

(a) **Binding constraint:** connector endpoint or platform limit hit first, with numeric
    threshold.
(b) **Primary gap:** specific action or burst path where protection is absent.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment requirement. Revision rule: inline `REVISED — see Role N` at gate boundary.

**Gate 1→2:** All four claims written. No analysis has appeared.

---

### ROLE 2 — FORMAT CONTRACT

---

#### SCHEMA PRODUCTION REGISTRY

Placed before all schema body entries. This is a dedicated named aggregate table.

Registry completeness rule: registry row count must equal the count of table-producing roles
in this document. A missing row is a **REGISTRY GAP** violation — detectable by row count
comparison alone, without scanning schema body entries.

| SCHEMA NAME | PRODUCING ROLE(S) | TABLE TYPE | GATE CONDITION |
|-------------|-------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact / cascade failure | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping | Gate 6→7 |
| SCHEMA-M | Role 8c | per-finding mitigation record | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

The per-entry annotations in the schema body below remain required. The registry provides
aggregate coverage verification; per-entry annotations provide per-entry governance.

---

#### SCHEMA BODY ENTRIES

**SCHEMA-A — PRIMARY ANALYSIS**

Applies to: Role 7 quantified impact; Role 8a cascade failure. Producing role(s): Role 7,
Role 8a.

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: connector API call volume at the burst-path source endpoint identified by
  Finding ID in Role 3 (BP-xx), measured at burst onset, before mitigation.
- PROTECTED: sustained throughput after Role 8c mitigation for BP-xx is applied.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing column header.
- SCHEMA-A CONTENT: DERIVATION CHAIN without arithmetic steps.

---

**SCHEMA-V — VOLUME MAPPING**

Applies to: Role 6. Producing role: Role 6.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Rejection clauses: SCHEMA-V STRUCTURAL, SCHEMA-V CONTENT.

---

**SCHEMA-M — MITIGATION RECORD**

Applies to: Role 8c. Producing role: Role 8c.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Rejection clauses: SCHEMA-M STRUCTURAL, SCHEMA-M CONTENT.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE**

Applies to: Role 5. Producing role: Role 5.

```
FIELD-A ERROR SIGNAL: [specific signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific user-visible state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific recovery step]
```

Rejection clauses: SCHEMA-B STRUCTURAL, SCHEMA-B CONTENT.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching its declared schema type is
a FORMAT-SCHEMA MISMATCH violation.

**Gate 2→3:** Schema Production Registry present with all four rows and gate conditions
filled. All schema body entries declared. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. Assign BP-xx Finding IDs. Classify STRUCTURAL / INCIDENTAL.
Record total count B.

**Gate 3→4:** At least one STRUCTURAL burst path. Finding IDs assigned. Count B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Three structurally distinct tiers with numeric thresholds and scope. Mapped to BP-xx.

**Gate 4→5:** Three tiers identified, mapped to BP-xx Finding IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

SCHEMA-B block per tier. Six-item gate per block. Tier count = B. At least two distinct
FIELD-B descriptions.

**Gate 5→6:** All B tiers complete, six-item gate satisfied.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V with at least three ranges including mandatory 5x spike. Derive spike from Verdict
Claim (a) threshold. Delta cells quantified.

**Gate 6→7:** SCHEMA-V complete with derived 5x spike and quantified Deltas.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce SCHEMA-A table at 5x load. DERIVATION CHAIN shows four-step arithmetic. Follow
with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A table present with four-step DERIVATION CHAIN. Compounding prose
present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a:** SCHEMA-A cascade table. Causal chain in DERIVATION CHAIN and prose.
**ROLE 8b:** 5x arithmetic, five steps.
**ROLE 8c:** SCHEMA-M, one row per BP-xx / RH-xx, specific AFTER STATE.

**Gate 8→9:** All deliverables present.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R20

This invariant is named FNMI-R20 and governs the Terminal Reconciler (Role 9).

(a) No REVISED markers after this point into Roles 1–8.
(b) Role 9 does not insert REVISED markers into Roles 1–8.
(c) Role 9 inserts zero (0) REVISED markers.
(d) FNMI-R20 VIOLATION: `FNMI-R20: VIOLATION at [reference] — [description]`.
    Compliance: `FNMI-R20: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R20 declared. Role 8 deliverables present. VERIFICATION-ONLY.

**CHECK (a):** Verdict revision marker audit.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit.
Findings: "Gate Audit: N/N gates pass, M gap(s): [list]"

**CHECK (c):** Derivation chain cell audit.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d):** SCHEMA-B structural scan.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — SCHEMA PRODUCTION REGISTRY AUDIT**

Audit the Schema Production Registry in Role 2 against the document's table-producing roles
and schema body entries. Two violation classes must be audited and reported under separate
labels:

- e.1: Count registry rows. Count table-producing roles in this document (roles that produce
       SCHEMA-A, SCHEMA-V, SCHEMA-M, or SCHEMA-B output). If row count ≠ producing role
       count: **REGISTRY GAP** violation — a producing role has no registry entry. Report:
       registry row count, producing role count, and the specific missing role(s). This class
       detects undercounting: the registry is smaller than it should be.

- e.2: For each registry row, confirm the GATE CONDITION column is filled. If not:
       **REGISTRY GATE GAP** violation — report schema name.

- e.3: For each schema body entry in Role 2, confirm it has a matching row in the Schema
       Production Registry. If a body entry has no registry row: **ORPHANED SCHEMA**
       violation — report the schema name. This class detects misalignment: the schema body
       contains a declaration that was never registered.

       **REGISTRY GAP and ORPHANED SCHEMA are logically independent violation classes:**
       REGISTRY GAP = a producing role exists without a registry entry (undercounting,
       detected by row count comparison). ORPHANED SCHEMA = a schema body entry exists
       without a registry entry (misalignment, detected by scanning body entries against
       registry rows). A registry can have REGISTRY GAP without ORPHANED SCHEMA, ORPHANED
       SCHEMA without REGISTRY GAP, both, or neither. Both classes must be separately
       named and separately reported. A combined finding that merges them does not satisfy
       the two-class requirement.

Findings: "Registry Audit: N registry rows, M producing role(s); REGISTRY GAP: [list or
none]; REGISTRY GATE GAP: [list or none]; ORPHANED SCHEMA: [list or none]; classes reported
separately: [Y/N]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R20: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-03

**Axis:** BURST PATH TABLE named rejection clause in Format Contract — the Format Contract's
SCHEMA-A rejection clauses list explicitly names "SCHEMA-A BASELINE SOURCE VIOLATION" as a
labeled violation class with the condition: "BASELINE cell cites a Finding ID directly
instead of routing through the BURST PATH TABLE." C-45 requires BASELINE definitions to
route through the BURST PATH TABLE by name and column, which defines the required structure.
C-48 converts the implied prohibition into a named, label-citable obligation declared in
the Format Contract itself — so a non-compliant cell can be flagged by violation class name
at scan time, without requiring knowledge of which round introduced the routing requirement.
No registry. No cell anchor requirement.

**Hypothesis:** Without a named rejection clause in the Format Contract, a cell that writes
"BP-01: 600 req/min" as its BASELINE value satisfies C-41 (cross-role ID anchoring) but
violates C-45 (should route through the BURST PATH TABLE). An auditor reading the cell
cannot flag it by violation class name — they must consult the routing requirement elsewhere.
Naming "SCHEMA-A BASELINE SOURCE VIOLATION" in the Format Contract's rejection clause list
makes the violation class self-contained: the Format Contract is the authority, the cell is
testable against it directly, and any prior-round distinction between "Finding-ID-anchored"
and "BURST-PATH-TABLE-routed" is visible at scan time without external context.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State four claims before any analysis begins:

(a) **Binding constraint:** connector endpoint or platform limit hit first, with numeric
    threshold.
(b) **Primary gap:** specific action or burst path where protection is absent.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment requirement. Revision rule: inline `REVISED — see Role N` at gate boundary.

**Gate 1→2:** All four claims written. No analysis has appeared.

---

### ROLE 2 — FORMAT CONTRACT

This section governs all tables and blocks in Roles 3–8.

**SCHEMA-A — PRIMARY ANALYSIS**

Applies to: Role 7 quantified impact; Role 8a cascade failure.
Producing role(s): Role 7 (Gate 7→8), Role 8a (Gate 8→9).

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: the connector API call volume at the burst-path endpoint identified in Role 3's
  BURST PATH TABLE, SCHEMA-A BASELINE SOURCE column — measured at burst onset, before any
  mitigation. This definition is anchored to the BURST PATH TABLE as the single authoritative
  source: a reader locates the BURST PATH TABLE in Role 3, finds the endpoint row, and reads
  the SCHEMA-A BASELINE SOURCE cell. This definition does not independently cite a Finding
  ID; it routes through the BURST PATH TABLE. The BURST PATH TABLE's SCHEMA-A BASELINE SOURCE
  column is named for this schema — that is the backward traceability anchor. This definition
  names the BURST PATH TABLE and its SCHEMA-A BASELINE SOURCE column — that is the forward
  traceability anchor.
- PROTECTED: sustained throughput at the same BURST PATH TABLE endpoint after Role 8c
  mitigation is applied.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: table missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell without arithmetic steps.
- **SCHEMA-A BASELINE SOURCE VIOLATION: a BASELINE cell cites a Finding ID directly
  (e.g., "BP-01: 600 req/min") instead of routing through the BURST PATH TABLE
  (e.g., "BURST PATH TABLE / BP-01 / SCHEMA-A BASELINE SOURCE: 600 req/min"). This
  violation class is named so that a non-compliant cell can be flagged by violation class
  name at scan time. A BASELINE cell with a direct Finding ID citation satisfies C-41
  (cross-role ID anchoring) but violates the BURST PATH TABLE routing requirement. The
  two conditions are distinguishable by checking whether the cell names the BURST PATH TABLE
  or names a Finding ID directly.**

---

**SCHEMA-V — VOLUME MAPPING**

Applies to: Role 6. Producing role: Role 6 (Gate 6→7).

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Rejection clauses: SCHEMA-V STRUCTURAL, SCHEMA-V CONTENT.

---

**SCHEMA-M — MITIGATION RECORD**

Applies to: Role 8c. Producing role: Role 8c (Gate 8→9).

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Rejection clauses: SCHEMA-M STRUCTURAL, SCHEMA-M CONTENT.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE**

Applies to: Role 5. Producing role: Role 5 (Gate 5→6).

```
FIELD-A ERROR SIGNAL: [specific signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific user-visible state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific recovery step]
```

Rejection clauses: SCHEMA-B STRUCTURAL, SCHEMA-B CONTENT.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching its declared schema type is
a FORMAT-SCHEMA MISMATCH violation.

**Gate 2→3:** All schemas declared. SCHEMA-A BASELINE definition names BURST PATH TABLE
and SCHEMA-A BASELINE SOURCE column. SCHEMA-A BASELINE SOURCE VIOLATION rejection clause
present in SCHEMA-A. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint — canonical name used throughout the document.
3. State the trigger condition.
4. Classify as STRUCTURAL or INCIDENTAL.
5. For STRUCTURAL: state why architectural redesign is required.
6. For INCIDENTAL: state the specific change that removes the burst.

After classifying all burst paths, produce the **BURST PATH TABLE**:

| BP ID | ENDPOINT NAME | BURST TYPE | TRIGGER CONDITION | SCHEMA-A BASELINE SOURCE |
|-------|---------------|------------|-------------------|--------------------------|
| BP-01 | [canonical endpoint name] | STRUCTURAL / INCIDENTAL | [trigger] | [baseline measurement value and unit] |

**BURST PATH TABLE requirements:**
- ENDPOINT NAME: canonical connector endpoint name. All downstream references use this name.
- SCHEMA-A BASELINE SOURCE: the baseline measurement for this endpoint. This is the
  authoritative value for Format Contract SCHEMA-A BASELINE definitions. The column name
  "SCHEMA-A BASELINE SOURCE" is named for the schema it feeds — this is the backward
  traceability anchor.
- Forward traceability: every Format Contract BASELINE definition names this table and the
  SCHEMA-A BASELINE SOURCE column as its source.
- Backward traceability: this column's name identifies the schema it feeds.

Record total burst path count as B.

If Verdict Claim (a)'s endpoint is not the ENDPOINT NAME in the primary burst row,
insert `REVISED — see Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL burst path. BURST PATH TABLE present with ENDPOINT
NAME and SCHEMA-A BASELINE SOURCE columns. Finding IDs assigned. Count B recorded.
Backward traceability present.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

For each tier:
1. Scope.
2. Numeric threshold and time window.
3. Enforcing layer.
4. Map to BP-xx from BURST PATH TABLE.
5. Scope-distinction check.

At least three structurally distinct tiers. Threshold in Verdict Claim (a) must appear.

**Gate 4→5:** Three structurally distinct tiers, mapped to BURST PATH TABLE BP-xx IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

SCHEMA-B block per tier. Six-item gate per block. Tier count = B. At least two distinct
FIELD-B descriptions.

**Gate 5→6:** All B tiers complete, six-item gate satisfied.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V with at least three ranges including mandatory 5x spike. BASELINE BEHAVIOR draws
from BURST PATH TABLE SCHEMA-A BASELINE SOURCE column value for the primary burst path.
Delta cells quantified.

**Gate 6→7:** SCHEMA-V complete with derived 5x spike and quantified Deltas.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce SCHEMA-A table at 5x load.

**BURST PATH TABLE anchor enforcement:** BASELINE cell must route through the BURST PATH
TABLE. Write the cell as: "BURST PATH TABLE / BP-xx / SCHEMA-A BASELINE SOURCE: [value]".
A BASELINE cell that cites a Finding ID directly (e.g., "BP-01: 3,000 req/min") without
naming the BURST PATH TABLE is a SCHEMA-A BASELINE SOURCE VIOLATION — detectable at scan
time by checking whether the cell names the BURST PATH TABLE or names a Finding ID directly.

DERIVATION CHAIN: four steps: (i) threshold × 5, (ii) − threshold = overflow, (iii) ×
retry factor, (iv) ÷ threshold = failure rate.

Follow with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A with BURST PATH TABLE-routed BASELINE cell and four-step DERIVATION
CHAIN. Compounding prose present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a:** SCHEMA-A cascade table. BASELINE cell routes through BURST PATH TABLE.
DERIVATION CHAIN shows causal chain. Required prose causal chain statement.

**ROLE 8b:** Five steps: threshold, ×5, overflow, retry amplification, failure rate.

**ROLE 8c:** SCHEMA-M. FINDING IDs match BURST PATH TABLE rows (BP-xx) or Role 5 retry
gaps (RH-xx). AFTER STATE names specific action, setting, or pattern.

**Gate 8→9:** All deliverables present. BASELINE cells in SCHEMA-A tables route through
BURST PATH TABLE. Causal chain in 8a. Five-step arithmetic in 8b. SCHEMA-M with specific
AFTER STATE in 8c.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R20

This invariant is named FNMI-R20 and governs the Terminal Reconciler (Role 9).

(a)–(d) as defined in V-01.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R20 declared. Role 8 deliverables present. VERIFICATION-ONLY.

**CHECK (a):** Verdict revision marker audit.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit.
Findings: "Gate Audit: N/N gates pass, M gap(s): [list]"

**CHECK (c):** Derivation chain cell audit.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d):** SCHEMA-B structural scan.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — BURST PATH TABLE BIDIRECTIONALITY AUDIT**

Audit the BURST PATH TABLE and Format Contract BASELINE definitions:

- e.1: Does Role 3 contain a table named BURST PATH TABLE? If not: BURST PATH TABLE ABSENT.
- e.2: Does the BURST PATH TABLE have a column named SCHEMA-A BASELINE SOURCE? If not:
       BACKWARD TRACEABILITY ABSENT.
- e.3: For each Format Contract BASELINE definition (SCHEMA-A): does it name the BURST
       PATH TABLE and the SCHEMA-A BASELINE SOURCE column as its source? If not:
       FORWARD TRACEABILITY ABSENT.
- e.4: For each SCHEMA-A BASELINE cell in Roles 7 and 8a: does the cell name the BURST
       PATH TABLE and its row (routing), or cite a Finding ID directly? Direct citation:
       **SCHEMA-A BASELINE SOURCE VIOLATION** (C-41 satisfied; BURST PATH TABLE routing
       not satisfied). Report cell location and the direct citation found.

Findings: "Burst Path Table Audit: BURST PATH TABLE present [Y/N]; SCHEMA-A BASELINE SOURCE
column present [Y/N]; Forward traceability [PASS/FAIL]; Cell routing: N BASELINE cells,
M SCHEMA-A BASELINE SOURCE VIOLATION(s): [list]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R20: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-04

**Axis:** Role sequence + output format — combines V-01's C-46 merge prohibition with
V-02's C-47 orphaned schema. The Format Contract opens with the Schema Production Registry
(C-44), followed by schema body entries that include the CELL ANCHOR requirement for
SCHEMA-A (C-43). Role 9 CHECK (e) audits two independent planes: Plane 1 (registry
completeness — REGISTRY GAP and ORPHANED SCHEMA as separate classes per C-47), Plane 2
(cell-level anchor — CELL ANCHOR and UNRESOLVED REFERENCE as separate classes, with the
merge prohibition explicitly named per C-46). No BURST PATH TABLE.

**Hypothesis:** C-46 and C-47 are structurally parallel enforcement escalations — both
convert an implicit distinctness requirement into an explicitly named prohibited merged
form. C-43 requires CELL ANCHOR vs. UNRESOLVED REFERENCE to be distinct (C-46 then names
the merged form that conflates them). C-44 requires REGISTRY GAP to be detectable (C-47
then adds the symmetric class ORPHANED SCHEMA). Combining both in one variation tests
whether a two-plane CHECK (e) can enforce both escalations simultaneously while keeping
the planes auditable independently. A document that satisfies Plane 1 but not Plane 2
(registry complete, cell anchors missing) must produce a finding naming exactly which
plane failed — not a combined registry-plus-cell audit result.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State four claims before any analysis begins:

(a) **Binding constraint:** connector endpoint or platform limit hit first, with numeric
    threshold.
(b) **Primary gap:** specific action or burst path where protection is absent.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment requirement. Revision rule: inline `REVISED — see Role N` at gate boundary.

**Gate 1→2:** All four claims written. No analysis has appeared.

---

### ROLE 2 — FORMAT CONTRACT

---

#### SCHEMA PRODUCTION REGISTRY

Placed before all schema body entries.

Registry completeness rule: registry row count must equal table-producing role count.
A missing row is a **REGISTRY GAP** violation (detectable by count comparison alone).

| SCHEMA NAME | PRODUCING ROLE(S) | TABLE TYPE | GATE CONDITION |
|-------------|-------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact / cascade failure | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping | Gate 6→7 |
| SCHEMA-M | Role 8c | per-finding mitigation record | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

Per-entry annotations below remain required.

---

#### SCHEMA BODY ENTRIES

**SCHEMA-A — PRIMARY ANALYSIS**

Applies to: Role 7; Role 8a. Producing role(s): Role 7, Role 8a.

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: connector API call volume at the burst-path source endpoint identified by
  Finding ID in Role 3 (BP-xx), measured at burst onset, before mitigation.
- PROTECTED: sustained throughput after Role 8c mitigation for BP-xx is applied.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

**SCHEMA-A CELL ANCHOR requirement:** every data cell in a SCHEMA-A-governed column must
open with "BP-xx: [value]" where BP-xx is the Finding ID from Role 3 the cell's value was
measured from.

Two violation classes — explicitly distinguished:
- **CELL ANCHOR violation:** cell missing the "BP-xx:" prefix. Scan-time detectable.
- **UNRESOLVED REFERENCE violation:** cell has a syntactically valid "BP-xx:" prefix but
  the named Finding ID does not exist in Role 3. Format-compliant; requires cross-reference.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing column header.
- SCHEMA-A CONTENT: DERIVATION CHAIN without arithmetic steps.
- SCHEMA-A CELL ANCHOR: missing BP-xx prefix (scan-time).
- SCHEMA-A UNRESOLVED REFERENCE: BP-xx prefix names a non-existent Finding ID (cross-ref).

---

**SCHEMA-V — VOLUME MAPPING**

Applies to: Role 6.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

Rejection clauses: SCHEMA-V STRUCTURAL, SCHEMA-V CONTENT.

---

**SCHEMA-M — MITIGATION RECORD**

Applies to: Role 8c.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

Rejection clauses: SCHEMA-M STRUCTURAL, SCHEMA-M CONTENT.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE**

Applies to: Role 5.

```
FIELD-A ERROR SIGNAL: [specific signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific user-visible state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific recovery step]
```

Rejection clauses: SCHEMA-B STRUCTURAL, SCHEMA-B CONTENT.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching its declared schema type is
a FORMAT-SCHEMA MISMATCH violation.

**Gate 2→3:** Schema Production Registry present with all four rows and gate conditions
filled. All schema body entries declared. SCHEMA-A CELL ANCHOR requirement and both
violation class definitions present. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. Assign BP-xx IDs. Classify STRUCTURAL / INCIDENTAL. Record B.

**Gate 3→4:** At least one STRUCTURAL path. BP-xx IDs assigned. B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Three structurally distinct tiers with numeric thresholds, scope, and BP-xx mapping.

**Gate 4→5:** Three tiers identified and mapped.

---

### ROLE 5 — UX PER THROTTLE TIER

SCHEMA-B block per tier. Six-item gate per block. Tier count = B. Two distinct FIELD-B.

**Gate 5→6:** All B tiers complete.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V with three rows, 5x spike derived arithmetically, Delta cells quantified.

**Gate 6→7:** SCHEMA-V complete.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

SCHEMA-A table at 5x load. All cells carry BP-xx prefix. DERIVATION CHAIN: four steps.
Prose on compounding effect.

**Gate 7→8:** SCHEMA-A with BP-xx prefixes on all cells and four-step chain.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a:** SCHEMA-A cascade table. All cells BP-xx prefixed. Causal chain in DERIVATION
CHAIN and prose.
**ROLE 8b:** 5x arithmetic, five steps.
**ROLE 8c:** SCHEMA-M, one row per BP-xx / RH-xx, specific AFTER STATE.

**Gate 8→9:** All deliverables present with BP-xx prefixes and causal chain.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R20

This invariant is named FNMI-R20 and governs the Terminal Reconciler (Role 9).

(a)–(d) as defined in V-01.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R20 declared. Role 8 deliverables present. VERIFICATION-ONLY.

**CHECK (a):** Verdict revision marker audit.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit.
Findings: "Gate Audit: N/N gates pass, M gap(s): [list]"

**CHECK (c):** Derivation chain cell audit.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d):** SCHEMA-B structural scan.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — TWO-PLANE SCHEMA AUDIT**

This check audits two independent planes. Partial failure in one plane does not affect the
other.

**Plane 1 — Schema Production Registry Completeness (C-47 enforcement):**

- e.1: Count registry rows in Role 2's Schema Production Registry. Count table-producing
       roles. If row count ≠ producing role count: **REGISTRY GAP** violation — a producing
       role has no registry entry (undercounting). Report: registry row count, producing role
       count, and the specific missing role(s).
- e.2: For each registry row, confirm gate condition column is filled. If not:
       **REGISTRY GATE GAP** for that row (report schema name).
- e.3: For each schema body entry in Role 2, confirm it has a matching registry row. If not:
       **ORPHANED SCHEMA** violation (report schema name). **REGISTRY GAP and ORPHANED SCHEMA
       are logically independent: REGISTRY GAP = producing role without registry entry
       (undercounting); ORPHANED SCHEMA = schema body entry without registry entry
       (misalignment). The two classes must be reported under separate named labels. A
       combined report that merges them does not satisfy the two-class requirement.**

Plane 1 findings: "Registry Audit: N rows, M producing roles; REGISTRY GAP: [list or none];
REGISTRY GATE GAP: [list or none]; ORPHANED SCHEMA: [list or none]; classes separate: [Y/N]"

**Plane 2 — Schema-A Cell-Level ID Anchor (C-46 enforcement):**

- e.4: Scan every data cell in every SCHEMA-A table (Roles 7 and 8a). For each cell:
       Does it open with "BP-xx:" prefix? If not: **CELL ANCHOR** violation (scan-time
       detectable). Record location and column name.
- e.5: For each cell with a "BP-xx:" prefix: does the named Finding ID exist in Role 3?
       If not: **UNRESOLVED REFERENCE** violation (cross-reference required). Record
       location, claimed prefix, and the Finding ID gap.
- e.6: Report CELL ANCHOR and UNRESOLVED REFERENCE with distinct labels. **The prohibited
       merged form is "missing or invalid prefix" — any findings report that uses this phrase
       or an equivalent combined label to describe both violation classes in a single category
       does not satisfy the violation-class distinction requirement.**

Plane 2 findings: "Cell Anchor Audit: N cells checked, M CELL ANCHOR violation(s): [list],
P UNRESOLVED REFERENCE violation(s): [list]; classes reported separately: [Y/N]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e) Plane 1: [findings output]
- Check (e) Plane 2: [findings output]
- FNMI-R20: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-05

**Axis:** Full integration — all three R20 criteria enforced simultaneously. The Format
Contract opens with a Schema Production Registry (C-44) followed by schema body entries
that include the CELL ANCHOR requirement (C-43) and the SCHEMA-A BASELINE SOURCE VIOLATION
rejection clause (C-48). Role 3 produces a BURST PATH TABLE (C-45) that serves as the
single authoritative source for all BASELINE definitions. Role 9 CHECK (e) runs a
three-plane audit: Plane 1 (registry completeness — REGISTRY GAP and ORPHANED SCHEMA as
independent classes per C-47), Plane 2 (BURST PATH TABLE bidirectionality — SCHEMA-A
BASELINE SOURCE VIOLATION per C-48), Plane 3 (cell-level anchor — merge prohibition per
C-46).

**Hypothesis:** The three R20 criteria are escalations of three different traceability
contracts from R19. C-46 escalates C-43's two-class distinction: naming the prohibited
merged form pre-empts summary-level re-conflation. C-47 escalates C-44's single violation
class: naming ORPHANED SCHEMA as REGISTRY GAP's symmetric counterpart closes the reverse
direction of the completeness contract. C-48 escalates C-45's implied routing prohibition:
naming SCHEMA-A BASELINE SOURCE VIOLATION in the Format Contract itself converts an
implied obligation into a scan-time-citable rejection clause. All three escalations are
additive: each names a previously unnamed prohibited pattern and makes it a labeled
violation class. The three-plane CHECK (e) audits each escalation independently, producing
a findings summary that identifies which traceability level (document structure, baseline
definition, or individual cell) and which direction (gap vs. misalignment; format vs.
semantic; routing vs. direct-citation) the violation occurs at.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State four claims before any analysis begins:

(a) **Binding constraint:** connector endpoint or platform limit hit first, with numeric
    threshold.
(b) **Primary gap:** specific action or burst path where protection is absent.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows all four items without proceeding to
evidence sections. Revision rule: inline `REVISED — see Role N` at gate boundary.

**Gate 1→2:** All four claims written. No analysis has appeared.

---

### ROLE 2 — FORMAT CONTRACT

This section governs all tables and blocks in Roles 3–8. It opens with a Schema Production
Registry (aggregate coverage verification), followed by schema body entries (per-entry
governance including CELL ANCHOR requirements and rejection clauses).

---

#### SCHEMA PRODUCTION REGISTRY

Single aggregate table placed before all schema body entries.

| SCHEMA NAME | PRODUCING ROLE(S) | TABLE TYPE | GATE CONDITION |
|-------------|-------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact / cascade failure | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping | Gate 6→7 |
| SCHEMA-M | Role 8c | per-finding mitigation record | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

**Registry completeness rule:** registry row count must equal producing role count (4 above).
A missing row is a **REGISTRY GAP** violation detectable by count comparison alone — no
schema body entry scan required. The per-entry annotations in the body below remain required.

---

#### SCHEMA BODY ENTRIES

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 7 quantified impact; Role 8a cascade failure.
Producing role(s): Role 7 (Gate 7→8), Role 8a (Gate 8→9).

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: the connector API call volume at the burst-path endpoint identified in Role 3's
  BURST PATH TABLE, SCHEMA-A BASELINE SOURCE column — measured at burst onset, before any
  mitigation. This definition is anchored to the BURST PATH TABLE as the single authoritative
  source: a reader locates the BURST PATH TABLE in Role 3, finds the endpoint row, and reads
  the SCHEMA-A BASELINE SOURCE cell. This definition does not independently cite a Finding
  ID; it routes through the BURST PATH TABLE. The BURST PATH TABLE's SCHEMA-A BASELINE SOURCE
  column is named for this schema — that is the backward traceability anchor. This definition
  names the BURST PATH TABLE and its SCHEMA-A BASELINE SOURCE column — that is the forward
  traceability anchor.
- PROTECTED: sustained throughput at the same BURST PATH TABLE endpoint after Role 8c
  mitigation is applied and active.
- DERIVATION CHAIN: step-by-step arithmetic tracing the computation. Bare conclusions are
  SCHEMA-A CONTENT violations.

**SCHEMA-A CELL ANCHOR requirement:** every data cell in a SCHEMA-A-governed column must
open with "BP-xx: [value]" where BP-xx is the Finding ID from Role 3's BURST PATH TABLE
the cell's value was measured from. This prefix makes each cell independently verifiable:
a reader locates BP-xx in the BURST PATH TABLE and confirms the cell's measurement without
reading the Format Contract column definition.

Two violation classes — explicitly distinguished in all compliance checks:
- **CELL ANCHOR violation:** cell missing the "BP-xx:" prefix entirely. Format violation,
  scan-time detectable by inspecting cell's opening characters.
- **UNRESOLVED REFERENCE violation:** cell has a syntactically valid "BP-xx:" prefix but
  the named Finding ID does not exist in Role 3's BURST PATH TABLE. Format-compliant;
  semantically invalid. Detectable by cross-referencing the prefix against the BURST PATH
  TABLE's BP ID column.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell without arithmetic steps.
- SCHEMA-A CELL ANCHOR: cell missing BP-xx prefix (scan-time).
- SCHEMA-A UNRESOLVED REFERENCE: BP-xx prefix names a Finding ID not in BURST PATH TABLE
  (cross-reference required).
- **SCHEMA-A BASELINE SOURCE VIOLATION: a BASELINE cell cites a Finding ID directly
  (e.g., "BP-01: 600 req/min") instead of routing through the BURST PATH TABLE
  (e.g., "BURST PATH TABLE / BP-01 / SCHEMA-A BASELINE SOURCE: 600 req/min"). A direct
  Finding ID citation satisfies C-41 (cross-role ID anchoring) but does not satisfy the
  BURST PATH TABLE routing requirement. Detectable at scan time by checking whether the
  BASELINE cell names the BURST PATH TABLE or names a Finding ID directly.**

---

**SCHEMA-V — VOLUME MAPPING**

Applies to: Role 6. Producing role: Role 6 (Gate 6→7).

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- VOLUME RANGE: named volume band derived from the threshold in Verdict Claim (a).
- BASELINE BEHAVIOR: system behavior without mitigation, for the primary BURST PATH TABLE
  endpoint.
- PROTECTED BEHAVIOR: system behavior with Role 8c mitigation active.
- Delta: quantified improvement.

Rejection clauses: SCHEMA-V STRUCTURAL, SCHEMA-V CONTENT.

---

**SCHEMA-M — MITIGATION RECORD**

Applies to: Role 8c. Producing role: Role 8c (Gate 8→9).

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- FINDING ID: BP-xx from Role 3's BURST PATH TABLE or RH-xx from Role 5.
- BEFORE STATE: unmitigated behavior — names component, volume condition, failure mode.
- AFTER STATE: mitigated behavior — names specific action, setting, or pattern.
- Addresses: BURST PATH TABLE BP-xx paths covered.

Rejection clauses: SCHEMA-M STRUCTURAL, SCHEMA-M CONTENT.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE**

Applies to: Role 5. Producing role: Role 5 (Gate 5→6).

```
FIELD-A ERROR SIGNAL: [specific signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific user-visible state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific recovery step]
```

Rejection clauses: SCHEMA-B STRUCTURAL, SCHEMA-B CONTENT.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching its declared schema type is
a FORMAT-SCHEMA MISMATCH violation.

**Gate 2→3:** Schema Production Registry present (4 rows, gate conditions filled). All
schema body entries declared with per-entry annotations. SCHEMA-A BASELINE definition names
BURST PATH TABLE and SCHEMA-A BASELINE SOURCE column. SCHEMA-A CELL ANCHOR requirement and
both violation classes defined. SCHEMA-A BASELINE SOURCE VIOLATION rejection clause present.
No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint — canonical name used throughout the document.
3. State the trigger condition.
4. Classify as STRUCTURAL or INCIDENTAL.
5. For STRUCTURAL: state why architectural redesign is required.
6. For INCIDENTAL: state the specific change that removes the burst.

After classifying all burst paths, produce the **BURST PATH TABLE**:

| BP ID | ENDPOINT NAME | BURST TYPE | TRIGGER CONDITION | SCHEMA-A BASELINE SOURCE |
|-------|---------------|------------|-------------------|--------------------------|
| BP-01 | [canonical endpoint name] | STRUCTURAL / INCIDENTAL | [trigger condition] | [baseline measurement: volume at burst onset, unit] |

**BURST PATH TABLE requirements:**
- ENDPOINT NAME: canonical connector endpoint name. All downstream references use this name.
- SCHEMA-A BASELINE SOURCE: the baseline measurement for this endpoint. This is the
  authoritative value for Format Contract SCHEMA-A BASELINE definitions. The column name
  "SCHEMA-A BASELINE SOURCE" is named for the schema it feeds — this is the backward
  traceability anchor. A reader who sees this column name knows it feeds SCHEMA-A.
- Forward traceability: the Format Contract SCHEMA-A BASELINE definition names this table
  and this column as its source.
- Backward traceability: this column's name identifies the schema it feeds.
- Each BP-xx cell-level prefix used in SCHEMA-A tables downstream must reference a BP ID
  that appears in this table. A cell with "BP-05:" prefix is an UNRESOLVED REFERENCE if
  BP-05 does not appear in this table's BP ID column.

Record total burst path count as B.

If Verdict Claim (a)'s endpoint is not the ENDPOINT NAME in the primary burst row of the
BURST PATH TABLE, insert `REVISED — see Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL burst path. BURST PATH TABLE present with BP ID,
ENDPOINT NAME, and SCHEMA-A BASELINE SOURCE columns. Finding IDs assigned. Count B
recorded. Backward traceability present (SCHEMA-A BASELINE SOURCE column named for schema).

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

For each tier:
1. Scope.
2. Numeric threshold and time window.
3. Enforcing layer.
4. Map to BP-xx from BURST PATH TABLE.
5. Scope-distinction check.

At least three structurally distinct tiers. Threshold in Verdict Claim (a) must appear.

**Gate 4→5:** Three structurally distinct tiers, mapped to BURST PATH TABLE BP-xx IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier, SCHEMA-B block. Six-item gate per block. Tier count = B from Role 3.
At least two tiers with distinct FIELD-B descriptions.

**Gate 5→6:** All B tiers complete, six-item gate satisfied.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V with at least three ranges including mandatory 5x spike row. Derive spike from
Verdict Claim (a) threshold. BASELINE BEHAVIOR draws from BURST PATH TABLE SCHEMA-A
BASELINE SOURCE. Delta cells quantified.

**Gate 6→7:** SCHEMA-V complete with derived 5x spike and quantified Deltas.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce SCHEMA-A table at 5x load.

**Cell anchor enforcement:** every cell in BASELINE, PROTECTED, and DERIVATION CHAIN must
open with "BP-xx: [value]". Use the BP ID from the BURST PATH TABLE row for the primary
burst path. Example cells:

- BASELINE: "BP-01: 3,000 req/min [BURST PATH TABLE / BP-01 / SCHEMA-A BASELINE SOURCE × 5]"
- PROTECTED: "BP-01: 580 req/min [concurrency cap applied, post-Role-8c]"
- DERIVATION CHAIN: "BP-01: (i) 600 × 5 = 3,000 req/min; (ii) 3,000 − 600 = 2,400 overflow;
  (iii) 2,400 × 3 retries = 7,200 total attempts; (iv) 7,200 ÷ 600 = 12× failure pressure"

A BASELINE cell that cites a Finding ID without naming the BURST PATH TABLE is a SCHEMA-A
BASELINE SOURCE VIOLATION. A cell missing the BP-xx prefix is a CELL ANCHOR violation.
A cell whose BP-xx prefix does not match a BURST PATH TABLE row is an UNRESOLVED REFERENCE.

Follow table with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A present. All cells carry BP-xx prefixes referencing BURST PATH TABLE
rows. DERIVATION CHAIN shows four-step arithmetic. Compounding prose present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

SCHEMA-A table for cascade. All cells carry BP-xx prefixes. DERIVATION CHAIN shows causal
chain step-by-step. Required prose: "When [endpoint A] hits [threshold] at [volume],
[downstream effect] because [mechanism]. This triggers [endpoint B] to receive [overflow],
hitting [threshold]."

**ROLE 8b — 5x ARITHMETIC DERIVATION**

Five steps: threshold, ×5, overflow, retry amplification, failure rate. No bare assertions.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

SCHEMA-M table. FINDING IDs match BURST PATH TABLE rows (BP-xx) or Role 5 retry gaps
(RH-xx). AFTER STATE names specific action, setting, or pattern. Generic descriptions do
not pass.

**Gate 8→9:** All deliverables present. SCHEMA-A cells carry BP-xx prefixes pointing to
BURST PATH TABLE rows. Causal chain in 8a. Five-step arithmetic in 8b. SCHEMA-M with
specific AFTER STATE in 8c.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R20

This invariant is named FNMI-R20 and governs the Terminal Reconciler (Role 9).

(a) No REVISED markers after this point into Roles 1–8.
(b) Role 9 does not insert REVISED markers into Roles 1–8.
(c) Role 9 inserts zero (0) REVISED markers.
(d) FNMI-R20 VIOLATION: `FNMI-R20: VIOLATION at [reference] — [description]`.
    Compliance: `FNMI-R20: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R20 declared. All Role 8 deliverables present.

VERIFICATION-ONLY per FNMI-R20. Perform five checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — THREE-PLANE SCHEMA AUDIT**

This check audits three traceability planes independently. Partial failure in one plane
does not affect the others. Each plane must be audited and reported under its own heading.

**Plane 1 — Schema Production Registry Completeness (e.1–e.3) [C-47]:**

- e.1: Count registry rows in Role 2's Schema Production Registry. Count table-producing
       roles (roles that produce SCHEMA-A, SCHEMA-V, SCHEMA-M, or SCHEMA-B output). If
       row count ≠ producing role count: **REGISTRY GAP** violation — a producing role has
       no registry entry. Report: registry row count, producing role count, missing role(s).
       This class detects undercounting: the registry is smaller than it should be.
- e.2: For each registry row, confirm the GATE CONDITION column is filled. If not:
       **REGISTRY GATE GAP** for that specific row (report schema name).
- e.3: For each schema body entry in Role 2, confirm it has a matching registry row. If a
       schema body entry has no registry row: **ORPHANED SCHEMA** violation (report schema
       name). This class detects misalignment: a schema body entry without a registry entry.
       **REGISTRY GAP and ORPHANED SCHEMA are logically independent: REGISTRY GAP = producing
       role without registry entry (undercounting, detected by row count comparison);
       ORPHANED SCHEMA = schema body entry without registry entry (misalignment, detected by
       scanning body entries against registry rows). Both classes must appear under separate
       named labels in the findings output.**

Plane 1 findings: "Registry Audit: N registry rows, M producing role(s); REGISTRY GAP:
[list or none]; REGISTRY GATE GAP: [list or none]; ORPHANED SCHEMA: [list or none];
classes reported separately: [Y/N]"

**Plane 2 — BURST PATH TABLE Bidirectionality (e.4) [C-48]:**

- e.4: Audit the BURST PATH TABLE in Role 3 and the Format Contract SCHEMA-A BASELINE
       definition for bidirectionality and cell routing:

  Forward check: does the Format Contract SCHEMA-A BASELINE definition name the BURST
  PATH TABLE by name and the SCHEMA-A BASELINE SOURCE column by name? If not: FORWARD
  TRACEABILITY ABSENT (the definition is independently anchored, satisfying C-41 but not
  C-45).

  Backward check: does the BURST PATH TABLE contain a column named SCHEMA-A BASELINE
  SOURCE? If not: BACKWARD TRACEABILITY ABSENT.

  Cell routing check: for each SCHEMA-A BASELINE cell in Roles 7 and 8a, does the cell
  name the BURST PATH TABLE and row (routing), or cite a Finding ID directly? Direct
  Finding ID citation: **SCHEMA-A BASELINE SOURCE VIOLATION** (C-41 satisfied; BURST PATH
  TABLE routing not satisfied). Report cell location and the direct citation found.

Plane 2 findings: "Burst Path Table: present [Y/N]; Forward [PASS/FAIL]; Backward
[PASS/FAIL]; Cell routing: N BASELINE cells, M SCHEMA-A BASELINE SOURCE VIOLATION(s):
[list]"

**Plane 3 — Schema Cell-Level ID Anchor (e.5–e.6) [C-46]:**

- e.5: Scan every data cell in every SCHEMA-A table (Roles 7 and 8a). For each cell:
  - If cell does not open with "BP-xx:" prefix: **CELL ANCHOR** violation. Record location
    and column name. This is scan-time detectable.
  - If cell opens with "BP-xx:" prefix: proceed to e.6 for this cell.

- e.6: For each cell with a "BP-xx:" prefix, verify the named BP-xx Finding ID exists in
  Role 3's BURST PATH TABLE BP ID column.
  - If exists: prefix is resolved — no violation.
  - If not found: **UNRESOLVED REFERENCE** violation. Record cell location, the claimed
    prefix, and the gap (BP-xx not in BURST PATH TABLE).

  Violation class distinction: CELL ANCHOR violations (e.5) and UNRESOLVED REFERENCE
  violations (e.6) must appear as separate named violation classes in the findings output.
  **The prohibited merged form is "missing or invalid prefix" — any findings report that
  uses this phrase, or an equivalent combined label, to describe both violation classes in
  a single category does not satisfy the violation-class distinction requirement.**

Plane 3 findings: "Cell Anchor Audit: N cells checked, M CELL ANCHOR violation(s): [list],
P UNRESOLVED REFERENCE violation(s): [list]; violation classes reported separately: [Y/N]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e) Plane 1: [findings output]
- Check (e) Plane 2: [findings output]
- Check (e) Plane 3: [findings output]
- FNMI-R20: COMPLIANT / VIOLATION at [reference] — [description]
