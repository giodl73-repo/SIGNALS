---
skill: quest-variate
skill_target: flow-ratelimit
date: 2026-03-17
round: 19
rubric_version: 18
---

# flow-ratelimit — Variate R19

Five complete, runnable skill body prompt variations.
Single-axis variations: V-01 (cell-level ID anchor — SCHEMA-A CELL ANCHOR pattern + two
violation classes), V-02 (Schema Production Registry at Format Contract head — REGISTRY GAP
violation detectable by row count), V-03 (BURST PATH TABLE in Role 3 as authoritative
single-source anchor for all downstream BASELINE definitions).
Combination variations: V-04 (cell anchor + registry — Planes 1–2 CHECK (e)), V-05 (full
integration — registry + BURST PATH TABLE + cell anchor + three-plane CHECK (e) at
e.1–e.6).

**R19 target criteria: C-43, C-44, C-45**

C-43 (Schema Cell-Level ID Anchor): Every SCHEMA-A data cell must open with "BP-xx: [value]",
making each cell independently verifiable without reading the Format Contract column
definition. Two violation classes must be explicitly distinguished: CELL ANCHOR (cell missing
the prefix — format violation, scan-time detectable) vs. UNRESOLVED REFERENCE (cell has a
syntactically valid prefix but the named Finding ID does not exist in Role 3 — format-
compliant but semantically invalid, detectable by cross-referencing). A compliance check
that enforces the prefix without distinguishing these two classes does not fully satisfy C-43.
Requires C-41.

C-44 (Schema Production Registry): The Format Contract must include a Schema Production
Registry — a dedicated named table placed before individual schema body entries — aggregating
all schema → producing role(s) → table type → gate condition mappings. Registry completeness
rule: every table-producing role must have exactly one registry entry. A missing row is a
REGISTRY GAP violation detectable by comparing registry row count against producing role
count. The per-entry role governance annotations required by C-42 remain necessary and do
not replace the registry. Requires C-42.

C-45 (BURST PATH TABLE as Authoritative Single-Source Anchor): Role 3 must produce a
dedicated named table (BURST PATH TABLE) with columns including ENDPOINT NAME and SCHEMA-A
BASELINE SOURCE. Every Format Contract BASELINE definition must reference this table by name
and column rather than independently citing Finding IDs. Bidirectional traceability must be
present: each BASELINE definition names the BURST PATH TABLE column it draws from (forward);
at least one BURST PATH TABLE column is named for the schema it feeds (backward). A Format
Contract that cites individual Finding IDs from Role 3 without routing through the BURST
PATH TABLE satisfies C-41 but not C-45. Requires C-41.

**R19 variation axes:**

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| C-43 cell anchor | CELL ANCHOR + UNRESOLVED REFERENCE defined in Format Contract | inherited from R17 base | inherited from R17 base | CELL ANCHOR + UNRESOLVED REFERENCE | three-plane enforcement, e.4–e.6 |
| C-44 registry | no registry | Schema Production Registry at Format Contract head | no registry | Schema Production Registry | three-plane Plane 1, e.1–e.3 |
| C-45 BURST PATH TABLE | no BURST PATH TABLE | no BURST PATH TABLE | Role 3 produces BURST PATH TABLE; BASELINE definitions reference it | no BURST PATH TABLE | BURST PATH TABLE + cell prefix resolves to BURST PATH TABLE row |
| Role 9 CHECK (e) | single-plane cell audit | two-plane registry audit | single-plane bidirectionality audit | two-plane: registry + cell anchor | three-plane: registry + BURST PATH TABLE + cell anchor |
| Predicted C-43 | PASS | partial (no violation-class distinction) | partial (no cell prefix) | PASS | PASS |
| Predicted C-44 | miss | PASS | miss | PASS | PASS |
| Predicted C-45 | miss | miss | PASS | miss | PASS |

---

## V-01

**Axis:** Cell-level ID anchor — the Format Contract's SCHEMA-A definition extends C-41's
column-level artifact traceability to per-cell level by requiring every SCHEMA-A data cell
to open with "BP-xx: [value]". Two violation classes are introduced and explicitly
distinguished: CELL ANCHOR (missing prefix, scan-time detectable) and UNRESOLVED REFERENCE
(prefix present but Finding ID not in Role 3, cross-reference required). Role 9 gains a
CHECK (e) that audits both violation classes in one pass.

**Hypothesis:** Enforcing the BP-xx prefix at cell level makes each cell independently
falsifiable without reading the Format Contract column definition: a reader who sees
"BP-03: 847 req/min" can go directly to Role 3 and locate BP-03 to verify the measurement.
Distinguishing the two violation classes is necessary because format-compliant prefixes
("BP-05:") cannot be challenged as invalid unless a reader separately verifies that BP-05
exists in Role 3. A Role 9 CHECK (e) that reports CELL ANCHOR and UNRESOLVED REFERENCE as
distinct findings closes this gap structurally.

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

A compliance check that enforces prefix presence without distinguishing these two classes
conflates format compliance with semantic validity and does not fully satisfy C-43.

Rejection clauses:
- SCHEMA-A STRUCTURAL: table missing one or more of BASELINE, PROTECTED, DERIVATION CHAIN
  column headers. Detectable at scan time.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell contains a conclusion without computation steps.
  Requires reading cell content to detect.
- SCHEMA-A CELL ANCHOR: a cell in any SCHEMA-A column is missing the "BP-xx:" prefix.
  Detectable at scan time by inspecting cell opening characters.
- SCHEMA-A UNRESOLVED REFERENCE: a cell's BP-xx prefix names a Finding ID that does not
  exist in Role 3. Detectable by cross-referencing against Role 3's Finding ID list.

---

**SCHEMA-V — VOLUME MAPPING** (volume-to-behavior mapping table)

Applies to: Role 6 volume-to-behavior mapping.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- VOLUME RANGE: named volume band using values derived from the threshold cited in
  Verdict Claim (a).
- BASELINE BEHAVIOR: system behavior at this volume range without mitigation.
- PROTECTED BEHAVIOR: system behavior at this volume range with Role 8c mitigation active.
- Delta: quantified improvement. Generic labels without quantified values are SCHEMA-V
  CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: table missing one or more declared column headers.
- SCHEMA-V CONTENT: Delta cell states a relative improvement without a quantified value.

---

**SCHEMA-M — MITIGATION RECORD** (per-finding mitigation tables)

