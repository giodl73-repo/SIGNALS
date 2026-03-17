# flow-dataflow — Round 8 Variations (Rubric v7)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v7 (C-01 through C-20, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 8 advances the three structural mechanisms confirmed in R7 and tests three new axes
derived from the patterns identified in R7 evidence that were not captured by C-01 through
C-18. R7 established that typed entity handoff manifests drive field-level entity-at-risk
citations (C-20 precursor), that SLA budget % framing forces boundary latency quantification
(C-22 precursor), and that closure enforcement statements catch recovery table omissions
(C-23 precursor). R8 asks: what structural form must each mechanism take to fully satisfy
the C-21/C-22/C-23 proposed criteria?

**R8 Hypothesis space:**

**H1 — Decomposed latency as separate additive columns (V-01)**
R7 V-02 required boundary latency expressed as SLA budget % in one column. C-21 requires
Transport and Processing Overhead as *separate numeric columns* — not a single total with
optional sub-description. If the table schema itself pre-separates the two components, the
model cannot collapse them into one cell. Tests whether column-level separation produces
independently-valued sub-components (each with its own numeric estimate) vs split columns
that receive the same value or leave one blank. Predicts that a table requiring both columns
to be independently filled forces the model to reason about transport overhead (network,
serialization, queue depth) separately from processing overhead (computation, enrichment,
I/O), producing more precise latency attribution than a single combined total.

**H2 — Cumulative SLA% running total with domination-point identification (V-02)**
R7 SLA% was per-boundary: each row expressed its own percentage independently. C-22 requires
a *cumulative* running total across all boundaries — the running sum from B1 forward — so
the boundary that causes the cumulative total to cross 50% is structurally visible as the
domination point. Tests whether cumulative accounting changes which boundary the model flags
as dominant, compared to per-boundary % which flags the highest individual consumer. Predicts
that pipelines with several moderate-latency boundaries (none individually dominant) will
reveal a different domination point under cumulative accounting than under per-boundary
comparison, and that the cumulative column prevents the model from designating the final
boundary as dominant by default.

**H3 — Structurally separate closure gate as a standalone table (V-03)**
R7 V-03 required a "closure check" as a post-recovery prose statement or inline list.
C-23 requires the closure gate to be *structurally separate* from the recovery table — a
distinct section with its own table that forward-checks every declared NH-NN and LP-NN
identifier against the recovery table rows. Tests whether separating the closure gate from
the recovery audit table prevents the model from generating a closure statement that simply
mirrors the recovery table rows it just produced (a self-confirming closure) rather than
independently enumerating the declared set and checking each against the table. Predicts
that a structurally separate closure gate, with its own row-per-identifier schema, is more
likely to surface gaps where a declared NH or LP identifier has no recovery row than a prose
closure appended to the recovery section.

**H4 — Combined: decomposed latency columns + cumulative SLA% (V-04)**
Combines H1 (separate Transport/Processing Overhead columns) and H2 (cumulative SLA%
running total). Tests whether the two latency precision mechanisms reinforce each other:
when each boundary's latency is independently decomposed AND a cumulative % column tracks
budget consumption, does the combination drive more accurate stale window quantification
(C-06) and domination-point identification (C-22) than either mechanism alone? Also tests
whether the additional columns crowd out essential annotations (C-02 error handling, C-03
loss points) by making the boundary table too wide to complete.

**H5 — Combined: cumulative SLA% + separate closure gate (V-05)**
Combines H2 (cumulative SLA% running total with domination point) and H3 (structurally
separate closure gate table). Tests whether pairing the two structural accountability
mechanisms — one for latency budget (H2) and one for recovery completeness (H3) — raises
composite scores on the new proposed criteria simultaneously without degrading C-01 through
C-04 essential coverage. The pairing tests a specific failure mode: whether the cumulative
SLA% column crowds out the model's attention to the closure gate section at the end of the
trace, leaving the closure gate populated with fewer rows than the declared NH/LP set.

**Axes selected for R8:**

1. **Decomposed latency as separate additive columns** — Transport and Processing Overhead
   as distinct numeric columns in the boundary table (single axis: V-01)
2. **Cumulative SLA% running total** — per-boundary % plus a running cumulative column
   with explicit domination-point identification (single axis: V-02)
3. **Structurally separate closure gate table** — a standalone section that enumerates
   every declared NH/LP identifier and checks against recovery rows (single axis: V-03)
4. **Combined (H1 + H2)** — decomposed latency columns + cumulative SLA% (V-04)
5. **Combined (H2 + H3)** — cumulative SLA% + separate closure gate (V-05)

**New signal candidates for R8:**

1. **Sub-component value quality** (V-01, V-04) — whether the model assigns independently
   reasoned values to Transport and Processing Overhead columns vs splitting a single total
   50/50 across both columns, or leaving one column at 0. Success signal: at least one
   boundary where Transport and Processing Overhead receive materially different values
   with a rationale distinguishing the two (e.g., a queue-backed boundary where transport
   dominates vs a sync API boundary where processing dominates). Failure signal: all
   boundaries show symmetric or proportional splits with no rationale.

2. **Domination-point precision** (V-02, V-04, V-05) — whether cumulative SLA% identifies
   a different boundary as dominant than per-boundary % would have identified. Success
   signal: the model explicitly states which boundary causes the cumulative total to cross
   50% and whether this differs from the single highest-% boundary. Failure signal: the
   model designates the highest single-% boundary as the domination point without computing
   the cumulative threshold crossing.

