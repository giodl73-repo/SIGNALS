# flow-dataflow — Round 3 Variations (Rubric v2)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v2 (C-01 through C-12, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 3 builds on R2's two new aspirational signals: C-10 (pre-trace entity inventory),
C-11 (systematic boundary labeling), and C-12 (verified-unchanged schema assertion). These
three criteria represent structural discipline that can be scaffolded into prompts explicitly
— each one is testable without reading the surrounding text if the prompt creates the right
compliance surface.

The rubric's essential criteria represent the four floor failures in naive outputs:
- C-01: Lineage chain breaks (an entity appears at destination with no traceable origin)
- C-02: Boundary silence (inter-stage handoffs with no error annotation at all)
- C-03: Loss-point vagueness (stage "can fail" without naming a specific failure mode)
- C-04: Schema drift without annotation (a stage that silently changes types or fields)

**Failure modes to probe in R3:**

The v2 aspirationals raise a structural design question: can each of C-10, C-11, C-12 be
explicitly scaffolded into a prompt without creating a verbose, unusable prompt? And does
scaffolding all three simultaneously in V-05 produce a prompt that is measurably better
on those criteria without hurting the essential coverage?

**Axes selected:**

1. **Role sequence** — natural Finance → Operations → Commerce vs non-natural
   Operations → Commerce → Finance establishes whether role ordering affects
   citation-chain completeness and incumbent-baseline visibility.

2. **Output format** — table-dominant format with a named-column schema-diff table
   per stage tests whether structural column requirements enforce C-04 and C-11
   better than prose descriptions.