Applies to: Role 8c per-finding mitigation prescriptions.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- FINDING ID: BP-xx from Role 3 or RH-xx from Role 5 that this mitigation targets.
- BEFORE STATE: unmitigated behavior — names component, volume condition, and failure mode.
- AFTER STATE: mitigated behavior — names specific action, setting, or pattern applied.
- Addresses: burst path Finding IDs (BP-xx) covered by this mitigation.

Rejection clauses:
- SCHEMA-M STRUCTURAL: table missing one or more declared column headers.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE cell is generic — no component named,
  no action named, or a non-answer present.

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
- SCHEMA-B CONTENT: a field contains a non-answer (blank, "N/A", "varies", "see above",
  or a generic instruction without specifics).

---

Unified FORMAT-SCHEMA MISMATCH clause: any table in this document whose column structure
does not match the schema type declared for its producing role is a FORMAT-SCHEMA MISMATCH
violation, detectable at scan time. At least one SCHEMA-A table, one SCHEMA-V table, and
one SCHEMA-M table must appear in Roles 3–8; any that do not appear are schema declaration
gaps.

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

Record the total burst path count as B. This count is the authoritative source for the
tier count verification in Role 5 gate item (e).

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
- DERIVATION CHAIN: "BP-xx: [step-by-step arithmetic including (i) threshold × 5 = spike,
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

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R19

This invariant is named FNMI-R19 and governs the Terminal Reconciler (Role 9) that follows.

(a) After this invariant is declared, no REVISED markers may be inserted into Roles 1–8.
    A condition discovered during Role 9 that would in forward execution require a REVISED
    marker is recorded as a named FNMI-R19 reconciler finding — the marker is not inserted.
(b) The Terminal Reconciler (Role 9) does not insert REVISED markers into any section
    authored during Roles 1–8.
(c) The Terminal Reconciler inserts zero (0) REVISED markers. Insertion count = 0.
(d) Any REVISED marker insertion by Role 9 is a FNMI-R19 VIOLATION. Named as:
    `FNMI-R19: VIOLATION at [Finding ID or Claim reference] — [description]`.
    Absence of violations: `FNMI-R19: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R19 declared. Role 8 deliverables present.

This role is VERIFICATION-ONLY per FNMI-R19. Perform five checks.

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
       ANCHOR violation. A cell failing e.2 is an UNRESOLVED REFERENCE violation. Do not
       merge these into a single violation category.

Findings: "Cell Anchor Audit: N cells checked, M CELL ANCHOR violation(s): [list],
P UNRESOLVED REFERENCE violation(s): [list]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R19: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-02

**Axis:** Output format — the Format Contract opens with a Schema Production Registry:
a dedicated named table placed before individual schema body entries, aggregating all
schema → producing role(s) → table type → gate condition mappings. Registry completeness
is verifiable by row count without scanning schema body entries. Role 9 gains a CHECK (e)
that audits registry completeness in two planes.

**Hypothesis:** The Schema Production Registry makes C-44's coverage rule mechanically
enforceable: a reader can verify that every table-producing role has a governing schema by
comparing the registry's row count against the count of table-producing roles. This is
O(1) — the reader does not scan schema body entries. A REGISTRY GAP violation is
structurally detectable from a single count comparison, paralleling how C-38's
reconciler-citation rule detects violations by checking for the FNMI label rather than
verifying behavioral equivalence. The per-entry role governance annotations from C-42
remain and are not replaced by the registry.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any rate limit inventory, burst path audit, cascade
analysis, UX description, or volume mapping begins.

(a) **Binding constraint:** connector endpoint or platform limit hit first, with numeric
    threshold.
(b) **Primary gap:** specific action or burst path where protection is absent.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding, primary gap, system
status, and UX coverage scope.

**Revision rule:** any analysis role that revises a Verdict claim inserts an inline
`REVISED — see Role N` marker at that role's gate boundary before the gate is unblocked.

**Gate 1→2:** All four claims written. No analysis has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section governs all tables and blocks produced in Roles 3–8. It opens with a Schema
Production Registry that makes total role-to-schema coverage verifiable by row count, then
declares individual schema body entries with per-entry role governance annotations.

---

#### SCHEMA PRODUCTION REGISTRY

This table is the single aggregate source for schema → role mappings. It is placed before
schema body entries so that coverage is verifiable without scanning the body.

| SCHEMA NAME | PRODUCING ROLE(S) | TABLE TYPE | GATE CONDITION |
|-------------|-------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact / cascade failure | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping | Gate 6→7 |
| SCHEMA-M | Role 8c | per-finding mitigation record | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

**Registry completeness rule:** the number of registry rows must equal the number of
table-producing roles in this document. If a table-producing role has no registry entry,
that is a **REGISTRY GAP** violation. This violation is detectable by comparing registry
row count (4 above) against the count of table-producing roles (4: Roles 5, 6, 7/8a, 8c)
without reading any schema body entry. Adding a new table-producing role without adding
a registry row is a REGISTRY GAP violation regardless of whether a matching schema body
entry exists.

The per-entry "Applies to:" annotations in schema body entries below remain required. The
registry does not replace them — the registry provides aggregate coverage verification;
the inline annotations provide per-entry governance confirmation.

---

#### SCHEMA BODY ENTRIES

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 7 quantified impact at load spike; Role 8a cascade failure analysis.

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: the connector API call volume directed at the burst-path source endpoint
  identified by Finding ID in Role 3 (BP-xx), measured at burst onset, before any
  mitigation. This definition refers to the specific endpoint and Finding ID from Role 3.
- PROTECTED: sustained throughput at the same endpoint after Role 8c mitigation for BP-xx
  is applied and active.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell without computation steps.

---

**SCHEMA-V — VOLUME MAPPING** (volume-to-behavior mapping table)

Applies to: Role 6 volume-to-behavior mapping.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- VOLUME RANGE: named volume band derived from the threshold in Verdict Claim (a).
- BASELINE BEHAVIOR: system behavior without mitigation.
- PROTECTED BEHAVIOR: system behavior with Role 8c mitigation active.
- Delta: quantified improvement. Generic labels are SCHEMA-V CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: missing one or more declared column headers.
- SCHEMA-V CONTENT: Delta cell without quantified value.

---

**SCHEMA-M — MITIGATION RECORD** (per-finding mitigation tables)

Applies to: Role 8c per-finding mitigation prescriptions.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- FINDING ID: BP-xx from Role 3 or RH-xx from Role 5.
- BEFORE STATE: unmitigated behavior — names component, volume condition, failure mode.
- AFTER STATE: mitigated behavior — names specific action, setting, or pattern.
- Addresses: BP-xx burst paths covered by this mitigation.

Rejection clauses:
- SCHEMA-M STRUCTURAL: missing one or more declared column headers.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE is generic.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE** (UX per throttle tier)

Applies to: Role 5 UX descriptions per throttle tier.

```
FIELD-A ERROR SIGNAL: [specific signal — not "error occurs"]
FIELD-B USER-VISIBLE BEHAVIOR: [specific user-visible state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific actionable recovery step]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: block missing FIELD-A through FIELD-D labels.
- SCHEMA-B CONTENT: field contains a non-answer.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table whose column structure does not match its
declared schema type is a FORMAT-SCHEMA MISMATCH violation, detectable at scan time.