3. **Closure gate independence** (V-03, V-05) — whether the closure gate table enumerates
   the declared set independently of the recovery table rather than copying its rows.
   Success signal: a closure gate that flags at least one NH or LP identifier as "recovery
   row absent" when the recovery table omits it, or that enumerates the full declared set
   with row-level status even when all rows are present. Failure signal: a closure gate
   that lists only the identifiers that appear in the recovery table, producing a closure
   that cannot detect omissions.

4. **Column-width pressure vs coverage** (V-04) — whether the combined latency table
   (Boundary | Error Handling | Transport | Processing | Total | SLA% | Cumulative SLA%)
   is completed in full vs partially abandoned, with model falling back to prose for the
   rightmost columns. Success signal: all seven columns filled for all boundaries. Failure
   signal: the rightmost columns (SLA%, Cumulative SLA%) are omitted or collapsed to prose
   for more than one boundary.

---

## V-01 — Decomposed Latency as Separate Additive Columns

**Variation axis**: Structure — require boundary latency to be stated as two independently
valued numeric columns (Transport Latency and Processing Overhead) rather than a single
total, so the two sub-components are visibly separate and independently scorable.
**Hypothesis**: Column-level separation of Transport and Processing Overhead forces the
model to reason about the two components distinctly — network/serialization/queue overhead
vs computation/enrichment/I/O — producing independently valued estimates with different
numeric values and supporting rationale, rather than a single total that can be split
arbitrarily. Predicts that at least one boundary will show a material asymmetry between
transport and processing overhead, and that the stale window addend sequence will cite the
dominant sub-component by name as the contributing factor.

Scenario: Commerce order fulfillment pipeline — an Operations domain pipeline in which
customer orders flow from the e-commerce platform through inventory reservation, warehouse
pick-and-pack scheduling, carrier assignment, and shipment confirmation back to the order
management system. Stages: Order Capture => Inventory Reservation => Pick Scheduling =>
Carrier Assignment => Shipment Dispatch => Order Status Sync.

---

You are an Operations data domain expert tracing data through a commerce order fulfillment
pipeline — customer orders through inventory reservation, pick scheduling, carrier
assignment, shipment dispatch, and order status sync.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual order fulfillment procedure this pipeline
replaces. Present it as the following four-column table with a mandatory Step ID column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per order batch] |
| MS-02   | ...         | ...           | ...                    |

**Minimum required**: five distinct manual steps specific to order fulfillment operations
(e.g., `MS-01: Warehouse supervisor exports overnight orders from OMS to spreadsheet and
distributes pick lists to floor teams: 45 min per shift`). Generic workflow steps not
grounded in fulfillment operations do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

**Citation rule**: cite incumbent steps by Step ID (MS-NN format) in all downstream
recovery entries. A citation that describes step content without the Step ID does not
satisfy C-16.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced. Required entities:
**CustomerOrder, InventoryReservation, PickList, CarrierAssignment, ShipmentRecord,
OrderStatusEvent.**

State: (a) order processing SLA — the maximum elapsed time from order capture to
shipment dispatch confirmation before a carrier SLA breach risk arises (numeric, in hours
or minutes), (b) the peak order volume assumption in orders per hour.

Both values are fixed at declaration and are the reference standard for all latency
annotations in SECTION 3.

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS**

For each stage, state all five required items.

Required items per stage:
- **Input schema**: key fields, types, cardinality at stage entry (specific field names)
- **Transformations**: every field added, renamed, retyped, or removed; if no change:
  `verified: no field added, removed, renamed, or retyped`
- **Loss point LP-NN**: [concrete named failure] — assign a sequential LP identifier at
  declaration. Example: `LP-01: SKU unavailable in inventory system at reservation time —
  CustomerOrder written to staging with unresolvable line item; item is silently dropped
  from PickList.` "Errors may occur" does not qualify.
