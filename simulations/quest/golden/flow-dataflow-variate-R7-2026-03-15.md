# flow-dataflow — Round 7 Variations (Rubric v6)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v6 (C-01 through C-18, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 7 advances the three structural mechanisms crystallized in R6 and tests a fourth new
axis. R6 established that pre-numbering NH-NN/LP-NN trigger IDs at declaration improves
C-18 row-completeness, that stage-exit entity declarations tighten C-17 entity provenance,
that decomposed boundary latency reveals hidden latency domination, and that a post-trace
verification index makes gaps co-visible across criteria. R7 asks: what is the *next*
structural depth each of these mechanisms can reach?

**R7 Hypothesis space:**

**H1 — Typed entity handoff manifests (V-01)**
R6 V-02 required each stage to declare "Entities exiting this stage: [list]" before the
downstream boundary annotation. This enforced C-17 provenance to a forward-declared set
but did not constrain entity quality: a stage could list "ExpenseClaim (modified)" without
specifying what modification occurred or whether the modification changed the type
contract. If the stage-exit declaration is elevated to a typed handoff manifest — entity
name, field count, key field assertions — then the boundary's Entity at Risk annotation
must name an entity whose type contract is specified, not just named. Tests whether typed
handoffs improve C-04 (schema state at each stage) alongside C-17 (entity-at-risk quality).
Specifically tests whether type assertions in the exit manifest trigger downstream boundary
annotations to name the specific field or type at risk, not just the entity.

**H2 — SLA budget framing for boundary latency (V-02)**
R6 V-03 decomposed boundary latency into Transport Latency + Processing Overhead sub-columns.
This produced more precise stale window addend sequences but did not connect each sub-component
to the end-to-end SLA. If each boundary latency annotation also expresses each sub-component
as a percentage of the declared total SLA budget, then latency domination becomes visible in a
single column: a boundary consuming 40% of the SLA budget in transport latency stands out
without requiring the scorer to sum and compare across rows. Tests whether SLA budget framing
forces quantification at boundaries that would otherwise receive qualitative characterization
("real-time" / "micro-batch") and whether it surfaces SLA breaches that additive totals miss.

**H3 — Declaration-to-reference closure enforcement (V-03)**
R6 V-01 required NH-NN and LP-NN identifiers to be assigned at declaration and cited by
number in recovery entries. This created a citation surface but did not enforce that the
recovery table is exhaustive against the declared set. If the prompt explicitly requires a
"closure check" — a post-recovery statement of the form "All NH identifiers declared:
NH-01 through NH-NN. All recovery rows present: [list]" — the LLM must reconcile the
declared set against the recovery table before completing the section. Tests whether
explicit closure enforcement catches recovery table omissions that pre-numbering alone misses,
and whether the closure check surfaces the gap as a visible structural deficit when it fails
rather than a silently missing row.

**H4 — Combined: Typed handoff manifests + SLA budget framing (V-04)**
Combines H1 (typed entity handoff manifests anchor C-17 entity type quality) and H2 (SLA
budget framing forces quantified boundary latency). Tests whether the two mechanisms
reinforce each other: when each stage exit carries type assertions AND each boundary latency
is expressed as SLA budget %, does the combination drive higher C-04 (schema state) and
C-06 (stale window quantification) coverage simultaneously, without crowding out the
essential criteria C-01 through C-04?

**H5 — Combined: All three R7 axes (V-05)**
Combines H1 (typed entity handoff manifests), H2 (SLA budget framing), and H3
(declaration-to-reference closure enforcement). Tests whether all three R7 structural
mechanisms active simultaneously produce the highest composite score for C-04, C-06, C-16,
C-17, C-18 without degrading essential coverage. Tests specifically whether closure
enforcement (H3) catches gaps in the recovery table that go undetected when typed handoffs
(H1) and SLA framing (H2) are both active — i.e., whether H3 is independently load-bearing
or redundant given H1+H2.

**Axes selected for R7:**

1. **Typed entity handoff manifests** — stage-exit declarations with field count and key
   field assertions vs entity-name-only declarations (single axis: V-01)
2. **SLA budget framing** — boundary latency as absolute + SLA % vs absolute only (single
   axis: V-02)
3. **Declaration-to-reference closure enforcement** — explicit closure check after recovery
   table vs pre-numbering only (single axis: V-03)
4. **Combined (H1 + H2)** — typed handoffs + SLA budget framing (V-04)
5. **Combined (H1 + H2 + H3)** — all three R7 axes (V-05)

**New signal candidates for R7:**

1. **Typed entity handoff manifests** (V-01, V-04, V-05) — whether field count and key
   field assertions in stage-exit declarations drive C-04 schema state annotations to name
   the specific field or type at risk (improving criterion depth) vs produce mechanical
   compliance (LLM lists fields without reasoning about risk). Success signal: boundary
   Entity at Risk column cites a specific field name from the exit manifest, not just the
   entity.

2. **SLA budget framing** (V-02, V-04, V-05) — whether expressing boundary latency as % of
   declared SLA budget forces quantification at boundaries that would otherwise be
   characterized as "real-time" or "negligible." Success signal: every boundary has a numeric
   % value in the SLA Budget column, including synchronous API crossings. Failure signal: LLM
   assigns "< 1%" to every synchronous boundary without support, collapsing the SLA budget
   signal.

3. **Closure enforcement** (V-03, V-05) — whether the explicit post-recovery closure
   statement catches recovery table omissions vs whether LLMs produce closure statements that
   are internally inconsistent (closure states NH-01 through NH-04 but table has only 3 rows).
   Success signal: when a gap exists, the closure statement flags it explicitly before the
   section ends. Failure signal: closure statement is generated to match the existing table
   rather than the declared set.