**Gate 2→3:** Schema Production Registry present with all four rows. All schema body entries
declared with per-entry "Applies to:" annotations. Rejection clauses stated. No analysis
has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint(s) — consistent with Verdict Claim (a).
3. State the trigger condition.
4. Classify as STRUCTURAL or INCIDENTAL.
5. For STRUCTURAL: state why architectural redesign is required.
6. For INCIDENTAL: state the specific change that removes the burst.

Record total burst path count as B.

If Verdict Claim (a)'s endpoint is not the primary burst source, insert `REVISED — see
Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL burst path. Finding IDs assigned. Total count B
recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

For each tier:
1. Scope: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window.
3. Enforcing layer: connector / platform / both.
4. Map to BP-xx Finding IDs from Role 3.
5. Scope-distinction check: same scope level ≠ structurally distinct tier.

At least three structurally distinct tiers. Threshold in Verdict Claim (a) must appear here.

**Gate 4→5:** Three structurally distinct tiers with numeric thresholds. All tiers mapped
to BP-xx Finding IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier, answer (i)–(iv), then write the SCHEMA-B block:

```
FIELD-A ERROR SIGNAL: [answer to (i)]
FIELD-B USER-VISIBLE BEHAVIOR: [answer to (ii)]
FIELD-C VISIBILITY LEVEL: [answer to (iii)]
FIELD-D RECOVERY PATH: [answer to (iv)]
```

Gate items per block: (a)–(f) as defined in Format Contract. Tier count must equal B from
Role 3. At least two tiers with distinct FIELD-B descriptions.

**Gate 5→6:** All B tiers complete. Six-item gate satisfied per tier.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

Produce SCHEMA-V table with at least three volume ranges including mandatory 5x spike row.
Derive spike volume arithmetically. Delta cells must be quantified.

**Gate 6→7:** SCHEMA-V with three rows, quantified Deltas, derived 5x spike.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

Produce SCHEMA-A table at 5x load:
- BASELINE: BP-xx prefix required.
- PROTECTED: BP-xx prefix required.
- DERIVATION CHAIN: BP-xx prefix required; four-step arithmetic: (i) × 5, (ii) − threshold,
  (iii) × retry factor, (iv) ÷ threshold.

Follow with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A present with four-step DERIVATION CHAIN. Compounding prose present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

SCHEMA-A table for cascade. Second throttle causally triggered by first.

Required prose causal chain: "When [endpoint A] hits [threshold] at [volume],
[downstream effect] because [mechanism]. This triggers [endpoint B] to receive [overflow],
hitting its [threshold]."

**ROLE 8b — 5x ARITHMETIC DERIVATION**

Threshold, 5x, overflow, retry amplification, failure rate — all five steps shown.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

SCHEMA-M table, one row per BP-xx / RH-xx. AFTER STATE names specific action, setting,
or pattern.

**Gate 8→9:** SCHEMA-A in 8a with causal chain. 5x arithmetic in 8b. SCHEMA-M in 8c with
specific AFTER STATE cells.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R19

This invariant is named FNMI-R19 and governs the Terminal Reconciler (Role 9) that follows.