- **Typed exit manifest**: declare the entities exiting this stage:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count at exit] | key field assertions:
  [field_name: TYPE(precision), e.g., reserved_qty: INTEGER; reservation_expiry: TIMESTAMP(6)]`

  Minimum two key field assertions per entity. The exit manifest is the sole authority for
  field names and types available for downstream boundary annotations.
- **Stage latency**: value or range (e.g., `< 200 ms` or `2–5 min batch`)

**Stage 1 — Order Capture**: e-commerce platform => order management system (OMS)
**Stage 2 — Inventory Reservation**: OMS => inventory service
**Stage 3 — Pick Scheduling**: inventory service => warehouse management system (WMS)
**Stage 4 — Carrier Assignment**: WMS => carrier routing engine
**Stage 5 — Shipment Dispatch**: carrier routing engine => dispatch service => carrier API
**Stage 6 — Order Status Sync**: dispatch service => OMS status topic => customer notification service

---

**SECTION 3 — BOUNDARY INVENTORY WITH DECOMPOSED LATENCY**

Produce one row per inter-stage boundary. All seven columns are required — a row with any
blank cell is a structural gap.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Transport Latency (ms or s) | Processing Overhead (ms or s) | Total Boundary Latency | Entity at Risk (entity.field — cite exit manifest) |
|----------|--------------------------------------------------------------------|------------------------------------------------|----------------------------|------------------------------|----------------------|--------------------------------------------------|
| B1->2    |                                                                    |                                                |                            |                              |                      |                                                  |
| B2->3    |                                                                    |                                                |                            |                              |                      |                                                  |
| B3->4    |                                                                    |                                                |                            |                              |                      |                                                  |
| B4->5    |                                                                    |                                                |                            |                              |                      |                                                  |
| B5->6    |                                                                    |                                                |                            |                              |                      |                                                  |

**Transport Latency column**: network transit, queue depth penalty, serialization overhead.
State as a numeric value or range. "Negligible" is not acceptable — estimate in ms.
**Processing Overhead column**: computation, enrichment lookup, transformation, I/O at the
receiving stage before data is available to the next stage. State as a numeric value or range.
**Total Boundary Latency**: Transport + Processing Overhead. Must equal the sum of the two
preceding columns.

**NH-NN format rule**: declare as `NH-01: no handling — risk accepted`. Fixed at declaration
and carried forward to SECTION 6.
**Entity at Risk column rule**: name a specific entity AND a specific field from that
entity's typed exit manifest. Format: `entity.field_name — risk description`. Entity-only
annotations do not qualify. A field not in the upstream exit manifest is an invalid citation.

---

**SECTION 4 — STALE WINDOW ANALYSIS**

Accumulate stage latencies (SECTION 2) and boundary latencies (SECTION 3) step by step:

- After Stage 1: [elapsed]
- After B1->2: [elapsed — state Transport and Processing Overhead addends separately]
- After Stage 2: [elapsed]
- ... continue through Stage 6 ...

Identify the single stage or boundary contributing the largest share of elapsed time by
label. Separately state whether the dominant contributor is Transport Latency or Processing
Overhead at that crossing.

Compare the final accumulated total against the SLA declared in SECTION 1 under:
1. **Normal operation**: FRESH or STALE with elapsed value
2. **Worst-case failure mode** (name the specific failure, citing its LP-NN or NH-NN): FRESH or STALE

---

**SECTION 5 — RECOVERY AUDIT TABLE**

Produce one row for every NH-NN annotation from SECTION 3 and one row for every LP-NN loss
point from SECTION 2. All five columns are required.

| Trigger ID | Triggering Condition (verbatim NH-NN text or LP-NN description) | Recovery Mechanism (specific — generic advice fails) | MS Step ID Cited | Manual Step Cited (exact text from SECTION 0) |
|------------|----------------------------------------------------------------|-----------------------------------------------------|-----------------|-----------------------------------------------|

A missing row for any declared NH or LP identifier is a structural gap. All recovery entries
must name a specific mechanism at a specific boundary (e.g., "dead-letter queue on
OMS-to-inventory topic with 3-retry backoff before escalation to MS-03").

---

**SECTION 6 — PATTERN ASSESSMENT**

Name the integration pattern (event-driven async, synchronous API chain, CDC stream, etc.).
Name one alternative pattern. State at least two trade-off dimensions, at least one
quantified or qualified in operations terms (e.g., "synchronous chain increases carrier
assignment latency by ~800 ms per order vs async queue, but reduces duplicate shipment risk
from ~0.3% to near-zero at peak volume").

---

*Scoring note: Complete every table. A blank cell, a missing row, or a "negligible"
in a numeric latency column is a structural gap — not a formatting choice. Transport Latency
and Processing Overhead must each have their own independently-stated numeric value.*

---

## V-02 — Cumulative SLA% Running Total with Domination-Point Identification

**Variation axis**: Structure — add a cumulative SLA% column to the boundary inventory
table that tracks the running total of SLA budget consumed from B1 forward, and require
explicit identification of the boundary where cumulative consumption crosses 50%.
**Hypothesis**: Per-boundary SLA% (R7 V-02) identifies the single highest consumer but
misses pipelines where several moderate-latency boundaries collectively exhaust the budget
before the declared domination point. A cumulative running total forces the model to
identify the precise crossing boundary — the one that tips cumulative consumption over 50%
— which may differ from the highest single-% boundary. Predicts that the model will
identify a different domination point under cumulative accounting for pipelines with
multiple 10–20% boundaries, and that the stale window analysis will cite this crossing
boundary by cumulative threshold rather than peak individual value.

Scenario: Finance GL consolidation pipeline — a Finance domain pipeline in which regional
trial balance extracts from four subsidiary ERPs are validated, currency-converted at
period-end rates, eliminated for intercompany transactions, and posted to the consolidated
general ledger for financial close reporting. Stages: Regional ERP Extract =>
Trial Balance Validation => Currency Conversion => Intercompany Elimination =>
Consolidation Posting => Close Package Generation.

---

You are a Finance data domain expert tracing data through a GL consolidation pipeline —
regional trial balance extracts through validation, currency conversion, intercompany
elimination, consolidation posting, and close package generation.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual GL consolidation procedure this pipeline
replaces. Present it as the following four-column table with a mandatory Step ID column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per close cycle] |
| MS-02   | ...         | ...           | ...                    |

**Minimum required**: five distinct manual steps specific to period-end GL consolidation
(e.g., `MS-01: Finance controller at each subsidiary exports trial balance to Excel template
and emails to group controller: 2 hours per subsidiary per close cycle`). Generic workflow
steps not grounded in GL consolidation do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.
**CLOSE SLA**: maximum elapsed time from regional ERP cut-off to close package availability
before the financial close deadline is missed — state in hours. Fixed at declaration.

**Citation rule**: cite by Step ID (MS-NN) in all downstream recovery entries.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced. Required entities:
**TrialBalanceEntry, CurrencyConversionRate, IntercompanyTransaction, EliminationEntry,
ConsolidatedLedgerEntry, ClosePackage.**

State: (a) close cycle cadence (monthly / quarterly), (b) number of subsidiaries in scope,
(c) the Close SLA value declared above.

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS**

For each stage, state all five required items.

Required items per stage:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: every field added, renamed, retyped, or removed; if no change:
  `verified: no field added, removed, renamed, or retyped`
- **Loss point LP-NN**: [concrete named failure] with sequential LP identifier.
  Example: `LP-01: TrialBalanceEntry with functional currency mismatch against CurrencyConversionRate
  vintage — entry carried at stale rate; rate differential silently absorbed into consolidation
  variance.`
- **Typed exit manifest**:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count at exit] | key field assertions:
  [field_name: TYPE(precision)]`

  Minimum two key field assertions per entity.
