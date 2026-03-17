# flow-dataflow — Round 18 Variations (Rubric v15)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v15 (C-01 through C-37, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

R18 targets the three criteria added in v15 from R17 evidence:

**C-35 — Phase gate PG-NN pre-registration**: R17 V-01 declared gate tables in the
scaffold under PG-NN identifiers, converting gate blocks into referenceable artifacts.
The compliance risk C-35 introduces: a gate block that satisfies C-34 structurally
(table with Required Table / Population Status / Go/No-Go columns) but has no PG-NN
entry in the scaffold is an undeclared artifact. The PG-NN name is the identifier that
permits C-23 and C-16 to cite the gate by name rather than by position. R17 V-01 satisfied
C-35 by pre-declaring PG-01–PG-04 in the scaffold; R17 V-02 through V-05 produced named
gates but did not all include PG-NN scaffold entries. All R18 variations pre-declare every
gate under a PG-NN identifier in the scaffold.

**C-36 — Count parity verification gate**: R17 V-02 introduced a running total annotation
in the per-stage checkpoint ("N rows this stage, M total in T-07 as of Stage X") and a
Phase 3 gate count-chain check. C-36 makes the cross-stage arithmetic gate independently
scorable: the gate must be a separate pre-declared artifact (not a sentence, not a gate
column, not a per-stage note), it must enumerate each per-stage count by stage identifier,
show the arithmetic, and issue GO/FLAG. The key gap in R17: V-02's count chain verification
was embedded in PG-03 as a column annotation, not as a standalone named table. C-36 requires
T-PARITY (or equivalent) to be pre-declared in the scaffold as its own row — the arithmetic
gate must be independently citable. All R18 variations declare T-PARITY as a standalone
scaffold artifact.

**C-37 — Structural compliance command register (CMD-NN)**: R17 V-03 introduced a CMD
register with explicit DO NOT prohibitions. C-37 requires: (1) the CMD register is a
named table (not a prose checklist), (2) each entry carries CMD-NN identifier, positive
imperative, and DO NOT prohibition, and (3) the CMD register is pre-declared in the C-24
scaffold. The key gap in R17 V-03: the CMD register was declared at the top of the prompt
but some variations did not register it in the scaffold itself. A CMD register that appears
before the scaffold but is not listed in the scaffold's T-NN inventory is an undeclared
artifact under C-24's navigational contract. All R18 variations pre-declare the CMD
register in the scaffold.

---

**What R17 established:**

- PG-NN gate table pre-declaration in scaffold (V-01) converts gate blocks from
  structural elements into independently citable artifacts. Gate tables absent from
  the scaffold are undeclared artifacts under C-24.
- Running count chain in checkpoint annotation (V-02) makes per-stage accumulation
  verifiable, but the count chain embedded in a gate column does not satisfy C-36 —
  a separate T-PARITY table is required.
- CMD register with DO NOT prohibitions (V-03) achieves C-37 when the register is a
  table with CMD-NN identifiers and the register is pre-declared in the scaffold.
- Two-role handoff gate (V-04) satisfies C-34 for the role boundary but not for all
  inter-phase gates unless every phase has a corresponding PG-NN gate.
- Inertia-first framing (V-05) maximizes C-14/C-15/C-16 but does not structurally
  force C-35/C-36/C-37 compliance.

---

**R18 hypothesis space:**

**H1 — CMD register as scaffold's first declared artifact (V-01)**
The CMD register is the first entry in the scaffold table (before T-01) and the first
table produced in the response. The scaffold uses "CMD" or "T-00" as the identifier.
Every subsequent scaffold row carries a "CMD Binding" column linking it to the CMD-NN
entries that govern its production. Hypothesis: declaring the CMD register before all
T-NN artifacts creates forward pressure — every T-NN table the scaffold subsequently
declares inherits a named CMD obligation before a single stage trace begins.

**H2 — Per-phase parity accumulation in PG-NN + standalone T-PARITY (V-02)**
Each PG-NN gate table carries a "T-07 Running Total" column that verifies the cumulative
checkpoint sum at that phase boundary. A standalone T-PARITY table appears after all stage
traces with full per-stage enumeration and the sum assertion. PG-03's T-07 Running Total
column is the per-phase verification; T-PARITY is the final arithmetic artifact. Hypothesis:
per-phase running totals in gate tables catch accumulation drift at each phase boundary
(not just post-trace), making C-36's T-PARITY finding retroactively verifiable against
the per-phase audit trail already established in PG-NN.

**H3 — Three-role sequence (Finance → Operations → Commerce) with role-owned CMD slices (V-03)**
Finance Controller, Operations Analyst, and Commerce Data Analyst each own a CMD slice
pre-declared in the scaffold. The stage assignment map assigns every stage to exactly one
role. Role handoff gates serve as PG-NN phase gates. Each role's gate verifies its CMD
slice before handing off to the next role. Hypothesis: role-specific CMD slices eliminate
assignment ambiguity — a CMD breach is attributable to a named role, and each role's gate
enforces its own slice before the handoff. This creates three independent C-37 enforcement
points rather than one post-hoc audit.