(a) After this invariant is declared, no REVISED markers may be inserted into Roles 1–8.
(b) The Terminal Reconciler does not insert REVISED markers into Roles 1–8.
(c) The Terminal Reconciler inserts zero (0) REVISED markers.
(d) Any REVISED marker insertion by Role 9 is a FNMI-R19 VIOLATION:
    `FNMI-R19: VIOLATION at [reference] — [description]`.
    Absence: `FNMI-R19: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R19 declared. Role 8 deliverables present.

VERIFICATION-ONLY per FNMI-R19. Perform five checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Findings: "Gate Audit: N/N gates pass, M gate(s) with missing deliverables: [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — SCHEMA PRODUCTION REGISTRY AUDIT**

Audit the Schema Production Registry in Role 2 in two planes:

- e.1: Count registry rows. Count table-producing roles in this document (roles that
       produce SCHEMA-A, SCHEMA-V, SCHEMA-M, or SCHEMA-B output). If registry row count
       ≠ producing role count: REGISTRY GAP violation. Report: row count, producing role
       count, and which role(s) are missing from the registry.
- e.2: For each registry row, confirm the gate condition column is filled. An empty gate
       condition cell means the production responsibility is declared without a governance
       gate — report as REGISTRY GATE GAP for that row.
- e.3: For each schema body entry, confirm it has a matching registry row. A schema body
       entry with no registry row is an ORPHANED SCHEMA — report its name. This is distinct
       from a REGISTRY GAP (a producing role with no registry row).

Findings: "Registry Audit: N rows counted, M producing role(s) identified; REGISTRY GAP:
[list or none]; REGISTRY GATE GAP: [list or none]; ORPHANED SCHEMA: [list or none]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R19: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-03

**Axis:** Lifecycle emphasis — Role 3 is expanded to produce a BURST PATH TABLE: a dedicated
named table with ENDPOINT NAME and SCHEMA-A BASELINE SOURCE columns that serves as the
single authoritative source for all downstream BASELINE definitions. The Format Contract's
BASELINE definition references this table by name and column rather than independently
citing a Finding ID. Bidirectional traceability is required: each BASELINE definition names
the BURST PATH TABLE column it draws from (forward); the SCHEMA-A BASELINE SOURCE column
is named for the schema it feeds (backward).

**Hypothesis:** The BURST PATH TABLE concentrates endpoint identity authority. When multiple
downstream roles each define BASELINE using the BURST PATH TABLE as their single source,
endpoint identity ambiguity is eliminated: there is one place that names each endpoint and
one column that anchors the BASELINE measurement. The bidirectionality requirement makes
the anchor verifiable in both directions — a reader can go from a Format Contract BASELINE
definition to the table column (forward) and from the table column name to the schema it
serves (backward). A Format Contract that cites individual Finding IDs from Role 3 satisfies
C-41 but disperses authority; the BURST PATH TABLE concentrates it.

---

You are a Connectors / Power Automate throughput domain expert executing the `flow-ratelimit`
skill. Simulate throughput across rate-limited systems.

**SCENARIO:** {scenario}

Execute the following roles in sequence. Do not begin a role until its gate condition is
fully satisfied.

---

### ROLE 1 — VERDICT BLOCK

State the following four claims before any rate limit inventory, burst path audit, cascade
analysis, UX description, or volume mapping begins.

(a) **Binding constraint:** connector endpoint or platform limit hit first, with numeric
    threshold.
(b) **Primary gap:** specific action or burst path where protection is absent.
(c) **System status at stated load:** SAFE / DEGRADED / FAILING.
(d) **UX coverage commitment:** "N tiers described; all tiers use the four-field UX
    template (FIELD-A through FIELD-D)."

Self-containment: a reader of only this block knows the core finding, primary gap, system
status, and UX coverage scope.

**Revision rule:** any analysis role that revises a Verdict claim inserts an inline
`REVISED — see Role N` marker at that role's gate boundary.

**Gate 1→2:** All four claims written. No analysis has appeared yet.

---

### ROLE 2 — FORMAT CONTRACT

This section declares all structural schemas governing output in Roles 3–8.

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 7 quantified impact at load spike; Role 8a cascade failure analysis.

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: the connector API call volume at the BURST PATH TABLE endpoint identified in
  Role 3's BURST PATH TABLE, SCHEMA-A BASELINE SOURCE column — measured at burst onset,
  before any mitigation prescribed in Role 8c. The BURST PATH TABLE is the authoritative
  source for this definition: BASELINE is not independently anchored to a Finding ID; it
  is anchored to the BURST PATH TABLE row for the endpoint named in Verdict Claim (a).
  Forward traceability: this definition names the BURST PATH TABLE and the specific column
  (SCHEMA-A BASELINE SOURCE) it draws from.
- PROTECTED: sustained throughput at the same BURST PATH TABLE endpoint after Role 8c
  mitigation for the burst path is applied and active.
- DERIVATION CHAIN: step-by-step arithmetic. Bare conclusions are SCHEMA-A CONTENT
  violations.

Rejection clauses:
- SCHEMA-A STRUCTURAL: table missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell without computation steps.
- SCHEMA-A BASELINE SOURCE VIOLATION: a BASELINE cell references a Finding ID directly
  rather than routing through the BURST PATH TABLE. Detectable by checking whether the
  cell names the BURST PATH TABLE by name or names a Finding ID directly.

---

**SCHEMA-V — VOLUME MAPPING** (volume-to-behavior mapping table)

Applies to: Role 6 volume-to-behavior mapping.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- VOLUME RANGE: named volume band derived from the threshold in Verdict Claim (a).
- BASELINE BEHAVIOR: system behavior without mitigation, for the BURST PATH TABLE endpoint.
- PROTECTED BEHAVIOR: system behavior with Role 8c mitigation active.
- Delta: quantified improvement. Generic labels are SCHEMA-V CONTENT violations.

Rejection clauses:
- SCHEMA-V STRUCTURAL: missing declared column headers.
- SCHEMA-V CONTENT: Delta cell without quantified value.

---

**SCHEMA-M — MITIGATION RECORD** (per-finding mitigation tables)

Applies to: Role 8c per-finding mitigation prescriptions.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- FINDING ID: BP-xx from Role 3's BURST PATH TABLE or RH-xx from Role 5.
- BEFORE STATE: unmitigated behavior — names component, volume condition, failure mode.
- AFTER STATE: mitigated behavior — names specific action, setting, or pattern.
- Addresses: BP-xx burst paths from BURST PATH TABLE covered by this mitigation.

Rejection clauses:
- SCHEMA-M STRUCTURAL: missing declared column headers.
- SCHEMA-M CONTENT: BEFORE STATE or AFTER STATE is generic.

---

**SCHEMA-B — UX TIER BLOCK TEMPLATE** (UX per throttle tier)

Applies to: Role 5.

```
FIELD-A ERROR SIGNAL: [specific signal]
FIELD-B USER-VISIBLE BEHAVIOR: [specific user-visible state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific recovery step]
```

Rejection clauses:
- SCHEMA-B STRUCTURAL: missing FIELD labels.
- SCHEMA-B CONTENT: non-answer in any field.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching its declared schema type is
a FORMAT-SCHEMA MISMATCH violation.

**Gate 2→3:** All schemas declared with BURST PATH TABLE anchoring in SCHEMA-A BASELINE
definition. Bidirectionality requirement stated (forward: definition → table column;
backward: column named for schema). No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint — must match the endpoint name that will appear in the
   BURST PATH TABLE.
3. State the trigger condition.
4. Classify as STRUCTURAL or INCIDENTAL.
5. For STRUCTURAL: state why architectural redesign is required.
6. For INCIDENTAL: state the specific change that removes the burst.

After classifying all burst paths, produce the **BURST PATH TABLE**:

| BP ID | ENDPOINT NAME | BURST TYPE | TRIGGER CONDITION | SCHEMA-A BASELINE SOURCE |
|-------|---------------|------------|-------------------|--------------------------|
| BP-01 | [connector endpoint name] | STRUCTURAL / INCIDENTAL | [trigger] | [baseline measurement value and unit — this cell is the authoritative source for SCHEMA-A BASELINE column values referencing this row] |

**BURST PATH TABLE requirements:**
- Column ENDPOINT NAME: the canonical name of the connector endpoint. Every downstream
  reference to this endpoint uses this name exactly.
- Column SCHEMA-A BASELINE SOURCE: the baseline measurement (volume at burst onset) for
  this endpoint. This is the authoritative value that Format Contract BASELINE definitions
  draw from. The column name "SCHEMA-A BASELINE SOURCE" is named for the schema it feeds —
  this is the backward traceability anchor.
- The table must have at least one row per burst path identified above.
- Forward traceability: every Format Contract BASELINE definition names this table and the
  SCHEMA-A BASELINE SOURCE column as its source.
- Backward traceability: the SCHEMA-A BASELINE SOURCE column name identifies the schema
  it feeds. A reader can go from the column name to SCHEMA-A in the Format Contract.

Record total burst path count as B.

If Verdict Claim (a)'s endpoint does not appear as the ENDPOINT NAME in the BURST PATH
TABLE's primary burst row, insert `REVISED — see Role 3` on Claim (a).

**Gate 3→4:** At least one STRUCTURAL burst path. BURST PATH TABLE present with ENDPOINT
NAME and SCHEMA-A BASELINE SOURCE columns. Finding IDs assigned. Total count B recorded.
Bidirectionality verifiable: SCHEMA-A BASELINE SOURCE column name identifies the target
schema.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

For each tier:
1. Scope: per-connection / per-user / per-tenant / global / platform.
2. Numeric threshold and time window.
3. Enforcing layer.
4. Map to BP-xx Finding IDs from Role 3's BURST PATH TABLE.
5. Scope-distinction check.

At least three structurally distinct tiers. Threshold in Verdict Claim (a) must appear.

**Gate 4→5:** Three structurally distinct tiers, mapped to BURST PATH TABLE BP-xx IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier, SCHEMA-B block. Gate items (a)–(f). Tier count equals B from Role 3.
At least two tiers with distinct FIELD-B descriptions.

**Gate 5→6:** All B tiers complete. Six-item gate satisfied per tier.

---

### ROLE 6 — VOLUME-TO-BEHAVIOR MAPPING

SCHEMA-V table, three volume ranges including 5x spike. BASELINE BEHAVIOR draws from the
BURST PATH TABLE SCHEMA-A BASELINE SOURCE column value for the primary burst path. Delta
cells quantified.

**Gate 6→7:** SCHEMA-V with three rows, quantified Deltas, derived 5x spike, BASELINE
BEHAVIOR sourced from BURST PATH TABLE.

---

### ROLE 7 — QUANTIFIED IMPACT AT LOAD SPIKE

SCHEMA-A table at 5x load.

BURST PATH TABLE anchor enforcement: BASELINE cell must state the BURST PATH TABLE row it
draws from (e.g., "BURST PATH TABLE / BP-01 / SCHEMA-A BASELINE SOURCE: [value]"). Direct
Finding ID citation without routing through the BURST PATH TABLE is a SCHEMA-A BASELINE
SOURCE VIOLATION.

The table must show:
- BASELINE: sourced from BURST PATH TABLE SCHEMA-A BASELINE SOURCE column, BP-xx row.
- PROTECTED: sustained throughput after Role 8c mitigation.
- DERIVATION CHAIN: four-step arithmetic: (i) × 5, (ii) − threshold, (iii) × retry factor,
  (iv) ÷ threshold.

Follow with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A with BURST PATH TABLE-anchored BASELINE cell and four-step DERIVATION
CHAIN. Compounding prose present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

SCHEMA-A table for cascade. BASELINE sourced from BURST PATH TABLE. Causal chain in
DERIVATION CHAIN. Required prose causal chain statement.

**ROLE 8b — 5x ARITHMETIC DERIVATION**

Five steps: threshold, 5x, overflow, retry amplification, failure rate.

**ROLE 8c — PER-FINDING-ID MITIGATIONS**

SCHEMA-M table. FINDING IDs match BURST PATH TABLE rows (BP-xx) or Role 5 retry gaps
(RH-xx). AFTER STATE names specific action, setting, or pattern.

**Gate 8→9:** SCHEMA-A in 8a with BURST PATH TABLE-anchored BASELINE and causal chain.
5x arithmetic in 8b. SCHEMA-M in 8c with specific AFTER STATE cells.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R19

This invariant is named FNMI-R19 and governs the Terminal Reconciler (Role 9).

(a) No REVISED markers after this point into Roles 1–8.
(b) Role 9 does not insert REVISED markers into Roles 1–8.
(c) Role 9 inserts zero (0) REVISED markers.
(d) FNMI-R19 VIOLATION: `FNMI-R19: VIOLATION at [reference] — [description]`.
    Compliance: `FNMI-R19: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R19 declared. Role 8 deliverables present.