- **Stage latency**: value or range

**Stage 1 — Regional ERP Extract**: each subsidiary ERP => consolidation staging database
**Stage 2 — Trial Balance Validation**: staging database => validation engine
**Stage 3 — Currency Conversion**: validation engine => FX conversion service
**Stage 4 — Intercompany Elimination**: FX conversion service => elimination engine
**Stage 5 — Consolidation Posting**: elimination engine => consolidated GL
**Stage 6 — Close Package Generation**: consolidated GL => reporting layer => close package store

---

**SECTION 3 — BOUNDARY INVENTORY WITH SLA BUDGET ACCOUNTING**

Produce one row per inter-stage boundary. All seven columns are required.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | SLA% This Boundary | Cumulative SLA% | Entity at Risk (entity.field — cite exit manifest) |
|----------|--------------------------------------------------------------------|------------------------------------------------|-----------------|-------------------|-----------------|----------------------------------------------------|
| B1->2    |                                                                    |                                                |                 |                   |                 |                                                    |
| B2->3    |                                                                    |                                                |                 |                   |                 |                                                    |
| B3->4    |                                                                    |                                                |                 |                   |                 |                                                    |
| B4->5    |                                                                    |                                                |                 |                   |                 |                                                    |
| B5->6    |                                                                    |                                                |                 |                   |                 |                                                    |

**SLA% This Boundary**: boundary latency as a percentage of the Close SLA declared in
SECTION 0. State as a numeric % (e.g., `12%`). "Negligible" or "<1%" without a numeric
basis is not acceptable.
**Cumulative SLA% column**: running total of SLA% from B1->2 through this row. The value in
each row equals the previous row's Cumulative SLA% plus this row's SLA% This Boundary.

After the table, state:

**DOMINATION POINT**: identify the specific boundary label (B[N]->[N+1]) where the
Cumulative SLA% column first exceeds 50%. State the cumulative % value at that crossing.
If no single boundary causes the crossing (i.e., cumulative reaches 50% between two
boundaries), identify the boundary that tips it over. State whether this boundary is also
the highest single SLA% consumer, or whether the two differ.

**NH-NN format rule**: declare as `NH-01: no handling — risk accepted`. Fixed at
declaration and carried forward to SECTION 6.
**Entity at Risk column rule**: entity AND field from that entity's typed exit manifest.
Format: `entity.field_name — risk description`.

---

**SECTION 4 — STALE WINDOW ANALYSIS**

Accumulate all stage latencies and boundary latencies step by step. Compare to Close SLA.

1. **Normal operation**: FRESH or STALE; total elapsed vs Close SLA
2. **Worst-case failure mode** (LP-NN or NH-NN cited): FRESH or STALE; total elapsed vs Close SLA

State whether the domination point identified in SECTION 3 is also the primary driver of
failure-mode staleness, or whether a different stage/boundary dominates under failure.

---

**SECTION 5 — STALE DATA WINDOWS**

1. **Normal operation staleness**: for a group controller reading TrialBalanceEntry between
   Stage 2 and Stage 5 — state the maximum elapsed time they may read stale (pre-FX, pre-elimination)
   values during the consolidation run
2. **Failure-mode staleness**: for the worst-case failure, state how long the stale window
   persists before recovery closes it; cite the recovery mechanism by Trigger ID from
   SECTION 6

---

**SECTION 6 — RECOVERY AUDIT TABLE**

One row per NH-NN annotation (SECTION 3) and per LP-NN loss point (SECTION 2).

| Trigger ID | Triggering Condition | Recovery Mechanism (specific) | MS Step ID Cited | Manual Step Cited (exact text from SECTION 0) |
|------------|---------------------|-------------------------------|-----------------|-----------------------------------------------|

A missing row for any declared NH or LP identifier is a structural gap.

---

**SECTION 7 — PATTERN ASSESSMENT**

Name the integration pattern. Name one alternative. State two trade-off dimensions, at
least one quantified in Finance close-cycle terms.

---

*Scoring note: The Cumulative SLA% column must be computed incrementally — each row's
value must equal the sum of all preceding SLA% values plus the current row's. A column
where each row contains the same value as SLA% This Boundary is not a cumulative column.*

---

