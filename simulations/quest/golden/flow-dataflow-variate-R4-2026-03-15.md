# flow-dataflow — Round 4 Variations (Rubric v3)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v3 (C-01 through C-14, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 4 targets the two new aspirational criteria added in v3:

- **C-13 (Structural completeness enforcement)** — tables or inline gates that make
  omissions visible as blank cells or missing gate blocks, not as prose gaps.
- **C-14 (Incumbent baseline anchoring)** — at least one recovery prescription names
  the pre-automation operational process explicitly, grounded in the domain scenario.

R3's top scorers (V-02, V-03 at 96 pts each) both enforce C-13 via different structural
mechanisms: V-02 via blank-cell tables, V-03 via inline gate prohibition. R3's V-04 earns
C-14 by naming INCUMBENT BASELINE as the fallback source. R4 tests three hypotheses:

**H1 — Phrasing register degradation (V-01)**
Conversational/descriptive phrasing ("you'll want to include...") relieves the structural
compliance pressure that imperative phrasing creates. If C-13 requires explicit structural
framing, advisory language should produce lower C-13 scores than identical content stated
imperatively — omissions hide more easily in prose guidance than in mandatory tables.

**H2 — All-section structural enforcement (V-02)**
Extending structural tables to cover all three scorable requirement types simultaneously
(schema diffs for C-04, boundary table for C-02, loss-point table for C-03) maximizes
C-13 coverage. Single-section tables (V-02 R3) target one requirement; this variation
targets all three at once. Predicts highest C-13 score of the round.

**H3 — Structured incumbent baseline table (V-03)**
Presenting the incumbent baseline as a named four-column table (Manual Step / Actor /
Duration / Entity Handled) and requiring subsequent sections to cite rows by their
**Manual Step** value forces C-14 at structural depth — not just "the manual process"
but a specific named step from a declared table. Predicts C-14 pass rate higher than
R3's V-04 baseline because cited-row requirement removes the "named operational process"
ambiguity.

**Axes selected for R4:**

1. **Phrasing register** — conversational/descriptive vs imperative (not explored in R3)
2. **Output format** — all-section structural completeness tables (extends R3 V-02 from
   one section to three)
3. **Inertia framing** — structured incumbent baseline table with per-row citation
   requirement (extends R3 V-04 from prose baseline to enforced table)

V-04 combines phrasing register (imperative) with lifecycle emphasis (inline gates).
V-05 combines all three axes simultaneously.

**New signal candidates for R4:**

1. **Per-row baseline citation** (V-03, V-05) — requiring recovery prescriptions to
   cite the incumbent by its **Manual Step** column value, not by generic baseline
   reference, makes C-14 machine-verifiable: either the cited step name appears verbatim
   or it doesn't.

2. **Advisory-register C-13 probe** (V-01) — if conversational prompts score comparably
   to imperative on C-13, the criterion is phrasing-invariant and the structural mechanism
   (table or gate) is the actual driver. If they score lower, imperative register is itself
   a C-13 amplifier.

3. **All-section table simultaneity** (V-02) — three independent tables targeting C-02,
   C-03, and C-04 test whether gap detection improves proportionally to the number of
   structural surfaces, or whether one table suffices and additional tables produce
   diminishing returns.

---

## V-01 — Phrasing Register: Conversational / Descriptive

