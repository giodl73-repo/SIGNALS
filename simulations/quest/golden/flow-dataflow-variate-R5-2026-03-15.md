# flow-dataflow — Round 5 Variations (Rubric v4)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v4 (C-01 through C-16, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

Round 5 targets the two new aspirational criteria added in v4:

- **C-15 (Structured incumbent baseline table)** — the pre-automation baseline must be a
  table with at minimum three columns: step identifier/name, responsible actor/role, and
  elapsed time/frequency. Prose paragraphs and bullet lists do not qualify. Each row must
  carry a name or identifier that downstream recovery citations can reference individually.

- **C-16 (Full recovery-to-baseline traceability)** — every recovery prescription (not just
  "at least one") must cite a specific named step or row from the incumbent baseline table.
  Prescriptions that cite only the process category ("manual reconciliation") without a
  step-level identifier do not qualify.

R4's top performers (V-03, V-05) both introduced 4-col incumbent baseline tables with per-row
citation requirements. C-15 and C-16 crystallize these patterns as formal criteria. R5 tests
three hypotheses about the depth and enforcement surface of these new criteria:

**H1 — Minimal 3-column baseline (V-01)**
C-15 requires three columns minimum. A table with exactly the minimum (Manual Step, Actor,
Elapsed Time) satisfies C-15 at the floor while removing the Entity Handled column present in
R4's V-03/V-05. Tests whether the absence of an entity anchor column degrades C-16 citation
specificity: without a row-level entity, step names must carry more disambiguation weight.
Predicts C-15 pass (table form satisfied) but potentially weaker C-16 citation precision than
the 4-column form.

**H2 — Recovery audit table with mandatory "Baseline Step Cited" column (V-02)**
If recovery prescriptions are organized as a table where one column is "Baseline Step Cited,"
every missing C-16 citation is a blank cell — making full traceability structurally enforced
rather than relying on prose discipline. R4 V-03/V-05 enforced citations at the baseline table
level (per-row citation in recovery prose); this variation enforces them at the recovery table
level. Tests whether the enforcement surface (baseline vs recovery) produces different C-16
citation completion rates.

**H3 — Step ID numbering for machine-verifiable citation (V-03)**
Assigning explicit numbered IDs (MS-01 through MS-N) to each manual step creates a citation
target verifiable by substring: a recovery prescription either contains "MS-03" or it does not.
R4's V-03/V-05 used step names as citation targets — names can be paraphrased; IDs cannot.
Predicts higher C-16 precision and verifiability than name-based citation.

V-04 combines imperative register with a positional citation mandate: each recovery entry must
open with "Fallback: [Step ID] — [step name]" before the mechanism description. Tests whether
positional enforcement (first token of each entry is the baseline step citation) achieves C-16
compliance without requiring a separate recovery table structure.

V-05 combines all three new axes: step IDs (V-03) + recovery audit table with a Baseline Step
Cited column (V-02) + per-entry citation mandate (V-04) + per-stage schema-diff tables from
R4 V-02. Tests whether quadruple structural enforcement produces the highest combined C-15 and
C-16 scores, and whether structural density at this level crowds out essential coverage.

**Axes selected for R5:**

1. **Baseline table column structure** — 3-col minimal (floor of C-15) vs 4-col extended
2. **Recovery citation enforcement surface** — recovery audit table as the citation surface
   (new; R4 used recovery prose)
3. **Step ID precision** — numbered MS-NN IDs as citation targets vs named step titles

V-04 combines phrasing register (hard imperative) with positional citation mandate.
V-05 combines step IDs + recovery audit table + per-entry mandate + schema-diff tables.

**New signal candidates for R5:**

1. **Recovery audit table** (V-02, V-05) — a mandatory "Baseline Step Cited" column in the
   recovery prescriptions table makes every missing C-16 citation a blank cell. Tests whether
   enforcement at the recovery surface produces higher compliance than enforcement at the
   baseline surface.

2. **Step ID citation** (V-03, V-04, V-05) — numbered IDs (MS-01, MS-02) vs named steps. If
   LLM outputs cite "MS-03" verbatim, C-16 is unambiguously satisfied; if they cite a
   paraphrase of the step name, C-16 scoring requires interpretation. The ID format removes
   the interpretation dependency.

3. **Per-entry opening citation** (V-04, V-05) — requiring "Fallback: [Step ID]" as the
   first structural element of each recovery entry makes C-16 position-verifiable. Tests
   whether positional mandate is as effective as structural table enforcement.

---