## V-03 — Structurally Separate Closure Gate Table

**Variation axis**: Structure — require a dedicated closure gate section (structurally
separate from the recovery audit table) that forward-checks every declared NH-NN and LP-NN
identifier against the recovery table using its own table with a row per identifier and an
explicit status column.
**Hypothesis**: A closure gate that is a separate table with its own row-per-identifier
schema cannot be generated by simply mirroring the recovery table rows, because it must
enumerate the declared set independently. When the recovery table omits an identifier, the
closure gate's row for that identifier will have no matching row to mirror and must show
the gap explicitly. This is a stronger structural guarantee than an inline closure
statement that can be generated to match whatever the recovery table contains.

Scenario: Operations inventory sync pipeline — a dual-write Commerce/Operations pipeline
in which inventory position updates from the warehouse management system (WMS) are
simultaneously written to the order management system (OMS) and the product catalog
service, then reconciled against a master inventory record. Stages: WMS Position Update =>
Dual-Write Dispatcher => OMS Write => Catalog Write => Reconciliation Auditor =>
Discrepancy Resolution.

---

You are an Operations data domain expert tracing data through an inventory sync pipeline
using a dual-write pattern — WMS position updates dispatched simultaneously to OMS and
product catalog, then reconciled against the master inventory record.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual inventory synchronization procedure this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID
column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per sync cycle] |
| MS-02   | ...         | ...           | ...                   |

**Minimum required**: five distinct manual steps specific to inventory sync operations
(e.g., `MS-01: Warehouse operations lead exports inventory position delta from WMS to
CSV and uploads to shared drive for OMS team: 30 min per sync cycle`). Generic workflow
steps not grounded in inventory operations do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.
**SYNC SLA**: maximum elapsed time from WMS position update event to OMS and Catalog
write confirmation before inventory accuracy SLA is breached — state in minutes.
Fixed at declaration.

**Citation rule**: cite by Step ID (MS-NN) in all downstream recovery entries.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities. Required entities:
**InventoryPositionUpdate, DispatchManifest, OMSInventoryRecord, CatalogStockLevel,
MasterInventoryRecord, DiscrepancyReport.**

State: (a) sync frequency (real-time event-driven / micro-batch interval), (b) Sync SLA
value declared above, (c) the dual-write consistency model in use (synchronous 2PC /
async eventual / saga-compensating).

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS**

For each stage, state all five required items.

Required items per stage:
- **Input schema**: key fields, types, cardinality
- **Transformations**: field-level changes; if no change: `verified: no field added,
  removed, renamed, or retyped`
- **Loss point LP-NN**: concrete named failure with sequential LP identifier.
  Example: `LP-01: OMS write succeeds and Catalog write fails — DispatchManifest consumed
  from both paths; no compensating transaction issued; OMS and Catalog hold divergent
  InventoryPositionUpdate values indefinitely.`
