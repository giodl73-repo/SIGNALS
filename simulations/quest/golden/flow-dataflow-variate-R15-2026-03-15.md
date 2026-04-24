# flow-dataflow — Round 15 Variations (Rubric v12)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v12 (C-01 through C-28, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

R15 targets the two criteria added in v12 from R14 evidence:

**C-27 — FM-NN resolution section scaffold pre-registration**: R14 V-02 declared the
resolution section as a named T-NN artifact in the STEP 0 scaffold, earning C-24 PASS.
R14 V-03 described its resolution section post-trace without scaffold pre-registration,
earning C-24 PARTIAL. C-27 makes this gap independently scorable. All R15 variations
pre-declare the resolution section in the scaffold with explicit purpose text identifying
it as the "FM-NN lifecycle resolution audit" and citing its dependency on the prediction
register.

**C-28 — Inline FM-NN stage acknowledgment with deferred resolution**: R14 V-03 introduced
inline acknowledgments during stage traces — each FM-NN whose anticipated event intersects
a stage boundary is acknowledged inline with a deferral statement. V-02 produced no inline
acknowledgments. C-28 rewards the deferred-acknowledgment discipline. All R15 variations
include inline FM-NN acknowledgments with explicit deferral; the key variable is *how*
the acknowledgment is structured (prose note, table row, or embedded sub-bullet).

**What R14 established:**

- Scaffold pre-registration of the FM-NN resolution section (C-27) is achievable by a
  single scaffold row naming T-07 as "FM-NN lifecycle resolution audit" with dependency
  on T-02 (prediction register).
- Inline deferred acknowledgments (C-28) work best when the deferral statement names both
  the specific boundary or condition touched AND the section identifier to which resolution
  is deferred — e.g., "FM-02: intersects B2->3 type-coercion boundary — resolution
  deferred to Section 8 (FM-NN Resolution Audit)."
- Multi-role designs (R14 V-01, V-04) that pre-assign stages in the scaffold produce
  cleaner C-04/C-19 coverage because each stage has a designated producer for its exit
  manifest.
- Boundary-first scaffold layout (C-11 declared before stage traces) ensures C-20
  entity.field citations have manifest field names to reference from the first stage.

**R15 hypothesis space:**

