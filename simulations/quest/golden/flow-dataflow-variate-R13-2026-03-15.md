# flow-dataflow — Round 13 Variations (Rubric v10)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v10 (C-01 through C-24, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

R13 builds on validated rubric v10. R11 V-01 (17/17 aspirational) established the
protocol-contract scaffold-first design as the high-water mark. R12 explored three axes:
conversational phrasing (V-01, V-04), boundary-first lifecycle (V-02, V-04), and
incumbent-centric narrative (V-03, V-05). R12 V-05 tested a four-role sequence (Scaffold
Architect → Operations → Finance → Commerce) combined with inertia-first framing.

**R13 goal**: Three axes not yet explored as clean single-axis controls —
(1) Commerce-first role sequence as a pure ordering variable with no other axes changed,
(2) Failure-mode-first lifecycle where LP-NN/NH-NN identifiers are predicted before any
stage trace begins, and (3) explicit criterion-tagging where the rubric criteria IDs are
visible in the prompt and the model tags its output sections against them. Secondary
question: does criterion transparency improve or degrade organic domain quality?

**What R12 established:**

- Conversational register does NOT cause C-24 scaffold collapse if the structural
  requirements (T-NN tokens, upstream references column) are preserved. The invitation
  framing affects tone; the scaffold dependency graph is maintained when the column
  contract is explicit.
- Boundary-first lifecycle (T-03 declared before stage traces) creates visible structural
  pressure on C-17/C-20 field citations — the stub row forces the model to return and
  populate entity.field after exit manifests are available.
- Incumbent-centric framing (INCUMBENT EQUIVALENT block per stage) measurably increases
  MS-NN step citation density in recovery prescriptions, supporting C-16 full compliance.
- Four-role sequence (Scaffold Architect isolated from domain roles) produces the cleanest
  C-24 scaffold — the scaffold role cannot contaminate the scaffold with domain content.

**R13 hypothesis space:**

**H1 — Commerce-first role sequence (V-01)**
Commerce domain expert runs first (entity inventory + source-side exit manifests for
Commerce-sensitive stages). Operations runs second (pipeline mechanics, boundary inventory,
latency). Finance runs third (SLA budget, domination point, recovery audit, closure gate).
Commerce expertise is strongest at source-side field semantics: which SKU fields drive
purchase decisions, which catalog fields are nullable vs required, what stale windows mean
in terms of lost conversion. The hypothesis: leading with Commerce produces higher-quality
C-10 entity inventory (more SKU/Commerce-specific field vocabulary), richer C-07 domain
framing in the entity.field citations (C-20), and better C-06 stale window characterization
because Commerce can quantify the revenue impact of a stale inventory count.
Prediction: stronger C-20 field citation vocabulary (Commerce-native field names rather
than generic "id/amount/status" patterns); C-22 domination point linked to a Commerce-
articulated revenue consequence rather than a Finance SLA fraction.

**H2 — Failure-mode-first lifecycle (V-02)**
Before any stage trace begins, a dedicated PHASE 0 catalogs known failure modes for the
pipeline pattern as LP-NN (data loss points) and NH-NN (no-handling annotations), drawing
on pattern knowledge rather than stage-by-stage discovery. This creates a prediction
register. The stage trace (PHASE 2) validates predictions: each stage either confirms a
predicted LP-NN/NH-NN or adds a new one that was not anticipated. The hypothesis: pre-
cataloging failure modes from pattern knowledge produces a more complete LP-NN/NH-NN
register than discover-as-you-trace, because the model applies systematic pattern-level
reasoning before being constrained by stage-by-stage detail. Prediction: fewer unaddressed
LP-NN/NH-NN at closure gate (C-23) because the prediction phase catches failure modes that
individual stage traces might miss; higher C-03 completeness; possible increase in total
LP-NN/NH-NN count vs stage-first lifecycle designs from R11/R12.

**H3 — Explicit criterion-tagging (V-03)**
Each prompt section header names the C-NN criteria it satisfies. The model is instructed
to tag its output subsections with the criterion IDs they address. The rubric is made
partially visible: the model sees which criteria matter (by structural section placement)
but not the full pass/fail conditions. The hypothesis is ambiguous — two outcomes are
plausible: (A) Criterion visibility causes the model to produce criterion-targeted output
that hits all marks cleanly, improving completeness on aspirational criteria (C-19, C-20,
C-21, C-22); (B) Criterion visibility causes the model to produce mechanical "checkbox"
outputs that satisfy literal pass conditions but degrade organic domain framing (C-07),
producing entity names that feel like criterion satisfaction placeholders rather than real
Commerce/Finance/Operations vocabulary. Distinguishing (A) from (B) is the primary signal
R13 seeks from this axis.

**H4 — Combined: Commerce-first role sequence + failure-mode-first lifecycle (V-04)**
Combines H1 (Commerce leads with entity inventory) with H2 (failure-mode prediction before
stage trace). Commerce expert produces both the entity inventory AND the failure mode
prediction register — on the hypothesis that Commerce domain expertise includes the best
knowledge of which catalog and inventory data quality problems are endemic to the pipeline
type. Operations expert traces stages against predictions. Finance expert closes: SLA
budget, recovery audit, domination point, closure gate.
The combination test: does Commerce-owned failure prediction produce more domain-specific
LP-NN descriptions (named SKU fields, named Commerce failure modes) than Operations-owned
failure prediction from standard pipeline pattern knowledge?

**H5 — Combined: Explicit criterion-tagging + Scaffold Authority (V-05)**
Combines H3 (criterion-tagging) with R11 V-01's proven Scaffold Authority design (STEP 0
scaffold precedes all domain content; every table declared with T-NN token, purpose, and
upstream references). The scaffold itself is criterion-mapped: each scaffold row declares
not just the table purpose but which C-NN criteria the table satisfies. The body sections
are criterion-tagged. The hypothesis: adding criterion transparency to the proven highest-
scoring design either (A) preserves 17/17 while exposing which output sections are most
mechanically driven, or (B) introduces checkbox degradation in C-07/C-09 domain framing
sections. If (A), criterion-tagging is a safe addition and could be promoted as a
structural reinforcement for weaker prompt designs. If (B), it confirms that organic domain
immersion is incompatible with explicit rubric visibility.

**Axes selected for R13:**

1. **Commerce-first role sequence** — Commerce produces entity inventory + source-side
   exit manifests before Operations traces pipeline internals (single axis: V-01)
2. **Failure-mode-first lifecycle** — LP-NN/NH-NN prediction register before any stage
   trace; stage trace validates predictions (single axis: V-02)
3. **Explicit criterion-tagging** — C-NN IDs visible in prompt section headers; model tags
   output sections with criterion IDs they address (single axis: V-03)
4. **Combined (H1 + H2)** — Commerce-first role sequence + failure-mode-first lifecycle
   (V-04)
5. **Combined (H3 + Scaffold Authority)** — criterion-tagging + proven R11 V-01 scaffold
   design (V-05)

**New signal candidates for R13:**

1. **Commerce-native field vocabulary in C-20** (V-01, V-04) — whether Commerce-first role
   sequence produces entity.field citations with Commerce-native field names (e.g.,
   `SKU.list_price_USD`, `InventoryRecord.available_to_promise_qty`) vs generic names
   (e.g., `Product.price`, `Inventory.count`). Success signal: field names use domain-
   specific identifiers found in real Commerce data models. Failure signal: field names
   are generic cross-domain identifiers that any role would produce.

2. **Prediction register completeness vs discover-as-you-trace** (V-02, V-04) — total
   LP-NN/NH-NN count in failure-mode-first designs vs R11/R12 stage-first designs.
   Success signal: prediction phase surfaces >= 2 LP-NN/NH-NN identifiers not typically
   found by stage-first tracing. Failure signal: prediction register has 100% overlap
   with stage-by-stage discovery — no additional failure modes from pattern-level reasoning.

3. **Criterion-tagging effect on C-07 domain framing quality** (V-03, V-05) — whether
   explicit criterion visibility degrades organic domain vocabulary. Proxy: entity names
   and field citations in criterion-tagged sections vs non-tagged sections. Success signal
   for (A): domain entity vocabulary is richer in tagged sections because the model is
   primed to satisfy C-07 explicitly. Failure signal (B) indicator: entity names in tagged
   sections become generic ("Record," "DataItem") while named entities appear only in
   scaffold rows.