- **Typed exit manifest**:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count at exit] | key field assertions:
  [field_name: TYPE(precision)]`

  Minimum two key field assertions per entity. Exit manifest is the sole authority for
  downstream field citations.
- **Stage latency**: value or range

**Stage 1 — WMS Position Update**: WMS event bus => dual-write dispatcher
**Stage 2 — Dual-Write Dispatcher**: dispatcher => OMS write path + Catalog write path (parallel)
**Stage 3a — OMS Write**: dispatcher => OMS inventory store
**Stage 3b — Catalog Write**: dispatcher => product catalog service
**Stage 4 — Reconciliation Auditor**: OMS + Catalog writes => reconciliation service
**Stage 5 — Discrepancy Resolution**: reconciliation service => discrepancy queue => resolution service => master inventory

Note: Stages 3a and 3b are parallel. Trace each separately with its own exit manifest and
loss points.

---

**SECTION 3 — BOUNDARY INVENTORY**

Produce one row per inter-stage boundary, including both parallel paths (B2->3a and B2->3b).
All six columns are required.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk (entity.field — cite exit manifest) | NH/LP Declared |
|----------|--------------------------------------------------------------------|------------------------------------------------|-----------------|---------------------------------------------------|----------------|
| B1->2    |                                                                    |                                                |                 |                                                   |                |
| B2->3a   |                                                                    |                                                |                 |                                                   |                |
| B2->3b   |                                                                    |                                                |                 |                                                   |                |
| B3a->4   |                                                                    |                                                |                 |                                                   |                |
| B3b->4   |                                                                    |                                                |                 |                                                   |                |
| B4->5    |                                                                    |                                                |                 |                                                   |                |

**NH/LP Declared column**: list the NH-NN or LP-NN identifiers associated with this
boundary. Multiple identifiers per row are permitted. A boundary with no declared
NH or LP must state `none`.

---

**SECTION 4 — STALE WINDOW ANALYSIS**

For the dual-write pattern, analyze two staleness paths:
1. **OMS path** (B1->2, B2->3a): elapsed from WMS event to OMS write confirmation
2. **Catalog path** (B1->2, B2->3b): elapsed from WMS event to Catalog write confirmation

Compare each path total against the Sync SLA. State which path has the larger staleness
window and by how much.

**Failure-mode staleness**: for the worst divergence scenario (LP-01 or whichever loss
point produces maximum divergence), state how long OMS and Catalog can hold divergent
values before the Reconciliation Auditor closes the gap. Cite the failure by its LP-NN.

---

**SECTION 5 — RECOVERY AUDIT TABLE**

One row per NH-NN annotation (SECTION 3) and per LP-NN loss point (SECTION 2).

| Trigger ID | Triggering Condition | Recovery Mechanism (specific) | MS Step ID Cited | Manual Step Cited (exact text from SECTION 0) |
|------------|---------------------|-------------------------------|-----------------|-----------------------------------------------|

All recovery entries must name a specific mechanism at a specific boundary. A missing row
for any declared NH or LP identifier is a structural gap here — and will be flagged in
SECTION 6.

---

**SECTION 6 — CLOSURE GATE**

*This section is structurally separate from SECTION 5. It does not summarize SECTION 5;
it independently verifies SECTION 5 against the declared NH/LP set.*

Enumerate every NH-NN identifier declared in SECTION 3 and every LP-NN identifier declared
in SECTION 2. For each, check whether a recovery row is present in SECTION 5.

| Identifier | Type (NH / LP) | Declared In (Section and Row) | Recovery Row Present in §5 | Status |
|------------|---------------|-------------------------------|---------------------------|--------|
| NH-01      | NH            | §3, B[?]->?                   | Yes / No                  | CLOSED / OPEN |
| LP-01      | LP            | §2, Stage ?                   | Yes / No                  | CLOSED / OPEN |
| ...        | ...           | ...                           | ...                       | ...          |

**All rows must show CLOSED.** Any row showing OPEN is an explicit, unfixed gap. Do not
proceed past this section if any row is OPEN — state the gap and name the missing recovery
mechanism before continuing.

*The closure gate table must contain one row per declared NH-NN and LP-NN identifier.
Fewer rows than declared identifiers means the gate was not fully executed.*

---

**SECTION 7 — PATTERN ASSESSMENT**

Name the dual-write consistency pattern variant in use. Name one alternative (e.g.,
saga-choreography, outbox pattern, CDC-based sync). State two trade-off dimensions, at
least one quantified in inventory operations terms.

---

*Scoring note: The closure gate in SECTION 6 is independent of SECTION 5. It must enumerate
the declared NH/LP set from first principles — do not generate it by listing what SECTION 5
contains. The purpose is to catch omissions, not to confirm what is present.*

---

## V-04 — Combined: Decomposed Latency Columns + Cumulative SLA%

**Variation axis**: Combined H1 + H2 — both Transport/Processing Overhead separate columns
and a cumulative SLA% running total column in the same boundary inventory table.
**Hypothesis**: Decomposed latency sub-columns force independent component reasoning (H1);
cumulative SLA% forces budget accountability across all boundaries (H2). Together they
should produce the highest latency attribution precision: each boundary has a transport
cost, a processing cost, a per-boundary SLA% draw, and a running budget total. Predicts
that the combined columns will surface the boundary where transport overhead is the
dominant SLA budget consumer — a finding that neither mechanism alone would produce.
Tests whether a seven-column boundary table is completable or whether column-width pressure
causes the model to collapse rightmost columns to prose.

Scenario: Finance accounts receivable aging pipeline — a Finance domain pipeline in which
customer invoice records flow from the billing system through payment application,
aging classification, bad-debt provisioning, and DSO (Days Sales Outstanding) reporting.
Stages: Billing System Extract => Payment Application => Aging Classification =>
Bad-Debt Provisioning => DSO Aggregation => AR Management Report.

---

You are a Finance data domain expert tracing data through an accounts receivable aging
pipeline — customer invoices through payment application, aging classification, bad-debt
provisioning, DSO aggregation, and AR management reporting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Document the manual AR aging procedure this pipeline replaces.

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per close cycle] |

**Minimum required**: five distinct manual steps specific to AR aging and DSO reporting
(e.g., `MS-01: AR analyst exports open invoice list from billing system and applies
payments manually against each invoice line in spreadsheet: 3 hours per daily close`).

After the table:
**INCUMBENT TOTAL**: additive sum. Fixed at declaration.
**AR REPORTING SLA**: maximum elapsed time from billing system cut-off to AR management
report availability before DSO reporting deadline is missed — state in hours. Fixed at
declaration.

**Citation rule**: cite by Step ID (MS-NN) in recovery entries.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Required entities:
**InvoiceRecord, PaymentApplication, AgingBucket, BadDebtProvision, DSOMetric, ARReport.**

State: (a) aging classification bands (e.g., Current / 30 / 60 / 90+ days), (b) DSO
reporting cadence, (c) AR Reporting SLA value.

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS**

Required items per stage:
- **Input schema**: key fields, types, cardinality
- **Transformations**: field-level changes; if unchanged: `verified: no field added,
  removed, renamed, or retyped`
- **Loss point LP-NN**: concrete named failure with sequential LP identifier
- **Typed exit manifest**:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count] | key field assertions:
  [field_name: TYPE(precision)]`

  Minimum two key field assertions per entity.
- **Stage latency**: value or range

**Stage 1 — Billing System Extract**: billing system => AR staging area
**Stage 2 — Payment Application**: AR staging => payment matching service
**Stage 3 — Aging Classification**: payment matching service => aging engine
**Stage 4 — Bad-Debt Provisioning**: aging engine => provisioning service
**Stage 5 — DSO Aggregation**: provisioning service => DSO calculator
**Stage 6 — AR Management Report**: DSO calculator => reporting warehouse => report distribution