**Variation axis**: Phrasing register
**Hypothesis**: A conversational, advisory register ("it's worth capturing...", "try to
include...") relieves the structural compliance pressure that imperative phrasing creates.
Tests whether C-13 structural enforcement is phrasing-dependent: if omissions can hide in
advisory prose but not in mandatory tables, the phrasing contrast isolates the mechanism.
Essential coverage (C-01 through C-04) should be unaffected because the advisory text
still describes what is needed; C-13 should score lower because no structural surface
enforces the presence of required content.

Scenario: Retail markdown pipeline — from a markdown decision through price engine
processing, POS and ecommerce price synchronization, inventory cost adjustment, and
margin impact reporting. Commerce domain owns the markdown decision; Operations manages
the sync stages; Finance owns margin reporting.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
retail markdown pipeline — markdown decision through price engine processing, POS and
ecommerce price sync, inventory cost adjustment, and margin impact reporting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**Getting Started — Domain Context**

Before diving into the stages, it's worth establishing the world you're operating in.
Think about what a MarkdownDecision actually looks like as a data record — what fields
would it carry? How does it become a PriceAdjustment? Where does an EcommercePriceListing
come from, and how does it relate to a POSPriceListing?

Try to name your entity vocabulary upfront — something like: MarkdownDecision,
PriceAdjustment, POSPriceListing, EcommercePriceListing, InventoryCostRecord, MarginReport.
Add any entities the pipeline actually needs. It's also useful to note the business
cadence (is this batch-nightly? near-real-time?) and to anchor on a staleness threshold —
how long can POS prices diverge from the markdown decision before it becomes a pricing
risk? Whatever you set here, try to carry it through the stale analysis later.

---

**Tracing the Markdown Pipeline**

For each stage, it helps to include:

- **What comes in**: the schema at stage entry — key fields, types, cardinality
- **What changes**: any fields added, renamed, retyped, or dropped; specific field names
  make this useful — "data flows through" doesn't tell the reader much
- **What comes out**: schema at stage exit; if nothing changed, note that explicitly
- **How long it takes**: even a rough characterization helps (real-time, micro-batch,
  daily batch)
- **What could go wrong**: try to name a concrete failure mode — the kind that would
  appear in an incident report

Work through the stages in order. Feel free to organize your response as prose or as a
structured list, whichever makes the lineage clearest.

**Stage 1 — Markdown Approval**: merchandising system → markdown engine
**Stage 2 — Price Calculation**: markdown engine → price adjustment service
**Stage 3 — POS Sync**: price adjustment service → POS price update service
**Stage 4 — Ecommerce Sync**: POS price update service → ecommerce price service
**Stage 5 — Margin Capture**: ecommerce price service → margin analytics service

---

**Boundaries Between Stages**

When data moves from one stage to the next, it's worth thinking about what happens at
that handoff. For each transition, try to capture:

- How errors are handled — if there's a retry mechanism, dead-letter queue, or idempotency
  key in play, name it; if there's genuinely no handling, say so
- Whether the schema changes at this boundary
- How much latency the handoff adds

Cover the transitions between adjacent stages (Stage 1→2, 2→3, 3→4, 4→5). Using
boundary labels like B1->2, B2->3 makes it easier to reference them later.

---

**Staleness Check**

Once you've traced all stages and boundaries, it helps to add up the latencies into an
end-to-end elapsed time. Two scenarios are worth addressing separately: normal operation
and a specific failure mode — name the failure rather than describing it generically.
Compare both against the staleness threshold from your domain context.

---

**Recovery Suggestions**

For any handoffs with no error handling, and for any loss points named in the stage
trace, try to pair each one with a specific recovery idea. The more grounded the better —
if the pipeline was automated from a prior manual process, it's worth noting what a
merchandising or finance associate would have done before the pipeline existed. That
named manual process is often the natural fallback for the failure mode it replaced.

---

**Alternative Patterns**

Finally, consider whether this pipeline's design is the best fit. Name an alternative
(for example, event-driven CDC vs batch price updates, or a unified price master vs
separate POS and ecommerce feeds). Try to give at least two trade-off dimensions, and
ground at least one in markdown-domain terms — something like "a unified feed eliminates
the divergence window between POS and ecommerce prices during peak markdown hours."

---

Work through all topics in the order shown. There's no strict formatting requirement;
organize your response in whatever structure makes the lineage and analysis clearest.

---

## V-02 — Output Format: All-Section Structural Completeness Tables

**Variation axis**: Output format
**Hypothesis**: Extending structural completeness tables to all three scorable requirement
types simultaneously (schema diffs for C-04, boundary table for C-02, loss-point table
for C-03) maximizes C-13 coverage. R3's V-02 enforced structural completeness for schema
diffs and boundaries; this variation adds an explicit loss-point table, making all three
mandatory requirement types structurally verified. Predicts the highest C-13 score of the
round and strong essential coverage because no requirement type remains in prose-only form.

Scenario: Employee expense reimbursement pipeline — from expense submission through
approval routing, accounting classification, payment batch creation, bank transfer
execution, and GL posting. Finance domain owns classification and GL posting; Operations
manages the approval routing and batch scheduling.

---

You are a Finance / Operations / Commerce data domain expert tracing data through an
employee expense reimbursement pipeline — expense submission through approval routing,
accounting classification, payment batch creation, bank transfer execution, and GL posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**DOMAIN CONTEXT**

Declare the entity vocabulary: ExpenseReport, ExpenseLine, ApprovalDecision,
AccountingEntry, PaymentBatch, BankTransfer, GLPosting. State the business cadence
(daily batch / weekly / on-demand). State the maximum acceptable reimbursement-posting
staleness threshold — the maximum elapsed time from submission to GL posting that
triggers a compliance risk. This threshold is the sole authority for STALE ANALYSIS;
it is fixed at declaration and may not be revised.

---

**STAGE TRACE TABLE**

Produce one row per stage. **All seven columns are required — a row with any blank cell
is a structural gap detectable without reading the surrounding text.**

| Stage | Source => Destination | Input Schema (key fields : types) | Transformations (field names, change type) | Output Schema (key fields : types) | Latency | Loss Point (named failure mode) |
|-------|-----------------------|-----------------------------------|--------------------------------------------|------------------------------------|---------|---------------------------------|
| Stage 1 — Expense Submission | employee portal => expense mgmt service | | | | | |
| Stage 2 — Approval Routing | expense mgmt service => approval engine | | | | | |
| Stage 3 — Accounting Classification | approval engine => GL classification service | | | | | |
| Stage 4 — Payment Batch | GL classification service => payment batch service | | | | | |
| Stage 5 — Bank Transfer | payment batch service => banking API | | | | | |
| Stage 6 — GL Posting | banking API => GL system | | | | | |

**Transformations column rule**: if a stage makes no schema change, write exactly:
`verified: no field added, removed, renamed, or retyped`. A blank cell or bare
"unchanged" without this verification claim fails.

**Loss Point column rule**: name the failure mode as it would appear in an incident
report — "errors may occur" or "data loss possible" do not qualify.

---

**BOUNDARY TABLE**

Produce one row per inter-stage boundary. **All five columns are required — a row with
any blank cell is a structural gap.**

| Boundary | Error Handling (mechanism or "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk |
|----------|------------------------------------------------------------|------------------------------------------------|-----------------|----------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

**Entity at Risk column rule**: name a specific entity from DOMAIN CONTEXT. "Data" or
"records" do not qualify.

---

**LOSS-POINT RECOVERY TABLE**

Produce one row for every "no handling — risk accepted" entry in BOUNDARY TABLE and one
row for every named Loss Point in STAGE TRACE TABLE. **All four columns are required —
a row with any blank cell is a structural gap.**

| Entry Source | Location (boundary label or stage name) | Recovery Mechanism (specific — generic advice fails) | Named Entity Protected |
|-------------|----------------------------------------|-----------------------------------------------------|------------------------|

**Named Entity Protected column rule**: cite a specific entity from DOMAIN CONTEXT.
Generic entity references ("data", "records") do not qualify.

---

**INCUMBENT BASELINE**

Describe the manual expense reimbursement process this pipeline replaces. Name at least
three manual steps with the actor and a duration estimate per step (e.g., "Finance
coordinator opens shared expense inbox and batch-reviews receipts: 30 min per weekly
run"). Compute a total manual cycle time. At least one entry in LOSS-POINT RECOVERY TABLE
must reference a named step from this section as the identified fallback process.

---

**STALE ANALYSIS**

Sum the Latency column from STAGE TRACE TABLE and the Boundary Latency column from
BOUNDARY TABLE into an end-to-end elapsed total. Show the additive accumulation:
Stage 1 + B1->2 + Stage 2 + B2->3 + ... + Stage 6. State FRESH or STALE under:

1. **Normal operation**: compare total against threshold from DOMAIN CONTEXT; state verdict
2. **Worst-case failure** (name the specific failure from STAGE TRACE TABLE Loss Point
   column): compare total against threshold; state verdict separately

---

**TRADE-OFF ANALYSIS**

Name an alternative reimbursement pipeline pattern (e.g., real-time continuous expense
posting vs weekly payment run, automated GL classification vs manual account coding,
direct bank API integration vs payment processor intermediary). State at least two
trade-off dimensions. At least one must compare the automated pipeline's total elapsed
time against the total manual cycle time declared in INCUMBENT BASELINE.

---

Produce all sections in the order shown. Every table must be fully populated — structural
gaps are detectable from blank cells without reading surrounding prose.

---

## V-03 — Inertia Framing: Structured Incumbent Baseline Table

**Variation axis**: Inertia framing
**Hypothesis**: Presenting the incumbent manual process as a named four-column table
(Manual Step / Actor / Duration / Entity Handled) and requiring subsequent recovery
prescriptions to cite specific rows by their **Manual Step** value enforces C-14 at
structural depth. R3's V-04 named the baseline as a prose section; this variation makes
the baseline itself structurally enforced — a recovery prescription that says "manual
review" without citing a row name fails. Predicts higher C-14 pass rates than R3's V-04
because the citation requirement is verifiable without interpreting prose.

Scenario: Product availability sync pipeline — from ERP inventory records through CDX
availability publication, storefront display update, order acceptance, and fulfillment
commitment. Operations owns the ERP-to-CDX stages; Commerce owns storefront and order
stages; Finance owns revenue commitment.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
product availability sync pipeline — from ERP inventory records through CDX availability
publication, storefront display update, order acceptance, and fulfillment commitment.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 1 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual availability process this
pipeline replaces. Present it as the following named table:

| Manual Step | Actor | Duration | Entity Handled |
|-------------|-------|----------|----------------|
| [step name] | [role / team] | [time per unit or cycle] | [domain entity] |

**Minimum required**: four distinct manual steps. Steps must be specific to the product
availability domain (e.g., "Warehouse associate manually counts shelf stock: 15 min
per SKU bin per shift"), not generic workflow steps.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values assuming sequential execution.
This token is fixed at declaration and may not be revised.

This table and its INCUMBENT TOTAL are the sole authority for:
- The named fallback process required in SECTION 6 (Recovery Prescriptions)
- The baseline comparison required in SECTION 7 (Trade-Off Analysis)

Do not paraphrase or re-derive these values in later sections. Cite by **Manual Step**
column value or by the `INCUMBENT TOTAL` token.

---

**SECTION 2 — DOMAIN CONTEXT**

Declare the entity vocabulary: InventoryRecord, CDXPayload, StorefrontListing,
OrderAcceptance, FulfillmentCommit, RevenueEntry. State the business cadence. State the
maximum acceptable availability-staleness threshold — how long can the storefront display
availability for an out-of-stock item before it becomes a customer-experience or revenue
risk? This threshold is fixed at declaration; revisions are not permitted.

---

**SECTION 3 — STAGE TRACE**

For each stage, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: specific field names for every addition, rename, type change, or
  removal; if no change, state: `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: a concrete named failure mode — "errors may occur" does not qualify

**Stage 1 — Inventory Update**: ERP system => inventory service
**Stage 2 — CDX Publication**: inventory service => CDX gateway
**Stage 3 — Storefront Sync**: CDX gateway => storefront display service
**Stage 4 — Order Acceptance**: storefront display service => order management system
**Stage 5 — Fulfillment Commit**: order management system => fulfillment service

---

**SECTION 4 — BOUNDARY CHECKS**

For each inter-stage boundary, provide:
- **Error handling**: the specific mechanism (idempotency key, retry queue, dead-letter
  queue, compensating write) — or state exactly: `no handling — risk accepted`
- **Schema transition**: whether schema changes; if unchanged, state: `verified unchanged`
- **Boundary latency**: processing overhead at this crossing

Label all boundaries: **B1->2**, **B2->3**, **B3->4**, **B4->5**.

---

**SECTION 5 — STALE ANALYSIS**

Accumulate stage latencies and boundary latencies into an end-to-end elapsed total.
Show the running accumulation (Stage 1 + B1->2 + Stage 2 + ... + Stage 5). Compare
the final total against the threshold from SECTION 2 under:

1. **Normal operation**: state FRESH or STALE and the total elapsed
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE

Address both scenarios separately. Do not blend them.

---

**SECTION 6 — RECOVERY PRESCRIPTIONS**

For every `no handling — risk accepted` annotation in SECTION 4 and every named loss
point in SECTION 3, provide a paired recovery prescription. Each prescription must:

1. Name the specific recovery mechanism (retry with backoff, idempotency key, manual
   requeue, compensating write — generic advice does not qualify)
2. **For at least one critical failure mode**, cite the fallback by its **Manual Step**
   column value from the SECTION 1 INCUMBENT BASELINE TABLE — generic terms such as
   "manual review" or "human intervention" without naming a specific table row do not
   qualify for C-14

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative availability-sync pattern (e.g., event-driven CDC vs polling batch
sync, real-time CDX push vs scheduled pull, unified commerce inventory vs siloed channel
stock). State at least two trade-off dimensions. At least one must compare the automated
pipeline's end-to-end latency from SECTION 5 against the **INCUMBENT TOTAL** declared
in SECTION 1.

---

Produce all sections in the order shown (Sections 1 through 7). SECTION 1 must appear
before any stage or boundary content — a Section 3 stage written before Section 1 is a
protocol violation.

---

## V-04 — Combined: Imperative Register + Inline Boundary Gates

**Variation axis**: Phrasing register (imperative) + Lifecycle emphasis (inline gates)
**Hypothesis**: Combining hard imperative phrasing ("You must...", "Silence fails.",
"You may not proceed until...") with inline boundary gate protocol creates dual compliance
pressure: imperative register closes prose escape hatches where advisory language permits
vague adherence, while inline gates make boundary omissions a structural violation rather
than a prose gap. Predicts stronger C-02 and C-13 scores than V-01 (advisory, no gates),
and tests whether imperative phrasing alone (without tables) is sufficient for C-13 via
the gate mechanism.

Scenario: Trade promotion accrual pipeline — from trade promotion approval through
accrual posting, claim filing, deduction processing, and vendor credit settlement.
Finance owns accrual posting and GL settlement; Operations owns claim filing and
deduction processing; Commerce owns the promotion approval and vendor relationship.

---

You are a Finance / Operations / Commerce data domain expert. You must trace data through
a trade promotion accrual pipeline — from promotion approval through accrual posting,
claim filing, deduction processing, and vendor credit settlement.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

**You must work through every section in the stated order. You may not skip a section.
Silence on any required item within a section is a protocol failure.**

---

**INCUMBENT BASELINE**

You must describe the manual trade promotion reconciliation process this pipeline
replaces. Name at least three manual steps. For each step, you must state the actor
and a duration estimate. Compute a total manual cycle time and state it explicitly as
**INCUMBENT TOTAL**. This total is fixed; you may not revise it once declared.

At least one recovery prescription in RECOVERY PRESCRIPTIONS must name a specific step
from this section as the identified fallback process. Generic phrases such as "manual
review" or "human intervention" without citing a named step from this section do not
satisfy the requirement.

---

**DOMAIN CONTEXT**

You must declare: entity vocabulary (TradePromotion, AccrualEntry, PromoClaim,
DeductionRecord, VendorCredit, SettlementPosting); business cadence; maximum acceptable
accrual-posting staleness threshold. This threshold is fixed at declaration. You may not
revise it after this section.

---

**STAGE TRACE WITH INLINE BOUNDARY GATES**

For each stage, you must state all five items. Omitting any item is a protocol failure:

1. **Input schema**: key fields, types, cardinality at entry — specific field names
   required; categories alone do not qualify
2. **Transformations**: every field added, renamed, retyped, or removed — "same as input"
   fails; if no change, you must state exactly: `verified: no field added, removed,
   renamed, or retyped`
3. **Output schema**: key fields, types, cardinality at exit
4. **Latency**: a value, range, or characterization — silence fails
5. **Loss point**: a concrete named failure mode — "errors may occur" fails; name the
   failure as it would appear in an incident report

---

**Stage 1 — Promotion Approval**: trade management system => accrual engine

[State all five items for Stage 1.]

**BOUNDARY GATE B1->2** — You must complete this gate before writing Stage 2. The gate
must contain all three items; a gate with any item missing is a protocol failure:

- (a) **Error handling**: name the specific mechanism (retry, dead-letter queue,
  idempotency key, compensating transaction) — or state exactly:
  `no handling — risk accepted [B1->2]`
- (b) **Boundary latency**: state the processing overhead as an additive increment
- (c) **Schema continuity**: state whether schema changes; if not, state:
  `verified unchanged at B1->2`

**Stage 2 does not open until BOUNDARY GATE B1->2 is fully stated.**

---

**Stage 2 — Accrual Posting**: accrual engine => accrual ledger

[State all five items for Stage 2.]

**BOUNDARY GATE B2->3** — Complete before opening Stage 3. Same three items as B1->2.
Use label B2->3 in every annotation.

**Stage 3 does not open until BOUNDARY GATE B2->3 is fully stated.**

---

**Stage 3 — Claim Filing**: accrual ledger => claim management service

[State all five items for Stage 3.]

**BOUNDARY GATE B3->4** — Complete before opening Stage 4. Same three items. Use label
B3->4.

**Stage 4 does not open until BOUNDARY GATE B3->4 is fully stated.**

---

**Stage 4 — Deduction Processing**: claim management service => accounts payable system

[State all five items for Stage 4.]

**BOUNDARY GATE B4->5** — Complete before opening Stage 5. Same three items. Use label
B4->5.

**Stage 5 does not open until BOUNDARY GATE B4->5 is fully stated.**

---

**Stage 5 — Vendor Credit Settlement**: accounts payable system => GL settlement service

[State all five items for Stage 5. This is the terminal stage; no outbound gate is
required.]

---

**STALE ANALYSIS**

You must accumulate all stage latencies and boundary latencies step by step. Showing
each addend is required — a final total with no breakdown fails. You must address exactly
two scenarios and state each verdict using exactly the token FRESH or STALE:

1. **Normal operation**: accumulated total vs threshold from DOMAIN CONTEXT — state
   verdict
2. **Worst-case failure** (you must name the specific failure): same comparison — state
   verdict separately

A stale analysis that addresses only one scenario or blends both into a single paragraph
fails.

---

**RECOVERY PRESCRIPTIONS**

For every `no handling — risk accepted [B[N]->[N+1]]` gate annotation and every named
loss point in STAGE TRACE, you must provide a paired recovery prescription. Each entry
must:

- Name the specific recovery mechanism (retry policy, compensating transaction, dead-
  letter queue with manual replay — generic advice fails)
- For at least one critical failure mode, name a specific step from INCUMBENT BASELINE
  as the identified fallback process; this step name must appear verbatim as it does in
  that section

---

**TRADE-OFF ANALYSIS**

You must name an alternative trade promotion settlement pattern (e.g., vendor-managed
accrual vs buyer-side calculation, event-triggered claim vs periodic sweep, real-time
deduction matching vs end-of-month reconciliation). You must state at least two trade-off
dimensions. At least one must compare the automated pipeline's total elapsed time against
the **INCUMBENT TOTAL** declared in INCUMBENT BASELINE.

---

Produce all sections in the stated order. You may not reorder or consolidate sections.
Every required item within each section must be present.

---

## V-05 — Combined: Incumbent Baseline Table + Schema-Diff Tables + Inline Gates

**Variation axis**: Inertia framing + Output format + Lifecycle emphasis (all three axes)
**Hypothesis**: Three independent structural enforcement mechanisms operating
simultaneously produce the highest combined C-13 and C-14 scores: the incumbent baseline
table (per-row citation requirement enforces C-14), schema-diff tables (blank cell = C-04
gap, enforces C-13 for schema), and inline boundary gates (missing gate = C-02 violation,
enforces C-13 for boundaries). The co-presence test: does triple scaffolding produce a
coherent, readable prompt, or does structural density obscure essential coverage?

Scenario: Payroll processing pipeline — from time and attendance capture through payroll
calculation, tax withholding, net pay disbursement, and cost center GL allocation.
Finance owns payroll calculation, tax withholding, and GL allocation; Operations owns
time capture and payment disbursement scheduling.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
payroll processing pipeline — from time and attendance capture through payroll
calculation, tax withholding, net pay disbursement, and cost center GL allocation.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**STEP 0 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual payroll process this pipeline
replaces. Present it as the following named table:

| Manual Step | Actor | Duration | Entity Handled |
|-------------|-------|----------|----------------|
| [step name] | [role / team] | [time per unit or cycle] | [domain entity] |

**Minimum required**: four distinct manual steps specific to the payroll domain (e.g.,
"Payroll administrator collects paper timesheets and enters hours into spreadsheet:
45 min per department per period"). Generic workflow steps not grounded in the payroll
domain do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution).
This token is fixed at declaration. You may not revise it.

This table and its INCUMBENT TOTAL are the sole authority for:
- Named fallback citations required in STEP 8 (Recovery Prescriptions)
- The baseline comparison required in STEP 9 (Trade-Off Analysis)

Cite by **Manual Step** column value or by the `INCUMBENT TOTAL` token. Do not
paraphrase or re-derive these values.

---

**STEP 1 — DOMAIN CONTEXT**

Declare the entity vocabulary: TimesheetRecord, PayrollRun, TaxWithholding,
NetPayInstruction, CostCenterAllocation, GLEntry. State the business cadence. State the
maximum acceptable payroll-posting staleness threshold — the maximum elapsed time from
time-entry cutoff to GL posting before compliance risk arises (e.g., a regulatory
reporting deadline or an employee SLA). This threshold is fixed at declaration; you may
not revise it.

---

**STEP 2 — STAGE 1: Time Capture**

Time and attendance system => payroll calculation engine.

Produce a **schema-diff table** followed by the latency and loss-point entries.
**The schema-diff table must be fully populated — a blank Transformations cell is a
structural gap visible without reading the stage prose.**

Schema-diff table format:

| Field | Entry Schema (type : cardinality) | Transformations | Exit Schema (type : cardinality) |
|-------|------------------------------------|-----------------|----------------------------------|
| [field name] | [type : cardinality at entry] | [change description or `verified: no change`] | [type : cardinality at exit] |

**Transformations cell rule**: if no change for a field, write exactly:
`verified: no field added, removed, renamed, or retyped`. A blank cell or bare
"unchanged" fails.

After the table:
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly /
  daily)
- **Loss point**: concrete named failure — "errors may occur" fails

**BOUNDARY GATE B1->2** — Complete before opening Stage 2. All three items required;
a gate with any item missing is a structural gap:

- (a) **Error handling**: name the mechanism — or state exactly:
  `no handling — risk accepted [B1->2]`
- (b) **Boundary latency**: additive contribution to elapsed total
- (c) **Schema continuity**: if unchanged, state: `verified unchanged at B1->2`

**Stage 2 does not open until BOUNDARY GATE B1->2 is fully stated.**

---

**STEP 3 — STAGE 2: Payroll Calculation**

Payroll calculation engine => payroll register service.

Same format as Step 2: schema-diff table (fully populated, Transformations cell rule
applies), then latency and loss point.

**BOUNDARY GATE B2->3** — Same three items as B1->2. Use label B2->3 in every
annotation.

**Stage 3 does not open until BOUNDARY GATE B2->3 is fully stated.**

---

**STEP 4 — STAGE 3: Tax Withholding**

Payroll register service => tax withholding service.

Same format.

**BOUNDARY GATE B3->4** — Same three items. Use label B3->4.

**Stage 4 does not open until BOUNDARY GATE B3->4 is fully stated.**

---

**STEP 5 — STAGE 4: Payment Disbursement**

Tax withholding service => payment disbursement service.

Same format.

**BOUNDARY GATE B4->5** — Same three items. Use label B4->5.

**Stage 5 does not open until BOUNDARY GATE B4->5 is fully stated.**

---

**STEP 6 — STAGE 5: Cost Center GL Allocation**

Payment disbursement service => HR finance service => GL system.

Same format (schema-diff table + latency + loss point). This is the terminal stage;
no outbound boundary gate is required.

---

**STEP 7 — STALE ANALYSIS**

Accumulate elapsed time step by step, showing each addend:

- After Stage 1: [elapsed]
- After B1->2: [elapsed]
- After Stage 2: [elapsed]
- After B2->3: [elapsed]
- After Stage 3: [elapsed]
- After B3->4: [elapsed]
- After Stage 4: [elapsed]
- After B4->5: [elapsed]
- After Stage 5: [elapsed total]

Compare the final total against the threshold from STEP 1:

1. **Normal operation**: state exactly FRESH or STALE
2. **Worst-case failure** (name the specific failure): state exactly FRESH or STALE

---

**STEP 8 — RECOVERY PRESCRIPTIONS**

For every `no handling — risk accepted [B[N]->[N+1]]` gate annotation and every named
loss point in the stage trace steps, produce a paired prescription. Each entry must:

1. Open with the specific boundary label or stage name (e.g., `B2->3:` or
   `Stage 3 loss point:`)
2. Name the specific recovery mechanism (retry with backoff, dead-letter queue with
   manual replay, compensating transaction, idempotency key — generic advice fails)
3. For at least one critical failure mode, cite the fallback by its **Manual Step**
   column value from the STEP 0 INCUMBENT BASELINE TABLE — generic terms such as
   "manual review" or "human intervention" without naming a specific table row do not
   qualify

---

**STEP 9 — TRADE-OFF ANALYSIS**

Name an alternative payroll architecture (e.g., continuous real-time payroll accrual vs
end-of-period batch run, off-cycle payment processing vs main-cycle inclusion, direct GL
integration vs payroll journal import). State at least two trade-off dimensions. At least
one must compare the automated pipeline's total elapsed time from STEP 7 against the
**INCUMBENT TOTAL** declared in STEP 0.

---

Work through Steps 0 through 9 in order. Do not skip any step or gate.

---

## Axis Coverage Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Phrasing register | conversational | imperative | imperative | imperative | imperative |
| Output format: schema tables | none | yes (STAGE TRACE TABLE) | none | none | yes (per-stage) |
| Output format: boundary table | none | yes (BOUNDARY TABLE) | none | none | no (gates) |
| Output format: loss-point table | none | yes (RECOVERY TABLE) | none | none | no (inline) |
| Inline boundary gates | none | none | none | yes | yes |
| Structured incumbent table | none | no (prose) | yes (4-col table) | no (prose) | yes (4-col table) |
| Per-row baseline citation | none | no | yes | no | yes |
| C-13 structural surfaces | 0 | 3 (all tables) | 0 | 1 (gate) | 2 (table + gate) |
| C-14 depth | low | medium | high | medium | high |