4. **SLA budget domination visibility** (V-02, V-04, V-05) — whether the % column
   immediately reveals which boundary is the pipeline latency bottleneck. Success signal:
   stale analysis cites the high-% boundary by name as the domination point, a conclusion
   that the non-% R6 format did not enforce.

---

## V-01 — Typed Entity Handoff Manifests for Stage-Exit Declarations

**Variation axis**: Structure — elevate stage-exit entity declarations from name-only lists
to typed handoff manifests: entity name, field count delta from entry schema, and at least
one key field assertion (field name and type assertion).
**Hypothesis**: Stage-exit declarations with type assertions constrain the boundary Entity
at Risk annotation to a field-level risk claim, not just an entity-level risk claim. This
drives C-04 (schema state) and C-17 (entity-at-risk) depth simultaneously. Predicts that
typed manifests produce boundary Entity at Risk annotations that name a specific field and
type (e.g., "InvoiceRecord.supplier_bank_code — declared as VARCHAR(20), risk of truncation
at BIC-encoded SWIFT routing field") rather than entity-level labels. A boundary annotation
that names only the entity without a field-level risk claim is evidence that the manifest
constraint was not propagated.

Scenario: Intercompany settlement pipeline — a Finance domain pipeline in which settlement
instructions from subsidiary ledgers are reconciled, netted by currency, and submitted to the
central treasury for intraday SWIFT transfer. Stages: Subsidiary Ledger Extract →
Intercompany Matching → Currency Netting → Settlement Instruction Generation →
SWIFT Transmission → Confirmation Reconciliation.

---

You are a Finance data domain expert tracing data through an intercompany settlement
pipeline — subsidiary ledger extracts through intercompany matching, currency netting,
settlement instruction generation, SWIFT transmission, and confirmation reconciliation.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual intercompany settlement procedure this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID
column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per settlement run] |
| MS-02   | ...         | ...           | ...                       |