## V-01 — Baseline Table Column Structure: 3-Column Minimal

**Variation axis**: Incumbent baseline table format (minimal C-15 floor — 3 columns)
**Hypothesis**: A 3-column incumbent baseline table (Manual Step | Actor | Elapsed Time)
satisfies C-15 at its stated minimum while removing the Entity Handled column present in R4's
V-03/V-05. Tests whether the absence of an entity anchor column reduces citation specificity
for C-16: without a row-level entity, step names must carry full disambiguation weight.
Predicts C-15 pass (table form is present) but weaker C-16 citation anchoring than the
4-column form. Essential coverage (C-01 through C-04) should be unaffected.

Scenario: Vendor master data onboarding pipeline — new vendor creation request through legal
entity validation, tax identity verification, banking detail verification, payment terms
classification, and ERP master record activation. Finance owns tax verification and payment
terms; Operations owns banking verification and ERP activation; Commerce owns vendor
relationship intake and contract setup.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a vendor
master data onboarding pipeline — new vendor creation request through legal entity validation,
tax identity verification, banking detail verification, payment terms classification, and ERP
master record activation.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 1 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual vendor onboarding process this
pipeline replaces. Present it as the following three-column table:

| Manual Step | Actor | Elapsed Time |
|-------------|-------|--------------|
| [step name] | [role / team] | [time per vendor or per batch] |

**Minimum required**: five distinct manual steps specific to the vendor onboarding domain
(e.g., "AP coordinator collects and photocopies vendor tax forms: 20 min per vendor").
Generic workflow steps not grounded in vendor onboarding do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Elapsed Time values (sequential execution). This
token is fixed at declaration and may not be revised.

This table and its INCUMBENT TOTAL are the sole authority for:
- Named fallback citations required in SECTION 6 (Recovery Prescriptions)
- The baseline comparison required in SECTION 7 (Trade-Off Analysis)

Cite by the **Manual Step** column value or by the `INCUMBENT TOTAL` token. Do not paraphrase
or re-derive these values.

---

**SECTION 2 — DOMAIN CONTEXT**

Declare the entity vocabulary: VendorRequest, LegalEntityRecord, TaxIdentityRecord,
BankingDetailRecord, PaymentTermsProfile, VendorMasterRecord. State the business cadence.
State the maximum acceptable vendor-activation staleness threshold — the elapsed time from a
verified vendor request to ERP master record activation before a procurement risk arises
(e.g., a blocked PO or a missed invoice cycle). This threshold is fixed at declaration;
revisions are not permitted.

---

**SECTION 3 — STAGE TRACE**

