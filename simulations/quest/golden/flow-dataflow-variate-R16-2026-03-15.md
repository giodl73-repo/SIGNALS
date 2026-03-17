# flow-dataflow — Round 16 Variations (Rubric v13)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v13 (C-01 through C-31, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

R16 targets the three criteria added in v13 from R15 evidence:

**C-29 — Inline FM-NN acknowledgment log as a named table artifact**: R15 V-02 introduced
the "Inline Acknowledgment Log" table (T-07) as an append-log pre-declared in the scaffold,
with stage trace blocks appending rows and a consolidated view produced after the final stage.
C-29 makes this the independently scorable structural requirement: the log must be a *named,
pre-declared append-log table* (not prose bullets), rows must *accumulate during the trace
sequence* (not be written post-trace), and the three-column format — FM-NN, stage + boundary,
deferral statement — must be explicit. All R16 variations pre-declare T-07 (or equivalent) in
the scaffold as the FM-NN Append-Log with these columns, and include a mandatory "APPEND"
instruction at each stage trace block.

**C-30 — SLA domination point as a named dedicated table artifact**: R15 variations produced
the domination point as a prose statement following the boundary inventory table, or as a
single-row inline table appended to the boundary inventory section. C-30 requires it to be a
*separate* named table, *pre-declared* in the scaffold, with a B[N]->[N+1] column that is
cross-referenceable from the boundary inventory (C-11) and latency decomposition (C-21). The
key failure pattern: an inline note appended to T-04 with the right three columns satisfies
C-22 but fails C-30 — separation and pre-declaration are the distinguishing requirements. All
R16 variations declare the domination point as its own T-NN entry in the scaffold, separate
from the boundary inventory, with a cross-reference note at the bottom of the boundary table.

**C-31 — Structured recovery framing template with actor and cadence fields**: R15 variations
produced a "T-05 Step ID Citation" column in the recovery audit table that satisfied C-16
(step-level citation for fallback anchor). C-31 upgrades this: every recovery row must carry a
*Recovery Framing* column containing all three fields — IB-NN step name, responsible actor,
and frequency/cadence — in the *same* cell using the template `Revert to [IB-NN Step Name]
performed by [Role] at [frequency/trigger]`. Distributing these fields across separate columns
does not satisfy C-31. All R16 variations replace the standalone T-05 Step ID column with a
Recovery Framing column carrying the full three-field template.

**What R15 established:**

- Phase-gate lifecycle (R15 V-01) produces the highest C-26/C-28 compliance because structural
  pressure to complete each gate prevents partial prediction registers and missing inline
  acknowledgments.
- Table-density format with running append-log (R15 V-02) produces the most complete C-28/C-29
  coverage because table rows are harder to omit silently than prose bullets.
- Baseline-first framing (R15 V-04) maximizes C-14/C-15/C-16 compliance because IB-NN step
  identifiers are established before any recovery prescriptions are written.
- Stage assignment maps in multi-role designs (R15 V-03) produce clean C-25 coverage because
  every stage has a designated manifest producer from the start.

**R16 hypothesis space:**

**H1 — Scaffold column-spec mandate forces C-29/C-30 separation (V-01)**
The scaffold table includes a "Mandatory Columns" column (exact names required). T-07 is
declared as "FM-NN Append-Log" with columns `FM-NN, Stage ID, Boundary / Condition, Deferral
Statement`. The SLA Domination Point is declared as T-08 — a separate entry with columns
`Domination Boundary, Exact Cumulative SLA%, Justification`. Hypothesis: declaring column
specs at the scaffold level prevents the model from producing a prose domination statement or
embedding acknowledgments as bullets, because the scaffold contract specifies what a valid
artifact looks like before any content is written.

**H2 — Phase-gate with explicit T-07 APPEND CHECKPOINT per stage (V-02)**
Extends the R15 V-01 phase-gate pattern with a mandatory "T-07 APPEND CHECKPOINT" declaration
between every stage and the next. The checkpoint requires the model to state how many rows were
appended and which FM-NN identifiers were acknowledged before proceeding. Hypothesis: an
explicit checkpoint *between* stages prevents the C-29 failure pattern where all acknowledgments
are written post-trace as a batch — the checkpoint enforces the "accumulate during trace sequence"
requirement structurally.

**H3 — Imperative command register with explicit DO NOT prohibitions (V-03)**
All instructions are numbered imperative commands (CMD-01 through CMD-13). Critical prohibition:
"DO NOT embed FM-NN acknowledgments as prose bullets — APPEND TABLE ROWS ONLY." Critical
separation command: "DO NOT embed the domination point in T-04 — produce T-08 as a standalone
table." Recovery framing command: "USE EXACTLY this template in the Recovery Framing cell:
Revert to [IB-NN Step Name] performed by [Role] at [frequency/trigger]." Hypothesis: explicit
prohibitions reduce the ambiguity that causes the most common C-29 and C-30 failure modes
better than descriptive instructions alone.

**H4 — Two-role design with handoff gate T-07 checkpoint (V-04)**
Finance Controller leads extract/validate stages. Operations Analyst leads transform/sync/load
stages. A handoff gate between roles requires confirmation that T-07 has been appended with all
Finance Controller stage intersections before Operations Analyst begins. The SLA Domination
Point (T-06) is Finance Controller's responsibility, produced separately after the boundary
inventory. Recovery Framing in T-11 uses the full three-field template. Hypothesis: the
handoff gate makes the append-log completeness check explicit and domain-grounded — "Finance
Controller confirms T-08 rows appended for all FC stages" is harder to omit than a generic
completion declaration.