**Minimum required**: five distinct manual steps specific to intercompany settlement (e.g.,
MS-01: "Finance controller exports subsidiary ledger to CSV and emails to treasury team:
45 min per settlement cycle"). Generic workflow steps not grounded in intercompany settlement
do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

**Citation rule**: cite incumbent steps by Step ID (MS-NN format) in all downstream recovery
entries. A citation that describes step content without the Step ID does not satisfy C-16.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**SubsidiaryLedgerEntry, IntercompanyMatchRecord, NetPosition, SettlementInstruction,
SWIFTMessage, ConfirmationRecord.**

State: (a) settlement cycle cadence, (b) maximum acceptable settlement staleness threshold
— the elapsed time from ledger cut-off to SWIFT transmission before an intraday
settlement SLA breach risk arises. Fixed at declaration; revisions not permitted.

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS**

For each stage, state all five required items.

Required items per stage:
- **Input schema**: key fields, types, cardinality at stage entry — specific field names
- **Transformations**: every field added, renamed, retyped, or removed; if no change:
  `verified: no field added, removed, renamed, or retyped`
- **Loss point LP-NN**: [concrete named failure] — assign a sequential LP identifier at
  declaration. Example: `LP-01: SWIFT BIC code not found in routing table — settlement
  instruction cannot be generated; claim is orphaned in netting output.`
  "Errors may occur" does not qualify.
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Typed exit manifest**: declare the entities exiting this stage in the following format:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count at exit] | key field assertions:
  [field_name: type, e.g., net_amount: DECIMAL(18,4); currency_code: CHAR(3) ISO-4217]`

  The manifest must include at minimum two key field assertions per entity. A manifest that
  names an entity without field assertions does not qualify. The exit manifest is the sole
  authority for which entities and field types are available for downstream boundary
  annotations.

**Stage 1 — Subsidiary Ledger Extract**: ERP ledger database => settlement staging area
**Stage 2 — Intercompany Matching**: settlement staging area => matching engine
**Stage 3 — Currency Netting**: matching engine => netting calculator
**Stage 4 — Settlement Instruction Generation**: netting calculator => instruction builder
**Stage 5 — SWIFT Transmission**: instruction builder => SWIFT gateway
**Stage 6 — Confirmation Reconciliation**: SWIFT gateway => reconciliation service => treasury ledger

---

**SECTION 3 — BOUNDARY INVENTORY WITH ENTITY AND LATENCY ANNOTATIONS**

Produce one row per inter-stage boundary. All five columns are required — a row with any
blank cell is a structural gap.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk: [entity.field — cite exit manifest] |
|----------|--------------------------------------------------------------------|------------------------------------------------|-----------------|------------------------------------------------------|
| B1->2    |                                                                    |                                                |                 |                                                      |
| B2->3    |                                                                    |                                                |                 |                                                      |
| B3->4    |                                                                    |                                                |                 |                                                      |
| B4->5    |                                                                    |                                                |                 |                                                      |
| B5->6    |                                                                    |                                                |                 |                                                      |

**NH-NN format rule**: if an inter-stage boundary has no error handling mechanism, declare
it as: `NH-01: no handling — risk accepted` (sequential NH number). The identifier is fixed
at declaration and carried forward to SECTION 6.

**Entity at Risk column rule**: the annotation must name a specific entity AND a specific
field from that entity's typed exit manifest in SECTION 2. Format: `entity.field_name —
risk description`. An annotation naming only the entity without a field-level risk claim
does not qualify. A field cited here that is not in the upstream stage's typed exit manifest
is an invalid citation.

**Boundary Latency column rule**: state a value, range, or characterization representing
the overhead at this crossing, distinct from the stage latency in SECTION 2.

---

**SECTION 4 — STALE ANALYSIS**

Accumulate all stage latencies (from SECTION 2) and boundary latencies (from SECTION 3)
step by step, showing each addend:

- After Stage 1: [elapsed]
- After B1->2: [elapsed]
- After Stage 2: [elapsed]
...continue through Stage 6...

Compare the final total against the threshold declared in SECTION 1:
1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure, citing its LP-NN or NH-NN
   identifier): state FRESH or STALE separately

Also identify the single boundary or stage that contributes the largest share of total
elapsed time, citing it by label (B-label or Stage N).

---

**SECTION 5 — STALE DATA WINDOW CHARACTERIZATION**

Separately from Section 4:
1. Under normal operation: state the staleness window for a treasury workstation consumer
   reading net positions between Stage 3 and Stage 5 — this is distinct from end-to-end total
2. Under the worst-case failure mode: state how long the stale window persists before
   recovery closes it

---

**SECTION 6 — RECOVERY AUDIT TABLE**

Produce one row for every NH-NN annotation from SECTION 3 and one row for every LP-NN
loss point from SECTION 2. All five columns are required — a row with any blank cell is a
structural gap.

| Trigger ID | Triggering Condition (verbatim NH-NN text or LP-NN loss point description) | Recovery Mechanism (specific — generic advice fails) | Step ID Cited (MS-NN) | Manual Step Cited (exact value from SECTION 0) |
|-----------|---------------------------------------------------------------------------|------------------------------------------------------|----------------------|------------------------------------------------|

**Trigger ID column rule**: cite the exact NH-NN or LP-NN identifier from its point of
declaration. A row without a Trigger ID is structurally ungroupable.

**Step ID Cited column rule**: cite the MS-NN Step ID from SECTION 0 that serves as the
fallback for this recovery entry. Generic terms such as "manual review" without a Step ID
do not satisfy C-16.

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative settlement architecture (e.g., gross SWIFT per transaction vs end-of-day
netting, bilateral netting vs multilateral central counterparty, real-time gross settlement
vs deferred net settlement). State at least two trade-off dimensions. At least one must
compare the automated pipeline's total elapsed time from SECTION 4 against the **INCUMBENT
TOTAL** declared in SECTION 0, expressed in domain terms (settlement cycle minutes,
cut-off windows, or FX risk exposure time).

---

Produce all sections in order (Sections 0 through 7). Section 0 must appear before any
stage is traced. Section 1 entity inventory must be complete before Section 2 begins.
Typed exit manifests in Section 2 must appear before the corresponding downstream boundary
row in Section 3. A boundary that cites a field not present in the upstream stage's exit
manifest is a traceability failure.

---

## V-02 — SLA Budget Framing for Boundary Latency

**Variation axis**: Output format — add an SLA Budget Consumed (%) column to the boundary
inventory. Each boundary latency sub-component (transport + processing overhead) must also
be expressed as a percentage of the end-to-end SLA budget declared in Section 1.
**Hypothesis**: Expressing boundary latency as SLA budget % forces quantification at
boundaries that would otherwise receive qualitative characterizations ("real-time,"
"negligible"). A boundary consuming 35% of the SLA budget cannot be labeled "negligible"
without contradiction — the % column makes the label false as a structural fact. Predicts
that SLA budget framing drives numeric latency values at every boundary, increases stale
analysis precision (Section 4 can cite the dominant boundary by % rather than by relative
comparison), and surfaces SLA breach conditions that additive totals might obscure
(e.g., when three sub-SLA boundaries sum to a supra-SLA total). A boundary with no % value
is a structural gap in the same way a blank Entity at Risk cell is a gap.

Scenario: Retail vendor replenishment pipeline — an Operations domain pipeline in which
point-of-sale depletion events trigger purchase order generation, vendor fulfillment
confirmation, advance shipment notice receipt, goods receipt, and inventory ledger posting.
Stages: POS Depletion Capture → Replenishment Signal Generation → Purchase Order Issuance
→ Vendor Confirmation → ASN Receipt and Validation → Goods Receipt Posting.

---

You are an Operations data domain expert tracing data through a retail vendor replenishment
pipeline — POS depletion events through replenishment signal generation, purchase order
issuance, vendor confirmation, ASN receipt, and goods receipt posting to inventory ledger.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual replenishment procedure this pipeline
replaces:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per replenishment cycle] |
| MS-02   | ...         | ...           | ...                            |

**Minimum required**: five distinct manual steps specific to retail replenishment (e.g.,
MS-01: "Replenishment planner reviews daily depletion reports and selects SKUs below
reorder point: 2 hours per buyer category"). Generic steps not grounded in retail
replenishment do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

**INCUMBENT SLA**: the end-to-end elapsed time from depletion event to goods receipt
posting that the incumbent process is contractually or operationally expected to achieve.
This value is the denominator for all SLA Budget Consumed (%) calculations in SECTION 3.
Fixed at declaration; may not be revised.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**DepletionEvent, ReplenishmentSignal, PurchaseOrder, VendorConfirmation,
AdvanceShipmentNotice, GoodsReceiptRecord, InventoryLedgerEntry.**

State: (a) replenishment cadence (event-driven vs scheduled), (b) maximum acceptable
replenishment latency — the elapsed time from depletion event to inventory ledger posting
before a stockout SLA breach risk arises. This value must equal the INCUMBENT SLA declared
in SECTION 0. Fixed at declaration.

---

**SECTION 2 — STAGE TRACE**

For each stage, state all five required items:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: every field added, renamed, retyped, or removed; if no change:
  `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point LP-NN**: [concrete named failure] — assign a sequential LP identifier at
  declaration. "Errors may occur" does not qualify.

