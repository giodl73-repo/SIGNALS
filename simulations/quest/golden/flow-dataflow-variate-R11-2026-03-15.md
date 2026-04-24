# flow-dataflow — Round 11 Variations (Rubric v9)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v9 (C-01 through C-24, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 11 targets C-24 as the single new criterion in rubric v9. C-24 requires a
pre-declared complete output scaffold — a table appearing before the first stage trace
entry that lists every output table by table number, name, stated purpose, and upstream
table references. No table may appear for the first time mid-trace. The scaffold functions
as the navigational contract for cross-table citations required by C-15, C-16, C-18,
C-19, C-20, and C-23.

The prior high-water mark (R9) established the ARTIFACT REGISTRY pattern (A-NN tokens
covering sections), the BOUNDARY BLOCK SCHEMA (pre-declared column requirements), and
structural constraints SC-1 through SC-8. R9 did not require the scaffold to declare
upstream table references per row — the new criterion requires the dependency graph to be
declared, not just a table inventory.

**R11 Hypothesis space:**

**H1 — Scaffold-first output format (V-01)**
The scaffold table is the absolute first section of output — before domain context, before
entity inventory, before role assignments. The prompt requires: table number, table name,
stated purpose, and an "Upstream Tables" column listing which prior tables each table
references by T-NN token. The model must plan its full table dependency graph before
producing any content. Tests whether declaring upstream references per row forces the model
to reason about table dependency before filling content, producing C-16/C-18/C-20/C-23
cross-table citations that resolve against declared scaffold entries rather than ad-hoc
section names.

**H2 — Scaffold-authority role sequence (V-02)**
A designated "Scaffold Authority" pass runs before any domain expert role. It produces
only the scaffold table and is explicitly forbidden from producing any domain content.
Domain roles that follow are forbidden from introducing any table not listed in the
scaffold. Tests whether separating the scaffold declaration into its own role-pass produces
a more complete upstream-reference dependency graph — the Scaffold Authority must reason
about all downstream roles' outputs before any role begins content.

**H3 — Protocol-contract phrasing register (V-03)**
The scaffold enforcement is written in formal protocol-contract language (SHALL, MUST, IS
REQUIRED, SCAFFOLD VIOLATION). Each section references its scaffold registration by T-NN
token in its header. Tests whether protocol-contract phrasing makes scaffold compliance a
structural prerequisite rather than a formatting suggestion, and whether per-section token
headers drive consistent cross-table citation behavior.

**H4 — Combined: scaffold + boundary-first lifecycle (V-04)**
Combines H1 (scaffold-first format) with a boundary-centric lifecycle where boundaries are
first-class scaffold entries registered in the scaffold table before stage bodies. The
scaffold must declare both stage tables and boundary tables, each with their upstream refs.
Tests whether pre-registering boundaries as T-NN entries in the scaffold forces complete
C-11 boundary labeling and C-17 entity-at-risk annotations to resolve against the scaffold
rather than being generated ad-hoc mid-trace.

**H5 — Combined: scaffold + inertia-first role sequence (V-05)**
Combines scaffold-first format with an inertia-first role sequence: Operations runs first
and must declare the incumbent baseline as T-01 before any pipeline stage is traced.
Finance and Commerce are explicitly forbidden from producing tables not listed in the
Operations-declared scaffold. Tests whether anchoring T-01 = INCUMBENT BASELINE at the
scaffold level (before any pipeline stage) drives full C-14/C-15/C-16 traceability, since
every recovery entry that cites T-01 is resolved against a table pre-declared in the
scaffold's dependency graph.

**Axes selected for R11:**

1. **Scaffold-first output format** — scaffold table as absolute first section, with
   upstream table references column (single axis: V-01)
2. **Scaffold-authority role sequence** — designated pre-content Scaffold Authority pass
   producing only the scaffold; domain roles forbidden from undeclared tables (single axis:
   V-02)
3. **Protocol-contract phrasing** — formal imperative scaffold enforcement with T-NN token
   headers per section (single axis: V-03)
4. **Combined (H1 + H4)** — scaffold-first format + boundary-first lifecycle with
   boundaries as pre-registered scaffold entries (V-04)
5. **Combined (H1 + H5)** — scaffold-first format + inertia-first role sequence with
   incumbent baseline as T-01 (V-05)

**New signal candidates for R11:**

1. **Upstream reference completeness** (V-01, V-02, V-04, V-05) — whether the model
   populates the "Upstream Tables" column with specific T-NN tokens vs "none" for tables
   that structurally depend on prior tables. Success signal: recovery audit table row
   declares `T-03, T-04` as upstream references (stage tables and boundary table); closure
   gate declares `T-05` (recovery audit) as its upstream reference. Failure signal: all
   rows in the "Upstream Tables" column contain "none" or prose descriptions instead of
   T-NN tokens.

2. **Mid-trace table prevention** (all variations) — whether any table appears for the
   first time after the scaffold section. Success signal: every table produced in the body
   has an exact T-NN match in the scaffold. Failure signal: a new table introduced in
   the recovery section or closure gate whose name does not match any scaffold row.

3. **Scaffold-authority separation** (V-02) — whether the Scaffold Authority pass
   produces domain content (domain context, entity vocabulary) or limits itself to the
   dependency graph. Success signal: Scaffold Authority produces only the T-NN table with
   names, purposes, and upstream refs — no entity vocabulary, no SLA values. Failure
   signal: Scaffold Authority produces domain context inline with the scaffold table.

4. **Boundary pre-registration quality** (V-04) — whether boundaries declared in the
   scaffold as T-NN entries receive more complete C-11 labeling (B1->2 format) and C-17
   entity-at-risk annotations than variations where boundaries are not pre-registered.
   Success signal: every boundary label in the body matches a pre-declared scaffold entry.
   Failure signal: boundary table produced in body has more rows than scaffold declared.

---

## V-01 — Scaffold-First Output Format

**Variation axis**: Output format — the OUTPUT TABLE SCAFFOLD is the absolute first
section of the response, before domain context, entity inventory, or any role content
begins. The scaffold declares every output table by table number, name, stated purpose,
and upstream table references. No table may appear in the body that was not declared here.

**Hypothesis**: Placing the scaffold as the literal first output forces the model to
enumerate its complete table dependency graph before generating any content. When the
"Upstream Tables" column requires T-NN citations, the model builds the cross-reference
surface for C-15/C-16/C-18/C-19/C-20/C-23 before filling it in. Predicts complete C-24
compliance (all body tables resolve to scaffold entries) and improved cross-table citation
quality in the recovery audit and closure gate sections.

Scenario: Finance — SaaS revenue recognition pipeline. Billing events from a subscription
management platform flow through revenue schedule generation, VSOE allocation, deferred
revenue waterfall, and ASC 606 GL posting to the revenue subledger and consolidated
financial statements. Stages: Billing Event Capture => Revenue Schedule Generation =>
VSOE Allocation => Deferred Revenue Waterfall => GL Revenue Posting => Financial
Consolidation Sync.