VERIFICATION-ONLY. Five checks.

**CHECK (a) — VERDICT REVISION MARKER AUDIT**
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b) — GATE DELIVERABLE AUDIT**
Findings: "Gate Audit: N/N gates pass, M gap(s): [list]"

**CHECK (c) — DERIVATION CHAIN CELL AUDIT**
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d) — SCHEMA-B STRUCTURAL SCAN**
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — BURST PATH TABLE BIDIRECTIONALITY AUDIT**

Audit the BURST PATH TABLE and Format Contract BASELINE definitions:

- e.1: Does Role 3 contain a table named BURST PATH TABLE? If not: BURST PATH TABLE ABSENT
       violation — all downstream BASELINE definitions are unanchored.
- e.2: Does the BURST PATH TABLE have a column named SCHEMA-A BASELINE SOURCE? If not:
       BACKWARD TRACEABILITY ABSENT violation — the table cannot be linked to the schema
       it feeds without reading column names.
- e.3: For each Format Contract BASELINE definition (SCHEMA-A): does it name the BURST
       PATH TABLE and the SCHEMA-A BASELINE SOURCE column as its source? If not:
       FORWARD TRACEABILITY ABSENT violation — the definition is independently anchored
       (C-41 satisfied) but not table-routed (C-45 not satisfied).
- e.4: For each SCHEMA-A table in Roles 7 and 8a: does the BASELINE cell name the BURST
       PATH TABLE row it draws from rather than citing a Finding ID directly? If a BASELINE
       cell cites a Finding ID directly without routing through the BURST PATH TABLE:
       SCHEMA-A BASELINE SOURCE VIOLATION — report cell location and the direct citation.

Findings: "Burst Path Table Audit: BURST PATH TABLE present [Y/N]; SCHEMA-A BASELINE SOURCE
column present [Y/N]; Forward traceability: [PASS/FAIL — description]; Cell-level routing:
N BASELINE cells checked, M SCHEMA-A BASELINE SOURCE VIOLATION(s): [list]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e): [findings output]
- FNMI-R19: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-04

