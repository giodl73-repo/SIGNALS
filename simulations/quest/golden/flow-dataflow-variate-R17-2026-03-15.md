# flow-dataflow — Round 17 Variations (Rubric v14)

**Skill**: flow-dataflow — Trace data through ETL pipelines, sync processes, CDX flows,
or dual-write patterns.
**Rubric**: v14 (C-01 through C-34, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Variation Design Notes

R17 targets the three criteria added in v14 from R16 evidence:

**C-32 — Explicit per-stage count statement in T-07 APPEND CHECKPOINT**: R16 V-02
introduced per-stage T-07 APPEND CHECKPOINT blocks and ended them with `State: "T-07
APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."` C-32 makes this count
statement independently scorable: the checkpoint must carry a row count, not just an
FM-NN identifier list. The key compliance risk is a checkpoint that names which FM-NN
entries were acknowledged but omits the count — this satisfies C-29 (rows are appended
per stage) but fails C-32 (accumulation is not numerically verified). R16 V-02 satisfied
C-32 via the quoted format; R16 V-01/V-03/V-04/V-05 did not consistently include the count
statement. All R17 variations use the exact format: `T-07 APPEND CHECKPOINT [Stage ID]
COMPLETE — [N] rows appended.`

**C-33 — Scaffold declares Mandatory Columns (exact names)**: R16 V-01 introduced a
"Mandatory Columns (exact names)" column in the scaffold table. C-33 makes this
independently scorable: the scaffold must declare exact column names for each output
table, and produced tables must use those exact names. The key gap in R16: V-02 used
`Key Columns` (descriptive, not binding) in the scaffold; V-03 through V-05 included
columns in scaffold but labeled them inconsistently. The compliance test is whether
column drift is structurally visible — a table with "T-07 Rows Consulted" in the scaffold
but "Evidence Source" in the produced artifact is a detectable mismatch under C-33.
All R17 variations use the header `Mandatory Columns (exact names)` and include a column-
match instruction.

**C-34 — Named phase-completion gate blocks**: R16 V-02 ended each phase with a prose
completion condition (`PHASE N COMPLETE when: [condition]. State: "PHASE N COMPLETE."`).
C-34 requires a *named gate block* — structurally separate from the phase's content
sections — that lists each required table for that phase by name, verifies each is
populated, and provides a per-artifact Go/No-Go determination. A prose completion
statement does not qualify. A gate block that names tables but omits population status
does not qualify. The gate must be a table or structured protocol where a missing entry
or empty cell is structurally visible — the inter-phase analogue of C-13 applied to
phase boundaries. All R17 variations produce named gate blocks using a Required Table |
Population Status | Go/No-Go column format, with explicit "Phase N+1 may not begin if
any row shows NO-GO" enforcement language.

---

**What R16 established:**

- Scaffold column-spec mandate (V-01) achieves C-33 when the column is labeled "Mandatory
  Columns (exact names)" and the table body uses exact-name cell values, not descriptions.
  A "Key Columns" label is not binding — the word "Mandatory" is load-bearing.
- Per-stage APPEND CHECKPOINT with count (V-02) satisfies C-32 when the exact format
  `[N] rows appended` appears. R16 V-02 is the only variation that satisfied C-32; all
  others acknowledged FM-NN entries without counting.
- Phase completion as prose (V-02) satisfies phasing discipline but does not satisfy C-34 —
  listing the gate condition in a sentence is not the same as a per-artifact verification
  table. C-34 is not satisfied by R16 V-02 as written.
- Imperative DO NOT prohibitions (V-03) reduce substitution failures for C-29/C-30 but
  do not structurally force gate-block production or count statements.
- Two-role handoff gate (V-04) is naturally gate-like but covers only the role boundary —
  not every inter-phase boundary. C-34 requires all phases, not just the handoff.
- Inertia-first framing (V-05) maximizes C-14/C-15/C-16 compliance but adds no structural
  mechanism for C-32 or C-34.

---

**R17 hypothesis space:**

**H1 — Scaffold column-spec + PG-NN gate table series (V-01)**
The scaffold is extended with PG-NN gate table rows (PG-01 through PG-04), each declared
as a named artifact. Gate tables appear at the end of each phase as verification tables
with columns: Required Artifact | Population Status | Go/No-Go. The Mandatory Columns
column in the scaffold declares exact column names for all T-NN and PG-NN artifacts.
Hypothesis: pre-declaring the gate tables in the scaffold creates a contractual obligation
to produce them — they become undeclared artifacts if absent, just like any T-NN entry.
This leverages C-24's navigational contract to enforce C-34.

**H2 — Phase-gated lifecycle with double-loop verification (V-02)**
Six phases. Each phase ends with a named gate block produced as a two-column verification
table (Per-Artifact GO/NO-GO status). Stage traces include both a per-stage T-07 APPEND
CHECKPOINT with count and a running-total accumulation note: `[N] rows this stage,
[M] total in T-07 as of [Stage ID]`. Phase 3 gate verifies count consistency: "T-07
accumulated [M] rows across all stages — consistent with per-stage checkpoint totals."
Hypothesis: the running total creates a self-auditing count chain — a discrepancy between
per-stage counts and the consolidated total is structurally visible in the Phase 3 gate,
catching silent batch-write violations that a single final count misses.

**H3 — Imperative command register with gate mandate and column mandate (V-03)**
CMD-01 through CMD-16. Three new commands target C-32/C-33/C-34: CMD-03 mandates
"Mandatory Columns (exact names)" scaffold column with binding enforcement language;
CMD-09 mandates per-stage count statement with exact quoted format; CMD-15 mandates
phase gate production with exact column names. Critical prohibition: "DO NOT advance
to Phase N+1 until the Phase N gate table shows GO for all rows." Hypothesis: explicit
DO NOT language applied to gate advancement — not just artifact production — creates
harder stopping points than descriptive lifecycle instructions.

**H4 — Two-role with role-boundary phase gates and per-role APPEND CHECKPOINT audit (V-04)**
Finance Controller handles extract and validate stages. Operations Analyst handles
transform, sync, and load stages. Each stage ends with a T-07 APPEND CHECKPOINT with
count. Two phase gates: Gate A (Finance Controller phase completion) and Gate B (Operations
Analyst phase completion). Gate A explicitly verifies T-07 row count parity with the
number of FC-stage checkpoints before the handoff. Scaffold uses Mandatory Columns.
Hypothesis: binding the phase gate to a role handoff creates motivating context — the
Finance Controller cannot transfer to the Operations Analyst without confirming all T-07
rows are present. Count parity check in Gate A catches the C-32 failure mode (checkpoint
stated but count omitted) before the role transition.

**H5 — Inertia-first framing with baseline-anchored phase gates and count-chain (V-05)**
The incumbent baseline (T-01 in this design) is produced before the scaffold and before
any FM-NN predictions. Phase gates are anchored to incumbent baseline step availability:
Phase 2 gate verifies that IB-NN step identifiers are populated before any recovery
prescriptions are written (Phase 5). Phase 3 gate carries both artifact verification and
a T-07 count chain column: "Running Total at End of [Stage ID]" must match the declared
[N] value from each checkpoint. Recovery Framing is the leftmost non-identifier column
in T-10, creating structural pressure to cite IB-NN steps before writing technical
recovery detail. Hypothesis: leading with the incumbent baseline before the scaffold
establishes IB-NN identifiers as the semantic anchor for the entire trace; phase gates
that verify IB-NN availability block the recovery phase from beginning without anchors,
which addresses the most frequent C-14/C-15/C-16 partial failure pattern.

---

## V-01 — Output Format: Pre-Declared Gate Tables + Mandatory Columns Scaffold

**Axis**: Output format — the scaffold includes both T-NN output tables and PG-NN gate
tables as pre-declared artifacts. The scaffold Mandatory Columns column declares exact
column names binding on all produced tables. Phase gate blocks are verification tables
pre-registered in the scaffold under PG-NN identifiers, preventing their absence from
being silent.
**Hypothesis**: declaring gate tables in the scaffold under their own T-NN-style
identifiers leverages C-24's navigational contract to enforce C-34 — a missing gate
table is an undeclared artifact gap, not just a missed procedure.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for the following pipeline:

{topic}

Every table in your response must be pre-declared in STEP 0. A table that first appears
after STEP 0 is an undeclared artifact. Use exact column names as declared in the
Mandatory Columns column — column names in produced tables must match scaffold declarations.

---

## STEP 0: Output Scaffold

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| T-01 | Entity Inventory | Domain entities; trace references only entities declared here | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure mode predictions; resolved in T-09 only | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Named and sequenced pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Inter-stage boundaries with latency decomposition and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process; IB-NN Step IDs cited in T-10 Recovery Framing | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-06 | Stage Exit Manifests | One sub-manifest per stage; typed field authority for T-04 and T-10 | field_name, TYPE(precision), Notes | T-03 |
| T-07 | FM-NN Append-Log | Append-log accumulating FM-NN rows during stage traces; count stated per stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | SLA Domination Point | Standalone domination boundary artifact — separate from T-04 | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution; consumes T-07 | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN / LP-NN recovery with mandatory Recovery Framing template | Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary / Stage, Recovery Framing | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status for every NH-NN and LP-NN | Identifier, Source (Stage / Boundary), T-10 Row, Status | T-10 |
| PG-01 | Phase 1 Gate | Scaffold completeness and column-match verification | Required Artifact, Declaration Status, Column-Match Status, Go/No-Go | T-01–T-11, PG-01–PG-04 |
| PG-02 | Phase 2 Gate | Pre-trace table population verification before Stage 1 begins | Required Table, Population Status, Go/No-Go | T-01–T-05, T-08 |
| PG-03 | Phase 3 Gate | Stage trace completeness and T-07 count verification | Required Artifact, Completion Status, Go/No-Go | T-03, T-06, T-07 |
| PG-04 | Phase 4 Gate | Post-trace resolution completeness verification | Required Table, Population Status, Go/No-Go | T-09, T-10, T-11 |

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert. Single-role designs satisfy C-25 by default.

---

## PHASE 1: SCAFFOLD VALIDATION

### PG-01: Phase 1 Gate

Verify that all artifacts above are declared with Mandatory Columns populated.

| Required Artifact | Declaration Status | Column-Match Status | Go/No-Go |
|------------------|--------------------|---------------------|---------|
| T-01 Entity Inventory | | | |
| T-02 FM-NN Prediction Register | | | |
| T-03 Stage Enumeration | | | |
| T-04 Boundary Inventory | | | |
| T-05 Incumbent Baseline | | | |
| T-06 Stage Exit Manifests | | | |
| T-07 FM-NN Append-Log — declared separate from stage sections | | | |
| T-08 SLA Domination Point — declared separate from T-04 | | | |
| T-09 FM-NN Resolution Audit | | | |
| T-10 Recovery Audit Table — Recovery Framing column declared | | | |
| T-11 Closure Gate | | | |
| PG-02 through PG-04 gate tables declared | | | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2: PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

List every in-scope domain entity using domain names (Invoice, PurchaseOrder, SKU,
LedgerEntry, CostCenter, etc.) — not "data," "records," or "payload." Stage traces,
T-06 manifests, and T-10 recovery rows reference only entities declared here.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### T-02: FM-NN Prediction Register

Predict every anticipated failure mode before tracing any stage. Minimum 3 entries.
Resolve in T-09 only. During stage traces, FM-NN intersections are logged by appending
rows to T-07 — not as prose bullets within stage sections.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### T-03: Stage Enumeration

Name and sequence every pipeline stage. A stage referenced in traces but absent here
is an undeclared stage and fails.

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### T-04: Boundary Inventory

Complete all columns for every inter-stage boundary. Rules:
- "Negligible" is not a valid latency value — use numeric ms estimates.
- Transport (ms) and Processing (ms) are independent; their sum equals Total (ms).
- Entity at Risk names a specific T-01 entity — not "data" or "records."
- entity.field: leave stub "→ back-fill from T-06.[Stage ID]" until the manifest exists.
- Boundary labels: B[N]->[N+1] format (e.g., B1->2, B2->3).

After completing T-04, add footnote: "→ Domination analysis: see T-08."

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### T-08: SLA Domination Point

*Produced immediately after T-04 as a standalone table. Do not embed inside T-04 or
append as an inline note to T-04. T-08 is a pre-declared artifact cross-referenceable
from T-04 and T-06 latency totals.*

Identify the single boundary where cumulative SLA% first exceeds 50% of the total SLA
budget.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. Domination Boundary: B[N]->[N+1] label from T-04. Justification: one sentence
naming the specific domain operation that consumes the majority of the SLA budget.

---

### T-05: Incumbent Baseline

Document the pre-automation operational process this pipeline replaces. Minimum 4 rows.
Step IDs: IB-01, IB-02, etc. T-10 Recovery Framing must cite specific Step IDs — citing
the process category without a step identifier does not qualify.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

### PG-02: Phase 2 Gate

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-01 Entity Inventory | | |
| T-02 FM-NN Prediction Register (≥3 rows) | | |
| T-03 Stage Enumeration | | |
| T-04 Boundary Inventory (all columns populated) | | |
| T-08 SLA Domination Point (produced as separate table, not embedded) | | |
| T-05 Incumbent Baseline (≥4 rows, IB-NN step identifiers present) | | |

Phase 3 may not begin if any row shows EMPTY or NO-GO. State the actual population
status for each row based on your output above.

---

## PHASE 3: STAGE TRACES

For each stage in T-03, produce one trace block. After each block, produce a T-07 APPEND
CHECKPOINT — count stated before advancing to the next stage.

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: [Fields entering this stage. Stage 1: source schema fields. All other
stages: diff from prior T-06 exit manifest — fields added, removed, renamed, or retyped.
If unchanged: "verified: no field added, removed, renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest** (authority for entity.field back-fill in T-04
and field citations in T-10):

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario; "errors may occur" does not qualify]
- Latency: [value, range, or characterization: real-time / micro-batch / hourly / daily]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified — separate from normal-operation value]
- Active entities (from T-01): [names]