---

You are a Finance data domain expert tracing data through a SaaS revenue recognition
pipeline — subscription billing events through revenue schedule generation, VSOE
allocation, deferred revenue waterfall, and ASC 606 general ledger posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### STEP 0 — OUTPUT TABLE SCAFFOLD

**This section must appear first, before any domain context, entity inventory, or stage
trace.** It is the navigational contract for this entire response.

Declare every table that will appear anywhere in this response. A table that first appears
after this scaffold is an undeclared artifact and constitutes a structural gap. No table
may be added mid-response after this section is complete.

Produce the scaffold as the following four-column table. Every row represents one table
that will appear in this response:

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | [table name] | [one sentence: what this table contains and which C-criterion it satisfies] | [comma-separated T-NN tokens this table draws data from, or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

**Minimum required scaffold entries** (add rows for any additional tables you produce):
- Incumbent Baseline Table — satisfies C-15
- Entity Inventory Table — satisfies C-10
- Stage Trace Table for each stage (one per stage) — satisfies C-04, C-19
- Boundary Inventory Table — satisfies C-11, C-17, C-21, C-22
- Recovery Audit Table — satisfies C-18, C-16
- Closure Gate Table — satisfies C-23

**Upstream Tables column rules**: If this table draws data from, extends, or references
another declared table, list those tables by T-NN token (e.g., `T-02, T-04`). "none" is
only valid if no prior table is referenced. The Recovery Audit Table must declare the
Boundary Inventory Table and all Stage Trace Tables as upstream references. The Closure
Gate Table must declare the Recovery Audit Table as an upstream reference.

**Citation rule**: Every cross-table reference in this response must use the T-NN token
from this scaffold. A reference to a table by prose name alone (without the T-NN token)
is not a resolvable citation. A T-NN token cited in a cross-table reference that does not
appear in this scaffold is an invalid citation.

---

### SECTION 1 — INCUMBENT BASELINE TABLE (T-01)

Document the manual revenue recognition and reporting process this pipeline replaces. This
is T-01 from the scaffold — begin this section with the header `[T-01] INCUMBENT BASELINE
TABLE`.

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step name] | [revenue accountant / controller / etc.] | [time] |
| ... | ... | ... | ... |

**Minimum five distinct manual steps** specific to revenue recognition operations (e.g.,
`MS-01: Revenue accountant exports billing events from Salesforce CPQ to Excel and manually
maps each contract line to an ASC 606 performance obligation — 3.5 hrs per close cycle`).
Generic workflow steps not grounded in revenue accounting do not qualify.

State after the table:
- **INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution).
  Fixed at declaration; may not be revised.
- **Citation rule**: cite steps by Step ID (MS-NN) in all recovery entries in T-07.
  A recovery entry without an MS-NN citation fails C-16.

---

### SECTION 2 — DOMAIN CONTEXT AND ENTITY INVENTORY (T-02)

Enumerate all in-scope domain entities. Begin this section with `[T-02] ENTITY INVENTORY`.

Present as a table:

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

**Required entities**: BillingEvent, RevenueSchedule, VSOEAllocation, DeferredRevenue,
GLRevenueEntry, ConsolidationPackage.

State the following **SLA declaration** immediately after the table (immutable — cite this
by section reference in all downstream latency comparisons; do not re-derive):
- **Close cycle SLA**: maximum elapsed time from billing event capture to GL revenue
  posting within the monthly close window (numeric, in hours)
- **Billing volume assumption**: events per day at peak close period

---

### SECTION 3 — STAGE TRACE WITH TYPED EXIT MANIFESTS

For each stage, produce one stage table (each stage table is a T-NN entry from the
scaffold — begin each with `[T-NN] STAGE TRACE — Stage N: [Stage Name]`).

**Required columns per stage table**:

| Field | Type | Schema Delta | Data Loss Risk | Stage Latency |
|-------|------|-------------|----------------|---------------|

- **Field + Type**: field name and type at stage exit using `field_name: TYPE(precision)`.
  List all fields present at stage exit.
- **Schema Delta**: `ADDED field_name: TYPE` / `RENAMED old→new: TYPE` /
  `REMOVED field_name` / `RETYPED field_name from TYPE to TYPE`. If no change:
  `NONE — verified: no field added, removed, renamed, or retyped`.
- **Data Loss Risk**: assign LP-NN identifier at declaration. Concrete failure only.
  Example: `LP-01: BillingEvents with null contract_id silently excluded from
  RevenueSchedule — orphaned revenue not recognized in current period`. "Errors may occur"
  does not qualify.
- **Stage Latency**: value, range, or characterization (real-time / near-real-time / batch
  / daily). May not be omitted.

After each stage table, produce a **Typed Exit Manifest**:

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count at exit]
  key field assertions:
    [field_name: TYPE(precision)]
    [field_name: TYPE(precision)]
    [minimum two assertions per entity]