For each stage, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: specific field names for every addition, rename, type change, or
  removal; if no change, state: `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: a concrete named failure mode — "errors may occur" does not qualify

**Stage 1 — Vendor Request Intake**: vendor portal => vendor onboarding service
**Stage 2 — Legal Entity Validation**: vendor onboarding service => legal entity verification service
**Stage 3 — Tax Identity Verification**: legal entity verification service => tax identity service
**Stage 4 — Banking Detail Verification**: tax identity service => banking verification service
**Stage 5 — Payment Terms Classification**: banking verification service => payment terms engine
**Stage 6 — ERP Master Activation**: payment terms engine => ERP master data service

---

**SECTION 4 — BOUNDARY CHECKS**

For each inter-stage boundary, provide:
- **Error handling**: the specific mechanism (idempotency key, retry queue, dead-letter queue,
  compensating write) — or state exactly: `no handling — risk accepted`
- **Schema transition**: whether schema changes; if unchanged, state: `verified unchanged`
- **Boundary latency**: processing overhead at this crossing

Label all boundaries: **B1->2**, **B2->3**, **B3->4**, **B4->5**, **B5->6**.

---

**SECTION 5 — STALE ANALYSIS**

Accumulate stage latencies and boundary latencies into an end-to-end elapsed total. Show the
running accumulation (Stage 1 + B1->2 + Stage 2 + ... + Stage 6). Compare the final total
against the threshold from SECTION 2 under:

1. **Normal operation**: state FRESH or STALE and the total elapsed
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE

Address both scenarios separately.

---

**SECTION 6 — RECOVERY PRESCRIPTIONS**

For every `no handling — risk accepted` annotation in SECTION 4 and every named loss point in
SECTION 3, provide a paired recovery prescription. Each prescription must:

1. Name the specific recovery mechanism (retry with backoff, idempotency key, manual requeue,
   compensating write — generic advice does not qualify)
2. **For every prescription**, cite the fallback by its **Manual Step** column value from the
   SECTION 1 INCUMBENT BASELINE TABLE — citing only the process category ("manual
   verification") without naming a specific table row does not satisfy C-16; every recovery
   entry must carry a named step citation

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative vendor onboarding pattern (e.g., sequential stage-gated validation vs
parallel multi-source verification, batch weekly onboarding vs real-time on-demand activation,
third-party vendor screening service vs in-house validation pipeline). State at least two
trade-off dimensions. At least one must compare the automated pipeline's total elapsed time
from SECTION 5 against the **INCUMBENT TOTAL** declared in SECTION 1.

---

Produce all sections in the order shown (Sections 1 through 7). SECTION 1 must appear before
any stage or boundary content.

---

## V-02 — Recovery Citation Structure: Recovery Audit Table with Baseline Step Column

**Variation axis**: Output format — recovery prescriptions structured as an audit table with
a mandatory "Baseline Step Cited" column
**Hypothesis**: When recovery prescriptions are organized as a table where one column is
"Baseline Step Cited (from INCUMBENT BASELINE TABLE)," every missing citation is a visible
blank cell — making C-16 enforcement a table-completeness check rather than a prose discipline
requirement. R4's V-03/V-05 enforced citations at the baseline table level (recovery prose
cites per-row step); this variation enforces citations at the recovery table level. Tests
whether the enforcement surface (baseline vs recovery) produces different C-16 citation
completion rates. Predicts that recovery-table enforcement catches more C-16 violations
because the blank cell is co-located with the recovery mechanism, not in a separate section.

Scenario: Customer returns and credit memo processing pipeline — return merchandise
authorization creation through physical return receipt, condition assessment, inventory
reinstatement, credit memo generation, and customer account adjustment. Commerce owns the
RMA and condition assessment stages; Operations owns physical receipt and inventory
reinstatement; Finance owns credit memo generation and account adjustment.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a customer
returns and credit memo processing pipeline — return merchandise authorization through physical
return receipt, condition assessment, inventory reinstatement, credit memo generation, and
customer account adjustment.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**INCUMBENT BASELINE TABLE**

Document the manual returns processing procedure this pipeline replaces. Present it as the
following four-column table:

| Manual Step | Actor | Duration | Entity Handled |
|-------------|-------|----------|----------------|
| [step name] | [role / team] | [time per return or per batch] | [domain entity] |

**Minimum required**: five distinct manual steps specific to the returns domain (e.g.,
"Customer service agent reviews return request and issues paper RMA form: 15 min per return").
Generic steps not grounded in the returns domain do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. Fixed at declaration; may not be
revised.

---

**DOMAIN CONTEXT**

Declare the entity vocabulary: ReturnRequest, RMARecord, PhysicalReturnReceipt,
ConditionAssessment, InventoryReinstatement, CreditMemo, CustomerAccountAdjustment. State
the business cadence. State the maximum acceptable returns-processing staleness threshold —
the elapsed time from RMA approval to customer account credit before a customer satisfaction
or compliance risk arises. Fixed at declaration.

---

**STAGE TRACE**

For each stage, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: specific field names for every addition, rename, type change, or
  removal; if no change: `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: concrete named failure — "errors may occur" does not qualify

**Stage 1 — RMA Creation**: commerce portal => returns management service
**Stage 2 — Physical Return Receipt**: carrier API => warehouse receiving service
**Stage 3 — Condition Assessment**: warehouse receiving service => condition grading service
**Stage 4 — Inventory Reinstatement**: condition grading service => inventory management service
**Stage 5 — Credit Memo Generation**: inventory management service => billing service
**Stage 6 — Account Adjustment**: billing service => customer AR service

---

**BOUNDARY TABLE**

Produce one row per inter-stage boundary. All five columns are required — a row with any blank
cell is a structural gap.

| Boundary | Error Handling (mechanism or "no handling — risk accepted") | Schema Change (Y/N; if N: "verified unchanged") | Boundary Latency | Entity at Risk |
|----------|------------------------------------------------------------|------------------------------------------------|-----------------|----------------|
| B1->2 | | | | |
| B2->3 | | | | |
| B3->4 | | | | |
| B4->5 | | | | |
| B5->6 | | | | |

Entity at Risk column: must name a specific entity from DOMAIN CONTEXT — "data" or "records"
do not qualify.

---

**STALE ANALYSIS**

Accumulate all stage and boundary latencies step by step, showing each addend through Stage 6.
Compare the final total against the threshold from DOMAIN CONTEXT:

1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE separately

---

**RECOVERY AUDIT TABLE**

Produce one row for every `no handling — risk accepted` entry in BOUNDARY TABLE and one row
for every named loss point in STAGE TRACE. **All five columns are required — a row with any
blank cell is a structural gap detectable without reading surrounding prose.**

| Entry Source | Location (B-label or stage name) | Recovery Mechanism (specific — generic advice fails) | Named Entity Protected | Baseline Step Cited (Manual Step value from INCUMBENT BASELINE TABLE) |
|-------------|----------------------------------|------------------------------------------------------|------------------------|-----------------------------------------------------------------------|

**Baseline Step Cited column rule**: cite the exact **Manual Step** column value from the
INCUMBENT BASELINE TABLE that serves as the fallback for this recovery entry. Generic terms
such as "manual review" or "human intervention" without naming a specific table row do not
qualify. Every row must carry a citation — a blank Baseline Step Cited cell is a structural
gap for C-16.

---

**TRADE-OFF ANALYSIS**

Name an alternative returns processing pattern (e.g., instant digital credit vs physical
return-first policy, centralized returns facility vs store-level processing, automated
condition grading vs manual inspection). State at least two trade-off dimensions. At least one
must compare the automated pipeline's total elapsed time from STALE ANALYSIS against the
**INCUMBENT TOTAL** declared in INCUMBENT BASELINE TABLE.

---

Produce all sections in the order shown. Every table must be fully populated — structural gaps
are visible as blank cells.

---

## V-03 — Step ID Precision: Numbered Incumbent Baseline Identifiers

**Variation axis**: Inertia framing — numbered step IDs (MS-01 through MS-N) as citation
targets for C-16
**Hypothesis**: Assigning explicit numbered IDs to each manual step in the incumbent baseline
table creates a machine-verifiable citation target: a recovery prescription either contains
"MS-03" verbatim or it does not. R4's V-03/V-05 used step names as citation targets — names
can be paraphrased, reducing verifiability. Numbered IDs cannot be paraphrased. Predicts
higher C-16 precision than name-based citation and tests whether the ID format changes how
LLMs structure recovery prescriptions — do they naturally carry the ID forward, or do they
require a per-entry mandate to force ID inclusion?

Scenario: Contract-to-cash settlement pipeline — customer contract activation through usage
metering, invoice generation, payment collection, dispute resolution, and cash application to
revenue ledger. Finance owns invoice generation and cash application; Operations owns usage
metering and payment collection; Commerce owns contract activation and dispute resolution.

---

You are a Finance / Operations / Commerce data domain expert tracing data through a
contract-to-cash settlement pipeline — from customer contract activation through usage
metering, invoice generation, payment collection, dispute resolution, and cash application to
revenue ledger.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**SECTION 1 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual contract-to-cash process this
pipeline replaces. Present it as a four-column table with a mandatory Step ID column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per contract or per period] |
| MS-02 | ... | ... | ... |