**Axis:** Role sequence + output format — combines V-01's SCHEMA-A CELL ANCHOR pattern
(C-43) with V-02's Schema Production Registry (C-44). The Format Contract opens with the
Schema Production Registry, followed by schema body entries that include the CELL ANCHOR
requirement for SCHEMA-A. Role 9 CHECK (e) audits two planes: Plane 1 (registry
completeness) and Plane 2 (cell-level anchor with violation-class distinction).

**Hypothesis:** Combining the registry and cell anchor in one variation tests whether the
two mechanisms reinforce each other. The registry makes role-to-schema coverage verifiable
at O(1); the cell anchor makes each measurement verifiable against a specific upstream
artifact. Together they close two distinct traceability gaps: schema-to-role mapping
(registry) and cell-to-artifact linkage (cell anchor). A two-plane CHECK (e) audits both
simultaneously, producing a findings summary that separates structural gaps (REGISTRY GAP)
from semantic gaps (UNRESOLVED REFERENCE).

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

Placed before schema body entries. Registry completeness rule: registry row count must equal
table-producing role count. Missing row = REGISTRY GAP violation (detectable by count
comparison alone).

| SCHEMA NAME | PRODUCING ROLE(S) | TABLE TYPE | GATE CONDITION |
|-------------|-------------------|------------|----------------|
| SCHEMA-A | Role 7; Role 8a | quantified impact / cascade failure | Gate 7→8; Gate 8→9 |
| SCHEMA-V | Role 6 | volume-to-behavior mapping | Gate 6→7 |
| SCHEMA-M | Role 8c | per-finding mitigation record | Gate 8→9 |
| SCHEMA-B | Role 5 | UX tier block | Gate 5→6 |

Per-entry annotations below remain required. The registry provides aggregate coverage
verification; per-entry annotations provide per-entry governance confirmation.

---

#### SCHEMA BODY ENTRIES

**SCHEMA-A — PRIMARY ANALYSIS**

Applies to: Role 7 quantified impact; Role 8a cascade failure.

| BASELINE | PROTECTED | DERIVATION CHAIN |

