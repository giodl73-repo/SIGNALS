# flow-dataflow — Round 6 Variations (Rubric v5)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v5 (C-01 through C-19, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 6 targets the three new aspirational criteria crystallized in v5 from R5 V-02 patterns:

- **C-17 (Entity-at-risk annotation per boundary)** — every boundary in the C-11 labeled
  inventory must name a specific domain entity at risk of loss or corruption. Generic labels
  ("data," "records") fail. A boundary with no entity-at-risk annotation fails.

- **C-18 (Structured recovery audit table)** — all recovery prescriptions organized as a
  table with at minimum three columns: triggering condition (the specific "no handling"
  annotation or named loss point), recovery mechanism, and boundary or stage reference.
  Prose recovery sections do not qualify. Every NH annotation and every loss point must
  have a row.

- **C-19 (Per-boundary latency annotation)** — the boundary inventory includes a latency
  annotation per boundary — value, range, or characterization — distinct from the per-stage
  latency required by C-05. A boundary with no latency annotation fails.

R5 V-02 introduced structural prototypes for all three: an Entity at Risk column in the
BOUNDARY TABLE (C-17 prototype), a five-column RECOVERY AUDIT TABLE with "Entry Source" and
"Location" (C-18 prototype), and a Boundary Latency column in the BOUNDARY TABLE (C-19
prototype). R6 tests how to sharpen these structural surfaces — specifically the quality and
verifiability of C-17 entity naming, C-18 triggering-condition linkage, and C-19 latency
specificity.

**R6 Hypothesis space:**

**H1 — Trigger ID pre-numbering (V-01)**
R5's C-18 recovery table used "Entry Source" (prose) and "Location" (B-label) to identify
what each recovery row addresses. The v5 rubric sharpens C-18 by requiring the triggering
condition column to contain "the specific 'no handling' annotation or named loss point being
addressed" — not a generic category. If "no handling" annotations and loss points are
pre-numbered (NH-NN, LP-NN) at the point of declaration, the triggering condition column
becomes a citation target: a recovery row either contains "NH-02" or it does not. Tests
whether pre-numbering at declaration time produces higher C-18 row-completeness than
expecting the LLM to reconstruct which annotation each row addresses from memory.

**H2 — Stage-exit entity declaration (V-02)**
R5 V-02 required the Entity at Risk column to be populated at boundary annotation time,
with no prior declaration constraining which entities were in scope. This introduces risk
of ad-hoc entity invention — entities named at the boundary that were not established in
the C-10 pre-trace inventory or C-07 domain framing. If each stage is required to declare
"Entities exiting this stage: [list]" before the downstream boundary is written, the
boundary's Entity at Risk annotation must choose from a declared, traceable set. Tests
whether stage-exit entity declaration produces higher C-17 entity quality (entities drawn
from C-10/C-07 vocabulary, not invented at boundary time) than boundary-level free-form
naming.

**H3 — Boundary latency decomposition (V-03)**
C-19 requires per-boundary latency distinct from per-stage latency (C-05) but does not
specify what the latency represents. A boundary latency can be composed of: (a) transport
latency — time for the data payload to traverse the network or queue between stages, and
(b) processing overhead — time for boundary-level transformation, validation, or routing
before the next stage begins. Splitting these into two sub-columns forces independent
characterization and makes the stale analysis addend sequence more precise. Tests whether
decomposition produces more specific stale window analysis and whether it surfaces
otherwise-hidden latency that changes FRESH/STALE verdicts. A single combined column
still satisfies C-19 floor; this tests aspirational depth.

**H4 — Cross-reference verification index (V-04)**
After the boundary table and recovery audit table, requiring a named verification index
(one row per boundary: Boundary | Entity at Risk | Boundary Latency | Recovery Row
Reference | Step ID Cited) creates a single surface where C-11, C-17, C-18, C-19, and
C-16 are simultaneously visible. A blank cell in any column reveals which criterion is
missing for which boundary — without requiring the scorer to cross-reference four separate
sections. Tests whether a post-trace verification index catches C-17/C-18/C-19 gaps that
were missed when the criteria were embedded in separate sections.

**H5 — Combined: Trigger IDs + stage-exit entity declaration + recovery audit table
with triggering condition column + cross-reference verification index (V-05)**
Combines H1 (trigger IDs make C-18 triggering conditions machine-verifiable) + H2
(stage-exit entity declarations anchor C-17 entity quality) + C-18 recovery table with
an explicit "Triggering Condition" column containing the NH-NN/LP-NN citation + H4
(cross-reference index makes all three criteria co-visible per boundary). Tests whether
the combination of all three R6 axes produces the highest composite score for the new
criteria while maintaining essential coverage and not crowding out C-01 through C-04.

**Axes selected for R6:**

1. **Trigger ID precision** — NH-NN/LP-NN pre-numbering at declaration vs free-text
   triggering condition (single axis: V-01)
2. **Entity-at-risk declaration timing** — stage-exit forward declaration vs boundary-level
   annotation only (single axis: V-02)
3. **Boundary latency decomposition** — transport + processing sub-columns vs single
   combined column (single axis: V-03)
4. **Cross-reference verification index** — post-trace verification table vs embedded-only
   criteria (single axis: V-04)
5. **Combined** — all three R6 innovations together (V-05)

**New signal candidates for R6:**

1. **NH-NN / LP-NN trigger IDs** (V-01, V-05) — pre-numbering boundary "no handling"
   annotations and stage loss points at declaration creates the citation surface for C-18
   triggering condition completeness. If LLM outputs cite "NH-03" verbatim, C-18 row
   coverage is unambiguously verifiable; if they use free-text, the scorer must interpret
   whether the description matches an annotation.