```

The exit manifest is the sole authority for field names and types available to downstream
boundary annotations. A boundary annotation citing a field not present in the upstream
exit manifest is an invalid citation.

**Stages**:
1. Billing Event Capture — subscription platform → revenue engine intake queue
2. Revenue Schedule Generation — revenue engine → schedule service
3. VSOE Allocation — schedule service → allocation engine
4. Deferred Revenue Waterfall — allocation engine → deferred revenue ledger
5. GL Revenue Posting — deferred revenue ledger → GL subledger
6. Financial Consolidation Sync — GL subledger → consolidation platform

**NH-NN format rule**: when a stage or boundary has no error-handling mechanism, declare
as `NH-01: no handling — risk accepted at [location]`. Assign sequentially at first
occurrence; cite by NH-NN in T-07 (Recovery Audit Table).

---

### SECTION 4 — BOUNDARY INVENTORY TABLE (T-[N])

This is the Boundary Inventory Table declared in the scaffold. Begin this section with
`[T-NN] BOUNDARY INVENTORY TABLE`.

Produce one row per inter-stage boundary. All nine columns are required — a row with any
blank cell is a structural gap.

| Boundary | Error Handling | Schema Change | Entity at Risk | Transport Latency (ms) | Processing Overhead (ms) | Total Latency (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|---------------|----------------|----------------------|------------------------|------------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

**Column rules**:
- **Error Handling**: named mechanism (retry, dead-letter, rollback) or
  `NH-NN: no handling — risk accepted`. Silence fails.
- **Schema Change**: `Y — [named changes]` or `N — verified unchanged`.
- **Entity at Risk**: `entity.field_name — risk description`, where entity is from T-02
  and field_name is from the upstream exit manifest. Entity-only annotations (no field)
  fail C-20. Generic "data" or "records" fails C-17.
- **Transport Latency**: network transit, queue depth, serialization overhead — numeric
  ms estimate. "Negligible" is not acceptable.
- **Processing Overhead**: computation, enrichment, transformation, I/O — numeric ms
  estimate. "Negligible" is not acceptable.
- **Total Latency**: must equal Transport + Processing Overhead.
- **SLA% This Boundary**: fraction of close cycle SLA consumed at this boundary alone.
- **Cumulative SLA%**: running total from B1 through this boundary.

After the table, state:
**DOMINATION POINT**: boundary label where Cumulative SLA% first exceeds 50% of the
declared SLA, the exact cumulative percentage at that crossing, and a one-sentence
justification. If the cumulative total never reaches 50%, state that explicitly.

---

### SECTION 5 — STALE WINDOW ANALYSIS

Accumulate stage latencies (Section 3) and boundary latencies (Section 4) sequentially,
showing Transport and Processing Overhead addends separately at each boundary step:

- After Stage 1: [elapsed]
- After B1->2: [elapsed — Transport: X ms + Processing: Y ms = Z ms cumulative]
- After Stage 2: [elapsed]
- ... continue through Stage 6 ...

Identify the single largest contributor by label (stage or boundary). State whether the
dominant contributor is Transport Latency or Processing Overhead.

Compare final accumulated total against the close cycle SLA from Section 2 under:
1. **Normal operation**: FRESH or STALE with elapsed value
2. **Worst-case failure mode** (name the failure, cite LP-NN or NH-NN): FRESH or STALE

---

### SECTION 6 — RECOVERY AUDIT TABLE (T-[N])

Begin with `[T-NN] RECOVERY AUDIT TABLE`. Cite upstream tables by T-NN as declared in
the scaffold.

Produce one row for every NH-NN and every LP-NN declared in Sections 3 and 4. All five
columns are required — a missing row for any declared identifier is a structural gap.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

Every recovery mechanism must name a specific action at a specific boundary or stage.
Every entry must cite an MS-NN step from T-01. Generic "manual review" without a named
incumbent step does not satisfy C-16.

---

### SECTION 7 — CLOSURE GATE TABLE (T-[N])

Begin with `[T-NN] CLOSURE GATE TABLE`. This section is **structurally separate** from
T-[N-1] (Recovery Audit Table) and must appear after it.

Enumerate every declared identifier (all NH-NN and LP-NN from Sections 3 and 4)
independently — do not derive this list from the Recovery Audit Table. Check each against
the Recovery Audit Table.

| Identifier | Source (stage or boundary) | Recovery Row Present (YES/NO) | Status (CLOSED/OPEN) |
|------------|---------------------------|-------------------------------|----------------------|

An OPEN status means the identifier has no recovery row — a structural deficit. Every
identifier must appear in this table; a count summary ("5 of 6 covered") does not qualify.

---

### SECTION 8 — PATTERN ASSESSMENT

Name the integration pattern (event-driven async, CDC stream, synchronous API chain,
dual-write, etc.). Name one alternative pattern. State at least two trade-off dimensions,
at least one quantified or qualified in Finance / revenue recognition terms (e.g.,
"synchronous VSOE validation adds ~2.1 s per billing event but eliminates ~0.12% of
misallocated revenue risk estimated at peak contract renewal volume").

---

*Scaffold contract: The scaffold in Step 0 is a binding contract. Every table must appear
in the scaffold before appearing in the body. Every cross-table citation must use a T-NN
token resolvable against the scaffold. A table introduced mid-response without a scaffold
entry is a protocol gap. Complete every table — no blank cells, no "negligible" in numeric
latency columns.*

---

## V-02 — Scaffold-Authority Role Sequence

**Variation axis**: Role sequence — a designated Scaffold Authority pass runs before any
domain expert role begins. The Scaffold Authority produces only the OUTPUT TABLE SCAFFOLD
and is explicitly forbidden from producing any domain content. Domain roles (Finance,
Operations, Commerce) run after and are forbidden from introducing any table not registered
in the scaffold. Scaffold Authority → Finance → Operations → Commerce.

**Hypothesis**: Separating the scaffold declaration into its own role pass forces the model
to reason about all downstream roles' table outputs before any domain content is written.
The "forbidden from undeclared tables" constraint on domain roles prevents mid-trace table
introductions and creates structural pressure to declare the full dependency graph upfront.
Predicts that the Scaffold Authority produces a more complete upstream-reference graph than
a self-scaffolded Finance role, because the Scaffold Authority must consider Operations and
Commerce table needs simultaneously before domain framing narrows attention.

Scenario: Operations — DC-to-store inventory replenishment sync. Purchase order receipts
at the distribution center flow through receiving confirmation, put-away validation, and
a nightly replenishment calculation that dispatches store transfer orders and updates
store-level stock-on-hand records. Stages: DC Receiving Confirmation => Put-Away
Validation => Replenishment Calculation => Store Transfer Dispatch => Store SOH Update =>
Commerce Platform Sync.

---

You are tracing data through a DC-to-store inventory replenishment pipeline. Three expert
roles run in the sequence **Scaffold Authority → Finance → Operations → Commerce**. Roles
run in this order and may not be reordered.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### SCAFFOLD AUTHORITY PASS

**The Scaffold Authority produces ONLY the OUTPUT TABLE SCAFFOLD below. It may not produce
domain context, entity vocabulary, SLA values, stage content, or any table other than the
scaffold itself. Domain content begins only after the scaffold is complete.**

Produce the scaffold as the following four-column table. Every table that will appear
anywhere in this response must have a row here. No domain role may produce a table not
registered in this scaffold:

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | [table name] | [purpose and criterion satisfied] | [T-NN references or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

**Required scaffold entries** (declare in dependency order — tables with no upstream
references first; tables that depend on prior tables after):
- Incumbent Baseline Table (satisfies C-15) — no upstream references
- Entity Inventory Table (satisfies C-10) — no upstream references
- One Stage Trace Table per stage (satisfies C-04, C-19) — upstream: Entity Inventory Table
- Boundary Inventory Table (satisfies C-11, C-17, C-21, C-22) — upstream: all Stage Trace Tables
- Recovery Audit Table (satisfies C-18, C-16) — upstream: Boundary Inventory Table, all Stage Trace Tables, Incumbent Baseline Table
- Closure Gate Table (satisfies C-23) — upstream: Recovery Audit Table

**Dependency order enforcement**: declare tables with no upstream references before tables
that reference them. A row in the scaffold that cites a T-NN token that has not yet
appeared earlier in the scaffold table is an out-of-order declaration — move it to the
correct position.

After the scaffold, state: `SCAFFOLD CLOSED — [N] tables declared. No domain role may
produce an undeclared table. Proceed to Finance.`

---

### ROLE 1 — Finance

Finance establishes the staleness threshold and incumbent baseline. **Finance may not
produce any table not registered in the Scaffold Authority scaffold.**

Begin with `Citing scaffold entries: [list T-NN tokens this role will produce]`.

**[T-01] INCUMBENT BASELINE TABLE**

Document the manual replenishment process this pipeline replaces:

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step name] | [DC supervisor / buyer / etc.] | [time] |
| ... | ... | ... | ... |

**Minimum five distinct steps** specific to DC-to-store replenishment operations (e.g.,
`MS-01: DC receiving supervisor manually counts pallets against ASN and enters quantities
into WMS — 45 min per truck`). Generic steps do not qualify.

State:
- **INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.
- **Replenishment SLA**: maximum elapsed time from DC receiving confirmation to store
  SOH update visible to the Commerce platform (numeric, in hours). Fixed at declaration —
  Operations and Commerce must cite this value by section reference; they may not
  re-declare or adjust it.

**[T-02] ENTITY INVENTORY TABLE**

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

Required entities: DCReceiptEvent, PutAwayRecord, ReplenishmentOrder, StoreTransferOrder,
StoreSOH, CommercePlatformInventory.

---

### ROLE 2 — Operations

Operations traces the pipeline stages and boundary conditions. **Operations may not
produce any table not registered in the Scaffold Authority scaffold.**

Begin with `Citing: T-01, T-02` (and any other prior T-NN tokens Operations draws from).

**[T-NN] STAGE TRACE — Stages 1 through 6**

For each stage, produce a stage table (using its scaffold-declared T-NN header):

| Field | Type | Schema Delta | LP-NN Loss Point | NH-NN No-Handling | Stage Latency |
|-------|------|-------------|-----------------|------------------|---------------|

**Schema Delta**: named field changes or `NONE — verified: no field added, removed,
renamed, or retyped`. A pass-through assertion without "verified" fails C-12.

**LP-NN**: assign sequential identifier at declaration. Example: `LP-01: DCReceiptEvent
records with unresolvable ASN reference written to error queue — quantity not posted to
PutAwayRecord; store replenishment calculation runs on stale SOH`. "Errors may occur"
does not qualify.

**NH-NN**: `NH-01: no handling — risk accepted at [boundary/stage name]`.

After each stage table, produce a Typed Exit Manifest:

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count]  key field assertions: [field_name: TYPE(precision), minimum two]
```