- BASELINE: connector API call volume at the burst-path source endpoint identified by
  Finding ID in Role 3 (BP-xx), measured at burst onset, before mitigation. This definition
  is anchored to the specific Finding ID produced in Role 3 — not a generic "before" state.
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
A check that enforces prefix presence without distinguishing these classes does not fully
satisfy C-43.

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
FIELD-B USER-VISIBLE BEHAVIOR: [specific state]
FIELD-C VISIBILITY LEVEL: [Silent / Banner / Modal / Blocking]
FIELD-D RECOVERY PATH: [specific recovery step]
```

Rejection clauses: SCHEMA-B STRUCTURAL, SCHEMA-B CONTENT.

---

Unified FORMAT-SCHEMA MISMATCH clause: any table not matching its declared schema type is
a FORMAT-SCHEMA MISMATCH violation.

**Gate 2→3:** Schema Production Registry present with all four rows. All schema body entries
declared. SCHEMA-A CELL ANCHOR requirement and both violation class definitions present.
No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. Assign BP-xx IDs. Classify STRUCTURAL / INCIDENTAL. Record B.

**Gate 3→4:** At least one STRUCTURAL path. BP-xx IDs assigned. B recorded.

---

### ROLE 4 — RATE LIMIT TIER INVENTORY

Three structurally distinct tiers with numeric thresholds, mapped to BP-xx IDs.

**Gate 4→5:** Three tiers identified, mapped.

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
CHAIN and in prose.

**ROLE 8b:** 5x arithmetic, five steps.

**ROLE 8c:** SCHEMA-M, one row per BP-xx / RH-xx, specific AFTER STATE cells.

**Gate 8→9:** All deliverables present with BP-xx prefixes and causal chain.

---

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R19

(a) No REVISED markers after this point into Roles 1–8.
(b)–(d) as defined in prior variations.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R19 declared. Role 8 deliverables present. VERIFICATION-ONLY.

**CHECK (a):** Verdict revision marker audit.
Findings: "Verdict Audit: N marker(s) verified, M gap(s) found"

**CHECK (b):** Gate deliverable audit.
Findings: "Gate Audit: N/N gates pass, M gap(s): [list]"

**CHECK (c):** Derivation chain cell audit.
Findings: "Derivation Chain Audit: N cells checked, M SCHEMA-A CONTENT violation(s): [list]"

**CHECK (d):** SCHEMA-B structural scan.
Findings: "Schema B Scan: N tier(s) checked, M SCHEMA-B STRUCTURAL violation(s): [list]"

**CHECK (e) — TWO-PLANE SCHEMA AUDIT**

**Plane 1 — Schema Production Registry Completeness:**

- e.1: Count registry rows in Role 2's Schema Production Registry. Count table-producing
       roles (roles that produce SCHEMA-A, SCHEMA-V, SCHEMA-M, or SCHEMA-B output).
       If row count ≠ producing role count: REGISTRY GAP violation — report which roles
       are missing from the registry.
- e.2: For each registry row, confirm gate condition column is filled. Empty gate condition:
       REGISTRY GATE GAP for that row.
- e.3: For each schema body entry, confirm it has a matching registry row. If not:
       ORPHANED SCHEMA — report schema name.

Plane 1 findings: "Registry Audit: N rows, M producing roles; REGISTRY GAP: [list or none];
REGISTRY GATE GAP: [list or none]; ORPHANED SCHEMA: [list or none]"

**Plane 2 — Schema-A Cell-Level Anchor:**

- e.4: Scan every data cell in every SCHEMA-A table (Roles 7 and 8a). For each cell,
       check that the cell opens with "BP-xx:" prefix. If missing: CELL ANCHOR violation
       (scan-time detectable). Record cell location and column name.
- e.5: For each cell with a "BP-xx:" prefix, verify the named Finding ID exists in Role 3.
       If not: UNRESOLVED REFERENCE violation (requires cross-reference). Record cell
       location, prefix claimed, and the Finding ID gap.
- e.6: Report CELL ANCHOR and UNRESOLVED REFERENCE violations with distinct labels.
       Do not merge into a single violation category.

Plane 2 findings: "Cell Anchor Audit: N cells checked, M CELL ANCHOR violation(s): [list],
P UNRESOLVED REFERENCE violation(s): [list]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e) Plane 1: [findings output]
- Check (e) Plane 2: [findings output]
- FNMI-R19: COMPLIANT / VIOLATION at [reference] — [description]

---

## V-05

**Axis:** Full integration — all three R19 criteria enforced simultaneously. The Format
Contract opens with a Schema Production Registry (C-44) followed by schema body entries
that include the CELL ANCHOR requirement (C-43). Role 3 produces a BURST PATH TABLE (C-45)
that serves as the single authoritative source for all BASELINE definitions. The Format
Contract BASELINE definition references the BURST PATH TABLE by name and column. Role 9
CHECK (e) runs a three-plane audit: Plane 1 (registry completeness), Plane 2 (BURST PATH
TABLE bidirectionality), Plane 3 (cell-level anchor with violation-class distinction at
e.4–e.6).

**Hypothesis:** The three mechanisms operate at different traceability granularities and
are non-redundant. The registry (Plane 1) ensures every table-producing role has a declared
governing schema — coverage at document structure level. The BURST PATH TABLE (Plane 2)
concentrates endpoint identity authority in one named table — coverage at baseline
definition level. The cell anchor (Plane 3) makes each individual measurement verifiable
against a specific upstream artifact — coverage at cell level. A document satisfying all
three planes closes the traceability stack from document structure (schema → role) through
baseline definition (definition → table column) down to individual cell values (cell →
Finding ID). The three-plane CHECK (e) audits each plane independently so that a partial
failure names the specific plane and granularity level that broke.

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

Self-containment: a reader of only this block knows all four items. Revision rule: inline
`REVISED — see Role N` at gate boundary.

**Gate 1→2:** All four claims written. No analysis has appeared.

---

### ROLE 2 — FORMAT CONTRACT

This section governs all tables and blocks in Roles 3–8. It opens with a Schema Production
Registry (aggregate coverage verification), followed by schema body entries (per-entry
governance + CELL ANCHOR requirements).

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
A missing row is a **REGISTRY GAP** violation detectable by count comparison alone —
no schema body entry scan required. The per-entry annotations in the body below remain
required and are not replaced by this registry. This registry provides aggregate coverage
verification; per-entry annotations provide per-entry governance confirmation.

---

#### SCHEMA BODY ENTRIES

**SCHEMA-A — PRIMARY ANALYSIS** (cascade failure tables, quantified impact tables)

Applies to: Role 7 quantified impact; Role 8a cascade failure.

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

A compliance check that reports both classes as a single violation category does not
fully distinguish format compliance from semantic validity.

Rejection clauses:
- SCHEMA-A STRUCTURAL: missing BASELINE, PROTECTED, or DERIVATION CHAIN header.
- SCHEMA-A CONTENT: DERIVATION CHAIN cell without arithmetic steps.
- SCHEMA-A CELL ANCHOR: cell missing BP-xx prefix (scan-time).
- SCHEMA-A UNRESOLVED REFERENCE: BP-xx prefix names a Finding ID not in BURST PATH TABLE
  (cross-reference required).
- SCHEMA-A BASELINE SOURCE VIOLATION: BASELINE cell cites a Finding ID directly instead
  of routing through the BURST PATH TABLE (detectable by checking whether the cell names
  the BURST PATH TABLE or names a Finding ID directly).

---

**SCHEMA-V — VOLUME MAPPING**

Applies to: Role 6.

| VOLUME RANGE | BASELINE BEHAVIOR | PROTECTED BEHAVIOR | Delta |

- VOLUME RANGE: named volume band derived from the threshold in Verdict Claim (a).
- BASELINE BEHAVIOR: system behavior without mitigation, for the primary BURST PATH TABLE
  endpoint.
- PROTECTED BEHAVIOR: system behavior with Role 8c mitigation active.
- Delta: quantified improvement.

Rejection clauses: SCHEMA-V STRUCTURAL, SCHEMA-V CONTENT.

---

**SCHEMA-M — MITIGATION RECORD**

Applies to: Role 8c.

| FINDING ID | BEFORE STATE | AFTER STATE | Addresses |

- FINDING ID: BP-xx from Role 3's BURST PATH TABLE or RH-xx from Role 5.
- BEFORE STATE: unmitigated behavior — names component, volume condition, failure mode.
- AFTER STATE: mitigated behavior — names specific action, setting, or pattern.
- Addresses: BURST PATH TABLE BP-xx paths covered.

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

**Gate 2→3:** Schema Production Registry present (4 rows, gate conditions filled). All
schema body entries declared with per-entry annotations. SCHEMA-A BASELINE definition
names BURST PATH TABLE and SCHEMA-A BASELINE SOURCE column. CELL ANCHOR requirement and
both violation classes defined. No analysis has begun.

---

### ROLE 3 — BURST PATH AUDIT

Identify all burst paths. For each:

1. Assign Finding ID: BP-01, BP-02, ... (sequential, no gaps).
2. Name the connector endpoint — canonical name used throughout the document.
3. State the trigger condition.
4. Classify as STRUCTURAL or INCIDENTAL.
5. For STRUCTURAL: state why architectural redesign is required.
6. For INCIDENTAL: state the specific change that removes the burst.

After classifying all paths, produce the **BURST PATH TABLE**:

| BP ID | ENDPOINT NAME | BURST TYPE | TRIGGER CONDITION | SCHEMA-A BASELINE SOURCE |
|-------|---------------|------------|-------------------|--------------------------|
| BP-01 | [canonical endpoint name] | STRUCTURAL / INCIDENTAL | [trigger condition] | [baseline measurement: volume at burst onset, unit] |

**BURST PATH TABLE requirements:**
- ENDPOINT NAME: canonical connector endpoint name. All downstream references use this name.
- SCHEMA-A BASELINE SOURCE: the baseline measurement for this endpoint. This is the
  authoritative value for Format Contract SCHEMA-A BASELINE definitions. The column name
  "SCHEMA-A BASELINE SOURCE" is named for the schema it feeds — this is the backward
  traceability anchor. A reader who sees this column name in the table knows it feeds
  SCHEMA-A's BASELINE column.
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

At least three structurally distinct tiers. Threshold in Verdict Claim (a) must appear here.

**Gate 4→5:** Three structurally distinct tiers, mapped to BURST PATH TABLE BP-xx IDs.

---

### ROLE 5 — UX PER THROTTLE TIER

For each tier, SCHEMA-B block. Six-item gate per block. Tier count = B from Role 3.
At least two tiers with distinct FIELD-B descriptions. Verdict-currency check on Claim (d).

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

- BASELINE: "BP-01: 3,000 req/min [5× threshold: 600 × 5]"
- PROTECTED: "BP-01: 580 req/min [concurrency cap applied]"
- DERIVATION CHAIN: "BP-01: (i) 600 × 5 = 3,000 req/min; (ii) 3,000 − 600 = 2,400 overflow;
  (iii) 2,400 × 3 retries = 7,200 total attempts; (iv) 7,200 ÷ 600 = 12× failure pressure"

A BASELINE cell that cites a Finding ID without routing through the BURST PATH TABLE is a
SCHEMA-A BASELINE SOURCE VIOLATION. A cell missing the BP-xx prefix is a CELL ANCHOR
violation. A cell whose BP-xx prefix does not match a BURST PATH TABLE row is an
UNRESOLVED REFERENCE violation.

Follow table with prose on compounding effect at T+30s and T+60s.

**Gate 7→8:** SCHEMA-A present. All cells carry BP-xx prefixes referencing BURST PATH TABLE
rows. DERIVATION CHAIN shows four-step arithmetic. Compounding prose present.

---

### ROLE 8 — CASCADE, ARITHMETIC, AND MITIGATIONS

**ROLE 8a — CASCADING FAILURE SCENARIO**

SCHEMA-A table for cascade. All cells carry BP-xx prefixes. DERIVATION CHAIN shows causal
chain. Required prose: "When [endpoint A] hits [threshold] at [volume], [downstream effect]
because [mechanism]. This triggers [endpoint B] to receive [overflow], hitting [threshold]."

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

### FORMAL NON-MODIFICATION INVARIANT — FNMI-R19

This invariant is named FNMI-R19 and governs the Terminal Reconciler (Role 9).

(a) No REVISED markers after this point into Roles 1–8.
(b) Role 9 does not insert REVISED markers into Roles 1–8.
(c) Role 9 inserts zero (0) REVISED markers.
(d) FNMI-R19 VIOLATION: `FNMI-R19: VIOLATION at [reference] — [description]`.
    Compliance: `FNMI-R19: COMPLIANT`.

---

### ROLE 9 — TERMINAL RECONCILER

Gate in: FNMI-R19 declared. All Role 8 deliverables present.

VERIFICATION-ONLY per FNMI-R19. Perform six checks.

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
does not affect the others.

**Plane 1 — Schema Production Registry Completeness (e.1–e.3):**

- e.1: Count registry rows in Role 2's Schema Production Registry. Count table-producing
       roles in this document. If row count ≠ producing role count: REGISTRY GAP violation.
       Report: registry row count, producing role count, and which role(s) are missing.
- e.2: For each registry row, confirm the gate condition column is filled. If not:
       REGISTRY GATE GAP for that specific row (report schema name).
- e.3: For each schema body entry in Role 2, confirm it has a matching registry row. If a
       schema body entry has no registry row: ORPHANED SCHEMA violation (report schema name).
       This is distinct from REGISTRY GAP: REGISTRY GAP = producing role without registry
       entry; ORPHANED SCHEMA = schema body entry without registry entry.

Plane 1 findings: "Registry Audit: N registry rows, M producing role(s); REGISTRY GAP:
[list or none]; REGISTRY GATE GAP: [list or none]; ORPHANED SCHEMA: [list or none]"

**Plane 2 — BURST PATH TABLE Bidirectionality (e.4):**

- e.4: Audit the BURST PATH TABLE in Role 3 and the Format Contract SCHEMA-A BASELINE
       definition for bidirectionality:

  Forward check: does the Format Contract SCHEMA-A BASELINE definition name the BURST
  PATH TABLE by name and the SCHEMA-A BASELINE SOURCE column by name? If not: FORWARD
  TRACEABILITY ABSENT (the definition is independently anchored, satisfying C-41 but not
  C-45).

  Backward check: does the BURST PATH TABLE contain a column named SCHEMA-A BASELINE
  SOURCE (or a column name that explicitly identifies the schema it feeds)? If not:
  BACKWARD TRACEABILITY ABSENT (the table exists but cannot be linked to its downstream
  schema by column name alone).

  Cell routing check: for each SCHEMA-A table's BASELINE cell in Roles 7 and 8a, does
  the cell route through the BURST PATH TABLE (by naming the table and row) or cite a
  Finding ID directly? Direct Finding ID citation: SCHEMA-A BASELINE SOURCE VIOLATION
  (C-41 satisfied; C-45 not satisfied).

  Report: "Burst Path Table: present [Y/N]; Forward [PASS/FAIL]; Backward [PASS/FAIL];
  Cell routing: N BASELINE cells, M SCHEMA-A BASELINE SOURCE VIOLATION(s): [list]"

Plane 2 findings: "[Burst Path Table report as above]"

**Plane 3 — Schema Cell-Level ID Anchor (e.5–e.6):**

- e.5: Scan every data cell in every SCHEMA-A table (Roles 7 and 8a). For each cell:
  - If cell does not open with "BP-xx:" prefix: CELL ANCHOR violation. Record location
    and column name. This is scan-time detectable.
  - If cell opens with "BP-xx:" prefix: proceed to e.6 for this cell.

- e.6: For each cell with a "BP-xx:" prefix, verify the named BP-xx Finding ID exists
  in Role 3's BURST PATH TABLE BP ID column.
  - If the Finding ID exists: prefix is resolved — no violation.
  - If the Finding ID does not exist in the BURST PATH TABLE: UNRESOLVED REFERENCE
    violation. Record cell location, the claimed prefix, and the gap (BP-xx not in table).

  Violation class distinction: CELL ANCHOR violations (e.5) and UNRESOLVED REFERENCE
  violations (e.6) must appear as separate named violation classes in the findings output.
  A report that merges them as "missing or invalid prefix" does not satisfy this requirement.

Plane 3 findings: "Cell Anchor Audit: N cells checked, M CELL ANCHOR violation(s): [list],
P UNRESOLVED REFERENCE violation(s): [list]; violation classes reported separately: [Y/N]"

RECONCILER FINDINGS SUMMARY:
- Check (a): [findings output]
- Check (b): [findings output]
- Check (c): [findings output]
- Check (d): [findings output]
- Check (e) Plane 1: [Plane 1 findings output]
- Check (e) Plane 2: [Plane 2 findings output]
- Check (e) Plane 3: [Plane 3 findings output]
- FNMI-R19: COMPLIANT / VIOLATION at [reference] — [description]