4. **Criterion-to-scaffold mapping clarity** (V-05) — whether adding C-NN annotations to
   each scaffold row (T-01 through T-NN) makes the scaffold more navigable and improves
   cross-table citation accuracy. Success signal: every cross-table citation in the body
   resolves against a scaffold row with a matching C-NN tag, creating a verifiable
   dependency graph. Failure signal: C-NN tags in scaffold rows drift from the actual
   criteria satisfied, because the model assigns criterion IDs by proximity rather than
   by genuine structural matching.

---

## V-01 — Commerce-First Role Sequence

**Variation axis**: Role sequence — Commerce domain expert runs first, establishing the
entity inventory and source-side typed exit manifests before any pipeline mechanics are
traced. Operations runs second and owns the pipeline internals: stage trace for non-source
stages, boundary inventory, latency decomposition, stale window analysis. Finance runs
third and owns the financial frame: SLA budget, domination point, incumbent baseline,
recovery audit, closure gate.

**Hypothesis**: Leading with Commerce expertise front-loads the entity vocabulary and
source-side schema authority, producing richer C-10 entity inventory and C-20 field
citations with Commerce-native field names. Finance anchoring the SLA budget after
Commerce establishes the entity frame means the domination point statement (C-22) is
expressed in Commerce-articulated revenue terms rather than generic SLA fractions.
Predicts: higher field-name specificity in entity.field citations; stale window (C-06)
characterized in Commerce impact terms (conversion loss, stockout probability) rather than
just latency hours.

Scenario: Commerce — product SKU catalog and inventory availability sync pipeline.
SKU master data and real-time inventory counts flow from ERP Product Information Management
through CDC capture, message queue, product sync service, e-commerce platform cache, and
inventory availability calculation to the customer-facing product listing service.
Stages: ERP PIM Export → CDC Capture → Message Queue → Product Sync Service →
E-commerce Platform Cache → Inventory Availability Calculation.

---

You are running a three-role analysis of a product SKU catalog and inventory availability
sync pipeline. The pipeline carries SKU master data and inventory counts from an ERP
Product Information Management system to the customer-facing product listing service on an
e-commerce platform. Roles execute in sequence: Commerce domain expert runs first,
Operations domain expert runs second, Finance domain expert runs third.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### STEP 0 — OUTPUT TABLE SCAFFOLD

Before any domain analysis begins, declare every table that will appear in this response.
A table not listed here is an undeclared artifact. Every row must have a T-NN token, a
table name, a one-sentence purpose statement naming which criteria it satisfies, and a
complete list of upstream T-NN tokens (or "none" if foundational).

The scaffold is the navigation contract for all cross-table citations that follow. Any
citation that cannot be resolved by consulting this table is an invalid citation.