**H4 — Conversational register + inertia-first with CMD anchored to IB-NN steps (V-04)**
The incumbent baseline (T-IB) is produced in Section 0 before the scaffold is declared.
The CMD register entries in the DO NOT prohibition column explicitly reference IB-NN step
identifiers (e.g., "DO NOT write a recovery mechanism row without citing IB-03 or another
IB-NN step"). The framing is narrative ("walk through") rather than imperative. Hypothesis:
anchoring CMD prohibitions to IB-NN identifiers that already exist converts the incumbent
baseline from an optional depth marker into a contract anchor that the CMD register enforces
— a recovery row missing an IB-NN citation is simultaneously a C-16 violation and a
named CMD breach.

**H5 — Scaffold three-way binding: CMD + PG-NN + T-PARITY simultaneously declared
with criterion annotation (V-05)**
The scaffold includes a "Satisfies Criterion" column. The CMD register entry annotates
C-37, every PG-NN entry annotates C-35, and T-PARITY annotates C-36. PG-NN entries
carry a compound "Tables Checked | CMD Commands Enforced" field binding each gate to
the CMD entries that govern its production. A cross-reference consistency check in PG-03
verifies that every CMD entry corresponding to a table in Phase 3 is satisfied. Hypothesis:
making the criterion-to-artifact mapping explicit in the scaffold converts rubric compliance
from an evaluator's inference task into a structural verification task — an evaluator
confirms C-35 by reading the scaffold's PG-NN rows, C-36 by reading T-PARITY's scaffold
entry, and C-37 by reading CMD's scaffold entry, without needing to inspect trace content.

---

## V-01 — Output Format: CMD Register First in Scaffold

**Axis**: Output format — the CMD-NN structural compliance register is declared as the
scaffold's first artifact (before T-01) and produced as the first table in the response.
Every subsequent scaffold entry carries a "CMD Binding" field linking it to the CMD-NN
entries that govern its production. PG-NN gate tables and T-PARITY are pre-declared in
the scaffold as full citizens alongside T-NN output tables.
**Hypothesis**: declaring CMD before T-01 makes the meta-contract the structural anchor
for all downstream table declarations — every T-NN artifact commits to a named CMD
obligation before stage traces begin, converting structural shortfalls from oversight
into named CMD breaches that can be cited without re-reading the prompt.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for the following pipeline:

{topic}

STRUCTURAL RULE: The CMD-NN Structural Compliance Register is the first entry in your
scaffold and the first table produced in your response. No T-NN table may be declared
in the scaffold before the CMD entry. Every table you subsequently produce is bound to
a named CMD-NN entry. A CMD breach is any structural shortfall citable by CMD identifier.

Every table in your response must be pre-declared in STEP 0. A table first appearing
after STEP 0 is an undeclared artifact. Use exact column names as declared in the
Mandatory Columns (exact names) column — column names in produced tables must match
scaffold declarations.

---

## STEP 0: Output Scaffold

The scaffold's first row is the CMD register. All T-NN, PG-NN, and T-PARITY entries
follow. The CMD Binding column links each row to the CMD-NN entries that govern it.

| T# | Table Name | Purpose | Mandatory Columns (exact names) | CMD Binding | Depends On |
|----|-----------|---------|----------------------------------|-------------|------------|
| CMD | Structural Compliance Register | Meta-contract pre-declared before all T-NN; every structural shortfall is a named CMD breach | CMD ID, Positive Imperative, DO NOT Prohibition | — | — |
| T-01 | Entity Inventory | Domain entities; all stage traces reference only entities declared here | Entity, Description, Key Fields | CMD-07 | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure hypotheses; resolved in T-09 only | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | CMD-03 | — |
| T-03 | Stage Enumeration | Named and sequenced pipeline stages | Stage ID, Stage Name, Description | CMD-08 | — |
| T-04 | Boundary Inventory | Inter-stage boundaries with latency decomposition, entity-at-risk, and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | CMD-09, CMD-10, CMD-11 | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process; IB-NN step identifiers cited in T-10 | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | CMD-13 | — |
| T-06 | Stage Exit Manifests | One typed manifest per stage; authority for entity.field back-fill in T-04 | field_name, TYPE(precision), Notes | CMD-05 | T-03 |
| T-07 | FM-NN Append-Log | Accumulating per-stage rows appended during trace blocks; count verified per stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | CMD-04 | T-02, T-03 |
| T-08 | SLA Domination Point | Standalone domination boundary — separate from T-04 | Domination Boundary, Exact Cumulative SLA%, Justification | CMD-12 | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution audit | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | CMD-03 | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN/LP-NN recovery with IB-NN step citations | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage | CMD-13, CMD-14 | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status for every NH-NN and LP-NN | Identifier, Source (Stage / Boundary), T-10 Row, Status | CMD-15 | T-10 |
| T-PARITY | Count Parity Gate | Cross-stage arithmetic parity verification; separate from all per-stage checkpoints | Stage ID, N Rows This Stage, Running Total, GO / FLAG | CMD-06 | T-07 |
| PG-01 | Phase 1 Gate | CMD register completeness and scaffold validation | Required Artifact, Declaration Status, CMD Binding Status, Go/No-Go | CMD-01, CMD-16 | CMD, T-01–T-11, T-PARITY |
| PG-02 | Phase 2 Gate | Pre-trace table population before Stage 1 | Required Table, Population Status, Go/No-Go | CMD-01, CMD-16 | T-01–T-05, T-08 |
| PG-03 | Phase 3 Gate | Stage trace completeness and T-07 checkpoint verification | Required Artifact, Completion Status, Go/No-Go | CMD-01, CMD-04, CMD-16 | T-03, T-06, T-07 |
| PG-04 | Phase 4 Gate | Post-trace resolution completeness including T-PARITY | Required Table, Population Status, Go/No-Go | CMD-01, CMD-06, CMD-16 | T-09, T-10, T-11, T-PARITY |

Phase gates registered (C-35):
- PG-01 closes Phase 1: CMD completeness + scaffold declaration check.
- PG-02 closes Phase 2: pre-trace table population check.
- PG-03 closes Phase 3: stage trace completeness + T-07 checkpoint sum.
- PG-04 closes Phase 4: post-trace resolution + T-PARITY arithmetic verified.

Stage assignment: single-role design — C-25 satisfied by default.

---

## PHASE 1: CMD REGISTER AND SCAFFOLD VALIDATION

### CMD: Structural Compliance Register

Produce this table first. Every subsequent structural shortfall is citable by CMD ID.
The CMD Binding column in the scaffold maps each T-NN artifact to the CMD-NN entries
that govern its production.

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in the scaffold before Phase 1 gate runs | DO NOT produce a gate block with no corresponding PG-NN scaffold entry |
| CMD-02 | Label the scaffold's column contract field as "Mandatory Columns (exact names)" | DO NOT label column contracts as "Key Columns," "Required Fields," or any descriptive variant |
| CMD-03 | Produce T-02 FM-NN Prediction Register before any stage trace; resolve in T-09 only | DO NOT write a resolution status (CONFIRMED / EXONERATED / NEW) inline during stage traces |
| CMD-04 | Append T-07 rows during each stage trace block as table rows; close with CHECKPOINT | DO NOT embed FM-NN acknowledgments as prose bullets within stage sections |
| CMD-05 | Produce one T-06 typed exit manifest per stage; back-fill T-04 entity.field after | DO NOT state schema state in prose without typed field assertions |
| CMD-06 | Produce T-PARITY as a standalone named table with per-stage enumeration and arithmetic | DO NOT substitute a prose sentence or PG-NN gate column for T-PARITY |
| CMD-07 | List all in-scope domain entities in T-01 before Stage 1; references bind to T-01 names | DO NOT introduce an entity during stage traces that was not declared in T-01 |
| CMD-08 | Enumerate all pipeline stages in T-03 before Stage 1 trace | DO NOT reference a stage in trace content that has no T-03 entry |
| CMD-09 | Label every inter-stage boundary B[N]->[N+1] in T-04 | DO NOT reference a boundary by stage names without the B[N]->[N+1] label |
| CMD-10 | Decompose boundary latency into Transport (ms) and Processing (ms) as separate columns | DO NOT use a single aggregate "Boundary Latency" column; "Negligible" is not a valid value |
| CMD-11 | Annotate entity.field for every T-04 boundary using field names from T-06 manifests | DO NOT use "data," "records," or "payload" as entity-at-risk identifiers |
| CMD-12 | Produce T-08 SLA Domination Point as a standalone table separate from T-04 | DO NOT embed the domination point as a prose note or footnote appended to T-04 |
| CMD-13 | Produce T-05 Incumbent Baseline with IB-NN Step IDs before writing any T-10 rows | DO NOT write recovery framing without citing a specific IB-NN step from T-05 |
| CMD-14 | Cite a specific IB-NN Step ID in every T-10 row under "IB-NN Step Cited" | DO NOT name the process category only; "IB-03" not "AP reconciliation process" |
| CMD-15 | Produce T-11 Closure Gate with one row per NH-NN and LP-NN identifier | DO NOT substitute an aggregate count ("N of M covered") for per-row CLOSED / OPEN status |
| CMD-16 | Close each phase with a named gate block (PG-NN) listing all expected tables | DO NOT advance to the next phase until all PG-NN gate rows show GO |
| CMD-17 | Close each stage trace block: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended" | DO NOT omit the [N] row count from the checkpoint statement |
| CMD-18 | Declare CMD register as the first row of the scaffold, before T-01 | DO NOT produce the CMD register without a corresponding scaffold entry |

---

### PG-01: Phase 1 Gate

Verify CMD register completeness and scaffold declaration status.

| Required Artifact | Declaration Status | CMD Binding Status | Go/No-Go |
|------------------|--------------------|--------------------|---------|
| CMD register (CMD-01 through CMD-18, table format) | | | |
| T-01 through T-11 declared with Mandatory Columns (exact names) | | | |
| T-PARITY declared as standalone scaffold row (not embedded in PG-NN) | | | |
| PG-01 through PG-04 declared with PG-NN identifiers in scaffold | | | |
| Scaffold column labeled "Mandatory Columns (exact names)" — not "Key Columns" | | | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

List every in-scope domain entity before Stage 1. Use Finance / Operations / Commerce
domain vocabulary: Invoice, PurchaseOrder, LedgerEntry, VendorInvoice, SKU,
InventoryRecord, ShipmentAdvice, CostCenter, GLAccount, RevenueEvent, etc. Stage traces
reference only entity names declared in this table. An entity introduced mid-trace that
has no T-01 row is a CMD-07 breach.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register

Declare all anticipated failure modes before Stage 1. Minimum 3 entries. The Expected
Designation column names the NH-NN or LP-NN identifier this prediction will produce if
it materializes. Resolve in T-09 only — inline stage acknowledgments use T-07 rows only.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

Name and sequence every pipeline stage. A stage referenced in traces but absent from
T-03 is an undeclared stage (CMD-08 breach).

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

Produce all columns for every inter-stage boundary. Rules:
- "Negligible" is not a valid latency value — use numeric ms estimates (CMD-10).
- Transport (ms) and Processing (ms) are independent; their sum equals Total (ms).
- Entity at Risk: a specific T-01 entity name — not "data" or "records" (CMD-11).
- entity.field: leave stub "→ back-fill from T-06.[Stage ID]" until manifest exists.
- Boundary label: B[N]->[N+1] format (B1->2, B2->3, etc.) (CMD-09).
- SLA%: compute from stated total pipeline SLA budget.

After completing T-04, add footnote: "Domination analysis: see T-08."

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-08: SLA Domination Point

Produced immediately after T-04 as a standalone table. CMD-12 prohibits embedding
inside T-04 or appending as a prose note. Cross-referenceable from T-04 footnote and
from T-06 latency totals.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. B[N]->[N+1] label from T-04. Cumulative SLA% is the exact percentage at the
boundary where running total first exceeds 50% of the SLA budget. Justification: one
sentence naming the specific domain operation driving the domination.

---

### T-05: Incumbent Baseline

Document the pre-automation operational process this pipeline replaces. Step IDs: IB-01,
IB-02, etc. T-10 rows must cite specific Step IDs — citing the process category without
a step identifier is a CMD-14 breach. Minimum 4 rows.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-01 Entity Inventory (domain names only, no generic labels) | | |
| T-02 FM-NN Prediction Register (≥3 rows, Expected Designation populated) | | |
| T-03 Stage Enumeration (all stages named) | | |
| T-04 Boundary Inventory (all latency columns numeric, no "Negligible") | | |
| T-08 SLA Domination Point (standalone table, not embedded) | | |
| T-05 Incumbent Baseline (≥4 rows, IB-NN Step IDs present) | | |

Phase 3 may not begin if any row shows EMPTY or NO-GO. State actual status per row.

---

## PHASE 3: STAGE TRACES

For each stage in T-03, produce one trace block in the structure below. After each
block, append T-07 rows and state the CHECKPOINT. T-04 entity.field stubs back-filled
during this phase.

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: [Stage 1: source schema fields entering the pipeline. All other stages:
diff from prior T-06 exit manifest — specify fields added, removed, renamed, or retyped.
If no changes: "verified: no field added, removed, renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest**

Authority for T-04 entity.field back-fill and for T-10 field citations:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotations** (back-fill T-04 entity.field after manifest produced):
- Error handling: [specific mechanism] OR [NH-NN — no handling — risk accepted: {named risk}]
- Data loss point: [LP-NN — named, specific loss scenario] OR [none at this boundary]
- Latency: Transport (ms): X, Processing (ms): Y, Total: X+Y ms
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified separately from normal-operation value]
- Active domain entities (from T-01): [entity names]

---

**T-07 APPEND CHECKPOINT — [Stage ID]**

Append rows for every T-02 FM-NN whose anticipated failure mode intersects this stage.
Use table rows only — CMD-04 prohibits prose bullets.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If no intersections: `| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |`

State: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

CMD-17 violation: a checkpoint without [N] is a CMD-17 breach, independently citable.

---

*(Repeat stage block + T-07 APPEND CHECKPOINT for every stage in T-03.)*

---

After the final stage, consolidate T-07 rows:

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | Go/No-Go |
|------------------|-------------------|---------|
| T-06 manifests (one per stage in T-03) | | |
| T-07 Append-Log consolidated (rows from all stage checkpoints) | | |
| T-04 entity.field stubs back-filled (all boundary rows) | | |
| Schema diffs recorded for every stage (verified-unchanged where applicable) | | |
| NH-NN and LP-NN identifiers assigned for all unhandled boundaries and loss points | | |

Checkpoint sum verification: state "Checkpoint sum = [sum of all per-stage N values];
T-07 consolidated rows = [consolidated count]. [MATCH / DISCREPANCY at Stage X]."
A discrepancy is a FLAG that will appear in T-PARITY.

Phase 4 may not begin if any row shows INCOMPLETE or NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION AND CLOSURE

### Pattern Trade-Off Analysis

Name one alternative architectural pattern for this pipeline type. State ≥2 trade-off
dimensions, at least one quantified or qualified in domain terms (e.g., "eliminates the
N-hour stale window at cost of M ms additional CDC latency per Invoice update").

---

### T-09: FM-NN Resolution Audit

Resolve every FM-NN from T-02. This section is the designated resolution target for all
T-07 deferral statements. Do not assign resolution status anywhere else.

- CONFIRMED: prediction materialized — cite the specific NH-NN or LP-NN it produced
- EXONERATED: prediction did not materialize — state the specific reason it was absent
- NEW: emerged during trace without prior prediction — assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|---------------------|-------------------|

---

### T-10: Recovery Audit Table

One row per NH-NN and LP-NN from Phase 3. CMD-14 requires a specific IB-NN Step ID —
naming the process category without a step identifier is a CMD-14 breach.

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|------------------|

---

### T-PARITY: Count Parity Gate

Standalone table — CMD-06 prohibits substitution with a prose sentence or gate column.
Enumerate every stage's checkpoint count, show the arithmetic, and issue GO or FLAG.

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|-------------------|---------------|-----------|

State: "Parity assertion: sum([N1] + [N2] + ... + [Nk]) == [M cumulative]. Status: GO /
FLAG at Stage [X] where per-stage count [N] does not match accumulated rows."

---

### T-11: Closure Gate

Per-identifier CLOSED / OPEN status for every NH-NN and LP-NN. CMD-15 prohibits
aggregate count summaries — one row per identifier.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching row in T-10 with IB-NN citation. OPEN = no T-10 row — state reason.

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-09 FM-NN Resolution Audit (every T-02 FM-NN resolved) | | |
| T-10 Recovery Audit Table (all NH-NN/LP-NN with IB-NN citations) | | |
| T-PARITY Count Parity Gate (arithmetic shown, GO / FLAG stated) | | |
| T-11 Closure Gate (one row per identifier, no aggregate substitute) | | |

State T-PARITY result and T-11 OPEN count. If OPEN > 0 or T-PARITY FLAG, trace has
unresolved gaps.
```

---

## V-02 — Lifecycle Emphasis: Per-Phase Parity Accumulation in PG-NN + Standalone T-PARITY

**Axis**: Lifecycle emphasis — each PG-NN gate table carries a "T-07 Running Total"
verification column that must equal the cumulative checkpoint sum through that phase.
A standalone T-PARITY table appears after all stage traces with full per-stage enumeration
and cross-stage arithmetic. The per-phase gate columns provide an in-flight parity trail;
T-PARITY is the final arithmetic artifact. CMD register and PG-NN entries are co-declared
in the scaffold.
**Hypothesis**: per-phase running totals in PG-NN gate tables create a two-tier parity
audit — drift detectable at each phase boundary (not only post-trace), making T-PARITY's
final arithmetic statement retroactively verifiable against the phase-gate audit trail
already committed to during trace execution.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for the following pipeline:

{topic}

Work through the five phases below in strict order. Each phase ends with a named gate
block (PG-NN). Every PG-NN gate table carries a "T-07 Running Total" column verifying
that accumulated checkpoint counts match the consolidated T-07 row count at that phase
boundary. A standalone T-PARITY Count Parity Gate is produced in Phase 5 with explicit
per-stage enumeration and the sum assertion.

Every table must be pre-declared in STEP 0. The scaffold column for column contracts is
labeled exactly "Mandatory Columns (exact names)" — no variant label qualifies.

---

## STEP 0: Output Scaffold

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| CMD | Structural Compliance Register | CMD-NN meta-contract; every structural shortfall citable by CMD ID | CMD ID, Positive Imperative, DO NOT Prohibition | — |
| T-01 | Entity Inventory | Domain entities; trace vocabulary locked; no mid-trace introductions | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure hypotheses; resolved in T-09 only | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Named and sequenced pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Boundaries with latency decomposition, entity-at-risk, and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process; IB-NN steps cited in T-10 | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-06 | Stage Exit Manifests | One typed manifest per stage | field_name, TYPE(precision), Notes | T-03 |
| T-07 | FM-NN Append-Log | Accumulating per-stage rows; count verified at every PG-NN gate | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | SLA Domination Point | Standalone domination boundary — separate from T-04 | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution audit | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN/LP-NN recovery with IB-NN step citations | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source (Stage / Boundary), T-10 Row, Status | T-10 |
| T-PARITY | Count Parity Gate | Cross-stage arithmetic parity; standalone artifact separate from PG-NN columns | Stage ID, N Rows This Stage, Running Total, GO / FLAG | T-07 |
| PG-01 | Phase 1 Gate — Scaffold | CMD and scaffold declaration completeness | Required Artifact, Declaration Status, T-07 Running Total, Go/No-Go | CMD, T-01–T-11, T-PARITY |
| PG-02 | Phase 2 Gate — Pre-Trace | Pre-trace table population before Stage 1 | Required Table, Population Status, T-07 Running Total, Go/No-Go | T-01–T-05, T-08 |
| PG-03 | Phase 3 Gate — Traces | Stage trace completeness + T-07 count chain checkpoint | Required Artifact, Completion Status, T-07 Running Total, Go/No-Go | T-03, T-06, T-07 |
| PG-04 | Phase 4 Gate — Resolution | Post-trace artifacts complete; T-PARITY arithmetic verified | Required Table, Population Status, T-07 Running Total, Go/No-Go | T-09, T-10, T-11, T-PARITY |

Phase gates registered (C-35):
- PG-01 closes Phase 1. Tables checked: CMD, T-01–T-11, T-PARITY, PG-02–PG-04.
- PG-02 closes Phase 2. Tables checked: T-01, T-02, T-03, T-04, T-08, T-05.
- PG-03 closes Phase 3. Tables checked: T-03 (all stages traced), T-06, T-07.
- PG-04 closes Phase 4. Tables checked: T-09, T-10, T-11, T-PARITY.

T-07 Running Total column in all PG-NN gates: state cumulative T-07 row count through
the end of each phase. Phase 1 and 2 value is 0 (no stage traces yet).

Stage assignment: single-role design — C-25 satisfied by default.

---

## PHASE 1: CMD AND SCAFFOLD VALIDATION

### CMD: Structural Compliance Register

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in scaffold before producing any gate block | DO NOT produce a gate block without a PG-NN scaffold entry |
| CMD-02 | Label scaffold column contract field "Mandatory Columns (exact names)" | DO NOT use "Key Columns," "Required Fields," or any descriptive label variant |
| CMD-03 | Produce T-PARITY as a standalone named table separate from all PG-NN gate tables | DO NOT substitute the T-07 Running Total column in PG-NN for T-PARITY |
| CMD-04 | Carry "T-07 Running Total" column in every PG-NN gate table | DO NOT omit the running-total verification column from any phase gate |
| CMD-05 | Append T-07 rows during each stage trace as table rows | DO NOT embed FM-NN acknowledgments as prose bullets within stage sections |
| CMD-06 | Close each stage block: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended. T-07 total to date: [M]." | DO NOT omit either [N] (this-stage count) or [M] (running total) |
| CMD-07 | Produce T-06 typed exit manifest at every stage exit | DO NOT state schema state in prose without typed field assertions |
| CMD-08 | Annotate entity.field for every T-04 boundary using T-06 field names | DO NOT use "data," "records," or "payload" as entity-at-risk identifiers |
| CMD-09 | Produce T-05 Incumbent Baseline with IB-NN Step IDs before any T-10 rows | DO NOT write recovery framing without a named pre-automation process and IB-NN step |
| CMD-10 | Cite a specific IB-NN Step ID in every T-10 row | DO NOT name the process category without a step identifier |
| CMD-11 | Produce T-08 as a standalone table — not embedded in T-04 | DO NOT append the domination point as prose or inline note to T-04 |
| CMD-12 | Produce T-11 Closure Gate with one row per NH-NN / LP-NN | DO NOT substitute an aggregate count for per-row CLOSED / OPEN status |
| CMD-13 | Resolve every FM-NN in T-09 as CONFIRMED, EXONERATED, or NEW | DO NOT leave FM-NN entries without resolution status |
| CMD-14 | Decompose boundary latency into Transport (ms) and Processing (ms) as separate columns | DO NOT use a single aggregate "Boundary Latency" column; "Negligible" is not valid |

---

### PG-01: Phase 1 Gate

| Required Artifact | Declaration Status | T-07 Running Total | Go/No-Go |
|------------------|--------------------|---------------------|---------|
| CMD register (CMD-01 through CMD-14, table format) | | 0 | |
| T-01 through T-11 declared with Mandatory Columns (exact names) | | 0 | |
| T-PARITY declared as standalone scaffold row | | 0 | |
| PG-01 through PG-04 declared with PG-NN identifiers in scaffold | | 0 | |
| Scaffold column header reads "Mandatory Columns (exact names)" | | 0 | |

Phase 2 may not begin if any row shows NO-GO. T-07 Running Total = 0.

---

## PHASE 2: PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

| Entity | Description | Key Fields |
|--------|-------------|-----------|

List every in-scope domain entity using Finance / Operations / Commerce vocabulary.
Stage traces, T-06 manifests, and T-10 rows reference only entities declared here.

---

### T-02: FM-NN Prediction Register

Minimum 3 entries. Expected Designation specifies the NH-NN or LP-NN this prediction
will produce if it materializes. Resolve in T-09 only.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

Transport (ms) and Processing (ms) are independent columns summing to Total (ms).
"Negligible" is not valid. Entity at Risk must be a T-01 entity name. entity.field:
stub "→ back-fill from T-06.[Stage ID]" until manifest is produced.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-08: SLA Domination Point

Standalone table. CMD-11 prohibits embedding in T-04. One row.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### T-05: Incumbent Baseline

Minimum 4 rows. IB-NN Step IDs required before any T-10 rows are written.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-01 Entity Inventory (domain vocabulary, no generic labels) | | 0 | |
| T-02 FM-NN Prediction Register (≥3 rows) | | 0 | |
| T-03 Stage Enumeration | | 0 | |
| T-04 Boundary Inventory (all columns numeric, no "Negligible") | | 0 | |
| T-08 SLA Domination Point (standalone, not embedded in T-04) | | 0 | |
| T-05 Incumbent Baseline (≥4 rows, IB-NN identifiers present) | | 0 | |

Phase 3 may not begin if any row shows EMPTY or NO-GO. T-07 Running Total = 0.

---

## PHASE 3: STAGE TRACES

For each stage in T-03, produce one trace block. After every block, append T-07 rows
and state the CHECKPOINT with both this-stage count [N] and running total [M].

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: [Stage 1: source fields entering. Other stages: diff from prior T-06
manifest — fields added, removed, renamed, or retyped. No changes: "verified: no field
added, removed, renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest**

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotations** (back-fill T-04 entity.field from this manifest):
- Error handling: [mechanism] OR [NH-NN — no handling — risk: {named risk}]
- Data loss point: [LP-NN — named loss scenario] OR [none]
- Latency: Transport (ms): X, Processing (ms): Y, Total: X+Y ms
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified separately]
- Active entities (T-01): [names]

---

**T-07 APPEND CHECKPOINT — [Stage ID]**

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If no intersections: `| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |`

State: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended. T-07 total to date: [M]."

CMD-06 violation: omitting [N] or [M] is a CMD-06 breach.

---

*(Repeat stage block + T-07 APPEND CHECKPOINT for every stage in T-03.)*

---

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### PG-03: Phase 3 Gate

Count chain verification: state "Checkpoint sum = [sum of all per-stage N values];
T-07 consolidated rows = [count]. [MATCH / DISCREPANCY at Stage X]."

| Required Artifact | Completion Status | T-07 Running Total | Go/No-Go |
|------------------|-------------------|--------------------|---------|
| T-06 manifests (one per stage) | | [checkpoint sum] | |
| T-07 Append-Log consolidated | | [same] | |
| T-04 entity.field stubs back-filled | | | |
| Schema diffs for all stages recorded | | | |
| NH-NN and LP-NN identifiers assigned | | | |

Phase 4 may not begin if any row shows INCOMPLETE or NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION AND CLOSURE

### Pattern Trade-Off Analysis

Name one alternative architectural pattern. State ≥2 trade-off dimensions, at least
one quantified or qualified in domain terms.

---

### T-09: FM-NN Resolution Audit

Resolve every T-02 FM-NN entry. Resolution status assigned here only — not inline.

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|---------------------|-------------------|

---

### T-10: Recovery Audit Table

One row per NH-NN and LP-NN. IB-NN Step Cited must be a specific step from T-05.

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|------------------|

---

### T-PARITY: Count Parity Gate

Standalone table — CMD-03 prohibits substitution with PG-NN Running Total column.
Enumerate every stage, show arithmetic, issue GO or FLAG.

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|-------------------|---------------|-----------|

State: "Parity assertion: sum([N1] + [N2] + ... + [Nk]) == [M cumulative]. Status: GO
/ FLAG at Stage [X] where per-stage count diverges from accumulated rows."

Compare T-PARITY findings against PG-03 T-07 Running Total. Any discrepancy between
per-phase gate counts and T-PARITY arithmetic is a structural gap — name the stage.

---

### T-11: Closure Gate

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-07 Running Total | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-09 FM-NN Resolution Audit (all FM-NN resolved) | | [M from T-PARITY] | |
| T-10 Recovery Audit Table (all NH-NN/LP-NN with IB-NN citations) | | | |
| T-PARITY Count Parity Gate (per-stage arithmetic, GO/FLAG stated) | | | |
| T-11 Closure Gate (one row per identifier, no aggregate) | | | |

State T-PARITY result and T-11 OPEN count. If OPEN > 0 or FLAG, trace has unresolved
structural gaps.
```

---

## V-03 — Role Sequence: Finance → Operations → Commerce with Role-Owned CMD Slices

**Axis**: Role sequence — three explicitly named roles execute in sequence. Finance
Controller owns STEP 0 (complete scaffold + CMD) and Phase 1 (extract + validate stages).
Operations Analyst owns Phase 2 (transform + load + sync stages). Commerce Data Analyst
owns Phase 3 (analytics + distribution stages) and Phase 4 (post-trace resolution). Each
role declares a CMD slice governing its assigned stages; the master CMD table is the union.
Role handoff gates serve as PG-NN phase gates.
**Hypothesis**: role-specific CMD slices eliminate responsibility ambiguity — a CMD breach
is attributable to a named role, and each role's handoff gate enforces its own slice
before the next role begins. The stage assignment map binds every T-06 typed manifest and
every T-04 entity.field back-fill to a named responsible role, making unstaffed stages
structurally visible.

---

```
You are executing a three-role data pipeline trace team. The roles are:

- FINANCE CONTROLLER (FC): AP / GL / Invoice domain, runs STEP 0 and Phase 1
- OPERATIONS ANALYST (OA): Supply chain / inventory / logistics domain, runs Phase 2
- COMMERCE DATA ANALYST (CDA): SKU / revenue / catalog domain, runs Phase 3 and Phase 4

Trace the following pipeline:

{topic}

Role sequence is strict. FC completes its phase gate (PG-FC) before OA begins. OA
completes its phase gate (PG-OA) before CDA begins. CDA completes the trace and all
post-trace resolution artifacts.

Every table must be pre-declared in STEP 0 by FC. Mandatory Columns (exact names) is
the binding column header for all column specifications.

---

## STEP 0 — FINANCE CONTROLLER

### CMD: Master Structural Compliance Register

FC declares all CMD entries before any T-NN artifact. OA and CDA CMD slices are
subsets of this master register. CMD slices are identified by role prefix in the
"Owner Role" column.

| CMD ID | Owner Role | Positive Imperative | DO NOT Prohibition |
|--------|------------|--------------------|--------------------|
| CMD-01 | FC | Pre-declare every phase gate as PG-NN in scaffold before the phase it governs begins | DO NOT produce a gate block without a PG-NN scaffold entry |
| CMD-02 | FC | Label scaffold column contracts "Mandatory Columns (exact names)" | DO NOT label column contracts as "Key Columns," "Required Fields," or any variant |
| CMD-03 | FC | Produce T-02 FM-NN Prediction Register before Stage 1; resolve only in T-09 | DO NOT assign CONFIRMED/EXONERATED/NEW status inline during stage traces |
| CMD-04 | FC | Produce T-04 Boundary Inventory with T-01 entity names and entity.field from T-06 | DO NOT use "data," "records," or "payload" as entity identifiers |
| CMD-05 | FC | Produce T-05 Incumbent Baseline with IB-NN Step IDs before any T-10 rows | DO NOT write recovery framing without a named pre-automation step |
| CMD-06 | FC | Produce Stage Assignment Map (T-00) mapping every stage to exactly one named role | DO NOT leave a pipeline stage unassigned in T-00 |
| CMD-07 | OA | Append T-07 rows during each OA stage trace as table rows; close with CHECKPOINT | DO NOT embed FM-NN acknowledgments as prose bullets in OA stage sections |
| CMD-08 | OA | State "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended" after every OA stage | DO NOT omit [N] row count from OA checkpoint statements |
| CMD-09 | OA | Produce T-06 typed exit manifests for all OA-assigned stages | DO NOT describe OA stage schema state in prose without typed field assertions |
| CMD-10 | OA | Back-fill T-04 entity.field stubs for all OA-assigned boundaries | DO NOT leave OA boundary entity.field stubs as "→ back-fill" after OA phase completes |
| CMD-11 | CDA | Append T-07 rows during each CDA stage trace as table rows; close with CHECKPOINT | DO NOT embed FM-NN acknowledgments as prose bullets in CDA stage sections |
| CMD-12 | CDA | State "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended" after every CDA stage | DO NOT omit [N] row count from CDA checkpoint statements |
| CMD-13 | CDA | Produce T-PARITY as a standalone named table with per-stage arithmetic | DO NOT substitute a prose parity sentence for T-PARITY |
| CMD-14 | CDA | Cite a specific IB-NN Step ID in every T-10 row | DO NOT name the process category without a step identifier |
| CMD-15 | CDA | Produce T-11 Closure Gate with one row per NH-NN / LP-NN | DO NOT substitute an aggregate count for per-row CLOSED / OPEN status |
| CMD-16 | CDA | Produce T-08 SLA Domination Point as a standalone table separate from T-04 | DO NOT embed the domination point inside or appended to T-04 |

---

### Output Scaffold

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Owner Role | Depends On |
|----|-----------|---------|----------------------------------|------------|------------|
| CMD | Master CMD Register | Meta-contract; breach citable by CMD ID | CMD ID, Owner Role, Positive Imperative, DO NOT Prohibition | FC | — |
| T-00 | Stage Assignment Map | Every stage mapped to exactly one named role | Stage ID, Stage Name, Assigned Role | FC | — |
| T-01 | Entity Inventory | Domain entities from all three roles; locks trace vocabulary | Entity, Description, Key Fields, Domain | FC / OA / CDA | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure hypotheses; resolved in T-09 only | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | FC | — |
| T-03 | Stage Enumeration | Named and sequenced stages | Stage ID, Stage Name, Description | FC | — |
| T-04 | Boundary Inventory | Boundaries with latency decomposition, entity-at-risk, SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | FC (structure); OA/CDA (back-fill) | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process steps; IB-NN identifiers | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | FC | — |
| T-06 | Stage Exit Manifests | One typed manifest per stage; produced by stage's assigned role | field_name, TYPE(precision), Notes | FC / OA / CDA | T-03 |
| T-07 | FM-NN Append-Log | Accumulating per-stage rows; rows added by each role's stage traces | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | FC / OA / CDA | T-02, T-03 |
| T-08 | SLA Domination Point | Standalone domination boundary | Domination Boundary, Exact Cumulative SLA%, Justification | CDA | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace lifecycle resolution; FM-NN resolution audit | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | CDA | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN / LP-NN recovery with IB-NN citations | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage | CDA | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source (Stage / Boundary), T-10 Row, Status | CDA | T-10 |
| T-PARITY | Count Parity Gate | Cross-stage arithmetic parity; standalone | Stage ID, N Rows This Stage, Running Total, GO / FLAG | CDA | T-07 |
| PG-FC | Finance Controller Handoff Gate | FC phase completion before OA begins | Required Artifact, Population Status, CMD Slice Verified, Go/No-Go | FC | CMD (FC slice), T-01–T-05 |
| PG-OA | Operations Analyst Handoff Gate | OA phase completion before CDA begins | Required Artifact, Population Status, CMD Slice Verified, Go/No-Go | OA | CMD (OA slice), T-06 (OA stages), T-07 (OA rows) |
| PG-CDA | Commerce Data Analyst Closure Gate | CDA phase completion and full trace closure | Required Table, Population Status, CMD Slice Verified, Go/No-Go | CDA | CMD (CDA slice), T-08–T-11, T-PARITY |

Phase gates registered (C-35):
- PG-FC closes Finance Controller phase. Gates: CMD (FC slice), T-00, T-01–T-05.
- PG-OA closes Operations Analyst phase. Gates: CMD (OA slice), T-06 (OA), T-07 (OA rows).
- PG-CDA closes Commerce Data Analyst phase. Gates: CMD (CDA slice), T-08–T-11, T-PARITY.

---

### T-00: Stage Assignment Map

Map every pipeline stage to exactly one named role. A stage absent from T-00 is a
CMD-06 breach.

| Stage ID | Stage Name | Assigned Role |
|----------|------------|--------------|

---

### T-01: Entity Inventory (Finance Controller — initial entries)

FC declares Finance domain entities. OA and CDA append their domain entities before
their phases begin.

| Entity | Description | Key Fields | Domain |
|--------|-------------|-----------|--------|

---

### T-02: FM-NN Prediction Register

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

Minimum 3 entries across FC, OA, and CDA domains.

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory (Structure)

FC declares structure; OA and CDA back-fill entity.field stubs for their assigned
boundaries after producing T-06 manifests.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-05: Incumbent Baseline

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 rows. IB-NN Step IDs required before CDA writes any T-10 rows.

---

### PG-FC: Finance Controller Handoff Gate

FC verifies its CMD slice (CMD-01 through CMD-06) and pre-trace artifacts before
handing off to Operations Analyst.

| Required Artifact | Population Status | CMD Slice Verified | Go/No-Go |
|------------------|-------------------|--------------------|---------|
| CMD register (CMD-01–CMD-16, all Owner Role entries) | | CMD-01 through CMD-06 | |
| T-00 Stage Assignment Map (all stages, all roles assigned) | | CMD-06 | |
| T-01 Entity Inventory (FC domain entities declared) | | CMD-04 | |
| T-02 FM-NN Prediction Register (≥3 rows, Expected Designation populated) | | CMD-03 | |
| T-03 Stage Enumeration | | — | |
| T-04 Boundary Inventory structure (FC-boundary rows present) | | CMD-04 | |
| T-05 Incumbent Baseline (≥4 rows, IB-NN present) | | CMD-05 | |
| T-06 manifests for FC-assigned stages (typed field assertions) | | — | |
| T-07 rows appended for FC-assigned stages with CHECKPOINT counts | | — | |

Operations Analyst phase may not begin if any row shows NO-GO.

---

## PHASE 2 — OPERATIONS ANALYST

OA first appends Operations domain entities to T-01 (InventoryRecord, ShipmentAdvice,
GoodsReceipt, VendorAcknowledgment, etc.), then traces OA-assigned stages.

### T-01 Append — Operations Analyst Entities

| Entity | Description | Key Fields | Domain |
|--------|-------------|-----------|--------|

---

For each OA-assigned stage (from T-00), produce the stage trace block:

### Stage [Stage ID]: [Stage Name] — OPERATIONS ANALYST

**Schema diff**: [diff from prior T-06 manifest; or "verified: no field added, removed,
renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest**

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotations** (back-fill T-04 after manifest produced):
- Error handling: [mechanism] OR [NH-NN — no handling — risk: {named risk}]
- Data loss point: [LP-NN — named loss scenario] OR [none]
- Latency: Transport (ms): X, Processing (ms): Y, Total: X+Y ms
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified separately]
- Active entities (T-01): [names]

---

**T-07 APPEND CHECKPOINT — [Stage ID]** (OA)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

State: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended." (CMD-08 breach if [N] omitted)

---

*(Repeat OA stage block for every OA-assigned stage in T-00.)*

---

### PG-OA: Operations Analyst Handoff Gate

OA verifies its CMD slice (CMD-07 through CMD-10) before handing off to Commerce
Data Analyst.

| Required Artifact | Population Status | CMD Slice Verified | Go/No-Go |
|------------------|-------------------|--------------------|---------|
| T-01 OA entity entries appended | | — | |
| T-06 manifests for all OA-assigned stages | | CMD-09 | |
| T-04 entity.field back-filled for all OA-assigned boundaries | | CMD-10 | |
| T-07 CHECKPOINT rows appended for all OA stages (with [N] counts) | | CMD-07, CMD-08 | |

Commerce Data Analyst phase may not begin if any row shows NO-GO.

---

## PHASE 3 — COMMERCE DATA ANALYST

CDA first appends Commerce domain entities to T-01 (SKU, OrderLine, ProductCatalog,
RevenueRecognitionEvent, etc.), then traces CDA-assigned stages.

### T-01 Append — Commerce Data Analyst Entities

| Entity | Description | Key Fields | Domain |
|--------|-------------|-----------|--------|

---

For each CDA-assigned stage (from T-00), produce the stage trace block:

### Stage [Stage ID]: [Stage Name] — COMMERCE DATA ANALYST

**Schema diff**: [diff from prior T-06 manifest; or "verified: no field added, removed,
renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest**

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotations** (back-fill T-04 after manifest produced):
- Error handling: [mechanism] OR [NH-NN — no handling — risk: {named risk}]
- Data loss point: [LP-NN — named loss scenario] OR [none]
- Latency: Transport (ms): X, Processing (ms): Y, Total: X+Y ms
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified separately]
- Active entities (T-01): [names]

---

**T-07 APPEND CHECKPOINT — [Stage ID]** (CDA)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

State: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended." (CMD-12 breach if [N] omitted)

---

*(Repeat CDA stage block for every CDA-assigned stage in T-00.)*

---

### T-07: FM-NN Append-Log (Consolidated — all roles)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

## PHASE 4 — COMMERCE DATA ANALYST: POST-TRACE RESOLUTION AND CLOSURE

### T-08: SLA Domination Point

Standalone table. CMD-16 prohibits embedding in T-04. One row.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### Pattern Trade-Off Analysis

Name one alternative architectural pattern. State ≥2 trade-off dimensions, at least
one quantified or qualified in domain terms.

---

### T-09: FM-NN Resolution Audit

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|---------------------|-------------------|

Resolve every T-02 FM-NN as CONFIRMED (cite NH-NN or LP-NN), EXONERATED (state reason),
or NEW (assign identifier retroactively).

---

### T-10: Recovery Audit Table

One row per NH-NN and LP-NN. IB-NN Step Cited must be a specific IB-NN from T-05
(CMD-14).

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|------------------|

---

### T-PARITY: Count Parity Gate

Standalone table — CMD-13 prohibits substitution with prose or PG-NN column.

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|-------------------|---------------|-----------|

State: "Parity assertion: sum([N1] + ... + [Nk]) == [M cumulative]. Status: GO / FLAG."
Attribute each [N] to its owner role (FC / OA / CDA).

---

### T-11: Closure Gate

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### PG-CDA: Commerce Data Analyst Closure Gate

| Required Table | Population Status | CMD Slice Verified | Go/No-Go |
|---------------|-------------------|--------------------|---------|
| T-08 SLA Domination Point (standalone, separate from T-04) | | CMD-16 | |
| T-09 FM-NN Resolution Audit (all T-02 entries resolved) | | CMD-03, CMD-13 | |
| T-10 Recovery Audit Table (all NH-NN/LP-NN with IB-NN Step Cited) | | CMD-14 | |
| T-PARITY Count Parity Gate (per-stage arithmetic, GO/FLAG, roles attributed) | | CMD-13 | |
| T-11 Closure Gate (one row per identifier, no aggregate substitute) | | CMD-15 | |

State T-PARITY result and T-11 OPEN count.
```

---

## V-04 — Phrasing Register + Inertia Framing: Conversational with IB-NN-Anchored CMD

**Axis**: Phrasing register (conversational "walk through" framing) plus inertia framing
(incumbent baseline produced before the scaffold and before any structural declaration).
CMD register entries in the DO NOT prohibition column explicitly reference IB-NN step
identifiers from the already-produced baseline. The prompt speaks to the analyst in
narrative voice rather than imperative blocks.
**Hypothesis**: anchoring CMD prohibitions to IB-NN identifiers that exist before the
scaffold is declared converts the incumbent baseline from a depth requirement into a
contract anchor — the CMD register's DO NOT language pre-commits to specific step
citations before the first stage is named, so a recovery row missing an IB-NN step
is simultaneously a named CMD breach and a C-16 failure, creating dual-citation pressure.

---

```
You are a Finance / Operations / Commerce data domain expert. Walk me through a complete
data flow trace of this pipeline:

{topic}

Start by documenting how this process worked before the pipeline existed — the manual
or legacy process it replaced. That documentation becomes the baseline your recovery
prescriptions will cite. Then declare your structural commitments as a CMD register, and
from there build out the full trace.

---

## Section 0: Pre-Automation Baseline

Before declaring any tables or scaffold, document the operational process this pipeline
replaced. Give each step an IB-NN identifier. You will cite specific IB-NN steps in your
CMD register and in every recovery prescription you write later.

### T-IB: Incumbent Baseline

The process that a Finance, Operations, or Commerce team ran before this pipeline existed.
Minimum 5 steps. Give each step an ID (IB-01, IB-02, etc.), name, the role who owned it,
and how long it took or how often it ran.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Keep this table in mind: every time you write a recovery prescription later in the trace,
you will point to a specific row here by Step ID.

---

## Section 1: Structural Commitments (CMD Register)

Now declare what you commit to building. The CMD register is your binding promise for
every structural element. The DO NOT prohibitions below reference the IB-NN Step IDs
from Section 0 to lock recovery prescriptions to the specific baseline steps they
fall back on.

These commitments are pre-declared in the scaffold below, so any shortfall is citable
by CMD ID.

### CMD: Structural Compliance Register

| CMD ID | Commitment | DO NOT Prohibition |
|--------|------------|--------------------|
| CMD-01 | Declare every table in the scaffold before producing it | DO NOT introduce a table that has no scaffold entry |
| CMD-02 | Use "Mandatory Columns (exact names)" as the scaffold column-contract label | DO NOT label column specs as "Key Columns" or "Required Fields" |
| CMD-03 | Pre-declare every phase gate as PG-NN in the scaffold with the tables it checks | DO NOT produce a gate block that has no PG-NN scaffold entry |
| CMD-04 | Produce T-PARITY as a standalone table separate from phase gate columns | DO NOT substitute the parity check as a prose sentence or gate-column annotation |
| CMD-05 | Append T-07 FM-NN log rows during each stage trace — as table rows, not prose | DO NOT write FM-NN acknowledgments as bullets within a stage section |
| CMD-06 | Close every stage trace: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended" | DO NOT omit the row count [N] from the checkpoint statement |
| CMD-07 | Produce a typed T-06 exit manifest at every stage | DO NOT describe schema state in prose without typed field-level assertions |
| CMD-08 | Annotate entity.field for every T-04 boundary using T-06 field names | DO NOT write "data" or "records" as the entity at risk |
| CMD-09 | Produce T-08 SLA Domination Point as its own table, not inside T-04 | DO NOT attach the domination finding as an inline note to T-04 |
| CMD-10 | Write one T-10 recovery row for every NH-NN and LP-NN, citing a specific IB-NN step | DO NOT write recovery guidance that cites the process category without naming IB-01, IB-02, or another specific step from T-IB |
| CMD-11 | Back all recovery fallbacks to a named operational actor from T-IB | DO NOT use "human intervention" or "manual review" without naming the Responsible Role from the T-IB row you are citing |
| CMD-12 | Produce T-11 Closure Gate with one row per identifier | DO NOT write "N of M covered" as a substitute for per-row CLOSED / OPEN status |
| CMD-13 | Decompose boundary latency into Transport (ms) and Processing (ms) separately | DO NOT aggregate latency into a single column; do not write "Negligible" as a value |
| CMD-14 | Resolve every FM-NN in T-09 post-trace; no resolution status inline during traces | DO NOT write CONFIRMED, EXONERATED, or NEW during stage trace sections |

---

## Section 2: Output Scaffold

Here is every table this response will produce. The Mandatory Columns column commits to
exact column names — produced tables must use those exact names.

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| T-IB | Incumbent Baseline | Pre-automation process steps; produced in Section 0 | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| CMD | Structural Compliance Register | Meta-contract; produced in Section 1 | CMD ID, Commitment, DO NOT Prohibition | — |
| T-01 | Entity Inventory | Domain entities locked before Stage 1 | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Failure hypotheses; resolved in T-09 | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Named pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Latency, entity-at-risk, SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | FM-NN Append-Log | Per-stage rows accumulate during trace | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-06 | Stage Exit Manifests | Typed manifests per stage | field_name, TYPE(precision), Notes | T-03 |
| T-07 | SLA Domination Point | Standalone domination finding | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-08 | FM-NN Resolution Audit | Post-trace lifecycle resolution audit | FM-NN, Status, T-05 Rows Consulted, Evidence / Reason | T-02, T-05 |
| T-09 | Recovery Audit Table | Recovery with IB-NN step citations from T-IB | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage | T-04, T-IB, T-06 |
| T-10 | Closure Gate | Per-identifier CLOSED / OPEN | Identifier, Source (Stage / Boundary), T-09 Row, Status | T-09 |
| T-PARITY | Count Parity Gate | Cross-stage arithmetic parity | Stage ID, N Rows This Stage, Running Total, GO / FLAG | T-05 |
| PG-01 | Phase 1 Gate | Baseline, CMD, and scaffold completeness | Required Artifact, Population Status, Go/No-Go | T-IB, CMD, T-01–T-10, T-PARITY |
| PG-02 | Phase 2 Gate | Pre-trace table population | Required Table, Population Status, Go/No-Go | T-01–T-04, T-07 |
| PG-03 | Phase 3 Gate | Stage trace completeness | Required Artifact, Completion Status, Go/No-Go | T-03, T-06, T-05 |
| PG-04 | Phase 4 Gate | Post-trace resolution completeness | Required Table, Population Status, Go/No-Go | T-08, T-09, T-10, T-PARITY |

Phase gates registered (C-35):
- PG-01 closes Phase 1: T-IB, CMD, and scaffold declared and populated.
- PG-02 closes Phase 2: pre-trace tables T-01 through T-04 and T-07 populated.
- PG-03 closes Phase 3: all stage traces, T-06 manifests, T-05 append-log complete.
- PG-04 closes Phase 4: all post-trace resolution artifacts complete.

Stage assignment: single-role design — C-25 satisfied by default.

---

### PG-01: Phase 1 Gate

Take stock of what Section 0 and Section 1 have produced.

| Required Artifact | Population Status | Go/No-Go |
|------------------|-------------------|---------|
| T-IB Incumbent Baseline (≥5 rows, IB-NN identifiers) | | |
| CMD register (CMD-01 through CMD-14) | | |
| Scaffold declared with Mandatory Columns (exact names) header | | |
| PG-01 through PG-04 registered in scaffold with tables they check | | |
| T-PARITY declared as standalone scaffold row | | |

Phase 2 may not begin if any row shows NO-GO.

---

## Phase 2: Pre-Trace Setup

Before tracing any stage, set up the entity inventory, predict failure modes, enumerate
stages, and document boundaries. These tables give you the vocabulary and structure
everything else refers back to.

### T-01: Entity Inventory

List every domain entity in scope — Finance (Invoice, PurchaseOrder, LedgerEntry,
APVoucher), Operations (InventoryRecord, ShipmentAdvice, GoodsReceipt), Commerce
(SKU, OrderLine, ProductCatalog, RevenueRecognitionEvent), and any others this pipeline
touches. Every entity reference in stage traces, T-06 manifests, and T-09 recovery rows
draws from this table.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register

Walk through the pipeline mentally and predict every failure mode you expect to encounter.
Write them here before tracing any stage. You will acknowledge each one inline during
the trace (as T-05 rows) and formally resolve them in T-08 after the trace is done.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

Minimum 3 entries.

---

### T-03: Stage Enumeration

Name every pipeline stage in sequence.

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

For every inter-stage boundary, document the entity at risk, latency components, and
SLA impact. Use entity.field format for the risk annotation — back-fill from each
stage's T-06 manifest after you produce it.

Rules to keep in mind:
- Latency has two components — Transport and Processing — as separate columns. No
  aggregate "Boundary Latency." No "Negligible."
- Entity at risk must be a named T-01 entity, not "data" or "records."
- SLA% columns track how much of your total SLA budget each boundary consumes.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-07: SLA Domination Point

After completing T-04, identify the domination boundary as its own table. Do not
append this to T-04 — it needs to be separately referenceable.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-01 Entity Inventory (all in-scope domain entities named) | | |
| T-02 FM-NN Prediction Register (≥3 predictions, Expected Designation populated) | | |
| T-03 Stage Enumeration | | |
| T-04 Boundary Inventory (all latency values numeric) | | |
| T-07 SLA Domination Point (standalone table, not embedded) | | |

Phase 3 may not begin if any row shows EMPTY or NO-GO.

---

## Phase 3: Walking Through Each Stage

For each stage in T-03, trace what happens to the data, what the schema looks like
at exit, what can go wrong at the boundary, and which FM-NN predictions touch this
stage. After each stage, note the T-05 append-log checkpoint.

---

### Stage [Stage ID]: [Stage Name]

Here is what enters this stage and what leaves:

**Schema diff**: [Stage 1: describe the source fields entering the pipeline. For all
subsequent stages: compare to the prior T-06 manifest and state what changed — fields
added, removed, renamed, or retyped. If nothing changed: "verified: no field added,
removed, renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest**

What the schema looks like at stage exit. This is the authority for the entity.field
back-fill in T-04 and for field citations in T-09 recovery rows.

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**At boundary B[N]->[N+1], here is what can go wrong:**
- Error handling: [what mechanism catches errors here, or NH-NN if nothing does]
- Data loss point: [LP-NN — describe the loss scenario specifically, or none]
- Latency: Transport X ms, Processing Y ms, Total X+Y ms
- Normal stale window: [how stale can data be under normal operation]
- Failure-mode stale window: [how stale under failure — separate answer]
- Entities active at this boundary (from T-01): [names]

---

**T-05 Append-Log Checkpoint — [Stage ID]**

Which FM-NN predictions from T-02 touched this stage? Append them to the log now,
as table rows.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If none: `| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |`

State: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

---

*(Walk through every stage in T-03 this way.)*

---

### T-05: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### Pattern Trade-Off

Describe one alternative pattern for this pipeline — name it, then give at least two
trade-off dimensions compared to the current design. Make at least one of those
dimensions concrete in domain terms.

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | Go/No-Go |
|------------------|-------------------|---------|
| T-06 manifests produced for every stage in T-03 | | |
| T-05 append-log rows present for every stage (with checkpoint counts) | | |
| T-04 entity.field stubs back-filled for all boundaries | | |
| Schema diffs recorded for every stage | | |
| NH-NN and LP-NN identifiers assigned for all unhandled cases | | |

Phase 4 may not begin if any row shows INCOMPLETE or NO-GO.

---

## Phase 4: Resolution and Closure

Now resolve everything you deferred during the trace and close out the audit trail.

### T-08: FM-NN Resolution Audit

Go through every FM-NN from T-02 and resolve it. Pull your T-05 rows as evidence.

For each entry: CONFIRMED if the failure materialized (cite the NH-NN or LP-NN it
produced), EXONERATED if it didn't (say specifically why), or NEW if something
emerged mid-trace that you didn't predict (assign it an identifier now).

| FM-NN | Status | T-05 Rows Consulted | Evidence / Reason |
|-------|--------|---------------------|-------------------|

---

### T-09: Recovery Audit Table

For every NH-NN and LP-NN from the trace, write a recovery prescription. Every row
must cite a specific Step ID from T-IB — not the process category, the actual step.
Remember: CMD-10 says "DO NOT write recovery guidance without naming IB-01, IB-02, or
another specific step from T-IB."

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|------------------|

---

### T-PARITY: Count Parity Gate

Enumerate every stage's T-05 checkpoint count, show the arithmetic, and issue GO or
FLAG. This is its own table — not a sentence, not a column in PG-03.

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|-------------------|---------------|-----------|

State: "Parity assertion: sum([N1] + ... + [Nk]) == [M cumulative]. Status: GO / FLAG."

---

### T-10: Closure Gate

One row per identifier. Go through every NH-NN and LP-NN and confirm it has a row in
T-09. OPEN means it doesn't — state why.

| Identifier | Source (Stage / Boundary) | T-09 Row | Status |
|-----------|--------------------------|----------|--------|

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-08 FM-NN Resolution Audit (all T-02 FM-NN resolved) | | |
| T-09 Recovery Audit Table (all NH-NN/LP-NN with IB-NN step citations from T-IB) | | |
| T-PARITY Count Parity Gate (arithmetic complete, GO/FLAG) | | |
| T-10 Closure Gate (one row per identifier) | | |

State T-PARITY result and T-10 OPEN count. If OPEN > 0, the trace has unclosed gaps.
```

---

## V-05 — Combined: Criterion-Annotated Scaffold with Three-Way Binding (CMD + PG-NN + T-PARITY)

**Axis**: Combined output format and lifecycle emphasis — the scaffold includes a
"Satisfies Criterion" column explicitly mapping each artifact to C-35, C-36, or C-37.
CMD entries, PG-NN entries, and T-PARITY are co-declared in the scaffold's first four
rows. PG-NN entries carry a compound "Tables Checked | CMD Enforced" field. A
cross-reference consistency check in PG-03 verifies that every CMD entry governing
a Phase 3 table has been satisfied. The prompt's framing is structural-audit first:
the scaffold is a compliance map before it is a table list.
**Hypothesis**: making the criterion-to-artifact mapping explicit in the scaffold converts
rubric compliance from evaluator inference into structural verification — confirming C-35
requires only reading the scaffold's PG-NN rows, C-36 requires reading T-PARITY's row,
and C-37 requires reading the CMD row; no trace content inspection is required to confirm
these three criteria are satisfied.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for:

{topic}

This prompt uses a criterion-annotated scaffold. The scaffold's "Satisfies Criterion"
column marks which rubric criterion each artifact directly satisfies. Use this column
to verify coverage of C-35 (PG-NN pre-registration), C-36 (count parity gate), and
C-37 (CMD register) before producing any stage trace.

Every table must be pre-declared in STEP 0. Column contracts are declared under the
header "Mandatory Columns (exact names)" — any other label fails.

---

## STEP 0: Criterion-Annotated Output Scaffold

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Satisfies Criterion | Depends On |
|----|-----------|---------|----------------------------------|---------------------|------------|
| CMD | Structural Compliance Register | C-37 artifact: CMD-NN table pre-declared in scaffold; every structural shortfall citable by ID | CMD ID, Positive Imperative, DO NOT Prohibition | C-37 | — |
| T-PARITY | Count Parity Gate | C-36 artifact: standalone cross-stage arithmetic parity gate; separate from all PG-NN columns and per-stage checkpoints | Stage ID, N Rows This Stage, Running Total, GO / FLAG | C-36 | T-07 |
| PG-01 | Phase 1 Gate | C-35 artifact: scaffold and CMD validation gate; pre-declared with PG-01 identifier | Required Artifact, Population Status, CMD-NN Verified, Criterion Coverage, Go/No-Go | C-35 | CMD, T-01–T-11, T-PARITY |
| PG-02 | Phase 2 Gate | C-35 artifact: pre-trace population gate; pre-declared with PG-02 identifier | Required Table, Population Status, CMD-NN Verified, Go/No-Go | C-35 | T-01–T-05, T-08 |
| PG-03 | Phase 3 Gate | C-35 artifact: stage trace completeness gate with CMD-NN cross-reference; pre-declared with PG-03 identifier | Required Artifact, Completion Status, CMD-NN Verified, Go/No-Go | C-35 | T-03, T-06, T-07 |
| PG-04 | Phase 4 Gate | C-35 artifact: post-trace closure gate; pre-declared with PG-04 identifier | Required Table, Population Status, T-PARITY Status, Go/No-Go | C-35 | T-09, T-10, T-11, T-PARITY |
| T-01 | Entity Inventory | Domain entities; trace vocabulary locked | Entity, Description, Key Fields | — | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure hypotheses; resolved in T-09 only | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — | — |
| T-03 | Stage Enumeration | Named and sequenced pipeline stages | Stage ID, Stage Name, Description | — | — |
| T-04 | Boundary Inventory | Boundaries with latency decomposition, entity-at-risk, SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | — | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process; IB-NN steps cited in T-10 | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — | — |
| T-06 | Stage Exit Manifests | One typed manifest per stage | field_name, TYPE(precision), Notes | — | T-03 |
| T-07 | FM-NN Append-Log | Accumulating per-stage rows; count verified in T-PARITY | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | — | T-02, T-03 |
| T-08 | SLA Domination Point | Standalone domination boundary — separate from T-04 | Domination Boundary, Exact Cumulative SLA%, Justification | — | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution audit | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | — | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN/LP-NN recovery with IB-NN step citations | NH/LP ID, Triggering Condition, Recovery Mechanism, IB-NN Step Cited, Boundary / Stage | — | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source (Stage / Boundary), T-10 Row, Status | — | T-10 |

C-35 verification: scaffold rows PG-01 through PG-04 each carry a PG-NN identifier and
are marked "C-35" in the Satisfies Criterion column. Any gate block produced without a
corresponding PG-NN scaffold row is an undeclared artifact.

C-36 verification: scaffold row T-PARITY is marked "C-36." A count parity gate produced
without a T-PARITY scaffold entry, or embedded as prose or as a PG-NN column, fails C-36
regardless of arithmetic correctness.

C-37 verification: scaffold row CMD is marked "C-37." A CMD register produced without a
CMD scaffold entry, or formatted as a prose checklist without CMD-NN identifiers, fails
C-37 regardless of content.

Phase gates registered (C-35):
- PG-01 closes Phase 1. Checks: CMD (C-37 satisfied), T-PARITY (C-36 satisfied),
  PG-01–PG-04 scaffold entries (C-35 satisfied), T-01–T-11 declared.
- PG-02 closes Phase 2. Checks: T-01–T-05, T-08 populated.
- PG-03 closes Phase 3. Checks: T-06 manifests, T-07 complete, T-04 back-filled.
- PG-04 closes Phase 4. Checks: T-09, T-10, T-11, T-PARITY arithmetic.

Stage assignment: single-role design — C-25 satisfied by default.

---

## PHASE 1: SCAFFOLD VALIDATION AND CMD DECLARATION

### CMD: Structural Compliance Register

The CMD register satisfies C-37. It is pre-declared in the scaffold as the CMD row.
Every subsequent structural shortfall is citable by CMD identifier.

| CMD ID | Positive Imperative | DO NOT Prohibition |
|--------|--------------------|--------------------|
| CMD-01 | Pre-declare every phase gate as PG-NN in scaffold, marked C-35, before producing it | DO NOT produce a gate block without a PG-NN scaffold entry and a C-35 marker |
| CMD-02 | Declare T-PARITY in scaffold, marked C-36, as a standalone row before any stage trace | DO NOT substitute a prose parity sentence or PG-NN gate column for T-PARITY |
| CMD-03 | Declare CMD in scaffold, marked C-37, as the first scaffold row | DO NOT produce a CMD register without a CMD scaffold entry |
| CMD-04 | Use "Mandatory Columns (exact names)" as the scaffold column-contract header | DO NOT label column contracts as "Key Columns," "Required Fields," or any variant |
| CMD-05 | Append T-07 rows during each stage trace as table rows; close with CHECKPOINT | DO NOT embed FM-NN acknowledgments as prose bullets within stage sections |
| CMD-06 | State "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended" after each stage | DO NOT omit [N] row count from checkpoint statement |
| CMD-07 | Produce one T-06 typed exit manifest per stage | DO NOT state schema state in prose without typed field assertions |
| CMD-08 | Annotate entity.field for every T-04 boundary using T-06 field names | DO NOT use "data," "records," or "payload" as entity-at-risk identifiers |
| CMD-09 | Produce T-08 SLA Domination Point as standalone table separate from T-04 | DO NOT embed domination point inside or appended to T-04 |
| CMD-10 | Produce T-05 Incumbent Baseline with IB-NN Step IDs before any T-10 rows | DO NOT write recovery framing without citing a specific IB-NN step |
| CMD-11 | Cite specific IB-NN Step ID in every T-10 row | DO NOT cite the process category without a step identifier |
| CMD-12 | Produce T-11 Closure Gate with one row per NH-NN / LP-NN | DO NOT substitute aggregate count for per-row CLOSED / OPEN status |
| CMD-13 | Decompose latency into Transport (ms) and Processing (ms) as separate columns | DO NOT use a single aggregate column; do not write "Negligible" as a latency value |
| CMD-14 | Resolve every FM-NN in T-09 as CONFIRMED, EXONERATED, or NEW post-trace only | DO NOT assign resolution status inline during stage trace sections |
| CMD-15 | T-PARITY must enumerate per-stage counts by Stage ID and show the arithmetic sum | DO NOT omit the per-stage enumeration or the sum assertion from T-PARITY |
| CMD-16 | Advance to next phase only after PG-NN gate shows GO on all rows | DO NOT begin a phase before its preceding PG-NN gate is complete and GO |

---

### PG-01: Phase 1 Gate

This gate verifies C-35, C-36, and C-37 before any pre-trace table is produced.
The Criterion Coverage column confirms which rubric criterion each row satisfies.

| Required Artifact | Population Status | CMD-NN Verified | Criterion Coverage | Go/No-Go |
|------------------|-------------------|-----------------|--------------------|---------|
| CMD register (CMD-01 through CMD-16, table format, CMD-NN identifiers) | | CMD-03 | C-37 | |
| T-PARITY declared as standalone scaffold row (not embedded in PG-NN) | | CMD-02 | C-36 | |
| PG-01 through PG-04 declared in scaffold with PG-NN identifiers and C-35 markers | | CMD-01 | C-35 | |
| Scaffold column labeled "Mandatory Columns (exact names)" | | CMD-04 | — | |
| T-01 through T-11 declared with Mandatory Columns populated | | — | — | |

Phase 2 may not begin if any row shows NO-GO. C-35/C-36/C-37 rows must all show GO
before the pre-trace work begins.

---

## PHASE 2: PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

| Entity | Description | Key Fields |
|--------|-------------|-----------|

List every in-scope domain entity before Stage 1. Finance / Operations / Commerce
vocabulary only — Invoice, PurchaseOrder, LedgerEntry, SKU, InventoryRecord, etc.
An entity introduced mid-trace without a T-01 entry is a CMD-07-adjacent gap.

---

### T-02: FM-NN Prediction Register

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

Minimum 3 entries. Expected Designation: the NH-NN or LP-NN this prediction produces
if it materializes. Resolve in T-09 only.

---

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

Transport and Processing are separate columns (CMD-13). entity.field: stub "→ back-fill
from T-06.[Stage ID]" until manifest produced. After T-04: "Domination analysis: T-08."

---

### T-08: SLA Domination Point

Standalone table — CMD-09 prohibits embedding in T-04. One row.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

---

### T-05: Incumbent Baseline

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 rows. IB-NN Step IDs must exist before any T-10 rows are written (CMD-10).

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | CMD-NN Verified | Go/No-Go |
|---------------|-------------------|-----------------|---------|
| T-01 Entity Inventory (domain names, no generic labels) | | — | |
| T-02 FM-NN Prediction Register (≥3 rows, Expected Designation populated) | | — | |
| T-03 Stage Enumeration | | — | |
| T-04 Boundary Inventory (numeric latency, no "Negligible," Transport+Processing separate) | | CMD-13 | |
| T-08 SLA Domination Point (standalone, not embedded) | | CMD-09 | |
| T-05 Incumbent Baseline (≥4 rows, IB-NN present) | | CMD-10 | |

Phase 3 may not begin if any row shows EMPTY or NO-GO.

---

## PHASE 3: STAGE TRACES

For each stage in T-03, produce one trace block. Append T-07 rows and state CHECKPOINT.
Back-fill T-04 entity.field from each stage's T-06 manifest.

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: [Stage 1: source fields entering. Other stages: diff from prior T-06
manifest. No changes: "verified: no field added, removed, renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest**

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotations** (back-fill T-04 entity.field after manifest):
- Error handling: [mechanism] OR [NH-NN — no handling — risk: {named risk}]
- Data loss point: [LP-NN — named loss scenario] OR [none]
- Latency: Transport (ms): X, Processing (ms): Y, Total: X+Y ms
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified separately]
- Active entities (T-01): [names]

---

**T-07 APPEND CHECKPOINT — [Stage ID]**

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If no intersections: `| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |`

State: "CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

---

*(Repeat stage block + T-07 APPEND CHECKPOINT for every stage in T-03.)*

---

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### PG-03: Phase 3 Gate

The CMD-NN Verified column confirms which CMD entries govern each artifact. A GO row
where the governing CMD entry was not satisfied is a structural inconsistency.

| Required Artifact | Completion Status | CMD-NN Verified | Go/No-Go |
|------------------|-------------------|-----------------|---------|
| T-06 manifests (one per stage) | | CMD-07 | |
| T-07 Append-Log consolidated (all stage checkpoints present) | | CMD-05 | |
| T-04 entity.field stubs back-filled (all boundaries) | | CMD-08 | |
| Schema diffs recorded for all stages (verified-unchanged where applicable) | | CMD-07 | |
| NH-NN and LP-NN identifiers assigned | | — | |
| All per-stage CHECKPOINT statements include [N] row count | | CMD-06 | |

Checkpoint sum verification: "sum = [N1 + N2 + ... + Nk]; T-07 consolidated rows = [M].
[MATCH / DISCREPANCY at Stage X — will FLAG in T-PARITY]."

Phase 4 may not begin if any row shows INCOMPLETE or NO-GO.

---

## PHASE 4: POST-TRACE RESOLUTION AND CLOSURE

### Pattern Trade-Off Analysis

Name one alternative architectural pattern. State ≥2 trade-off dimensions, at least
one quantified or qualified in domain terms.

---

### T-09: FM-NN Resolution Audit

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|---------------------|-------------------|

CONFIRMED: cite NH-NN or LP-NN. EXONERATED: state specific reason. NEW: assign identifier.

---

### T-10: Recovery Audit Table

One row per NH-NN / LP-NN. IB-NN Step Cited must name a specific T-05 step (CMD-11).

| NH/LP ID | Triggering Condition | Recovery Mechanism | IB-NN Step Cited | Boundary / Stage |
|----------|---------------------|--------------------|-----------------|------------------|

---

### T-PARITY: Count Parity Gate

C-36 artifact: this table satisfies C-36 by being pre-declared in the scaffold as T-PARITY
and by containing per-stage enumeration with explicit arithmetic. CMD-02 and CMD-15
prohibit substitution.

| Stage ID | N Rows This Stage | Running Total | GO / FLAG |
|----------|-------------------|---------------|-----------|

State: "Parity assertion: sum([N1] + [N2] + ... + [Nk]) == [M cumulative]. C-36 status:
[GO if match / FLAG at Stage X if discrepancy]. Parity gate pre-declared in scaffold
as T-PARITY — C-36 satisfied."

---

### T-11: Closure Gate

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | T-PARITY Status | Go/No-Go |
|---------------|-------------------|-----------------|---------|
| T-09 FM-NN Resolution Audit (all T-02 FM-NN resolved with status) | | — | |
| T-10 Recovery Audit Table (all NH-NN/LP-NN with IB-NN Step Cited) | | — | |
| T-PARITY Count Parity Gate (per-stage arithmetic, GO/FLAG, C-36 confirmed) | | [GO/FLAG] | |
| T-11 Closure Gate (one row per identifier, no aggregate substitute) | | — | |

State criterion coverage summary:
- C-35: PG-01–PG-04 pre-declared in scaffold with PG-NN identifiers — [SATISFIED / GAP]
- C-36: T-PARITY produced as standalone named table with arithmetic — [SATISFIED / GAP]
- C-37: CMD register pre-declared in scaffold with CMD-NN identifiers — [SATISFIED / GAP]
```