**Stages**:
1. DC Receiving Confirmation — carrier manifest → WMS receiving dock
2. Put-Away Validation — WMS receiving → put-away service
3. Replenishment Calculation — put-away service → replenishment engine
4. Store Transfer Dispatch — replenishment engine → store transfer queue
5. Store SOH Update — store transfer queue → store WMS
6. Commerce Platform Sync — store WMS → commerce inventory API

**[T-NN] BOUNDARY INVENTORY TABLE**

Produce one row per boundary. All nine columns required — blank cells are structural gaps.

| Boundary | Error Handling | Schema Change | Entity at Risk (entity.field — cite exit manifest) | Transport Latency (ms) | Processing Overhead (ms) | Total Latency (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|---------------|--------------------------------------------------|----------------------|------------------------|------------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

**Transport Latency**: numeric ms estimate — "negligible" does not qualify.
**Processing Overhead**: numeric ms estimate — "negligible" does not qualify.
**Total Latency**: must equal Transport + Processing Overhead.
**SLA%**: fraction of replenishment SLA consumed at this boundary.
**Cumulative SLA%**: running total from B1 through this boundary.

State **DOMINATION POINT** after the table: boundary where Cumulative SLA% first exceeds
50%, with the exact crossing percentage and a one-sentence justification.

---

### ROLE 3 — Commerce

Commerce performs stale window analysis, recovery audit, closure gate, and pattern
assessment. **Commerce may not produce any table not registered in the Scaffold Authority
scaffold.**

Begin with `Citing: T-01, T-02, [all stage T-NN tokens], [boundary T-NN token]`.

**Stale Window Analysis**

Accumulate stage and boundary latencies sequentially (citing Transport and Processing
Overhead addends separately at each boundary step). Compare final total against
replenishment SLA (cite by T-01 reference):
1. Normal operation: FRESH or STALE
2. Worst-case failure mode (cite LP-NN or NH-NN): FRESH or STALE

**[T-NN] RECOVERY AUDIT TABLE**

One row per NH-NN and LP-NN — all five columns required; missing rows are structural gaps.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

**[T-NN] CLOSURE GATE TABLE**

Structurally separate from the Recovery Audit Table. Enumerate all NH-NN and LP-NN
identifiers independently (not from the Recovery Audit Table rows) and check each:

| Identifier | Source | Recovery Row Present | Status |
|------------|--------|---------------------|--------|
| NH-01 | [source] | YES / NO | CLOSED / OPEN |

**Pattern Assessment**

Name the integration pattern and one alternative. State ≥2 trade-off dimensions with ≥1
quantified in supply chain / Operations terms. Cite T-01 as the comparison baseline.

---

*Scaffold contract: The Scaffold Authority declares the complete table contract before any
domain role begins. A domain role that produces an undeclared table is a scaffold
violation. A cross-table citation using a T-NN token not in the scaffold is invalid.*

---

## V-03 — Protocol-Contract Phrasing Register

**Variation axis**: Phrasing register — formal protocol-contract language (SHALL, MUST,
IS REQUIRED, SCAFFOLD VIOLATION, PROTOCOL GATE) throughout all scaffold and structural
enforcement instructions. Each body section references its scaffold registration by T-NN
token in its section header.

**Hypothesis**: Protocol-contract phrasing signals that scaffold compliance is a
structural prerequisite rather than a formatting suggestion. When each section header
cites its T-NN registration (`[T-03 — INCUMBENT BASELINE TABLE]`), the model anchors
every cross-table citation to the scaffold token. Predicts higher C-24 compliance and
more consistent T-NN citation behavior in cross-table references (C-16 incumbent step
citations, C-18 recovery table entries, C-23 closure gate status rows) than neutral
instructional phrasing.

Scenario: Commerce — promotional pricing CDX flow. Promotional price overrides from a
merchandising system flow through a pricing engine, discount validation service, CDX
publisher, and storefront cache update, finally reaching the customer-facing availability
and pricing API. Stages: Promotion Entry => Price Override Generation => Discount
Validation => CDX Publication => Storefront Cache Write => Availability API Refresh.

---

You are a Commerce data domain expert tracing data through a promotional pricing CDX
pipeline — promotional price overrides from a merchandising system through pricing engine,
discount validation, CDX publication, storefront cache, and customer-facing API.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### PROTOCOL PREAMBLE

The following structural requirements SHALL govern this entire response. Violation of any
PROTOCOL GATE constitutes a SCAFFOLD VIOLATION and MUST be resolved before proceeding.

**PROTOCOL GATE 0 — SCAFFOLD DECLARATION IS REQUIRED FIRST**
The OUTPUT TABLE SCAFFOLD SHALL be the absolute first section of output. No domain
content, entity vocabulary, stage trace, or table of any kind SHALL appear before the
scaffold. Any table produced before the scaffold is declared is a SCAFFOLD VIOLATION.

**PROTOCOL GATE 1 — SCAFFOLD REGISTRATION IS BINDING**
Every table that appears anywhere in this response SHALL have an entry in the scaffold
declared in PROTOCOL GATE 0. A table appearing in the body that cannot be resolved
against a scaffold row by T-NN token IS a SCAFFOLD VIOLATION. Undeclared tables SHALL
be treated as structural deficits, not formatting alternatives.

**PROTOCOL GATE 2 — T-NN CITATION IS REQUIRED**
Every cross-table reference in this response SHALL use the T-NN token from the scaffold.
A reference by table name alone (e.g., "the Recovery Audit Table") without a T-NN token
does not constitute a resolvable citation and SHALL NOT satisfy C-16, C-18, or C-23.

**PROTOCOL GATE 3 — SECTION HEADERS SHALL INCLUDE SCAFFOLD TOKEN**
Every section that produces a registered table SHALL begin its header with the T-NN token
in brackets: `[T-NN] SECTION NAME`. A section that produces a table without this header
violates the scaffold traceability requirement.

**PROTOCOL GATE 4 — UPSTREAM REFERENCES SHALL BE DECLARED**
The "Upstream Tables" column of the scaffold SHALL list T-NN tokens for every prior table
this table references. A recovery entry that cites the Incumbent Baseline SHALL list T-01
in its upstream references. "none" is only valid if no prior table is drawn from.

---

### [T-NN] OUTPUT TABLE SCAFFOLD

**PROTOCOL GATE 0 applies. This section IS REQUIRED before any domain content.**

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | [table name] | [purpose + criterion] | [T-NN tokens or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

Tables that SHALL be registered (declare in dependency order):
- Incumbent Baseline Table — upstream: none
- Entity Inventory Table — upstream: none
- Stage Trace Table per stage — upstream: T-02 (Entity Inventory)
- Boundary Inventory Table — upstream: all Stage Trace T-NN entries
- Recovery Audit Table — upstream: Boundary Inventory, all Stage Trace entries, T-01
- Closure Gate Table — upstream: Recovery Audit Table

After the scaffold, append: `SCAFFOLD CLOSED — [N] tables registered. PROTOCOL GATES 0
through 4 are now in effect for all subsequent sections.`

---

### [T-01] INCUMBENT BASELINE TABLE

**PROTOCOL GATE 3 applies. This section header includes the scaffold token.**

Document the manual promotional pricing and discount validation process this pipeline
replaces. This table is T-01 in the scaffold.

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step name] | [merchandising analyst / commerce ops / etc.] | [time] |
| ... | ... | ... | ... |

**Five distinct steps REQUIRED** specific to promotional pricing operations (e.g.,
`MS-01: Merchandising analyst manually enters promotional price overrides into ERP
pricing module and validates against margin floor rules — 2 hrs per promotion launch`).
Generic steps SHALL NOT qualify.

**INCUMBENT TOTAL**: sum of all Duration values. This value IS REQUIRED and SHALL NOT
be omitted. Fixed at declaration.

**MS-NN Citation requirement**: Every recovery entry in T-[Recovery Audit] SHALL cite an
MS-NN step ID from this table. A recovery entry without an MS-NN citation IS a C-16
protocol violation.

---

### [T-02] ENTITY INVENTORY TABLE

**PROTOCOL GATE 3 applies. Upstream tables: none.**

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

Required entities: PromotionalOverride, PriceEngineOutput, ValidationResult,
CDXPublication, StorefrontCacheEntry, AvailabilityAPIPayload.

**SLA DECLARATION** (immutable — SHALL NOT be re-declared or adjusted by any downstream
section; cite by T-02 reference in all latency comparisons):
- **Promotion activation SLA**: maximum elapsed time from promotional override entry to
  availability API reflecting the new price (numeric, in minutes)
- **SKU volume assumption**: SKUs per promotional batch at peak campaign launch

---

### STAGE TRACE — STAGES 1 THROUGH 6

**PROTOCOL GATE 3 applies to each stage. Use T-NN header from scaffold.**

For each stage, produce a table registered in the scaffold. Columns REQUIRED:

| Field | Type | Schema Delta | LP-NN Loss Point | NH-NN No-Handling | Stage Latency |
|-------|------|-------------|-----------------|------------------|---------------|

**Schema Delta SHALL state**: named changes or `NONE — verified: no field added, removed,
renamed, or retyped`. A bare "NONE" without the verification clause IS a C-12 protocol
violation.

**LP-NN SHALL state**: concrete, named failure. `LP-01: PromotionalOverride records with
effective_date in the past silently excluded from PriceEngineOutput — expired promotions
re-activated without validation`. "Errors may occur" SHALL NOT qualify.

**NH-NN SHALL state**: `NH-01: no handling — risk accepted at [location]`.

After each stage table, produce a **Typed Exit Manifest** (REQUIRED — omission IS a
protocol violation):

```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count]  key field assertions: [field_name: TYPE, minimum two assertions]
```

**Stages**:
1. Promotion Entry — merchandising system → pricing engine intake
2. Price Override Generation — pricing engine → override service
3. Discount Validation — override service → validation engine
4. CDX Publication — validation engine → CDX broker
5. Storefront Cache Write — CDX broker → storefront cache
6. Availability API Refresh — storefront cache → customer-facing API

---

### [T-NN] BOUNDARY INVENTORY TABLE

**PROTOCOL GATE 3 applies. Upstream tables: all Stage Trace T-NN entries.**

All nine columns REQUIRED. A row with any blank cell IS a structural gap.

| Boundary | Error Handling | Schema Change | Entity at Risk (entity.field — SHALL cite exit manifest) | Transport Latency (ms) | Processing Overhead (ms) | Total Latency (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|---------------|--------------------------------------------------------|----------------------|------------------------|------------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

Transport and Processing Overhead SHALL each carry independent numeric ms estimates.
"Negligible" SHALL NOT be an acceptable value in either column.

**DOMINATION POINT** SHALL follow the table: boundary where Cumulative SLA% first
exceeds 50%, the exact crossing percentage, and a one-sentence justification. Omission of
the DOMINATION POINT IS a C-22 protocol violation.

---

### Stale Window Analysis

Accumulate stage and boundary latencies sequentially. At each boundary step, state
Transport and Processing Overhead addends separately. Compare final total against
promotion activation SLA (cite by T-02 reference):
1. Normal operation: FRESH or STALE
2. Worst-case failure (cite LP-NN or NH-NN): FRESH or STALE

---

### [T-NN] RECOVERY AUDIT TABLE

**PROTOCOL GATES 2, 3, 4 apply. Upstream tables: T-01, [boundary T-NN], [all stage T-NN].**

One row per NH-NN and LP-NN — all five columns REQUIRED. Missing rows ARE structural
deficits. PROTOCOL GATE 2: every MS citation SHALL use MS-NN format; every table
reference SHALL use T-NN format.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

---

### [T-NN] CLOSURE GATE TABLE

**PROTOCOL GATES 2, 3 apply. Upstream table: [Recovery Audit T-NN]. This section IS
REQUIRED and SHALL be structurally separate from the Recovery Audit Table.**

Enumerate all NH-NN and LP-NN identifiers independently. Do NOT derive this list from
the Recovery Audit Table rows — enumerate from declaration sites in Stage Trace and
Boundary Inventory sections.

| Identifier | Source | Recovery Row Present | Status |
|------------|--------|---------------------|--------|
| NH-01 | [source] | YES / NO | CLOSED / OPEN |

An OPEN status IS a structural deficit. A count summary SHALL NOT substitute for a
per-identifier status table.

---

### Pattern Assessment

Name the integration pattern and one alternative. Provide ≥2 trade-off dimensions with
≥1 quantified in Commerce / promotional pricing terms. Cite T-01 (incumbent baseline) by
T-NN token as the comparison baseline per PROTOCOL GATE 2.

---

*Protocol compliance: PROTOCOL GATES 0–4 apply throughout. The scaffold declared above
IS the navigational contract. SCAFFOLD VIOLATION = undeclared table in body or invalid
T-NN citation. Every numeric latency column SHALL contain an independent estimate.*

---

## V-04 — Combined: Scaffold-First Format + Boundary-First Lifecycle

**Variation axis**: Combined — scaffold-first output format (boundaries are first-class
scaffold entries, registered before stage bodies) + boundary-centric lifecycle (boundaries
are analyzed before stage content; each boundary receives its own dedicated analysis block
drawing from flanking stage exit manifests).

**Hypothesis**: Pre-registering boundary tables as first-class T-NN scaffold entries
(separate rows for each boundary block, not a single Boundary Inventory Table) forces the
model to name every boundary before writing any stage content. When boundaries are analyzed
in their own blocks — after each stage, drawing from that stage's exit manifest — the
boundary block structure reinforces C-11 boundary labeling, C-17 entity-at-risk field
citations, C-21 decomposed latency, and C-22 cumulative SLA% simultaneously. The scaffold
upstream-references column connects each boundary block to its flanking stage tables,
making cross-table referenceability explicit before any content is written.

Scenario: Finance/Operations — intercompany elimination dual-write. Intercompany
transactions are simultaneously written to both a regional ERP (for subsidiary reporting)
and a consolidation staging layer (for elimination entries). Each write path has
independent transformation, validation, and posting stages. A reconciliation check verifies
both writes before the consolidation period closes. Stages (dual paths): IC Transaction
Capture => [Path A] Regional ERP Posting + [Path B] Consolidation Staging Write =>
Elimination Calculation => Consolidation Period Close.

---

You are a Finance data domain expert tracing data through an intercompany elimination
dual-write pipeline — intercompany transactions written simultaneously to a regional ERP
subsidiary ledger and a consolidation staging layer, with an elimination reconciliation
check before period close.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### STEP 0 — OUTPUT TABLE SCAFFOLD (BOUNDARIES AS FIRST-CLASS ENTRIES)

**This section must appear before any domain context, entity inventory, stage trace, or
boundary block begins.** Boundaries are first-class scaffold entries — each boundary has
its own T-NN registration row.

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | [table name] | [purpose + criterion] | [T-NN or "none"] |
| ... | ... | ... | ... |

**Required scaffold entries** — register in this dependency order:

**Foundation tables (upstream: none)**:
- T-01: Incumbent Baseline Table — C-15 (pre-automation elimination process)
- T-02: Entity Inventory Table — C-10 (domain entities)

**Stage trace tables** (upstream: T-02):
- T-03: Stage Trace — IC Transaction Capture
- T-04: Stage Trace — Regional ERP Posting (Path A)
- T-05: Stage Trace — Consolidation Staging Write (Path B)
- T-06: Stage Trace — Elimination Calculation
- T-07: Stage Trace — Consolidation Period Close

**Boundary blocks** (each upstream: the flanking stage tables it connects):
- T-08: Boundary Block B1->2A (Capture → ERP) — upstream: T-03, T-04
- T-09: Boundary Block B1->2B (Capture → Consolidation) — upstream: T-03, T-05
- T-10: Boundary Block B2A->3 (ERP → Elimination) — upstream: T-04, T-06
- T-11: Boundary Block B2B->3 (Consolidation → Elimination) — upstream: T-05, T-06
- T-12: Boundary Block B3->4 (Elimination → Period Close) — upstream: T-06, T-07

**Synthesis tables**:
- T-13: Stale Window Analysis — upstream: T-03 through T-12
- T-14: Recovery Audit Table — upstream: T-01, T-03 through T-12
- T-15: Closure Gate Table — upstream: T-14

After the scaffold, state: `SCAFFOLD CLOSED — 15 tables declared in dependency order.
Boundary blocks T-08 through T-12 are pre-registered as first-class entries. No table
may appear in the body that is not declared here.`

---

### [T-01] INCUMBENT BASELINE TABLE

Document the manual intercompany elimination process before this dual-write pipeline was
implemented:

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step name] | [IC accountant / consolidation team / etc.] | [time] |
| ... | ... | ... | ... |

**Five distinct steps required** specific to intercompany elimination (e.g., `MS-01: IC
accountant exports subsidiary transaction extract from regional ERP to Excel and
identifies intercompany pairs by counterparty entity code — 4 hrs per period`).

- **INCUMBENT TOTAL**: additive sum of Duration values. Fixed.
- **Period close SLA**: maximum elapsed time from IC transaction capture to consolidation
  period close verification (numeric, in hours). Fixed. All downstream latency comparisons
  cite this value by T-01 reference.

---

### [T-02] ENTITY INVENTORY TABLE

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

Required entities: ICTransaction, RegionalERPEntry, ConsolidationStagingRecord,
EliminationEntry, ReconciliationReport, PeriodCloseVerification.

---

### STAGE AND BOUNDARY INTERLEAVE SEQUENCE

For this dual-write pipeline, produce stages and boundary blocks in this alternating
sequence, using each section's scaffold T-NN header:

`[T-03] Stage 1 → [T-08] Boundary B1->2A → [T-04] Stage 2A → [T-09] Boundary B1->2B →
[T-05] Stage 2B → [T-10] Boundary B2A->3 → [T-11] Boundary B2B->3 → [T-06] Stage 3 →
[T-12] Boundary B3->4 → [T-07] Stage 4`

**Stage table format** (required columns for each T-03 through T-07):

| Field | Type | Schema Delta | LP-NN Loss Point | NH-NN No-Handling | Stage Latency |
|-------|------|-------------|-----------------|------------------|---------------|

After each stage table, produce an Exit Manifest (minimum two typed field assertions).

**Boundary block format** (required columns for each T-08 through T-12):

| Entity at Risk (entity.field — cite exit manifest) | Error Handling | Schema Change | Transport Latency (ms) | Processing Overhead (ms) | Total Latency (ms) | Elapsed Cumulative (ms) | SLA% This Boundary | Cumulative SLA% |
|--------------------------------------------------|---------------|---------------|----------------------|------------------------|------------------|------------------------|-------------------|-----------------|

Each boundary block header must state: `[T-NN] BOUNDARY BLOCK — B[from]->[to] |
Upstream: [flank stage T-NN tokens from scaffold] | Elapsed before this boundary: [ms]`

**Boundary block specific rules**:
- **Entity at Risk**: `entity.field_name — risk description`, field from upstream exit
  manifest. Entity-only annotations fail C-20.
- **Transport Latency**: network, serialization, queue depth — numeric ms, no "negligible".
- **Processing Overhead**: computation, enrichment, I/O — numeric ms, no "negligible".
- **Elapsed Cumulative**: sum of all prior stage and boundary latencies including this one.
- **Domination Point**: after T-12, state the boundary where Cumulative SLA% first exceeds
  50%, the crossing percentage, and a one-sentence justification.

---

### [T-13] STALE WINDOW ANALYSIS

Accumulate elapsed time across the complete sequence (both paths A and B). Identify the
dual-write divergence point: the stage or boundary at which the two write paths produce
different elapsed totals. Compare both path totals and the reconciliation elapsed against
the period close SLA:
1. Normal operation (both paths): FRESH or STALE
2. Worst-case failure (cite LP-NN or NH-NN): FRESH or STALE
3. Path divergence scenario (one path delayed — name the mechanism): FRESH or STALE

---

### [T-14] RECOVERY AUDIT TABLE

Upstream tables: T-01, T-03 through T-12 (as declared in scaffold). One row per NH-NN
and LP-NN — five columns required; missing rows are structural gaps.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

---

### [T-15] CLOSURE GATE TABLE

Upstream table: T-14 (as declared in scaffold). Structurally separate from T-14. Enumerate
all NH-NN and LP-NN identifiers independently:

| Identifier | Source | Recovery Row Present | Status |
|------------|--------|---------------------|--------|

---

### Pattern Assessment

Name the dual-write pattern and one alternative. State ≥2 trade-off dimensions with ≥1
quantified in Finance / intercompany consolidation terms. Cite T-01 as the comparison
baseline.

---

*Scaffold contract: T-08 through T-12 are pre-registered boundary tables — not ad-hoc
annotations. Produce each boundary block using its T-NN header, in the declared
interleave sequence. No undeclared tables. Independent numeric estimates in all latency
columns.*

---

## V-05 — Combined: Scaffold-First Format + Inertia-First Role Sequence

**Variation axis**: Combined — scaffold-first output format (incumbent baseline as T-01,
first registered scaffold entry) + inertia-first role sequence (Operations runs first and
owns the scaffold declaration and incumbent baseline; Finance and Commerce run after and
are forbidden from producing tables not registered in the Operations scaffold).

**Hypothesis**: When Operations owns the scaffold declaration and declares the incumbent
baseline as T-01 (the first scaffold entry, with no upstream references), every recovery
entry that must cite T-01 is anchored to a table pre-declared in the scaffold's dependency
graph. This mechanically enforces C-16 full recovery-to-baseline traceability because the
MS-NN → T-01 citation chain is established at the scaffold level before any domain content
appears. Predicts higher C-14/C-15/C-16 compliance than scaffolds where the incumbent
baseline is declared mid-trace by a Finance role, because Operations — owning pipeline
mechanics — produces more operationally specific incumbent steps with named operational
processes rather than accounting procedures.

Scenario: Commerce/Operations — product catalog ETL. Product master records from a Product
Information Management (PIM) system flow through attribute normalization, pricing engine
enrichment, availability calculation, and storefront publication to a CDN-cached catalog
API. Stages: PIM Extract => Attribute Normalization => Price Enrichment => Availability
Calculation => Catalog Publication => CDN Cache Propagation.

---

You are tracing data through a product catalog ETL pipeline. Three expert roles run in
the sequence **Operations → Finance → Commerce**. Operations runs first and owns the
scaffold declaration. Finance and Commerce run after and are forbidden from producing any
table not registered in the Operations scaffold.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### ROLE 1 — Operations (Scaffold Owner)

Operations runs first and produces two deliverables before any stage trace begins:
(1) the OUTPUT TABLE SCAFFOLD and (2) the INCUMBENT BASELINE TABLE (T-01). Operations
also owns the stage trace and boundary inventory sections.

**Operations may not begin any stage trace until the scaffold is complete.**

---

#### STEP 0 — OUTPUT TABLE SCAFFOLD

Declare every table that will appear in this response. The Incumbent Baseline Table is
T-01 — the first entry, with no upstream references — because all recovery prescriptions
in this pipeline trace back to the pre-automation catalog operations process.

| Table # | Table Name | Purpose | Upstream Tables |
|---------|------------|---------|-----------------|
| T-01 | Incumbent Baseline Table | Pre-automation product catalog operations process; reference anchor for all recovery prescriptions (C-15, C-16) | none |
| T-02 | [entity inventory] | [purpose] | none |
| T-03 | [stage trace — Stage 1] | [purpose] | T-02 |
| T-04 | [stage trace — Stage 2] | [purpose] | T-02, T-03 |
| T-05 | [stage trace — Stage 3] | [purpose] | T-02, T-04 |
| T-06 | [stage trace — Stage 4] | [purpose] | T-02, T-05 |
| T-07 | [stage trace — Stage 5] | [purpose] | T-02, T-06 |
| T-08 | [stage trace — Stage 6] | [purpose] | T-02, T-07 |
| T-09 | [boundary inventory] | [purpose + C-11, C-17, C-21, C-22] | T-03, T-04, T-05, T-06, T-07, T-08 |
| T-10 | [recovery audit] | [purpose + C-18, C-16] | T-01, T-03 through T-09 |
| T-11 | [closure gate] | [purpose + C-23] | T-10 |

**Scaffold rules for downstream roles**:
- Finance and Commerce may not produce any table not registered here.
- Any cross-table reference in this response must use T-NN tokens from this scaffold.
- Recovery entries in T-10 must cite T-01 by T-NN token and cite an MS-NN step by ID.
- T-11 must derive its identifier list from declaration sites, not from T-10 rows.

State: `SCAFFOLD CLOSED — T-01 anchored as recovery baseline. 11 tables declared.
Finance and Commerce may not produce undeclared tables.`

---

#### [T-01] INCUMBENT BASELINE TABLE

Document the manual product catalog operations process this ETL pipeline replaces.
**This is T-01 — declared first in the scaffold and upstream for all recovery entries.**

| Step ID | Manual Step | Actor/Team | Duration |
|---------|-------------|------------|----------|
| MS-01 | [step name] | [catalog ops / pricing analyst / commerce merchandising] | [time] |
| MS-02 | ... | ... | ... |
| MS-03 | ... | ... | ... |
| MS-04 | ... | ... | ... |
| MS-05 | ... | ... | ... |

**Five distinct steps required** specific to product catalog operations (e.g., `MS-01:
Catalog ops specialist exports PIM delta extract to CSV and manually maps attribute
schema to commerce platform field names using a cross-reference spreadsheet — 3 hrs per
batch`). Generic steps do not qualify.

State:
- **INCUMBENT TOTAL**: sum of all Duration values. Fixed at T-01 declaration.
- **Catalog SLA**: maximum elapsed time from PIM extract to CDN-cached catalog API
  reflecting the updated product record (numeric, in hours). Fixed at T-01 declaration —
  Finance and Commerce must cite by T-01 reference; they may not re-declare this value.

---

#### [T-02] ENTITY INVENTORY TABLE

| Entity Name | Domain | Key Fields | Role in Pipeline |
|-------------|--------|------------|-----------------|

Required entities: PIMProductRecord, NormalizedAttribute, PriceEnrichedProduct,
AvailabilityRecord, CatalogPublicationEvent, CDNCachedPayload.

---

#### STAGE TRACE — [T-03] THROUGH [T-08]

For each stage, produce the registered stage table using its T-NN scaffold header.
Required columns:

| Field | Type | Schema Delta | LP-NN Loss Point | NH-NN No-Handling | Stage Latency |
|-------|------|-------------|-----------------|------------------|---------------|

**Schema Delta rules**:
- Named changes: `ADDED field_name: TYPE / RENAMED old→new / REMOVED field_name /
  RETYPED old TYPE to new TYPE`
- No change: `NONE — verified: no field added, removed, renamed, or retyped`
- A bare "NONE" without the verification clause fails C-12.

**LP-NN**: assign at declaration. Example: `LP-01: PIMProductRecords with null
primary_category_id silently excluded from NormalizedAttribute output — products
invisible to downstream pricing enrichment and availability calculation`. Assign
sequentially.

**NH-NN**: `NH-01: no handling — risk accepted at [stage/boundary name]`. Assign
sequentially.

After each stage table, produce an Exit Manifest (minimum two typed field assertions per
entity):
```
EXIT MANIFEST — Stage N: [entity name]
  fields: [count]  key field assertions: [field_name: TYPE(precision), ...]
```

**Stages**:
1. PIM Extract — PIM system → ETL intake queue
2. Attribute Normalization — ETL intake → normalization service
3. Price Enrichment — normalization service → pricing engine
4. Availability Calculation — pricing engine → inventory service
5. Catalog Publication — inventory service → catalog publisher
6. CDN Cache Propagation — catalog publisher → CDN edge nodes

---

#### [T-09] BOUNDARY INVENTORY TABLE

One row per boundary. Nine columns required — blank cells are structural gaps.

| Boundary | Error Handling | Schema Change | Entity at Risk (entity.field — cite exit manifest) | Transport Latency (ms) | Processing Overhead (ms) | Total Latency (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|---------------|---------------|--------------------------------------------------|----------------------|------------------------|------------------|-------------------|-----------------|
| B1->2 | | | | | | | | |
| B2->3 | | | | | | | | |
| B3->4 | | | | | | | | |
| B4->5 | | | | | | | | |
| B5->6 | | | | | | | | |

**Transport Latency**: numeric ms estimate — "negligible" does not qualify.
**Processing Overhead**: numeric ms estimate — "negligible" does not qualify.
**Entity at Risk**: `entity.field_name — risk description`, field from upstream exit
manifest. Entity-only fails C-17. No manifest field? Invalid citation.

After the table, state **DOMINATION POINT**: boundary where Cumulative SLA% first exceeds
50%, the exact crossing percentage, and a one-sentence justification.

---

### ROLE 2 — Finance

Finance provides financial domain overlay. Finance may not produce any table not
registered in the Operations scaffold.

Begin with `Citing scaffold entries: [T-NN tokens this role draws from]`.

**Stale Window Analysis**

Accumulate stage latencies (T-03 through T-08) and boundary latencies (T-09) sequentially.
State Transport and Processing Overhead addends separately at each boundary step. Compare
final elapsed against the Catalog SLA (cite by T-01 reference — do not re-state the value):

1. Normal operation: FRESH or STALE
2. Worst-case failure (cite LP-NN or NH-NN): FRESH or STALE

**Financial Risk Annotation**

For each STALE verdict: name the financial risk (e.g., pricing mismatches driving margin
erosion, incorrect promotional price visible to customers). Quantify where possible.

---

### ROLE 3 — Commerce

Commerce produces recovery audit, closure gate, and pattern assessment. Commerce may not
produce any table not registered in the Operations scaffold.

Begin with `Citing scaffold entries: [T-NN tokens this role draws from]`.

**[T-10] RECOVERY AUDIT TABLE**

Upstream tables: T-01, T-03 through T-09 (as declared in scaffold). One row per NH-NN
and LP-NN — five columns required; missing rows are structural gaps.

| Trigger ID | Triggering Condition | Recovery Mechanism | MS Step ID | Incumbent Step (verbatim from T-01) |
|------------|---------------------|-------------------|------------|-------------------------------------|

**T-01 citation requirement**: every recovery entry must cite T-01 by T-NN token AND cite
a specific MS-NN step from T-01 by Step ID. A recovery entry that names only the process
category ("fall back to manual catalog operations") without citing a specific MS-NN row
from T-01 does not satisfy C-16.

**[T-11] CLOSURE GATE TABLE**

Upstream table: T-10 (as declared in scaffold). Structurally separate from T-10. Enumerate
all NH-NN and LP-NN identifiers from their declaration sites — do not derive from T-10 rows:

| Identifier | Source (stage or boundary) | Recovery Row in T-10 | Status |
|------------|---------------------------|---------------------|--------|
| NH-01 | [source] | YES / NO | CLOSED / OPEN |
| LP-01 | [source] | YES / NO | CLOSED / OPEN |

An OPEN status is a structural deficit. A count summary does not substitute for a
per-identifier table.

**Pattern Assessment**

Name the ETL pattern and one alternative. State ≥2 trade-off dimensions with ≥1
quantified in Commerce / product catalog terms (e.g., "batch PIM extraction introduces
a ~3–4 hr catalog staleness window per daily run vs CDC streaming, which reduces the
window to <90 s but requires PIM CDC connector licensing and schema-on-read handling for
attribute adds"). Cite T-01 as the comparison baseline using T-01 token.

---

*Scaffold contract: T-01 is the recovery anchor — every recovery entry in T-10 must
resolve to a named MS-NN step from T-01. The scaffold was declared by Operations; Finance
and Commerce may not introduce undeclared tables. All T-NN cross-references must resolve
against the scaffold declared in STEP 0.*