---

**SECTION 3 — BOUNDARY INVENTORY WITH DECOMPOSED LATENCY AND CUMULATIVE SLA%**

Produce one row per inter-stage boundary. All eight columns are required — any blank cell
is a structural gap.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Transport Latency | Processing Overhead | Total Boundary Latency | SLA% This Boundary | Cumulative SLA% | Entity at Risk (entity.field — cite exit manifest) |
|----------|--------------------------------------------------------------------|------------------------------------------------|-----------------|--------------------|-----------------------|-------------------|----------------|----------------------------------------------------|
| B1->2    |                                                                    |                                                |                 |                    |                       |                   |                |                                                    |
| B2->3    |                                                                    |                                                |                 |                    |                       |                   |                |                                                    |
| B3->4    |                                                                    |                                                |                 |                    |                       |                   |                |                                                    |
| B4->5    |                                                                    |                                                |                 |                    |                       |                   |                |                                                    |
| B5->6    |                                                                    |                                                |                 |                    |                       |                   |                |                                                    |

**Transport Latency**: network transit, queue depth, serialization. State as numeric ms or s.
"Negligible" is not acceptable — estimate in ms with basis stated inline.
**Processing Overhead**: computation, enrichment lookup, I/O at receiving stage before data
is available downstream. State as numeric ms or s independently from Transport Latency.
**Total Boundary Latency**: must equal Transport Latency + Processing Overhead.
**SLA% This Boundary**: (Total Boundary Latency / AR Reporting SLA) × 100. Numeric %.
**Cumulative SLA%**: running total from B1->2. Must equal previous row's Cumulative SLA%
plus this row's SLA% This Boundary. Carry through all rows.

After the table, state:

**DOMINATION POINT**: the boundary label (B[N]->[N+1]) where Cumulative SLA% first
exceeds 50%. State the cumulative value at crossing. State whether Transport Latency or
Processing Overhead is the larger sub-component at this boundary.

---

**SECTION 4 — STALE WINDOW ANALYSIS**

Accumulate latencies step by step. Name each addend. Compare to AR Reporting SLA.
State whether the domination point from SECTION 3 is the primary staleness driver.
Under failure-mode (LP-NN or NH-NN cited), state separately.

---

**SECTION 5 — RECOVERY AUDIT TABLE**

One row per NH-NN and LP-NN identifier.

| Trigger ID | Triggering Condition | Recovery Mechanism (specific) | MS Step ID Cited | Manual Step Cited (exact text from SECTION 0) |
|------------|---------------------|-------------------------------|-----------------|-----------------------------------------------|

---

**SECTION 6 — PATTERN ASSESSMENT**

Name the integration pattern. Name one alternative. Two trade-off dimensions, at least one
quantified in AR / DSO reporting terms.

---

*Scoring note: Transport Latency and Processing Overhead must each carry an independently
stated numeric value. A table where both columns contain the same value for every boundary,
or where one column is consistently zero, does not satisfy the decomposition requirement.
The Cumulative SLA% column must be computed incrementally, not assigned per-boundary.*

---

## V-05 — Combined: Cumulative SLA% + Structurally Separate Closure Gate

**Variation axis**: Combined H2 + H3 — cumulative SLA% running total with domination-point
identification and a structurally separate closure gate table.
**Hypothesis**: SLA budget accountability (H2) and recovery completeness accountability
(H3) are complementary structural guarantees for the two most common silent failures in
data lineage traces: unquantified latency budget overruns and missing recovery prescriptions.
Combining them tests whether the model can sustain both accountability structures across a
full trace without degrading one in favor of the other. The specific failure mode to probe:
whether the cumulative SLA% column, by requiring ongoing computation through SECTION 3,
causes the model to produce a less complete closure gate in SECTION 6 — i.e., whether
cognitive load on the latency column trades off against closure gate completeness.

Scenario: Operations procurement-to-pay (P2P) pipeline — an Operations/Finance domain
pipeline in which purchase requisitions flow through approval, PO issuance, goods receipt
matching, invoice matching, and payment release. Stages: Requisition Submission =>
Approval Workflow => PO Issuance => Goods Receipt Matching => Invoice Matching =>
Payment Release.

---

You are an Operations data domain expert tracing data through a procurement-to-pay (P2P)
pipeline — purchase requisitions through approval, PO issuance, goods receipt matching,
three-way invoice matching, and payment release.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Document the manual P2P procedure this pipeline replaces.

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per transaction or cycle] |

**Minimum required**: five distinct manual steps specific to P2P operations
(e.g., `MS-01: Procurement officer receives requisition via email, validates budget
availability in ERP, and forwards to department manager for approval: 4 hours per
requisition`). Generic workflow steps not grounded in P2P do not qualify.

After the table:
**INCUMBENT TOTAL**: additive sum. Fixed at declaration.
**PAYMENT SLA**: maximum elapsed time from approved invoice receipt to payment release
before early-payment discount window expires — state in days or hours. Fixed at declaration.

**Citation rule**: cite by Step ID (MS-NN) in recovery entries.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Required entities:
**PurchaseRequisition, ApprovalRecord, PurchaseOrder, GoodsReceiptNote,
VendorInvoice, PaymentInstruction.**