**H5 — Inertia framing with Recovery Framing as lead column (V-05)**
The incumbent baseline (T-01) is produced before the scaffold, before the pipeline is named.
Recovery Framing is the *first substantive column* in the recovery audit table (after the
identifier), placing it before Triggering Condition and Recovery Mechanism — structural
ordering that forces the model to write the IB-NN step, actor, and cadence fields before
writing any technical recovery detail. The SLA Domination Point is T-06, separate from T-05
(boundary inventory), with a footnote at the bottom of T-05 cross-referencing T-06. Hypothesis:
leading with the incumbent baseline establishes all IB-NN identifiers before any recovery
framing is needed, and placing Recovery Framing as the leftmost non-identifier column creates
gravitational pressure toward C-31 compliance over C-16-only compliance.

---

## V-01 — Output Format: Scaffold Column Specification

**Axis**: Output format — the scaffold table includes a "Mandatory Columns" column declaring
exact column names for each output table. T-07 is pre-declared as FM-NN Append-Log with exact
columns. T-08 is pre-declared as SLA Domination Point — a separate artifact from the boundary
inventory. Recovery audit table includes a Recovery Framing column with template.
**Hypothesis**: declaring column specs in the scaffold contract prevents prose substitution
for C-29 and C-30 artifacts before any domain content is written.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for the following pipeline:

{topic}

Every table in your response must be pre-declared in STEP 0. A table that first appears
after STEP 0 is an undeclared artifact. Scaffold rows specify mandatory column names —
use exact names as declared.

---

## STEP 0: Output Scaffold

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| T-01 | Entity Inventory | Domain entities declared before any trace | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure mode predictions | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Named and sequenced pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Inter-stage boundaries: labels, latency decomposition, SLA% columns | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation operational process; IB-NN Step IDs cited in T-10 Recovery Framing | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-06 | Stage Exit Manifests | One sub-manifest per stage; typed field authority for T-04 back-fill and T-10 | field_name, TYPE(precision), Notes | T-03 |
| T-07 | FM-NN Append-Log | Running append-log that accumulates FM-NN acknowledgment rows during stage traces; rows appended per stage, not post-trace | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | SLA Domination Point | Standalone domination boundary table — separate from T-04; cross-referenceable from T-04 and T-06 latency totals | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution; consumes T-07 as evidence | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN / LP-NN recovery with mandatory Recovery Framing template column | Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary / Stage, Recovery Framing | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source (Stage / Boundary), T-10 Row, Status | T-10 |

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert. Single-role designs satisfy C-25 by default.

---

## T-01: Entity Inventory

List every in-scope domain entity using domain names (Invoice, PurchaseOrder, SKU,
LedgerEntry, etc.) — not "data," "records," or "payload." Stage traces and T-06 manifests
may only reference entities declared here.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

## T-02: FM-NN Prediction Register

Predict every anticipated failure mode before tracing any stage. Minimum 3 FM-NN entries.
FM-NN identifiers are resolved in T-09 only (post-trace). During stage traces, every FM-NN
whose anticipated event intersects a stage boundary is logged by APPENDING a row to T-07
using the column format declared in the scaffold — not as prose bullets within the stage
block. Do not commit to CONFIRMED / EXONERATED / NEW status in T-07.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

## T-03: Stage Enumeration

Name and sequence every pipeline stage. A stage referenced in traces but absent here fails.

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

## T-04: Boundary Inventory

Populate all columns for every inter-stage boundary. Rules:
- "Negligible" is not a valid latency value — use a numeric ms estimate.
- Transport (ms) and Processing (ms) are independent; their sum equals Total (ms).
- Entity at Risk must name a specific T-01 entity — not "data" or "records."
- entity.field is back-filled from T-06 after the relevant stage manifest is produced.
  Leave stub "→ back-fill from T-06.[Stage ID]" until the manifest is available.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

After completing T-04, add a cross-reference note: "→ Domination analysis: see T-08."
Then produce T-08 as a separate table below.

---

## T-08: SLA Domination Point

*Produced immediately after T-04 as a standalone artifact. Do not embed this table inside
T-04 or as an inline note appended to T-04. T-08 is pre-declared in the scaffold and must
be cross-referenceable by name from T-04 and from T-06 latency totals.*

Identify the single boundary where cumulative SLA% first exceeds 50% of the total SLA budget.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. Domination Boundary uses the B[N]->[N+1] label from T-04. Justification names
the specific domain operation that consumes the majority of the SLA budget (one sentence,
domain-grounded — name the operation, not a generic process label).

---

## T-05: Incumbent Baseline

Document the pre-automation operational process this pipeline replaces. Minimum 4 rows.
Step IDs use format IB-01, IB-02, etc. These IDs are cited in the Recovery Framing column
of T-10 — category-level process names without Step IDs are invalid citations.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

## Stage Traces (T-06, T-07)

For each stage in T-03, produce the following block. Every element is mandatory.

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: Describe fields entering this stage. Stage 1: describe source schema
fields. All other stages: diff from prior stage exit manifest — list fields added, removed,
renamed, or retyped. If no change: state "verified: no field added, removed, renamed, or
retyped."

**T-06.[Stage ID] — Typed Exit Manifest** (authority for entity.field back-fill in T-04
and entity.field citations in T-10):

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary [B-NN->NN] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario; "errors may occur" does not qualify]
- Latency: [value, range, or characterization: real-time / micro-batch / hourly / daily]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified — separate from normal-operation value]
- Active entities (from T-01): [names]