**Stage 1 — POS Depletion Capture**: POS terminals => inventory event stream
**Stage 2 — Replenishment Signal Generation**: inventory event stream => replenishment engine
**Stage 3 — Purchase Order Issuance**: replenishment engine => procurement system
**Stage 4 — Vendor Confirmation**: procurement system => vendor EDI portal
**Stage 5 — ASN Receipt and Validation**: vendor EDI portal => receiving system
**Stage 6 — Goods Receipt Posting**: receiving system => inventory ledger

---

**SECTION 3 — BOUNDARY INVENTORY WITH SLA BUDGET FRAMING**

Produce one row per inter-stage boundary. All seven columns are required — a row with any
blank cell is a structural gap.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Transport Latency | Processing Overhead | SLA Budget Consumed (%) | Entity at Risk |
|----------|--------------------------------------------------------------------|------------------------------------------------|-------------------|---------------------|------------------------|----------------|
| B1->2    |                                                                    |                                                |                   |                     |                        |                |
| B2->3    |                                                                    |                                                |                   |                     |                        |                |
| B3->4    |                                                                    |                                                |                   |                     |                        |                |
| B4->5    |                                                                    |                                                |                   |                     |                        |                |
| B5->6    |                                                                    |                                                |                   |                     |                        |                |

**NH-NN format rule**: if an inter-stage boundary has no error handling mechanism, declare
it as `NH-01: no handling — risk accepted` (sequential NH number). Fixed at declaration.

**Transport Latency column**: time for the data payload to traverse the queue, network, or
protocol between stages. Must be a value or range; characterizations ("fast," "immediate")
do not qualify.

**Processing Overhead column**: time for boundary-level transformation, validation, or
routing before the next stage begins. Must be a value or range.

**SLA Budget Consumed (%) column**: (Transport Latency + Processing Overhead) ÷ INCUMBENT
SLA, expressed as a percentage. A boundary that receives "negligible" or "< 1%" must carry
a numeric value that supports that characterization. A boundary without a numeric % value
is a structural gap. The column must sum to ≤ 100% under normal operation; if it exceeds
100%, the stale analysis in SECTION 4 must state STALE.

**Entity at Risk column**: name a specific domain entity from SECTION 1. Generic labels
("data," "records") do not qualify.

---

**SECTION 4 — STALE ANALYSIS**

Accumulate transport and processing overhead columns from SECTION 3 separately, then
sum them with stage latencies from SECTION 2, showing each addend. Format:

- After Stage 1: [elapsed] ([SLA% consumed running total])
- After B1->2: [elapsed — transport + processing] ([SLA% consumed running total])
...continue through Stage 6...

At each step, show the running SLA budget total (%). When the running total exceeds 100%,
state the SLA breach point explicitly: "**SLA BREACH** at [step label]: budget exhausted
([running %])."

Compare final total against threshold declared in SECTION 1:
1. **Normal operation**: state FRESH or STALE; cite the single boundary with the highest
   SLA Budget Consumed % as the **budget domination point**
2. **Worst-case failure mode** (name the specific failure, citing LP-NN or NH-NN): state
   FRESH or STALE; state whether the failure shifts the budget domination point

---

**SECTION 5 — STALE DATA WINDOW CHARACTERIZATION**

Separately from Section 4:
1. Under normal operation: the staleness window for a warehouse management system consumer
   reading inventory levels between Stage 3 and Stage 5 (open PO, no goods receipt yet)
2. Under the worst-case failure mode: how long the stale window persists; whether the SLA
   budget domination point from Section 4 determines the recovery window duration

---

**SECTION 6 — RECOVERY AUDIT TABLE**

Produce one row for every NH-NN annotation from SECTION 3 and one row for every LP-NN
loss point from SECTION 2. All five columns are required.

| Trigger ID | Triggering Condition (verbatim NH-NN or LP-NN description) | Recovery Mechanism (specific) | Step ID Cited (MS-NN) | Manual Step Cited (exact value from SECTION 0) |
|-----------|-------------------------------------------------------------|------------------------------|----------------------|------------------------------------------------|

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative replenishment architecture (e.g., consignment vendor-managed inventory
vs buyer-managed replenishment, point-of-sale event streaming vs daily depletion batch,
drop-ship direct vendor vs distribution center routing). State at least two trade-off
dimensions. At least one must compare the automated pipeline's SLA budget consumption
(from SECTION 4) against the **INCUMBENT SLA** declared in SECTION 0, naming the boundary
or stage responsible for the largest budget share.

---

Produce all sections in order (Sections 0 through 7). Section 0 must appear before any
stage is traced. The INCUMBENT SLA declared in Section 0 is the sole denominator for all
SLA Budget Consumed (%) values. The SLA Budget Consumed (%) column in Section 3 must sum
before Section 4 begins; the Section 4 running total is derived from that sum.

---

## V-03 — Declaration-to-Reference Closure Enforcement

**Variation axis**: Structure — require an explicit closure check after the recovery audit
table, reconciling declared NH-NN and LP-NN identifiers against recovery table rows.
**Hypothesis**: Pre-numbering NH-NN/LP-NN identifiers at declaration (R6 Pattern 1) creates
a citation surface but does not enforce exhaustiveness: an LLM may produce a recovery table
that omits a row for NH-03 without detecting the gap if the table is otherwise coherent.
An explicit closure statement of the form "Declared NH identifiers: NH-01 through NH-NN.
Recovery table rows present for: [list]. Missing: [list or NONE]" forces reconciliation.
This shifts gap detection from the scorer (who must cross-reference two sections) to the
producing model (which must enumerate both sets and compare). Predicts that closure
enforcement will either (a) catch omissions the model otherwise misses, or (b) reveal that
LLMs generate closure statements that match the table rather than the declared set —
producing a false-complete closure statement when a row is missing. Either outcome is a
signal: (a) confirms the mechanism works; (b) confirms it fails in a specific, detectable
way that a meta-rubric criterion can address.