State: (a) three-way match policy (PO line + GRN + Invoice within tolerance),
(b) Payment SLA value declared above,
(c) early-payment discount rate if applicable.

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS**

Required items per stage:
- **Input schema**: key fields, types, cardinality
- **Transformations**: field-level changes; if unchanged: `verified: no field added,
  removed, renamed, or retyped`
- **Loss point LP-NN**: concrete named failure with sequential LP identifier.
  Example: `LP-01: GoodsReceiptNote quantity differs from PurchaseOrder line quantity by
  more than tolerance threshold — VendorInvoice enters matching hold; payment instruction
  not generated; early-payment discount window expires silently.`
- **Typed exit manifest**:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count] | key field assertions:
  [field_name: TYPE(precision)]`

  Minimum two key field assertions per entity.
- **Stage latency**: value or range

**Stage 1 — Requisition Submission**: requestor system => approval workflow engine
**Stage 2 — Approval Workflow**: approval engine => ERP procurement module
**Stage 3 — PO Issuance**: ERP procurement module => PO management service => vendor portal
**Stage 4 — Goods Receipt Matching**: warehouse receiving system => GRN service => matching engine
**Stage 5 — Invoice Matching**: vendor portal + matching engine => invoice matching service
**Stage 6 — Payment Release**: invoice matching service => payment approval service => bank payment gateway

---

**SECTION 3 — BOUNDARY INVENTORY WITH SLA BUDGET ACCOUNTING**

Produce one row per inter-stage boundary. All seven columns are required.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | SLA% This Boundary | Cumulative SLA% | Entity at Risk (entity.field — cite exit manifest) |
|----------|--------------------------------------------------------------------|------------------------------------------------|-----------------|-------------------|-----------------|----------------------------------------------------|
| B1->2    |                                                                    |                                                |                 |                   |                 |                                                    |
| B2->3    |                                                                    |                                                |                 |                   |                 |                                                    |
| B3->4    |                                                                    |                                                |                 |                   |                 |                                                    |
| B4->5    |                                                                    |                                                |                 |                   |                 |                                                    |
| B5->6    |                                                                    |                                                |                 |                   |                 |                                                    |

**SLA% This Boundary**: (Boundary Latency / Payment SLA) × 100. Numeric %. "Negligible"
is not acceptable.
**Cumulative SLA%**: running total from B1->2. Must equal previous Cumulative SLA% plus
this row's SLA% This Boundary. The column must be incrementally computed — not each row
independently.

After the table:

**DOMINATION POINT**: the boundary (B[N]->[N+1]) where Cumulative SLA% first exceeds 50%.
State the value at crossing. State whether this boundary is also the highest single-% consumer.
If cumulative crosses 50% between two specific boundaries, identify the precise crossing row.

---

**SECTION 4 — STALE WINDOW ANALYSIS**

Accumulate latencies step by step. State elapsed time from requisition submission to
payment release under:
1. **Normal operation** (happy path): WITHIN SLA or BREACH; elapsed vs Payment SLA
2. **Three-way match failure** (cite LP-NN): how long the VendorInvoice sits in matching
   hold before resolution; whether the early-payment discount window survives

---

**SECTION 5 — RECOVERY AUDIT TABLE**

One row per NH-NN annotation (SECTION 3) and per LP-NN loss point (SECTION 2).

| Trigger ID | Triggering Condition | Recovery Mechanism (specific) | MS Step ID Cited | Manual Step Cited (exact text from SECTION 0) |
|------------|---------------------|-------------------------------|-----------------|-----------------------------------------------|

All recovery entries must name a specific mechanism at a specific boundary. A missing row
for any declared NH or LP identifier is a structural gap that SECTION 6 will surface.

---

**SECTION 6 — CLOSURE GATE**

*This section is structurally separate from SECTION 5. Do not generate it by listing what
SECTION 5 contains. Generate it by enumerating every NH-NN identifier declared in SECTION 3
and every LP-NN identifier declared in SECTION 2, then checking each against SECTION 5.*

| Identifier | Type (NH / LP) | Declared In (Section and Stage/Boundary) | Recovery Row Present in §5 | Status |
|------------|---------------|------------------------------------------|---------------------------|--------|
| NH-01      | NH            | §3, B[?]->[?]                            | Yes / No                  | CLOSED / OPEN |
| LP-01      | LP            | §2, Stage ?                              | Yes / No                  | CLOSED / OPEN |

**All rows must show CLOSED.** An OPEN row is an unfixed gap — state the missing recovery
mechanism before proceeding. The table must contain one row per declared identifier.
Fewer rows than declared identifiers means the gate was not fully executed.

After the table, state:

**CLOSURE SUMMARY**: `All [N] declared NH/LP identifiers accounted for in §5.` or list
every OPEN identifier by ID with the missing recovery mechanism described.

---

**SECTION 7 — PATTERN ASSESSMENT**

Name the P2P integration pattern. Name one alternative. Two trade-off dimensions, at least
one quantified in P2P operational terms (e.g., "three-way match timeout of 48h increases
on-time payment rate by ~12% vs manual reconciliation but adds 2-day latency vs
two-way-match pipelines").

---

*Scoring note: The closure gate in SECTION 6 must enumerate the declared NH/LP set
independently — do not copy SECTION 5 rows. The Cumulative SLA% column must be computed
as a running total across all five boundaries. Both mechanisms are independently verifiable
and must both be present and complete.*