| Table # | Table Name | Purpose (criteria satisfied) | Upstream Tables |
|---------|------------|------------------------------|-----------------|
| T-01 | [table name] | [purpose + criteria IDs: e.g., C-10, C-19, ...] | [T-NN list or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

Minimum expected entries:
- Entity Inventory (foundational — C-10)
- Incumbent Baseline (foundational — C-14, C-15)
- One exit manifest per pipeline stage (T-NN for each stage exit — C-04, C-12, C-19)
- Boundary Inventory (references exit manifests — C-11, C-17, C-20, C-21, C-22)
- Stale Window Analysis (references boundary inventory — C-06)
- Recovery Audit Table (references boundary inventory + exit manifests + incumbent — C-08, C-16, C-18)
- Closure Gate (references recovery audit — C-23)

No table may appear in the body that is not declared here.

---

### ROLE 1 — COMMERCE DOMAIN EXPERT

*Commerce domain expert produces: entity inventory, source-side exit manifests (ERP PIM
Export and CDC Capture stages), and initial LP-NN/NH-NN identification for Commerce-
sensitive boundaries.*

**Entity Inventory** (T-NN from scaffold)

Before the first stage trace, enumerate all in-scope domain entities. Every entity that
appears in any subsequent stage trace or boundary annotation must be declared here first.
An entity introduced mid-trace without prior declaration is a structural gap.

| Entity Name | Domain area | Key fields | Role in pipeline |
|-------------|-------------|------------|-----------------|

Required entities include at minimum: SKUMaster, InventoryRecord, CDCEvent, SyncMessage,
PlatformCatalogEntry, AvailabilitySignal. Use Commerce-native field names — the field
vocabulary established here will be required in all entity.field citations downstream
(C-17, C-20). Generic field names ("id", "status", "amount") are insufficient; use names
drawn from standard Commerce data models (e.g., `SKUMaster.list_price_USD`,
`InventoryRecord.available_to_promise_qty`, `SKUMaster.fulfillment_channel_code`).

Also declare the SLA context: what is the maximum acceptable end-to-end latency from ERP
PIM Export to customer-facing availability update? Express as a numeric value in minutes
(the SLA budget). We will use this to compute SLA% per boundary in the Finance role.

**Stage Trace — ERP PIM Export** (T-NN from scaffold)

Trace the first stage: ERP Product Information Management system exports SKU master data
and inventory snapshots.

| Field | Type at Exit | Schema Change from Entry | Data Loss Risk | Stage Latency |
|-------|-------------|--------------------------|----------------|---------------|

- Schema change: if no change, state "NONE — verified: no field added, removed, renamed,
  or retyped." A bare "unchanged" without the verification claim fails C-12.
- Data loss risk: assign LP-NN identifier with a named entity and specific condition.
  "LP-01: SKUMaster records with null fulfillment_channel_code excluded from export
  batch — downstream platform receives no availability signal for affected SKUs."
  Generic risks ("errors may occur") do not qualify.
- Error handling: if no error handling exists at this stage exit, annotate:
  "NH-NN: no handling — risk accepted at [stage name]."

After the stage table, produce a typed exit manifest:

```
EXIT MANIFEST — ERP PIM Export: [entity names exported]
  fields: [count]
  key field assertions:
    [field_name: TYPE(precision)]
    [field_name: TYPE(precision)]
    (minimum four assertions for Commerce-critical fields)
```

**Stage Trace — CDC Capture** (T-NN from scaffold)

Trace the second stage: Change Data Capture captures row-level changes from the ERP
transaction log.

Same structure as ERP PIM Export: stage table + typed exit manifest. Commerce-specific
focus: which CDC event types (INSERT, UPDATE, DELETE) are captured for SKUMaster vs
InventoryRecord? Are soft-delete SKU records captured and propagated, or silently dropped?

---

### ROLE 2 — OPERATIONS DOMAIN EXPERT

*Operations domain expert produces: stage traces for Message Queue, Product Sync Service,
and E-commerce Platform Cache stages; boundary inventory; latency decomposition; stale
window analysis.*

**Stage Traces — Message Queue, Product Sync Service, E-commerce Platform Cache**
(T-NN entries from scaffold for each stage)

For each stage, produce a stage table and typed exit manifest in the same format as Role 1.
Operations focus areas:
- Message Queue: message ordering guarantees, dead-letter handling, at-least-once vs
  exactly-once semantics for CDCEvent delivery
- Product Sync Service: conflict resolution when multiple CDC events arrive for the same
  SKU within one processing window; field-level merge vs full-record replace
- E-commerce Platform Cache: TTL-based vs event-driven invalidation; cache coherence
  between product details and inventory availability signals

Assign LP-NN and NH-NN identifiers to every data loss point and unhandled boundary
discovered in these stages. Continue the LP-NN/NH-NN sequence from Role 1.

**Boundary Inventory** (T-NN from scaffold)

Produce a complete boundary inventory covering all inter-stage handoffs: B1->2 through
B5->6.

| Boundary | Error Handling (NH-NN or mechanism) | Entity at Risk (entity.field — risk) | Transport Latency (ms) | Processing Overhead (ms) | Total (ms) |
|----------|-------------------------------------|--------------------------------------|------------------------|--------------------------|------------|
| B1->2 | | | | | |
| B2->3 | | | | | |
| B3->4 | | | | | |
| B4->5 | | | | | |
| B5->6 | | | | | |

Rules:
- Entity at Risk: must use entity.field format from the upstream exit manifest.
  `SKUMaster.list_price_USD — risk description` is valid. `Product data — at risk` fails.
  A boundary with no entity.field annotation fails C-17/C-20.
- Transport Latency and Processing Overhead: both must be independent numeric estimates
  in ms. "Negligible" is not acceptable. The sum must equal or account for Total.
- NH-NN reference: if a boundary has no error handling, use the NH-NN identifier declared
  in the stage trace (do not create new identifiers here).

**Stale Window Analysis** (T-NN from scaffold)

Compute accumulated end-to-end latency by summing stage and boundary latencies from ERP
PIM Export through Inventory Availability Calculation. Show Transport and Processing
Overhead separately at each step.

- Normal operation: is the customer-facing availability signal fresh relative to the SLA
  declared in the entity inventory?
- Worst failure mode: name it using the LP-NN or NH-NN identifier, quantify the stale
  window in minutes, and state what it means for inventory availability in Commerce terms
  (e.g., "SKUs show available while actual on-hand is zero — estimated 0.X% phantom
  availability rate at peak throughput").

---

### ROLE 3 — FINANCE DOMAIN EXPERT

*Finance domain expert produces: SLA% columns for boundary inventory, domination point
statement, incumbent baseline table, recovery audit table, closure gate.*

**SLA% Columns for Boundary Inventory**

Return to the boundary inventory produced by Operations (T-NN from scaffold) and add two
columns: "SLA% This Boundary" and "Cumulative SLA%". Use the SLA budget declared by the
Commerce expert in the entity inventory as the denominator.

After the updated table, state the DOMINATION POINT: the first boundary where Cumulative
SLA% crosses 50% of the SLA budget. Name the boundary, cite the exact cumulative
percentage at that crossing, and provide one sentence explaining why this boundary
dominates in Commerce/operational terms.

**Incumbent Baseline** (T-NN from scaffold)

Before this automation pipeline existed, the product and inventory data reached the
e-commerce platform through a manual or batch process. Describe that process as a named
table:

| Step ID | Manual Step | Responsible Actor/Role | Elapsed Time / Frequency |
|---------|-------------|------------------------|--------------------------|
| MS-01 | [step description] | [role] | [time or frequency] |
| MS-02 | ... | ... | ... |

Minimum: five steps. Steps must be specific enough to reference by row from recovery
prescriptions downstream (e.g., "MS-03: E-commerce catalog admin runs manual bulk import
script from shared FTP directory — 45 min per batch"). Generic descriptions like "review
data" do not qualify.

After the table, state the INCUMBENT TOTAL elapsed time if all steps run sequentially.

**Recovery Audit Table** (T-NN from scaffold)

For every NH-NN and LP-NN declared across all three roles, produce a recovery prescription
organized as a table:

| Trigger ID | Triggering Condition | Recovery Mechanism | Boundary/Stage | Incumbent Step Fallback (MS-NN from T-NN) |
|------------|---------------------|-------------------|----------------|-------------------------------------------|
| [NH-NN or LP-NN] | [specific condition from stage or boundary trace] | [specific mechanism naming action and boundary] | [B-NN or stage name] | [exact MS-NN step ID and step name from incumbent baseline] |

Rules:
- Incumbent Step Fallback: every row must cite a specific MS-NN step ID (not just the
  process name). "Revert to manual process" fails C-16. "MS-03: E-commerce catalog admin
  bulk import" is valid.
- Recovery Mechanism: must name the specific action and the specific boundary or service
  where it executes. "Manual review" fails C-08.
- Every NH-NN and LP-NN identifier declared in Roles 1, 2, and 3 must have a row here.
  A missing row is a structural gap.

**Closure Gate** (T-NN from scaffold)

Perform a forward check confirming that every NH-NN and LP-NN identifier declared in this
response has exactly one corresponding row in the recovery audit table. Check against the
original declarations in the stage traces and boundary inventory — do not derive this list
from the recovery table itself.

| Identifier | Where Declared | Recovery Row Present? | Status |
|------------|---------------|----------------------|--------|
| [NH-NN or LP-NN] | [stage or boundary + T-NN] | [YES / NO] | [CLOSED / OPEN] |

A count summary ("all 8 are covered") does not satisfy this requirement. Per-identifier
status is required. An identifier with no recovery row must appear as OPEN.

**Pattern Assessment**

Name the integration pattern this pipeline implements. Name one alternative pattern and
provide at least two trade-off dimensions — at least one quantified or qualified in
Commerce-domain terms (e.g., "event-driven sync eliminates 45-min batch window but
introduces per-SKU processing overhead of 12 ms vs 3 ms per record in batch mode, raising
risk of message queue backlog during peak catalog update events").

---

*Scaffold contract: the scaffold produced in STEP 0 is the navigational contract for this
response. Every cross-table citation uses T-NN tokens from that scaffold. A table that
appears for the first time in the body without a corresponding scaffold row is an undeclared
artifact. All NH-NN and LP-NN identifiers are declared at their source stage or boundary
and referenced — never renamed or re-assigned — in the recovery audit and closure gate.*

---

## V-02 — Failure-Mode-First Lifecycle

**Variation axis**: Lifecycle emphasis — before any stage trace begins, a dedicated
PHASE 0 catalogs predicted failure modes for the pipeline pattern as LP-NN (data loss
points) and NH-NN (no-handling annotations). This prediction register is produced from
pattern-level knowledge, not stage-by-stage discovery. The stage trace (PHASE 2) then
validates each prediction: each stage either confirms a predicted identifier (cite the
LP-NN/NH-NN token), adds a new one discovered during tracing (assigned next available
token), or explicitly exonerates a prediction ("LP-03 not observed — this stage has
idempotent insert with UPSERT semantics"). The recovery audit and closure gate close
against the final merged register.

**Hypothesis**: Pattern-level failure prediction before stage tracing produces a more
complete LP-NN/NH-NN register than discover-as-you-trace, because the model applies
systematic pattern knowledge before being constrained by stage-by-stage detail. Predicts:
higher total LP-NN/NH-NN count; fewer OPEN identifiers at closure gate; possible false
positives (predicted LP-NN identifiers that the stage trace exonerates) which themselves
become valuable signal about pipeline resilience relative to pattern expectations.

Scenario: Finance — dual-write AP GL consolidation pipeline. The accounts payable
subledger simultaneously writes committed AP accrual entries to the transactional GL
(Oracle Fusion) and a financial reporting data lake (Azure Synapse) via a CDX coordination
layer. A reconciliation service runs period-end to detect and resolve divergence.
Stages: AP Subledger Commit → CDX Write Coordinator → Transactional GL Write →
Data Lake Ingest → Reconciliation Service → Consolidated Reporting View.

---

You are a Finance data domain expert tracing data through a dual-write AP GL consolidation
pipeline. The accounts payable subledger commits AP accrual entries simultaneously to a
transactional GL (Oracle Fusion) and a financial reporting data lake (Azure Synapse) via a
CDX coordination layer. A reconciliation service runs at period-end to detect and resolve
divergence between the two write destinations.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### STEP 0 — OUTPUT TABLE SCAFFOLD

Declare every table that will appear in this response before producing any domain content.
The scaffold is the navigation contract. A table not declared here is an undeclared
artifact. Every row requires: T-NN token, table name, purpose (with C-NN criteria IDs),
upstream T-NN references.

| Table # | Table Name | Purpose (criteria satisfied) | Upstream Tables |
|---------|------------|------------------------------|-----------------|
| T-01 | [table name] | [purpose + criteria IDs] | [T-NN list or "none"] |
| T-02 | ... | ... | ... |
| ... | ... | ... | ... |

Minimum expected entries:
- Failure Mode Prediction Register (foundational — C-03, C-02 partial)
- Incumbent Baseline Table (foundational — C-14, C-15)
- Entity Inventory (foundational — C-10)
- One exit manifest per pipeline stage (C-04, C-12, C-19)
- Boundary Inventory (C-11, C-17, C-20, C-21, C-22)
- Stale Window / Divergence Window Analysis (C-06)
- Recovery Audit Table (C-08, C-14, C-16, C-18)
- Closure Gate (C-23)

The Failure Mode Prediction Register must appear in the scaffold as T-NN before any
stage trace table entry.

---

### PHASE 0 — FAILURE MODE PREDICTION

*Produce a prediction register of expected LP-NN and NH-NN identifiers for a dual-write
CDX pattern BEFORE tracing any individual stage. Draw on pattern-level knowledge of
dual-write failure modes, not stage-specific discovery.*

**Failure Mode Prediction Register** (T-NN from scaffold)

For a dual-write pipeline pattern with a CDX coordination layer, predict the full set of
expected failure modes before examining any specific stage. Assign LP-NN identifiers to
predicted data loss points and NH-NN identifiers to boundaries likely to lack explicit
error handling.

| Prediction ID | Failure Mode Category | Predicted Location | Domain Impact (Finance terms) | Confidence |
|---------------|----------------------|-------------------|-------------------------------|------------|
| LP-01 | [category e.g., partial commit] | [stage or boundary] | [e.g., "GL accrual recorded but data lake missing — period-end balance sheet divergence"] | HIGH / MEDIUM / LOW |
| LP-02 | ... | ... | ... | ... |
| NH-01 | [no-handling boundary] | [boundary] | [e.g., "silent drop on data lake write timeout — no retry, no alert"] | ... |
| ... | ... | ... | ... | ... |

Minimum: six predictions (mix of LP-NN and NH-NN). For dual-write patterns, predicted
failure categories must include: partial commit (one destination succeeds, other fails),
ordering violation (same entity written to both destinations in different field states),
reconciliation false negative (divergence exists but reconciliation service does not detect
it), and schema drift between write destinations.

After the table, state the DUAL-WRITE RISK SUMMARY: which predicted failure mode carries
the highest Finance-domain impact, and why? (Reference specific Finance consequences:
e.g., "incorrect period-end accrual balance," "auditor-visible GL/lake divergence,"
"SOX reconciliation gap.")

---

### PHASE 1 — INCUMBENT BASELINE AND ENTITY INVENTORY

**Incumbent Baseline** (T-NN from scaffold)

Before this dual-write pipeline existed, GL consolidation was performed manually or via
batch extract-load. Describe that process:

| Step ID | Manual Step | Responsible Actor/Role | Elapsed Time / Frequency |
|---------|-------------|------------------------|--------------------------|
| MS-01 | [step] | [Controller / AP Manager / IT Ops] | [time] |
| MS-02 | ... | ... | ... |

Minimum: five steps specific enough to reference by row. Examples of required specificity:
"MS-02: Controller manually extracts AP accrual journal from Oracle GL using period-end
close template — 3 hours per close cycle." Generic steps ("review transactions") do not
qualify.

State the INCUMBENT TOTAL elapsed time. Declare the GL close SLA: maximum elapsed time
from AP subledger commit to consolidated reporting view refresh that keeps the period-end
close on schedule. This value is the SLA budget for all C-22 SLA% calculations.

**Entity Inventory** (T-NN from scaffold)

Enumerate all in-scope domain entities. Any entity introduced mid-trace without prior
declaration fails C-10.

| Entity Name | Domain Area | Key Fields | Role in Pipeline |
|-------------|-------------|------------|-----------------|

Required entities: APAccrualEntry, CDXWriteToken, GLJournalLine, DataLakeAccrualRecord,
ReconciliationFlag, ConsolidatedReportingRow. Declare Finance-native field names (e.g.,
`APAccrualEntry.accrual_period_YYYYMM`, `GLJournalLine.debit_amount_USD(12,2)`).

---

### PHASE 2 — STAGE TRACE WITH PREDICTION VALIDATION

For each stage, produce a stage table and typed exit manifest. Each stage trace section
MUST explicitly validate or exonerate its relevant PHASE 0 predictions:

- **CONFIRMED**: "LP-02 confirmed at this stage — [specific evidence from stage trace]."
- **EXONERATED**: "LP-04 exonerated — this stage implements [mechanism] which prevents
  the predicted failure mode."
- **NEW**: "LP-07 (NEW, not predicted): [description of newly discovered failure mode]."

Stage table format for each stage:

| Field | Type at Exit | Schema Change from Entry | Data Loss Risk (LP-NN) | Error Handling (NH-NN or mechanism) | Stage Latency |
|-------|-------------|--------------------------|------------------------|-------------------------------------|---------------|

After each stage table, produce a typed exit manifest:

```
EXIT MANIFEST — [Stage Name]: [entity name]
  fields: [count]
  key field assertions:
    [field_name: TYPE(precision)]
    [field_name: TYPE(precision)]
    (minimum three assertions for Finance-critical fields)
```

Stages to trace:
1. AP Subledger Commit — AP system → CDX coordination layer
2. CDX Write Coordinator — coordination layer dispatches simultaneous writes
3. Transactional GL Write — CDX → Oracle Fusion GL
4. Data Lake Ingest — CDX → Azure Synapse data lake
5. Reconciliation Service — period-end divergence detection across both destinations
6. Consolidated Reporting View — unified reporting layer refresh

For the CDX Write Coordinator stage: explicitly address whether the write to Transactional
GL and Data Lake Ingest are strictly atomic, or whether partial commit is possible. Confirm
or exonerate LP-NN predictions related to partial commit.

---

### PHASE 3 — BOUNDARY INVENTORY AND SLA ANALYSIS

**Boundary Inventory with SLA%** (T-NN from scaffold)

Produce the complete boundary inventory. For dual-write, include both write-path boundaries
(B2->3: CDX → GL and B2->4: CDX → Data Lake) as separate rows, not merged.

| Boundary | Error Handling (NH-NN or mechanism) | Entity at Risk (entity.field — risk) | Transport Latency (ms) | Processing Overhead (ms) | Total (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|-------------------------------------|--------------------------------------|------------------------|--------------------------|------------|-------------------|-----------------|
| B1->2 | | | | | | | |
| B2->3 | | | | | | | |
| B2->4 | | | | | | | |
| B3->5 | | | | | | | |
| B4->5 | | | | | | | |
| B5->6 | | | | | | | |

Rules (same as V-01): entity.field notation required; Transport and Processing Overhead
must be independent numeric ms values; SLA% uses the GL close SLA declared in Phase 1.

**DOMINATION POINT**: name the boundary where Cumulative SLA% first crosses 50%, cite the
exact percentage, and explain in one sentence in Finance terms why this boundary dominates
(e.g., "Reconciliation Service processing at B5->6 consumes 63% of the close SLA because
it must perform a full-table GL/lake comparison before the reporting view can refresh").

**Divergence Window Analysis** (T-NN from scaffold)

For a dual-write pattern, the stale window is the maximum divergence window: how long can
the GL and data lake hold different values for the same APAccrualEntry?

- Normal operation: maximum divergence window from simultaneous dispatch to both
  destinations confirming writes
- Failure mode: name the LP-NN identifier, quantify the divergence window, and state the
  Finance consequence (e.g., "GL balance and lake balance show different period accrual
  totals for up to 3 hours — any mid-period management report pulled during this window
  reflects incorrect accrual state")

---

### PHASE 4 — RECOVERY AUDIT AND CLOSURE

**Recovery Audit Table** (T-NN from scaffold)

Produce recovery prescriptions for every NH-NN and LP-NN identifier from the merged
register (PHASE 0 predictions + PHASE 2 confirmed + PHASE 2 new identifiers). Include
exonerated predictions for traceability — mark them "EXONERATED (no recovery needed)."

| Trigger ID | Status | Triggering Condition | Recovery Mechanism | Boundary/Stage | Incumbent Step (MS-NN from T-NN) |
|------------|--------|---------------------|-------------------|----------------|----------------------------------|
| LP-01 | CONFIRMED / EXONERATED / NEW | [condition] | [mechanism] | [location] | [MS-NN step ID and name] |

For CONFIRMED and NEW rows: every recovery row must cite a specific MS-NN step from the
incumbent baseline (C-16 full compliance). "Manual GL reconciliation process" fails — cite
"MS-03: Controller manual GL extract."

**Closure Gate** (T-NN from scaffold)

Forward check: for every LP-NN and NH-NN in the merged register, confirm whether a
recovery row exists. Check against original declarations, not against the recovery table.

| Identifier | Where Declared | Recovery Row Present? | Status |
|------------|---------------|----------------------|--------|
| [LP-NN or NH-NN] | [phase + T-NN] | [YES / NO / EXONERATED] | [CLOSED / OPEN] |

**Pattern Assessment**

Name the integration pattern (dual-write with CDX). Name one alternative (e.g., event
sourcing with CQRS, saga pattern with compensating transactions). Provide at least two
trade-off dimensions, at least one quantified in Finance terms (e.g., "saga pattern
eliminates partial commit risk but adds 180-250 ms per transaction for compensation
coordination — at 5,000 AP accrual commits per close day, this adds 15-20 min to the
close cycle").

---

*Scaffold contract: T-NN tokens from STEP 0 scaffold are the only valid cross-table
citation identifiers. All NH-NN and LP-NN identifiers assigned in PHASE 0 are carried
forward unchanged — identifiers are not renamed or re-assigned between phases.*

---

## V-03 — Explicit Criterion-Tagging

**Variation axis**: Phrasing register / transparency — each prompt section header
explicitly names the C-NN rubric criteria it satisfies. The model is instructed to tag
its output subsections with the criterion IDs they address. The rubric is made partially
visible: the model sees which criteria are being targeted by structural section placement
and explicit labeling, but not the full pass/fail condition text.

**Hypothesis**: Two competing outcomes are plausible. (A) Criterion visibility primes the
model to produce targeted, criterion-aware output that hits all marks cleanly — entity
names are richer because C-07 is explicitly named, field citations more precise because
C-20 is explicitly named. (B) Criterion visibility produces mechanical "checkbox" outputs
— the model satisfies literal pass conditions but organic domain vocabulary degrades:
entity names become generic placeholders and domain framing (C-07) is achieved by
inserting a domain entity name once rather than building a domain-saturated narrative.
R13 seeks to distinguish (A) from (B) using field-name specificity as the proxy.

Scenario: Operations — EDI 856 ASN-to-DC-receiving pipeline. Supplier advance ship
notices flow through EDI validation, DC gate check, QC inspection grading, put-away
assignment, WMS inventory update, and ERP balance sync. The incumbent process was
DC supervisor manual receiving against a paper packing list.
Stages: EDI 856 Receipt → EDI Validation → DC Gate Check → QC Inspection →
Put-Away Assignment → WMS Inventory Update → ERP Balance Sync.

---

You are an Operations data domain expert. You are tracing data through a supplier EDI 856
ASN-to-DC-receiving pipeline. Your role is to produce a structured data flow analysis
covering entity inventory, stage-by-stage schema traces, boundary error handling, latency
analysis, stale window characterization, incumbent baseline documentation, recovery
prescriptions, and closure verification.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

**Output tagging instruction**: Each section of your output should be tagged with the
rubric criterion IDs it addresses. Use the format `[C-NN, C-MM]` at the end of each
section header. For example: `## Entity Inventory [C-07, C-10]`. Tag only criteria that
your output in that section genuinely satisfies — do not tag criteria speculatively.

---

### STEP 0 — Output Table Scaffold [C-24]

Before any domain analysis, declare every table that will appear in this response. The
scaffold is the navigational contract. A table that appears in the body without a scaffold
entry is an undeclared artifact.

Each scaffold row must declare:
- T-NN token (unique identifier for this table)
- Table Name
- Purpose statement: one sentence naming what the table contains AND which C-NN criteria
  it satisfies (e.g., "Typed stage-exit manifest for WMS Inventory Update — satisfies
  C-04, C-12, C-19")
- Upstream Tables: T-NN tokens this table draws from or references

| Table # | Table Name | Purpose (C-NN criteria) | Upstream Tables |
|---------|------------|--------------------------|-----------------|

The scaffold must cover at minimum:
- Incumbent Baseline Table (C-14, C-15)
- Entity Inventory (C-07, C-10)
- Exit manifest per stage — 7 stages means 7 manifest tables (C-04, C-12, C-19)
- Boundary Inventory (C-02, C-11, C-13, C-17, C-20, C-21, C-22)
- Stale Window Analysis (C-05, C-06)
- Recovery Audit Table (C-08, C-14, C-16, C-18)
- Closure Gate (C-23)

---

### Incumbent Baseline [C-14, C-15]

Before this pipeline existed, DC receiving was performed by DC supervisors manually
working against paper packing lists and verbal handoffs from the dock. Document that
process as a table.

| Step ID | Manual Step | Responsible Actor/Role | Elapsed Time / Frequency |
|---------|-------------|------------------------|--------------------------|
| MS-01 | [specific step] | [DC supervisor / QC inspector / etc.] | [time] |

Required: minimum five steps. Each step must be specific enough to cite by MS-NN row
from recovery prescriptions. Example of required specificity: "MS-02: DC receiving
supervisor manually counts carton quantities against EDI 856 line items — 20 min per
pallet." Generic steps ("review inbound shipment") do not qualify.

After the table, state:
- INCUMBENT TOTAL elapsed time (sequential sum)
- DC receiving SLA: maximum elapsed time from EDI 856 arrival to WMS on-hand balance
  update that avoids inventory accuracy degradation. This is the SLA budget for C-22
  SLA% calculations.

*Tag your output: `[C-14, C-15]`*

---

### Entity Inventory [C-07, C-10]

Enumerate all in-scope domain entities before the first stage trace. Use Operations-native
field names drawn from standard warehouse management and EDI data models.

| Entity Name | Domain Area | Key Fields | Role in Pipeline |
|-------------|-------------|------------|-----------------|

Required entities: EDI856ASN, EDIValidationResult, GateCheckRecord, QCGrade,
PutAwayAssignment, WMSInventoryBalance, ERPOnHandBalance.

Field naming must use domain-specific identifiers: `EDI856ASN.ship_unit_count_EA`,
`QCGrade.inspection_disposition_code`, `WMSInventoryBalance.available_qty_EA`.
Generic field names ("id", "status", "count") do not qualify for C-20 field citations.

Also declare the SLA budget value (minutes) established in the incumbent baseline section.

*Tag your output: `[C-07, C-10]`*

---

### Stage Traces [C-01, C-02, C-03, C-04, C-05, C-12, C-19]

For each stage, produce: (1) a stage trace table, (2) a typed exit manifest.

Stage trace table format:

| Field | Type at Exit | Schema Change from Entry | Data Loss Risk (LP-NN) | Error Handling (NH-NN or mechanism) | Stage Latency |
|-------|-------------|--------------------------|------------------------|-------------------------------------|---------------|

Rules:
- Schema change: if unchanged, state "NONE — verified: no field added, removed, renamed,
  or retyped" [satisfies C-12]
- Data loss risk: assign LP-NN with entity name, specific field, specific condition [C-03]
- Error handling: if none, annotate "NH-NN: no handling — risk accepted at [stage]" [C-02]
- Stage latency: numeric value or characterization (real-time / micro-batch) [C-05]

Typed exit manifest format:
```
EXIT MANIFEST — [Stage Name]: [entity name]  [C-04, C-19]
  fields: [count]
  key field assertions:
    [field_name: TYPE(precision)]  ← minimum four assertions
```

*Tag each stage subsection: `[C-01, C-02, C-03, C-04, C-05, C-12, C-19]`*

Stages to trace:
1. EDI 856 Receipt — EDI gateway → validation queue
2. EDI Validation — validation queue → DC gate check staging
3. DC Gate Check — staging → QC inspection queue
4. QC Inspection — QC queue → put-away assignment service
5. Put-Away Assignment — put-away service → WMS inventory update
6. WMS Inventory Update — put-away → WMS balance table
7. ERP Balance Sync — WMS → ERP on-hand balance

---

### Boundary Inventory [C-02, C-11, C-13, C-17, C-20, C-21, C-22]

Produce a complete boundary inventory for all inter-stage handoffs B1->2 through B6->7.
Every cell must have a value. A blank cell is a structural gap [C-13 enforcement point].

| Boundary | Error Handling (NH-NN or mechanism) | Entity at Risk (entity.field — risk) | Transport Latency (ms) | Processing Overhead (ms) | Total (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|-------------------------------------|--------------------------------------|------------------------|--------------------------|------------|-------------------|-----------------|
| B1->2 | | | | | | | |
| B2->3 | | | | | | | |
| B3->4 | | | | | | | |
| B4->5 | | | | | | | |
| B5->6 | | | | | | | |
| B6->7 | | | | | | | |

- Entity at Risk: must be `entity.field_name — risk description` format. Entity name
  only (e.g., "EDI856ASN — at risk") does not qualify for C-20. [C-17, C-20]
- Transport Latency and Processing Overhead: separate numeric ms values. [C-21]
- SLA%: fraction of DC receiving SLA consumed at this boundary; Cumulative SLA% running
  total through this boundary. [C-22]

DOMINATION POINT statement: identify the boundary where Cumulative SLA% first exceeds
50% of the SLA budget. Name the boundary, cite the exact cumulative percentage, and
provide one sentence in Operations terms (e.g., "QC Inspection processing at B3->4
dominates at 58% cumulative because 100% manual inspection disposition is required for
each carton before put-away can begin"). [C-22]

*Tag your output: `[C-02, C-11, C-13, C-17, C-20, C-21, C-22]`*

---

### Stale Window Analysis [C-05, C-06]

Compute accumulated end-to-end latency (EDI 856 Receipt → ERP Balance Sync), showing
Transport and Processing Overhead separately at each boundary step.

- Normal operation staleness: is the ERP on-hand balance fresh relative to the DC
  receiving SLA?
- Failure mode staleness: name it using its LP-NN or NH-NN identifier, quantify the
  stale window, and state what it means operationally (e.g., "ERP shows stale on-hand
  balance for affected ASN lines — replenishment triggers may fire incorrectly for
  48+ hours after physical receipt").

*Tag your output: `[C-05, C-06]`*

---

### Recovery Audit [C-08, C-14, C-16, C-18]

Organize recovery prescriptions for every NH-NN and LP-NN declared in the stage traces
and boundary inventory as a structured table.

| Trigger ID | Triggering Condition | Recovery Mechanism | Boundary/Stage | Incumbent Step Fallback (MS-NN) |
|------------|---------------------|-------------------|----------------|----------------------------------|

Rules:
- Recovery Mechanism: names the specific action at the specific boundary. [C-08]
- Incumbent Step Fallback: cites the specific MS-NN step ID and step name from the
  incumbent baseline. "MS-02: DC supervisor manual carton count" is valid. "Manual
  process" alone fails C-16. [C-14, C-16]
- Every NH-NN and LP-NN must have a row. [C-18]

*Tag your output: `[C-08, C-14, C-16, C-18]`*

---

### Closure Gate [C-23]

Perform a forward check against every NH-NN and LP-NN declared in this response. Derive
the identifier list from stage traces and boundary inventory — not from the recovery table.

| Identifier | Where Declared | Recovery Row Present? | Status |
|------------|---------------|----------------------|--------|
| [NH-NN or LP-NN] | [section + T-NN] | [YES / NO] | [CLOSED / OPEN] |

A count summary does not satisfy this criterion. Per-identifier status is required. [C-23]

*Tag your output: `[C-23]`*

---

### Pattern Assessment [C-09]

Name the integration pattern. Name one alternative with at least two trade-off dimensions,
at least one quantified in Operations/warehouse terms. [C-09]

*Tag your output: `[C-09]`*

---

## V-04 — Commerce-First Role Sequence + Failure-Mode-First Lifecycle

**Variation axes**: Role sequence (Commerce leads) + Lifecycle emphasis (failure-mode
prediction before stage trace). Commerce expert produces both the entity inventory AND
the failure mode prediction register. The hypothesis is that Commerce domain expertise
includes the best knowledge of which catalog and order data quality problems are endemic
to e-commerce fulfillment pipelines — leading with Commerce for failure prediction should
produce more domain-specific LP-NN descriptions (Commerce-native field names and Commerce
failure mode vocabulary) than Operations-owned failure prediction from generic pipeline
pattern knowledge.

**Combined hypothesis**: Commerce-owned failure prediction (H1 + H2) produces LP-NN
identifiers with Commerce-native field citations (C-20 quality) from the prediction phase
itself, before any stage trace occurs — creating a richer pre-committed entity.field
vocabulary in the failure mode register that the stage trace must then validate or refine.
This earlier entity.field commitment in the LP-NN register may produce stronger C-17/C-20
compliance in the boundary inventory than designs where entity.field citations first appear
during stage tracing.

Scenario: Commerce — customer order fulfillment pipeline. Customer orders from the
e-commerce platform flow through OMS validation, fulfillment routing, warehouse pick
authorization, carrier manifest generation, shipment event ingest, and order status update
back to the customer order record.
Stages: Customer Order Receipt → OMS Validation → Fulfillment Routing →
Warehouse Pick Authorization → Carrier Manifest Generation → Shipment Event Ingest →
Order Status Update.

---

You are running a two-role analysis of a customer order fulfillment pipeline. Commerce
domain expert runs first and produces: the failure mode prediction register AND the entity
inventory. Operations domain expert runs second and produces: stage traces (validating
Commerce predictions), boundary inventory, stale window analysis, incumbent baseline,
recovery audit, and closure gate.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

---

### STEP 0 — OUTPUT TABLE SCAFFOLD

Declare every table before producing any domain content. The scaffold row for the Failure
Mode Prediction Register must appear before any stage trace table entry.

| Table # | Table Name | Purpose (criteria satisfied) | Upstream Tables |
|---------|------------|------------------------------|-----------------|
| T-01 | [table name] | [purpose + criteria IDs] | [T-NN or "none"] |
| T-02 | ... | ... | ... |

The Failure Mode Prediction Register and Entity Inventory must both be foundational entries
(upstream = "none" or each other only). Stage trace tables must declare the entity
inventory as upstream. All downstream tables (boundary inventory, recovery audit, closure
gate) must declare their upstream T-NN dependencies completely.

---

### ROLE 1 — COMMERCE DOMAIN EXPERT

#### Phase 0 — Failure Mode Prediction Register (T-NN from scaffold)

Before examining any individual stage, apply Commerce domain knowledge of order
fulfillment pipelines to predict the complete set of expected failure modes. Assign LP-NN
identifiers to predicted data loss points and NH-NN identifiers to expected unhandled
boundaries.

| Prediction ID | Failure Mode | Predicted Location | Commerce Domain Impact | Field-Level Risk (entity.field) | Confidence |
|---------------|-------------|-------------------|----------------------|--------------------------------|------------|
| LP-01 | [Commerce failure category] | [stage or boundary] | [e.g., "Order visible as Processing to customer but not yet routed to warehouse — phantom fulfillment window"] | [e.g., `CustomerOrder.fulfillment_status_code` — risk of stale status for 15+ min] | HIGH / MEDIUM |

Minimum: seven predictions. Must include failure modes endemic to Commerce fulfillment:
- Split-order routing divergence (one multi-line order routed to multiple fulfillment
  centers with no order-level reconciliation)
- Carrier manifest generation failure with no requeue (order line confirmed picked but
  no shipping label generated)
- Shipment event deduplication failure (duplicate tracking events corrupting
  OrderStatusUpdate)
- Order cancellation race condition (customer cancels during pick authorization)
- Inventory reservation expiry without order release

For each prediction, cite the entity.field that carries the risk using the entity
vocabulary you will establish in the entity inventory immediately below.

**COMMERCE RISK SUMMARY**: which prediction carries the highest customer-facing impact?
Quantify if possible (e.g., "LP-03 — carrier manifest failure with no requeue affects
an estimated 0.3% of order lines at peak volume, creating orphaned picked-not-shipped
lines that require manual intervention within the 4-hour ship commitment window").

#### Entity Inventory (T-NN from scaffold)

Enumerate all in-scope domain entities. This inventory is the authority for all entity.field
citations that follow.

| Entity Name | Domain Area | Key Fields | Role in Pipeline |
|-------------|-------------|------------|-----------------|

Required entities: CustomerOrder, OrderLine, OMSValidationResult, FulfillmentRoute,
PickAuthorization, CarrierManifest, ShipmentEvent, OrderStatusRecord.

Use Commerce-native field names: `CustomerOrder.promised_ship_date`,
`OrderLine.allocated_qty_EA`, `CarrierManifest.tracking_number_UPS`,
`FulfillmentRoute.dc_assignment_code`. Generic field names do not qualify.

Also declare the order fulfillment SLA: maximum elapsed time from Customer Order Receipt
to Order Status Update reflecting a shipped status that satisfies the customer's promised
ship date. Express in hours. This is the SLA budget for C-22 SLA% calculations.

---

### ROLE 2 — OPERATIONS DOMAIN EXPERT

#### Stage Traces with Prediction Validation (T-NN entries from scaffold)

For each stage, produce a stage table and typed exit manifest. Each stage section MUST
include an explicit prediction validation block referencing the Commerce prediction register:

```
PREDICTION VALIDATION — [Stage Name]
  Confirmed: [LP-NN / NH-NN] — [evidence from this stage trace]
  Exonerated: [LP-NN / NH-NN] — [mechanism that prevents the predicted failure]
  New (not predicted): [LP-NN / NH-NN] — [description]
```

Stage table format:

| Field | Type at Exit | Schema Change from Entry | Data Loss Risk (LP-NN) | Error Handling (NH-NN or mechanism) | Stage Latency |
|-------|-------------|--------------------------|------------------------|-------------------------------------|---------------|

Typed exit manifest (minimum four field assertions):
```
EXIT MANIFEST — [Stage Name]: [entity]
  fields: [count]
  key field assertions:
    [field_name: TYPE(precision)]
```

Stages to trace:
1. Customer Order Receipt — e-commerce platform → OMS ingest queue
2. OMS Validation — OMS validates line-level inventory allocation
3. Fulfillment Routing — routing engine assigns order lines to DC(s)
4. Warehouse Pick Authorization — WMS receives pick authorization from OMS
5. Carrier Manifest Generation — manifest engine creates carrier labels
6. Shipment Event Ingest — carrier webhook or EDI 214 events ingested
7. Order Status Update — status service updates CustomerOrder and OrderLine

#### Boundary Inventory with SLA% (T-NN from scaffold)

| Boundary | Error Handling (NH-NN or mechanism) | Entity at Risk (entity.field — risk) | Transport Latency (ms) | Processing Overhead (ms) | Total (ms) | SLA% This Boundary | Cumulative SLA% |
|----------|-------------------------------------|--------------------------------------|------------------------|--------------------------|------------|-------------------|-----------------|
| B1->2 | | | | | | | |
| B2->3 | | | | | | | |
| B3->4 | | | | | | | |
| B4->5 | | | | | | | |
| B5->6 | | | | | | | |
| B6->7 | | | | | | | |

Entity at Risk must use entity.field from the upstream exit manifest. SLA% uses the SLA
budget declared by Commerce. After the table, state the DOMINATION POINT.

#### Stale Window Analysis (T-NN from scaffold)

Compute accumulated latency end-to-end. State:
- Normal operation staleness (order status lag vs promised ship date)
- Worst failure mode staleness using LP-NN identifier and Commerce impact terms

#### Incumbent Baseline (T-NN from scaffold)

Before this pipeline, order fulfillment was tracked manually by the operations team using
spreadsheets, email confirmations from warehouse staff, and manual carrier booking.

| Step ID | Manual Step | Responsible Actor/Role | Elapsed Time / Frequency |
|---------|-------------|------------------------|--------------------------|
| MS-01 | [step] | [role] | [time] |

Minimum five steps, specific enough for MS-NN row citation in recovery.

State INCUMBENT TOTAL elapsed time.

#### Recovery Audit Table (T-NN from scaffold)

For every NH-NN and LP-NN in the merged register (Commerce predictions + Operations
stage trace), produce a recovery row.

| Trigger ID | Status | Triggering Condition | Recovery Mechanism | Boundary/Stage | MS-NN Fallback |
|------------|--------|---------------------|-------------------|----------------|----------------|
| [LP-NN / NH-NN] | CONFIRMED / EXONERATED / NEW | [condition] | [mechanism] | [location] | [MS-NN step ID + name] |

All CONFIRMED and NEW rows must cite a specific MS-NN step. EXONERATED rows may leave
MS-NN Fallback blank.

#### Closure Gate (T-NN from scaffold)

Forward check against every LP-NN and NH-NN in the merged register. Derive the list from
the prediction register and stage traces — not from the recovery audit table.

| Identifier | Where Declared | Commerce-Predicted? | Recovery Row? | Status |
|------------|---------------|---------------------|---------------|--------|
| [LP-NN / NH-NN] | [phase + T-NN] | [YES / NO] | [YES / NO / EXONERATED] | [CLOSED / OPEN] |

#### Pattern Assessment

Name the integration pattern. Name one alternative with at least two trade-off dimensions,
at least one quantified in Commerce-domain terms.

---

*Scaffold contract: every cross-table citation uses T-NN tokens from the STEP 0 scaffold.
Commerce prediction LP-NN/NH-NN identifiers are carried forward unchanged into all
subsequent phases — no renaming.*

---

## V-05 — Explicit Criterion-Tagging + Scaffold Authority

**Variation axes**: Explicit criterion-tagging (C-NN IDs in section headers, model tags
its output) + Scaffold Authority design (proven highest-scoring structure from R11 V-01:
STEP 0 scaffold as pre-declared navigational contract, T-NN dependency graph fully
populated before domain content begins).

**Hypothesis**: Adding criterion transparency to the proven highest-scoring design (R11
V-01, 17/17 aspirational) either (A) preserves 17/17 while making the criterion-output
mapping explicitly verifiable — each scaffold row tags C-NN criteria, each body section
tags C-NN criteria, creating a dual-layer auditable contract — or (B) introduces checkbox
degradation in organic framing sections (C-07, C-09), where domain vocabulary is deployed
instrumentally to satisfy a named criterion rather than emerging from domain immersion.
If (A), criterion-tagging is a structural reinforcement that could strengthen weaker prompt
designs. If (B), it exposes a fundamental tension between rubric-visible design and organic
domain quality that prior rounds have not tested.

Scenario: Operations — warehouse replenishment trigger pipeline. Sales velocity signals
from the e-commerce platform flow through demand signal aggregation, replenishment
calculation, purchase order generation, EDI 850 supplier dispatch, PO acknowledgment
receipt, and receiving schedule update to the DC receiving calendar.
Stages: Sales Velocity Ingest → Demand Signal Aggregation → Replenishment Calculation →
PO Generation → EDI 850 Dispatch → PO Acknowledgment Receipt → Receiving Schedule Update.

---

You are an Operations data domain expert running a structured data flow analysis of a
warehouse replenishment trigger pipeline. Sales velocity signals drive demand calculations
that generate purchase orders, dispatch them to suppliers via EDI 850, receive PO
acknowledgments, and update the DC receiving calendar.

**Inputs**

- Topic: `{{topic}}`
- Signal: `{{signal}}`

**Criterion-tagging instruction**: This prompt is organized around evaluation criteria.
Each section header lists the criterion IDs it targets. When you produce output for a
section, tag the header of your output with the same criterion IDs in brackets
(e.g., `## Entity Inventory [C-07, C-10]`). Tag only criteria your output in that section
genuinely satisfies. Do not tag a criterion speculatively.

---

### STEP 0 — Output Table Scaffold [C-24]

**SCAFFOLD AUTHORITY RULE**: Every table that will appear in this response must be
declared in this scaffold before any domain content begins. A table that appears for the
first time in the body without a scaffold entry is a SCAFFOLD VIOLATION and fails C-24.
No exceptions.

Each scaffold row must declare:

| Table # | Table Name | Purpose (C-NN criteria this table satisfies) | Upstream Tables (T-NN tokens) |
|---------|------------|-----------------------------------------------|-------------------------------|
| T-01 | [name] | [one sentence + C-NN list: e.g., "Typed exit manifest for Sales Velocity Ingest stage — C-04, C-12, C-19"] | [T-NN list or "none"] |
| T-02 | ... | ... | ... |

**Minimum scaffold entries required:**

Foundational (no upstream dependencies):
- Incumbent Baseline Table (C-14, C-15)
- Entity Inventory (C-07, C-10)
- Failure Mode Prediction placeholder (C-03) — optional but strongly recommended

Stage exit manifests (one per stage — 7 stages = 7 manifest T-NN entries):
- Each declares C-04, C-12, C-19
- Upstream = entity inventory T-NN

Mid-tier tables (reference entity inventory + exit manifests):
- Boundary Inventory Table (C-02, C-11, C-13, C-17, C-20, C-21, C-22)
  upstream = all 7 exit manifest T-NN tokens
- Stale Window Analysis (C-05, C-06)
  upstream = boundary inventory T-NN

Terminal tables (reference all prior):
- Recovery Audit Table (C-08, C-14, C-16, C-18)
  upstream = boundary inventory T-NN + incumbent baseline T-NN
- Closure Gate (C-23)
  upstream = recovery audit T-NN + boundary inventory T-NN

The C-NN column in the scaffold is the primary audit surface for criterion-tagging.
Every C-NN listed in a scaffold row must be legibly satisfied by the content of that table
in the body. A scaffold row citing C-20 whose body table contains entity-name-only
citations (no entity.field format) is a criterion-tagging integrity failure.

---

### Incumbent Baseline [C-14, C-15]

Before this pipeline, warehouse replenishment was managed manually by the demand planning
team using sales reports, spreadsheets, and phone/email communication with suppliers.

| Step ID | Manual Step | Responsible Actor/Role | Elapsed Time / Frequency |
|---------|-------------|------------------------|--------------------------|
| MS-01 | [step] | [Demand Planner / Procurement Analyst / DC Manager] | [time] |

Minimum five steps with specificity sufficient for MS-NN row citation:
"MS-03: Procurement analyst manually creates PO in ERP from demand planner's replenishment
list — 8 min per SKU, batch of 40-60 SKUs per planning run." Generic steps do not qualify.

State: INCUMBENT TOTAL elapsed time; Replenishment SLA (maximum elapsed time from sales
velocity signal ingestion to confirmed supplier PO acknowledgment within the purchasing
lead time window — express in hours; this is the SLA budget for C-22).

---

### Entity Inventory [C-07, C-10]

Enumerate all in-scope domain entities. This inventory is the sole authority for all
entity.field citations. An entity or field introduced mid-trace without prior declaration
is a structural gap.

| Entity Name | Domain Area | Key Fields | Role in Pipeline |
|-------------|-------------|------------|-----------------|

Required entities: SalesVelocitySignal, DemandAggregate, ReplenishmentPlan, PurchaseOrder,
POLine, EDI850Message, POAcknowledgment, ReceivingScheduleEntry.

Use Operations-native field names: `SalesVelocitySignal.rolling_7d_units_sold_EA`,
`ReplenishmentPlan.reorder_qty_EA`, `PurchaseOrder.po_number_alphanumeric`,
`POAcknowledgment.supplier_confirmed_ship_date`. Generic field names fail C-20.

Declare the Replenishment SLA value (hours) established in the incumbent baseline.

---

### Stage Traces [C-01, C-02, C-03, C-04, C-05, C-12, C-19]

For each stage, produce: (1) stage trace table, (2) typed exit manifest.

**Stage trace table** [C-01, C-02, C-03, C-04, C-05, C-12]:

| Field | Type at Exit | Schema Change | Data Loss Risk (LP-NN) | Error Handling (NH-NN or mechanism) | Stage Latency |
|-------|-------------|---------------|------------------------|-------------------------------------|---------------|

Schema change: if unchanged, state "NONE — verified: no field added, removed, renamed,
or retyped" [C-12]. LP-NN must name entity, specific field, specific condition [C-03].
NH-NN: "NH-NN: no handling — risk accepted at [stage]" [C-02].

**Typed exit manifest** [C-04, C-12, C-19]:
```
EXIT MANIFEST — [Stage Name] [T-NN from scaffold]: [entity]
  fields: [count]
  key field assertions:
    [field_name: TYPE(precision)]   ← minimum four assertions
```

The T-NN token in the manifest header must match the scaffold entry exactly.

Stages to trace:
1. Sales Velocity Ingest — e-commerce analytics → demand signal queue
2. Demand Signal Aggregation — demand signal queue → replenishment engine
3. Replenishment Calculation — replenishment engine → PO generation service
4. PO Generation — PO generation service → ERP purchase order records
5. EDI 850 Dispatch — ERP → supplier EDI gateway
6. PO Acknowledgment Receipt — EDI gateway ← supplier acknowledgment
7. Receiving Schedule Update — acknowledgment service → DC receiving calendar

---

### Boundary Inventory [C-02, C-11, C-13, C-17, C-20, C-21, C-22]

Complete boundary inventory covering B1->2 through B6->7.
**C-13 enforcement**: every cell must have a value. A blank cell is a structurally visible
gap.

| Boundary | Error Handling [C-02] | Entity at Risk [C-17, C-20] | Transport Latency ms [C-21] | Processing Overhead ms [C-21] | Total ms | SLA% [C-22] | Cumulative SLA% [C-22] |
|----------|----------------------|-----------------------------|-----------------------------|-----------------------------|----------|-------------|------------------------|
| B1->2 | | | | | | | |
| B2->3 | | | | | | | |
| B3->4 | | | | | | | |
| B4->5 | | | | | | | |
| B5->6 | | | | | | | |
| B6->7 | | | | | | | |

**C-20 requirement** [column "Entity at Risk"]: every cell must use `entity.field_name —
risk description` format citing a field from the upstream exit manifest T-NN. Entity name
only fails. The T-NN in the upstream manifest header must be resolvable from the scaffold.

**C-21 requirement**: Transport Latency and Processing Overhead are independent numeric ms
values. "Negligible" fails. Sum must account for Total.

**DOMINATION POINT** [C-22]: name the boundary where Cumulative SLA% first crosses 50%
of the Replenishment SLA budget, cite the exact percentage, and provide one sentence in
Operations/procurement terms.

---

### Stale Window Analysis [C-05, C-06]

Compute accumulated latency from Sales Velocity Ingest to Receiving Schedule Update.
Show Transport and Processing Overhead separately per boundary.

- Normal operation staleness vs Replenishment SLA
- Failure-mode staleness: LP-NN or NH-NN identifier, quantified stale window in hours,
  Operations impact (e.g., "stockout risk for affected SKUs if supplier is not notified
  within the replenishment lead time window")

---

### Recovery Audit [C-08, C-14, C-16, C-18]

| Trigger ID | Triggering Condition | Recovery Mechanism | Boundary/Stage | Incumbent Step Fallback (MS-NN) |
|------------|---------------------|-------------------|----------------|----------------------------------|

All CONFIRMED rows: specific MS-NN step ID from incumbent baseline (T-NN). "Manual
process" alone fails C-16. "MS-03: Procurement analyst manual PO creation" is valid.
Every NH-NN and LP-NN must have exactly one row [C-18].

---

### Closure Gate [C-23]

Forward check: derive the identifier list from stage traces and boundary inventory —
not from the recovery audit table.

| Identifier | Where Declared (T-NN) | Recovery Row Present? | Status |
|------------|----------------------|----------------------|--------|
| [NH-NN / LP-NN] | [section + T-NN] | [YES / NO] | [CLOSED / OPEN] |

Count summaries do not satisfy C-23. Per-identifier status required.

---

### Pattern Assessment [C-09]

Name the integration pattern. Name one alternative with at least two trade-off dimensions,
at least one quantified in Operations/procurement terms.

---

*SCAFFOLD AUTHORITY ENFORCEMENT: the scaffold produced in STEP 0 is the sole navigation
contract. Every T-NN token cited in the body must resolve to a scaffold row. Every C-NN
tag in the body must correspond to criteria genuinely satisfied by the tagged section — the
scaffold's C-NN column is the audit surface. Cross-table citations that cannot be resolved
from the scaffold are SCAFFOLD VIOLATIONS.*