3. **Lifecycle emphasis** — inline boundary gates ("complete B[N]->[N+1] before
   opening Stage N+1") test whether gate language enforces C-02 compliance better
   than a post-hoc boundary summary section.

4. **Inertia framing** — a mandatory incumbent-baseline section owned by the first
   role, which subsequent roles must cite, tests whether grounding the trace in a
   named manual process improves C-06 (stale window quantification) and C-09
   (trade-off analysis) quality.

**New signal candidates for R3:**

1. **Schema-diff table** (V-02) — a 4-column table (Field / Entry Schema /
   Transformations / Exit Schema) makes silent schema changes visually detectable;
   an empty Transformations cell is an obvious structural gap even without reading
   the stage prose.

2. **Inline boundary gate with stage-open prohibition** (V-03) — stating "Stage N+1
   does not open until boundary gate B[N]->[N+1] is complete" makes omission
   structurally impossible in a way that post-hoc summary sections do not.

3. **Label-embedded "no handling" flag** (V-05) — requiring the boundary label to
   appear inside the flag text itself (e.g., "no handling — risk accepted [B2->3]")
   makes each unhandled boundary directly addressable in recovery prescriptions
   without re-reading the full trace.

---

## V-01 — Role Sequence: Natural Finance-First

**Variation axis**: Role sequence
**Hypothesis**: Finance → Operations → Commerce in natural domain order with standard
prose structure and no explicit aspirational scaffolding. Finance traces the financial
pipeline stages; Operations traces fulfillment and sync stages; Commerce traces revenue
and reporting stages. Tests whether natural ordering plus explicit essential-criteria
instructions can reach all four essential and three recommended criteria without
scaffolding for C-10, C-11, or C-12.

Scenario: B2B accounts receivable-to-GL synchronization pipeline — customer payment
receipt through AR matching, aging calculation, GL journal posting, and revenue
reporting. Finance-domain entities dominate; Operations manages the sync and scheduling
stages; Commerce owns the reporting layer.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a B2B
accounts receivable-to-GL synchronization pipeline — customer payment receipt through AR
matching, aging bucket calculation, GL journal posting, and revenue analytics reporting.
Three expert roles contribute in the sequence **Finance → Operations → Commerce**.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**DOMAIN CONTEXT** (Finance)

Declare the entity vocabulary in scope for this trace: CustomerPayment, AREntry,
AgingBucket, JournalEntry, GLPosting, RevenueSnapshot. State the business cadence
(real-time, hourly, daily). State the maximum acceptable AR staleness threshold — this
value is fixed after this section; revisions are not permitted once Stage 1 begins.

---

**FINANCE — STAGE TRACE**

For each stage below, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: every field added, renamed, retyped, or removed — specific names
  required, "same as input" does not qualify
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: at least one concrete, named failure mode at this stage — "errors may
  occur" does not qualify

**Stage 1 — Payment Receipt**: customer banking portal → payment ingestion service
**Stage 2 — AR Matching**: payment ingestion service → AR matching engine

---

**OPERATIONS — STAGE TRACE**

Continue the trace using the same stage format.

**Stage 3 — Aging Calculation**: AR matching engine → aging scheduler service
**Stage 4 — GL Journal Posting**: aging scheduler service → GL journal writer

---

**COMMERCE — STAGE TRACE**

Continue the trace using the same stage format.

**Stage 5 — Revenue Snapshot**: GL journal writer → revenue aggregation service
**Stage 6 — Analytics Reporting**: revenue aggregation service → finance analytics
dashboard

---

**BOUNDARY CHECKS**

For each inter-stage boundary, produce one entry covering:
- **Error handling**: the specific mechanism (retry, dead-letter queue, compensating
  transaction, idempotency key, manual requeue) or "no handling — risk accepted"
- **Schema transition**: whether the schema changes at this boundary; if unchanged,
  state "unchanged"
- **Boundary latency**: processing overhead at this crossing point

Cover all five boundaries: B1->2, B2->3, B3->4, B4->5, B5->6.

---

**STALE ANALYSIS** (Commerce)

Sum all stage latencies and boundary latencies into an end-to-end elapsed total. Compare
against the staleness threshold declared in DOMAIN CONTEXT under two scenarios:

1. **Normal operation**: state FRESH or STALE and the elapsed total
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE

Address failure-mode staleness separately from normal-operation staleness.

---

**RECOVERY PRESCRIPTIONS** (Commerce)

For every "no handling — risk accepted" annotation in BOUNDARY CHECKS and every loss
point in STAGE TRACE, produce a paired recovery prescription. Each prescription must
name the specific recovery mechanism and the boundary or stage it applies to. Generic
advice does not qualify.

---

**TRADE-OFF ANALYSIS** (Commerce)

Name an alternative pipeline pattern (e.g., event-driven CDC vs daily batch ETL,
dual-write vs single-write with async replication, real-time AR matching vs
end-of-day sweep). State at least two trade-off dimensions. At least one must be
quantified or qualified in AR-to-GL domain terms (e.g., "introduces a 4-hour stale
window in aging buckets under the daily-batch variant").

---

Produce all sections in the order shown. Do not skip or reorder sections.

---

## V-02 — Output Format: Table-Dominant Schema Diffs

**Variation axis**: Output format
**Hypothesis**: Every stage gets a named-column schema-diff table (Field / Entry Schema /
Transformations / Exit Schema) and every boundary appears as a row in a BOUNDARY SUMMARY
TABLE. This structural approach makes schema drift (C-04) visually auditable — an empty
Transformations cell is an obvious gap — and forces boundary label discipline (C-11) via
required row labels without naming the criterion explicitly.

Scenario: Customer order CDX sync pipeline — SalesOrder creation in the commerce system
through inventory reservation, warehouse fulfillment allocation, shipment tracking, invoice
generation, and AR posting. Commerce-to-Finance data flow with Operations owning the
fulfillment stages.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
customer order CDX sync pipeline — order creation through inventory reservation, warehouse
fulfillment allocation, shipment event processing, invoice generation, and AR posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**DOMAIN CONTEXT**

Declare: entity vocabulary (SalesOrder, OrderLineItem, InventoryReservation,
FulfillmentAllocation, ShipmentEvent, Invoice, AREntry); business cadence; maximum
acceptable order-status staleness threshold — fixed after this section.

---

**STAGE TRACE**

For each stage, produce a schema-diff table followed by the latency and loss-point entries.
**Every stage must have a complete schema-diff table and both the latency and loss-point
entries — a missing row or blank cell is a structural gap.**

Schema-diff table format:

| Field | Entry Schema | Transformations | Exit Schema |
|-------|-------------|-----------------|-------------|
| [field name] | [type / cardinality at entry] | [change description or "— no change"] | [type / cardinality at exit] |

After each table:
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: concrete named failure mode — "errors may occur" fails

**Stage 1 — Order Capture**: customer web portal → order management service
**Stage 2 — Inventory Reservation**: order management service → inventory reservation
service
**Stage 3 — Fulfillment Allocation**: inventory reservation service → warehouse management
system
**Stage 4 — Shipment Event Processing**: warehouse management system → shipment tracking
service
**Stage 5 — Invoice Generation**: shipment tracking service → invoicing service
**Stage 6 — AR Posting**: invoicing service → AR system → finance data warehouse

---

**BOUNDARY SUMMARY TABLE**

Produce one row per inter-stage boundary. **All five columns are required — a row with any
blank cell is a structural gap.**

| Boundary | Error Handling (mechanism or "no handling — risk accepted") | Schema Change (Y/N; if N: "unchanged") | Boundary Latency | Domain Entity at Risk |
|----------|-------------------------------------------------------------|----------------------------------------|-----------------|----------------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

The Domain Entity at Risk column must name a specific entity from DOMAIN CONTEXT — "data"
or "records" does not qualify.

---

**STALE ANALYSIS**

Sum stage latencies and boundary latencies from the schema-diff tables and BOUNDARY SUMMARY
TABLE into an end-to-end elapsed total. State FRESH or STALE under (1) normal operation
and (2) worst-case failure mode, comparing against the threshold from DOMAIN CONTEXT.
Address both scenarios separately.

---

**RECOVERY PRESCRIPTIONS**

For every "no handling — risk accepted" row in BOUNDARY SUMMARY TABLE and every loss point
in STAGE TRACE, produce a paired prescription naming the mechanism and the boundary row
label or stage. Reference the boundary label (e.g., "B3->4:") at the start of each entry.
Generic advice does not qualify.

---

**TRADE-OFF ANALYSIS**

Name an alternative order-sync pattern (e.g., CDX event stream vs polling pull, dual-write
vs CDC, synchronous allocation vs async reservation). State at least two trade-off
dimensions, at least one quantified in order-fulfillment domain terms.

---

Produce all sections in the order shown.

---

## V-03 — Lifecycle Emphasis: Inline Boundary Gates

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Explicit inline gate language — "Stage N+1 does not open until boundary
gate B[N]->[N+1] is complete" — enforces C-02 (boundary error handling) by making
omission structurally visible rather than relying on a post-hoc summary section. When
the boundary check is an integral gate that must fire before the next stage body opens,
a missing annotation is a gate-not-cleared protocol violation, not a prose omission.

Scenario: Inventory demand-to-replenishment batch pipeline — warehouse demand signal
generation through purchase order creation, supplier EDI transmission, goods receipt
processing, and stock ledger update.

---

You are a Finance / Operations / Commerce data domain expert tracing data through an
inventory demand-to-replenishment batch pipeline — warehouse demand signal generation
through purchase order creation, supplier EDI transmission, goods receipt processing, and
stock ledger update.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**STEP 1 — DOMAIN CONTEXT**

Declare: entity vocabulary (DemandSignal, PurchaseOrder, SupplierOrder, GoodsReceipt,
StockLedgerEntry, InventoryPosition); business cadence; maximum acceptable stock-level
staleness threshold — this value is locked after Step 1 and may not be revised.

---

**STEP 2 — STAGE 1: Demand Signal Generation**

Warehouse management system → demand calculation service.

State:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: every field added, renamed, retyped, or removed — specific names
  required
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization
- **Loss point**: concrete named failure — "errors may occur" fails

**BOUNDARY GATE B1->2** — Complete before opening Stage 2:
- Error handling at Stage 1 → Stage 2: name the mechanism (retry, dead-letter, idempotency
  key) or state "no handling — risk accepted"
- Boundary latency at B1->2
- Schema continuity at B1->2: state whether schema changes; if not, state "unchanged"

**Stage 2 does not open until BOUNDARY GATE B1->2 is fully stated.**

---

**STEP 3 — STAGE 2: Purchase Order Creation**

Demand calculation service → purchase order service.

Same format as Stage 1.

**BOUNDARY GATE B2->3** — Complete before opening Stage 3:
- Same three fields as B1->2.

**Stage 3 does not open until BOUNDARY GATE B2->3 is fully stated.**

---

**STEP 4 — STAGE 3: Supplier EDI Transmission**

Purchase order service → supplier EDI gateway.

Same format.

**BOUNDARY GATE B3->4** — Complete before opening Stage 4:
- Same three fields.

**Stage 4 does not open until BOUNDARY GATE B3->4 is fully stated.**

---

**STEP 5 — STAGE 4: Goods Receipt Processing**

Supplier EDI gateway → goods receipt service.

Same format.

**BOUNDARY GATE B4->5** — Complete before opening Stage 5:
- Same three fields.

**Stage 5 does not open until BOUNDARY GATE B4->5 is fully stated.**

---

**STEP 6 — STAGE 5: Stock Ledger Update**

Goods receipt service → stock ledger service → inventory analytics dashboard.

Same format. This is the terminal stage; no outbound boundary gate is required.

---

**STEP 7 — STALE ANALYSIS**

Sum all stage latencies and boundary latencies (accumulate step by step, showing each
addend). Compare the end-to-end total against the threshold from Step 1 under:

1. **Normal operation**: FRESH or STALE?
2. **Worst-case failure** (name the specific failure): FRESH or STALE?

State the two verdicts separately. Do not blend them.

---

**STEP 8 — RECOVERY PRESCRIPTIONS**

For every "no handling — risk accepted" boundary gate and every named loss point, provide
a paired prescription naming the recovery mechanism and the specific gate label or stage.
Generic advice fails.

---

**STEP 9 — TRADE-OFF ANALYSIS**

Name an alternative replenishment pattern (e.g., continuous min-max replenishment vs
periodic batch review, vendor-managed inventory vs buyer-driven PO, event-driven demand
signal vs scheduled MRP run). State at least two trade-off dimensions, at least one in
inventory-management domain terms (e.g., "VMI eliminates B1->2 transmission latency but
requires supplier read-access to stock ledger").

---

Work through Steps 1 through 9 in order. Do not skip any step or gate.

---

## V-04 — Role Sequence + Inertia Framing: Non-Natural Operations-First

**Variation axis**: Role sequence (non-natural O→C→F) combined with inertia framing
**Hypothesis**: Operations runs first and establishes the incumbent manual workflow as a
mandatory baseline section. Commerce (pos 2) cites Operations' artifacts; Finance
(pos 3) runs last and must cite Operations' boundary checks directly — two positions prior
in the O→C→F sequence — as a required skip-level citation. The inertia framing tests
whether grounding the trace in named manual steps with durations improves stale-window
quantification (C-06) and trade-off analysis quality (C-09), since the baseline provides
an explicit comparison point that all subsequent roles must reference.

Scenario: Purchase-to-pay procurement pipeline — goods receipt confirmation through
invoice 3-way matching, payment authorization, bank payment execution, and GL
reconciliation. Operations owns the receiving and matching stages; Commerce owns the
payment and settlement stages; Finance runs last and owns GL reconciliation and
trade-off analysis.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
purchase-to-pay procurement pipeline — goods receipt confirmation through supplier invoice
3-way matching, payment authorization, bank payment execution, and GL reconciliation.
Three expert roles run in the non-natural sequence **Operations → Commerce → Finance**.

Operations runs first and establishes the incumbent manual procurement baseline that all
subsequent roles must cite. Commerce and Finance must reference Operations' artifacts by
section name — they may not redeclare or re-derive the baseline or the entity vocabulary.
Finance runs last and must cite Operations' boundary artifacts directly — two positions
prior in the Operations → Commerce → Finance sequence — as a required skip-level citation.
A Finance section that cites only Commerce artifacts without citing Operations' boundary
checks fails the skip-level citation requirement.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**OPERATIONS — INCUMBENT BASELINE**

Describe the manual procurement process this pipeline replaces. Name at least four manual
steps with durations (e.g., "AP clerk opens supplier email: 10 min per invoice"). Compute
a total manual processing time. This total is the sole authority for the manual-process
comparison required in Finance's trade-off analysis. Do not split or re-derive this total
in later sections.

---

**OPERATIONS — DOMAIN CONTEXT**

Declare the entity vocabulary: GoodsReceipt, SupplierInvoice, PurchaseOrder,
ThreeWayMatchResult, PaymentAuthorization, BankPayment, GLEntry. State the business
cadence. State the maximum acceptable payment-processing staleness threshold — fixed after
this section.

---

**OPERATIONS — STAGE TRACE**

For each stage: input schema (key fields, types, cardinality), transformations (specific
named fields), output schema, latency, loss point (concrete — "errors may occur" fails).

**Stage 1 — Goods Receipt**: receiving dock scanner → goods receipt service
**Stage 2 — Invoice Ingestion**: supplier portal → invoice digitization service

**Boundary check B1->2** (inline, before Stage 2 text): error-handling mechanism or
"no handling — risk accepted"; boundary latency; schema transition note.

---

**COMMERCE — STAGE TRACE**

Citing: Operations INCUMBENT BASELINE (total manual processing time) and Operations
DOMAIN CONTEXT (entity vocabulary, staleness threshold). These are the sole sources
for the baseline total and entity names; do not redeclare them.

**Stage 3 — Three-Way Match**: invoice digitization service → 3-way match engine
**Stage 4 — Payment Authorization**: 3-way match engine → payment authorization service

Same stage format.

**Boundary check B2->3** (inline, before Stage 3): same format.
**Boundary check B3->4** (inline, before Stage 4): same format.
**Boundary check B4->5** (inline, stated after Stage 4 and before Finance opens):
same format.

---

**FINANCE — STAGE TRACE**

Citing: Operations INCUMBENT BASELINE total (skip-level — two positions prior in
Operations → Commerce → Finance); Operations boundary checks B1->2 and B2->3
(skip-level). A Finance section that cites only Commerce artifacts without naming
Operations INCUMBENT BASELINE or Operations boundary checks does not satisfy the
skip-level citation requirement.

**Stage 5 — Bank Payment Execution**: payment authorization service → bank payment
gateway
**Stage 6 — GL Reconciliation**: bank payment gateway → GL reconciliation service →
ERP general ledger

Same stage format.

**Boundary check B5->6** (inline, before Stage 6): same format.

---

**STALE ANALYSIS** (Finance)

Accumulate elapsed time across all stages (1–6) and all boundary latencies (B1->2 through
B5->6). State FRESH or STALE under (1) normal operation and (2) worst-case failure mode
(named). Address both separately, comparing against the threshold from Operations DOMAIN
CONTEXT.

---

**RECOVERY PRESCRIPTIONS** (Finance)

For every "no handling — risk accepted" boundary check and every named loss point across
all three role sections, provide a paired prescription naming the mechanism and location.
For critical failure modes, the prescription must reference Operations INCUMBENT BASELINE
as the identified fallback process. Generic advice fails.

---

**TRADE-OFF ANALYSIS** (Finance)

Name an alternative payment-processing pattern (e.g., straight-through processing vs
exception-based routing, same-day ACH vs next-day batch, pre-approved PO vs invoice-led
matching). State at least two trade-off dimensions. One must compare the automated
pipeline's total latency against the Operations INCUMBENT BASELINE total manual time
cited by token.

---

Produce all sections in the order shown: Operations, Commerce, Finance.

---

## V-05 — Combined: Entity Inventory + Boundary Labeling + Schema Verification

**Variation axis**: Lifecycle emphasis combined with output format (C-10 + C-11 + C-12
all explicitly scaffolded)
**Hypothesis**: All three new aspirational criteria can be scaffolded into a single prompt
without producing a verbose or unusable output. C-10 (pre-trace entity inventory) is
enforced by a dedicated STEP 0 section that locks the entity namespace before Stage 1.
C-11 (boundary labeling) is enforced by requiring the boundary label to appear inside
every "no handling" flag. C-12 (verified-unchanged schema assertion) is enforced by a
named rule requiring an explicit verification statement at pass-through stages. If all
three criteria can be structurally enforced without obscuring essential coverage, the
combined prompt should score higher on all five aspirational criteria than any
single-axis variation.

Scenario: Subscription billing-to-revenue recognition pipeline — usage event collection
through metering aggregation, billing calculation, invoice generation, revenue schedule
creation, and deferred revenue GL posting. All three domain roles are represented in
natural Finance → Operations → Commerce ordering.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
subscription billing-to-revenue recognition pipeline — usage event collection through
metering aggregation, billing calculation, invoice generation, revenue schedule creation,
and deferred revenue GL posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**STEP 0 — DOMAIN ENTITY INVENTORY**

Before any stage is traced, enumerate all in-scope domain entities by name in a dedicated
list. Every entity that appears in the stage trace, boundary checks, or stale analysis
must appear here first. An entity introduced mid-trace without a prior entry in this
inventory is a protocol violation.

Minimum required entities: UsageEvent, MeteringAggregate, BillingRecord, Invoice,
RevenueSchedule, DeferredRevenueEntry, GLPosting. Add any additional entities the
pipeline requires.

After the entity list, state:
- Business cadence
- Maximum acceptable revenue-recognition staleness threshold — fixed after Step 0;
  revisions are not permitted

---

**STAGE TRACE**

For each stage, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: every field added, renamed, retyped, or removed — specific field
  names required; "same as input" fails
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: concrete named failure — "errors may occur" fails

**Schema-unchanged rule**: If a stage makes no schema change, you must state: "**verified:
no field added, removed, renamed, or retyped at this stage.**" A bare "unchanged" with no
verification claim fails.

**Stage 1 — Usage Metering**: usage event collector → metering aggregation service
**Stage 2 — Billing Calculation**: metering aggregation service → billing calculation
engine
**Stage 3 — Invoice Generation**: billing calculation engine → invoicing service
**Stage 4 — Revenue Recognition**: invoicing service → revenue recognition engine
**Stage 5 — GL Posting**: revenue recognition engine → deferred revenue GL service →
finance data warehouse

---

**BOUNDARY CHECKS**

Produce one labeled entry per inter-stage boundary. The label must follow the exact pattern
B[N]->[N+1]. **All four boundaries are required — a missing label is a structural gap
visible without reading any surrounding text.**

For each boundary:
- **Label**: B[N]->[N+1] (e.g., B1->2)
- **Error handling**: the specific mechanism (retry, idempotency key, dead-letter queue,
  compensating write) — or exactly: "no handling — risk accepted [B[N]->[N+1]]" with the
  boundary label embedded in the flag
- **Schema transition**: whether schema changes; if unchanged: "verified unchanged at
  B[N]->[N+1]"
- **Boundary latency**: processing overhead at this crossing

Required labels: **B1->2**, **B2->3**, **B3->4**, **B4->5**.

A labeled boundary with no error-handling annotation is a visible, scorable gap.

---

**STALE ANALYSIS**

Accumulate elapsed time across all stages and boundaries, showing each step:

- After Stage 1: [elapsed]
- After B1->2: [elapsed]
- After Stage 2: [elapsed]
- ... through Stage 5

Compare the final total against the threshold from STEP 0 under:
1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE

---

**RECOVERY PRESCRIPTIONS**

For every "no handling — risk accepted [B[N]->[N+1]]" annotation in BOUNDARY CHECKS and
every loss point in STAGE TRACE, produce a paired prescription. Each entry must:

1. Open with the specific boundary label or stage (e.g., "**B2->3:**", "**Stage 3 loss
   point:**")
2. Name the recovery mechanism
3. Name the specific entity from the Step 0 inventory that the recovery protects

Generic advice — without a boundary label and an entity name — does not qualify.

---

**TRADE-OFF ANALYSIS**

Name an alternative billing architecture (e.g., event-sourced metering vs periodic
aggregation batch, waterfall revenue recognition vs ASC 606 performance-obligation
allocation engine, synchronous GL posting vs async journal queue). State at least two
trade-off dimensions. At least one must be quantified in subscription-billing domain
terms (e.g., "periodic aggregation introduces a 1-hour recognition lag vs real-time
accrual for UsageEvents").

---

Produce all steps and sections in the order shown. Reference only entities from the Step 0
DOMAIN ENTITY INVENTORY throughout the trace, boundary checks, stale analysis, and
recovery prescriptions.