**Minimum required**: five distinct manual steps specific to the contract-to-cash domain
(e.g., MS-01: "Finance analyst exports usage data from billing spreadsheet: 45 min per
monthly cycle"). Each Step ID must follow the MS-NN format exactly. Generic steps not
grounded in contract settlement do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

**Citation rule for all downstream sections**: when referencing an incumbent step, cite it by
its **Step ID** (e.g., MS-02) in addition to or instead of the step name. A recovery
prescription that describes step content without citing the Step ID does not satisfy C-16.
Every recovery entry must carry a Step ID citation.

---

**SECTION 2 — DOMAIN CONTEXT**

Declare the entity vocabulary: ContractRecord, UsageMeteringEvent, InvoiceRecord,
PaymentRecord, DisputeRecord, CashApplicationEntry, RevenueLedgerPosting. State the business
cadence. State the maximum acceptable revenue-recognition staleness threshold — the elapsed
time from invoice generation to cash application before a revenue reporting risk arises.
Fixed at declaration.

---

**SECTION 3 — STAGE TRACE**

For each stage, state:
- **Input schema**: key fields, types, cardinality at stage entry
- **Transformations**: specific field names for every addition, rename, type change, or
  removal; if no change: `verified: no field added, removed, renamed, or retyped`
- **Output schema**: key fields, types, cardinality at stage exit
- **Latency**: value, range, or characterization (real-time / micro-batch / hourly / daily)
- **Loss point**: concrete named failure — "errors may occur" does not qualify

**Stage 1 — Contract Activation**: contract management system => billing configuration service
**Stage 2 — Usage Metering**: usage event collector => metering aggregation service
**Stage 3 — Invoice Generation**: metering aggregation service => invoicing service
**Stage 4 — Payment Collection**: invoicing service => payment processing service
**Stage 5 — Dispute Resolution**: payment processing service => dispute management service
**Stage 6 — Cash Application**: dispute management service => cash application service => revenue ledger

---

**SECTION 4 — BOUNDARY CHECKS**

For each inter-stage boundary, provide:
- **Error handling**: the specific mechanism — or state exactly: `no handling — risk accepted`
- **Schema transition**: whether schema changes; if unchanged: `verified unchanged`
- **Boundary latency**: processing overhead at this crossing

Label all boundaries: **B1->2**, **B2->3**, **B3->4**, **B4->5**, **B5->6**.

---

**SECTION 5 — STALE ANALYSIS**

Accumulate stage latencies and boundary latencies step by step, showing each addend through
Stage 6. Compare the final total against the threshold from SECTION 2:

1. **Normal operation**: state FRESH or STALE
2. **Worst-case failure mode** (name the specific failure): state FRESH or STALE separately

---

**SECTION 6 — RECOVERY PRESCRIPTIONS**

For every `no handling — risk accepted` annotation in SECTION 4 and every named loss point in
SECTION 3, provide a paired recovery prescription. Each entry must:

1. Open with the specific boundary label or stage name (e.g., `B3->4:` or
   `Stage 5 loss point:`)
2. Name the specific recovery mechanism (retry policy, dead-letter queue, compensating
   transaction, idempotency key — generic advice fails)
3. Cite the fallback by its **Step ID** (MS-NN format) from the SECTION 1 INCUMBENT BASELINE
   TABLE — citing step content without the Step ID does not satisfy C-16. Every recovery
   entry must carry a Step ID citation.

---

**SECTION 7 — TRADE-OFF ANALYSIS**

Name an alternative contract-to-cash pattern (e.g., usage-based real-time billing vs monthly
invoice cycle, automated dispute routing vs manual escalation queue, integrated CRM-billing
vs separate contract and billing systems). State at least two trade-off dimensions. At least
one must compare the automated pipeline's total elapsed time from SECTION 5 against the
**INCUMBENT TOTAL** declared in SECTION 1.

---

Produce all sections in the order shown (Sections 1 through 7).

---

## V-04 — Phrasing Register: Hard Imperative + Per-Entry Positional Citation Mandate

**Variation axis**: Phrasing register (hard imperative) + per-entry baseline citation at
opening position of every recovery entry
**Hypothesis**: Hard imperative phrasing ("You must...", "Silence fails.") combined with a
positional citation mandate — each recovery entry must open with "Fallback: [Step ID] —
[step name]" before the mechanism description — enforces C-16 by two independent mechanisms:
register pressure (advisory language is disallowed) and position-verifiable structure (the
citation appears at a fixed location in every entry). Tests whether positional enforcement
achieves equivalent C-16 compliance to structural table enforcement (V-02) without requiring
a separate recovery table. Also tests the interaction between imperative register and C-13:
without a structural table, does imperative register alone keep essential criteria coverage
intact?

Scenario: Subscription renewal billing pipeline — from subscription renewal trigger through
entitlement reactivation, proration calculation, invoice generation, payment retry logic, and
renewal confirmation posting. Finance owns invoice generation and payment retry; Operations
owns entitlement reactivation and proration calculation; Commerce owns renewal trigger and
confirmation posting.

---

You are a Finance / Operations / Commerce data domain expert. You must trace data through a
subscription renewal billing pipeline — from subscription renewal trigger through entitlement
reactivation, proration calculation, invoice generation, payment retry, and renewal
confirmation posting.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

**You must work through every section in the stated order. You may not skip a section.
Silence on any required item within a section is a protocol failure.**

---

**INCUMBENT BASELINE TABLE**

You must document the manual subscription renewal process this pipeline replaces before any
stage is traced. Present it as the following four-column table with a Step ID column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per renewal or per batch] |