**T-04 back-fill**: After producing this manifest, update the entity.field stub for
boundary B[N]->[N+1] in T-04 using field names from T-06.[Stage ID].

**T-07 APPEND — FM-NN Append-Log update for this stage:**
Append one row to T-07 for every T-02 FM-NN whose anticipated event intersects this
stage's boundary or processing. Use the column format declared in the scaffold.
Do not use prose bullets — table rows only.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|
| [FM-NN] | [Stage ID] | [specific boundary label or condition] | Resolution deferred to T-09 (FM-NN Resolution Audit) |

If no T-02 predictions intersect this stage, append one row:
| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |

---

*(Repeat stage block for every stage in T-03.)*

---

After all stage traces, present the full consolidated T-07 Append-Log collecting all
appended rows.

## T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

## Pattern Trade-Off Analysis

Name one alternative architecture pattern for this pipeline type. State ≥2 trade-off
dimensions comparing it to the current pattern — at least one dimension quantified or
expressed in domain terms (e.g., "eliminates the 20-minute reconciliation window at cost
of 150ms additional CDC latency per Invoice update").

---

## T-10: Recovery Audit Table

One row per NH-NN and LP-NN. Missing rows are visible gaps.

The Recovery Framing column is mandatory on every row. Use exactly this template in the
Recovery Framing cell — all three components in the same cell:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

Rules:
- IB-NN Step Name must correspond to a row in T-05.
- Responsible Role must be a named operational role, not a generic label.
- frequency/trigger must specify when the fallback applies (e.g., "on each batch failure,"
  "daily at reconciliation window," "immediately on NH-NN trigger").
- A row that satisfies step citation but omits actor or cadence fails C-31.
- Distributing step, actor, and cadence across separate columns fails C-31.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

---

## T-09: FM-NN Resolution Audit

Consumes T-07. Produced after all stage traces are complete. Resolve every FM-NN from T-02.
One row per FM-NN. This section is the designated resolution target for all T-07 deferral
statements — do not assign resolution status before this section.

Status rules:
- CONFIRMED: prediction materialized — cite the specific NH-NN or LP-NN produced
- EXONERATED: prediction did not materialize — state the specific reason it was absent
- NEW: emerged during trace without prior prediction — assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

## T-11: Closure Gate

Per-identifier status for every NH-NN and LP-NN declared in stage traces. A summary count
("N of M covered") does not satisfy this requirement — one row per identifier.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching row in T-10. OPEN = no row — state reason.
```

---

## V-02 — Lifecycle Emphasis: Phase-Gated with Per-Stage T-07 Append Checkpoints

**Axis**: Lifecycle emphasis — six phases with explicit completion guards and a mandatory
"T-07 APPEND CHECKPOINT" declaration between every stage trace and the next. The checkpoint
requires stating which FM-NN entries were appended (or confirming no intersections) before
the next stage block begins.
**Hypothesis**: an explicit checkpoint *between* stages — not just at phase end — enforces
C-29's "rows must accumulate during the trace sequence" requirement structurally, preventing
the failure pattern where all FM-NN acknowledgments are batch-written after the final stage.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for:

{topic}

Work through the six phases below in strict sequence. Declare each phase complete before
beginning the next. Every section header is mandatory output. You may not advance past a
phase gate until the gate's completion conditions are met.

---

## PHASE 1 — OUTPUT SCAFFOLD

Before writing any domain content, declare every table and section that will appear in your
response. No table may appear for the first time after PHASE 2 begins.

| T# | Table Name | Purpose | Key Columns | Depends On |
|----|-----------|---------|-------------|------------|
| T-01 | Entity Inventory | Domain entities pre-declared before any trace | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure mode predictions; resolved in T-10 only | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Named, ordered pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Boundaries with latency decomposition and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | SLA Domination Point | Standalone domination boundary artifact — separate from T-04; cross-referenceable from T-04 and T-07 | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-06 | Incumbent Baseline | Pre-automation process; IB-NN Step IDs cited in T-11 Recovery Framing | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-07 | FM-NN Append-Log | Running append-log that accumulates rows during stage traces; one checkpoint per stage; consolidated after final stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | Stage Exit Manifests | One sub-manifest per stage; authority for entity.field citations | field_name, TYPE(precision), Notes | T-03 |
| T-09 | Pattern Trade-Off | Alternative pattern with ≥2 trade-off dimensions | Alternative Pattern, Trade-Off Dimension 1, Trade-Off Dimension 2 | — |
| T-10 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution; consumes T-07 | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-11 | Recovery Audit Table | NH-NN / LP-NN recovery with mandatory Recovery Framing template | Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary / Stage, Recovery Framing | T-04, T-06, T-08 |
| T-12 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source, T-11 Row, Status | T-11 |

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert.

**PHASE 1 COMPLETE when**: all 12 tables declared, no table appears post-scaffold.
State: "PHASE 1 COMPLETE."

---

## PHASE 2 — PRE-TRACE DECLARATIONS

Produce T-01 through T-06 in order. No stage trace may begin until all six tables are
complete and the PHASE 2 gate is declared.

### T-01: Entity Inventory

| Entity | Description | Key Fields |
|--------|-------------|-----------|

Entities not declared here may not appear in stage traces, manifests, or T-11 recovery rows.

### T-02: FM-NN Prediction Register

Minimum 3 FM-NN entries. FM-NN identifiers are resolved in T-10 (Phase 5) only — not during
stage traces. During Phase 3, FM-NN entries that intersect a stage boundary are logged by
appending rows to T-07 at the T-07 APPEND CHECKPOINT after each stage. Rows accumulate
during the trace sequence — do not defer all T-07 population to post-trace.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

### T-04: Boundary Inventory

"Negligible" is not a valid latency value. Transport and Processing are independent columns.
Entity at Risk names a specific T-01 entity. entity.field back-filled from T-08 during
Phase 3 — leave stub until the relevant manifest is produced.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

After completing T-04, add footnote: "→ Domination analysis: T-05." Then produce T-05.

### T-05: SLA Domination Point

*Produced immediately after T-04 as a separate table — do not embed inside T-04.*

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. B[N]->[N+1] label from T-04. Justification: one sentence naming the specific
domain operation that dominates the SLA budget.

### T-06: Incumbent Baseline

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 rows. Step IDs: IB-01, IB-02, etc. T-11 Recovery Framing cites specific Step IDs.

**PHASE 2 COMPLETE when**: T-01 through T-06 fully populated.
State: "PHASE 2 COMPLETE."

---

## PHASE 3 — STAGE TRACES

Produce one trace block per stage from T-03. After each stage block, declare the T-07 APPEND
CHECKPOINT before advancing to the next stage. T-07 rows must accumulate during this phase —
they are not consolidated until after the final stage.

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: [Fields added/removed/renamed/retyped vs. prior stage exit. Stage 1:
source schema. If unchanged: "verified: no field added, removed, renamed, or retyped."]

**T-08.[Stage ID] — Typed Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary [B-NN->NN] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate from normal operation]
- Active entities (from T-01): [names]

**T-04 back-fill**: Update entity.field stub for B[N]->[N+1] using T-08.[Stage ID] fields.

---

**T-07 APPEND CHECKPOINT — [Stage ID]**

Before advancing to the next stage, append all relevant FM-NN intersections to T-07.
Do not embed acknowledgments as prose bullets — table rows only.
State the count of rows appended this stage: "Appended N rows to T-07 at [Stage ID]."

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|
| [FM-NN] | [Stage ID] | [specific boundary label or condition] | Resolution deferred to T-10 (FM-NN Resolution Audit, Phase 5) |

If no T-02 prediction intersects this stage, append:
| (none) | [Stage ID] | No T-02 intersections at [Stage ID] | N/A |

State: "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

---

*(Repeat stage block + T-07 APPEND CHECKPOINT for every stage in T-03.)*

---

After the final stage, consolidate all appended T-07 rows:

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

**PHASE 3 COMPLETE when**: all T-03 stages traced, all T-08 manifests produced, T-04
entity.field stubs back-filled, T-07 consolidated with one row per intersection.
State: "PHASE 3 COMPLETE."

---

## PHASE 4 — PATTERN TRADE-OFF

### T-09: Pattern Trade-Off

Name one alternative architecture pattern. State ≥2 trade-off dimensions vs. the current
pattern — at least one quantified or expressed in domain terms.

| Alternative Pattern | Trade-Off Dimension 1 | Trade-Off Dimension 2 |
|--------------------|-----------------------|-----------------------|

State: "PHASE 4 COMPLETE."

---

## PHASE 5 — POST-TRACE RESOLUTION

### T-10: FM-NN Resolution Audit

Consumes T-07 consolidated log. Resolve every FM-NN from T-02. One row per FM-NN.
This is the designated resolution target for all T-07 deferral statements. Status rules:

- CONFIRMED: prediction materialized — cite the specific NH-NN or LP-NN produced
- EXONERATED: prediction did not materialize — state the specific reason it was absent
- NEW: emerged during trace without prior prediction — assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

### T-11: Recovery Audit Table

One row per NH-NN and LP-NN from Phase 3. Missing rows are visible gaps.

The Recovery Framing column is mandatory on every row. Template (all three fields in ONE cell):

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

- IB-NN Step Name must correspond to a T-06 row.
- Responsible Role names the operational actor (AP Clerk, Inventory Controller, etc.).
- frequency/trigger specifies when the fallback applies.
- A row satisfying step citation but omitting actor or cadence fails C-31.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

**PHASE 5 COMPLETE when**: T-10 and T-11 fully populated.
State: "PHASE 5 COMPLETE."

---

## PHASE 6 — CLOSURE GATE

### T-12: Closure Gate

Per-identifier status for every NH-NN and LP-NN declared in Phase 3. A summary count
does not satisfy this gate — one row per identifier. OPEN identifiers must include
a stated reason.

| Identifier | Source (Stage / Boundary) | T-11 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching row in T-11. OPEN = no row — state reason.

State: "TRACE COMPLETE."
```

---

## V-03 — Phrasing Register: Imperative Commands with Explicit Prohibitions

**Axis**: Phrasing register — all instructions are numbered imperative commands (CMD-01
through CMD-13). Critical prohibitions address C-29 and C-30 directly: "DO NOT use prose
bullets for FM-NN acknowledgments," "DO NOT embed the domination point in T-04." Recovery
framing template is presented as a mandatory command with exact syntax.
**Hypothesis**: explicit DO NOT constraints eliminate the ambiguity that causes C-29 and
C-30 failures more effectively than descriptive instructions, because they name the failure
pattern before the model reaches the decision point.

---

```
You are a Finance / Operations / Commerce data domain expert. Trace data through this
pipeline:

{topic}

Execute the numbered commands below in order. Each command specifies exactly what to
produce. DO NOT skip any command. DO NOT combine outputs designated as separate artifacts.

---

### CMD-01 — Declare the Output Scaffold

PRODUCE a scaffold table. Include: table number, table name, purpose, mandatory columns
(exact names), and dependencies.

DO NOT omit T-07 (FM-NN Append-Log) or T-08 (SLA Domination Point) from the scaffold.
These are structurally separate artifacts — they may not be merged into other tables.

Required scaffold rows (add rows if needed):

| T# | Table Name | Purpose | Mandatory Columns | Depends On |
|----|-----------|---------|-------------------|------------|
| T-01 | Entity Inventory | Domain entities | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace predictions | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Ordered pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Boundaries with latency and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-06 | Stage Exit Manifests | Typed field declarations | field_name, TYPE(precision), Notes | T-03 |
| T-07 | FM-NN Append-Log | Append-log accumulating during stage traces | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | SLA Domination Point | Separate domination boundary artifact | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN / LP-NN recovery with Recovery Framing | Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary / Stage, Recovery Framing | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source, T-10 Row, Status | T-10 |

---

### CMD-02 — Produce T-01: Entity Inventory

LIST every in-scope domain entity using domain names (Invoice, PurchaseOrder, SKU,
LedgerEntry, CostCenter, etc.).

DO NOT use generic labels: "data," "records," "payload," or "item."

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### CMD-03 — Produce T-02: FM-NN Prediction Register

PREDICT every anticipated failure mode before any stage trace begins. Minimum 3 entries.

DO NOT write CONFIRMED, EXONERATED, or NEW in this table.
DO NOT resolve FM-NN status here.
Resolution happens in T-09 only, after all stage traces are complete.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### CMD-04 — Produce T-03: Stage Enumeration

LIST every pipeline stage in sequence. A stage referenced later but absent here is
an undeclared stage.

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### CMD-05 — Produce T-04: Boundary Inventory

COMPLETE all columns for every inter-stage boundary.

- "Negligible" is NOT a valid latency value — use numeric ms estimates.
- Transport (ms) and Processing (ms) are independent — their sum equals Total (ms).
- Entity at Risk must name a specific T-01 entity.
- entity.field: leave stub "→ back-fill from T-06.[Stage ID]" until manifests are available.

After completing T-04, ADD a footnote: "→ Domination analysis: see T-08."

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### CMD-06 — Produce T-08: SLA Domination Point

PRODUCE T-08 immediately after T-04.

DO NOT embed this as a prose note appended to T-04.
DO NOT produce it as an inline sub-section of T-04.
T-08 is a separate named table, pre-declared in the scaffold.

Identify the single boundary where cumulative SLA% first exceeds 50% of the total budget.
T-08 is cross-referenceable from T-04 (via footnote) and from T-06 latency totals.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. Domination Boundary: B[N]->[N+1] label from T-04. Justification names the
specific domain operation that dominates (one sentence).

---

### CMD-07 — Produce T-05: Incumbent Baseline

LIST the pre-automation operational process this pipeline replaces. Minimum 4 rows.
Step IDs: IB-01, IB-02, etc. T-10 Recovery Framing must cite specific IB-NN Step IDs.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

### CMD-08 — Trace Each Stage

For every stage in T-03, EXECUTE sub-commands CMD-08a through CMD-08e in order.

**CMD-08a — Schema diff**
DESCRIBE fields entering this stage. Stage 1: describe source schema. Otherwise: diff
vs. prior stage exit — list fields added, removed, renamed, or retyped. If no change:
state "verified: no field added, removed, renamed, or retyped."

**CMD-08b — Produce T-06.[Stage ID]: Typed Exit Manifest**
DECLARE every output field with typed notation.

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**CMD-08c — Annotate boundary [B-NN->NN]**
PROVIDE for every boundary at this stage exit:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific description}]
- Data loss point: LP-NN — [specific named scenario; "errors may occur" does not qualify]
- Latency: [value, range, or characterization: real-time / micro-batch / hourly / daily]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate from normal-operation value]
- Active entities (from T-01): [names]

**CMD-08d — Back-fill T-04 entity.field stub**
UPDATE the entity.field stub for boundary B[N]->[N+1] in T-04 using field names from
T-06.[Stage ID]. Format: entity.field_name.

**CMD-08e — APPEND to T-07: FM-NN Append-Log**

DO NOT write FM-NN acknowledgments as prose bullets within the stage block.
APPEND TABLE ROWS ONLY.

For every FM-NN from T-02 whose anticipated event intersects this stage's boundary or
processing, append one row using exact T-07 column format:

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|
| [FM-NN] | [Stage ID] | [specific boundary label or condition] | Resolution deferred to T-09 (FM-NN Resolution Audit) |

If no T-02 prediction intersects this stage, append:
| (none) | [Stage ID] | No T-02 intersections at [Stage ID] | N/A |

DO NOT commit to CONFIRMED / EXONERATED / NEW status in this append block.

---

*(Execute CMD-08a through CMD-08e for every stage in T-03.)*

---

### CMD-09 — Consolidate T-07: FM-NN Append-Log

After the final stage, PRESENT the full consolidated T-07 table collecting all rows
appended in CMD-08e steps across all stages. This consolidated log is the input to T-09.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### CMD-10 — Pattern Trade-Off

NAME one alternative architecture pattern. STATE ≥2 trade-off dimensions vs. the
current pattern — at least one dimension quantified or expressed in domain terms.

---

### CMD-11 — Produce T-10: Recovery Audit Table

PRODUCE one row per NH-NN and LP-NN. Missing rows are visible gaps.

The Recovery Framing column is MANDATORY on every row. USE EXACTLY this template:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

RULES:
- All three fields (IB-NN step name, actor, cadence) MUST appear in the SAME Recovery
  Framing cell.
- DO NOT distribute step, actor, and cadence across separate columns.
- A row that satisfies step citation but omits actor or cadence FAILS.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

---

### CMD-12 — Produce T-09: FM-NN Resolution Audit

CONSUME T-07 consolidated log. RESOLVE every FM-NN from T-02. One row per FM-NN.

DO NOT assign resolution status before this command — T-07 deferral statements point here.

Status rules:
- CONFIRMED: cite the specific NH-NN or LP-NN produced
- EXONERATED: state the specific reason the failure mode was absent
- NEW: assign NH-NN or LP-NN retroactively with a formal identifier

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### CMD-13 — Produce T-11: Closure Gate

LIST every NH-NN and LP-NN declared in stage traces.

DO NOT produce a summary count — one row per identifier.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = T-10 row exists. OPEN = no row — state reason.
```

---

## V-04 — Combined: Role Sequence + Lifecycle Emphasis (Finance First, Operations Second)

**Axis**: Role sequence (Finance Controller leads extract/validate; Operations Analyst leads
transform/sync/load) combined with lifecycle emphasis (phase-gated with a handoff gate that
audits T-07 completeness across Finance Controller stages before Operations Analyst begins).
**Hypothesis**: The handoff gate makes FM-NN append-log completeness a named transfer
condition — "Finance Controller confirms T-07 rows appended for all FC stages" — which
is harder to omit than a generic completion declaration and enforces C-29 accumulation
before the role boundary is crossed.

---

```
This data flow trace is performed by two domain experts in sequence.

Finance Controller runs first: owns source extraction, validation, and schema authority
for Finance-side entities (Invoice, LedgerEntry, GL codes).

Operations Analyst runs second: owns transformation, synchronization, CDC mechanics,
and load stages.

Pipeline to trace: {topic}

---

## STEP 0: Output Scaffold and Stage Assignment

### Scaffold

| T# | Table Name | Purpose | Depends On |
|----|-----------|---------|-----------|
| T-01 | Entity Inventory | Domain entities; Finance Controller leads | — |
| T-02 | FM-NN Prediction Register | Pre-trace predictions from both roles | — |
| T-03 | Stage Enumeration | Named, ordered pipeline stages | — |
| T-04 | Stage Assignment Map | Every T-03 stage mapped to one named role | T-03 |
| T-05 | Boundary Inventory | Boundaries with labels, latency decomposition, SLA% | T-03 |
| T-06 | SLA Domination Point | Standalone domination artifact — separate from T-05; Finance Controller produces | T-05 |
| T-07 | Incumbent Baseline | Pre-automation process; IB-NN Step IDs cited in T-11 Recovery Framing | — |
| T-08 | FM-NN Append-Log | Append-log accumulating during both role sections; consolidated after Operations' final stage | T-02, T-03 |
| T-09 | Stage Exit Manifests | One sub-manifest per stage; typed field authority | T-03 |
| T-10 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution; consumes T-08 | T-02, T-08 |
| T-11 | Recovery Audit Table | NH-NN / LP-NN recovery with Recovery Framing template | T-05, T-07, T-09 |
| T-12 | Closure Gate | Per-identifier CLOSED / OPEN status | T-11 |

### Stage Assignment Map (T-04)

Produce T-04 after completing T-03. Every stage from T-03 must appear. A stage with
no assigned role is a structural gap.

| Stage ID | Stage Name | Assigned Role |
|----------|------------|--------------|

Finance Controller is assigned: source extraction, validation, and Finance-schema stages.
Operations Analyst is assigned: transformation, CDC, synchronization, and load stages.

---

## PRE-TRACE DECLARATIONS

### T-01: Entity Inventory (Finance Controller leads)

Finance Controller declares Finance-native entities (Invoice, LedgerEntry, PurchaseOrder,
CostCenter, GL code structure, etc.). Operations Analyst may add CDC/pipeline-internal
entities if distinct from Finance entities.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

### T-02: FM-NN Prediction Register (both roles contribute)

Finance Controller predicts Finance-domain failure modes (GL code truncation, invoice
amount overflow, approval status loss, period-close timing violations). Operations Analyst
predicts pipeline-mechanics failure modes (CDC offset gaps, null propagation, ordering
violations, idempotency failures). Minimum 4 FM-NN entries. FM-NN identifiers are
resolved in T-10 only.

During stage traces, FM-NN intersections are logged by APPENDING rows to T-08 — not
as prose bullets. Rows must accumulate during the trace sequence.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation | Predicting Role |
|-------|------------------|--------------------|---------------------|----------------|

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

After T-03, complete the Stage Assignment Map (T-04).

### T-05: Boundary Inventory

Finance Controller populates extract-side boundary rows. Operations Analyst populates
transform/load-side boundary rows. "Negligible" is not a valid latency value. entity.field
stubs back-filled from T-09 manifests during stage traces.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

After completing T-05, add footnote: "→ Domination analysis: T-06." Then produce T-06.

### T-06: SLA Domination Point (Finance Controller — SLA budget authority)

Produced immediately after T-05 as a SEPARATE table. Do not embed inside T-05.
Finance Controller identifies the single boundary where cumulative SLA% first exceeds
50% of the total budget. T-06 is cross-referenceable from T-05 and T-09 latency totals.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. Justification names the Finance-domain operation that dominates the SLA budget.

### T-07: Incumbent Baseline (Finance Controller)

Pre-automation process this pipeline replaces. T-11 Recovery Framing must cite specific
IB-NN Step IDs — category labels without Step IDs are invalid citations.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 rows. Step IDs: IB-01, IB-02, etc.

---

## ROLE SECTION 1: Finance Controller

Finance Controller traces every stage assigned to Finance Controller in T-04. Produce
the following block for each Finance Controller stage.

---

### Stage [Stage ID]: [Stage Name] — Finance Controller

**Schema diff**: [vs. prior stage exit. Stage 1: source schema. If unchanged: "verified:
no field added, removed, renamed, or retyped."]

**T-09.[Stage ID] — Typed Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary [B-NN->NN] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate]
- Active entities (from T-01): [names]

**T-05 back-fill**: Update entity.field stub for B[N]->[N+1] using T-09.[Stage ID] fields.

**T-08 APPEND** — FM-NN Append-Log update (TABLE ROWS ONLY — no prose bullets):

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|
| [FM-NN] | [Stage ID] | [boundary or condition] | Resolution deferred to T-10 (FM-NN Resolution Audit) |

---

*(Repeat for all Finance Controller stages from T-04.)*

---

## HANDOFF GATE

Before Operations Analyst begins, Finance Controller confirms the following:

1. T-08 append-log: confirm rows are present for all Finance Controller stages
   (or "no T-02 intersections" rows where applicable). State count: "T-08 has N rows
   from Finance Controller stages."
2. T-09 exit manifests: confirm all Finance Controller stage manifests are produced.
3. T-05 entity.field stubs: confirm all Finance Controller boundary stubs are back-filled.

State: "HANDOFF GATE PASSED — Operations Analyst begins."

---

## ROLE SECTION 2: Operations Analyst

Operations Analyst traces every stage assigned to Operations Analyst in T-04. Produce
the following block for each Operations Analyst stage.

---

### Stage [Stage ID]: [Stage Name] — Operations Analyst

**Schema diff**: [vs. Finance Controller's last exit manifest or prior Operations stage.
Note type coercions, field transformations, cardinality changes. If unchanged: "verified:
no field added, removed, renamed, or retyped."]

**T-09.[Stage ID] — Typed Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary [B-NN->NN] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate]
- Active entities (from T-01): [names]

**T-05 back-fill**: Update entity.field stub for B[N]->[N+1] using T-09.[Stage ID] fields.

**T-08 APPEND** — FM-NN Append-Log update (TABLE ROWS ONLY):

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

*(Repeat for all Operations Analyst stages from T-04.)*

---

## T-08: FM-NN Append-Log (Consolidated)

After Operations Analyst's final stage, consolidate all T-08 rows accumulated across
both role sections. Present the full accumulated table.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

## Pattern Trade-Off Analysis

Name one alternative architecture pattern. State ≥2 trade-off dimensions vs. the current
pipeline — at least one dimension quantified or expressed in domain terms.

---

## T-10: FM-NN Resolution Audit

Produced after all stage traces by both roles. Consumes T-08 consolidated log. Resolve
every FM-NN from T-02. One row per FM-NN.

Status rules:
- CONFIRMED: prediction materialized — cite specific NH-NN or LP-NN produced
- EXONERATED: prediction did not materialize — state specific reason it was absent
- NEW: emerged without prior prediction — assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-08 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

## T-11: Recovery Audit Table

One row per NH-NN and LP-NN from both role sections. Missing rows are visible gaps.

Recovery Framing is mandatory. Template (all three fields in ONE cell):

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

- IB-NN Step Name must correspond to a T-07 row.
- Responsible Role names the operational actor (AP Clerk, Inventory Controller, etc.).
- Frequency/trigger specifies when the fallback applies.
- Step, actor, and cadence must be in the same Recovery Framing cell — not separate columns.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

---

## T-12: Closure Gate

One row per identifier. No summary counts.

| Identifier | Source (Stage / Boundary) | T-11 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = T-11 row exists. OPEN = no row — state reason.
```

---

## V-05 — Combined: Inertia Framing + Output Format (Baseline-First, Recovery Framing as Lead Column)

**Axis**: Inertia framing (incumbent baseline is produced before the scaffold — the pipeline
is introduced as "the automated replacement for T-01") combined with output format (Recovery
Framing is the *first* substantive column in T-10, placed before Triggering Condition and
Recovery Mechanism, establishing the fallback contract before technical detail).
**Hypothesis**: producing T-01 before the scaffold ensures all IB-NN identifiers are
established before any downstream table references them; leading with Recovery Framing in
T-10's column order creates gravitational pressure toward C-31 compliance because the model
must write the actor and cadence fields before it can populate the technical recovery column.

---

```
You are a Finance / Operations / Commerce data domain expert tasked with tracing data through
a new automated pipeline that replaces an existing manual process. You will document what the
pipeline replaces before you describe the pipeline itself.

Pipeline to trace: {topic}

---

## BEFORE: Incumbent Process (T-01)

Before writing any scaffold, stage list, or pipeline description, document the
pre-automation operational process that this pipeline replaces. This is the recovery
anchor for every prescription you write later — every T-10 Recovery Framing entry will
cite a specific IB-NN Step ID from this table.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Step IDs: IB-01, IB-02, etc. Minimum 4 rows. Name real operational roles (AP Clerk,
Inventory Controller, Finance Analyst, Procurement Coordinator) — not generic labels.

---

## OUTPUT SCAFFOLD (T-00)

The incumbent baseline above is T-01. Declare every remaining table below. No table may
appear for the first time after Stage 1 trace begins.

| T# | Table Name | Purpose | Key Columns | Depends On |
|----|-----------|---------|-------------|------------|
| T-01 | Incumbent Baseline | Pre-automation process (already produced above) | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-02 | Entity Inventory | Domain entities; established before any trace | Entity, Description, Key Fields | — |
| T-03 | FM-NN Prediction Register | Pre-trace failure mode predictions | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-04 | Stage Enumeration | Named, ordered pipeline stages | Stage ID, Stage Name, Description | — |
| T-05 | Boundary Inventory | Boundaries with latency decomposition and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-04 |
| T-06 | SLA Domination Point | Standalone domination artifact — separate from T-05 | Domination Boundary, Exact Cumulative SLA%, Justification | T-05 |
| T-07 | Stage Exit Manifests | Typed field authority per stage; referenced by T-05 entity.field and T-10 | field_name, TYPE(precision), Notes | T-04 |
| T-08 | FM-NN Append-Log | Append-log accumulating during stage traces; rows appended per stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-03, T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution | FM-NN, Status, T-08 Rows Consulted, Evidence / Reason | T-03, T-08 |
| T-10 | Recovery Audit Table | NH-NN / LP-NN recovery; Recovery Framing is the first substantive column | Row, NH/LP ID, Recovery Framing, Triggering Condition, Recovery Mechanism, Boundary / Stage | T-01, T-05, T-07 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source, T-10 Row, Status | T-10 |

Note: T-10 places Recovery Framing before Triggering Condition. This ordering commits the
fallback contract (which T-01 step to revert to, who performs it, at what cadence) before
the technical recovery mechanism is described.

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert.

---

## T-02: Entity Inventory

List every in-scope domain entity using domain names. "Data" and "records" are not entity
names. Stage traces and T-07 manifests may only reference entities declared here.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

## T-03: FM-NN Prediction Register

Predict every anticipated failure mode before tracing any stage. Minimum 3 FM-NN entries.
FM-NN identifiers are resolved in T-09 only. During stage traces, intersecting FM-NN
entries are APPENDED as rows to T-08 — not as prose bullets within stage blocks.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

## T-04: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

## T-05: Boundary Inventory

"Negligible" is not a valid latency value. entity.field stubs back-filled from T-07
manifests during stage traces.

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

After completing T-05, add footnote: "→ Domination analysis: T-06." Then produce T-06.

---

## T-06: SLA Domination Point

Produced immediately after T-05 as a SEPARATE named table. Do not embed as prose annotation
or footnote within T-05. T-06 is cross-referenceable from T-05 (via footnote) and from
T-07 latency totals.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. Domination Boundary: B[N]->[N+1] label from T-05. Justification names the domain
operation that dominates the SLA budget (one sentence, domain-grounded).

---

## Stage Traces

For each stage in T-04, produce the following block. Every element is mandatory.

---

### Stage [Stage ID]: [Stage Name]

*This pipeline replaces T-01 step [most relevant IB-NN] at this stage. Keep that step
available when prescribing recovery for any handling gaps identified below.*

**Schema diff**: [vs. prior stage exit. Stage 1: source schema. If unchanged: "verified:
no field added, removed, renamed, or retyped."]

**T-07.[Stage ID] — Typed Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary [B-NN->NN] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate]
- Active entities (from T-02): [names]

**T-05 back-fill**: Update entity.field stub for B[N]->[N+1] using T-07.[Stage ID] fields.

**T-08 APPEND — FM-NN Append-Log** (TABLE ROWS ONLY — no prose bullets):
Append one row per T-03 FM-NN that intersects this stage. If none: append one row noting
no intersections at this stage.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|
| [FM-NN] | [Stage ID] | [specific condition] | Resolution deferred to T-09 (FM-NN Resolution Audit) |

---

*(Repeat for every stage in T-04.)*

---

## T-08: FM-NN Append-Log (Consolidated)

Full accumulated log from all stage trace APPEND blocks.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

## Pattern Trade-Off Analysis

Name one alternative architecture pattern. State ≥2 trade-off dimensions vs. the current
pattern — at least one quantified or expressed in domain terms relative to this scenario.

---

## T-10: Recovery Audit Table

One row per NH-NN and LP-NN. Missing rows are visible gaps.

**Column ordering**: Recovery Framing is the first substantive column after the identifier,
establishing the T-01 fallback contract before technical recovery detail. Use exactly this
template in the Recovery Framing cell:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

Rules:
- All three components (IB-NN step name, actor, cadence) must appear in the SAME
  Recovery Framing cell — not distributed across separate columns.
- IB-NN Step Name must correspond to a row in T-01.
- Responsible Role names the operational actor (AP Clerk, Inventory Controller, etc.).
- A row with step citation but no actor or cadence fails C-31.

| Row | NH/LP ID | Recovery Framing | Triggering Condition | Recovery Mechanism | Boundary / Stage |
|-----|----------|-----------------|---------------------|-------------------|-----------------|

---

## T-09: FM-NN Resolution Audit

Consumes T-08. Produced after all stage traces. Resolves every FM-NN from T-03.
One row per FM-NN. Status rules:

- CONFIRMED: cite specific NH-NN or LP-NN produced
- EXONERATED: state specific reason the failure mode was absent
- NEW: assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-08 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

## T-11: Closure Gate

One row per identifier. No summary counts.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = T-10 row exists. OPEN = no row — state reason.
```