Scenario: Subscription billing pipeline — a Commerce domain pipeline in which usage
metering data is aggregated, contract entitlements applied, billing line items calculated,
invoices generated, and payment collection initiated. Stages: Usage Meter Ingestion →
Entitlement Application → Billing Calculation → Invoice Generation → Payment Collection
→ Revenue Recognition Posting.

---

You are a Commerce data domain expert tracing data through a subscription billing pipeline
— usage metering through entitlement application, billing calculation, invoice generation,
payment collection, and revenue recognition posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual billing procedure this pipeline replaces:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per billing cycle] |
| MS-02   | ...         | ...           | ...                      |

**Minimum required**: five distinct manual steps specific to subscription billing (e.g.,
MS-01: "Billing analyst exports raw usage logs from monitoring system and cross-references
against contract tiers in spreadsheet: 3 hours per billing period").

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**UsageMeterRecord, EntitlementRecord, BillingLineItem, Invoice, PaymentTransaction,
RevenueRecognitionEntry.**

State: (a) billing cycle cadence, (b) maximum acceptable billing staleness threshold — the
elapsed time from usage meter ingestion to revenue recognition posting before a monthly-close
revenue reporting SLA breach risk arises. Fixed at declaration.

---

**SECTION 2 — STAGE TRACE WITH NH-NN AND LP-NN ASSIGNMENT**

For each stage, state all five required items. All NH and LP identifiers assigned in this
section and in SECTION 3 constitute the complete declared set. The closure check in
SECTION 6b will reconcile the recovery table against this set.

- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: every field added, renamed, retyped, or removed; if no change:
  `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization
- **Loss point LP-NN**: [concrete named failure] — assign a sequential LP identifier at
  declaration. This identifier is a member of the declared set. "Errors may occur" does
  not qualify.

**Stage 1 — Usage Meter Ingestion**: metering agents => usage aggregation service
**Stage 2 — Entitlement Application**: usage aggregation service => entitlement engine
**Stage 3 — Billing Calculation**: entitlement engine => billing engine
**Stage 4 — Invoice Generation**: billing engine => invoice service
**Stage 5 — Payment Collection**: invoice service => payment gateway
**Stage 6 — Revenue Recognition Posting**: payment gateway => revenue ledger

---

**SECTION 3 — BOUNDARY INVENTORY**

Produce one row per inter-stage boundary. All five columns are required.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk |
|----------|--------------------------------------------------------------------|------------------------------------------------|-----------------|----------------|
| B1->2    |                                                                    |                                                |                 |                |
| B2->3    |                                                                    |                                                |                 |                |
| B3->4    |                                                                    |                                                |                 |                |
| B4->5    |                                                                    |                                                |                 |                |
| B5->6    |                                                                    |                                                |                 |                |

**NH-NN format rule**: declare no-handling annotations as `NH-NN: no handling — risk
accepted` (sequential number). The identifier is a member of the declared set. Fixed at
declaration; may not be revised or renumbered in later sections.

**Entity at Risk column rule**: name a specific domain entity from SECTION 1.

**Boundary Latency column rule**: value, range, or characterization distinct from stage
latency.

---

**SECTION 4 — STALE ANALYSIS**

Accumulate all stage and boundary latencies step by step. Compare final total against
threshold declared in SECTION 1:
1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (cite LP-NN or NH-NN): state FRESH or STALE separately

---

**SECTION 5 — STALE DATA WINDOW CHARACTERIZATION**

1. Under normal operation: staleness window for a revenue controller reading billing status
   between Stage 3 and Stage 5
2. Under the worst-case failure mode: how long the stale window persists

---

**SECTION 6 — RECOVERY AUDIT TABLE WITH CLOSURE ENFORCEMENT**

**SECTION 6a — Recovery Audit Table**

Produce one row for every NH-NN annotation from SECTION 3 and one row for every LP-NN
loss point from SECTION 2. All five columns are required.

| Trigger ID | Triggering Condition (verbatim NH-NN or LP-NN description) | Recovery Mechanism (specific) | Step ID Cited (MS-NN) | Manual Step Cited (exact value from SECTION 0) |
|-----------|-------------------------------------------------------------|------------------------------|----------------------|------------------------------------------------|

**SECTION 6b — Closure Check** (mandatory — must appear after 6a and before Section 7)

State the following four items explicitly:

1. **Declared NH identifiers**: list every NH-NN identifier assigned in SECTION 3, in
   order (e.g., "NH-01, NH-02, NH-03").
   If no NH identifiers were declared, state: "No NH identifiers declared."

2. **Declared LP identifiers**: list every LP-NN identifier assigned in SECTION 2, in
   order (e.g., "LP-01, LP-02, LP-03, LP-04, LP-05, LP-06").
   If no LP identifiers were declared, state: "No LP identifiers declared."

3. **Recovery rows present for**: list every Trigger ID that appears in the SECTION 6a
   table (e.g., "NH-01, NH-02, LP-01, LP-02, LP-03, LP-04, LP-05, LP-06").

4. **Missing recovery rows**: list every declared identifier (from items 1 and 2) that
   does not appear in item 3. If all declared identifiers have a recovery row, state:
   "NONE — all declared identifiers have a recovery row."

A closure check that lists zero missing rows when the declared set is larger than the
recovery table row count is a traceability failure. The closure check does not repair the
gap — it surfaces it. If missing rows are identified, do not add rows retroactively; leave
the gap visible.

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative billing architecture (e.g., usage-based post-pay vs prepaid credit
drawdown, consolidated monthly invoice vs per-event micro-invoice, batch revenue
recognition vs real-time continuous recognition). State at least two trade-off dimensions.
At least one must compare the automated pipeline's total elapsed time from SECTION 4
against the **INCUMBENT TOTAL** declared in SECTION 0.

---

Produce all sections in order (Sections 0 through 7). Section 6b (Closure Check) must
appear after Section 6a and before Section 7. The declared NH and LP sets in Section 6b
are read-only: identifiers may not be added or removed after their point of declaration
(SECTION 2 for LP, SECTION 3 for NH). The closure check compares the declared set against
the table; it does not revise either.

---

## V-04 — Combined: Typed Entity Handoff Manifests + SLA Budget Framing

**Variation axes**: (V-01) Typed entity handoff manifests at stage exit + (V-02) SLA
budget framing for boundary latency.
**Hypothesis**: Typed handoff manifests (H1) constrain Entity at Risk annotations to
field-level risk claims; SLA budget framing (H2) forces numeric latency quantification at
every boundary. Together they create two independent structural surfaces that each drive
criteria depth for different criteria (C-04/C-17 for H1; C-05/C-06 for H2). The combined
prompt tests whether the two mechanisms reinforce each other: when a stage exit carries
type assertions AND each boundary latency is expressed as SLA %, does the combination
drive the stale analysis (Section 4) to cite a specific field type at the dominant boundary
— a conclusion neither mechanism alone enforces? Also tests whether the additional
structural requirements crowd out C-01 (lineage chain completeness) by increasing section
length.

Scenario: Vendor invoice payment terms sync pipeline — a Finance domain pipeline in which
vendor payment terms from a supplier portal are synchronized to the ERP accounts payable
module, validated against procurement contract terms, and applied to open purchase orders.
Stages: Supplier Portal Extract → Payment Terms Normalization → Contract Terms Validation
→ ERP Payment Terms Update → Open PO Application → AP Ledger Reconciliation.

---

You are a Finance data domain expert tracing data through a vendor invoice payment terms
sync pipeline — supplier portal extracts through payment terms normalization, contract
terms validation, ERP update, open PO application, and AP ledger reconciliation.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual payment terms synchronization procedure
this pipeline replaces:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per sync cycle] |
| MS-02   | ...         | ...           | ...                   |

**Minimum required**: five distinct manual steps specific to payment terms management
(e.g., MS-01: "AP coordinator downloads updated supplier payment terms PDF and manually
keys net days and discount tiers into ERP vendor master: 15 min per vendor, up to 40
vendors per cycle").

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.

**INCUMBENT SLA**: the end-to-end elapsed time from supplier portal update to AP ledger
reconciliation that the manual process achieves. This is the SLA budget denominator for
SECTION 3. Fixed at declaration.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities:
**VendorPaymentTermsRecord, NormalizedPaymentTerm, ContractTermsRecord,
ERPVendorMasterRecord, OpenPurchaseOrder, APLedgerEntry.**

State: (a) sync cadence, (b) maximum acceptable payment terms staleness threshold — the
elapsed time from supplier portal update to AP ledger reconciliation before a late-payment
penalty risk arises. Must equal the INCUMBENT SLA declared in SECTION 0.

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS**

For each stage, state all five required items:
- **Input schema**: key fields, types, cardinality
- **Transformations**: every field change; if none: `verified: no field added, removed,
  renamed, or retyped`
- **Loss point LP-NN**: concrete named failure — sequential LP identifier at declaration
- **Latency**: value, range, or characterization
- **Typed exit manifest**: declare entities exiting this stage in the format:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count at exit] | key field assertions:
  [field_name: type, e.g., net_days: INTEGER(3); early_pay_discount_pct: DECIMAL(5,4)]`

  Minimum two key field assertions per entity. A manifest naming an entity without field
  assertions does not qualify. The exit manifest is the sole authority for field types
  available to downstream boundary Entity at Risk annotations.

**Stage 1 — Supplier Portal Extract**: supplier self-service portal => integration middleware
**Stage 2 — Payment Terms Normalization**: integration middleware => normalization service
**Stage 3 — Contract Terms Validation**: normalization service => contract compliance engine
**Stage 4 — ERP Payment Terms Update**: contract compliance engine => ERP vendor master
**Stage 5 — Open PO Application**: ERP vendor master => PO management module
**Stage 6 — AP Ledger Reconciliation**: PO management module => AP ledger

---

**SECTION 3 — BOUNDARY INVENTORY WITH SLA BUDGET FRAMING**

Produce one row per inter-stage boundary. All seven columns are required.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Transport Latency | Processing Overhead | SLA Budget Consumed (%) | Entity at Risk: [entity.field — cite exit manifest] |
|----------|--------------------------------------------------------------------|------------------------------------------------|-------------------|---------------------|------------------------|------------------------------------------------------|
| B1->2    |                                                                    |                                                |                   |                     |                        |                                                      |
| B2->3    |                                                                    |                                                |                   |                     |                        |                                                      |
| B3->4    |                                                                    |                                                |                   |                     |                        |                                                      |
| B4->5    |                                                                    |                                                |                   |                     |                        |                                                      |
| B5->6    |                                                                    |                                                |                   |                     |                        |                                                      |

**NH-NN format rule**: declare no-handling as `NH-NN: no handling — risk accepted`.
Fixed at declaration.

**Transport Latency**: time for payload traversal. Value or range required.

**Processing Overhead**: time for boundary-level validation or routing. Value or range
required.

**SLA Budget Consumed (%)**: (Transport + Processing) ÷ INCUMBENT SLA as a percentage.
Numeric value required — qualitative characterizations do not qualify. Sum must be stated
before Section 4 begins.

**Entity at Risk**: `entity.field_name — risk description`. The field_name must appear in
the upstream stage's typed exit manifest. An annotation citing a field not in the
upstream manifest is a traceability failure.

---

**SECTION 4 — STALE ANALYSIS WITH SLA BUDGET RUNNING TOTAL**

Accumulate stage and boundary latencies step by step. Show SLA budget % running total at
each step. Identify the **budget domination point** — the single step (stage or boundary)
with the largest individual SLA % contribution. State whether the domination point is
determined by Transport Latency or Processing Overhead sub-component.

Compare final total against threshold declared in SECTION 1:
1. **Normal operation**: FRESH or STALE; cite budget domination point by label and field
   type (from exit manifest) at that stage/boundary
2. **Worst-case failure mode** (cite LP-NN or NH-NN): FRESH or STALE separately; state
   whether the domination point shifts under failure

---

**SECTION 5 — STALE DATA WINDOW CHARACTERIZATION**

1. Under normal operation: staleness window for an AP controller reading vendor payment
   terms between Stage 3 and Stage 5 (validated but not yet applied to open POs)
2. Under worst-case failure mode: how long the stale window persists; whether the budget
   domination point determines the recovery window duration

---

**SECTION 6 — RECOVERY AUDIT TABLE**

Produce one row for every NH-NN annotation from SECTION 3 and one row for every LP-NN
loss point from SECTION 2. All five columns are required.

| Trigger ID | Triggering Condition (verbatim NH-NN or LP-NN description) | Recovery Mechanism (specific) | Step ID Cited (MS-NN) | Manual Step Cited (exact value from SECTION 0) |
|-----------|-------------------------------------------------------------|------------------------------|----------------------|------------------------------------------------|

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative payment terms synchronization architecture (e.g., supplier portal
push via EDI ORDERS vs buyer-initiated portal pull, real-time event webhook vs nightly
batch sync, centralized vendor master vs distributed ERP-per-subsidiary). State at least
two trade-off dimensions. At least one must compare the automated pipeline's SLA budget
consumption from SECTION 4 against the **INCUMBENT SLA**, naming the budget domination
point and its field type as the primary architectural driver.

---

Produce all sections in order (Sections 0 through 7). Typed exit manifests in Section 2
must appear before the corresponding boundary row in Section 3. The SLA Budget Consumed (%)
column must be populated before Section 4 begins — Section 4 running totals are derived
directly from it. The budget domination point identified in Section 4 must be cited in
Section 7 by label and field type.

---

## V-05 — Combined: Typed Handoff Manifests + SLA Budget Framing + Closure Enforcement

**Variation axes**: (V-01) Typed entity handoff manifests + (V-02) SLA budget framing +
(V-03) Declaration-to-reference closure enforcement.
**Hypothesis**: All three R7 structural mechanisms active simultaneously: typed manifests
anchor C-17 field-level Entity at Risk quality; SLA % framing forces numeric boundary
latency quantification; closure enforcement reconciles the declared NH/LP set against the
recovery table. Tests whether H3 (closure check) is independently load-bearing when H1
and H2 are also active: if typed manifests and SLA framing already drive high structural
completeness, does the closure check catch residual gaps or produce redundant reporting
of an already-complete table? Also tests whether the combined prompt is too long — whether
section complexity causes the LLM to drop entity field assertions or LP identifiers under
cognitive load, degrading C-01 or C-04 coverage in a way that neither V-01, V-02, nor
V-03 alone produces.

Scenario: Customer order-to-cash pipeline — a Finance/Operations/Commerce domain pipeline
in which customer purchase orders are received, credit checked, fulfilled, shipped, invoiced,
and cash collected. Finance owns credit check and cash collection; Operations owns
fulfillment and shipping; Commerce owns order receipt and invoicing. Stages: Order Receipt
→ Credit Check → Order Fulfillment → Shipment → Invoice Generation → Cash Collection.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
customer order-to-cash pipeline — order receipt through credit check, fulfillment,
shipment, invoice generation, and cash collection.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any stage is traced, document the manual order-to-cash procedure this pipeline
replaces:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01   | [step name] | [role / team] | [time per order] |
| MS-02   | ...         | ...           | ...              |

**Minimum required**: five distinct manual steps specific to order-to-cash (e.g., MS-01:
"Credit analyst pulls customer credit history from bureau portal and manually scores
against internal credit policy matrix: 30 min per order for new customers").

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.

**INCUMBENT SLA**: the end-to-end elapsed time from order receipt to cash collection
posting that the manual process achieves. This is the SLA budget denominator for
SECTION 3. Fixed at declaration.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities:
**CustomerPurchaseOrder, CreditAssessmentRecord, FulfillmentOrder, ShipmentRecord,
Invoice, PaymentReceipt.**

State: (a) order processing cadence, (b) maximum acceptable order-to-cash staleness
threshold — the elapsed time from order receipt to cash collection before a days-sales-
outstanding (DSO) SLA breach risk arises. Must equal the INCUMBENT SLA.

---

**SECTION 2 — STAGE TRACE WITH TYPED EXIT MANIFESTS AND NH/LP ASSIGNMENT**

For each stage, state all five required items. All LP identifiers assigned here, and all
NH identifiers assigned in SECTION 3, constitute the complete **declared set** for the
closure check in SECTION 6b.

- **Input schema**: key fields, types, cardinality
- **Transformations**: every field change; if none: `verified: no field added, removed,
  renamed, or retyped`
- **Loss point LP-NN**: concrete named failure — sequential LP identifier at declaration.
  This identifier is a member of the declared set and will be verified in SECTION 6b.
- **Latency**: value, range, or characterization
- **Typed exit manifest**:

  `EXIT MANIFEST — Stage N: [entity name] | fields: [count at exit] | key field assertions:
  [field_name: type, e.g., credit_limit_usd: DECIMAL(15,2); approval_status: ENUM(APPROVED,
  PENDING, REJECTED)]`

  Minimum two key field assertions per entity. Field assertions are the sole authority for
  which field types are available to downstream boundary Entity at Risk annotations.

**Stage 1 — Order Receipt**: customer portal / EDI => order management system
**Stage 2 — Credit Check**: order management system => credit assessment service
**Stage 3 — Order Fulfillment**: credit assessment service => warehouse management system
**Stage 4 — Shipment**: warehouse management system => logistics system
**Stage 5 — Invoice Generation**: logistics system => billing service
**Stage 6 — Cash Collection**: billing service => accounts receivable ledger

---

**SECTION 3 — BOUNDARY INVENTORY WITH SLA BUDGET FRAMING**

Produce one row per inter-stage boundary. All seven columns are required — a row with any
blank cell is a structural gap. All NH identifiers assigned here are members of the
declared set for the closure check in SECTION 6b.

| Boundary | Error Handling (mechanism or NH-NN: "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Transport Latency | Processing Overhead | SLA Budget Consumed (%) | Entity at Risk: [entity.field — cite exit manifest] |
|----------|--------------------------------------------------------------------|------------------------------------------------|-------------------|---------------------|------------------------|------------------------------------------------------|
| B1->2    |                                                                    |                                                |                   |                     |                        |                                                      |
| B2->3    |                                                                    |                                                |                   |                     |                        |                                                      |
| B3->4    |                                                                    |                                                |                   |                     |                        |                                                      |
| B4->5    |                                                                    |                                                |                   |                     |                        |                                                      |
| B5->6    |                                                                    |                                                |                   |                     |                        |                                                      |

**NH-NN format rule**: declare no-handling as `NH-NN: no handling — risk accepted`. Fixed
at declaration; member of the declared set.

**Transport Latency**: time for payload traversal — value or range required.

**Processing Overhead**: time for boundary-level validation or routing — value or range
required.

**SLA Budget Consumed (%)**: (Transport + Processing) ÷ INCUMBENT SLA as a percentage.
Numeric value required for every boundary.

**Entity at Risk**: `entity.field_name — risk description`. The field_name must appear in
the upstream stage's typed exit manifest. A field not in the manifest is an invalid citation.

---

**SECTION 4 — STALE ANALYSIS WITH SLA BUDGET RUNNING TOTAL**

Accumulate stage and boundary latencies step by step. Show SLA budget % running total at
each step. Identify the **budget domination point** and state which sub-component
(Transport or Processing Overhead) drives it.

Compare final total against threshold declared in SECTION 1:
1. **Normal operation**: FRESH or STALE; cite budget domination point by label and by
   the specific field type at risk (from exit manifest) at that stage/boundary
2. **Worst-case failure mode** (cite LP-NN or NH-NN): FRESH or STALE separately

---

**SECTION 5 — STALE DATA WINDOW CHARACTERIZATION**

1. Under normal operation: staleness window for an AR controller reading invoice status
   between Stage 4 and Stage 6 (shipped but not yet collected)
2. Under the worst-case failure mode: how long the stale window persists; whether the
   budget domination point determines recovery window duration

---

**SECTION 6 — RECOVERY AUDIT TABLE WITH CLOSURE ENFORCEMENT**

**SECTION 6a — Recovery Audit Table**

Produce one row for every NH-NN annotation from SECTION 3 and one row for every LP-NN
loss point from SECTION 2. All five columns are required.

| Trigger ID | Triggering Condition (verbatim NH-NN or LP-NN description) | Recovery Mechanism (specific) | Step ID Cited (MS-NN) | Manual Step Cited (exact value from SECTION 0) |
|-----------|-------------------------------------------------------------|------------------------------|----------------------|------------------------------------------------|

**SECTION 6b — Closure Check** (mandatory — must appear after 6a and before Section 7)

State the following four items:

1. **Declared NH identifiers**: list every NH-NN assigned in SECTION 3, in order.
   If none, state: "No NH identifiers declared."

2. **Declared LP identifiers**: list every LP-NN assigned in SECTION 2, in order.
   If none, state: "No LP identifiers declared."

3. **Recovery rows present for**: list every Trigger ID appearing in the SECTION 6a table.

4. **Missing recovery rows**: list every declared identifier (items 1 + 2) not in item 3.
   If none, state: "NONE — all declared identifiers have a recovery row."

The closure check does not repair gaps. If missing rows are identified, leave the gap
visible — do not add rows after the check.

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative order-to-cash architecture (e.g., credit pre-screening at account
setup vs per-order credit check, ship-from-store vs warehouse-to-door fulfillment, real-
time invoice-on-ship vs end-of-period consolidated invoicing). State at least two trade-off
dimensions. At least one must compare the automated pipeline's SLA budget consumption from
SECTION 4 against the **INCUMBENT SLA**, naming the budget domination point and its field
type as the primary architectural driver. At least one dimension must reference a specific
domain role (Finance credit controller, Operations warehouse manager, or Commerce AR
specialist) and the decision authority that role exercises in the incumbent baseline.

---

Produce all sections in order (Sections 0 through 7). Typed exit manifests in Section 2
must appear before the corresponding boundary row in Section 3. The SLA Budget Consumed (%)
column must be populated before Section 4 begins. Section 6b (Closure Check) must appear
after Section 6a and before Section 7. The declared NH and LP sets are read-only from the
point of declaration: identifiers may not be added or removed after their declaring section
completes.