**Minimum required**: five distinct manual steps specific to the subscription renewal domain
(e.g., MS-01: "Billing coordinator reviews lapsing subscription list in spreadsheet: 30 min
per weekly run"). Each Step ID must follow the MS-NN format. Generic steps not grounded in
subscription renewal do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values. You may not revise this value after
this section.

Every recovery entry in RECOVERY PRESCRIPTIONS must open with a Step ID citation from this
table — "at least one" is insufficient to satisfy full traceability for C-16.

---

**DOMAIN CONTEXT**

You must declare: entity vocabulary (RenewalTrigger, EntitlementRecord, ProrationCalculation,
RenewalInvoice, PaymentAttempt, RenewalConfirmation); business cadence; maximum acceptable
renewal-posting staleness threshold — the elapsed time from renewal trigger to confirmation
posting before a customer SLA breach risk arises. This threshold is fixed at declaration. You
may not revise it.

---

**STAGE TRACE WITH INLINE BOUNDARY GATES**

For each stage, you must state all five items. Omitting any item is a protocol failure:

1. **Input schema**: key fields, types, cardinality at entry — specific field names required
2. **Transformations**: every field added, renamed, retyped, or removed; if no change, you
   must state exactly: `verified: no field added, removed, renamed, or retyped`
3. **Output schema**: key fields, types, cardinality at exit
4. **Latency**: value, range, or characterization — silence fails
5. **Loss point**: a concrete named failure mode as it would appear in an incident report —
   "errors may occur" fails

---

**Stage 1 — Renewal Trigger**: subscription management service => renewal processing service

[State all five items for Stage 1.]

**BOUNDARY GATE B1->2** — You must complete this gate before writing Stage 2. The gate must
contain all three items; a gate with any item missing is a protocol failure:

- (a) **Error handling**: name the specific mechanism — or state exactly:
  `no handling — risk accepted [B1->2]`
- (b) **Boundary latency**: additive increment to elapsed total
- (c) **Schema continuity**: if unchanged, state: `verified unchanged at B1->2`

**Stage 2 does not open until BOUNDARY GATE B1->2 is fully stated.**

---

**Stage 2 — Entitlement Reactivation**: renewal processing service => entitlement service

[State all five items for Stage 2.]

**BOUNDARY GATE B2->3** — Complete before opening Stage 3. Same three items as B1->2.
Use label B2->3 in every annotation.

**Stage 3 does not open until BOUNDARY GATE B2->3 is fully stated.**

---

**Stage 3 — Proration Calculation**: entitlement service => proration calculation service

[State all five items for Stage 3.]

**BOUNDARY GATE B3->4** — Complete before opening Stage 4. Same three items. Use label B3->4.

**Stage 4 does not open until BOUNDARY GATE B3->4 is fully stated.**

---

**Stage 4 — Invoice Generation**: proration calculation service => invoicing service

[State all five items for Stage 4.]

**BOUNDARY GATE B4->5** — Complete before opening Stage 5. Same three items. Use label B4->5.

**Stage 5 does not open until BOUNDARY GATE B4->5 is fully stated.**

---

**Stage 5 — Payment Retry**: invoicing service => payment processing service

[State all five items for Stage 5.]

**BOUNDARY GATE B5->6** — Complete before opening Stage 6. Same three items. Use label B5->6.

**Stage 6 does not open until BOUNDARY GATE B5->6 is fully stated.**

---

**Stage 6 — Renewal Confirmation Posting**: payment processing service => subscription management service

[State all five items for Stage 6. No outbound gate is required for the terminal stage.]

---

**STALE ANALYSIS**

You must accumulate all stage latencies and boundary latencies step by step. A final total
with no breakdown fails. You must address exactly two scenarios and state each verdict using
exactly the token FRESH or STALE:

1. **Normal operation**: accumulated total vs threshold from DOMAIN CONTEXT — state verdict
2. **Worst-case failure** (you must name the specific failure): same comparison — state
   verdict separately

---

**RECOVERY PRESCRIPTIONS**

For every `no handling — risk accepted [B[N]->[N+1]]` gate annotation and every named loss
point in the stage trace, you must provide a paired recovery prescription.

**Each entry must follow this exact three-part structure:**

1. **Location**: boundary label (e.g., `B3->4`) or stage loss point name
2. **Fallback**: [Step ID in MS-NN format] — [Manual Step value from INCUMBENT BASELINE TABLE].
   You must cite the Step ID. Generic terms such as "manual review" without a Step ID are
   protocol failures. Every recovery entry must carry a Fallback line — entries without one
   are protocol failures.
3. **Recovery Mechanism**: the specific mechanism (retry with backoff, dead-letter queue,
   compensating transaction, idempotency key — generic advice fails)

---

**TRADE-OFF ANALYSIS**

You must name an alternative subscription renewal architecture (e.g., dunning sequence with
grace period vs immediate suspension on payment failure, prorated renewal vs full-period
renewal, self-service renewal portal vs automated trigger). You must state at least two
trade-off dimensions. At least one must compare the automated pipeline's total elapsed time
against the **INCUMBENT TOTAL** declared in INCUMBENT BASELINE TABLE.

---

Produce all sections and gates in the stated order. You may not reorder or consolidate
sections. Every required item must be present.

---

## V-05 — Combined: Step IDs + Recovery Audit Table + Per-Entry Mandate + Schema-Diff Tables

**Variation axis**: Step ID numbering (V-03) + Recovery audit table with Baseline Step Cited
column (V-02) + Per-entry citation mandate (V-04) + Per-stage schema-diff tables (R4 V-02)
**Hypothesis**: Quadruple structural enforcement produces the highest combined C-15 and C-16
scores while also maximizing C-04 and C-13 coverage from prior rounds. Step IDs (V-03) make
citations machine-verifiable; the recovery audit table (V-02) makes every missing C-16
citation a blank cell; per-entry mandate (V-04) closes prose escape routes; schema-diff tables
(R4 V-02) surface C-04 violations as structurally visible blank Transformations cells. The
co-presence test: does quadruple scaffolding produce a coherent, executable prompt, or does
structural density at this level obscure essential coverage (C-01 through C-04) by crowding
out prose lineage descriptions?

Scenario: Inventory cost revaluation pipeline — from standard cost update through open purchase
order cost adjustment, on-hand inventory revaluation, cost of goods sold recalculation,
variance posting, and GL cost reconciliation. Finance owns variance posting and GL
reconciliation; Operations owns PO cost adjustment and inventory revaluation; Commerce owns
COGS recalculation and cost reporting.

---

You are a Finance / Operations / Commerce data domain expert tracing data through an inventory
cost revaluation pipeline — from standard cost update through open purchase order cost
adjustment, on-hand inventory revaluation, COGS recalculation, variance posting, and GL cost
reconciliation.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

**STEP 0 — INCUMBENT BASELINE TABLE**

Before any pipeline stage is traced, document the manual cost revaluation process this
pipeline replaces. Present it as the following four-column table with a mandatory Step ID
column:

| Step ID | Manual Step | Actor | Duration |
|---------|-------------|-------|----------|
| MS-01 | [step name] | [role / team] | [time per revaluation cycle] |
| MS-02 | ... | ... | ... |

**Minimum required**: five distinct manual steps specific to the inventory cost revaluation
domain (e.g., MS-01: "Cost accountant exports current standard costs from ERP to spreadsheet:
25 min per monthly cycle"). Each Step ID must follow the MS-NN format exactly. Generic steps
not grounded in cost revaluation do not qualify.

After the table, state:

**INCUMBENT TOTAL**: additive sum of all Duration values (sequential execution). Fixed at
declaration; may not be revised.

**Citation rule**: in all downstream sections, cite incumbent steps by Step ID (MS-NN format).
A citation that describes step content without the Step ID does not qualify. All recovery
entries must carry a Step ID citation.

This table and its INCUMBENT TOTAL are the sole authority for:
- Step ID citations required in STEP 8 (Recovery Audit Table)
- Baseline comparison required in STEP 9 (Trade-Off Analysis)

---

**STEP 1 — DOMAIN CONTEXT**

Declare the entity vocabulary: StandardCostRecord, PurchaseOrderLine, InventoryLot,
COGSRecord, CostVariance, GLCostEntry. State the business cadence. State the maximum
acceptable cost-revaluation staleness threshold — the elapsed time from standard cost update
to GL reconciliation before financial reporting accuracy risk arises. Fixed at declaration;
revisions not permitted.

---

**STEP 2 — STAGE 1: Standard Cost Update**

Standard cost management service => cost distribution service.

Produce a schema-diff table followed by latency and loss-point entries. **The schema-diff
table must be fully populated — a blank Transformations cell is a structural gap visible
without reading stage prose.**

Schema-diff table format:

| Field | Entry Schema (type : cardinality) | Transformations | Exit Schema (type : cardinality) |
|-------|------------------------------------|-----------------|----------------------------------|
| [field name] | [type : cardinality] | [change description or `verified: no change`] | [type : cardinality] |

**Transformations cell rule**: if no change for a field, write exactly:
`verified: no field added, removed, renamed, or retyped`. A blank cell or bare "unchanged"
fails.

After the table:
- **Latency**: value, range, or characterization
- **Loss point**: concrete named failure

**BOUNDARY GATE B1->2** — Complete before opening Stage 2. All three items required;
a gate with any item missing is a structural gap:

- (a) **Error handling**: name the mechanism — or: `no handling — risk accepted [B1->2]`
- (b) **Boundary latency**: additive increment to elapsed total
- (c) **Schema continuity**: if unchanged: `verified unchanged at B1->2`

**Stage 2 does not open until BOUNDARY GATE B1->2 is fully stated.**

---

**STEP 3 — STAGE 2: PO Cost Adjustment**

Cost distribution service => purchase order service.

Same format as Step 2: schema-diff table (fully populated, Transformations cell rule applies),
then latency and loss point.

**BOUNDARY GATE B2->3** — Same three items as B1->2. Use label B2->3.

**Stage 3 does not open until BOUNDARY GATE B2->3 is fully stated.**

---

**STEP 4 — STAGE 3: Inventory Revaluation**

Purchase order service => inventory management service.

Same format.

**BOUNDARY GATE B3->4** — Same three items. Use label B3->4.

**Stage 4 does not open until BOUNDARY GATE B3->4 is fully stated.**

---

**STEP 5 — STAGE 4: COGS Recalculation**

Inventory management service => COGS calculation service.

Same format.

**BOUNDARY GATE B4->5** — Same three items. Use label B4->5.

**Stage 5 does not open until BOUNDARY GATE B4->5 is fully stated.**

---

**STEP 6 — STAGE 5: Variance Posting and GL Reconciliation**

COGS calculation service => variance ledger service => GL reconciliation service.

Same format (schema-diff table + latency + loss point). This is the terminal stage; no
outbound boundary gate is required.

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

**STEP 8 — RECOVERY AUDIT TABLE**

Produce one row for every `no handling — risk accepted [B[N]->[N+1]]` gate annotation and one
row for every named loss point in the stage trace steps. **All six columns are required — a
row with any blank cell is a structural gap detectable without reading surrounding prose.**

| Entry Source | Location (B-label or stage name) | Recovery Mechanism (specific — generic fails) | Named Entity Protected | Step ID Cited (MS-NN from STEP 0) | Manual Step Cited (exact value from STEP 0) |
|-------------|----------------------------------|-----------------------------------------------|------------------------|-----------------------------------|---------------------------------------------|

**Step ID Cited column rule**: cite the Step ID in MS-NN format from the STEP 0 INCUMBENT
BASELINE TABLE. A blank cell or a citation without the MS-NN format is a structural gap
for C-16.

**Manual Step Cited column rule**: cite the exact **Manual Step** column value from STEP 0,
verbatim. A paraphrase that omits the Step ID does not satisfy the requirement.

Every row must carry both a Step ID and a Manual Step citation. A blank cell in either
citation column is a visible, scorable C-16 gap.

---

**STEP 9 — TRADE-OFF ANALYSIS**

Name an alternative cost revaluation architecture (e.g., standard costing vs actual costing
with real-time lot-level tracking, period-end mass revaluation vs continuous incremental
adjustment, integrated ERP cost engine vs separate specialist cost management system). State
at least two trade-off dimensions. At least one must compare the automated pipeline's total
elapsed time from STEP 7 against the **INCUMBENT TOTAL** declared in STEP 0.

---

Work through Steps 0 through 9 in order. Do not skip any step or gate.

---

## Axis Coverage Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Baseline table columns | 3-col minimal | 4-col standard | 4-col + Step ID | 4-col + Step ID | 4-col + Step ID |
| Step IDs (MS-NN) | no | no | yes | yes | yes |
| Recovery citation enforcement | prose mandate (all entries, name) | recovery table (5-col, Baseline Step Cited) | prose mandate (all entries, ID format) | positional mandate (entry Fallback header) | recovery audit table (6-col, ID + name) |
| Recovery table format | none | yes (5-col) | none | none | yes (6-col) |
| Inline boundary gates | no | no | no | yes | yes |
| Schema-diff tables | no | no | no | no | yes (per-stage) |
| Phrasing register | imperative | imperative | imperative | hard imperative | imperative |
| C-15 depth | floor (3-col) | standard (4-col) | extended (4-col + ID) | extended (4-col + ID) | extended (4-col + ID) |
| C-16 enforcement surface | recovery prose | recovery table | prose (ID-verifiable) | positional mandate | table + positional |
| C-13 structural surfaces | 0 | 2 (boundary + recovery) | 0 | 1 (gate) | 3 (schema-diff + gate + recovery) |
| C-14 depth | medium | medium | high | high | high |