**H1 — Phase-gated lifecycle with explicit completion guards (V-01)**
Each lifecycle phase is a named gate with a mandatory completion check before proceeding.
The model must declare phase completion ("PHASE 1 COMPLETE — all pre-trace tables
declared") before entering the next phase. Hypothesis: explicit phase guards prevent
the most common failure pattern — partial C-26 prediction registers and missing inline
C-28 acknowledgments — by creating structural pressure to complete each phase in full
before the next begins. Prediction: C-26 and C-28 compliance improves; risk is that
phase-gate overhead increases response length without improving domain framing (C-07).

**H2 — Maximum table density with inline acknowledgment log (V-02)**
Every section uses table format. Inline FM-NN acknowledgments (C-28) are not prose notes
within stage trace blocks but rows appended to a running "Inline Acknowledgment Log" table
that accumulates across all stages. The resolution section (C-26, C-27) consumes the log
as input. Hypothesis: a running log table prevents acknowledgments from being omitted
mid-trace (C-28 is enforced by table structure, not prose discipline); the log also makes
the "accumulated evidence" model for C-28's deferred-resolution rationale structurally
visible. Prediction: highest C-28 completeness of any R15 variation; risk is that table
rows feel mechanical rather than domain-grounded (C-07 degradation).

**H3 — Commerce → Operations → Finance role sequence (V-03)**
Three named roles, each assigned a pipeline stage slice via STEP 0 stage assignment map.
Commerce Domain Expert runs first (entity model, source schema, extract-side manifests).
Operations Analyst runs second (transform, sync, CDC boundary mechanics). Finance
Controller runs third (load, reconciliation, SLA budget, domination point, recovery
audit). C-28 inline acknowledgments appear within each role's assigned stage trace
blocks; C-27 requires the scaffold to register the resolution section before Commerce's
first stage trace begins. Hypothesis: domain-native field names (SKU.unit_cost,
Invoice.approval_status, LedgerEntry.posting_date) appear earlier in exit manifests when
Commerce leads — improving C-20 citation vocabulary in downstream roles.

**H4 — Inertia framing + lifecycle emphasis (V-04)**
The incumbent baseline table is the first substantive output — produced before the
pipeline is named or described. The pipeline is introduced as "the replacement for
the process in T-01." Every subsequent phase references incumbent step IDs. Lifecycle
phases are preserved from V-01 but framed around the before/after narrative arc:
PHASE 0 (baseline), PHASE 1 (scaffold), PHASE 2 (pipeline trace), PHASE 3 (failure
resolution), PHASE 4 (recovery grounded in baseline steps). Hypothesis: baseline-first
framing maximizes C-14/C-15/C-16 compliance because the incumbent process vocabulary
is established before recovery prescriptions are written; all recovery entries then
cite specific step IDs rather than category-level process names.

**H5 — Conversational register + list-heavy format + compressed lifecycle (V-05)**
Direct second-person imperative phrasing throughout — "Do this," "Your job now is,"
"List each stage." Inline stage traces use bullet lists rather than sub-tables. The
lifecycle is compressed to a single numbered checklist with no phase labels. Hypothesis:
compressed format preserves structural compliance (C-27, C-28 inline acknowledgments)
while producing more concise domain framing; tests whether the phase-gate scaffold
pattern from V-01 is necessary for C-26/C-28 compliance or whether a checklist contract
achieves the same result with less overhead.

---

## V-01 — Lifecycle Emphasis (Phase-Gated Sequential Gates)

**Axis**: Lifecycle emphasis — six sequential phases with explicit completion guards.
Each phase is a named gate. The model declares phase completion before proceeding.
**Hypothesis**: phase guards prevent partial C-26 registers and missing C-28 inline
acknowledgments by creating structural pressure to complete each gate in full.

---

```
You are a Finance / Operations / Commerce data domain expert. You will produce a
complete data flow trace for the following pipeline:

{topic}

Work through the six phases below in strict sequence. Declare each phase complete before
beginning the next. Every section header is mandatory output.

---

## PHASE 1 — OUTPUT SCAFFOLD

Before writing any domain content, declare every table and section that will appear in
your response. This scaffold is the navigational contract. Any table that appears for
the first time after Stage 1 begins is an undeclared artifact. Use the following table
structure, adding rows for any additional tables you introduce:

| # | Table / Section Name | Purpose | Dependencies |
|---|---------------------|---------|--------------|
| T-01 | Entity Inventory | All in-scope domain entities with key fields | — |
| T-02 | Failure Mode Prediction Register | Pre-trace FM-NN failure mode predictions | — |
| T-03 | Stage Enumeration | Named and sequenced pipeline stages | — |
| T-04 | Boundary Inventory | Inter-stage boundaries: labels, entity-at-risk, latency decomposition, SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation operational process (step-level, three columns minimum) | — |
| T-06 | Stage Trace Blocks | Per-stage schema entry/exit, typed exit manifests, error handling, loss points, FM-NN inline acknowledgments | T-01, T-02, T-04, T-05 |
| T-07 | FM-NN Resolution Audit | FM-NN lifecycle resolution audit: CONFIRMED / EXONERATED / NEW status for every FM-NN from T-02, resolved after all stage traces complete | T-02, T-06 |
| T-08 | Recovery Audit Table | NH-NN / LP-NN triggering condition → recovery mechanism → boundary/stage → incumbent step citation | T-04, T-05, T-06 |
| T-09 | Closure Gate | Per-identifier CLOSED / OPEN status: every NH-NN and LP-NN mapped to its T-08 row | T-08 |

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert.

**PHASE 1 COMPLETE when**: T-01 through T-09 rows declared, no table appears
post-scaffold. Declare: "PHASE 1 COMPLETE."

---

## PHASE 2 — PRE-TRACE DECLARATIONS

Produce the following four tables in order. No stage trace may begin until all four
are complete.

### 2.1 Entity Inventory (T-01)

List every in-scope domain entity. Stage traces may only reference entities declared here.
Use domain entity names (Invoice, PurchaseOrder, SKU, LedgerEntry, etc.) — not generic
labels.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

### 2.2 Failure Mode Prediction Register (T-02)

Before tracing any stage, predict every anticipated failure mode. Minimum 3 entries.
Each FM-NN entry declares a prediction identifier, the specific anticipated event,
the domain-specific consequence (quantified or qualified), and the expected designation
if the prediction materializes. FM-NN identifiers are resolved only in T-07 (Phase 5)
after all stage traces are complete — not during traces.

During Phase 3 stage traces, every FM-NN whose anticipated event intersects a stage
boundary must carry an inline acknowledgment: record the FM-NN identifier, the specific
boundary or condition touched, and an explicit deferral statement naming T-07 as the
resolution target. Do not commit to CONFIRMED / EXONERATED / NEW status inline.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

### 2.3 Stage Enumeration (T-03)

Name and sequence every pipeline stage. A stage referenced in traces but absent here fails.

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

### 2.4 Boundary Inventory (T-04)

For every inter-stage boundary, complete all columns. "Negligible" is not a valid latency
value; use a numeric estimate in ms. Transport Latency and Processing Overhead are
independent columns — their sum equals Total. Entity at Risk must name a specific entity
from T-01 (not "data" or "records"). The field-level annotation (entity.field_name) is
added after Stage Exit Manifests are available in Phase 3 — leave a stub reference here
and complete the field annotation as a back-fill after the first manifest that covers this
boundary is produced.

| Boundary | From Stage | To Stage | Entity at Risk (entity.field — add after manifests) | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|------------------------------------------------------|---------------|-----------------|-----------|-----------|-----------------|

**DOMINATION POINT**: After completing the table, state the single boundary where
cumulative SLA% first exceeds 50% of the total SLA budget, the exact cumulative
percentage at that boundary, and one sentence explaining why this boundary dominates
(reference the specific domain operation that consumes the budget).

**PHASE 2 COMPLETE when**: T-01, T-02, T-03, T-04 fully populated. Declare:
"PHASE 2 COMPLETE."

---

## PHASE 3 — INCUMBENT BASELINE

Before tracing any pipeline stage, document the pre-automation process that this pipeline
replaces. This is the first artifact in the recovery chain: every recovery prescription in
T-08 will cite a specific Step ID from this table.

### Incumbent Baseline (T-05)

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 rows. Step IDs must be referenceable (MS-01, MS-02, etc.) — downstream
T-08 citations must name a specific Step ID, not a process category.

**PHASE 3 COMPLETE when**: T-05 has ≥4 rows with named Step IDs. Declare:
"PHASE 3 COMPLETE."

---

## PHASE 4 — STAGE TRACES (T-06)

Produce one trace block per stage from T-03. Use the exact structure below.

---

### Stage [Stage ID]: [Stage Name]

**Schema entry**: Describe field set entering this stage. If this is Stage 1, describe
the source schema. Otherwise, diff from prior stage exit manifest: list fields added,
removed, renamed, or retyped. If no schema change: state
"verified: no field added, removed, renamed, or retyped."

**Typed exit manifest** (T-06 sub-artifact — referenced by boundary entity.field stubs
in T-04 and by entity-at-risk annotations in T-08):

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary [B-NN->NN] error handling**: [Named mechanism] OR
[NH-NN — no handling — risk accepted: {specific risk description}]

**Data loss point**: LP-NN — [specific named scenario tied to this stage; not generic]

**Latency**: [value in ms, range, or characterization: real-time / micro-batch / hourly / daily]

**Stale data window**: Normal operation: [quantified window]. Failure mode: [separate
quantified window — not the same as normal operation].

**Active domain entities** (from T-01): [entity names]

**FM-NN inline acknowledgments**:
For every FM-NN from T-02 whose anticipated event intersects this stage's boundary or
processing:
- [FM-NN]: intersects [specific boundary label or processing condition] — resolution
  deferred to T-07 (FM-NN Resolution Audit, Phase 5)
If no FM-NN from T-02 intersects this stage: state "No T-02 predictions intersect
this stage."

---

After all stage traces, complete the entity.field stubs in T-04 using field names from
the typed exit manifests.

**PHASE 4 COMPLETE when**: all T-03 stages traced, all exit manifests produced, T-04
entity.field stubs filled in. Declare: "PHASE 4 COMPLETE."

---

## PHASE 5 — POST-TRACE RESOLUTION

### 5.1 Pattern Trade-Off

Name one alternative architecture pattern for this pipeline type. State ≥2 trade-off
dimensions comparing it to the current pattern — at least one dimension quantified or
expressed in domain terms (e.g., "eliminates the 15-minute reconciliation window at
cost of 200ms additional CDC latency per SKU update").

### 5.2 Recovery Audit Table (T-08)

One row per NH-NN and LP-NN from Phase 4. A missing row is a visible gap. Every row
must cite a specific Step ID from T-05 as its incumbent baseline fallback — category-
level process names (e.g., "manual review") without a Step ID do not qualify.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | T-05 Step ID Citation |
|-----|----------|---------------------|--------------------|-----------------|----------------------|

### 5.3 FM-NN Resolution Audit (T-07)

Resolve every FM-NN from T-02. Exactly one status per entry. This section is the
designated resolution target for all inline deferral statements from Phase 4.

| FM-NN | Status | Evidence / Reason |
|-------|--------|------------------|

Status rules:
- CONFIRMED: prediction materialized — must cite the specific NH-NN or LP-NN it produced
- EXONERATED: prediction did not materialize — must state the specific reason it was absent
- NEW: emerged during trace without prior prediction — must be assigned NH-NN or LP-NN
  retroactively with a formal identifier

**PHASE 5 COMPLETE when**: T-08 has one row per NH-NN and LP-NN; T-07 has one row
per FM-NN with status and evidence. Declare: "PHASE 5 COMPLETE."

---

## PHASE 6 — CLOSURE GATE (T-09)

Produce a per-identifier status table. Every NH-NN and LP-NN declared in Phase 4 must
appear. This section is structurally separate from T-08 and from all stage trace blocks.
A summary count ("N of M rows covered") does not satisfy this requirement — a per-
identifier row is required.

| Identifier | Source (Stage / Boundary) | T-08 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching row found in T-08. OPEN = no matching row — this is an explicit gap
that must be explained or addressed.

**PHASE 6 COMPLETE when**: all NH-NN and LP-NN identifiers appear, no OPEN status
is unexplained. Declare: "TRACE COMPLETE."
```

---

## V-02 — Output Format: Maximum Table Density with Inline Acknowledgment Log

**Axis**: Output format — every section uses table format. Inline FM-NN acknowledgments
(C-28) are collected into a running "Inline Acknowledgment Log" table that accumulates
rows across all stage traces rather than appearing as prose notes within each stage block.
**Hypothesis**: a running log table prevents acknowledgments from being omitted mid-trace
and makes accumulated evidence structurally visible before the resolution audit commits.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete
data flow trace for:

{topic}

All output is structured as named tables. Prose is limited to one-sentence transitions
between tables. Every section below is mandatory.

---

## STEP 0: Output Scaffold

| T# | Table Name | Purpose | Depends On |
|----|-----------|---------|-----------|
| T-01 | Entity Inventory | In-scope domain entities: name, description, key fields | — |
| T-02 | Failure Mode Prediction Register | Pre-trace FM-NN predictions: event, domain consequence, expected designation | — |
| T-03 | Stage Enumeration | Pipeline stages: ID, name, description | — |
| T-04 | Boundary Inventory | Boundaries: label, stages, entity at risk, entity.field, transport ms, processing ms, total ms, SLA% this, cumulative SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process: Step ID, step name, responsible role, elapsed time | — |
| T-06 | Stage Exit Manifests | One sub-table per stage: field_name, TYPE(precision), notes | T-03 |
| T-07 | Inline Acknowledgment Log | Running FM-NN acknowledgments during stage traces: FM-NN, stage ID, boundary/condition, deferral statement | T-02, T-03 |
| T-08 | FM-NN Resolution Audit | FM-NN lifecycle resolution audit: FM-NN, status (CONFIRMED/EXONERATED/NEW), evidence — resolves all T-07 entries post-trace | T-02, T-07 |
| T-09 | Recovery Audit Table | NH-NN/LP-NN → recovery mechanism → boundary/stage → T-05 step citation | T-04, T-05, T-06 |
| T-10 | Closure Gate | Per-identifier CLOSED/OPEN status: every NH-NN and LP-NN mapped to T-09 row | T-09 |

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert. Single-role designs satisfy C-25 by default.

---

## T-01: Entity Inventory

| Entity | Description | Key Fields |
|--------|-------------|-----------|

Entities not listed here may not appear in stage traces or manifests.

---

## T-02: Failure Mode Prediction Register

Minimum 3 entries. FM-NN identifiers are resolved in T-08 only — not during stage traces.
During stage traces, FM-NN entries that intersect a stage boundary are logged in T-07
(one row per intersection); T-07 rows carry a deferral statement naming T-08.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

## T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

## T-04: Boundary Inventory

The entity.field column references field names from T-06 exit manifests. Populate
entity.field after the relevant stage manifest is produced (back-fill). "Negligible"
is not a valid latency value.

| Boundary | From | To | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------|------|----------------|-------------|---------------|-----------------|-----------|-----------|-----------------|

**DOMINATION POINT** (one row): The boundary where cumulative SLA% first exceeds 50%.

| Domination Boundary | Exact Cumulative SLA% | Justification (one sentence, domain-grounded) |
|--------------------|-----------------------|----------------------------------------------|

---

## T-05: Incumbent Baseline

The pre-automation process this pipeline replaces. Recovery prescriptions in T-09
must cite specific Step IDs from this table.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

## Stage Traces

For each stage in T-03, produce the following table set. Use "Stage [ID]: [Name]" as
the section header.

### Stage [Stage ID]: [Stage Name]

**Schema diff** (one-sentence prose): [Fields added / removed / renamed / retyped
vs. prior stage exit manifest. If no change: "verified: no field added, removed,
renamed, or retyped."]

**T-06.[Stage ID] — Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Stage Boundary Annotation Table**:

| Boundary | Error Handling (mechanism or NH-NN label) | Data Loss Point (LP-NN label) | Latency | Normal Stale Window | Failure-Mode Stale Window |
|----------|------------------------------------------|------------------------------|---------|--------------------|--------------------------:|

**Active entities** (from T-01): [names, comma-separated]

After completing the Boundary Annotation Table for this stage, append any relevant
FM-NN intersections to T-07:

*T-07 rows appended this stage*:

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|--------------------|
| [FM-NN] | [Stage ID] | [specific boundary label or processing condition] | Resolution deferred to T-08 (FM-NN Resolution Audit) |

If no T-02 predictions intersect this stage, append one row: "No T-02 intersections
at [Stage ID]."

---

*(Repeat the stage block above for every stage in T-03.)*

---

## T-07: Inline Acknowledgment Log (Consolidated)

After all stage traces, present the full consolidated T-07 table collecting all rows
appended during stage traces. This table is the input consumed by T-08.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|--------------------|

---

## Pattern Trade-Off

| Alternative Pattern | Trade-Off Dimension 1 | Trade-Off Dimension 2 (quantified or domain-qualified) |
|--------------------|-----------------------|-------------------------------------------------------|

---

## T-09: Recovery Audit Table

One row per NH-NN and LP-NN. Missing rows are visible gaps. T-05 Step ID citation
is mandatory — category-level process names without a Step ID do not qualify.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | T-05 Step ID |
|-----|----------|---------------------|--------------------|-----------------|-------------|

---

## T-08: FM-NN Resolution Audit

Consumes T-07. Resolves every FM-NN from T-02 using cross-stage evidence accumulated
in T-07. One row per FM-NN. Status rules:

| FM-NN | Status | T-07 Entries Consulted | Evidence / Reason |
|-------|--------|-----------------------|------------------|

- CONFIRMED: cites specific NH-NN or LP-NN produced
- EXONERATED: states specific reason failure mode was absent
- NEW: assigns NH-NN or LP-NN retroactively with formal identifier

---

## T-10: Closure Gate

Per-identifier status. Every NH-NN and LP-NN from stage traces must appear.
Summary counts do not satisfy this requirement.

| Identifier | Source Stage / Boundary | T-09 Row | Status |
|-----------|------------------------|----------|--------|

OPEN = no corresponding T-09 row. Every OPEN entry must be explained.
```

---

## V-03 — Role Sequence: Commerce → Operations → Finance (Multi-Role)

**Axis**: Role sequence — three named roles with explicit stage assignments and hand-off
boundaries. Commerce Domain Expert leads (entity model, source extraction). Operations
Analyst handles transform and sync stages. Finance Controller owns load, reconciliation,
SLA budget, and post-trace artifacts.
**Hypothesis**: Commerce-first sequencing produces richer C-20 entity.field citations
because Commerce-native field names (SKU.list_price, PurchaseOrder.approval_status) are
established in exit manifests before Operations and Finance write boundary annotations.

---

```
This trace is performed by three named domain experts in sequence. Each expert produces
output only for their assigned stages, as declared in the STEP 0 stage assignment map.

Topic: {topic}

---

## STEP 0: Output Scaffold (produced before any role begins tracing)

### Scaffold Table

| T# | Table / Section Name | Purpose | Depends On |
|----|---------------------|---------|-----------|
| T-01 | Entity Inventory | All in-scope domain entities | — |
| T-02 | Failure Mode Prediction Register | Pre-trace FM-NN predictions with expected designations | — |
| T-03 | Stage Enumeration | Named, sequenced pipeline stages | — |
| T-04 | Boundary Inventory | Inter-stage boundaries with latency decomposition, entity-at-risk, SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process: Step ID, role, elapsed time | — |
| T-06 | Stage Trace Blocks | Per-stage schema, typed exit manifests, error handling, loss points, FM-NN inline acknowledgments | T-01, T-02, T-04 |
| T-07 | FM-NN Resolution Audit | FM-NN lifecycle resolution audit: status for every FM-NN from T-02 after all stage traces complete | T-02, T-06 |
| T-08 | Recovery Audit Table | NH-NN/LP-NN → mechanism → boundary/stage → T-05 Step ID citation | T-04, T-05, T-06 |
| T-09 | Closure Gate | Per-identifier CLOSED/OPEN status for all NH-NN and LP-NN | T-08 |

### Stage-to-Role Assignment Map

Every stage from T-03 must appear in this map. A stage absent from this map has no
designated manifest producer.

| Stage ID | Stage Name | Assigned Role |
|----------|------------|--------------|

Complete this table after T-03 is produced. Roles:
- Commerce Domain Expert: source extraction and Commerce-side schema stages
- Operations Analyst: transformation, sync, and CDC stages
- Finance Controller: load, ledger posting, reconciliation, and reporting stages

---

## STEP 1: Pre-Trace Declarations (all roles contribute, Commerce leads)

### T-01: Entity Inventory

*Led by Commerce Domain Expert — Operations and Finance annotate as needed.*

| Entity | Description | Key Fields (domain-native names) |
|--------|-------------|----------------------------------|

### T-02: Failure Mode Prediction Register

*All three roles contribute predictions from their domain perspective.*

Minimum 3 entries (at least one per role). FM-NN identifiers are resolved in T-07
(post-trace) only. During stage traces, FM-NN intersections are acknowledged inline
with explicit deferral to T-07 — no resolution status committed during traces.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation | Predicting Role |
|-------|------------------|--------------------|---------------------|----------------|

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

After T-03, complete the Stage-to-Role Assignment Map in STEP 0.

### T-04: Boundary Inventory

*Operations Analyst owns latency decomposition. Finance Controller owns SLA%.
Commerce Domain Expert annotates entity-at-risk field names after exit manifests.*

| Boundary | From | To | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------|------|----------------|-------------|---------------|-----------------|-----------|-----------|-----------------|

**DOMINATION POINT**: [boundary, exact cumulative SLA%, one-sentence Finance-grounded
justification: how does this boundary's budget share impact close-cycle or reporting SLA?]

### T-05: Incumbent Baseline

*Finance Controller leads — documents the manual process replaced by this pipeline.*

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

## STEP 2: Commerce Domain Expert — Assigned Stages

*Trace only the stages assigned to Commerce in the Stage-to-Role Assignment Map.*

For each assigned stage, produce:

**Stage [ID]: [Name]** *(Commerce Domain Expert)*

**Schema entry**: [source schema description or diff from prior exit manifest]

**Typed exit manifest** (T-06.[ID]):
| field_name | TYPE(precision) | Commerce Notes |
|------------|-----------------|----------------|

**Boundary [B-NN->NN] error handling**: [mechanism] or [NH-NN — no handling — risk
accepted: {Commerce-specific risk: e.g., SKU not found in catalog, PurchaseOrder without
approval status}]

**Data loss point**: LP-NN — [Commerce-specific scenario: which entity, which field,
under what extraction condition]

**Latency**: [value or characterization]

**Stale window**: Normal: [window]. Failure mode: [separate window — Commerce impact].

**Active entities** (from T-01): [names]

**FM-NN inline acknowledgments**:
- [FM-NN]: intersects [boundary/condition in this stage] — resolution deferred to T-07
  (FM-NN Resolution Audit)
If none: "No T-02 predictions intersect this stage."

---

## STEP 3: Operations Analyst — Assigned Stages

*Trace only the stages assigned to Operations in the Stage-to-Role Assignment Map.
Back-fill entity.field stubs in T-04 for boundaries covered by Commerce exit manifests.*

For each assigned stage, use the same structure as STEP 2:
- Schema entry / diff / verification assertion
- Typed exit manifest (T-06.[ID])
- Boundary error handling (NH-NN labels)
- Data loss point (LP-NN labels)
- Latency annotation
- Stale window (normal vs. failure-mode)
- Active entities
- FM-NN inline acknowledgments with explicit deferral to T-07

Back-fill remaining T-04 entity.field stubs using Operations-stage exit manifest
field names.

---

## STEP 4: Finance Controller — Assigned Stages

*Trace only the stages assigned to Finance in the Stage-to-Role Assignment Map.*

For each assigned stage, use the same structure as STEP 2 and STEP 3.

After completing all Finance stage traces, back-fill any remaining T-04 entity.field
stubs using Finance-stage exit manifest field names.

---

## STEP 5: Post-Trace Resolution (Finance Controller leads, all roles validate)

### Pattern Trade-Off

Name one alternative pipeline pattern. State ≥2 trade-off dimensions — at least one
quantified or qualified in Finance / Commerce / Operations domain terms.

### T-08: Recovery Audit Table

*Finance Controller produces T-08. Operations Analyst validates mechanism feasibility.
Commerce Domain Expert validates entity.field citations.*

One row per NH-NN and LP-NN from all stage traces. T-05 Step ID citation mandatory.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | T-05 Step ID |
|-----|----------|---------------------|--------------------|-----------------|-------------|

### T-07: FM-NN Resolution Audit

*All three roles contribute evidence. Finance Controller owns the resolution table.*

Resolves every FM-NN from T-02. One row per FM-NN. Resolution uses cross-stage
evidence accumulated across STEP 2, 3, and 4 traces.

| FM-NN | Status | Predicting Role | NH-NN / LP-NN Cited or Reason Exonerated | Notes |
|-------|--------|----------------|------------------------------------------|-------|

Status rules:
- CONFIRMED: cites specific NH-NN or LP-NN
- EXONERATED: states reason the failure mode was absent in the pipeline
- NEW: assigns NH-NN or LP-NN retroactively

### T-09: Closure Gate

Per-identifier table. Every NH-NN and LP-NN from all role traces must appear.

| Identifier | Source Role / Stage | T-08 Row | Status |
|-----------|--------------------|---------|--------------------|

OPEN = no T-08 row. Every OPEN entry must name the role responsible for resolution.
```

---

## V-04 — Inertia Framing + Lifecycle Emphasis

**Axes**: (1) Incumbent baseline is the first substantive artifact — the pipeline is
introduced as "the replacement" for the manual process documented in PHASE 1.
(2) Lifecycle phases frame the before/after narrative: PHASE 1 (baseline), PHASE 2
(scaffold + pipeline declaration), PHASE 3 (trace), PHASE 4 (failure resolution),
PHASE 5 (recovery grounded in baseline steps).
**Hypothesis**: baseline-first framing maximizes C-14/C-15/C-16 compliance because
all recovery entries are written after the incumbent process vocabulary is established.

---

```
You are a Finance / Operations / Commerce data domain expert. Your task is to trace
data flow through a pipeline — but before introducing the pipeline, you will first
document the manual process it replaces. The pipeline is the replacement. Recovery
paths return to that manual process.

Topic: {topic}

Work through the phases below in order. Do not describe the automated pipeline until
PHASE 2 has established the incumbent baseline.

---

## PHASE 1 — INCUMBENT BASELINE

Before naming the automated pipeline, document the pre-automation process that existed
in this domain. This process is the default recovery fallback for every failure mode
the pipeline encounters.

### T-01: Incumbent Baseline

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 5 rows. Step IDs must be individually referenceable (IB-01, IB-02, etc.)
from recovery prescriptions. "Manual review" without a named role and process step
does not qualify as a row.

**Incumbent process summary** (two sentences): What manual workflow did this domain
run before the pipeline? What was its primary operational rhythm (daily batch, hourly
reconciliation, on-demand)?

**PHASE 1 COMPLETE when**: T-01 has ≥5 named rows. Declare: "PHASE 1 COMPLETE."

---

## PHASE 2 — PIPELINE DECLARATION AND SCAFFOLD

Now introduce the automated pipeline as the replacement for the T-01 baseline process.

### 2.1 Output Scaffold

Declare every table that will appear in your response. T-01 is already declared above.

| T# | Table / Section Name | Purpose | Depends On |
|----|---------------------|---------|-----------|
| T-01 | Incumbent Baseline | [already produced in PHASE 1] | — |
| T-02 | Entity Inventory | In-scope domain entities | — |
| T-03 | Failure Mode Prediction Register | Pre-trace FM-NN predictions | — |
| T-04 | Stage Enumeration | Named and sequenced pipeline stages | — |
| T-05 | Boundary Inventory | Inter-stage boundaries with latency decomposition, entity-at-risk, SLA% | T-04 |
| T-06 | Stage Trace Blocks | Per-stage schema, typed exit manifests, error handling, loss points | T-02, T-03, T-05 |
| T-07 | FM-NN Resolution Audit | FM-NN lifecycle resolution audit: CONFIRMED / EXONERATED / NEW for every FM-NN, resolved post-trace using cross-stage evidence | T-03, T-06 |
| T-08 | Recovery Audit Table | NH-NN/LP-NN → mechanism → boundary/stage → T-01 incumbent step citation | T-05, T-06 |
| T-09 | Closure Gate | Per-identifier CLOSED/OPEN status for all NH-NN and LP-NN | T-08 |

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert.

### 2.2 Entity Inventory (T-02)

| Entity | Description | Key Fields |
|--------|-------------|-----------|

### 2.3 Failure Mode Prediction Register (T-03)

Predict failure modes through the lens of the incumbent baseline: what manual safeguards
existed in T-01 that the automated pipeline may lack? Each FM-NN states the anticipated
event, the domain consequence (quantified or qualified), and the expected designation.
Minimum 3 entries.

FM-NN identifiers are resolved in T-07 (PHASE 4) only. During stage traces, FM-NN
intersections receive inline acknowledgments with explicit deferral to T-07.

| FM-NN | Anticipated Event | Domain Consequence | T-01 Manual Safeguard at Risk | Expected Designation |
|-------|------------------|--------------------|-------------------------------|---------------------|

### 2.4 Stage Enumeration (T-04)

| Stage ID | Stage Name | Description | Replaces T-01 Step(s) |
|----------|------------|-------------|----------------------|

The "Replaces T-01 Step(s)" column links each pipeline stage to the manual steps it
automates. A stage with no corresponding T-01 step is a net-new capability.

### 2.5 Boundary Inventory (T-05)

| Boundary | From | To | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------|------|----------------|-------------|---------------|-----------------|-----------|-----------|-----------------|

"Negligible" is not a valid latency value. entity.field back-filled after stage manifests.

**DOMINATION POINT**: [boundary, exact cumulative SLA%, one-sentence justification
framed in terms of what the incumbent process took for the equivalent step in T-01]

**PHASE 2 COMPLETE when**: Scaffold declared, T-02 through T-05 complete.
Declare: "PHASE 2 COMPLETE."

---

## PHASE 3 — STAGE TRACES (T-06)

For each stage in T-04, produce a trace block. Frame each trace against the T-01 step(s)
it replaces: what manual safeguard is now automated, and where does the automation
introduce new failure exposure that the manual step did not have?

---

### Stage [Stage ID]: [Stage Name]

**Replaces T-01 steps**: [IB-NN, IB-NN — the manual steps this stage automates]

**Automation gap**: [What manual safeguard from those T-01 steps is NOT replicated
by this stage? This is the primary failure exposure introduced by automation.]

**Schema entry**: [describe or diff from prior stage]

**Typed exit manifest** (T-06.[ID]):
| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

If schema unchanged from prior stage: "verified: no field added, removed, renamed,
or retyped."

**Boundary [B-NN->NN] error handling**: [mechanism] OR
[NH-NN — no handling — risk accepted: {specific risk}]

**Data loss point**: LP-NN — [specific scenario]

**Latency**: [value or characterization]

**Stale window**: Normal: [window]. Failure mode: [separate quantified window].

**Active entities** (from T-02): [names]

**FM-NN inline acknowledgments**:
- [FM-NN]: intersects [boundary/condition] — resolution deferred to T-07 (PHASE 4)
If none: "No T-03 predictions intersect this stage."

---

After all stage traces, back-fill entity.field in T-05 using manifest field names.

**PHASE 3 COMPLETE when**: all T-04 stages traced, all exit manifests produced.
Declare: "PHASE 3 COMPLETE."

---

## PHASE 4 — FAILURE RESOLUTION AND RECOVERY

### 4.1 Pattern Trade-Off

Name one alternative pipeline pattern. State ≥2 trade-off dimensions — at least one
framed in terms of the incumbent baseline: how does the alternative compare to the
manual process in T-01 on recovery speed or operational cost?

### 4.2 Recovery Audit Table (T-08)

One row per NH-NN and LP-NN. Every row cites a specific T-01 Step ID as the incumbent
fallback. Category-level names ("manual reconciliation") without a specific IB-NN
citation do not qualify.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | T-01 Step ID | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-------------|-----------------|

The Recovery Framing column states: "Revert to [IB-NN Step Name] performed by
[Responsible Role] at [frequency]."

### 4.3 FM-NN Resolution Audit (T-07)

Resolves every FM-NN from T-03 using cross-stage evidence accumulated during PHASE 3
traces. This section is the designated resolution target for all inline deferral
statements.

| FM-NN | Status | T-01 Safeguard That Confirmed or Exonerated | Evidence |
|-------|--------|--------------------------------------------|----------|

Status rules:
- CONFIRMED: cites specific NH-NN or LP-NN produced
- EXONERATED: states reason absent (often: the pipeline retained the manual safeguard
  from T-01 step IB-NN, or the failure mode requires a condition not present in this domain)
- NEW: assigns NH-NN or LP-NN retroactively

**PHASE 4 COMPLETE when**: T-08 has one row per NH-NN/LP-NN; T-07 has one row per
FM-NN. Declare: "PHASE 4 COMPLETE."

---

## PHASE 5 — CLOSURE GATE (T-09)

Per-identifier status check. Every NH-NN and LP-NN declared in PHASE 3 must appear.
A summary count does not satisfy this requirement.

| Identifier | Source Stage / Boundary | T-08 Row | Status |
|-----------|------------------------|----------|--------|

OPEN = no T-08 row. OPEN entries are explicit gaps. Each OPEN entry must name the
T-01 step that would have caught this failure in the manual process.

**TRACE COMPLETE.**
```

---

## V-05 — Combined: Conversational Register + List-Heavy Format + Compressed Lifecycle

**Axes**: (1) Direct second-person imperative phrasing throughout — "Your first job,"
"Do not skip," "List each stage now." (2) Inline stage traces use bullet lists for
schema diffs and annotations rather than sub-tables. (3) Lifecycle is compressed to a
single numbered checklist — all phases present but no phase-gate declarations.
**Hypothesis**: a checklist contract can achieve C-26/C-28 structural compliance without
the overhead of phase-gate declarations; tests whether compressed format degrades domain
framing (C-07) or whether the imperative register compensates.

---

```
You are a Finance / Operations / Commerce data domain expert. Your job is to trace
data through the pipeline described below and produce a complete evidence record.

Topic: {topic}

Follow these steps in order. Do not skip steps. Do not proceed to Step 3 until Step 2
is done.

---

### Step 1: Declare your output tables

Before writing any domain content, list every table you will produce. Your output table
list is the navigational contract — any table you produce that is not on this list is
an undeclared artifact.

| T# | Name | What it does | Needs |
|----|------|--------------|-------|
| T-01 | Entity Inventory | Names every in-scope entity and its key fields | — |
| T-02 | Failure Mode Predictions | Pre-trace FM-NN predictions: event, domain consequence, expected designation | — |
| T-03 | Stage List | Every pipeline stage, named and sequenced | — |
| T-04 | Boundary Map | Every inter-stage boundary: label, entity at risk, entity.field, transport ms, processing ms, total ms, SLA% this, cumulative SLA% | T-03 |
| T-05 | Manual Baseline | The pre-automation process this pipeline replaces: Step ID, step name, role, elapsed time | — |
| T-06 | Stage Traces | Per-stage: schema entry/exit, typed exit manifest, error handling, loss points, FM-NN inline acknowledgments | T-01, T-02, T-04 |
| T-07 | FM-NN Resolution | FM-NN lifecycle resolution audit: CONFIRMED / EXONERATED / NEW for every FM-NN from T-02, produced after all traces | T-02, T-06 |
| T-08 | Recovery Table | NH-NN/LP-NN → mechanism → boundary/stage → T-05 step citation | T-04, T-05, T-06 |
| T-09 | Closure Check | Every NH-NN and LP-NN: CLOSED or OPEN | T-08 |

Single-role design. All stages belong to you.

---

### Step 2: Fill in your pre-trace tables

**T-01 — Entity Inventory**: List every domain entity you'll reference. Use real
entity names — Invoice, SKU, PurchaseOrder, LedgerEntry, InventoryCount, etc. Not
"record" or "item."

| Entity | Description | Key Fields |
|--------|-------------|-----------|

**T-02 — Failure Mode Predictions**: Before you trace a single stage, predict your
failure modes. Write at least 3 FM-NN entries now. You'll resolve each one in T-07
after all traces are done — not before.

During each stage trace, if a T-02 prediction intersects that stage's boundary or
processing, you must write an inline acknowledgment: "FM-NN: touches [specific
boundary or condition] — resolution deferred to T-07." That's it — no status
decision yet. Evidence accumulates across stages before you resolve anything.

| FM-NN | What could go wrong | Domain impact | Expected label (NH-NN or LP-NN) |
|-------|--------------------|--------------|---------------------------------|

**T-03 — Stage List**: Name every pipeline stage in order.

| Stage ID | Stage Name | What it does |
|----------|------------|-------------|

**T-04 — Boundary Map**: Every inter-stage boundary gets a row. Break latency into
Transport and Processing — no aggregate-only column, no "negligible." Entity at risk:
a real entity name, not "data." Entity.field: fill this in after you've produced the
relevant stage exit manifest (back-fill is fine).

| Boundary | From | To | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------|------|----------------|-------------|---------------|-----------------|-----------|-----------|-----------------|

After the table: state your DOMINATION POINT — the boundary where cumulative SLA%
first tops 50%. Name it, cite the exact percentage, one sentence why it dominates.

**T-05 — Manual Baseline**: Document the manual process this pipeline replaced. You'll
cite specific Step IDs (MB-01, MB-02, etc.) in T-08 recovery prescriptions.

| Step ID | Step Name | Responsible Role | How often / how long |
|---------|-----------|-----------------|---------------------|

---

### Step 3: Trace each stage

For every stage in T-03, write a trace block. Use this format:

**[Stage ID]: [Stage Name]**

- **Schema entry**: What fields arrive at this stage? (For Stage 1: source schema. For
  later stages: diff from prior exit manifest — list added/removed/renamed/retyped
  fields. If nothing changed: write exactly "verified: no field added, removed, renamed,
  or retyped.")
- **Exit manifest** — T-06.[Stage ID]:
  | field_name | TYPE(precision) | Notes |
  |------------|-----------------|-------|
- **[B-NN->NN] error handling**: Name the mechanism, OR write
  "[NH-NN] — no handling — risk accepted: [specific risk]"
- **Data loss point**: [LP-NN] — [specific scenario — not "errors may occur"]
- **Latency**: [value, range, or one of: real-time / micro-batch / hourly / daily]
- **Stale window**: Normal: [window duration]. Failure mode: [separate, quantified]
- **Active entities** (from T-01): [list]
- **FM-NN check**: For each FM-NN from T-02 that intersects this stage:
  - [FM-NN]: touches [boundary label or specific condition] — resolution deferred to T-07
  If nothing from T-02 intersects this stage: write "No T-02 predictions touch this stage."

---

### Step 4: Write your post-trace analysis

**Pattern trade-off**: Name one alternative pipeline pattern. Give 2+ trade-off
dimensions — at least one in concrete domain terms (latency numbers, stale window
duration, reconciliation cost).

**T-08 — Recovery Table**: One row for each NH-NN and LP-NN you produced in Step 3.
Missing rows are visible gaps. Every row needs a T-05 Step ID citation — not a
category name.

| NH/LP ID | What triggered it | Recovery mechanism | Boundary / Stage | T-05 Step ID |
|----------|------------------|--------------------|-----------------|-------------|

**T-07 — FM-NN Resolution**: Now resolve every FM-NN from T-02. Use the cross-stage
picture you built in Step 3 — that's why you deferred. One row per FM-NN.

| FM-NN | Status | Evidence |
|-------|--------|----------|

- CONFIRMED: cite the specific NH-NN or LP-NN it produced
- EXONERATED: state the specific reason the failure mode didn't materialize
- NEW: assign it an NH-NN or LP-NN identifier right now

---

### Step 5: Close it out

**T-09 — Closure Check**: Every NH-NN and LP-NN from your stage traces gets a row.
No summaries — a per-identifier table.

| Identifier | Where it came from | T-08 row | CLOSED or OPEN |
|-----------|--------------------|----------|----------------|

OPEN means no T-08 row exists. If you have OPEN entries, state what's needed to close
them.

You're done.
```

---

*End of R15 Variations*