2. **Stage-exit entity declaration** (V-02, V-05) — "Entities exiting this stage: [list]"
   as a mandatory stage-close element chains C-07/C-10 into C-17 lineage. Whether the
   exiting entity declaration improves C-17 citation quality vs generates pass-through
   compliance (LLM copies entity list without grounded reasoning about which is at risk).

3. **Boundary latency decomposition** (V-03) — whether splitting transport and processing
   overhead produces more specific FRESH/STALE thresholds and whether the decomposition
   reveals latency domination at specific boundary types (queue-based vs synchronous API).

4. **Cross-reference verification index** (V-04, V-05) — whether a post-trace
   verification table catches C-17/C-18/C-19 gaps vs whether the per-boundary tabular
   view creates redundancy that LLMs fill mechanically rather than substantively.

---

## V-01 — Trigger ID Pre-Numbering for C-18 Triggering Condition Precision

**Variation axis**: Output format — pre-number every "no handling" annotation (NH-NN) and
every stage loss point (LP-NN) at the point of declaration, enabling machine-verifiable
C-18 triggering condition completeness
**Hypothesis**: The v5 C-18 rubric requires the triggering condition column to contain the
specific annotation or loss point being addressed — not a category label. Pre-numbering
each NH annotation and LP loss point at declaration creates a citation target the recovery
table can reference by ID. Without pre-numbering, recovery rows must reconstruct the
triggering condition from memory, risking paraphrase ambiguity and missed rows. Predicts
higher C-18 row-completeness than free-text triggering conditions because every NH-NN and
LP-NN declared is a recovery table row that either exists or is a visible gap.

Scenario: Employee expense claim processing pipeline — expense claim submission through
receipt OCR validation, policy compliance check, manager approval, finance audit, and
payment disbursement. Finance owns finance audit and payment disbursement; Operations
owns receipt OCR validation and policy compliance; Commerce owns expense claim submission
and manager approval routing.

---

You are a Finance / Operations / Commerce data domain expert tracing data through an
employee expense claim processing pipeline — expense claim submission through receipt OCR
validation, policy compliance check, manager approval, finance audit, and payment
disbursement.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual expense processing procedure this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID
column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per claim or per batch] |
| MS-02 | ... | ... | ... |