**T-04 back-fill**: Update the entity.field stub for B[N]->[N+1] in T-04 using field
names from T-06.[Stage ID].

---

**T-07 APPEND CHECKPOINT — [Stage ID]**

Append all T-02 FM-NN intersections for this stage to T-07. Use table rows only —
not prose bullets within this section.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If no T-02 prediction intersects this stage:
| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |

State: "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

---

*(Repeat stage block + T-07 APPEND CHECKPOINT for every stage in T-03.)*

---

After the final stage, consolidate all appended T-07 rows:

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### PG-03: Phase 3 Gate

| Required Artifact | Completion Status | Go/No-Go |
|-------------------|------------------|---------|
| All T-03 stages traced (one block per stage in T-03) | | |
| All T-06.[Stage ID] typed manifests produced | | |
| All T-04 entity.field stubs back-filled | | |
| T-07 APPEND CHECKPOINT declared after every stage (count stated) | | |
| T-07 Append-Log consolidated (one row per FM-NN / stage intersection) | | |

Phase 4 may not begin if any row shows INCOMPLETE or NO-GO.

---

## PHASE 4: PATTERN TRADE-OFF

Name one alternative architecture pattern for this pipeline type. State ≥2 trade-off
dimensions comparing it to the current pattern — at least one quantified or expressed
in domain terms (e.g., "eliminates the 20-minute reconciliation window at cost of 150ms
additional CDC latency per Invoice update").

---

## PHASE 5: POST-TRACE RESOLUTION AND RECOVERY

### T-09: FM-NN Resolution Audit

Consumes T-07 consolidated. Resolve every FM-NN from T-02. One row per FM-NN. This
section is the designated resolution target for all T-07 deferral statements.

- CONFIRMED: prediction materialized — cite the specific NH-NN or LP-NN produced
- EXONERATED: prediction did not materialize — state the specific reason it was absent
- NEW: emerged during trace without prior prediction — assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### T-10: Recovery Audit Table

One row per NH-NN and LP-NN from Phase 3. Missing rows are visible gaps.

Recovery Framing column — mandatory on every row. All three fields in ONE cell:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

- IB-NN Step Name must correspond to a T-05 row.
- Responsible Role is a named operational actor (AP Clerk, Inventory Controller, etc.).
- frequency/trigger specifies when the fallback applies.
- Satisfying step citation but omitting actor or cadence fails.
- Distributing step, actor, and cadence across separate columns fails.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

---

### PG-04: Phase 4 Gate

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-09 FM-NN Resolution Audit (every T-02 FM-NN resolved) | | |
| T-10 Recovery Audit Table (one row per NH-NN and LP-NN) | | |
| T-10 Recovery Framing column (all three fields in each row) | | |

Phase 6 may not begin if any row shows EMPTY or NO-GO.

---

## PHASE 6: CLOSURE GATE

### T-11: Closure Gate

Per-identifier status for every NH-NN and LP-NN declared in Phase 3. A summary count
("N of M covered") does not satisfy this gate — one row per identifier.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching row in T-10. OPEN = no row — state reason.

State: "TRACE COMPLETE."
```

---

## V-02 — Lifecycle Emphasis: Phase-Gated with Running Count-Chain Verification

**Axis**: Lifecycle emphasis — six phases with named gate tables at the end of each phase.
Stage traces include both a per-stage T-07 APPEND CHECKPOINT with count and a running
total annotation: `[N] rows this stage, [M] total in T-07 as of [Stage ID]`. The Phase 3
gate carries a count-chain verification column confirming that per-stage checkpoint totals
sum to the consolidated T-07 row count.
**Hypothesis**: a running total in the checkpoint creates a self-auditing count chain —
a mismatch between per-stage counts and the consolidated total is structurally visible
in the Phase 3 gate, catching silent batch-write violations that a single final count
misses.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for:

{topic}

Work through the six phases below in strict sequence. Each phase ends with a named gate
table. The gate table lists every required artifact for that phase by name, states its
population status, and assigns a Go/No-Go. Do not advance to the next phase until all
gate rows show GO. Every section header is mandatory output.

---

## PHASE 1 — OUTPUT SCAFFOLD

Before writing any domain content, declare every table and section in your response.
No table may first appear after PHASE 2 begins.

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| T-01 | Entity Inventory | Domain entities pre-declared before any trace | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure mode predictions; resolved in T-10 only | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Named, ordered pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Boundaries with latency decomposition and SLA% columns | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | SLA Domination Point | Standalone domination artifact — separate from T-04 | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-06 | Incumbent Baseline | Pre-automation process; IB-NN Step IDs cited in T-11 Recovery Framing | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-07 | FM-NN Append-Log | Running append-log; one T-07 APPEND CHECKPOINT per stage with count and running total | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | Stage Exit Manifests | One sub-manifest per stage; typed field authority | field_name, TYPE(precision), Notes | T-03 |
| T-09 | Pattern Trade-Off | Alternative pattern with ≥2 trade-off dimensions | Alternative Pattern, Trade-Off Dimension 1, Trade-Off Dimension 2 | — |
| T-10 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution; consumes T-07 | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-11 | Recovery Audit Table | NH-NN / LP-NN recovery with mandatory Recovery Framing template | Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary / Stage, Recovery Framing | T-04, T-06, T-08 |
| T-12 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source, T-11 Row, Status | T-11 |

Stage assignment: single-role design — all stages assigned to Finance / Operations /
Commerce data domain expert.

### PHASE 1 GATE

| Required Artifact | Declaration Status | Column-Match Status | Go/No-Go |
|------------------|--------------------|---------------------|---------|
| All 12 T-NN tables declared | | | |
| T-05 SLA Domination Point declared separately from T-04 | | | |
| T-07 FM-NN Append-Log declared with "Mandatory Columns" header | | | |
| T-11 Recovery Audit Table — Recovery Framing column declared | | | |

Phase 2 may not begin if any row shows NO-GO.

---

## PHASE 2 — PRE-TRACE DECLARATIONS

### T-01: Entity Inventory

| Entity | Description | Key Fields |
|--------|-------------|-----------|

Entities not declared here may not appear in stage traces, T-08 manifests, or T-11.

### T-02: FM-NN Prediction Register

Minimum 3 FM-NN entries. Resolution in T-10 only — not during stage traces. During Phase
3, FM-NN entries intersecting a stage boundary are logged by appending rows to T-07.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

### T-04: Boundary Inventory

"Negligible" is invalid — use numeric ms estimates. Transport and Processing are
independent columns. Entity at Risk: specific T-01 entity. entity.field: stub
"→ back-fill from T-08.[Stage ID]" until manifest produced. Boundary labels: B[N]->[N+1].

After completing T-04, add footnote: "→ Domination analysis: T-05."

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

### T-05: SLA Domination Point

*Produced immediately after T-04 as a separate table — do not embed inside T-04.*

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. B[N]->[N+1] label from T-04. Justification: one sentence naming the specific
domain operation that dominates the SLA budget.

### T-06: Incumbent Baseline

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 rows. Step IDs: IB-01, IB-02, etc. T-11 Recovery Framing cites specific IDs.

### PHASE 2 GATE

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-01 Entity Inventory | | |
| T-02 FM-NN Prediction Register (≥3 rows) | | |
| T-03 Stage Enumeration | | |
| T-04 Boundary Inventory (all columns) | | |
| T-05 SLA Domination Point (separate table, not in T-04) | | |
| T-06 Incumbent Baseline (≥4 rows, IB-NN IDs present) | | |

Phase 3 may not begin if any row shows EMPTY or NO-GO.

---

## PHASE 3 — STAGE TRACES

Produce one trace block per stage from T-03. After each block, declare the T-07 APPEND
CHECKPOINT with a per-stage count and a running total before advancing to the next stage.

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: [Entering schema. Stage 1: source fields. Later stages: diff from
prior T-08 exit manifest. If unchanged: "verified: no field added, removed, renamed,
or retyped."]

**T-08.[Stage ID] — Typed Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate from normal operation]
- Active entities (from T-01): [names]

**T-04 back-fill**: Update entity.field stub for B[N]->[N+1] using T-08.[Stage ID] fields.

---

**T-07 APPEND CHECKPOINT — [Stage ID]**

Append all T-02 FM-NN intersections for this stage. Table rows only — not prose bullets.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If no T-02 prediction intersects this stage:
| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |

State: "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended this stage,
[M] total rows in T-07 as of [Stage ID]."

---

*(Repeat stage block + T-07 APPEND CHECKPOINT for every stage in T-03.)*

---

After the final stage, consolidate all appended T-07 rows:

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

### PHASE 3 GATE

| Required Artifact | Completion Status | Count Verified | Go/No-Go |
|-------------------|------------------|----------------|---------|
| All T-03 stages traced | | N/A | |
| All T-08.[Stage ID] typed manifests produced | | N/A | |
| All T-04 entity.field stubs back-filled | | N/A | |
| T-07 APPEND CHECKPOINT declared after every stage | | N/A | |
| T-07 consolidated row count matches sum of per-stage checkpoint counts | | [M total = sum of all [N] values] | |

Phase 4 may not begin if any row shows INCOMPLETE, MISMATCH, or NO-GO.

---

## PHASE 4 — PATTERN TRADE-OFF

### T-09: Pattern Trade-Off

Name one alternative architecture pattern. State ≥2 trade-off dimensions vs. the current
pattern — at least one quantified or expressed in domain terms.

| Alternative Pattern | Trade-Off Dimension 1 | Trade-Off Dimension 2 |
|--------------------|-----------------------|-----------------------|

### PHASE 4 GATE

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-09 Pattern Trade-Off (≥2 trade-off dimensions, ≥1 quantified or domain-grounded) | | |

Phase 5 may not begin if any row shows EMPTY or NO-GO.

---

## PHASE 5 — POST-TRACE RESOLUTION

### T-10: FM-NN Resolution Audit

Consumes T-07 consolidated. Resolve every FM-NN from T-02. One row per FM-NN.
This section is the designated resolution target for all T-07 deferral statements.

- CONFIRMED: prediction materialized — cite the specific NH-NN or LP-NN produced
- EXONERATED: prediction did not materialize — state the specific reason it was absent
- NEW: emerged during trace — assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

### T-11: Recovery Audit Table

One row per NH-NN and LP-NN from Phase 3. Missing rows are visible gaps.

Recovery Framing column — mandatory on every row. All three fields in ONE cell:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

- IB-NN Step Name: corresponds to a T-06 row.
- Responsible Role: named operational actor.
- frequency/trigger: when the fallback applies.
- Satisfying step citation but omitting actor or cadence fails.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

### PHASE 5 GATE

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-10 FM-NN Resolution Audit (all T-02 FM-NN entries resolved) | | |
| T-11 Recovery Audit Table (one row per NH-NN and LP-NN) | | |
| T-11 Recovery Framing column (all three fields in each row) | | |

Phase 6 may not begin if any row shows EMPTY or NO-GO.

---

## PHASE 6 — CLOSURE GATE

### T-12: Closure Gate

Per-identifier status for every NH-NN and LP-NN from Phase 3. A summary count does not
satisfy this requirement — one row per identifier.

| Identifier | Source (Stage / Boundary) | T-11 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching row in T-11. OPEN = no row — state reason.

### PHASE 6 GATE

| Required Artifact | Completion Status | Go/No-Go |
|-------------------|------------------|---------|
| T-12 Closure Gate (one row per NH-NN and LP-NN) | | |
| All OPEN identifiers include a stated reason | | |

State: "TRACE COMPLETE."
```

---

## V-03 — Phrasing Register: Imperative Commands with Gate Mandate and Column Mandate

**Axis**: Phrasing register — all instructions are numbered imperative commands (CMD-01
through CMD-16). Three new commands target C-32/C-33/C-34 directly: CMD-03 mandates
the Mandatory Columns scaffold header; CMD-09 mandates the count statement with exact
quoted format; CMD-14 mandates phase gate production with exact column names and
advancement prohibition. Critical DO NOT constraints address gate-skip behavior and
count omission.
**Hypothesis**: DO NOT applied to gate advancement — not just artifact production —
creates harder stopping points than descriptive lifecycle instructions because it names
the advancement failure before the model reaches the phase boundary.

---

```
You are a Finance / Operations / Commerce data domain expert. Trace data through this
pipeline:

{topic}

Execute the numbered commands below in order. Each command specifies exactly what to
produce. DO NOT skip any command. DO NOT advance past a GATE command until the gate
table shows GO for all rows.

---

### CMD-01 — Produce the Output Scaffold

PRODUCE a scaffold table with columns: T#, Table Name, Purpose, Mandatory Columns (exact
names), Depends On.

DO NOT use "Key Columns" or "Columns" as the column header — the header must read
"Mandatory Columns (exact names)" and the cell values must be exact column names.

Required rows (add rows if needed for the pipeline):

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| T-01 | Entity Inventory | Domain entities | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace predictions | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Ordered pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Boundaries with latency and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | Incumbent Baseline | Pre-automation process | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-06 | Stage Exit Manifests | Typed field declarations per stage | field_name, TYPE(precision), Notes | T-03 |
| T-07 | FM-NN Append-Log | Append-log accumulating during stage traces | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | SLA Domination Point | Separate domination boundary artifact | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-09 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-10 | Recovery Audit Table | NH-NN / LP-NN recovery with Recovery Framing | Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary / Stage, Recovery Framing | T-04, T-05, T-06 |
| T-11 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source, T-10 Row, Status | T-10 |

---

### CMD-02 — GATE: Scaffold Completeness

PRODUCE a gate table:

| Required Artifact | Declaration Status | Column-Match Status | Go/No-Go |
|------------------|--------------------|---------------------|---------|
| T-07 FM-NN Append-Log declared in scaffold | | Mandatory Columns (exact names) header used | |
| T-08 SLA Domination Point declared separate from T-04 | | | |
| T-10 Recovery Framing column declared in scaffold | | | |

DO NOT proceed to CMD-03 if any row shows NO-GO.

---

### CMD-03 — Produce T-01: Entity Inventory

LIST every in-scope domain entity by domain name (Invoice, PurchaseOrder, SKU, etc.).

DO NOT use: "data," "records," "payload," "item," or "entity" as an entity name.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

---

### CMD-04 — Produce T-02: FM-NN Prediction Register

PREDICT every anticipated failure mode before any stage trace. Minimum 3 entries.

DO NOT assign CONFIRMED, EXONERATED, or NEW status here.
DO NOT resolve FM-NN entries before CMD-12.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

---

### CMD-05 — Produce T-03: Stage Enumeration

LIST every pipeline stage in sequence.

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

---

### CMD-06 — Produce T-04: Boundary Inventory

COMPLETE all columns per boundary.

DO NOT use "Negligible" as a latency value — use numeric ms estimates.
Transport (ms) and Processing (ms) are independent — their sum equals Total (ms).
Entity at Risk: specific T-01 entity name only.
entity.field: stub "→ back-fill from T-06.[Stage ID]" until the manifest is available.
Boundary label format: B[N]->[N+1].

ADD a footnote after completing T-04: "→ Domination analysis: see T-08."

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

---

### CMD-07 — Produce T-08: SLA Domination Point

PRODUCE T-08 as a separate table immediately after T-04.

DO NOT embed T-08 as a prose note appended to T-04.
DO NOT produce T-08 as an inline row within T-04.
T-08 is a pre-declared artifact — it must be produced as a standalone table.

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. B[N]->[N+1] label from T-04. Justification: one sentence naming the specific
domain operation consuming the majority of the SLA budget.

---

### CMD-08 — Produce T-05: Incumbent Baseline

LIST the pre-automation operational process this pipeline replaces. Minimum 4 rows.

Step IDs: IB-01, IB-02, etc. T-10 Recovery Framing cites these IDs — a row without
a step ID cannot be cited.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

### CMD-09 — GATE: Pre-Trace Completeness

PRODUCE a gate table:

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-01 Entity Inventory | | |
| T-02 FM-NN Prediction Register (≥3 rows) | | |
| T-03 Stage Enumeration | | |
| T-04 Boundary Inventory (all columns populated) | | |
| T-08 SLA Domination Point (separate table, not embedded) | | |
| T-05 Incumbent Baseline (≥4 rows, IB-NN IDs present) | | |

DO NOT proceed to CMD-10 if any row shows EMPTY or NO-GO.

---

### CMD-10 — Produce Stage Traces

For each stage in T-03, produce a stage block with:

(a) Schema diff from prior stage exit. Stage 1: source schema. If no change: "verified:
no field added, removed, renamed, or retyped."

(b) T-06.[Stage ID] — Typed Exit Manifest:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

(c) Boundary B[N]->[N+1] annotation:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate from normal operation]
- Active entities (from T-01): [names]

(d) T-04 back-fill: update entity.field stub for B[N]->[N+1].

---

### CMD-11 — T-07 APPEND CHECKPOINT (after each stage in CMD-10)

After each stage block, PRODUCE a T-07 APPEND CHECKPOINT:

APPEND FM-NN intersections as table rows — DO NOT use prose bullets.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If no T-02 prediction intersects this stage: append a single (none) row.

STATE exactly: "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

DO NOT omit the count statement. DO NOT substitute a list of FM-NN identifiers for a
count. "[N] rows appended" is mandatory — it is not optional descriptive text.

Repeat CMD-10 + CMD-11 for every stage in T-03.

---

### CMD-12 — Consolidate T-07

After the final stage, PRODUCE T-07 consolidated:

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### CMD-13 — GATE: Stage Trace Completeness

PRODUCE a gate table:

| Required Artifact | Completion Status | Go/No-Go |
|-------------------|------------------|---------|
| All T-03 stages traced (one block per stage) | | |
| All T-06.[Stage ID] manifests produced | | |
| All T-04 entity.field stubs back-filled | | |
| T-07 APPEND CHECKPOINT declared after every stage (count stated) | | |
| T-07 consolidated | | |

DO NOT proceed to CMD-14 if any row shows INCOMPLETE or NO-GO.

---

### CMD-14 — Pattern Trade-Off

NAME one alternative architecture pattern. STATE ≥2 trade-off dimensions — at least one
quantified or expressed in domain terms.

---

### CMD-15 — Produce T-09: FM-NN Resolution Audit

RESOLVE every T-02 FM-NN using T-07 as evidence. One row per FM-NN.

DO NOT assign resolution status before this command. All T-07 deferral statements
resolve here.

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### CMD-16 — Produce T-10: Recovery Audit Table

One row per NH-NN and LP-NN. Missing rows are structurally visible gaps.

Recovery Framing column — mandatory on every row. Template — all three components in
ONE cell:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

DO NOT split step, actor, and cadence into separate columns.
DO NOT use "manual review" or "human intervention" as the IB-NN step — cite a specific
T-05 step name.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

---

### CMD-17 — GATE: Post-Trace Resolution Completeness

PRODUCE a gate table:

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-09 FM-NN Resolution Audit (all T-02 FM-NN entries resolved) | | |
| T-10 Recovery Audit Table (one row per NH-NN and LP-NN) | | |
| T-10 Recovery Framing column (all three fields in each cell) | | |

DO NOT proceed to CMD-18 if any row shows EMPTY or NO-GO.

---

### CMD-18 — Produce T-11: Closure Gate

Per-identifier status for every NH-NN and LP-NN from stage traces. One row per
identifier — a summary count does not qualify.

| Identifier | Source (Stage / Boundary) | T-10 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching T-10 row. OPEN = no row — state reason.

State: "TRACE COMPLETE."
```

---

## V-04 — Combined: Role Sequence + Lifecycle (Two-Role with Role-Boundary Phase Gates)

**Axis**: Role sequence + lifecycle emphasis — Finance Controller handles extract and
validate stages; Operations Analyst handles transform, sync, and load stages. Each stage
ends with a T-07 APPEND CHECKPOINT with count. Two named phase gates separate the role
phases: Gate A (Finance Controller completion) verifies T-07 count parity across FC-stage
checkpoints before handoff; Gate B (Operations Analyst completion) verifies final
resolution tables. Scaffold uses Mandatory Columns column.
**Hypothesis**: binding phase gates to a role handoff creates motivating context for
C-34 compliance — the Finance Controller cannot transfer to the Operations Analyst
without populating Gate A; count parity in Gate A structurally catches C-32 omissions
before the role transition.

---

```
You are producing a data flow trace with two domain roles:

- FINANCE CONTROLLER: responsible for extract, validate, and schema-enforcement stages.
- OPERATIONS ANALYST: responsible for transform, sync, load, and reconciliation stages.

Pipeline:

{topic}

Work through the phases below. Finance Controller completes PHASES 1–3 in full before
Operations Analyst begins PHASE 4. Each role phase ends with a named gate table. Use
exact column names as declared in the scaffold Mandatory Columns column.

---

## PHASE 1 — OUTPUT SCAFFOLD (Finance Controller)

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| T-01 | Entity Inventory | Domain entities; Finance Controller declares all in-scope entities | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure mode predictions | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | All pipeline stages with role assignment | Stage ID, Stage Name, Assigned Role, Description | — |
| T-04 | Boundary Inventory | Boundaries with latency decomposition and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | SLA Domination Point | Standalone domination boundary artifact — separate from T-04 | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-06 | Incumbent Baseline | Pre-automation process; IB-NN Step IDs cited in T-12 | Step ID, Step Name, Responsible Role, Elapsed Time / Frequency | — |
| T-07 | FM-NN Append-Log | Append-log accumulating during stage traces with count per stage | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | FC Stage Exit Manifests | Finance Controller stage exit manifests; typed field authority | field_name, TYPE(precision), Notes | T-03 |
| T-09 | OA Stage Exit Manifests | Operations Analyst stage exit manifests; typed field authority | field_name, TYPE(precision), Notes | T-03 |
| T-10 | Pattern Trade-Off | Alternative pattern; ≥2 trade-off dimensions | Alternative Pattern, Trade-Off Dimension 1, Trade-Off Dimension 2 | — |
| T-11 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-12 | Recovery Audit Table | NH-NN / LP-NN recovery with Recovery Framing | Row, NH/LP ID, Triggering Condition, Recovery Mechanism, Boundary / Stage, Recovery Framing | T-04, T-06, T-08, T-09 |
| T-13 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source, T-12 Row, Status | T-12 |

---

## PHASE 2 — PRE-TRACE DECLARATIONS (Finance Controller)

### T-01: Entity Inventory

| Entity | Description | Key Fields |
|--------|-------------|-----------|

### T-02: FM-NN Prediction Register

Minimum 3 entries. Resolve in T-11 only. During stage traces, log FM-NN intersections
by appending rows to T-07 — not as prose bullets.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

### T-03: Stage Enumeration with Role Assignment

The Assigned Role column satisfies the C-25 stage assignment requirement.

| Stage ID | Stage Name | Assigned Role | Description |
|----------|------------|--------------|-------------|

Finance Controller stages: extract and validate.
Operations Analyst stages: transform, sync, load, and any reconciliation stages.

### T-04: Boundary Inventory

"Negligible" invalid. Transport and Processing are independent. Entity at Risk:
specific T-01 entity. entity.field: stub "→ back-fill from T-08/T-09.[Stage ID]."
Boundary labels: B[N]->[N+1].

Add footnote after T-04: "→ Domination analysis: T-05."

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

### T-05: SLA Domination Point

*Separate table produced immediately after T-04 — Finance Controller responsibility.*

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

### T-06: Incumbent Baseline

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

Minimum 4 rows. IB-NN step IDs used in T-12 Recovery Framing.

---

## PHASE 3 — FINANCE CONTROLLER STAGE TRACES

Produce one trace block for each Finance Controller stage from T-03. After each block,
declare the T-07 APPEND CHECKPOINT with count before advancing.

---

### FC Stage [Stage ID]: [Stage Name]

**Schema diff**: [Source schema (Stage 1) or diff from prior exit manifest.]

**T-08.[Stage ID] — Finance Controller Typed Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate from normal operation]
- Active entities: [T-01 names]

**T-04 back-fill**: Update entity.field stub for B[N]->[N+1] using T-08.[Stage ID].

---

**T-07 APPEND CHECKPOINT — [Stage ID] (Finance Controller)**

Append T-02 FM-NN intersections as table rows — not prose bullets.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

State: "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

---

*(Repeat FC stage block + checkpoint for every Finance Controller stage.)*

---

### GATE A — Finance Controller Phase Completion

| Required Artifact | Completion Status | Count Verified | Go/No-Go |
|-------------------|------------------|----------------|---------|
| All FC stages from T-03 traced (one block per FC stage) | | N/A | |
| All T-08.[Stage ID] typed manifests produced | | N/A | |
| T-04 entity.field stubs back-filled for all FC boundaries | | N/A | |
| T-05 SLA Domination Point produced as separate table | | N/A | |
| T-07 APPEND CHECKPOINT declared after every FC stage (count stated) | | T-07 rows from FC stages = sum of FC checkpoint counts | |

Operations Analyst may not begin PHASE 4 if any row shows INCOMPLETE or NO-GO.
Finance Controller states: "GATE A CLEAR — handing off to Operations Analyst."

---

## PHASE 4 — OPERATIONS ANALYST STAGE TRACES

Produce one trace block for each Operations Analyst stage from T-03. After each block,
declare the T-07 APPEND CHECKPOINT with count.

---

### OA Stage [Stage ID]: [Stage Name]

**Schema diff**: [Diff from prior exit manifest. If unchanged: "verified: no field added,
removed, renamed, or retyped."]

**T-09.[Stage ID] — Operations Analyst Typed Exit Manifest**:

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate from normal operation]
- Active entities: [T-01 names]

**T-04 back-fill**: Update entity.field stub for B[N]->[N+1] using T-09.[Stage ID].

---

**T-07 APPEND CHECKPOINT — [Stage ID] (Operations Analyst)**

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

State: "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended."

---

*(Repeat OA stage block + checkpoint for every Operations Analyst stage.)*

---

After final OA stage, consolidate T-07:

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

---

### T-10: Pattern Trade-Off

Name one alternative architecture pattern. State ≥2 trade-off dimensions — at least one
quantified or domain-grounded.

| Alternative Pattern | Trade-Off Dimension 1 | Trade-Off Dimension 2 |
|--------------------|-----------------------|-----------------------|

---

## PHASE 5 — POST-TRACE RESOLUTION (Operations Analyst)

### T-11: FM-NN Resolution Audit

Consumes T-07 consolidated. Resolve every T-02 FM-NN. One row per FM-NN.

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

### T-12: Recovery Audit Table

One row per NH-NN and LP-NN. Missing rows are visible gaps.

Recovery Framing column — mandatory on every row. All three fields in ONE cell:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

IB-NN Step Name: T-06 row. Responsible Role: named operational actor.
Satisfying step citation but omitting actor or cadence fails.

| Row | NH/LP ID | Triggering Condition | Recovery Mechanism | Boundary / Stage | Recovery Framing |
|-----|----------|---------------------|--------------------|-----------------|-----------------|

### GATE B — Operations Analyst Phase Completion

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-07 Append-Log consolidated | | |
| T-10 Pattern Trade-Off (≥2 dimensions, ≥1 quantified) | | |
| T-11 FM-NN Resolution Audit (all T-02 FM-NN resolved) | | |
| T-12 Recovery Audit Table (one row per NH-NN and LP-NN) | | |
| T-12 Recovery Framing column (all three fields in each row) | | |

Phase 6 may not begin if any row shows EMPTY or NO-GO.

---

## PHASE 6 — CLOSURE GATE

### T-13: Closure Gate

Per-identifier status for every NH-NN and LP-NN. One row per identifier.

| Identifier | Source (Stage / Boundary) | T-12 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching T-12 row. OPEN = no row — state reason.

State: "TRACE COMPLETE."
```

---

## V-05 — Combined: Inertia Framing + Count-Chain + Baseline-Anchored Phase Gates

**Axis**: Inertia framing + lifecycle emphasis — the incumbent baseline is produced
before the scaffold, before the pipeline stages are enumerated. Phase gates are anchored
to baseline availability: the Phase 2 gate verifies that IB-NN step identifiers are
established before any stage trace begins. The Phase 3 gate carries a count-chain
verification row confirming that per-stage checkpoint totals sum to the consolidated T-07
row count. Recovery Framing is the leftmost non-identifier column in T-10.
**Hypothesis**: leading with the incumbent baseline before the scaffold establishes
IB-NN identifiers as the semantic ground before the pipeline contract is written;
phase gates that verify IB-NN availability before the trace phase prevent the most
common C-14/C-15/C-16 partial failure — starting recovery prescriptions before step
identifiers exist.

---

```
You are a Finance / Operations / Commerce data domain expert. Produce a complete data flow
trace for the following pipeline:

{topic}

Produce sections in the order below. The incumbent baseline is produced first — before
the scaffold and before stage enumeration — because recovery prescriptions cite specific
IB-NN step identifiers. If the baseline does not exist before recovery prescriptions
are written, citation is impossible.

---

## SECTION 0: Incumbent Baseline (Produced Before Scaffold)

Document the pre-automation operational process this pipeline replaces. Minimum 4 rows.
Step IDs: IB-01, IB-02, etc. These identifiers anchor Recovery Framing in T-10.
A recovery row that cites a process category without a specific IB-NN step ID fails.

| Step ID | Step Name | Responsible Role | Elapsed Time / Frequency |
|---------|-----------|-----------------|--------------------------|

---

## SECTION 1: Output Scaffold

Every table appearing in this response must be declared here. A table first appearing
after this section is an undeclared artifact. Use exact column names declared in the
Mandatory Columns column — column names in produced tables must match.

| T# | Table Name | Purpose | Mandatory Columns (exact names) | Depends On |
|----|-----------|---------|----------------------------------|------------|
| T-01 | Entity Inventory | Domain entities declared before any trace | Entity, Description, Key Fields | — |
| T-02 | FM-NN Prediction Register | Pre-trace failure mode predictions | FM-NN, Anticipated Event, Domain Consequence, Expected Designation | — |
| T-03 | Stage Enumeration | Named and sequenced pipeline stages | Stage ID, Stage Name, Description | — |
| T-04 | Boundary Inventory | Inter-stage boundaries with latency decomposition and SLA% | Boundary, From Stage, To Stage, Entity at Risk, entity.field, Transport (ms), Processing (ms), Total (ms), SLA% This, Cumulative SLA% | T-03 |
| T-05 | SLA Domination Point | Standalone domination boundary artifact — separate from T-04 | Domination Boundary, Exact Cumulative SLA%, Justification | T-04 |
| T-06 | Stage Exit Manifests | One sub-manifest per stage; typed field authority | field_name, TYPE(precision), Notes | T-03 |
| T-07 | FM-NN Append-Log | Append-log; count stated per stage; running total accumulated | FM-NN, Stage ID, Boundary / Condition, Deferral Statement | T-02, T-03 |
| T-08 | FM-NN Resolution Audit | Post-trace FM-NN lifecycle resolution | FM-NN, Status, T-07 Rows Consulted, Evidence / Reason | T-02, T-07 |
| T-09 | Recovery Audit Table | NH-NN / LP-NN recovery; Recovery Framing column leads | Row, NH/LP ID, Recovery Framing, Triggering Condition, Recovery Mechanism, Boundary / Stage | IB-table, T-04, T-06 |
| T-10 | Closure Gate | Per-identifier CLOSED / OPEN status | Identifier, Source (Stage / Boundary), T-09 Row, Status | T-09 |

Note: Recovery Framing is the first substantive column in T-09 (before Triggering Condition
and Recovery Mechanism) — structural ordering that enforces IB-NN citation before
technical recovery detail.

---

## PHASE 1 — ENTITY AND FAILURE MODE DECLARATIONS

### T-01: Entity Inventory

List every in-scope domain entity by domain name. Stage traces reference only entities
declared here.

| Entity | Description | Key Fields |
|--------|-------------|-----------|

### T-02: FM-NN Prediction Register

Predict every anticipated failure mode. Minimum 3 entries. Resolution in T-08 only.
During stage traces, FM-NN intersections are logged by appending rows to T-07.

| FM-NN | Anticipated Event | Domain Consequence | Expected Designation |
|-------|------------------|--------------------|---------------------|

### T-03: Stage Enumeration

| Stage ID | Stage Name | Description |
|----------|------------|-------------|

### PHASE 1 GATE

| Required Table | Population Status | IB-NN Step IDs Available | Go/No-Go |
|---------------|-------------------|--------------------------|---------|
| Section 0 Incumbent Baseline (≥4 rows, IB-NN IDs) | | IB-NN identifiers declared | |
| T-01 Entity Inventory | | N/A | |
| T-02 FM-NN Prediction Register (≥3 rows) | | N/A | |
| T-03 Stage Enumeration | | N/A | |

Phase 2 may not begin if any row shows EMPTY or NO-GO or if IB-NN IDs are absent.

---

## PHASE 2 — BOUNDARY INVENTORY AND SLA ANALYSIS

### T-04: Boundary Inventory

"Negligible" invalid — use numeric ms. Transport and Processing are independent columns.
Entity at Risk: specific T-01 entity. entity.field: stub "→ back-fill from T-06.[Stage ID]."
Boundary labels: B[N]->[N+1].

Add footnote after T-04: "→ Domination analysis: T-05."

| Boundary | From Stage | To Stage | Entity at Risk | entity.field | Transport (ms) | Processing (ms) | Total (ms) | SLA% This | Cumulative SLA% |
|----------|------------|---------|----------------|-------------|----------------|-----------------|-----------|-----------|-----------------|

### T-05: SLA Domination Point

*Standalone table produced immediately after T-04 — not embedded in T-04.*

| Domination Boundary | Exact Cumulative SLA% | Justification |
|--------------------|-----------------------|--------------|

One row. Domination Boundary: B[N]->[N+1] from T-04. Justification: one sentence naming
the specific domain operation dominating the SLA budget.

### PHASE 2 GATE

| Required Table | Population Status | Go/No-Go |
|---------------|-------------------|---------|
| T-04 Boundary Inventory (all columns, numeric latency values) | | |
| T-05 SLA Domination Point (produced as separate table, not in T-04) | | |

Phase 3 may not begin if any row shows EMPTY or NO-GO.

---

## PHASE 3 — STAGE TRACES

For each stage in T-03, produce one trace block. After each block, declare the T-07
APPEND CHECKPOINT with per-stage count and running total.

---

### Stage [Stage ID]: [Stage Name]

**Schema diff**: [Source schema (Stage 1) or diff from prior exit manifest. If unchanged:
"verified: no field added, removed, renamed, or retyped."]

**T-06.[Stage ID] — Typed Exit Manifest** (authority for entity.field back-fill in T-04
and field citations in T-09):

| field_name | TYPE(precision) | Notes |
|------------|-----------------|-------|

**Boundary B[N]->[N+1] annotation**:
- Error handling: [mechanism] OR [NH-NN — no handling — risk accepted: {specific risk}]
- Data loss point: LP-NN — [specific named scenario]
- Latency: [value, range, or characterization]
- Normal stale window: [quantified]
- Failure-mode stale window: [quantified, separate from normal operation]
- Active entities (from T-01): [names]

**T-04 back-fill**: Update entity.field stub for B[N]->[N+1] with T-06.[Stage ID] fields.

---

**T-07 APPEND CHECKPOINT — [Stage ID]**

Append T-02 FM-NN intersections as table rows — not prose bullets.

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

If no T-02 prediction intersects this stage:
| (none) | [Stage ID] | No T-02 intersections at this stage | N/A |

State: "T-07 APPEND CHECKPOINT [Stage ID] COMPLETE — [N] rows appended this stage,
[M] total rows in T-07 as of [Stage ID]."

---

*(Repeat stage block + T-07 APPEND CHECKPOINT for every stage in T-03.)*

---

After the final stage, consolidate T-07:

### T-07: FM-NN Append-Log (Consolidated)

| FM-NN | Stage ID | Boundary / Condition | Deferral Statement |
|-------|----------|---------------------|---------------------|

### PHASE 3 GATE

| Required Artifact | Completion Status | Verification | Go/No-Go |
|-------------------|------------------|--------------|---------|
| All T-03 stages traced (one block per stage) | | N/A | |
| All T-06.[Stage ID] typed manifests produced | | N/A | |
| All T-04 entity.field stubs back-filled | | N/A | |
| T-07 APPEND CHECKPOINT declared after every stage | | N/A | |
| T-07 consolidated row count matches sum of per-stage counts | | [M total rows = sum of all per-stage [N] values — state the arithmetic] | |

Phase 4 may not begin if any row shows INCOMPLETE, MISMATCH, or NO-GO.

---

## PHASE 4 — POST-TRACE RESOLUTION AND RECOVERY

Pattern trade-off: name one alternative architecture pattern. State ≥2 trade-off
dimensions — at least one quantified or expressed in domain terms.

---

### T-08: FM-NN Resolution Audit

Consumes T-07 consolidated. Resolve every T-02 FM-NN. One row per FM-NN.

- CONFIRMED: prediction materialized — cite the NH-NN or LP-NN produced
- EXONERATED: prediction did not materialize — state the specific reason
- NEW: emerged during trace — assign NH-NN or LP-NN retroactively

| FM-NN | Status | T-07 Rows Consulted | Evidence / Reason |
|-------|--------|--------------------|--------------------|

---

### T-09: Recovery Audit Table

One row per NH-NN and LP-NN. Recovery Framing is the first substantive column —
write the IB-NN citation before writing the technical recovery mechanism.

Recovery Framing template — all three fields in ONE cell:

    Revert to [IB-NN Step Name] performed by [Responsible Role] at [frequency/trigger]

- IB-NN Step Name: specific row from Section 0 Incumbent Baseline.
- Responsible Role: named operational actor (AP Clerk, Inventory Controller, etc.).
- frequency/trigger: when the fallback applies.
- Satisfying step citation but omitting actor or cadence fails.
- Using "manual review" or "human intervention" without a named IB-NN step fails.

| Row | NH/LP ID | Recovery Framing | Triggering Condition | Recovery Mechanism | Boundary / Stage |
|-----|----------|-----------------|---------------------|--------------------|-----------------|

### PHASE 4 GATE

| Required Table | Population Status | IB-NN Citations Valid | Go/No-Go |
|---------------|-------------------|----------------------|---------|
| T-08 FM-NN Resolution Audit (all T-02 FM-NN resolved) | | N/A | |
| T-09 Recovery Audit Table (one row per NH-NN and LP-NN) | | Every T-09 row cites a specific Section 0 IB-NN step | |
| T-09 Recovery Framing column (all three fields in each row) | | | |

Phase 5 may not begin if any row shows EMPTY, MISSING, or NO-GO.

---

## PHASE 5 — CLOSURE GATE

### T-10: Closure Gate

Per-identifier status for every NH-NN and LP-NN. One row per identifier — a summary
count does not satisfy this gate.

| Identifier | Source (Stage / Boundary) | T-09 Row | Status |
|-----------|--------------------------|----------|--------|

CLOSED = matching T-09 row. OPEN = no row — state reason.

State: "TRACE COMPLETE."
```