**Minimum required**: five distinct manual steps specific to the expense processing domain
(e.g., MS-01: "Finance coordinator manually reviews printed receipts against claim form:
20 min per claim"). Each Step ID must follow the MS-NN format exactly. Generic workflow
steps not grounded in expense processing do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

**Citation rule**: in all downstream sections, cite incumbent steps by Step ID (MS-NN
format). A citation that describes step content without the Step ID does not satisfy C-16.
Every recovery entry in SECTION 6 must carry a Step ID citation.

This table and its INCUMBENT TOTAL are the sole authority for:
- Step ID citations required in SECTION 6 (Recovery Audit Table)
- Baseline comparison required in SECTION 7 (Trade-Off Analysis)

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**ExpenseClaim, ReceiptImage, OCRReceiptRecord, PolicyAssessment, ApprovalRecord,
FinanceAuditRecord, PaymentInstruction, DisbursementConfirmation.**

State: (a) business cadence, (b) maximum acceptable claim-to-payment staleness threshold —
the elapsed time from claim submission to payment disbursement before an employee
reimbursement SLA breach risk arises. Fixed at declaration; revisions not permitted.

---

**SECTION 2 — STAGE TRACE WITH TRIGGER ID ASSIGNMENT**

For each stage, state all five required items. Loss points must be declared using the LP-NN
format — this identifier is fixed at declaration and referenced in SECTION 6.

Required items per stage:
- **Input schema**: key fields, types, cardinality at stage entry — specific field names
- **Transformations**: every field added, renamed, retyped, or removed; if no change:
  `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point LP-NN**: [concrete named failure] — assign a sequential LP identifier.
  Example: `LP-01: Receipt image corruption during upload causes OCR to return empty fields
  — claim cannot proceed without manual re-upload.` "Errors may occur" does not qualify.

**Stage 1 — Claim Submission**: employee portal => expense management service
**Stage 2 — Receipt OCR Validation**: expense management service => OCR processing service
**Stage 3 — Policy Compliance Check**: OCR processing service => policy engine
**Stage 4 — Manager Approval**: policy engine => approval workflow service
**Stage 5 — Finance Audit**: approval workflow service => finance review service
**Stage 6 — Payment Disbursement**: finance review service => payment processing service => payroll/AP service

---

**SECTION 3 — BOUNDARY INVENTORY WITH TRIGGER ID ASSIGNMENT**

Produce one row per inter-stage boundary. All six columns are required — a row with any
blank cell is a structural gap.

"No handling" annotations must be declared using the NH-NN format — this identifier is
fixed at declaration and referenced in SECTION 6.

| Boundary | Error Handling (NH-NN: "no handling — risk accepted" or mechanism name) | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk |
|----------|-------------------------------------------------------------------------|------------------------------------------------|-----------------|----------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

**NH-NN format rule**: if an inter-stage boundary has no error handling mechanism, declare
it as: `NH-01: no handling — risk accepted` (assigning the next sequential NH number). The
identifier is carried forward to SECTION 6. Boundaries that cannot silently drop data
should still annotate their mechanism by name.

**Entity at Risk column rule**: name a specific entity from SECTION 1 inventory. Generic
labels ("data," "records," "payload") do not qualify. The entity must be the one most at
risk of loss or corruption if the error handling described fails.

**Boundary Latency column rule**: state a value, range, or characterization representing
the overhead at this crossing, distinct from the stage latency in SECTION 2.

---

**SECTION 4 — STALE ANALYSIS**

Accumulate all stage latencies (from SECTION 2) and boundary latencies (from SECTION 3
Boundary Latency column) step by step, showing each addend:

- After Stage 1: [elapsed]
- After B1->2: [elapsed]
- After Stage 2: [elapsed]
- After B2->3: [elapsed]
- After Stage 3: [elapsed]
- After B3->4: [elapsed]
- After Stage 4: [elapsed]
- After B4->5: [elapsed]
- After Stage 5: [elapsed]
- After B5->6: [elapsed]
- After Stage 6: [elapsed total]

Compare the final total against the threshold declared in SECTION 1:
1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure, citing its LP-NN or NH-NN
   identifier): state FRESH or STALE separately

---

**SECTION 5 — STALE DATA WINDOW CHARACTERIZATION**

Separately from Section 4's pipeline latency analysis:
1. Under normal operation: state the staleness window for a consumer reading claim status
   mid-pipeline (between Stage 3 and Stage 5) — this is distinct from the end-to-end total
2. Under the worst-case failure mode identified in Section 4: state how long the stale
   window persists before recovery closes it

---

**SECTION 6 — RECOVERY AUDIT TABLE**

Produce one row for every NH-NN annotation from SECTION 3 and one row for every LP-NN
loss point from SECTION 2. **All five columns are required — a row with any blank cell
is a structural gap detectable without reading surrounding prose.**

| Trigger ID | Triggering Condition (verbatim NH-NN text or LP-NN loss point description) | Recovery Mechanism (specific — generic advice fails) | Step ID Cited (MS-NN) | Manual Step Cited (exact value from SECTION 0) |
|-----------|---------------------------------------------------------------------------|------------------------------------------------------|----------------------|------------------------------------------------|

**Trigger ID column rule**: cite the exact NH-NN or LP-NN identifier from the point of
declaration. A row without a Trigger ID is structurally ungroupable — it may duplicate
or miss an NH or LP.

**Triggering Condition column rule**: state the verbatim NH-NN declaration text or the
LP-NN loss point description from the section where it was declared. A paraphrase that
omits the identifier does not qualify.

**Step ID Cited column rule**: cite the MS-NN Step ID from SECTION 0 that serves as the
fallback for this recovery entry. Generic terms such as "manual review" without a Step ID
do not satisfy C-16. Every row must carry an MS-NN citation — a blank cell is a C-16 gap.

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative expense processing architecture (e.g., receipt-first OCR-gated
submission vs claim-first async receipt matching, mobile real-time approval vs weekly
batch finance audit, direct AP disbursement vs payroll cycle integration). State at least
two trade-off dimensions. At least one must compare the automated pipeline's total elapsed
time from SECTION 4 against the **INCUMBENT TOTAL** declared in SECTION 0.

---

Produce all sections in order (Sections 0 through 7). Section 0 must appear before any
stage or boundary content. Every NH-NN and LP-NN declared must appear as a row in the
Section 6 Recovery Audit Table — a missing row is a structural gap.

---

## V-02 — Stage-Exit Entity Declaration for C-17 Entity Quality

**Variation axis**: Lifecycle emphasis — entities exiting each stage must be explicitly
declared before the downstream boundary annotation, anchoring C-17 entity-at-risk
selection to a forward-declared traceable set
**Hypothesis**: R5 V-02 required the Entity at Risk column at boundary time with no prior
declaration constraining which entities were in scope — creating risk of ad-hoc entity
invention at boundary level. If each stage closes with "Entities exiting this stage:
[EntityName, EntityName]" before the boundary annotation is written, the boundary's
Entity at Risk annotation must choose from a declared, in-scope set traceable to the C-10
inventory or C-07 domain framing. Tests whether stage-exit entity declaration produces
higher C-17 entity quality (inventory-traced, not invented) vs boundary-level free-form
naming. Predicts that stage-exit declaration catches entity substitution artifacts — cases
where an LLM invents a plausible-sounding entity name at boundary time that was never
declared in the entity vocabulary.

Scenario: Purchase order to payment pipeline — PO approval through goods receipt,
three-way match, AP invoice creation, payment authorization, and bank reconciliation.
Finance owns AP invoice creation, payment authorization, and bank reconciliation;
Operations owns goods receipt and three-way match; Commerce owns PO approval and supplier
relationship data.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
purchase order to payment pipeline — from PO approval through goods receipt, three-way
match, AP invoice creation, payment authorization, and bank reconciliation.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual PO-to-payment process this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per PO or per batch] |
| MS-02 | ... | ... | ... |

**Minimum required**: five distinct manual steps specific to the PO-to-payment domain
(e.g., MS-01: "AP coordinator manually matches printed PO, goods receipt slip, and
supplier invoice: 30 min per PO"). Generic steps not grounded in procure-to-pay do not
qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.

Citation rule: cite incumbent steps by Step ID (MS-NN format) in all downstream
sections. Every recovery entry must carry an MS-NN citation.

---

**DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**PurchaseOrder, GoodsReceiptNote, SupplierInvoice, ThreeWayMatchResult, APInvoiceRecord,
PaymentInstruction, BankReconciliationEntry.**

State: (a) business cadence (e.g., daily PO volumes, invoice batch cycle), (b) maximum
acceptable PO-to-payment staleness threshold — the elapsed time from goods receipt to bank
reconciliation before payment terms compliance risk arises (e.g., net-30 breach). Fixed
at declaration.

---

**STAGE TRACE WITH STAGE-EXIT ENTITY DECLARATION**

For each stage, state all required items in the order shown. The "Entities Exiting" line
is mandatory and must appear before the downstream boundary annotation is written.

Required items per stage:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: specific field names for every addition, rename, type change, or
  removal; if no change: `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization
- **Loss point**: a concrete named failure mode — "errors may occur" does not qualify
- **Entities exiting this stage**: [EntityName, EntityName] — list every domain entity
  (from the ENTITY INVENTORY above) that exits this stage and is the direct subject of
  the next boundary. An entity not listed in the inventory must not appear here. This
  declaration is the constraint on the downstream boundary's Entity at Risk selection.

**Stage 1 — PO Approval**: ERP procurement module => PO management service
**Stage 2 — Goods Receipt**: warehouse receiving system => goods receipt service
**Stage 3 — Three-Way Match**: goods receipt service => matching engine
**Stage 4 — AP Invoice Creation**: matching engine => AP invoicing service
**Stage 5 — Payment Authorization**: AP invoicing service => payment gateway
**Stage 6 — Bank Reconciliation**: payment gateway => bank reconciliation service

---

**BOUNDARY TABLE**

Produce one row per inter-stage boundary. All six columns are required — a row with any
blank cell is a structural gap.

**Entity at Risk column rule**: the entity named here must appear in the "Entities exiting
this stage" declaration of the preceding stage. An entity that was not declared as exiting
does not qualify — its presence here is an inventory violation. Generic labels ("data,"
"records") do not qualify.

| Boundary | Error Handling (mechanism or "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk (must be drawn from preceding stage-exit declaration) |
|----------|-------------------------------------------------------------|------------------------------------------------|-----------------|----------------------------------------------------------------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

---

**STALE ANALYSIS**

Accumulate stage and boundary latencies step by step, showing each addend through Stage 6.
Compare the final total against the threshold declared in DOMAIN CONTEXT:

1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE separately

Also state the staleness exposure window for a supplier querying invoice status between
Stage 4 (AP Invoice Creation) and Stage 5 (Payment Authorization) — distinguish from the
end-to-end total.

---

**RECOVERY PRESCRIPTIONS**

For every "no handling — risk accepted" annotation in BOUNDARY TABLE and every named loss
point in STAGE TRACE, provide a paired recovery prescription. Each entry must:

1. Open with the specific boundary label (B[N]->[N+1]) or stage loss point name
2. Name the specific recovery mechanism (retry with backoff, dead-letter queue,
   compensating write, idempotency key — generic advice fails)
3. Name the protected entity drawn from the Entity at Risk column or stage entity
   vocabulary
4. Cite the fallback by its Step ID (MS-NN format) from the INCUMBENT BASELINE TABLE —
   every recovery entry must carry an MS-NN citation

---

**TRADE-OFF ANALYSIS**

Name an alternative PO-to-payment architecture (e.g., two-way match vs three-way match
with automated receipt, early payment discount program vs standard net-30 cycle, integrated
ERP AP module vs standalone payment orchestration layer). State at least two trade-off
dimensions. At least one must compare the automated pipeline's total elapsed time from
STALE ANALYSIS against the **INCUMBENT TOTAL** declared in INCUMBENT BASELINE TABLE.

---

Produce all sections in the order shown. Every "Entities exiting this stage" declaration
must appear before the downstream boundary row for that stage is written. A boundary's
Entity at Risk that cannot be traced to the preceding stage-exit declaration is a C-17
inventory violation.

---

## V-03 — Boundary Latency Decomposition for C-19 Depth

**Variation axis**: Output format — boundary latency split into Transport Latency (queue /
network traversal) and Processing Overhead (boundary-level validation, routing, or
transformation) as distinct columns
**Hypothesis**: C-19 requires per-boundary latency distinct from per-stage latency but
does not specify its composition. Boundary latency consists of two independently observable
components: transport latency (time for the data payload to traverse the queue or network
between stages) and processing overhead (time for boundary-level validation, routing,
schema mapping, or buffering before the next stage begins). Splitting these forces
independent characterization, makes it possible to identify which latency component
dominates at each boundary type (synchronous API call vs async queue vs batch window),
and produces a more precise stale analysis addend sequence. Tests whether decomposition
surfaces latency domination patterns that a single combined column obscures — and whether
a boundary with near-zero transport latency but high processing overhead would be
mischaracterized without decomposition.

Scenario: Financial period close pipeline — from subledger data extraction through
consolidation aggregation, currency revaluation, intercompany elimination, trial balance
generation, and statutory report output. Finance owns all stages but Operations owns
subledger maintenance and Commerce owns the revenue recognition subledger.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
financial period close pipeline — from subledger data extraction through consolidation
aggregation, currency revaluation, intercompany elimination, trial balance generation,
and statutory report output.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual period close process this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per close period] |
| MS-02 | ... | ... | ... |

**Minimum required**: five distinct manual steps specific to the period close domain (e.g.,
MS-01: "Controller exports subledger journal entries to Excel and reviews for completeness:
2 hours per monthly close"). Generic steps not grounded in financial close do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

Citation rule: cite incumbent steps by Step ID (MS-NN format). Every recovery entry must
carry an MS-NN citation.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**SubledgerJournalEntry, ConsolidationLedger, CurrencyRevaluationAdjustment,
IntercompanyEliminationEntry, TrialBalance, StatutoryReport.**

State: (a) close cadence (monthly, quarterly, or annual), (b) maximum acceptable close
staleness threshold — the elapsed time from subledger extraction to statutory report
generation before financial reporting deadline risk arises. Fixed at declaration.

---

**SECTION 2 — STAGE TRACE**

For each stage, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: specific field names for every addition, rename, type change, or
  removal; if no change: `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: a concrete named failure mode — "errors may occur" does not qualify

**Stage 1 — Subledger Extraction**: general ledger system => close orchestration service
**Stage 2 — Consolidation Aggregation**: close orchestration service => consolidation engine
**Stage 3 — Currency Revaluation**: consolidation engine => FX revaluation service
**Stage 4 — Intercompany Elimination**: FX revaluation service => elimination engine
**Stage 5 — Trial Balance Generation**: elimination engine => trial balance service
**Stage 6 — Statutory Report Output**: trial balance service => reporting service => regulatory output store

---

**SECTION 3 — BOUNDARY TABLE WITH DECOMPOSED LATENCY**

Produce one row per inter-stage boundary. All seven columns are required — a row with any
blank cell is a structural gap.

| Boundary | Error Handling (mechanism or "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Transport Latency (queue / network traversal) | Processing Overhead (boundary-level validation, routing, buffering) | Total Boundary Latency (sum of Transport + Processing Overhead) | Entity at Risk |
|----------|-------------------------------------------------------------|------------------------------------------------|----------------------------------------------|---------------------------------------------------------------------|----------------------------------------------------------------|----------------|
| B1->2 | | | | | | |
| B2->3 | | | | | | |
| B3->4 | | | | | | |
| B4->5 | | | | | | |
| B5->6 | | | | | | |

**Transport Latency column**: the time for the data payload to traverse the network,
queue, or file transfer between stages. For synchronous API calls with no queue, state
network round-trip time. For queue-based boundaries, state queue head-of-line wait time.

**Processing Overhead column**: the time consumed at the boundary before the downstream
stage begins processing — schema validation, routing decisions, payload buffering,
authentication, or header enrichment. Excludes stage processing time.

**Total Boundary Latency column**: must equal the sum of Transport Latency and Processing
Overhead. The stale analysis in SECTION 4 uses this total as the boundary addend.

**Entity at Risk column**: name a specific entity from SECTION 1 inventory at risk of loss
or corruption if the error handling fails. Generic labels do not qualify.

---

**SECTION 4 — STALE ANALYSIS WITH DECOMPOSED ADDENDS**

Accumulate elapsed time step by step, showing each stage latency and each total boundary
latency as separate addends. Where instructive, show the transport/processing split in
parentheses:

- After Stage 1: [elapsed]
- After B1->2 (transport: X + processing overhead: Y = total Z): [elapsed]
- After Stage 2: [elapsed]
- After B2->3 (transport: X + processing overhead: Y = total Z): [elapsed]
- ...continue through Stage 6...
- **Pipeline total**: [elapsed total]

Compare the pipeline total against the threshold declared in SECTION 1:
1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure, identify which latency component
   explodes): state FRESH or STALE separately; identify whether transport or processing
   overhead is the dominant contributor under the failure mode

Also state the staleness window for downstream consumers reading trial balance data
between Stage 5 (Trial Balance Generation) and Stage 6 (Statutory Report Output).

---

**SECTION 5 — RECOVERY PRESCRIPTIONS**

For every "no handling — risk accepted" annotation in SECTION 3 and every named loss point
in SECTION 2, provide a paired recovery prescription. Each entry must:

1. Open with the specific boundary label (B[N]->[N+1]) or stage loss point name
2. Name the specific recovery mechanism
3. Name the protected entity drawn from SECTION 3 Entity at Risk column or SECTION 1
   inventory
4. Cite the fallback by its Step ID (MS-NN format) from SECTION 0 — every recovery entry
   must carry an MS-NN citation

---

**SECTION 6 — TRADE-OFF ANALYSIS**

Name an alternative period close architecture (e.g., continuous close with daily
subledger sync vs monthly batch extraction, single-instance consolidation engine vs
distributed subsidiary-level consolidation, automated FX revaluation vs month-end manual
treasury adjustment). State at least two trade-off dimensions. At least one must compare
the automated pipeline's total elapsed time from SECTION 4 against the **INCUMBENT TOTAL**
declared in SECTION 0. At least one dimension should identify which boundary's
decomposed latency (transport or processing overhead) is the primary optimization target.

---

Produce all sections in order (Sections 0 through 6). Section 3's Total Boundary Latency
column values must be used as the boundary addends in Section 4 — a Section 4 total that
differs from the sum of Section 2 stage latencies plus Section 3 total boundary latencies
is a structural inconsistency.

---

## V-04 — Cross-Reference Verification Index for C-17/C-18/C-19 Co-Visibility

**Variation axis**: Output format — a post-trace cross-reference verification index table
makes C-17, C-18, C-19, and C-16 simultaneously visible per boundary in a single structure
**Hypothesis**: When C-17, C-18, and C-19 are enforced in separate sections (boundary
table, recovery table, stale analysis), a criterion gap is only visible by cross-
referencing those sections. A post-trace verification index (one row per boundary: Boundary
| Entity at Risk | Boundary Latency | Recovery Row Ref | Step ID Cited) creates a single
surface where all three criteria are co-visible. A blank cell in any column reveals exactly
which criterion is missing for which boundary — without the scorer needing to maintain
multiple section references. Tests whether the verification index catches C-17/C-18/C-19
gaps that are invisible within the local section but visible at the boundary-level aggregate
view. Also tests whether requiring the index prompts LLMs to backfill gaps discovered
during index construction, producing self-correcting behavior.

Scenario: Customer credit limit management pipeline — credit application submission through
credit bureau query, risk scoring, credit limit assignment, ERP credit profile activation,
and order management credit check enforcement. Finance owns risk scoring and credit limit
assignment; Operations owns ERP credit profile activation and order management enforcement;
Commerce owns credit application submission and bureau query orchestration.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
customer credit limit management pipeline — credit application submission through credit
bureau query, risk scoring, credit limit assignment, ERP credit profile activation, and
order management credit check enforcement.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 0 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual credit review process this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per credit application] |
| MS-02 | ... | ... | ... |

**Minimum required**: five distinct manual steps specific to the customer credit domain
(e.g., MS-01: "Credit analyst manually requests Dun & Bradstreet report and reviews
payment history: 45 min per application"). Generic steps not grounded in credit management
do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration.

Citation rule: cite incumbent steps by Step ID (MS-NN format). Every recovery entry must
carry an MS-NN citation.

---

**SECTION 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**CreditApplication, CreditBureauReport, RiskScoreRecord, CreditLimitDecision,
ERPCreditProfile, OrderManagementCreditRule.**

State: (a) business cadence, (b) maximum acceptable credit-activation staleness threshold
— the elapsed time from credit bureau query to order management credit rule enforcement
before a customer being wrongly blocked from placing orders (or wrongly allowed beyond
their approved limit) constitutes a business risk. Fixed at declaration.

---

**SECTION 2 — STAGE TRACE**

For each stage, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: specific field names for every addition, rename, type change, or
  removal; if no change: `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization
- **Loss point**: a concrete named failure mode — "errors may occur" does not qualify

**Stage 1 — Credit Application**: commerce portal => credit application service
**Stage 2 — Bureau Query**: credit application service => credit bureau API gateway
**Stage 3 — Risk Scoring**: credit bureau API gateway => risk scoring engine
**Stage 4 — Credit Limit Assignment**: risk scoring engine => credit decision service
**Stage 5 — ERP Credit Profile**: credit decision service => ERP customer master service
**Stage 6 — Order Management Enforcement**: ERP customer master service => order management credit rules service

---

**SECTION 3 — BOUNDARY TABLE**

Produce one row per inter-stage boundary. All five columns are required — a row with any
blank cell is a structural gap.

| Boundary | Error Handling (mechanism or "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk |
|----------|-------------------------------------------------------------|------------------------------------------------|-----------------|----------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

Entity at Risk column: name a specific entity from SECTION 1 inventory. Generic labels
do not qualify.

---

**SECTION 4 — STALE ANALYSIS**

Accumulate stage and boundary latencies step by step through Stage 6. Compare the final
total against the threshold declared in SECTION 1:
1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE separately

State the staleness window for an order management system enforcing a credit rule that
has not yet propagated from Stage 5 to Stage 6 — name the entity and the business
consequence (erroneous credit block or erroneous credit release).

---

**SECTION 5 — RECOVERY PRESCRIPTIONS**

For every "no handling — risk accepted" annotation in SECTION 3 and every named loss point
in SECTION 2, provide a paired recovery prescription. Each entry must:

1. Open with the specific boundary label (B[N]->[N+1]) or stage loss point name
2. Name the specific recovery mechanism
3. Name the protected entity
4. Cite the fallback by its Step ID (MS-NN format) from SECTION 0 — every recovery entry
   must carry an MS-NN citation

---

**SECTION 6 — CROSS-REFERENCE VERIFICATION INDEX**

After completing all sections above, produce the following verification index. This index
has one row per inter-stage boundary and must be consistent with Sections 2, 3, and 5 —
it is a structured summary, not new content. A blank cell in any column is a structural
gap for the criterion it represents.

| Boundary | Entity at Risk (from Section 3; C-17) | Boundary Latency (from Section 3; C-19) | Recovery Refs (list of Section 5 entry identifiers that address this boundary; C-18) | Step ID(s) Cited (MS-NN from Section 5 entries for this boundary; C-16) |
|----------|--------------------------------------|-----------------------------------------|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

**Entity at Risk column rule**: must match SECTION 3 exactly. Any discrepancy between
this index and the Section 3 boundary table is a structural inconsistency.

**Boundary Latency column rule**: must match SECTION 3 exactly. A blank cell means C-19
is not satisfied for this boundary.

**Recovery Refs column rule**: list every Section 5 entry (by its boundary label or loss
point name) that addresses this boundary — including entries for loss points from the
stage preceding this boundary. A boundary with no recovery refs means either (a) the
boundary had no NH annotation and the preceding stage had no loss point, or (b) a C-18
gap exists.

**Step ID(s) Cited column rule**: list all MS-NN identifiers cited in Section 5 entries
for this boundary. A blank cell here means C-16 is not satisfied for any recovery entry
associated with this boundary.

After the verification index, state for each criterion: **C-17 STATUS** (all rows
populated / N rows missing entity), **C-19 STATUS** (all rows populated / N rows missing
latency), **C-18 STATUS** (all boundaries with NH or loss point have recovery refs /
N gaps), **C-16 STATUS** (all recovery entries carry MS-NN citation / N gaps).

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative credit management architecture (e.g., synchronous real-time bureau
pull vs async bureau pre-fetch and cache, rule-based scoring vs ML-based risk model,
hard credit stop in order management vs soft warning with manual override). State at least
two trade-off dimensions. At least one must compare the automated pipeline's total elapsed
time from SECTION 4 against the **INCUMBENT TOTAL** declared in SECTION 0.

---

Produce all sections in order (Sections 0 through 7). SECTION 6 must be produced after
all other sections are complete — it summarizes and cross-validates. Any blank cell in
SECTION 6 discovered during construction should prompt backfilling in the relevant
earlier section before the index is finalized.

---

## V-05 — Combined: Trigger IDs + Stage-Exit Entity Declaration + Recovery Audit Table + Verification Index

**Variation axis**: Trigger IDs (V-01) + stage-exit entity declaration (V-02) +
recovery audit table with Triggering Condition column (C-18 full structure) +
cross-reference verification index (V-04), all on one pipeline
**Hypothesis**: The three R6 innovations are structurally complementary: Trigger IDs
(NH-NN/LP-NN) make C-18 triggering condition citations machine-verifiable; stage-exit
entity declarations anchor C-17 entity-at-risk selection to a forward-declared set;
the recovery audit table's Triggering Condition column provides the linkage that makes
row-completeness structurally visible; and the cross-reference verification index
makes C-17, C-18, and C-19 co-visible per boundary in a single post-trace sweep.
Tests whether the combination of all three axes produces the highest composite score
for C-17/C-18/C-19 while maintaining essential coverage (C-01 through C-04) — and
whether the structural density at this combination level is navigable and executable
without crowding out lineage prose or schema annotations.

Scenario: Subscription usage-to-revenue pipeline — usage event ingestion through CDR
(call detail record) enrichment, rating and pricing, invoice line generation, revenue
recognition allocation, and GL posting. Finance owns revenue recognition and GL posting;
Operations owns CDR enrichment and rating; Commerce owns usage event ingestion and
invoice line generation.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
subscription usage-to-revenue pipeline — usage event ingestion through CDR enrichment,
rating and pricing, invoice line generation, revenue recognition allocation, and GL
posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**STEP 0 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual usage-to-revenue process this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per billing cycle] |
| MS-02 | ... | ... | ... |

**Minimum required**: five distinct manual steps specific to the usage-to-revenue domain
(e.g., MS-01: "Billing analyst downloads raw usage logs and manually classifies usage
events by product SKU: 3 hours per monthly cycle"). Each Step ID must follow the MS-NN
format exactly. Generic steps not grounded in subscription billing do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed
at declaration; may not be revised.

**Citation rule**: in all downstream steps, cite incumbent steps by Step ID (MS-NN
format). All recovery entries in STEP 8 must carry an MS-NN citation. The recovery audit
table's Step ID Cited column is the enforcement surface for C-16.

This table and its INCUMBENT TOTAL are the sole authority for:
- MS-NN citations required in STEP 8 (Recovery Audit Table)
- Baseline comparison required in STEP 9 (Trade-Off Analysis)

---

**STEP 1 — DOMAIN CONTEXT AND ENTITY INVENTORY**

Enumerate all in-scope domain entities before any stage is traced:
**UsageEvent, CDRRecord, RatedLineItem, InvoiceLineRecord, RevenueAllocation,
GLPostingEntry.**

State: (a) business cadence (real-time ingestion, daily batch rating, monthly invoice
cycle), (b) maximum acceptable revenue-recognition staleness threshold — the elapsed time
from usage event ingestion to GL posting before revenue reporting accuracy risk arises.
Fixed at declaration; revisions not permitted.

---

**STEP 2 — STAGE 1: Usage Event Ingestion**

Usage event collector => CDR pre-processing service.

State all five required items:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: every field added, renamed, retyped, or removed; if no change:
  `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization
- **Loss point LP-01**: [concrete named failure — "errors may occur" does not qualify.
  Declare with LP-01 identifier. Example: `LP-01: Usage event deduplication key collision
  causes duplicate events to be silently dropped at the pre-processor — double-charging
  or under-charging risk for UsageEvent.`]

**Entities exiting Stage 1**: [list every entity from STEP 1 inventory that exits this
stage as the subject of downstream processing. This declaration constrains the B1->2
Entity at Risk selection in STEP 7.]

---

**STEP 3 — STAGE 2: CDR Enrichment**

CDR pre-processing service => CDR enrichment service.

Same five-item format as STEP 2. Declare loss point with LP-02 identifier.

**Entities exiting Stage 2**: [list from STEP 1 inventory. Constrains B2->3 Entity at
Risk selection.]

---

**STEP 4 — STAGE 3: Rating and Pricing**

CDR enrichment service => rating engine.

Same format. Loss point: LP-03.

**Entities exiting Stage 3**: [list. Constrains B3->4.]

---

**STEP 5 — STAGE 4: Invoice Line Generation**

Rating engine => invoicing service.

Same format. Loss point: LP-04.

**Entities exiting Stage 4**: [list. Constrains B4->5.]

---

**STEP 6 — STAGE 5: Revenue Recognition**

Invoicing service => revenue recognition service.

Same format. Loss point: LP-05.

**Entities exiting Stage 5**: [list. Constrains B5->6.]

---

**STEP 6B — STAGE 6: GL Posting**

Revenue recognition service => general ledger service.

Same format. Loss point: LP-06.

[No outbound entity declaration required for the terminal stage.]

---

**STEP 7 — BOUNDARY TABLE WITH TRIGGER ID AND ENTITY CONSTRAINT**

Produce one row per inter-stage boundary. All six columns are required — a row with any
blank cell is a structural gap.

"No handling" annotations must use the NH-NN format; the identifier is fixed at
declaration and referenced in STEP 8.

| Boundary | Error Handling (NH-NN: "no handling — risk accepted" or specific mechanism) | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk (must be drawn from preceding stage's Entities Exiting declaration) |
|----------|----------------------------------------------------------------------------|------------------------------------------------|-----------------|-----------------------------------------------------------------------------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

**NH-NN format rule**: assign a sequential NH number to each "no handling" annotation
(NH-01, NH-02, ...). The identifier is used in STEP 8's Trigger ID column.

**Entity at Risk column rule**: the entity named here must appear in the "Entities
exiting" declaration of the preceding stage (STEP 2–STEP 6B). An entity that was not
in the preceding stage-exit declaration is an inventory violation. Generic labels fail.

**Boundary Latency column rule**: value, range, or characterization distinct from stage
latency. A blank cell fails C-19.

---

**STEP 7B — STALE ANALYSIS**

Accumulate stage and boundary latencies step by step, showing each addend:
- After Stage 1: [elapsed]
- After B1->2: [elapsed]
- After Stage 2: [elapsed]
- After B2->3: [elapsed]
- After Stage 3: [elapsed]
- After B3->4: [elapsed]
- After Stage 4: [elapsed]
- After B4->5: [elapsed]
- After Stage 5: [elapsed]
- After B5->6: [elapsed]
- After Stage 6: [elapsed total]

Compare the final total against the threshold from STEP 1:
1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure, cite its LP-NN or NH-NN
   identifier): state FRESH or STALE separately

State the staleness window for revenue not yet recognized between Stage 5 (Revenue
Recognition) and Stage 6 (GL Posting) — specify the RevenueAllocation entity, the
duration, and the reporting consequence.

---

**STEP 8 — RECOVERY AUDIT TABLE**

Produce one row for every NH-NN annotation from STEP 7 and one row for every LP-NN
loss point from STEPS 2–6B. **All six columns are required — a row with any blank cell
is a structural gap detectable without reading surrounding prose. Every NH-NN and LP-NN
declared must have a corresponding row — a missing row is a structural C-18 gap.**

| Trigger ID (NH-NN or LP-NN) | Triggering Condition (verbatim declaration text from point of declaration) | Recovery Mechanism (specific — generic advice fails) | Named Entity Protected | Step ID Cited (MS-NN from STEP 0) | Manual Step Cited (exact value from STEP 0) |
|----------------------------|---------------------------------------------------------------------------|------------------------------------------------------|------------------------|-----------------------------------|---------------------------------------------|

**Trigger ID column rule**: cite the exact NH-NN or LP-NN identifier assigned at
declaration. A row without a Trigger ID cannot be verified for completeness.

**Triggering Condition column rule**: copy the verbatim NH-NN annotation or LP-NN
loss point description from the step where it was declared. A paraphrase does not qualify.

**Step ID Cited column rule**: cite the MS-NN identifier from STEP 0. A blank cell or
a citation without MS-NN format fails C-16. Every row must carry a citation.

**Manual Step Cited column rule**: cite the exact Manual Step column value from STEP 0,
verbatim. Paraphrase fails.

---

**STEP 8B — CROSS-REFERENCE VERIFICATION INDEX**

After completing STEP 8, produce the following verification index. One row per boundary.
Must be consistent with STEP 7 and STEP 8 — summarizes, does not introduce new content.

| Boundary | Entity at Risk (from STEP 7; C-17) | Boundary Latency (from STEP 7; C-19) | STEP 8 Recovery Rows (list Trigger IDs that reference this boundary; C-18) | MS-NN Citations (Step IDs from STEP 8 rows for this boundary; C-16) |
|----------|------------------------------------|--------------------------------------|----------------------------------------------------------------------------|----------------------------------------------------------------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

After the table, state for each criterion:
- **C-17 STATUS**: all five rows carry a named entity / N rows missing
- **C-19 STATUS**: all five rows carry a boundary latency / N rows missing
- **C-18 STATUS**: all NH-NN and LP-NN associated with each boundary have recovery rows /
  N gaps (name the missing Trigger IDs)
- **C-16 STATUS**: all STEP 8 rows carry MS-NN citations / N gaps

If any status reports a gap, correct it in the relevant upstream step before finalizing
the index.

---

**STEP 9 — TRADE-OFF ANALYSIS**

Name an alternative usage-to-revenue architecture (e.g., real-time streaming rating vs
hourly micro-batch CDR aggregation, pre-paid usage model with event-time billing vs
post-paid with period-end invoice, integrated billing-revenue engine vs separate billing
and ASC 606 revenue recognition service). State at least two trade-off dimensions. At
least one must compare the automated pipeline's total elapsed time from STEP 7B against
the **INCUMBENT TOTAL** declared in STEP 0. At least one dimension should identify the
boundary latency from STEP 7 that is the dominant contributor to the end-to-end total.

---

Work through Steps 0 through 9 in order. Do not skip any step. Every LP-NN and NH-NN
declared must appear as a row in STEP 8 — a missing row is a visible C-18 gap. The
STEP 8B cross-reference index must be produced after STEP 8 is complete; any gap
discovered during index construction must be corrected in the relevant upstream step
before the index is finalized.

---

## Axis Coverage Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Trigger IDs (NH-NN/LP-NN) at declaration | yes | no | no | no | yes |
| Stage-exit entity declaration | no | yes | no | no | yes |
| Boundary latency decomposed (transport + overhead) | no | no | yes | no | no |
| Cross-reference verification index | no | no | no | yes | yes |
| Recovery audit table (C-18 structured) | yes (5-col, Trigger ID + Condition) | no (prose) | no (prose) | no (prose) | yes (6-col, Trigger ID + Condition) |
| Entity at Risk column in boundary table (C-17) | yes | yes (constrained by stage-exit) | yes | yes | yes (constrained by stage-exit) |
| Boundary latency column (C-19) | yes | yes | yes (decomposed) | yes | yes |
| Incumbent baseline table (C-14/C-15) | yes (4-col + MS-NN) | yes (4-col + MS-NN) | yes (4-col + MS-NN) | yes (4-col + MS-NN) | yes (4-col + MS-NN) |
| Step IDs (MS-NN) (C-16) | yes | yes | yes | yes | yes |
| Inline boundary gates | no | no | no | no | no |
| Schema-diff tables | no | no | no | no | no |
| Phrasing register | imperative | imperative | formal/technical | imperative | imperative |
| Verification index self-correction mandate | no | no | no | yes | yes |
| C-17 enforcement mechanism | entity inventory constraint | stage-exit forward declaration | column presence | verification index | stage-exit + verification index |
| C-18 enforcement mechanism | Trigger ID citation completeness | prose (loss point coverage) | prose (loss point coverage) | recovery refs in index | Trigger ID + table + index |
| C-19 enforcement mechanism | boundary latency column | boundary latency column | decomposed sub-columns | verification index | boundary latency column + index |
| C-13 structural surfaces | 1 (recovery table) | 1 (boundary table) | 1 (boundary table, 7-col) | 2 (boundary + verification index) | 3 (boundary + recovery + index) |
| New vs R5 | Trigger IDs | Stage-exit entity | Latency decomposition | Verification index | All three combined |
